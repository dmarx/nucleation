---
status: Proposed
title: 'Beyond linear probes no single span of the conditional-expectation operator is the decision-sufficient signature: a nonlinear readout recovers stable targets outside the top-d linear span, sufficiency for a stated decision is span-relative, and direction-dependent decisions are served by no left span'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A single construction from the pair operator is exhibited that is
  decision-sufficient for a stated family of nonlinear decisions outside the
  observed probes, holding across the spans that tie for linear probes and
  without the decision family being fixed in advance; for instance the top-d
  left singular span is shown sufficient, with a nonlinear readout, for every
  compatible target and for decisions that turn on the direction of the
  transport.
tags:
- representation-learning
- mathematical-statistics
- mathematics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
bears_on:
- QUESTION-052
grounds:
- CASE-tmp5w2ty
complements:
- CLAIM-164
- CLAIM-209
corroborates:
- CLAIM-193
---
<!-- inactive-ok-file: CASE-tmp5w2ty CLAIM-tmpc54vj — Proposed; the study that grounds this claim and the companion reduction claim, filed with it on 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-209 CLAIM-193 — Proposed; the thesis this bounds and the linear-probe claim it corroborates, cited as open -->

# CLAIM-tmpm4oom: Beyond linear probes no single span of the conditional-expectation operator is the decision-sufficient signature: a nonlinear readout recovers stable targets outside the top-d linear span, sufficiency for a stated decision is span-relative, and direction-dependent decisions are served by no left span

## The claim

[THEORY-239](../theory.d/THEORY-239.md) shows the top-d left singular span is **minimax-optimal for
linear probes** over the compatible class, and that other spans can tie it.
Read as "the top-d left singular space is the decision-sufficient signature"
the candidate fails once the decisions are not linear probes, in three ways,
each exhibited in [CASE-tmp5w2ty](../cases.d/CASE-tmp5w2ty.md).

1. **The signature is the encoder, not the subspace.** A nonlinear readout of
   the d-dimensional encoder (μ₁…μ_d) recovers any function of those
   coordinates, including stable targets that lie outside their linear span.
   In the product-chain example the interaction χ_a·χ_b is a view-invariant
   target (two-step eigenvalue 0.518) with linear-probe residual 1.0 on the
   top-2 span, recovered exactly by the product readout. So the object that is
   decision-sufficient for nonlinear decisions is the σ-algebra the encoder
   generates, and a smaller d can suffice than the linear truncation of the
   target would suggest. This extends [CLAIM-164](CLAIM-164.md)'s point that the definite
   object is the eigenspace, not a vector: for nonlinear decisions it is
   coarser still, the σ-algebra, not even the span.

2. **Sufficiency for a stated decision is span-relative.** Because [THEORY-239](../theory.d/THEORY-239.md)'s
   optimality is a worst-case over the whole compatible class, it does not make
   the top span sufficient for an arbitrary stated compatible decision. The
   compatible target χ_b has residual 1.0 from the top-1 encoder χ_a and 0
   from the equally small competitor χ_b. Absent a fixed family of decisions,
   no single span is the signature — which is the gap [CLAIM-209](CLAIM-209.md) is faulted
   for ("names no family of decisions"), now shown to be load-bearing.

3. **Direction-dependent decisions are served by no left span.** The left
   signature is a function of the input alone. A decision that turns on the
   direction of the transport — the order decision sign(x − a) — keeps a
   positive irreducible error from any function of x (0.2245 of variance
   0.824) while the ordered pair determines it. No left span, at any d,
   is the signature for such decisions.

Together with [CLAIM-tmpc54vj](CLAIM-tmpc54vj.md)'s reduction, this locates the open part of
[QUESTION-052](../questions.d/QUESTION-052.md) precisely: the directed nonlinear input-decision case is the
symmetric nonlinear case (nothing directed is left there), and the genuinely
directed residue is decisions about the transport itself. That a linear probe
sees only the span here corroborates [CLAIM-193](CLAIM-193.md).

## What it does not say

- Not that the top-d span is useless: it remains [THEORY-239](../theory.d/THEORY-239.md)'s
  minimax-optimal linear-probe span, and its encoder is a sufficient starting
  point for nonlinear readouts of targets that are functions of its
  coordinates.
- Not that a decision-sufficient signature cannot exist once a family of
  decisions is fixed — that is [CLAIM-209](CLAIM-209.md)'s open thesis, which this bounds
  rather than denies.
- Not a measurement of how often the candidate fails in practice; the
  examples are chosen constructions, exact at the population level.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
