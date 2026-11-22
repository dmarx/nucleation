"""LEAD-035 driver. Each item (one model, one setting, one seed) is trained
and its trajectory appended to results.jsonl as one line when it ends.
Items already in the file are skipped, so a rerun resumes.

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run.py [--quick]
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import snr  # noqa: E402

OUT = os.path.join(HERE, "results.jsonl")  # --out=PATH overrides
C, N, D_IN, SEP = 4, 50, 20, 3.0


def record(H, Y, labels, k, eta, extra=None):
    om, cond = snr.snr_singular_values(H, labels, C)
    row = {"step": int(k), "t": float(k * eta),
           "omega": [float(x) for x in om], "sw_cond": cond,
           "L_LS": float(snr.ls_loss(H, Y)), "nc1": snr.nc1(H, labels, C)}
    if extra:
        row.update(extra)
    return row


def stop(row):
    """End a run at divergence, or where omega is past what double
    precision can measure (L_LS near rounding, Sigma_W singular)."""
    return (not np.isfinite(row["L_LS"]) or not np.isfinite(row.get("L", 0.0))
            or row["L_LS"] < 1e-11 or row["sw_cond"] < 1e-13)


def ufm(kind, seed, steps, eta, p=16):
    """Unconstrained features. kind:
    renorm - Han et al.'s flow: projected gradient of L_LS, then re-whiten;
    lsplain - plain gradient of L_LS (classifier at its LS optimum), no
              re-whitening, i.e. without assumption A3;
    joint  - ordinary gradient descent on (W, b, H) under MSE, lambda 0."""
    rng = np.random.default_rng(seed)
    labels = np.repeat(np.arange(C), N)
    Y = np.eye(C)[:, labels]
    H = 0.3 * rng.standard_normal((p, C)) [:, labels] + rng.standard_normal((p, C * N))
    if kind == "renorm":
        H = snr.whiten(H, labels, C)
    W = rng.standard_normal((C, p)) / np.sqrt(p)
    b = np.zeros((C, 1))
    marks = set(snr.log_steps(steps))
    traj, n = [], C * N
    for k in range(steps + 1):
        if k in marks:
            extra = None
            if kind == "joint":
                extra = {"L": float(snr.mse(W, b, H, Y))}
            traj.append(record(H, Y, labels, k, eta, extra))
            if stop(traj[-1]):
                break
        if k == steps:
            break
        if kind == "renorm":
            H = snr.whiten(H - eta * snr.projected_ls_grad(H, Y, labels, C),
                           labels, C)
        elif kind == "lsplain":
            H = H - eta * snr.ls_grad(H, Y)
        else:
            R = (W @ H + b - Y) / n
            # matrix gradients of L itself, the time unit of Han et al.'s
            # flow (checked in test_renormalized_flow_step_matches_lemma5)
            gW, gb, gH = R @ H.T, R.sum(axis=1, keepdims=True), W.T @ R
            W -= eta * gW
            b -= eta * gb
            H -= eta * gH
    return traj


def mlp(arch, wd, seed, steps, lr):
    rng = np.random.default_rng(1000 + seed)
    X, Y, labels = snr.gaussian_mixture(C, N, D_IN, SEP, rng)
    sizes = {"mlp2": [D_IN, 64, 32], "mlp3bn": [D_IN, 64, 64, 32]}[arch]
    bn = arch.endswith("bn")
    params = snr.init_mlp(sizes, C, rng)
    marks = set(snr.log_steps(steps))
    traj = []
    for k in range(steps + 1):
        tot, L, H, g = snr.loss_and_grads(params, X, Y, bn, wd)
        if k in marks:
            pred = params["Wo"] @ H + params["bo"]
            acc = float(np.mean(pred.argmax(axis=0) == labels))
            traj.append(record(H, Y, labels, k, lr,
                               {"L": float(L), "obj": float(tot), "acc": acc}))
            if stop(traj[-1]):
                break
        if k == steps:
            break
        snr.sgd_step(params, g, lr)
    return traj


def items(quick):
    s = 0.1 if quick else 1.0
    out = []
    for seed in range(3):
        out.append(("ufm-renorm", seed, dict(kind="renorm", steps=int(20000 * s), eta=200.0)))
        out.append(("ufm-lsplain", seed, dict(kind="lsplain", steps=int(20000 * s), eta=20.0)))
        out.append(("ufm-joint", seed, dict(kind="joint", steps=int(200000 * s), eta=0.5)))
    for arch in ["mlp2", "mlp3bn"]:
        for wd in [0.0, 5e-4]:
            for seed in range(3):
                out.append((f"{arch}-wd{wd:g}", seed,
                            dict(arch=arch, wd=wd, steps=int(200000 * s), lr=0.05)))
    # one long run: does omega settle under weight decay (a finite minimum)
    # or keep growing? 200000 steps (t = 1e4) left it undecided.
    out.append(("long-mlp2-wd0.0005", 0,
                dict(arch="mlp2", wd=5e-4, steps=int(1000000 * s), lr=0.05)))
    return out


def done_ids():
    if not os.path.exists(OUT):
        return set()
    with open(OUT) as f:
        return {json.loads(line)["id"] for line in f if line.strip()}


def main():
    global OUT
    quick = "--quick" in sys.argv
    for a in sys.argv[1:]:
        if a.startswith("--out="):
            OUT = os.path.abspath(a[len("--out="):])
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    have = done_ids()
    for name, seed, cfg in items(quick):
        iid = f"{name}/s{seed}" + ("/quick" if quick else "")
        if iid in have or (only and not any(o in iid for o in only)):
            continue
        t0 = time.time()
        if name.startswith("ufm"):
            traj = ufm(seed=seed, **cfg)
        else:
            traj = mlp(seed=seed, **cfg)
        row = {"id": iid, "model": name, "seed": seed, "C": C, "N": N,
               "cfg": cfg, "secs": round(time.time() - t0, 1), "traj": traj}
        with open(OUT, "a") as f:
            f.write(json.dumps(row) + "\n")
        print(iid, row["secs"], "s; final omega", traj[-1]["omega"], flush=True)


if __name__ == "__main__":
    main()
