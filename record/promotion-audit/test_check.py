# record/promotion-audit/test_check.py
"""Fires check.py against a consistent ledger and against each kind of drift (DP-4)."""
from pathlib import Path

import yaml

from check import problems

DECISION = {"id": "CLAIM-001", "disposition": "promote", "reviewed_revision": "abc"}


def ledger(tmp_path: Path, candidates: list[dict], decisions: list[dict], waves: list[dict] | None = None) -> Path:
    (tmp_path / "decisions").mkdir()
    for d in decisions:
        (tmp_path / "decisions" / f"{d['id']}.yaml").write_text(yaml.safe_dump(d))
    queue = {"version": 1, "handoff": {"batch": "batch-001", "next_step": "x"},
             "waves": waves or [], "candidates": candidates}
    (tmp_path / "queue.yaml").write_text(yaml.safe_dump(queue))
    return tmp_path


def decided(code: str = "CLAIM-001", disposition: str = "promote", wave: int = 1) -> dict:
    return {"code": code, "wave": wave, "state": "decided", "disposition": disposition,
            "decision": f"decisions/{code}.yaml"}


def test_consistent_ledger_passes(tmp_path):
    root = ledger(tmp_path, [decided(), {"code": "CLAIM-002", "wave": 1, "state": "pending"}], [DECISION],
                  [{"wave": 1, "reviewed": 1, "promotion_paths": 1}])
    assert problems(root) == []


def test_decided_without_file_fails(tmp_path):
    root = ledger(tmp_path, [decided()], [])
    assert any("no decision file" in p for p in problems(root))


def test_file_without_queue_entry_fails(tmp_path):
    root = ledger(tmp_path, [], [DECISION])
    assert any("not decided in the queue" in p for p in problems(root))


def test_disposition_mismatch_fails(tmp_path):
    root = ledger(tmp_path, [decided(disposition="split")], [DECISION])
    assert any("disposition" in p for p in problems(root))


def test_unknown_disposition_fails(tmp_path):
    bad = dict(DECISION, disposition="maybe")
    root = ledger(tmp_path, [decided(disposition="maybe")], [bad])
    assert any("not one of" in p for p in problems(root))


def test_wave_counts_must_match(tmp_path):
    root = ledger(tmp_path, [decided()], [DECISION], [{"wave": 1, "reviewed": 2, "promotion_paths": 1}])
    assert any("wave 1" in p for p in problems(root))


def test_duplicate_candidate_fails(tmp_path):
    root = ledger(tmp_path, [decided(), decided()], [DECISION])
    assert any("twice" in p for p in problems(root))


def test_more_than_one_in_review_fails(tmp_path):
    cands = [{"code": c, "wave": 1, "state": "in_review"} for c in ("CLAIM-002", "CLAIM-003")]
    root = ledger(tmp_path, cands, [])
    assert any("in_review" in p for p in problems(root))


def test_unparseable_batch_file_fails(tmp_path):
    root = ledger(tmp_path, [], [])
    (root / "batches").mkdir()
    (root / "batches" / "batch-001.yaml").write_text('note: "quoted" then more\n')
    assert any("batches/batch-001.yaml does not parse" in p for p in problems(root))
