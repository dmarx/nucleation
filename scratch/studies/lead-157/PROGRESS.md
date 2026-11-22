# LEAD-157 progress

- Lead: LEAD-157 (advances QUESTION-069, CLAIM-263, CLAIM-187)
- Branch: claude/lead-157-loss-barriers (cut from origin/staging)

## Task as understood

Train small numpy networks; align pairs by permutation (weight matching and
activation matching); measure the loss barrier along several path families
(linear, aligned linear, fitted curve, piecewise via a centre); build a pair
known to share a mechanism by an independent test and ask whether alignment
always removes its barrier (CLAIM-263's defeater).

Step 1 check: no case, claim or study in record/ or scratch/studies/ holds
an executed permutation-alignment barrier study (grep of "permutation
alignment", "loss barrier", "linear mode connectivity"; only the lead,
CLAIM-263, CLAIM-187, QUESTION-312 and curation entries mention it).

## Choices made

- Task: synthetic 4-class, 16-dim input with two redundant cue blocks (A dims
  0-3, B dims 4-7; 3 Gaussian clusters per class per cue). D_A scrambles cue
  B, D_B scrambles cue A, D_both keeps both. Mechanism test independent of
  the barrier: accuracy when only cue A, or only cue B, carries the label.
- Nets: 2-hidden-layer ReLU MLP, SGD momentum 0.9, wd 1e-4.
- Alignments: none, weight matching (wm), activation matching (am), scale
  canonicalisation + wm (swm: quotients ReLU rescaling too), and at width
  <= 5 (e1) / 4 (e2) an exhaustive search over permutations plus optimised
  rescaling ("fullgroup").
- Path families: linear, trained quadratic Bezier, trained one-bend
  polychain. Barrier = max_t L(t) - linear interpolation of endpoint values,
  on the both-cue test set (and train set), in loss and 0-1 error.
- e1: pairs sameA, sameB, both, diff (A-net vs B-net), twin (an A-net and
  a permuted, rescaled copy: the same function) at widths 5-256, 4 pairs.
- e2: load x temperature analogue of THEORY-108's grid: widths 4-64 x batch
  256/32/8, 3 pairs; top Hessian eigenvalue for flatness.

## Done

- Step 1 check (not held).
- lb.py + test_lb.py (13 pass); run.py (e1, e2), results_e*.jsonl written
  per item, resumable.

## Next

- Finish e1/e2 runs (started 17:10 UTC); analyse; file CASE, CLAIM(s),
  dated notes on CLAIM-263, CLAIM-187, QUESTION-069, LEAD-157; changelog.
