---
number: 412
status: Proposed
formerly:
- THEORY-tmp1lcfx
promote_when: >-
  A many-body driven system, simulated or in the laboratory, in which the
  internal-entropy and reversal terms of Eq. (8) are estimated or held
  fixed, and the frequencies of its outcomes are predicted in advance from
  Ψ − Φ. The account is promoted if the dissipation term improves the
  prediction over one from entropy and kinetic accessibility alone, and if
  the favoured outcomes are those whose formation absorbed the drive's work
  more reliably. It is refuted if the outcomes are predicted as well
  without the dissipation term, or if the favoured states do not differ in
  reliable work absorption. Further single-particle landscapes, in which
  "all else equal" is arranged by hand, cannot settle it. Neither can
  observations, after the fact, that self-organized structures such as
  dunes or vortices dissipate, nor the exactness of Eq. (8), which is
  granted.
title: "Driven matter tends toward states that look adapted to the drive, with no replication needed: of two outcomes of a system driven by a fixed external field, equal in internal entropy and in the probability of reversal, the likelier is the one whose formation absorbed work from the drive and dissipated it more reliably"
version: 1
tags:
- thermodynamics
- complex-systems
date: '2026-10-16'
source:
- LIT-518
- LIT-515
presupposes:
- THEORY-431
- THEORY-679
summary: >-
  Perunov, Marsland & England (2014; Phys. Rev. X 2016), [LIT-518](../literature.d/LIT-518.md), read in
  [NOTE-416](../notes.d/NOTE-416.md), on England's macrostate relation ([LIT-515](../literature.d/LIT-515.md)). The log-odds of two
  driven outcomes decompose exactly into an internal-entropy term, a
  reversal term and Ψ − Φ = −ln⟨e^{−βΔQ}⟩. The "tendency towards adaptation"
  needs the first two held equal. The paper does that only in two
  single-particle hopping models, argues the many-body case, and reports a
  driven-chemistry simulation without showing it. The reading judged the
  claim too weak to source a THEORY; it is filed as Proposed for that
  reason. "Adapted" here means absorbing the drive's work, nothing more.
---

<!-- inactive-ok-file: THEORY-026 THEORY-072 THEORY-532 THEORY-671 — Proposed; named as accounts this one is contrasted with, not leaned on -->

# THEORY-412: Driven matter tends toward states that look adapted to the drive, with no replication needed: of two outcomes of a system driven by a fixed external field, equal in internal entropy and in the probability of reversal, the likelier is the one whose formation absorbed work from the drive and dissipated it more reliably

## Source

Perunov, Marsland & England (*Phys. Rev. X* 6:021036, 2016), [LIT-518](../literature.d/LIT-518.md), read
in full in [NOTE-416](../notes.d/NOTE-416.md) from arXiv v1 (2014). The PRX text was not seen and may
differ. The macrostate relation it starts from is England (2013), [LIT-515](../literature.d/LIT-515.md),
read in [NOTE-419](../notes.d/NOTE-419.md).

[NOTE-416](../notes.d/NOTE-416.md) concludes that "no new THEORY is indicated" because the central
claim (its C2) "is too weakly supported to source one". This document
files the claim as an account the record does not yet believe, with its
weakness stated. It does not dispute that judgement.

## What was actually shown

**The exact part (Eq. 8).** Prepare a system in macrostate I and drive it
with a field λ(t) fixed in advance, with no feedback. For two outcomes II
and III, ln[π^fwd(I→II)/π^fwd(I→III)] = Δln Ω_{II,III} + ln[ratio of
reversal probabilities] + ΔΨ − ΔΦ. Here Ψ = β⟨ΔQ⟩ is the mean heat
released on the way, and Φ = ln⟨e^{−βΔQ}⟩ + Ψ ≥ 0 grows with how much that
heat varies between paths, so Ψ − Φ = −ln⟨e^{−βΔQ}⟩. The step to Eq. (5)
adds no-correlation and near-uniformity assumptions. Eq. (6) restricts to
likely paths, which is stated, not derived, and the cumulant reading
(Eq. 7) is called "heuristic".

**The interpretive claim.** Hold the entropy and reversal terms equal, and
the likelier outcome is the one reached by paths that absorbed more work
and shed it more reliably. Such states have "dynamical response properties"
tuned to the drive, as a resonant oscillator is tuned to its forcing, and
the paper calls them "better adapted". "The adaptation we predict is
expected to take place independent of whether or not there is anything in
the system that can copy itself."

**The toy models, checked in [NOTE-416](../notes.d/NOTE-416.md).**

- *Three states* (Fig. 3). The barrier is set by hand so return rates are
  equal. Hops to x₁ release βΔE/2 and hops to x₃ release nothing, and
  r_max(2→1)/r(2→3) = e^{ΔΨ} (Eq. 12). The cycle-averaged ratio is
  I₀(βΔE/2), so the identity holds to leading order in βΔE.
- *Two paths* (Fig. 4). Two barriers driven out of phase give Ψ = 0 and
  Φ ≃ βΔE/2, and the forward rate falls as ln r ≃ −Φ (Eq. 13).
  Fluctuating dissipation slows the transition.
- *Futile cycles.* For paths that return to their start, Ψ = Φ, so heat
  made in cycles drives no drift.

**What is argued, not shown.** Some of the ∼10²⁵ directions of a many-body
phase space "should" behave the same way (C3, weak). A driven chemical
mixture showing "adaptive" resonance is summarised from a study "published
in a separate article, rather than shown here" (C6).

**What could have come out otherwise.** In the toy models the dissipating
transition could have failed to dominate. It did, but the comparison was
built so that it would.

## What this does not say

- **That the drifted states are better at anything but absorbing the
  drive's work.** "Adaptation" is defined by the paper's own quantity, so
  calling the states "better adapted" is partly a choice of word ([NOTE-416](../notes.d/NOTE-416.md)).
- **That "all else equal" can be had in a real system.** The paper admits
  it is "not immediately intuitive" what equal reversal probability means
  in general, and does not show a parcelling of many-body phase space into
  equal, equally accessible macrostates exists.
- **That driven systems maximize dissipation.** Maximizing Ψ alone "is not
  predicted to correspond to a likely outcome": the fluctuation term and
  the other two terms count too. This is the paper's contrast with
  maximum-entropy-production principles (C7, informal; [THEORY-671](THEORY-671.md)).
- **That an adapted system dissipates more in every sense.** In [THEORY-026](THEORY-026.md)
  a system matched to its drive keeps a predictive memory and wastes less
  work. Here a system matched to its drive absorbs and dissipates more.
  The two answer different questions and do not contradict each other, but
  a claim that "adapted systems dissipate more" or "less" has to say which
  sense it means ([NOTE-416](../notes.d/NOTE-416.md)).
- **That Darwinian and thermodynamic adaptation are one.** The paper says
  they "become one and the same" for self-replicators, supported only by
  England's replication bound (C5, assertion).
- **Where a living thing ends.** The paper calls it "somewhat arbitrary how
  we have decided to draw a line around a whale". It offers no criterion
  that would separate a cell from a hurricane except degree of reliable
  dissipation.
- **Anything with feedback.** The drive is fixed in advance.

## Connections

- **Premises.** The Crooks relation ([THEORY-431](THEORY-431.md)) and England's
  macrostate form of it ([THEORY-679](THEORY-679.md)). If either fails, Eq. (8) loses
  its derivation.
- **Gradient dissipation ([THEORY-532](THEORY-532.md)).** Schneider and Kay make a
  related claim, that pushed systems develop structures that degrade the
  applied gradient, as a law of development rather than as statistical
  mechanics.
- **The demarcation question.** [THEORY-072](THEORY-072.md) holds that organisms differ
  from dissipative structures by organisational differentiation. This
  account denies there is a physical line to draw and replaces it with a
  graded property of histories. The two are not declared rivals: this
  account's claim is the tendency, and its denial of a line is a framing,
  not a result.
- **A test the record could run.** The primitive metabolic cycles of
  [LIT-036](../literature.d/LIT-036.md) are self-organized states of a chemically driven system. This
  account predicts they are the states that absorb and dissipate the drive
  reliably. [LIT-036](../literature.d/LIT-036.md) does not compute dissipation.
