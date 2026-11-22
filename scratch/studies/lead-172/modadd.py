"""LEAD-172: modular-addition checkpoint study (numpy, CPU only).

Model: the attention-free reduction of a one-layer transformer on (a, b):
separate embeddings for a and b summed into a ReLU hidden layer, then an
unembedding to p logits.  z = Ea[a] + Eb[b] + b1; h = relu(z); f = h W2 + b2.
Trained full batch with AdamW on a fraction of all p^2 pairs.

Measures at checkpoints (all in the Fourier basis of Z/p, which the task
supplies):
  - loss/acc on train and test;
  - C1sel: of the hidden layer's mixed-mode energy (k != 0, l != 0 in the
    2D DFT over (a, b)), the fraction on the selection-rule cells l = k;
  - C2: of the class-centred logits' 3D DFT energy, the fraction on the
    selection-rule triads (k, k, -k), k != 0 (p - 1 edges);
  - null couplings at equal edge budget: the same fractions on random sets
    of p - 1 off-rule cells / triads (fixed draws, NNULL of them);
  - fourier_energy: mean over hidden units of the top frequency's share of
    the embedding spectrum (Ea and Eb), the Fourier-sparsity progress
    measure;
  - kernel: empirical NTK over all p^2 inputs (trace over classes, closed
    form); KA = share of the top-p eigenspace inside the span of the
    diagonal characters chi_k(a) chi_k(b) (functions of a + b); and the
    rotation of that eigenspace since the previous kernel checkpoint
    (1 - ||U_t^T U_prev||_F^2 / m), a proxy for the moving-basis term.

Metrics are appended as JSON lines to results/<run>.jsonl; weights and
optimizer state are saved to STATE_DIR so an interrupted run resumes.
"""
import gzip
import json
import os
import sys
import time

import numpy as np

P = 37
HIDDEN = 128
NNULL = 20
STUDY = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(STUDY, "results")
STATE_DIR = os.environ.get("LEAD172_STATE", os.path.join(STUDY, "state"))


def all_pairs(p):
    a, b = np.meshgrid(np.arange(p), np.arange(p), indexing="ij")
    a, b = a.ravel(), b.ravel()
    return a, b, (a + b) % p


def init_params(p, n, rng):
    return {
        "Ea": rng.normal(0, 1.0, (p, n)) / np.sqrt(2),
        "Eb": rng.normal(0, 1.0, (p, n)) / np.sqrt(2),
        "b1": np.zeros(n),
        "W2": rng.normal(0, 1.0, (n, p)) / np.sqrt(n),
        "b2": np.zeros(p),
    }


def forward(params, a, b):
    z = params["Ea"][a] + params["Eb"][b] + params["b1"]
    h = np.maximum(z, 0.0)
    f = h @ params["W2"] + params["b2"]
    return z, h, f


def loss_and_grads(params, a, b, y):
    z, h, f = forward(params, a, b)
    n = len(y)
    f = f - f.max(1, keepdims=True)
    e = np.exp(f)
    s = e / e.sum(1, keepdims=True)
    loss = -np.log(s[np.arange(n), y] + 1e-30).mean()
    df = s
    df[np.arange(n), y] -= 1.0
    df /= n
    g = {"W2": h.T @ df, "b2": df.sum(0)}
    dz = (df @ params["W2"].T) * (z > 0)
    g["b1"] = dz.sum(0)
    p = params["Ea"].shape[0]
    eye = np.eye(p)
    g["Ea"] = eye[a].T @ dz
    g["Eb"] = eye[b].T @ dz
    return loss, g


def accuracy(params, a, b, y):
    return float((forward(params, a, b)[2].argmax(1) == y).mean())


def ce(params, a, b, y):
    f = forward(params, a, b)[2]
    f = f - f.max(1, keepdims=True)
    return float(-(f[np.arange(len(y)), y] - np.log(np.exp(f).sum(1))).mean())


# ---------- Fourier measures ----------

def rule_masks(p):
    k = np.arange(p)
    m2 = np.zeros((p, p), bool)
    m2[k[1:], k[1:]] = True                      # l = k, k != 0
    m3 = np.zeros((p, p, p), bool)
    m3[k[1:], k[1:], (-k[1:]) % p] = True        # (k, k, -k)
    return m2, m3


def null_masks(p, n_null, seed=12345):
    """Random off-rule sets with the rule's edge count (p - 1)."""
    rng = np.random.default_rng(seed)
    m2, m3 = rule_masks(p)
    mixed = np.zeros((p, p), bool)
    mixed[1:, 1:] = True
    cand2 = np.flatnonzero((mixed & ~m2).ravel())
    nonconst = np.ones((p, p, p), bool)
    nonconst[:, :, 0] = False
    cand3 = np.flatnonzero((nonconst & ~m3).ravel())
    out2, out3 = [], []
    for _ in range(n_null):
        a = np.zeros(p * p, bool)
        a[rng.choice(cand2, p - 1, replace=False)] = True
        out2.append(a.reshape(p, p))
        c = np.zeros(p ** 3, bool)
        c[rng.choice(cand3, p - 1, replace=False)] = True
        out3.append(c.reshape(p, p, p))
    return out2, out3


def hidden_spectrum(params, p):
    a, b, _ = all_pairs(p)
    h = forward(params, a, b)[1].reshape(p, p, -1)
    h = h - h.mean((0, 1), keepdims=True)
    return (np.abs(np.fft.fft2(h, axes=(0, 1))) ** 2).sum(2)   # (p, p)


def logit_spectrum(params, p):
    a, b, _ = all_pairs(p)
    f = forward(params, a, b)[2].reshape(p, p, p)
    f = f - f.mean(2, keepdims=True)                          # softmax-invariant
    return np.abs(np.fft.fftn(f)) ** 2


def coupling_fractions(params, p, m2, m3, nulls2, nulls3):
    E2 = hidden_spectrum(params, p)
    mixed = E2[1:, 1:].sum()
    E3 = logit_spectrum(params, p)
    tot3 = E3.sum()
    return {
        "mixed_frac": float(mixed / (E2.sum() + 1e-30)),
        "C1sel": float(E2[m2].sum() / (mixed + 1e-30)),
        "C2": float(E3[m3].sum() / (tot3 + 1e-30)),
        "C1null": [float(E2[m].sum() / (mixed + 1e-30)) for m in nulls2],
        "C2null": [float(E3[m].sum() / (tot3 + 1e-30)) for m in nulls3],
    }


def fourier_energy(params, p):
    out = []
    for key in ("Ea", "Eb"):
        F = np.abs(np.fft.fft(params[key], axis=0)) ** 2     # (p, n)
        F = F[1:]
        half = F[: (p - 1) // 2] + F[::-1][: (p - 1) // 2]   # pair k, -k
        out.append((half.max(0) / (half.sum(0) + 1e-30)).mean())
    return float(np.mean(out))


# ---------- kernel ----------

def ntk(params, p):
    """Trace-over-classes empirical NTK on all p^2 inputs (closed form)."""
    a, b, _ = all_pairs(p)
    z, h, _ = forward(params, a, b)
    S = (z > 0).astype(float)
    w = (params["W2"] ** 2).sum(1)
    same = (a[:, None] == a[None, :]).astype(float) + (b[:, None] == b[None, :]) + 1.0
    return p * (h @ h.T) + p + ((S * w) @ S.T) * same


def diag_char_basis(p):
    """Orthonormal real basis of functions of (a + b) mod p on p^2 inputs."""
    a, b, c = all_pairs(p)
    Y = np.zeros((p * p, p))
    Y[np.arange(p * p), c] = 1.0
    Q, _ = np.linalg.qr(Y)
    return Q


def kernel_measures(params, p, Q, U_prev, m):
    K = ntk(params, p)
    from scipy.sparse.linalg import eigsh
    top, U = eigsh(K, k=m, which="LA", v0=np.ones(len(K)))
    KA = float((np.linalg.norm(Q.T @ U) ** 2) / m)
    rot = None if U_prev is None else float(1 - np.linalg.norm(U.T @ U_prev) ** 2 / m)
    return {"KA": KA, "K_rot": rot, "K_topfrac": float(top.sum() / np.trace(K))}, U


# ---------- training ----------

def run(name, frac, wd, seed, lr=1e-2, max_steps=15000, every=50, kevery=250,
        stop_after=500, p=P, n=HIDDEN):
    os.makedirs(RESULTS, exist_ok=True)
    os.makedirs(STATE_DIR, exist_ok=True)
    out = os.path.join(RESULTS, name + ".jsonl.gz")
    st_path = os.path.join(STATE_DIR, name + ".npz")
    done = False
    if os.path.exists(out):
        with gzip.open(out, "rt") as fh:
            done = any(json.loads(l).get("done") for l in fh if l.strip())
    if done:
        print(name, "already done", flush=True)
        return
    rng = np.random.default_rng(seed)
    a, b, y = all_pairs(p)
    perm = rng.permutation(p * p)
    ntr = int(round(frac * p * p))
    tr, te = perm[:ntr], perm[ntr:]
    params = init_params(p, n, rng)
    mom = {k: np.zeros_like(v) for k, v in params.items()}
    vel = {k: np.zeros_like(v) for k, v in params.items()}
    step0, t_gen = 0, None
    if os.path.exists(st_path):
        z = np.load(st_path)
        for k in params:
            params[k], mom[k], vel[k] = z["p_" + k], z["m_" + k], z["v_" + k]
        step0 = int(z["step"])
        t_gen = int(z["t_gen"]) if int(z["t_gen"]) >= 0 else None
        print(name, "resuming at", step0, flush=True)
    m2, m3 = rule_masks(p)
    n2, n3 = null_masks(p, NNULL)
    Q = diag_char_basis(p)
    U_prev = None
    b1_, b2_, eps = 0.9, 0.98, 1e-8
    def write(obj):
        # one gzip member per row: append-only, and readable after a kill
        with gzip.open(out, "at") as g:
            g.write(json.dumps(obj) + "\n")

    if step0 == 0:
        write({"meta": True, "name": name, "frac": frac, "wd": wd,
                             "seed": seed, "lr": lr, "p": p, "hidden": n})
    t0 = time.time()
    for step in range(step0, max_steps + 1):
        if step % every == 0:
            row = {"step": step,
                   "train_loss": ce(params, a[tr], b[tr], y[tr]),
                   "test_loss": ce(params, a[te], b[te], y[te]),
                   "train_acc": accuracy(params, a[tr], b[tr], y[tr]),
                   "test_acc": accuracy(params, a[te], b[te], y[te]),
                   "fourier_energy": fourier_energy(params, p)}
            row.update(coupling_fractions(params, p, m2, m3, n2, n3))
            if step % kevery == 0:
                km, U_prev = kernel_measures(params, p, Q, U_prev, p)
                row.update(km)
            write(row)
            if t_gen is None and row["test_acc"] >= 0.95:
                t_gen = step
            if step % kevery == 0:
                tmp = st_path + ".tmp.npz"
                np.savez(tmp, step=step + 1, t_gen=-1 if t_gen is None else t_gen,
                         **{"p_" + k: v for k, v in params.items()},
                         **{"m_" + k: v for k, v in mom.items()},
                         **{"v_" + k: v for k, v in vel.items()})
                os.replace(tmp, st_path)
            if t_gen is not None and step >= t_gen + stop_after:
                break
        _, g = loss_and_grads(params, a[tr], b[tr], y[tr])
        t = step + 1
        for k in params:
            mom[k] = b1_ * mom[k] + (1 - b1_) * g[k]
            vel[k] = b2_ * vel[k] + (1 - b2_) * g[k] ** 2
            mh = mom[k] / (1 - b1_ ** t)
            vh = vel[k] / (1 - b2_ ** t)
            params[k] -= lr * (mh / (np.sqrt(vh) + eps) + wd * params[k])
    write({"done": True, "t_gen": t_gen, "last_step": step,
           "secs": time.time() - t0})
    print(name, "done t_gen", t_gen, "secs %.0f" % (time.time() - t0), flush=True)


# Training arms (fit set) and the held-out intervention arms.
FIT = [(f, 1.0, s) for f in (0.4, 0.5, 0.6) for s in (0, 1, 2)]
HELDOUT = ([(f, 0.5, s) for f in (0.5, 0.6) for s in (0, 1)]
           + [(0.5, 2.0, s) for s in (0, 1)])


def arm_name(f, wd, s):
    return "f%02d_wd%03d_s%d" % (round(f * 100), round(wd * 100), s)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    arms = {"fit": FIT, "heldout": HELDOUT, "all": FIT + HELDOUT}[which]
    shard, nshard = (int(x) for x in (sys.argv[2:4] if len(sys.argv) > 3 else (0, 1)))
    for f, wd, s in arms[shard::nshard]:
        run(arm_name(f, wd, s), f, wd, s)
