# record/promotion-audit/test_warrant_sweep.py
"""Tests for warrant_sweep.py: which interpretive CLAIMs carry an empirical-sounding defeater."""
from pathlib import Path

from warrant_sweep import empirical_cues, sweep


def write_claim(d: Path, code: str, status: str, warrant: str, defeated_if: str) -> None:
    (d / f"{code}.md").write_text(
        f"---\nstatus: {status}\nwarrant: {warrant}\ndefeated_if: {defeated_if!r}\n---\n# {code}\n"
    )


def make_record(tmp_path: Path) -> Path:
    claims = tmp_path / "claims.d"
    claims.mkdir()
    write_claim(claims, "CLAIM-010", "Proposed", "interpretive", "A study showing readers ignore the label.")
    write_claim(claims, "CLAIM-002", "Proposed", "interpretive", "An observed case where uptake fails.")
    write_claim(claims, "CLAIM-003", "Proposed", "interpretive", "A reading that makes the two notions coincide.")
    write_claim(claims, "CLAIM-004", "Active", "interpretive", "A study showing the opposite.")
    write_claim(claims, "CLAIM-005", "Proposed", "empirical", "A measurement contradicting it.")
    return tmp_path


def test_cues_match_observation_words():
    assert empirical_cues("A survey finds no effect")
    assert empirical_cues("measured in a replication")
    assert not empirical_cues("An argument that the distinction collapses")


def test_empirical_model_is_a_term_of_art():
    assert not empirical_cues("Every empirical model of pragmatic judgements has a global extension")
    assert empirical_cues("an empirical test of the reading")


def test_sweep_keeps_proposed_interpretive_with_empirical_defeater(tmp_path):
    rec = make_record(tmp_path)
    assert sweep(rec) == ["CLAIM-002", "CLAIM-010"]


def test_sweep_sorts_numerically(tmp_path):
    rec = make_record(tmp_path)
    codes = sweep(rec)
    assert codes == sorted(codes, key=lambda c: int(c.split("-")[1]))


def test_sweep_skips_missing_defeater(tmp_path):
    claims = tmp_path / "claims.d"
    claims.mkdir()
    (claims / "CLAIM-001.md").write_text("---\nstatus: Proposed\nwarrant: interpretive\n---\n")
    assert sweep(tmp_path) == []
