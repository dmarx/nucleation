"""Summarise coded.jsonl by arm under the measures fixed in codebook.md.
Usage: python3 -I summarize.py coded.jsonl > results.md"""
import json, sys
from collections import Counter


def load(path):
    last = {}
    for l in open(path):
        r = json.loads(l)
        last[r["id"]] = r  # a later line for the same id supersedes (append-only corrections)
    return list(last.values())


def rates(items):
    n = len(items)
    f = lambda pred: sum(1 for i in items if pred(i))
    return {"n": n, "H>=3": f(lambda i: i["H"] >= 3), "H>=4": f(lambda i: i["H"] >= 4),
            "A>=3": f(lambda i: i["A"] >= 3), "A>=4": f(lambda i: i["A"] >= 4), "SYS": f(lambda i: i["SYS"] == 1),
            "vendor": f(lambda i: i["vendor"] == 1),
            "H_dist": dict(sorted(Counter(i["H"] for i in items).items())),
            "A_dist": dict(sorted(Counter(i["A"] for i in items).items()))}


def verdict(internal, independent):
    pi_h, pi_a = internal["H>=3"] / internal["n"], internal["A>=3"] / internal["n"]
    pe_h, pe_a = independent["H>=3"] / independent["n"], independent["A>=3"] / independent["n"]
    if pi_h < .25 and pi_a < .25 and pe_h - pi_h >= .30 and pe_a - pi_a >= .30:
        return "prediction holds in the pilot"
    if (abs(pe_h - pi_h) <= .15 and abs(pe_a - pi_a) <= .15) or (pi_h > .5 and pi_a > .5):
        return "defeater's direction met"
    return "inconclusive"


def main(path):
    items = load(path)
    arms = {a: rates([i for i in items if i["arm"] == a]) for a in ("internal", "independent")}
    print("| measure | internal | independent |\n|---|---|---|")
    for k in ("n", "H>=3", "H>=4", "A>=3", "A>=4", "SYS", "vendor"):
        a, b = arms["internal"][k], arms["independent"][k]
        if k == "n":
            print(f"| n | {a} | {b} |")
        else:
            print(f"| {k} | {a} ({100*a/arms['internal']['n']:.0f}%) | {b} ({100*b/arms['independent']['n']:.0f}%) |")
    print(f"\nH distribution: internal {arms['internal']['H_dist']}, independent {arms['independent']['H_dist']}")
    print(f"A distribution: internal {arms['internal']['A_dist']}, independent {arms['independent']['A_dist']}")
    print(f"\nReading under the rule fixed in advance: {verdict(arms['internal'], arms['independent'])}")


if __name__ == "__main__":
    main(sys.argv[1])
