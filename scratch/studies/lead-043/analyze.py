"""Summarize LEAD-043's results.jsonl into summary.json and summary.md.

For every arm, each readout is reported as a rate over the target facts
that were forgotten at cue A, pooled over seeds and over both worlds
(each world's model read against its own values), next to the same
readout's rate against the twin world's values (the false-positive
baseline: the model never held those values).

Usage: python3 -I analyze.py results.jsonl OUTDIR
"""
import json
import sys

import numpy as np

STAGES = ("emb", "attn0", "mlp0", "attn1", "mlp1")
O = 16


def flags(post, tag, cues):
    d = post[tag]
    n = len(d["cue"]["A"])
    held = [t for t in ("B", "C") if t not in cues]
    f = {}
    f["forgotten_A"] = np.array([1 - x for x in d["cue"]["A"]]) if tag == "own" else None
    for t in ("A", "B", "C"):
        f["cue_" + t] = np.array(d["cue"][t])
    f["readdress"] = np.max([d["cue"][t] for t in held], 0) if held else np.zeros(n, int)
    f["second"] = np.array(d["second"])
    for i in (1, 2, 3):
        f[f"lens_{STAGES[i]}"] = np.array(d["lens"][i])
        f[f"lin_{STAGES[i]}"] = np.array(d["lin"][i])
        f[f"mlp_{STAGES[i]}"] = np.array(d["mlp"][i])
    f["lin_final"] = np.array(d["lin"][4])
    f["mlp_final"] = np.array(d["mlp"][4])
    f["upstream_reader"] = np.max([d[k][i] for k in ("lens", "lin", "mlp") for i in (1, 2, 3)], 0)
    for k, v in d["revert"].items():
        f["revert_" + k] = np.array(v)
    f["revert_late"] = np.max([d["revert"][k] for k in ("head", "mlp1", "from_mlp1")], 0)
    pA = np.array(d["p"]["A"])
    f["elevated_p"] = (pA > 2.0 / O).astype(int)
    f["pA"] = pA
    return f


def summarize(recs):
    arms = sorted({r["arm"] for r in recs}, key=lambda a: [r["arm"] for r in recs].index(a))
    out = {}
    for arm in arms:
        rs = [r for r in recs if r["arm"] == arm]
        own, oth, mask = {}, {}, []
        rel = {"own": [], "other": [], "held_own": [], "held_other": [],
               "held0_own": [], "held0_other": []}
        pre = {"A": [], "B": [], "C": []}
        ft, retain, allold = [], [], []
        for r in rs:
            cues = r["cues"]
            for wd in "AB":
                post = r["post"][wd]
                fo, fx = flags(post, "own", cues), flags(post, "other", cues)
                m = fo["forgotten_A"] if not arm.startswith("overwrite") else 1 - fo["cue_A"]
                mask.append(m)
                for k in fo:
                    if k == "forgotten_A":
                        continue
                    own.setdefault(k, []).append(fo[k])
                    oth.setdefault(k, []).append(fx[k])
                for tag in ("own", "other"):
                    rl = r["relearn"][wd][tag]
                    rel[tag].append(rl["steps"])
                    tr = np.array(rl["traj"])
                    rel["held_" + tag].append(float(tr[-1, 2]))
                    rel["held0_" + tag].append(float(tr[0, 2]))
                for t in pre:
                    pre[t].append(r["pre"][wd]["target"][t])
                ft.append(r["ft_steps"][wd])
                retain.append(post["retain_acc"]["A"])
                allold.append(post["all_old_acc_A"])
        mask = np.concatenate(mask).astype(bool)
        res = {"n_items": len(rs), "n_target_facts": int(mask.size),
               "n_forgotten_A": int(mask.sum()),
               "pre_target_acc": {t: float(np.mean(v)) for t, v in pre.items()},
               "ft_steps_median": float(np.median(ft)),
               "retain_acc_A": float(np.mean(retain)),
               "all_old_acc_A": float(np.mean(allold)),
               "readouts_on_forgotten": {}, "relearn": {}}
        for k in own:
            a, b = np.concatenate(own[k]), np.concatenate(oth[k])
            if k == "pA":
                res["mean_pA_own"] = float(a[mask].mean()) if mask.any() else None
                res["mean_pA_other"] = float(b[mask].mean()) if mask.any() else None
                for N in (1, 16, 256):
                    res[f"coverage_N{N}_own"] = float((1 - (1 - a[mask]) ** N).mean()) if mask.any() else None
                    res[f"coverage_N{N}_other"] = float((1 - (1 - b[mask]) ** N).mean()) if mask.any() else None
                continue
            if mask.any():
                res["readouts_on_forgotten"][k] = [round(float(a[mask].mean()), 3),
                                                   round(float(b[mask].mean()), 3)]
        for tag in ("own", "other"):
            res["relearn"][f"steps_median_{tag}"] = float(np.median(rel[tag]))
            res["relearn"][f"steps_all_{tag}"] = rel[tag]
            res["relearn"][f"heldout_acc_end_{tag}"] = float(np.mean(rel["held_" + tag]))
            res["relearn"][f"heldout_acc_start_{tag}"] = float(np.mean(rel["held0_" + tag]))
        out[arm] = res
    return out


def to_md(s):
    lines = ["# LEAD-043 summary", "",
             "Each readout: rate among target facts forgotten at cue A, "
             "against own values / against the twin's values (baseline).", ""]
    for arm, r in s.items():
        lines.append(f"## {arm}")
        lines.append("")
        lines.append(f"- items {r['n_items']}, target facts {r['n_target_facts']}, "
                     f"forgotten at A {r['n_forgotten_A']}; pre-fine-tune target acc "
                     f"{r['pre_target_acc']}; fine-tune steps (median) {r['ft_steps_median']}; "
                     f"retained-fact acc at A {r['retain_acc_A']:.3f}; all old facts at A "
                     f"{r['all_old_acc_A']:.3f}")
        if r.get("mean_pA_own") is not None:
            lines.append(f"- p(value) at A: own {r['mean_pA_own']:.4f}, other {r['mean_pA_other']:.4f}; "
                         + ", ".join(f"coverage N={N} {r[f'coverage_N{N}_own']:.3f}/{r[f'coverage_N{N}_other']:.3f}"
                                     for N in (1, 16, 256)))
        rl = r["relearn"]
        lines.append(f"- relearning: steps to criterion (median) own {rl['steps_median_own']}, "
                     f"other {rl['steps_median_other']}; held-out half acc at A, start->end: own "
                     f"{rl['heldout_acc_start_own']:.3f}->{rl['heldout_acc_end_own']:.3f}, other "
                     f"{rl['heldout_acc_start_other']:.3f}->{rl['heldout_acc_end_other']:.3f}")
        for k, (a, b) in r["readouts_on_forgotten"].items():
            lines.append(f"  - {k}: {a} / {b}")
        lines.append("")
    return "\n".join(lines)


def main():
    recs = [json.loads(l) for l in open(sys.argv[1])]
    s = summarize(recs)
    json.dump(s, open(f"{sys.argv[2]}/summary.json", "w"), indent=1)
    open(f"{sys.argv[2]}/summary.md", "w").write(to_md(s))
    print(to_md(s))


if __name__ == "__main__":
    main()
