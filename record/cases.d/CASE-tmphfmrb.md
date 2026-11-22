---
status: Proposed
title: 'Small numpy MLPs aligned by permutation and measured on three path families: the barrier left after alignment falls with width whatever the mechanism, so at narrow width pairs that rely on the same cue keep a barrier even under an exhaustive search of the full group, at width 64 and above pairs that rely on different cues are connected, an exact copy rescaled per unit keeps a barrier under permutations alone, and in a flat, poorly connected grid cell a trained curve removes the barrier the aligned straight line keeps'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-157 as a delegated
    lead worker. Code, per-pair results and a rerun recipe are committed
    under scratch/studies/lead-157/.
standing: documented
kind: executed-study
tags:
- loss-landscapes
- representation-learning
date: '2026-11-22'
line:
- learned-structure
- pragmatic-transport
bears_on:
- QUESTION-069
draws_on:
- THEORY-112
- THEORY-116
- THEORY-111
- THEORY-108
- THEORY-109
- THEORY-113
summary: >-
  LEAD-157's design run at toy scale on CPU. Two-hidden-layer ReLU MLPs are
  trained in numpy on a task with two redundant cues, A and B. A test that
  uses no barrier says which cue each net relies on: its accuracy when only
  A, or only B, carries the label. Pairs are aligned four ways (none,
  weight matching, activation matching, and rescaling quotiented before
  weight matching), and at width 5 by an exhaustive search over permutations
  plus optimised rescaling. The barrier is then measured on the straight
  line, a trained Bezier curve and a trained one-bend polychain. The
  aligned linear barrier falls with width for every kind of pair. At width
  5, three of four pairs that both rely on cue A keep a loss barrier of
  0.09 to 0.25 after the exhaustive search, about as much as pairs relying
  on different cues (0.15 to 0.54). At widths 64 and 256 an A-net and a
  B-net are connected after activation matching (0.000). A copy of a net,
  permuted and rescaled per unit, computes exactly the same function, yet
  permutation alignment alone leaves it a barrier of 0.19 to 0.59. In a
  load-by-temperature grid, one cell is flat and poorly connected without
  alignment. There, alignment plus a trained curve removes the barrier,
  while the aligned straight line keeps 0.07 error, and the cell's accuracy
  deficit stays. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-263 CLAIM-187 THEORY-116 THEORY-108 THEORY-109 CLAIM-142 — Proposed; the claims this study tests, the readings it draws on, and the probe caution, open -->
<!-- inactive-ok-file: CLAIM-tmpr7v4j CLAIM-tmpv22hv CLAIM-tmp46m6e — new; the finding and the two alternative readings filed with this study -->

# CASE-tmphfmrb: Small numpy MLPs aligned by permutation and measured on three path families: the barrier left after alignment falls with width whatever the mechanism, so at narrow width pairs that rely on the same cue keep a barrier even under an exhaustive search of the full group, at width 64 and above pairs that rely on different cues are connected, an exact copy rescaled per unit keeps a barrier under permutations alone, and in a flat, poorly connected grid cell a trained curve removes the barrier the aligned straight line keeps

## What was done

LEAD-157 asks for the barrier between permutation-aligned networks on
several path families, and for a pair known to share a mechanism, tested
for whether alignment always removes its barrier (QUESTION-069's "what
would answer it"). Only a CPU and numpy were available, so this is a
**toy-scale stand-in**. The networks are two-hidden-layer ReLU MLPs with
hand-written backpropagation, not image classifiers or transformers.

- **Task.** Four classes and 16 inputs. Cue A (inputs 0–3) and cue B
  (inputs 4–7) each place an example near one of three Gaussian centres
  of its class. The other inputs are noise. In `both` both cues carry the
  label; in `A`, cue B is drawn from a random class; in `B`, cue A is.
- **Mechanism test, independent of any barrier.** A net's accuracy when only
  cue A carries the label and when only cue B does. A-trained nets score
  0.87–0.91 on A-only and chance (0.25) on B-only. B-trained nets score the
  reverse (0.93–0.97). So a pair of A-nets shares "the input attributes
  relied on" (CLAIM-263's defeater). An A-net and a B-net do not.
- **Pairs (experiment e1; 4 pairs a cell; widths 5, 8, 16, 64, 256).**
  `sameA`, `sameB`: two seeds on the same single-cue data. `both`: two seeds
  on `both` (their mechanism is measured, not built: each leans on B, 0.76
  against 0.37). `diff`: an A-net and a B-net. `twin`: an A-net and a copy
  of it permuted and rescaled per unit by factors in [e^-1.4, e^1.4], which
  is the same function exactly.
- **Alignment.** None; weight matching (Git Re-Basin's coordinate descent);
  activation matching (correlation of post-ReLU activations); `swm`, each
  unit's incoming weights normalised to quotient ReLU rescaling, then
  weight matching. At width 5, "full group" is the best of all 14,400
  permutation pairs for the mean loss at t = ¼, ½, ¾, followed by
  per-unit rescaling optimised by L-BFGS, starting from both raw and
  normalised weights.
- **Path families.** The straight line, a quadratic Bezier curve with a
  trained control point, and a one-bend polychain with a trained bend
  (THEORY-109's families), each run on the unaligned and the aligned
  endpoints.
- **Barrier.** The largest excess, over 25 points, of the path's loss above
  the straight interpolation of the endpoint losses. It is measured in
  cross-entropy and in 0-1 error, on a held-out both-cue set, which every
  net in every pair fits.
- **Load by temperature (experiment e2).** A small analogue of THEORY-108's
  grid: widths 4–64 against batch sizes 256, 32 and 8 at one learning rate,
  three pairs a cell, all on `both`. Flatness is the top Hessian
  eigenvalue. The classification was fixed before reading the results:
  "flat" means below the grid median of the cell means, and "poorly
  connected" means an unaligned Bezier barrier of at least 0.02 in
  training error, which is Yang et al.'s measure.

## Results (mean test loss barrier; error barrier in brackets)

| pair | width | unaligned line | best permutation-aligned line | aligned Bezier |
|---|---|---|---|---|
| sameA | 5 | 2.13 (0.57) | 0.13 (0.08), exhaustive search | 0.000 |
| sameA | 8 / 16 | 1.76 / 2.16 | 0.14 / 0.06 (wm) | 0.000 |
| sameA | 64 / 256 | 1.35 / 0.75 | 0.000 / 0.000 | 0.000 |
| sameB | 5 | 2.15 (0.59) | 0.28 (0.12), exhaustive search | 0.023 |
| diff | 5 | 1.79 (0.47) | 0.35 (0.15), exhaustive search | 0.035 |
| diff | 8 / 16 | 1.87 / 1.24 | 0.40 / 0.32 (am) | 0.000 |
| diff | 64 / 256 | 0.47 / 0.41 | 0.000 / 0.000 (am) | 0.000 |
| twin | 5–256 | 1.2–5.8 | 0.19–0.59 (am, wm); 0.000 once rescaling is quotiented | 0.000 |

- **Same mechanism, barrier kept.** At width 5 the exhaustive search
  leaves sameA pairs 0.253, 0.000, 0.092 and 0.168, and sameB pairs 0.095,
  0.646, 0.097 and 0.292. Error barriers run up to 28 points. Within
  sameA, the barrier falls as the matched units' activation correlation
  rises. The pair at 0.000 has layer correlations 0.92 and 0.66, the pair
  at 0.253 has 0.48 and 0.03.
- **Different mechanism, connected.** At widths 64 and 256 all eight diff
  pairs reach 0.000 after activation matching, and error barriers fall
  under one point. The endpoints still differ on the independent test,
  0.89 against 0.25 on A-only. Feature correlation after matching is
  lower for diff pairs than for same pairs at the same width (first layer
  0.50–0.60 against 0.60–0.64; second 0.32–0.34 against 0.40–0.55). The
  layerwise feature cosine at the midpoint is 0.88–0.90 against
  0.94–0.97.
- **The barrier does not sort the pairs.** At widths 5–16, the per-pair
  best aligned barriers of diff pairs (0.15–0.54) overlap those of
  same-cue pairs (0.00–0.65). From width 64 up, none of the three kinds
  has a barrier.
- **Group.** For the twin, permutations recover the hidden permutation, but
  the rescaling leaves a linear barrier at every width. Quotienting it
  removes the barrier exactly. For trained pairs, `swm` was no better than
  weight matching, and worse where a unit had died.
- **Path family.** A trained curve on the aligned endpoints joins nearly
  every pair from width 8 up. Unaligned, it does so from width 8 for the single-cue pairs and from 16 for the rest. So
  under a fitted curve none of the pairs, same or different, shows a
  barrier.
- **Phase-III analogue (e2).** One cell is flat and poorly connected: width
  6 at batch 8 (λmax 0.47, unaligned Bezier 0.068 error). After activation
  matching the Bezier barrier there is 0.003 and the polychain 0.002, but
  the aligned straight line keeps 0.067 error (0.024, 0.059 and 0.118 by
  pair). Its test error, 0.013, stays above the flat connected cells'
  0.002–0.004. Every cell's barrier falls with width at each temperature,
  and the narrowest cells keep a barrier on every family.

## What it shows

1. **Alignment does not always remove the barrier between networks that
   share a mechanism.** That holds at narrow width with an exhaustive
   permutation search, and with any permutation search where a symmetry
   outside the permutations is present. This is the case QUESTION-069 asked
   for, at toy scale.
2. **In this toy the barrier tracks width and feature correspondence, not
   which input attribute is relied on.** Different-cue pairs connect once
   the networks are wide, and same-cue pairs stay apart when narrow.
3. **The verdict depends on the instrument.** The same aligned endpoints are
   separated on the straight line and joined on a trained curve. That is
   QUESTION-069's alternative, that connectedness belongs partly to the
   path family searched.

What this does to CLAIM-263 turns on what "share a mechanism" means in its
defeater, which the record leaves open. CLAIM-tmpr7v4j states the finding.
CLAIM-tmpv22hv and CLAIM-tmp46m6e are the two readings, filed as
alternatives for the owner.

## What it cannot show

- It is a toy: one synthetic task, MLPs of width 256 at most, numpy SGD,
  four pairs a cell. It says nothing directly about ResNets, ViTs or
  language models, where THEORY-112's measurements live.
- The barrier is measured on both-cue data, where the two cues agree. A
  probe on which the cues conflict could separate the A-net from the B-net
  where this one does not (CLAIM-142's caution). That was not run.
- The exhaustive search covers only width 5, and its rescaling step is a
  local optimum. At other widths, alignment is by heuristic matching, so
  a barrier left there may be a failure of the search.
- The phase-III analogue is one cell, on a classification fixed in advance
  by thresholds of the assistant's choosing. It is not Yang et al.'s phase
  III.
