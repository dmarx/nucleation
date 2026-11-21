# scratch/formal/decision-census/test_census.py
import pytest

from census import cohen_kappa, crosstab, jaccard, week_of


def test_kappa_perfect_and_chance():
    assert cohen_kappa(["a", "b", "a"], ["a", "b", "a"]) == pytest.approx(1.0)
    # Observed 0.5, expected 0.5 -> kappa 0
    assert cohen_kappa(["a", "a", "b", "b"], ["a", "b", "a", "b"]) == pytest.approx(0.0)


def test_kappa_single_category_agreeing_is_one():
    assert cohen_kappa(["x", "x"], ["x", "x"]) == 1.0


def test_jaccard_of_lists():
    assert jaccard(["a", "b"], ["b", "c"]) == pytest.approx(1 / 3)
    assert jaccard([], []) == 1.0


def test_week_of_counts_from_the_scaffold():
    assert week_of("2026-09-25") == 1
    assert week_of("2026-10-02") == 2
    assert week_of("2026-11-19") == 8


def test_crosstab_counts_pairs():
    rows = [{"a": "x", "b": "p"}, {"a": "x", "b": "q"}, {"a": "y", "b": "p"}]
    assert crosstab(rows, "a", "b") == {("x", "p"): 1, ("x", "q"): 1, ("y", "p"): 1}
