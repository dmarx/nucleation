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
- First launch (lr 3e-3) stopped at 13:07: the machine is shared (load
  ~17 on 4 cores) and its pace said arms would not grok within budget.
  Pilots: lr 1e-2, wd 1.0, frac 0.5 groks in ~2k steps (~40 s).
- Relaunched 13:08 with lr 1e-2: 9 fit arms (frac 0.4/0.5/0.6 x seeds
  0-2, wd 1.0) and 6 held-out arms (wd 0.5 at frac 0.5/0.6 x seeds 0-1;
  wd 2.0 at frac 0.5 x seeds 0-1). Earlier plan below superseded.
- analyze.py written; early checkpoints fixed at steps 250 and 500
  (memorization happens by step ~100 in every arm, so T_mem does not
  separate arms).
- Old: runs launched 13:05 UTC: 12 fit arms (frac 0.3-0.6 x seeds 0-2, wd 1.0)
  and 8 held-out-intervention arms (wd 0.5 and 2.0, frac 0.4/0.5, seeds
  0-1), 4 shards in parallel; estimate ~13 min, limit 30 min.

- All 25 arms done by 13:16 (10 added at 13:15: fit seeds 3-5 at frac
  0.5/0.6; held-out wd 0.5 seeds 2-3). f40 (wd 1.0) and wd 2.0 arms did
  not generalize within 15000 steps (censored). Results recompressed to
  one gzip stream per arm after completion (1.2 MB).
- analyze.py run: analysis_te250.json, analysis_te500.json,
  analysis_stdout.txt. Headline: logit selection-rule coupling C2 at step
  250/500 forecasts log10 T_gen on held-out weight-decay arms with RMSE
  0.154/0.130 (constant 0.345; Fourier energy 0.192/0.197; test acc
  0.276/0.247; kernel alignment 0.186/0.350); beats all 20 equal-edge null
  draws at both checkpoints (null median 0.34). No measure foresaw the 5
  censored arms. C2 crosses 0.5 at or after T_gen, not before.

- Filed CASE-tmpb4hg0 (executed-study), CLAIM-tmp6rhuv (thesis,
  empirical), changelog fragment, and dated notes of 2026-11-22 on
  LEAD-172, QUESTION-275, QUESTION-217, QUESTION-360, CLAIM-698.

## Next

- Report to the lead. Nothing else pending in this worker's scope.

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
