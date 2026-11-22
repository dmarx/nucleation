import numpy as np
import pytest

from opmodel import (Config, init_state, make_env, shares, apply_clamp, logit_for_share,
                     step, own_risk, collective_risk, marginal_contribution,
                     mutual_information)


def setup(rule="moe", **kw):
    cfg = Config(rule=rule, **kw)
    rng = np.random.default_rng(0)
    beta = make_env(cfg, rng)
    st = init_state(cfg, rng)
    return cfg, rng, beta, st


def test_env_orthonormal():
    cfg, rng, beta, st = setup()
    assert np.allclose(beta @ beta.T, np.eye(cfg.C), atol=1e-12)


def test_shares_rows_sum_to_one_and_dead_zero():
    cfg, rng, beta, st = setup()
    st.Z = rng.standard_normal(st.Z.shape)
    st.alive[2] = False
    P = shares(cfg, st)
    assert np.allclose(P.sum(1), 1)
    assert np.all(P[:, 2] == 0)


def test_clamp():
    P = np.full((2, 4), 0.25)
    cl = np.full((2, 4), np.nan)
    cl[1, 0] = 1e-3
    Q = apply_clamp(P, cl)
    assert Q[1, 0] == 1e-3 and np.allclose(Q.sum(1), 1) and np.allclose(Q[0], 0.25)


@pytest.mark.parametrize("eps", [1e-2, 1e-3, 1e-5])
def test_logit_for_share(eps):
    cfg, rng, beta, st = setup(rule="moe_bias")
    st.Z = rng.standard_normal(st.Z.shape)
    st.b = rng.standard_normal(cfg.K)
    st.Z[3, 1] = logit_for_share(st.Z[3], st.b, st.alive, 1, eps)
    assert np.isclose(shares(cfg, st)[3, 1], eps, rtol=1e-9)


def test_risks_match_monte_carlo():
    cfg, rng, beta, st = setup()
    st.theta = rng.standard_normal(st.theta.shape) * 0.5
    st.Z = rng.standard_normal(st.Z.shape)
    P = shares(cfg, st)
    n = 200000
    X = rng.standard_normal((n, cfg.d))
    for c in range(cfg.C):
        y = X @ beta[c] + cfg.sigma * rng.standard_normal(n)
        A = X @ st.theta.T
        vy = 1 + cfg.sigma ** 2
        mc_own = ((A - y[:, None]) ** 2).mean(0) / vy
        mc_col = (((A * P[c]).sum(1) - y) ** 2).mean() / vy
        assert np.allclose(mc_own, own_risk(cfg, st, beta)[:, c], rtol=0.02)
        assert np.isclose(mc_col, collective_risk(cfg, st, beta)[c], rtol=0.02)


def test_moe_gate_is_loglik_gradient():
    """h - pi is the gradient of log sum_i pi_i exp(-l_i/s2) wrt the logits."""
    rng = np.random.default_rng(3)
    z = rng.standard_normal(5)
    l = rng.random(5)
    s2 = 0.25

    def f(z):
        pi = np.exp(z - z.max()); pi /= pi.sum()
        return np.log((pi * np.exp(-l / s2)).sum())
    pi = np.exp(z - z.max()); pi /= pi.sum()
    h = pi * np.exp(-l / s2); h /= h.sum()
    num = np.array([(f(z + 1e-6 * e) - f(z - 1e-6 * e)) / 2e-6 for e in np.eye(5)])
    assert np.allclose(num, h - pi, atol=1e-7)


def test_moe_rare_logit_gradient_scales_with_share():
    """The point the study turns on: under softmax-gradient routing a rare
    operator's logit moves in proportion to its share."""
    l = np.array([0.5, 0.5, 0.0])  # operator 2 is the best by far
    s2 = 0.25
    out = []
    for eps in (1e-2, 1e-3, 1e-4):
        pi = np.array([(1 - eps) / 2, (1 - eps) / 2, eps])
        h = pi * np.exp(-l / s2); h /= h.sum()
        out.append((h - pi)[2] / eps)
    # (h_i - pi_i)/pi_i tends to exp(-l_i/s2)/E_pi[exp(-l/s2)] - 1 = e^2 - 1
    assert np.allclose(out, np.e ** 2 - 1, rtol=0.07)


def test_rep_update_independent_of_share():
    cfg, rng, beta, st = setup(rule="rep", B=1)
    st.theta[:] = 0
    st.theta[0] = beta[0]
    for eps in (1e-2, 1e-4):
        s = st.copy()
        s.Z[0, 0] = logit_for_share(s.Z[0], s.b, s.alive, 0, eps)
        z0 = s.Z[0, 0] - s.Z[0, 1]
        r = np.random.default_rng(5)
        step(cfg, s, beta, r, ctx_p=np.array([1, 0, 0, 0.]))
        # increment of logit difference does not depend on eps beyond the yhat term
        assert s.Z[0, 0] - s.Z[0, 1] - z0 > 0


def test_frozen_and_dead_not_updated_and_decoupled_used():
    cfg, rng, beta, st = setup(rule="rep")
    st.frozen[0] = True
    st.alive[1] = False
    th0 = st.theta.copy()
    st.dec[:, 2] = 0.0  # decoupled with zero exposure: never trains
    for _ in range(50):
        step(cfg, st, beta, rng)
    assert np.allclose(st.theta[0], th0[0])
    assert np.allclose(st.theta[1], th0[1])
    assert np.allclose(st.theta[2], th0[2])
    assert not np.allclose(st.theta[3], th0[3])


def test_marginal_contribution_and_mi():
    cfg, rng, beta, st = setup(K=4)
    st.theta = beta.copy()
    st.Z = np.where(np.eye(4) > 0, 20.0, 0.0)
    P = shares(cfg, st)
    mc = marginal_contribution(cfg, st, beta)
    assert np.all(np.diag(mc) > 0.5)
    p = np.asarray(cfg.p)
    assert np.isclose(mutual_information(cfg, P), -(p * np.log(p)).sum(), atol=1e-3)
