# scratch/formal/analytics/snapshot.py
"""Hamilton nodes: the record as it stands at one revision.

Each public function is a node; its parameters name the nodes or inputs it
depends on. Inputs: `repo` (path to the repository) and `rev` (the revision
to read). Nodes tagged role=intermediate feed other nodes and are not
written by `--outputs=all`.
"""
from collections import Counter

from hamilton.function_modifiers import tag

import gitread as gr
from gitread import _flat, crosstab, vocabulary_terms


@tag(role="meta")
def computed_at(repo: str, rev: str) -> dict:
    """The commit every snapshot figure was read from: sha, committer date, subject."""
    return {"rev": rev, **gr.commit_info(repo, rev)}


@tag(role="intermediate")
def tree_files(repo: str, computed_at: dict) -> list[str]:
    return gr.ls_files(repo, computed_at["sha"])


@tag(role="intermediate")
def luria_yaml_text(repo: str, computed_at: dict) -> str:
    return gr.read_text(repo, computed_at["sha"], "luria.yaml") or ""


@tag(role="intermediate")
def luria_config(luria_yaml_text: str) -> dict:
    return gr.load_yaml(luria_yaml_text)


@tag(role="intermediate")
def scheme_dirs(luria_config: dict) -> dict[str, str]:
    return {n: (s or {}).get("dir") for n, s in (luria_config.get("schemes") or {}).items()}


@tag(role="intermediate")
def entries(repo: str, computed_at: dict, tree_files: list[str], scheme_dirs: dict[str, str]) -> list[dict]:
    """Every entry of every declared scheme, with its parsed frontmatter."""
    return gr.read_entries(repo, computed_at["sha"], tree_files, scheme_dirs)


@tag(feeds="§12.1, §12.5", section="snapshot")
def repo_file_count(tree_files: list[str]) -> int:
    """Files in the repository tree."""
    return len(tree_files)


@tag(feeds="§12.5", section="snapshot")
def record_file_count(tree_files: list[str]) -> int:
    """Files under record/."""
    return sum(1 for f in tree_files if f.startswith("record/"))


@tag(feeds="§12.5", section="snapshot")
def luria_yaml_lines(luria_yaml_text: str) -> int:
    return len(luria_yaml_text.splitlines())


@tag(feeds="§12.5", section="snapshot")
def scheme_count(scheme_dirs: dict[str, str]) -> int:
    return len(scheme_dirs)


@tag(feeds="§12.5", section="snapshot")
def vocabulary_count(luria_config: dict) -> int:
    return len(luria_config.get("vocabularies") or {})


@tag(feeds="", section="snapshot")
def vocabulary_term_counts(luria_config: dict) -> dict[str, int]:
    """Terms declared in each vocabulary."""
    return {k: len(v) for k, v in vocabulary_terms(luria_config).items()}


@tag(feeds="§12.5", section="snapshot")
def topic_term_count(vocabulary_term_counts: dict[str, int]) -> int:
    return vocabulary_term_counts.get("topics", 0)


@tag(feeds="", section="snapshot")
def entry_count(entries: list[dict]) -> int:
    return len(entries)


@tag(feeds="", section="snapshot")
def entries_by_scheme(entries: list[dict]) -> dict[str, int]:
    return dict(sorted(Counter(e["scheme"] for e in entries).items()))


@tag(feeds="§13.4 (LIT), §14.1 (ADR)", section="snapshot")
def entries_by_scheme_status(entries: list[dict]) -> dict[str, dict[str, int]]:
    """{scheme: {status: count}}."""
    out: dict[str, Counter] = {}
    for e in entries:
        out.setdefault(e["scheme"], Counter())[str(e["fm"].get("status"))] += 1
    return {s: dict(c.most_common()) for s, c in sorted(out.items())}


@tag(feeds="§14.1", section="snapshot")
def decision_status_counts(entries_by_scheme_status: dict[str, dict[str, int]]) -> dict[str, int]:
    """ADRs by status (the manuscript: 114 decisions, 70 Active, 37 Proposed, ...)."""
    return entries_by_scheme_status.get("ADR", {})


@tag(feeds="§13.4", section="snapshot")
def lit_status_counts(entries_by_scheme_status: dict[str, dict[str, int]]) -> dict[str, int]:
    """LITs by status (Active, Unavailable, Unfetched, Deferred, ...)."""
    return entries_by_scheme_status.get("LIT", {})


@tag(feeds="§13.2", section="snapshot")
def case_kind_by_standing(entries: list[dict]) -> dict[str, dict[str, int]]:
    """CASEs: kind x standing."""
    return crosstab([e for e in entries if e["scheme"] == "CASE"], "kind", "standing")


@tag(feeds="§13.3", section="snapshot")
def claim_warrant_by_status(entries: list[dict]) -> dict[str, dict[str, int]]:
    """CLAIMs: warrant x status."""
    return crosstab([e for e in entries if e["scheme"] == "CLAIM"], "warrant", "status")


@tag(feeds="§14.4", section="snapshot")
def lead_stage_counts(entries: list[dict]) -> dict[str, int]:
    """LEADs by stage (idea, specified, costed, ...)."""
    return dict(Counter(str(e["fm"].get("stage")) for e in entries if e["scheme"] == "LEAD").most_common())


@tag(feeds="manuscript README open item 2 (current count; the 237 of §15.2 is the carrier count when ADR-048 landed, in term_change_summary)", section="snapshot")
def anthology_candidate_count(entries: list[dict]) -> int:
    """Entries whose tags carry the `anthology-candidate` flag."""
    return sum(1 for e in entries if "anthology-candidate" in _flat(e["fm"].get("tags")))
