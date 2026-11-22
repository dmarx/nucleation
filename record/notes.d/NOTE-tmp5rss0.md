---
status: Read
paper: LIT-2230
title: 'Ocampo-Espindola, Singhal, Li and Kiss — Optimal phase-selective entrainment of electrochemical oscillators with different phase response curves'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 for LEAD-023 from the copy in the NSF Public
    Access Repository (https://par.nsf.gov/servlets/purl/10557355), the
    published version as AIP supplied it to the repository, 13 pages.
    PAR is a public-access repository run under the funder's policy, a
    lawful copy (ADR-074). Figures read through their captions.
    Quotations checked by script against the downloaded text.
date: '2026-11-22'
summary: >-
  A single global periodic signal, designed by convex optimization from each
  unit's natural frequency and phase response curve, entrains uncoupled
  electrochemical oscillators into a chosen phase pattern (in-phase,
  anti-phase, out-of-phase, and one-, two- and three-cluster states of
  four), in a kinetic model and in nickel electrodissolution experiments,
  open-loop, with less power than a design from the mean response curve,
  which with heterogeneous units can lock them into the wrong pattern.
---
<!-- inactive-ok-file: CLAIM-167 — Proposed; the one-way drive claim this reading bears on -->

# NOTE-tmp5rss0: Ocampo-Espindola, Singhal, Li and Kiss — Optimal phase-selective entrainment of electrochemical oscillators with different phase response curves

## Contribution

An experimental validation of an earlier optimal-input method (their
ref. 42): one common periodic input, built from the units' measured
frequencies and phase response curves (PRCs), places each unit at a
prescribed phase relative to the input, so that a chosen synchrony
pattern appears among units that differ in both frequency and PRC.

## Key results

1. **The task (abstract).** "finding an external waveform that can induce
   a predetermined sequence (e.g., some units peak together and others at
   different times) is a tremendously challenging task because each unit
   responds to the external signal differently."
2. **Method (§II.B).** In the averaged phase model ϕ̇ⱼ = Δωⱼ + Λᵤ,ⱼ(ϕⱼ),
   entrainment at ϕⱼ* needs Δωⱼ + Λᵤ,ⱼ(ϕⱼ*) = 0 with negative slope (eq.
   4); minimizing input power under these constraints is a convex
   quadratic program (eq. 5).
3. **Mean PRC fails with heterogeneity (§III.A, Case 3).** Designing from
   the mean PRC gave the slower oscillator two stable phases, "depending on
   its initial phase", and in experiment (§III.B, Case 3) "the baseline
   method entrains the oscillators in an in-phase configuration instead of
   an out-of-phase pattern".
4. **Experiments (§III.B).** Pairs in in-, anti- and out-of-phase
   patterns, and four oscillators in one-, two- and three-cluster states
   (Fig. 8); the proposed input used three to ten times less power than
   the baseline, with phase errors of 0.40 to 0.68 rad.
5. **Open loop (§IV).** "our technique does not require real-time feedback
   and can successfully obtain stable synchronization structures using
   only the knowledge of the natural frequencies and the PRCs of the
   population".
6. **Limits (§IV).** "As the heterogeneity in oscillator frequency
   increases, stronger inputs are required for phase-selective
   entrainment. This might invalidate the weak forcing assumption that
   underpins the validity of phase models."

## Assumptions

Weak forcing, so that phase reduction holds; the PRCs and natural
frequencies known (measured by pulse responses); entrainment at a single
input frequency. The model units (eq. 6) are not coupled to one another;
the experiment's electrodes share the potentiostat signal and the paper
does not discuss any coupling between them.

## Concepts

Phase response curve; interaction function (the input's averaged effect
over one cycle); phase-selective entrainment; open-loop control; cluster
state.

## Bearing on the record

- **[CLAIM-167](../claims.d/CLAIM-167.md).** A clear one-way drive: the signal is open-loop and fixed
  in advance, so nothing the oscillators do changes it. It makes units
  that are not coupled to one another hold a designed phase pattern, a
  combined form, in the claim's sense, relative to a target that needs the
  drive and the units, with the drive at the top of the architecture.
- **[CLAIM-172](../claims.d/CLAIM-172.md)** (a contrast with its version-5 sharpening). Selective
  synchrony, some units together and others apart, is here made wholly by
  a common drive, with no couplings for it to match. So selective
  synchrony alone, without knowing the couplings, does not mark peers.
- **[QUESTION-063](../questions.d/QUESTION-063.md).** A synchrony pattern, clusters included, can be the
  signature of a shared drive acting through units' different phase
  responses, not of coupling. Telling them apart needs the drive recorded
  or manipulated, as the question says.
- **[QUESTION-147](../questions.d/QUESTION-147.md).** Clusters here are set by the drive and by each unit's
  PRC, not by symmetry orbits of a graph: an observed cluster pattern
  that matches no orbit may be driven rather than coupled.

## Limitations

Small ensembles (two and four units); phase errors in experiment are not
small (up to 0.68 rad). The method needs measured PRCs, and the authors
note that stronger heterogeneity may push the input beyond the weak-forcing
regime. It does not address coupled units or how to detect a drive.
