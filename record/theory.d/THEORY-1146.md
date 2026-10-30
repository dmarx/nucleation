---
number: 1146
status: Active
formerly:
- THEORY-tmppip5e
title: 'Under confounding the partition of a variable X by what it predicts about a target Y can differ from its partition by what setting it does to Y, so the information bottleneck at full sufficiency can learn distinctions no intervention could use and miss ones only intervention reveals, as it did in two confounded toy models, while the causal information bottleneck, computed from observational data through a backdoor set, recovered the causal partition in all three toy models, projected gradient search finding it in 95 to 100 percent of runs'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted by the twenty-second status review, at the
    status review's ruling (the owner delegated these rulings;
    ADR-065; ADR-047 kind 3 for the narrowing): NOTE-1347 read the
    paper in full. The old title stated universally that under
    confounding the partitions differ and that the information
    bottleneck learns useless distinctions and misses causal ones;
    confounding makes that possible, not necessary, so the title now
    says "can" and reports what happened in the two confounded toy
    models. That the causal partition is the optimum is THEORY-1125.
    Whether search finds it on larger systems moves to
    QUESTION-tmprxak2, which this entry now bears on. The old title:
    "Under confounding the partition of a variable X by what it
    predicts about a target Y differs from its partition by what
    setting it does to Y, so the information bottleneck at full
    sufficiency learns distinctions no intervention could use and
    misses ones only intervention reveals, while the causal
    information bottleneck, computed from observational data through a
    backdoor set, recovers the causal partition; in three toy models
    projected gradient search found it in 95 to 100 percent of runs"
    The old promote_when: "Results on causal systems larger than toy
    SCMs, with confounding and a known causal partition, in which the
    information bottleneck at full sufficiency recovers the
    observational partition by p(y | x) and the causal bottleneck,
    computed through an adjustment set, recovers the partition by p(y
    | do(x)), reliably and with the optimiser's failure rate reported;
    or a case where the observational and causal partitions differ and
    the causal bottleneck does not find the latter."
tags:
- causality
- information-theory
date: '2026-10-29'
source:
- LIT-1802
bears_on:
- QUESTION-tmprxak2
summary: >-
  Simoes, Dastani and van Ommen (UAI 2025), [LIT-1802](../literature.d/LIT-1802.md), §8 and
  Appendices E–F, read in [NOTE-1347](../notes.d/NOTE-1347.md). Three SCMs with 7, 4 and 16
  values of X; ensembles of 4 to 12 optimisers; a penalty against unused
  values of T was needed at full control. The difference between the
  partitions follows from the definitions; what the experiments add is
  that the search finds the causal one, in toy problems only. Active as a
  report (ADR-065); whether search finds it at scale is QUESTION-tmprxak2.
---

<!-- inactive-ok-file: QUESTION-tmprxak2 — Open; the question this report leaves, cited as open -->

# THEORY-1146: Under confounding the partition of a variable X by what it predicts about a target Y can differ from its partition by what setting it does to Y, so the information bottleneck at full sufficiency can learn distinctions no intervention could use and miss ones only intervention reveals, as it did in two confounded toy models, while the causal information bottleneck, computed from observational data through a backdoor set, recovered the causal partition in all three toy models, projected gradient search finding it in 95 to 100 percent of runs

## Source

Simoes, Dastani and van Ommen (2025), [LIT-1802](../literature.d/LIT-1802.md), §8 (pp. 5–7) and
Appendices E–F (pp. 16–20) of arXiv 2410.00535v5; read in [NOTE-1347](../notes.d/NOTE-1347.md).

## What was actually shown

**Three SCMs** (Figs. 2 and 4). Odd and Even: X uniform on {0, …, 6}, Y its
parity with noise, no confounding. Confounded Addition: Y depends on
X₁ + X₂, and W confounds X₁ and Y. Genetic Mutations: Y = S + X₁ + X₂ +
(2 − X₃)X₁X₂ + noise, with the strain S driving X₃ and X₄. Only the joint
distribution and a backdoor set are given to the method (p. 6).

**The CIB.** At γ = 1 the causal ground truth (parity, X₁ + X₂, and the
four-valued θ(X)) was found in 100%, 98% and 95% of runs (pp. 6–7), with
ensembles of 4, 6 and 12 optimisers. At γ = 0 the abstractions carry no
information about X, and causal information gain does not decrease with γ,
in all three and for other noise settings (Figs. 1, 5).

**The IB.** Run on the same data, the ordinary bottleneck at γ = 1 finds
the ground truth only in the unconfounded Odd and Even case (Appendix F.2,
p. 18). On Confounded Addition it gives (X₁, X₂) = (0, 1) and (1, 0)
different values, though they have the same effect on Y (Table 1, p. 19).
On Genetic Mutations it does not separate X₃'s protective effect and is not
invariant in X₄, which has no effect on Y (Table 2, p. 20).

**My check.** On the Genetic Mutations SCM the observational partition has
ten classes and the causal one four ([NOTE-1347](../notes.d/NOTE-1347.md)).

**What could have failed.** The local search could have stuck in poor
optima, as the authors report it did before they added a penalty against
encoders that leave values of T unused (p. 17).

## What this does not say

- **That the method scales.** The largest X has 16 values; the authors
  expect local minima to need "modifications" at scale (p. 8).
- **That the IB's failure is a finding about the IB.** It follows from
  the definitions: the IB targets p(y | x). The experiment shows the
  difference matters in these cases.
- **That intermediate γ is meaningful.** Only monotonicity is checked
  there.
- **That the causal knowledge is free.** The backdoor set is an input;
  without one the causal partition is not identifiable this way.
- **That the abstractions reveal causal structure better than direct
  inspection.** The paper argues it (p. 7) and compares with nothing.

## Note of 2026-10-30: narrowed and promoted

The title said the partitions differ under confounding and that the
bottleneck learns and misses distinctions, as if always; it now says what
confounding makes possible and what the toy models showed. Whether the
search scales is [QUESTION-tmprxak2](../questions.d/QUESTION-tmprxak2.md).
