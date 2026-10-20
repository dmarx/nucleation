---
status: Proposed
promote_when: 'A replication on a different family of factored generators, or under a second objective on the same data, in which the dimension and per-factor orthogonality of the learned representation are measured, and in which the noise experiment reports the loss gap between the factored and joint representations at each noise level. It is refuted by a transformer trained on a lossless factored process with room for the joint representation that settles near the joint dimension, or by a lossy process on which training reaches the joint representation without first passing near the factored one. What cannot settle it: linear decodability of each factor''s belief alone, since a representation with overlapping factor subspaces also supports accurate linear readout (App. H.1.2).'
title: Transformers trained by next-token prediction on sequence processes whose latent dynamics factor as a tensor product learn to represent the belief state in approximately orthogonal per-factor subspaces of about the factored dimension rather than the joint one, and reach that factored representation first even when noise makes it lossy
version: 1
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-20'
source:
- LIT-986
summary: The general reading that [THEORY-256](THEORY-256.md) held before the promotion audit narrowed it to the five Mess3 and Bloch Walk factors and the 4-layer GPT-2-style models tested (batch 019). Shai et al. (2026), [LIT-986](../literature.d/LIT-986.md), read in [NOTE-758](../notes.d/NOTE-758.md), present next-token training (the paper is titled “Transformers learn factored representations”) as yielding factored, orthogonal belief representations; [NOTE-758](../notes.d/NOTE-758.md)'s claims C2 to C4 are each shown on one family of synthetic processes. Filed under [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis evidence can confirm or reject. It does not include the paper's inference that the preference is architectural (C5), which App. D.4 leaves open, or the claim that the factored form persists at convergence under strong noise, which Fig. 12 contradicts.
extends:
- THEORY-256
answers:
- QUESTION-157
---

# THEORY-tmpq57h3: Transformers trained by next-token prediction on sequence processes whose latent dynamics factor as a tensor product learn to represent the belief state in approximately orthogonal per-factor subspaces of about the factored dimension rather than the joint one, and reach that factored representation first even when noise makes it lossy

## Source

Shai et al. (2026), [LIT-986](../literature.d/LIT-986.md), §§4.1–4.3 and Apps. C.4, D.3–D.5, read in full
in [NOTE-758](../notes.d/NOTE-758.md). The lossless embedding (Prop. 2.2, Thm 2.3) is the theorem
[THEORY-256](THEORY-256.md) states; the learned representation is the paper's experimental
finding, which it frames as a property of next-token training on factored
processes.

## What is asserted, and by whom

The thesis is that what [THEORY-256](THEORY-256.md) measured on one family is what next-token
training does on factored processes in general: the learned representation
uses about Σ(d_n − 1) dimensions, not the joint state's, in per-factor
subspaces that are approximately orthogonal, and under lossy factoring
training passes through the factored form first. Shai et al. assert it from
their experiments ([NOTE-758](../notes.d/NOTE-758.md), C2–C4). Two things are left out because the
paper's own results do not carry them: that the preference is an inductive
bias of the architecture (C5, weak; App. D.4 says the source is open), and
that the factored form is kept at convergence under strong noise (for large
ε the converged representation departs from it, Fig. 12).

## What the record holds toward it

- [THEORY-256](THEORY-256.md) (Active): the theorem, and the measurement on five Mess3 and Bloch Walk factors: about 10 effective dimensions against 242 for the joint state, linear independence and approximate orthogonality in the leading components, and under the token noise tested the factored form reached first.
- [NOTE-758](../notes.d/NOTE-758.md) also records that recurrent networks factor less sharply in four small configurations (C6, weak), which is the only evidence beyond transformers.

## What would confirm or reject it

A replication of the kind the promote_when describes confirms it; a
transformer that settles near the joint dimension with room to spare, or a
lossy process on which training goes straight to the joint representation,
rejects it. [QUESTION-157](../questions.d/QUESTION-157.md) asks the same thing as a question; this entry is
the answer Shai et al. propose.
