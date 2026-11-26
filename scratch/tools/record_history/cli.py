# scratch/tools/record_history/cli.py
"""CLI: derive the event table, per-entry profiles and the phase view.

    python3 -I scratch/tools/record_history/cli.py run --repo=. --out=DIR --keep_events=True
    python3 -I scratch/tools/record_history/cli.py report --events=DIR/events.csv.gz --out=DIR
"""
from __future__ import annotations

import csv
import gzip
import json
import sys
from pathlib import Path

if __package__ in (None, ""):  # run as a script under python3 -I
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import fire
from loguru import logger
from omegaconf import OmegaConf

from record_history.entries import Schema
from record_history.events import alias_map, formerly_on_disk, replay, tree_entries
from record_history.gitlog import BlobReader, read_log, tree_blobs
from record_history.phase import classify, exemplars, plot, summary_table
from record_history.profile import DAY, Params, profiles, sweep_commits


def _write_csv(path: Path, rows: list[dict]) -> None:
    keys: list[str] = []
    for r in rows:
        keys += [k for k in r if k not in keys]
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "wt", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def extract(repo: str = ".", rev: str = "origin/staging", walk: str = "all"):
    """Replay the record's history into event rows; read the tip's state."""
    root = Path(repo).resolve()
    config = OmegaConf.to_container(OmegaConf.load(root / "luria.yaml"), resolve=False)
    schema = Schema.from_config(config)
    dirs = [s["dir"] for s in config["schemes"].values()]
    commits = read_log(root, rev, dirs, walk)
    logger.info(f"{len(commits)} commits touch the scheme directories")
    alias = alias_map(commits, formerly_on_disk(root, dirs))
    logger.info(f"{len(alias)} code aliases")
    blobs = BlobReader(root)
    try:
        rows = replay(commits, blobs, schema, alias)
        tip = tree_entries(blobs, tree_blobs(root, rev, dirs), schema, alias)
    finally:
        blobs.close()
    return rows, tip


def read_events(path: str) -> list[dict]:
    """Load an event table written by `run --keep_events=True`."""
    rows = []
    with gzip.open(path, "rt", newline="") as f:
        for r in csv.DictReader(f):
            r["time"], r["breadth"] = int(r["time"]), int(r.get("breadth") or 1)
            r["bot"] = r["bot"] == "True"
            for k in ("churn", "added", "removed"):
                r[k] = int(r[k]) if r.get(k) else 0
            rows.append(r)
    return rows


def run(repo: str = ".", out: str = "scratch/studies/record-history",
        rev: str = "origin/staging", walk: str = "all", keep_events: bool = False, **kw) -> None:
    """Replay the history, then write the report (see `report` for its options)."""
    out_dir = Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    rows, tip = extract(repo, rev, walk)
    if keep_events:
        _write_csv(out_dir / "events.csv.gz",
                   [{**r, "fields": json.dumps(r["fields"])} if "fields" in r else r for r in rows])
        (out_dir / "tip.json").write_text(json.dumps({c: sorted(es) for c, es in tip.items()}))
    _report(rows, out_dir, tip=tip, **kw)


def report(events: str, out: str, tip: str | None = None, **kw) -> None:
    """Write the report from a saved event table (and tip.json), without replaying."""
    state = None
    if tip:
        state = {c: {tuple(e) for e in es} for c, es in json.loads(Path(tip).read_text()).items()}
    _report(read_events(events), Path(out), tip=state, **kw)


def _report(rows: list[dict], out_dir: Path, tip: dict | None = None, sweep_breadth: int = 250, created_share: float = 0.1,
            stable_days: int = 14, generative: int = 1, window: int = 30,
            reactivation_days: int = 14, scheme: str = "CLAIM", now: int | None = None,
            stability: str = "revision") -> None:
    """profiles.csv, summary.md and phase-<scheme>.png, for live entries."""
    out_dir.mkdir(parents=True, exist_ok=True)
    now = now or max(r["time"] for r in rows)
    params = Params(now=now, sweep_breadth=sweep_breadth, created_share=created_share,
                    reactivation_days=reactivation_days, windows=(7, window))
    every = profiles(rows, params, tip)
    profs = {c: p for c, p in every.items() if not p["deleted"]}
    classify(profs, stable_days, generative, window, stability)
    _write_csv(out_dir / "profiles.csv", sorted(every.values(), key=lambda p: p["code"]))
    plot(profs, scheme, window, stable_days, out_dir / f"phase-{scheme}.png", stability)
    sweeps = sweep_commits(rows, sweep_breadth, created_share)
    listed = sorted({(r["commit"][:9], r["breadth"], r["subject"]) for r in rows
                     if r["commit"] in sweeps}, key=lambda x: -x[1])
    kinds: dict[str, int] = {}
    for r in rows:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    ex = exemplars(profs, scheme, window)
    lines = [f"# Record history: {scheme} profiles\n",
             f"Reference time: day {now // DAY} (Unix days). Events: {len(rows)}; entries profiled: "
             f"{len(every)}, of which deleted: {len(every) - len(profs)}. Parameters: "
             f"stability={stability}, sweep_breadth={sweep_breadth}, created_share={created_share}, stable_days={stable_days}, "
             f"generative>={generative} new dependents in {window} days, reactivation gap "
             f"{reactivation_days} days.\n",
             "## Events by kind\n", "| kind | events |\n|---|---|",
             *[f"| {k} | {v} |" for k, v in sorted(kinds.items(), key=lambda x: -x[1])], "",
             "## Quadrants by scheme (live entries)\n", summary_table(profs),
             f"## Sweeps (at least {sweep_breadth} entries, under {created_share:.0%} created; "
             "their edits count as maintenance)\n",
             *[f"- `{c}` ({b} entries): {s}" for c, b, s in listed], "",
             f"## Exemplars ({scheme}, not young, most new dependents first)\n"]
    for q, ps in ex.items():
        lines.append(f"**{q}:** " + (", ".join(
            f"{p['code']} (+{p[f'new_dependents_{window}d']}, in {p['in_degree']}, "
            f"{p['days_since_revision']}d)" for p in ps) or "none"))
        lines.append("")
    (out_dir / "summary.md").write_text("\n".join(lines))
    logger.info(f"wrote {out_dir}")


if __name__ == "__main__":
    fire.Fire({"run": run, "report": report})
