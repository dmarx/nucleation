"""The two measures, as the record's readings define them.

Bourrat 2024 (LIT-005, read in NOTE-027):
  A* = I(S'; S), A = I(S'; S | E), nC = I(S'; E | S)   (Krakauer et al.'s, Eq. 5)
  Ahat = I(S'; S^) with S^ = do(S), Eq. 6. NOTE-027's correct route:
      p(s' | do(s)) = sum_e p(s' | s, e) p(e), then the MI of that channel under
      a chosen input distribution for S^ (fn. 4 leaves the choice open).
  C1: Ahat_S2 / H(S^2) >= [Ahat_S1 / H(S^1)] at theta_0.
  C2: Var over interventions e on E2 of Ahat_S2 | do(E2 = e) is low.
  Also I(E1'; S^1), whose rise marks the start of a scaffolded transition.

Bourrat 2023 (LIT-049, read in NOTE-064):
  dC = C_T - C_P: truthful (evolve fine, then coarse-grain by averaging) less
  projected (coarse-grain, then evolve the coarse state); a partition is
  acceptable if dC < theta; d*C the minimal one; dC|E conditions the
  projection on the environment and asks it to stay below theta in all
  environmental states. See coarse.py.
"""
import numpy as np


def H(p):
    p = np.asarray(p, float).ravel()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def mi_joint(pxy):
    """I(X;Y) from a 2-D joint."""
    pxy = np.asarray(pxy, float)
    return H(pxy.sum(1)) + H(pxy.sum(0)) - H(pxy)


def channel_mi(q_in, W):
    """I(X;Y) for input distribution q_in and channel W[x, y] = p(y|x)."""
    return mi_joint(q_in[:, None] * W)


def project(n_vars, var_idx):
    """Map each full state to the index of the sub-state on var_idx."""
    n = 2 ** n_vars
    out = np.zeros(n, int)
    for s in range(n):
        out[s] = sum(((s >> v) & 1) << j for j, v in enumerate(var_idx))
    return out


def split(n_vars, S):
    E = [v for v in range(n_vars) if v not in S]
    return E, project(n_vars, S), project(n_vars, E)


def observational(P, pi, n_vars, S):
    """Krakauer et al.'s terms for candidate S (E = the rest)."""
    E, sidx, eidx = split(n_vars, S)
    nS, nE = 2 ** len(S), 2 ** len(E)
    # joint p(s, e, s')
    Pto = np.zeros((P.shape[0], nS))
    for x2 in range(P.shape[0]):
        Pto[:, sidx[x2]] += P[:, x2]
    J = np.zeros((nS, nE, nS))
    for x in range(P.shape[0]):
        J[sidx[x], eidx[x], :] += pi[x] * Pto[x]
    p_s_sp = J.sum(1)
    p_e_sp = J.sum(0)
    Astar = mi_joint(p_s_sp)
    Ei = mi_joint(p_e_sp)
    joint_all = mi_joint(J.reshape(nS * nE, nS))  # I(S,E; S')
    return dict(Astar=Astar, A=joint_all - Ei, nC=joint_all - Astar, Ei=Ei)


def _cond_channels(P, n_vars, S, target):
    """W[s, e, t'] = p(target' = t' | S = s, E = e), exact from the kernel."""
    E, sidx, eidx = split(n_vars, S)
    tidx = project(n_vars, target)
    nS, nE, nT = 2 ** len(S), 2 ** len(E), 2 ** len(target)
    Pto = np.zeros((P.shape[0], nT))
    for x2 in range(P.shape[0]):
        Pto[:, tidx[x2]] += P[:, x2]
    W = np.zeros((nS, nE, nT))
    for x in range(P.shape[0]):
        W[sidx[x], eidx[x]] = Pto[x]
    return W, sidx, eidx


def do_channel(P, pi, n_vars, S, target=None):
    """p(target' | do(S = s)) = sum_e p(target' | s, e) p(e)."""
    target = list(S) if target is None else list(target)
    W, sidx, eidx = _cond_channels(P, n_vars, S, target)
    pE = np.zeros(W.shape[1])
    np.add.at(pE, eidx, pi)
    return np.einsum("set,e->st", W, pE), W, pE


def marginal(pi, idx, n):
    out = np.zeros(n)
    np.add.at(out, idx, pi)
    return out


def ahat(P, pi, n_vars, S, input_dist="uniform"):
    """Ahat = I(S'; S^) and its normalised form Ahat / H(S^)."""
    Wdo, W, pE = do_channel(P, pi, n_vars, S)
    nS = Wdo.shape[0]
    if input_dist == "uniform":
        q = np.full(nS, 1.0 / nS)
    else:  # the population (stationary) distribution of S
        q = marginal(pi, project(n_vars, S), nS)
    a = channel_mi(q, Wdo)
    return a, a / H(q)


def c2_profile(P, n_vars, S):
    """Ahat_S | do(E = e) for every e, uniform input on S^; its mean and
    variance over e taken uniformly (all interventions on E possible)."""
    E, sidx, eidx = split(n_vars, S)
    W, _, _ = _cond_channels(P, n_vars, S, list(S))
    nS = W.shape[0]
    q = np.full(nS, 1.0 / nS)
    vals = np.array([channel_mi(q, W[:, e, :]) for e in range(W.shape[1])])
    return dict(mean=float(vals.mean()), var=float(vals.var()),
                sd=float(vals.std()), min=float(vals.min()),
                max=float(vals.max()), values=vals)


def effect_on_environment(P, pi, n_vars, S):
    """I(E' ; S^), uniform input on S^."""
    E, _, _ = split(n_vars, S)
    Wdo, _, _ = do_channel(P, pi, n_vars, S, target=E)
    nS = Wdo.shape[0]
    return channel_mi(np.full(nS, 1.0 / nS), Wdo)
