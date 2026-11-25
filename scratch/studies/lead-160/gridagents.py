"""Three gridworld agents for LEAD-160 (the study CASE-187 proposes).

Deterministic, fully observed maze. States are cells s = r*w + c; actions
N, E, S, W; moving into a wall leaves the agent where it is. The goal
family is "reach cell g", for every cell g. A transition table T[s, a] -> s'
is the environment.

Agents (all tabular, all trained on the same stream of experience):

- Planner (M): holds a one-step transition model Th[s, a] (last observed
  outcome; unknown = stay) and plans for each goal by value iteration on it.
- Policy (P): a goal-conditioned action-value table Q[s, a, g], learned
  model-free by Q-learning with hindsight relabelling to every goal
  (reward 1 on arriving at g, episode ends there). It acts greedily.
- Distributed predictor (D): a bank of occupancy demons, one per
  (s, a, g): Msr[s, a, g] predicts the discounted number of visits to g
  after taking a in s and then acting uniformly at random (an action-
  conditioned successor representation). Each demon is learned by its own
  TD rule; there is no transition table. It acts by greedy ascent on
  Msr[x, :, g].

Unknown units are treated the same way by all three: as "stay".
"""
from __future__ import annotations

import numpy as np

A = 4
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
OPP = (2, 3, 0, 1)
GAMMA_P = 0.9   # planner and policy discount (any value < 1 gives shortest paths)
GAMMA_D = 0.95  # occupancy demons' discount


# ---------------------------------------------------------------- environment

class Maze:
    def __init__(self, h: int, w: int, T: np.ndarray):
        self.h, self.w, self.T = h, w, T

    @property
    def S(self) -> int:
        return self.h * self.w

    def neighbour(self, s: int, d: int):
        r, c = divmod(s, self.w)
        nr, nc = r + DIRS[d][0], c + DIRS[d][1]
        if 0 <= nr < self.h and 0 <= nc < self.w:
            return nr * self.w + nc
        return None

    def copy(self) -> "Maze":
        return Maze(self.h, self.w, self.T.copy())

    def passages(self):
        """Open interior passages as (s, d), d in (E, S), each listed once."""
        return [(s, d) for s in range(self.S) for d in (1, 2)
                if self.neighbour(s, d) is not None and self.T[s, d] != s]

    def walls(self):
        return [(s, d) for s in range(self.S) for d in (1, 2)
                if self.neighbour(s, d) is not None and self.T[s, d] == s]

    def open(self, s: int, d: int):
        t = self.neighbour(s, d)
        self.T[s, d] = t
        self.T[t, OPP[d]] = s

    def block(self, s: int, d: int):
        t = self.T[s, d]
        self.T[s, d] = s
        self.T[t, OPP[d]] = t


def make_maze(h: int, w: int, extra: int, rng: np.random.Generator) -> Maze:
    """Perfect maze by randomized depth-first search, then `extra` walls removed (loops)."""
    S = h * w
    m = Maze(h, w, np.repeat(np.arange(S)[:, None], A, axis=1))
    visited = np.zeros(S, bool)
    stack = [0]
    visited[0] = True
    while stack:
        s = stack[-1]
        nb = [(d, m.neighbour(s, d)) for d in range(A)
              if m.neighbour(s, d) is not None and not visited[m.neighbour(s, d)]]
        if not nb:
            stack.pop()
            continue
        d, t = nb[rng.integers(len(nb))]
        m.open(s, d)
        visited[t] = True
        stack.append(t)
    walls = m.walls()
    for i in rng.choice(len(walls), size=min(extra, len(walls)), replace=False):
        m.open(*walls[i])
    return m


def bfs_from(T: np.ndarray, x: int) -> np.ndarray:
    S = T.shape[0]
    d = np.full(S, np.inf)
    d[x] = 0
    frontier = np.array([x])
    k = 0
    while frontier.size:
        k += 1
        nxt = np.unique(T[frontier].ravel())
        nxt = nxt[np.isinf(d[nxt])]
        d[nxt] = k
        frontier = nxt
    return d


def all_pairs_dist(T: np.ndarray) -> np.ndarray:
    return np.stack([bfs_from(T, x) for x in range(T.shape[0])])


def random_walk_P(T: np.ndarray) -> np.ndarray:
    S = T.shape[0]
    P = np.zeros((S, S))
    for a in range(A):
        np.add.at(P, (np.arange(S), T[:, a]), 1.0 / A)
    return P


def occupancy(T: np.ndarray, gamma: float = GAMMA_D) -> np.ndarray:
    """Discounted visit counts under the uniform-random policy: (I - gamma P)^-1."""
    S = T.shape[0]
    return np.linalg.solve(np.eye(S) - gamma * random_walk_P(T), np.eye(S))


def random_walk(T: np.ndarray, n: int, rng: np.random.Generator, start=None):
    S = T.shape[0]
    s = int(rng.integers(S)) if start is None else start
    acts = rng.integers(A, size=n)
    out = np.empty((n, 3), dtype=np.int64)
    for i in range(n):
        s2 = T[s, acts[i]]
        out[i] = (s, acts[i], s2)
        s = s2
    return out


def last_unique(trans: np.ndarray) -> np.ndarray:
    """The last observed outcome of each (s, a) unit, in first-seen order."""
    seen = {}
    for s, a, s2 in trans:
        seen[(int(s), int(a))] = int(s2)
    return np.array([(s, a, s2) for (s, a), s2 in seen.items()], dtype=np.int64).reshape(-1, 3)


# ---------------------------------------------------------------- agents

def value_iteration(Th: np.ndarray, gamma: float = GAMMA_P) -> np.ndarray:
    """Q[s, a, g] for reaching g under model Th: 1 on arrival, gamma per further step."""
    S = Th.shape[0]
    arrive = Th[:, :, None] == np.arange(S)[None, None, :]
    V = np.zeros((S, S))
    for _ in range(S + 2):
        Q = np.where(arrive, 1.0, gamma * V[Th])
        Vn = Q.max(axis=1)
        if np.array_equal(Vn, V):
            break
        V = Vn
    return Q


class Planner:
    name = "M"

    def __init__(self, S: int):
        self.S = S
        self.Th = np.repeat(np.arange(S)[:, None], A, axis=1)
        self.updates = 0

    def learn(self, s, a, s2):
        self.Th[s, a] = s2
        self.updates += 1

    def train(self, trans):
        u = last_unique(trans)
        if len(u):
            self.Th[u[:, 0], u[:, 1]] = u[:, 2]
        self.updates += len(trans)

    def values(self):
        return value_iteration(self.Th)

    def error(self, s, a, s2) -> bool:
        return bool(self.Th[s, a] != s2)

    def local_edit_block(self, s, a):
        self.Th[s, a] = s

    def overwrite(self, dst, src):
        self.Th[dst[:, 0], dst[:, 1]] = self.Th[src[:, 0], src[:, 1]]

    def memory(self):
        return self.S * A

    def model(self):
        return self.Th.copy()


class Policy:
    name = "P"

    def __init__(self, S: int):
        self.S = S
        self.Q = np.zeros((S, A, S))
        self.updates = 0

    def _target(self, s2):
        t = GAMMA_P * self.Q[s2].max(axis=0)
        t[s2] = 1.0
        return t

    def learn(self, s, a, s2):
        self.Q[s, a] = self._target(s2)
        self.updates += 1

    def train(self, trans, max_sweeps=10_000):
        u = last_unique(trans)
        if not len(u):
            return 0
        ss, aa, s2 = u[:, 0], u[:, 1], u[:, 2]
        for k in range(max_sweeps):
            tgt = GAMMA_P * self.Q[s2].max(axis=1)
            tgt[np.arange(len(u)), s2] = 1.0
            changed = not np.array_equal(self.Q[ss, aa], tgt)
            self.Q[ss, aa] = tgt
            self.updates += len(u)
            if not changed:
                return k + 1
        return max_sweeps

    def values(self):
        return self.Q

    def error(self, s, a, s2) -> bool:
        t = self._target(s2)
        return bool(np.abs(t - self.Q[s, a]).max() > 1e-9)

    def local_edit_block(self, s, a):
        """Set the unit to its locally consistent value for a bump: gamma * best other action."""
        others = [b for b in range(A) if b != a]
        t = GAMMA_P * self.Q[s, others].max(axis=0)
        t[s] = 1.0
        self.Q[s, a] = t

    def overwrite(self, dst, src):
        self.Q[dst[:, 0], dst[:, 1]] = self.Q[src[:, 0], src[:, 1]]

    def memory(self):
        return self.S * A * self.S

    def model(self):
        """Read a transition table out of Q: the goal reached in one step has value 1."""
        Qm = self.Q.max(axis=2)
        Th = self.Q.argmax(axis=2)
        stay = np.repeat(np.arange(self.S)[:, None], A, axis=1)
        return np.where(Qm >= 1.0 - 1e-12, Th, stay)


class Demons:
    name = "D"

    def __init__(self, S: int):
        self.S = S
        self.Msr = np.zeros((S, A, S))
        self.Msr[np.arange(S), :, np.arange(S)] = 1.0 / (1.0 - GAMMA_D)  # unknown = stay
        self.updates = 0

    def _target(self, s, s2):
        t = GAMMA_D * self.Msr[s2].mean(axis=0)
        t[s] += 1.0
        return t

    def learn(self, s, a, s2):
        self.Msr[s, a] = self._target(s, s2)
        self.updates += 1

    def train(self, trans, max_sweeps=20_000):
        u = last_unique(trans)
        if not len(u):
            return 0
        ss, aa, s2 = u[:, 0], u[:, 1], u[:, 2]
        for k in range(max_sweeps):
            tgt = GAMMA_D * self.Msr[s2].mean(axis=1)
            tgt[np.arange(len(u)), ss] += 1.0
            changed = not np.array_equal(self.Msr[ss, aa], tgt)
            self.Msr[ss, aa] = tgt
            self.updates += len(u)
            if not changed:
                return k + 1
        return max_sweeps

    def values(self):
        return self.Msr

    def error(self, s, a, s2) -> bool:
        t = self._target(s, s2)
        row = self.Msr[s, a]
        return bool(np.abs(t - row).max() > 1e-9 * max(1.0, np.abs(row).max()))

    def local_edit_block(self, s, a):
        """Locally consistent bump value: x = e_s + gamma/A (sum_{b != a} M[s,b] + x)."""
        others = [b for b in range(A) if b != a]
        e = np.zeros(self.S)
        e[s] = 1.0
        self.Msr[s, a] = (e + GAMMA_D / A * self.Msr[s, others].sum(axis=0)) / (1.0 - GAMMA_D / A)

    def overwrite(self, dst, src):
        self.Msr[dst[:, 0], dst[:, 1]] = self.Msr[src[:, 0], src[:, 1]]

    def memory(self):
        return self.S * A * self.S

    def occupancy(self):
        return self.Msr.mean(axis=1)

    def readout(self, s, a):
        """Next state from the demons' own Bellman relation: M[s,a] = e_s + gamma Mpi[s']."""
        Mpi = self.occupancy()
        r = self.Msr[s, a].copy()
        r[s] -= 1.0
        res = np.abs(r[None, :] - GAMMA_D * Mpi).max(axis=1)
        return int(res.argmin())

    def model(self):
        Mpi = self.occupancy()
        Th = np.empty((self.S, A), dtype=np.int64)
        for s in range(self.S):
            r = self.Msr[s].copy()          # (A, S)
            r[:, s] -= 1.0
            res = np.abs(r[:, None, :] - GAMMA_D * Mpi[None, :, :]).max(axis=2)  # (A, S)
            Th[s] = res.argmin(axis=1)
        return Th

    def occupancy_after_block(self, s, a, t):
        """Woodbury update of Mpi for blocking the passage s -a-> t (both directions)."""
        Mpi = self.occupancy()
        S = self.S
        U = np.zeros((S, 2))
        U[s, 0] = 1.0
        U[t, 1] = 1.0
        V = np.zeros((S, 2))
        V[s, 0], V[t, 0] = 1.0 / A, -1.0 / A   # row s: mass moves from t to s
        V[t, 1], V[s, 1] = 1.0 / A, -1.0 / A   # row t: mass moves from s to t
        MU = Mpi @ U
        VM = V.T @ Mpi
        core = np.linalg.inv(np.eye(2) - GAMMA_D * V.T @ MU)
        return Mpi + GAMMA_D * MU @ core @ VM

    def global_edit_block(self, s, a, t):
        """Propagate a blocked passage through every demon without a transition table.

        Mpi' = Mpi + dMpi (Woodbury). Each demon M[x,b] = e_x + gamma Mpi[n] for its
        unknown successor n, and the rows of Mpi[n] it needs (columns s and t) are read
        off the demon itself: Mpi[n, j] = (M[x,b,j] - [x == j]) / gamma.
        """
        S = self.S
        Mpi = self.occupancy()
        V = np.zeros((S, 2))
        V[s, 0], V[t, 0] = 1.0 / A, -1.0 / A
        V[t, 1], V[s, 1] = 1.0 / A, -1.0 / A
        U_cols = Mpi[:, [s, t]]                      # Mpi U
        core = np.linalg.inv(np.eye(2) - GAMMA_D * V.T @ U_cols)
        right = core @ (V.T @ Mpi)                   # (2, S)
        succ_cols = self.Msr[:, :, [s, t]].copy()    # (S, A, 2)
        succ_cols[s, :, 0] -= 1.0
        succ_cols[t, :, 1] -= 1.0
        succ_cols /= GAMMA_D                         # Mpi[n(x,b), [s,t]]
        self.Msr += GAMMA_D * GAMMA_D * np.einsum("xbk,kj->xbj", succ_cols, right)
        Mpi_new = Mpi + GAMMA_D * U_cols @ right
        for (u, b) in ((s, a), (t, OPP[a])):
            e = np.zeros(S)
            e[u] = 1.0
            self.Msr[u, b] = e + GAMMA_D * Mpi_new[u]


AGENTS = (Planner, Policy, Demons)


# ---------------------------------------------------------------- evaluation

def greedy(values: np.ndarray) -> np.ndarray:
    return values.argmax(axis=1)  # (S, G)


def rollout(T: np.ndarray, pi: np.ndarray, H: int):
    S = T.shape[0]
    g = np.tile(np.arange(S)[None, :], (S, 1))
    pos = np.tile(np.arange(S)[:, None], (1, S))
    done = pos == g
    steps = np.zeros((S, S), dtype=np.int64)
    for _ in range(H):
        a = pi[pos, g]
        pos = np.where(done, pos, T[pos, a])
        steps += ~done
        done |= pos == g
    return done, steps


def competence(T: np.ndarray, values: np.ndarray, dist: np.ndarray, H=None):
    S = T.shape[0]
    H = H or S
    done, steps = rollout(T, greedy(values), H)
    mask = ~np.eye(S, dtype=bool) & np.isfinite(dist)
    succ = done & mask
    excess = float((steps[succ] / dist[succ]).mean()) if succ.any() else float("nan")
    return float(succ.sum() / mask.sum()), excess, done
