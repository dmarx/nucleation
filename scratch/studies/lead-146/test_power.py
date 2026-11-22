import numpy as np

import power


def _sim(rng, I, dlat):
    return power.simulate(rng, I, dlat, **{k: power.DEFAULTS[k] for k in power.SIM_KEYS})


def test_cv_errors_recover_known_r2():
    rng = np.random.default_rng(0)
    I, R = 400, 5
    item = np.repeat(np.arange(I), R)
    x = rng.standard_normal(I * R)
    y = 0.6 * x + 0.8 * rng.standard_normal(I * R)  # R^2 = 0.36
    err, _ = power.ols_cv_sq_errors(x[:, None], y, item, 5, rng)
    assert abs((1 - err.mean() / y.var()) - 0.36) < 0.03


def test_folds_are_grouped_by_item():
    rng = np.random.default_rng(1)
    item = np.repeat(np.arange(50), 4)
    _, f = power.ols_cv_sq_errors(rng.standard_normal((200, 2)), rng.standard_normal(200), item, 5, rng)
    for i in range(50):
        assert len(set(f[item == i])) == 1


def test_delta_ci_brackets_estimate_and_null_increment_is_small():
    rng = np.random.default_rng(2)
    item, y, Xb, Xt = _sim(rng, 200, 0.0)
    eb, _ = power.ols_cv_sq_errors(Xb, y, item, 5, np.random.default_rng(5))
    ef, _ = power.ols_cv_sq_errors(np.column_stack([Xb, Xt]), y, item, 5, np.random.default_rng(5))
    est, lo, hi = power.delta_r2_with_ci(eb, ef, y, item, 300, rng)
    assert lo <= est <= hi
    assert abs(est) < 0.02


def test_real_increment_is_detected_at_large_n():
    r = power.power(300, 0.15, 0.0, reps=20)
    assert r["p_support"] > 0.9
    assert r["p_defeat"] == 0.0


def test_criterion_reliability_rises_with_receivers():
    assert power.criterion_reliability(I=500, J=30) > power.criterion_reliability(I=500, J=10)
