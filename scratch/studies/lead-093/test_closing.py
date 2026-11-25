import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from closing import (params, rhs, produce_steady_states, stable, maintained_state,
                     closes, background_N, sigma_needed, run, y0_empty,
                     critical, run_generations, gillespie_extinction,
                     min_founding_time, persists_after_withdrawal)


def test_steady_states_are_zeros_of_rhs():
    for kw in [dict(), dict(kT=0.15), dict(eps=0.3), dict(sigma=0.02)]:
        p = params(**kw)
        for m, T, N, B in produce_steady_states(p):
            f = np.array(rhs(0, [m, T, N, B, 0.0], p))
            assert np.max(np.abs(f[:4])) < 1e-8


def test_base_is_bistable_with_a_saddle():
    p = params()
    sts = produce_steady_states(p, 0.0)
    assert len(sts) == 3
    st = [stable(p, s, 0.0)[0] for s in sts]
    assert st == [True, False, True]


def test_no_loop_no_closure():
    for kT in [0.01, 0.1, 1.0]:
        assert not closes(params(beta=0.0, kT=kT))


def test_background_matches_spontaneous_only():
    p = params(a1=0.0, beta=0.0)
    sts = produce_steady_states(p, 0.0)
    assert len(sts) == 1
    m, T, N, B = sts[0]
    # with a1 = 0 consumption is small; N = a0 m^2 / d with m slightly below J/delta
    assert abs(N - p["a0"] * m * m / p["d"]) < 1e-12
    assert abs(N - background_N(p)) / background_N(p) < 0.01


def test_sigma_needed_gives_a_steady_state():
    p = params(kT=0.4)
    sig, m, T = sigma_needed(p, 2.0)
    assert sig > 0
    q = params(kT=0.4, sigma=sig)
    f = np.array(rhs(0, [m, T, 2.0, 0.0, 0.0], q))
    assert np.max(np.abs(f[:4])) < 1e-9


def test_sigma_needed_zero_when_closed():
    p = params()
    ms = maintained_state(p)
    sig, _, _ = sigma_needed(p, 0.99 * ms[2])
    assert sig == 0.0


def test_repair_conserves_teacher_mass_up_to_loss():
    p = params(arm="repair", rho=0.5, lam=0.05, sigma=0.03)
    y = [3.0, 1.2, 2.0, 0.1, 0.7]
    f = rhs(0, y, p)
    assert abs((f[1] + f[4]) - (p["sigma"] - p["lam"] * y[4])) < 1e-12


def test_critical_kT_is_a_fold():
    p = params()
    kc = critical(p, "kT", 0.01, 5.0)
    below = produce_steady_states(params(kT=kc * (1 - 1e-4)), 0.0)
    above = produce_steady_states(params(kT=kc * (1 + 1e-4)), 0.0)
    assert len(below) == 3 and len(above) == 1
    # saddle and maintained state close together just below the fold
    assert abs(below[2][2] - below[1][2]) < 0.2 * below[2][2]


def test_generations_sum_to_aggregate():
    p = params()
    t, m, T, N = run_generations(p, 0.05, 10.0, 200.0, G=40, n_eval=11)
    from closing import founding
    sol_t, Y = run(p, y0_empty(p), 200.0, sigma_of_t=founding(0.05, 10.0), n_eval=11)
    assert np.allclose(T.sum(0), Y[1], rtol=1e-4, atol=1e-7)
    assert np.allclose(N.sum(0), Y[2], rtol=1e-4, atol=1e-7)
    assert np.allclose(m, Y[0], rtol=1e-5)


def test_founding_bisection_brackets():
    p = params()
    tw = min_founding_time(p, 0.1)
    q = dict(p)
    q["sigma"] = 0.1
    from closing import run as r
    _, Y1 = r(q, y0_empty(p), tw + 0.1, n_eval=2)
    _, Y0 = r(q, y0_empty(p), max(tw - 0.1, 1e-6), n_eval=2)
    assert persists_after_withdrawal(p, Y1[:, -1])
    assert not persists_after_withdrawal(p, Y0[:, -1])


def test_gillespie_dies_at_high_turnover():
    p = params(kT=2.0)
    rng = np.random.default_rng(0)
    t = gillespie_extinction(p, 5, (20, 10, 10), 500.0, rng)
    assert t < 500.0
    assert gillespie_extinction(p, 5, (20, 0, 0), 500.0, rng) == 0.0
