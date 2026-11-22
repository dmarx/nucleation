"""LEAD-043: a toy-scale run of CASE-274's forgetting study.

A 2-layer numpy transformer memorizes random subject-relation-object facts
under three query templates; a target set of facts is then fine-tuned away
by one of five methods ("arms"); the readouts below then ask whether the
fact is still there. Every model has a matched twin trained in a world
that differs only in the target facts' values, from the same
initialization on the same schedule, so that each readout's rate on the
other world's values is its false-positive baseline.

Usage: python3 -I study.py OUT.jsonl CACHE_DIR [seed ...]
Writes one JSON line per (seed, arm); skips items already written.
"""
import json
import os
import sys
import time

import numpy as np

import probes
import tinytf as tt

S_OLD, S_NEW, R, O = 64, 64, 4, 16
N_TARGET_SUBJ, TARGET_REL = 16, (0, 1)
D, HEADS, DMLP = 64, 4, 256
REL0 = S_OLD + S_NEW
QTOK = REL0 + 3 * R
VOCAB = QTOK + 1
TEMPLATES = ("A", "B", "C")
METHODS = ("unlearn", "ascent", "overwrite")
ARMS = tuple(m + c for m in METHODS for c in ("A", "AB")) + ("newtask",)
PRE_STEPS, PRE_LR, WD = 600, 3e-3, 0.01
FT_LR, FT_MAX, RL_LR, RL_MAX = 1e-3, 1500, 1e-3, 600
STAGES = ("emb", "attn0", "mlp0", "attn1", "mlp1")


def seq(s, r, t):
    rel = REL0 + TEMPLATES.index(t) * R + r
    return {"A": [s, rel, QTOK], "B": [rel, s, QTOK], "C": [rel, QTOK, s]}[t]


def make_world(seed):
    rng = np.random.default_rng(seed)
    vals = rng.integers(0, O, (S_OLD + S_NEW, R))
    tsubj = np.sort(rng.choice(S_OLD, N_TARGET_SUBJ, replace=False))
    targets = [(s, r) for s in tsubj for r in TARGET_REL]
    twin = vals.copy()
    over = vals.copy()
    for s, r in targets:
        twin[s, r] = (vals[s, r] + rng.integers(1, O)) % O
        choices = [o for o in range(O) if o not in (vals[s, r], twin[s, r])]
        over[s, r] = rng.choice(choices)
    half = rng.permutation(N_TARGET_SUBJ)
    relearn_subj = set(tsubj[half[: N_TARGET_SUBJ // 2]].tolist())
    return {"vals": {"A": vals, "B": twin}, "over": over, "tsubj": tsubj,
            "targets": targets,
            "relearn": [f for f in targets if f[0] in relearn_subj],
            "heldout": [f for f in targets if f[0] not in relearn_subj]}


def rows(facts, templates, vals):
    tok = np.array([seq(s, r, t) for s, r in facts for t in templates])
    y = np.array([vals[s, r] for s, r in facts for t in templates])
    return tok, y


def old_facts():
    return [(s, r) for s in range(S_OLD) for r in range(R)]


def pretrain_rows(w, vals):
    tset = set(w["targets"])
    allf = old_facts()
    tA, yA = rows(allf, "AB", vals)
    cf = [(s, r) for s, r in allf if s not in set(w["tsubj"].tolist())]
    tC, yC = rows(cf, "C", vals)
    return np.concatenate([tA, tC]), np.concatenate([yA, yC])


def retain_rows(w, vals):
    """Every pretraining row except the target facts' rows."""
    tset = set(w["targets"])
    keep = [f for f in old_facts() if f not in tset]
    tAB, yAB = rows(keep, "AB", vals)
    cf = [(s, r) for s, r in keep if s not in set(w["tsubj"].tolist())]
    tC, yC = rows(cf, "C", vals)
    return np.concatenate([tAB, tC]), np.concatenate([yAB, yC])


def acc(p, tok, y):
    return float((tt.predict(p, tok).argmax(1) == y).mean())


def train(p, tok, tgt, wt, lr, steps, stop=None, every=10, log=None):
    tgt, wt = tgt.astype(np.float32), wt.astype(np.float32)
    opt = tt.Adam(p, lr, wd=WD)
    for i in range(1, steps + 1):
        lg, c = tt.forward(p, tok)
        _, d = tt.loss_grad(lg, tgt, wt)
        opt.step(p, tt.backward(p, c, d))
        if log is not None and i % every == 0:
            log(i, p)
        if stop is not None and i % every == 0 and stop(p):
            return i
    return steps


def pretrain(seed, w, world, cache):
    path = os.path.join(cache, f"pre_s{seed}_{world}.npz")
    if os.path.exists(path):
        z = np.load(path)
        return {k: z[k] for k in z.files}
    p = tt.init_params(np.random.default_rng(1000 + seed), VOCAB, 3, D, HEADS, DMLP, O)
    p = {k: (v if k == "_meta" else v.astype(np.float32)) for k, v in p.items()}
    tok, y = pretrain_rows(w, w["vals"][world])
    train(p, tok, np.eye(O)[y], np.ones(len(y)), PRE_LR, PRE_STEPS)
    np.savez(path, **p)
    return p


def arm_batch(arm, w, world):
    vals = w["vals"][world]
    T = w["targets"]
    rt, ry = retain_rows(w, vals)
    if arm == "newtask":
        newf = [(s, r) for s in range(S_OLD, S_OLD + S_NEW) for r in range(R)]
        tok, y = rows(newf, "AB", vals)
        return tok, np.eye(O)[y], np.ones(len(y)), (tok, y), "AB"
    cues = "AB" if arm.endswith("AB") else "A"
    ft, fy = rows(T, cues, vals)
    if arm.startswith("unlearn"):
        ftg, fw = np.full((len(fy), O), 1.0 / O), np.ones(len(fy))
    elif arm.startswith("ascent"):
        ftg, fw = np.eye(O)[fy], -np.ones(len(fy))
    else:
        _, oy = rows(T, cues, w["over"])
        ftg, fw = np.eye(O)[oy], np.ones(len(fy))
    fw = fw / len(fy)
    rw = np.ones(len(ry)) / len(ry)
    tok = np.concatenate([ft, rt])
    tgt = np.concatenate([ftg, np.eye(O)[ry]])
    wt = np.concatenate([fw, rw])
    return tok, tgt, wt, (ft, fy), cues


def finetune(p0, arm, w, world):
    p = tt.copy_params(p0)
    tok, tgt, wt, (ft, fy), cues = arm_batch(arm, w, world)
    if arm == "newtask":
        stop = lambda q: acc(q, ft, fy) >= 0.99
    elif arm.startswith("overwrite"):
        _, oy = rows(w["targets"], cues, w["over"])
        stop = lambda q: acc(q, ft, oy) >= 1.0
    else:
        stop = lambda q: acc(q, ft, fy) <= 1.0 / O
    steps = train(p, tok, tgt, wt, FT_LR, FT_MAX, stop=stop)
    return p, steps, cues


def readouts(p, p0, w, own, other, retain_world):
    """Per-target-fact readouts of the fine-tuned model p against the value
    tables own (its world) and other (the twin's world)."""
    T = w["targets"]
    out = {}
    lg = {t: tt.predict(p, rows(T, t, own)[0]) for t in TEMPLATES}
    pr = {t: tt.softmax(lg[t]) for t in TEMPLATES}
    tokA = rows(T, "A", own)[0]
    _, cache = tt.forward(p, tokA)
    # probes fitted on retained old facts under template A, labels shared by both worlds
    keep = [f for f in old_facts() if f not in set(T)]
    ktok, ky = rows(keep, "A", retain_world)
    _, kc = tt.forward(p, ktok)
    lin, mlp, lens = [], [], []
    for i, st in enumerate(STAGES):
        lens.append((cache["resid"][i] @ p["Wu"] + p["bu"]).argmax(1))
        if st == "emb":  # constant at the query position: nothing to read
            lin.append(np.full(len(T), -1))
            mlp.append(np.full(len(T), -1))
            continue
        lp = probes.fit_linear(kc["resid"][i], ky, O)
        mp = probes.fit_mlp(kc["resid"][i], ky, O, hidden=128, steps=800, seed=i)
        lin.append(probes.predict(lp, cache["resid"][i]).argmax(1))
        mlp.append(probes.predict(mp, cache["resid"][i]).argmax(1))
    # weight-delta reversion
    rev = {}
    sets = {b: (b,) for b in tt.BLOCKS}
    for k in range(1, len(tt.BLOCKS)):
        sets["from_" + tt.BLOCKS[k]] = tt.BLOCKS[k:]
    for name, blocks in sets.items():
        q = {k: (p0[k] if k != "_meta" and tt.block_of(k) in blocks else v) for k, v in p.items()}
        rev[name] = tt.predict(q, tokA).argmax(1)
    for tag, vals in (("own", own), ("other", other)):
        v = np.array([vals[s, r] for s, r in T])
        top = lg["A"].argmax(1)
        masked = lg["A"].copy()
        masked[np.arange(len(T)), top] = -np.inf
        out[tag] = {
            "cue": {t: (lg[t].argmax(1) == v).astype(int).tolist() for t in TEMPLATES},
            "p": {t: pr[t][np.arange(len(T)), v].round(5).tolist() for t in TEMPLATES},
            "second": (masked.argmax(1) == v).astype(int).tolist(),
            "lens": [(x == v).astype(int).tolist() for x in lens],
            "lin": [(x == v).astype(int).tolist() for x in lin],
            "mlp": [(x == v).astype(int).tolist() for x in mlp],
            "revert": {k: (x == v).astype(int).tolist() for k, x in rev.items()},
        }
    return out


def relearn(p_ft, arm, w, world, values, cues):
    """Relearn the relearn half of the targets at the forgotten cues, with the
    value table `values`, rehearsing the arm's retain rows. Returns steps to
    criterion and the held-out half's accuracy trajectory at A and B."""
    p = tt.copy_params(p_ft)
    rt_tok, rt_y = rows(w["relearn"], cues, values)
    if arm == "newtask":
        newf = [(s, r) for s in range(S_OLD, S_OLD + S_NEW) for r in range(R)]
        kt, ky = rows(newf, "AB", w["vals"][world])
    else:
        kt, ky = retain_rows(w, w["vals"][world])
    tok = np.concatenate([rt_tok, kt])
    tgt = np.eye(O)[np.concatenate([rt_y, ky])]
    wt = np.concatenate([np.ones(len(rt_y)) / len(rt_y), np.ones(len(ky)) / len(ky)])
    hA = rows(w["heldout"], "A", values)
    hB = rows(w["heldout"], "B", values)
    rA = rows(w["relearn"], "A", values)
    traj = []

    def log(i, q):
        traj.append([i, acc(q, *rA), acc(q, *hA), acc(q, *hB)])

    log(0, p)
    steps = train(p, tok, tgt, wt, RL_LR, RL_MAX, stop=lambda q: acc(q, rt_tok, rt_y) >= 1.0,
                  every=5, log=log)
    return {"steps": steps, "traj": traj}


def run_item(seed, arm, cache):
    w = make_world(seed)
    pre = {wd: pretrain(seed, w, wd, cache) for wd in "AB"}
    rec = {"seed": seed, "arm": arm, "pre": {}, "post": {}, "relearn": {}, "ft_steps": {}}
    for wd in "AB":
        own, other = w["vals"][wd], w["vals"]["B" if wd == "A" else "A"]
        rec["pre"][wd] = {
            "train_acc": acc(pre[wd], *pretrain_rows(w, own)),
            "target": {t: acc(pre[wd], *rows(w["targets"], t, own)) for t in TEMPLATES},
        }
        p, steps, cues = finetune(pre[wd], arm, w, wd)
        rec["ft_steps"][wd] = steps
        rec["cues"] = cues
        keep = [f for f in old_facts() if f not in set(w["targets"])]
        rec["post"][wd] = readouts(p, pre[wd], w, own, other, own)
        rec["post"][wd]["retain_acc"] = {t: acc(p, *rows(keep, t, own)) for t in "AB"}
        rec["post"][wd]["all_old_acc_A"] = acc(p, *rows(old_facts(), "A", own))
        rec["relearn"][wd] = {"own": relearn(p, arm, w, wd, own, cues),
                              "other": relearn(p, arm, w, wd, other, cues)}
    return rec


def main():
    out, cache = sys.argv[1], sys.argv[2]
    seeds = [int(s) for s in sys.argv[3:]] or [0, 1, 2, 3, 4]
    os.makedirs(cache, exist_ok=True)
    done = set()
    if os.path.exists(out):
        for line in open(out):
            r = json.loads(line)
            done.add((r["seed"], r["arm"]))
    for seed in seeds:
        for arm in ARMS:
            if (seed, arm) in done:
                continue
            t0 = time.time()
            rec = run_item(seed, arm, cache)
            rec["secs"] = round(time.time() - t0, 1)
            with open(out, "a") as f:
                f.write(json.dumps(rec) + "\n")
            print(seed, arm, rec["secs"], rec["ft_steps"], flush=True)


if __name__ == "__main__":
    main()
