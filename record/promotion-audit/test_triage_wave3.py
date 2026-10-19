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


def test_eligible_excludes_active_and_queued_but_not_mathematics(tmp_path: Path) -> None:
    # triage-005: the tag is no class boundary (batches 011, 016, 017); `formal` routes instead
    theory(tmp_path, 1)
    theory(tmp_path, 2, tags=("mathematics",))
    theory(tmp_path, 3, status="Active")
    theory(tmp_path, 4)
    codes = [code for code, _, _ in t3.eligible(tmp_path, skip={"THEORY-004"})]
    assert codes == ["THEORY-001", "THEORY-002"]


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


def test_theory_depth_is_the_best_source(tmp_path: Path) -> None:
    # triage-005: the best source, since the weakest hid a full reading of the core's source (batch 017)
    note(tmp_path, 1, "LIT-001", "Read", "Read in full.")
    note(tmp_path, 2, "LIT-002", "Read", "Read from the PDF, sections 1-2.")
    note(tmp_path, 3, "LIT-003", "Skimmed", "Skimmed.")
    depths = t3.lit_depths(tmp_path)
    assert t3.theory_depth(["LIT-001"], depths) == 2
    assert t3.theory_depth(["LIT-001", "LIT-002"], depths) == 2
    assert t3.theory_depth(["LIT-002", "LIT-003"], depths) == 1
    assert t3.theory_depth(["LIT-003", "LIT-999"], depths) == 0
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


def test_firsthand_flags_negative_phrases() -> None:
    assert t3.firsthand("Nothing is measured; the argument runs from examples.") == 0
    assert t3.firsthand("No theorems are stated.") == 0
    assert t3.firsthand("The constant was not computed.") == 0
    assert t3.firsthand("The step is stated by no source; it is the filer's synthesis.") == 0
    assert t3.firsthand("Nothing was tested.") == 0
    assert t3.firsthand("Lemma 1 was followed as statements, not re-derived.") == 0
    assert t3.firsthand("Lemma 1 is proved in Appendix B.") == 1


def test_formal_needs_a_formal_title_and_a_shown_result() -> None:
    shown_proof = "Theorem 1 is proved in Section 3; the bound is derived."
    assert t3.formal("An optimal nearest-neighbour bound holds in the unit cube", shown_proof) == 1
    assert t3.formal("The top C eigenvalues are carried by the class means", shown_proof) == 1
    # a formal-sounding title with nothing proved in the shown section
    assert t3.formal("The Bayes-optimal denoiser recovers the class below a threshold", "Simulations agree.") == 0
    # a proof mentioned, but the title states no formal result
    assert t3.formal("Platform decay is caused by weakened constraints", shown_proof) == 0


def test_empirical_hedged_shape() -> None:
    assert t3.empirical_hedged(
        "Correlations have the Betti-curve signature of a hyperbolic ball, not of a uniform cube") == 1
    assert t3.empirical_hedged(
        "Odours have the signature of points near a boundary, not a Euclidean cloud") == 1
    assert t3.empirical_hedged("Place cells encode hyperbolic space") == 0


def test_score_rows_route_formal_entries(tmp_path: Path) -> None:
    theory(tmp_path, 1, title="An exact bound holds")
    theory(tmp_path, 2, title="People prefer stories")
    p = tmp_path / "theory.d" / "THEORY-001.md"
    p.write_text(p.read_text().replace("Stuff.", "Theorem 2 is proved."))
    by = {r["code"]: r for r in t3.score_rows(tmp_path, skip=set())}
    assert by["THEORY-001"]["route"] == "re-derivation"
    assert by["THEORY-002"]["route"] == "source"
    assert by["THEORY-001"]["rubric"]["formal"] == 1
    assert by["THEORY-001"]["triage"] == "triage-005"
