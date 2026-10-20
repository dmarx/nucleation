# record/promotion-audit/test_triage_narrowing.py
import subprocess

from triage_narrowing import carriers, cited, frontmatter, last_proposed, links, summarize


def test_frontmatter_parses_and_tolerates_missing():
    assert frontmatter("---\nstatus: Active\ntitle: x\n---\nbody") == {"status": "Active", "title": "x"}
    assert frontmatter("no frontmatter") == {}


def test_links_reads_only_carrier_relations():
    fm = {"extends": ["THEORY-001"], "supports": ["THEORY-002"], "refined_by": ["CLAIM-003"]}
    assert links(fm) == {"THEORY-001", "CLAIM-003"}


def test_carriers_both_directions_and_only_proposed():
    docs = {
        "THEORY-010": {"status": "Active", "extended_by": ["THEORY-012"]},
        "THEORY-011": {"status": "Proposed", "extends": ["THEORY-010"]},
        "THEORY-012": {"status": "Proposed"},
        "CLAIM-013": {"status": "Active", "refines": ["THEORY-010"]},
        "QUESTION-014": {"status": "Proposed", "extends": ["THEORY-010"]},
    }
    assert carriers("THEORY-010", docs) == ["THEORY-011", "THEORY-012"]


def test_last_proposed_finds_newest_proposed_revision(tmp_path):
    g = lambda *a: subprocess.run(["git", "-C", str(tmp_path), *a], check=True, capture_output=True)
    g("init", "-q"); g("config", "user.email", "t@t"); g("config", "user.name", "t")
    p = tmp_path / "T.md"
    for status, title in [("Proposed", "wide"), ("Proposed", "wider"), ("Active", "narrow")]:
        p.write_text(f"---\nstatus: {status}\ntitle: {title}\n---\n")
        g("add", "T.md"); g("commit", "-qm", title)
    assert last_proposed(p, root=tmp_path)["title"] == "wider"


def test_summarize_orders_kind1_first_then_citations_and_skips_carried():
    entries = {
        "THEORY-001": [{"kind": 2, "existing_carrier": None}],
        "THEORY-002": [{"kind": 1, "existing_carrier": None}, {"kind": 3}],
        "THEORY-003": [{"kind": 1, "existing_carrier": "THEORY-099"}],
        "THEORY-004": [{"kind": 1, "existing_carrier": None}],
        "THEORY-005": [{"kind": 4}],
    }
    s = summarize(entries, {"THEORY-002": 1, "THEORY-004": 7}, size=2)
    assert s["clauses_by_kind"] == {1: 3, 2: 1, 3: 1, 4: 1}
    assert s["codes_to_file"] == 3 and s["kind1_codes"] == 2 and s["kind2_only_codes"] == 1
    assert [b["codes"] for b in s["batches"]] == [["THEORY-004", "THEORY-002"], ["THEORY-001"]]


def test_cited_counts_files_naming_the_code_but_not_its_own(tmp_path):
    (tmp_path / "THEORY-001.md").write_text("THEORY-001 itself")
    (tmp_path / "NOTE-1.md").write_text("see THEORY-001.")
    (tmp_path / "NOTE-2.md").write_text("THEORY-0011 is another code")
    assert cited("THEORY-001", root=tmp_path) == 1
