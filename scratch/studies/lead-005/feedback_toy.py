"""A percept-action loop in which the predictive and the interventional
partitions of the percept differ, priced with the Still et al. (2012)
bookkeeping of still2012.py (the per-switch identity holds under feedback;
its sign does not).

Percept x = (u, v, y), 8 values, index 4u + 2v + y.
  u : a fresh fair coin each step (the context the action must match)
  v : a sticky bit, v' = v with prob 1 - eps (predicts the next percept,
      irrelevant to what the action does)
  y : the outcome of the last action, y' = [a == u] with prob 1 - delta
Action a in {0, 1} is a function of the memory state s.

Memory: a physical system s whose energy is 0 where s = phi(x) and `gap`
(in k_B T) elsewhere, fully re-equilibrated after each switch of the percept
(a kernel that keeps each equilibrium stationary).  phi is the partition the
memory keeps.
"""
from __future__ import annotations

import itertools

import numpy as np

from still2012 import Model, entropy, equilibrate_kernel, run_exact

U, V, Y = 0, 1, 2


def decode(x: int) -> tuple[int, int, int]:
    return (x >> 2) & 1, (x >> 1) & 1, x & 1


def encode(u: int, v: int, y: int) -> int:
    return 4 * u + 2 * v + y


def env_T(eps: float, delta: float) -> np.ndarray:
    """T[x, a, x'] = p(x' | x, do(a))."""
    T = np.zeros((8, 2, 8))
    for x in range(8):
        u, v, _ = decode(x)
        for a in (0, 1):
            ok = int(a == u)
            for u2, v2, y2 in itertools.product((0, 1), repeat=3):
                pu = 0.5
                pv = 1 - eps if v2 == v else eps
                py = 1 - delta if y2 == ok else delta
                T[x, a, encode(u2, v2, y2)] = pu * pv * py
    return T


# ---------------------------------------------------------------- partitions
def partition_by(rows: np.ndarray, tol: float = 1e-12) -> list[tuple[int, ...]]:
    """Group indices whose rows are equal (within tol)."""
    classes: list[list[int]] = []
    reps: list[np.ndarray] = []
    for i, r in enumerate(rows):
        for c, rep in zip(classes, reps):
            if np.max(np.abs(rep - r)) < tol:
                c.append(i)
                break
        else:
            classes.append([i])
            reps.append(r)
    return [tuple(c) for c in classes]


def predictive_partition(T: np.ndarray, policy_x: np.ndarray) -> list:
    """Partition of x_t by p(x_{t+1} | x_t) under the regime policy_x[x, a]."""
    return partition_by(np.einsum("xa,xay->xy", policy_x, T))


def interventional_partition(T: np.ndarray, target: str = "y") -> list:
    """Partition of x_t by its response to every intervention do(a):
    target "y" uses p(y_{t+1} | x_t, do(a)) (the causal-bottleneck reading,
    relative to the task's outcome); target "x" uses the whole next percept."""
    if target == "x":
        resp = T
    else:
        resp = np.zeros((8, 2, 2))
        for x2 in range(8):
            resp[:, :, decode(x2)[Y]] += T[:, :, x2]
    return partition_by(resp.reshape(8, -1))


def describe(part: list) -> str:
    """Name a partition of the 8 percepts by the bits it distinguishes."""
    bits = []
    for name, k in (("u", U), ("v", V), ("y", Y)):
        if any(len({decode(x)[k] for x in c}) > 1 for c in part):
            continue
        if len({decode(c[0])[k] for c in part}) > 1:
            bits.append(name)
    return "{" + ",".join(bits) + "}" if len(part) == 2 ** len(bits) else f"{len(part)} classes"


# ---------------------------------------------------------------- memories
MEMORIES = {
    # name: (phi(x) -> memory state, number of memory states)
    "none": (lambda x: 0, 1),
    "predictive {v}": (lambda x: decode(x)[V], 2),
    "interventional {u}": (lambda x: decode(x)[U], 2),
    "u and v": (lambda x: 2 * decode(x)[U] + decode(x)[V], 4),
    "full {u,v,y}": (lambda x: x, 8),
}


def best_policy(name: str):
    """The action rule each memory affords: match u when u is held, else a = 0."""
    phi, n = MEMORIES[name]
    if name in ("interventional {u}",):
        return lambda s: s
    if name == "u and v":
        return lambda s: s >> 1
    if name.startswith("full"):
        return lambda s: decode(s)[U]
    return lambda s: 0


def build(name: str, policy, eps=0.1, delta=0.05, gap=6.0) -> Model:
    phi, n = MEMORIES[name]
    T = env_T(eps, delta)
    E = np.full((n, 8), gap)
    for x in range(8):
        E[phi(x), x] = 0.0
    D = np.zeros((8, n, 8))
    for s in range(n):
        D[:, s, :] = T[:, policy(s), :]
    K = np.stack([equilibrate_kernel(E[:, x]) for x in range(8)])
    # start from the percept's stationary law: u, v, y uniform-ish; use uniform
    p0x = np.full(8, 1 / 8)
    return Model(E=E, p0x=p0x, D=D, K=K)


def evaluate(name: str, policy=None, eps=0.1, delta=0.05, gap=6.0, tau=40) -> dict:
    """Late-time per-step quantities (the chain is stationary well before tau)."""
    policy = policy or best_policy(name)
    m = build(name, policy, eps, delta, gap)
    r = run_exact(m, tau)
    last = r.steps[-1]
    prev = r.steps[-2]["p_after"]          # p[s, x] before the last switch
    # success: P(y_{t+1} = 1) after the last switch
    q = prev[:, :, None] * m.D.transpose(1, 0, 2)
    p_next_x = q.sum((0, 1))
    success = sum(p_next_x[x] for x in range(8) if decode(x)[Y] == 1)
    return dict(memory=name, success=float(success), I_mem=last["I_mem"],
                I_pred=last["I_pred"], nostalgia=last["nostalgia"],
                relax=-last["dF_relax"], Wdiss_step=last["nostalgia"] - last["dF_relax"],
                heat_step=-last["Q"], H_overwrite=last["H_overwrite"],
                H_mem=entropy(last["p_after"].sum(1)))
