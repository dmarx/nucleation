---
number: 536
status: Read
formerly:
- NOTE-tmpqfhaa
paper: 'LIT-657'
title: 'The Generalization Ridge: Information Flow in Natural Language Generation'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v6 (22 pages, text layer, COLM 2026 header). Sections
    1–7 read in full; Appendices A (estimator), B (datasets), C
    (implementation, residual scaling), D (compute) and E (confidence
    intervals, kernel ablation, residual scaling per model) read. Several
    displayed equations (the hypothesis, the batch definitions, the
    multi-token kernel) did not survive text extraction and are described
    from the prose. Table 1 and Table 2 values were recovered from the text
    layer. Earlier arXiv versions were not compared.
date: '2026-10-03'
summary: >-
  I(Zℓ; Y) = H(G_Z) + H(G_Y) − H(G_Z ∘ G_Y), with H(G) = −tr(G log G) on
  trace-normalized Gaussian Gram matrices (bandwidth 1) of ℓ2-normalized
  last-token states and target-token embeddings. It rises, peaks at layers
  10/12 (GPT-2-S, synthetic: 0.2721) and falls (0.0188 at layer 12), where
  OOD early-exit accuracy peaks (56.90%) and ID accuracy keeps rising
  (93.17%). Middle residual updates add most; OOD-fitted residual scales
  downweight the last layers. The profile's shape persists over 50 decoding
  steps.
---

<!-- inactive-ok-file: THEORY-035 — Rejected; named as the record's verdict on the compression account of generalization, which this paper's vocabulary echoes -->
<!-- inactive-ok-file: THEORY-039 — Proposed; named for the record's caution about later-phase claims, with no relation claimed -->

# NOTE-536: The Generalization Ridge: Information Flow in Natural Language Generation

## Contribution

A layer-by-layer, training-step-by-training-step profile of how strongly
transformer hidden states align with the target token, using a kernel
estimator of mutual information, for four language models of 117M to 8B
parameters fine-tuned on three tasks. It reports a consistent mid-to-upper
layer peak and ties it, on one synthetic task, to the layer whose early
exit generalizes best out of distribution. It adds two corroborating
probes: attention to task tokens and learned per-block residual scales.

## Key insight

Depth in a fine-tuned language model may divide labour: the middle builds
the features that predict the answer in a way that transfers, and the last
few blocks tune those features to the training distribution. If so, the
best place to read a transferable prediction is not the top, and a measure
that peaks in the middle marks the spot.

## Assumptions

- **Representation**: the hidden state at the last input position, Zℓ, and
  the residual update ΔZℓ = Zℓ − Zℓ−1. Vectors are ℓ2-normalized.
- **Target**: Y is the input-embedding vector of the true next token, taken
  from the embedding layer in a second forward pass with the token appended
  (Figure 1).
- **Estimator** (Giraldo et al. 2014): trace-normalized Gaussian Gram
  matrices with bandwidth 1, order-1 matrix Rényi entropy
  H(G) = −tr(G log G), and I(U; V) = H(G_U) + H(G_V) − H(G_U ∘ G_V).
  Laplacian and polynomial kernels change the magnitude but not the trend
  (Appendix E, Figure 8).
- **Models**: GPT-2 Small (117M) and Medium (345M), Qwen-2.5 0.5B, Llama 3.1
  8B; all fine-tuned on the task for Section 4; pretrained models for the
  multi-token experiment.
- **Data**: CLUTRR, ECQA, CNN/DailyMail and a synthetic arithmetic-
  progression task, sequences "S{signal} N{noise}" of 10 elements with
  signal st = (s0 + t·d) mod K. ID uses K = 13; OOD draws K uniformly from
  {5, …, 25} \ {13} (footnote 2).
- **Residual scaling**: z(ℓ) = z(ℓ−1) + βℓ·block(ℓ)(z(ℓ−1)), βℓ ≥ 0
  initialized to 1, fitted with all weights frozen, separately on ID and
  OOD splits.

## Key results

- **Three phases in depth (Section 4.1).** Progressive accrual, an
  information peak, then "representational compression". Table 1 (GPT-2-S,
  synthetic): I(Z; Y) 0.0002 (layer 1) … 0.0185 (6), 0.0416 (7), 0.1883
  (8), 0.2301 (9), 0.2721 (10), 0.2475 (11), 0.0188 (12). Early-exit
  accuracy, all / ID / OOD: layer 10, 55.15 / 53.40 / 56.90; layer 11,
  65.92 / 79.17 / 52.67; layer 12, 71.58 / 93.17 / 50.00. Layers 1–6 are at
  0.00.
- **Attention (Table 2).** Signal-token attention peaks in mid-to-late
  layers and falls in the last; for Qwen-2.5 0.5B on ECQA, 0.2307 at layer
  17 against 0.0104 at the final layer, where last-token attention is
  0.2169.
- **Incremental gain (Section 4.2, Figure 3).** Largest for middle blocks;
  late blocks contribute little and "in some cases" reduce alignment.
- **Residual scaling (Figure 4, Appendix E Figure 9, Table 5).** ID-fitted
  βℓ are relatively higher on the last layers; OOD-fitted βℓ are lower
  there and higher in the middle, and OOD accuracy improves when fitted on
  OOD data.
- **Multi-token (Section 5).** With a sequence kernel averaging pairwise
  token similarities, I(Z(t)ℓ; Y) grows with the decoding step but keeps the
  same layer-wise shape over 50 steps for Qwen-2.5 0.5B and Llama 3.1 8B.
- **Variability (Appendix E).** Five sampling seeds, 2σ bands for the
  information curves; five seeds and 1σ bands for βℓ.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The estimated I(Zℓ; Y) peaks at an intermediate layer and declines in the final layers, across models and tasks | moderate: consistent across the settings shown, with seed intervals | Figures 2, 6; Table 1 |
| C2 | The peak layer is where generalizable (OOD-robust) features are strongest | weak to moderate: shown by early-exit OOD accuracy on the synthetic task only | Table 1 |
| C3 | The final layers memorize training-distribution patterns | weak: inferred from ID accuracy rising while OOD accuracy and the estimate fall; no memorization test | Section 4.1 |
| C4 | Middle blocks contribute most new target-relevant information | moderate for the estimator | Figure 3 |
| C5 | Residual scaling gives causal evidence for the ridge | weak: the βℓ show where OOD fitting puts weight, which is an intervention on the model but not a test of the ridge hypothesis against an alternative | Figure 4 |
| C6 | The profile persists in multi-token generation | moderate for the shape; the level depends on the step | Section 5 |

## Method

For each checkpoint, run a batch of N inputs, take the last-token hidden
state at each layer and the per-layer residual updates; take the target
token's input embedding; build Gaussian Gram matrices; compute matrix-based
entropies and their Hadamard-product joint entropy; plot the mutual
information over layers and training steps. Separately, compute early-exit
accuracies, attention statistics and fitted residual scales.

## Concepts

- **predictive information**: here, the matrix-based estimate of
  I(Zℓ; Y) between the layer's last-token state and the target embedding.
- **incremental information gain**: the same estimate for the residual
  update ΔZℓ.
- **generalization ridge**: the layer ℓ* at which the estimate peaks,
  hypothesized to carry the most generalizable representation.
- **generalization funnel layer** (He et al. 2024): the depth at which a
  Wasserstein-based generalization bound is smallest, the motivation cited.

## Connections

- **Uselis and Oh ([LIT-678](../literature.d/LIT-678.md))**: intermediate layers generalize better
  under shift in vision classifiers; cited as prior evidence three times.
- **He et al. (2024)**: the generalization funnel and the Min Wasserstein
  Generalization Bound, the paper's motivation.
- **Shwartz-Ziv and Tishby ([LIT-324](../literature.d/LIT-324.md))**: cited among information-theoretic
  approaches to layers.
- **Skean et al. (2025), Fan et al. (2024), Jin et al. (2024)**: intermediate
  layers of language models are richer than final ones.

## Bearing on the record

- **What the estimator measures.** Table 1 is the paper's own evidence that
  the estimate is not Shannon mutual information with the target. At layer
  12 it is 0.0188, near the layer-6 value of 0.0185, yet layer 12's early
  exit decodes the target with 93.17% ID accuracy and layer 6's with 0%.
  A layer from which the target is decoded at 93% cannot carry almost no
  information about it. What falls at the last layer is the alignment
  between the Gaussian-kernel geometry of the hidden states and that of the
  target-token input embeddings, at a fixed bandwidth. The ridge is a real
  feature of that alignment, and its coincidence with the OOD early-exit
  peak is a real observation. "Information" and "compression" are the
  wrong words for it. This is my reading, not the paper's.
- **[THEORY-035](../theory.d/THEORY-035.md) (Rejected) and [THEORY-039](../theory.d/THEORY-039.md).** The record rejected the claim
  that generalization comes from compressing input information, partly
  because the compression was an artifact of the estimator (Saxe et al.,
  [LIT-372](../literature.d/LIT-372.md)). This paper's "representational compression" in the final
  layers should not be read as support for that account. It concerns a
  different quantity, alignment with the target, across depth rather than
  training time, and its own numbers show the estimate departing from
  decodability.
- **THEORY candidate (not filed):** "In fine-tuned transformers, the layer
  whose early exit is most robust to a shift in the task distribution lies
  below the last layer, and the final blocks raise in-distribution accuracy
  at the cost of out-of-distribution accuracy." Source this paper (Table 1)
  and [LIT-678](../literature.d/LIT-678.md); promote when the early-exit result is shown on more
  than the synthetic task.
- **Anthology.** The logit lens ([ANTH-LIT-570](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-570.md)) and the robustness of middle
  layers to deletion ([ANTH-THEORY-020](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-020.md)) are the anthology's nearest holdings.

## Limitations

- **The OOD link rests on one synthetic task.** The early-exit table is
  GPT-2 Small on synthetic arithmetic; for the natural tasks the ridge is
  shown in the estimate, not in OOD accuracy.
- **The target is an input embedding.** I(Z; Y) is computed against the
  embedding of the next token, a fixed vector per token type, so the
  estimate is a similarity between two kernel geometries, not between a
  state and a label distribution.
- **Fixed bandwidth.** A bandwidth of 1 on unit vectors fixes the scale at
  which similarity is read; the kernel ablation changes the kernel family,
  not the bandwidth.
- **Memorization is inferred, not measured.**
- **Reading of v6.** The paper has been revised five times; claims in
  earlier versions may differ.

## Open questions

- Does the ridge layer coincide with the best OOD early-exit layer on the
  natural tasks?
- Does a decodability measure (probe accuracy, or a Shannon-consistent
  estimator) show the same peak, or only the rise?
- Is the late decline a change of representation toward the output head
  that a kernel at fixed bandwidth reads as lost alignment?

## Corrections

- none (there was no seed)
- **Repeated text.** Section 6 repeats one sentence on probing analyses and
  layer pruning verbatim.
