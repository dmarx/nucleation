# record/status-review/test_worklist.py
"""Fires each worklist section against a small record built to contain one case of it (DP-4)."""
from pathlib import Path

from worklist import Record

ENTRIES = {
    "claims.d/CLAIM-001.md": {"status": "Active", "role": "granted", "warrant": "demonstrated"},
    "claims.d/CLAIM-002.md": {"status": "Proposed", "role": "thesis", "warrant": "interpretive",
                              "rests_on": ["CLAIM-001"], "uses": ["TERM-001"]},
    "claims.d/CLAIM-003.md": {"status": "Proposed", "role": "thesis", "warrant": "interpretive",
                              "rests_on": ["CLAIM-002"], "objected_by": ["CLAIM-005"]},
    "claims.d/CLAIM-004.md": {"status": "Active", "role": "thesis", "warrant": "demonstrated",
                              "rests_on": ["CLAIM-003"]},
    "claims.d/CLAIM-005.md": {"status": "Proposed", "role": "counter", "warrant": "interpretive",
                              "objects_to": ["CLAIM-003"]},
    "terms.d/TERM-001.md": {"status": "Superseded", "superseded_by": "TERM-002"},
    "terms.d/TERM-002.md": {"status": "Active"},
    "terms.d/TERM-003.md": {"status": "Superseded", "superseded_by": "TERM-001"},
    "questions.d/QUESTION-001.md": {"status": "Open", "answered_by": ["CLAIM-001"]},
    "questions.d/QUESTION-002.md": {"status": "Open", "answered_by": ["CLAIM-002"]},
    "theory.d/THEORY-001.md": {"status": "Proposed", "presupposed_by": []},
}


def record(tmp_path: Path) -> Record:
    for rel, fm in ENTRIES.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        lines = "".join(f"{k}: {v!r}\n" if isinstance(v, str) else f"{k}: {v}\n" for k, v in fm.items())
        p.write_text(f"---\ntitle: 't {p.stem}'\n{lines}---\n\n# {p.stem}: t\n")
    return Record.load(tmp_path)


def test_dependents_are_transitive(tmp_path):
    r = record(tmp_path)
    assert r.dependents("CLAIM-002") == {"CLAIM-003", "CLAIM-004"}
    assert r.dependents("CLAIM-004") == set()


def test_load_bearing_lists_proposed_by_reach(tmp_path):
    rows = record(tmp_path).load_bearing()
    assert [x["code"] for x in rows] == ["CLAIM-002", "CLAIM-003"]
    # a Superseded TERM is a premise the record no longer holds
    assert rows[0]["reach"] == 2 and rows[0]["open_premises"] == ["TERM-001"] and rows[0]["live_objections"] == []
    assert rows[1]["open_premises"] == ["CLAIM-002"] and rows[1]["live_objections"] == ["CLAIM-005"]


def test_inversions_find_active_resting_on_proposed(tmp_path):
    assert record(tmp_path).inversions() == [("CLAIM-004", "rests_on", "CLAIM-003", "Proposed")]


def test_retired_premises_name_the_successor(tmp_path):
    assert record(tmp_path).retired_premises() == [("CLAIM-002", "uses", "TERM-001", "Superseded", ["TERM-002"])]


def test_answered_questions_need_an_active_answer(tmp_path):
    assert record(tmp_path).open_with_active_answer() == [("QUESTION-001", ["CLAIM-001"])]


def test_unblocked_means_premises_active_and_no_live_objection(tmp_path):
    # CLAIM-002 uses a retired TERM, CLAIM-003 has a live objection; the counter has neither
    assert record(tmp_path).unblocked() == ["CLAIM-005"]


def test_successors_are_followed_to_a_live_entry(tmp_path):
    assert record(tmp_path).live_successors("TERM-003") == ["TERM-002"]
