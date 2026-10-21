---
number: 831
status: Active
formerly:
- THEORY-tmp3kgjq
title: "For a system driven by a protocol fixed in advance, with microscopic reversibility and with forward and reverse processes started uniformly on their macrostates, the log-odds of two outcomes II and III reached from I equal the difference in their log state counts, plus the log-ratio of their reversal probabilities, plus the difference in minus the log mean of e^(−βQ) over the paths reaching each, where Q is the heat released; so when the first two terms are equal the likelier outcome is the one whose paths release more heat on average with less variation"
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Split from THEORY-412 by the promotion audit (batch 077, ADR-040 and
    ADR-047 v2), on the pattern of THEORY-770's split from THEORY-673.
    THEORY-412 bundled Perunov, Marsland and England's exact Eq. (8) with
    the thesis that driven matter tends toward adapted states. This THEORY
    holds the identity and its equal-terms corollary, re-derived in the
    review under uniform starting densities; THEORY-412 keeps the thesis
    and its promote_when, and extends this one.
tags:
- thermodynamics
- complex-systems
date: '2026-10-21'
source:
- LIT-518
- LIT-515
summary: >-
  Perunov, Marsland and England (2016), [LIT-518](../literature.d/LIT-518.md), Eq. (8), read in full
  in [NOTE-416](../notes.d/NOTE-416.md) (which checked Eqs. 3–8), building on England's macrostate
  relation (2013), [LIT-515](../literature.d/LIT-515.md); re-derived by the promotion audit. An exact
  identity from microscopic reversibility, under a fixed protocol and
  uniform starting densities; the paper itself uses near-uniformity. It
  says nothing about which macrostates a real many-body system can be
  divided into with the other two terms equal.
extended_by:
- THEORY-412
---
<!-- inactive-ok-file: THEORY-412 THEORY-671 THEORY-673 — Proposed; the account this one is split from, the maximum-entropy-production contrast, and the earlier split it follows -->

# THEORY-831: For a system driven by a protocol fixed in advance, with microscopic reversibility and with forward and reverse processes started uniformly on their macrostates, the log-odds of two outcomes II and III reached from I equal the difference in their log state counts, plus the log-ratio of their reversal probabilities, plus the difference in minus the log mean of e^(−βQ) over the paths reaching each, where Q is the heat released; so when the first two terms are equal the likelier outcome is the one whose paths release more heat on average with less variation

## Source

Perunov, Marsland and England (*Phys. Rev. X* 6:021036, 2016), [LIT-518](../literature.d/LIT-518.md),
Eq. (8), read in full in [NOTE-416](../notes.d/NOTE-416.md) from arXiv v1. The macrostate relation
it starts from is England (2013), [LIT-515](../literature.d/LIT-515.md), read in [NOTE-419](../notes.d/NOTE-419.md).

## What was actually shown

**The identity.** In the paper's notation, with Ψ = β⟨Q⟩ and
Φ = ln⟨e^{−βQ}⟩ + Ψ,

ln[π(I→II)/π(I→III)] = ln(Ω_II/Ω_III) + ln[π̃(II→I)/π̃(III→I)] + ΔΨ − ΔΦ,

where π̃ is the time-reversed protocol and the averages are over forward
paths from I ending in each outcome. Ψ − Φ = −ln⟨e^{−βQ}⟩.

**Re-derivation (promotion audit, batch 077).** Microscopic
reversibility gives, path by path, P[path]/P̃[reversed path] =
e^{βQ[path]}. Summing over the paths from microstate x to y,
π̃(y→x) = π(x→y)⟨e^{−βQ}⟩_{x→y}. Start the forward process uniformly on
I and each reverse process uniformly on its own macrostate J. Then
π(I→J) = Ω_I⁻¹ Σ π(x→y) and π̃(J→I) = Ω_J⁻¹ Σ π(x→y)⟨e^{−βQ}⟩_{x→y},
so π̃(J→I)/π(I→J) = (Ω_I/Ω_J)⟨e^{−βQ}⟩_{I→J}. Writing this for J = II
and J = III and dividing gives the identity. Uniform starting densities
are what make the state-count term exactly ln(Ω_II/Ω_III); the paper
reaches it under near-uniformity and no-correlation assumptions (its
Eq. 5), so this entry states the exact version with its condition.

**The corollary.** By Jensen's inequality Φ ≥ 0, with equality only when
Q does not vary across the paths. So if the two outcomes have equal state
counts and equal reversal probabilities, the likelier is the one with
larger −ln⟨e^{−βQ}⟩: more heat released on average, less spread across
paths. Heat released in futile cycles cancels and drives no drift.

## What this does not say

- **That driven matter tends toward adapted states.** That is [THEORY-412](THEORY-412.md),
  which extends this entry and stays Proposed: it needs real systems in
  which the other two terms can be held equal.
- **That driven systems maximize dissipation.** Ψ alone does not fix the
  odds; Φ and the other two terms count too ([THEORY-671](THEORY-671.md) is the
  maximum-entropy-production contrast).
- **Anything for feedback-controlled drives,** or for starting densities
  far from uniform on the macrostates.
