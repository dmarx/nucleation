"""Measures for LEAD-026, all linear-Gaussian, from simulated trajectories.

LEAD-167's measures.py computes Krakauer et al.'s A*, A, nC and Bourrat's
Ahat exactly from a 256-state transition matrix. CASE-101's populations
have continuous norms, turnover and lag-L transmission, which no small
discrete kernel holds, so the same definitions are re-implemented here in
Gaussian form, estimated from long simulations:

  A*(D) = I(S_{t+D}; S_t),  A(D) = I(S_{t+D}; S_t | E_t),
  nC(D) = I(S_{t+D}; E_t | S_t)         (Krakauer et al., LIT-1137, with
                                           A11's lag-dependent form),
  Ahat(D) = I(S_{t+D}; S^_t)            (Bourrat, LIT-005; NOTE-027's
      route: do(S) with E left at its own distribution; the input
      distribution of S^ is S's population marginal; run.py intervenes
      in the simulator),
  TE_{rest->S}(p) = I(S_{t+1}; R_{t-p+1..t} | S_{t-p+1..t})
      (dynamical independence, THEORY-257, read as zero transfer into
      the candidate; Barnett and Seth's linear case),
  the priced lagged block (CLAIM-157 with CLAIM-154's price, see
      block_scores).

Information is in nats. Every estimate is the Gaussian (linear) one, a
lower bound on the true information when the process is not Gaussian,
which turnover makes it.
"""
import itertools

import numpy as np


def logdet(C):
    sign, ld = np.linalg.slogdet(C)
    if sign <= 0:
        raise np.linalg.LinAlgError("covariance not positive definite")
    return ld


def cmi_cov(C, a, b, c=()):
    """I(a; b | c) for index lists into a Gaussian covariance C."""
    a, b, c = list(a), list(b), list(c)
    if not a or not b:
        return 0.0

    def ld(ix):
        return logdet(C[np.ix_(ix, ix)]) if ix else 0.0
    return 0.5 * (ld(a + c) + ld(b + c) - ld(c) - ld(a + b + c))


def embed_cov(traj, p):
    """Covariance of [V_{t+1}, V_t, ..., V_{t-p+1}] pooled over replicas
    and times. traj: (T, R, nv). Block j of the result is V_{t+1-j}.
    Returns (C, n_rows)."""
    T, R, nv = traj.shape
    d = (p + 1) * nv
    S = np.zeros((d, d))
    m = np.zeros(d)
    n = 0
    for r in range(R):
        x = traj[:, r, :]
        rows = T - p
        Z = np.empty((rows, d))
        for j in range(p + 1):
            Z[:, j * nv:(j + 1) * nv] = x[p - j:T - j]
        S += Z.T @ Z
        m += Z.sum(0)
        n += rows
    m /= n
    return S / n - np.outer(m, m), n


def lag_pair_cov(traj, D):
    """Covariance of [V_t, V_{t+D}] pooled; block 0 is V_t."""
    T, R, nv = traj.shape
    a = traj[:-D].reshape(-1, nv)
    b = traj[D:].reshape(-1, nv)
    Z = np.concatenate([a, b], 1)
    return np.cov(Z.T)


def krakauer(Cpair, S, E):
    """A*, A, nC at the pair covariance's lag, for candidate S and
    environment E (index lists into the nv variables)."""
    nv = Cpair.shape[0] // 2
    St = list(S)
    Sf = [nv + i for i in S]
    Et = list(E)
    Astar = cmi_cov(Cpair, Sf, St)
    A = cmi_cov(Cpair, Sf, St, Et)
    nC = cmi_cov(Cpair, Sf, Et, St)
    return dict(Astar=Astar, A=A, nC=nC)


def _ix(vars_, lags, nv):
    return [j * nv + v for j in lags for v in vars_]


def transfer_into(Cemb, nv, S, rest, p):
    """TE_{rest -> S} with history p from an embedding covariance."""
    if not rest:
        return 0.0
    tgt = _ix(S, [0], nv)
    past = list(range(1, p + 1))
    return cmi_cov(Cemb, tgt, _ix(rest, past, nv), _ix(S, past, nv))


def cut_lr(Cemb, n, nv, W, src, dst, V):
    """Likelihood-ratio statistic for the coefficients from src's lags
    1..W onto dst's next values, in the VAR(W) of all variables V.
    Returns (LR, k): LR = n [ln det S_{dst|restricted} - ln det S_{dst|full}]
    = 2 n I(dst_{t+1}; src_past | rest of the past), k = |src||dst|W."""
    past = list(range(1, W + 1))
    others = [v for v in V if v not in src]
    I = cmi_cov(Cemb, _ix(dst, [0], nv), _ix(src, past, nv), _ix(others, past, nv))
    return 2.0 * n * I, len(src) * len(dst) * W


def lnbf_keep(lr, k, n):
    """CLAIM-154's rule for a group of k coefficients: ln BF(keep) =
    1/2 (d'^2 - Occam). With a unit-information Gaussian prior on each
    coefficient (prior variance n times the posterior's), Occam is ln n per
    coefficient and d'^2 is the LR statistic: ln BF = 1/2 (LR - k ln n)."""
    return 0.5 * (lr - k * np.log(n))


def bipartitions(S):
    S = list(S)
    first, rest = S[0], S[1:]
    for mask in range(0, 2 ** len(rest) - 1):
        s1 = [first] + [rest[i] for i in range(len(rest)) if mask >> i & 1]
        s2 = [v for v in S if v not in s1]
        yield s1, s2


def block_scores(Cemb, n, nv, W, S, V):
    """The priced lagged block test of candidate S within the observed V,
    with window W (CLAIM-157, lagged as QUESTION-116 asks).

    internal = min over bipartitions (S1, S2) of S of ln BF(keep) for all
        coupling across the cut, both directions (S is not two systems);
    edge = ln BF(keep) for all coupling between S and V \\ S, both
        directions (the edge is weak).
    S passes when internal > 0 and edge <= 0. A singleton has no internal
    cut and passes on its edge alone."""
    V = list(V)
    S = list(S)
    rest = [v for v in V if v not in S]

    def two_way(a, b):
        l1, k1 = cut_lr(Cemb, n, nv, W, a, b, V)
        l2, k2 = cut_lr(Cemb, n, nv, W, b, a, V)
        return lnbf_keep(l1 + l2, k1 + k2, n), lnbf_keep(l1, k1, n), lnbf_keep(l2, k2, n)

    if rest:
        edge, edge_in, edge_out = two_way(rest, S)
    else:
        edge = edge_in = edge_out = -np.inf
    if len(S) > 1:
        internal = min(two_way(s1, s2)[0] for s1, s2 in bipartitions(S))
    else:
        internal = np.inf
    return dict(internal=float(internal), edge=float(edge),
                edge_in=float(edge_in), edge_out=float(edge_out),
                passes=bool(internal > 0 and edge <= 0))


def subsets(V):
    V = list(V)
    for k in range(1, len(V) + 1):
        for c in itertools.combinations(V, k):
            yield list(c)


def gaussian_mi_samples(X, Y):
    """I(X; Y) in nats from paired samples (n, dx), (n, dy)."""
    Z = np.concatenate([X, Y], 1)
    C = np.cov(Z.T)
    dx = X.shape[1]
    return cmi_cov(C, list(range(dx)), list(range(dx, Z.shape[1])))
