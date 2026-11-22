# Independent pytest for the restriction-trap model. Re-derives the key facts
# rather than re-asserting the script's own numbers.
# Run: OMP_NUM_THREADS=1 python3 -I -m pytest scratch/studies/lead-104/test_restriction_trap.py -q
import math
import importlib.util
import os

_spec = importlib.util.spec_from_file_location(
    "restriction_trap",
    os.path.join(os.path.dirname(__file__), "restriction_trap.py"))
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)


def test_free_landscape_matches_claim605():
    # The modification keeps CLAIM-605's free party: C=0, 0.276, 0.7.
    assert rt.free_limit(rt.C_LOW + 0.01) > 0.69     # above threshold -> kept
    assert rt.free_limit(rt.C_LOW - 0.01) < 0.01     # below -> lost
    assert abs(rt.C_HIGH - 0.7) < 1e-9


def test_bare_restriction_never_reinstates():
    # No route: monotone exp decay, so a party below C_r (restricted for lack
    # of competence) never reaches it -- the gate never opens.
    for c0 in (0.3, 0.5, 0.59):
        c_end, reinstated, t = rt.sim(c0, rt.C_R, rho=0.0, g=0.0)
        assert reinstated is False and t is None and c_end < 0.01


def test_decay_is_the_evidence():
    # Each review reads strictly less competence than the last; all below C_r.
    r = [0.5 * math.exp(-rt.MU * t) for t in (0, 2, 4, 6)]
    assert r == sorted(r, reverse=True) and max(r) < rt.C_R


def test_recoverability_deadline():
    # Freed before t_dead the party recovers; after it, it does not.
    for t_free in (0.5, 1.5):
        assert rt.free_limit(0.5 * math.exp(-rt.MU * t_free)) > 0.6
    for t_free in (2.5, 4.0):
        assert rt.free_limit(0.5 * math.exp(-rt.MU * t_free)) < 0.6


def test_practice_route_needs_rho_crit():
    # Below rho_crit=0.8 no positive restricted steady state exists.
    assert abs(rt.RHO_CRIT - 0.8) < 1e-12
    assert rt.sim(0.5, rt.C_R, rho=0.7, g=0.0)[1] is False
    assert rt.sim(0.5, rt.C_R, rho=0.7, g=0.0)[0] < 0.01


def test_training_route_ignites_from_zero():
    # Training adds capacity directly: C -> g/mu, reinstates iff g >= mu*C_r,
    # independent of the start (even C0=0).
    assert abs(rt.G_CRIT - rt.MU * rt.C_R) < 1e-12
    assert rt.sim(0.0, rt.C_R, rho=0.0, g=0.20)[1] is True
    assert rt.sim(0.0, rt.C_R, rho=0.0, g=0.15)[1] is False
    assert abs(rt.sim(0.4, rt.C_R, rho=0.0, g=0.12,
                      gated=False)[0] - 0.12 / rt.MU) < 1e-2


def test_each_condition_necessary():
    # (1) no decay: a static bar, not a worsening loop.
    assert abs(rt.sim(0.5, rt.C_R, rho=0.0, g=0.0, decay=False)[0] - 0.5) < 1e-6
    # (2) ungated release before the deadline recovers (loop cannot form).
    assert rt.free_limit(0.5 * math.exp(-rt.MU * 1.0)) > 0.69
    # (3) a sufficient route reinstates (covered above).
    assert rt.sim(0.5, rt.C_R, rho=1.0, g=0.0)[1] is True


def test_main_runs():
    rt.main()
