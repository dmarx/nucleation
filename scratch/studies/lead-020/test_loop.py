import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from loop import Config, Params, attention, commitment_score, lockin_rate, simulate, tracked  # noqa: E402
from dataclasses import replace  # noqa: E402

BARE = dict(capture=False, body=False, commit=False, fluency=False, others=False)


def test_attention_bounds_and_direction():
    assert attention(0.0, 1.0, 1.0) == 1.0
    assert attention(0.9, 1.0, 1.0) == pytest.approx(1.9)
    assert attention(0.9, -1.0, 1.0) == pytest.approx(0.1)
    assert attention(1.0, -1.0, 2.0) == 0.0
    assert attention(1.0, 1.0, 2.0) == 2.0


@pytest.mark.parametrize("m,r,s,kbar", [(0.3, 0.7, 0.5, 0.5), (-0.8, 0.1, 1.0, 0.2), (0.0, -2.0, 0.4, 0.9)])
def test_commitment_score_matches_case_106(m, r, s, kbar):
    # (p_B - r)^2 - (p_A - r)^2 = 4 s (r - kbar m)
    assert commitment_score(m, r, s, kbar) == pytest.approx(4 * s * (r - kbar * m))


def test_tracked_needs_a_run():
    assert tracked(np.array([1.0] * 20), 1.0)
    assert not tracked(np.array([1.0, -1.0] * 20), 1.0)


def test_lockin_rate_stuck_and_following():
    block = 50
    h = np.where((np.arange(400) // block) % 2 == 0, 1.0, -1.0)
    assert lockin_rate(np.full(400, 0.9), h, block) == 1.0
    assert lockin_rate(0.9 * h, h, block) == 0.0


def test_without_sense_drops_capture():
    c = Config().without("sense")
    assert not c.sense and not c.capture and c.body


def test_world_is_independent_of_the_loop():
    # action held fixed: the hidden state sequence is the same whatever the loop does
    p = Params()
    a = simulate(Config(), p, 600, 100, 0, record=True)["h"]
    b = simulate(Config(**BARE), replace(p, eta=2.0), 600, 100, 0, record=True)["h"]
    assert np.array_equal(a, b)


def test_bare_regime_a_locks_in_when_coupling_strong():
    p = replace(Params(), eta=0.5)
    rates = [simulate(Config(**BARE), p, 3000, 300, s)["lockin"] for s in range(5)]
    assert np.nanmean(rates) == 1.0


def test_bare_loop_without_gamma_arrow_does_not_lock_in():
    # post-hoc revision: no score, no authority, no capture (CLAIM-340)
    p = replace(Params(), eta=0.5)
    cfg = Config(**BARE, no_commit_mode="posthoc")
    rates = [simulate(cfg, p, 3000, 300, s)["lockin"] for s in range(5)]
    assert np.nanmean(rates) == 0.0


def test_no_evidence_is_blind():
    p = replace(Params(), eta=0.5)
    out = simulate(Config(sense=False, capture=False, body=False, others=False), p, 900, 300, 0)
    assert not out["first_block_tracked"]
