"""Posterior sampling across n for LEAD-175.

Target at sample size n: p_n(w) ∝ exp(-n L(w)) N(w; 0, I_18), with L the
population loss of tms.py (closed form) and the N(0, 1) prior Chen et al. use.
This is the tempered posterior whose free energy is Chen et al.'s Eq. 9,
F_n ≈ n L_α + λ_α log n + c_α, with the dataset fluctuation term removed
(choice stated in README.md).

Two modes, both vectorised over K independent chains and a geometric ladder of
n (the same ladder):

  pt          parallel-tempering HMC over the ladder; per block, the count of
              each region label at each rung (unrestricted occupancy, as in
              Chen et al.'s Fig. 2).
  restricted  HMC confined to one region label (a proposal that changes the
              label is rejected), at every rung, no swaps; per block, the mean
              of L at each rung. d log Z_α / dn = -E_{α,n}[L], so these give
              the n-dependence of each region's free energy by thermodynamic
              integration, down to probabilities the unrestricted run cannot see.

Each block is appended to the output JSONL as it finishes. After the line is
on disk, a checkpoint OUT.STATE.npz is replaced atomically. It holds the
number of blocks done, the configuration, the chains, the step sizes and the
generator's state. A rerun reconciles the two and resumes exactly, as an
uninterrupted run would have gone, or stops with a message (see
`reconcile`).

Usage: python3 -I posterior.py pt OUT.jsonl [--blocks B] [--iters I]
       python3 -I posterior.py restricted OUT.jsonl --region 5+ [...]
"""
import argparse, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import tms

LADDER = np.geomspace(20, 10000, 44)


def U_and_grad(th, n):
    """th (..., 18): W = th[..., :12].reshape(2, 6), b = th[..., 12:].
    U = n L + |th|^2 / 2 and its gradient; n broadcasts over th[..., 0]."""
    W = th[..., :12].reshape(th.shape[:-1] + (2, 6)); b = th[..., 12:]
    L, gW, gb = tms.pop_loss(W, b, grad=True)
    g = np.concatenate([gW.reshape(th.shape[:-1] + (12,)), gb], -1)
    U = n * L + 0.5 * (th * th).sum(-1)
    return U, n[..., None] * g + th, L


def labels_of(th):
    W = th[..., :12].reshape(th.shape[:-1] + (2, 6)); b = th[..., 12:]
    k, s, m = tms.classify(W, b)
    return k * 100 + s * 10 + m                      # integer code


def code_to_label(c):
    return tms.label(c // 100, (c // 10) % 10, c % 10)


def label_to_code(lab):
    k = int(lab[0]); s = lab.count("+"); m = lab.count("-")
    return k * 100 + s * 10 + m


def hmc_step(th, n, eps, nleap, rng, region=None):
    U0, g, _ = U_and_grad(th, n)
    p = rng.normal(size=th.shape)
    H0 = U0 + 0.5 * (p * p).sum(-1)
    e = (eps * rng.uniform(0.8, 1.2, size=eps.shape))[..., None]
    x = th.copy(); q = p - 0.5 * e * g
    for i in range(nleap):
        x = x + e * q
        U1, g, L1 = U_and_grad(x, n)
        if i < nleap - 1:
            q = q - e * g
    q = q - 0.5 * e * g
    H1 = U1 + 0.5 * (q * q).sum(-1)
    with np.errstate(over="ignore", invalid="ignore"):
        acc = np.log(rng.random(H0.shape)) < (H0 - H1)
    acc &= np.isfinite(H1)
    if region is not None:
        acc &= labels_of(x) == region
    th = np.where(acc[..., None], x, th)
    return th, acc


def init_state(mode, K, region, rng):
    nr = len(LADDER)
    if mode == "pt":
        th = rng.normal(size=(K, nr, 18))           # prior draws
    else:
        lab = tms.label(region // 100, (region // 10) % 10, region % 10)
        W, b = tms.CRIT[lab]
        th = np.broadcast_to(np.concatenate([W.ravel(), b]), (K, nr, 18)).copy()
        th += rng.normal(scale=1e-3, size=th.shape)
        # break exact ties in the off vertex / zero columns
    eps = np.broadcast_to(np.minimum(0.3, 0.5 / np.sqrt(LADDER)), (K, nr)).copy()
    return th, eps


def read_blocks(path):
    """Complete JSON lines of `path`, dropping a torn final line.

    A line cut off by an interruption is the last one. It is removed from the
    file, since the block it began is not reflected anywhere. A line that
    fails to parse anywhere else is damage this script did not make, and the
    run stops."""
    if not os.path.exists(path):
        return 0
    with open(path, "rb") as f:
        raw = f.read()
    lines = raw.split(b"\n")
    tail = lines.pop()                       # b"" when the file ends in a newline
    good = 0
    for i, line in enumerate(lines):
        try:
            json.loads(line)
        except ValueError:
            sys.exit(f"{path}: line {i + 1} is not JSON; not resuming over it")
        good += 1
    if tail:
        with open(path, "r+b") as f:
            f.truncate(len(raw) - len(tail))
    return good


def truncate_to(path, keep):
    """Keep the first `keep` lines of `path`."""
    with open(path, "rb") as f:
        lines = f.read().split(b"\n")
    with open(path, "wb") as f:
        f.write(b"".join(l + b"\n" for l in lines[:keep]))
        f.flush(); os.fsync(f.fileno())


def save_state(stfile, done, config, th, eps, rng):
    """Replace the checkpoint atomically: write a sibling, then rename."""
    tmp = stfile + ".tmp"
    with open(tmp, "wb") as f:
        np.savez(f, done=done, config=config, th=th, eps=eps,
                 rng=json.dumps(rng.bit_generator.state))
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, stfile)


def reconcile(out, stfile, config, rng):
    """Where to resume, from the output and the checkpoint together.

    Returns (blocks done, th, eps), or None for a fresh start. The checkpoint
    is saved after the block's line, so an interruption between the two
    leaves the output one block ahead. That block's line is dropped and the
    block is rerun from the checkpoint, which reproduces it, since the
    generator's state is part of the checkpoint. Any other mismatch stops the
    run."""
    nb = read_blocks(out)
    if not os.path.exists(stfile):
        if nb:
            sys.exit(f"{out}: {nb} block(s) written but no checkpoint {stfile}; "
                     f"not resuming (fresh chains would skip burn-in)")
        return None
    z = np.load(stfile)
    if "done" not in z or "config" not in z:
        sys.exit(f"{stfile}: a checkpoint from before block counts were kept; "
                 f"move it and the output aside to start afresh")
    if str(z["config"]) != config:
        sys.exit(f"{stfile}: checkpoint configuration differs from this run's; "
                 f"not resuming")
    done = int(z["done"])
    if nb == done + 1:
        truncate_to(out, done)
    elif nb != done:
        sys.exit(f"{out}: {nb} block(s) written but the checkpoint holds {done}; "
                 f"not resuming")
    rng.bit_generator.state = json.loads(str(z["rng"]))
    return done, z["th"], z["eps"]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("pt", "restricted"))
    ap.add_argument("out")
    ap.add_argument("--region", default=None)
    ap.add_argument("--chains", type=int, default=32)
    ap.add_argument("--blocks", type=int, default=40)
    ap.add_argument("--iters", type=int, default=500)
    ap.add_argument("--burn", type=int, default=4, help="adaptation blocks (written, flagged burn)")
    ap.add_argument("--nleap", type=int, default=8)
    ap.add_argument("--classify-every", type=int, default=5)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--ladder", default="20,10000,44", help="lo,hi,count of the geometric ladder of n")
    a = ap.parse_args(argv)
    global LADDER
    lo, hi, cnt = a.ladder.split(",")
    LADDER = np.geomspace(float(lo), float(hi), int(cnt))
    region = label_to_code(a.region) if a.region else None
    stfile = a.out + ".STATE.npz"
    # Everything that shapes the chains, so a checkpoint is resumed only by a
    # run that would have produced it. The block count is not part of it: a
    # run may be extended.
    config = json.dumps(dict(mode=a.mode, region=a.region, chains=a.chains,
                             iters=a.iters, burn=a.burn, nleap=a.nleap,
                             classify_every=a.classify_every, seed=a.seed,
                             ladder=a.ladder), sort_keys=True)
    rng = np.random.default_rng([a.seed, 0, 17])
    state = reconcile(a.out, stfile, config, rng)
    if state is None:
        nb = 0
        th, eps = init_state(a.mode, a.chains, region, rng)
    else:
        nb, th, eps = state
    K, nr = th.shape[:2]
    n = np.broadcast_to(LADDER, (K, nr)).astype(float)
    for blk in range(nb, a.blocks):
        t0 = time.time()
        burn = blk < a.burn
        counts = [dict() for _ in range(nr)]
        sumL = np.zeros(nr); sumL2 = np.zeros(nr); nL = 0
        chainL = np.zeros((K, nr))
        accs = np.zeros(nr); swaps = np.zeros(nr - 1); swap_tries = np.zeros(nr - 1)
        for it in range(a.iters):
            th, acc = hmc_step(th, n, eps, a.nleap, rng, region)
            accs += acc.mean(0)
            if burn:
                eps *= np.where(acc, 1.02, 0.97)
            if a.mode == "pt":
                _, _, L = U_and_grad(th, n)
                start = it % 2
                i = np.arange(start, nr - 1, 2)
                d = (LADDER[i] - LADDER[i + 1])[None, :] * (L[:, i + 1] - L[:, i])
                ok = np.log(rng.random(d.shape)) < -d
                tmp = th[:, i].copy()
                th[:, i] = np.where(ok[..., None], th[:, i + 1], th[:, i])
                th[:, i + 1] = np.where(ok[..., None], tmp, th[:, i + 1])
                swaps[i] += ok.mean(0); swap_tries[i] += 1
            if it % a.classify_every == 0:
                _, _, L = U_and_grad(th, n)
                sumL += L.sum(0); sumL2 += (L * L).sum(0); nL += K; chainL += L
                if a.mode == "pt":
                    lab = labels_of(th)
                    for r in range(nr):
                        u, c = np.unique(lab[:, r], return_counts=True)
                        for uu, cc in zip(u, c):
                            key = code_to_label(int(uu))
                            counts[r][key] = counts[r].get(key, 0) + int(cc)
        rec = dict(mode=a.mode, region=a.region, block=blk, burn=burn, iters=a.iters,
                   chains=K, ladder=LADDER.round(3).tolist(),
                   meanL=(sumL / nL).tolist(), varL=(sumL2 / nL - (sumL / nL) ** 2).tolist(),
                   chain_meanL=(chainL / (nL / K)).round(7).tolist(),
                   acc=(accs / a.iters).round(3).tolist(),
                   eps=eps.mean(0).round(5).tolist())
        if a.mode == "pt":
            rec["counts"] = counts
            rec["swap"] = (swaps / np.maximum(swap_tries, 1)).round(3).tolist()
        with open(a.out, "a") as f:
            f.write(json.dumps(rec) + "\n"); f.flush(); os.fsync(f.fileno())
        save_state(stfile, blk + 1, config, th, eps, rng)
        print(f"{a.mode} {a.region} block {blk} {time.time()-t0:.0f}s acc[min]={min(rec['acc']):.2f}", flush=True)


if __name__ == "__main__":
    main()
