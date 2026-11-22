"""Finite evaluative transport for LEAD-067 (QUESTION-130, A19 section 8).

Three contexts A, B, C. Each context holds a local representation of some
commitments: a vector in R^d for each commitment it holds, in its own
coordinates. Each pair of contexts overlaps in the commitments both hold
(the "anchors" of that overlap). Nothing here is chosen by the modeller
once the contexts are given:

* the transport T[b, a] : V_a -> V_b is DERIVED from the overlap, as the
  orthogonal map that best carries a's representations of the shared
  anchors onto b's (orthogonal Procrustes);
* it is determined (unique) exactly when the cross-covariance
  M = Y X^T of the anchors is nonsingular, in particular only if the
  anchors span R^d;
* the holonomy of the loop A -> B -> C -> A is H_A = T[A,C] T[C,B] T[B,A].

The gauge group is O(d): a change of a context's local coordinates is
v -> g v with g orthogonal, which preserves every inner product the context
holds (its comparisons among commitments). Under it the derived transport
goes to g_b T g_a^{-1} and the holonomy to g_A H g_A^{-1}.
"""

from __future__ import annotations

import numpy as np

LOOP = ("A", "B", "C")


# ---------------------------------------------------------------- basics


def rot2(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def random_orthogonal(d: int, rng: np.random.Generator) -> np.ndarray:
    """Haar-random element of O(d)."""
    q, r = np.linalg.qr(rng.standard_normal((d, d)))
    return q * np.sign(np.diag(r))


def shared(ctx: dict, a: str, b: str) -> list[str]:
    return sorted(set(ctx[a]) & set(ctx[b]))


def stack(ctx: dict, c: str, names: list[str]) -> np.ndarray:
    """Columns are context c's representations of the named commitments."""
    return np.column_stack([ctx[c][n] for n in names])


# ---------------------------------------------------------------- transport


def procrustes(X: np.ndarray, Y: np.ndarray, tol: float = 1e-9):
    """Orthogonal R minimizing ||R X - Y||_F.

    Returns (R, residual, determined). `determined` is False when the
    minimizer is not unique (some singular value of Y X^T vanishes), in
    which case R is one minimizer among a continuum and any holonomy
    computed from it carries the modeller's choice.
    """
    M = Y @ X.T
    U, s, Vt = np.linalg.svd(M)
    R = U @ Vt
    residual = float(np.linalg.norm(R @ X - Y))
    scale = max(1.0, float(s.max()) if s.size else 1.0)
    determined = bool(s.min() > tol * scale)
    return R, residual, determined


def derive_transports(ctx: dict, loop=LOOP, centred: bool = False):
    """T[(b, a)] for each consecutive pair of the loop and its reverse.

    With centred=True the overlap's comparisons are the differences among
    its shared commitments (each chart's origin is its own reference point,
    not a shared neutral evaluation), so the anchors are centred before the
    fit and T is the linear part of a rigid motion.
    """
    T, info = {}, {}
    n = len(loop)
    for i in range(n):
        a, b = loop[i], loop[(i + 1) % n]
        names = shared(ctx, a, b)
        X, Y = stack(ctx, a, names), stack(ctx, b, names)
        if centred:
            X = X - X.mean(axis=1, keepdims=True)
            Y = Y - Y.mean(axis=1, keepdims=True)
        R, res, det = procrustes(X, Y)
        T[(b, a)] = R
        T[(a, b)] = R.T
        info[(b, a)] = {"anchors": names, "residual": res, "determined": det}
    return T, info


def holonomy(T: dict, loop=LOOP) -> np.ndarray:
    """H based at loop[0]: go loop[0] -> loop[1] -> ... -> loop[0]."""
    n = len(loop)
    d = T[(loop[1], loop[0])].shape[0]
    H = np.eye(d)
    for i in range(n):
        a, b = loop[i], loop[(i + 1) % n]
        H = T[(b, a)] @ H
    return H


def deviation(H: np.ndarray) -> float:
    """||H - I||_F, a class function (invariant under conjugation by O(d))."""
    return float(np.linalg.norm(H - np.eye(H.shape[0])))


def rotation_angle_2d(H: np.ndarray) -> float:
    """Signed angle of a 2x2 rotation, in (-pi, pi]."""
    return float(np.arctan2(H[1, 0], H[0, 0]))


def eigen_angles(H: np.ndarray) -> np.ndarray:
    """Sorted |arg| of the eigenvalues of an orthogonal H (a class function)."""
    return np.sort(np.abs(np.angle(np.linalg.eigvals(H))))


# ---------------------------------------------------------------- gauge


def regauge(ctx: dict, g: dict) -> dict:
    """Change every context's local coordinates: v -> g[c] v."""
    return {c: {n: g[c] @ v for n, v in ctx[c].items()} for c in ctx}


def gram(ctx: dict, c: str) -> dict:
    """Context c's comparisons: inner products among the commitments it holds."""
    names = sorted(ctx[c])
    X = stack(ctx, c, names)
    return dict(names=names, G=X.T @ X)


# ---------------------------------------------------------------- gluing


def glue(ctx: dict, T: dict, base: str = "A", loop=LOOP):
    """Try to place every commitment in one configuration, in base's frame.

    Each context's representations are carried to the base along the open
    path base <- loop[1] <- ... (the tree that omits the edge back into
    the base, here C -> A is replaced by C -> B -> A).
    Returns (config, inconsistency): the largest disagreement between two
    contexts' placements of the same commitment.
    """
    assert base == loop[0]
    to_base = {loop[0]: np.eye(T[(loop[1], loop[0])].shape[0])}
    for i in range(1, len(loop)):
        prev, cur = loop[i - 1], loop[i]
        to_base[cur] = to_base[prev] @ T[(prev, cur)]
    placed: dict[str, list[np.ndarray]] = {}
    for c in loop:
        for n, v in ctx[c].items():
            placed.setdefault(n, []).append(to_base[c] @ v)
    config, worst = {}, 0.0
    for n, vs in placed.items():
        config[n] = vs[0]
        for v in vs[1:]:
            worst = max(worst, float(np.linalg.norm(v - vs[0])))
    return config, worst


def route_discrepancy(ctx: dict, T: dict, held: str, absent: str, via: str):
    """Comparisons a context imports by two routes.

    For a commitment `n` that `held` does not hold but `absent` does, held
    can import it directly (T[held, absent]) or through `via`
    (T[held, via] T[via, absent]). Returns, for each such n and each
    commitment m that `held` holds, the two imported inner products
    <m, T n>. Both are gauge-invariant; they differ exactly when the
    holonomy moves the imported vector.
    """
    out = []
    for n in sorted(set(ctx[absent]) - set(ctx[held])):
        v = ctx[absent][n]
        direct = T[(held, absent)] @ v
        routed = T[(held, via)] @ T[(via, absent)] @ v
        for m in sorted(ctx[held]):
            w = ctx[held][m]
            out.append((m, n, float(w @ direct), float(w @ routed)))
    return out


# ---------------------------------------------------------------- constructions


def null_construction(d: int, k: int, rng: np.random.Generator, frames=None):
    """The null: one configuration of commitments, three local frames.

    Commitments live in one configuration W in R^d (k per overlap, so 3k in
    all; the overlap A&B holds ab0..ab{k-1}, and so on). Context c holds
    the commitments of its two overlaps, represented as g_c w with g_c a
    random (or given) element of O(d). The three frames differ, so the
    contexts disagree in every coordinate: perspectival plurality.
    """
    names = {("A", "B"): "ab", ("B", "C"): "bc", ("C", "A"): "ca"}
    W = {f"{p}{i}": rng.standard_normal(d) for p in names.values() for i in range(k)}
    g = frames or {c: random_orthogonal(d, rng) for c in LOOP}
    ctx = {c: {} for c in LOOP}
    for (a, b), p in names.items():
        for i in range(k):
            n = f"{p}{i}"
            ctx[a][n] = g[a] @ W[n]
            ctx[b][n] = g[b] @ W[n]
    return ctx, g, W


def planar_construction(theta: dict, shape=(1.0, 0.7, 1.1), frames=None, rng=None):
    """A nontrivial case in R^2 built from each context's own comparisons.

    Each overlap is a pair of commitments with the same shape in both
    contexts that hold it (lengths r1, r2 at angle phi), so every overlap
    fit is exact and determined. Inside context c the pair of its
    incoming overlap and the pair of its outgoing overlap sit at a relative
    angle theta[c], an inner-product fact internal to c (how c compares a
    commitment it shares with one neighbour to one it shares with the
    other). Nothing about the transports is specified.
    """
    r1, r2, phi = shape
    pair = [np.array([r1, 0.0]), r2 * np.array([np.cos(phi), np.sin(phi)])]
    rng = rng or np.random.default_rng(0)
    g = frames or {c: random_orthogonal(2, rng) for c in LOOP}
    incoming = {"A": "ca", "B": "ab", "C": "bc"}
    outgoing = {"A": "ab", "B": "bc", "C": "ca"}
    ctx = {c: {} for c in LOOP}
    for c in LOOP:
        for i, u in enumerate(pair):
            ctx[c][f"{incoming[c]}{i}"] = g[c] @ u
            ctx[c][f"{outgoing[c]}{i}"] = g[c] @ rot2(theta[c]) @ u
    return ctx, g


def sphere_construction(centres, spread: float, k: int, rng, frames=None):
    """Local linear charts of a curved space of commitments.

    Commitments are unit vectors in R^3 (normalized evaluative profiles).
    Context c is centred on the unit vector m_c and represents each
    commitment it holds by the log map at m_c (a 2-vector in the tangent
    plane, in a frame of c's own). The overlap of a and b holds k
    commitments scattered with angular radius `spread` around the geodesic
    midpoint of m_a and m_b. All three contexts are exact local charts of
    one configuration; what they cannot do is glue in two dimensions.
    """
    m = {c: np.asarray(centres[c], float) / np.linalg.norm(centres[c]) for c in LOOP}
    frames = frames or {c: random_orthogonal(2, rng) for c in LOOP}
    basis = {}
    for c in LOOP:
        e1 = np.cross(m[c], [0.3, 0.5, 0.8])
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(m[c], e1)
        basis[c] = np.vstack([e1, e2])  # 2 x 3

    def log_map(c, x):
        cosang = np.clip(m[c] @ x, -1, 1)
        ang = np.arccos(cosang)
        t = x - cosang * m[c]
        nt = np.linalg.norm(t)
        v = np.zeros(3) if nt < 1e-15 else ang * t / nt
        return frames[c] @ (basis[c] @ v)

    ctx = {c: {} for c in LOOP}
    points = {}
    for a, b, p in (("A", "B", "ab"), ("B", "C", "bc"), ("C", "A", "ca")):
        mid = m[a] + m[b]
        mid /= np.linalg.norm(mid)
        for i in range(k):
            x = mid + spread * rng.standard_normal(3)
            x /= np.linalg.norm(x)
            n = f"{p}{i}"
            points[n] = x
            ctx[a][n] = log_map(a, x)
            ctx[b][n] = log_map(b, x)
    return ctx, m, points


def spherical_excess(m: dict) -> float:
    """Area of the geodesic triangle with vertices m_A, m_B, m_C on S^2."""
    a, b, c = (m[x] for x in LOOP)
    num = abs(a @ np.cross(b, c))
    den = 1 + a @ b + b @ c + c @ a
    return float(2 * np.arctan2(num, den))


def rotation_about(u: np.ndarray, phi: float) -> np.ndarray:
    """Rotation of R^3 by phi about the unit axis u (Rodrigues)."""
    u = u / np.linalg.norm(u)
    K = np.array([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])
    return np.eye(3) + np.sin(phi) * K + (1 - np.cos(phi)) * K @ K


def underdetermined_family(rng, phis):
    """An overlap that does not span leaves the transport, and so the holonomy, free.

    The null construction in R^3, except that A and B share ONE commitment.
    Procrustes is then not determined: if R fits, so does R composed with
    any rotation about A's representation of the shared commitment (and,
    in O(3), a reflected family besides; the SO(3) family is enough). Every
    member of that family fits the overlap exactly, and the holonomy runs
    over a whole range as the free angle does. Returns the family's
    residuals and holonomy deviations, and the fit's `determined` flag.
    """
    frames = {}
    for c in LOOP:  # proper rotations, so the SO(3) family contains the true frame change
        q = random_orthogonal(3, rng)
        frames[c] = q if np.linalg.det(q) > 0 else -q
    ctx, g, W = null_construction(3, 3, rng, frames=frames)
    for c in ("A", "B"):
        for n in ("ab1", "ab2"):
            del ctx[c][n]
    T, info = derive_transports(ctx)
    u, w = ctx["A"]["ab0"], ctx["B"]["ab0"]
    X, Y = stack(ctx, "A", ["ab0"]), stack(ctx, "B", ["ab0"])
    # one exact fit in SO(3): the rotation in the plane of u and w taking u to w
    axis = np.cross(u, w)
    ang = np.arctan2(np.linalg.norm(axis), u @ w)
    R0 = rotation_about(axis, ang)
    rows = []
    for phi in phis:
        Tphi = dict(T)
        R = R0 @ rotation_about(u, phi)
        Tphi[("B", "A")], Tphi[("A", "B")] = R, R.T
        rows.append((float(phi), float(np.linalg.norm(R @ X - Y)), deviation(holonomy(Tphi))))
    return info[("B", "A")]["determined"], rows


def noisy_null(d: int, k: int, sigma: float, rng):
    """The null with each context's representations perturbed by N(0, sigma^2)."""
    ctx, g, W = null_construction(d, k, rng)
    noisy = {c: {n: v + sigma * rng.standard_normal(d) for n, v in ctx[c].items()} for c in ctx}
    T, info = derive_transports(noisy)
    return deviation(holonomy(T))
