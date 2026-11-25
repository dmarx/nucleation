"""Tests for routes.py (LEAD-191). Run: python3 -I -m pytest -q (from this directory)."""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import routes as R  # noqa: E402

RNG = np.random.default_rng(191)
SAMPLE = [RNG.uniform(-1, 1, 3) * s for s in RNG.uniform(0, 1, 120)]


def test_pr_box_is_no_signalling_and_strongly_contextual():
    e = R.pr_like((0, 0, 0))
    assert R.signalling_fraction(e) == pytest.approx(0, abs=1e-9)
    assert R.contextual_fraction(e) == pytest.approx(1, abs=1e-9)
    assert R.cbd_contextual(e)
    assert R.sheaf_corrected(e)


def test_noncontextual_model_passes_every_test():
    # a deterministic global assignment x = (0, 0, 0): no signalling, no contextuality
    e = np.zeros((3, 4))
    e[:, 0] = 1
    assert R.signalling_fraction(e) == pytest.approx(0, abs=1e-9)
    assert R.contextual_fraction(e) == pytest.approx(0, abs=1e-9)
    assert not R.cbd_contextual(e)
    assert not R.sheaf_corrected(e)
    assert not R.ns_part_contextual(e)
    assert not R.nearest_ns_contextual(e)


@pytest.mark.parametrize("eps", SAMPLE)
def test_lp_matches_closed_forms(eps):
    e = R.pr_like(eps)
    cf = R.closed_form(eps)
    assert R.contextual_fraction(e) == pytest.approx(1, abs=1e-7)  # Prop. 3.3
    assert R.signalling_fraction(e) == pytest.approx(cf["SF"], abs=1e-7)  # Prop. 3.4
    if abs(cf["SF"] - 1 / 6) > 1e-6:
        assert R.sheaf_corrected(e) == cf["sheaf"]
    if abs(cf["Delta"] - 2) > 1e-6:
        assert R.cbd_contextual(e) == cf["cbd"]  # CNT1 = 3 - Delta - 1
    if abs(cf["SF"] - 1) > 1e-6:
        assert R.ns_part_contextual(e) == (cf["SF"] < 1)


@pytest.mark.parametrize("eps", SAMPLE)
def test_sheaf_region_inside_cbd_region(eps):
    cf = R.closed_form(eps)
    assert 2 * cf["SF"] - 1e-12 <= cf["Delta"] <= 6 * cf["SF"] + 1e-12
    if cf["sheaf"]:
        assert cf["cbd"]
    if cf["cbd"]:
        assert cf["SF"] < 1


@pytest.mark.parametrize("p", [1 / 6, 0.3, 0.5, 0.9, 0.99])
def test_uniform_family_diverges(p):
    # e = (1 - p) PR + p D, D deterministic and signalling
    e = R.pr_like((p, p, p))
    assert R.cbd_contextual(e)
    assert not R.sheaf_corrected(e)
    assert R.ns_part_contextual(e)


def test_fully_signalling_deterministic_model():
    # D: every context deterministic, marginals inconsistent; CF = 1 nonetheless
    e = R.pr_like((1, 1, 1))
    assert R.contextual_fraction(e) == pytest.approx(1, abs=1e-9)
    assert R.signalling_fraction(e) == pytest.approx(1, abs=1e-9)
    assert R.closed_form((1, 1, 1))["Delta"] == pytest.approx(2)
    assert not R.cbd_contextual(e)  # on the boundary CNT1 = 0
    assert not R.sheaf_corrected(e)
    assert not R.ns_part_contextual(e)


def test_cbd_lp_on_a_consistently_connected_noncontextual_case():
    # PR-like support cannot be noncontextual without signalling; mix with a
    # global assignment instead: half PR box, half x = (0,0,0)
    g = np.zeros((3, 4))
    g[:, 0] = 1
    e = 0.5 * R.pr_like((0, 0, 0)) + 0.5 * g
    # no signalling here, so CbD and the sheaf test must agree (CLAIM-374)
    assert R.signalling_fraction(e) == pytest.approx(0, abs=1e-9)
    assert R.cbd_contextual(e) == (R.contextual_fraction(e) > 1e-9)
