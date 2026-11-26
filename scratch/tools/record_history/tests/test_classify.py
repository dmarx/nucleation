# scratch/tools/record_history/tests/test_classify.py
from record_history.classify import diff_entries
from record_history.entries import Schema

SCHEMA = Schema.from_config({"schemes": {"CLAIM": {"dir": "record/claims.d",
    "references": {"rests_on": {"scheme": "CLAIM"},
                   "argued_by": {"scheme": "ARG", "derived": True}}}}})


def entry(status="Proposed", title="T", rests=(), argued=(), body="Body.", **extra):
    f = {"status": status, "title": title, "rests_on": list(rests),
         "argued_by": list(argued), "version": 1, **extra}
    return f, body


def kinds(events):
    return sorted(e["kind"] for e in events)


def test_creation_emits_created_and_one_relation_add_per_target():
    ev = diff_entries(None, entry(rests=["CLAIM-1", "CLAIM-2"]), "CLAIM", SCHEMA, {})
    assert kinds(ev) == ["created", "relation_add", "relation_add"]
    assert {e["target"] for e in ev if e["kind"] == "relation_add"} == {"CLAIM-1", "CLAIM-2"}


def test_link_repair_and_code_concretization_are_mechanical():
    old = entry(rests=["CLAIM-tmpx"], body="See [CLAIM-tmpx](a.md).")
    new = entry(rests=["CLAIM-9"], body="See CLAIM-9.")
    ev = diff_entries(old, new, "CLAIM", SCHEMA, {"CLAIM-tmpx": "CLAIM-9"})
    assert kinds(ev) == ["mechanical"]


def test_derived_field_change_alone_is_mechanical():
    ev = diff_entries(entry(), entry(argued=["ARG-1"]), "CLAIM", SCHEMA, {})
    assert kinds(ev) == ["mechanical"]


def test_status_title_prose_and_relations_are_separated():
    old = entry(rests=["CLAIM-1"], body="One.\nTwo.")
    new = entry(status="Active", title="U", rests=["CLAIM-2"], body="One.\nThree.\nFour.",
                version=2, history=[{"version": 2}])
    ev = diff_entries(old, new, "CLAIM", SCHEMA, {})
    assert kinds(ev) == ["prose", "relation_add", "relation_remove", "status", "title"]
    prose = next(e for e in ev if e["kind"] == "prose")
    assert prose["churn"] == 3  # one line removed, two added
    status = next(e for e in ev if e["kind"] == "status")
    assert (status["old"], status["new"]) == ("Proposed", "Active")


def test_prose_fields_in_front_matter_count_as_prose():
    ev = diff_entries(entry(summary="a b"), entry(summary="a c"), "CLAIM", SCHEMA, {})
    assert kinds(ev) == ["prose"]


def test_other_front_matter_changes_are_meta():
    ev = diff_entries(entry(tags=["x"]), entry(tags=["y"]), "CLAIM", SCHEMA, {})
    assert kinds(ev) == ["meta"]
    assert ev[0]["fields"] == ["tags"]


def test_identical_entries_emit_nothing():
    assert diff_entries(entry(), entry(), "CLAIM", SCHEMA, {}) == []
