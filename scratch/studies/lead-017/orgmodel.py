"""LEAD-017: three organizations of matched behaviour and different
endorsement relations, and a registration measure that does not read the
experimenter's setting.

The generator (`simulate`) takes a World (the setting) and returns two
objects: `Observables`, which is everything a measure may read, and
`Latent`, which holds the setting and hidden states and is used only to
score the measures. The measures in `measures.py` take Observables only.

One step t, for each agent (vectorized over agents):

1. Pursuit P chooses p_t ~ Bernoulli(sigmoid(L_t)),
   L_t = b + w_V V_t + drive + habit_w * Hb_t - uptake_t,
   where uptake_t reads what the organization registered at t-1 (u_{t-1})
   against the consummatory process's tolerance (see `World.auth`).
2. The outcome's hedonic value v_t (the experimenter's schedule, declining
   progressively from +1 to v_floor) is experienced if pursued; P learns
   V_{t+1} = V_t + a_V p_t (v_t - V_t).
3. The consummatory process H evaluates a probe of the outcome every step:
   h_t = v_t + s_t + xi_t + delta_t, where s_t is a physiological state
   (AR(1)), xi_t is H's own fluctuation and delta_t is the experimenter's
   randomized perturbation of H (a hotspot-style probe) on probe steps.
   The liking assay reads a_t = h_t + noise, independently of action.
4. The organization's record (its shared state, from which its reports
   and other processes read) is z_t = M c_t + noise, where M is a random
   orthogonal mixing per agent (unknown to the analyst) and the channels
   c_t are: outcome monitor p_t v_t; P's value V_t; P's prediction error
   p_t (v_t - V_t); the registered evaluation u_t = g h_t; a ledger
   (the tolerance tau_t in the accommodating organization, constant
   otherwise); an interoceptive channel (s_t in the decoy world, 0
   otherwise). g is the registration gain: the setting the measure must
   not read.
5. In the accommodating organization the tolerance is revised by
   reciprocal accommodation: each pursuit is followed by a compensation
   to H, and tau moves toward tau0 + tau_gain * comp_t.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

N_CH = 6  # record channels


@dataclass(frozen=True)
class World:
    name: str
    g_range: tuple = (0.5, 1.0)  # registration gain; (0, 0) = unregistered
    auth: str = "none"  # 'none' | 'tolerance' | 'direct'
    tol_mode: str = "fixed"  # 'fixed' | 'compensation'
    decoy_intero: bool = False  # record carries s_t by a route that bypasses H
    drive: float = 1.2  # persistent pursuit salience (cue drive)
    habit_w: float = 0.0
    b: float = 0.0  # base logit; set by calibration to match pursuit


@dataclass
class Observables:
    """What a measure may read."""
    pursued: np.ndarray  # (n, T) 0/1
    outcome: np.ndarray  # (T,) the experimenter's hedonic schedule v_t
    assay: np.ndarray  # (n, T) liking assay, read without action
    delta: np.ndarray  # (n, T) the experimenter's perturbation of H
    record: np.ndarray  # (n, T, N_CH) the organization's record, mixed
    report: np.ndarray  # (n, T) the organization's report, read off the record
    value: np.ndarray  # (n, T) P's learned value (a wanting proxy)


@dataclass
class Latent:
    """The setting and hidden states; for scoring only."""
    g: np.ndarray  # (n,)
    kappa: np.ndarray  # (n,)
    tau: np.ndarray  # (n, T)
    s: np.ndarray  # (n, T)
    world: World = field(default=None)


T_DEFAULT = 240
DEVAL_START, DEVAL_END = 20, 140


def schedule(T=T_DEFAULT, v_floor=-0.8):
    """Progressive devaluation: +1 until DEVAL_START, linear to v_floor at
    DEVAL_END, then flat."""
    t = np.arange(T)
    frac = np.clip((t - DEVAL_START) / (DEVAL_END - DEVAL_START), 0, 1)
    return 1.0 + (v_floor - 1.0) * frac


def random_orthogonal(rng, n, k):
    a = rng.standard_normal((n, k, k))
    q, r = np.linalg.qr(a)
    return q * np.sign(np.diagonal(r, axis1=1, axis2=2))[:, None, :]


def simulate(world: World, n: int, seed: int, T: int = T_DEFAULT,
             probe_rate: float = 0.3, delta_range=(-2.0, 0.6),
             with_probes: bool = True):
    rng = np.random.default_rng(seed)
    v = schedule(T)
    g = rng.uniform(*world.g_range, n)
    kappa = rng.uniform(2.0, 4.0, n)
    rec_sd = rng.uniform(0.3, 0.6, n)
    s_sd = rng.uniform(0.2, 0.35, n)
    xi_sd = rng.uniform(0.15, 0.25, n)
    M = random_orthogonal(rng, n, N_CH)
    wV, aV = 1.5, 0.15
    tau0, tau_gain, a_tau = 0.3, 0.8, 0.05

    p = np.zeros((n, T))
    a = np.zeros((n, T))
    d = np.zeros((n, T))
    z = np.zeros((n, T, N_CH))
    rep = np.zeros((n, T))
    Vs = np.zeros((n, T))
    taus = np.zeros((n, T))
    ss = np.zeros((n, T))

    V = np.ones(n)
    Hb = np.zeros(n)
    s = rng.standard_normal(n) * s_sd
    u_prev = g * 1.0
    h_prev = np.ones(n)
    tau = np.full(n, tau0)
    comp = np.zeros(n)
    rep_w = rng.standard_normal((n, N_CH))  # the org's own report readout

    for t in range(T):
        # 1. pursuit
        L = world.b + wV * V + world.drive + world.habit_w * Hb
        if world.auth == "tolerance":
            # uptake of the registered evaluation, beyond H's tolerance
            L = L - kappa * np.maximum(0.0, -u_prev - tau)
        elif world.auth == "direct":
            # H acts on pursuit by a route that does not pass the record
            L = L - kappa * np.maximum(0.0, -h_prev - tau)
        pt = (rng.random(n) < 1 / (1 + np.exp(-L))).astype(float)
        # 2. outcome and P's learning
        Vs[:, t] = V
        pe = pt * (v[t] - V)
        V = V + aV * pe
        Hb = 0.9 * Hb + 0.1 * pt
        # 3. H's evaluation and the assay
        s = 0.9 * s + np.sqrt(1 - 0.81) * s_sd * rng.standard_normal(n)
        dt = np.zeros(n)
        if with_probes:
            probe = rng.random(n) < probe_rate
            dt = np.where(probe, rng.uniform(*delta_range, n), 0.0)
        h = v[t] + s + xi_sd * rng.standard_normal(n) + dt
        at = h + 0.15 * rng.standard_normal(n)
        # 4. the record
        u = g * h
        ledger = tau if world.tol_mode == "compensation" else np.full(n, tau0)
        intero = s if world.decoy_intero else np.zeros(n)
        c = np.stack([pt * v[t], V, pe, u, ledger, intero], axis=1)
        zt = np.einsum("nij,nj->ni", M, c) + rec_sd[:, None] * rng.standard_normal((n, N_CH))
        # 5. reciprocal accommodation revises the tolerance
        if world.tol_mode == "compensation":
            comp = 0.95 * comp + 0.05 * pt
            tau = tau + a_tau * (tau0 + tau_gain * comp / 0.6 - tau)

        p[:, t], a[:, t], d[:, t], z[:, t], ss[:, t], taus[:, t] = pt, at, dt, zt, s, tau
        rep[:, t] = np.einsum("ni,ni->n", rep_w, zt) + 0.2 * rng.standard_normal(n)
        u_prev, h_prev = u, h

    obs = Observables(pursued=p, outcome=v, assay=a, delta=d, record=z,
                      report=rep, value=Vs)
    lat = Latent(g=g, kappa=kappa, tau=taus, s=ss, world=world)
    return obs, lat


def calibrate_b(world: World, target: float, n=400, seed=999, lo=-6.0, hi=6.0,
                window=(DEVAL_END, T_DEFAULT), iters=22):
    """Choose the base logit b so the world's mean pursuit over the window
    after devaluation equals target. Reads behaviour only."""
    from dataclasses import replace
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        obs, _ = simulate(replace(world, b=mid), n, seed)
        rate = obs.pursued[:, window[0]:window[1]].mean()
        if rate < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
