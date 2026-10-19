---
number: 379
status: Active
formerly:
- CLAIM-tmp861ar
title: 'On a finite set of stimuli, regularized linear readouts with ridge b > 0 cannot tell apart two centred representations of the same width exactly when one is an orthogonal transformation of the other, and the unregularized CCA member cannot tell apart representations with the same column space, which differ by an invertible linear map'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from CLAIM-269 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/CLAIM-269.yaml, batch 015, ADR-047;
    batch 004 decided the split and it waited on THEORY-008, Active since
    #165). The derivation below was re-checked for that decision. CLAIM-269
    rests on this claim and keeps its clauses grounded on THEORY-002 and
    THEORY-019, Proposed.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a pair of centred representations of
  the same width with the same Gram matrix but different readout kernels
  K = X G⁻¹ Xᵀ/M for some b > 0, or with different Gram matrices but the
  same K; or, for b = 0, two full-column-rank representations with the same
  column space that are not related by an invertible linear map.
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: formal-apparatus
grounds:
- THEORY-008
- THEORY-004
- THEORY-723
rests_on:
- CLAIM-290
summary: >-
  The proved core of [CLAIM-269](CLAIM-269.md). What a regularized linear readout decodes
  is a function of K_X = X G⁻¹ Xᵀ/M, with G = aC_X + bI ([THEORY-008](../theory.d/THEORY-008.md)). For
  b > 0, K_X and the Gram matrix XXᵀ determine each other, by a monotone
  map on the shared eigenvalues; and equal Gram matrices mean an
  orthogonal transformation ([CLAIM-290](CLAIM-290.md), [THEORY-004](../theory.d/THEORY-004.md)). For b = 0, K_X is the
  projection onto the column space, which fixes X only up to an invertible
  linear map, as for a softmax layer ([THEORY-723](../theory.d/THEORY-723.md)).
supports:
- CLAIM-269
---

# CLAIM-379: On a finite set of stimuli, regularized linear readouts with ridge b > 0 cannot tell apart two centred representations of the same width exactly when one is an orthogonal transformation of the other, and the unregularized CCA member cannot tell apart representations with the same column space, which differ by an invertible linear map

## The claim

Let X be an M × d representation of M stimuli, centred, with
C_X = XᵀX/M. [THEORY-008](../theory.d/THEORY-008.md) gives the decoded signal of a regularized linear
readout as K_X z, with K_X = X G⁻¹ Xᵀ/M and G = aC_X + bI. Two
representations are indistinguishable to such readouts when K_X = K_Y,
and distinguishable when K_X ≠ K_Y, since then some task z has
K_X z ≠ K_Y z.

**The kernel fixes the Gram matrix when b > 0.** Write the thin SVD
X = USVᵀ. Then C_X = VS²Vᵀ/M, and

K_X = U diag(s²/(as² + bM)) Uᵀ, while Γ_X = XXᵀ/M = U diag(s²/M) Uᵀ.

So K_X and Γ_X have the same eigenvectors, and each eigenvalue γ of Γ_X
goes to k = γ/(aγ + b), with zero going to zero. For b > 0 the map
t ↦ t/(at + b) has derivative b/(at + b)² > 0 on t ≥ 0, so it is
injective, with values below 1/a. Inverting it eigenvalue by eigenvalue
gives Γ_X = bK_X(I − aK_X)⁻¹. Equal kernels therefore mean equal Gram
matrices, and the converse is immediate.

**Equal Gram matrices mean an orthogonal map.** Two finite representation
matrices of the same width with the same Gram matrix differ by an
orthogonal transformation ([CLAIM-290](CLAIM-290.md)); with centring, by a translation and
an orthogonal transformation ([THEORY-004](../theory.d/THEORY-004.md)). So for b > 0, two centred
representations of the same width are indistinguishable to every such
readout exactly when one is an orthogonal transformation of the other.

**The CCA member sees only the column space.** For a = 1, b = 0,
K_X = U Uᵀ, the orthogonal projection onto the column space of X. If X and
Y have full column rank and the same column space, then Y = XA for an
invertible A, and every invertible A preserves the column space. So the
CCA member fixes a representation only up to an invertible linear map.
That is the freedom [THEORY-723](../theory.d/THEORY-723.md) and [THEORY-018](../theory.d/THEORY-018.md) find in a softmax model's
final layer.

## What it does not say

- **That kernels fix a representation up to the symmetry of the observed
  data.** That is [CLAIM-269](CLAIM-269.md)'s further clause, grounded on [THEORY-002](../theory.d/THEORY-002.md), and
  it is about converging kernels, not the orthogonal freedom of one
  representation.
- **Anything about nonlinear probes.** The family is the regularized
  linear readouts of [THEORY-008](../theory.d/THEORY-008.md).
- **Anything for infinitely many stimuli.** [THEORY-008](../theory.d/THEORY-008.md) is Active only on a
  finite stimulus set.
