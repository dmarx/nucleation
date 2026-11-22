import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from costmodel import (Demands, OnDemand, Store, availability_on_demand,
                       availability_store, break_even_n, lifetime,
                       per_demand_store)


def test_reduces_to_claim_303_case_088():
    # CASE-088: reconstruct 15, file 25, retrieve and check 3, three uses.
    s, a, d = Store(F=25, rho=1, v=2), OnDemand(c=15), Demands(n=3)
    r = lifetime(s, a, [d])
    assert math.isclose(r["on_demand"], 45)
    assert math.isclose(r["store"], 34)
    assert math.isclose(break_even_n(s, a, d), 25 / 12)


def test_staleness_moves_break_even_and_can_forbid_it():
    a, d = OnDemand(c=15), Demands(n=3)
    base = break_even_n(Store(F=25, rho=1, v=2), a, d)
    stale = break_even_n(Store(F=25, rho=1, v=2, sigma=0.1, delta=0.5, L=60), a, d)
    assert stale > base
    never = break_even_n(Store(F=25, rho=1, v=2, sigma=0.3, delta=0.0, L=60), a, d)
    assert never == math.inf


def test_phase_price_alone_can_make_a_store_pay():
    # Same work either way; the store moves it to a cheaper moment.
    a = OnDemand(c=2)
    flat = lifetime(Store(F=8, lam_F=1, rho=0), a, [Demands(n=4, lam=1)])
    shifted = lifetime(Store(F=8, lam_F=1, rho=0), a, [Demands(n=4, lam=3)])
    assert math.isclose(flat["saving"], 0)
    assert shifted["saving"] > 0


def test_feasibility_separate_from_lifetime():
    # CLAIM-761: 12 fresh, 3 with the store, budget 5; construction 100.
    s, a, d = Store(F=100, rho=3), OnDemand(c=12), Demands(n=1, B=5)
    assert availability_on_demand(a, d) == 0.0
    assert availability_store(s, a, d) == 1.0
    assert lifetime(s, a, [d])["saving"] < 0


def test_erosion_raises_fallback_only():
    a = OnDemand(c=10)
    d = Demands(n=1, pi=0.5)
    x0 = per_demand_store(Store(F=0, rho=1), a, d)
    x1 = per_demand_store(Store(F=0, rho=1, eps=0.5), a, d)
    assert math.isclose(x1 - x0, 0.5 * 0.5 * 10)
    # A store that always serves and is never wrong never falls back.
    d1 = Demands(n=1, pi=1.0)
    assert per_demand_store(Store(F=0, rho=1, eps=0.5), a, d1) == 1


def test_party_split_sums_to_total():
    s = Store(F=10, party_F="maker", spill=0.5, n_other=4, party_other="others")
    r = lifetime(s, OnDemand(c=3), [Demands(n=5)])
    assert math.isclose(sum(r["store_by_party"].values()), r["store"])
    assert set(r["store_by_party"]) == {"maker", "others", "user"}


def test_erosion_weight_is_chance_of_fallback_plus_checking_share():
    # d(cost)/d(eps) = c * [(1 - pi) + pi * (sigma * delta + phi)], where phi
    # is the share of the computing route that checking repeats, so that
    # v = v0 + phi * c * (1 + eps).
    c, pi, sigma, delta, phi, v0 = 10.0, 0.7, 0.1, 0.5, 0.2, 1.0
    a, d = OnDemand(c=c), Demands(n=1, pi=pi)
    def cost(eps):
        s = Store(F=0, rho=1, v=v0 + phi * c * (1 + eps), sigma=sigma,
                  delta=delta, eps=eps)
        return per_demand_store(s, a, d)
    slope = (cost(0.3) - cost(0.0)) / 0.3
    assert math.isclose(slope, c * ((1 - pi) + pi * (sigma * delta + phi)))
