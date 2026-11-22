"""Tests for the LEAD-123 agenda model. Run: python3 -I -m pytest -q."""
import itertools

import numpy as np
import pytest

import agenda_model as am


def test_cycle_prefs_is_a_condorcet_cycle():
    prefs = am.cycle_prefs()
    contests = am.all_contests(prefs)
    # three contests, each won 2-1
    assert len(contests) == 3
    assert all(margin == 1 for _, _, margin in contests)
    # the winning-move relation is W>R, R>S, S>W (a 3-cycle)
    wins = {(am.LABELS[w], am.LABELS[l]) for w, l, _ in contests}
    assert wins == {("W", "R"), ("R", "S"), ("S", "W")}


def test_full_graph_has_no_potential():
    prefs = am.cycle_prefs()
    contests = am.all_contests(prefs)
    assert am.topo_winner(contests, 3) is None
    # one of three arcs must reverse: nonintegrability 1/3
    assert am.min_feedback_arc_fraction(contests, 3) == pytest.approx(1 / 3)


def test_excluding_one_contest_makes_record_acyclic():
    prefs = am.cycle_prefs()
    contests = am.all_contests(prefs)
    for excluded in [frozenset(c[:2]) for c in contests]:
        admitted = {frozenset(c[:2]) for c in contests} - {excluded}
        res = am.recorded_outcome(prefs, admitted)
        assert res["has_potential"] is True
        assert res["nonintegrability"] == 0.0
        assert res["winner"] is not None


def test_chair_can_install_any_alternative():
    # The core agenda-power result: by choosing which single contest to leave
    # off, the chair can make each of the three options the recorded winner.
    prefs = am.cycle_prefs()
    installed = set(am.chair_can_install(prefs).values())
    assert installed == {"W", "R", "S"}


def test_sequential_agenda_order_decides_winner():
    # Against a Condorcet cycle, the successive procedure elects the option
    # introduced last: it faces the survivor in the final vote and the cycle
    # guarantees exactly one arc it wins.
    prefs = am.cycle_prefs()
    winners = {}
    for order in itertools.permutations(range(3)):
        w, _ = am.sequential_agenda(prefs, order)
        winners["".join(am.LABELS[o] for o in order)] = w
    # all three alternatives are reachable as winners across the six orders
    assert set(winners.values()) == {"W", "R", "S"}
    # the last-introduced option wins each time (property of a 3-cycle)
    for order_str, w in winners.items():
        assert w == order_str[-1]


def test_recorded_winner_depends_on_admission_not_preference():
    # Preferences are fixed; two different admission rules name two winners.
    prefs = am.cycle_prefs()
    pairs = [frozenset(c[:2]) for c in am.all_contests(prefs)]
    outs = {am.recorded_outcome(prefs, set(pairs) - {ex})["winner"]
            for ex in pairs}
    assert len(outs) == 3  # three admission rules, three recorded winners


def test_challenge_channel_raises_recorded_conflict():
    # CLAIM-448's prediction: raising the suppressed contest's legibility
    # monotonically raises recorded conflict and lowers coherence.
    prefs = am.cycle_prefs()
    contests = am.all_contests(prefs)
    suppressed = (contests[-1][0], contests[-1][1])
    rng = np.random.default_rng(0)
    rows = am.challenge_channel_sweep(prefs, suppressed, 3000, rng)
    conflict = [r["mean_nonintegrability"] for r in rows]
    coherent = [r["fraction_coherent"] for r in rows]
    # at zero legibility the record is always coherent, no conflict
    assert rows[0]["legibility"] == 0.0
    assert coherent[0] == 1.0
    assert conflict[0] == 0.0
    # monotone in the expected directions (allow Monte Carlo slack)
    assert conflict[-1] > conflict[0]
    assert coherent[-1] < coherent[0]
    for a, b in zip(conflict, conflict[1:]):
        assert b >= a - 0.02


def test_maintained_exclusion_is_persistent_but_an_artifact():
    # A regime that always excludes the closing contest yields one persistent
    # recorded winner over every window; occasional admission breaks coherence.
    prefs = am.cycle_prefs()
    contests = am.all_contests(prefs)
    suppressed = (contests[-1][0], contests[-1][1])
    maintained = am.persistence_windows(
        prefs, suppressed, 50, 0.0, np.random.default_rng(10))
    intermittent = am.persistence_windows(
        prefs, suppressed, 50, 0.5, np.random.default_rng(11))
    assert maintained["persistent"] is True
    assert len(maintained["distinct_winners"]) == 1
    assert intermittent["all_windows_coherent"] is False


def test_margins_symmetry_and_total():
    prefs = am.cycle_prefs()
    mg = am.margins(prefs)
    for i in range(3):
        for j in range(3):
            if i != j:
                assert mg[i, j] + mg[j, i] == 3  # three perspectives
