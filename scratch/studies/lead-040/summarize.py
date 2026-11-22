"""Tables for the CASE, from results.jsonl. Usage: python3 -I summarize.py"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = [json.loads(l) for l in open(os.path.join(HERE, "results.jsonl")) if l.strip()]


def f(x, nd=2):
    return "nan" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{nd}f}"


def group(prefix):
    return [r for r in ROWS if r["id"].startswith(prefix)]


def mean(xs):
    xs = [x for x in xs if x is not None and not (isinstance(x, float) and math.isnan(x))]
    return sum(xs) / len(xs) if xs else float("nan")


print("## Networks\n")
print("| id | test MSE | target var | strong order | final walls = input walls | causal states |")
print("|---|---:|---:|---:|---:|---:|")
for r in ROWS:
    print(f"| {r['id']} | {r['test_mse']:.1e} | {f(r['target_var'], 3)} | {f(r['order_frac_strong'])} | "
          f"{f(r['final_walls_equal_input_walls'])} | {r['causal_states']['n_causal_states']} |")

PAIRS = [("wall", "structure"), ("wall", "te"), ("wall", "operative"),
         ("structure", "te"), ("structure", "operative"), ("te", "operative")]
for name, rows in (("trained", group("trained")), ("frozen scale 0.5", group("frozen-d4-scale0.5")),
                   ("frozen scale 1.5", group("frozen-d4-scale1.5"))):
    if not rows:
        continue
    print(f"\n## Partitions, {name} (mean over {len(rows)} networks)\n")
    print("| slice | density wall/struct/te/oper | " + " | ".join(f"{a}→{b} / {b}→{a}" for a, b in PAIRS) + " |")
    print("|---|---|" + "---|" * len(PAIRS))
    for t in ("4", "8", "12", "16"):
        S = [r["slices"][t] for r in rows]
        dens = "/".join(f(mean([s["density"][k] for s in S])) for k in ("wall", "structure", "te", "operative"))
        cells = []
        for a, b in PAIRS:
            p = [s["pairs"][f"{a}|{b}"] for s in S]
            cells.append(f"{f(mean([q[f'{a}_near_{b}'] for q in p]))} / {f(mean([q[f'{b}_near_{a}'] for q in p]))}")
        print(f"| {t} | {dens} | " + " | ".join(cells) + " |")
    print("\n| slice | TE at walls | TE off walls | flip persisted at walls | off walls | operative at input walls |")
    print("|---|---:|---:|---:|---:|---:|")
    for t in ("4", "8", "12", "16"):
        S = [r["slices"][t] for r in rows]
        print(f"| {t} | {f(mean([s['te_mean_at_walls'] for s in S]))} | {f(mean([s['te_mean_off_walls'] for s in S]))} | "
              f"{f(mean([s['flip_persisted_at_walls'] for s in S]))} | {f(mean([s['flip_persisted_off_walls'] for s in S]))} | "
              f"{f(mean([s['operative_at_input_walls'] for s in S]))} |")

print("\n## Interchange (move one wall by 2 sites)\n")
print("| id | t0 | IIA task | IIA self | walls match source | control window changed | net separates source/base |")
print("|---|---:|---:|---:|---:|---:|---:|")
for r in ROWS:
    ic = r["interchange"]
    for t0 in ("4", "8"):
        d = ic[t0]
        print(f"| {r['id']} | {t0} | {f(d['iia_task'])} | {f(d['iia_self'])} | {f(d['walls_match_source'])} | "
              f"{f(d['control_window_changed'])} | {f(ic['net_source_vs_base_separable'])} |")

print("\n## Closed pair against anchored wall (200 free steps)\n")
print("| id | pair survives, L=1/2/3/4/8 (trained horizon) | same, long | anchored survives long | drift | shrunk to 2: survives/annihilated | shrunk to 1 | anchored erased: back at 12 steps / 200 |")
print("|---|---|---|---:|---:|---|---|---|")
for r in ROWS:
    c = r["closed_vs_anchored"]
    sv = c["closed_pair_survival_by_L"]
    a = "/".join(f(sv[L]["pair_at_trained_horizon"]) for L in ("1", "2", "3", "4", "8"))
    b = "/".join(f(sv[L]["pair_at_long_horizon"]) for L in ("1", "2", "3", "4", "8"))
    s2, s1 = c["closed_pair_shrunk_to_2"], c["closed_pair_shrunk_to_1"]
    er = c["anchored_wall_removed"]
    print(f"| {r['id']} | {a} | {b} | {f(c['anchored']['one_wall_at_long_horizon'])} | {f(c['anchored']['mean_abs_drift'])} | "
          f"{f(s2['pair_survives_long'])}/{f(s2['annihilated_long'])} | {f(s1['pair_survives_long'])}/{f(s1['annihilated_long'])} | "
          f"{f(er['walls_back_at_trained_horizon'])}/{f(er['walls_back_at_long_horizon'])} (pos {f(er['mean_position_long'], 1)}) |")
