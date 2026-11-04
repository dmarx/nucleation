---
status: Proposed
title: 'Four model classes on one task with two contexts, targets ±1 and demands ŷ_A ≥ ½, ŷ_B ≤ −½: a shared scalar is regular and frustrated (λ = ½), a shared product ab is singular and frustrated (λ = ½, multiplicity 2), a context-split x ± d is regular and compatible (λ = 1), and x ± de is singular and compatible (λ = 1 against d/2 = 3/2), so an SLT invariant and the compatibility complex vary independently'
version: 1
standing: fictional
kind: construction
tags:
- learning-theory
- mathematical-statistics
- mathematics
date: '2026-11-04'
line:
- learned-structure
variant_of:
- CASE-115
- CASE-152
illustrates:
- CLAIM-347
summary: >-
  A8's Proposal B, from the exchange "Organizational Nucleation and SLT"
  (2026-11-04). A's three arms are compared under one set of demands:
  regular and frustrated, singular and frustrated, regular and compatible.
  The reader added a fourth arm, singular and compatible, so that the table
  cannot be read as "differentiation is anti-singular". Its point: neither
  the real log canonical threshold nor its multiplicity tells whether the
  demands are jointly realizable. The wording is A's, sharpened by the
  reader; adopting it is the owner's call.
---

# CASE-tmpbd03o: Four model classes on one task with two contexts, targets ±1 and demands ŷ_A ≥ ½, ŷ_B ≤ −½: a shared scalar is regular and frustrated (λ = ½), a shared product ab is singular and frustrated (λ = ½, multiplicity 2), a context-split x ± d is regular and compatible (λ = 1), and x ± de is singular and compatible (λ = 1 against d/2 = 3/2), so an SLT invariant and the compatibility complex vary independently

## The construction

The owner's U8 asked for CASEs the record lacks. A8 called this proposal
"probably the most directly relevant proposal to our recent discussion".

**The task.** Two equally frequent contexts, A and B, have targets y_A = 1
and y_B = −1. The demands are fixed throughout: ŷ_A ≥ ½ and ŷ_B ≤ −½. The
loss is squared error averaged over the two contexts.

**The arms.** Arms 1 to 3 are A8's. Arm 4 is the reader's.

1. **Shared scalar.** ŷ_A = ŷ_B = θ. L₁ = 1 + θ².
2. **Shared product.** ŷ_A = ŷ_B = ab. L₂ = 1 + a²b².
3. **Context split.** ŷ_A = x + d, ŷ_B = x − d. L₃ = x² + (d − 1)².
4. **Context split through a product.** ŷ_A = x + de, ŷ_B = x − de.
   L₄ = x² + (de − 1)².

## Results

The learning coefficient λ is for the excess loss over its minimum, with a
smooth positive prior near the minimum.

| arm | geometry | λ | nominal d/2 | joint demands |
|---|---|---|---|---|
| 1, shared scalar | regular | ½ | ½ | frustrated |
| 2, shared product | singular | ½, multiplicity 2 | 1 | frustrated |
| 3, context split | regular | 1 | 1 | compatible |
| 4, split through a product | singular | 1 | 3/2 | compatible |

- **Arms 1 and 2.** Every output has the form (z, z), so no setting meets
  both demands. A8: "nothing about the original frustration has changed."
  Arm 2 is CASE-152's product singularity. Its λ equals Arm 1's. What makes
  it singular is the multiplicity, the log correction, and the gap below
  d/2. It does not have a lower λ.
- **Arm 3.** L₃ = ½[(x + d − 1)² + (x − d + 1)²] = x² + (d − 1)². At
  (x, d) = (0, 1) both demands are met exactly. This is CASE-115's split of
  θ, in rotated coordinates.
- **Arm 4.** The minimum set {x = 0, de = 1} is a smooth curve in ℝ³, of
  codimension 2, so λ = 1 < 3/2. Every point on it meets both demands.

**Checks by the reader.** L₃ was verified at random points. Monte Carlo
volume exponents of {K < ε} near the minimum came out as follows; the
scripts are scratch/formal/r2_rlct_and_arithmetic.py and
scratch/formal/r2_band_and_fourth_arm.py.

| excess loss | exponent | λ |
|---|---|---|
| θ² | 0.498 | ½ |
| a²b² | 0.398 | ½; the downward bias is the log factor at multiplicity 2 |
| x² + (d − 1)² | 0.988 | 1 |
| x² + (de − 1)² | 0.988 | 1 |

## What it shows and does not

**It shows that singularity and compatibility vary independently.** All
four combinations occur under the same declared demands. A8: "This
construction separates **representational redundancy from functional
differentiation**." Arm 2 "adds parameters and a genuine statistical
singularity but no new ability to satisfy the demands". Arm 4 shows the
converse: a singular model can also be one that relieves the frustration.

**It is a caution for QUESTION-133 and QUESTION-275.** A8: "It prevents us
from prematurely interpreting an SLT phase distinction as evidence of
improved organizational integration." A positive result must show "a
relationship between changes in the statistical geometry and changes in
*jointly realizable behavior*, rather than the mere presence of
singularities."

**Relief here is CLAIM-347's.** Arms 3 and 4 enlarge the attainable set
for the same acceptance sets. Arm 2 adds parameters without enlarging it.
CLAIM-305, now superseded, made the neighbouring point that resolving a
singularity adds no observation.

**It does not show a learning trajectory.** A8: "These are three fixed
model classes, not a demonstrated learning trajectory or Bayesian phase
transition." Whether a learnable architecture passes from Arm 1 or 2 to
Arm 3 or 4, and what happens to λ when it does, is the experiment A8
proposed next.
