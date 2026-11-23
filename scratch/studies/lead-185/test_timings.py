# scratch/studies/lead-185/test_timings.py: tests for timings.py and checks on the coded data
import csv
import os
from datetime import date

import pytest

import timings as T

HERE = os.path.dirname(os.path.abspath(__file__))
EVENT_KINDS = {
    "move", "announce", "first_release", "endorse_prearranged", "verdict_outside",
    "downstream_proposal", "downstream_replace", "downstream_effective", "community_vote",
    "host_accept", "original_restewarded", "original_end", "name_transfer", "reversal",
    "steward_escalation", "fork_call", "revocation",
}


def ev(case, event, dt, act="", independent="", reason=""):
    return {"case": case, "event": event, "date": dt, "act": act, "independent": independent, "reason": reason}


CASE = {"case": "x", "arm": "contested", "maintainers_moved": "yes", "outcome_2026": "successor"}


def test_days():
    assert T.days(date(2020, 1, 1), date(2020, 1, 31)) == 30
    assert T.days(None, date(2020, 1, 1)) is None


def test_first_picks_earliest_matching():
    rows = [ev("x", "downstream_replace", "2020-05-01", independent="no"),
            ev("x", "downstream_replace", "2020-06-01", independent="yes"),
            ev("x", "downstream_replace", "2020-04-01", independent="yes")]
    assert T.first(rows, "downstream_replace", independent="yes")["date"] == "2020-04-01"


def test_independent_response_ignores_founder_tied():
    rows = [ev("x", "announce", "2020-01-01"),
            ev("x", "downstream_replace", "2020-01-02", "statement+move", "no"),
            ev("x", "verdict_outside", "2020-01-10", "statement+move", "yes", "identity")]
    r = T.case_timings(CASE, rows)
    assert r["first_independent_response"] == "verdict_outside"
    assert r["lag_announce_to_first_independent_response"] == 9


def test_statement_before_move_detected():
    rows = [ev("x", "announce", "2020-01-01"),
            ev("x", "downstream_proposal", "2020-01-05", "statement", "yes", "licence"),
            ev("x", "downstream_replace", "2020-03-01", "statement+move", "yes", "licence")]
    r = T.case_timings(CASE, rows)
    assert r["independent_statement_before_any_independent_move"] is True
    assert r["first_independent_response_act"] == "statement"
    assert r["lag_announce_to_independent_downstream"] == 60


def test_statement_after_move_not_counted():
    rows = [ev("x", "announce", "2020-01-01"),
            ev("x", "verdict_outside", "2020-01-02", "statement+move", "yes"),
            ev("x", "downstream_proposal", "2020-01-05", "statement", "yes")]
    assert T.case_timings(CASE, rows)["independent_statement_before_any_independent_move"] is False


def test_prearranged_on_day_zero():
    rows = [ev("x", "announce", "2020-01-01"), ev("x", "endorse_prearranged", "2020-01-01", "statement", "no")]
    assert T.case_timings(CASE, rows)["prearranged_endorsement_on_announce_day"] is True


def test_capability_lag_and_lower_bound():
    rows = [ev("x", "announce", "2020-01-01"), ev("x", "original_end", "2021-01-01")]
    r = T.case_timings(CASE, rows)
    assert r["legitimacy_to_capability_lag"] == 366 and r["legitimacy_to_capability_lower_bound"] is None
    r2 = T.case_timings(CASE, [ev("x", "announce", "2026-11-13")])
    assert r2["legitimacy_to_capability_lag"] is None and r2["legitimacy_to_capability_lower_bound"] == 10


def test_reunited_case_gets_no_lower_bound():
    c = dict(CASE, outcome_2026="reunited")
    assert T.case_timings(c, [ev("x", "announce", "2020-01-01")])["legitimacy_to_capability_lower_bound"] is None


def test_accepted_case_gets_no_lower_bound():
    c = dict(CASE, arm="accepted")
    assert T.case_timings(c, [ev("x", "announce", "2020-01-01")])["legitimacy_to_capability_lower_bound"] is None


# Checks on the coded data itself (the rules of CODING.md).

def rows(name):
    with open(os.path.join(HERE, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_data_every_event_has_url_kind_and_date():
    cases = {c["case"] for c in rows("cases.csv")}
    for e in rows("events.csv"):
        assert e["case"] in cases
        assert e["event"] in EVENT_KINDS, e
        assert e["url"].startswith("http"), e
        date.fromisoformat(e["date"])
        assert e["checked"] in ("yes", "no")
        assert e["precision"] in ("day", "week", "month", "on-or-before")
        if e["reason"]:
            parts = e["reason"].split("+")
            assert parts == sorted(parts) and set(parts) <= {"identity", "licence", "practical", "unstated"}, e


def test_data_responses_code_act_and_independence():
    for e in rows("events.csv"):
        if e["event"] in T.INDEPENDENT_RESPONSES:
            assert e["act"] in ("statement", "statement+move"), e
            assert e["independent"] in ("yes", "no"), e


def test_data_case_vocabularies():
    for c in rows("cases.csv"):
        assert c["arm"] in ("contested", "accepted", "unclassified")
        assert c["maintainers_moved"] in ("yes", "partial", "no", "")
        assert c["outcome_2026"] in ("successor", "original", "split", "reunited", "revoked", "undetermined")


def test_data_contested_cases_have_announce():
    events = rows("events.csv")
    for c in rows("cases.csv"):
        if c["arm"] == "contested":
            assert T.first([e for e in events if e["case"] == c["case"]], "announce"), c["case"]


def test_run_on_data():
    rs, summary = T.run(os.path.join(HERE, "cases.csv"), os.path.join(HERE, "events.csv"))
    assert summary["n_cases"] == len(rs) == 11
    assert summary["n_contested"] == 8
