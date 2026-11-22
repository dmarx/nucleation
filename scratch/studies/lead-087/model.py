"""LEAD-087: CASE-145's populations, simulated.

Members hold category prototypes; they respond with the nearest one.
Arms differ only in how members interact at test (see README.md). All
randomness for a seed is drawn up front, so a perturbed run and its twin
share their random numbers (stimuli, pairings, referees, feedback).
"""
import numpy as np

K, D, N = 6, 4, 30
NOISE = 0.5          # stimulus noise around a category's prototype
LR_TRAIN = 0.05
LR_SOC = 0.05        # social and check updates
LR_ENV = 0.05        # environmental feedback updates
Q_BASE = 0.05        # base feedback probability per member per round
T_TRAIN = 400
T_TEST = 600
T_PERT = 100
WINDOW = 300         # rounds after T_PERT over which s and g are averaged
T_FLIP = 300         # collective contingency flips here
F_S = 0.2            # share of members perturbed
ARMS = ("independent", "learned-cut", "conform", "enforce", "evidential")


def teacher(rng):
    """A structured schema: two clusters of three prototypes."""
    centres = np.zeros((2, D))
    centres[0, 0], centres[1, 0] = -1.5, 1.5
    P = np.repeat(centres, 3, axis=0) + rng.normal(0, 0.8, (K, D))
    return P


def nearest(P, X):
    """P: (m, K, D) prototypes; X: (m, D) stimuli -> (m,) labels."""
    d = ((P - X[:, None, :]) ** 2).sum(-1)
    return d.argmin(-1)


def structure(P):
    """Upper triangle of the prototype distance matrix, per member."""
    iu = np.triu_indices(K, 1)
    d = np.sqrt(((P[:, :, None, :] - P[:, None, :, :]) ** 2).sum(-1))
    return d[:, iu[0], iu[1]]


def concordance(P):
    v = structure(P)
    c = np.corrcoef(v)
    iu = np.triu_indices(len(v), 1)
    return float(c[iu].mean())


def train(rng, W, social):
    """Each member learns from its own labelled stream; with social=True
    it also conforms to a partner's label each round (learned-cut)."""
    P = rng.normal(0, 1.0, (N, K, D))
    idx = np.arange(N)
    for _ in range(T_TRAIN):
        c = rng.integers(K, size=N)
        X = W[c] + rng.normal(0, NOISE, (N, D))
        P[idx, c] += LR_TRAIN * (X - P[idx, c])
        if social:
            perm = rng.permutation(N)
            a, b = perm[: N // 2], perm[N // 2:]
            cs = rng.integers(K, size=N // 2)
            Xs = W[cs] + rng.normal(0, NOISE, (N // 2, D))
            la, lb = nearest(P[a], Xs), nearest(P[b], Xs)
            P[a, lb] += LR_SOC * (Xs - P[a, lb])
            P[b, la] += LR_SOC * (Xs - P[b, la])
    return P


def draws(rng):
    """Every random number of the test phase, shared by a run and its twin."""
    h = N // 2
    return dict(
        perm=np.stack([rng.permutation(N) for _ in range(T_TEST)]),
        cat=rng.integers(K, size=(T_TEST, h)),
        noise=rng.normal(0, NOISE, (T_TEST, h, D)),
        ref=rng.integers(N, size=(T_TEST, h)),
        fb_u=rng.random((T_TEST, N)),
        fb_cat=rng.integers(K, size=(T_TEST, N)),
        fb_noise=rng.normal(0, NOISE, (T_TEST, N, D)),
        v_cat=rng.integers(K, size=T_TEST),
        v_noise=rng.normal(0, NOISE, (T_TEST, D)),
        v_eps=rng.random(T_TEST),
        v_rand=rng.integers(2, size=T_TEST),
    )


def run(P0, W0, R, arm, q, pert=None, shift=None, record_every=5):
    """Test phase. pert = (S, a, vec): add vec to S's prototype a at
    T_PERT. shift = (a, vec): move the world's prototype a at T_PERT.
    Returns trajectory of prototype a (every record_every rounds), the
    number of check events per member per round, and the collective
    agency series for both mechanism levels."""
    P = P0.copy()
    W = W0.copy()
    h = N // 2
    idx = np.arange(N)
    rule = np.arange(K) % 2               # correct collective action
    Qc = np.zeros((K, 2))                 # vote mechanism's policy table
    match_vote = np.zeros(T_TEST)         # collective action == current rule
    match_none = np.zeros(T_TEST)
    traj = []
    checks = 0
    for t in range(T_TEST):
        if t == T_PERT:
            if pert is not None:
                S, a, vec = pert
                P[S, a] += vec
            if shift is not None:
                a, vec = shift
                W[a] = W[a] + vec
        cur_rule = rule if t < T_FLIP else 1 - rule
        # --- pairs on a shared stimulus
        perm = R["perm"][t]
        i, j = perm[:h], perm[h:]
        c = R["cat"][t]
        X = W[c] + R["noise"][t]
        li, lj = nearest(P[i], X), nearest(P[j], X)
        if arm == "conform":
            P[i, lj] += LR_SOC * (X - P[i, lj])
            P[j, li] += LR_SOC * (X - P[j, li])
        elif arm == "enforce":
            dis = li != lj
            r = R["ref"][t]
            lr_ = nearest(P[r], X)
            # the holder of the label the referee does not share moves
            mi = dis & (lr_ == lj)      # i in the minority
            mj = dis & (lr_ == li)
            P[i[mi], lj[mi]] += LR_SOC * (X[mi] - P[i[mi], lj[mi]])
            P[j[mj], li[mj]] += LR_SOC * (X[mj] - P[j[mj], li[mj]])
        elif arm == "evidential":
            dis = li != lj
            checks += 2 * int(dis.sum())
            ii, jj, cc, XX = i[dis], j[dis], c[dis], X[dis]
            P[ii, cc] += LR_SOC * (XX - P[ii, cc])
            P[jj, cc] += LR_SOC * (XX - P[jj, cc])
        # --- environmental feedback
        fb = R["fb_u"][t] < q
        fc = R["fb_cat"][t][fb]
        FX = W[fc] + R["fb_noise"][t][fb]
        P[idx[fb], fc] += LR_ENV * (FX - P[idx[fb], fc])
        # --- collective choice (does not feed back into prototypes)
        vc = R["v_cat"][t]
        vx = W[vc] + R["v_noise"][t]
        labs = nearest(P, np.repeat(vx[None], N, 0))
        m = np.bincount(labs, minlength=K).argmax()
        act = R["v_rand"][t] if R["v_eps"][t] < 0.1 else int(Qc[m].argmax())
        rew = float(act == cur_rule[vc])
        Qc[m, act] += 0.1 * (rew - Qc[m, act])
        match_vote[t] = act == cur_rule[vc]
        # no mechanism: majority of members' individual fixed actions
        ind = rule[labs]
        match_none[t] = (np.bincount(ind, minlength=2).argmax()) == cur_rule[vc]
        if t % record_every == 0:
            traj.append(P[:, :, :].copy())
    return dict(traj=np.array(traj), check_rate=checks / (N * T_TEST),
                match_vote=match_vote, match_none=match_none, P_end=P)


def agency(match):
    """Adaptation to the flipped collective contingency: share matching the
    new rule in the final 100 rounds minus share matching it in the 100
    rounds before the flip (matching the new rule before the flip means
    not matching the old one)."""
    pre = 1 - match[T_FLIP - 100:T_FLIP].mean()
    post = match[-100:].mean()
    return float(post - pre)
