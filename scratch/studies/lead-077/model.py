"""CASE-158's design in numpy: frozen low-rank specialist denoisers propose for
one shared latent at each scheduler step; an allocation (spatial grants, or a
contextual router's gate) combines their proposals per region.

Allocators compared (all see audits only from earlier episodes):
  fixed       uniform grants, never revised
  governance  audited competence estimates per (region, specialist), an EMA,
              and grants that move with inertia toward softmax(-competence)
  conformity  the same update, scored by distance of each proposal from the
              combined proposal of the current episode (endogenous, unaudited)
  router      contextual linear score predictor per specialist, refit by
              exponentially forgetting ridge regression on the same audit
              records governance sees; gate = softmax(-predicted score) per
              item and step, from the region id and each specialist's
              captured energy of the current noisy patch

Arms (environment and audit stream), each applied to governance and router
alike:
  full        every proposal probed, independent probes
  cycles      three specialists whose pairwise wins cycle; audits are duels
  scale       each specialist's score reported in its own monotone units
  capture     a fraction of probe slots curated by the region's incumbent
  bandit      each probe audits one specialist, drawn from the allocation
  training    specialists keep training on the regions they are granted
"""
import numpy as np

SIGMAS = np.array([1.0, 0.6, 0.35, 0.2, 0.1])


def _orth(rng, d, m):
    q, _ = np.linalg.qr(rng.standard_normal((d, m)))
    return q[:, :m]


class World:
    """Content types are low-rank Gaussians in a p-dimensional patch."""

    def __init__(self, rng, n_types, p=16, m=4):
        self.p, self.m = p, m
        self.U = [_orth(rng, p, m) for _ in range(n_types)]
        self.lam = [np.sort(rng.uniform(0.5, 2.0, m))[::-1] for _ in range(n_types)]

    def sample(self, rng, t, n):
        z = rng.standard_normal((n, self.m)) * np.sqrt(self.lam[t])
        return z @ self.U[t].T + 0.05 * rng.standard_normal((n, self.p))


def fit_operator(X, rank):
    """A frozen low-rank denoiser: eigenbasis of the training covariance."""
    C = X.T @ X / len(X)
    w, V = np.linalg.eigh(C)
    idx = np.argsort(w)[::-1][:rank]
    return V[:, idx], np.maximum(w[idx], 1e-6)


def denoise(op, Y, sigma):
    """Wiener shrinkage in the operator's subspace. Y: (n, p)."""
    V, lam = op
    return ((Y @ V) * (lam / (lam + sigma ** 2))) @ V.T


def energy_features(ops, Y):
    """Fraction of the noisy patch's energy each operator's subspace captures."""
    tot = np.sum(Y ** 2, axis=1, keepdims=True) + 1e-9
    return np.stack([np.sum((Y @ V) ** 2, axis=1) for V, _ in ops], 1) / tot


def softmax_neg(s, tau):
    """Grants from scores (lower is better), scale-free in the score level."""
    s = np.asarray(s, float)
    z = -(s - s.min(axis=-1, keepdims=True)) / (tau * (np.abs(s).mean(axis=-1, keepdims=True) + 1e-9))
    z = np.exp(z - z.max(axis=-1, keepdims=True))
    return z / z.sum(axis=-1, keepdims=True)


def run_chain(ops, X0, rng, alloc_fn):
    """Denoise images X0 (n, R, p) from sigma_max with combined proposals.
    alloc_fn(r, Y_r, sigma) -> (n, K) weights. Returns final estimate."""
    n, R, p = X0.shape
    Y = X0 + SIGMAS[0] * rng.standard_normal(X0.shape)
    xhat = np.zeros_like(Y)
    for t, s in enumerate(SIGMAS):
        for r in range(R):
            props = np.stack([denoise(op, Y[:, r], s) for op in ops], 1)  # n,K,p
            g = alloc_fn(r, Y[:, r], s)
            xhat[:, r] = np.einsum('nk,nkp->np', g, props)
        if t + 1 < len(SIGMAS):
            Y = xhat + (SIGMAS[t + 1] / s) * (Y - xhat)
    return xhat


def router_features(ops, Y, r, R, sigma):
    e = energy_features(ops, Y)
    onehot = np.zeros((len(Y), R)); onehot[:, r] = 1
    inter = (onehot[:, :, None] * e[:, None, :]).reshape(len(Y), -1)
    return np.hstack([onehot, e, inter, np.full((len(Y), 1), sigma ** 2)])


class Router:
    """Per-specialist linear score predictor, ridge with exponential forgetting."""

    def __init__(self, d, K, forget=0.7, ridge=1e-2, tau=0.1):
        self.A = [ridge * np.eye(d) for _ in range(K)]
        self.b = [np.zeros(d) for _ in range(K)]
        self.w = [np.zeros(d) for _ in range(K)]
        self.forget, self.ridge, self.tau, self.K, self.d = forget, ridge, tau, K, d
        self.fitted = False

    def update(self, F, S):
        """F: (n, d) features; S: (n, K) scores with NaN for unobserved."""
        for k in range(self.K):
            m = ~np.isnan(S[:, k])
            self.A[k] = self.forget * self.A[k] + (1 - self.forget) * self.ridge * np.eye(self.d)
            self.b[k] = self.forget * self.b[k]
            if m.any():
                self.A[k] += F[m].T @ F[m]
                self.b[k] += F[m].T @ S[m, k]
            self.w[k] = np.linalg.solve(self.A[k], self.b[k])
        self.fitted = True

    def predict(self, F):
        return np.stack([F @ w for w in self.w], 1)

    def gate(self, F):
        if not self.fitted:
            return np.full((len(F), self.K), 1.0 / self.K)
        return softmax_neg(self.predict(F), self.tau)


class Governance:
    """Audited competence per (region, specialist) and grants with inertia."""

    def __init__(self, R, K, alpha=0.3, eta=0.3, tau=0.1, standardize=False):
        self.c = np.full((R, K), np.nan)
        self.g = np.full((R, K), 1.0 / K)
        self.alpha, self.eta, self.tau, self.standardize = alpha, eta, tau, standardize
        self.hist = [[] for _ in range(K)]

    def update(self, regions, S):
        R, K = self.c.shape
        if self.standardize:
            # each member scored against its own history (no common scale needed)
            S = S.copy()
            for k in range(K):
                v = S[~np.isnan(S[:, k]), k]
                self.hist[k].extend(v.tolist()); self.hist[k] = self.hist[k][-400:]
                h = np.asarray(self.hist[k])
                if len(h) > 1:
                    S[:, k] = (S[:, k] - h.mean()) / (h.std() + 1e-9)
        for r in range(R):
            sel = regions == r
            for k in range(K):
                v = S[sel, k]; v = v[~np.isnan(v)]
                if len(v) == 0:
                    continue
                m = v.mean()
                self.c[r, k] = m if np.isnan(self.c[r, k]) else (1 - self.alpha) * self.c[r, k] + self.alpha * m
        c = self.c.copy()
        for r in range(R):
            if np.all(np.isnan(c[r])):
                continue
            c[r][np.isnan(c[r])] = np.nanmean(c[r])
            if self.standardize:
                c[r] = c[r] - c[r].min() + 1.0  # shift so softmax_neg scale is defined
            target = softmax_neg(c[r], self.tau)
            self.g[r] = (1 - self.eta) * self.g[r] + self.eta * target
