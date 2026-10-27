---
number: 971
status: Active
formerly:
- THEORY-tmp7rb6m
title: 'A unit that thresholds a pre-activation equal to a term depending only on one operand plus a term depending only on the other cannot be active on exactly the pairs with a given sum when that sum has two decompositions: if it is active on (x, y) and (z, w), it is active on (x, w) or on (z, y); so a sum computed from separately represented operands needs an earlier unit that combines them, as Ameisen et al. argue for addition in language models'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1185. The argument is the "parallelogram
    constraint" of Ameisen et al.'s addition case study, stated there in a
    footnote; the record re-derived it step by step below (ADR-047 v2). The
    record states the premise as additive separability, which is what the
    proof uses, where the article says "an affine function of the
    operands".
tags:
- representation-learning
- mathematics
date: '2026-10-26'
source:
- LIT-1552
summary: >-
  Ameisen et al. (2025), [LIT-1552](../literature.d/LIT-1552.md), read in [NOTE-1185](../notes.d/NOTE-1185.md), re-derived
  here. It is why their addition graphs contain "lookup table" features
  between operand features and sum features. Whether a given unit in a
  trained model meets the premise is an empirical matter: attention
  patterns that depend on both operands, or any earlier nonlinearity that
  mixes them, break it, and that mixing is exactly the intermediate step
  the result says is required.
---
<!-- inactive-ok-file: THEORY-022 — Proposed; the neighbouring account of modular addition, named, nothing here rests on it -->
# THEORY-971: A unit that thresholds a pre-activation equal to a term depending only on one operand plus a term depending only on the other cannot be active on exactly the pairs with a given sum when that sum has two decompositions: if it is active on (x, y) and (z, w), it is active on (x, w) or on (z, y); so a sum computed from separately represented operands needs an earlier unit that combines them, as Ameisen et al. argue for addition in language models

## Source

Ameisen et al. (2025), *Circuit Tracing*, [LIT-1552](../literature.d/LIT-1552.md), read in
[NOTE-1185](../notes.d/NOTE-1185.md): "Addition Case Study", the paragraph on lookup table
features and its footnote, and "Global Weights in Addition".

## What was actually shown

An argument, checked by the record step by step.

**Premise.** A unit on inputs (a, b) has pre-activation h(a, b) = u(a) +
v(b) + c, for any functions u and v, and is active when h exceeds a
threshold θ. (A ReLU has θ = 0; a JumpReLU has its own θ.)

**Step 1.** For any x, z (first operands) and y, w (second operands),
h(x, y) + h(z, w) = u(x) + v(y) + u(z) + v(w) + 2c = h(x, w) + h(z, y).

**Step 2.** If the unit is active on (x, y) and (z, w), the left side
exceeds 2θ. So does the right, and a sum of two numbers exceeds 2θ only if
one of them exceeds θ. The unit is active on (x, w) or on (z, y).

**Step 3.** Suppose x + y = z + w = s with x ≠ z. Then y ≠ w, and (x, w)
and (z, y) have sums s + (w − y) and s − (w − y), neither equal to s. A unit
active on both (x, y) and (z, w) is therefore active on some pair whose
sum is not s. The article's example: a "sum = 5" unit that fires on 1 + 4
and 2 + 3 must fire on 1 + 3 or on 2 + 4. The same holds for a sum mod 10,
taking the sums mod 10, as long as w − y is not 0 mod 10.

**Step 4.** In a transformer at the "=" token, a feature whose inputs are
operand features carried there by frozen attention meets the premise, since
its pre-activation is the sum of what each operand's path contributes. Such
a feature cannot be a general sum detector. Something earlier must combine
the two operands nonlinearly. The article finds such units: "lookup table"
features, active on conditions of the form condition₁(a) AND condition₂(b)
(for instance, first operand ending in 6 and second ending in 9), which
feed "sum = _5" features.

**What could have come out otherwise.** As an argument, nothing. What the
article adds empirically is that the intermediate units in Claude 3.5
Haiku and 18L are of the lookup-table kind (ones-digit pairs and
magnitude-range pairs), observed in operand plots over all 10,000 prompts
"calc: a+b=", a, b < 100.

## What this does not say

- **Not that every trained model uses lookup tables.** The result forces
  some combining step before an exact sum unit, not its form. A network can
  combine operands by multiplying characters, as the grokking network of
  [THEORY-022](THEORY-022.md) does, and the article itself places its features beside
  Kantamneni and Tegmark's Fourier subspaces.
- **Not that the premise holds of a given unit.** The article states it as
  "the preactivation of f is an affine function of the operands", which is
  stronger than needed and is not checked unit by unit. Attention patterns
  that depend on both operands, or an MLP at "=" before the unit, can break
  separability.
- **Not about units that are only approximately sum detectors.** A unit
  may fire on most pairs with sum s and a few others; the result only
  excludes exactness on sums with two decompositions.

## Connections

- **[THEORY-022](THEORY-022.md).** Both are about how a network computes a sum from two
  separately represented inputs. [THEORY-022](THEORY-022.md)'s network forms products of
  characters; this result says a single thresholded additive step cannot
  form an exact sum detector, so some such combining step is needed in
  either.
