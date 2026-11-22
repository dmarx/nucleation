"""LEAD-137: informative-across-buffer variables vs the gap-isolated block,
in a non-lattice coupled-agent system.

Model (choice, see README): a linear Gaussian VAR(1) system of N coupled
agents, x_{t+1} = A x_t + xi, xi ~ N(0, I). The coupling graph is modular and
NON-lattice: K communities laid out on a PATH (community c couples only to
communities c-1 and c+1), each community a sparse Erdos-Renyi random subgraph
(so there is no lattice regularity inside a community). The path-of-communities
gives spatial locality: community 0 (region R) correlates with the far
communities (environment E) only through the intervening community/communities
(buffer B).

Two variables of region R are compared:

  u_info  "informative across a buffer": the unit direction w in R whose
          scalar coarse variable f = w . x_R carries the most information about
          the far environment x_E. For jointly Gaussian variables I(f; x_E) is
          monotone in the squared canonical correlation, so u_info is the top
          canonical-correlation direction of (x_R, x_E) under the stationary
          covariance Sigma: the leading generalized eigenvector of
          (Sigma_RE Sigma_EE^{-1} Sigma_ER , Sigma_RR). This is QUESTION-065's
          "informativeness about its far environment across a buffer" and the
          analogue of THEORY-205's leading transfer-matrix eigenvector.

  u_block "gap-isolated block" (CLAIM-157): region R's slow collective mode,
          the leading eigenvector of the dynamics restricted to R (A_RR). By
          CLAIM-164 the named unit is the projector onto the block's joint
          mode; for a community block that is its slowest internal mode.

Headline metric: overlap = |<u_info, u_block>| in [0,1] (both unit). Also the
2-D principal-angle overlap and the stationary-metric correlation of the two
coarse variables. Diagnostics confirm R is a genuine gap-isolated block (its
within/across coupling ratio and the spectral gap of A_RR).

All numerics are deterministic given the seed. CPU only, BLAS threads 1.
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov, eigh, eig, subspace_angles


def build_system(K, n, p_in, w_in, w_cross, mode, seed, homogeneous_border=False):
    """Build an N=K*n coupling matrix A for a path-of-communities graph.

    mode: 'symmetric' -> undirected couplings (A symmetric).
          'asymmetric' -> inter-community couplings are one-way, from the
          lower-index community to the higher-index one (upstream drives
          downstream), giving the one-way drive CLAIM-157 cares about.
    homogeneous_border: if True every node of a community connects to the next
          community with equal weight (a lattice-like, homogeneous slab edge).
          If False only a random subset of border nodes bridges, as in a
          generic modular graph.
    A is scaled to spectral radius rho=0.95*? no: caller scales. Here we return
    the raw weighted graph W as A-before-scaling plus community labels.
    """
    rng = np.random.default_rng(seed)
    N = K * n
    labels = np.repeat(np.arange(K), n)
    W = np.zeros((N, N))
    # intra-community Erdos-Renyi edges
    for c in range(K):
        idx = np.where(labels == c)[0]
        for a_i in range(len(idx)):
            for b_i in range(a_i + 1, len(idx)):
                if rng.random() < p_in:
                    w = w_in * (0.5 + rng.random())
                    i, j = idx[a_i], idx[b_i]
                    W[i, j] += w
                    W[j, i] += w  # intra always symmetric
    # inter-community edges between adjacent communities
    for c in range(K - 1):
        src = np.where(labels == c)[0]
        dst = np.where(labels == c + 1)[0]
        if homogeneous_border:
            for i in src:
                for j in dst:
                    w = w_cross
                    W[j, i] += w
                    if mode == 'symmetric':
                        W[i, j] += w
        else:
            # a random sparse subset of border pairs bridge
            n_edges = max(1, int(round(0.25 * len(src))))
            for _ in range(n_edges):
                i = src[rng.integers(len(src))]
                j = dst[rng.integers(len(dst))]
                w = w_cross * (0.5 + rng.random())
                W[j, i] += w
                if mode == 'symmetric':
                    W[i, j] += w
    return W, labels


def scale_to_radius(W, rho):
    """Scale W so its spectral radius is rho (<1 for a stable VAR(1))."""
    ev = np.linalg.eigvals(W)
    r = np.max(np.abs(ev))
    if r == 0:
        return W.copy()
    return (rho / r) * W


def stationary_cov(A):
    """Stationary covariance of x_{t+1}=A x_t + xi, Q=I."""
    N = A.shape[0]
    return solve_discrete_lyapunov(A, np.eye(N))


def partition(labels, K, buffer_width):
    """R = community 0; B = communities 1..buffer_width; E = the rest."""
    idx_R = np.where(labels == 0)[0]
    idx_B = np.where((labels >= 1) & (labels <= buffer_width))[0]
    idx_E = np.where(labels > buffer_width)[0]
    return idx_R, idx_B, idx_E


def info_direction(Sigma, idx_R, idx_E):
    """Top canonical-correlation direction on the R side: the unit w in R
    maximizing the squared correlation of w.x_R with the best predictor from
    x_E. Returns (u_info, top_sq_canonical_corr, full ordered eigvecs)."""
    S_RR = Sigma[np.ix_(idx_R, idx_R)]
    S_EE = Sigma[np.ix_(idx_E, idx_E)]
    S_RE = Sigma[np.ix_(idx_R, idx_E)]
    B = S_RE @ np.linalg.solve(S_EE, S_RE.T)   # symmetric PSD
    B = 0.5 * (B + B.T)
    vals, vecs = eigh(B, S_RR)                  # ascending
    order = np.argsort(vals)[::-1]
    vals, vecs = vals[order], vecs[:, order]
    u = vecs[:, 0]
    u = u / np.linalg.norm(u)
    return u, float(vals[0]), vecs


def block_direction(A, idx_R):
    """R's slow collective mode: leading eigenvector of A_RR (largest real
    part), real part normalized. Returns (u_block, gap, ordered eigvecs)."""
    A_RR = A[np.ix_(idx_R, idx_R)]
    if np.allclose(A_RR, A_RR.T):
        vals, vecs = eigh(A_RR)
        order = np.argsort(vals)[::-1]
        vals, vecs = vals[order], vecs[:, order]
        u = vecs[:, 0].real
        gap = float(vals[0] - vals[1]) if len(vals) > 1 else float(vals[0])
    else:
        vals, vecs = eig(A_RR)
        order = np.argsort(vals.real)[::-1]
        vals, vecs = vals[order], vecs[:, order]
        u = vecs[:, 0].real
        gap = float(vals[0].real - vals[1].real) if len(vals) > 1 else float(vals[0].real)
        vecs = vecs.real
    u = u / np.linalg.norm(u)
    return u, gap, vecs


def near_decomp_ratio(A, idx_R):
    """Simon near-decomposability diagnostic for R as a block: mean |A| inside
    R over mean |A| across R's edge. Large => R is a near-decomposable block."""
    N = A.shape[0]
    mask_R = np.zeros(N, bool)
    mask_R[idx_R] = True
    inside = np.abs(A[np.ix_(idx_R, idx_R)])
    inside_off = inside[~np.eye(len(idx_R), dtype=bool)]
    across = np.abs(A[np.ix_(idx_R, ~mask_R)])
    across2 = np.abs(A[np.ix_(np.where(~mask_R)[0], idx_R)])
    d_in = inside_off.mean() if inside_off.size else 0.0
    e = np.concatenate([across.ravel(), across2.ravel()])
    e_mean = e.mean() if e.size else 0.0
    return float(d_in / e_mean) if e_mean > 0 else np.inf


def overlap(u, v):
    return float(abs(np.dot(u, v)))


def coarse_corr(S_RR, u, v):
    num = abs(u @ S_RR @ v)
    den = np.sqrt((u @ S_RR @ u) * (v @ S_RR @ v))
    return float(num / den) if den > 0 else 0.0


def subspace_overlap(Vinfo, Vblock, k):
    """1 - (2/pi)*mean(principal angles) between the top-k subspaces; 1=same."""
    A1 = Vinfo[:, :k]
    A2 = Vblock[:, :k]
    ang = subspace_angles(A1, A2)
    return float(np.cos(ang).mean())


def run_item(cfg):
    W, labels = build_system(cfg['K'], cfg['n'], cfg['p_in'], cfg['w_in'],
                             cfg['w_cross'], cfg['mode'], cfg['seed'],
                             cfg.get('homogeneous_border', False))
    A = scale_to_radius(W, cfg['rho'])
    Sigma = stationary_cov(A)
    idx_R, idx_B, idx_E = partition(labels, cfg['K'], cfg['buffer_width'])
    u_info, cc2, Vinfo = info_direction(Sigma, idx_R, idx_E)
    u_block, gap, Vblock = block_direction(A, idx_R)
    S_RR = Sigma[np.ix_(idx_R, idx_R)]
    ndr = near_decomp_ratio(A, idx_R)
    k = min(2, len(idx_R))
    out = dict(cfg)
    out.update(
        N=int(W.shape[0]),
        overlap=overlap(u_info, u_block),
        coarse_corr=coarse_corr(S_RR, u_info, u_block),
        subspace2=subspace_overlap(Vinfo, Vblock, k),
        top_sq_canon_corr=cc2,
        block_gap=gap,
        near_decomp_ratio=ndr,
    )
    return out
