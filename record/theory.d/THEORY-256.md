---
number: 256
status: Proposed
formerly:
- THEORY-tmpbx1ck
promote_when: >-
  A replication on a different family of factored generators, or under a
  second objective on the same data, in which the dimension and per-factor
  orthogonality of the learned representation are measured, and in which
  the noise experiment reports the loss gap between the factored and joint
  representations at each noise level. It is refuted by a transformer
  trained on a lossless factored process with room for the joint
  representation that settles near the joint dimension, or by a lossy
  process on which training reaches the joint representation without first
  passing near the factored one. What cannot settle it: linear decodability
  of each factor's belief alone, since a representation with overlapping
  factor subspaces also supports accurate linear readout (App. H.1.2).
title: "When a sequence generator's latent dynamics factor as a tensor product, its predictive state embeds losslessly and linearly in orthogonal per-factor subspaces of total dimension Σ(d_n − 1); small transformers trained by next-token prediction on such processes settle near that dimension in approximately orthogonal subspaces, and reach it first even when noise makes it lossy"
version: 1
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-986
summary: >-
  Shai et al. (2026), [LIT-986](../literature.d/LIT-986.md), read in [NOTE-758](../notes.d/NOTE-758.md). The lossless
  embedding is an elementary theorem (Prop. 2.2, Thm 2.3, App. A). The
  rest is experiment on five synthetic factors: about 10 effective
  dimensions against 242 for the joint state, approximate orthogonality in
  the first two components, and under token noise a collapse to the
  factored form before expansion. It does not show that the preference is
  architectural rather than a feature of training, a question the paper
  leaves open, and it varies neither the objective nor the data domain.
answers:
- QUESTION-060
---
<!-- inactive-ok-file: THEORY-197 THEORY-206 THEORY-274 — Proposed; accounts on the same question, open -->

# THEORY-256: When a sequence generator's latent dynamics factor as a tensor product, its predictive state embeds losslessly and linearly in orthogonal per-factor subspaces of total dimension Σ(d_n − 1); small transformers trained by next-token prediction on such processes settle near that dimension in approximately orthogonal subspaces, and reach it first even when noise makes it lossy

## Source

Shai, Amdahl-Culleton, Christensen et al. (2026), [LIT-986](../literature.d/LIT-986.md), read in
[NOTE-758](../notes.d/NOTE-758.md): Proposition 2.2, Theorem 2.3, App. A.3–A.5 for the theory;
§§4.1–4.4, App. C.2–C.4, D.1–D.6 and H for the experiments.

## What was actually shown

**The theory.** For a generalized hidden Markov model whose token-labelled
operators are tensor products, T^(x) = ⊗_n T_n^(x), a product predictive
vector stays a product after every token (Prop. 2.2, eq. 11). The set of
product states has intrinsic dimension Σ_n(d_n − 1), and an explicit linear
map, partial traces followed by orthogonal per-factor embeddings, carries it
invertibly into a direct sum (Thm 2.3; eq. 13, 17). Off that manifold the
map loses the total correlation D[η ‖ ⊗η_n] (eq. 16). Dependency chains
between factors are covered, since only the operators must factor.

**The experiments.** Three Mess3 and two Bloch Walk factors, 432 product
tokens, a 4-layer GPT-2-style transformer (d_model 120, also 480):

- independent and chained factors: effective dimension at 95% variance
  falls to about 10–11, against 242 for the joint state, even at
  d_model = 480; each factor's belief is linearly recoverable;
- vary-one subspaces: per-factor dimensions sum to 14 against a union of
  12, and pairwise overlaps fall in the first two components only;
- token noise ε from 0.001 to 0.5: activations collapse to about 10
  dimensions within hundreds of steps for every ε, then expand under
  continued training, the more so the larger ε;
- RNNs and LSTMs: closer to factored than joint, but less sharply.

What could have come out otherwise: a model with ample width could have
used the joint representation, which the objective never penalizes, or
gone straight to it when factoring was lossy. Neither happened.

## What this does not say

- **Not that the architecture is the cause.** The paper names an
  "inductive bias of the architecture" but its own appendix (D.4) leaves
  open whether the effect comes from "training dynamics or inductive
  bias". Optimizer, initialization and width were not varied to separate
  them.
- **Not that cheapness beats the objective.** Under heavy noise the
  converged representation leaves the factored form (App. D.5, Fig. 12).
  Cheapness predicts what training reaches first; the objective still acts
  later.
- **Not orthogonality, strictly.** Dimension additivity shows linear
  independence of the factor subspaces; the overlap metric gives
  approximate orthogonality in two components per factor.
- **Not natural data.** Five small known processes, factors fixed by a
  product token code; whether factors are found in data without such
  structure is untested.
- **Not a measured fidelity cost.** The loss gap between factored and
  joint representations at each ε is argued from the construction, not
  reported for the trained models.

## Connections

- **[QUESTION-060](../questions.d/QUESTION-060.md).** An answer in part: a family with known relevant
  variables in which the learned variables coincide with them when
  factoring is lossless, and in which, when it is lossy, the variables
  reached first are the cheap ones rather than the objective's optimum. It
  varies the data, not the objective or the architecture, so it does not
  apportion the two the question names.
- **[THEORY-206](THEORY-206.md).** On the representational side, products of many inputs
  are costly for a shallow network; here a tensor product of beliefs is
  replaced by a sum, a case of the same cheapness shaping what is kept.
- **[THEORY-197](THEORY-197.md).** The contrasting case: there the objective fixes what is
  kept against a formal match; here the training path holds a
  representation the objective does not favour.
- **[THEORY-274](THEORY-274.md).** A second case in which what training reaches is not
  fixed by the objective's optimum alone.
