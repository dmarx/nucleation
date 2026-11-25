"""LEAD-157: permutation alignment and loss barriers over several path families.

Small two-hidden-layer ReLU MLPs in numpy. Parameters are a list
[W1 (h,d), b1 (h), W2 (h,h), b2 (h), W3 (K,h), b3 (K)].
"""
import itertools

import numpy as np
from scipy.optimize import linear_sum_assignment

D_IN, K = 16, 4
A_DIMS = slice(0, 4)
B_DIMS = slice(4, 8)


# ---------------------------------------------------------------- data
def make_task(seed=0, m=3, sep=2.0):
    """Cluster centres for the two cues: each class has m centres per cue."""
    r = np.random.default_rng(seed)
    return {"A": r.normal(0, sep, (K, m, 4)), "B": r.normal(0, sep, (K, m, 4)),
            "m": m}


def sample(task, n, mode, seed, noise=0.6):
    """mode: 'both' (both cues carry y), 'A' (cue B scrambled), 'B' (cue A scrambled)."""
    r = np.random.default_rng(seed)
    y = r.integers(0, K, n)
    X = r.normal(0, 1.0, (n, D_IN))
    for cue, dims in (("A", A_DIMS), ("B", B_DIMS)):
        informative = mode == "both" or mode == cue
        cls = y if informative else r.integers(0, K, n)
        c = r.integers(0, task["m"], n)
        X[:, dims] = task[cue][cls, c] + r.normal(0, noise, (n, 4))
    return X, y


# ---------------------------------------------------------------- model
def init(h, seed):
    r = np.random.default_rng(seed)
    he = lambda o, i: r.normal(0, np.sqrt(2.0 / i), (o, i))
    return [he(h, D_IN), np.zeros(h), he(h, h), np.zeros(h),
            r.normal(0, np.sqrt(1.0 / h), (K, h)), np.zeros(K)]


def forward(p, X, keep=False):
    W1, b1, W2, b2, W3, b3 = p
    z1 = X @ W1.T + b1
    a1 = np.maximum(z1, 0)
    z2 = a1 @ W2.T + b2
    a2 = np.maximum(z2, 0)
    out = a2 @ W3.T + b3
    return (out, (z1, a1, z2, a2)) if keep else out


def ce(logits, y):
    m = logits.max(1, keepdims=True)
    lse = np.log(np.exp(logits - m).sum(1)) + m[:, 0]
    return float(np.mean(lse - logits[np.arange(len(y)), y]))


def loss_err(p, X, y):
    o = forward(p, X)
    return ce(o, y), float(np.mean(o.argmax(1) != y))


def grad(p, X, y, wd=0.0):
    W1, b1, W2, b2, W3, b3 = p
    out, (z1, a1, z2, a2) = forward(p, X, keep=True)
    n = len(y)
    pr = np.exp(out - out.max(1, keepdims=True))
    pr /= pr.sum(1, keepdims=True)
    pr[np.arange(n), y] -= 1
    d3 = pr / n
    gW3, gb3 = d3.T @ a2, d3.sum(0)
    d2 = (d3 @ W3) * (z2 > 0)
    gW2, gb2 = d2.T @ a1, d2.sum(0)
    d1 = (d2 @ W2) * (z1 > 0)
    gW1, gb1 = d1.T @ X, d1.sum(0)
    g = [gW1, gb1, gW2, gb2, gW3, gb3]
    if wd:
        for i in (0, 2, 4):
            g[i] = g[i] + wd * p[i]
    return g


def train(p, X, y, lr=0.05, batch=64, epochs=30, mom=0.9, wd=1e-4, seed=0):
    r = np.random.default_rng(seed)
    p = [a.copy() for a in p]
    v = [np.zeros_like(a) for a in p]
    n = len(y)
    for _ in range(epochs):
        idx = r.permutation(n)
        for s in range(0, n - batch + 1, batch):
            b = idx[s:s + batch]
            g = grad(p, X[b], y[b], wd)
            for i in range(6):
                v[i] = mom * v[i] + g[i]
                p[i] -= lr * v[i]
    return p


# ---------------------------------------------------------------- symmetries
def permute(p, p1, p2):
    """Unit i of the result's layer l is unit p_l[i] of p."""
    W1, b1, W2, b2, W3, b3 = p
    return [W1[p1], b1[p1], W2[p2][:, p1], b2[p2], W3[:, p2], b3.copy()]


def rescale(p, d1, d2):
    """ReLU positive rescaling: function-preserving for d > 0."""
    W1, b1, W2, b2, W3, b3 = p
    W1n, b1n = W1 * d1[:, None], b1 * d1
    W2n = W2 / d1[None, :] * d2[:, None]
    b2n = b2 * d2
    W3n = W3 / d2[None, :]
    return [W1n, b1n, W2n, b2n, W3n, b3.copy()]


def canonical(p):
    """Quotient ReLU rescaling: each hidden unit's incoming weights+bias get unit norm."""
    W1, b1 = p[0], p[1]
    s1 = np.sqrt((W1 ** 2).sum(1) + b1 ** 2) + 1e-12
    q = rescale(p, 1 / s1, np.ones(len(b1)))
    s2 = np.sqrt((q[2] ** 2).sum(1) + q[3] ** 2) + 1e-12
    return rescale(q, np.ones(len(b1)), 1 / s2)


def _lap_max(S):
    r, c = linear_sum_assignment(S, maximize=True)
    out = np.empty(len(r), int)
    out[r] = c
    return out


def weight_match(pa, pb, iters=30, seed=0):
    """Ainsworth et al.-style coordinate descent; returns pb permuted onto pa."""
    h = len(pa[1])
    p1, p2 = np.arange(h), np.arange(h)
    r = np.random.default_rng(seed)
    W1a, b1a, W2a, b2a, W3a, _ = pa
    W1b, b1b, W2b, b2b, W3b, _ = pb
    for _ in range(iters):
        changed = False
        for layer in r.permutation(2):
            if layer == 0:
                S = W1a @ W1b.T + np.outer(b1a, b1b) + W2a.T @ W2b[p2]
                new = _lap_max(S)
                if not np.array_equal(new, p1):
                    p1, changed = new, True
            else:
                S = W2a @ W2b[:, p1].T + np.outer(b2a, b2b) + W3a.T @ W3b
                new = _lap_max(S)
                if not np.array_equal(new, p2):
                    p2, changed = new, True
        if not changed:
            break
    return permute(pb, p1, p2)


def _corr(A, B):
    A = (A - A.mean(0)) / (A.std(0) + 1e-8)
    B = (B - B.mean(0)) / (B.std(0) + 1e-8)
    return A.T @ B / len(A)


def act_match(pa, pb, X):
    """Match units by correlation of post-ReLU activations, layer by layer."""
    _, (_, a1a, _, a2a) = forward(pa, X, keep=True)
    _, (_, a1b, _, a2b) = forward(pb, X, keep=True)
    p1 = _lap_max(_corr(a1a, a1b))
    p2 = _lap_max(_corr(a2a, a2b))
    return permute(pb, p1, p2)


def feature_corr(pa, pb, X):
    """Mean matched-unit activation correlation per hidden layer (pb already aligned)."""
    _, (_, a1a, _, a2a) = forward(pa, X, keep=True)
    _, (_, a1b, _, a2b) = forward(pb, X, keep=True)
    return [float(np.mean(np.diag(_corr(a, b)))) for a, b in ((a1a, a1b), (a2a, a2b))]


def brute_force_match(pa, pb, X, y):
    """Exact best permutation pair for the mean linear-path loss at t = 1/4, 1/2, 3/4
    (small widths only)."""
    h = len(pa[1])
    best, arg = np.inf, None
    perms = [np.array(q) for q in itertools.permutations(range(h))]
    for p1 in perms:
        for p2 in perms:
            L = _path_loss(pa, permute(pb, p1, p2), X, y)
            if L < best:
                best, arg = L, (p1, p2)
    return permute(pb, *arg)


def align(method, pa, pb, X):
    """Return (endpoint A, endpoint B) after alignment."""
    if method == "none":
        return pa, pb
    if method == "wm":
        return pa, weight_match(pa, pb)
    if method == "am":
        return pa, act_match(pa, pb, X)
    if method == "swm":  # quotient rescaling, then weight-match: the full ReLU-MLP group
        ca, cb = canonical(pa), canonical(pb)
        return ca, weight_match(ca, cb)
    raise ValueError(method)


# ---------------------------------------------------------------- paths
def point(family, pa, pb, pm, t):
    if family == "linear":
        return [(1 - t) * a + t * b for a, b in zip(pa, pb)]
    if family == "bezier":
        return [(1 - t) ** 2 * a + 2 * t * (1 - t) * m + t ** 2 * b
                for a, m, b in zip(pa, pm, pb)]
    if family == "polychain":
        if t <= 0.5:
            s = 2 * t
            return [(1 - s) * a + s * m for a, m in zip(pa, pm)]
        s = 2 * t - 1
        return [(1 - s) * m + s * b for m, b in zip(pm, pb)]
    raise ValueError(family)


def coef(family, t):
    """d point / d control."""
    if family == "bezier":
        return 2 * t * (1 - t)
    return 2 * t if t <= 0.5 else 2 * (1 - t)


def fit_curve(family, pa, pb, X, y, steps=500, batch=128, lr=0.01, seed=0):
    """Train the bend with Adam on E_t L(point(t)), t ~ U(0,1)."""
    r = np.random.default_rng(seed)
    pm = [(a + b) / 2 for a, b in zip(pa, pb)]
    m1 = [np.zeros_like(a) for a in pm]
    m2 = [np.zeros_like(a) for a in pm]
    for k in range(1, steps + 1):
        t = r.uniform()
        b = r.integers(0, len(y), batch)
        g = grad(point(family, pa, pb, pm, t), X[b], y[b])
        c = coef(family, t)
        for i in range(6):
            gi = c * g[i]
            m1[i] = 0.9 * m1[i] + 0.1 * gi
            m2[i] = 0.999 * m2[i] + 0.001 * gi ** 2
            pm[i] -= lr * (m1[i] / (1 - 0.9 ** k)) / (np.sqrt(m2[i] / (1 - 0.999 ** k)) + 1e-8)
    return pm


def barrier(family, pa, pb, pm, X, y, n_t=25):
    """Max over t of L(t) minus the linear interpolation of the endpoint values,
    for loss and error. Returns dict."""
    ts = np.linspace(0, 1, n_t)
    vals = np.array([loss_err(point(family, pa, pb, pm, t), X, y) for t in ts])
    base = (1 - ts)[:, None] * vals[0] + ts[:, None] * vals[-1]
    gap = vals - base
    return {"loss_barrier": float(gap[:, 0].max()), "err_barrier": float(gap[:, 1].max()),
            "loss_curve": [round(float(v), 4) for v in vals[:, 0]],
            "end_loss": [float(vals[0, 0]), float(vals[-1, 0])]}


# ---------------------------------------------------------------- local curvature
def flat(p):
    return np.concatenate([a.ravel() for a in p])


def unflat(v, like):
    out, i = [], 0
    for a in like:
        out.append(v[i:i + a.size].reshape(a.shape))
        i += a.size
    return out


def top_hessian_eig(p, X, y, iters=30, eps=1e-3, seed=0):
    """Power iteration with finite-difference Hessian-vector products."""
    r = np.random.default_rng(seed)
    th = flat(p)
    v = r.normal(size=th.size)
    v /= np.linalg.norm(v)
    lam = 0.0
    for _ in range(iters):
        gp = flat(grad(unflat(th + eps * v, p), X, y))
        gm = flat(grad(unflat(th - eps * v, p), X, y))
        hv = (gp - gm) / (2 * eps)
        lam = float(v @ hv)
        v = hv / (np.linalg.norm(hv) + 1e-12)
    return lam


# ---------------------------------------------------------------- mechanism test
def cue_reliance(p, task, n=2000, seed=999):
    """Independent test of mechanism: accuracy when only cue A, or only cue B, carries y."""
    XA, yA = sample(task, n, "A", seed)
    XB, yB = sample(task, n, "B", seed + 1)
    return {"acc_A_only": 1 - loss_err(p, XA, yA)[1], "acc_B_only": 1 - loss_err(p, XB, yB)[1]}


def _path_loss(pa, pb, X, y, ts=(0.25, 0.5, 0.75)):
    """Mean loss at interior points of the linear path (endpoint losses are fixed
    under the group, so this is the barrier objective up to a constant)."""
    return float(np.mean([ce(forward([(1 - t) * a + t * b for a, b in zip(pa, pb)], X), y)
                          for t in ts]))


def full_group_search(pa, pb, X, y):
    """Search the full ReLU-MLP group for the linear path: exact best permutation pair
    (brute force over all h!^2, on raw and on canonical weights) for the mean loss
    at t = 1/4, 1/2, 3/4, then per-unit positive rescaling of pb optimised by
    L-BFGS from there. Small widths only. Returns (pa', pb')."""
    from scipy.optimize import minimize
    h = len(pa[1])
    cands = []
    for ea, eb in ((pa, pb), (canonical(pa), canonical(pb))):
        q = brute_force_match(ea, eb, X, y)
        f = lambda z, ea=ea, q=q: _path_loss(ea, rescale(q, np.exp(z[:h]), np.exp(z[h:])), X, y)
        res = minimize(f, np.zeros(2 * h), method="L-BFGS-B",
                       bounds=[(-3, 3)] * (2 * h))
        cands.append((res.fun, ea, rescale(q, np.exp(res.x[:h]), np.exp(res.x[h:]))))
    best = min(cands, key=lambda c: c[0])
    return best[1], best[2]


def llfc_cos(pa, pb, X, t=0.5):
    """Linear layerwise feature connectivity (THEORY-111's measure): mean cosine
    between the path point's hidden features and the interpolation of the
    endpoints' features, per hidden layer."""
    pt = [(1 - t) * a + t * b for a, b in zip(pa, pb)]
    _, (_, a1a, _, a2a) = forward(pa, X, keep=True)
    _, (_, a1b, _, a2b) = forward(pb, X, keep=True)
    _, (_, a1t, _, a2t) = forward(pt, X, keep=True)
    out = []
    for ha, hb, ht in ((a1a, a1b, a1t), (a2a, a2b, a2t)):
        mix = (1 - t) * ha + t * hb
        num = (mix * ht).sum(1)
        den = np.linalg.norm(mix, axis=1) * np.linalg.norm(ht, axis=1)
        ok = den > 1e-12
        out.append(float(np.mean(num[ok] / den[ok])) if ok.any() else float("nan"))
    return out
