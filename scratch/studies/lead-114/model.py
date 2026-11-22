"""A small numpy network for group composition and full-batch training.

Architecture (no matrix representation imposed; inputs are one-hot indices):

    e_g = E[g], e_h = E[h]                      shared embedding E (m x d)
    pre = Wl @ e_g + Wr @ e_h + b1              hidden (H,)
    hid = relu(pre)
    logits = Wu @ hid + b2                       (m,)
    loss = cross_entropy(logits, g*h) + wd * ||params||^2

Trained by full-batch gradient descent with momentum on a train split of the
m*m pairs; the rest is held out to test generalisation.
"""
import numpy as np


def init_params(m, d, H, seed):
    rng = np.random.default_rng(seed)
    s = 1.0
    return {
        "E": rng.standard_normal((m, d)) * (s / np.sqrt(d)),
        "Wl": rng.standard_normal((H, d)) * (s / np.sqrt(d)),
        "Wr": rng.standard_normal((H, d)) * (s / np.sqrt(d)),
        "b1": np.zeros(H),
        "Wu": rng.standard_normal((m, H)) * (s / np.sqrt(H)),
        "b2": np.zeros(m),
    }


def _softmax(z):
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


def forward(p, gidx, hidx):
    """Vectorised forward over arrays of element indices. Returns logits and a
    cache for backprop."""
    eg = p["E"][gidx]                     # (N, d)
    eh = p["E"][hidx]
    pre = eg @ p["Wl"].T + eh @ p["Wr"].T + p["b1"]   # (N, H)
    hid = np.maximum(pre, 0.0)
    logits = hid @ p["Wu"].T + p["b2"]    # (N, m)
    cache = (gidx, hidx, eg, eh, pre, hid)
    return logits, cache


def loss_and_grads(p, gidx, hidx, y, wd):
    N = len(y)
    logits, (gi, hi, eg, eh, pre, hid) = forward(p, gidx, hidx)
    probs = _softmax(logits)
    ll = -np.log(probs[np.arange(N), y] + 1e-12).mean()
    reg = wd * sum(np.sum(v * v) for k, v in p.items() if k.startswith("W"))
    loss = ll + reg

    dlogits = probs.copy()
    dlogits[np.arange(N), y] -= 1.0
    dlogits /= N                          # (N, m)
    g = {}
    g["Wu"] = dlogits.T @ hid + 2 * wd * p["Wu"]
    g["b2"] = dlogits.sum(axis=0)
    dhid = dlogits @ p["Wu"]              # (N, H)
    dpre = dhid * (pre > 0)
    g["Wl"] = dpre.T @ eg + 2 * wd * p["Wl"]
    g["Wr"] = dpre.T @ eh + 2 * wd * p["Wr"]
    g["b1"] = dpre.sum(axis=0)
    # embedding grads: each row of E receives from its appearances as g and h.
    dE = np.zeros_like(p["E"])
    deg = dpre @ p["Wl"]                  # (N, d)
    deh = dpre @ p["Wr"]
    np.add.at(dE, gi, deg)
    np.add.at(dE, hi, deh)
    g["E"] = dE
    return loss, g, ll


def accuracy(p, gidx, hidx, y):
    logits, _ = forward(p, gidx, hidx)
    return float(np.mean(logits.argmax(axis=1) == y))


def train(cayley, d=16, H=64, wd=1e-3, lr=0.5, mom=0.9, steps=4000,
          holdout=0.25, seed=0, log_every=0):
    """Train on a split of the composition task. Returns (params, info)."""
    m = cayley.shape[0]
    rng = np.random.default_rng(seed)
    pairs = [(g, h) for g in range(m) for h in range(m)]
    gid = np.array([a for a, _ in pairs])
    hid = np.array([b for _, b in pairs])
    yall = cayley[gid, hid]
    N = len(pairs)
    perm = rng.permutation(N)
    n_test = int(round(holdout * N))
    test_i = perm[:n_test]
    train_i = perm[n_test:]

    p = init_params(m, d, H, seed)
    vel = {k: np.zeros_like(v) for k, v in p.items()}
    gtr, htr, ytr = gid[train_i], hid[train_i], yall[train_i]
    hist = []
    for t in range(steps):
        loss, grads, ll = loss_and_grads(p, gtr, htr, ytr, wd)
        for k in p:
            vel[k] = mom * vel[k] - lr * grads[k]
            p[k] += vel[k]
        if log_every and (t % log_every == 0 or t == steps - 1):
            tr = accuracy(p, gtr, htr, ytr)
            te = (accuracy(p, gid[test_i], hid[test_i], yall[test_i])
                  if n_test else 1.0)
            hist.append((t, float(loss), tr, te))
    train_acc = accuracy(p, gtr, htr, ytr)
    test_acc = (accuracy(p, gid[test_i], hid[test_i], yall[test_i])
                if n_test else 1.0)
    info = {"m": m, "d": d, "H": H, "wd": wd, "lr": lr, "steps": steps,
            "holdout": holdout, "n_train": len(train_i), "n_test": n_test,
            "train_acc": train_acc, "test_acc": test_acc, "hist": hist}
    return p, info


def reconstruct_table(p):
    """Blind: the binary operation the NETWORK learned, read off by argmax over
    all (g, h). The true group is never consulted."""
    m = p["E"].shape[0]
    gid = np.array([g for g in range(m) for _ in range(m)])
    hid = np.array([h for _ in range(m) for h in range(m)])
    logits, _ = forward(p, gid, hid)
    return logits.argmax(axis=1).reshape(m, m).astype(np.int64)
