"""Driver for LEAD-048 (CASE-186). Appends one JSON line per cell to
results/<part>.jsonl and skips cells already written, so it resumes.

    python3 -I study.py core       # the principal grid, 64 seeds per cell
    python3 -I study.py baselines  # no-audit (habit) baseline

A cell's line holds counts over its seeds; per-seed records are not kept
(they would exceed the record's 1 MB limit for committed data).
"""
import itertools, json, os, sys, time
from statistics import median

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import Config, run, LESIONS, COMPONENT_LESIONS  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SEEDS = range(64)
RHO = {"ample": 0.6, "lean": 0.36}


def cells(part):
    if part == "core":
        for m, a, s, e, L, mt, sc, f in itertools.product(
                ("reciprocal", "external", "none"), ("protected", "selective"),
                ("independent", "captured", "ipw"), ("in_family", "out_family"),
                LESIONS, (False, True), (True, False), ("ample", "lean")):
            yield f, Config(maintenance=m, admission=a, scoring=s, env2=e,
                            lesion=L, matched=mt, self_check=sc, RHO=RHO[f])
    elif part == "baselines":
        for m, e, L, mt in itertools.product(
                ("reciprocal", "external", "none"), ("in_family", "out_family"),
                LESIONS, (False, True)):
            yield "ample", Config(maintenance=m, env2=e, lesion=L, matched=mt,
                                  audits=False, RHO=RHO["ample"])


def summarize(fuel, cfg, rows):
    n = len(rows)
    s1 = [r["S1"] for r in rows]
    s2 = [r["S2"] for r in rows]
    both = sum(a and b for a, b in zip(s1, s2))
    d = [r["detect_delay"] for r in rows if r["detect_delay"] is not None]
    out = {"key": cfg.key(), "maintenance": cfg.maintenance,
           "admission": cfg.admission, "scoring": cfg.scoring,
           "env2": cfg.env2, "lesion": cfg.lesion, "matched": cfg.matched,
           "self_check": cfg.self_check, "audits": cfg.audits, "fuel": fuel,
           "n": n, "S1": sum(s1), "S2": sum(s2), "S1andS2": both,
           "S2_correct": sum(r["S2_correct"] for r in rows),
           "S2_viable": sum(r["S2_viable"] for r in rows),
           "S2_budget": sum(r["S2_budget"] for r in rows),
           "detected": len(d), "delay_med": median(d) if d else None,
           "false_changes": sum(r["false_changes"] for r in rows),
           "regret_w2_mean": round(sum(r["regret_w2"] for r in rows) / n, 2),
           "regret_all_mean": round(sum(r["regret_all"] for r in rows) / n, 2),
           "fuel_spent_mean": round(sum(r["fuel_spent"] for r in rows) / n, 2),
           "prod_fuel_mean": round(sum(r["prod_fuel"] for r in rows) / n, 2),
           "fuel_short_runs": sum(r["fuel_short"] > 0 for r in rows),
           "final_A_mean": round(sum(r["final"][0] for r in rows) / n, 3),
           "final_G_mean": round(sum(r["final"][1] for r in rows) / n, 3)}
    if cfg.lesion in COMPONENT_LESIONS:
        out["flag_before_act"] = sum(r["flag_before_act"] for r in rows)
        fd = [r["flag_delay"] for r in rows if r["flag_delay"] is not None]
        out["flagged"] = len(fd)
        out["flag_delay_med"] = median(fd) if fd else None
    return out


def main(part):
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    path = os.path.join(HERE, "results", f"{part}.jsonl")
    done = set()
    if os.path.exists(path):
        with open(path) as fh:
            for line in fh:
                try:
                    done.add(json.loads(line)["key"])
                except (ValueError, KeyError):
                    pass  # a torn last line is rerun
    t0, k = time.time(), 0
    with open(path, "a") as fh:
        for fuel, cfg in cells(part):
            if cfg.key() in done:
                continue
            rows = [run(cfg, s) for s in SEEDS]
            fh.write(json.dumps(summarize(fuel, cfg, rows)) + "\n")
            fh.flush()
            k += 1
            if k % 100 == 0:
                print(f"{k} cells, {time.time() - t0:.0f}s", flush=True)
    print(f"done: {k} new cells in {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "core")
