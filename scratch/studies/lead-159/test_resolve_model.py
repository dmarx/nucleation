import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import resolve_model as m  # noqa: E402

N = 64


def stream(env="neither", age=300, vis="full", seed=1):
    return m.make_stream(env, age, vis, N, seed)


def test_stream_independent_of_agent_and_condition():
    a = stream("defeater")
    b = stream("defeater")
    for k in ("imm", "lng", "obs", "u"):
        assert np.array_equal(a[k], b[k])


def test_events_matched_in_size_and_onset():
    d = stream("defeater")
    i = stream("irrelevant")
    age = d["age"]
    # long-run difference B - A flips by 2*DELTA under the defeater only
    dl = d["mu_l"][:, 1] - d["mu_l"][:, 0]
    assert dl[age - 1] - dl[age] == pytest.approx(2 * m.DELTA)
    il = i["mu_l"][:, 1] - i["mu_l"][:, 0]
    assert np.allclose(il, m.DELTA)
    # the irrelevant event shifts the immediate difference by the same
    # amount at the same trial
    imm_mean_before = i["imm"][:age].mean(axis=(0, 1))
    imm_mean_after = i["imm"][age:].mean(axis=(0, 1))
    shift = (imm_mean_after - imm_mean_before)
    assert shift[0] - shift[1] == pytest.approx(2 * m.DELTA, abs=0.05)


def test_ablation_matches_information_and_capacity():
    """Before the onset an ablated run is the intact run, trial for trial:
    same inputs, same state, same choices."""
    s = stream("irrelevant")
    r0 = m.simulate("R", "intact", s, record_slow=True)
    r1 = m.simulate("R", "lesion", s, record_slow=True)
    age = s["age"]
    assert np.array_equal(r0["choices"][:age], r1["choices"][:age])
    assert np.allclose(r0["c"][:age], r1["c"][:age])
    assert not np.array_equal(r0["choices"][age:], r1["choices"][age:])


def test_lesion_freezes_and_perturb_recovers():
    s = stream("neither", age=300)
    les = m.simulate("R", "lesion", s, record_slow=True)
    per = m.simulate("R", "perturb", s, record_slow=True)
    assert np.allclose(les["lam"][-1], m.LAM0)
    assert per["lam"][-1].mean() > 0.8


def test_imposed_and_inertia_have_no_slow_dynamics():
    s = stream("defeater")
    for ag, lam in (("P", m.LAM_IMPOSED), ("I", m.LAM0)):
        r = m.simulate(ag, "intact", s, record_slow=True)
        assert np.allclose(r["lam"], lam)
        assert np.allclose(r["a"], 1.0)


def test_entrenchment_closes_admission():
    s = stream("neither", age=2000)
    r = m.simulate("E", "intact", s, record_slow=True)
    assert r["a"][-1].mean() < 0.05
    assert r["lam"][-1].mean() > 0.9


def test_yoked_uses_source_trajectory():
    s = stream("defeater")
    src = m.simulate("E", "intact", stream("neither", seed=2),
                     record_slow=True)
    r = m.simulate("E", "yoked", s, yoke=src, record_slow=True)
    age = s["age"]
    assert np.allclose(r["lam"][age:], src["lam"][age:])
    assert np.allclose(r["a"][age:], src["a"][age:])


def test_routed_attenuates_disconfirming_evidence():
    full = m.simulate("R", "intact", stream("defeater", vis="full"))
    routed = m.simulate("R", "intact", stream("defeater", vis="routed"))
    age = 300
    # c falls less far in the same number of trials when routed
    assert (full["c"][age + 200].mean() < routed["c"][age + 200].mean())


def test_endpoints_on_constructed_choices():
    s = stream("defeater", age=300)
    T = s["T"]
    ch = np.ones((T, N), dtype=np.int8)
    ch[300 + 100:, : N // 2] = 0  # half switch to A 100 trials after onset
    c = np.zeros((T, N))
    e = m.endpoints(ch, c, s)
    assert e["p_revise"] == pytest.approx(0.5)
    assert e["t_revise_median"] == pytest.approx(100 + m.RUNWIN // 2 + 1,
                                                 abs=1)
    assert e["pre_shareB"] == 1.0
    # regret: B is worse by DELTA after the defeater for the half that stays
    assert e["regret_per_trial"] > 0
