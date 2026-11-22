import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import ladder as L  # noqa: E402
import network as N  # noqa: E402


def test_probe_signatures_match_case_242_table():
    for state, sig in L.CATALOG.items():
        ok = {c: c != state for c in L.COMPONENTS}
        assert L.probe_truth(ok) == sig


def test_posterior_reproduces_case_242_numbers():
    # sensor pattern after all four probes: P(sensor) = 0.9604 / 1.0004
    p = L.posterior(L.CATALOG["sensor"])
    assert math.isclose(p["sensor"], 0.9604 / 1.0004, rel_tol=1e-9)
    # one silent injector test: likelihood ratio 0.98 / 0.02 = 49
    assert math.isclose((1 - L.EPS) / L.EPS, 49.0)


def test_mutual_information():
    a = np.array([0, 1] * 50)
    assert math.isclose(L.mutual_information(a, a), 1.0)
    assert L.mutual_information(a, np.zeros(100, int)) == 0.0


def test_rungs_share_the_sensor_channel():
    vals = {L.run(r, "relay", 3)["mi_pre"] for r in L.RUNGS}
    assert len(vals) == 1


def test_relay_acts_on_absence_without_registering():
    r = L.run("R0-relay", "sensor", 0)
    assert r["registrations"] == 0 and r["put_out_after"] == r["fires_after"]
    assert r["valve_open_no_fire"] > 1000


def test_tester_detects_but_does_not_locate_and_diagnoser_locates():
    r1 = L.run("R1-tester", "relay", 0)
    r2 = L.run("R2-diagnoser", "relay", 0)
    assert r1["registrations"] >= 1 and r1["located"] == []
    assert r2["located"][-1] == "relay"   # a misnaming is retested and corrected


def test_heat_fault_needs_the_reviser():
    assert L.run("R2-diagnoser", "heat-relay", 0)["located"] == []
    r3 = L.run("R3-reviser", "heat-relay", 0)
    assert r3["added_condition"] == ["hot"] and "relay" in r3["located"]


def test_fuse_recovers_state_with_true_maps():
    rng = np.random.default_rng(0)
    A = [N.rot(rng.uniform(-1, 1)) for _ in range(3)]
    b = [rng.normal(0, 1, 2) for _ in range(3)]
    z = np.array([0.7, -1.2])
    o = [Ai @ z + bi for Ai, bi in zip(A, b)]
    assert np.allclose(N.fuse(A, b, o), z)


def test_self_consistency_has_a_gauge_freedom():
    # a common shift of every bias, with the state shifted back, leaves all
    # residuals unchanged: disagreement cannot see it
    rng = np.random.default_rng(1)
    A = [N.rot(rng.uniform(-1, 1)) for _ in range(3)]
    b = [rng.normal(0, 1, 2) for _ in range(3)]
    o = [rng.normal(0, 1, 2) for _ in range(3)]
    z = N.fuse(A, b, o)
    v = np.array([0.5, 0.2])
    b2 = [bi + Ai @ v for Ai, bi in zip(A, b)]
    z2 = N.fuse(A, b2, o)
    assert np.allclose(z2, z - v)
    r1, r2 = N.residuals(A, b, o, z), N.residuals(A, b2, o, z2)
    assert all(np.allclose(x, y) for x, y in zip(r1, r2))


def test_anchored_beats_self_on_one_seed():
    a = N.run("anchored", 0, T=1500)
    s = N.run("self", 0, T=1500)
    assert a["err_late"] < s["err_late"] and s["rad_late"] < 0.3
