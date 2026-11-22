"""LEAD-063: one integration measure, one anti-nesting rule, two models.

Measure: Barrett & Seth's (2011) autoregressive integrated information,
Phi_AR, for a stationary linear Gaussian VAR(1) system
    X_{t+1} = A X_t + e_t,  e_t ~ N(0, I).
For a set of units S split into parts M_1..M_k,
    phi(S; split) = I(S_t; S_{t-1}) - sum_k I(M_k,t; M_k,t-1),
the information the whole carries about its own past beyond what its parts
carry about theirs. Phi(S) is phi at the minimum information bipartition
(MIB), found by minimizing phi / min(|M1|, |M2|) over bipartitions (size
normalization, as in Tononi's normalization of Phi); exact closed forms from
the stationary covariance, no sampling.

Anti-nesting rule: IIT's exclusion postulate. Of overlapping candidates, the
one with the larger Phi is the subject ("complex"); a candidate is a complex
only if no candidate overlapping it has a larger Phi.

Models (block-structured couplings):
- modular mind: m modules of n units; dense coupling inside a module
  (weight w), each module coupled to every other through `width` unit pairs
  of weight c (inter-module coupling).
- group: k members, each a copy of the modular mind, coupled to each other
  through `width` unit pairs of weight g (inter-member coupling).
The group is the modular-mind construction run one level up, with minds in
place of modules, so one procedure applies to both.
"""
from __future__ import annotations

import itertools

import numpy as np


# ---------------------------------------------------------------- statistics

def stationary_cov(A: np.ndarray, noise: np.ndarray | None = None) -> np.ndarray:
    """Solve Sigma = A Sigma A' + Q (discrete Lyapunov) by vectorization."""
    n = A.shape[0]
    Q = np.eye(n) if noise is None else noise
    rho = np.max(np.abs(np.linalg.eigvals(A)))
    if rho >= 1:
        raise ValueError(f"unstable system, spectral radius {rho:.3f}")
    K = np.eye(n * n) - np.kron(A, A)
    vec = np.linalg.solve(K, Q.reshape(-1, order="F"))
    S = vec.reshape(n, n, order="F")
    return (S + S.T) / 2


def self_info(Sigma: np.ndarray, Gamma: np.ndarray, idx) -> float:
    """I(S_t; S_{t-1}) in nats for the units idx, given Sigma = cov(X_t)
    and Gamma = cov(X_t, X_{t-1})."""
    idx = np.asarray(idx)
    S = Sigma[np.ix_(idx, idx)]
    G = Gamma[np.ix_(idx, idx)]
    E = S - G @ np.linalg.solve(S, G.T)  # residual cov of S_t given S_{t-1}
    _, ld_s = np.linalg.slogdet(S)
    _, ld_e = np.linalg.slogdet(E)
    return 0.5 * (ld_s - ld_e)


def phi_split(Sigma, Gamma, parts) -> float:
    whole = np.concatenate([np.asarray(p) for p in parts])
    return self_info(Sigma, Gamma, whole) - sum(self_info(Sigma, Gamma, p) for p in parts)


def bipartitions(units):
    """All bipartitions of `units` into two nonempty parts (each once)."""
    units = list(units)
    first, rest = units[0], units[1:]
    for r in range(0, len(rest)):
        for combo in itertools.combinations(rest, r):
            a = [first, *combo]
            b = [u for u in units if u not in a]
            if b:
                yield a, b


def block_bipartitions(blocks):
    """Bipartitions that do not cut any block (blocks: list of unit lists)."""
    for a_blocks, b_blocks in bipartitions(list(range(len(blocks)))):
        a = [u for i in a_blocks for u in blocks[i]]
        b = [u for i in b_blocks for u in blocks[i]]
        yield a, b


def Phi(Sigma, Gamma, units, splits=None, normalize=True):
    """Phi_AR of `units` at its MIB, size-normalized unless normalize=False.
    Returns (Phi, mib). `splits` defaults to every bipartition."""
    if splits is None:
        splits = bipartitions(units)
    best = None
    for a, b in splits:
        p = phi_split(Sigma, Gamma, [a, b])
        score = p / min(len(a), len(b)) if normalize else p
        if best is None or score < best[0]:
            best = (score, p, (a, b))
    return best[1], best[2]


# --------------------------------------------------------------------- models

def coupling_matrix(sizes_blocks, w, c, width, rng=None):
    """Couplings for blocks of units: weight w for every ordered pair inside
    a block (self-loops included), and for every pair of blocks, `width`
    reciprocal unit pairs of weight c. Deterministic: pair j links unit j of
    one block to unit j of the other."""
    blocks, n = [], 0
    for s in sizes_blocks:
        blocks.append(list(range(n, n + s)))
        n += s
    A = np.zeros((n, n))
    for b in blocks:
        A[np.ix_(b, b)] = w
    for i, j in itertools.combinations(range(len(blocks)), 2):
        for k in range(width):
            u, v = blocks[i][k], blocks[j][k]
            A[u, v] += c
            A[v, u] += c
    return A, blocks


def modular_mind(m=3, n=3, w=0.12, c=0.1, width=1):
    """A modular mind: m modules of n units."""
    A, modules = coupling_matrix([n] * m, w, c, width)
    return A, modules


def group(k=3, m=3, n=3, w=0.12, c=0.1, width_c=1, g=0.05, width_g=1):
    """A group of k members, each modular_mind(m, n, w, c, width_c), coupled
    member to member through `width_g` unit pairs of weight g. Member j's
    channel units are unit 0..width_g-1 of each of its modules in turn."""
    mind, modules = modular_mind(m, n, w, c, width_c)
    size = m * n
    N = k * size
    A = np.zeros((N, N))
    members, all_modules = [], []
    for j in range(k):
        off = j * size
        A[off:off + size, off:off + size] = mind
        members.append(list(range(off, off + size)))
        all_modules.extend([[u + off for u in mod] for mod in modules])
    # channel units of member j: one unit from successive modules
    def channel(j, r):
        mod = modules[r % m]
        return j * size + mod[(r // m) % n]
    for i, j in itertools.combinations(range(k), 2):
        for r in range(width_g):
            u, v = channel(i, r), channel(j, r)
            A[u, v] += g
            A[v, u] += g
    return A, members, all_modules


# ------------------------------------------------------------------ verdicts

def analyse(A, levels, normalize=True):
    """levels: dict name -> list of candidate unit sets (the candidates at
    that level; the top level is the whole). Phi for each candidate with
    exhaustive bipartitions where the candidate has <= 12 units, else
    bipartitions along the next level down (passed as `blocks`)."""
    Sigma = stationary_cov(A)
    Gamma = A @ Sigma
    out = {}
    for name, (cands, blocks_of) in levels.items():
        vals = []
        for cand in cands:
            if len(cand) <= 12:
                val, mib = Phi(Sigma, Gamma, cand, normalize=normalize)
            else:
                val, mib = Phi(Sigma, Gamma, cand,
                               block_bipartitions(blocks_of(cand)),
                               normalize=normalize)
            vals.append(val)
        out[name] = vals
    return out


def exclusion_winner(phis: dict) -> str:
    """Nested levels: each candidate at a lower level is inside the one
    candidate at each higher level. The complex is the level whose maximal
    Phi is largest (exclusion)."""
    return max(phis, key=lambda name: max(phis[name]))


def mind_levels(A, modules):
    whole = [u for mod in modules for u in mod]
    return {"module": (modules, None), "mind": ([whole], lambda c: modules)}


def group_levels(members, modules):
    whole = [u for mem in members for u in mem]
    mods_of = lambda cand: [m for m in modules if m[0] in cand]
    return {
        "module": (modules, None),
        "member": (members, mods_of),
        "group": ([whole], lambda c: modules),
    }
