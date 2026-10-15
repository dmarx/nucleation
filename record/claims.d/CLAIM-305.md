---
number: 305
status: Active
formerly:
- CLAIM-tmp0pdrg
title: 'Resolving a singularity by blow-up reparametrizes the states and adds no
  observation, so it cannot make indistinguishable states distinguishable: every
  point over a singular point gives the same distribution, and the Fisher information
  can stay degenerate there; what the resolution buys is a normal form for the divergence,
  and so the learning coefficient'
version: 1
role: thesis
defeated_if: >-
  A blow-up π of a parameter space and a model p(x | w) such that two points u ≠
  u′ with π(u) = π(u′) give different distributions p(x | π(u)) ≠ p(x | π(u′)).
  The composition rules this out, so the claim falls only if the model is not pulled
  back through π, which is then a different model.
tags:
- learning-theory
- mathematical-statistics
date: '2026-10-15'
line: formal-apparatus
grounds:
- THEORY-087
summary: >-
  The owner's LEGO monograph says, in Part I (chapters 4, 6, 7, 9, the Overview
  and "Definitions and Theorems"), that blow-up "restores identifiability", "introduces
  new observables" and makes the Fisher information non-degenerate, and maps it
  onto splitting a LEGO bin. The pulled-back model is p(x | π(u)), a function of
  u only through π(u), so every point of the exceptional divisor gives the distribution
  of the singular point. In p(x | a, b) = N(ab, 1), the chart a = u, b = uv gives
  mean u²v and a Fisher matrix of zero all along u = 0. Splitting a bin is refining
  the observable, which can separate states. [MOM-CLM-099](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-099.md) records that the monograph
  uses "blow-up" in three senses; this records why the analogy cannot hold in any
  of them.
---
<!-- inactive-ok-file: THEORY-087 — Proposed; an account cited for what it states, nothing here rests on its being settled -->

# CLAIM-305: Resolving a singularity by blow-up reparametrizes the states and adds no observation, so it cannot make indistinguishable states distinguishable: every point over a singular point gives the same distribution, and the Fisher information can stay degenerate there; what the resolution buys is a normal form for the divergence, and so the learning coefficient

## The claim

The monograph, Part I, "7. just the math": blow-up "introduces **new
observables** or latent variables that allow one to **disentangle**
previously indistinguishable states", and its final theorem lists, among
what resolution achieves, "Discriminability is locally restored". "Definitions and Theorems",
Theorem 3.2: "There exists a blow-up π such that in the new coordinates u,
the Fisher information matrix I(u) is non-degenerate." Chapter 9:
"Blow-Up as Restoration of Cramér–Rao". The LEGO reading, throughout:
splitting the "slope" bin into finer bins is the blow-up.

**Nothing observed changes.** A blow-up is a proper map π from a new
parameter space onto the old. The model on the new space is
p(x | π(u)). It depends on u only through π(u), so if π(u) = π(u′) the
two points give one distribution. The exceptional divisor is the set of
points mapped to the singular point, so all of it gives the singular
point's distribution. States that no data could tell apart before are
still not told apart, and there are now more of them.

**The Fisher information can stay degenerate.** Take x ~ N(ab, 1), with
the true distribution N(0, 1). The divergence is K(a, b) = (ab)²/2, singular
along the axes. In the chart a = u, b = uv, the mean is u²v and
K = u⁴v²/2, a normal crossing. The gradient of the mean is (2uv, u²), zero
at every point with u = 0. So the Fisher matrix is zero along the
exceptional divisor, and Theorem 3.2 fails for this model. It was checked
here by finite differences at v = −2, 0.5 and 3. In general, a normal
crossing K = Π u_j^{2k_j} has a zero Hessian at the origin whenever any
k_j ≥ 2, or whenever two or more coordinates appear.

**What resolution does buy.** The normal form lets the divergence's
behaviour near the true parameter be read off. It gives the real log
canonical threshold and so the Bayesian complexity penalty λ log n, in
place of (d/2) log n ([THEORY-087](../theory.d/THEORY-087.md)). That is a statement about how hard
learning is near the singularity. It is not one about separating the
states there.

**What splitting a LEGO bin is.** Replacing a sorting rule f by a finer f′
(f a function of f′) is refining the observation. It is a more
informative experiment, and it can separate brick types that f put
together. That is the comparison of experiments the record holds in its
Blackwell claims (for example [CLAIM-126](CLAIM-126.md)), not resolution of singularities.
The monograph's analogy joins the two because both are described as
"separating what was collapsed". [MOM-CLM-099](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-099.md) records the same
word used for three different operations. This claim adds that none of
them is a way of gaining observations.

## Why it is Active

The first point is the definition of a pulled-back model. The second is a
two-line computation, checked numerically. The third is [THEORY-087](../theory.d/THEORY-087.md)'s
reading of Watanabe's result.

## What it does not say

- Not that blow-up is useless for epistemology. The learning coefficient
  is a real measure of how much the data can say near a singularity.
- Not that the monograph's identifiability material is wrong.
  [MOM-CLM-135](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-135.md) grades its quotient construction correct. The error is in
  the step from resolution to discriminability.
