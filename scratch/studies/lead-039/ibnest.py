"""Information-bottleneck optima by the lower convex envelope of F_beta, and
the hull test for refinability (THEORY-753). LEAD-039.

F_beta(r) = H(kappa^T r) - H(r)/beta on the simplex of X (nats).
A Lagrangian optimum at beta is a decomposition of p(X) into points on the
lower convex envelope of F_beta (THEORY-753 step 5). On a grid the envelope
is the lower hull of the lifted grid points; the facet whose projection
contains p gives the decoder points.
"""
import itertools

import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def H(v, axis=-1):
    v = np.asarray(v, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(v > 0, -v * np.log(v), 0.0)
    return t.sum(axis=axis)


def F(R, kappa, beta):
    """R: (n, |X|) points of the simplex; kappa: (|X|, |Y|) rows p(Y|x)."""
    return H(R @ kappa) - H(R) / beta


def simplex_grid(k, m):
    """All points of the (k-1)-simplex with coordinates in (1/m)Z."""
    pts = []
    for c in itertools.product(range(m + 1), repeat=k - 1):
        s = sum(c)
        if s <= m:
            pts.append(list(c) + [m - s])
    return np.array(pts, float) / m


def envelope_decomp(p, kappa, beta, grid):
    """Decoder points and weights of the envelope decomposition of p.

    Returns (points, weights) of the lower-hull facet containing p, with
    zero-weight vertices dropped. Grid-exact, so accurate to the grid.
    """
    p = np.asarray(p, float)
    k = len(p)
    if k == 2:
        return _decomp_1d(p, kappa, beta, grid)
    X = grid[:, : k - 1]
    Z = np.column_stack([X, F(grid, kappa, beta)])
    hull = ConvexHull(Z, qhull_options="Qt")
    best = None
    for simplex, eq in zip(hull.simplices, hull.equations):
        if eq[k - 1] >= -1e-12:  # not a lower facet
            continue
        V = X[simplex]  # (k, k-1)
        A = np.vstack([V.T, np.ones(k)])
        try:
            w = np.linalg.solve(A, np.append(p[: k - 1], 1.0))
        except np.linalg.LinAlgError:
            continue
        if w.min() >= -1e-9:
            val = w @ Z[simplex, k - 1]
            if best is None or val < best[0] - 1e-12:
                best = (val, simplex, w)
    _, simplex, w = best
    keep = w > 1e-9
    return grid[simplex][keep], w[keep] / w[keep].sum()


def _decomp_1d(p, kappa, beta, grid):
    order = np.argsort(grid[:, 1])
    G = grid[order]
    x = G[:, 1]
    z = F(G, kappa, beta)
    lower = []  # monotone chain lower hull
    for i in range(len(x)):
        while len(lower) >= 2:
            i1, i2 = lower[-2], lower[-1]
            cross = (x[i2] - x[i1]) * (z[i] - z[i1]) - (z[i2] - z[i1]) * (x[i] - x[i1])
            if cross <= 0:
                lower.pop()
            else:
                break
        lower.append(i)
    t = p[1]
    for a, b in zip(lower[:-1], lower[1:]):
        if x[a] - 1e-12 <= t <= x[b] + 1e-12:
            if x[b] - x[a] < 1e-15:
                return G[[a]], np.array([1.0])
            wb = (t - x[a]) / (x[b] - x[a])
            pts, ws = G[[a, b]], np.array([1 - wb, wb])
            keep = ws > 1e-9
            return pts[keep], ws[keep] / ws[keep].sum()
    raise ValueError("p outside grid range")


def hull_distance(points, hull_pts):
    """Max over points of the L1 distance to conv(hull_pts), by LP."""
    hull_pts = np.atleast_2d(hull_pts)
    m, k = hull_pts.shape
    worst = 0.0
    for q in np.atleast_2d(points):
        # variables: alpha (m), e+ (k), e- (k); min sum e
        c = np.concatenate([np.zeros(m), np.ones(2 * k)])
        A = np.hstack([hull_pts.T, np.eye(k), -np.eye(k)])
        A = np.vstack([A, np.concatenate([np.ones(m), np.zeros(2 * k)])])
        b = np.append(q, 1.0)
        res = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="highs")
        worst = max(worst, res.fun)
    return worst


def lagrangian_values(p, kappa, pts, w):
    """(I(X;T), I(Y;T)) in nats of the encoder with decoder points pts, weights w."""
    p = np.asarray(p, float)
    IX = H(p) - w @ H(pts)
    IY = H(p @ kappa) - w @ H(pts @ kappa)
    return IX, IY


def phi(r, a, b):
    """phi(r) = r(1-r) sum_y (b_y - a_y)^2 / s_y(r), for a two-row channel."""
    r = np.asarray(r, float)[..., None]
    s = (1 - r) * a + r * b
    d2 = (b - a) ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(d2 > 0, d2 * r * (1 - r) / s, 0.0)
    return t.sum(-1)
