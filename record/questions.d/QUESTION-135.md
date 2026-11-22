---
number: 135
status: Open
formerly:
- QUESTION-tmpw9b04
title: 'When does spectral differentiation among learned features correspond to stabilizing coexistence among the processes that implement them, and what besides the feature geometry decides it?'
version: 4
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added, from the readings of Mehta et al. and
    Chizat and Bach. The question is unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: LEAD-049's Theorem B (CLAIM-tmp6kclm)
    bounds each specialist's recovery rate below by its abundance times
    its niche vector's squared distance from the span of the others, and
    so by abundance times λ_min(A). The question is unchanged.
- version: 4
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: in LEAD-016's run (CASE-tmpnti0m) a
    rare specialist's recovery followed its residual direction among
    learned operator vectors. The question is unchanged.
tags:
- representation-learning
- ecology
- complex-systems
date: '2026-10-18'
line: distributed-agency
refines:
- QUESTION-083
summary: >-
  From the synthesis the owner relayed on 2026-10-18. In symmetric
  resource-mediated competition the interaction matrix is the Gram matrix
  of the components' feature vectors, A = UᵀU, so representational
  redundancy and competitive overlap are one object ([CLAIM-369](../claims.d/CLAIM-369.md)). In
  the two-component case invasion growth equals λ_min(A) ([CASE-118](../cases.d/CASE-118.md)).
  But the same A supports coexistence or exclusion depending on the growth
  rates. An answer says when the Gram spectrum of a learned representation
  predicts that the processes carrying its features will coexist, and what
  else, such as supply, task distribution or evaluation opportunities, has
  to be fixed for it to.
---
<!-- inactive-ok-file: CASE-tmpnti0m — Proposed, filed 2026-11-22 by LEAD-016's study and cited in the note of that date -->
<!-- inactive-ok-file: CLAIM-tmp6kclm CLAIM-tmpdsv4t CASE-tmp5sk3q — Proposed, filed 2026-11-22 by LEAD-049 and cited in the note of that date -->
<!-- inactive-ok-file: CLAIM-193 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->

# QUESTION-135: When does spectral differentiation among learned features correspond to stabilizing coexistence among the processes that implement them, and what besides the feature geometry decides it?

## Why it is a question

The record already treats a representation as fixed by its kernel up to
symmetries ([THEORY-004](../theory.d/THEORY-004.md)), and holds that a linear probe family sees only
differences in normalized kernel ([CLAIM-193](../claims.d/CLAIM-193.md)). [CLAIM-369](../claims.d/CLAIM-369.md) shows that,
in symmetric resource competition, the kernel is also the competition
matrix. That suggests that how differentiated a set of features is
spectrally might predict whether the processes implementing them coexist.

[CASE-118](../cases.d/CASE-118.md) shows where the suggestion holds and where it fails. With
equal growth rates the rare component's invasion growth is exactly
λ_min(A) = 1 − ρ. With growth rates 1 ± δ the same A supports
coexistence only for |δ| < (1 − ρ)/(1 + ρ). So feature geometry is
necessary context and not sufficient. The supply, meaning the tasks,
resources or evaluation opportunities the system offers, also decides.
That is [CLAIM-152](../claims.d/CLAIM-152.md)'s target-relativity: what a representation supports
depends on what it is asked for.

## What would answer it

Conditions, in a stated class of learning systems, under which the Gram
spectrum of the learned features predicts the recovery rates of the
processes carrying them, together with the further quantities that must
be fixed for the prediction to hold. The answer should keep three
measurements apart:

- structural differentiation, from feature geometry;
- functional differentiation, from conditional performance across
  contexts;
- dynamical stabilization, from recovery when rare and from persistence.

It bears on [QUESTION-125](QUESTION-125.md). A change in feature geometry, such as an
eigengap opening, and a change in coexistence, such as a component
becoming able to invade, need not happen at the same parameter values. A
model in which they come apart in either direction would be informative.

## What would not answer it

Heterogeneous embeddings, or a well-conditioned Gram matrix, with no
account of recovery dynamics.

## Note of 2026-10-29: a large-system instance, and a model with no spectral condition

Two works read on this date bear on the question.

- Mehta, Cui, Wang and Marsland, [LIT-1231](../literature.d/LIT-1231.md) ([NOTE-1395](../notes.d/NOTE-1395.md)): in random
  quadratic programming the variance σ_c of the constraint vectors sets
  how many components survive, and more differentiated constraints
  coexist more. That is a large-system instance of the suggestion above,
  with the supply K and the costs m entering through the growth rates, as
  [CASE-118](../cases.d/CASE-118.md) found for two components.
- Chizat and Bach, [LIT-1232](../literature.d/LIT-1232.md) ([NOTE-1367](../notes.d/NOTE-1367.md)), supply no spectral
  condition. Their coexistence notion is first-order, the sign of F′, not
  the growth-rate comparison [CASE-118](../cases.d/CASE-118.md) uses.

The question is unchanged and stays Open.

## Note of 2026-11-04: A6's three geometries, and the persistence edge, from "Organizational Nucleation and SLT"

A6 answered the owner's U6, which treated "ecological coexistence as an
organization that can be appropriately characterized by a compatibility
complex", with this question's suggestion. It did not cite this question.

**What A6 restated.** It separated three geometries: "Representational
geometry", "Ecological compatibility geometry" and "Singular statistical
geometry". "They are not identical mathematical invariants, but they can be
generated by the same learning system." Its pipeline runs from shared
capacity through differentiated learning to a "New compatibility regime"
and "Maintained specialization". It restates [CLAIM-369](../claims.d/CLAIM-369.md) and [CASE-118](../cases.d/CASE-118.md) correctly.

**What it adds: the persistence edge.** "If we define the compatibility
complex in terms of robust persistence, its edge corresponding to joint
viability appears at that threshold." Take demand i to be component i's
persistence in [CASE-118](../cases.d/CASE-118.md). Each vertex is always present. The edge {1, 2}
appears exactly when |δ| < (1 − ρ)/(1 + ρ). So continuous differentiation (ρ
falling) gives a discrete change in the complex, with β₀ going from 2 to 1.

**A qualification.** Any strict-inequality criterion gives a discrete change
of this kind. By itself the edge says nothing about an SLT phase boundary, as
A6 granted: "an ecological coexistence threshold is not automatically an SLT
phase boundary". The edge marks feasibility. Stability still needs this
question's recovery dynamics. At ρ = 1, UᵀU, the Hessian of [CLAIM-369](../claims.d/CLAIM-369.md)'s
objective, is singular, so differentiation removes one degeneracy. That
holds only for this linear model.

[CLAIM-554](../claims.d/CLAIM-554.md) reads niche differentiation as relief of frustration among
persistence demands.

No status changes.

## Note of 2026-11-22: a k-component spectral bound on recovery

[LEAD-049](../leads.d/LEAD-049.md) proved a k-component version of [CASE-118](../cases.d/CASE-118.md)'s identity
([CLAIM-tmp6kclm](../claims.d/CLAIM-tmp6kclm.md), Theorem B). It holds in [CLAIM-369](../claims.d/CLAIM-369.md)'s class at fixed
features, with the Gram matrix A positive definite and an interior
equilibrium n*. A specialist i is removed and reintroduced rare against
the others' re-equilibrated community. Its recovery growth satisfies

  λ_i ≥ n*_i / (A⁻¹)_ii = n*_i d_i² ≥ n*_i λ_min(A).

Here d_i is the distance of i's feature vector from the span of the
others'. Equality holds in the first inequality when no other component
goes extinct in i's absence. [CASE-tmp5sk3q](../cases.d/CASE-tmp5sk3q.md)'s 7,981 random cases meet the
bound everywhere. In the 1,666 with a secondary extinction it is strict.

For this question the result sharpens [CASE-118](../cases.d/CASE-118.md)'s finding. What predicts
a component's recovery is not the spectrum as a whole. It is the
component's own residual direction, d_i², the Schur complement of A at i,
weighted by its abundance. λ_min(A) is only the worst case over
components. The abundance n* = A⁻¹r carries the supply, which is the
"what else" the question asks for. In this class the answer is exact:
feature geometry (d_i) and supply (n*_i) together set recovery. That
holds only while the features are fixed. When they adapt, a component's
recovery against re-adapted residents can be negative ([CLAIM-tmpdsv4t](../claims.d/CLAIM-tmpdsv4t.md)).

The question is unchanged and stays Open.

## Note of 2026-11-22: the residual direction in a learning population

In LEAD-016's reduced run of CASE-117 (CASE-tmpnti0m), the operators'
learned parameter vectors play the part of features. At the snapshot,
the rare specialist's squared distance d² from the span of the other
operators' normalized vectors was measured.

| condition | d² | recovery from 10⁻³ |
|---|---|---|
| no spare operator | 1.0 | positive, every seed |
| two spares, multiplicative rule | 0.000 | about zero |
| two spares, gating | 0.18 | negative |

Under the multiplicative rule a spare had co-learned the specialist's job,
with cosine 0.998. Under gating the spare learned it during the window.
This fits the note of 2026-11-22's reading of CLAIM-tmp6kclm: a
component's own residual direction, not the spectrum as a whole, is what
recovery tracks. Here it is observed in an adaptive population, not proved.

The geometry at the snapshot did not predict the gating case. There the
spare was still only partly aligned and became redundant during the test.
What else must be fixed includes the learning that happens while the
specialist is rare. The question is unchanged and stays Open.
