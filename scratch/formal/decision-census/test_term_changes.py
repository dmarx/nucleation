# scratch/formal/decision-census/test_term_changes.py
from term_changes import diff_terms, term_decls


def test_term_decls_reads_both_layouts():
    cfg = {"vocabularies": {"topics": {"terms": {"a": {"label": "A"}}},
                            "old": {"x": {"label": "X"}}}}
    assert term_decls(cfg) == {("topics", "a"): {"label": "A"}, ("old", "x"): {"label": "X"}}


def test_diff_terms_reports_changed_keys_and_removals():
    before = {("t", "a"): {"label": "A", "blurb": "old"}, ("t", "b"): {"label": "B"}}
    after = {("t", "a"): {"label": "A", "blurb": "new"}, ("t", "c"): {"label": "C"}}
    assert diff_terms(before, after) == [(("t", "a"), "changed", ["blurb"]), (("t", "b"), "removed", [])]


def test_unchanged_and_added_terms_are_not_events():
    same = {("t", "a"): {"label": "A"}}
    assert diff_terms(same, {**same, ("t", "z"): {"label": "Z"}}) == []


def test_scope_restricts_scheme_vocabularies():
    from term_changes import scope
    assert scope("synthesis-statuses") == "record/syntheses.d/"
    assert scope("lit-statuses") == "record/literature.d/"
    assert scope("topics") == "record/"
