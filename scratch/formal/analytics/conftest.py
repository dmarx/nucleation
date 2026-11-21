# scratch/formal/analytics/conftest.py
"""A tiny luria record in a git repository, and the import path the modules need."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "decision-census")]
os.environ.setdefault("HAMILTON_TELEMETRY_ENABLED", "false")

CONFIG_1 = """\
vocabularies:
  topics:
    terms:
      alpha: {label: Alpha, blurb: first}
      beta: {label: Beta, blurb: second}
  statuses:
    terms:
      Active: {label: Active}
      Proposed: {label: Proposed}
schemes:
  ADR:
    dir: record/decisions.d
  CLAIM:
    dir: record/claims.d
  LIT:
    dir: record/literature.d
"""

CONFIG_2 = CONFIG_1.replace("blurb: first", "blurb: reworded").replace(
    "      beta: {label: Beta, blurb: second}\n", "") + """\
  CASE:
    dir: record/cases.d
  LEAD:
    dir: record/leads.d
"""

ENTRIES_1 = {
    "record/decisions.d/ADR-001.md": {"status": "Active", "tags": ["process"]},
    "record/decisions.d/ADR-002.md": {"status": "Proposed", "tags": ["process"]},
    "record/claims.d/CLAIM-001.md": {"status": "Active", "warrant": "demonstrated", "tags": ["alpha"]},
    "record/literature.d/LIT-001.md": {"status": "Active", "tags": ["alpha", "anthology-candidate"]},
}

ENTRIES_2 = {
    "record/decisions.d/ADR-002.md": {"status": "Active", "tags": ["process"]},
    "record/decisions.d/ADR-tmpabc12.md": {"status": "Proposed", "tags": ["process"]},
    "record/claims.d/CLAIM-002.md": {"status": "Proposed", "warrant": "interpretive", "tags": ["alpha"]},
    "record/cases.d/CASE-001.md": {"status": "Active", "kind": "specimen", "standing": "documented"},
    "record/cases.d/CASE-002.md": {"status": "Active", "kind": "construction", "standing": "fictional"},
    "record/leads.d/LEAD-001.md": {"status": "Open", "stage": "idea"},
    "record/leads.d/LEAD-002.md": {"status": "Open", "stage": "specified"},
    "record/decisions.d/_template.md": {"status": "Proposed"},
    "record/decisions.d/README.stub": None,
}

CENSUS = [
    {"adr": "ADR-001", "date": "2026-09-25", "status": "Active", "grammar_change": True,
     "level": ["term"], "operation": ["add"], "regime": "refine", "component": ["language"],
     "trigger": "filing", "noticer": "owner", "proposer": "owner", "decider": "owner",
     "ratification": "explicit", "residue": "prose", "migration": 3, "outcome": "in_force",
     "later_harm": ""},
    {"adr": "ADR-002", "date": "2026-10-20", "status": "Proposed", "grammar_change": True,
     "level": ["relation"], "operation": ["change"], "regime": "revise", "component": ["criteria"],
     "trigger": "review_or_audit", "noticer": "review_process", "proposer": "assistant",
     "decider": "unknown", "ratification": "none", "residue": "forced", "migration": None,
     "outcome": "in_force", "later_harm": "a later error"},
]


def write_entry(root: Path, path: str, fm: dict | None) -> None:
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    if fm is None:
        p.write_text("stub\n")
        return
    lines = ["---"]
    for k, v in fm.items():
        lines.append(f"{k}:" if isinstance(v, list) else f"{k}: {v}")
        lines += [f"- {x}" for x in v] if isinstance(v, list) else []
    p.write_text("\n".join(lines + ["---", "", "Body.", ""]))


def commit(root: Path, message: str, date: str) -> None:
    env = {**os.environ, "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date,
           "GIT_AUTHOR_NAME": "Owner", "GIT_AUTHOR_EMAIL": "owner@example.invalid",
           "GIT_COMMITTER_NAME": "Owner", "GIT_COMMITTER_EMAIL": "owner@example.invalid"}
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True, env=env)
    subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", message], check=True, env=env)


@pytest.fixture(scope="session")
def tiny_record(tmp_path_factory) -> dict:
    """Two commits a month apart; the second rewords a term, removes one, adds two schemes."""
    root = tmp_path_factory.mktemp("record")
    subprocess.run(["git", "init", "-q", "-b", "main", str(root)], check=True)
    (root / "luria.yaml").write_text(CONFIG_1)
    for path, fm in ENTRIES_1.items():
        write_entry(root, path, fm)
    commit(root, "Scaffold", "2026-09-25T12:00:00Z")
    (root / "luria.yaml").write_text(CONFIG_2)
    (root / "record/decisions.d/ADR-001.md").unlink()
    for path, fm in ENTRIES_2.items():
        write_entry(root, path, fm)
    (root / "notes.txt").write_text("outside the record\n")
    commit(root, "Grow (#1)", "2026-10-25T12:00:00Z")
    census_dir = tmp_path_factory.mktemp("census")
    (census_dir / "batch-1.json").write_text(json.dumps(CENSUS))
    (census_dir / "recode.json").write_text(json.dumps([CENSUS[0]]))
    return {"repo": str(root), "census_dir": str(census_dir)}
