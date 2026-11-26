# scratch/tools/record_history/tests/test_classify.py
from record_history.classify import diff_entries
from record_history.entries import Schema

SCHEMA = Schema.from_config({"schemes": {"CLAIM": {"dir": "record/claims.d",
    "references": {"rests_on": {"scheme": "CLAIM"},
                   "argued_by": {"scheme": "ARG", "derived": True}}}}})


def entry(status="Proposed", title="T", rests=(), argued=(), body="# CLAIM-1: T\n\nBody.", **extra):
    f = {"status": status, "title": title, "rests_on": list(rests),
         "argued_by": list(argued), "version": 1, **extra}
    return f, body


def kinds(events):
    return sorted(e["kind"] for e in events)


def diff(old, new, alias=None):
    return diff_entries(old, new, "CLAIM", SCHEMA, alias or {})


def test_creation_emits_created_and_one_relation_add_per_target():
    ev = diff(None, entry(rests=["CLAIM-1", "CLAIM-2"]))
    assert kinds(ev) == ["created", "relation_add", "relation_add"]
    assert {e["target"] for e in ev if e["kind"] == "relation_add"} == {"CLAIM-1", "CLAIM-2"}


def test_link_repair_code_concretization_and_comments_are_mechanical():
    old = entry(rests=["CLAIM-tmpx"], body="# CLAIM-tmpy: T\n\nSee [CLAIM-tmpx](a.md).")
    new = entry(rests=["CLAIM-9"], body="<!-- inactive-ok-file: CLAIM-9 -->\n# CLAIM-8: T\n\nSee CLAIM-9.")
    assert kinds(diff(old, new, {"CLAIM-tmpx": "CLAIM-9", "CLAIM-tmpy": "CLAIM-8"})) == ["mechanical"]


def test_a_changed_citation_in_the_body_is_a_relation_matter_not_a_revision():
    old = entry(body="Body (CLAIM-1) holds.")
    new = entry(body="Body (CLAIM-2) holds.")
    assert kinds(diff(old, new)) == ["mechanical"]


def test_derived_field_change_alone_is_mechanical():
    assert kinds(diff(entry(), entry(argued=["ARG-1"]))) == ["mechanical"]


def test_classes_are_separated():
    old = entry(rests=["CLAIM-1"], body="One.\nTwo.", defeated_if="x")
    new = entry(status="Active", title="U", rests=["CLAIM-2"], body="One.\nThree.\nFour.",
                defeated_if="y", version=2, history=[{"version": 2}])
    ev = diff(old, new)
    assert kinds(ev) == ["body", "defeater", "relation_add", "relation_remove", "statement", "status"]
    body = next(e for e in ev if e["kind"] == "body")
    assert (body["added"], body["removed"]) == (2, 1)
    status = next(e for e in ev if e["kind"] == "status")
    assert (status["old"], status["new"]) == ("Proposed", "Active")


def test_a_dated_note_is_not_a_body_revision():
    old = entry(body="One.\n\n## Note of 2026-11-01: X\n\nA.")
    new = entry(body="One.\n\n## Note of 2026-11-01: X\n\nA.\n\n## Note of 2026-11-26: Y\n\nB.")
    ev = diff(old, new)
    assert kinds(ev) == ["note"]
    assert ev[0]["added"] == 2


def test_summary_and_backfills_are_their_own_classes():
    assert kinds(diff(entry(summary="a b"), entry(summary="a c"))) == ["summary"]
    assert kinds(diff(entry(), entry(warrant="empirical"))) == ["meta"]  # a backfill
    assert kinds(diff(entry(warrant="empirical"), entry(warrant="demonstrated"))) == ["role"]


def test_other_front_matter_changes_are_meta():
    ev = diff(entry(tags=["x"]), entry(tags=["y"]))
    assert kinds(ev) == ["meta"] and ev[0]["fields"] == ["tags"]


def test_identical_entries_emit_nothing():
    assert diff(entry(), entry()) == []
