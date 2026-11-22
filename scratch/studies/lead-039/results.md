# LEAD-039 results

## S1: two distinct rows of p(Y|x), |Y| = 2..6, grid 1/4000, 40 betas in [1.05, 80]

- sources: 300; decoder intervals nested at every consecutive beta: 300; largest violation 0.00e+00
- by |Y|: 2: 50, 3: 68, 4: 58, 5: 66, 6: 58
- mean number of betas with a nontrivial optimum (width > 3 grid steps): 27.7 of 40

## S2: three distinct rows, |Y| = 2 or 3, grid 1/300, 16 betas in [1.5, 60]

L1 distance of the coarse decoder points from the fine hull (uncertified: optima not proved unique).

| |Y| | sources | threshold | sources failing some adjacent pair | adjacent pairs failing | sources failing a far pair (5 steps apart) | sources with no failure at all |
|---|---|---|---|---|---|---|
| 2 | 75 | 0.01 | 45 | 108/1125 | 13 | 29 |
| 2 | 75 | 0.02 | 26 | 60/1125 | 6 | 46 |
| 2 | 75 | 0.05 | 13 | 25/1125 | 2 | 61 |
| 3 | 75 | 0.01 | 41 | 84/1125 | 6 | 34 |
| 3 | 75 | 0.02 | 27 | 50/1125 | 5 | 47 |
| 3 | 75 | 0.05 | 15 | 20/1125 | 0 | 60 |

The three largest failures were recomputed on a grid of 1/700 and kept their size (0.302 -> 0.275, 0.183 -> 0.184, 0.164 -> 0.162).

## S3: products of two independent two-row pairs, 4-state grid 1/40, beta in {2, 4, 8, 16}

- items: 12 (48 source-beta pairs)
- grid envelope minus the sum of the factors' envelopes: min -2.2e-16, max 1.9e-03
  (tensorization predicts >= 0, and small at a fine enough grid)
