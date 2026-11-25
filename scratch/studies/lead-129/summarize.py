"""Summarize the LEAD-129 matched comparison from pairs.json.

Run with isolation:  python3 -I summarize.py
Pure stdlib; no network. The input is a hand-built table of public-document
facts (see README.md for sources); this script only tallies it.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path=None):
    path = path or os.path.join(HERE, "pairs.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def persistence(arm):
    """Years a recognized inadequacy stood uncorrected, from the arm record."""
    return arm["correction"] - arm["recognition"]


def pair_gap(pair):
    """Fixed-arm persistence minus revising-arm persistence, in years.

    Positive means the arm WITHOUT an effective revision means left the
    recognized inadequacy standing longer, i.e. the direction CLAIM-685 predicts.
    """
    return persistence(pair["fixed_arm"]) - persistence(pair["revising_arm"])


def summarize(data):
    rows = []
    for p in data["pairs"]:
        rows.append(
            dict(
                id=p["id"],
                domain=p["domain"],
                revising_body=p["revising_arm"]["body"],
                revising_years=persistence(p["revising_arm"]),
                fixed_body=p["fixed_arm"]["body"],
                fixed_years=persistence(p["fixed_arm"]),
                gap_years=pair_gap(p),
            )
        )
    return rows


def main():
    data = load()
    rows = summarize(data)
    print(data["measure"])
    print()
    for r in rows:
        print(f"[{r['id']}] {r['domain']}")
        print(f"    revising: {r['revising_body']}: {r['revising_years']} yr")
        print(f"    fixed:    {r['fixed_body']}: {r['fixed_years']} yr")
        print(f"    gap (fixed - revising): {r['gap_years']} yr")
    x = data["unmatched_extreme"]
    print()
    print(f"[{x['id']}] UNMATCHED EXTREME: {x['body']}: "
          f"{x['correction'] - x['recognition']} yr (no revision organ)")
    gaps = [r["gap_years"] for r in rows]
    print()
    print(f"matched pairs: {len(rows)}; all gaps positive: {all(g > 0 for g in gaps)}; "
          f"gaps (yr): {gaps}")


if __name__ == "__main__":
    main()
