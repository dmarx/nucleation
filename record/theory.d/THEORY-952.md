---
number: 952
status: Active
formerly:
- THEORY-tmpeglfj
title: 'In Wald''s sequential probability ratio test, which samples until the likelihood ratio of two simple hypotheses leaves an interval (B, A), the realized error probabilities satisfy α/(1 − β) ≤ 1/A and β/(1 − α) ≤ B whenever the test terminates with probability one, with or without independent observations; so the boundaries A = (1 − β)/α and B = β/(1 − α), set with no distribution theory, give errors α′ ≤ α/(1 − β), β′ ≤ β/(1 − α) and α′ + β′ ≤ α + β, and they would be exact only if the ratio stopped on the boundary'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-1165, the reading of the copy the owner
    supplied on 2026-10-25. The test is Wald's (3.8)–(3.10), the
    inequalities his (3.16)–(3.19) and (3.24)–(3.30). They are re-derived
    below and checked by simulation, which meets the condition for Active
    under ADR-047 v2. The Bayesian reading of the walk with a prior is
    Wald's §3.1. Its use for the record's replicator walk is the
    record's.
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-25'
source:
- LIT-1523
summary: >-
  Wald (1945), [LIT-1523](../literature.d/LIT-1523.md), read in [NOTE-1165](../notes.d/NOTE-1165.md). The boundaries of a
  sequential likelihood-ratio test follow from the error rates by a
  two-line argument that needs only termination, so the test needs no
  sampling distribution. The approximate boundaries are conservative in
  sum. Either error alone may rise, but only by a factor 1/(1 − β) or
  1/(1 − α) at most. Nothing here says how many observations the test
  takes or that it is optimal: that is [THEORY-951](THEORY-951.md), and it needs
  i.i.d. observations.
supports:
- CLAIM-453
---
# THEORY-952: In Wald's sequential probability ratio test, which samples until the likelihood ratio of two simple hypotheses leaves an interval (B, A), the realized error probabilities satisfy α/(1 − β) ≤ 1/A and β/(1 − α) ≤ B whenever the test terminates with probability one, with or without independent observations; so the boundaries A = (1 − β)/α and B = β/(1 − α), set with no distribution theory, give errors α′ ≤ α/(1 − β), β′ ≤ β/(1 − α) and α′ + β′ ≤ α + β, and they would be exact only if the ratio stopped on the boundary

## Source

Wald (1945), "Sequential Tests of Statistical Hypotheses", *The Annals of
Mathematical Statistics* 16(2): 117–186, [LIT-1523](../literature.d/LIT-1523.md), read in full in
[NOTE-1165](../notes.d/NOTE-1165.md) from the JSTOR scan the owner supplied. The test is
(3.8)–(3.10), its Bayesian motivation (3.1)–(3.7), and termination (3.11).
The inequalities are (3.12)–(3.19) and the practical boundaries
(3.24)–(3.30). The derivations below follow Wald's and are written out by
the record.

## What was actually shown

**The test.** Let p_im be the joint density of the first m observations
under Hᵢ. Accept H₁ the first time p₁ₘ/p₀ₘ ≥ A, accept H₀ the first time
p₁ₘ/p₀ₘ ≤ B, and otherwise observe again, with 0 < B < A. For i.i.d.
observations, log p₁ₘ/p₀ₘ = Z_m = z₁ + … + z_m with zᵢ = log f₁(xᵢ)/f₀(xᵢ),
and the test stops when Z_m leaves (log B, log A).

**Where it comes from (§3.1).** With prior probabilities g₀, g₁, Bayes gives
posterior odds g₁ₘ/g₀ₘ = (g₁/g₀)·p₁ₘ/p₀ₘ. Accepting H₁ when g₁ₘ ≥ d₁ and H₀
when g₀ₘ ≥ d₀, with d₀, d₁ > ½, is the pair of thresholds (3.6)–(3.7) on
p₁ₘ/p₀ₘ, constants that do not depend on m. So the posterior log odds are
the walk shifted by the prior log odds, log(g₁/g₀) + Z_m. The SPRT is that
rule with the prior absorbed into A and B.

**The inequalities.** Let Q₁ be the set of sample paths that stop
accepting H₁. On each such path, stopped at n, p₁ₙ ≥ A p₀ₙ. Summing
(integrating) over Q₁ gives P₁(Q₁) ≥ A P₀(Q₁), that is 1 − β ≥ Aα (3.16).
Likewise P₁(Q₀) ≤ B P₀(Q₀), that is β ≤ B(1 − α) (3.17). The only other fact
used is P(Q₀ ∪ Q₁) = 1 under each hypothesis, so that P₀(Q₀) = 1 − α and
P₁(Q₁) = 1 − β. Independence enters only through termination, and Wald
notes that (3.11) "can be shown to hold also for dependent observations
under very general conditions" (p. 130).

**The boundaries.** Given target errors (α, β), put A = (1 − β)/α and
B = β/(1 − α). The realized errors α′, β′ then satisfy
α′/(1 − β′) ≤ α/(1 − β) and β′/(1 − α′) ≤ β/(1 − α) (3.26)–(3.27). The first
gives α′ ≤ α′/(1 − β′) ≤ α/(1 − β), and the second β′ ≤ β/(1 − α)
(3.28)–(3.29). Multiplying the first by (1 − β)(1 − β′) and the second by
(1 − α)(1 − α′), then adding, gives α′ + β′ ≤ α + β (3.30). So the
approximate boundaries never weaken the test in sum.

**Why they are inequalities.** The ratio jumps past the boundary when it
stops. If it stopped exactly on A or B, every inequality above would be
an equality. Wald: "If fractional observations were possible … A(α, β)
and B(α, β) would be exactly equal to (1 − β)/α and β/(1 − α)
respectively" (p. 132).

**Checked by simulation** (numpy, when filed; N(μ, 1),
H₀ μ = 0 against H₁ μ = δ, the boundaries above):

| α, β, δ | runs | α′, β′ | α′/(1 − β′) vs 1/A | β′/(1 − α′) vs B | α′ + β′ |
|---|---|---|---|---|---|
| .05, .05, .5 | 20,000 | .035, .039 | .037 ≤ .053 | .040 ≤ .053 | .074 ≤ .10 |
| .01, .10, .5 | 20,000 | .007, .073 | .008 ≤ .011 | .073 ≤ .101 | .080 ≤ .11 |
| .05, .05, .2 | 20,000 | .046, .043 | .048 ≤ .053 | .045 ≤ .053 | .089 ≤ .10 |
| .05, .05, .05 | 4,000 | .047, .046 | .049 ≤ .053 | .048 ≤ .053 | .093 ≤ .10 |

The slack shrinks as δ falls and the overshoot with it, as Wald says it
should. What could have failed: the realized errors could have exceeded
the bounds when the overshoot is large (δ = .5 is a large step). They
stayed below in every case.

## What this does not say

- **Not how long the test runs, or that it is optimal.** Those need i.i.d.
  observations and the overshoot to be neglected ([THEORY-951](THEORY-951.md)).
- **Not that both errors fall.** Only their sum is guaranteed not to rise.
  One error can exceed its target, by at most a factor 1/(1 − β) or
  1/(1 − α).
- **Not anything for composite hypotheses directly.** For those, Wald
  tests against a chosen simple alternative, or against a mixture over a
  weight function, which bounds a weighted average of the second-kind
  errors (§6).
- **Not that a walk without boundaries is a test.** The SPRT is the
  log-likelihood-ratio walk together with its stopping rule.

## Connections

- **[CASE-155](../cases.d/CASE-155.md)** (note of 2026-10-25) and **[CLAIM-453](../claims.d/CLAIM-453.md).** The replicator's
  log share odds, moving by each observation's log likelihood ratio from
  the prior log odds, are §3.1's posterior log odds log(g₁/g₀) + Z_m. They
  are Wald's walk, and the SPRT's statistic. They become the SPRT when
  commitment is a fixed bound on them, which the claim lists as a
  condition.
- **[THEORY-068](THEORY-068.md)** takes the SPRT through Bogacz et al. ([LIT-569](../literature.d/LIT-569.md)). This
  account supplies the primary statement of the test and its boundaries.
