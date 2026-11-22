"""Driver for LEAD-140 (CASE-255 on CASE-186's organization).

    python3 -I study.py lineages    # phase 1: 6 arms x 12 lineages, G = 60
    python3 -I study.py transplant  # phase 2: the 2x2 and the inheritance arms
    python3 -I study.py damage      # phase 3: lesions of the improver
    python3 -I study.py all

Each item's result is appended as one JSON line to results/<phase>.jsonl as
soon as it is produced; a rerun skips items already written. Phases 2 and 3
read phase 1's lineages. Two worker processes (the machine is shared).
"""
import json
import os
import sys
import time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rsi  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
N_LINEAGES = 12
G = 60
H = 10
REPS = 2
PROCS = 2


def path(phase):
    return os.path.join(RES, phase + ".jsonl")


def done(phase):
    p = path(phase)
    if not os.path.exists(p):
        return {}
    out = {}
    with open(p) as f:
        for line in f:
            line = line.strip()
            if line:
                r = json.loads(line)
                out[r["key"]] = r
    return out


def rnd(archive_dump):
    return [[m, [round(x, 5) for x in v]] for m, v in archive_dump]


# ------------------------------------------------------------ phase 1
def do_lineage(item):
    arm, seed = item
    t = time.time()
    L = rsi.lineage(arm, seed, G=G)
    L["archive"] = rnd(L["archive"])
    L["key"] = f"{arm}|{seed}"
    L["battery"] = rsi.battery(L["theta"])
    L["secs"] = round(time.time() - t, 1)
    return L


def items_lineages():
    return [(a, s) for a in rsi.ARMS for s in range(N_LINEAGES)]


# ------------------------------------------------------------ phase 2
def start_phi(arm):
    return (0, 1, 1, 1, 1) if arm == "archive" else rsi.PHI0


def improvers(L):
    arm = L["arm"]
    p0, pG = start_phi(arm), tuple(L["phi"])
    aG = L["archive"]
    return {"early": (p0, []), "late": (pG, aG),
            "knowledge": (p0, aG), "organization": (pG, [])}


def items_transplant(lins):
    out = [("theta0",)]
    for k in sorted(lins):
        for rep in range(REPS):
            for art, imp in (("orig", "early"), ("orig", "late"),
                             ("orig", "knowledge"), ("orig", "organization"),
                             ("improved", "early"), ("improved", "late")):
                out.append((k, art, imp, rep))
    return out


def do_transplant(item, lins):
    t = time.time()
    if item == ("theta0",):
        return {"key": "theta0", "battery": rsi.battery(rsi.THETA0)}
    k, art, imp, rep = item
    L = lins[k]
    theta = rsi.THETA0 if art == "orig" else tuple(L["theta"])
    phi, ar = improvers(L)[imp]
    seed = 10_000 + 100 * L["seed"] + rep   # same seed for every improver
    th, fl, ni, no = rsi.improve(theta, phi, ar, H, seed, arm=L["arm"])
    return {"key": f"{k}|{art}|{imp}|{rep}", "arm": L["arm"],
            "lineage": L["seed"], "artifact": art, "improver": imp, "rep": rep,
            "theta": list(th), "flagged_at": fl, "inner_eps": ni,
            "outer_eps": no, "battery": rsi.battery(th),
            "secs": round(time.time() - t, 1)}


# ------------------------------------------------------------ phase 3
DAMAGE = ("sham", "generate", "admit", "score", "obsolete",
          "generate_nocanary", "admit_nocanary")


def items_damage(lins):
    return [(k, d) for k in sorted(lins) for d in DAMAGE]


def do_damage(item, lins):
    t = time.time()
    k, d = item
    L = lins[k]
    phi = tuple(L["phi"])
    lesion = d
    if d.endswith("_nocanary"):
        lesion = d.split("_")[0]
        phi = phi[:4] + (0,)
    seed = 20_000 + 100 * L["seed"]
    th, fl, ni, no = rsi.improve(tuple(L["theta"]), phi, L["archive"], H, seed,
                                 lesion=lesion, arm=L["arm"])
    return {"key": f"{k}|{d}", "arm": L["arm"], "lineage": L["seed"],
            "damage": d, "theta": list(th), "flagged_at": fl,
            "inner_eps": ni, "outer_eps": no, "battery": rsi.battery(th),
            "secs": round(time.time() - t, 1)}


# ------------------------------------------------------------ runner
_LINS = None


def _init(lins):
    global _LINS
    _LINS = lins


def _t(item):
    return do_transplant(item, _LINS)


def _d(item):
    return do_damage(item, _LINS)


def run_phase(phase):
    os.makedirs(RES, exist_ok=True)
    have = done(phase)
    lins = done("lineages") if phase != "lineages" else None
    if phase == "lineages":
        items, fn, key = items_lineages(), do_lineage, lambda i: f"{i[0]}|{i[1]}"
    elif phase == "transplant":
        items, fn = items_transplant(lins), _t
        key = lambda i: "theta0" if i == ("theta0",) else "|".join(map(str, i))  # noqa: E731
    else:
        items, fn, key = items_damage(lins), _d, lambda i: f"{i[0]}|{i[1]}"
    todo = [i for i in items if key(i) not in have]
    print(f"{phase}: {len(todo)} of {len(items)} to run", flush=True)
    t0 = time.time()
    with Pool(PROCS, initializer=_init, initargs=(lins,)) as pool, \
            open(path(phase), "a") as f:
        for n, r in enumerate(pool.imap_unordered(fn, todo), 1):
            f.write(json.dumps(r) + "\n")
            f.flush()
            if n % 10 == 0 or n == len(todo):
                print(f"{phase}: {n}/{len(todo)} in {time.time() - t0:.0f}s",
                      flush=True)


if __name__ == "__main__":
    which = sys.argv[1]
    for ph in (("lineages", "transplant", "damage") if which == "all" else (which,)):
        run_phase(ph)
