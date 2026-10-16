---
status: Proposed
promote_when: >-
  A later review or primary paper, read for the purpose, that either gives
  an operational scheme linking ensemble work to single-shot work beyond
  taking limits of Rényi entropies, which would refute "not unified", or
  surveys the field after 2016 and finds no such link, which would promote
  it. The review's own side-by-side comparison cannot settle it, and
  neither can a further definition of work added to the list.
title: "Quantum thermodynamics has at least four inequivalent notions of work, the ensemble average, the two-point-measurement random variable, the ε-deterministic single-shot work content and the resource-theory work, which answer different operational questions; only the two single-shot optima coincide, by identification of formulas and for energy-diagonal states"
version: 1
tags:
- quantum-foundations
- thermodynamics
- information-theory
date: '2026-10-16'
source:
- LIT-010
summary: >-
  Vinjanampathy & Anders (2015/16), [LIT-010](../literature.d/LIT-010.md), read in full in [NOTE-011](../notes.d/NOTE-011.md). The
  review's one synthesis (§5.2, §7) sets four definitions side by side:
  ⟨W⟩ = ∫tr[ρḢ]dt (Eq. 2), W = E_m^(τ) − E_n^(0) (Eq. 24), A^ε ≈
  −kT ln(Z_Λ*/Z) (Eq. 49) and w^max_ε = F^min_ε(ρ_S) − F(τ_S) (Eq. 50).
  Only the last two agree, and that agreement is an observation that two
  published formulas match, for states diagonal in energy. It is an
  informed judgement of a 2016 snapshot, not a theorem that the notions
  cannot be unified.
---

<!-- inactive-ok-file: THEORY-030 — Proposed; named in Connections as the record's Landauer account, not leaned on -->

# THEORY-tmp2ae0w: Quantum thermodynamics has at least four inequivalent notions of work, the ensemble average, the two-point-measurement random variable, the ε-deterministic single-shot work content and the resource-theory work, which answer different operational questions; only the two single-shot optima coincide, by identification of formulas and for energy-diagonal states

## Source

Vinjanampathy & Anders (2015; *Contemporary Physics* 57, 2016), [LIT-010](../literature.d/LIT-010.md),
read in full in [NOTE-011](../notes.d/NOTE-011.md).

## What was actually shown

The review adds no new results. Its one synthesising observation is that
the strands of the field define "work" differently (§5.2, §7):

- **Ensemble work.** ⟨W⟩ = ∫₀^τ tr[ρḢ]dt, with heat ⟨Q⟩ = ∫ tr[ρ̇H]dt and
  ⟨Q⟩ + ⟨W⟩ = ΔU (Eqs. 1–3). Average heat and work are process-dependent
  and are not observables (§2.1, citing Talkner–Lutz–Hänggi).
- **Two-point-measurement work.** The difference of projective energy
  measurements at the start and end of a closed unitary process,
  W = E_m^(τ) − E_n^(0) (Eq. 24), a random variable with distribution
  Eq. 25. The measurements destroy energy coherences (§3.6).
- **ε-deterministic single-shot work content.** A^ε ≈ −kT ln(Z_Λ*/Z)
  (Eq. 49, after Åberg), with Λ* the smallest energy subspace carrying
  probability above 1 − ε.
- **Resource-theory work.** w^max_ε = F^min_ε(ρ_S) − F(τ_S) (Eq. 50, after
  Horodecki–Oppenheim and Gemmer–Anders). The work of formation (Eq. 51) is
  generally different.

The authors compare the plurality to the many entanglement measures, each
suited to a task (§7, p. 39). Only Eq. 49 and Eq. 50 coincide. The review
shows this on p. 26 by observing that Z_Λ*/Z equals the sum in Eq. 50.
[NOTE-011](../notes.d/NOTE-011.md) corrects §7's pointer, which names Eq. 48, the random single-shot
yield; the coinciding quantity is Eq. 49.

The single-shot and resource-theory notions are stated for states diagonal
in the energy eigenbasis (Eqs. 48–50, 53). For states with coherence §5.4
gives only necessary conditions (Eq. 57), and says sufficiency is unknown.

**What could have come out otherwise.** A derivation could have shown the
ensemble work to be the i.i.d. limit of the single-shot work, or the
two-point work to reproduce the ensemble average in general. The review
lists the operational link between ensemble and single-shot work as open
(§7).

## What this does not say

- **That the notions cannot be unified.** "Not unified" is the review's
  informed judgement as of early 2016 ([NOTE-011](../notes.d/NOTE-011.md), C12, moderate). The field
  was called rapidly evolving, and the record has not checked what came
  later.
- **That the single-shot and resource-theory works are proved equal.** The
  agreement is an identification of two published formulas, one of them
  stated with "≈", not a derivation ([NOTE-011](../notes.d/NOTE-011.md), C6, weak to moderate).
- **Anything for states with energy coherence.** The single-shot second
  laws (Eq. 53) and the coincidence hold for energy-diagonal states only.
- **Which notion is right.** Each answers a different question, so a claim
  about quantum work has to name its notion before it can be assessed.
  That is the review's point, and it does not rank them.
- **That thermodynamic entropy is von Neumann entropy out of equilibrium.**
  The review assumes it for the rest of the article and calls it debated
  (§2.1, p. 5). Results downstream inherit the assumption.

## Connections

- The fluctuation relations for the two-point work are filed as
  [THEORY-tmpagav0](THEORY-tmpagav0.md), from the same reading.
- The classical fluctuation theorems are [THEORY-tmp3uu1d](THEORY-tmp3uu1d.md) (Crooks, Jarzynski,
  Seifert). Landauer's principle, which the review states for mixed states
  "following from the second law", is [THEORY-030](THEORY-030.md).
- The smooth entropies use the unsquared fidelity whose operational meaning
  is [THEORY-tmpmfcjz](THEORY-tmpmfcjz.md) (Fuchs, [LIT-018](../literature.d/LIT-018.md)).
