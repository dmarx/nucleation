"""Exact and sampled bookkeeping for Still, Sivak, Bell & Crooks (2012),
"The thermodynamics of prediction" (arXiv 1203.3271 v3; PRL 109, 120604).

Setup (paper's "Problem setup"): a system with state s is driven by a signal x.
Energies E(s, x); beta = 1 throughout (units of k_B T, nats).  Each step
t = 0..tau-1 is

  work step     x_t -> x_{t+1} with s_t held;   W_t = E(s_t, x_{t+1}) - E(s_t, x_t)
  relaxation    s_t -> s_{t+1} ~ K_{x_{t+1}}(s_t, .);  Q_t = E(s_{t+1}, x_{t+1}) - E(s_t, x_{t+1})

starting from p(s_0 | x_0) = p_eq(s_0 | x_0).

The drive is Markov: x_{t+1} ~ D[x_t, s_t, :].  Without feedback D does not
depend on s; with feedback it does (that is the extension LEAD-005 asks for;
the paper excludes it).

Two readings of "dissipation" are computed:

* "current" (the paper's Eq. 13): free energies use p(s | x) conditional on the
  current signal value only, averaged over protocols.  Everything is then a
  function of the joint p(s, x), so a Markov drive (with or without feedback)
  needs only the joint chain.
* "path" (the paper's Eqs. 9-10 read per protocol): F_add uses
  p(s_tau | x_0..x_tau), averaged over protocols.  Computed by enumerating
  every drive path (no-feedback only).
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass, field

import numpy as np

TINY = 1e-300


# ---------------------------------------------------------------- basics
def entropy(p: np.ndarray) -> float:
    p = np.asarray(p, dtype=float).ravel()
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def mutual_info(joint: np.ndarray) -> float:
    """I[A;B] for a 2-d joint array p[a, b] (nats)."""
    joint = np.asarray(joint, dtype=float)
    return entropy(joint.sum(1)) + entropy(joint.sum(0)) - entropy(joint)


def cond_entropy_s_given_x(p_sx: np.ndarray) -> float:
    """H[S|X] for p[s, x]."""
    return entropy(p_sx) - entropy(p_sx.sum(0))


def kl(p: np.ndarray, q: np.ndarray) -> float:
    p = np.asarray(p, float)
    q = np.asarray(q, float)
    m = p > 0
    return float((p[m] * np.log(p[m] / q[m])).sum())


def boltzmann(E: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """p_eq[s, x] = exp(-E(s,x)) / Z(x) and F(x) = -ln Z(x)."""
    w = np.exp(-(E - E.min(0, keepdims=True)))
    Z = w.sum(0)
    peq = w / Z
    F = -np.log(Z) + E.min(0)
    return peq, F


def metropolis_kernel(E_col: np.ndarray, sweeps: int = 1) -> np.ndarray:
    """Metropolis kernel on states with energies E_col, uniform proposal over the
    other states.  Detailed balance with exp(-E), so it keeps p_eq stationary.
    `sweeps` applications are composed."""
    n = len(E_col)
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                K[i, j] = min(1.0, np.exp(-(E_col[j] - E_col[i]))) / (n - 1)
        K[i, i] = 1.0 - K[i].sum()
    return np.linalg.matrix_power(K, sweeps)


def equilibrate_kernel(E_col: np.ndarray) -> np.ndarray:
    """Full equilibration: every row is p_eq(.|x).  Keeps p_eq stationary."""
    w = np.exp(-(E_col - E_col.min()))
    return np.tile(w / w.sum(), (len(E_col), 1))


# ---------------------------------------------------------------- model
@dataclass
class Model:
    E: np.ndarray          # [n_s, n_x]
    p0x: np.ndarray        # [n_x] initial signal distribution
    D: np.ndarray          # [n_x, n_s, n_x]: p(x' | x, s)
    K: np.ndarray          # [n_x, n_s, n_s]: relaxation kernel at signal x
    peq: np.ndarray = field(init=False)
    F: np.ndarray = field(init=False)

    def __post_init__(self):
        self.peq, self.F = boltzmann(self.E)
        assert np.allclose(self.D.sum(-1), 1)
        assert np.allclose(self.K.sum(-1), 1)
        assert np.isclose(self.p0x.sum(), 1)

    @property
    def n_s(self):
        return self.E.shape[0]

    @property
    def n_x(self):
        return self.E.shape[1]

    @property
    def has_feedback(self) -> bool:
        return not np.allclose(self.D, self.D[:, :1, :])


def F_neq(p_sx: np.ndarray, E: np.ndarray) -> float:
    """Protocol-averaged nonequilibrium free energy, paper Eq. (13):
    beta <F_neq> = <E> - H[S|X]."""
    return float((p_sx * E).sum()) - cond_entropy_s_given_x(p_sx)


def F_add(p_sx: np.ndarray, peq: np.ndarray) -> float:
    """sum_x p(x) KL(p(s|x) || p_eq(s|x)), paper Eq. (6) averaged over x."""
    px = p_sx.sum(0)
    out = 0.0
    for x in range(p_sx.shape[1]):
        if px[x] > 0:
            out += px[x] * kl(p_sx[:, x] / px[x], peq[:, x])
    return out


@dataclass
class Run:
    steps: list            # per-step dicts
    totals: dict


def run_exact(m: Model, tau: int) -> Run:
    """Exact joint-chain bookkeeping, "current" reading (paper Eq. 13)."""
    p = m.peq * m.p0x[None, :]           # p[s, x] at t = 0
    p_start = p.copy()
    steps = []
    for t in range(tau):
        q = p[:, :, None] * m.D.transpose(1, 0, 2)      # q[s, x, x']
        W = float((q * (m.E[:, None, :] - m.E[:, :, None])).sum())
        I_mem = mutual_info(p)
        p_sw = q.sum(1)                                  # p[s, x'] after switch
        I_pred = mutual_info(p_sw)
        dF_sw = F_neq(p_sw, m.E) - F_neq(p, m.E)
        p_new = np.einsum("sx,xsr->rx", p_sw, m.K)        # relax at fixed x'
        Q = float((p_new * m.E).sum() - (p_sw * m.E).sum())
        dF_rel = F_neq(p_new, m.E) - F_neq(p_sw, m.E)
        # Landauer-style overwrite of the memory: H[S_t | S_{t+1}]
        joint_ss = np.einsum("sx,xsr->sr", p_sw, m.K)
        H_overwrite = entropy(joint_ss) - entropy(joint_ss.sum(0))
        steps.append(dict(t=t, W=W, Q=Q, I_mem=I_mem, I_pred=I_pred,
                          nostalgia=I_mem - I_pred, Wdiss_switch=W - dF_sw,
                          dF_relax=dF_rel, H_overwrite=H_overwrite,
                          p_after=p_new))
        p = p_new
    W = sum(s["W"] for s in steps)
    Q = sum(s["Q"] for s in steps)
    dFeq = float(p.sum(0) @ m.F - m.p0x @ m.F)
    Fadd = F_add(p, m.peq)
    Wex = W - dFeq
    Wdiss = Wex - Fadd
    Ie = cond_entropy_s_given_x(p_start) - cond_entropy_s_given_x(p)
    dE = float((p * m.E).sum() - (p_start * m.E).sum())
    totals = dict(W=W, Q=Q, dE=dE, dFeq=dFeq, Fadd=Fadd, Wex=Wex, Wdiss=Wdiss,
                  Ie=Ie,
                  nostalgia=sum(s["nostalgia"] for s in steps),
                  dF_relax=sum(s["dF_relax"] for s in steps))
    return Run(steps=steps, totals=totals)


def run_paths(m: Model, tau: int) -> dict:
    """Per-protocol ("path") reading of Eqs. (9)-(10), averaged over protocols.
    No feedback only.  Enumerates all n_x^(tau+1) drive paths."""
    assert not m.has_feedback
    Dx = m.D[:, 0, :]
    Wex = Wdiss = 0.0
    for path in itertools.product(range(m.n_x), repeat=tau + 1):
        pr = m.p0x[path[0]]
        for a, b in zip(path[:-1], path[1:]):
            pr *= Dx[a, b]
        if pr == 0:
            continue
        ps = m.peq[:, path[0]].copy()
        W = 0.0
        for a, b in zip(path[:-1], path[1:]):
            W += float(ps @ (m.E[:, b] - m.E[:, a]))
            ps = ps @ m.K[b]
        dF = m.F[path[-1]] - m.F[path[0]]
        fadd = kl(ps, m.peq[:, path[-1]])
        Wex += pr * (W - dF)
        Wdiss += pr * (W - dF - fadd)
    return dict(Wex=Wex, Wdiss=Wdiss)


def sample(m: Model, tau: int, n: int, rng: np.random.Generator) -> dict:
    """Monte Carlo over trajectories: mean and standard error of total W and Q.
    An independent check that the exact bookkeeping prices the same process."""
    def draw(P):  # P: [n, k] rows of probabilities
        c = P.cumsum(1)
        u = rng.random((P.shape[0], 1))
        return np.minimum((u > c).sum(1), P.shape[1] - 1)

    x = draw(np.tile(m.p0x, (n, 1)))
    s = draw(m.peq[:, x].T)
    W = np.zeros(n)
    Q = np.zeros(n)
    for _ in range(tau):
        x_new = draw(m.D[x, s, :])
        W += m.E[s, x_new] - m.E[s, x]
        s_new = draw(m.K[x_new, s, :])
        Q += m.E[s_new, x_new] - m.E[s, x_new]
        x, s = x_new, s_new
    return dict(W=W.mean(), W_se=W.std(ddof=1) / np.sqrt(n),
                Q=Q.mean(), Q_se=Q.std(ddof=1) / np.sqrt(n))


# ---------------------------------------------------------------- instances
def random_model(rng: np.random.Generator, n_s=4, n_x=3, feedback=False,
                 sweeps=1, e_scale=3.0, concentration=0.5) -> Model:
    """A random driven system: energies uniform in [0, e_scale], a Dirichlet
    Markov drive (feedback: one Dirichlet row per (x, s)), Metropolis kernels."""
    E = rng.uniform(0, e_scale, size=(n_s, n_x))
    if feedback:
        D = rng.dirichlet(np.full(n_x, concentration), size=(n_x, n_s))
    else:
        D = np.repeat(rng.dirichlet(np.full(n_x, concentration), size=n_x)[:, None, :],
                      n_s, axis=1)
    K = np.stack([metropolis_kernel(E[:, x], sweeps) for x in range(n_x)])
    p0x = rng.dirichlet(np.ones(n_x))
    return Model(E=E, p0x=p0x, D=D, K=K)
