"""Run CASE-158's arms. Every method of the arm runs on
the same test images, noise and probe draws. Results append to
results/runs.jsonl, one line per item; a rerun skips items already written.

    python3 -I study.py            # all arms, three gate temperatures, 12 seeds
    python3 -I study.py full 3     # one arm, first 3 seeds (smoke)

One item = (arm, tau, seed): tau is the shared gate temperature of governance
and router, swept so that neither is compared at a setting tuned for the other.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from model import (SIGMAS, World, fit_operator, denoise, run_chain,  # noqa: E402
                   router_features, Router, Governance, softmax_neg)

OUT = os.path.join(HERE, 'results', 'runs.jsonl')
E, B, NPROBE = 84, 8, 8
TAUS = [0.03, 0.1, 0.3]
ARMS = ['full', 'bandit', 'capture50', 'capture80', 'scale', 'cycles', 'training', 'full_rr']
# full_rr: the full arm again, adding a router that sees only the region id (no per-item context)
SEEDS = list(range(12))


def make_env(arm, rng):
    if arm == 'cycles':
        w = World(rng, 3)
        ops = []
        for k in range(3):
            X = np.vstack([w.sample(rng, k, 3000), 0.5 * w.sample(rng, (k + 1) % 3, 3000)])
            ops.append(fit_operator(X, 6))
        base = np.array([0.4, 0.3, 0.3])
        pre = [np.roll(base, r) for r in range(3)]
        post = [np.roll(base, r + 1) for r in range(3)]
        return w, ops, 3, pre, post
    w = World(rng, 4)
    ops = [fit_operator(w.sample(rng, k, 3000), w.m) for k in range(4)]
    pre = [np.eye(4)[r] for r in range(4)]
    post = [np.eye(4)[(r + 1) % 4] for r in range(4)]
    return w, ops, 4, pre, post


def draw(w, rng, mix, n):
    """n patches of a region whose content types are mixed by `mix`."""
    t = rng.choice(len(mix), size=n, p=mix)
    X = np.zeros((n, w.p))
    for k in np.unique(t):
        X[t == k] = w.sample(rng, k, int(np.sum(t == k)))
    return X


def probe_scores(ops, X, Y, sig):
    """Per-probe squared error of each specialist's one-step proposal."""
    out = []
    for V, lam in ops:
        P = ((Y @ V) * (lam[None] / (lam[None] + sig[:, None] ** 2))) @ V.T
        out.append(np.mean((P - X) ** 2, 1))
    return np.stack(out, 1)


def sel(m, F, R):
    """The region-only router sees the region id and sigma only."""
    return np.hstack([F[:, :R], F[:, -1:]]) if m == 'router_region' else F


def run_item(arm, seed, tau=0.1):
    env_rng = np.random.default_rng([seed, 0])
    w, ops0, K, pre, post = make_env(arm, env_rng)
    R = len(pre)
    scale_a = np.array([0.1, 0.46, 2.15, 10.0])[:K]
    scale_g = np.array([1.0, 0.5, 2.0, 1.0])[:K]
    cap = {'capture50': 0.5, 'capture80': 0.8}.get(arm, 0.0)

    methods = ['fixed', 'oracle', 'governance', 'conformity', 'router']
    if arm == 'full_rr':
        methods += ['router_region']
    if arm == 'scale':
        methods += ['governance_raw', 'router_std']
    if arm == 'bandit':
        methods += ['governance_explore', 'router_explore']
    d = R + K + R * K + 1
    state = {}
    for m in methods:
        state[m] = dict(ops=[(V.copy(), l.copy()) for V, l in ops0],
                        C=[(V * l) @ V.T for V, l in ops0],
                        gov=Governance(R, K, tau=tau, standardize=(m == 'governance' and arm == 'scale')),
                        router=Router(R + 1 if m == 'router_region' else d, K, tau=tau), hist=[[] for _ in range(K)])
    curve = {m: [] for m in methods}
    serve_old = {m: [] for m in methods}  # weight on each region's pre-reversal specialist, after reversal
    t0 = time.time()
    for e in range(E):
        mixes = pre if e < E // 2 else post
        ep_rng = np.random.default_rng([seed, 1, e])
        X0 = np.stack([draw(w, ep_rng, mixes[r], B) for r in range(R)], 1)
        # probe pool shared by methods; curated / bandit choices are each method's own
        pr_rng = np.random.default_rng([seed, 2, e])
        probes = []
        for r in range(R):
            Xp = draw(w, pr_rng, mixes[r], NPROBE * 16)
            sg = pr_rng.choice(SIGMAS, size=len(Xp))
            Yp = Xp + sg[:, None] * pr_rng.standard_normal(Xp.shape)
            probes.append((Xp, Yp, sg))
        coin = pr_rng.random((R, NPROBE))
        ubandit = pr_rng.random((R, NPROBE))
        for m in methods:
            st = state[m]
            ops = st['ops']
            gov, router = st['gov'], st['router']
            if m == 'fixed':
                fn = lambda r, Y, s: np.full((len(Y), K), 1.0 / K)
            elif m == 'oracle':
                fn = lambda r, Y, s, mixes=mixes: np.tile(np.eye(K)[int(np.argmax(mixes[r]))], (len(Y), 1))
            elif m.startswith('router'):
                fn = lambda r, Y, s, router=router, ops=ops, m=m: router.gate(sel(m, router_features(ops, Y, r, R, s), R))
            else:
                fn = lambda r, Y, s, gov=gov: np.tile(gov.g[r], (len(Y), 1))
            xhat = run_chain(ops, X0, np.random.default_rng([seed, 3, e]), fn)
            curve[m].append(float(np.mean((xhat - X0) ** 2)))
            # allocation actually used this episode, per region
            Ym = X0 + 0.6 * np.random.default_rng([seed, 4, e]).standard_normal(X0.shape)
            used = np.stack([fn(r, Ym[:, r], 0.6).mean(0) for r in range(R)])
            if e >= E // 2:
                serve_old[m].append(float(np.mean([used[r, int(np.argmax(pre[r]))] for r in range(R)])))
            if m in ('fixed', 'oracle'):
                continue
            if m == 'conformity':
                S = np.zeros((R, K))
                for r in range(R):
                    props = np.stack([denoise(op, Ym[:, r], 0.6) for op in ops], 1)
                    comb = np.einsum('k,nkp->np', used[r], props)
                    S[r] = np.mean((props - comb[:, None]) ** 2, axis=(0, 2))
                gov.update(np.arange(R), S)
            else:
                regs, Fs, Ss = [], [], []
                for r in range(R):
                    Xp, Yp, sg = probes[r]
                    F = router_features(ops, Yp, r, R, 0.0)
                    F[:, -1] = sg ** 2
                    F = sel(m, F, R)
                    Sall = probe_scores(ops, Xp, Yp, sg)
                    if m.startswith('router'):
                        incumbent = int(np.argmax(router.gate(F).mean(0)))
                    else:
                        incumbent = int(np.argmax(gov.g[r]))
                    for j in range(NPROBE):
                        i = j  # independent probe
                        dup = 1
                        if coin[r, j] < cap:
                            cand = np.arange(j * 16, (j + 1) * 16)
                            others = np.delete(Sall[cand], incumbent, axis=1).min(1)
                            i = int(cand[np.argmin(Sall[cand, incumbent] - others)])
                            dup = 2
                        s = Sall[i].copy()
                        if arm == 'bandit':
                            if m.startswith('router'):
                                pi = router.gate(F[i:i + 1])[0]
                            else:
                                pi = gov.g[r]
                            if m.endswith('_explore'):
                                pi = 0.9 * pi + 0.1 / K  # protected access: a floor on auditing
                            k = int(min(np.searchsorted(np.cumsum(pi), ubandit[r, j]), K - 1))
                            obs = np.full(K, np.nan); obs[k] = s[k]
                            s = obs
                        if arm == 'cycles':
                            a, b = np.random.default_rng([seed, 5, e, r, j]).choice(K, 2, replace=False)
                            obs = np.full(K, np.nan)
                            obs[a], obs[b] = float(s[a] > s[b]), float(s[b] > s[a])
                            s = obs
                        if arm == 'scale':
                            s = scale_a * s ** scale_g
                        for _ in range(dup):
                            regs.append(r); Fs.append(F[i]); Ss.append(s)
                regs, Fs, Ss = np.array(regs), np.array(Fs), np.array(Ss)
                if m == 'router_std':
                    Ss = Ss.copy()
                    for k in range(K):
                        v = Ss[~np.isnan(Ss[:, k]), k]
                        st['hist'][k].extend(v.tolist()); st['hist'][k] = st['hist'][k][-400:]
                        h = np.asarray(st['hist'][k])
                        if len(h) > 1:
                            Ss[:, k] = (Ss[:, k] - h.mean()) / (h.std() + 1e-9)
                if m.startswith('router'):
                    router.update(Fs, Ss)
                else:
                    gov.update(regs, Ss)
            if arm == 'training':
                rho = 0.1
                for k in range(K):
                    for r in range(R):
                        Xr = draw(w, np.random.default_rng([seed, 6, e, r]), mixes[r], 32)
                        st['C'][k] = st['C'][k] + rho * used[r, k] * (Xr.T @ Xr / 32 - st['C'][k])
                    ops[k] = fit_operator_cov(st['C'][k], w.m)
    h = E // 2
    rec = {'arm': arm, 'tau': tau, 'seed': seed, 'secs': round(time.time() - t0, 1), 'n_probe_audits': NPROBE * R * E}
    for m in methods:
        c = np.array(curve[m])
        rec[m] = {'pre': float(c[h - 10:h].mean()), 'post': float(c[h:].mean()),
                  'last10': float(c[-10:].mean()), 'serve_old_post': float(np.mean(serve_old[m])),
                  'serve_old_last10': float(np.mean(serve_old[m][-10:]))}
    # per-episode curves are left out of the results file to keep it under 1 MB
    return rec


def fit_operator_cov(C, rank):
    wv, V = np.linalg.eigh(C)
    idx = np.argsort(wv)[::-1][:rank]
    return V[:, idx], np.maximum(wv[idx], 1e-6)


def main():
    arms = ARMS if len(sys.argv) < 2 else [sys.argv[1]]
    seeds = SEEDS if len(sys.argv) < 3 else SEEDS[:int(sys.argv[2])]
    done = set()
    if os.path.exists(OUT):
        for line in open(OUT):
            j = json.loads(line); done.add((j['arm'], j['tau'], j['seed']))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    for arm in arms:
      for tau in TAUS:
        for seed in seeds:
            if (arm, tau, seed) in done:
                continue
            rec = run_item(arm, seed, tau)
            with open(OUT, 'a') as f:
                f.write(json.dumps(rec) + '\n')
            print(arm, tau, seed, rec['secs'], {m: round(rec[m]['post'], 4) for m in rec if isinstance(rec[m], dict) and 'post' in rec[m]}, flush=True)


if __name__ == '__main__':
    main()
