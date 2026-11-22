# LEAD-172 progress

- Lead: LEAD-172 (modular-addition checkpoint study, prospective test)
- Branch: claude/lead-172-modular-addition
- Task as understood: train small transformers on modular addition (CPU,
  ~1 hour budget, one or two small models, a few seeds); at checkpoints
  measure training-kernel eigenspaces and per-layer coupling among Fourier
  modes; fit on early checkpoints, predict later change (circuit formation,
  generalization), including under a held-out intervention; compare against
  a null at equal edge budget. File a CASE (executed-study), a CLAIM if
  warranted, dated notes on QUESTION-275, QUESTION-360, QUESTION-217,
  CLAIM-698 and LEAD-172, and a changelog fragment.

## Done

- modadd.py (model, training, measures, append-only gz JSONL, resume from
  saved state) and test_modadd.py (4 tests pass).
- Runs launched 13:05 UTC: 12 fit arms (frac 0.3-0.6 x seeds 0-2, wd 1.0)
  and 8 held-out-intervention arms (wd 0.5 and 2.0, frac 0.4/0.5, seeds
  0-1), 4 shards in parallel; estimate ~13 min, limit 30 min.

## Next

- analyze.py: features at memorization step T_mem, single-feature linear
  forecasts of log T_gen fitted on fit arms, scored on held-out arms;
  null couplings at equal edge budget (20 random off-rule sets of p-1).
- File CASE, CLAIM if warranted, notes, changelog.

## Choices

- torch is not installed: numpy only, hand-written forward and backward.
- Model is the attention-free reduction of a one-layer transformer
  (embeddings for a and b summed, ReLU layer, unembedding), not a
  transformer with attention: hand-written backprop for attention was too
  costly in the time available. Stated as a limit in the CASE.
- p = 37, hidden 128, AdamW lr 3e-3, full batch.
- "Coupling among Fourier modes" operationalized globally: hidden layer's
  mixed-mode energy on selection-rule cells (l = k), and output logits'
  3D DFT energy on triads (k, k, -k). Null: same count (p-1) of random
  off-rule cells/triads.
- Kernel: closed-form trace NTK on all p^2 inputs; alignment of top-p
  eigenspace with functions of a+b; eigenspace rotation between kernel
  checkpoints as moving-basis proxy.
- Held-out intervention: weight decay values not in the fit set.
- Target: T_gen, first step with test acc >= 0.95.
