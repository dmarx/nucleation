import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rsi  # noqa: E402


def test_theta0_is_lead048_settings():
    v = rsi.theta_values(rsi.THETA0)
    assert v == {"AUDIT_EVERY": 10, "N_AUDIT": 256, "SELF_CHECK_EVERY": 20,
                 "REPAIR_STEPS": 30, "TEACH": 0.1}


def test_apply_move_bounds():
    assert rsi.apply_move(rsi.THETA0, (0, -1)) == (0, 4, 1, 1, 1)
    assert rsi.apply_move(rsi.THETA0, (1, 1)) is None


def test_self_check_off_config():
    th = list(rsi.THETA0)
    th[rsi.SC] = 4
    c = rsi.cfg_for(tuple(th), "ordinary")
    assert c.self_check is False
    assert rsi.cfg_for(rsi.THETA0, "ordinary").self_check is True


def test_episode_deterministic_and_lesion_effect():
    a = rsi.episode(rsi.THETA0, "dmg:score", 7)
    assert a == rsi.episode(rsi.THETA0, "dmg:score", 7)
    assert a[1] is True
    off = list(rsi.THETA0)
    off[rsi.SC] = 4
    assert rsi.episode(tuple(off), "dmg:score", 7)[1] is False


def test_obsolete_injury_resets_teacher():
    cfg = rsi.cfg_for(rsi.THETA0, "obsolete")
    o = rsi.Org140(cfg, 1)
    o.st.interp = -1
    o.injure(cfg.T_INJ)
    assert o.st.interp == 1


def test_suite_lesions():
    s = rsi.Suite(0.5, 0.5, lesion="generate")
    ks = s.kinds(np.random.default_rng(0), 50)
    assert set(ks) == {"ordinary"}
    res = [("dmg:admit", (-0.8, False)), ("ordinary", (-0.1, True))]
    assert rsi.Suite(0.5, 0, lesion="admit").score(res) == -0.1
    assert rsi.Suite(0.5, 0).score(res) == np.mean([-0.8, -0.1])
    sc = rsi.Suite(0.5, 0, lesion="score")
    assert abs(sc.score(res, incumbent=True) - sc.score(res) - 0.05) < 1e-12


def test_canary_flags_generate_lesion_and_restores():
    suite = rsi.Suite(0.25, 0.25, lesion="generate")
    th, info = rsi.generation(rsi.THETA0, rsi.PHI0, rsi.Archive(), suite,
                              np.random.default_rng(3), rsi.Ledger())
    assert info["flagged"] and th == rsi.THETA0 and suite.lesion == "sham"


def test_canary_passes_intact_suite():
    suite = rsi.Suite(0.25, 0.25)
    flags = 0
    for s in range(5):
        _, info = rsi.generation(rsi.THETA0, rsi.PHI0, rsi.Archive(), suite,
                                 np.random.default_rng(s), rsi.Ledger())
        flags += info["flagged"]
    assert flags == 0


def test_weakening():
    assert rsi.weakens_phi(rsi.PHI0, (0, 0, 1, 0, 1))
    assert rsi.weakens_phi(rsi.PHI0, (0, 1, 1, 0, 0))
    assert not rsi.weakens_phi(rsi.PHI0, (1, 1, 1, 1, 1))
    assert rsi.weakens_theta_move((rsi.SC, 1))
    assert not rsi.weakens_theta_move((rsi.SC, -1))
    assert not rsi.weakens_theta_move((0, 1))


def test_archive_roundtrip_and_weights():
    a = rsi.Archive()
    a.add((0, 1), 0.01)
    a.add((0, 1), 0.03)
    b = rsi.Archive.load(a.dump())
    assert b.data == {(0, 1): [0.01, 0.03]}
    w = b.weights([(0, 1), (0, -1), (1, -1)])
    assert abs(w.sum() - 1) < 1e-12 and w[0] > w[2]


def test_improve_deterministic():
    r1 = rsi.improve(rsi.THETA0, rsi.PHI0, rsi.Archive(), 2, 11)
    r2 = rsi.improve(rsi.THETA0, rsi.PHI0, rsi.Archive(), 2, 11)
    assert r1 == r2
