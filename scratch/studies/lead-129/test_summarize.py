"""Tests for summarize.py.  Run:  python3 -I -m pytest test_summarize.py"""
import summarize


def test_persistence():
    assert summarize.persistence({"recognition": 1999, "correction": 2007}) == 8
    assert summarize.persistence({"recognition": 2019, "correction": 2019}) == 0


def test_pair_gap_direction():
    pair = {
        "revising_arm": {"recognition": 2004, "correction": 2006},
        "fixed_arm": {"recognition": 1999, "correction": 2007},
    }
    # fixed left it 8 yr, revising 2 yr -> gap +6 (direction CLAIM-685 predicts)
    assert summarize.pair_gap(pair) == 6


def test_real_data_all_gaps_positive():
    data = summarize.load()
    rows = summarize.summarize(data)
    assert len(rows) == 3
    assert all(r["gap_years"] > 0 for r in rows)


def test_extreme_is_centuries():
    x = summarize.load()["unmatched_extreme"]
    assert x["correction"] - x["recognition"] > 100
