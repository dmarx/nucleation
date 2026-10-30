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
    # one Proposed premise is all that holds two claims back, and one claim alone
    "claims.d/CLAIM-014.md": {"status": "Proposed", "role": "thesis", "line": "l1",
                              "rests_on": ["CLAIM-001", "CLAIM-015"]},
    "claims.d/CLAIM-015.md": {"status": "Proposed", "role": "thesis", "line": "l2"},
    "claims.d/CLAIM-016.md": {"status": "Proposed", "role": "thesis", "line": "l1", "grounds": ["CLAIM-015"]},
    "claims.d/CLAIM-017.md": {"status": "Proposed", "role": "thesis", "rests_on": ["CLAIM-015", "CLAIM-002"]},
    # readings: one read in full, one only skimmed, one with no note at all
    "theory.d/THEORY-002.md": {"status": "Proposed", "source": ["LIT-001"]},
    "theory.d/THEORY-003.md": {"status": "Proposed", "source": ["LIT-002"]},
    "theory.d/THEORY-004.md": {"status": "Proposed", "source": ["LIT-003"]},
    "notes.d/NOTE-001.md": {"status": "Read", "paper": "LIT-001"},
    "notes.d/NOTE-002.md": {"status": "Skimmed", "paper": "LIT-002"},
    # a Proposed reading still lists an Active claim under `supports`: the repair bot writes the
    # converse `grounds` onto the claim, and the lint's inverted_ground then fails
    "theory.d/THEORY-005.md": {"status": "Proposed", "source": ["LIT-001"], "supports": ["CLAIM-008"]},
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
    assert r.dependents("CLAIM-002") == {"CLAIM-003", "CLAIM-004", "CLAIM-017"}
    assert r.dependents("CLAIM-004") == set()


def test_load_bearing_lists_proposed_by_reach(tmp_path):
    rows = record(tmp_path).load_bearing()
    # CLAIM-015 and CLAIM-002 both reach three; CLAIM-015 more directly. CLAIM-005: ARG-001 rests on it
    assert [x["code"] for x in rows] == ["CLAIM-015", "CLAIM-002", "CLAIM-003", "CLAIM-005"]
    by = {x["code"]: x for x in rows}
    # a Superseded TERM is a premise the record no longer holds
    assert by["CLAIM-002"]["reach"] == 3 and by["CLAIM-002"]["open_premises"] == ["TERM-001"]
    assert by["CLAIM-002"]["live_objections"] == []
    # CLAIM-006 objects to CLAIM-003 with no converse on it, and its concession is unwritten
    assert by["CLAIM-003"]["open_premises"] == ["CLAIM-002"]
    assert by["CLAIM-003"]["live_objections"] == ["CLAIM-005", "CLAIM-006"]


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
    assert record(tmp_path).unblocked() == ["CLAIM-005", "CLAIM-011", "CLAIM-015"]


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


def test_ready_leaves_out_unblocked_claims_a_recent_blocker_note_holds(tmp_path):
    # the unblocked list read no blocker notes, so a pass re-read what the last one had decided
    r = record(tmp_path)
    r.bodies["CLAIM-011"] = "\n## Note of 2026-10-25: what holds it back\n\nA missing result.\n"
    today = date(2026, 10, 28)
    assert r.ready(today) == ["CLAIM-005", "CLAIM-015"]
    assert r.held_unblocked(today) == [("CLAIM-011", date(2026, 10, 25))]
    assert "CLAIM-011" in r.ready(date(2026, 11, 20))


def test_sole_blockers_rank_premises_by_the_claims_each_alone_holds_back(tmp_path):
    # CLAIM-015 is the only unheld premise of CLAIM-014 and CLAIM-016; CLAIM-017 needs CLAIM-002 too.
    # CLAIM-003 is one premise short but has a live objection, so the premise alone would not free it.
    # a retired premise holds a claim back too: CLAIM-002's Superseded TERM
    assert record(tmp_path).sole_blockers() == [("CLAIM-015", ["CLAIM-014", "CLAIM-016"]), ("TERM-001", ["CLAIM-002"])]


def test_reading_depth_is_the_best_note_on_any_source(tmp_path):
    r = record(tmp_path)
    assert [r.reading_depth(t) for t in ("THEORY-002", "THEORY-003", "THEORY-004")] == ["Read", "Skimmed", None]
    # THEORY-001 names no source at all, which the lint would also report
    assert r.unread_readings() == [("THEORY-001", None), ("THEORY-003", "Skimmed"), ("THEORY-004", None)]


def test_a_blocker_note_is_stale_when_a_premise_it_names_has_changed_since(tmp_path):
    r = record(tmp_path)
    r.bodies["CLAIM-014"] = "\n## Note of 2026-10-20: what holds it back\n\nCLAIM-001 is not shown.\n"
    assert r.stale_blockers() == []
    r.docs["CLAIM-001"]["history"] = [{"version": 2, "date": "2026-10-22", "note": "Promoted."}]
    assert r.stale_blockers() == [("CLAIM-014", "2026-10-20", ["CLAIM-001"])]


def test_a_stale_converse_is_an_inversion_in_waiting(tmp_path):
    # pass 8: the bot adds missing converses and never removes stale ones
    assert record(tmp_path).converse_inversions() == [("THEORY-005", "CLAIM-008")]


def test_an_objection_whose_target_lacks_the_converse_still_stands(tmp_path):
    # the repair bot does not write `objected_by` for every `objects_to`, so the worklist read
    # CLAIM-212 as unblocked while CLAIM-461 objected to it (pass 17)
    r = record(tmp_path)
    r = Record(r.docs | {"CLAIM-019": {"status": "Proposed", "role": "counter", "objects_to": ["CLAIM-015"]}}, r.bodies)
    assert r.live_objections("CLAIM-015") == ["CLAIM-019"]
    assert "CLAIM-015" not in r.unblocked() and "CLAIM-019" in r.unblocked()


def test_a_claim_argued_only_by_an_unsound_argument_is_not_unblocked(tmp_path):
    # CLAIM-058 has no premise of its own; its route is an ARG whose premise is Proposed (pass 17)
    r = record(tmp_path)
    claim = {"CLAIM-020": {"status": "Proposed", "role": "thesis"}}
    unsound = Record(r.docs | claim | {"ARG-004": {"status": "Active", "rests_on": ["CLAIM-015"],
                                                   "concludes": ["CLAIM-020"]}}, r.bodies)
    assert "CLAIM-020" not in unsound.unblocked()
    assert unsound.sole_blockers()[0] == ("CLAIM-015", ["CLAIM-014", "CLAIM-016", "CLAIM-020"])
    sound = Record(r.docs | claim | {"ARG-004": {"status": "Active", "rests_on": ["CLAIM-001"],
                                                 "concludes": ["CLAIM-020"]}}, r.bodies)
    assert "CLAIM-020" in sound.unblocked()


def test_a_live_claim_grounded_on_an_unread_work_is_listed(tmp_path):
    # an unread work takes no edge (ADR-058), but the worklist showed LIT grounds as "[None] ?"
    # and counted them as held, so CLAIM-426 and CLAIM-431 kept Unavailable grounds (pass 18)
    r = record(tmp_path)
    lit = {"LIT-001": {"status": "Active"}, "LIT-004": {"status": "Unavailable"}}
    claims = {"CLAIM-021": {"status": "Proposed", "grounds": ["LIT-001", "LIT-004"]},
              "CLAIM-022": {"status": "Superseded", "grounds": ["LIT-004"]}}
    r = Record(r.docs | lit | claims, r.bodies)
    # LIT-001 has a NOTE read in full; LIT-004 has none and is Unavailable
    assert r.unread_grounds() == [("CLAIM-021", ["LIT-004"])]
    # a work's status is its availability, not a credence: an Unavailable ground is listed here,
    # not as a credence inversion
    r.docs["CLAIM-021"]["status"] = "Active"
    assert not any(row[0] == "CLAIM-021" for row in r.inversions())
    assert r.unread_grounds() == [("CLAIM-021", ["LIT-004"])]


def test_a_history_note_that_only_mentions_an_objection_does_not_write_it_in(tmp_path):
    # passes 18 and 19: CLAIM-308's note said CLAIM-314's objection "is open", CLAIM-491's added
    # a converse edge for CLAIM-494, and CLAIM-212's filed CLAIM-461 "as the objection"; each was
    # read as a concession
    r = record(tmp_path)
    hist = r.docs["CLAIM-013"]["history"]
    for note in ("CLAIM-012's objection to it is open. The claim is unchanged.",
                 "objected_by converse added for CLAIM-012. The claim is unchanged.",
                 "The narrowing it proposed is filed as the objection CLAIM-012. The claim is unchanged."):
        hist[:] = [{"version": 2, "date": "2026-10-19", "note": note}]
        assert not r.written("CLAIM-012", "CLAIM-013"), note
    hist[:] = [{"version": 2, "date": "2026-10-19", "note": "Narrowed to concede CLAIM-012. Title changed."}]
    assert r.written("CLAIM-012", "CLAIM-013")


def test_a_sole_blocker_a_recent_note_already_holds_is_not_work(tmp_path):
    # after pass 19, 29 of 33 sole blockers had a premise or claims held by notes of that week
    r = record(tmp_path)
    today = date(2026, 10, 30)
    assert r.open_sole_blockers(today) == r.sole_blockers()
    r.bodies["CLAIM-015"] = "\n## Note of 2026-10-29: what holds it back\n\nA missing result.\n"
    assert [p for p, _ in r.open_sole_blockers(today)] == ["TERM-001"]
    # the claims held, not the premise: still not work while every claim is held
    r.bodies["CLAIM-015"] = ""
    for c in ("CLAIM-014", "CLAIM-016"):
        r.bodies[c] = "\n## Note of 2026-10-29: what holds it back\n\nA missing result.\n"
    assert [p for p, _ in r.open_sole_blockers(today)] == ["TERM-001"]
    assert [p for p, _ in r.open_sole_blockers(date(2026, 11, 20))] == ["CLAIM-015", "TERM-001"]


def test_a_blocker_note_is_stale_when_a_work_or_entry_it_names_has_moved_since(tmp_path):
    # a held claim's timer guarantees one look at most 14 days on; this brings it back sooner when
    # what its note waits on moves: a work it names gets read, or any entry it names is revised
    r = record(tmp_path)
    r.docs |= {"LIT-004": {"status": "Unavailable"}, "THEORY-009": {"status": "Proposed"}}
    r.bodies["CLAIM-015"] = ("\n## Note of 2026-10-20: what holds it back\n\n"
                             "It waits on LIT-004, unread, and on THEORY-009.\n")
    assert r.stale_blockers() == []
    r.docs["NOTE-003"] = {"status": "Read", "paper": "LIT-004", "date": "2026-10-25"}
    r = Record(r.docs, r.bodies)
    assert r.stale_blockers() == [("CLAIM-015", "2026-10-20", ["LIT-004"])]
    r.docs["THEORY-009"]["history"] = [{"version": 2, "date": "2026-10-26", "note": "Narrowed."}]
    assert r.stale_blockers() == [("CLAIM-015", "2026-10-20", ["LIT-004", "THEORY-009"])]
    # a reading dated before the note is what the note already knew
    r.docs["NOTE-003"]["date"] = "2026-10-19"
    r.docs["THEORY-009"]["history"] = []
    assert r.stale_blockers() == []
