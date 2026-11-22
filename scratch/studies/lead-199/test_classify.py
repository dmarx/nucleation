import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import classify, edges

BASE = """---
number: 1
status: Proposed
title: 'A claim'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Something.
rests_on:
- CLAIM-002
---
<!-- inactive-ok-file: CLAIM-002 -->

# CLAIM-001: A claim

## The claim

It rests on CLAIM-002 and says a thing.

## What it does not say

- Not another thing.
"""


def k(new, old=BASE, **kw):
    return classify(old, new, **kw)


def test_created():
    assert classify(None, BASE)["kind"] == "created"


def test_dated_note_and_history_only():
    new = BASE.replace("version: 1", "version: 2\nhistory:\n- version: 2\n  note: x") \
        + "\n## Note of 2026-11-21: more\n\nA dated note.\n"
    assert k(new)["kind"] == "nonsubstantive"


def test_relation_only():
    new = BASE.replace("- CLAIM-002\n", "- CLAIM-002\n- CLAIM-003\ngrounds:\n- THEORY-9\n")
    r = k(new)
    assert r["kind"] == "nonsubstantive"


def test_link_repair_and_rewrap_not_substantive():
    new = BASE.replace("It rests on CLAIM-002 and says a thing.",
                       "It rests on [CLAIM-002](CLAIM-002.md) and\nsays a thing.")
    assert k(new)["kind"] == "nonsubstantive"


def test_temp_code_concretization_not_substantive():
    old = BASE.replace("CLAIM-002", "CLAIM-tmpab12c")
    alias = lambda c: {"CLAIM-tmpab12c": "CLAIM-002"}.get(c, c)
    assert classify(old, BASE, author="Claude", alias=alias)["kind"] == "nonsubstantive"


def test_title_change():
    r = k(BASE.replace("title: 'A claim'", "title: 'A narrower claim'"))
    assert r["kind"] == "substantive" and r["title_change"] and r["lenient"]


def test_body_change():
    r = k(BASE.replace("says a thing.", "says a smaller thing."))
    assert r["kind"] == "substantive" and r["lenient"] and not r["title_change"]


def test_new_section_strict_vs_lenient():
    r = k(BASE + "\n## Admission\n\nAudited.\n")
    assert r["kind"] == "substantive" and not r["lenient"]


def test_defeater_change():
    assert k(BASE.replace("Something.", "Something else."))["kind"] == "substantive"


def test_status_change_counted_separately():
    r = k(BASE.replace("status: Proposed", "status: Active"))
    assert r["kind"] == "nonsubstantive" and r["status_change"]


def test_bot_is_mechanical():
    r = k(BASE.replace("says a thing.", "says x."), author="github-actions[bot]")
    assert r["kind"] == "mechanical"
    r = k(BASE.replace("says a thing.", "says x."), author="Claude", message="docs: repair sources")
    assert r["kind"] == "mechanical"


def test_edges():
    assert edges(BASE) == {"CLAIM-002"}
    assert edges("---\nrests_on: [CLAIM-5, CLAIM-tmpx1]\ngrounds:\n- THEORY-3\nuses:\n- TERM-1\n---\n") \
        == {"CLAIM-5", "CLAIM-tmpx1", "THEORY-3"}


def test_warrant_backfill_not_substantive():
    old = BASE.replace("warrant: interpretive\n", "")
    assert classify(old, BASE)["kind"] == "nonsubstantive"
    assert k(BASE.replace("warrant: interpretive", "warrant: empirical"))["kind"] == "substantive"


def test_citation_repoint_and_added_paren_cite_not_substantive():
    assert k(BASE.replace("rests on CLAIM-002", "rests on CLAIM-009"))["kind"] == "nonsubstantive"
    assert k(BASE.replace("says a thing.", "says a thing ([TERM-008](../terms.d/TERM-008.md)<!-- ref::uses: TERM-008 -->)."))["kind"] == "nonsubstantive"
