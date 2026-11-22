"""Tests for sentry.py (LEAD-076, part 2). Run: python3 -I -m pytest -q"""
import numpy as np
import pytest

from sentry import (Params, Condition, draws, simulate, measures, summarize, posterior, voi,
                    predict, world, first_true)

P = Params()
N = 200


@pytest.fixture(scope="module")
def U():
    return draws(P, N, seed=123)


def test_posterior_and_predict():
    b = np.array([0.5])
    assert np.isclose(posterior(b, np.array([1]), 0.9), 0.9)
    assert np.isclose(posterior(b, np.array([0]), 0.9), 0.1)
    assert np.isclose(predict(np.array([1.0]), 0.02), 0.98)


def test_voi_shape():
    b = np.linspace(0, 1, 101)
    v = voi(b, P)
    assert (v >= -1e-12).all()
    assert np.isclose(v[0], 0) and np.isclose(v[-1], 0)
    assert np.isclose(voi(np.array([0.5]), P)[0], 0.25)


def test_world_schedule():
    x = world(P)
    assert x[:P.T1].all() and not x[P.T1:P.T1 + P.T2].any() and x[P.T1 + P.T2:].all()


def test_common_random_numbers_deterministic(U):
    a = simulate(P, Condition(), U)
    b = simulate(P, Condition(), U)
    for k in a:
        assert np.array_equal(a[k], b[k])


def test_bayes_ignores_kappa(U):
    a = simulate(P, Condition(model="bayes"), U)
    b = simulate(Params(kappa=5.0), Condition(model="bayes"), U)
    assert np.array_equal(a["prot"], b["prot"]) and np.array_equal(a["b"], b["b"])


def test_habit_with_zero_kappa_is_bayes(U):
    p0 = Params(kappa=0.0)
    a = simulate(p0, Condition(model="bayes"), U)
    b = simulate(p0, Condition(model="habit"), U)
    assert np.array_equal(a["prot"], b["prot"])


def test_fixed_feedback_keeps_g(U):
    r = simulate(P, Condition(feedback="fixed"), U)
    assert np.allclose(r["g"], P.g0)


def test_success_feedback_rises_under_protection(U):
    r = simulate(P, Condition(), U)
    assert r["g"][:, P.T1 - 1].mean() > 0.9


def test_sheltering_is_uninformative(U):
    """Identifiability: if the agent never inspects, its belief is the same
    in a safe world and a dangerous one (CLAIM-446's step)."""
    cond = Condition(model="bayes", c_override=10.0)
    a = simulate(P, cond, U, x=np.zeros(P.T, int))
    b = simulate(P, cond, U, x=np.ones(P.T, int))
    assert a["insp"].sum() == 0
    assert np.array_equal(a["b"], b["b"])


def test_protects_when_danger_is_real(U):
    for cond in (Condition(model="bayes"), Condition(), Condition(correction="audit"),
                 Condition(correction="protected"), Condition(feedback="independent")):
        m = summarize(measures(P, simulate(P, cond, U)))
        assert m["prot3"] > 0.95, cond


def test_first_true_censor():
    m = np.array([[False, True, True], [False, False, False]])
    assert list(first_true(m, 3)) == [1, 3]


def test_intervention_authority_resets(U):
    r = simulate(P, Condition(intervention="authority"), U)
    t = P.T1 + 50
    F = ((r["prot"][:, t] > 0) | (r["harm"][:, t] > 0)).astype(float)
    assert np.allclose(r["g"][:, t], (1 - P.eta) * 0.05 + P.eta * F)
