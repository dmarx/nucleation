# record/promotion-audit/test_triage_bundling.py
"""Tests for triage_bundling.score: each of the three bundling signals, alone and together."""
from triage_bundling import score

READ = {"LIT-001"}


def test_no_signal_scores_zero():
    fm = {"title": "A single statement", "promote_when": "A close reading of the proof.", "source": ["LIT-999"]}
    assert score(fm, READ) == (0, {"extends": 0, "compound": 0, "read": 0})


def test_extension_in_promote_when():
    fm = {"title": "A statement", "promote_when": "A measurement on trained networks.", "source": []}
    assert score(fm, READ)[1]["extends"] == 1


def test_general_case_counts_as_extension():
    fm = {"title": "A statement", "promote_when": "A proof for the general case.", "source": []}
    assert score(fm, READ)[1]["extends"] == 1


def test_compound_title():
    fm = {"title": "X holds, so Y follows", "promote_when": "", "source": []}
    assert score(fm, READ)[1]["compound"] == 1


def test_read_source():
    fm = {"title": "A statement", "promote_when": "", "source": ["LIT-001"]}
    assert score(fm, READ)[1]["read"] == 1


def test_all_three():
    fm = {"title": "X and Y", "promote_when": "An experiment with people.", "source": ["LIT-002", "LIT-001"]}
    assert score(fm, READ)[0] == 3


def test_missing_fields_are_tolerated():
    assert score({}, READ)[0] == 0
