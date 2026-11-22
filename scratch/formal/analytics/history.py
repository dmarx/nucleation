# scratch/formal/analytics/history.py
"""Hamilton nodes: figures read from the record's git history.

Inputs: `repo`, `growth_ref` (the branch whose first-parent history gives
the dated snapshots), `growth_dates` (YYYY-MM-DD), `term_changes_rev` (the
revision the term-change audit reads up to). Nodes tagged cost=slow replay
the whole history and take minutes; `--outputs=fast` leaves them out.
"""
import contextlib
import io
from collections import Counter

from hamilton.function_modifiers import tag

import gitread as gr
import term_changes as tc  # noqa: E402  (decision-census/term_changes.py)
import schema_rates  # noqa: E402  (scratch/formal/schema_rates.py)
import record_rates  # noqa: E402  (scratch/formal/record_rates.py)

BOT = "github-actions[bot]"


@tag(feeds="§12.1, §12.5", section="history")
def growth_snapshots(repo: str, growth_ref: str, growth_dates: list[str]) -> dict[str, dict | None]:
    """{date: §12.5 measures at the last first-parent commit on growth_ref by 23:59 UTC that day}."""
    out = {}
    for day in growth_dates:
        sha = gr.last_first_parent_by(repo, growth_ref, day)
        out[day] = gr.grammar_counts(repo, sha) if sha else None
    return out


@tag(feeds="§12.1, §12.7", section="history")
def commit_counts(repo: str, computed_at: dict) -> dict[str, int]:
    """Commits reachable from the snapshot: all, non-merge, and non-merge by the bot."""
    sha = computed_at["sha"]
    authors = gr.git(repo, "log", "--no-merges", "--format=%an", sha).splitlines()
    return {
        "all": int(gr.git(repo, "rev-list", "--count", sha).strip()),
        "non_merge": len(authors),
        "non_merge_bot": sum(1 for a in authors if a == BOT),
    }


@tag(role="intermediate", cost="slow")
def term_change_events(repo: str, term_changes_rev: str) -> list[dict]:
    """term_changes.events: every reworded or removed vocabulary term up to term_changes_rev."""
    return tc.events(repo, term_changes_rev)


@tag(feeds="§15.2, §16.1", section="history", cost="slow")
def term_change_summary(term_change_events: list[dict]) -> dict:
    """Counts of the term-change audit, and each event's carriers and carriers touched."""
    ev = term_change_events
    return {
        "events": len(ev),
        "by_kind": dict(Counter(e["kind"] for e in ev)),
        "adr_in_unit": sum(1 for e in ev if e["adr_in_unit"]),
        "unit_is_commit": sum(1 for e in ev if e["pr"] is None),
        "untouched_with_carriers": [f"{e['vocabulary']}:{e['term']}" for e in ev
                                    if e["carriers"] and not e["carriers_touched"]],
        "events_list": ev,
    }


def _captured(fn, *args) -> list[str]:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*args)
    return buf.getvalue().splitlines()


@tag(feeds="§12.6 (CASE-178's measures, rerun on the whole history)", section="history", cost="slow")
def schema_rates_report(repo: str) -> list[str]:
    """schema_rates.py's report at the repository's HEAD, line by line."""
    return _captured(schema_rates.main, repo)


@tag(feeds="§12.7 (CASE-180's measures, rerun on the whole history)", section="history", cost="slow")
def record_rates_report(repo: str) -> list[str]:
    """record_rates.py's report at the repository's HEAD, line by line."""
    return _captured(record_rates.main, repo)
