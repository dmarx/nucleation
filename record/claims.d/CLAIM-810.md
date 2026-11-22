---
number: 810
status: Proposed
formerly:
- CLAIM-tmpbe2gh
title: 'Scale invariance, dependence across scales and transfer across scales are three properties, any of which can occur without the others, so a hierarchy of structure is not a hierarchy of causation'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2965 (NOTE-2275, THEORY-2187). The
    "What it does not say" bullet calling the 2024 study unread is updated
    in place with what it found and what it does not test (ARG-187).
    The thesis and status are unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A proof that, for a stated decomposition into scales, scale invariance
  of a stationary field's law forces statistical dependence between
  scales, or that dependence between scales forces a net transfer of a
  conserved quantity between them; or a showing that the Gaussian field
  below does not count as scale-invariant without cross-scale dependence
  under any reasonable decomposition. Not defeated by systems that have all
  three, such as turbulence.
tags:
- complex-systems
- natural-sciences
- causality
date: '2026-11-21'
line:
- formal-apparatus
rests_on:
- CLAIM-846
complements:
- CLAIM-850
uses:
- TERM-142
grounds:
- THEORY-748
- THEORY-754
summary: >-
  A's, at A23 §1 (scale invariance, cross-scale dependence and cross-scale
  transfer, "A system can possess one without necessarily possessing the
  others"), §8 and §10 ("A hierarchy of structure is not necessarily a
  hierarchy of causation"). A's own example, independent variables
  Y_j = 2^(−Hj) X_j, is a construction with no physical system behind it;
  the assistant supplies one: a stationary Gaussian field with a power-law
  spectrum, whose Fourier modes are independent and whose odd moments
  vanish, so it is scale-invariant with no dependence between wavenumber
  bands and no flux, while the 4/5 law ties turbulent transfer to a
  nonzero third moment. The wording is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A23); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-846 CLAIM-850 — filed with this claim on 2026-11-21 -->
<!-- inactive-ok-file: ARG-187 THEORY-2187 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-810: Scale invariance, dependence across scales and transfer across scales are three properties, any of which can occur without the others, so a hierarchy of structure is not a hierarchy of causation

## A's distinction (A23 §1)

| Property | Meaning | A's example |
|---|---|---|
| Scale invariance | the same scaling relation at different resolutions | a geometric fractal |
| Cross-scale dependence | structure at one scale is informative about another | correlated critical fluctuations |
| Cross-scale transfer | activity at one scale dynamically influences another | turbulent energy cascade |

> **Scale-free statistics describe relationships among magnitudes. They
> do not, by themselves, reveal how the system's different scales
> influence one another.**

A23 §10 draws the moral: "Something can be geometrically nested without
transmitting information directionally. Something can transmit
information across scales without being exactly self-similar. And
something can exhibit a power law without either kind of hierarchical
interaction."

## The physical instance A's construction lacked (the assistant's)

A23 §1's construction, Y_j = 2^(−Hj) X_j with independent X_j, has exact
amplitude scaling and independent scales by stipulation. The ledgers note
that A shows no physical system like it. One is at hand:

- **A stationary Gaussian field with a power-law spectrum**, such as the
  spin waves of an ordered magnet (A27 §3) or the simulated field of
  [CLAIM-846](CLAIM-846.md). Stationarity makes the covariance diagonal in the
  Fourier basis, and joint Gaussianity makes uncorrelated modes
  independent. So the bands of wavenumber, the natural decomposition into
  scales, are independent, while the band variances scale as a power law:
  scale invariance with no dependence between scales.
- **The same field has no transfer.** All its odd moments vanish, so the
  third-order increment moment is zero. In turbulence that moment is the
  flux: ⟨(δu_L(r))³⟩ = −(4/5)εr (A23 §3), whose sign "reflects a net
  forward transfer of energy". Transfer through scales thus needs
  non-Gaussian, odd-order statistics, which is also why [THEORY-748](../theory.d/THEORY-748.md)'s block
  entropies, blind to the reflection x → −x, cannot see it.

The other separations: dependence without transfer is the equilibrium
critical field, [CLAIM-850](CLAIM-850.md)'s row for criticality without a cascade; transfer without exact
self-similarity is intermittent turbulence, multifractal with
ζ(q) ≠ q/3 (A23 §4–5); a power law with neither is a sample of
independent Pareto draws ([CLAIM-846](CLAIM-846.md)).

Which decomposition counts as "scales" matters. In real space the
Gaussian field is correlated across distances; the claim is that in the
Fourier decomposition its scales are independent, so whether a system
shows cross-scale dependence depends on how scales are defined. A23 §6's
transfer entropy between a large-scale and a small-scale variable needs
that decomposition fixed (a filter or wavelet band), which A does not
give, and measures directed predictive improvement, not flow ([CLAIM-335](CLAIM-335.md)).

## A correction on the spectrum

A23 §2 gives the K41 spectrum E(k) ∼ ε^(2/3) k^(−5/3) and §5 the
intermittent departure of ζ(q) from q/3, without saying whether the
spectral exponent is itself corrected. It is, slightly: E(k) ∝
k^(−(1+ζ₂)), and in the She–Leveque model ζ₂ = 0.696 against K41's ⅔,
giving k^(−1.696) (computed from ζ_p = p/9 + 2(1 − (2/3)^(p/3)), which
also returns ζ₃ = 1 as the 4/5 law requires). The model is named here
for the size of the correction only; the record holds no reading of it.

## What it does not say

- That turbulence's interscale causation is settled. A23 §6 cites a 2024
  study decomposing it into unique, shared (the paper's "redundant") and
  synergistic parts (Martínez-Sánchez and colleagues, [LIT-2965](../literature.d/LIT-2965.md), read
  2026-11-22 as [THEORY-2187](../theory.d/THEORY-2187.md); changed in place, version 2). It finds
  directed, forward, mostly unique and redundant dependence among four
  volume-averaged flux signals of one simulation, with lags chosen to
  maximize the cross unique terms. That fits this claim's turbulence row,
  where all three properties are present, and does not test the
  separations ([ARG-187](../arguments.d/ARG-187.md)).
- That nesting never carries causation. The claim is only that structure
  across scales does not show it.

## Note of 2026-11-22: Martínez-Sánchez and colleagues, read

Martínez-Sánchez, Arranz and Lozano-Durán ([LIT-2965](../literature.d/LIT-2965.md)) were read
([NOTE-2275](../notes.d/NOTE-2275.md); the reading is [THEORY-2187](../theory.d/THEORY-2187.md)). **Qualifies, and supports
in part.**

- **Keeps transfer and dependence apart.** The energy transfer Σ̃ = τᵢⱼS̄ᵢⱼ
  is a physical flux, defined dynamically (p. 14); SURD then measures the
  predictive information among "the time signals of the volume-averaged
  energy transfer". A measure of dependence among transfers, not a measure
  of transfer: the distinction this claim draws, kept in the paper's own
  construction.
- **Fixes the decomposition** this claim says A23 §6's transfer entropy
  needs: Gaussian filters at four widths in the inertial range, then volume
  averaging.
- **Does not test the separations** ([ARG-187](../arguments.d/ARG-187.md), Rejected as that
  route). Turbulence has all three properties; the paper examines no
  system that has one without the others. Its limits: four volume-averaged
  scalars, so local backscatter that cancels in the average cannot show;
  one simulation; lags chosen to maximize the cross unique terms; and a
  leak of about 47% for the second scale.
- SURD's components are invariant under invertible transformations of the
  signals, and the flux's sign is in the variable, so it is not blind to
  the reflection x → −x as [THEORY-748](../theory.d/THEORY-748.md)'s block entropies on the velocity
  are. A parallel, no relation.
