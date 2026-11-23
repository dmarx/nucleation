"""LEAD-191 study: the two routes on LIT-844's published figures.

Run from this directory: OPENBLAS_NUM_THREADS=1 python3 -I study.py
Writes results.json and prints a summary. About a minute on one core.
"""

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import routes as R  # noqa: E402

# --- 1. Published counts (LIT-844 section 6b, 6c, 8; arXiv 2412.16806v1)
N = 51_966_480
SHEAF = 77_118
CBD = 36_938_948
counts = {
    "instances": N,
    "instances_check_866108_pairs_x_60": 866_108 * 60,
    "sheaf_contextual": SHEAF,
    "sheaf_rate": SHEAF / N,
    "cbd_contextual": CBD,
    "cbd_rate": CBD / N,
    # sheaf region is inside the CbD region (proved in routes / tests), so
    # the instances on which the verdicts differ are exactly CBD - SHEAF,
    # all CbD-contextual and not sheaf-contextual
    "diverging": CBD - SHEAF,
    "diverging_rate": (CBD - SHEAF) / N,
    "share_of_cbd_contextual_the_sheaf_test_misses": (CBD - SHEAF) / CBD,
    # Delta >= 2 SF, so every CbD-contextual instance has SF < 1, and the
    # ns-part reading (contextual iff SF < 1) calls at least CBD contextual
    "ns_part_reading_at_least": CBD,
    "similar_subset_models_check_8661_pairs_x_60": 8661 * 60,
}

# --- 2. Printed instances: (SF, Delta) from Tables 1 and 2, with rounding
TABLE1 = [  # nouns, SF, Delta; three decimals
    ("scholar/opposition", 0.963, 2.217), ("apprentice/side", 0.992, 2.626),
    ("camera/telescope", 0.824, 2.737), ("tea/tree", 0.787, 3.260),
    ("prey/day", 1.000, 2.035), ("fox/passenger", 0.748, 1.496),
    ("dwarf/bass", 0.985, 1.979), ("dancer/scene", 0.969, 1.938),
    ("videos/text", 1.000, 2.000), ("series/sheep", 1.000, 1.999),
    ("fire/relief", 0.165, 0.376), ("person/photographer", 0.155, 0.310),
    ("track/rule", 0.165, 0.779), ("memory/saint", 0.141, 0.283),
    ("island/architect", 0.142, 0.292),
]
TABLE2 = [  # two decimals
    ("television/tv", 0.74, 1.47), ("grandmother/grandfather", 0.37, 0.73),
    ("painting/sculpture", 0.86, 2.09), ("artist/facility", 1.00, 5.25),
    ("supplier/producer", 0.73, 1.62), ("railroad/railway", 0.11, 0.22),
    ("journalist/reporter", 0.12, 0.24), ("station/hospital", 0.14, 0.54),
    ("creature/snake", 0.13, 0.26), ("assassin/journalist", 0.58, 1.15),
]


def verdict(value, threshold, half):
    """True/False when the rounded value is clear of the threshold, else None."""
    if value + half < threshold:
        return True
    if value - half >= threshold:
        return False
    return None


def consistent_eps(sf, delta, half, rng, n=400_000, keep=40):
    """Sample eps triples whose (SF, Delta) round to the printed values."""
    sfs = rng.uniform(max(sf - half, 0), min(sf + half, 1), n)
    eps = rng.uniform(-1, 1, (n, 3)) * sfs[:, None]
    which = rng.integers(0, 3, n)
    sign = rng.choice([-1.0, 1.0], n)
    eps[np.arange(n), which] = sign * sfs
    d = np.abs(eps[:, 0] - eps[:, 1]) + np.abs(eps[:, 1] - eps[:, 2]) + np.abs(eps[:, 2] + eps[:, 0])
    ok = np.abs(d - delta) <= half
    return eps[ok][:keep], int(ok.sum())


def printed(rng):
    rows = []
    for table, data, half in (("Table 1", TABLE1, 0.0005), ("Table 2", TABLE2, 0.005)):
        for name, sf, delta in data:
            feasible = 2 * (sf - half) <= delta + half and delta - half <= 6 * (sf + half)
            row = {
                "table": table, "nouns": name, "SF": sf, "Delta": delta,
                "feasible": bool(feasible),
                "sheaf": verdict(sf, 1 / 6, half),
                "cbd": verdict(delta, 2, half),
                "ns_part": verdict(sf, 1, half),
            }
            row["diverge"] = (row["cbd"] is True and row["sheaf"] is False)
            # nearest-NS readings vary with eps beyond (SF, Delta): report the
            # share of consistent eps triples on which each says contextual
            sample, hits = consistent_eps(sf, delta, half, rng)
            row["eps_samples"] = int(len(sample))
            if len(sample):
                for norm in ("sum", "max"):
                    vals = [R.nearest_ns_contextual(R.pr_like(e), norm) for e in sample]
                    row[f"nearest_ns_{norm}_share"] = float(np.mean(vals))
            rows.append(row)
    return rows


# --- 3. The readings compared on a reference sample of the whole eps cube
def cube(rng, n=3000):
    tally = {}
    for _ in range(n):
        eps = rng.uniform(-1, 1, 3) * rng.uniform(0, 1) ** 0.5
        e = R.pr_like(eps)
        cf = R.closed_form(eps)
        key = (
            "sheaf" if cf["sheaf"] else "-",
            "cbd" if cf["cbd"] else "-",
            "nspart" if cf["SF"] < 1 else "-",
            "nearest_sum" if R.nearest_ns_contextual(e, "sum") else "-",
            "nearest_max" if R.nearest_ns_contextual(e, "max") else "-",
        )
        tally[" ".join(key)] = tally.get(" ".join(key), 0) + 1
    return dict(sorted(tally.items(), key=lambda kv: -kv[1]))


def uniform_family():
    out = []
    for p in (0.0, 0.1, 1 / 6, 0.2, 0.5, 0.8, 0.95, 0.99, 1.0):
        e = R.pr_like((p, p, p))
        out.append({
            "p": p,
            "SF": R.signalling_fraction(e),
            "CF": R.contextual_fraction(e),
            "Delta": R.closed_form((p, p, p))["Delta"],
            "sheaf": R.sheaf_corrected(e),
            "cbd": R.cbd_contextual(e),
            "ns_part": R.ns_part_contextual(e),
            "nearest_sum": R.nearest_ns_contextual(e, "sum"),
            "nearest_max": R.nearest_ns_contextual(e, "max"),
        })
    return out


def main():
    rng = np.random.default_rng(191)
    res = {
        "counts": counts,
        "printed": printed(rng),
        "uniform_family": uniform_family(),
        "cube_sample": cube(rng),
    }
    (HERE / "results.json").write_text(json.dumps(res, indent=1, default=bool))
    print(json.dumps(res["counts"], indent=1))
    for r in res["printed"]:
        print(r["table"], r["nouns"], r["SF"], r["Delta"], "feasible" if r["feasible"] else "INFEASIBLE",
              "sheaf", r["sheaf"], "cbd", r["cbd"], "diverge" if r["diverge"] else "",
              {k: round(v, 2) for k, v in r.items() if k.startswith("nearest")}, r["eps_samples"])
    for u in res["uniform_family"]:
        print(u)
    print(res["cube_sample"])


if __name__ == "__main__":
    main()
