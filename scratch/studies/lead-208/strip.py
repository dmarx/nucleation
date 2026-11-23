"""Exact predictive information on an infinite Ising strip, by transfer matrix.

The strip is W spins wide (periodic across) and infinitely long. Read along
its length it is a stationary Markov chain of columns c_t in {0..2^W - 1}.

Two definitions of the predictive information of TERM-141,
I_pred(T) = 2 H(T) - H(2T) (in bits), are computed:

- column blocks: the process is the sequence of whole columns. Because it is
  Markov, I(c_{1:T}; c_{T+1:2T}) = I(c_T; c_{T+1}) for every T >= 1, so the
  column-block quantity is a function of W alone.
- one row: the process is the sequence of a single row's spins, a hidden
  Markov process whose hidden state is the column. Its block entropies are
  computed exactly by the forward recursion over all 2^t row sequences.
"""
import numpy as np


def column_spins(W):
    """(2^W, W) array of +-1 spins; bit i of the column index is spin i."""
    c = np.arange(2 ** W)[:, None]
    return np.where((c >> np.arange(W)) & 1, 1, -1).astype(np.float64)


def transfer_matrix(W, K):
    """Symmetric column transfer matrix and its leading eigenpair."""
    S = column_spins(W)
    # periodic across the strip (for W = 2 the pair is bonded twice, as on
    # a 2-wide torus; for W = 1 the term is a constant)
    intra = (S * np.roll(S, -1, axis=1)).sum(axis=1)
    inter = S @ S.T
    logT = K * inter + 0.5 * K * (intra[:, None] + intra[None, :])
    shiftc = logT.max()
    Tm = np.exp(logT - shiftc)
    vals, vecs = np.linalg.eigh(Tm)
    lam = vals[-1]
    psi = np.abs(vecs[:, -1])
    return Tm, lam, psi, shiftc


def markov_chain(W, K):
    """Stationary distribution pi and transition matrix P of the column chain."""
    Tm, lam, psi, _ = transfer_matrix(W, K)
    pi = psi ** 2
    pi /= pi.sum()
    P = Tm * psi[None, :] / (lam * psi[:, None])
    P /= P.sum(axis=1, keepdims=True)  # remove rounding
    return pi, P


def _entropy_bits(p):
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def column_mi(W, K):
    """I(c_t; c_{t+1}) in bits, the column-block predictive information."""
    pi, P = markov_chain(W, K)
    joint = pi[:, None] * P
    return 2 * _entropy_bits(pi) - _entropy_bits(joint.ravel())


def column_block_entropy(W, K, T):
    """H(c_1..c_T) in bits by explicit enumeration (small W*T only; for tests)."""
    pi, P = markov_chain(W, K)
    p = pi.copy()
    for _ in range(T - 1):
        p = (p[..., None] * P.reshape((1,) * (p.ndim - 1) + P.shape))
    return _entropy_bits(p.ravel())


def row_block_entropies(W, K, tmax, row=0):
    """H(t) in bits for t = 1..tmax of one row's spin sequence (exact)."""
    pi, P = markov_chain(W, K)
    bit = ((np.arange(2 ** W) >> row) & 1).astype(bool)
    # alpha[seq, c] = P(row spins = seq, column at time t = c)
    alpha = np.stack([np.where(~bit, pi, 0.0), np.where(bit, pi, 0.0)])
    H = [_entropy_bits(alpha.sum(axis=1))]
    for _ in range(tmax - 1):
        nxt = alpha @ P  # (2^t, 2^W)
        alpha = np.empty((2 * nxt.shape[0], nxt.shape[1]))
        alpha[0::2] = np.where(~bit, nxt, 0.0)
        alpha[1::2] = np.where(bit, nxt, 0.0)
        H.append(_entropy_bits(alpha.sum(axis=1)))
    return np.array(H)


def row_ipred(W, K, Tmax):
    """I_pred(T) = 2 H(T) - H(2T) in bits, T = 1..Tmax, for one row."""
    H = row_block_entropies(W, K, 2 * Tmax)
    T = np.arange(1, Tmax + 1)
    return 2 * H[T - 1] - H[2 * T - 1]
