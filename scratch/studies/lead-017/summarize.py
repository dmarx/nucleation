"""Summarize results/results.jsonl into results/summary.json and stdout.

Thresholds are chosen on the calibration split (main worlds, seed 10) and
applied unchanged to the test split (seed 20) and the held-out worlds
(seed 30). The setting (g) is read here only to score.
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from measures import auc  # noqa: E402

rows = {}
for line in (HERE / "results" / "results.jsonl").read_text().splitlines():
    r = json.loads(line)
    rows[r["item"]] = r


def arr(split, world, key):
    return np.array(rows[f"{split}:{world}"][key])


def best_threshold(pos, neg):
    cand = np.unique(np.r_[pos, neg])
    ba = [(np.mean(pos > c) + np.mean(neg <= c)) / 2 for c in cand]
    return float(cand[int(np.argmax(ba))])


MAIN = ["denied", "unregistered", "accommodation"]
HELD = ["decoy_interoceptive", "direct_authority", "weak_registration", "habit_persistence"]
out = {}

# registration thresholds on calibration
thr = {}
for key in ["reg_int", "reg_pas", "reg_int_report", "reg_naive"]:
    pos = np.r_[arr("calibration", "denied", key), arr("calibration", "accommodation", key)]
    neg = arr("calibration", "unregistered", key)
    thr[key] = best_threshold(pos, neg)
pos = arr("calibration", "accommodation", "auth")
neg = np.r_[arr("calibration", "denied", "auth"), arr("calibration", "unregistered", "auth")]
thr["auth"] = best_threshold(pos, neg)
out["thresholds"] = thr

# test split: AUCs and the fraction called registered
test = {}
for key in ["reg_int", "reg_pas", "reg_int_report", "reg_naive"]:
    pos = np.r_[arr("test", "denied", key), arr("test", "accommodation", key)]
    neg = arr("test", "unregistered", key)
    test[key] = {"auc_registered_vs_not": round(auc(pos, neg), 3),
                 **{f"called_registered_{w}": round(float(np.mean(arr("test", w, key) > thr[key])), 3)
                    for w in MAIN}}
pa = arr("test", "accommodation", "auth")
test["auth"] = {"auc_accommodation_vs_denied": round(auc(pa, arr("test", "denied", "auth")), 3),
                "auc_accommodation_vs_unregistered": round(auc(pa, arr("test", "unregistered", "auth")), 3),
                **{f"called_authority_{w}": round(float(np.mean(arr("test", w, "auth") > thr["auth"])), 3)
                   for w in MAIN}}


def classify(split, w):
    r = arr(split, w, "reg_int") > thr["reg_int"]
    a = arr(split, w, "auth") > thr["auth"]
    lab = np.where(~r, "unregistered", np.where(a, "accommodation", "denied"))
    return {c: round(float(np.mean(lab == c)), 3) for c in MAIN}


test["three_way_by_reg_int_and_auth"] = {w: classify("test", w) for w in MAIN}
acc = np.mean([classify("test", w)[w] for w in MAIN])
test["three_way_accuracy"] = round(float(acc), 3)
# correlation with the setting, registered agents, scoring only
g = np.r_[arr("test", "denied", "g"), arr("test", "accommodation", "g")]
ri = np.r_[arr("test", "denied", "reg_int"), arr("test", "accommodation", "reg_int")]
test["spearman_reg_int_vs_g"] = round(float(stats.spearmanr(ri, g)[0]), 3)
out["test"] = test

held = {}
for w in HELD:
    held[w] = {"registered_truth": rows[f"held_out:{w}"]["registered_truth"],
               "pursuit_post": round(rows[f"held_out:{w}"]["pursuit_post"], 3)}
    for key in ["reg_int", "reg_pas", "reg_int_report", "reg_naive"]:
        held[w][f"called_registered_{key}"] = round(float(np.mean(arr("held_out", w, key) > thr[key])), 3)
    held[w]["called_authority"] = round(float(np.mean(arr("held_out", w, "auth") > thr["auth"])), 3)
    held[w]["three_way"] = classify("held_out", w)
out["held_out"] = held

out["pursuit"] = {w: [round(rows[f"test:{w}"]["pursuit_during"], 3),
                      round(rows[f"test:{w}"]["pursuit_post"], 3)] for w in MAIN}
out["behaviour"] = rows["behaviour:main"]
out["b"] = {k.split(":")[1]: round(v["b"], 3) for k, v in rows.items() if k.startswith("calib_b:")}

(HERE / "results" / "summary.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
