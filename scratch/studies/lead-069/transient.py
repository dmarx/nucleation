"""Search small random soups for a transient block that leaves no cell behind.

CASE-260 run 1's two blocks occupy the same four cells, and two of them stay live throughout,
so on a cell-continuity criterion of token identity they are one block, damaged and repaired.
This looks for a cleaner case of creation without stabilization: an exact block with an all-dead
border that appears and whose four cells are all dead within a few generations, with no block
on those cells again in the run.

Run from this directory:  python3 -I transient.py > transient.json
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from life import run, step  # noqa: E402


def isolated_blocks(g):
    """Top-left corners of exact 2 x 2 blocks whose 12-cell border is dead (no wrap at the edges)."""
    out = []
    h, w = g.shape
    rows, cols = np.nonzero(g[1:h - 2, 1:w - 2] & g[2:h - 1, 1:w - 2] & g[1:h - 2, 2:w - 1] & g[2:h - 1, 2:w - 1])
    for r, c in zip(rows + 1, cols + 1):
        win = g[r - 1:r + 3, c - 1:c + 3]
        if win.sum() == 4:
            out.append((int(r), int(c)))
    return out


def scan(seed, size=64, soup=6, t_max=150, window=10):
    rng = np.random.default_rng(seed)
    g = np.zeros((size, size), dtype=np.int8)
    m = size // 2 - soup // 2
    g[m:m + soup, m:m + soup] = rng.integers(0, 2, (soup, soup), dtype=np.int8)
    hist = [g]
    for _ in range(t_max + window):
        hist.append(step(hist[-1]))
    found, seen = [], set()
    for t in range(t_max):
        for r, c in isolated_blocks(hist[t]):
            if (r, c) in seen:      # count each block from its first isolated appearance
                continue
            seen.add((r, c))
            cells = [(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)]
            later = [sum(int(hist[s][p]) for p in cells) for s in range(t + 1, t + window + 1)]
            if 0 not in later:
                continue
            gone = t + 1 + later.index(0)   # first generation with all four cells dead
            ever_again = any(all(hist[s][p] for p in cells) for s in range(gone, len(hist)))
            if not ever_again:
                found.append({"seed": seed, "t": t, "corner": (r - m, c - m),
                              "generations_to_all_dead": gone - t,
                              "block_cells_live_next": later})
    return found, len(seen), hist[0][m:m + soup, m:m + soup].tolist()


def main(n_seeds=300):
    events, appearances, soups = [], 0, {}
    for seed in range(n_seeds):
        found, n_seen, soup = scan(seed)
        appearances += n_seen
        events += found
        soups[seed] = soup
    shortest = min(events, key=lambda e: (e["generations_to_all_dead"], e["seed"])) if events else None
    print(json.dumps({"seeds": n_seeds,
                      "distinct_isolated_block_appearances": appearances,
                      "transient_blocks_all_cells_dead_never_back": len(events),
                      "soups_with_one": len({e["seed"] for e in events}),
                      "shortest_lived": shortest,
                      "its_soup_6x6_at_centre_of_64x64": soups[shortest["seed"]] if shortest else None},
                     indent=1))


if __name__ == "__main__":
    main()
