"""Per-feature compatibility complex of the toy model of superposition
(c = 6 features, r = 2 hidden dimensions, high-sparsity limit) at the 5-gon
and 6-gon critical points, and in sampled neighbourhoods of them.
For CASE-tmps4kry. Run with python3 -I. Needs numpy and scipy."""
import numpy as np
from scipy.optimize import minimize

c = 6
mu = np.linspace(0, 1, 4001)          # mu ~ U[0, 1]; trapezoid quadrature

def per_feature(W, b):
    """Demand i: E_mu ||ReLU(W^T W mu e_i + b) - mu e_i||^2."""
    G = W.T @ W
    out = np.empty(c)
    for i in range(c):
        y = np.maximum(np.outer(mu, G[:, i]) + b, 0)
        y[:, i] -= mu
        out[i] = np.trapezoid((y ** 2).sum(1), mu)
    return out

def kgon(k, a, bb):
    ang = 2 * np.pi * np.arange(k) / k
    W = np.zeros((2, c))
    W[:, :k] = a * np.vstack([np.cos(ang), np.sin(ang)])
    b = np.full(c, -1.0)                # unrepresented features: output 0
    b[:k] = bb
    return W, b

rng = np.random.default_rng(0)
for k in (5, 6):
    r = minimize(lambda p: per_feature(*kgon(k, *p)).mean(), [1.0, 0.0],
                 method="Nelder-Mead",
                 options=dict(xatol=1e-8, fatol=1e-10, maxiter=4000))
    W, b = kgon(k, *r.x)
    pf = per_feature(W, b)
    print(f"{k}-gon a,b = {r.x.round(4)}  mean loss = {pf.mean():.5f}")
    print("  per-feature:", pf.round(4))
    # free re-minimisation of all 18 parameters from a small perturbation
    x0 = np.concatenate([W.ravel(), b])
    f = lambda x: per_feature(x[:12].reshape(2, 6), x[12:]).mean()
    rr = minimize(f, x0 + 1e-3 * rng.standard_normal(18), method="L-BFGS-B")
    print(f"  re-minimised from perturbation: {rr.fun:.5f}")
    # neighbourhood: least common tolerance at which some j features are
    # jointly met, j = 1..6, over 3000 samples within radius ~0.05
    best = np.full(c, np.inf)
    for _ in range(3000):
        x = x0 + 0.05 * rng.random() * rng.standard_normal(18)
        best = np.minimum(best, np.sort(per_feature(x[:12].reshape(2, 6), x[12:])))
    print("  neighbourhood, least eps for j = 1..6:", best.round(4))
