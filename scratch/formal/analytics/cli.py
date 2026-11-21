# scratch/formal/analytics/cli.py
"""Recompute the record's derived numbers with an Apache Hamilton dataflow.

Run from the repository root:

    python3 -I scratch/formal/analytics/cli.py run --outputs=all --out=analytics.json
    python3 -I scratch/formal/analytics/cli.py run --outputs=fast --out=analytics.json
    python3 -I scratch/formal/analytics/cli.py run --outputs=census_coverage,topic_term_count
    python3 -I scratch/formal/analytics/cli.py nodes

`--outputs` takes `all` (every figure), `fast` (every figure but those
tagged cost=slow, which replay the whole history) or node names. Hamilton
computes only the nodes the requested outputs need. The JSON names, under
`computed_at`, the commit every figure was read from.
"""
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "decision-census")]
os.environ.setdefault("HAMILTON_TELEMETRY_ENABLED", "false")

import fire  # noqa: E402
from hamilton import driver  # noqa: E402
from hamilton.lifecycle import NodeExecutionHook  # noqa: E402
from loguru import logger  # noqa: E402

import census_nodes  # noqa: E402
import gitread as gr  # noqa: E402
import history  # noqa: E402
import snapshot  # noqa: E402

MODULES = (snapshot, census_nodes, history)
CENSUS_DIR = HERE.parent / "decision-census" / "census"
GROWTH_DATES = ("2026-09-25", "2026-10-15", "2026-11-01", "2026-11-19")


class Timer(NodeExecutionHook):
    """Log each node's run time."""

    def __init__(self) -> None:
        self.t: dict[str, float] = {}

    def run_before_node_execution(self, *, node_name: str, **kwargs) -> None:
        self.t[node_name] = time.perf_counter()

    def run_after_node_execution(self, *, node_name: str, success: bool, **kwargs) -> None:
        dt = time.perf_counter() - self.t.pop(node_name, time.perf_counter())
        (logger.debug if success else logger.error)(f"{node_name}: {dt:.2f}s{'' if success else ' FAILED'}")


def build() -> driver.Driver:
    return driver.Builder().with_modules(*MODULES).with_adapters(Timer()).build()


def catalog(dr: driver.Driver) -> dict[str, dict]:
    """name -> tags for every computed node (external inputs left out)."""
    return {v.name: dict(v.tags) for v in dr.list_available_variables() if not v.is_external_input}


def select(cat: dict[str, dict], outputs: str | list[str] | tuple[str, ...]) -> list[str]:
    """Resolve `all`, `fast` or a list of node names to node names."""
    names = [outputs] if isinstance(outputs, str) else list(outputs)
    names = [n.strip() for x in names for n in str(x).split(",") if n.strip()]
    figures = [n for n, t in cat.items() if t.get("role") not in ("intermediate", "meta")]
    out: list[str] = []
    for n in names:
        if n == "all":
            out += figures
        elif n == "fast":
            out += [f for f in figures if cat[f].get("cost") != "slow"]
        elif n in cat:
            out.append(n)
        else:
            raise ValueError(f"unknown node {n!r}; see the `nodes` command")
    return list(dict.fromkeys(out))


def jsonable(x):
    """Make tuples, sets and non-string keys JSON-safe."""
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, set)):
        return [jsonable(v) for v in (sorted(x) if isinstance(x, set) else x)]
    return x


def compute(outputs: str | list[str] = "all", repo: str = ".", rev: str = "HEAD",
            census_dir: str | None = None, term_changes_rev: str | None = None,
            growth_ref: str | None = None, growth_dates: list[str] | None = None) -> dict:
    """Compute the requested nodes and return the document `run` writes."""
    repo = str(Path(repo).resolve())
    dr = build()
    names = select(catalog(dr), outputs)
    if growth_ref is None:
        growth_ref = next((r for r in ("origin/main", "main") if gr.has_rev(repo, r)), rev)
    inputs = {
        "repo": repo, "rev": rev,
        "census_dir": str(census_dir or CENSUS_DIR),
        "term_changes_rev": term_changes_rev or rev,
        "growth_ref": growth_ref,
        "growth_dates": list(growth_dates or GROWTH_DATES),
    }
    if gr.resolve(repo, rev) != gr.resolve(repo, "HEAD") and {"schema_rates_report", "record_rates_report"} & set(names):
        logger.warning("schema_rates_report and record_rates_report read HEAD, not --rev")
    logger.info(f"computing {len(names)} node(s) at {rev}")
    res = dr.execute(["computed_at", *names], inputs=inputs)
    return {
        "computed_at": res["computed_at"],
        "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "inputs": {k: v for k, v in inputs.items() if k != "repo"},
        "values": jsonable({n: res[n] for n in names}),
    }


class CLI:
    """Recompute the record's derived numbers."""

    def run(self, outputs: str = "all", out: str = "analytics.json", repo: str = ".", rev: str = "HEAD",
            census_dir: str | None = None, term_changes_rev: str | None = None,
            growth_ref: str | None = None, growth_dates: str | None = None) -> None:
        """Compute `outputs` against `rev` and write one JSON to `out` ('-' for stdout)."""
        dates = None
        if growth_dates:
            dates = growth_dates.split(",") if isinstance(growth_dates, str) else [str(d) for d in growth_dates]
        doc = compute(outputs, repo, rev, census_dir, term_changes_rev, growth_ref, dates)
        text = json.dumps(doc, indent=1, ensure_ascii=False)
        if out == "-":
            print(text)
        else:
            Path(out).write_text(text + "\n")
            logger.info(f"wrote {len(doc['values'])} figure(s) to {out} "
                        f"(computed at {doc['computed_at']['short']}, {doc['computed_at']['date']})")

    def nodes(self) -> None:
        """List the nodes, with the manuscript sections each one feeds."""
        for name, tags in sorted(catalog(build()).items()):
            role = tags.get("role", "figure")
            print(f"{name:28s} {role:12s} {tags.get('cost', ''):5s} {tags.get('feeds', '')}")


if __name__ == "__main__":
    fire.Fire(CLI)
