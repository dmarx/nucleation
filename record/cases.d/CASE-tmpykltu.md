---
status: Proposed
title: 'Cluster sizes in two-dimensional site percolation and final sizes of a small Reed–Frost epidemic, below and above their thresholds'
version: 1
standing: stipulated
kind: construction
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  Two simulations run with python3 -I in this session to check the
  owner's bulk-and-tail conjecture (CLAIM-tmpr9au6, U5 of the exchange
  "Rich Get Richer Power Laws") in its gap reading. In 2D site percolation
  on a 2,000 × 2,000 lattice, the cluster-size histogram has no gap at
  p = 0.50, 0.55 or 0.58 and a wide one at 0.62 and 0.65, where one
  cluster holds over half the sites. In a Reed–Frost epidemic of 1,000,
  final sizes are unimodal at R0 = 0.8 and 1.0 and split into minor and
  major outbreaks at 1.5 and 2. Stipulated models, one seeded run each.
  The construction is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpr9au6 CLAIM-tmpvrbdt — Proposed or new; the owner's conjecture and the reading this case checks -->

# CASE-tmpykltu: Cluster sizes in two-dimensional site percolation and final sizes of a small Reed–Frost epidemic, below and above their thresholds

## Percolation

Each site of a 2,000 × 2,000 square lattice is occupied with probability
p. Clusters are nearest-neighbour components (`scipy.ndimage.label`), seed
20261121. Sizes are binned in 40 logarithmic bins from 1 to 4 × 10⁶.
The infinite-lattice threshold is p_c ≈ 0.5927, the value A gives at A5 §2.

| p | clusters | largest | share of sites | second | largest / second | empty bins between occupied ones |
|---|---:|---:|---:|---:|---:|---|
| 0.50 | 264,099 | 754 | 0.0002 | 645 | 1.2 | none |
| 0.55 | 175,530 | 3,438 | 0.001 | 2,951 | 1.2 | none |
| 0.58 | 128,169 | 46,412 | 0.012 | 32,087 | 1.4 | none |
| 0.5927 | 110,755 | 672,002 | 0.168 | 346,813 | 1.9 | a few, among the largest clusters |
| 0.62 | 81,513 | 2,205,860 | 0.551 | 1,385 | 1,593 | every bin from about 1,650 to 2.2 × 10⁶ |
| 0.65 | 56,829 | 2,464,540 | 0.616 | 202 | 12,201 | every bin from about 230 to 2.5 × 10⁶ |

Below p_c the number of clusters per site falls over every occupied bin.
At p_c on a finite lattice, the few largest clusters are spread out over
sizes up to the system's limit. Above it, the giant cluster stands alone.

## Epidemic

Reed–Frost chain-binomial SIR among N = 1,000 with one initial case: each
susceptible escapes each infective with probability 1 − R0/N per
generation. 20,000 runs per R0. Counts of final size:

| final size | R0 = 0.8 | 1.0 | 1.5 | 2.0 |
|---|---:|---:|---:|---:|
| 1 | 8,957 | 7,350 | 4,391 | 2,628 |
| 2–9 | 8,709 | 7,518 | 3,638 | 1,364 |
| 10–49 | 2,209 | 3,140 | 394 | 17 |
| 50–199 | 125 | 1,800 | 5 | 0 |
| 200–399 | 0 | 192 | 4 | 0 |
| 400–699 | 0 | 0 | 11,562 | 0 |
| 700–899 | 0 | 0 | 6 | 15,991 |

The major-outbreak peaks sit at the final-size equation's
z = 1 − e^(−R0 z): 583 at R0 = 1.5 and 797 at R0 = 2.

## The check

```python
import numpy as np; from scipy import ndimage
rng = np.random.default_rng(20261121); L = 2000
for p in [0.50, 0.55, 0.58, 0.5927, 0.62, 0.65]:
    lab, n = ndimage.label(rng.random((L, L)) < p)
    sizes = np.sort(np.bincount(lab.ravel())[1:])
    print(p, n, sizes[-1], sizes[-2])
N, runs = 1000, 20000
for R0 in [0.8, 1.0, 1.5, 2.0]:
    S = np.full(runs, N-1); I = np.ones(runs, int); tot = I.copy()
    while I.max() > 0:
        I = rng.binomial(S, 1 - (1 - R0/N)**I); S -= I; tot += I
    print(R0, np.histogram(tot, [1,2,10,50,200,400,700,900,1001])[0])
```

The snippet reproduces both tables exactly.

## What it cannot show

One lattice size and one population size. It does not show how the gap
scales with N, or how a finite system piles up mass at its size limit
near criticality. It shows only that the gap is a far-side feature in
these two models.
