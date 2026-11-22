"""LEAD-015: two coupled meaning-influence institutions, an evaluator E and an
evaluated party P, and the condition under which their symmetric state is
unstable.

Each institution is LEAD-090's reduced CASE-092 model (CASE-363):
meaning m in [-1, 1] (lean toward hypothesis A) and authority a in [-1, 1]
(the A-specialist's share of conferral), with its own parameters
rho, sigma, phi, eps, g, delta. The one-institution reduced map is

    m' = (1 - rho) m + rho (b + sigma a + phi' m),     phi' = phi (1 - eps)
    a' = delta a + (1 - delta) tanh(g sigma m / 2 + t)

with b the imbalance of the corpus the institution reads and t an outside
tilt of its conferral (t = 0 in LEAD-090).

The two institutions read the same two hypotheses (A, say, "the party's
practice is sound"). They are coupled through four channels, each a reading
of CLAIM-404's "the evaluated party affects its evidence or resources" and
"the evaluator's reading affects the party's standing":

  theta : evidence      P -> E   b_E = b0_E + theta * m_P
          (what the party discloses or generates leans with its own
          prevailing interpretation: the informational route)
  omega : resources     P -> E   t_E = omega * m_P
          (the party's resources favour the evaluator's specialist whose
          line agrees with the party's: tilted conferral inside E)
  chi   : evidence      E -> P   b_P = b0_P + chi * m_E
          (the evaluator's published reading is itself evidence the party
          reads)
  psi   : standing      E -> P   t_P = psi * m_E
          (the evaluator's reading redistributes resources and authority
          inside the party toward the specialist whose line it favours:
          A21's "regulatory decisions -> distribution of resources and
          authority -> conditions of future production")

A21's chain is theta and psi. The state is x = (m_E, a_E, m_P, a_P).

Linearized at x = 0 (b0 = 0) the Jacobian is the 4x4 block matrix

    J = [[J_E, C_EP], [C_PE, J_P]],
    J_i  = [[alpha_i, beta_i], [gamma_i, delta_i]]   (CASE-363's entries)
    C_EP = [[rho_E theta, 0], [(1 - delta_E) omega, 0]]
    C_PE = [[rho_P chi,   0], [(1 - delta_P) psi,   0]]

Result (derived in README.md, checked in test_model.py and run.py): with
every entry nonnegative and each institution stable alone, the symmetric
state is unstable exactly when

    (theta + sigma_E omega)(chi + sigma_P psi) > Delta_E Delta_P,
    Delta_i = (1 - phi'_i) - g_i sigma_i^2 / 2   (> 0: i stable alone).

It is the general block condition rho(G_P C_PE G_E C_EP) > 1,
G_i = (I - J_i)^{-1}, specialized to rank-one channels, and rho_i and
delta_i cancel from it as they do from CLAIM-947's one-institution
threshold.
"""
from __future__ import annotations

import importlib.util
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "lead090_model", os.path.join(_HERE, "..", "lead-090", "model.py"))
one = importlib.util.module_from_spec(_spec)  # LEAD-090's one-institution model
_spec.loader.exec_module(one)

INST_KEYS = ("rho", "sigma", "phi", "eps", "g", "delta")


def institution(**kw):
    p = dict(rho=0.2, sigma=0.4, phi=0.3, eps=0.2, g=4.0, delta=0.9, b0=0.0)
    p.update(kw)
    return p


def params(E=None, P=None, theta=0.0, omega=0.0, chi=0.0, psi=0.0,
           resource_form="additive", k=50):
    """Two-institution parameters. resource_form: 'additive' (omega tilts E's
    conferral, the default) or 'multiplicative' (omega scales E's conferral
    gain, g_E (1 + omega m_P): resources as capacity, not direction)."""
    return dict(E=institution(**(E or {})), P=institution(**(P or {})),
                theta=theta, omega=omega, chi=chi, psi=psi,
                resource_form=resource_form, k=k)


def phi_eff(I):
    return I["phi"] * (1 - I["eps"])


def margin(I):
    """Delta_i = (1 - phi'_i) - g_i sigma_i^2 / 2; > 0 iff i is stable alone
    (CLAIM-947's threshold, halved)."""
    return (1 - phi_eff(I)) - I["g"] * I["sigma"] ** 2 / 2


# ------------------------------------------------------------ reduced map
def _inst_step(m, a, I, b, tilt, gain=1.0):
    ph = phi_eff(I)
    m_new = (1 - I["rho"]) * m + I["rho"] * (b + I["sigma"] * a + ph * m)
    a_new = I["delta"] * a + (1 - I["delta"]) * np.tanh(
        gain * I["g"] * I["sigma"] * m / 2 + tilt)
    return m_new, a_new


def step(x, Q):
    """The two-institution reduced map, simultaneous update. x = (mE, aE, mP, aP)."""
    mE, aE, mP, aP = x
    E, P = Q["E"], Q["P"]
    bE = E["b0"] + Q["theta"] * mP
    bP = P["b0"] + Q["chi"] * mE
    if Q["resource_form"] == "additive":
        mE2, aE2 = _inst_step(mE, aE, E, bE, Q["omega"] * mP)
    else:
        mE2, aE2 = _inst_step(mE, aE, E, bE, 0.0, gain=1 + Q["omega"] * mP)
    mP2, aP2 = _inst_step(mP, aP, P, bP, Q["psi"] * mE)
    return np.array([mE2, aE2, mP2, aP2])


def step_via_lead090(x, Q):
    """The same map computed through LEAD-090's exact mean_field (frame
    averaged, k -> infinity), with the tilt added to the conferral argument.
    Used to check that each half is LEAD-090's institution."""
    mE, aE, mP, aP = x
    out = []
    for (m, a, I, b, tilt) in (
            (mE, aE, Q["E"], Q["E"]["b0"] + Q["theta"] * mP, Q["omega"] * mP),
            (mP, aP, Q["P"], Q["P"]["b0"] + Q["chi"] * mE, Q["psi"] * mE)):
        Pd = one.default_params(**{k: I[k] for k in INST_KEYS}, b=0.0)
        Pd["b"] = b  # may exceed the agent-level range; the mean field is linear in b
        m2, _ = one.mean_field(m, a, Pd)
        # conferral with tilt: a' = delta a + (1 - delta) tanh(g sigma m / 2 + tilt)
        _, a_no = one.mean_field(m, a, Pd)
        target = (a_no - I["delta"] * a) / (1 - I["delta"])  # tanh(g sigma m / 2)
        a2 = I["delta"] * a + (1 - I["delta"]) * np.tanh(np.arctanh(target) + tilt)
        out += [m2, a2]
    return np.array(out)


def run(x0, Q, T, fn=step):
    X = np.empty((T + 1, 4))
    X[0] = x0
    x = np.asarray(x0, float)
    for t in range(T):
        x = fn(x, Q)
        X[t + 1] = x
    return X


# ------------------------------------------------------------ linearization
def block(I):
    ph = phi_eff(I)
    return np.array([[1 - I["rho"] * (1 - ph), I["rho"] * I["sigma"]],
                     [(1 - I["delta"]) * I["g"] * I["sigma"] / 2, I["delta"]]])


def cross_blocks(Q):
    E, P = Q["E"], Q["P"]
    om = Q["omega"] if Q["resource_form"] == "additive" else 0.0
    C_EP = np.array([[E["rho"] * Q["theta"], 0.0], [(1 - E["delta"]) * om, 0.0]])
    C_PE = np.array([[P["rho"] * Q["chi"], 0.0], [(1 - P["delta"]) * Q["psi"], 0.0]])
    return C_EP, C_PE


def jacobian(Q):
    C_EP, C_PE = cross_blocks(Q)
    return np.block([[block(Q["E"]), C_EP], [C_PE, block(Q["P"])]])


def jacobian_numeric(Q, h=1e-6):
    J = np.empty((4, 4))
    for i in range(4):
        e = np.zeros(4)
        e[i] = h
        J[:, i] = (step(e, Q) - step(-e, Q)) / (2 * h)
    return J


def spectral_radius(J):
    return float(np.max(np.abs(np.linalg.eigvals(J))))


def leading_real(J):
    ev = np.linalg.eigvals(J)
    return float(np.max(ev.real))


def loop_gains(Q):
    """L_E, L_P: each institution's static gain from the channel entering it
    to its own meaning. L_E = (theta + sigma_E omega) / Delta_E, etc."""
    E, P = Q["E"], Q["P"]
    om = Q["omega"] if Q["resource_form"] == "additive" else 0.0
    return ((Q["theta"] + E["sigma"] * om) / margin(E),
            (Q["chi"] + P["sigma"] * Q["psi"]) / margin(P))


def condition(Q):
    """True iff (theta + sigma_E omega)(chi + sigma_P psi) > Delta_E Delta_P."""
    E, P = Q["E"], Q["P"]
    om = Q["omega"] if Q["resource_form"] == "additive" else 0.0
    return (Q["theta"] + E["sigma"] * om) * (Q["chi"] + P["sigma"] * Q["psi"]) \
        > margin(E) * margin(P)


def schur_gain(J_E, J_P, C_EP, C_PE):
    """General block condition: rho(G_P C_PE G_E C_EP), G_i = (I - J_i)^{-1}.
    For nonnegative J with rho(J_E), rho(J_P) < 1, rho(J) > 1 iff this > 1."""
    G_E = np.linalg.inv(np.eye(len(J_E)) - J_E)
    G_P = np.linalg.inv(np.eye(len(J_P)) - J_P)
    return spectral_radius(G_P @ C_PE @ G_E @ C_EP)


def response(Q):
    """Linear response of the stationary state to a standing bias b0_P of the
    party's corpus: d m_E* / d b0_P and d m_P* / d b0_P, from (I - J)^{-1}."""
    J = jacobian(Q)
    R = np.linalg.inv(np.eye(4) - J)
    u = np.array([0.0, 0.0, Q["P"]["rho"], 0.0])  # b0_P enters m_P' with weight rho_P
    d = R @ u
    return float(d[0]), float(d[2])


# ------------------------------------------------------------ agent level
def step_agents(state, Q, rng):
    """One round of two agent-level CASE-092 institutions (LEAD-090's
    step_stochastic), coupled through the four channels. state = (pE, wE, pP, wP)."""
    pE, wE, pP, wP = state
    mE, mP = 2 * pE - 1, 2 * pP - 1
    out = []
    for (p_, w, I, b, tilt) in (
            (pE, wE, Q["E"], Q["E"]["b0"] + Q["theta"] * mP, Q["omega"] * mP),
            (pP, wP, Q["P"], Q["P"]["b0"] + Q["chi"] * mE, Q["psi"] * mE)):
        lim = 1 - I["sigma"] - I["phi"]
        b = float(np.clip(b, -lim, lim))
        q = (1 - I["eps"]) * p_ + I["eps"] / 2
        f = 1.0 if rng.random() < q else -1.0
        pi = 0.5 + (b + one.SIGNS * I["sigma"] + I["phi"] * f) / 2
        ehat = rng.binomial(Q["k"], pi) / Q["k"]
        wv = np.array([w, 1 - w])
        p_new = (1 - I["rho"]) * p_ + I["rho"] * float(wv @ ehat)
        score = p_ * ehat + (1 - p_) * (1 - ehat)
        z = I["g"] * (score[0] - score[1]) + 2 * tilt
        w_new = I["delta"] * w + (1 - I["delta"]) / (1 + np.exp(-z))
        out += [p_new, w_new]
    return out


def simulate_agents(Q, T, seed=0, state0=(0.5, 0.5, 0.5, 0.5)):
    rng = np.random.default_rng(seed)
    X = np.empty((T + 1, 4))
    X[0] = state0
    s = list(state0)
    for t in range(T):
        s = step_agents(s, Q, rng)
        X[t + 1] = s
    return 2 * X - 1  # in (m, a) coordinates
