"""LEAD-101: summarize the coded cases and the study coefficients.

Run from this directory:  python3 -I summarize.py
Writes results.json beside this file.
"""
import csv
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def pct_from_log(beta):
    """Percent change in the count implied by a coefficient on log(count)."""
    return 100.0 * (math.exp(beta) - 1.0)


def significant(t, crit=1.96):
    """Two-tailed 5% significance from a t statistic."""
    return abs(t) >= crit


def standard_conditions(case):
    """The conditions CODING.md sets for meeting LEAD-101's standard.

    Returns a dict of condition -> bool. A W- case can meet the standard only
    by pairing with a case in the other arm with the same reputation and
    benefit codes; that is checked across cases in `pairs`.
    """
    after = case["outcome_after"]
    ended = after not in ("unripe", "open", "")
    arm_coded = case["arm"] in ("R", "S")
    outcome = after.startswith("W+") or after.startswith("W-")
    standing_ok = case["source_standing"] in ("finding", "study")
    if after.startswith("W+"):
        confounds_ok = case["reputation"] == "private" and case["benefit"] == "opposed"
    else:
        confounds_ok = False  # settled only by a pair; see pairs()
    return {
        "ended_with_window": ended,
        "arm_R_or_S": arm_coded,
        "post_lift_outcome": outcome and ended,
        "finding_or_study": standing_ok,
        "reputation_and_benefit_exclude": confounds_ok,
    }


def pairs(cases):
    """W- pairs across arms with equal reputation and benefit codes, each
    from a finding or study, with a post-lift window."""
    out = []
    eligible = [
        c for c in cases
        if c["arm"] in ("R", "S")
        and c["outcome_after"].startswith(("W+", "W-"))
        and c["source_standing"] in ("finding", "study")
        and c["reputation"] not in ("", "unknown")
        and c["benefit"] not in ("", "unknown")
    ]
    for i, a in enumerate(eligible):
        for b in eligible[i + 1:]:
            if a["arm"] != b["arm"] and a["reputation"] == b["reputation"] and a["benefit"] == b["benefit"]:
                out.append((a["case"], b["case"]))
    return out


def meets(case, paired):
    c = standard_conditions(case)
    base = c["ended_with_window"] and c["arm_R_or_S"] and c["post_lift_outcome"] and c["finding_or_study"]
    if case["outcome_after"].startswith("W+"):
        return base and c["reputation_and_benefit_exclude"]
    return base and case["case"] in paired


def load(name):
    with open(os.path.join(HERE, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    cases = load("cases.csv")
    studies = load("studies.csv")
    paired = {x for p in pairs(cases) for x in p}
    res = {"cases": {}, "pairs": pairs(cases), "coefficients": []}
    for c in cases:
        cond = standard_conditions(c)
        res["cases"][c["case"]] = {
            "arm": c["arm"],
            "outcome_after": c["outcome_after"],
            "conditions": cond,
            "lacks": [k for k, v in cond.items() if not v],
            "meets_standard": meets(c, paired),
        }
    for s in studies:
        b, t = float(s["beta"]), float(s["t"])
        res["coefficients"].append({
            "term": s["term"], "panel": s["panel"], "beta": b, "t": t,
            "percent": round(pct_from_log(b), 1), "significant_5pct": significant(t),
        })
    res["any_case_meets_standard"] = any(v["meets_standard"] for v in res["cases"].values())
    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    return res


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
