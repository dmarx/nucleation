---
number: 621
status: Read
formerly:
- NOTE-tmpepej2
paper: LIT-792
title: 'Transformers learn in-context by gradient descent'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v2 PDF (31 May 2023, 24 pp.). Sections 1–5 read in
    full; Appendix A.1 (the construction of Proposition 1) checked by
    hand, block by block; A.9 (softmax and LayerNorm, with the
    first-order argument for a second head) and A.11 (phase transitions)
    read. A.2–A.8, A.10 and A.12 were looked over, not read; the proof of
    Proposition 3 (A.5) and the kernel-regression discussion of
    Proposition 2 (A.8) were not followed. The anthology's own reading
    (ANTH-LIT-533) was not consulted until this note was drafted.
date: '2026-10-09'
summary: >-
  Constructs weights for which one linear self-attention layer reproduces,
  on every token, the data change induced by one gradient step of a linear
  model on the in-context regression loss, so the query's output equals
  the post-update prediction; shows a trained single layer finds these
  weights up to scale, and that deeper trained models implement a
  curvature-corrected variant (GD++) rather than gradient descent.
---

<!-- inactive-ok-file: THEORY-169 — Proposed; the account this reading supports -->

# NOTE-621: Transformers learn in-context by gradient descent

## Contribution

Before it, gradient-descent-like behaviour of in-context learners was
established mainly by matching predictions (Garg et al. 2022; Akyürek et
al. 2023, with a multi-layer construction). This paper gives a one-layer,
exact construction in plain linear self-attention, builds on the
linear-attention/fast-weight identity of Schlag et al. (2021), and shows
that optimisation on regression tasks actually lands on the construction.
It also identifies what deeper trained models do instead (GD++), and a
copying mechanism that assembles the tokens the construction needs.

## Key insight

A gradient step on a linear model's weights can be rewritten as a change
to the targets: L(W + ΔW) = (1/2N) Σ ‖Wx_i − (y_i − ΔW x_i)‖². Linear
self-attention computes exactly a sum of value–key outer products applied
to a query, which is the form of ΔW x_j. So the layer can perform the
update on the data rather than on any weights, and the prediction comes
out the same. Reading a context and learning from it are, in this
setting, one computation described two ways.

## Assumptions

- Linear self-attention (softmax removed), no biases; tokens
  e_j = (x_j, y_j) concatenating input and target.
- Keys and values computed from the N context tokens only (the query is
  excluded), or, equivalently in practice, W₀ ≈ 0 by small initialisation.
- Query token initialised as (x_test, −W₀x_test), read out by negation.
- Training tasks: teacher W_τ ~ N(0, I), x ~ U(−1, 1)^{n_I}, noiseless
  targets, N = n_I = 10, n_O = 1; loss on the query only; fresh tasks at
  every step.
- The construction is unique only up to the products PW_V and W_KW_Q and a
  common rescaling.

## Key results

- **Proposition 1.** With the block weights above, one LSA layer gives
  e_j ← (x_j, y_j) + (0, −ΔW x_j) for every j including the query; the
  read-out is (W₀ + ΔW)x_test. Checked: W_KW_Q selects x, W_V produces
  (0, W₀x_i − y_i), and the sum over i with P = (η/N)I gives
  (0, −ΔW x_j).
- **Single trained layer (§3, Figure 2).** Loss equals that of one GD
  step with line-searched η; prediction difference and model difference
  near zero, cosine similarity near 1; interpolating trained and
  constructed weights (after scale correction) leaves the loss unchanged;
  out-of-distribution input ranges and teacher scales degrade both
  identically.
- **Repeated application.** Applying the trained layer repeatedly, with a
  damping λ = 0.75 on both it and GD, tracks repeated GD steps (Figure 1).
- **Deeper models (Figure 3).** Looped two-layer and unrolled five-layer
  LSA models beat 2 and 5 GD steps and align with GD++ (data transformed
  by I − γXXᵀ, η and γ per step); naive interpolation fails for the
  five-layer case.
- **Proposition 2.** MLP followed by LSA gives gradient descent on
  (1/2N) Σ ‖W m(x_i) − y_i‖², hence kernel least squares with
  k(x, y) = m(x)ᵀm(y) when iterated; sine-wave experiments match a
  meta-learned MLP with one output-layer GD step (Figure 4).
- **Proposition 3 and §4.** With alternating input and target tokens, a
  softmax first layer copies neighbours together (the derivative of its
  output on e_{j+1} spikes before the loss drops), then a second layer
  matches one GD step. Training with linear attention in the first layer
  failed.
- **A.9.** A single softmax layer does not match GD; to first order the
  softmax adds an offset that a second head can cancel, and with that
  modification alignment returns, though worse than linear attention.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | One linear self-attention layer can exactly implement one GD step on an in-context linear regression, as a change to the tokens | strong (proof) | Proposition 1, Appendix A.1, checked here |
| C2 | Training a single LSA layer on such tasks finds that construction up to scale | strong (for the setting) | Figure 2, interpolation, OOD tests |
| C3 | Deeper trained LSA models implement GD++, not GD | moderate | Figure 3, alignment after tuning per-layer η and γ |
| C4 | Softmax attention can copy inputs and targets into single tokens, enabling the step in a later layer | moderate | Proposition 3 (proof not followed), Figure 5 |
| C5 | In-context learning in large language models emerges through mechanisms like these | weak (hypothesis) | stated as Hypothesis 1 and "we hypothesize"; untested beyond small synthetic models |

## Method

Train attention-only (and later MLP-plus-attention) models with Adam on a
stream of freshly sampled regression tasks, the loss taken on the query
token's prediction. Compare with gradient descent of tuned learning rate
on the same in-context data by loss, prediction difference, cosine
similarity of input sensitivities, and weight interpolation after
correcting the construction's scale ambiguity.

## Concepts

- **LSA**: linear self-attention, e_j + Σ_h P_h V_h K_hᵀ q_{h,j}.
- **mesa-optimizer**: a learned model that itself runs an optimiser in its
  forward pass (after Hubinger et al. 2019).
- **GD++**: gradient descent on data transformed by H(X) = I − γXXᵀ before
  each step; an iterative curvature correction.
- **θ_GD**: the weights of Proposition 1.
- **fast weights**: per-input weights computed by a slow network; linear
  attention is a fast-weight programmer (Schlag et al. 2021).

## Connections

It rests on Schlag, Irie and Schmidhuber (2021), "linear transformers are
secretly fast weight programmers", and frames transformer training as
meta-learning on two time scales. Sun et al. ([LIT-801](../literature.d/LIT-801.md)) reach the same
identity from the other side: their TTT layer with a linear inner model and
batch gradient descent is linear attention (their Theorem 1), and softmax
attention is a nonparametric kernel learner (their Theorem 2). Xie et al.
([LIT-797](../literature.d/LIT-797.md)) give a rival account of the same phenomenon in terms of the
data distribution, not the computation. The anthology's [ANTH-LIT-533](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-533.md) and
[ANTH-THEORY-068](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-068.md) record later work (Fu et al., Shen et al.) that separates
trained transformers from gradient descent beyond this setting.

## Bearing on the record

- **[THEORY-169](../theory.d/THEORY-169.md).** Proposition 1, together with Sun et al.'s
  Theorems 1 and 2, is the evidence for that account: in linear
  attention, conditioning on a context and taking a gradient step on an
  implicit model's weights produce the same output, so the difference
  between changing the context and changing the interpreter is not, in
  this class of system, a difference in the computation. The account is
  restricted to the exact constructions; it does not rest on C5.
- **Agreement with the anthology.** [ANTH-THEORY-068](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-068.md) rejects "in-context
  learning is gradient descent" for trained transformers beyond one layer,
  on this paper's own GD++ result and on later work. Nothing here
  contradicts that. This reading takes from the paper only what the
  anthology keeps: the construction and the one-layer finding.
- No instruction for machine-learning practice is drawn.

## Limitations

- Linear attention, synthetic noiseless regression, small models; the
  softmax case needs an architectural modification and fits worse.
- The update ΔW is relative to a W₀ hidden in the weights; the trained
  model's initial linear model is not directly observable, so agreement is
  approximate by design.
- Deeper models are described by a fitted family (GD++) with per-layer
  parameters, which makes alignment easier to obtain.
- The step to language models (Hypothesis 1) is not tested.

## Open questions

- Is there an exact analogue of Proposition 1 for softmax attention
  without the second-head correction? Sun et al.'s Theorem 2 answers with
  a nonparametric learner rather than a gradient step.
- In a pretrained language model, does any layer's effect of a context
  admit description as an update of an identifiable implicit model, and
  how long would such an update persist? The construction's update lives
  only in the activations of one forward pass.
