---
number: 1502
status: Active
formerly:
- THEORY-tmp6zy9r
title: 'For a real scalar field with a potential analytic at its minimum, the only one-parameter family of exactly time-periodic localized solutions that shrinks to the vacuum is the 1+1 dimensional sine-Gordon breather family; small-amplitude oscillons radiate at a rate exponentially small in their amplitude parameter, to leading order a coefficient times an exponential in minus a constant over that parameter, and, since their core energy scales as the parameter to the power 2 − d, in 3+1 dimensions they are stable only above a minimum amplitude and decay suddenly once radiation carries them below it, while in 1 and 2 dimensions small and moderate amplitude oscillons are stable and, their loss falling exponentially with amplitude, never decay'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed (kind 3) and promoted at the status review's ruling (the owner
    delegated these rulings), the twenty-ninth status review, on NOTE-1698
    v2, which read §§2.3 and 2.7–2.10 (ADR-065). Old title, verbatim: "For a
    real scalar field with an analytic potential, every localized
    oscillating state except the 1+1 dimensional sine-Gordon breather
    radiates, at a rate exponentially small in its amplitude parameter but
    nonzero; in 3+1 dimensions such oscillons are stable only above a
    minimum amplitude and decay suddenly once radiation has carried them
    below it, after a few thousand oscillations at most, while in 1 and 2
    dimensions the loss rate falls exponentially as the amplitude falls and
    they never decay". Old promote_when, verbatim: "A reading of the
    review's derivations (§§2.8–2.9), or an independent source, that
    confirms the three things the title asserts: that for a real scalar
    with an analytic potential no exactly time-periodic localized solution
    exists except the 1+1 sine-Gordon breather; that oscillon radiation is
    nonzero and exponentially small in the amplitude parameter; and that
    3+1 dimensional oscillons are stable only above a minimum amplitude and
    decay suddenly once radiation carries them below it, while in 1 and 2
    dimensions the loss rate falls exponentially with amplitude so that
    they never decay. Whether fine-tuned oscillons are permanent is not
    asked." What the review derives is narrower: no one-parameter family
    tending to the vacuum (§2.3); isolated breathers only "unlikely" on
    numerics; the leading radiation coefficient vanishes at isolated
    parameters (§2.9.4); and the 1–2 dimensional stability is for small and
    moderate amplitudes (§2.8.6). The reading of the derivations meets the
    old condition for the narrowed title. The old title, which the review
    asserts in Ch. 1 and §2.7, is filed as THEORY-tmplbj45, which extends this
    entry and keeps the old condition word for word (ADR-065, kind 1).
    Status Proposed → Active; promote_when removed on promotion.
tags:
- natural-sciences
- mathematics
date: '2026-11-06'
source:
- LIT-2197
extended_by:
- THEORY-tmplbj45
summary: >-
  Fodor (2019), LIT-2197, read in NOTE-1698 (Chapter 2, the introduction and
  the summary). What the review derives: the family result, the
  exponentially small leading-order radiation (checked by two independent
  computations, by Segur and Kruskal's earlier value for φ4, and by numerics
  that approach it as the amplitude falls), and the dimension dependence of
  stability from the core energy. A neighbour of Copeland, Gleiser & Müller
  (1995), LIT-2200, whose sudden end it generalizes. The wider statement,
  that every state but the sine-Gordon breather radiates and that 3+1
  oscillons last a few thousand oscillations at most, is THEORY-tmplbj45.
  Whether fine-tuned resonant oscillons are permanent is left open.
---
<!-- inactive-ok-file: THEORY-tmplbj45 — Proposed; the wider statement this entry was narrowed from -->

# THEORY-1502: For a real scalar field with a potential analytic at its minimum, the only one-parameter family of exactly time-periodic localized solutions that shrinks to the vacuum is the 1+1 dimensional sine-Gordon breather family; small-amplitude oscillons radiate at a rate exponentially small in their amplitude parameter, to leading order a coefficient times an exponential in minus a constant over that parameter, and, since their core energy scales as the parameter to the power 2 − d, in 3+1 dimensions they are stable only above a minimum amplitude and decay suddenly once radiation carries them below it, while in 1 and 2 dimensions small and moderate amplitude oscillons are stable and, their loss falling exponentially with amplitude, never decay

## Source

Fodor (2019), LIT-2197; read in NOTE-1698 (Chapter 2, Ch. 1 and Ch. 4).

## What was actually shown

- **One family (§2.3, §2.7.1).** "for analytic potentials the family of sine-Gordon breathers is the
  only truly periodic localized one-parameter family of solutions which tends to the vacuum
  solution for the small value of the parameter"; for d > 1 "there is no potential for which a
  family of exactly periodically oscillating localized breather solutions can exist". A counting
  argument: "Three conditions for each mode for coupled second order equations is generally too
  much."
- **Radiation (§§2.8–2.10).** The tail is "exp(−1/ε) order small", at leading order a coefficient
  νk times an exponential in −P/ε, P the distance of the nearest complex singularity of the leading
  profile. ν3 for the symmetric sextic potential by numerical integration and by Borel summation
  agrees to seven digits; ν2 for φ4 agrees with Segur and Kruskal's; large-amplitude numerics
  exceed the leading order by one or two orders of magnitude, "The obvious reason for this is that
  our analytic results are valid only to leading order", and approach it as ε falls.
- **Stability by dimension (§§2.8.4–2.8.6, §2.7.3).** The core energy goes as ε^(2−d); stable where
  energy rises with amplitude; 3D φ4 oscillons "become stable only above a relatively large
  amplitude value"; in 2D "small and moderate amplitude oscillons turn out to be stable. If an
  oscillon develops from some initial data, its lifetime is infinite, it never decays suddenly."
- **Numerics (§2.6.4, §2.10).** An independent code reproduces Gleiser's Gaussian case (about 1240
  oscillations, decay near t = 5800 over about 25); "In case of one and two spatial dimensions,
  stable oscillon states oscillate for infinitely long time, without ever decaying."

## What this does not say

- That no isolated breather exists; the review finds it "unlikely" numerically (THEORY-tmplbj45).
- That the radiation is nonzero for every analytic potential: the leading coefficient vanishes at
  isolated parameters (ν3 = 0 at g5 = 0.26495), and the next order derived carries a factor d − 1.
- Anything about 1–2 dimensional oscillons above the amplitude where the energy peaks, which is
  "currently unknown".
- That 3+1 oscillons last a few thousand oscillations at most (THEORY-tmplbj45).
- Whether fine-tuned resonant oscillons are permanent: the review holds that the peak states
  "necessarily radiate in a detectable way", and Gleiser & Krackow (2019) argue the contrary.
- Anything for non-analytic potentials, complex fields with a conserved charge, coupled
  environments, or self-gravitating oscillatons.

## Note of 2026-11-06: §§2.8–2.10 read

NOTE-1698 v2 read the derivations that the earlier note of this date named as missing. The title
is narrowed to what they derive and the entry promoted (history v2).
