# scratch/tools/record_history/cli.py
"""CLI: derive the event table, per-entry profiles and the phase view.

    python3 -I scratch/tools/record_history/cli.py run --repo=. --out=scratch/studies/record-history
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
from record_history.events import alias_map, formerly_on_disk, replay
from record_history.gitlog import BlobReader, read_log
from record_history.phase import classify, exemplars, plot, summary_table
from record_history.profile import DAY, Params, profiles


def _write_csv(path: Path, rows: list[dict]) -> None:
    keys: list[str] = []
    for r in rows:
        keys += [k for k in r if k not in keys]
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "wt", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def extract(repo: str = ".", revs: str = "origin/main,origin/staging") -> tuple[list[dict], Schema]:
    """Replay the record's history into event rows."""
    root = Path(repo).resolve()
    config = OmegaConf.to_container(OmegaConf.load(root / "luria.yaml"), resolve=False)
    schema = Schema.from_config(config)
    dirs = [s["dir"] for s in config["schemes"].values()]
    commits = read_log(root, revs.split(","), dirs)
    logger.info(f"{len(commits)} commits touch the scheme directories")
    alias = alias_map(commits, formerly_on_disk(root, dirs))
    logger.info(f"{len(alias)} code aliases")
    blobs = BlobReader(root)
    try:
        rows = replay(commits, blobs, schema, alias)
    finally:
        blobs.close()
    return rows, schema


def run(repo: str = ".", out: str = "scratch/studies/record-history",
        revs: str = "origin/main,origin/staging", sweep_breadth: int = 250,
        stable_days: int = 14, generative: int = 1, window: int = 30,
        reactivation_days: int = 14, scheme: str = "CLAIM", keep_events: bool = False) -> None:
    """Write profiles.csv, summary.md and phase-<scheme>.png to `out`."""
    out_dir = Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    rows, _ = extract(repo, revs)
    now = max(r["time"] for r in rows)
    if keep_events:
        _write_csv(out_dir / "events.csv.gz", [{**r, "fields": json.dumps(r["fields"])} if "fields" in r else r for r in rows])
    params = Params(now=now, sweep_breadth=sweep_breadth, reactivation_days=reactivation_days,
                    windows=(7, window))
    profs = profiles(rows, params)
    classify(profs, stable_days, generative, window)
    _write_csv(out_dir / "profiles.csv", sorted(profs.values(), key=lambda p: p["code"]))
    plot(profs, scheme, window, stable_days, out_dir / f"phase-{scheme}.png")
    sweeps = sorted({(r["commit"][:9], r["breadth"], r["subject"]) for r in rows
                     if r.get("breadth", 0) >= sweep_breadth and not r["bot"]}, key=lambda x: -x[1])
    kinds: dict[str, int] = {}
    for r in rows:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    ex = exemplars(profs, scheme, window)
    lines = [f"# Record history: {scheme} profiles\n",
             f"Reference time: last commit, day {now // DAY} (Unix days). "
             f"Events: {len(rows)}; entries: {len(profs)}. Parameters: sweep_breadth={sweep_breadth}, "
             f"stable_days={stable_days}, generative>={generative} new dependents in {window} days, "
             f"reactivation gap {reactivation_days} days.\n",
             "## Events by kind\n", "| kind | events |\n|---|---|",
             *[f"| {k} | {v} |" for k, v in sorted(kinds.items(), key=lambda x: -x[1])], "",
             "## Quadrants by scheme\n", summary_table(profs),
             f"## Sweeps (owner commits touching at least {sweep_breadth} entries; their edits count as maintenance)\n",
             *[f"- `{c}` ({b} entries): {s}" for c, b, s in sweeps], "",
             f"## Exemplars ({scheme}, not young, most new dependents first)\n"]
    for q, ps in ex.items():
        lines.append(f"**{q}:** " + (", ".join(
            f"{p['code']} (+{p[f'new_dependents_{window}d']}, in {p['in_degree']}, "
            f"{p['days_since_prose']}d)" for p in ps) or "none"))
        lines.append("")
    (out_dir / "summary.md").write_text("\n".join(lines))
    logger.info(f"wrote {out_dir}")


if __name__ == "__main__":
    fire.Fire({"run": run})
