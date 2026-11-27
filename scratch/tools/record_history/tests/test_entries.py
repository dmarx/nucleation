# scratch/tools/record_history/tests/test_entries.py
from record_history.entries import (
    code_of_path, normalize_body, parse_entry, Schema, canonical,
)

TEXT = """---
number: 12
status: Proposed
title: 'A claim'
rests_on:
- CLAIM-3
- CLAIM-tmpab12c
argued_by:
- ARG-4
tags:
- x
---

# CLAIM-12: A claim

It rests on [CLAIM-3](../claims.d/CLAIM-3.md) and CLAIM-tmpab12c.
"""


def test_parse_entry_splits_front_matter_and_body():
    fields, body = parse_entry(TEXT)
    assert fields["status"] == "Proposed"
    assert fields["rests_on"] == ["CLAIM-3", "CLAIM-tmpab12c"]
    assert body.lstrip().startswith("# CLAIM-12")


def test_parse_entry_without_front_matter_returns_whole_text_as_body():
    fields, body = parse_entry("just text\n")
    assert fields == {} and body == "just text\n"


def test_parse_entry_with_broken_yaml_does_not_raise():
    fields, body = parse_entry("---\nkey: [unclosed\n---\nbody\n")
    assert fields == {} and "body" in body


def test_code_of_path():
    assert code_of_path("record/claims.d/CLAIM-12.md") == "CLAIM-12"
    assert code_of_path("record/claims.d/CLAIM-tmpab12c.md") == "CLAIM-tmpab12c"
    assert code_of_path("record/claims.d/README.stub") is None
    assert code_of_path("record/curation.d/2026/11/22/231046.md") is None


def test_normalize_body_strips_link_targets_and_applies_aliases():
    alias = {"CLAIM-tmpab12c": "CLAIM-77"}
    a = normalize_body("It rests on [CLAIM-3](../claims.d/CLAIM-3.md) and CLAIM-tmpab12c.", alias)
    b = normalize_body("It rests on CLAIM-3   and CLAIM-77.\n\n", alias)
    assert a == b == ["It rests on CLAIM-3 and CLAIM-77."]


def test_normalize_body_ignores_inactive_ok_directives():
    body = "<!-- inactive-ok-file: CLAIM-1 CLAIM-2 -- why -->\nText.\n"
    assert normalize_body(body, {}) == ["Text."]


def test_canonical_follows_chains_and_stops_on_cycles():
    alias = {"A-tmp1": "A-tmp2", "A-tmp2": "A-5", "B-1": "B-2", "B-2": "B-1"}
    assert canonical("A-tmp1", alias) == "A-5"
    assert canonical("A-9", alias) == "A-9"
    assert canonical("B-1", alias) in {"B-1", "B-2"}


def test_schema_reads_forward_and_derived_fields():
    config = {"schemes": {"CLAIM": {"dir": "record/claims.d", "active": ["Active"],
        "references": {
            "rests_on": {"scheme": "CLAIM"},
            "argued_by": {"scheme": "ARG", "derived": True},
        }}}}
    s = Schema.from_config(config)
    assert s.forward_fields("CLAIM") == {"rests_on"}
    assert s.derived_fields("CLAIM") == {"argued_by"}
    assert s.scheme_of("CLAIM-12") == "CLAIM"
    assert s.scheme_of("NOPE-1") is None
