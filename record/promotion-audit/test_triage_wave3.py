# record/promotion-audit/test_triage_wave3.py
"""Tests for triage_wave3.py: eligibility, the bundling overlap, reading depth, the control."""
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import triage_wave3 as t3  # noqa: E402


def entry(path: Path, fm: dict, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False) + "---\n" + body)


def theory(root: Path, n: int, *, tags=("epistemology",), status="Proposed", title="A claim",
           promote_when="A replication.", source=("LIT-001",), disclaim="Nothing.") -> None:
    entry(
        root / "theory.d" / f"THEORY-{n:03d}.md",
        {"number": n, "status": status, "title": title, "tags": list(tags),
         "promote_when": promote_when, "source": list(source)},
        f"\n# THEORY-{n:03d}: {title}\n\n## What was actually shown\n\nStuff.\n\n"
        f"## What this does not say\n\n{disclaim}\n\n## Connections\n\nNone.\n",
    )


def note(root: Path, n: int, paper: str, status: str, v1: str) -> None:
    entry(
        root / "notes.d" / f"NOTE-{n:03d}.md",
        {"number": n, "status": status, "paper": paper,
         "history": [{"version": 1, "date": "2026-10-01", "note": v1}]},
    )


def test_eligible_excludes_mathematics_active_and_queued(tmp_path: Path) -> None:
    theory(tmp_path, 1)
    theory(tmp_path, 2, tags=("mathematics",))
    theory(tmp_path, 3, status="Active")
    theory(tmp_path, 4)
    codes = [code for code, _, _ in t3.eligible(tmp_path, skip={"THEORY-004"})]
    assert codes == ["THEORY-001"]


def test_disclaimer_section_is_extracted() -> None:
    body = "## What was actually shown\n\nA.\n\n## What this does not say\n\nNot trained networks.\n\n## Connections\n\nB.\n"
    assert t3.section(body, "What this does not say").strip() == "Not trained networks."


def test_bundling_counts_promote_when_terms_the_body_disclaims() -> None:
    fm = {"title": "Kernels align across vision models",
          "promote_when": "Shown for trained language models at scale, across modalities."}
    disclaim = "It does not say that trained language models align, nor anything across modalities at scale."
    assert t3.bundling(fm, disclaim) == 2
    assert t3.bundling(fm, "It says nothing about birds.") == 0


def test_bundling_ignores_terms_shared_with_the_title() -> None:
    fm = {"title": "Trained language models align", "promote_when": "Trained language models align again."}
    assert t3.bundling(fm, "Not that trained language models align.") == 0


def test_depth_levels() -> None:
    assert t3.note_depth("Read", "Read in full from the arXiv PDF; every proof followed.") == 2
    assert t3.note_depth("Read", "Read from the journal copy; Sections 1-3.") == 1
    assert t3.note_depth("Read", "Read in outline only; the appendix was not seen.") == 0
    assert t3.note_depth("Skimmed", "Read in full.") == 0


def test_theory_depth_is_the_weakest_source(tmp_path: Path) -> None:
    note(tmp_path, 1, "LIT-001", "Read", "Read in full.")
    note(tmp_path, 2, "LIT-002", "Read", "Read from the PDF, sections 1-2.")
    depths = t3.lit_depths(tmp_path)
    assert t3.theory_depth(["LIT-001"], depths) == 2
    assert t3.theory_depth(["LIT-001", "LIT-002"], depths) == 1
    assert t3.theory_depth(["LIT-001", "LIT-999"], depths) == 0
    assert t3.theory_depth([], depths) == 0


def test_lit_depth_takes_the_best_note(tmp_path: Path) -> None:
    note(tmp_path, 1, "LIT-001", "Skimmed", "Skimmed.")
    note(tmp_path, 2, "LIT-001", "Read", "Read in full.")
    assert t3.lit_depths(tmp_path)["LIT-001"] == 2


def test_control_is_every_kth_outside_the_top() -> None:
    codes = [f"THEORY-{i:03d}" for i in range(30)]
    ctrl = t3.control(codes, exclude=set(codes[:5]), size=5)
    assert len(ctrl) == 5
    assert not set(ctrl) & set(codes[:5])
    assert ctrl == sorted(ctrl)
    assert ctrl == t3.control(codes, exclude=set(codes[:5]), size=5)


def test_firsthand_flags_second_hand_evidence() -> None:
    assert t3.firsthand("Theorem 2 is proved in Section 4.") == 1
    assert t3.firsthand("Theorem 2 is cited to an unpublished manuscript.") == 0
    assert t3.firsthand("The lemma is asserted, not proved.") == 0


def test_compound_is_the_narrow_pattern() -> None:
    assert t3.COMPOUND.search("A holds, so B follows")
    assert t3.COMPOUND.search("A holds; B does not")
    assert not t3.COMPOUND.search("A and B hold: both")
