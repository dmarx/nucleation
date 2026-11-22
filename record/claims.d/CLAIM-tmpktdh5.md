---
status: Proposed
title: 'A probe family that supplied a system''s training signal does certify a preserved property when that property is bounded, by a stated inequality, by the probes'' value over contexts they cover, and that value is estimated on draws the system was not fitted to; optimizing against the probes then tightens the bound, the property depends on nothing they cannot see, and the training-signal limit holds only where the property outruns the probes or their coverage'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the step from the bound to the certificate: a property P,
  a probe family with value V over a context distribution μ, an
  inequality bounding P's failure by V over the contexts μ covers, and an
  estimate of V from draws of μ the system was not fitted to, from which
  the certificate does not follow at the stated confidence. In
  particular, an error in CLAIM-517's Pinsker and coverage steps, which
  are this claim's instance. It is not defeated by a case where a
  training probe fails to certify with no such bound, such as CASE-041:
  that is the case it leaves to CLAIM-266.
tags:
- model-comparison
- mathematics
- information-theory
- philosophy-of-science
date: '2026-11-22'
line:
- formal-apparatus
- records-of-inquiry
- distributed-agency
objects_to:
- CLAIM-266
rests_on:
- CLAIM-517
summary: >-
  Filed for LEAD-194, on the tension the curation entry of 2026-11-11
  (061331) named: CLAIM-266 says without qualification that probes
  supplying a training signal cannot certify what is preserved, while
  CLAIM-517's coverage step certifies viability from a distillation loss.
  This claim states the condition under which the training probes do
  certify: a stated inequality from their value, over the contexts they
  cover, to the preserved property, with the value estimated out of
  sample. It narrows CLAIM-266 to the case the condition fails, which is
  every case CLAIM-266 cites. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1803 — Proposed; cited as the boundary case CLAIM-266's note already names, nothing here rests on it -->

# CLAIM-tmpktdh5: A probe family that supplied a system's training signal does certify a preserved property when that property is bounded, by a stated inequality, by the probes' value over contexts they cover, and that value is estimated on draws the system was not fitted to; optimizing against the probes then tightens the bound, the property depends on nothing they cannot see, and the training-signal limit holds only where the property outruns the probes or their coverage

## The tension

[CLAIM-266](CLAIM-266.md)'s title says that a family of probes supplying an optimized
system's training signal "cannot also certify what the system preserves",
and that preservation "must be shown under probes not used to train it".
[CLAIM-517](CLAIM-517.md)'s coverage step takes a successor trained to forward KL ε
against a reference regulator under a context distribution μ, the
training signal, and certifies from that same quantity that a viable set
stays positively invariant: with each boundary context sampled with
probability at least μ_min, Pinsker gives TV ≤ √(ε/(2μ_min)) at each, so
ε < 2μ_min(γ/L)² suffices. The probe family that trained the successor
(KL to the reference under μ) is the one that certifies it. Read as
written, the two cannot both hold. Neither cites the other.

They do not disagree everywhere. [CLAIM-517](CLAIM-517.md)'s second half, that fidelity
measured in ordinary operation certifies nothing about viability, is
[CLAIM-266](CLAIM-266.md)'s limit in its coverage form: the contexts ordinary operation
does not sample are what the training probes cannot see. The two disagree
only when the boundary contexts are covered.

## The claim

Let P be a property of the system to be preserved, V the value of the
probe family over a context distribution μ, and suppose a stated
inequality bounds P's failure by V over the contexts μ covers: in
[CLAIM-517](CLAIM-517.md), the inward margin at every boundary point is at least
γ − L·√(ε/(2μ_min)), from the Lipschitz bound, Pinsker and coverage.
Then a small enough V certifies P. Optimizing against the probes lowers V
and so tightens the bound. [CLAIM-266](CLAIM-266.md)'s mechanism, that optimization
pushes toward what the probes reward "including what they cannot see",
needs something P depends on that V does not bound, and under the
inequality there is none: at a covered context, KL zero is equality of
distributions, and P depends on the regulator only through the
distributions at those contexts.

Two things survive from [CLAIM-266](CLAIM-266.md) inside the certificate.

- **The estimate.** The ε the step needs is the population value of the
  loss under μ. Read off the draws the successor was fitted to, it is
  biased low by exactly the optimization [CLAIM-266](CLAIM-266.md) describes. It must be
  estimated on fresh draws from μ, and then it certifies with a stated
  confidence, not with certainty. That is a sample held out, not a probe
  family held out: the family is the one used to train.
- **The bound's terms.** γ, L and μ_min come from a model of the dynamics
  and of the sampling, not from the probes. The certificate is the
  inequality together with the probe value; the probes alone certify
  nothing, which is the part of [CLAIM-266](CLAIM-266.md) this claim keeps.

So [CLAIM-266](CLAIM-266.md) holds where the preserved property outruns what the
training probes bound, or where they do not cover the contexts it is
decided at; and it fails as stated, without qualification, because the
training probes can certify where a bound links them to the property.
Every case [CLAIM-266](CLAIM-266.md) cites is of the first kind. In [CASE-041](../cases.d/CASE-041.md) no
inequality bounds quality in CLIP space or to human judges by FID in
ImageNet features; in [CASE-071](../cases.d/CASE-071.md) none bounds translation quality by the
selection metric. The FunSearch reading in [CLAIM-266](CLAIM-266.md)'s note of 2026-11-12
([THEORY-1803](../theory.d/THEORY-1803.md)) is the degenerate case, where the probe is the property
and the inequality is equality.

## What it does not say

- That training probes certify in practice. Most do not come with an
  inequality to the property, and [CLAIM-517](CLAIM-517.md)'s own coverage condition is
  one ordinary training does not supply.
- That held-out probe families are unnecessary where no bound is known.
  There [CLAIM-266](CLAIM-266.md) stands.
- That the inequality certifies itself. Its constants, and the claim that
  the property depends on the system only through what the probes
  measure, are premises shown by other means.
