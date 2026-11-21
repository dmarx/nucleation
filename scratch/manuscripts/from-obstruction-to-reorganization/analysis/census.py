# scratch/manuscripts/from-obstruction-to-reorganization/analysis/census.py
"""Aggregate the census of the record's decisions (census/batch-*.json) and
measure agreement with the second coder (census/recode.json).

Usage: python -I census.py [CENSUS_DIR]   (default: ./census)
Prints markdown tables to stdout.
"""
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

T0 = date(2026, 9, 25)  # the record's scaffold (af387c07b); the repository was created empty on 7 Sep
CATEGORICAL = ["grammar_change", "regime", "trigger", "noticer", "proposer",
               "decider", "ratification", "residue", "outcome"]
LISTS = ["level", "operation", "component"]


def week_of(day):
    return (date.fromisoformat(day) - T0).days // 7 + 1


def cohen_kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def jaccard(a, b):
    a, b = set(a or []), set(b or [])
    return 1.0 if not a | b else len(a & b) / len(a | b)


def crosstab(rows, f, g):
    return dict(Counter((str(r.get(f)), str(r.get(g))) for r in rows))


def table(counter, title, keyname):
    out = [f"\n**{title}**\n", f"| {keyname} | n |", "|---|---:|"]
    out += [f"| {k} | {v} |" for k, v in sorted(counter.items(), key=lambda kv: -kv[1])]
    return "\n".join(out)


def period(day):
    if day >= "2026-11-21":  # batch 5, coded single-handed on 2026-11-21
        return "21 Nov"
    w = week_of(day)
    return "25 Sep-15 Oct" if w <= 3 else "16 Oct-5 Nov" if w <= 6 else "6-20 Nov"


def main(d="census"):
    d = Path(d)
    rows = [r for p in sorted(d.glob("batch-*.json")) for r in json.loads(p.read_text())]
    rows.sort(key=lambda r: r["adr"])
    g = [r for r in rows if r.get("grammar_change") is True]
    print(f"Decisions coded: {len(rows)}; grammar changes: {len(g)}")
    print(table(Counter(r["regime"] for r in g), "Regime (grammar changes)", "regime"))
    print(table(Counter(c for r in g for c in r["component"]), "Component revised", "component"))
    print(table(Counter(o for r in g for o in r["operation"]), "Operation", "operation"))
    print(table(Counter(r["residue"] for r in g), "Residue before the decision", "residue"))
    print(table(Counter(r["outcome"] for r in g), "Outcome", "outcome"))
    pers = ["25 Sep-15 Oct", "16 Oct-5 Nov", "6-20 Nov", "21 Nov"]
    for field in ("regime", "level", "trigger", "noticer", "proposer", "ratification"):
        listy = isinstance(g[0][field], list)
        vals = lambda r: r[field] if listy else [r[field]]  # noqa: E731
        print(f"\n**{field} by period (grammar changes)**\n")
        cats = sorted({v for r in g for v in vals(r)})
        print("| period | n | " + " | ".join(cats) + " |")
        print("|---|---:|" + "---:|" * len(cats))
        for p in pers:
            rs = [r for r in g if period(r["date"]) == p]
            c = Counter(v for r in rs for v in vals(r))
            print(f"| {p} | {len(rs)} | " + " | ".join(str(c[k]) for k in cats) + " |")
    print("\n**All decisions coded, by period**\n")
    print("| period | n | grammar changes | Rejected | ratification explicit | decider owner |")
    print("|---|---:|---:|---:|---:|---:|")
    for p in pers:
        rs = [r for r in rows if period(r["date"]) == p]
        print(f"| {p} | {len(rs)} | {sum(r['grammar_change'] is True for r in rs)} | "
              f"{sum(r['status'] == 'Rejected' for r in rs)} | "
              f"{sum(r['ratification'] == 'explicit' for r in rs)} | "
              f"{sum(r['decider'] == 'owner' for r in rs)} |")
    print(table(Counter(f"{r['noticer']} / {r['regime']}" for r in g),
                "Noticer by regime", "noticer / regime"))
    mig = [r["migration"] for r in g if isinstance(r.get("migration"), int)]
    print(f"\nMigrations stated: {len(mig)}; entries changed: {sum(mig)}; "
          f"median {sorted(mig)[len(mig) // 2] if mig else 0}")
    harm = [r for r in g if r.get("later_harm")]
    print(f"\nGrammar changes with recorded later harm: {len(harm)}: "
          + ", ".join(r["adr"] for r in harm))
    rec = Path(d).resolve().parents[4] / "record" / "decisions.d"
    if rec.is_dir():
        drift = []
        for r in rows:
            f = rec / f"{r['adr']}.md"
            if f.exists():
                for line in f.read_text().split("---")[1].splitlines():
                    if line.startswith("status:"):
                        now = line.split(":", 1)[1].strip()
                        if now != r["status"]:
                            drift.append(f"{r['adr']} {r['status']}->{now}")
        print(f"\nCoded status changed in the record since coding: {len(drift)}"
              + (": " + ", ".join(drift) if drift else ""))
    rp = d / "recode.json"
    if rp.exists():
        second = {r["adr"]: r for r in json.loads(rp.read_text())}
        first = {r["adr"]: r for r in rows if r["adr"] in second}
        keys = sorted(first)
        print(f"\n**Agreement, {len(keys)} decisions coded twice**\n")
        print("| field | agreement | Cohen's kappa |\n|---|---:|---:|")
        for f in CATEGORICAL:
            a = [str(first[k].get(f)) for k in keys]
            b = [str(second[k].get(f)) for k in keys]
            po = sum(x == y for x, y in zip(a, b)) / len(keys)
            print(f"| {f} | {po:.2f} | {cohen_kappa(a, b):.2f} |")
        for f in LISTS:
            j = sum(jaccard(first[k].get(f), second[k].get(f)) for k in keys) / len(keys)
            print(f"| {f} (mean Jaccard) | {j:.2f} | |")


if __name__ == "__main__":
    main(*sys.argv[1:])
