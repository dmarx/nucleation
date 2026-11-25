import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as M  # noqa: E402


def random_Q(rng, stable_alone=True, form="additive"):
    while True:
        E = dict(rho=rng.uniform(0.02, 1), sigma=rng.uniform(0.05, 0.5),
                 phi=rng.uniform(0, 0.45), eps=rng.uniform(0, 1),
                 g=rng.uniform(0, 30), delta=rng.uniform(0, 0.98))
        P = dict(rho=rng.uniform(0.02, 1), sigma=rng.uniform(0.05, 0.5),
                 phi=rng.uniform(0, 0.45), eps=rng.uniform(0, 1),
                 g=rng.uniform(0, 30), delta=rng.uniform(0, 0.98))
        Q = M.params(E, P, theta=rng.uniform(0, 1.5), omega=rng.uniform(0, 1.5),
                     chi=rng.uniform(0, 1.5), psi=rng.uniform(0, 1.5),
                     resource_form=form)
        for c in ("theta", "omega", "chi", "psi"):
            if rng.random() < 0.3:
                Q[c] = 0.0
        if not stable_alone or (M.margin(Q["E"]) > 0 and M.margin(Q["P"]) > 0):
            return Q


def test_each_half_is_lead090_institution():
    rng = np.random.default_rng(1)
    for _ in range(100):
        Q = random_Q(rng)
        x = rng.uniform(-0.6, 0.6, 4)
        assert np.allclose(M.step(x, Q), M.step_via_lead090(x, Q), atol=1e-12)


def test_uncoupled_blocks_are_lead090_jacobians():
    rng = np.random.default_rng(2)
    for _ in range(50):
        Q = random_Q(rng)
        for c in ("theta", "omega", "chi", "psi"):
            Q[c] = 0.0
        J = M.jacobian(Q)
        for I, sl in ((Q["E"], slice(0, 2)), (Q["P"], slice(2, 4))):
            Pd = M.one.default_params(**{k: I[k] for k in M.INST_KEYS})
            assert np.allclose(J[sl, sl], M.one.jacobian_analytic(Pd))
        assert np.allclose(J[0:2, 2:4], 0) and np.allclose(J[2:4, 0:2], 0)


@pytest.mark.parametrize("form", ["additive", "multiplicative"])
def test_jacobian_analytic_equals_numeric(form):
    rng = np.random.default_rng(3)
    for _ in range(100):
        Q = random_Q(rng, form=form)
        assert np.allclose(M.jacobian(Q), M.jacobian_numeric(Q), atol=1e-7)


def test_multiplicative_resources_vanish_at_symmetry():
    rng = np.random.default_rng(4)
    Q = random_Q(rng, form="multiplicative")
    Q["omega"] = 1.0
    assert abs(M.jacobian_numeric(Q)[1, 2]) < 1e-8


def test_condition_iff_unstable():
    rng = np.random.default_rng(5)
    n = 0
    for _ in range(3000):
        Q = random_Q(rng)
        r = M.spectral_radius(M.jacobian(Q))
        if abs(r - 1) < 1e-6:
            continue
        assert M.condition(Q) == (r > 1)
        n += 1
    assert n > 2900


def test_condition_is_schur_gain():
    rng = np.random.default_rng(6)
    for _ in range(300):
        Q = random_Q(rng)
        C_EP, C_PE = M.cross_blocks(Q)
        s = M.schur_gain(M.block(Q["E"]), M.block(Q["P"]), C_EP, C_PE)
        LE, LP = M.loop_gains(Q)
        assert np.isclose(s, LE * LP, rtol=1e-8, atol=1e-12)


@pytest.mark.parametrize("nE,nP", [(2, 2), (3, 2), (3, 3), (4, 5)])
def test_block_theorem_general(nE, nP):
    """For nonnegative J with stable diagonal blocks, rho(J) > 1 iff the
    round-trip gain rho(G_P C_PE G_E C_EP) > 1."""
    rng = np.random.default_rng(7 + nE * 10 + nP)
    n = 0
    for _ in range(2000):
        def stable(k):
            while True:
                A = rng.uniform(0, 1, (k, k)) * (rng.random((k, k)) < 0.7)
                A *= rng.uniform(0.2, 0.99) / max(M.spectral_radius(A), 1e-9)
                return A
        J_E, J_P = stable(nE), stable(nP)
        s = rng.uniform(0, 1.5)
        C_EP = s * rng.uniform(0, 1, (nE, nP)) * (rng.random((nE, nP)) < 0.5)
        C_PE = s * rng.uniform(0, 1, (nP, nE)) * (rng.random((nP, nE)) < 0.5)
        J = np.block([[J_E, C_EP], [C_PE, J_P]])
        r = M.spectral_radius(J)
        g = M.schur_gain(J_E, J_P, C_EP, C_PE)
        if abs(r - 1) < 1e-6 or abs(g - 1) < 1e-6:
            continue
        assert (r > 1) == (g > 1)
        n += 1
    assert n > 1900


def test_rate_and_memory_cancel():
    rng = np.random.default_rng(8)
    for _ in range(100):
        Q = random_Q(rng)
        c = M.condition(Q)
        for rho in (0.05, 0.5, 1.0):
            for d in (0.0, 0.5, 0.95):
                Q2 = M.params({**Q["E"], "rho": rho, "delta": d},
                              {**Q["P"], "rho": rho, "delta": 1 - d / 2},
                              Q["theta"], Q["omega"], Q["chi"], Q["psi"])
                r = M.spectral_radius(M.jacobian(Q2))
                if abs(r - 1) > 1e-6:
                    assert (r > 1) == c


def test_response_closed_form():
    rng = np.random.default_rng(9)
    for _ in range(100):
        Q = random_Q(rng)
        LE, LP = M.loop_gains(Q)
        if LE * LP >= 0.95:
            continue
        dE, dP = M.response(Q)
        DP = M.margin(Q["P"])
        assert np.isclose(dP, 1 / (DP * (1 - LE * LP)))
        assert np.isclose(dE, LE / (DP * (1 - LE * LP)))


def test_agent_level_mean_matches_map():
    """Expectation of one agent-level round, by Monte Carlo at large k, equals
    the reduced map (frame averaged) to Monte Carlo error."""
    Q = M.params(theta=0.2, omega=0.3, chi=0.1, psi=0.4, k=400)
    x = np.array([0.2, -0.1, -0.15, 0.3])
    s0 = (x + 1) / 2
    rng = np.random.default_rng(10)
    acc = np.zeros(4)
    N = 20000
    for _ in range(N):
        acc += M.step_agents(list(s0), Q, rng)
    mean = 2 * acc / N - 1
    # m is linear in the item shares: exact in expectation. a is nonlinear in
    # them (softmax), so allow the finite-k curvature term.
    pred = M.step(x, Q)
    assert abs(mean[0] - pred[0]) < 3e-3 and abs(mean[2] - pred[2]) < 3e-3
    assert abs(mean[1] - pred[1]) < 5e-3 and abs(mean[3] - pred[3]) < 5e-3
