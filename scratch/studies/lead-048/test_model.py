"""Tests for model.py (LEAD-048). Run: python3 -I -m pytest -q test_model.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import Config, World, State, admit_probs, score, run, LESIONS


def test_world_schedule_and_matched_stream():
    c = Config(env2="out_family")
    w = World(c, 3)
    assert w.regime(0) == 1 and w.regime(c.T1) == -1 and w.regime(c.T2) == 0
    a = World(c, 3).sample(150, 100)
    b = World(c, 3).sample(150, 256)
    # fewer draws see a prefix of the same stream
    assert a[0] <= b[0] and a == World(c, 3).sample(150, 100)


def test_admission_rates():
    c = Config(admission="selective")
    st = State(interp=1)
    assert admit_probs(c, st, 1) == 0.9 and admit_probs(c, st, 0) == 0.1
    st.interp = 0
    assert admit_probs(c, st, 1) == 1.0
    # protection is maintained: lost below G_MIN
    c2 = Config(admission="protected")
    st2 = State(interp=-1, G=0.1)
    assert admit_probs(c2, st2, 0) == 0.9
    st2.G = 1.0
    st2.broken["admit"] = True
    assert admit_probs(c2, st2, 1) == 0.05


def test_scoring_capture_and_ipw():
    st = State(interp=1)
    assert abs(score(Config(), st, 25, 75, 1, 1) - 0.25) < 1e-12
    assert abs(score(Config(scoring="captured"), st, 25, 75, 1, 1) - 0.65) < 1e-12
    # selective admission under belief +, truth 0.25: admitted 225 ones
    # and 75 zeros of 250/750; IPW recovers 0.25
    m = score(Config(scoring="ipw"), st, 225, 75, 0.9, 0.1)
    assert abs(m - 0.25) < 1e-12


def test_reference_arm_corrects_twice_and_capture_fails_first():
    c = Config()
    assert all(run(c, s)["S1"] and run(c, s)["S2"] for s in range(4))
    for kw in ({"scoring": "captured"}, {"admission": "selective"}):
        assert sum(run(Config(**kw), s)["S1"] for s in range(8)) <= 2
    # IPW repairs selective admission
    assert all(run(Config(admission="selective", scoring="ipw"), s)["S1"]
               for s in range(4))


def test_double_lesion_separates_reciprocal_from_external():
    r = [run(Config(maintenance="reciprocal", lesion="double"), s)["S2"] for s in range(4)]
    e = [run(Config(maintenance="external", lesion="double"), s)["S2"] for s in range(4)]
    assert not any(r) and all(e)


def test_component_lesion_needs_self_check():
    for L in ("generate", "admit", "score"):
        on = run(Config(lesion=L), 1)
        off = run(Config(lesion=L, self_check=False), 1)
        assert on["S2"] and on["flag_before_act"]
        assert not off["S2"]


def test_matched_branch_runs_all_lesions():
    for L in LESIONS:
        out = run(Config(lesion=L, matched=True), 0)
        assert out["S1"] is True and "S2" in out
