import numpy as np
from metareg import metareg


def test_recovers_slope_and_tau2():
    rng = np.random.default_rng(0)
    k = 4000
    x = rng.uniform(0, 12, k)
    v = rng.uniform(0.02, 0.2, k)
    tau2 = 0.3
    y = -0.1 - 0.08 * x + rng.normal(0, np.sqrt(v + tau2))
    X = np.column_stack([np.ones(k), x])
    out = metareg(y, v, X, cluster=np.arange(k) // 4)
    assert abs(out["beta"][1] + 0.08) < 0.01
    assert abs(out["tau2"] - tau2) < 0.05
    assert out["se_robust"][1] > 0


def test_fixed_effect_limit():
    y = np.array([1.0, 1.0, 1.0])
    v = np.array([0.1, 0.2, 0.3])
    out = metareg(y, v, np.ones((3, 1)))
    assert out["tau2"] < 1e-6 and abs(out["beta"][0] - 1) < 1e-9
