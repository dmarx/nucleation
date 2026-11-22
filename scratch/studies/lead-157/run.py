"""LEAD-157 runs. Usage: python3 -I run.py e1|e2  (resumes: skips items already in the JSONL)."""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import lb  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TASK = lb.make_task(0)
DATA = {"both": lb.sample(TASK, 4000, "both", 1), "A": lb.sample(TASK, 4000, "A", 3),
        "B": lb.sample(TASK, 4000, "B", 4)}
XT, YT = lb.sample(TASK, 2000, "both", 2)          # measurement set (test, both cues)
XTR, YTR = DATA["both"]                             # both-cue train set
ALIGNS = ("none", "wm", "am", "swm")
CURVES = ("bezier", "polychain")


def done_keys(path):
    if not os.path.exists(path):
        return set()
    with open(path) as f:
        return {json.loads(l)["key"] for l in f if l.strip()}


def emit(path, rec):
    with open(path, "a") as f:
        f.write(json.dumps(rec) + "\n")
        f.flush()
        os.fsync(f.fileno())


def bar(fam, a, b, m):
    te = lb.barrier(fam, a, b, m, XT, YT)
    tr = lb.barrier(fam, a, b, m, XTR, YTR)
    return {"test_loss_barrier": te["loss_barrier"], "test_err_barrier": te["err_barrier"],
            "train_loss_barrier": tr["loss_barrier"], "train_err_barrier": tr["err_barrier"],
            "test_curve": te["loss_curve"]}


def measure_pair(a, b, full_group=False):
    out = {"paths": {}}
    Xal = XTR[:2000]
    for al in ALIGNS:
        pa, pb = lb.align(al, a, b, Xal)
        out["paths"][f"{al}/linear"] = bar("linear", pa, pb, None)
        out["paths"][f"{al}/linear"]["llfc_cos"] = lb.llfc_cos(pa, pb, XT)
        for fam in CURVES:
            pm = lb.fit_curve(fam, pa, pb, XTR, YTR, seed=1)
            out["paths"][f"{al}/{fam}"] = bar(fam, pa, pb, pm)
        if al == "am":
            out["feature_corr_am"] = lb.feature_corr(pa, pb, Xal)
    if full_group:
        pa, pb = lb.full_group_search(a, b, Xal, YTR[:2000])
        out["paths"]["fullgroup/linear"] = bar("linear", pa, pb, None)
        out["paths"]["fullgroup/linear"]["llfc_cos"] = lb.llfc_cos(pa, pb, XT)
        out["feature_corr_fullgroup"] = lb.feature_corr(pa, pb, Xal)
    return out


def net(mode, h, seed, **kw):
    X, y = DATA[mode]
    return lb.train(lb.init(h, seed), X, y, seed=seed, **kw)


def e1():
    path = os.path.join(HERE, "results_e1.jsonl")
    have = done_keys(path)
    for h in (5, 8, 16, 64, 256):
        for cond in ("sameA", "sameB", "both", "diff", "twin"):
            for i in range(4):
                key = f"e1|{cond}|{h}|{i}"
                if key in have:
                    continue
                t0 = time.time()
                if cond == "twin":
                    a = net("A", h, i)
                    r = np.random.default_rng(i + 7)
                    b = lb.rescale(lb.permute(a, r.permutation(h), r.permutation(h)),
                                   np.exp(r.uniform(-1.4, 1.4, h)), np.exp(r.uniform(-1.4, 1.4, h)))
                else:
                    ma, mb = {"sameA": ("A", "A"), "sameB": ("B", "B"), "both": ("both", "both"),
                              "diff": ("A", "B")}[cond]
                    a, b = net(ma, h, i), net(mb, h, i + 50)
                rec = {"key": key, "cond": cond, "width": h, "pair": i,
                       "reliance": [lb.cue_reliance(a, TASK), lb.cue_reliance(b, TASK)],
                       "end_test": [lb.loss_err(a, XT, YT), lb.loss_err(b, XT, YT)]}
                rec.update(measure_pair(a, b, full_group=(h <= 5)))
                rec["secs"] = round(time.time() - t0, 1)
                emit(path, rec)
                print(key, rec["secs"], flush=True)


TEMPS = {"b256": dict(lr=0.02, batch=256, epochs=60), "b32": dict(lr=0.02, batch=32, epochs=30),
         "b8": dict(lr=0.02, batch=8, epochs=30)}


def e2():
    path = os.path.join(HERE, "results_e2.jsonl")
    have = done_keys(path)
    for h in (4, 6, 8, 16, 64):
        for temp, kw in TEMPS.items():
            for i in range(3):
                key = f"e2|{temp}|{h}|{i}"
                if key in have:
                    continue
                t0 = time.time()
                a, b = net("both", h, i, **kw), net("both", h, i + 50, **kw)
                rec = {"key": key, "temp": temp, "width": h, "pair": i,
                       "lam_max": [lb.top_hessian_eig(p, XTR[:2000], YTR[:2000]) for p in (a, b)],
                       "end_train": [lb.loss_err(a, XTR, YTR), lb.loss_err(b, XTR, YTR)],
                       "end_test": [lb.loss_err(a, XT, YT), lb.loss_err(b, XT, YT)]}
                rec.update(measure_pair(a, b, full_group=(h <= 4)))
                rec["secs"] = round(time.time() - t0, 1)
                emit(path, rec)
                print(key, rec["secs"], flush=True)


if __name__ == "__main__":
    {"e1": e1, "e2": e2}[sys.argv[1]]()
