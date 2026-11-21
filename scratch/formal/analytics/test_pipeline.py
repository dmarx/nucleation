# scratch/formal/analytics/test_pipeline.py
"""The dataflow on the tiny fixture record (conftest.py), and the CLI's helpers."""
import json

import pytest

import cli
from gitread import crosstab, is_entry, vocabulary_terms


def run(tiny_record, outputs, **kw):
    return cli.compute(outputs, repo=tiny_record["repo"], census_dir=tiny_record["census_dir"],
                       growth_ref="main", **kw)


def test_snapshot_counts_at_head(tiny_record):
    v = run(tiny_record, "fast")["values"]
    assert v["repo_file_count"] == 13
    assert v["record_file_count"] == 11
    assert v["scheme_count"] == 5
    assert v["vocabulary_count"] == 2
    assert v["topic_term_count"] == 1
    assert v["entry_count"] == 9  # templates and README stubs are not entries
    assert v["entries_by_scheme"] == {"ADR": 2, "CASE": 2, "CLAIM": 2, "LEAD": 2, "LIT": 1}
    assert v["decision_status_counts"] == {"Active": 1, "Proposed": 1}
    assert v["claim_warrant_by_status"] == {"demonstrated": {"Active": 1}, "interpretive": {"Proposed": 1}}
    assert v["case_kind_by_standing"] == {"construction": {"fictional": 1}, "specimen": {"documented": 1}}
    assert v["lead_stage_counts"] == {"idea": 1, "specified": 1}
    assert v["anthology_candidate_count"] == 1


def test_an_earlier_revision_is_read_from_git_not_the_worktree(tiny_record):
    doc = run(tiny_record, "scheme_count,entry_count,topic_term_count", rev="HEAD~1")
    assert doc["values"] == {"scheme_count": 3, "entry_count": 4, "topic_term_count": 2}
    assert doc["computed_at"]["date"].startswith("2026-09-25")
    assert doc["computed_at"]["subject"] == "Scaffold"


def test_census_coverage_reports_uncoded_decisions(tiny_record):
    v = run(tiny_record, "census_coverage,census_status_drift")["values"]
    assert v["census_coverage"]["uncoded"] == ["ADR-tmpabc12"]
    assert v["census_coverage"]["uncoded_count"] == 1
    assert v["census_coverage"]["coded_not_in_record"] == ["ADR-001"]
    assert v["census_status_drift"]["changed"] == {"ADR-002": {"coded": "Proposed", "now": "Active"}}


def test_census_tables_reuse_census_py(tiny_record):
    v = run(tiny_record, "census_summary,census_agreement")["values"]
    s = v["census_summary"]
    assert (s["decisions_coded"], s["grammar_changes"]) == (2, 2)
    assert s["regime"] == {"refine": 1, "revise": 1}
    assert s["by_period"]["regime"]["16 Oct-5 Nov"] == {"n": 1, "refine": 0, "revise": 1}
    assert (s["migrations_stated"], s["entries_migrated"]) == (1, 3)
    assert s["later_harm"] == ["ADR-002"]
    assert v["census_agreement"]["n"] == 1
    assert v["census_agreement"]["fields"]["regime"] == {"agreement": 1.0, "kappa": 1.0}


def test_growth_snapshots_take_the_last_commit_by_each_date(tiny_record):
    g = run(tiny_record, "growth_snapshots", growth_dates=["2026-09-01", "2026-09-30", "2026-11-01"])
    g = g["values"]["growth_snapshots"]
    assert g["2026-09-01"] is None
    assert (g["2026-09-30"]["schemes"], g["2026-09-30"]["repo_files"], g["2026-09-30"]["topic_terms"]) == (3, 5, 2)
    assert (g["2026-11-01"]["schemes"], g["2026-11-01"]["record_files"]) == (5, 11)


def test_term_change_audit_reuses_term_changes_py(tiny_record):
    s = run(tiny_record, "term_change_summary")["values"]["term_change_summary"]
    assert s["events"] == 2
    assert s["by_kind"] == {"changed": 1, "removed": 1}
    alpha = next(e for e in s["events_list"] if e["term"] == "alpha")
    assert (alpha["keys"], alpha["carriers"], alpha["carriers_touched"], alpha["pr"]) == (["blurb"], 2, 0, 1)
    assert alpha["adr_in_unit"] is True
    assert s["untouched_with_carriers"] == ["topics:alpha"]


def test_commit_counts(tiny_record):
    assert run(tiny_record, "commit_counts")["values"]["commit_counts"] == {
        "all": 2, "non_merge": 2, "non_merge_bot": 0}


def test_run_writes_one_dated_json(tiny_record, tmp_path):
    out = tmp_path / "a.json"
    cli.CLI().run(outputs="scheme_count", out=str(out), repo=tiny_record["repo"],
                  census_dir=tiny_record["census_dir"])
    doc = json.loads(out.read_text())
    assert set(doc) == {"computed_at", "run_at", "inputs", "values"}
    assert len(doc["computed_at"]["sha"]) == 40
    assert doc["values"] == {"scheme_count": 5}


def test_select_resolves_groups_and_names():
    cat = {"a": {}, "b": {"cost": "slow"}, "c": {"role": "intermediate"}, "m": {"role": "meta"}}
    assert cli.select(cat, "all") == ["a", "b"]
    assert cli.select(cat, "fast") == ["a"]
    assert cli.select(cat, ("c", "a")) == ["c", "a"]  # fire passes a,b as a tuple
    assert cli.select(cat, "a,b,a") == ["a", "b"]
    with pytest.raises(ValueError):
        cli.select(cat, "nope")


def test_every_figure_says_what_it_feeds_or_is_internal():
    cat = cli.catalog(cli.build())
    assert {"computed_at", "census_coverage", "growth_snapshots", "term_change_summary"} <= set(cat)
    assert cli.select(cat, "all")  # nothing raises


def test_helpers():
    assert is_entry("record/claims.d/CLAIM-001.md", "record/claims.d")
    assert not is_entry("record/claims.d/_template.md", "record/claims.d")
    assert not is_entry("record/claims.d/sub/CLAIM-001.md", "record/claims.d")
    es = [{"fm": {"k": "x", "s": ["p", "q"]}}, {"fm": {"k": "x"}}]
    assert crosstab(es, "k", "s") == {"x": {"None": 1, "p": 1, "q": 1}}
    assert vocabulary_terms({"vocabularies": {"a": {"terms": {"t": {}}}, "old": {"u": {}}}}) == {
        "a": ["t"], "old": ["u"]}
    assert cli.jsonable({("a", 1): {1, 2}}) == {"('a', 1)": [1, 2]}


def test_all_includes_the_rate_studies(tiny_record):
    v = run(tiny_record, "all")["values"]
    assert {"schema_rates_report", "record_rates_report", "term_change_summary"} <= set(v)
    assert "computed_at" not in v and "entries" not in v
    assert any("declared now" in line for line in v["schema_rates_report"])
    assert v["record_rates_report"][0].startswith("history: 2 non-merge commits")
