"""LEAD-084: finite Markovian augmentation of a linear coarse variable.

Class: X_{t+1} = A X_t + w_t, A stable, w_t ~ N(0, Sigma) iid, Sigma > 0,
and a coarse variable Y_t = L X_t (m x n, full row rank), no observation
noise. Everything is computed from exact stationary covariances.

Quantities:
  Pi        stationary covariance of X.
  P_p       Cov(X_{t+1} | Y_t, ..., Y_{t-p+1}): the Riccati recursion
            started at P_0 = Pi (the Kalman predictor started p steps
            back from the stationary prior).
  P_inf     its limit: Cov(X_{t+1} | whole past of Y).
  E_p       L P_p L^T, the one-step error of predicting Y_{t+1} from p lags.
  A_cl      A - K L with the steady gain K = A P_inf L^T (L P_inf L^T)^-1.
  bound_p   L A_cl^p (Pi - P_inf) A_cl^pT L^T  (the fixed-gain filter's
            excess error; the optimal p-lag predictor does no worse).
"""
import numpy as np
from scipy.linalg import solve_discrete_are


def lyap(A, Q):
    """Solve P = A P A^T + Q (A stable) by vectorisation."""
    n = A.shape[0]
    M = np.eye(n * n) - np.kron(A, A)
    P = np.linalg.solve(M, Q.reshape(-1)).reshape(n, n)
    return (P + P.T) / 2


def riccati_step(P, A, L, S):
    G = L @ P @ L.T
    K = A @ P @ L.T @ np.linalg.inv(G)
    Pn = A @ P @ A.T + S - K @ L @ P @ A.T
    return (Pn + Pn.T) / 2


def riccati_seq(A, L, S, p):
    """[P_0 = Pi, P_1, ..., P_p]."""
    P = lyap(A, S)
    out = [P]
    for _ in range(p):
        P = riccati_step(P, A, L, S)
        out.append(P)
    return out


def steady_iter(A, L, S, tol=1e-14, maxit=20000, accept=1e-10):
    """Steady predicted covariance by iterating the Riccati recursion
    (a cross-check on `steady`)."""
    P = lyap(A, S)
    d = np.inf
    for _ in range(maxit):
        Pn = riccati_step(P, A, L, S)
        d = np.max(np.abs(Pn - P)) / max(1.0, np.max(np.abs(P)))
        P = Pn
        if d < tol:
            return P
    if d < accept:
        return P
    raise RuntimeError("Riccati did not converge (step %.1e)" % d)


def steady(A, L, S):
    """P_inf = Cov(X_{t+1} | Y's whole past), via the reduced filter's
    algebraic Riccati equation (scipy), which has a non-singular
    measurement noise S11: Cov(X_t | Y_<=t) = T^-1 diag(0, P_R) T^-T and
    P_inf = A Cov(X_t | Y_<=t) A^T + S."""
    rf = reduced_filter(A, L, S)
    T = rf["T"]
    m, n = L.shape
    D = np.zeros((n, n))
    D[m:, m:] = rf["P"]
    Ti = np.linalg.inv(T)
    Pft = Ti @ D @ Ti.T
    P = A @ Pft @ A.T + S
    return (P + P.T) / 2


def gain(A, L, P):
    return A @ P @ L.T @ np.linalg.inv(L @ P @ L.T)


def acov_Y(A, L, Pi, k):
    """C_Y(k) = Cov(Y_{t+k}, Y_t) = L A^k Pi L^T."""
    return L @ np.linalg.matrix_power(A, k) @ Pi @ L.T


def regression_error(A, L, S, p):
    """Cov(Y_{t+1} | Y_t..Y_{t-p+1}) from block autocovariances alone:
    an independent check on L P_p L^T."""
    Pi = lyap(A, S)
    m = L.shape[0]
    C = lambda k: acov_Y(A, L, Pi, k) if k >= 0 else acov_Y(A, L, Pi, -k).T
    if p == 0:
        return C(0)
    # past vector (Y_t, Y_{t-1}, ..., Y_{t-p+1})
    G = np.block([[C(j - i) for j in range(p)] for i in range(p)])
    # Cov(Y_{t+1}, Y_{t-i}) = C(i+1)
    c = np.hstack([C(i + 1) for i in range(p)])
    return C(0) - c @ np.linalg.solve(G, c.T)


def excess_and_bound(A, L, S, p):
    Ps = riccati_seq(A, L, S, p)
    Pinf = steady(A, L, S)
    Pi = Ps[0]
    K = gain(A, L, Pinf)
    Acl = A - K @ L
    Ap = np.linalg.matrix_power(Acl, p)
    exc = L @ (Ps[p] - Pinf) @ L.T
    bnd = L @ Ap @ (Pi - Pinf) @ Ap.T @ L.T
    return exc, bnd, Acl


def frame(A, L, S):
    """Coordinates X = T^-1 (Y, R) with R the Pi-orthogonal complement of Y
    (Mori's projection): Cov(Y_t, R_t) = 0. Returns blocks of A and Sigma
    in that frame, and T."""
    Pi = lyap(A, S)
    m, n = L.shape
    # rows of N span {r : r Pi L^T = 0}
    U, s, Vt = np.linalg.svd((Pi @ L.T).T)
    N = Vt[m:]
    T = np.vstack([L, N])
    Ti = np.linalg.inv(T)
    At = T @ A @ Ti
    St = T @ S @ T.T
    return At, St, T


def reduced_filter(A, L, S):
    """Kalman filter of the eliminated R given exact Y, in Mori's frame.
    Returns Atilde = A22 - S21 S11^-1 A12, the reduced closed loop, A22."""
    At, St, T = frame(A, L, S)
    m = L.shape[0]
    A11, A12 = At[:m, :m], At[:m, m:]
    A21, A22 = At[m:, :m], At[m:, m:]
    S11, S21, S22 = St[:m, :m], St[m:, :m], St[m:, m:]
    Atil = A22 - S21 @ np.linalg.solve(S11, A12)
    Q = S22 - S21 @ np.linalg.solve(S11, S21.T)
    # Cov(R_t | Y_<=t): Kalman filter of R with measurement
    # z_t = Y_{t+1} - A11 Y_t = A12 R_t + w1, process noise decorrelated
    P = solve_discrete_are(Atil.T, A12.T, Q, S11)
    P = (P + P.T) / 2
    G = A12 @ P @ A12.T + S11
    Kf = P @ A12.T @ np.linalg.inv(G)
    Acl_r = Atil @ (np.eye(P.shape[0]) - Kf @ A12)
    return dict(Atil=Atil, A22=A22, A12=A12, Acl_r=Acl_r, P=P, T=T, Q=Q, S11=S11,
                Pf=P - Kf @ A12 @ P)


def lyap_safe(A, Q):
    return lyap(A, Q)


def rho(M):
    return 0.0 if M.size == 0 else float(np.max(np.abs(np.linalg.eigvals(M))))


def num_rank(M, tol=1e-12):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * max(1.0, s[0])))


def obs_matrix(A, L):
    n = A.shape[0]
    return np.vstack([L @ np.linalg.matrix_power(A, k) for k in range(n)])


def k_min(A, L, S):
    """Fewest coordinates s_t (functions of Y's past) such that (Y_t, s_t)
    determines the law of Y's future given Y's whole past:
    rank Cov(O xhat_{t+1|t} | Y_t)."""
    Pi = lyap(A, S)
    Pinf = steady(A, L, S)
    G = L @ Pinf @ L.T
    Pf = Pinf - Pinf @ L.T @ np.linalg.solve(G, L @ Pinf)
    O = obs_matrix(A, L)
    Sx = Pi - Pinf                     # Cov(xhat_{t+1|t})
    Cxy = A @ (Pi - Pf) @ L.T          # Cov(xhat_{t+1|t}, Y_t)
    Ccond = Sx - Cxy @ np.linalg.solve(L @ Pi @ L.T, Cxy.T)
    return num_rank(O @ Ccond @ O.T)


def augmented_error(A, L, S, W):
    """One-step error of predicting Y_{t+1} from (Y_t, W xhat_{t+1|t})."""
    Pi = lyap(A, S)
    Pinf = steady(A, L, S)
    G = L @ Pinf @ L.T
    Pf = Pinf - Pinf @ L.T @ np.linalg.solve(G, L @ Pinf)
    Sx = Pi - Pinf
    Cxy = A @ (Pi - Pf) @ L.T
    # regressors z = (Y_t, W xhat); target Y_{t+1}
    Czz = np.block([[L @ Pi @ L.T, (W @ Cxy).T], [W @ Cxy, W @ Sx @ W.T]])
    # Cov(Y_{t+1}, Y_t) = L A Pi L^T ; Cov(Y_{t+1}, xhat) = L Sx  (since
    # Y_{t+1} = L xhat + innovation, innovation orthogonal to the past)
    Cyz = np.hstack([L @ A @ Pi @ L.T, L @ Sx @ W.T])
    return L @ Pi @ L.T - Cyz @ np.linalg.pinv(Czz) @ Cyz.T


def predictive_coords(A, L, S):
    """W whose rows give k_min memory coordinates W xhat_{t+1|t}: the range
    of O Cov(xhat | Y_t) O^T pulled back (least squares) to x."""
    Pi = lyap(A, S)
    Pinf = steady(A, L, S)
    G = L @ Pinf @ L.T
    Pf = Pinf - Pinf @ L.T @ np.linalg.solve(G, L @ Pinf)
    Sx = Pi - Pinf
    Cxy = A @ (Pi - Pf) @ L.T
    Ccond = Sx - Cxy @ np.linalg.solve(L @ Pi @ L.T, Cxy.T)
    O = obs_matrix(A, L)
    M = O @ Ccond @ O.T
    k = num_rank(M)
    U, s, _ = np.linalg.svd(M)
    # scale each coordinate to unit conditional variance, for conditioning
    return (U[:, :k] / np.sqrt(s[:k])).T @ O, k


def mz_kernels(A, L, S, J):
    """Mori-Zwanzig memory kernels M_j = K12 K22^{j-1} K21 (j = 1..J) for
    Mori's projection onto span(Y_t), in a Pi-orthonormal basis (NOTE-989)."""
    Pi = lyap(A, S)
    w, V = np.linalg.eigh(Pi)
    Ph = V @ np.diag(np.sqrt(w)) @ V.T
    Phi = V @ np.diag(1 / np.sqrt(w)) @ V.T
    Aw = Phi @ A @ Ph
    Lw = L @ Ph
    Q, _ = np.linalg.qr(np.hstack([Lw.T, np.random.default_rng(0).standard_normal((A.shape[0], A.shape[0]))]))
    m = L.shape[0]
    Kop = Q.T @ Aw.T @ Q
    K12, K21, K22 = Kop[:m, m:], Kop[m:, :m], Kop[m:, m:]
    return [K12 @ np.linalg.matrix_power(K22, j - 1) @ K21 for j in range(1, J + 1)], (K12, K21, K22)


def mz_hankel_rank(A, L, S):
    n = A.shape[0]
    Ms, (K12, K21, K22) = mz_kernels(A, L, S, 2 * n + 2)
    m = L.shape[0]
    N = n + 1
    H = np.block([[Ms[i + j] for j in range(N)] for i in range(N)])
    return num_rank(H)


def krylov_dim(A, L):
    """dim of the smallest A^T-invariant subspace containing row(L):
    the augmentation that is exactly dynamically independent (NOTE-989)."""
    n = A.shape[0]
    B = np.vstack([L @ np.linalg.matrix_power(A, k) for k in range(n)])
    return num_rank(B)


def transfer_entropy_Y(A, L, S):
    """T(X -> Y) with Y's whole past: 1/2 log det(L P_inf L^T)/det(L S L^T)."""
    Pinf = steady(A, L, S)
    return 0.5 * (np.linalg.slogdet(L @ Pinf @ L.T)[1] - np.linalg.slogdet(L @ S @ L.T)[1])


def transfer_entropy_Z(A, L, S, W):
    """T(X -> Z), Z = (Y, W xhat), computed directly: the innovation of
    Z_{t+1} given Z's past against given X_t. Z_{t+1} = (Y_{t+1}, W xhat_{t+2|t+1}),
    xhat_{t+2|t+1} = A xhat + K e_{t+1}; given X_t (and the past), the
    residual is (L w, W K L w) since e_{t+1} = L(X_{t+1} - xhat) ..."""
    Pinf = steady(A, L, S)
    K = gain(A, L, Pinf)
    n = A.shape[0]
    m = L.shape[0]
    # Z_{t+1} - E[.|Y past] = F e_{t+1}, e = Y_{t+1} - L xhat, Cov e = L Pinf L^T
    F = np.vstack([np.eye(m), W @ K])
    Cz_y = F @ (L @ Pinf @ L.T) @ F.T
    # given X_t and Y past: Y_{t+1} - L A X_t = L w, so residual F L w
    Cz_x = F @ (L @ S @ L.T) @ F.T
    # both singular when rows of F are dependent: use the range of F
    U, s, _ = np.linalg.svd(F)
    r = num_rank(F)
    B = U[:, :r]
    a = np.linalg.slogdet(B.T @ Cz_y @ B)[1]
    b = np.linalg.slogdet(B.T @ Cz_x @ B)[1]
    return 0.5 * (a - b)


def random_model(n, m, rng, radius=0.95, corr=True):
    A = rng.standard_normal((n, n))
    A *= radius * rng.uniform(0.3, 1.0) / rho(A)
    if corr:
        B = rng.standard_normal((n, n))
        S = B @ B.T / n + 0.05 * np.eye(n)
    else:
        S = np.diag(rng.uniform(0.2, 1.5, n))
    L = rng.standard_normal((m, n))
    return A, L, S


def joint_state(A, L, S, W):
    """V_t = (X_t, xhat_{t+1|t}) is itself a VAR(1):
    V_{t+1} = F V_t + G w_t. Returns F, G Sigma G^T and the readout M with
    Z_t = M V_t = (Y_t, W xhat_{t+1|t})."""
    n = A.shape[0]
    Pinf = steady(A, L, S)
    K = gain(A, L, Pinf)
    F = np.block([[A, np.zeros((n, n))], [K @ L @ A, A - K @ L]])
    G = np.vstack([np.eye(n), K @ L])
    M = np.block([[L, np.zeros((L.shape[0], n))],
                  [np.zeros((W.shape[0], n)), W]])
    return F, G @ S @ G.T, M


def cond_cov_lags(F, Q, M, p, extra=False):
    """Cov(Z_{t+1} | Z_t, ..., Z_{t-p+1} [, and V_t]) for Z = M V,
    V_{t+1} = F V_t + noise(Q), from exact stationary covariances."""
    Pv = lyap(F, Q)
    C = lambda k: M @ np.linalg.matrix_power(F, k) @ Pv @ M.T  # Cov(Z_{t+k}, Z_t)
    blocks = []
    for i in range(p):
        blocks.append([C(j - i) if j >= i else C(i - j).T for j in range(p)])
    Gz = np.block(blocks)
    cz = np.hstack([C(i + 1) for i in range(p)])
    if extra:
        # Cov(Z_{t-i}, V_t) = M Pv (F^i)^T
        Cv = np.vstack([M @ Pv @ np.linalg.matrix_power(F, i).T for i in range(p)])
        Gz = np.block([[Gz, Cv], [Cv.T, Pv]])
        cz = np.hstack([cz, M @ F @ Pv])
    R = C(0) - cz @ np.linalg.pinv(Gz, rcond=1e-12, hermitian=True) @ cz.T
    return (R + R.T) / 2


def markov_defect(F, Q, M, K=None):
    """A stationary Gaussian Z is Markov iff C(k) = C(1)C(0)^-1 C(k-1) for
    every k >= 1. Returns max_k |C(k) - Omega^k C(0)| in whitened
    coordinates (scale-free), k = 1..K."""
    Pv = lyap(F, Q)
    K = K or 2 * F.shape[0] + 2
    C0 = M @ Pv @ M.T
    w, V = np.linalg.eigh(C0)
    Wh = V @ np.diag(1 / np.sqrt(w)) @ V.T
    C = lambda k: Wh @ M @ np.linalg.matrix_power(F, k) @ Pv @ M.T @ Wh
    Om = C(1)
    return max(float(np.abs(C(k) - np.linalg.matrix_power(Om, k)).max()) for k in range(1, K + 1))


def logdet_range(Cbig, Csmall, tol=1e-10):
    """1/2 log det(Cbig)/det(Csmall) on the range of Cbig."""
    w, V = np.linalg.eigh(Cbig)
    keep = w > tol * max(1.0, w.max())
    B = V[:, keep]
    return 0.5 * (np.linalg.slogdet(B.T @ Cbig @ B)[1] - np.linalg.slogdet(B.T @ Csmall @ B)[1])


def contraction_factor(A, L, S):
    """c = sqrt(1 - lambda_min(P_R^-1 Q)): the reduced closed loop is a
    contraction by c in the norm |v| = |P_R^-1/2 v|, so rho(A_cl) <= c."""
    rf = reduced_filter(A, L, S)
    P, Q = rf["P"], rf["Q"]
    lam = np.min(np.real(np.linalg.eigvals(np.linalg.solve(P, Q))))
    c = np.sqrt(max(0.0, 1 - lam))
    w, V = np.linalg.eigh(P)
    Ph = V @ np.diag(np.sqrt(w)) @ V.T
    Phi = V @ np.diag(1 / np.sqrt(w)) @ V.T
    normed = np.linalg.norm(Phi @ rf["Acl_r"] @ Ph, 2)
    return c, normed, rf


def ma_zeros_scalar(A, L, S):
    """For scalar Y: the minimum-phase zeros of phi(B) Y, phi = det(I - A B),
    from its autocovariances (CLAIM-398's moving-average part)."""
    n = A.shape[0]
    phi = np.poly(A)  # phi(B) = sum_k phi[k] B^k
    Pi = lyap(A, S)
    gam = lambda k: (acov_Y(A, L, Pi, k) if k >= 0 else acov_Y(A, L, Pi, -k).T)[0, 0]
    q = n - 1
    g = [sum(phi[i] * phi[j] * gam(k + j - i) for i in range(n + 1) for j in range(n + 1))
         for k in range(q + 1)]
    coeffs = np.array(g[::-1] + g[1:])  # z^q g(z), highest power first
    r = np.roots(coeffs)
    return np.sort_complex(r[np.abs(r) < 1])


def exact_discretization(Ac, h):
    """A_h = exp(Ac h) and Sigma_h = int_0^h e^{Ac s} e^{Ac^T s} ds (unit
    white noise), by Van Loan's block exponential."""
    from scipy.linalg import expm
    n = Ac.shape[0]
    M = np.block([[-Ac, np.eye(n)], [np.zeros((n, n)), Ac.T]]) * h
    E = expm(M)
    Ah = E[n:, n:].T
    Sh = Ah @ E[:n, n:]
    return Ah, (Sh + Sh.T) / 2
