"""LEAD-075: A's staging experiment, states A and B with a staging state C.

The model (choices are stated in README.md):

* A state is (q, z): a configuration q on a grid over [0, 1] and an
  architecture z in {0 (home), 1 (staging)}.  A = (0, home), B = (1, home).
  The staging state C is any (q, staging); in CASE-198's route it is
  entered at q_A and left at q_B.
* One resource, a capacity (CLAIM-571's scope): holding (q, z) takes
  r_z(q).  Home: r0(q) = h0 + beta0 q(1-q).  Staging: r1(q) = h1 + beta1 q(1-q).
* Moves: a step along q under z takes time d_z / (n - 1) and peaks at the
  larger of its two ends.  Under the home architecture a "gap" (a crease
  or linkage constraint) can forbid steps whose midpoint lies in
  (gap_lo, gap_hi): the home configuration space is then disconnected.
  A switch of z at fixed q takes time t_s and peaks at max(r0, r1) + s.
  Moves are reversible.  The repertoire Z says which architectures may be
  used: (0,) home only, or (0, 1) staging admitted.
* B*(A, B; Z) is the least peak over admissible paths (CLAIM-571),
  infinite when none.  T*(A, B; b, Z) is the least time over paths whose
  peak is at most b.
* Readiness R^pi(A -> B; b, Z, tau) (TERM-115's sense): the contingency
  "be at B by tau" is imposed while a random background load U ~
  Uniform[0, u_max] holds part of the capacity b, and a temporary reserve
  rho is available with probability p.  The capacity for the transition is
  C = b - U + rho K, K ~ Bernoulli(p), fixed for its duration.  The
  policy pi takes the fastest route whose peak is within C among those its
  repertoire Z admits.  Holding B afterwards needs r0(1) <= b - U (the
  reserve is temporary).
"""
from __future__ import annotations

import heapq
import math
from dataclasses import dataclass, field

import numpy as np

INF = math.inf


@dataclass(frozen=True)
class Params:
    n: int = 201                 # grid points on [0, 1]; q = 1/2 is a point
    h0: float = 0.7              # home holding cost at the ends
    beta0: float = 2.4           # home barrier: r0(1/2) = h0 + beta0/4
    h1: float = 0.8              # staging holding cost at the ends
    beta1: float = 0.4           # staging barrier
    s: float = 0.2               # extra peak of a switch
    d0: float = 1.0              # time to cross [0, 1] under home
    d1: float = 2.0              # time to cross [0, 1] under staging
    t_s: float = 0.5             # time of one switch
    gap: bool = False            # home steps blocked in (gap_lo, gap_hi)
    gap_lo: float = 0.45
    gap_hi: float = 0.55
    switch_ok: tuple = field(default=(0.0, 1.0))  # interval of q where z may switch

    def q(self) -> np.ndarray:
        return np.linspace(0.0, 1.0, self.n)

    def r(self) -> np.ndarray:
        q = self.q()
        r0 = self.h0 + self.beta0 * q * (1 - q)
        r1 = self.h1 + self.beta1 * q * (1 - q)
        return np.vstack([r0, r1])


def build_graph(p: Params, Z=(0, 1)):
    """Return node costs (2n,), and adjacency lists of (j, peak, time)."""
    n = p.n
    q = p.q()
    r = p.r()
    cost = np.full(2 * n, INF)
    adj = [[] for _ in range(2 * n)]
    for z in Z:
        cost[z * n:(z + 1) * n] = r[z]
        dt = (p.d0 if z == 0 else p.d1) / (n - 1)
        for k in range(n - 1):
            mid = 0.5 * (q[k] + q[k + 1])
            if z == 0 and p.gap and p.gap_lo < mid < p.gap_hi:
                continue
            i, j = z * n + k, z * n + k + 1
            peak = max(r[z][k], r[z][k + 1])
            adj[i].append((j, peak, dt))
            adj[j].append((i, peak, dt))
    if 0 in Z and 1 in Z:
        lo, hi = p.switch_ok
        for k in range(n):
            if lo - 1e-12 <= q[k] <= hi + 1e-12:
                peak = max(r[0][k], r[1][k]) + p.s
                adj[k].append((n + k, peak, p.t_s))
                adj[n + k].append((k, peak, p.t_s))
    return cost, adj


def bottleneck(p: Params, Z=(0, 1), src=None, dst=None) -> float:
    """B*(A, B; Z): least, over admissible paths, of the peak requirement."""
    cost, adj = build_graph(p, Z)
    src = 0 if src is None else src
    dst = p.n - 1 if dst is None else dst
    best = np.full(len(cost), INF)
    best[src] = cost[src]
    heap = [(best[src], src)]
    while heap:
        v, i = heapq.heappop(heap)
        if v > best[i]:
            continue
        if i == dst:
            return float(v)
        for j, peak, _ in adj[i]:
            w = max(v, peak, cost[j])
            if w < best[j]:
                best[j] = w
                heapq.heappush(heap, (w, j))
    return INF


def least_time(p: Params, b: float, Z=(0, 1), src=None, dst=None) -> float:
    """T*(A, B; b, Z): least time over paths whose peak is at most b."""
    cost, adj = build_graph(p, Z)
    src = 0 if src is None else src
    dst = p.n - 1 if dst is None else dst
    eps = 1e-12
    if cost[src] > b + eps:
        return INF
    dist = np.full(len(cost), INF)
    dist[src] = 0.0
    heap = [(0.0, src)]
    while heap:
        t, i = heapq.heappop(heap)
        if t > dist[i]:
            continue
        if i == dst:
            return float(t)
        for j, peak, dt in adj[i]:
            if peak > b + eps or cost[j] > b + eps:
                continue
            if t + dt < dist[j]:
                dist[j] = t + dt
                heapq.heappush(heap, (t + dt, j))
    return INF


def time_profile(p: Params, Z=(0, 1)):
    """The step function b -> T*(b): its breakpoints and values.

    T* changes only at a node or edge peak, so evaluating at each distinct
    peak value gives it exactly.  Returns (budgets, times), budgets sorted,
    times nonincreasing, starting at B*.
    """
    cost, adj = build_graph(p, Z)
    levels = set(float(c) for c in cost if np.isfinite(c))
    for lst in adj:
        for _, peak, _ in lst:
            levels.add(float(peak))
    B = bottleneck(p, Z)
    if not np.isfinite(B):
        return np.array([]), np.array([])
    bs, ts = [], []
    last = INF
    for b in sorted(x for x in levels if x >= B - 1e-12):
        t = least_time(p, b, Z)
        if t < last - 1e-12:
            bs.append(b)
            ts.append(t)
            last = t
    return np.array(bs), np.array(ts)


def capacity_for_deadline(p: Params, tau: float, Z=(0, 1)) -> float:
    """c_tau: least capacity at which B is reached by tau (inf if none)."""
    bs, ts = time_profile(p, Z)
    ok = np.nonzero(ts <= tau + 1e-12)[0]
    return float(bs[ok[0]]) if len(ok) else INF


def _p_uniform_le(x: float, u_max: float) -> float:
    """P(U <= x) for U ~ Uniform[0, u_max]; u_max = 0 means U = 0."""
    if u_max <= 0:
        return 1.0 if x >= 0 else 0.0
    return float(min(1.0, max(0.0, x / u_max)))


def readiness(p: Params, b: float, tau: float, Z=(0, 1), rho=0.0,
              p_res=0.0, u_max=0.0) -> float:
    """R^pi(A -> B; b, Z, tau), exact for U uniform and K Bernoulli.

    Success needs C = b - U + rho K >= c_tau (the transition is fast
    enough within the capacity it has) and b - U >= r0(B) (B can be held
    once the reserve is returned).
    """
    c_tau = capacity_for_deadline(p, tau, Z)
    if not np.isfinite(c_tau):
        return 0.0
    r_B = float(p.r()[0][-1])
    out = 0.0
    for k, pk in ((0, 1 - p_res), (1, p_res)):
        if pk == 0:
            continue
        # need U <= b + rho k - c_tau and U <= b - r_B
        x = min(b + rho * k - c_tau, b - r_B)
        out += pk * _p_uniform_le(x, u_max)
    return out


def readiness_mc(p: Params, b, tau, Z=(0, 1), rho=0.0, p_res=0.0,
                 u_max=0.0, n=20000, seed=0) -> float:
    """Monte Carlo check of readiness(): simulate U and K, run T*."""
    rng = np.random.default_rng(seed)
    U = rng.uniform(0, u_max, n) if u_max > 0 else np.zeros(n)
    K = rng.random(n) < p_res
    bs, ts = time_profile(p, Z)
    r_B = float(p.r()[0][-1])
    hits = 0
    for u, k in zip(U, K):
        C = b - u + rho * k
        if b - u < r_B - 1e-12:
            continue
        ok = np.nonzero(bs <= C + 1e-12)[0]
        if len(ok) and ts[ok[-1]] <= tau + 1e-12:
            hits += 1
    return hits / n


KINDS = (
    "not holdable",          # B cannot be held at b at all
    "reachable as is",       # home architecture, no reserve
    "statically feasible, unreachable",   # K1: no admissible path in Z
    "reachable, too expensive",           # K2: finite B*, beyond b + rho
    "only through architectural change",  # K3
    "only with temporary reserve",        # K4
    "either change or reserve",
    "change and reserve together",
)


def classify(B_home: float, B_all: float, b: float, rho: float,
             r_A: float, r_B: float) -> str:
    """The kind of case at budget b and reserve rho, from B* per repertoire."""
    e = 1e-12
    if max(r_A, r_B) > b + e:
        return "not holdable"
    if B_home <= b + e:
        return "reachable as is"
    if not np.isfinite(B_all):
        return "statically feasible, unreachable"
    s = B_all <= b + e
    r = B_home <= b + rho + e
    if s and r:
        return "either change or reserve"
    if s:
        return "only through architectural change"
    if r:
        return "only with temporary reserve"
    if B_all <= b + rho + e:
        return "change and reserve together"
    return "reachable, too expensive"
