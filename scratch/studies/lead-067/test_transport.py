"""Tests for transport.py (LEAD-067). Run: python3 -m pytest -q test_transport.py"""

import numpy as np
import pytest

import transport as t


@pytest.fixture
def rng():
    return np.random.default_rng(20261122)


def frame_disagreement(g):
    return min(np.linalg.norm(g[a] - g[b]) for a, b in (("A", "B"), ("B", "C"), ("C", "A")))


# ----------------------------------------------------------------- the null


@pytest.mark.parametrize("d,k", [(2, 2), (3, 3), (5, 6)])
def test_null_has_trivial_holonomy_with_plural_frames(rng, d, k):
    for _ in range(50):
        ctx, g, W = t.null_construction(d, k, rng)
        assert frame_disagreement(g) > 1e-3  # the contexts' coordinates differ
        T, info = t.derive_transports(ctx)
        assert all(i["determined"] for i in info.values())
        for (b, a), R in T.items():  # the derived transport is the frame change
            assert np.allclose(R, g[b] @ g[a].T, atol=1e-10)
        assert t.deviation(t.holonomy(T)) < 1e-10


def test_null_coordinates_disagree_on_every_shared_commitment(rng):
    ctx, g, W = t.null_construction(3, 3, rng)
    for a, b in (("A", "B"), ("B", "C"), ("C", "A")):
        for n in t.shared(ctx, a, b):
            assert np.linalg.norm(ctx[a][n] - ctx[b][n]) > 1e-6


def test_null_glues(rng):
    ctx, g, W = t.null_construction(3, 3, rng)
    T, _ = t.derive_transports(ctx)
    _, worst = t.glue(ctx, T)
    assert worst < 1e-10


# ----------------------------------------------------------------- gauge


def test_transport_and_holonomy_are_covariant(rng):
    ctx, _ = t.planar_construction({"A": 0.3, "B": -0.1, "C": 0.5}, rng=rng)
    T, _ = t.derive_transports(ctx)
    H = t.holonomy(T)
    for _ in range(20):
        h = {c: t.random_orthogonal(2, rng) for c in t.LOOP}
        T2, _ = t.derive_transports(t.regauge(ctx, h))
        for (b, a), R in T.items():
            assert np.allclose(T2[(b, a)], h[b] @ R @ h[a].T, atol=1e-10)
        H2 = t.holonomy(T2)
        assert np.allclose(H2, h["A"] @ H @ h["A"].T, atol=1e-10)
        assert t.deviation(H2) == pytest.approx(t.deviation(H), abs=1e-10)
        assert np.allclose(t.eigen_angles(H2), t.eigen_angles(H), atol=1e-10)


def test_regauge_preserves_each_contexts_comparisons(rng):
    ctx, _, _ = t.null_construction(4, 3, rng)
    h = {c: t.random_orthogonal(4, rng) for c in t.LOOP}
    ctx2 = t.regauge(ctx, h)
    for c in t.LOOP:
        assert np.allclose(t.gram(ctx, c)["G"], t.gram(ctx2, c)["G"])


# ----------------------------------------------------------------- the nontrivial case


@pytest.mark.parametrize(
    "theta",
    [
        {"A": 0.3, "B": -0.1, "C": 0.5},
        {"A": 1.0, "B": 1.0, "C": 1.0},
        {"A": 0.4, "B": -0.9, "C": 0.5},  # sums to zero: flat
    ],
)
def test_planar_holonomy_is_the_sum_of_internal_angles(rng, theta):
    ctx, g = t.planar_construction(theta, rng=rng)
    T, info = t.derive_transports(ctx)
    assert all(i["determined"] and i["residual"] < 1e-10 for i in info.values())
    H = t.holonomy(T)
    total = sum(theta.values())
    expected = abs(np.angle(np.exp(1j * total)))
    assert abs(t.rotation_angle_2d(H)) == pytest.approx(expected, abs=1e-10)
    _, worst = t.glue(ctx, T)
    assert (worst < 1e-10) == (expected < 1e-10)


def test_internal_angle_is_a_comparison_the_context_holds(rng):
    theta = {"A": 0.3, "B": -0.1, "C": 0.5}
    ctx, g = t.planar_construction(theta, rng=rng)
    # A's comparison of its first ca-commitment with its first ab-commitment
    u, v = ctx["A"]["ca0"], ctx["A"]["ab0"]
    cos = u @ v / np.linalg.norm(u) / np.linalg.norm(v)
    assert cos == pytest.approx(np.cos(theta["A"]))


def test_route_discrepancy_is_invariant_and_tracks_holonomy(rng):
    theta = {"A": 0.3, "B": -0.1, "C": 0.5}
    ctx, g = t.planar_construction(theta, rng=rng)
    T, _ = t.derive_transports(ctx)
    rows = t.route_discrepancy(ctx, T, held="A", absent="B", via="C")
    assert rows and max(abs(d - r) for _, _, d, r in rows) > 1e-2
    h = {c: t.random_orthogonal(2, rng) for c in t.LOOP}
    ctx2 = t.regauge(ctx, h)
    T2, _ = t.derive_transports(ctx2)
    rows2 = t.route_discrepancy(ctx2, T2, held="A", absent="B", via="C")
    assert np.allclose([r[2:] for r in rows], [r[2:] for r in rows2], atol=1e-10)
    # in the null the two routes agree
    ctx0, _, _ = t.null_construction(2, 2, rng)
    T0, _ = t.derive_transports(ctx0)
    rows0 = t.route_discrepancy(ctx0, T0, held="A", absent="B", via="C")
    assert max(abs(d - r) for _, _, d, r in rows0) < 1e-10


def test_glue_iff_trivial_holonomy_random(rng):
    """Exact, determined overlaps: gluing succeeds exactly when H = I."""
    for _ in range(200):
        theta = {c: rng.uniform(-np.pi, np.pi) for c in t.LOOP}
        if rng.random() < 0.3:
            theta["C"] = -theta["A"] - theta["B"]
        ctx, _ = t.planar_construction(theta, rng=rng)
        T, _ = t.derive_transports(ctx)
        dev = t.deviation(t.holonomy(T))
        _, worst = t.glue(ctx, T)
        assert (dev < 1e-9) == (worst < 1e-9)


# ----------------------------------------------------------------- curved charts


def test_sphere_charts_holonomy_approaches_spherical_excess(rng):
    s = 0.8
    m = {"A": [1, 0, 0], "B": [np.cos(s), np.sin(s), 0], "C": [np.cos(s), 0, np.sin(s)]}
    errs = []
    for spread in (0.04, 0.01, 0.0025):
        ctx, mm, _ = t.sphere_construction(m, spread, 10, rng)
        T, _ = t.derive_transports(ctx, centred=True)
        H = t.holonomy(T)
        errs.append(abs(abs(t.rotation_angle_2d(H)) - t.spherical_excess(mm)))
    assert errs[-1] < 0.01
    assert errs[-1] < errs[0]


def test_flat_charts_have_trivial_holonomy(rng):
    """Control: the same chart construction on a plane (no curvature) is flat."""
    centres = {"A": np.array([0.0, 0.0]), "B": np.array([1.0, 0.2]), "C": np.array([0.3, 0.9])}
    g = {c: t.random_orthogonal(2, rng) for c in t.LOOP}
    ctx = {c: {} for c in t.LOOP}
    for a, b, p in (("A", "B", "ab"), ("B", "C", "bc"), ("C", "A", "ca")):
        mid = (centres[a] + centres[b]) / 2
        for i in range(6):
            x = mid + 0.05 * rng.standard_normal(2)
            ctx[a][f"{p}{i}"] = g[a] @ (x - centres[a])
            ctx[b][f"{p}{i}"] = g[b] @ (x - centres[b])
    T, _ = t.derive_transports(ctx, centred=True)
    assert t.deviation(t.holonomy(T)) < 1e-10


# ----------------------------------------------------------------- underdetermination


def test_underdetermined_overlap_makes_holonomy_a_choice(rng):
    det, rows = t.underdetermined_family(rng, np.linspace(0, 2 * np.pi, 73))
    assert det is False
    assert max(r[1] for r in rows) < 1e-10  # every member fits exactly
    devs = [r[2] for r in rows]
    assert min(devs) < 0.15 and max(devs) > 1.0


def test_procrustes_flags_rank_deficiency():
    X = np.array([[1.0], [0.0], [0.0]])
    _, _, det = t.procrustes(X, X)
    assert det is False
    X = np.eye(3)
    _, _, det = t.procrustes(X, X)
    assert det is True


def test_noisy_null_is_small_and_scales_with_noise(rng):
    a = np.mean([t.noisy_null(3, 5, 0.01, rng) for _ in range(100)])
    b = np.mean([t.noisy_null(3, 5, 0.1, rng) for _ in range(100)])
    assert 5 < b / a < 20
