"""Synthetic cases for the LEAD-041 procedure. Run: python3 -I -m pytest -q
from this directory (or pass the file path)."""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import procedure as P  # noqa: E402

OPTS = ("cut", "hike", "hold")
TIGHTEN = {"hike": 2, "hold": 1, "cut": 0}
EASE = {"cut": 2, "hold": 1, "hike": 0}
FLAT = {"cut": 0, "hold": 0, "hike": 0}
NAMED = {
    "inflation": [("hike", "hold", "cut")],
    "employment": [("cut", "hold", "hike")],
    "inertia": [("hold", "hike", "cut"), ("hold", "cut", "hike")],
}


def ep(t, w, dec, a=TIGHTEN, b=EASE, ctx="", options=OPTS):
    return P.Episode(t, w, options, {"A": a, "B": b}, dec, ctx)


def rng():
    return np.random.default_rng(0)


def test_contested_pairs_and_wins():
    e = ep(0, "w", "hold")
    assert set(P.contested_pairs(e)) == {("cut", "hike"), ("cut", "hold"), ("hike", "hold")}
    assert set(P.wins(e)) == {("hold", "cut"), ("hold", "hike")}
    # a tie against a strict ranking is not a contest
    assert P.contested_pairs(ep(0, "w", "hike", TIGHTEN, FLAT)) == []
    assert P.contested_pairs(ep(0, "w", "hike", TIGHTEN, TIGHTEN)) == []


def test_fit_and_class():
    ws = [("hold", "hike"), ("hold", "cut")]
    rev, cls = P.fit(ws, OPTS)
    assert rev == 0.0
    assert set(cls) == {("hold", "hike", "cut"), ("hold", "cut", "hike")}
    assert P.leading_perspective(P.candidate_alignment(ws, NAMED)) == "inertia"


def test_no_contest_is_not_neutral():
    # both channels indifferent: the evaluative space model's neutral point
    eps = [ep(t, "w", "hold", FLAT, FLAT) for t in range(10)]
    r = P.analyse_window("w", eps, NAMED, 0.2, rng())
    assert r.verdict == "no contest"


def test_persistent_ordering_prevails():
    decs = ["hike"] * 9 + ["hold"]
    eps = [ep(t, "w", d) for t, d in enumerate(decs)]
    r = P.analyse_window("w", eps, NAMED, 0.2, rng())
    assert r.verdict == "prevails"
    assert r.leading == "inflation"
    assert r.perspective_agreement["A"] > 0.9


def test_alternation_is_ambivalent():
    decs = ["hike", "cut"] * 6
    eps = [ep(t, "w", d) for t, d in enumerate(decs)]
    r = P.analyse_window("w", eps, NAMED, 0.1, rng())
    # the pair hike-cut reverses half the time; the compromise loses to both
    assert r.reversal == 0.25
    assert all(o[-1] == "hold" for o in r.best_class)
    assert r.verdict == "ambivalent"


def test_holds_under_contest_are_inertia_not_ambivalence():
    # the middling expression: the same output as neutrality, but here an
    # ordering (hold on top) prevails among contested pairs
    eps = [ep(t, "w", "hold") for t in range(8)]
    r = P.analyse_window("w", eps, NAMED, 0.1, rng())
    assert r.verdict == "prevails"
    assert r.leading == "inertia"


def test_neutral_and_signed():
    eps = [ep(t, "w", "hike") for t in range(6)]
    prog = lambda name, e: 1.0  # noqa: E731
    r = P.analyse_window("w", eps, NAMED, 0.1, rng(), progress=prog, reference=1.0, tol=0.1)
    assert r.sign == "neutral"
    r = P.analyse_window("w", eps, NAMED, 0.1, rng(), progress=prog, reference=0.0, tol=0.1)
    assert r.sign == "positive"


def test_split_by_context():
    eps = [ep(t, "w", "hike", ctx="a") for t in range(5)] + \
          [ep(t, "w", "cut", ctx="b") for t in range(5, 10)]
    r = P.analyse_window("w", eps, NAMED, 0.3, rng())
    # a context split with a reversal fraction of 0.5 is still flagged by the
    # null when departures are rare; with frequent departures it is a split
    assert r.verdict in ("split by context", "ambivalent")
    assert P._disjoint_classes(r.by_context)


def test_departure_rate():
    eps = [ep(0, "w", "hike", TIGHTEN, TIGHTEN), ep(1, "w", "hold", TIGHTEN, TIGHTEN),
           ep(2, "w", "hold", FLAT, FLAT), ep(3, "w", "cut")]
    assert P.departure_rate(eps) == 0.5


def test_resumption():
    seq = [("1", "x"), ("2", "x"), ("3", "y"), ("4", None), ("5", "x")]
    out = P.persistence_and_resumption(seq, "x")
    assert out["longest_run"] == 2
    assert out["resumptions"] == [{"after": "2", "interruption": ["3"], "resumed": "5"}]


def test_alternation_test_detects_stop_go_and_regimes():
    r = np.random.default_rng(1)
    # regimes: four windows of hikes, then four of cuts: fewer switches than chance
    eps, wins = [], []
    for wi in range(8):
        d = "hike" if wi < 4 else "cut"
        for k in range(5):
            eps.append(ep(wi * 5 + k, str(wi), d))
        wins.append(str(wi))
    out = P.alternation_test(eps, wins, NAMED, r, n_perm=200)
    assert out["observed"] == 1
    assert out["p_fewer"] < 0.05
    # stop-go: windows alternate: more switches than chance
    eps = []
    for wi in range(8):
        d = "hike" if wi % 2 == 0 else "cut"
        for k in range(5):
            eps.append(ep(wi * 5 + k, str(wi), d))
    out = P.alternation_test(eps, wins, NAMED, r, n_perm=200)
    assert out["observed"] == 7
    assert out["p_more"] < 0.05
