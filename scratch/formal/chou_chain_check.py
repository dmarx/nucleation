# scratch/formal/chou_chain_check.py
# Pass 29 (status review), cluster E: re-check for THEORY-1392 / NOTE-1604.
# Monte Carlo check of Chou, Chua, Teo and Zheng (2010) sec. 3: long-chain expected sales as a share of
# full flexibility, balanced i.i.d. demand, capacity mu=1 per plant. Chain max-flow computed exactly by
# the paper's greedy on the path (Algorithm 1) plus the closing arc via an exact LP-free max-flow
# (networkx-free): we compute the path greedy (Lemma 1 says the closing arc does not matter asymptotically).
# Controls: dedicated ratio (closed form 0.75 for uniform[0,2]); ACE vs ratio relation of eq. (10).
import numpy as np
rng = np.random.default_rng(1)
def path_flow(D, mu=1.0):
    S, served = 0.0, 0.0
    for d in D:
        T = mu - S                       # primary capacity left for this product
        use_p = min(d, T); rem = d - use_p
        use_s = min(rem, mu); S = use_s  # secondary capacity of next plant consumed
        served += use_p + use_s
    return served
def run(sampler, n=2000, reps=200):
    ch, fu, de = [], [], []
    for _ in range(reps):
        D = sampler(n); ch.append(path_flow(D)); fu.append(min(D.sum(), n)); de.append(np.minimum(D, 1).sum())
    ch, fu, de = map(np.mean, (ch, fu, de))
    return ch/fu, de/fu, (ch-de)/(fu-de)
for name, s, paper in [("uniform[0,2]", lambda n: rng.uniform(0, 2, n), "43/48=0.8958, ACE 7/12=0.583"),
                       ("normal CV .33 (trunc)", lambda n: np.clip(rng.normal(1, .33, n), 0, 2), "0.9614 (Table 2)"),
                       ("two-point {0,2}", lambda n: 2.0*(rng.random(n) < .5), "0.75, ACE 0.5")]:
    r, d, ace = run(s)
    print(f"{name}: chain/full={r:.4f} dedicated/full={d:.4f} finite-n CE={ace:.3f}  paper: {paper}")
