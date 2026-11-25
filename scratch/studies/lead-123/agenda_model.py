"""Three-perspective agenda model with a latent Condorcet cycle (LEAD-123).

A legibility/agenda regime selects which pairwise contests enter the record.
The point of the model is that the *recorded* outcome -- whether the record is
coherent (admits a potential), which option it names as winner, and how much
conflict it shows -- is set by the admission rule, not by the perspectives'
preferences, which are held fixed throughout.

Run as a script (`python3 -I agenda_model.py`) to reproduce results.json.
Functions are unit-tested in test_agenda_model.py.

Preferences are a (P, M) integer array of ranks: prefs[p, o] is the rank that
perspective p assigns option o, 0 = most preferred. Options are referred to by
integer index; a label map is kept only for printing.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

# The record's own Condorcet cycle (CLAIM-451): three perspectives, three
# options W(ork), R(ecovery), S(ociety). Productivity W>R>S, recovery R>S>W,
# belonging S>W>R. Pairwise majority: W beats R, R beats S, S beats W.
LABELS = ("W", "R", "S")
PERSPECTIVES = ("productivity", "recovery", "belonging")


def cycle_prefs() -> np.ndarray:
    """Ranks for the latent Condorcet cycle. Row p = perspective p's ranks."""
    orders = (("W", "R", "S"), ("R", "S", "W"), ("S", "W", "R"))
    prefs = np.zeros((3, 3), dtype=int)
    for p, order in enumerate(orders):
        for rank, lab in enumerate(order):
            prefs[p, LABELS.index(lab)] = rank
    return prefs


def margins(prefs: np.ndarray) -> np.ndarray:
    """margins[i, j] = number of perspectives ranking option i above option j."""
    p, m = prefs.shape
    out = np.zeros((m, m), dtype=int)
    for i in range(m):
        for j in range(m):
            if i != j:
                out[i, j] = int(np.sum(prefs[:, i] < prefs[:, j]))
    return out


def all_contests(prefs: np.ndarray):
    """Every pairwise majority contest as (winner, loser, margin).

    margin is winners-minus-losers votes; ties (even electorate) are skipped.
    """
    p, m = prefs.shape
    mg = margins(prefs)
    out = []
    for i, j in itertools.combinations(range(m), 2):
        if mg[i, j] > mg[j, i]:
            out.append((i, j, mg[i, j] - mg[j, i]))
        elif mg[j, i] > mg[i, j]:
            out.append((j, i, mg[j, i] - mg[i, j]))
        # exact tie: no recorded winner for the pair
    return out


def topo_winner(edges, m: int):
    """A total order (as a tuple of option indices) consistent with the directed
    edges (winner, loser, *), or None if the edges contain a cycle. The winner
    is order[0]. edges may be (w, l) or (w, l, margin)."""
    pairs = [(e[0], e[1]) for e in edges]
    for order in itertools.permutations(range(m)):
        pos = {o: k for k, o in enumerate(order)}
        if all(pos[w] < pos[l] for w, l in pairs):
            return order
    return None


def min_feedback_arc_fraction(edges, m: int, weighted: bool = False) -> float:
    """Minimum fraction of recorded wins whose reversal makes the record acyclic.

    This is CLAIM-451's degree of organizational nonintegrability: the minimum
    (weighted) feedback-arc fraction of the window's wins, zero exactly when an
    ordinal potential exists (TERM-077). With weighted=False each contest counts
    1; with weighted=True it counts its margin.
    """
    if not edges:
        return 0.0
    def w(e):
        return (e[2] if weighted and len(e) > 2 else 1)
    total = sum(w(e) for e in edges)
    best = min(
        sum(w(e) for e in edges if order.index(e[1]) < order.index(e[0]))
        for order in itertools.permutations(range(m))
    )
    return best / total


def recorded_outcome(prefs: np.ndarray, admitted_pairs, weighted: bool = False):
    """Outcome the record shows when only `admitted_pairs` (unordered frozensets
    of option indices) are admitted. Returns a dict: the admitted directed wins,
    whether a potential exists, the named winner (top of the order) or None, and
    the nonintegrability degree of the admitted record."""
    m = prefs.shape[1]
    admitted = [e for e in all_contests(prefs) if frozenset(e[:2]) in admitted_pairs]
    order = topo_winner(admitted, m)
    return {
        "admitted_wins": [(LABELS[w], LABELS[l]) for w, l, *_ in admitted],
        "has_potential": order is not None,
        "winner": LABELS[order[0]] if order is not None else None,
        "order": tuple(LABELS[o] for o in order) if order is not None else None,
        "nonintegrability": min_feedback_arc_fraction(admitted, m, weighted),
    }


# --- Agenda rules ----------------------------------------------------------

def chair_can_install(prefs: np.ndarray):
    """For a chair who admits all contests but one (excludes exactly one pair):
    map each excluded pair to the winner the resulting record names. Shows that a
    chair facing a cycle can install a chosen alternative by choosing what to
    leave off the agenda."""
    m = prefs.shape[1]
    pairs = [frozenset(c[:2]) for c in all_contests(prefs)]
    out = {}
    for excluded in pairs:
        admitted = set(pairs) - {excluded}
        res = recorded_outcome(prefs, admitted)
        excl = tuple(sorted(LABELS[o] for o in excluded))
        out["-".join(excl)] = res["winner"]
    return out


def sequential_agenda(prefs: np.ndarray, order):
    """Successive (amendment) procedure: options enter in `order`; the current
    survivor meets the next option in a pairwise majority vote, the loser is
    eliminated. Returns (winner_label, recorded_pairs). The option voted last
    tends to win against a Condorcet cycle, so the agenda order fixes the
    outcome. order is a tuple of option indices."""
    mg = margins(prefs)
    survivor = order[0]
    recorded = []
    for challenger in order[1:]:
        recorded.append(frozenset((survivor, challenger)))
        if mg[challenger, survivor] > mg[survivor, challenger]:
            survivor = challenger
        # ties keep the survivor
    return LABELS[survivor], recorded


def legibility_filter(prefs: np.ndarray, admit_probs, n_records: int, rng):
    """A legibility regime that admits each contest independently with a given
    probability. admit_probs maps an unordered pair (frozenset of option indices)
    to its admission probability. Over n_records draws, returns the fraction of
    records that are acyclic (coherent), the distribution of recorded winners
    (None = no potential), and the mean nonintegrability degree."""
    m = prefs.shape[1]
    contests = all_contests(prefs)
    winners = {}
    coherent = 0
    noninteg_sum = 0.0
    for _ in range(n_records):
        admitted = [
            e for e in contests
            if rng.random() < admit_probs[frozenset(e[:2])]
        ]
        order = topo_winner(admitted, m)
        win = LABELS[order[0]] if order is not None else None
        winners[win] = winners.get(win, 0) + 1
        if order is not None:
            coherent += 1
        noninteg_sum += min_feedback_arc_fraction(admitted, m)
    return {
        "fraction_coherent": coherent / n_records,
        "winner_counts": winners,
        "mean_nonintegrability": noninteg_sum / n_records,
    }


def challenge_channel_sweep(prefs: np.ndarray, suppressed_pair, n_records, rng,
                            levels=(0.0, 0.1, 0.25, 0.5, 0.75, 1.0)):
    """CLAIM-448's prediction. A regime admits two contests with certainty and
    the third (the suppressed/ marginalized one) only with probability `level`.
    Raising `level` is a protected challenge channel. Returns, per level, the
    fraction of records that stay coherent and the mean nonintegrability
    (recorded conflict). The prediction: as legibility rises, recorded conflict
    rises."""
    contests = all_contests(prefs)
    rows = []
    for level in levels:
        probs = {}
        for e in contests:
            pair = frozenset(e[:2])
            probs[pair] = level if pair == frozenset(suppressed_pair) else 1.0
        res = legibility_filter(prefs, probs, n_records, rng)
        rows.append({
            "legibility": level,
            "fraction_coherent": res["fraction_coherent"],
            "mean_nonintegrability": res["mean_nonintegrability"],
        })
    return rows


def persistence_windows(prefs: np.ndarray, suppressed_pair, n_windows, admit_level,
                        rng):
    """Sequential windows under a maintained regime. Two contests are always
    admitted; the suppressed one is admitted with probability admit_level each
    window. A *persistent* potential (TERM-078) is a single ordering that wins
    every window. Returns the number of distinct recorded winners across windows
    and whether every window was coherent -- a maintained exclusion yields one
    persistent winner that is nonetheless an artifact of admission."""
    m = prefs.shape[1]
    contests = all_contests(prefs)
    winners = []
    all_coherent = True
    for _ in range(n_windows):
        admitted = []
        for e in contests:
            pair = frozenset(e[:2])
            prob = admit_level if pair == frozenset(suppressed_pair) else 1.0
            if rng.random() < prob:
                admitted.append(e)
        order = topo_winner(admitted, m)
        if order is None:
            all_coherent = False
            winners.append(None)
        else:
            winners.append(LABELS[order[0]])
    distinct = sorted({w for w in winners if w is not None},
                      key=lambda x: x)
    return {
        "all_windows_coherent": all_coherent,
        "distinct_winners": distinct,
        "persistent": all_coherent and len(distinct) == 1,
    }


def main():
    prefs = cycle_prefs()
    contests = all_contests(prefs)
    full_order = topo_winner(contests, prefs.shape[1])
    rng = np.random.default_rng(20261122)

    results = {}

    # 0. The latent cycle: the full contest graph has no potential.
    results["full_graph"] = {
        "wins": [(LABELS[w], LABELS[l], mgn) for w, l, mgn in contests],
        "has_potential": full_order is not None,
        "nonintegrability": min_feedback_arc_fraction(contests, 3),
    }

    # 1. Chair control: excluding one contest installs a chosen winner.
    results["chair_control"] = chair_can_install(prefs)

    # 2. Agenda order: the successive procedure's winner depends on the order.
    agenda = {}
    for order in itertools.permutations(range(3)):
        winner, recorded = sequential_agenda(prefs, order)
        agenda["".join(LABELS[o] for o in order)] = {
            "winner": winner,
            "recorded_pairs": ["".join(sorted(LABELS[o] for o in p))
                               for p in recorded],
        }
    results["agenda_order"] = agenda

    # 3. Legibility filter: the suppressed contest is S-beats-W (the one that
    # closes the cycle on top of the chair's x,y,z record). Suppress each in turn.
    filt = {}
    for w, l, _ in contests:
        pair = frozenset((w, l))
        probs = {frozenset(e[:2]): (0.0 if frozenset(e[:2]) == pair else 1.0)
                 for e in contests}
        res = legibility_filter(prefs, probs, 2000, np.random.default_rng(1))
        filt["suppress_" + "".join(sorted(LABELS[o] for o in pair))] = {
            "winner_counts": res["winner_counts"],
            "fraction_coherent": res["fraction_coherent"],
        }
    results["legibility_filter"] = filt

    # 4. Protected challenge channel: raise the suppressed contest's legibility.
    suppressed = (contests[-1][0], contests[-1][1])  # S beats W, the closing arc
    results["challenge_channel"] = {
        "suppressed_pair": "".join(sorted(LABELS[o] for o in suppressed)),
        "sweep": challenge_channel_sweep(prefs, suppressed, 4000, rng),
    }

    # 5. Persistence: a maintained exclusion gives one persistent winner.
    results["persistence"] = {
        "maintained_exclusion": persistence_windows(
            prefs, suppressed, 50, 0.0, np.random.default_rng(2)),
        "intermittent_admission": persistence_windows(
            prefs, suppressed, 50, 0.5, np.random.default_rng(3)),
    }

    out = Path(__file__).with_name("results.json")
    out.write_text(json.dumps(results, indent=2, default=str))
    print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()
