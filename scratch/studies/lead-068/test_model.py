import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from model import Params, fcfs_reneging, simulate, timing_prediction  # noqa: E402

INF = np.inf


def test_fcfs_single_server_order_and_times():
    enq = np.array([0.0, 0.5, 1.0])
    svc = np.array([2.0, 1.0, 1.0])
    start, finish, served = fcfs_reneging(enq, svc, np.full(3, INF), 1)
    assert served.all()
    assert np.allclose(start, [0.0, 2.0, 3.0])
    assert np.allclose(finish, [2.0, 3.0, 4.0])


def test_fcfs_two_servers():
    enq = np.array([0.0, 0.0, 0.0])
    svc = np.array([3.0, 1.0, 1.0])
    start, finish, _ = fcfs_reneging(enq, svc, np.full(3, INF), 2)
    assert np.allclose(start, [0.0, 0.0, 1.0])


def test_fcfs_reneging_frees_server():
    # item 1 would start at 2 but its deadline is 1.5: it leaves and item 2 starts at 2
    enq = np.array([0.0, 0.1, 0.2])
    svc = np.array([2.0, 5.0, 1.0])
    dl = np.array([INF, 1.5, INF])
    start, finish, served = fcfs_reneging(enq, svc, dl, 1)
    assert list(served) == [True, False, True]
    assert start[2] == pytest.approx(2.0)
    assert np.isnan(start[1])


def test_timing_prediction_deterministic_reading():
    # means: D 2 + E 1.5 + I 0.25 = 3.75 against T = 30 / s
    assert timing_prediction(Params(speed=1))
    assert timing_prediction(Params(speed=7))      # 30/7 = 4.29 > 3.75
    assert not timing_prediction(Params(speed=10))  # 3 < 3.75
    assert timing_prediction(Params(speed=10, variant="pause", pause=1.0))


def test_ample_reviewers_match_race_probability():
    # With effectively unlimited reviewers there is no queue, so intervention
    # capacity is P(D + E + I < T), estimated independently here.
    p = Params(speed=10, reviewers=100000, days=2000, warmup=0)
    caps = [simulate(p, s)["intervention_capacity"] for s in range(5)]
    rng = np.random.default_rng(123)
    m = 400000
    T = rng.gamma(p.t_irr_shape, p.t_irr_mean / p.speed / p.t_irr_shape, m)
    D = rng.exponential(p.det_mean, m)
    E = rng.gamma(p.eval_shape, p.eval_mean / p.eval_shape, m)
    race = np.mean(D + E + p.lag < T)
    assert np.mean(caps) == pytest.approx(race, abs=0.02)


def test_speed_lowers_capacity_and_raises_benefit():
    slow = simulate(Params(speed=1), 0)
    fast = simulate(Params(speed=10), 0)
    assert slow["intervention_capacity"] > fast["intervention_capacity"] + 0.3
    assert fast["benefit_per_benign"] > slow["benefit_per_benign"]


def test_full_suspension_equals_detection_before_irreversibility():
    r = simulate(Params(speed=10, variant="suspend", h=1.0, fa=0.0), 1)
    assert r["intervention_capacity"] == pytest.approx(r["detected_before_irreversible_obj"])
    assert r["benign_share_held"] == 0.0


def test_full_coverage_limits_intercept_everything():
    r = simulate(Params(speed=10, variant="limits", q=1.0, fp=0.0), 2)
    assert r["intervention_capacity"] == 1.0
    assert r["benign_mean_delay"] == pytest.approx(simulate(Params(speed=10), 2)["benign_mean_delay"])


def test_limits_restore_about_their_coverage():
    base = simulate(Params(speed=10), 3)["intervention_capacity"]
    r = simulate(Params(speed=10, variant="limits", q=0.5, fp=0.0), 3)["intervention_capacity"]
    assert r == pytest.approx(0.5 + 0.5 * base, abs=0.04)


def test_pause_adds_its_length_to_every_benign_delay():
    a = simulate(Params(speed=10), 4)["benign_mean_delay"]
    b = simulate(Params(speed=10, variant="pause", pause=4.0), 4)["benign_mean_delay"]
    assert b - a == pytest.approx(4.0, abs=1e-9)


def test_unknown_variant_rejected():
    with pytest.raises(ValueError):
        simulate(Params(variant="bogus"), 0)
