---
number: 534
status: Read
formerly:
- NOTE-tmppzhcy
paper: 'LIT-660'
title: 'Mode Connectivity Beyond Classifiers: Evidence from Generative and Contrastive Models'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v1, main text and Appendices A–E.
    Curves (Figs. 3–9) were read from captions and the numbers the text
    states; FID values in Fig. 6 are not given in the text.
date: '2026-10-03'
summary: >-
  One pair of DDPMs (Flowers102) and one pair of NanoCLIP models (Flickr30k)
  are joined by chains built by staged layer moves, per-layer variance
  correction and AdamW retraining to a loss threshold. DDPM training loss
  stays below 0.04 (AutoNEB peaks at 0.17), NanoCLIP below 0.09 (AutoNEB
  6.69, accuracy 0.05). Ablations: all-layers, forward-order and SGD
  variants all raise the average loss. Intermediate DDPMs generate worse
  (higher FID) at endpoint-level training loss.
---

<!-- inactive-ok-file: LIT-660 — Proposed by this reading; the note is the reading that placed it -->
<!-- inactive-ok-file: LIT-676 — Proposed: named as a sibling test of connectivity outside image classifiers -->
<!-- inactive-ok-file: LIT-677 — Proposed: named as a sibling test of connectivity outside image classifiers -->
<!-- inactive-ok-file: LIT-354 — Deferred: Watanabe's book is unread; named as the source of the singular-learning-theory argument the paper cites, with no relation claimed -->

# NOTE-534: Mode Connectivity Beyond Classifiers: Evidence from Generative and Contrastive Models

## Contribution

It reports non-linear mode connectivity between independently trained
modes of a denoising diffusion model and of a small CLIP model. It does so
with a layer-wise path-building procedure adapted from LLPF: a moving order
that follows the architecture's dataflow, and Adam-based refinement.

## Key insight

Generative and contrastive models have more parameters and farther-apart
modes than the CIFAR classifiers mode connectivity was established on, so a
path has to be built in stages, a few coupled layers at a time, with an
adaptive optimiser pulling each staged point back to low loss.

## Assumptions

- **Two modes per model**, from different random seeds, no shared early
  training and no permutation alignment (§3).
- **Variance sphere** (Eqs. 2–5): independently trained layers have
  approximately zero mean and equal variance, so fixing a layer's variance
  fixes its distance from the origin. App. A, Fig. 7 supports this
  empirically across seeds.
- **Low-loss region** = {P : L(P, D) ≤ L_thres} (Eq. 1); thresholds 0.03
  (DDPM) and 0.04 (NanoCLIP) for refinement (Table 2).
- **Procedure** (Algorithm 1): step = α|P_iP_E| + β|arc P_0P_E| + γ along
  the active layers' direction to the end mode; variance correction;
  retrain until loss < threshold or a round limit (500 DDPM, 200 NanoCLIP);
  variance correction again. 39 stages of 400 iterations (DDPM) and 20
  stages (NanoCLIP), runtimes 59 and 77 hours on an RTX 5090 (Table 2).
- **DDPM** is evaluated by denoising loss (train and test), **NanoCLIP** by
  contrastive loss, training accuracy and Recall@1; NanoCLIP has no test loss.

## Key results

- **Paths** (Fig. 3): DDPM training loss < 0.04 throughout, test loss ending
  near 0.04, "even lower than the starting mode"; NanoCLIP training loss <
  0.09, with accuracy and Recall@1 "relatively stable".
- **Against AutoNEB** (Fig. 4): DDPM maximum training / test loss 0.17 /
  0.18 for AutoNEB, 0.03 / 0.15 for this method; NanoCLIP maximum training
  loss 6.69 and minimum accuracy 0.05 for AutoNEB, 0.09 and 0.95 here.
- **Ablations** (Fig. 5, partial paths): moving all layers at once, DDPM
  average loss 0.031 vs 0.025, NanoCLIP more than double; forward order
  0.002 worse on both; SGD instead of Adam, DDPM 0.030 vs 0.024, NanoCLIP up
  to two orders of magnitude worse.
- **Segment check** (App. B): 20 interpolation points between each pair of
  consecutive NanoCLIP anchors raise the maximum loss by under 5.3%.
- **Generation** (Fig. 6): 41 checkpoints along the DDPM path, 1000 images
  each with fixed noise; intermediate FID generally higher than the
  endpoints'.
- **Near the end mode** (App. E, Fig. 9): checkpoint 16400 has layer-wise
  cosine similarity near one to the end mode; the straight line between
  them peaks at 0.038, the path at 0.034.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Independently trained DDPM modes, and NanoCLIP modes, are connected by low-loss paths | weak: one pair each; the path is a chain of retrained anchors; segments checked for NanoCLIP only | §5, Fig. 3, App. B |
| C2 | AutoNEB fails to find low-loss paths for these models | moderate for NanoCLIP (6.69 vs 0.09); weak for DDPM (test-loss peak 0.18 vs 0.15) | Fig. 4 |
| C3 | Dataflow-ordered staged movement and Adam refinement are needed | moderate: ablations on partial paths | Fig. 5 |
| C4 | Low training loss along the path does not imply generation quality | moderate: FID along one path | Fig. 6 |
| C5 | The low-loss region near a trained mode is anisotropic, not a flat basin | weak: one checkpoint, a 0.004 difference in peak loss | App. E |

## Method

Algorithm 1, two stages per iteration: Weighted Movement (move the active
layer subset U_i towards the end mode, then variance-correct every layer to
the reference sphere of the start mode), and Training Refinement (AdamW to
below the loss threshold, then variance-correct again). Layer subsets grow
stage by stage: for DDPM, matching encoder and decoder blocks from the
outside inward; for NanoCLIP, two vision blocks then one text layer,
repeated.

## Concepts

- **mode**: a well-trained parameter point with low loss.
- **variance sphere S_var^{(k)}(v)**: the set of layer-k parameters with
  variance v.
- **layer moving sequence U**: the order in which layer groups are allowed
  to move.
- **tick**: one iteration of Algorithm 1, producing one anchor.

## Connections

- **LLPF (Tian et al. 2026)**, not in the record: the two-stage layer-wise
  method this paper adapts; its ablation "forward order + SGD" is said to
  stand in for LLPF.
- **Draxler et al. ([LIT-653](../literature.d/LIT-653.md))**: AutoNEB, the baseline.
- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md))**: FGE, set aside because its released
  implementation is said to be in error, citing Tian et al. 2026.
- **Frankle et al. ([LIT-654](../literature.d/LIT-654.md)), Entezari et al. ([LIT-652](../literature.d/LIT-652.md)), Git
  Re-Basin ([LIT-661](../literature.d/LIT-661.md))**: cited as the linear-connectivity line (shared
  early trajectory, or permutation alignment) that this paper does not use.
- **Singular learning theory (Watanabe 2009; [LIT-354](../literature.d/LIT-354.md))**: cited as the
  theoretical reason to expect connected minima in singular models.

## Bearing on the record

- Counts towards the question whether mode connectivity is a property of
  deep networks in general or of supervised classifiers. With the GNN
  ([LIT-676](../literature.d/LIT-676.md)) and ELBO ([LIT-677](../literature.d/LIT-677.md)) readings, a THEORY candidate on
  connectivity from degeneracy (non-identifiable parameterisations) could
  draw on it, but its evidence is thin.
- No ML instruction as such; the flag follows [ADR-027](../decisions.d/ADR-027.md)'s batch rule.

## Limitations

- **One pair of modes per architecture.** No variance across seeds is
  reported.
- **Anchors are retrained.** A chain whose every point is optimised to low
  loss demonstrates a walk, not a pre-existing path; App. B checks the
  straight segments only for NanoCLIP.
- **Inconsistent numbers.** §5 says DDPM training loss stays below 0.04 and
  test loss ends near 0.04; the AutoNEB comparison gives this method's
  maximum test loss as 0.15. The two may refer to smoothed and raw curves,
  which the text does not say.
- The paper says Adam and its configuration table says AdamW, with weight
  decay 0.
- Small models and datasets (Flowers102, Flickr30k), far from the "modern
  foundation models" the discussion invokes.

## Open questions

- Do the paths hold with more pairs, and with barrier measured densely along
  the whole DDPM path?
- Why does generation quality fall in the middle while denoising loss does
  not?
