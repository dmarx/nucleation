---
number: 1312
status: Active
formerly:
- THEORY-tmp66yzx
title: 'A phase-amplitude coupling measure can be significant when only one non-sinusoidal rhythm is present, because the rhythm''s harmonics carry amplitude that depends on its own phase; such coupling is confined to bands spanning the rhythm''s harmonics, so a measured coupling is evidence of one rhythm modulating another only after waveform shape is controlled'
version: 1
tags:
- neuroscience
- mathematical-statistics
date: '2026-11-03'
source:
- LIT-1999
summary: >-
  Donoghue, Schaworonkow and Voytek (2021), [LIT-1999](../literature.d/LIT-1999.md), §5 and Fig.
  5D–E, read in [NOTE-1529](../notes.d/NOTE-1529.md) from the PsyArXiv preprint, standing on
  Kramer et al. 2008 and Cole et al. 2017. Active: checked by a short
  simulation in which a sharp-peaked 10 Hz wave gave a modulation index
  of 0.021 between its phase and 25–60 Hz amplitude against 0.0001 for a
  cosine, and none in a single-harmonic or an 80–250 Hz band. It does not
  say any particular published PAC is an artefact, nor that broadband
  coupling far above the harmonics is.
---

# THEORY-1312: A phase-amplitude coupling measure can be significant when only one non-sinusoidal rhythm is present, because the rhythm's harmonics carry amplitude that depends on its own phase; such coupling is confined to bands spanning the rhythm's harmonics, so a measured coupling is evidence of one rhythm modulating another only after waveform shape is controlled

## Source

Donoghue, Schaworonkow and Voytek (2021), [LIT-1999](../literature.d/LIT-1999.md), pp. 24–27 of the
PsyArXiv preprint; read in [NOTE-1529](../notes.d/NOTE-1529.md).

## What was actually shown

A simulated non-sinusoidal 10 Hz alpha rhythm, band-passed at 15–25 Hz,
shows a beta envelope that dips at a particular alpha phase, "indicating
phase-amplitude coupling, which is driven by the waveform shape of the
alpha rhythm", where a pure beta sinusoid shows none (Fig. 5D–E caption,
p. 27). The text: such values "reflect a relationship between frequencies
in the spectral domain", and the fallacy is to read them as "coupling
between independent rhythms, when in fact no such interaction between
multiple rhythms need exist" (p. 25). The proposed diagnostic is the extent
of the coupled band: narrow ranges at exact multiples suggest shape
(p. 26).

**Check.** In a 60 s simulation (scipy Butterworth filters, Hilbert
transform, 18-bin Tort modulation index), exp(3 cos φ) at 10 Hz plus noise
gave MI = 0.021 for 8–12 Hz phase with 25–60 Hz amplitude, against 0.0001
for cos φ; 15–25 Hz and 80–250 Hz amplitude bands gave ≤ 0.00006 for both.
The effect needs a band that holds several harmonics, which is why it is
confined to them. The paper's single-band 15–25 Hz case was not
reproduced with a strictly periodic wave.

## What this does not say

- **That any reported PAC is spurious.** The paper re-analyses no
  empirical result.
- **That broadband coupling far above the harmonics, such as 2–5 Hz phase
  with 80–250 Hz amplitude ([THEORY-1317](THEORY-1317.md)), is a shape artefact.** By
  the paper's own diagnostic it is the less suspect kind; it remains
  uncontrolled.
- **That PAC is never one rhythm gating another.** Genuine nesting is
  possible; the point is that the measure alone does not show it.
