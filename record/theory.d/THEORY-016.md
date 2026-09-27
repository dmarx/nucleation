---
number: 16
status: Active
formerly:
- THEORY-tmpw2brf
title: 'An operational theory admits a generalized-noncontextual model exactly when its GPT admits a positive quasiprobability representation, and for a tomographically local theory any diagram-preserving such model is an exact frame with exactly as many ontic states as the GPT''s dimension'
version: 1
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-09-27'
source:
- LIT-003
- LIT-007
- LIT-073
summary: >-
  Schmid et al. (2020), [LIT-003](../literature.d/LIT-003.md), Prop 3.2, Prop 3.4, Cor 3.5, Thm 4.1, Cor
  4.2, Prop 4.3 — proved. Spekkens's odd-d stabilizer Wigner representation
  ([LIT-007](../literature.d/LIT-007.md)) is a worked instance. The theorem gives no test for whether a
  positive representation exists.
extended_by:
- THEORY-014
- THEORY-015
---

# THEORY-016: An operational theory admits a generalized-noncontextual model exactly when its GPT admits a positive quasiprobability representation, and for a tomographically local theory any diagram-preserving such model is an exact frame with exactly as many ontic states as the GPT's dimension

## Source

Schmid et al. (2020), [LIT-003](../literature.d/LIT-003.md), Def. 3.1, Props 3.2 and 3.4, Cor 3.5, Thm 2.8, Thm 4.1 (proof in App. B), Cor 4.2, Prop 4.3, §5.2, App. A ([NOTE-017](../notes.d/NOTE-017.md)). Worked instance: Spekkens (2014), [LIT-007](../literature.d/LIT-007.md), §IV.A. Background on GPTs: [LIT-073](../literature.d/LIT-073.md).

## What was actually shown

Spekkens's generalized noncontextuality asks that operationally equivalent procedures — ones no preparation or measurement can tell apart — receive identical representations in the ontological model. [LIT-003](../literature.d/LIT-003.md) states it for arbitrary compositional scenarios (Def. 3.1) and proves that a noncontextual ontological model of an operational theory exists iff its GPT admits an ontological model (a simplex embedding) iff it admits a positive quasiprobabilistic model (Props 3.2, 3.4, Cor 3.5), with no tomographic-locality assumption. For tomographically local GPTs, every diagram-preserving quasiprobabilistic map has the form M(T) = χ_B ∘ T ∘ χ_A⁻¹ (Thm 4.1), so a noncontextual model has |Λ_A| = dim A (Cor 4.2) and is an exact, non-overcomplete frame (Prop 4.3); §5.2 shows tomographic locality is needed for the count. A GPT has no contexts at all (App. A), which is where Kochen–Specker measurement contexts become invisible.

Spekkens's quadrature/stabilizer subtheory for odd d is a worked instance: its Wigner representation is an ontological model ([LIT-007](../literature.d/LIT-007.md) §IV.A), hence noncontextual, and [NOTE-017](../notes.d/NOTE-017.md) checked the d^(2n) count for small cases.

## What this does not say

- How to decide whether a positive representation exists (§4.5).
- Anything for overcomplete frames (the Q and P functions) or excess-baggage models, which diagram preservation rules out by fiat, or for theories without tomographic locality, such as real quantum theory.
- That the ontic states are unique up to relabelling; uniqueness is up to an invertible real linear map (Thm 4.7).
- That Catani et al.'s toy field theory ([LIT-019](../literature.d/LIT-019.md)) is noncontextual; that paper asserts it without proof ([NOTE-018](../notes.d/NOTE-018.md)).
