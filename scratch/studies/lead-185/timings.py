# scratch/studies/lead-185/timings.py: computes LEAD-185's timings from cases.csv and events.csv
"""Timing the community's verdicts against the move, per CODING.md.

Run:  python3 -I timings.py            (writes results.json and summary.md)
Test: python3 -m pytest -q test_timings.py
"""
import csv
import json
import os
from collections import Counter, defaultdict
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY_DATE = date(2026, 11, 23)
INDEPENDENT_RESPONSES = ("verdict_outside", "downstream_proposal", "downstream_replace", "revocation")


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def d(s):
    return date.fromisoformat(s)


def days(a, b):
    """Days from a to b, or None when either is missing."""
    if a is None or b is None:
        return None
    return (b - a).days


def first(events, kind, **match):
    """The earliest event of a kind whose fields match, or None."""
    rows = [e for e in events if e["event"] == kind and all(e.get(k) == v for k, v in match.items())]
    rows.sort(key=lambda e: e["date"])
    return rows[0] if rows else None


def first_independent_response(events):
    rows = [e for e in events if e["event"] in INDEPENDENT_RESPONSES and e["independent"] == "yes"]
    rows.sort(key=lambda e: (e["date"], e["act"] != "statement"))
    return rows[0] if rows else None


def case_timings(case, events):
    ev = [e for e in events if e["case"] == case["case"]]
    move = first(ev, "move")
    ann = first(ev, "announce")
    rel = first(ev, "first_release")
    resp = first_independent_response(ev)
    down = first(ev, "downstream_replace", independent="yes")
    vote = first(ev, "community_vote")
    end = first(ev, "original_end")
    prearr = first(ev, "endorse_prearranged")
    t = lambda e: d(e["date"]) if e else None
    indep = [e for e in ev if e["event"] in INDEPENDENT_RESPONSES and e["independent"] == "yes"]
    moves = [t(e) for e in indep if e["act"] == "statement+move"]
    statement_only_first = any(
        e["act"] == "statement" and (not moves or t(e) < min(moves)) for e in indep
    )
    out = {
        "case": case["case"],
        "arm": case["arm"],
        "maintainers_moved": case["maintainers_moved"] or None,
        "outcome_2026": case["outcome_2026"],
        "lag_move_to_announce": days(t(move), t(ann)),
        "lag_announce_to_release": days(t(ann), t(rel)),
        "prearranged_endorsement_on_announce_day": bool(prearr and ann and prearr["date"] == ann["date"]),
        "first_independent_response": resp["event"] if resp else None,
        "first_independent_response_act": resp["act"] if resp else None,
        "first_independent_response_reason": resp["reason"] if resp else None,
        "lag_announce_to_first_independent_response": days(t(ann), t(resp)),
        "lag_announce_to_independent_downstream": days(t(ann), t(down)),
        "independent_statement_before_any_independent_move": statement_only_first if indep else None,
        "community_vote_lag_from_announce": days(t(ann), t(vote)),
        "legitimacy_to_capability_lag": days(t(ann), t(end)),
        "legitimacy_to_capability_lower_bound": None,
    }
    if case["arm"] == "contested" and case["outcome_2026"] != "reunited" and end is None and ann is not None:
        out["legitimacy_to_capability_lower_bound"] = days(t(ann), STUDY_DATE)
    return out


def crosstab(rows, a, b):
    tab = defaultdict(Counter)
    for r in rows:
        tab[r[a] or "uncoded"][r[b] or "uncoded"] += 1
    return {k: dict(v) for k, v in sorted(tab.items())}


def run(cases_path, events_path):
    cases = load(cases_path)
    events = load(events_path)
    rows = [case_timings(c, events) for c in cases]
    contested = [r for r in rows if r["arm"] == "contested"]
    resp = [r for r in contested if r["first_independent_response"]]
    summary = {
        "n_cases": len(rows),
        "n_contested": len(contested),
        "n_events": len(events),
        "n_events_checked": sum(e["checked"] == "yes" for e in events),
        "contested_with_prearranged_endorsement_on_day_0": sum(r["prearranged_endorsement_on_announce_day"] for r in contested),
        "contested_with_independent_response": len(resp),
        "independent_response_acts": dict(Counter(r["first_independent_response_act"] for r in resp)),
        "independent_response_reasons": dict(Counter(r["first_independent_response_reason"] for r in resp)),
        "contested_with_independent_statement_before_move": sum(bool(r["independent_statement_before_any_independent_move"]) for r in resp),
        "maintainers_by_outcome_contested": crosstab(contested, "maintainers_moved", "outcome_2026"),
        "successor_took_name": [r["case"] for r in rows if r["outcome_2026"] == "reunited"],
    }
    return rows, summary


def write_summary(rows, summary, path):
    cols = ["case", "arm", "maintainers_moved", "outcome_2026", "lag_move_to_announce",
            "lag_announce_to_first_independent_response", "first_independent_response_act",
            "first_independent_response_reason", "lag_announce_to_independent_downstream",
            "legitimacy_to_capability_lag", "legitimacy_to_capability_lower_bound"]
    lines = ["<!-- scratch/studies/lead-185/summary.md: generated by timings.py -->",
             "# LEAD-185: timings", "", "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        lines.append("| " + " | ".join("" if r[c] is None else str(r[c]) for c in cols) + " |")
    lines += ["", "```json", json.dumps(summary, indent=2), "```", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    rows, summary = run(os.path.join(HERE, "cases.csv"), os.path.join(HERE, "events.csv"))
    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as f:
        json.dump({"cases": rows, "summary": summary}, f, indent=2)
    write_summary(rows, summary, os.path.join(HERE, "summary.md"))
    print(json.dumps(summary, indent=2))
