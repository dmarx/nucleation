# record/promotion-audit/test_sample_wave5.py
"""Tests for sample_wave5.py: the wave-5 population and the fixed-rule sample."""
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import sample_wave5 as s5  # noqa: E402


def entry(path: Path, fm: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False) + "---\n\n# body\n")


def claim(root: Path, n: int, *, status="Proposed", warrant="interpretive") -> None:
    entry(root / "claims.d" / f"CLAIM-{n:03d}.md", {"number": n, "status": status, "warrant": warrant})


def theory(root: Path, n: int, *, status="Proposed", tags=("epistemology",), source=("LIT-001", "LIT-002", "LIT-003")) -> None:
    entry(root / "theory.d" / f"THEORY-{n:03d}.md",
          {"number": n, "status": status, "tags": list(tags), "source": list(source)})


def queue(path: Path, codes: list[str], requeue: list[str] = ()) -> Path:
    path.write_text(yaml.safe_dump({"candidates": [{"code": c} for c in codes],
                                    "requeue": [{"code": c} for c in requeue]}))
    return path


def test_population_takes_proposed_interpretive_claims_only(tmp_path):
    claim(tmp_path, 1)
    claim(tmp_path, 2, status="Active")
    claim(tmp_path, 3, warrant="demonstrated")
    claim(tmp_path, 4, warrant="empirical")
    q = queue(tmp_path / "q.yaml", [])
    assert s5.population(tmp_path, q) == ["CLAIM-001"]


def test_population_takes_multi_source_non_mathematics_theories(tmp_path):
    theory(tmp_path, 1)
    theory(tmp_path, 2, source=("LIT-001", "LIT-002"))
    theory(tmp_path, 3, tags=("mathematics", "epistemology"))
    theory(tmp_path, 4, status="Active")
    theory(tmp_path, 5, source=("LIT-001", "LIT-001", "LIT-002"))
    q = queue(tmp_path / "q.yaml", [])
    assert s5.population(tmp_path, q) == ["THEORY-001"]


def test_population_excludes_queued_and_requeued_codes(tmp_path):
    claim(tmp_path, 1)
    claim(tmp_path, 2)
    claim(tmp_path, 3)
    q = queue(tmp_path / "q.yaml", ["CLAIM-001"], requeue=["CLAIM-003"])
    assert s5.population(tmp_path, q) == ["CLAIM-002"]


def test_sample_takes_every_kth_from_the_middle_of_the_first_stride():
    codes = [f"CLAIM-{i:03d}" for i in range(1, 21)]  # 20 codes, k = 4, start = 2
    assert s5.sample(codes, 5) == ["CLAIM-003", "CLAIM-007", "CLAIM-011", "CLAIM-015", "CLAIM-019"]


def test_sample_of_a_small_population_returns_all_of_it():
    codes = ["CLAIM-001", "CLAIM-002", "CLAIM-003"]
    assert s5.sample(codes, 5) == codes


def test_codes_sort_by_scheme_then_number():
    assert s5.sort_codes(["THEORY-010", "CLAIM-100", "THEORY-002", "CLAIM-020"]) == \
        ["CLAIM-020", "CLAIM-100", "THEORY-002", "THEORY-010"]


def test_roots_drop_claims_resting_on_a_proposed_interpretive_claim(tmp_path):
    claim(tmp_path, 1)
    entry(tmp_path / "claims.d" / "CLAIM-002.md",
          {"number": 2, "status": "Proposed", "warrant": "interpretive", "rests_on": ["CLAIM-001"]})
    entry(tmp_path / "claims.d" / "CLAIM-003.md",
          {"number": 3, "status": "Proposed", "warrant": "interpretive", "rests_on": ["CLAIM-004"]})
    claim(tmp_path, 4, status="Active")
    theory(tmp_path, 1)
    q = queue(tmp_path / "q.yaml", [])
    assert s5.roots(tmp_path, q) == ["CLAIM-001", "CLAIM-003", "THEORY-001"]


def test_a_queued_premise_still_blocks_its_dependent(tmp_path):
    claim(tmp_path, 1)
    entry(tmp_path / "claims.d" / "CLAIM-002.md",
          {"number": 2, "status": "Proposed", "warrant": "interpretive", "rests_on": ["CLAIM-001"]})
    q = queue(tmp_path / "q.yaml", ["CLAIM-001"])
    assert s5.roots(tmp_path, q) == []


def test_a_demonstrated_proposed_premise_does_not_block(tmp_path):
    claim(tmp_path, 1, warrant="demonstrated")
    entry(tmp_path / "claims.d" / "CLAIM-002.md",
          {"number": 2, "status": "Proposed", "warrant": "interpretive", "rests_on": ["CLAIM-001"]})
    q = queue(tmp_path / "q.yaml", [])
    assert s5.roots(tmp_path, q) == ["CLAIM-002"]
