"""CASE-249's simulated institution, built for LEAD-181.

An institution faces N requirements, fixed and independently specified.
Some are visible from the start; the rest are hidden and become recognized
only by inquiry (or, optionally, by exogenous surfacing). Each requirement is
met or violated by the institution's current arrangement. Each period it
splits a budget B among inquiry (a units), remediation (up to b units, one
unit per fix) and ordinary output (the rest, worth alpha per unit).

Within a period, in order:
  1. inquiry: each unrecognized requirement is found w.p. 1 - (1 - q)**a;
  2. surfacing: each hidden requirement not yet known outside surfaces
     w.p. s, whether or not the institution has found it, and is then
     recognized; one still violated when it surfaces costs sigma once (the
     cost of being found out from outside, which internal knowledge does not
     shield);
  3. remediation: up to b recognized violations whose age since recognition
     is at least L are fixed, oldest first (remediation takes L periods);
  4. scoring: the governance regime's violation penalty is charged.

The internal evaluator sees recognized requirements only; the independent
evaluator sees all. Governance regimes (penalty per period, lam per
violation counted):
  pen      recognized violations (newly recognized ones included), discovery
           not rewarded: CLAIM-662's governance;
  amnesty  recognized violations recognized at least g periods ago: newly
           recognized violations are not penalized;
  none     no violation penalty;
  disc     pen, plus mu per requirement the institution finds by inquiry;
  ext      every true violation, recognized or not: the independent
           evaluator's count.

Everything is vectorized over R independent runs, each with its own
stationary policy (a[r], b[r]).
"""
import numpy as np

REGIMES = ("pen", "amnesty", "none", "disc", "ext")

DEFAULTS = dict(
    n_vis=10, n_hid=20, p_v=0.3, B=10, T=20, q=0.10, s=0.0, sigma=0.0,
    L=1, g=1, lam=1.0, alpha=0.1, mu=0.5,
)


def simulate(a, b, regime, rng, **kw):
    """Run len(a) independent episodes. Returns a dict of per-run arrays."""
    p = {**DEFAULTS, **kw}
    if regime not in REGIMES:
        raise ValueError(regime)
    a = np.asarray(a, dtype=int)
    b = np.asarray(b, dtype=int)
    R = a.shape[0]
    N = p["n_vis"] + p["n_hid"]
    hidden = np.zeros((R, N), bool)
    hidden[:, p["n_vis"]:] = True
    violated = rng.random((R, N)) < p["p_v"]
    recognized = ~hidden
    public = ~hidden  # requirements outsiders already know of
    big_neg = -10**6
    rec_time = np.where(recognized, big_neg, 0)
    reward = np.zeros(R)
    inquiry_units = np.zeros(R)
    self_found = np.zeros(R)
    p_find = 1.0 - (1.0 - p["q"]) ** a  # per run
    for t in range(p["T"]):
        # 1. inquiry
        found = (~recognized) & (rng.random((R, N)) < p_find[:, None])
        recognized |= found
        rec_time = np.where(found, t, rec_time)
        n_found = found.sum(1)
        self_found += n_found
        inquiry_units += a
        if regime == "disc":
            reward += p["mu"] * n_found
        # 2. exogenous surfacing
        if p["s"] > 0:
            surf = (~public) & (rng.random((R, N)) < p["s"])
            public |= surf
            new = surf & ~recognized
            recognized |= new
            rec_time = np.where(new, t, rec_time)
            reward -= p["sigma"] * (surf & violated).sum(1)
        # 3. remediation, oldest first, capacity b
        eligible = recognized & violated & (t - rec_time >= p["L"])
        key = np.where(eligible, rec_time, np.iinfo(np.int64).max)
        order = np.argsort(key, axis=1, kind="stable")
        rank = np.empty_like(order)
        np.put_along_axis(rank, order, np.arange(N)[None, :].repeat(R, 0), 1)
        fix = eligible & (rank < b[:, None])
        violated &= ~fix
        used = fix.sum(1)
        # 4. scoring
        rv = recognized & violated
        if regime in ("pen", "disc"):
            pen = rv.sum(1)
        elif regime == "amnesty":
            pen = (rv & (t - rec_time >= p["g"])).sum(1)
        elif regime == "ext":
            pen = violated.sum(1)
        else:
            pen = np.zeros(R)
        reward -= p["lam"] * pen
        reward += p["alpha"] * (p["B"] - a - used)
    return dict(
        reward=reward,
        inquiry=inquiry_units / p["T"],
        found_frac=self_found / p["n_hid"],
        hidden_recognized=(recognized & hidden).sum(1) / p["n_hid"],
        true_viol=violated.sum(1),
        recog_viol=(recognized & violated).sum(1),
    )


def arms(a_max=6, b_grid=(0, 2, 4, 6)):
    """The policy grid: (inquiry units, remediation cap) pairs."""
    return [(ai, bi) for ai in range(a_max + 1) for bi in b_grid]


def evaluate_arms(regime, arm_list, reps, seed, **kw):
    """Monte Carlo value of every arm, common random numbers across arms."""
    out = []
    for ai, bi in arm_list:
        rng = np.random.default_rng(seed)
        r = simulate(np.full(reps, ai), np.full(reps, bi), regime, rng, **kw)
        out.append({k: float(v.mean()) for k, v in r.items()})
    return out


def learn(regime, arm_list, episodes, seeds, rng, lr=0.1, warmup=20, **kw):
    """Gradient bandit (softmax preferences, running-average baseline,
    advantage divided by the running spread of rewards),
    one episode per step, `seeds` independent learners run in parallel.
    Returns each learner's final arm probabilities."""
    K = len(arm_list)
    A = np.array([x[0] for x in arm_list])
    Bc = np.array([x[1] for x in arm_list])
    H = np.zeros((seeds, K))
    base = np.zeros(seeds)
    sq = np.zeros(seeds)
    for e in range(episodes):
        P = np.exp(H - H.max(1, keepdims=True))
        P /= P.sum(1, keepdims=True)
        k = (P.cumsum(1) > rng.random((seeds, 1))).argmax(1)
        r = simulate(A[k], Bc[k], regime, rng, **kw)["reward"]
        # baseline and spread from earlier episodes only; the first
        # `warmup` episodes only estimate them
        if e >= warmup:
            scale = np.sqrt(sq / e) + 1e-9
            onehot = np.zeros_like(H)
            onehot[np.arange(seeds), k] = 1.0
            H += lr * ((r - base) / scale)[:, None] * (onehot - P)
        d = r - base
        base += d / (e + 1)
        sq += d * (r - base)  # Welford's sum of squared deviations
    P = np.exp(H - H.max(1, keepdims=True))
    return P / P.sum(1, keepdims=True)
