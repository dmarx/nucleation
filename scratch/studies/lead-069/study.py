"""LEAD-069: apply the record's individuation criteria to the Life block and eater.

Run from this directory:  python3 -I study.py > results.json   (a minute or two)
"""
import itertools
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # python3 -I drops the script dir
from life import (BLOCK, EATER, GLIDER_SE, GUN, GUN_LEFT_BLOCK, GUN_RIGHT_BLOCK,
                  board, cells_of, chebyshev, place, ring, run, step)

N = 48          # torus for lone forms
OFF = (20, 20)  # where the lone form sits


def shifted(cells, off=OFF):
    return {(r + off[0], c + off[1]) for r, c in cells}


def outcome(form, flips, t=200):
    """Flip the given cells of the lone form's board; classify what is left after t generations."""
    g = board((N, N), form, OFF)
    for r, c in flips:
        g[r % N, c % N] ^= 1
    live = cells_of(run(g, t))
    target = shifted(form)
    if live == target:
        return "returns"
    if not live:
        return "empty"
    if target <= live:
        return "form-kept-with-debris"
    return "form-lost"


def perturbation_profile(form):
    """Single-cell flips of every cell of the form (distance 0) and of every cell within 3 of it."""
    target = shifted(form)
    res = {}
    for p in sorted(target | ring(target, 3)):
        d = 0 if p in target else chebyshev(p, target)
        o = outcome(form, [p])
        res.setdefault(d, {}).setdefault(o, 0)
        res[d][o] += 1
    return res


def pair_deletions(form):
    out = {}
    for a, b in itertools.combinations(sorted(shifted(form)), 2):
        o = outcome(form, [a, b])
        out[o] = out.get(o, 0) + 1
    return out


def sensitivity(g, sources, targets, k):
    """Fraction of pairs (source j, target i), i != j, for which flipping j at t changes i at t+k."""
    base = run(g, k)
    hits = tot = 0
    for j in sources:
        h = g.copy()
        h[j] ^= 1
        diff = run(h, k) != base
        for i in targets:
            if i == j:
                continue
            tot += 1
            hits += int(diff[i])
    return hits / tot if tot else float("nan")


def gap_profile(form, ks=(1, 2, 5, 10)):
    """Coupling inside the lone form and across its edge at its fixed point, as k-step sensitivity."""
    g = board((N, N), form, OFF)
    inside = sorted(shifted(form))
    border = sorted(ring(shifted(form), 1))
    return {k: {"inside": sensitivity(g, inside, inside, k),
                "border_to_form": sensitivity(g, border, inside, k),
                "form_to_border": sensitivity(g, inside, border, k)} for k in ks}


def eater_strike_lanes():
    """CASE-259's strike in lanes -3..+3, and the eating lane with all four glider phases."""
    res = {}
    for lane in range(-3, 4):
        g = np.zeros((64, 64), dtype=np.int8)
        place(g, GLIDER_SE)
        place(g, EATER, (12 + lane, 12 - lane))
        live = cells_of(run(g, 200))
        target = {(r + 12 + lane, c + 12 - lane) for r, c in EATER}
        if live == target:
            res[lane] = "eater-exact"
        elif not live:
            res[lane] = "empty"
        else:
            kept = "eater-kept" if target <= live else "eater-lost"
            res[lane] = f"{kept}, {len(live - target)} other cells"
    phases = []
    for ph in range(4):
        g = run(board((64, 64), GLIDER_SE), ph)
        place(g, EATER, (12, 12))
        phases.append(cells_of(run(g, 200)) == {(r + 12, c + 12) for r, c in EATER})
    return res, phases


def strike_timeline(t0=33, t1=40):
    g = board((64, 64), GLIDER_SE)
    place(g, EATER, (12, 12))
    target = {(r + 12, c + 12) for r, c in EATER}
    rows = []
    for t in range(t1):
        if t >= t0:
            live = cells_of(g)
            rows.append({"t": t, "form_cells_live": len(target & live),
                         "other_live": len(live - target)})
        g = step(g)
    return rows


def gun_board(eater=False, shape=(160, 160)):
    g = board(shape, GUN, (10, 10))
    if eater:
        place(g, EATER, (10 + 30, 10 + 44))
    return g


def gliders_away(t, shape=(200, 200)):
    """Gliders that have left the gun by time t: 5-cell components wholly below or right of its box."""
    from scipy.ndimage import label
    g = run(gun_board(shape=shape), t)
    lab, n = label(g, structure=np.ones((3, 3)))
    count = 0
    for k in range(1, n + 1):
        cells = np.argwhere(lab == k)
        if len(cells) == 5 and ((cells[:, 0] > 10 + 12).all() or (cells[:, 1] > 10 + 38).all()):
            count += 1
    return count


CREATION_GLIDERS = [(0, 5), (1, 3), (1, 4), (2, 4), (2, 5), (4, 1), (5, 2), (6, 0), (6, 1), (6, 2)]
CREATION_BLOCK = {(6, 1), (6, 2), (7, 1), (7, 2)}   # where both of CASE-260's blocks appear


def creation_run(t_max=30, off=(30, 30)):
    """CASE-260 run 1: per generation, which of the block's four cells are live, and how many of its
    border cells, so that the t = 20 block and the lasting block can be compared cell by cell."""
    g = board((80, 80), CREATION_GLIDERS, off)
    cells = shifted(CREATION_BLOCK, off)
    border = ring(cells, 1)
    rows = []
    for t in range(t_max):
        live = cells_of(g)
        if t >= 18:
            rows.append({"t": t,
                         "block_cells_live": sorted((r - off[0], c - off[1]) for r, c in cells & live),
                         "border_live": len(border & live), "total_live": len(live)})
        g = step(g)
    final = cells_of(run(g, 300 - t_max))
    return rows, final == cells


def gun_block_continuity(block, t_max=300):
    """Minimum number of a gun block's cells alive over the run, and the most border cells alive."""
    g = gun_board()
    cells = shifted(block, (10, 10))
    border = ring(cells, 1)
    mins, border_live = 4, 0
    for _ in range(t_max):
        live = cells_of(g)
        mins = min(mins, len(cells & live))
        border_live = max(border_live, len(border & live))
        g = step(g)
    return {"min_block_cells_live": mins, "max_border_cells_live": border_live}


def gun_gap(block, period=(60, 90)):
    """One-step sensitivity inside a gun block and across its edge, averaged over one gun period."""
    g = run(gun_board(), period[0])
    cells = sorted(shifted(block, (10, 10)))
    border = sorted(ring(set(cells), 1))
    acc = {"inside": [], "border_to_form": [], "form_to_border": []}
    for _ in range(*period):
        acc["inside"].append(sensitivity(g, cells, cells, 1))
        acc["border_to_form"].append(sensitivity(g, border, cells, 1))
        acc["form_to_border"].append(sensitivity(g, cells, border, 1))
        g = step(g)
    return {k: float(np.mean(v)) for k, v in acc.items()}


def gun_eater_continuity(t0=300, t1=600):
    g = run(gun_board(eater=True), t0)
    cells = shifted(EATER, (40, 54))
    mins = 7
    for _ in range(t0, t1):
        mins = min(mins, len(cells & cells_of(g)))
        g = step(g)
    return mins


def main():
    out = {}
    for name, form in (("block", BLOCK), ("eater", EATER)):
        g = board((N, N), form, OFF)
        out[name] = {
            "fixed_point_1000": bool((run(g, 1000) == g).all()),
            "single_flip_profile_by_distance": perturbation_profile(form),
            "pair_deletions": pair_deletions(form),
            "gap_profile": gap_profile(form),
        }
    lanes, phases = eater_strike_lanes()
    out["eater"]["strike_lanes"] = lanes
    out["eater"]["strike_phases_exact"] = phases
    out["eater"]["strike_timeline"] = strike_timeline()
    rows, lasting = creation_run()
    out["creation_run"] = {"rows": rows, "only_the_block_at_t300": lasting}
    out["gun"] = {
        "gliders_away_t100_200_300_400": [gliders_away(t) for t in (100, 200, 300, 400)],
        "left_block": gun_block_continuity(GUN_LEFT_BLOCK),
        "right_block": gun_block_continuity(GUN_RIGHT_BLOCK),
        "left_block_gap_over_period": gun_gap(GUN_LEFT_BLOCK),
        "right_block_gap_over_period": gun_gap(GUN_RIGHT_BLOCK),
        "eater_min_live_cells_t300_600": gun_eater_continuity(),
    }
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
