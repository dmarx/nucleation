---
number: 1502
status: Proposed
formerly:
- THEORY-tmp6zy9r
promote_when: >-
  A reading of the review's derivations (§§2.8–2.9), or an independent
  source, that confirms the three things the title asserts: that for a real
  scalar with an analytic potential no exactly time-periodic localized
  solution exists except the 1+1 sine-Gordon breather; that oscillon
  radiation is nonzero and exponentially small in the amplitude parameter;
  and that 3+1 dimensional oscillons are stable only above a minimum
  amplitude and decay suddenly once radiation carries them below it, while
  in 1 and 2 dimensions the loss rate falls exponentially with amplitude so
  that they never decay. Whether fine-tuned oscillons are permanent is not
  asked.
title: 'For a real scalar field with an analytic potential, every localized oscillating state except the 1+1 dimensional sine-Gordon breather radiates, at a rate exponentially small in its amplitude parameter but nonzero; in 3+1 dimensions such oscillons are stable only above a minimum amplitude and decay suddenly once radiation has carried them below it, after a few thousand oscillations at most, while in 1 and 2 dimensions the loss rate falls exponentially as the amplitude falls and they never decay'
version: 1
tags:
- natural-sciences
- mathematics
date: '2026-11-06'
source:
- LIT-2197
summary: >-
  Fodor (2019), [LIT-2197](../literature.d/LIT-2197.md), read in part in [NOTE-1698](../notes.d/NOTE-1698.md) (Ch. 1,
  §§2.3–2.4, 2.6.3–2.6.5, the start of §2.10, Ch. 4). The statements are
  the review's, from its introduction and summary; the derivations behind
  the radiation law (§§2.8–2.9) were not read. A neighbour of Copeland,
  Gleiser & Müller (1995), [LIT-2200](../literature.d/LIT-2200.md), whose sudden end it generalizes.
  It does not settle whether fine-tuned resonant oscillons are permanent,
  which Gleiser & Krackow (2019) argue and the review denies.
---

# THEORY-1502: For a real scalar field with an analytic potential, every localized oscillating state except the 1+1 dimensional sine-Gordon breather radiates, at a rate exponentially small in its amplitude parameter but nonzero; in 3+1 dimensions such oscillons are stable only above a minimum amplitude and decay suddenly once radiation has carried them below it, after a few thousand oscillations at most, while in 1 and 2 dimensions the loss rate falls exponentially as the amplitude falls and they never decay

## Source

Fodor (2019), [LIT-2197](../literature.d/LIT-2197.md); read in part in [NOTE-1698](../notes.d/NOTE-1698.md).

## What was actually shown

- **Exact breathers (Ch. 1, §2.3).** Sine-Gordon in 1+1 "is the only theory
  involving a real scalar field where an exactly time-periodic localized
  breather can exist"; for higher dimensions "there is no potential for
  which a family of exactly periodically oscillating localized breather
  solutions can exist". The review states these; the proofs it cites were
  not read.
- **Radiation (Ch. 1, Ch. 4, §2.10).** "the radiation is exponentially
  small in terms of the parameter" ε, computed asymptotically and checked
  by spectral numerics against quasibreather tails; for large φ4 oscillons
  the measured radiation is "one or two magnitude larger than the
  theoretically predicted value", attributed to shape-modes.
- **Stability and dimension (Ch. 1).** Stable where total energy rises
  with central amplitude; "3 + 1 dimensional oscillons are stable only if
  their amplitude is above a certain limit", and below it "they suddenly
  decay"; in lower dimensions they "never decay".
- **Numerics (§2.6.4).** An independent code reproduces the Gaussian-data
  results of Gleiser and of Copeland, Gleiser & Müller: for one initial
  radius about 1240 oscillations, decay beginning near t = 5800 and lasting
  about 25 oscillations.

## What this does not say

- That fine-tuned oscillons are or are not permanent: the review holds that
  the peak states "necessarily radiate in a detectable way", but lifetimes
  there are bounded by numerical precision, and Gleiser & Krackow (2019)
  argue the contrary. Unresolved.
- Anything for non-analytic potentials, complex fields with a conserved
  charge, or coupled environments.
- That the radiation law was checked here: the derivations were not read.
- Anything about self-gravitating oscillatons, whose chapter was mostly not
  read.

## Note of 2026-11-06: what holds it back

[NOTE-1698](../notes.d/NOTE-1698.md) is Skimmed: §§2.8–2.9, which derive the radiation law, and the
rest of §2.10 were not read, so the exponentially small but nonzero rate and
the dimension-dependent stability are held only as the review's statements.
A full reading of those sections, or of another source that derives the law,
is what must come first.
