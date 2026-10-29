---
status: Active
title: "Weiss's mark of a system, that the whole varies far less than the summed variances of its parts, is met by any aggregate of independent parts when the whole is measured as their average; when it is measured as their sum, it holds only if the parts' fluctuations compensate one another, with ∑ᵢ<ⱼ Cov(xᵢ, xⱼ) close to −½ ∑ᵢ Var(xᵢ)"
version: 1
tags:
- complex-systems
- philosophy-of-biology
date: '2026-10-29'
source:
- LIT-tmptd6hn
summary: >-
  Nicholson (2026), [LIT-tmptd6hn](../literature.d/LIT-tmptd6hn.md), read in [NOTE-tmpo9v9c](../notes.d/NOTE-tmpo9v9c.md), reports Weiss's
  one formula, VS ≪ ∑ (va + … + vn), as a property "we would invariably
  find, if we studied any system", and as a way of identifying systems
  empirically. The variance of a sum settles what it can show. Active:
  an identity, checked numerically. It does not say Weiss's systems lack
  compensating covariance, only that the inequality as stated does not
  test for it.
---

# THEORY-tmp1244l: Weiss's mark of a system, that the whole varies far less than the summed variances of its parts, is met by any aggregate of independent parts when the whole is measured as their average; when it is measured as their sum, it holds only if the parts' fluctuations compensate one another, with ∑ᵢ<ⱼ Cov(xᵢ, xⱼ) close to −½ ∑ᵢ Var(xᵢ)

## Source

Nicholson (2026), [LIT-tmptd6hn](../literature.d/LIT-tmptd6hn.md), §5, reporting Weiss (1963, 1969a, 1971c,
1973, 1977, 1978); read in [NOTE-tmpo9v9c](../notes.d/NOTE-tmpo9v9c.md) from the Europe PMC full text.

## What was actually shown

**The inequality as given.** For each part a of a system S, measure "all
the fluctuations from the mean for a range of physical and chemical
parameters over a given period of time", call the cumulative record va,
and do the same for S, giving VS. Then "What we would invariably find, if
we studied any system in this way, is that the sum of the individual
variances of the parts is far greater than the total variance of the
whole":

VS ≪ ∑ (va + vb + vc + vd + … + vn)

Nicholson says it is "the only mathematical expression we find in Weiss's
theoretical writings about systems", used "sometimes as a way of
illustrating how one might go about empirically identifying systems in
nature" (§5).

**What it can show.** Read it with one scalar quantity xᵢ per part, and
the whole's quantity either their sum or their average. For any random
variables,

Var(∑ᵢ xᵢ) = ∑ᵢ Var(xᵢ) + 2 ∑ᵢ<ⱼ Cov(xᵢ, xⱼ).

- **Average.** Var((1/n)∑xᵢ) = (1/n²)[∑Var(xᵢ) + 2∑Cov]. With independent
  parts it is ∑v/n², far below ∑v for any n of more than a few. Every
  aggregate meets the inequality, so it cannot distinguish a system.
- **Sum.** With independent parts Var(∑xᵢ) = ∑v, and the inequality fails.
  It holds exactly when 2∑ᵢ<ⱼ Cov is close to −∑v, so that the parts'
  deviations cancel in the total. That is compensation, and it is a mark
  of regulation that an aggregate does not show.

**A numerical check** (numpy, 100 parts, 20,000 samples, seed 0; my
script): independent parts gave VS = 0.010 against ∑v = 100 for the
average and VS = 101 against ∑v = 100 for the sum. Parts held to a fixed
total, plus a small common fluctuation, gave VS ≈ 25 against ∑v ≈ 99 for
the sum, and the identity matched to three decimals.

**What could have failed.** If the inequality as stated separated systems
from aggregates, independent parts would have violated it under both
readings. They violate it only under the sum.

## What this does not say

- **That Weiss's systems lack compensation.** Cells and embryos may well
  show strongly negative covariance among parts in an extensive quantity.
  The point is that the inequality as reported does not require it, so
  finding VS ≪ ∑v is no evidence of it unless the quantity is extensive.
- **That Weiss meant the average.** The paper fixes neither the
  parameters nor how the whole's value is formed from the parts', and it
  sums variances across "a range of physical and chemical parameters",
  whose units differ. The two readings above are the simplest that make
  the formula a statement at all.
- **That variance reduction is the whole of Weiss's concept.** His
  definitions also require restoration "after non-destructive
  disturbances" (Weiss 1971c, quoted in §3), a dynamical property no
  single-time variance measures.
- **That any measurement was made.** Neither Nicholson nor the passages
  he quotes report a value of VS or of ∑v for any system.
