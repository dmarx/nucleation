"""Northstar priced: a will-organization model against control-only models.

LEAD-089. Episodes of a fictional company (CASE-023) decide which of three
regimes becomes effective: 0 routine deployment, 1 cautious verification,
2 emergency suspension.

Context x = (o, r, b), three bits:
    o  an authorized reliability specialist objects
    r  an incident signal is present
    b  the release is flagged business-critical
Arrangement of authority a = (s, j, v), three bits (CASE-003, CASE-002):
    s  an objection suspends deployment pending review (Northstar-A) or not (B)
    j  severity is classified by an independent reliability group (1) or by
       the product team (0)
    v  senior management may override a freeze for a business-critical release

Indices: x = 4*o + 2*r + b, a = 4*s + 2*j + v.  Counts are n[x, a, y].

Models
------
WO   will-organization: the regimes' proposals are fixed, and maintained
     relations (precedence of a severe classification, jurisdiction over
     classification, suspension by objection, an override) decide which
     becomes effective. Four parameters: q0, q1 (how readily the product
     team and the reliability group classify a signal severe), m (how often
     senior management orders verification under B), eps (execution noise).
C0   controller blind to authority: P(y | x), Dirichlet(1,1,1) per context.
C1   saturated metacontrol lookup: P(y | x, a), Dirichlet(1,1,1) per cell.
C2   metacontrol gate: softmax over regimes, values linear in (1, x, a).
C3   C2 plus every pairwise product within x and between x and a.
C4   a gate saturated in the context, each authority bit modulating each
     context separately: one-hot x, and one-hot x times s, j and v (32
     features), with no product of two authority bits.

Evidence (log marginal likelihood) is exact for C0 and C1, by quadrature for
WO, and by Laplace's approximation for C2 and C3 (regular, Gaussian prior).
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln, logsumexp

NX, NA, NY = 8, 8, 3


def bits(i):
    return (i >> 2) & 1, (i >> 1) & 1, i & 1


# ---------------------------------------------------------------- WO model

def wo_table(q0, q1, m, eps):
    """P(y | x, a) under the will-organization relations. Vectorized: the
    parameters may be arrays of one shape S; the result is S + (8, 8, 3)."""
    q0, q1, m, eps = (np.asarray(t, float) for t in (q0, q1, m, eps))
    S = np.broadcast(q0, q1, m, eps).shape
    P = np.zeros(S + (NX, NA, NY))
    for x in range(NX):
        o, r, b = bits(x)
        for a in range(NA):
            s, j, v = bits(a)
            q = q1 if j else q0
            sev = r * q                       # severe classification
            p = np.zeros(S + (NY,))
            # precedence: a severe classification freezes deployment,
            # unless the override is held and the release is business-critical
            if v and b:
                p[..., 0] += sev
            else:
                p[..., 2] += sev
            ns = 1.0 - sev
            if o:
                if s:                          # objection suspends: verify
                    p[..., 1] += ns
                else:                          # B: only if senior orders it
                    p[..., 1] += ns * m
                    p[..., 0] += ns * (1.0 - m)
            else:
                p[..., 0] += ns
            P[..., x, a, :] = (1.0 - eps)[..., None] * p + eps[..., None] / NY
    return P


EPS_MAX = 0.5


def gl_nodes(G, lo, hi):
    t, w = np.polynomial.legendre.leggauss(G)
    return lo + (hi - lo) * (t + 1) / 2, w * (hi - lo) / 2


def wo_posterior(n, G=16):
    """Log evidence and posterior predictive table for WO under uniform
    priors: q0, q1, m on (0, 1), eps on (0, EPS_MAX). Tensor Gauss-Legendre
    quadrature with G nodes per dimension."""
    u, wu = gl_nodes(G, 0.0, 1.0)
    e, we = gl_nodes(G, 0.0, EPS_MAX)
    logprior_density = -np.log(EPS_MAX)
    Q1, M, E = np.meshgrid(u, u, e, indexing="ij")
    W3 = (wu[:, None, None] * wu[None, :, None] * we[None, None, :])
    logs, preds = [], []
    for i, q0 in enumerate(u):
        P = wo_table(np.full_like(Q1, q0), Q1, M, E)            # G,G,G,8,8,3
        ll = (n * np.log(P)).sum(axis=(-3, -2, -1))
        lw = ll + np.log(W3 * wu[i]) + logprior_density
        logs.append(lw)
        preds.append(P)
    lw = np.stack(logs)                                         # G^4
    logZ = logsumexp(lw)
    post = np.exp(lw - logZ)
    pred = np.zeros((NX, NA, NY))
    for i in range(G):
        pred += np.tensordot(post[i], preds[i], axes=([0, 1, 2], [0, 1, 2]))
    return float(logZ), pred


# ------------------------------------------------------- Dirichlet models

def dirichlet_cells(counts, alpha=1.0):
    """counts: (..., NY). Exact log evidence summed over cells and the
    posterior-mean table."""
    k = counts.shape[-1]
    nc = counts.sum(-1)
    le = (gammaln(k * alpha) - gammaln(k * alpha + nc)
          + (gammaln(alpha + counts) - gammaln(alpha)).sum(-1)).sum()
    pred = (alpha + counts) / (k * alpha + nc)[..., None]
    return float(le), pred


def c0(n):
    le, pred = dirichlet_cells(n.sum(axis=1))
    return le, np.repeat(pred[:, None, :], NA, axis=1)


def c1(n):
    return dirichlet_cells(n)


# ---------------------------------------------------------- logistic gates

def features(kind):
    """Feature matrix Phi[x, a, d] for gate C2, C3 or C4."""
    if kind == "C4":
        Phi = np.zeros((NX, NA, 4 * NX))
        names = [f"x{x}" for x in range(NX)] + [f"x{x}*{c}" for c in "sjv" for x in range(NX)]
        for x in range(NX):
            for a in range(NA):
                Phi[x, a, x] = 1.0
                for i, bit in enumerate(bits(a)):
                    Phi[x, a, NX * (i + 1) + x] = bit
        return Phi, names
    rows = np.zeros((NX, NA), dtype=object)
    names = None
    for x in range(NX):
        xb = bits(x)
        for a in range(NA):
            ab = bits(a)
            f = {"1": 1.0}
            for nm, val in zip("orb", xb):
                f[nm] = val
            for nm, val in zip("sjv", ab):
                f[nm] = val
            if kind == "C3":
                for (n1, v1), (n2, v2) in itertools.combinations(zip("orb", xb), 2):
                    f[n1 + n2] = v1 * v2
                for (n1, v1), (n2, v2) in itertools.product(zip("orb", xb), zip("sjv", ab)):
                    f[n1 + n2] = v1 * v2
            rows[x, a] = f
            names = list(f)
    Phi = np.array([[[rows[x, a][k] for k in names] for a in range(NA)]
                    for x in range(NX)], float)
    return Phi, names


def _gate_probs(Wflat, Phi):
    d = Phi.shape[-1]
    W = Wflat.reshape(NY - 1, d)
    z = np.concatenate([np.zeros(Phi.shape[:2] + (1,)), Phi @ W.T], axis=-1)
    z -= z.max(-1, keepdims=True)
    p = np.exp(z)
    return p / p.sum(-1, keepdims=True)


def gate_fit(n, Phi, sigma=2.0, ndraw=400, rng=None):
    """MAP, Laplace log evidence and Laplace posterior predictive for a
    multinomial logistic gate with reference regime 0 and N(0, sigma^2)
    weights."""
    d = Phi.shape[-1]
    k = (NY - 1) * d
    X = Phi.reshape(-1, d)
    N = n.reshape(-1, NY)
    nc = N.sum(1)

    def f(w):
        W = w.reshape(NY - 1, d)
        z = np.concatenate([np.zeros((X.shape[0], 1)), X @ W.T], axis=1)
        lse = logsumexp(z, axis=1)
        ll = (N * z).sum() - (nc * lse).sum()
        p = np.exp(z - lse[:, None])
        g = ((N[:, 1:] - nc[:, None] * p[:, 1:]).T @ X).ravel()
        val = -ll + 0.5 * (w @ w) / sigma**2
        return val, -g + w / sigma**2

    res = minimize(f, np.zeros(k), jac=True, method="L-BFGS-B",
                   options={"maxiter": 5000, "gtol": 1e-9})
    w = res.x
    # Hessian of the negative log posterior
    W = w.reshape(NY - 1, d)
    z = np.concatenate([np.zeros((X.shape[0], 1)), X @ W.T], axis=1)
    p = np.exp(z - logsumexp(z, axis=1)[:, None])[:, 1:]
    H = np.zeros((k, k))
    for c1_ in range(NY - 1):
        for c2_ in range(NY - 1):
            wgt = nc * (p[:, c1_] * ((c1_ == c2_) - p[:, c2_]))
            H[c1_ * d:(c1_ + 1) * d, c2_ * d:(c2_ + 1) * d] = (X * wgt[:, None]).T @ X
    H += np.eye(k) / sigma**2
    sign, logdet = np.linalg.slogdet(H)
    assert sign > 0
    negpost = res.fun
    log_prior_norm = -0.5 * k * np.log(2 * np.pi * sigma**2)
    # ln p(D) ~ ln p(D|w) + ln p(w) + k/2 ln 2pi - 1/2 ln det H
    le = -negpost + log_prior_norm + 0.5 * k * np.log(2 * np.pi) - 0.5 * logdet
    rng = np.random.default_rng(0) if rng is None else rng
    L = np.linalg.cholesky(np.linalg.inv(H))
    draws = w + rng.standard_normal((ndraw, k)) @ L.T
    pred = np.mean([_gate_probs(dw, Phi) for dw in draws], axis=0)
    return float(le), pred, w


# ------------------------------------------------------------------ worlds

P_CTX = (0.3, 0.3, 0.3)                       # P(o), P(r), P(b)


def context_probs():
    px = np.zeros(NX)
    for x in range(NX):
        px[x] = np.prod([p if bit else 1 - p for p, bit in zip(P_CTX, bits(x))])
    return px


def world_table(world, rng):
    """True P(y | x, a) for one seed of a world."""
    if world == "governed":
        th = (rng.uniform(0.1, 0.6), rng.uniform(0.6, 0.95),
              rng.uniform(0.0, 0.4), rng.uniform(0.01, 0.1))
        return wo_table(*th), {"theta": [float(t) for t in th]}
    if world == "idle":                       # CLAIM-089's surviving case
        t = rng.dirichlet(np.ones(NY), size=NX)
        return np.repeat(t[:, None, :], NA, axis=1), {}
    if world == "idiosyncratic":
        return rng.dirichlet(np.ones(NY), size=(NX, NA)), {}
    if world == "interacting":
        # the same relations, except that where classification lies with the
        # reliability group, that group takes objections over and an
        # objection no longer suspends by itself (s is idle when j = 1)
        th = (rng.uniform(0.1, 0.6), rng.uniform(0.6, 0.95),
              rng.uniform(0.0, 0.4), rng.uniform(0.01, 0.1))
        P = wo_table(*th)
        for a in range(NA):
            s, j, v = bits(a)
            if s and j:
                P[:, a, :] = P[:, a - 4, :]   # behaves as s = 0
        return P, {"theta": [float(t) for t in th]}
    raise ValueError(world)


TRAIN_A = [0b000, 0b100, 0b010, 0b001]      # baseline and each single change
TEST_A = [0b110, 0b101, 0b011, 0b111]       # unseen combined interventions


def sample_counts(P, arrangements, n_per, rng):
    n = np.zeros((NX, NA, NY))
    px = context_probs()
    for a in arrangements:
        xs = rng.multinomial(n_per, px)
        for x in range(NX):
            if xs[x]:
                n[x, a] += rng.multinomial(xs[x], P[x, a])
    return n


def log_pred(n_test, pred):
    return float((n_test * np.log(pred)).sum())
