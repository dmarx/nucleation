# scratch/formal/analytics/test_manuscript_figures.py
"""The pipeline reproduces the figures the manuscript quotes, at the commits it read.

scratch/manuscripts/from-obstruction-to-reorganization reads the record at
`main` 09950cdf (20 Nov) and at four dated snapshots (§12.1). These tests
run against this repository's own history and are skipped where it lacks
those commits (a shallow clone). Reading every entry takes about 20 s.
"""
from pathlib import Path

import pytest

import cli
import gitread as gr

REPO = Path(__file__).resolve().parents[3]
CENSUS_REV = "09950cdf"
GROWTH_REF = "origin/main" if gr.has_rev(REPO, "origin/main") else "main"
needs_history = pytest.mark.skipif(
    not all(gr.has_rev(REPO, r) for r in (CENSUS_REV, "f5c040c6a", "eed84a74e")),
    reason="needs the repository's full history")


@pytest.fixture(scope="module")
def at_census():
    names = ("decision_status_counts,lit_status_counts,case_kind_by_standing,"
             "claim_warrant_by_status,lead_stage_counts,entries_by_scheme,census_summary,"
             "census_agreement,census_coverage")
    return cli.compute(names, repo=str(REPO), rev=CENSUS_REV)["values"]


@needs_history
def test_growth_table_12_5():
    g = cli.compute("growth_snapshots", repo=str(REPO), growth_ref=GROWTH_REF)["values"]["growth_snapshots"]
    rows = {d: (s["commit"], s["repo_files"], s["record_files"], s["schemes"], s["vocabularies"],
                s["topic_terms"], s["luria_yaml_lines"]) for d, s in g.items()}
    assert rows == {
        "2026-09-25": ("f5c040c6a", 315, 214, 5, 6, 19, 481),
        "2026-10-15": ("b84ad2e37", 4072, 3419, 10, 14, 62, 1468),
        "2026-11-01": ("55cd0d814", 7597, 6875, 10, 14, 67, 1736),
        "2026-11-19": ("eed84a74e", 11112, 10058, 12, 18, 69, 2379),
    }


@needs_history
def test_decisions_14_1(at_census):
    assert at_census["decision_status_counts"] == {
        "Active": 70, "Proposed": 37, "Superseded": 5, "Deferred": 1, "Rejected": 1}


@needs_history
def test_lit_statuses_13_4(at_census):
    s = at_census["lit_status_counts"]
    assert (s["Active"], s["Unavailable"], s["Unfetched"], s["Deferred"]) == (2114, 531, 179, 58)


@needs_history
def test_case_kind_by_standing_13_2(at_census):
    t = at_census["case_kind_by_standing"]
    assert at_census["entries_by_scheme"]["CASE"] == 298
    assert t["specimen"] == {"documented": 61, "stipulated": 13}
    assert t["thought-experiment"] == {"documented": 1, "stipulated": 24, "fictional": 29}
    assert t["executed-study"] == {"documented": 3, "stipulated": 7, "fictional": 2}


@needs_history
def test_claim_warrant_by_status_13_3(at_census):
    t = at_census["claim_warrant_by_status"]
    assert at_census["entries_by_scheme"]["CLAIM"] == 766
    other = lambda row: sum(v for k, v in row.items() if k not in ("Active", "Proposed"))  # noqa: E731
    assert [(r["Active"], r["Proposed"], other(r)) for r in (t["demonstrated"], t["empirical"], t["interpretive"])] \
        == [(198, 39, 6), (10, 20, 1), (185, 262, 45)]


@needs_history
def test_leads_14_4(at_census):
    s = at_census["lead_stage_counts"]
    assert (sum(s.values()), s["idea"], s["specified"]) == (198, 137, 57)


@needs_history
def test_census_13_1(at_census):
    s, a = at_census["census_summary"], at_census["census_agreement"]["fields"]
    assert (s["decisions_coded"], s["grammar_changes"]) == (114, 88)
    assert s["regime"] == {"refine": 62, "revise": 25, "restraint": 1}
    assert (s["migrations_stated"], s["entries_migrated"], s["migration_median"]) == (58, 2664, 6)
    assert len(s["later_harm"]) == 10
    assert round(a["grammar_change"]["kappa"], 2) == 0.92
    assert round(a["outcome"]["kappa"], 2) == 0.38
    assert at_census["census_coverage"]["uncoded_count"] == 0  # the census was complete at 09950cdf
