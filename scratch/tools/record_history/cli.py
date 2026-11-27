# scratch/tools/record_history/cli.py
"""CLI: derive the event table, per-entry profiles and the phase view.

    python3 -I scratch/tools/record_history/cli.py run --repo=. --out=DIR --keep_events=True
    python3 -I scratch/tools/record_history/cli.py report --events=DIR/events.csv.gz --tip=DIR/tip.json --out=DIR
    python3 -I scratch/tools/record_history/cli.py lead199 --dir=DIR --until=2026-11-22
"""
from __future__ import annotations

import csv
import datetime as dt
import gzip
import json
import sys
from pathlib import Path

if __package__ in (None, ""):  # run as a script under python3 -I
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import fire
from loguru import logger
from omegaconf import OmegaConf

from record_history.entries import Schema, code_of_path
from record_history.events import alias_map, formerly_on_disk, replay, tree_entries
from record_history.gitlog import BlobReader, read_log, tree_blobs
from record_history.phase import classify, exemplars, plot, summary_table
from record_history.lead199 import to_lead199
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
    tree = tree_blobs(root, rev, dirs)
    live = {c for c in map(code_of_path, tree) if c}
    alias = alias_map(commits, formerly_on_disk(root, dirs), live)
    logger.info(f"{len(alias)} code aliases")
    blobs = BlobReader(root)
    try:
        rows = replay(commits, blobs, schema, alias)
        tip = tree_entries(blobs, tree, schema, alias)
    finally:
        blobs.close()
    return rows, tip, alias


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
    rows, tip, alias = extract(repo, rev, walk)
    if keep_events:
        _write_csv(out_dir / "events.csv.gz",
                   [{**r, "fields": json.dumps(r["fields"])} if "fields" in r else r for r in rows])
        (out_dir / "tip.json").write_text(json.dumps({c: sorted(es) for c, es in tip.items()}))
        (out_dir / "alias.json").write_text(json.dumps(alias))
    _report(rows, out_dir, tip=tip, **kw)


def _load_tip(path: str) -> dict[str, set]:
    return {c: {tuple(e) for e in es} for c, es in json.loads(Path(path).read_text()).items()}


def lead199(dir: str, until: str = "2026-11-22") -> None:
    """Write LEAD-199's revisions.json, edges.json and population.json to DIR/lead199.

    Rows after the end of `until` (UTC) are dropped, so the window is CASE-307's.
    Then copy scratch/studies/lead-199/analyze.py and check1.py there and run them.
    """
    d = Path(dir)
    end = int(dt.datetime.fromisoformat(until).replace(tzinfo=dt.timezone.utc).timestamp()) + 86400
    rows = [r for r in read_events(str(d / "events.csv.gz")) if r["time"] < end]
    tip = _load_tip(str(d / "tip.json"))
    status = {p["code"]: p["status"] for p in profiles(rows, Params(now=end), tip).values()}
    revs, edges, pop = to_lead199(rows, tip, status, json.loads((d / "alias.json").read_text()))
    out = d / "lead199"
    out.mkdir(exist_ok=True)
    for name, obj in (("revisions", revs), ("edges", edges), ("population", pop)):
        (out / f"{name}.json").write_text(json.dumps(obj))
    logger.info(f"{len(revs)} revisions, {len(edges)} edge events, {len(pop)} claims in {out}")


def identities(rows: list[dict], tip: dict[str, set]) -> str:
    """LEAD-tmpn6mi2's check 3: one `created` per live entry; few temporary codes."""
    created: dict[str, int] = {}
    for r in rows:
        if r["kind"] == "created":
            created[r["code"]] = created.get(r["code"], 0) + 1
    none = sorted(c for c in tip if c not in created)
    many = sorted(c for c in tip if created.get(c, 0) > 1)
    tmp = sum(1 for r in rows if "-tmp" in r["code"] or "-tmp" in r.get("target", ""))
    return (f"Live entries: {len(tip)}; with no `created` event: {len(none)} {none[:10]}; "
            f"with more than one: {len(many)} {many[:10]}. Events naming a temporary code: "
            f"{tmp} of {len(rows)} ({tmp / max(len(rows), 1):.2%}).\n")


def report(events: str, out: str, tip: str | None = None, **kw) -> None:
    """Write the report from a saved event table (and tip.json), without replaying."""
    state = _load_tip(tip) if tip else None
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
             "## Identities (check 3)\n", identities(rows, tip) if tip is not None else "(no tip)\n",
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
    fire.Fire({"run": run, "report": report, "lead199": lead199})
