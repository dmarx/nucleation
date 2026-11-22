# scratch/studies/unfetched-api-sweep/summarize.py
"""Summarize the sweep's results.jsonl into an outcome table and a reading queue.

Run: python3 -I summarize.py out/results.jsonl out/
"""
from __future__ import annotations

import collections
import csv
import json
import sys
from pathlib import Path

ORDER = ["pdf", "html", "other", "challenge", "refused", "not-found", "error", "skipped-host-challenged"]
# Pages that answer but are not a copy of the work: abstracts, catalogues, search and link resolvers.
NOT_COPIES = ("pubmed.ncbi.nlm.nih.gov", "global.oup.com", "www.doabooks.org", "links.jstor.org", "econpapers.repec.org")


def best(rec: dict) -> tuple[str, dict | None]:
    """The best outcome over a work's probes, and the probe that gave it."""
    for o in ORDER:
        for p in rec["probes"]:
            if p["result"] == o:
                return o, p
    return "no-candidate", None


def queue_class(outcome: str, probe: dict | None) -> str:
    """Reading-queue class: read (a copy answered), check (a landing page to open), or none."""
    if outcome == "pdf":
        return "read"
    if outcome == "html" and probe is not None:
        return "none" if probe["host"] in NOT_COPIES else "check"
    return "none"


def main(jsonl: str, out_dir: str) -> None:
    recs = [json.loads(l) for l in Path(jsonl).read_text().splitlines() if l.strip()]
    out = Path(out_dir)
    counts = collections.Counter()
    rows = []
    for r in recs:
        o, p = best(r)
        counts[o] += 1
        rows.append({"code": r["code"], "outcome": o, "queue": queue_class(o, p),
                     "host": p["host"] if p else "", "kind": p["kind"] if p else "",
                     "version": p["version"] if p else "", "url": p["url"] if p else "",
                     "oa_status": r.get("oa_status", ""), "pmcid": r.get("pmcid", ""),
                     "title": r["title"]})
    with (out / "outcomes.tsv").open("w") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    q = collections.Counter(r["queue"] for r in rows)
    lines = [f"# Sweep outcomes ({len(rows)} works)", "", "| best outcome | works |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in counts.most_common()]
    lines += ["", f"Reading queue: {q['read']} with an open copy that answered, {q['check']} landing pages to open."]
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main(*sys.argv[1:3])
