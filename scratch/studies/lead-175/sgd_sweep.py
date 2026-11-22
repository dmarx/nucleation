"""SGD sweep for LEAD-175: TMS (c = 6, r = 2, high sparsity) trained by plain
minibatch SGD on a fixed training set of n samples, across n, batch size,
learning rate and initialisation. Does SGD reach the 6-gon?

One item = one (n, batch, epochs) job, vectorised over learning rates x
initialisations x seeds; each job appends one JSON line per run to the output
file when it finishes, and a rerun skips jobs already written (resumable).

Usage: python3 -I sgd_sweep.py OUT.jsonl [--epochs E] [--ns 300,500,...]
       [--batches 5,20,100] [--lrs ...] [--inits ...] [--seeds S]
"""
import argparse, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import tms

INITS = ("4gon", "5gon", "6gon", "prior", "5pgon")


def init_params(kind, seed):
    """Paper's init: the 4-gon (l = 1, b = 0; two zero columns with bias 0) plus
    N(0, 0.01^2) noise on every parameter (Chen et al. §5). '5gon' and '6gon':
    those critical points (sixth column of the 5-gon zero, bias -0.1) plus the same
    noise; '6gon' is a stability control; '5pgon' is the 5+-gon plus the noise. 'prior': a draw from N(0, 1) on all 18
    parameters, the prior Chen et al. sample under."""
    rng = np.random.default_rng([7, INITS.index(kind), seed])
    if kind == "prior":
        return rng.normal(size=(2, 6)), rng.normal(size=6)
    if kind == "4gon":
        W, b = tms.kgon(4, 1.0, 0.0, [0.0, 0.0])
    elif kind == "5gon":
        W, b = tms.kgon(5, 1.17046, -0.28230, [-0.1])
    elif kind == "5pgon":                               # the 5+-gon: sixth column zero, bias 1/12
        W, b = tms.CRIT["5+"]
    else:
        W, b = tms.CRIT["6"]
    return W + rng.normal(scale=0.01, size=W.shape), b + rng.normal(scale=0.01, size=b.shape)


def dataset(n, seed):
    rng = np.random.default_rng([11, n, seed])
    return rng.integers(0, 6, size=n), rng.random(n)


def run_job(n, B, epochs, lrs, inits, seeds, checkpoints):
    combos = [(lr, ini, s) for lr in lrs for ini in inits for s in range(seeds)]
    Rn = len(combos)
    W = np.empty((Rn, 2, 6)); b = np.empty((Rn, 6))
    D_idx = np.empty((Rn, n), int); D_mu = np.empty((Rn, n))
    for r, (lr, ini, s) in enumerate(combos):
        W[r], b[r] = init_params(ini, s)
        D_idx[r], D_mu[r] = dataset(n, s)
    lr_v = np.array([c[0] for c in combos])[:, None, None]
    alive = np.ones(Rn, bool)
    rng = np.random.default_rng([13, n, B])
    steps = n // B
    hist = {r: {} for r in range(Rn)}
    rows = np.arange(Rn)[:, None]

    def snap(ep):
        k, s, m = tms.classify(W, b)
        for r in range(Rn):
            hist[r][ep] = tms.label(k[r], s[r], m[r]) if alive[r] else "diverged"

    snap(0)
    for ep in range(1, epochs + 1):
        perm = np.argsort(rng.random((Rn, n)), axis=1)
        I = D_idx[rows, perm]; M = D_mu[rows, perm]
        for t in range(steps):
            sl = slice(t * B, (t + 1) * B)
            _, gW, gb = tms.batch_loss_grad(W, b, I[:, sl], M[:, sl])
            W -= lr_v * gW
            b -= lr_v[:, :, 0] * gb
        bad = ~np.isfinite(W).all((1, 2)) | ~np.isfinite(b).all(1) | (np.abs(W).max((1, 2)) > 1e3)
        if bad.any():
            alive &= ~bad
            W[bad] = 0.0; b[bad] = 0.0
        if ep in checkpoints:
            snap(ep)
    L = tms.pop_loss(W, b)
    out = []
    for r, (lr, ini, s) in enumerate(combos):
        Wd, bd = W[r:r + 1], b[r:r + 1]
        tl, _, _ = tms.batch_loss_grad(Wd, bd, D_idx[r:r + 1], D_mu[r:r + 1])
        out.append(dict(n=n, batch=B, lr=lr, init=ini, seed=s, epochs=epochs,
                        alive=bool(alive[r]), labels={str(e): hist[r][e] for e in sorted(hist[r])},
                        final=hist[r][epochs], pop_loss=float(L[r]) if alive[r] else None,
                        train_loss=float(tl[0]) if alive[r] else None,
                        W=np.round(W[r], 5).tolist(), b=np.round(b[r], 5).tolist()))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--epochs", type=int, default=4500)
    ap.add_argument("--ns", default="300,500,700,1000,2000")
    ap.add_argument("--batches", default="100,20,5")
    ap.add_argument("--lrs", default="0.001,0.005,0.02,0.05")
    ap.add_argument("--inits", default="4gon,5gon,6gon,prior")
    ap.add_argument("--seeds", type=int, default=6)
    a = ap.parse_args()
    ns = [int(x) for x in a.ns.split(",")]; Bs = [int(x) for x in a.batches.split(",")]
    lrs = [float(x) for x in a.lrs.split(",")]; inits = a.inits.split(",")
    cps = {e for e in (10, 100, 300, 1000, 2000, 3000, 4500, 9000, 13500, 18000, 27000, 36000, 45000) if e <= a.epochs} | {a.epochs}
    done = set()
    if os.path.exists(a.out):
        with open(a.out) as f:
            for line in f:
                d = json.loads(line); done.add((d["n"], d["batch"], d["epochs"]))
    jobs = sorted(((n, B) for n in ns for B in Bs), key=lambda j: j[0] * a.epochs / j[1])
    for n, B in jobs:
        if (n, B, a.epochs) in done:
            continue
        t0 = time.time()
        res = run_job(n, B, a.epochs, lrs, inits, a.seeds, cps)
        with open(a.out, "a") as f:
            for d in res:
                f.write(json.dumps(d) + "\n")
            f.flush(); os.fsync(f.fileno())
        fin = {}
        for d in res:
            fin[d["final"]] = fin.get(d["final"], 0) + 1
        print(f"n={n} B={B} epochs={a.epochs} runs={len(res)} {time.time()-t0:.0f}s finals={fin}", flush=True)


if __name__ == "__main__":
    main()
