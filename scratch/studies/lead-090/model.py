"""LEAD-090: CASE-092's coupled meaning-influence model, its linearization,
and the predecessor models it is compared with.

CASE-092 (as read here)
-----------------------
Two hypotheses A and B with comparable evidence in a fixed corpus (imbalance
b = 0 is CASE-092's balanced corpus; b != 0 is used only for hysteresis
sweeps). Two retrieval specialists j in {A, B}, s_A = +1, s_B = -1: the
A-specialist is better at finding A-evidence (specialization sigma).

State: p in [0, 1], the collective's weight on A (meaning; m = 2p - 1), and
w in [0, 1], the A-specialist's share of authority (influence; a = 2w - 1).

Each round:
  * Query framing set by the dominant interpretation, with exploration eps:
    the query is framed for A with probability q = (1 - eps) p + eps/2
    (frame f = +1 for A, -1 for B).
  * Each specialist retrieves k items from the corpus; an item supports A
    with probability pi_j = 1/2 + (b + s_j sigma + phi f)/2 (phi: framing
    effect). Requires |b| + sigma + phi <= 1.
  * Meaning: p <- (1 - rho) p + rho * sum_j w_j ehat_j  (ehat_j: share of
    j's items supporting A; authority pools the specialists' output).
  * Conferral from apparent retrieval success, score_j:
      Regime A, soft (default): agreement of j's items with an
        interpretation drawn from the current meaning distribution,
        score_j = p ehat_j + (1 - p)(1 - ehat_j).
      Regime A, hard: share of j's items supporting the currently dominant
        hypothesis (argmax p).
      Regime B: independently assessed relevance, share of j's items that
        are relevant (prob r_j, the same for both under CASE-092's design).
  * Conferral rule (two readings of "updated from apparent retrieval
    success, with an adjustable memory timescale"):
      'ema'       : w <- delta w + (1 - delta) softmax(g * score)_A
                    (LEAD-081's convention; delta is the memory)
      'replicator': w_A <- w_A e^{eta s_A} / sum_j w_j e^{eta s_j}
                    (reflected-appraisal / Ito-Kaneko style reinforcement,
                    no memory parameter)

Mean-field reduced form (k -> infinity, frame averaged), in (m, a):
  m' = (1 - rho) m + rho (b + sigma a + phi (1 - eps) m)
  a' = delta a + (1 - delta) tanh(g sigma m / 2)          [A, soft, ema]
  a' = delta a + (1 - delta) tanh(g sigma sign(m) / 2)    [A, hard, ema]
  a' = delta a + (1 - delta) tanh(g (r_A - r_B) / 2)      [B, ema]
  a' = tanh(atanh(a) + eta sigma m / 2)                   [A, soft, replicator]
(the hard-scoring score difference is sigma*sign(m) only to first order in
the framing-independent part; mean_field() computes it exactly).
"""
from __future__ import annotations

import numpy as np

SIGNS = np.array([1.0, -1.0])  # s_A, s_B


# ------------------------------------------------------------ parameters
def default_params(**kw):
    p = dict(rho=0.2, sigma=0.4, phi=0.3, eps=0.2, b=0.0, g=8.0, delta=0.9,
             eta=0.8, regime="A", scoring="soft", conferral="ema",
             r=(0.7, 0.7), k=50)
    p.update(kw)
    assert abs(p["b"]) + p["sigma"] + p["phi"] <= 1 + 1e-12, "pi out of [0,1]"
    return p


def _softmax_share(z):
    """softmax over two scores, share of the first."""
    return 1.0 / (1.0 + np.exp(-(z[0] - z[1])))


# ------------------------------------------------------------ full model
def step_stochastic(p_, w, P, rng):
    """One round of the agent-level model. Returns (p', w')."""
    q = (1 - P["eps"]) * p_ + P["eps"] / 2
    f = 1.0 if rng.random() < q else -1.0
    pi = 0.5 + (P["b"] + SIGNS * P["sigma"] + P["phi"] * f) / 2
    ehat = rng.binomial(P["k"], pi) / P["k"]
    wv = np.array([w, 1 - w])
    p_new = (1 - P["rho"]) * p_ + P["rho"] * float(wv @ ehat)
    score = _score(p_, ehat, P, rng)
    w_new = _confer(w, score, P)
    return p_new, w_new


def _score(p_, ehat, P, rng=None):
    if P["regime"] == "B":
        r = np.asarray(P["r"], float)
        if rng is None:
            return r
        return rng.binomial(P["k"], r) / P["k"]
    if P["scoring"] == "soft":
        return p_ * ehat + (1 - p_) * (1 - ehat)
    if p_ > 0.5:
        return ehat
    if p_ < 0.5:
        return 1 - ehat
    return np.full(2, 0.5)


def _confer(w, score, P):
    if P["conferral"] == "ema":
        return P["delta"] * w + (1 - P["delta"]) * _softmax_share(P["g"] * score)
    # replicator
    num = w * np.exp(P["eta"] * score[0])
    return num / (num + (1 - w) * np.exp(P["eta"] * score[1]))


def simulate_stochastic(p0, w0, P, T, seed=0):
    rng = np.random.default_rng(seed)
    out = np.empty((T + 1, 2))
    out[0] = p0, w0
    p_, w = p0, w0
    for t in range(T):
        p_, w = step_stochastic(p_, w, P, rng)
        out[t + 1] = p_, w
    return out


# ------------------------------------------------------------ mean field
def mean_field(m, a, P):
    """Exact expectation map of the agent-level model as k -> infinity, in (m, a).

    The frame is averaged over q; scores are taken at the expected item shares
    under each frame and averaged over frames (exact for the soft score,
    which is linear in ehat; the hard score is linear in ehat too)."""
    p_ = (1 + m) / 2
    w = (1 + a) / 2
    q = (1 - P["eps"]) * p_ + P["eps"] / 2
    wv = np.array([w, 1 - w])
    p_new = 0.0
    score = np.zeros(2)
    for f, prob in ((1.0, q), (-1.0, 1 - q)):
        pi = 0.5 + (P["b"] + SIGNS * P["sigma"] + P["phi"] * f) / 2
        p_new += prob * float(wv @ pi)
        if P["regime"] == "B":
            score += prob * np.asarray(P["r"], float)
        else:
            score += prob * _score(p_, pi, P)
    p_new = (1 - P["rho"]) * p_ + P["rho"] * p_new
    if P["conferral"] == "ema":
        w_new = P["delta"] * w + (1 - P["delta"]) * _softmax_share(P["g"] * score)
    else:
        w_new = _confer(w, score, P)
    return 2 * p_new - 1, 2 * w_new - 1


def mean_field_closed(m, a, P):
    """The closed form of the reduced map (Regime A soft / B, ema or replicator)."""
    ph = P["phi"] * (1 - P["eps"])
    m_new = (1 - P["rho"]) * m + P["rho"] * (P["b"] + P["sigma"] * a + ph * m)
    if P["regime"] == "B":
        target = np.tanh(P["g"] * (P["r"][0] - P["r"][1]) / 2)
        return m_new, P["delta"] * a + (1 - P["delta"]) * target
    assert P["scoring"] == "soft"
    if P["conferral"] == "ema":
        return m_new, P["delta"] * a + (1 - P["delta"]) * np.tanh(P["g"] * P["sigma"] * m / 2)
    return m_new, np.tanh(np.arctanh(a) + P["eta"] * P["sigma"] * m / 2)


def run_map(fn, m0, a0, P, T):
    out = np.empty((T + 1, 2))
    out[0] = m0, a0
    m, a = m0, a0
    for t in range(T):
        m, a = fn(m, a, P)
        out[t + 1] = m, a
    return out


# ------------------------------------------------------------ linearization
def jacobian_analytic(P):
    """Jacobian of the reduced map at (m, a) = (0, 0), b = 0.

    Returns J = [[alpha, beta], [gamma, delta_eff]]."""
    ph = P["phi"] * (1 - P["eps"])
    alpha = 1 - P["rho"] + P["rho"] * ph
    beta = P["rho"] * P["sigma"]
    if P["regime"] == "B":
        gamma, d = 0.0, P["delta"]
    elif P["conferral"] == "ema":
        gamma, d = (1 - P["delta"]) * P["g"] * P["sigma"] / 2, P["delta"]
    else:
        gamma, d = P["eta"] * P["sigma"] / 2, 1.0
    return np.array([[alpha, beta], [gamma, d]])


def jacobian_numeric(fn, P, h=1e-6):
    J = np.empty((2, 2))
    for i, (dm, da) in enumerate(((h, 0.0), (0.0, h))):
        fp = np.array(fn(dm, da, P))
        fm = np.array(fn(-dm, -da, P))
        J[:, i] = (fp - fm) / (2 * h)
    return J


def threshold_holds(P):
    """CLAIM-330's condition beta*gamma > (1-alpha)(1-delta) on the reduced map,
    and its closed form for Regime A soft ema: g sigma^2 / 2 > 1 - phi(1-eps)."""
    J = jacobian_analytic(P)
    return J[0, 1] * J[1, 0] > (1 - J[0, 0]) * (1 - J[1, 1])


# ------------------------------------------------------------ predecessors
def to_bc_params(P):
    """The map from CASE-092's reduced parameters (Regime A, soft, ema) to an
    adaptive-weight opinion model with two stubborn sources.

    Collective opinion m with self-weight 1 - lam, sources at opinions
    o_j = (b + s_j sigma)/(1 - phi'), phi' = phi(1 - eps), weights on them
    lam * w_j, and w relaxing with memory delta toward a homophily kernel
    K_j(m) proportional to exp(kappa * m * o_j) (agreement kernel), with
    kappa = g (1 - phi') / 2.  At b = 0 the agreement kernel equals the
    Gaussian bounded-confidence kernel exp(-kappa/2 * (m - o_j)^2) up to a
    factor common to both sources."""
    ph = P["phi"] * (1 - P["eps"])
    lam = P["rho"] * (1 - ph)
    o = (P["b"] + SIGNS * P["sigma"]) / (1 - ph)
    kappa = P["g"] * (1 - ph) / 2
    return dict(lam=lam, o=o, kappa=kappa, delta=P["delta"])


def adaptive_bc_step(m, a, Q, kernel="agreement"):
    """Weighted averaging with two stubborn sources and homophilous weights
    with memory (delta = 0: memoryless smooth bounded confidence)."""
    w = (1 + a) / 2
    wv = np.array([w, 1 - w])
    m_new = (1 - Q["lam"]) * m + Q["lam"] * float(wv @ Q["o"])
    if kernel == "agreement":
        logits = Q["kappa"] * m * Q["o"]
    else:  # gaussian bounded confidence
        logits = -0.5 * Q["kappa"] * (m - Q["o"]) ** 2
    target = _softmax_share(logits)
    w_new = Q["delta"] * w + (1 - Q["delta"]) * target
    return m_new, 2 * w_new - 1


def degroot_stubborn_step(m, a_fixed, Q):
    """DeGroot / Friedkin-Johnsen with the same stubborn sources, fixed weights."""
    w = (1 + a_fixed) / 2
    return (1 - Q["lam"]) * m + Q["lam"] * (w * Q["o"][0] + (1 - w) * Q["o"][1])


def network_from_case(P, a):
    """Relative interaction matrix C (zero diagonal, rows sum to 1) of the
    3-member system {collective, A-specialist, B-specialist} at authority a.
    The specialists attend to the collective (they take its framing) and
    a little to each other; the collective attends to them by authority."""
    w = (1 + a) / 2
    return np.array([[0.0, w, 1 - w],
                     [0.9, 0.0, 0.1],
                     [0.9, 0.1, 0.0]])


def degroot_friedkin_step(x, C):
    """Jia, MirTabatabaei, Friedkin and Bullo (2015): W = diag(x) + (I-diag x) C,
    next x = dominant left eigenvector of W (sum 1). Reads no opinions."""
    W = np.diag(x) + (np.eye(len(x)) - np.diag(x)) @ C
    vals, vecs = np.linalg.eig(W.T)
    v = np.real(vecs[:, np.argmax(np.real(vals))])
    v = np.abs(v) / np.abs(v).sum()
    return v


def friedkin2011_step(x, C):
    """Friedkin (2011) with the Friedkin-Johnsen step: A = diag(1-x),
    W = AC + I - A, V = (I - AW)^-1 (I - A), next x = column means of V.
    Reads no opinions."""
    n = len(x)
    A = np.diag(1 - x)
    W = A @ C + np.eye(n) - A
    V = np.linalg.solve(np.eye(n) - A @ W, np.eye(n) - A)
    return V.mean(axis=0)


def opinions_under(W, y0, steps=200):
    y = np.array(y0, float)
    for _ in range(steps):
        y = W @ y
    return y
