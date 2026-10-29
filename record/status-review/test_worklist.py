# record/status-review/test_worklist.py
"""Fires each worklist section against a small record built to contain one case of it (DP-4)."""
from datetime import date
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
    "arguments.d/ARG-001.md": {"status": "Active", "rests_on": ["CLAIM-001", "CLAIM-005"]},
    "arguments.d/ARG-002.md": {"status": "Active", "rests_on": ["CLAIM-001"], "concludes": ["CLAIM-003"]},
    "arguments.d/ARG-003.md": {"status": "Active", "rests_on": ["CLAIM-001"], "concludes": ["CLAIM-005"],
                               "undercut_by": ["CLAIM-001"]},
    # two concessions: CLAIM-006's target was never revised, CLAIM-007's was revised after it
    "claims.d/CLAIM-006.md": {"status": "Active", "role": "granted", "date": "2026-10-10",
                              "objects_to": ["CLAIM-003"]},
    "claims.d/CLAIM-007.md": {"status": "Active", "role": "granted", "date": "2026-10-10",
                              "objects_to": ["CLAIM-008"]},
    "claims.d/CLAIM-008.md": {"status": "Active", "role": "thesis", "version": 2,
                              "history": [{"version": 2, "date": "2026-10-12", "note": "Narrowed for CLAIM-007."}],
                              "objected_by": ["CLAIM-007", "CLAIM-011"]},
    # a Proposed objection the target was narrowed for, and one revised past for something else
    "claims.d/CLAIM-011.md": {"status": "Proposed", "role": "counter", "date": "2026-10-10",
                              "objects_to": ["CLAIM-008"]},
    "claims.d/CLAIM-012.md": {"status": "Active", "role": "granted", "date": "2026-10-10",
                              "objects_to": ["CLAIM-013"]},
    "claims.d/CLAIM-013.md": {"status": "Proposed", "role": "thesis", "version": 2,
                              "history": [{"version": 2, "date": "2026-10-19", "note": "Warrant corrected."}],
                              "objected_by": ["CLAIM-012"]},
    # an Active counter is held true whatever its role, so it is a concession too (ADR-059)
    "claims.d/CLAIM-009.md": {"status": "Active", "role": "counter", "date": "2026-10-10",
                              "objects_to": ["CLAIM-010"]},
    # filed the same day with the concession already in its text, and saying so
    "claims.d/CLAIM-010.md": {"status": "Proposed", "role": "thesis", "date": "2026-10-10",
                              "objected_by": ["CLAIM-009"]},
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
    assert [x["code"] for x in rows] == ["CLAIM-002", "CLAIM-003", "CLAIM-005"]  # CLAIM-005: ARG-001 rests on it
    # a Superseded TERM is a premise the record no longer holds
    assert rows[0]["reach"] == 2 and rows[0]["open_premises"] == ["TERM-001"] and rows[0]["live_objections"] == []
    assert rows[1]["open_premises"] == ["CLAIM-002"] and rows[1]["live_objections"] == ["CLAIM-005"]


def test_inversions_find_active_resting_on_proposed(tmp_path):
    # an ARG's status is credence in its inference, not its premises (ADR-059)
    assert record(tmp_path).inversions() == [("CLAIM-004", "rests_on", "CLAIM-003", "Proposed")]


def test_sound_arguments_with_unheld_conclusions(tmp_path):
    # ARG-002: inference Active, every premise Active, conclusion Proposed; ARG-001 has an unheld premise;
    # ARG-003 is the same but a held undercutter already says what it does not carry (ADR-059)
    assert record(tmp_path).sound_unheld() == [("ARG-002", "CLAIM-003", "Proposed")]


def test_retired_premises_name_the_successor(tmp_path):
    assert record(tmp_path).retired_premises() == [("CLAIM-002", "uses", "TERM-001", "Superseded", ["TERM-002"])]


def test_answered_questions_need_an_active_answer(tmp_path):
    assert record(tmp_path).open_with_active_answer() == [("QUESTION-001", ["CLAIM-001"])]


def test_unblocked_means_premises_active_and_no_live_objection(tmp_path):
    # CLAIM-002 uses a retired TERM, CLAIM-003 has a live objection; the counters have neither
    assert record(tmp_path).unblocked() == ["CLAIM-005", "CLAIM-011"]


def test_successors_are_followed_to_a_live_entry(tmp_path):
    assert record(tmp_path).live_successors("TERM-003") == ["TERM-002"]


def test_unwritten_concessions_find_a_target_not_revised_since(tmp_path):
    # ADR-059: a conceded objection is recorded by revising its target
    assert record(tmp_path).unwritten_concessions() == [("CLAIM-006", "CLAIM-003", "2026-10-10", "never"),
                                                        ("CLAIM-009", "CLAIM-010", "2026-10-10", "never"),
                                                        ("CLAIM-012", "CLAIM-013", "2026-10-10", "2026-10-19")]


def test_a_revision_counts_only_if_it_names_the_objection(tmp_path):
    # CLAIM-013 was revised after CLAIM-012 for something else: that does not write the concession in
    r = record(tmp_path)
    assert not r.written("CLAIM-012", "CLAIM-013") and r.written("CLAIM-007", "CLAIM-008")


def test_a_target_filed_with_its_concession_says_so(tmp_path):
    r = record(tmp_path)
    r.bodies["CLAIM-010"] = "\n## Note of 2026-10-10: filed with its concessions\n\nCLAIM-009, in its scope.\n"
    assert ("CLAIM-009", "CLAIM-010", "2026-10-10", "never") not in r.unwritten_concessions()
    # a note dated before the concession does not cover it
    r.bodies["CLAIM-010"] = "\n## Note of 2026-10-09: filed with its concessions\n\nCLAIM-009.\n"
    assert ("CLAIM-009", "CLAIM-010", "2026-10-10", "never") in r.unwritten_concessions()


def test_a_written_concession_is_no_longer_a_live_objection(tmp_path):
    # ADR-057: narrowing the target answers the objection; an unwritten one still stands
    r = record(tmp_path)
    assert r.live_objections("CLAIM-008") == ["CLAIM-011"] and r.live_objections("CLAIM-010") == ["CLAIM-009"]
    # a Proposed objection the target was narrowed for no longer stands either
    r.docs["CLAIM-008"]["history"].append({"version": 3, "date": "2026-10-20", "note": "CLAIM-011 written in."})
    assert r.live_objections("CLAIM-008") == []


def test_a_recent_blocker_note_holds_an_entry_out_of_the_work(tmp_path):
    r = record(tmp_path)
    r.bodies["CLAIM-003"] = "\n## Note of 2026-10-20: what holds it back\n\nA missing result.\n"
    work = [x["code"] for x in r.load_bearing(today=date(2026, 10, 28))]
    held = [x["code"] for x in r.load_bearing(today=date(2026, 10, 28), held=True)]
    assert "CLAIM-003" not in work and held == ["CLAIM-003"]
    # after HELD_DAYS the note is stale and the entry is work again
    assert "CLAIM-003" in [x["code"] for x in r.load_bearing(today=date(2026, 11, 10))]
