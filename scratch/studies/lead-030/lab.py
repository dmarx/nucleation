"""The laboratory of genres (LEAD-030, CASE-296).

A simulated bipartite engagement network: users see items (exposure) and
engage with some of them. Two worlds:

  taste    - users and items carry latent preference vectors drawn from K
             clusters, so genres and audiences exist in the preferences;
             exposure is popularity-weighted and otherwise unstructured.
  exposure - preference vectors have the same spread but no clusters;
             exposure is channelled through G communities (a language, a
             region, a promotion slot), so clusters in engagement come from
             exposure alone. This is CASE-296's negative control.

Classes (genres of items, audiences of users) are inferred once, from the
burn-in periods' raw engagement counts, by degree-normalized spectral
co-clustering, and held fixed. Five arms then run:

  inferred         base exposure policy; preferences fixed
  inferred+adapt   base exposure policy; users drift toward what they
                   engage with, creators copy what is engaged
  used             class policy: exposure steered to the item class the
                   user's audience engages most; preferences fixed
  used+adapt       class policy with adaptation
  popular+adapt    exposure steered to globally popular items, with
                   adaptation (the arm where erasure is expected)

Measures, at the start (after burn-in) and the end, are in `evaluate`.
"""
from __future__ import annotations

import numpy as np
from scipy.cluster.vq import kmeans2
from scipy.optimize import minimize

# ----------------------------------------------------------------- worlds

DEFAULTS = dict(
    U=600, I=400, d=8, K=6, G=6,
    s_between=0.60, s_within=0.30,
    a=-2.0, b=1.0, s_pop=0.7, pop_power=0.5,
    kappa_comm=0.08,      # exposure weight outside one's community (exposure world)
    kappa_class=0.05,     # exposure weight outside the target class (class policy)
    m=30,                 # exposures per user per period
    m_probe=20,           # random exposures per user per probe fold
    burn=5, T=15,
    lam_item=2.0,         # ridge on the item-level factors (tuned once, see README)
    eta=0.10,             # user drift per period toward engaged items
    turnover=0.03,        # share of items replaced per period by creators
)


def sigmoid(x):
    return 0.5 * (1.0 + np.tanh(0.5 * x))


def make_world(kind, rng, p):
    U, I, d, K, G = p["U"], p["I"], p["d"], p["K"], p["G"]
    st = dict(kind=kind)
    if kind == "taste":
        mu = rng.normal(0, p["s_between"], (K, d))
        tu = rng.integers(0, K, U)
        ti = rng.integers(0, K, I)
        st["u"] = mu[tu] + rng.normal(0, p["s_within"], (U, d))
        st["v"] = mu[ti] + rng.normal(0, p["s_within"], (I, d))
        st["true_u"], st["true_i"] = tu, ti
        st["comm_u"] = np.zeros(U, int)
        st["comm_i"] = np.zeros(I, int)
    elif kind == "exposure":
        s = np.hypot(p["s_between"], p["s_within"])
        st["u"] = rng.normal(0, s, (U, d))
        st["v"] = rng.normal(0, s, (I, d))
        st["comm_u"] = rng.integers(0, G, U)
        st["comm_i"] = rng.integers(0, G, I)
        st["true_u"], st["true_i"] = st["comm_u"].copy(), st["comm_i"].copy()
    else:
        raise ValueError(kind)
    st["beta"] = rng.normal(0, p["s_pop"], I)
    st["item_class_override"] = np.full(I, -1)  # class a new item is labelled with
    return st


def base_weights(st, p):
    w = np.exp(p["pop_power"] * st["beta"])[None, :].repeat(len(st["u"]), 0)
    if st["kind"] == "exposure":
        same = st["comm_u"][:, None] == st["comm_i"][None, :]
        w = w * np.where(same, 1.0, p["kappa_comm"])
    return w


def sample_exposure(w, m, rng):
    """Weighted sampling of m items per row without replacement (Gumbel top-k)."""
    keys = np.log(w) + rng.gumbel(size=w.shape)
    return np.argpartition(-keys, m, axis=1)[:, :m]


def engage_prob(st, p, users, items):
    aff = np.einsum("nd,nd->n", st["u"][users], st["v"][items])
    return sigmoid(p["a"] + p["b"] * aff + st["beta"][items])


def engage(st, p, X, rng):
    U, m = X.shape
    users = np.repeat(np.arange(U), m)
    pr = engage_prob(st, p, users, X.ravel()).reshape(U, m)
    return rng.random((U, m)) < pr


def policy_weights(st, p, arm, cls, pop_counts):
    w = base_weights(st, p)
    if arm.startswith("used"):
        icls = item_classes(st, cls)
        tgt = cls["target"][cls["user"]]
        inside = icls[None, :] == tgt[:, None]
        w = w * np.where(inside, 1.0, p["kappa_class"])
    elif arm.startswith("popular"):
        q = (pop_counts + 1.0) ** 2
        w = w * (q / q.mean())[None, :]
    return w


def item_classes(st, cls):
    ic = cls["item"].copy()
    ov = st["item_class_override"]
    ic[ov >= 0] = ov[ov >= 0]
    return ic


def adapt(st, p, X, Y, rng, cls):
    """Users drift toward the items they engaged with; creators replace the
    least-engaged items with variants of engaged ones."""
    U, m = X.shape
    eng_n = Y.sum(1)
    vsum = np.zeros_like(st["u"])
    np.add.at(vsum, np.repeat(np.arange(U), m)[Y.ravel()], st["v"][X.ravel()[Y.ravel()]])
    has = eng_n > 0
    target = vsum[has] / eng_n[has, None]
    st["u"][has] = (1 - p["eta"]) * st["u"][has] + p["eta"] * target
    # creators
    I = len(st["v"])
    shown = np.bincount(X.ravel(), minlength=I)
    hits = np.bincount(X.ravel()[Y.ravel()], minlength=I)
    rate = (hits + 1) / (shown + 4)
    n_rep = int(round(p["turnover"] * I))
    if n_rep == 0 or hits.sum() == 0:
        return
    worst = np.argsort(rate)[:n_rep]
    parents = rng.choice(I, n_rep, p=hits / hits.sum())
    icls = item_classes(st, cls)
    st["v"][worst] = st["v"][parents] + rng.normal(0, p["s_within"], (n_rep, st["v"].shape[1]))
    st["beta"][worst] = rng.normal(0, p["s_pop"], n_rep)
    st["comm_i"][worst] = st["comm_i"][parents]
    st["true_i"][worst] = st["true_i"][parents]
    st["item_class_override"][worst] = icls[parents]


# ------------------------------------------------------------- inference

def spectral_coclusters(C, K, rng, tau=None):
    """Regularized, degree-normalized spectral co-clustering of a U x I count
    matrix. Returns user labels, item labels (each 0..K-1)."""
    C = np.asarray(C, float)
    du, di = C.sum(1), C.sum(0)
    if tau is None:
        tau = C.sum() / C.shape[0] / 2 + 1e-9
    A = C / np.sqrt(du + tau)[:, None] / np.sqrt(di + tau * C.shape[0] / C.shape[1])[None, :]
    Uu, s, Vt = np.linalg.svd(A, full_matrices=False)
    k = min(K, len(s))
    eu = Uu[:, :k] * s[:k]
    ei = Vt[:k].T * s[:k]
    eu = eu / (np.linalg.norm(eu, axis=1, keepdims=True) + 1e-12)
    ei = ei / (np.linalg.norm(ei, axis=1, keepdims=True) + 1e-12)
    lu = _kmeans(eu, K, rng)
    li = _kmeans(ei, K, rng)
    return lu, li


def _kmeans(X, K, rng, restarts=5):
    best, best_in = None, np.inf
    for _ in range(restarts):
        cen, lab = kmeans2(X, K, minit="++", seed=rng.integers(1 << 31))
        inertia = ((X - cen[lab]) ** 2).sum()
        if inertia < best_in:
            best, best_in = lab, inertia
    return best


def block_rates(C, lu, li, K):
    """Degree-corrected block intensity omega[c, d] = m_cd / (R_c C_d)."""
    M = np.zeros((K, K))
    np.add.at(M, (lu[:, None].repeat(C.shape[1], 1), li[None, :].repeat(C.shape[0], 0)), C)
    R = np.bincount(lu, weights=C.sum(1), minlength=K)
    Cd = np.bincount(li, weights=C.sum(0), minlength=K)
    return M / np.maximum(np.outer(R, Cd), 1e-12)


def make_classes(C, K, rng, lu=None, li=None):
    if lu is None:
        lu, li = spectral_coclusters(C, K, rng)
    om = block_rates(C, lu, li, K)
    return dict(user=lu, item=li, target=om.argmax(1), omega=om)


def size_matched_partition(score, sizes):
    """Assign the rank-ordered entities into blocks of the given sizes."""
    order = np.argsort(-score, kind="stable")
    lab = np.empty(len(score), int)
    start = 0
    for c, n in enumerate(sizes):
        lab[order[start:start + n]] = c
        start += n
    return lab


def ari(a, b):
    """Adjusted Rand index."""
    a = np.unique(a, return_inverse=True)[1]
    b = np.unique(b, return_inverse=True)[1]
    n = len(a)
    T = np.zeros((a.max() + 1, b.max() + 1))
    np.add.at(T, (a, b), 1)
    c2 = lambda x: x * (x - 1) / 2
    s = c2(T).sum()
    sa, sb = c2(T.sum(1)).sum(), c2(T.sum(0)).sum()
    exp = sa * sb / c2(n)
    mx = (sa + sb) / 2
    return 0.0 if mx == exp else (s - exp) / (mx - exp)


# ------------------------------------------------- predictive models

def fit_logistic(users, items, y, U, I, cu=None, ci=None, K=0, rank=0,
                 lam=1.0, lam_fe=0.01, seed=0):
    """Logistic model on exposed pairs:
       logit p = c0 + alpha_u + beta_i [+ gamma[cu, ci]] [+ P_u . Q_i].
    Penalized mean log-loss, L-BFGS. Returns a parameter dict."""
    n = len(y)
    y = y.astype(float)
    use_cls = cu is not None
    G = K if use_cls else 0
    sizes = [1, U, I, G * G, U * rank, I * rank]
    offs = np.cumsum([0] + sizes)
    rng = np.random.default_rng(seed)
    x0 = np.zeros(offs[-1])
    if rank:
        x0[offs[4]:offs[6]] = rng.normal(0, 0.1, U * rank + I * rank)
    x0[0] = np.log(y.mean() / (1 - y.mean() + 1e-12) + 1e-12)
    if use_cls:
        pair = cu[users] * G + ci[items]

    def unpack(x):
        c0 = x[0]
        al = x[offs[1]:offs[2]]
        be = x[offs[2]:offs[3]]
        ga = x[offs[3]:offs[4]]
        P = x[offs[4]:offs[5]].reshape(U, rank)
        Q = x[offs[5]:offs[6]].reshape(I, rank)
        return c0, al, be, ga, P, Q

    def f(x):
        c0, al, be, ga, P, Q = unpack(x)
        z = c0 + al[users] + be[items]
        if use_cls:
            z = z + ga[pair]
        if rank:
            z = z + np.einsum("nr,nr->n", P[users], Q[items])
        pz = sigmoid(z)
        loss = np.mean(np.logaddexp(0, z) - y * z)
        r = pz - y
        g = np.zeros_like(x)
        g[0] = r.mean()
        g[offs[1]:offs[2]] = np.bincount(users, r, U) / n
        g[offs[2]:offs[3]] = np.bincount(items, r, I) / n
        if use_cls:
            g[offs[3]:offs[4]] = np.bincount(pair, r, G * G) / n
        if rank:
            gP = np.zeros((U, rank)); gQ = np.zeros((I, rank))
            np.add.at(gP, users, r[:, None] * Q[items])
            np.add.at(gQ, items, r[:, None] * P[users])
            g[offs[4]:offs[5]] = gP.ravel() / n
            g[offs[5]:offs[6]] = gQ.ravel() / n
        # penalties (scaled per observation)
        sc = 1.0 / n
        fe = np.concatenate([al, be, ga])
        loss += sc * (lam_fe * fe @ fe + lam * (P.ravel() @ P.ravel() + Q.ravel() @ Q.ravel()))
        g[offs[1]:offs[4]] += sc * 2 * lam_fe * fe
        g[offs[4]:offs[6]] += sc * 2 * lam * x[offs[4]:offs[6]]
        return loss, g

    res = minimize(f, x0, jac=True, method="L-BFGS-B", options=dict(maxiter=500))
    c0, al, be, ga, P, Q = unpack(res.x)
    return dict(c0=c0, al=al, be=be, ga=ga, P=P, Q=Q, cu=cu, ci=ci, K=G, rank=rank)


def predict_logistic(mdl, users, items):
    z = mdl["c0"] + mdl["al"][users] + mdl["be"][items]
    if mdl["cu"] is not None:
        z = z + mdl["ga"][mdl["cu"][users] * mdl["K"] + mdl["ci"][items]]
    if mdl["rank"]:
        z = z + np.einsum("nr,nr->n", mdl["P"][users], mdl["Q"][items])
    return z


def mean_loglik(z, y):
    return float(np.mean(y * z - np.logaddexp(0, z)))


def closure_score(ll_deg, ll_cls, ll_item):
    """Share of the item-level model's gain over the degree-only model that
    the class-level model keeps. 1: the classes carry all of it; 0: none."""
    den = ll_item - ll_deg
    return float((ll_cls - ll_deg) / den) if den > 1e-6 else float("nan")


def poisson_gain(Ctrain, Ctest, lu, li, K):
    """Unconditional test on raw counts (exposure not conditioned on): the
    degree-corrected block model's Poisson log-likelihood per user-item cell
    on the test counts, minus the degree-only model's, in millinats."""
    tot = Ctest.sum()
    du, di = Ctrain.sum(1), Ctrain.sum(0)
    E0 = np.outer(du, di) / Ctrain.sum()
    om = block_rates(Ctrain, lu, li, K)
    E1 = np.outer(du, di) * om[lu][:, li]
    out = []
    for E in (E0, E1):
        E = E * tot / E.sum()
        E = np.maximum(E, 1e-3 * tot / E.size)
        E = E * tot / E.sum()
        out.append(float(np.mean(Ctest * np.log(E) - E)))
    return 1000 * (out[1] - out[0])


# -------------------------------------------------------- run

def counts(X, Y, U, I):
    C = np.zeros((U, I))
    np.add.at(C, (np.repeat(np.arange(U), X.shape[1]), X.ravel()), Y.ravel())
    return C


def pairs(X):
    U, m = X.shape
    return np.repeat(np.arange(U), m), X.ravel()


def probe(st, p, rng):
    """Uniform random exposure, m_probe per user; changes nothing."""
    U, I = len(st["u"]), len(st["v"])
    X = sample_exposure(np.ones((U, I)), p["m_probe"], rng)
    return X, engage(st, p, X, rng)


def separation_r2(vecs, labels):
    """Between-class share of the variance of true preference vectors."""
    tot = ((vecs - vecs.mean(0)) ** 2).sum()
    btw = 0.0
    for c in np.unique(labels):
        g = vecs[labels == c]
        btw += len(g) * ((g.mean(0) - vecs.mean(0)) ** 2).sum()
    return float(btw / tot)


def evaluate(st, p, arm, cls, hist, pop_counts, rng, controls=None):
    """All measures at one time point. `hist` holds the last periods'
    (X, Y) under the arm's policy."""
    U, I, K = len(st["u"]), len(st["v"]), p["K"]
    icls = item_classes(st, cls)
    ucls = cls["user"]
    tgt = cls["target"]
    out = {}
    # observational concentration: share of engagements (policy data) in the
    # user's target class
    Xl, Yl = hist[-1]
    inside = icls[Xl] == tgt[ucls][:, None]
    out["concentration"] = float((Yl & inside).sum() / max(Yl.sum(), 1))
    out["yield"] = float(Yl.mean())
    # probes: two folds of uniform random exposure
    XA, YA = probe(st, p, rng)
    XB, YB = probe(st, p, rng)
    insB = icls[XB] == tgt[ucls][:, None]
    rin = np.array([YB[u][insB[u]].mean() if insB[u].any() else np.nan for u in range(U)])
    rout = np.array([YB[u][~insB[u]].mean() if (~insB[u]).any() else np.nan for u in range(U)])
    out["probe_gap"] = float(np.nanmean(rin - rout))
    out["probe_rate"] = float(YB.mean())
    # conditional closure: train on policy history + probe A; test on probe B
    # (changed exposure) and on a fresh policy draw (same exposure regime)
    tr_u, tr_i, tr_y = [], [], []
    for X, Y in list(hist) + [(XA, YA)]:
        uu, ii = pairs(X); tr_u.append(uu); tr_i.append(ii); tr_y.append(Y.ravel())
    tr_u, tr_i, tr_y = map(np.concatenate, (tr_u, tr_i, tr_y))
    wpol = policy_weights(st, p, arm, cls, pop_counts)
    XP = sample_exposure(wpol, p["m"], rng)
    YP = engage(st, p, XP, rng)
    tests = dict(probe=(pairs(XB), YB.ravel()), policy=(pairs(XP), YP.ravel()))
    m_deg = fit_logistic(tr_u, tr_i, tr_y, U, I)
    m_itm = fit_logistic(tr_u, tr_i, tr_y, U, I, rank=p["d"], lam=p["lam_item"])
    parts = dict(genre=(ucls, icls))
    if controls:
        parts.update(controls)
    for name, (cu, ci) in parts.items():
        m_cls = fit_logistic(tr_u, tr_i, tr_y, U, I, cu=cu, ci=ci, K=K)
        for tname, ((tu, ti), ty) in tests.items():
            lls = [mean_loglik(predict_logistic(m, tu, ti), ty) for m in (m_deg, m_cls, m_itm)]
            out[f"closure_{tname}_{name}"] = closure_score(*lls)
            out[f"defect_{tname}_{name}"] = lls[2] - lls[1]
    # unconditional closure on raw counts: train = history, test = fresh policy draw
    Ctr = sum(counts(X, Y, U, I) for X, Y in hist)
    Cte = counts(XP, YP, U, I)
    for name, (cu, ci) in parts.items():
        out[f"rawgain_{name}"] = poisson_gain(Ctr, Cte, cu, ci, K)
    # ground truth
    out["truth_r2_users"] = separation_r2(st["u"], ucls)
    out["truth_r2_items"] = separation_r2(st["v"], icls)
    # disagreement in true preference: mean within-class spread of users
    out["truth_spread_users"] = float(np.mean([st["u"][ucls == c].var(0).sum()
                                               for c in range(K) if (ucls == c).any()]))
    # true in-class minus out-of-class engagement probability, all pairs
    P = sigmoid(p["a"] + p["b"] * st["u"] @ st["v"].T + st["beta"][None, :])
    insA = icls[None, :] == tgt[ucls][:, None]
    out["truth_gap"] = float(np.mean([P[u][insA[u]].mean() - P[u][~insA[u]].mean()
                                      for u in range(U) if insA[u].any() and (~insA[u]).any()]))
    return out


ARMS = ["inferred", "inferred+adapt", "used", "used+adapt", "popular+adapt"]


def run(world, arm, seed, p=None):
    p = dict(DEFAULTS, **(p or {}))
    rng = np.random.default_rng([seed, ["taste", "exposure"].index(world)])
    st = make_world(world, rng, p)
    U, I, K = p["U"], p["I"], p["K"]
    # burn-in under the base policy
    hist = []
    for _ in range(p["burn"]):
        X = sample_exposure(base_weights(st, p), p["m"], rng)
        hist.append((X, engage(st, p, X, rng)))
    C0 = sum(counts(X, Y, U, I) for X, Y in hist)
    E0 = sum(counts(X, np.ones_like(Y), U, I) for X, Y in hist)
    cls = make_classes(C0, K, rng)
    # control partitions: popularity (size-matched) and exposure co-clusters
    usz = np.bincount(cls["user"], minlength=K)
    isz = np.bincount(cls["item"], minlength=K)
    pop_u = size_matched_partition(C0.sum(1), usz)
    pop_i = size_matched_partition(C0.sum(0), isz)
    eu, ei = spectral_coclusters(E0, K, rng)
    controls = dict(popularity=(pop_u, pop_i), exposure=(eu, ei))
    # a variant inference conditioned on exposure: co-clusters of the residual
    # of engagement given exposure under the degree model
    rate_u = C0.sum(1) / np.maximum(E0.sum(1), 1)
    rate_i = C0.sum(0) / np.maximum(E0.sum(0), 1)
    resid = C0 - E0 * np.outer(rate_u, rate_i) / max(C0.sum() / E0.sum(), 1e-9)
    Ur, sr, Vr = np.linalg.svd(resid, full_matrices=False)
    cu_c = _kmeans(Ur[:, :K - 1] * sr[:K - 1], K, rng)
    ci_c = _kmeans(Vr[:K - 1].T * sr[:K - 1], K, rng)
    controls["conditional"] = (cu_c, ci_c)
    pop_counts = C0.sum(0)
    rec = dict(world=world, arm=arm, seed=seed)
    rec["ari_true_users"] = ari(cls["user"], st["true_u"])
    rec["ari_true_items"] = ari(cls["item"], st["true_i"])
    rec["ari_cond_true_users"] = ari(cu_c, st["true_u"])
    rec["ari_exposure_true_users"] = ari(eu, st["true_u"])
    ev0 = evaluate(st, p, arm, cls, hist, pop_counts, rng, controls)
    hist = hist[-p["burn"]:]
    for t in range(p["T"]):
        w = policy_weights(st, p, arm, cls, pop_counts)
        X = sample_exposure(w, p["m"], rng)
        Y = engage(st, p, X, rng)
        hist = (hist + [(X, Y)])[-p["burn"]:]
        pop_counts = np.bincount(X.ravel()[Y.ravel()], minlength=I).astype(float)
        if arm.endswith("adapt"):
            adapt(st, p, X, Y, rng, cls)
    ev1 = evaluate(st, p, arm, cls, hist, pop_counts, rng, None)
    # stability: classes re-inferred from the end data against the start's
    Cend = sum(counts(X, Y, U, I) for X, Y in hist)
    lu2, li2 = spectral_coclusters(Cend, K, rng)
    rec["stability_users"] = ari(lu2, cls["user"])
    rec["stability_items"] = ari(li2, item_classes(st, cls))
    rec["start"], rec["end"] = ev0, ev1
    return rec
