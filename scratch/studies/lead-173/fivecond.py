"""Exact defects of the five conditions of QUESTION-252 for a linear Gaussian VAR(p).

A model is X_t = sum_k A_k X_{t-k} + eps_t, eps ~ N(0, Sigma), stable.
A description is a linear coarse-graining Y_t = L X_t; a target is Z_t = G X_t.
Everything is computed from exact stationary covariances (no sampling), in
the companion state S_t = (X_t, ..., X_{t-p+1}), which carries the full past.

The declared regime (see README.md):
  P  predictive sufficiency: E[Z_{t+1} | X past] = E[Z_{t+1} | Y_t].
  D  dynamical independence: E[Y_{t+1} | X past] = E[Y_{t+1} | Y past]
     (transfer entropy X -> Y is zero).
  M  memory closure under the Mori projection onto span(Y_t):
     every Mori-Zwanzig memory kernel vanishes, equivalently
     R(k) = Omega^k R(0) for all k, Omega = R(1) R(0)^{-1}.
  A  approximation fidelity: the memoryless reduced model
     Zhat_{t+k} = H Omega^{k-1} Y_t, H = Cov(Z_{t+1}, Y_t) R(0)^{-1},
     has relative excess mean squared error over E[Z_{t+k} | X past]
     at most eps for every k = 1..h.
  C  tractability: the reduced model's state, Y, has dimension m <= b.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import solve_discrete_lyapunov

TOL = 1e-9


def companion(A_list, Sigma):
    A_list = [np.atleast_2d(np.asarray(a, float)) for a in A_list]
    n = A_list[0].shape[0]
    p = len(A_list)
    Ac = np.zeros((n * p, n * p))
    Ac[:n, :] = np.hstack(A_list)
    if p > 1:
        Ac[n:, :-n] = np.eye(n * (p - 1))
    Sc = np.zeros((n * p, n * p))
    Sc[:n, :n] = np.asarray(Sigma, float)
    return Ac, Sc


def lift(M, n, p):
    """A map on X_t (rows act on X_t) lifted to the companion state."""
    M = np.atleast_2d(np.asarray(M, float))
    out = np.zeros((M.shape[0], n * p))
    out[:, :n] = M
    return out


class Model:
    def __init__(self, A_list, Sigma, L, G, name=""):
        self.name = name
        self.A_list = [np.atleast_2d(np.asarray(a, float)) for a in A_list]
        self.n = self.A_list[0].shape[0]
        self.p = len(self.A_list)
        self.Sigma = np.asarray(Sigma, float)
        self.Ac, self.Sc = companion(self.A_list, self.Sigma)
        rho = max(abs(np.linalg.eigvals(self.Ac)))
        if rho >= 1:
            raise ValueError(f"{name}: not stable (spectral radius {rho})")
        self.Pi = solve_discrete_lyapunov(self.Ac, self.Sc)
        self.L = lift(L, self.n, self.p)
        self.G = lift(G, self.n, self.p)
        self.m = self.L.shape[0]

    # --- covariances of Y -------------------------------------------------
    def R(self, k):
        return self.L @ np.linalg.matrix_power(self.Ac, k) @ self.Pi @ self.L.T

    def omega(self):
        return self.R(1) @ np.linalg.inv(self.R(0))

    # --- D: transfer entropy X -> Y ----------------------------------------
    def var_y_given_ypast(self, iters=5000):
        """Innovation covariance of Y in its own law, by the Kalman
        predictor of the companion state from Y's past (Y observed exactly)."""
        Ac, Sc, L = self.Ac, self.Sc, self.L
        P = self.Pi.copy()  # P_{t|t-1}
        prev = None
        for _ in range(iters):
            S = L @ P @ L.T
            K = P @ L.T @ np.linalg.pinv(S)
            Pf = P - K @ L @ P
            P = Ac @ Pf @ Ac.T + Sc
            P = (P + P.T) / 2
            cur = L @ P @ L.T
            if prev is not None and np.max(abs(cur - prev)) < 1e-15:
                break
            prev = cur
        return L @ P @ L.T

    def te(self):
        full = self.L @ self.Sc @ self.L.T
        own = self.var_y_given_ypast()
        return 0.5 * (np.linalg.slogdet(own)[1] - np.linalg.slogdet(full)[1])

    # --- M: Mori-Zwanzig memory under projection onto span(Y_t) ------------
    def memory_cov_defect(self, K=80):
        """max_k ||R(k) - Omega^k R(0)|| / ||R(0)||, k = 1..K."""
        R0 = self.R(0)
        Om = self.omega()
        d = 0.0
        for k in range(1, K + 1):
            d = max(d, np.linalg.norm(self.R(k) - np.linalg.matrix_power(Om, k) @ R0)
                    / np.linalg.norm(R0))
        return d

    def memory_kernels(self, J=30):
        """Norms of the discrete Mori-Zwanzig kernels P K (Q K)^{j-1} Q K P on
        linear functionals of the companion state, inner product <u,v> = u'Pi v,
        Koopman operator v -> Ac' v."""
        Pi, L = self.Pi, self.L
        Kop = self.Ac.T
        Proj = L.T @ np.linalg.inv(L @ Pi @ L.T) @ L @ Pi
        Q = np.eye(Pi.shape[0]) - Proj
        out = []
        QK = Q @ Kop
        mid = np.eye(Pi.shape[0])
        Ct = np.linalg.cholesky(Pi).T  # ||v||_Pi = ||Ct v||
        for _ in range(J):
            Mj = Proj @ Kop @ mid @ Q @ Kop @ Proj
            # Pi-norm of the operator restricted to W
            out.append(np.linalg.norm(Ct @ Mj @ np.linalg.inv(Ct), 2))
            mid = mid @ QK
        return np.array(out)

    # --- P: predictive sufficiency of Y_t for Z_{t+1} ----------------------
    def var_z(self):
        return float((self.G @ self.Pi @ self.G.T)[0, 0]) if self.G.shape[0] == 1 \
            else float(np.trace(self.G @ self.Pi @ self.G.T))

    def H(self):
        C = self.G @ self.Ac @ self.Pi @ self.L.T  # Cov(Z_{t+1}, Y_t)
        return C @ np.linalg.inv(self.R(0))

    def excess(self, k):
        """Relative excess MSE of Zhat_{t+k} = H Omega^{k-1} Y_t over the
        optimal predictor G Ac^k S_t (whose error is orthogonal to S_t)."""
        v = self.G @ np.linalg.matrix_power(self.Ac, k) \
            - self.H() @ np.linalg.matrix_power(self.omega(), k - 1) @ self.L
        return float(np.trace(v @ self.Pi @ v.T)) / self.var_z()

    def p_defect(self):
        # equals excess(1): H Y_t is the best predictor of Z_{t+1} from Y_t
        return self.excess(1)

    def a_defect(self, h):
        return max(self.excess(k) for k in range(1, h + 1))

    # --- all five ------------------------------------------------------------
    def evaluate(self, h=2, eps=0.0, b=2):
        d = dict(
            P=self.p_defect(),
            D=self.te(),
            M=self.memory_cov_defect(),
            A=self.a_defect(h),
            m=self.m,
        )
        tol = TOL
        d["holds"] = dict(
            P=d["P"] <= tol,
            D=d["D"] <= tol,
            M=d["M"] <= tol,
            A=d["A"] <= eps + tol,
            C=self.m <= b,
        )
        return d


def config(holds):
    return "".join("1" if holds[c] else "0" for c in "PDMAC")
