"""Two-dimensional Ising model on periodic L x L lattices, numpy only.

Spins are int8 arrays of shape (B, L, L), B independent replicas.
Coupling K = J / T (k_B = 1), field zero throughout the sampling: the Fisher
metric is evaluated at the ordinary Ising point, as in THEORY-777.

Contents
- swendsen_wang: SW cluster update, optionally with frozen sites (for
  sampling the free spins conditional on an observed sublattice).
- heat_bath: checkerboard heat-bath sweep, optionally with frozen sites.
- metropolis: checkerboard Metropolis sweep (a cross-check in the tests).
- label_clusters: connected components on the periodic square lattice for
  given bond masks (union by hooking + pointer jumping, vectorized).
- observables: the 13 sufficient statistics (field + 12 two-spin couplings).
- rb_given_black: their exact conditional means given the black sublattice.
- observed_mask: the sites kept after k checkerboard decimations.
"""
import numpy as np

K_C = 0.5 * np.log(1.0 + np.sqrt(2.0))  # critical coupling, J/T_c

# Two-spin offsets: every offset in the 5 x 5 box around the origin, up to
# sign (12 of them), vertical and horizontal separate. With the field this
# is 13 parameters, the main-text count of Machta et al. (THEORY-777).
OFFSETS = [(0, 1), (1, 0), (1, 1), (1, -1),
           (0, 2), (2, 0), (1, 2), (2, 1), (1, -2), (2, -1),
           (2, 2), (2, -2)]
PARAM_NAMES = ["h"] + ["J%+d%+d" % o for o in OFFSETS]
NPARAM = 1 + len(OFFSETS)


def shift(s, di, dj):
    """s[..., i+di, j+dj] with periodic boundaries."""
    return np.roll(s, (-di, -dj), axis=(-2, -1))


def random_spins(rng, B, L):
    return np.where(rng.random((B, L, L)) < 0.5, 1, -1).astype(np.int8)


def energy_mag(s):
    """Nearest-neighbour energy E = -sum s_i s_j and magnetisation M, per replica."""
    s = s.astype(np.int64)
    e = -(s * shift(s, 0, 1)).sum(axis=(-2, -1)) - (s * shift(s, 1, 0)).sum(axis=(-2, -1))
    m = s.sum(axis=(-2, -1))
    return e, m


# ---------------------------------------------------------------- labelling

def label_clusters(bond_r, bond_d):
    """Connected components of the periodic lattice graph.

    bond_r[b, i, j]: edge between (i, j) and (i, j+1); bond_d: (i, j)-(i+1, j).
    Returns int64 labels of shape (B, L, L); each label is the smallest flat
    index (over the whole batch) of a site in the component.
    """
    B, L, _ = bond_r.shape
    N = L * L
    idx = np.arange(B * N, dtype=np.int64).reshape(B, L, L)
    ea = np.concatenate([idx[bond_r], idx[bond_d]])
    eb = np.concatenate([shift(idx, 0, 1)[bond_r], shift(idx, 1, 0)[bond_d]])
    lab = np.arange(B * N, dtype=np.int64)
    if ea.size == 0:
        return lab.reshape(B, L, L)
    while True:
        la, lb = lab[ea], lab[eb]
        diff = la != lb
        if not diff.any():
            break
        la, lb = la[diff], lb[diff]
        m = np.minimum(la, lb)
        np.minimum.at(lab, la, m)
        np.minimum.at(lab, lb, m)
        while True:  # pointer jumping to the roots
            nl = lab[lab]
            if np.array_equal(nl, lab):
                break
            lab = nl
    return lab.reshape(B, L, L)


def geometric_bonds(s):
    """Bonds between aligned nearest neighbours (geometric spin clusters)."""
    return s == shift(s, 0, 1), s == shift(s, 1, 0)


# ---------------------------------------------------------------- updates

def swendsen_wang(s, K, rng, frozen=None):
    """One Swendsen-Wang update at coupling K, field zero, in place.

    frozen: bool (L, L) or (B, L, L) mask of sites held fixed; a cluster that
    contains a frozen site is not flipped. This samples the free spins from
    their conditional law given the frozen ones (the frozen spins act as a
    fixed boundary), so it can be used for compatible Monte Carlo.
    Returns the FK cluster labels.
    """
    p = 1.0 - np.exp(-2.0 * K)
    br, bd = geometric_bonds(s)
    br &= rng.random(s.shape) < p
    bd &= rng.random(s.shape) < p
    lab = label_clusters(br, bd)
    flat = lab.ravel()
    flip_root = rng.random(flat.size) < 0.5
    if frozen is not None:
        fz = np.broadcast_to(frozen, s.shape).ravel()
        flip_root[flat[fz]] = False
    flip = flip_root[flat].reshape(s.shape)
    s[flip] *= -1
    return lab


def _local_field(s):
    return (shift(s, 0, 1) + shift(s, 0, -1) + shift(s, 1, 0) + shift(s, -1, 0)).astype(np.float64)


def checkerboard(L):
    i, j = np.indices((L, L))
    return (i + j) % 2 == 0


def heat_bath(s, K, rng, frozen=None):
    """One checkerboard heat-bath sweep at coupling K, field zero, in place."""
    L = s.shape[-1]
    black = checkerboard(L)
    for colour in (black, ~black):
        upd = colour if frozen is None else colour & ~frozen
        hloc = _local_field(s)
        pup = 0.5 * (1.0 + np.tanh(K * hloc))
        new = np.where(rng.random(s.shape) < pup, 1, -1).astype(np.int8)
        s[..., upd] = new[..., upd]


def metropolis(s, K, rng):
    """One checkerboard Metropolis sweep at coupling K, field zero, in place."""
    L = s.shape[-1]
    black = checkerboard(L)
    for colour in (black, ~black):
        hloc = _local_field(s)
        dE = 2.0 * s * hloc  # energy change in units of J
        acc = rng.random(s.shape) < np.exp(-K * dE)
        flip = acc & colour
        s[flip] *= -1


# ---------------------------------------------------------------- statistics

def observables(s):
    """Sufficient statistics Phi of the 13-parameter family, shape (B, 13).

    Phi_h = sum_i s_i; Phi_(a,b) = sum_i s_i s_{i+(a,b)}.
    """
    s = s.astype(np.float64)
    out = [s.sum(axis=(-2, -1))]
    for a, b in OFFSETS:
        out.append((s * shift(s, a, b)).sum(axis=(-2, -1)))
    return np.stack(out, axis=-1)


def rb_given_black(s, K):
    """Exact E[Phi | black spins] at the nearest-neighbour point (K, h = 0).

    Given the black sublattice (i + j even), the white spins are independent
    with means m_w = tanh(K * sum of their four black neighbours). A pair
    statistic takes s s, s m or m m according to the colours of its ends
    (two distinct white sites are conditionally independent).
    """
    L = s.shape[-1]
    black = checkerboard(L)
    sf = s.astype(np.float64)
    m = np.tanh(K * _local_field(s))
    x = np.where(black, sf, m)  # black: the spin; white: its conditional mean
    out = [x.sum(axis=(-2, -1))]
    for a, b in OFFSETS:
        out.append((x * shift(x, a, b)).sum(axis=(-2, -1)))
    # Offsets are never zero, so no white site is paired with itself; a pair
    # of distinct white sites factorises. Hence the product of x is exact.
    return np.stack(out, axis=-1)


def observed_mask(L, k):
    """Sites kept after k checkerboard decimations (b = sqrt 2 per step).

    k = 0: all sites; k = 1: i + j even; k = 2: i, j even; k = 2m: i, j
    multiples of 2^m; k = 2m + 1: those of them with (i + j) / 2^m even.
    """
    i, j = np.indices((L, L))
    m, r = divmod(k, 2)
    step = 2 ** m
    mask = (i % step == 0) & (j % step == 0)
    if r:
        mask &= ((i // step + j // step) % 2 == 0)
    return mask
