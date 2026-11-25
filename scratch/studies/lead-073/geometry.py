"""The quantities of NOTE-746 (Marconato et al., LIT-950), computed from finite samples.

Notation as in NOTE-746:
  F = SIm(f), the span of the context representations f(x);
  G = SIm(g0), the span of the pivoted unembeddings g0(y) = g(y) - g(y0)
      (pivot-independent: it equals the span of the centred unembeddings);
  M = Im(P_F P_G),  N = ker(P_F P_G)^perp            (Eq. 7)
  Gamma   = span of the reply difference vectors of one relation (a subspace of G);
  A_q     = the affine map with P_Gamma f(s ^ q) = P_Gamma A_q f(s) + a_q   (Def. 9);
  Gamma_q = Im(A_q^T P_Gamma)                         (Theorem 14).

Every span is estimated numerically: a right-singular vector is kept when its
singular value exceeds rtol times the largest. The tolerances are arguments so
that the pre-registered values (PREREG.md) and their sensitivity runs use the
same code.
"""
from __future__ import annotations

import numpy as np


def span_basis(X: np.ndarray, rtol: float) -> tuple[np.ndarray, np.ndarray]:
    """Orthonormal basis (d, k) of the row span of X (n, d) at relative tolerance rtol.

    Returns (Q, s) with s every singular value of X, largest first.
    """
    X = np.asarray(X, dtype=np.float64)
    _, s, vt = np.linalg.svd(X, full_matrices=False)
    if s.size == 0 or s[0] == 0:
        return np.zeros((X.shape[1], 0)), s
    k = int(np.sum(s > rtol * s[0]))
    return vt[:k].T, s


def pivot_span(Gm: np.ndarray, rtol: float) -> tuple[np.ndarray, np.ndarray]:
    """G = span{g(y) - g(y0)}: the row span of the centred unembedding matrix."""
    Gm = np.asarray(Gm, dtype=np.float64)
    return span_basis(Gm - Gm.mean(0, keepdims=True), rtol)


def m_and_n(QF: np.ndarray, QG: np.ndarray, ctol: float):
    """M = Im(P_F P_G) and N = ker(P_F P_G)^perp, with dim M = dim N (Lemma 2).

    P_F P_G = QF (QF^T QG) QG^T. With QF^T QG = U S V^T (S the cosines of the
    principal angles between F and G), Im = QF U_+ and the row space = QG V_+,
    where + keeps the cosines above ctol.
    """
    if QF.shape[1] == 0 or QG.shape[1] == 0:
        d = QF.shape[0]
        return np.zeros((d, 0)), np.zeros((d, 0)), np.zeros(0)
    U, S, Vt = np.linalg.svd(QF.T @ QG, full_matrices=False)
    keep = S > ctol
    return QF @ U[:, keep], QG @ Vt[keep].T, S


def containment(QS: np.ndarray, QT: np.ndarray) -> dict:
    """How far subspace S lies inside subspace T (both orthonormal bases).

    mean_out  : mean over an orthonormal basis of S of the squared norm outside T
                (= 1 - mean cos^2 of the principal angles);
    worst_out : the same for the worst direction of S (= 1 - min cos^2);
    max_angle : the largest principal angle, in degrees.
    """
    k = QS.shape[1]
    if k == 0:
        return {"dim": 0, "mean_out": 0.0, "worst_out": 0.0, "max_angle_deg": 0.0}
    if QT.shape[1] == 0:
        return {"dim": k, "mean_out": 1.0, "worst_out": 1.0, "max_angle_deg": 90.0}
    c = np.linalg.svd(QT.T @ QS, compute_uv=False)
    c = np.concatenate([c, np.zeros(max(0, k - c.size))])[:k]
    c = np.clip(c, 0.0, 1.0)
    return {"dim": k, "mean_out": float(1 - np.mean(c ** 2)), "worst_out": float(1 - np.min(c) ** 2),
            "max_angle_deg": float(np.degrees(np.arccos(np.min(c))))}


def energy_outside(B: np.ndarray, QT: np.ndarray) -> float:
    """Fraction of the Frobenius energy of the columns of B (d, k) that lies outside span(QT)."""
    tot = float(np.sum(B ** 2))
    if tot == 0:
        return 0.0
    inside = float(np.sum((QT.T @ B) ** 2)) if QT.shape[1] else 0.0
    return max(0.0, 1.0 - inside / tot)


def reply_subspace(Gm: np.ndarray, reply_ids, rtol: float = 1e-6) -> np.ndarray:
    """Gamma: the span of the differences g(y) - g(y') over the relation's replies."""
    R = np.asarray(Gm, dtype=np.float64)[list(reply_ids)]
    Q, _ = span_basis(R - R.mean(0, keepdims=True), rtol)
    return Q


def fit_relation(Fs: np.ndarray, Fsq: np.ndarray, QGam: np.ndarray, lam: float):
    """Ridge fit of Def. 9 in Gamma coordinates: z = QGam^T f(s^q) ~ A f(s) + a.

    Returns A (k, d) and a (k,). In these coordinates A = QGam^T A_q, so
    Gamma_q = Im(A_q^T P_Gamma) = Im(A^T). lam is relative to the mean squared
    singular value of the centred inputs.
    """
    X = np.asarray(Fs, dtype=np.float64)
    Z = np.asarray(Fsq, dtype=np.float64) @ QGam
    xm, zm = X.mean(0), Z.mean(0)
    Xc, Zc = X - xm, Z - zm
    n, d = Xc.shape
    scale = np.sum(Xc ** 2) / max(1, min(n, d))
    K = Xc @ Xc.T + lam * scale * np.eye(n)      # dual form: n is small, d large
    A = (Xc.T @ np.linalg.solve(K, Zc)).T        # (k, d), rows in span of the inputs
    a = zm - A @ xm
    return A, a


def loo_r2(Fs, Fsq, QGam, lam) -> tuple[float, np.ndarray]:
    """Leave-one-out R^2 of the relational map, and the held-out predictions (n, k)."""
    X = np.asarray(Fs, dtype=np.float64)
    Z = np.asarray(Fsq, dtype=np.float64) @ QGam
    n = X.shape[0]
    pred = np.zeros_like(Z)
    for i in range(n):
        m = np.arange(n) != i
        A, a = fit_relation(X[m], np.asarray(Fsq)[m], QGam, lam)
        pred[i] = A @ X[i] + a
    ss_res = np.sum((Z - pred) ** 2)
    ss_tot = np.sum((Z - Z.mean(0)) ** 2)
    return float(1 - ss_res / ss_tot), pred


def gamma_q_basis(A: np.ndarray, rtol: float = 1e-6) -> np.ndarray:
    """Orthonormal basis of Gamma_q = Im(A^T), A of shape (k, d)."""
    Q, _ = span_basis(A, rtol)
    return Q


def visibility(Gm: np.ndarray, QF: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Logit visibility of the directions of F.

    For a unit u in F, Var_y[g(y)^T u] is how much moving f along u spreads the
    logits over tokens. The right-singular vectors W of Gc QF, with singular
    values sigma, order F's directions from most to least visible. Returns
    (W in ambient coordinates (d, kF), sigma / sigma_max).
    """
    Gc = np.asarray(Gm, dtype=np.float64)
    Gc = Gc - Gc.mean(0, keepdims=True)
    _, s, vt = np.linalg.svd(Gc @ QF, full_matrices=False)
    return QF @ vt.T, s / s[0]
