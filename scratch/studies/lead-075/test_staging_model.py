import math

import numpy as np
import pytest

from staging_model import (Params, bottleneck, least_time, time_profile,
                           capacity_for_deadline, readiness, readiness_mc,
                           classify)

P = Params()  # CASE-198's numbers


def test_case_233_home_bottleneck():
    # CLAIM-571 / CASE-233: r(q) = 0.7 + 2.4q(1-q), B* = 1.3
    assert bottleneck(P, Z=(0,)) == pytest.approx(1.3)


def test_case_198_staging_bottleneck():
    # CASE-198: with the staging architecture admitted, B* = 1.0
    assert bottleneck(P, Z=(0, 1)) == pytest.approx(1.0)


def test_bottleneck_never_rises_when_repertoire_grows():
    for beta0 in (0.5, 1.5, 2.4, 3.0):
        p = Params(beta0=beta0)
        assert bottleneck(p, (0, 1)) <= bottleneck(p, (0,)) + 1e-12


def test_gap_disconnects_home_and_staging_reconnects():
    p = Params(gap=True)
    assert math.isinf(bottleneck(p, (0,)))
    assert bottleneck(p, (0, 1)) == pytest.approx(1.0)
    # switching only on the left of the gap cannot reach B
    p2 = Params(gap=True, switch_ok=(0.0, 0.4))
    assert math.isinf(bottleneck(p2, (0, 1)))


def test_least_time_values():
    # at b = 1.0 only the staging route: switch, cross under staging, switch
    assert least_time(P, 1.0, (0, 1)) == pytest.approx(0.5 + 2.0 + 0.5)
    # at b = 1.3 the direct route, time 1
    assert least_time(P, 1.3, (0, 1)) == pytest.approx(1.0)
    assert math.isinf(least_time(P, 0.99, (0, 1)))
    assert math.isinf(least_time(P, 1.2, (0,)))


def test_least_time_nonincreasing_in_budget():
    bs = np.linspace(0.9, 1.5, 25)
    ts = [least_time(P, b, (0, 1)) for b in bs]
    for a, c in zip(ts, ts[1:]):
        assert c <= a + 1e-12


def test_time_profile_matches_pointwise():
    bs, ts = time_profile(P, (0, 1))
    assert bs[0] == pytest.approx(1.0)
    for b in np.linspace(1.0, 1.4, 17):
        k = np.nonzero(bs <= b + 1e-12)[0][-1]
        assert least_time(P, b, (0, 1)) == pytest.approx(ts[k])


def test_capacity_for_deadline():
    assert capacity_for_deadline(P, 3.0, (0, 1)) == pytest.approx(1.0)
    assert capacity_for_deadline(P, 1.0, (0, 1)) == pytest.approx(1.3)
    assert math.isinf(capacity_for_deadline(P, 0.5, (0, 1)))


def test_readiness_deterministic_cases():
    assert readiness(P, 1.0, 3.0, (0, 1)) == 1.0
    assert readiness(P, 1.0, 3.0, (0,)) == 0.0
    assert readiness(P, 1.0, 3.0, (0,), rho=0.3, p_res=0.6) == pytest.approx(0.6)


@pytest.mark.parametrize("Z", [(0,), (0, 1)])
def test_readiness_matches_monte_carlo(Z):
    kw = dict(rho=0.25, p_res=0.5, u_max=0.4)
    exact = readiness(P, 1.2, 3.0, Z, **kw)
    mc = readiness_mc(P, 1.2, 3.0, Z, n=20000, seed=1, **kw)
    assert mc == pytest.approx(exact, abs=0.015)


def test_classify():
    rA = rB = 0.7
    assert classify(1.3, 1.0, 0.6, 0, rA, rB) == "not holdable"
    assert classify(1.3, 1.0, 1.3, 0, rA, rB) == "reachable as is"
    assert classify(math.inf, math.inf, 1.0, 0.5, rA, rB) == "statically feasible, unreachable"
    assert classify(1.3, 1.0, 0.8, 0.1, rA, rB) == "reachable, too expensive"
    assert classify(1.3, 1.0, 1.0, 0.1, rA, rB) == "only through architectural change"
    assert classify(1.3, 1.2, 1.1, 0.2, rA, rB) == "only with temporary reserve"
    assert classify(1.3, 1.0, 1.0, 0.3, rA, rB) == "either change or reserve"
    assert classify(1.3, 1.1, 0.95, 0.15, rA, rB) == "change and reserve together"


def test_classify_deadline():
    assert classify(math.inf, math.inf, 1.0, 0.5, 0.7, 0.7, B_untimed=1.0) == "reachable, not by the deadline"
    assert classify(math.inf, math.inf, 1.0, 0.5, 0.7, 0.7, B_untimed=math.inf) == "statically feasible, unreachable"


def test_staging_route_too_slow_for_tight_deadline():
    # the fastest route that uses the staging architecture takes >= 2.58,
    # so at tau = 2 admitting it changes nothing
    assert capacity_for_deadline(P, 2.0, (0, 1)) == pytest.approx(1.3)
    assert math.isinf(capacity_for_deadline(Params(gap=True), 2.0, (0, 1)))
