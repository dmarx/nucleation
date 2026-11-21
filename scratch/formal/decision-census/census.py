# scratch/formal/decision-census/census.py
"""Aggregate the census of the record's decisions (census/batch-*.json) and
measure agreement with the second coder (census/recode.json).

Usage: python -I census.py [CENSUS_DIR]   (default: ./census)
Prints markdown tables to stdout.

The tables are also available as data, for the analytics pipeline
(scratch/formal/analytics): `load_rows`, `load_recode`, `summary` and
`agreement` return what `main` prints.
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
PERIODS = ["25 Sep-15 Oct", "16 Oct-5 Nov", "6-20 Nov"]
BY_PERIOD = ("regime", "level", "trigger", "noticer", "proposer", "ratification")


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
    w = week_of(day)
    return "25 Sep-15 Oct" if w <= 3 else "16 Oct-5 Nov" if w <= 6 else "6-20 Nov"


def load_rows(d="census"):
    """Every coded decision in d/batch-*.json, sorted by code."""
    rows = [r for p in sorted(Path(d).glob("batch-*.json")) for r in json.loads(p.read_text())]
    rows.sort(key=lambda r: r["adr"])
    return rows


def load_recode(d="census"):
    """The second coder's rows by code, or {} when d/recode.json is absent."""
    rp = Path(d) / "recode.json"
    return {r["adr"]: r for r in json.loads(rp.read_text())} if rp.exists() else {}


def by_period(g, field):
    """{period: {"n": changes in it, category: count}} for one field of the grammar changes."""
    listy = isinstance(g[0][field], list)
    vals = lambda r: r[field] if listy else [r[field]]  # noqa: E731
    cats = sorted({v for r in g for v in vals(r)})
    out = {}
    for p in PERIODS:
        rs = [r for r in g if period(r["date"]) == p]
        c = Counter(v for r in rs for v in vals(r))
        out[p] = {"n": len(rs), **{k: c[k] for k in cats}}
    return out


def summary(rows):
    """The census tables as data (counts are over grammar changes)."""
    g = [r for r in rows if r.get("grammar_change") is True]
    mig = [r["migration"] for r in g if isinstance(r.get("migration"), int)]
    return {
        "decisions_coded": len(rows),
        "grammar_changes": len(g),
        "regime": dict(Counter(r["regime"] for r in g)),
        "component": dict(Counter(c for r in g for c in r["component"])),
        "operation": dict(Counter(o for r in g for o in r["operation"])),
        "residue": dict(Counter(r["residue"] for r in g)),
        "outcome": dict(Counter(r["outcome"] for r in g)),
        "by_period": {f: by_period(g, f) for f in BY_PERIOD} if g else {},
        "noticer_by_regime": dict(Counter(f"{r['noticer']} / {r['regime']}" for r in g)),
        "decider": dict(Counter(str(r.get("decider")) for r in g)),
        "ratification": dict(Counter(str(r.get("ratification")) for r in g)),
        "migrations_stated": len(mig),
        "entries_migrated": sum(mig),
        "migration_median": sorted(mig)[len(mig) // 2] if mig else 0,
        "later_harm": [r["adr"] for r in g if r.get("later_harm")],
    }


def agreement(rows, second):
    """Raw agreement and Cohen's kappa per categorical field, mean Jaccard per list field."""
    first = {r["adr"]: r for r in rows if r["adr"] in second}
    keys = sorted(first)
    out = {"n": len(keys), "fields": {}}
    if not keys:
        return out
    for f in CATEGORICAL:
        a = [str(first[k].get(f)) for k in keys]
        b = [str(second[k].get(f)) for k in keys]
        po = sum(x == y for x, y in zip(a, b)) / len(keys)
        out["fields"][f] = {"agreement": po, "kappa": cohen_kappa(a, b)}
    for f in LISTS:
        j = sum(jaccard(first[k].get(f), second[k].get(f)) for k in keys) / len(keys)
        out["fields"][f] = {"mean_jaccard": j}
    return out


def main(d="census"):
    rows = load_rows(d)
    s = summary(rows)
    print(f"Decisions coded: {s['decisions_coded']}; grammar changes: {s['grammar_changes']}")
    print(table(Counter(s["regime"]), "Regime (grammar changes)", "regime"))
    print(table(Counter(s["component"]), "Component revised", "component"))
    print(table(Counter(s["operation"]), "Operation", "operation"))
    print(table(Counter(s["residue"]), "Residue before the decision", "residue"))
    print(table(Counter(s["outcome"]), "Outcome", "outcome"))
    for field, per in s["by_period"].items():
        print(f"\n**{field} by period (grammar changes)**\n")
        cats = [k for k in per[PERIODS[0]] if k != "n"]
        print("| period | n | " + " | ".join(cats) + " |")
        print("|---|---:|" + "---:|" * len(cats))
        for p in PERIODS:
            print(f"| {p} | {per[p]['n']} | " + " | ".join(str(per[p][k]) for k in cats) + " |")
    print(table(Counter(s["noticer_by_regime"]), "Noticer by regime", "noticer / regime"))
    print(f"\nMigrations stated: {s['migrations_stated']}; entries changed: {s['entries_migrated']}; "
          f"median {s['migration_median']}")
    print(f"\nGrammar changes with recorded later harm: {len(s['later_harm'])}: "
          + ", ".join(s["later_harm"]))
    second = load_recode(d)
    if second:
        a = agreement(rows, second)
        print(f"\n**Agreement, {a['n']} decisions coded twice**\n")
        print("| field | agreement | Cohen's kappa |\n|---|---:|---:|")
        for f in CATEGORICAL:
            x = a["fields"][f]
            print(f"| {f} | {x['agreement']:.2f} | {x['kappa']:.2f} |")
        for f in LISTS:
            print(f"| {f} (mean Jaccard) | {a['fields'][f]['mean_jaccard']:.2f} | |")


if __name__ == "__main__":
    main(*sys.argv[1:])
