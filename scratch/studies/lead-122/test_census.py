#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the LEAD-122 census parser. Run: python3 -I -m pytest -q."""
import census as c


def test_disposition_binning():
    assert c.disposition_of("Filed") == "filed"
    assert c.disposition_of("Missed") == "not_filed"
    assert c.disposition_of("Not filed") == "not_filed"
    assert c.disposition_of("Held, not filed") == "not_filed"
    assert c.disposition_of("Struck") == "not_filed"
    assert c.disposition_of("Corrected") == "corrected"
    # not a filing decision -> other, excluded from shares
    assert c.disposition_of("Right") == "other"
    assert c.disposition_of("Already held") == "other"
    assert c.disposition_of("Checked") == "other"


def test_contributor_turn_markers():
    assert c.classify_contributor("U10: the owner's mapping. Filed as CLAIM-1.") == "owner"
    assert c.classify_contributor("A10: the mapping worked out.") == "assistant"
    # both present -> both
    assert c.classify_contributor("A9's correction of the owner's U8") == "both"
    assert c.classify_contributor("derived by the reader, checked by simulation") == "reader"
    assert c.classify_contributor("the double well is bistable") == "unattributed"


def test_contributor_prefers_both_when_coattributed():
    ctx = "the owner's thesis, with A18's three sources"
    assert c.classify_contributor(ctx) == "both"


def test_kind_from_codes():
    assert c.classify_kind("CLAIM-538 (Active, demonstrated)") == "claim"
    assert c.classify_kind("QUESTION-370 takes U10 and U11") == "question"
    assert c.classify_kind("TERM-050, intrapersonal synchronization") == "term"
    assert c.classify_kind("CASE-124 and CLAIM-400") == "case"
    # 'note on' wins over the code type it names
    assert c.classify_kind("a note on CLAIM-122, since the paper was unread") == "note"
    assert c.classify_kind("notes on QUESTION-133 and CLAIM-354") == "note"
    assert c.classify_kind("Ten works registered") == "work"
    assert c.classify_kind("adoption is the owner's decision") == "unclassified"


def test_extract_moves_spans_and_block_context():
    text = (
        "- **U10: the owner's mapping.** On Friston. "
        "**Filed:** CLAIM-338, the owner's thesis.\n\n"
        "- **A11: a derivation.** **Missed:** CLAIM-345 and THEORY-121.\n"
    )
    moves = c.extract_moves(text)
    assert len(moves) == 2
    f = moves[0]
    assert f["disposition"] == "filed"
    assert "CLAIM-338" in f["span"]
    # block context reaches back to the U10 bullet head -> owner
    assert c.classify_contributor(f["context"]) == "owner"
    assert c.classify_kind(f["span"]) == "claim"
    m = moves[1]
    assert m["disposition"] == "not_filed"
    assert c.classify_contributor(m["context"]) == "assistant"


def test_extract_moves_two_labels_one_block():
    text = "**Filed:** CLAIM-1. **Missed:** CLAIM-2 by A5.\n\n"
    moves = c.extract_moves(text)
    assert [m["disposition"] for m in moves] == ["filed", "not_filed"]
    # first span must stop at the next label, not swallow CLAIM-2
    assert "CLAIM-2" not in moves[0]["span"]
    assert "CLAIM-1" in moves[0]["span"]
