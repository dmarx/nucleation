import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model as m  # noqa: E402


def test_routine_probes_never_separate():
    for p in m.all_probes(caps=(True, False), delays=(0, 3)):
        if m.routine(p):
            assert m.trace("I", p) == m.trace("C", p)


def test_minimal_separating_probe_parts_at_enforcement():
    p = m.Probe("x", True, True, "withhold")
    ti, tc = m.trace("I", p), m.trace("C", p)
    assert ti[:3] == tc[:3]
    assert m.first_divergence(ti, tc) == "enforcement"
    assert ti[4] == "reversed" and tc[4] == "stands"


def test_incapable_enforcer_hides_the_difference():
    p = m.Probe("x", True, True, "withhold", cap=False)
    assert m.trace("I", p) == m.trace("C", p)


def test_delay_parts_timing_before_outcome():
    early = m.Probe("x", True, True, "withhold", delay=3, deadline=10)
    late = m.Probe("x", True, True, "withhold", delay=10, deadline=10)
    assert m.first_divergence(m.trace("I", early), m.trace("C", early)) == "enforcement"
    assert m.outcome("C", early) == "reversed"
    assert m.outcome("C", late) == "stands"


def test_structural_dependence():
    assert not m.f_depends_on_signal("I")
    assert m.f_depends_on_signal("C")


def test_game_depths():
    # E disposed to withhold (g > kw), deterred in I ((1-p) g < p c)
    pay = m.Payoffs(g=1.0, c=1.0, kw=0.5, p=0.6, u=0.5, l=1.0)
    assert m.first_divergence_game(pay, "myopic") == "enforcement"
    assert m.first_divergence_game(pay, "reviewer") == "ruling"
    assert m.first_divergence_game(pay, "full") == "action"
    # E not disposed to withhold: no difference at any depth
    pay2 = m.Payoffs(g=0.4, c=1.0, kw=0.5, p=0.6, u=0.5, l=1.0)
    for d in ("myopic", "reviewer", "full"):
        assert m.first_divergence_game(pay2, d) is None


def test_nonexecution_posterior():
    assert m.p_withheld_given_not_executed(1.0, 0.1) == 1.0
    assert m.p_withheld_given_not_executed(0.5, 0.0) == 0.0
    assert abs(m.p_withheld_given_not_executed(0.8, 0.5) - 0.4 / 0.6) < 1e-12
