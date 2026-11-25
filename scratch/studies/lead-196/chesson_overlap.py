"""Chesson's overlap and fitness for MacArthur's consumer-resource model,
in the notation of CLAIM-369 (A = U^T U, r = U^T b - c).

MacArthur's model, as Chesson (2011, Table 1) states it:
    (1/N_j) dN_j/dt = sum_l c_jl R_l v_l - mu_j
    (1/R_l) dR_l/dt = r_l (1 - R_l / K_l) - sum_j N_j c_jl

Chesson's measures (Table 1):
    s_j   = sqrt(sum_l c_jl^2 v_l K_l / r_l)
    kappa_j = (sum_l c_jl K_l v_l - mu_j) / s_j
    rho_jk  = sum_l c_jl v_l K_l c_kl / r_l / (s_j s_k)

Map used here: u_jl = c_jl sqrt(v_l K_l / r_l), b_l = sqrt(v_l K_l r_l),
c_j = mu_j. Run `python3 -I chesson_overlap.py` for a report, or
`python3 -I -m pytest -q test_chesson_overlap.py` for the tests.
"""
import numpy as np
from scipy.integrate import solve_ivp


def random_model(rng, S=3, M=6):
    c = rng.uniform(0.0, 1.0, size=(S, M))
    v = rng.uniform(0.5, 1.5, size=M)
    K = rng.uniform(0.5, 2.0, size=M)
    r = rng.uniform(0.5, 2.0, size=M)
    mu = rng.uniform(0.05, 0.3, size=S)
    return c, v, K, r, mu


def chesson_measures(c, v, K, r, mu):
    w = v * K / r
    s = np.sqrt((c ** 2 * w).sum(axis=1))
    kappa = ((c * K * v).sum(axis=1) - mu) / s
    rho = (c * w) @ c.T / np.outer(s, s)
    return s, kappa, rho


def feature_form(c, v, K, r, mu):
    """U (columns u_j), b and maintenance cost, so that A = U^T U, r = U^T b - mu."""
    U = (c * np.sqrt(v * K / r)).T
    b = np.sqrt(v * K * r)
    return U, b, mu


def reduced_lv(c, v, K, r, mu):
    """Lotka-Volterra form obtained by substituting the fast-resource
    quasi-steady state R_l = K_l (1 - sum_j N_j c_jl / r_l), valid while
    every R_l stays positive."""
    A = (c * v * K / r) @ c.T
    g = (c * v * K).sum(axis=1) - mu
    return A, g


def invasion_vs_lone_resident(c, v, K, r, mu, i, j):
    """Per-capita growth of rare i against j alone at equilibrium, from the
    reduced LV form."""
    A, g = reduced_lv(c, v, K, r, mu)
    nj = g[j] / A[j, j]
    return g[i] - A[i, j] * nj


def chesson_invasion(c, v, K, r, mu, i, j):
    s, kappa, rho = chesson_measures(c, v, K, r, mu)
    return s[i] * (kappa[i] - rho[i, j] * kappa[j])


def full_model_invasion(c, v, K, r, mu, i, j, T=400.0):
    """Integrate the full consumer-resource model with j alone, then
    evaluate the per-capita growth a rare i would have on the resulting
    resources. Returns (growth, min resource) so the caller can check that
    every resource stayed positive."""
    M = c.shape[1]

    def f(t, y):
        Nj, R = y[0], y[1:]
        dN = Nj * ((c[j] * R * v).sum() - mu[j])
        dR = R * (r * (1 - R / K) - Nj * c[j])
        return np.concatenate([[dN], dR])

    y0 = np.concatenate([[0.1], K.copy()])
    sol = solve_ivp(f, (0, T), y0, rtol=1e-10, atol=1e-12)
    R = sol.y[1:, -1]
    return (c[i] * R * v).sum() - mu[i], R.min()


if __name__ == "__main__":
    rng = np.random.default_rng(196)
    c, v, K, r, mu = random_model(rng, S=2, M=6)
    s, kappa, rho = chesson_measures(c, v, K, r, mu)
    U, b, cost = feature_form(c, v, K, r, mu)
    A, g = reduced_lv(c, v, K, r, mu)
    print("A = U^T U:", np.allclose(A, U.T @ U))
    print("g = U^T b - mu:", np.allclose(g, U.T @ b - cost))
    cos = (U.T @ U) / np.outer(np.linalg.norm(U, axis=0), np.linalg.norm(U, axis=0))
    print("rho = cosine of u_j:", np.allclose(rho, cos))
    print("s_j = |u_j|:", np.allclose(s, np.linalg.norm(U, axis=0)))
    print("kappa_j = g_j/|u_j|:", np.allclose(kappa, g / s))
    alpha = A / g[:, None]  # normalized LV form, alpha_ij = A_ij / g_i
    print("eq (1) kappa_j/kappa_i rho = alpha_ij/alpha_jj:",
          np.isclose(kappa[1] / kappa[0] * rho[0, 1], alpha[0, 1] / alpha[1, 1]))
    print("invasion = |u_i|(kappa_i - rho kappa_j):",
          np.isclose(invasion_vs_lone_resident(c, v, K, r, mu, 0, 1),
                     chesson_invasion(c, v, K, r, mu, 0, 1)))
    mu = mu + 1.5  # keep every resource positive under the resident
    gfull, Rmin = full_model_invasion(c, v, K, r, mu, 0, 1)
    print("full model invasion %.6f, formula %.6f, min R %.3f"
          % (gfull, chesson_invasion(c, v, K, r, mu, 0, 1), Rmin))
