"""LEAD-190: population comparisons for the authority-grant claims.

Built on LEAD-090's one-institution model (CASE-363), loaded by path from
../lead-090/model.py and not modified. Each operator of a population is both
a reader (an interpreter with a meaning, as LEAD-090's collective) and a
retriever (a specialist, as LEAD-090's A- and B-specialists) for the others.

Population
----------
N operators. Operator j has a preferred policy p_j (sign s_j = +1 for the A
side, -1 for the B side), a retrieval specialization toward its own side
(s_j * sigma, LEAD-090's specialist), and a relevance r_j in (0, 1), its
competence as an error detector / critic, drawn independently of s_j.
Operator i holds a meaning m_i in [-1, 1] (p_i^m = (1 + m_i)/2 on A).

Meaning layer (LEAD-090's step, one per reader):
  * i frames its query for A with prob (1 - eps) P_i + eps/2 (frame f_i);
    the source j answers with its own lean too: frame f_j drawn the same
    way from j's meaning (phi_s, the source's interpretation bias; phi_s = 0
    makes each reader an independent LEAD-090 institution).
  * an item j returns to i supports A with prob
        pi_ij = 1/2 + (b + s_j sigma + phi f_i + phi_s f_j) / 2.
  * P_i <- (1 - rho) P_i + rho sum_j W_ij ehat_ij   (W: critic weights,
    row-stochastic over all j, i included: whose evidence i reads, and how
    much; W_ii is the weight on one's own retrieval)
  * critic score of j for i:
        zeta * agree_ij + (1 - zeta) * rel_j
    agree_ij = P_i ehat_ij + (1 - P_i)(1 - ehat_ij)   (LEAD-090 Regime A soft)
    rel_j    = observed relevance, Binomial(k, r_j)/k   (LEAD-090 Regime B)
    zeta is CASE-092's "independence of evaluation" (zeta = 0 independent).
  * W_i <- delta W_i + (1 - delta) softmax_j(g * score_ij)  (ema)

Decision layer (CLAIM-282, CLAIM-375, CLAIM-502):
  * decision grants E_ij >= 0, E_ii = 0, row sums <= 1, budgets b_i = 1.
  * authority g from one of three aggregation rules, all with damping eta:
        one-hop   g = (1 - eta) bud + eta E^T bud
        recursive g = (1 - eta)(I - eta E^T)^-1 bud
        loo       g_k = [(1 - eta)(I - eta E_(-k)^T)^-1 bud]_k,
                  E_(-k) = E with row k zeroed (CLAIM-502)
  * decision p* = sum_j g_j p_j / sum_j g_j.
  * objectives: 'policy'    J_i = -(p* - p_i)^2 - lam sum_j E_ij
                'authority' J_i = log g_i     - lam sum_j E_ij
  * operators move their grant rows by projected gradient ascent on J_i
    (simultaneous, exact gradients).

Bound by A2's two conditions = an aggregation under which g_i does not
respond to E_i. (one-hop, loo) and the 'policy' objective. Unbound =
recursive with 'authority'.

Grant schemes for the population comparison of CLAIM-281:
  scalar-agree  one grant row, scored by agreement (zeta = 1); it weights
                evidence and confers decision authority: E = W off the
                diagonal (what i does not grant it keeps, W_ii).
  scalar-comp   one grant row, scored by relevance (zeta = 0); E = W off
                the diagonal.
  scalar-policy one grant row, moved by the policy objective (the
                CLAIM-285 operator); W = E + diag(1 - rowsum E).
  role          two rows: W scored with the given zeta (default 0), E moved
                by the policy objective. CLAIM-281's E_i(j, r, ...).
  role-agree    two rows, W scored by agreement (zeta = 1): role indexing
                without independent scoring (ablation).
"""
from __future__ import annotations

import importlib.util
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "lead090_model", os.path.join(_HERE, "..", "lead-090", "model.py"))
one = importlib.util.module_from_spec(_spec)  # LEAD-090's model, unmodified
_spec.loader.exec_module(one)

SCHEMES = ("scalar-agree", "scalar-comp", "scalar-policy", "role", "role-agree")


# ------------------------------------------------------------ population
def population(N=20, seed=0, pref_lo=0.3, r_lo=0.4, r_hi=0.9):
    """Half on each side; preferences s_i * U(pref_lo, 1); relevance
    U(r_lo, r_hi), independent of side."""
    rng = np.random.default_rng(seed)
    s = np.where(np.arange(N) < N // 2, 1.0, -1.0)
    pref = s * rng.uniform(pref_lo, 1.0, N)
    r = rng.uniform(r_lo, r_hi, N)
    return dict(N=N, s=s, pref=pref, r=r)


def params(**kw):
    p = dict(rho=0.2, sigma=0.4, phi=0.3, phi_s=0.0, eps=0.2, b=0.0, g=12.0,
             delta=0.9, k=50, zeta=1.0, eta=0.5, lam=0.005, lr=2.0,
             agg="one-hop", objective="policy")
    p.update(kw)
    assert abs(p["b"]) + p["sigma"] + p["phi"] + p["phi_s"] <= 1 + 1e-12
    return p


def _softmax(Z, mask=None):
    Z = Z.copy()
    if mask is not None:
        Z[~mask] = -np.inf
    Z -= Z.max(axis=1, keepdims=True)
    X = np.exp(Z)
    return X / X.sum(axis=1, keepdims=True)


def full_W(N):
    return np.full((N, N), 1.0 / N)


def W_from_E(E):
    return E + np.diag(1.0 - E.sum(axis=1))


def E_from_W(W):
    E = W.copy()
    np.fill_diagonal(E, 0.0)
    return E


def uniform_W(N):
    W = np.full((N, N), 1.0 / (N - 1))
    np.fill_diagonal(W, 0.0)
    return W


# ------------------------------------------------------------ meaning layer
def expected_pi(m, pop, P):
    """E[pi_ij] over both frames, an N x N array."""
    ph = P["phi"] * (1 - P["eps"])
    phs = P["phi_s"] * (1 - P["eps"])
    x = P["b"] + pop["s"][None, :] * P["sigma"] + ph * m[:, None] + phs * m[None, :]
    return 0.5 + x / 2


def critic_scores(Pm, ehat, rel, P):
    agree = Pm[:, None] * ehat + (1 - Pm[:, None]) * (1 - ehat)
    return P["zeta"] * agree + (1 - P["zeta"]) * rel[None, :]


def meaning_mean_field(m, W, pop, P, mask=None):
    """Mean-field step of the meaning layer: returns (m', W_target) where
    W_target is the softmax the ema relaxes toward. Exact expectation as
    k -> infinity (scores are linear in ehat; frames are independent)."""
    Pm = (1 + m) / 2
    pi = expected_pi(m, pop, P)
    Pm_new = (1 - P["rho"]) * Pm + P["rho"] * (W * pi).sum(axis=1)
    sc = critic_scores(Pm, pi, pop["r"], P)
    return 2 * Pm_new - 1, _softmax(P["g"] * sc, mask)


def meaning_stochastic(m, W, pop, P, rng, mask=None):
    N = pop["N"]
    Pm = (1 + m) / 2
    q = (1 - P["eps"]) * Pm + P["eps"] / 2
    f = np.where(rng.random(N) < q, 1.0, -1.0)      # asker frames
    fs = np.where(rng.random(N) < q, 1.0, -1.0)     # sources' own leans
    pi = 0.5 + (P["b"] + pop["s"][None, :] * P["sigma"] + P["phi"] * f[:, None]
                + P["phi_s"] * fs[None, :]) / 2
    ehat = rng.binomial(P["k"], pi) / P["k"]
    rel = rng.binomial(P["k"], pop["r"]) / P["k"]
    Pm_new = (1 - P["rho"]) * Pm + P["rho"] * (W * ehat).sum(axis=1)
    sc = critic_scores(Pm, ehat, rel, P)
    return 2 * Pm_new - 1, _softmax(P["g"] * sc, mask)


def population_jacobian(pop, P):
    """Linearisation of the mean-field meaning layer (ema on W) at m = 0,
    W uniform (1/N, self included), b = 0, equal relevance, in the
    variables (m_i, a_i), a_i = sum_j W_ij s_j (the net side of i's
    reading):

    m_i' = alpha m_i + rho sigma a_i + rho phi_s' mean_j m_j
    a_i' = delta a_i + (1 - delta) (g zeta sigma / 2) c m_i,
    c = mean_j s_j^2 - (mean_j s_j)^2  (= 1 for a balanced population).

    The other directions of W do not enter at first order (m = 0 there).
    Returns the 2N x 2N matrix."""
    N, s = pop["N"], pop["s"]
    ph = P["phi"] * (1 - P["eps"])
    phs = P["phi_s"] * (1 - P["eps"])
    avg = np.ones((N, N)) / N
    c = float(np.mean(s ** 2) - np.mean(s) ** 2)
    J = np.zeros((2 * N, 2 * N))
    I = np.eye(N)
    J[:N, :N] = (1 - P["rho"] + P["rho"] * ph) * I + P["rho"] * phs * avg
    J[:N, N:] = P["rho"] * P["sigma"] * I
    J[N:, :N] = (1 - P["delta"]) * P["g"] * P["zeta"] * P["sigma"] / 2 * c * I
    J[N:, N:] = P["delta"] * I
    return J


def meaning_threshold(P, c=1.0):
    """Closed forms from population_jacobian: the uniform mode (all
    meanings move together; the population is captured as one) is unstable
    iff  g zeta sigma^2 c / 2 > 1 - phi' - phi_s';  every differentiating
    mode (meanings move apart; factions) iff  g zeta sigma^2 c / 2 > 1 - phi'.
    With zeta = 1 and phi_s = 0 both are CLAIM-947's threshold. Returns the
    left side and both right sides."""
    ph = P["phi"] * (1 - P["eps"])
    phs = P["phi_s"] * (1 - P["eps"])
    return (P["g"] * P["zeta"] * P["sigma"] ** 2 * c / 2, 1 - ph - phs, 1 - ph)


# ------------------------------------------------------------ decision layer
def authority(E, P, bud=None):
    N = E.shape[0]
    bud = np.ones(N) if bud is None else bud
    eta = P["eta"]
    if P["agg"] == "one-hop":
        return (1 - eta) * bud + eta * E.T @ bud
    if P["agg"] == "recursive":
        return (1 - eta) * np.linalg.solve(np.eye(N) - eta * E.T, bud)
    g = np.empty(N)
    for k in range(N):
        Ek = E.copy()
        Ek[k] = 0.0
        g[k] = (1 - eta) * np.linalg.solve(np.eye(N) - eta * Ek.T, bud)[k]
    return g


def _loo_parts(E, P, bud):
    """A[k, j] = M_k[k, j], G[k, i] = g^(k)_i, M_k = (I - eta E_(-k)^T)^-1."""
    N = E.shape[0]
    eta = P["eta"]
    A = np.empty((N, N))
    G = np.empty((N, N))
    for k in range(N):
        Ek = E.copy()
        Ek[k] = 0.0
        Mk = np.linalg.inv(np.eye(N) - eta * Ek.T)
        A[k] = Mk[k]
        G[k] = (1 - eta) * Mk @ bud
    return A, G


def objective(E, pref, P, bud=None):
    g = authority(E, P, bud)
    pstar = g @ pref / g.sum()
    cost = P["lam"] * E.sum(axis=1)
    if P["objective"] == "policy":
        return -(pstar - pref) ** 2 - cost
    return np.log(g) - cost


def grad(E, pref, P, bud=None):
    """G[i, j] = dJ_i / dE_ij (diagonal zero)."""
    N = E.shape[0]
    bud = np.ones(N) if bud is None else bud
    eta = P["eta"]
    agg = P["agg"]
    if agg == "loo":
        A, Gk = _loo_parts(E, P, bud)
        g = np.diag(Gk).copy()
    else:
        g = authority(E, P, bud)
    S = g.sum()
    pstar = g @ pref / S
    dev = pref - pstar
    if P["objective"] == "policy":
        if agg == "one-hop":
            dp = eta * bud[:, None] * dev[None, :] / S
        elif agg == "recursive":
            Mt = np.linalg.inv(np.eye(N) - eta * E.T)
            v = Mt.T @ dev                       # v_j = sum_k M[k, j] dev_k
            dp = eta * g[:, None] * v[None, :] / S
        else:
            T = Gk.T @ (dev[:, None] * A)       # sum_k G[k,i] dev_k A[k,j]
            T -= (dev * np.diag(Gk))[:, None] * A  # drop k = i
            dp = eta * T / S
        G_ = -2 * (pstar - pref)[:, None] * dp
    else:
        if agg == "recursive":
            Mt = np.linalg.inv(np.eye(N) - eta * E.T)
            G_ = eta * Mt.copy()                 # d log g_i / dE_ij = eta M[i, j]
        else:
            G_ = np.zeros((N, N))
    G_ = G_ - P["lam"]
    np.fill_diagonal(G_, 0.0)
    return G_


def project_rows(X):
    """Project each row (diagonal excluded, kept 0) onto {x >= 0, sum x <= 1}."""
    N = X.shape[0]
    out = np.zeros_like(X)
    for i in range(N):
        idx = np.arange(N) != i
        x = np.maximum(X[i, idx], 0.0)
        if x.sum() > 1.0:
            x = _project_simplex(X[i, idx])
        out[i, idx] = x
    return out


def _project_simplex(v):
    u = np.sort(v)[::-1]
    css = np.cumsum(u)
    rho_ = np.nonzero(u * np.arange(1, len(v) + 1) > (css - 1))[0][-1]
    theta = (css[rho_] - 1) / (rho_ + 1.0)
    return np.maximum(v - theta, 0.0)


def grant_step(E, pref, P):
    return project_rows(E + P["lr"] * grad(E, pref, P))


def reach(E, P, bud=None):
    """R[i, k]: authority at k per unit of i's budget (d g_k / d bud_i)."""
    N = E.shape[0]
    eta = P["eta"]
    if P["agg"] == "one-hop":
        return (1 - eta) * np.eye(N) + eta * E
    if P["agg"] == "recursive":
        M = np.linalg.inv(np.eye(N) - eta * E.T)
        return (1 - eta) * M.T
    bud = np.ones(N) if bud is None else bud
    A, _ = _loo_parts(E, P, bud)
    return (1 - eta) * A.T                         # R[i, k] = (1-eta) M_k[k, i]


# ------------------------------------------------------------ measures
def grant_measures(E, pop):
    """Delegation and its alignment, for a decision-grant matrix."""
    N, s, pref = pop["N"], pop["s"], pop["pref"]
    same = (s[:, None] == s[None, :]) & ~np.eye(N, dtype=bool)
    mass = E.sum(axis=1)
    tot = mass.sum()
    chance = (same.sum(axis=1) / (N - 1)).mean()
    aligned = (E * same).sum() / tot if tot > 1e-12 else np.nan
    off = ~np.eye(N, dtype=bool)
    dist = np.abs(pref[:, None] - pref[None, :])[off]
    e = E[off]
    corr_dist = float(np.corrcoef(e, -dist)[0, 1]) if e.std() > 1e-12 else np.nan
    # within one's own side, does i favour the nearer or the more extreme?
    ext = (s[None, :] * pref[None, :] * np.ones((N, 1)))[same]
    corr_ext = float(np.corrcoef(E[same], ext)[0, 1]) if E[same].std() > 1e-12 else np.nan
    near = -np.abs(pref[:, None] - pref[None, :])[same]
    corr_near = float(np.corrcoef(E[same], near)[0, 1]) if E[same].std() > 1e-12 else np.nan
    return dict(mass=float(mass.mean()), aligned_share=float(aligned),
                chance_share=float(chance), corr_neg_distance=corr_dist,
                within_side_corr_extremity=corr_ext,
                within_side_corr_nearness=corr_near)


def reach_measures(E, pop, P):
    """Where i's budget ends up beyond the one-hop part of its grants."""
    N, s = pop["N"], pop["s"]
    R = reach(E, P)
    eta = P["eta"]
    direct = (1 - eta) * eta * E if P["agg"] != "one-hop" else eta * E
    ind = R - direct
    np.fill_diagonal(ind, 0.0)
    ind = np.maximum(ind, 0.0)
    same = (s[:, None] == s[None, :]) & ~np.eye(N, dtype=bool)
    tot_off = (R * ~np.eye(N, dtype=bool)).sum()
    tot_ind = ind.sum()
    self_return = np.diag(R) - (1 - eta)
    return dict(indirect_fraction=float(tot_ind / tot_off) if tot_off > 0 else 0.0,
                indirect_aligned_share=float((ind * same).sum() / tot_ind)
                if tot_ind > 1e-12 else np.nan,
                self_return=float(self_return.mean()))


def meaning_measures(m, W, E, pop, P):
    N, s, r = pop["N"], pop["s"], pop["r"]
    opp = s[:, None] != s[None, :]
    gap = float(m[s > 0].mean() - m[s < 0].mean())
    corr = float(np.corrcoef(m, s)[0, 1]) if m.std() > 1e-9 else 0.0
    crit_cross = float((W * opp).sum(axis=1).mean())
    tot = E.sum(axis=1)
    dec_cross = float(np.nanmean(np.where(tot > 1e-12, (E * opp).sum(axis=1) / np.maximum(tot, 1e-12), np.nan)))
    # do i's critic weights on opponents follow the opponents' competence?
    w_opp = W[opp]
    r_opp = np.broadcast_to(r[None, :], (N, N))[opp]
    corr_r = float(np.corrcoef(w_opp, r_opp)[0, 1]) if w_opp.std() > 1e-12 else np.nan
    g = authority(E, P) if E.sum() > 0 else np.ones(N)
    pstar = float(g @ pop["pref"] / g.sum())
    loss = float(((pstar - pop["pref"]) ** 2).mean())
    sign_ok = float((np.sign(m) == np.sign(P["b"])).mean()) if P["b"] != 0 else np.nan
    return dict(gap=gap, corr_m_side=corr, critic_cross=crit_cross,
                critic_cross_chance=float(opp[0].mean()),
                decision_cross=dec_cross, critic_opp_corr_relevance=corr_r,
                pstar=pstar, policy_loss=loss, fidelity=sign_ok,
                m_mean=float(m.mean()))


# ------------------------------------------------------------ the comparison
def run_scheme(scheme, pop, P, T=600, m0=None, stochastic=False, seed=0,
               E0=None, record=None):
    """Run one grant scheme on a population; returns (m, W, E)."""
    N = pop["N"]
    P = dict(P)
    if scheme in ("scalar-agree", "role-agree"):
        P["zeta"] = 1.0
    elif scheme == "scalar-comp":
        P["zeta"] = 0.0
    rng = np.random.default_rng(seed)
    m = np.zeros(N) if m0 is None else np.array(m0, float)
    W = full_W(N)
    E = (0.5 * uniform_W(N)) if E0 is None else E0.copy()
    if scheme in ("scalar-agree", "scalar-comp"):
        E = E_from_W(W)
    PE = dict(P, agg="one-hop", objective="policy")
    for t in range(T):
        if scheme == "scalar-policy":
            W = W_from_E(E)
        if stochastic:
            m_new, Wt = meaning_stochastic(m, W, pop, P, rng)
        else:
            m_new, Wt = meaning_mean_field(m, W, pop, P)
        if scheme != "scalar-policy":
            W = P["delta"] * W + (1 - P["delta"]) * Wt
        if scheme in ("scalar-agree", "scalar-comp"):
            E = E_from_W(W)
        else:
            E = grant_step(E, pop["pref"], PE)
        m = np.clip(m_new, -1, 1)
        if record is not None:
            record.append(m.copy())
    if scheme == "scalar-policy":
        W = W_from_E(E)
    return m, W, E


def run_game(pop, P, T=400, E0=None):
    """The decision-grant game alone (CLAIM-285's comparison)."""
    N = pop["N"]
    E = (0.5 * uniform_W(N)) if E0 is None else E0.copy()
    for _ in range(T):
        E = grant_step(E, pop["pref"], P)
    return E
