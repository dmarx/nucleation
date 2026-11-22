# LEAD-069: does the record individuate the Life block and eater?

Computations behind the study case and claims filed for LEAD-069
(2026-11-22). Conway's Game of Life, B3/S23, on a torus big enough that
nothing wraps in the runs used. NumPy only (SciPy for one component count).

## Files

- `life.py`: the rule, the patterns (block, eater 1, glider, Gosper's gun
  in the frame of CASE-260 and CASE-259), helpers.
- `study.py`: the criterion-by-criterion checks. Writes `results.json`.
  - lone block and lone eater: fixed point over 1,000 generations;
    every single-cell flip of the form and of every cell within Chebyshev
    distance 3 of it, classified after 200 generations (`returns` = the
    lattice is exactly the form again); every pair of deletions;
  - coupling inside the form and across its edge, read as k-step
    sensitivity: the fraction of ordered pairs (j, i), i != j, for which
    flipping cell j changes cell i k generations later (k = 1, 2, 5, 10),
    for j and i in the form ("inside"), j on the one-cell border and i in
    the form, and the reverse;
  - the eater struck by a glider in its eating lane (all four phases) and
    with the eater shifted 1 to 3 cells across the glider's path;
  - CASE-260 run 1 cell by cell: which of the block's four cells are live
    at t = 18 to 29;
  - Gosper's gun: gliders away at t = 100 to 400, the fewest of each
    block's cells live in 300 generations, the same coupling read over
    one period (t = 60 to 89); the eater across the stream, its fewest
    live cells over t = 300 to 600.
- `transient.py`: 300 random 6 x 6 soups (seeds 0 to 299, density 1/2)
  on a 64 x 64 torus, 150 generations: exact blocks with an all-dead
  border, counted once per position from their first such appearance, and
  those whose four cells are all dead within 10 generations and never all
  live again in the run. Writes `transient.json`.
- `test_study.py`: pytest for the rule, the helpers and the main results.

## Rerun

    cd scratch/studies/lead-069
    python3 -I study.py > results.json        # about 5 s
    python3 -I transient.py > transient.json  # about 10 s
    python3 -m pytest -q -p no:cacheprovider test_study.py

## Results in brief

| | block | eater |
|---|---|---|
| fixed point alone | yes | yes |
| single deletion of its own cells, returns | 4 of 4 | 0 of 7 |
| single birth on the border (distance 1), returns | 0 of 12 | 0 of 21 |
| single birth at distance 2, returns | 4 of 20 | 11 of 28 |
| single birth at distance 3, returns | 28 of 28 | 36 of 36 |
| pair deletions, returns | 0 of 6 | 0 of 21 |
| glider strike in its own lane, returns | (annihilated, CASE-259) | 4 of 4 phases |
| inside / border-to-form coupling, k = 1 | 0 / 0.42 | 0.24 / 0.07 |
| inside / border-to-form coupling, k = 5 | 0 / 0.75 | 0.52 / 0.55 |
| in the gun, over one period, k = 1 | 0.06 / 0.38 | |
| fewest own cells live in its role | 2 of 4 (gun) | 6 of 7 (across the stream) |

CASE-260 run 1: the block at t = 20 and the block that lasts occupy the
same four cells, and two of them, (6,1) and (6,2), are live at every
generation from t = 19 to 29. Soups: of 1,263 isolated block appearances,
540 lose all four cells and never return (149 of the 300 soups); in
seed 1 an isolated block at t = 28 has all four cells live at t = 29 and
none at t = 30.

Gliders away from the gun at t = 100 / 200 / 300 / 400: 2 / 6 / 9 / 12 by
this script's box (CASE-260 has 2 / 5 / 9 / 12; the difference at t = 200 is
a glider at the box edge). Eater offsets across the glider's path: -3 is a
miss (the glider passes), -2 and +2 leave debris without the eater, -1, +1
and +3 leave an empty lattice. The offsets are not CASE-259's lanes.
