---
number: 482
status: Active
formerly:
- THEORY-tmpagav0
title: "For a closed quantum system that starts thermal and is measured projectively in energy before and after a unitary drive, the two-point-measurement work obeys the Jarzynski equality and the Tasaki–Crooks relation in exactly the classical form, because those energy measurements erase the coherences in which a quantum difference could appear"
version: 1
tags:
- quantum-foundations
- thermodynamics
date: '2026-10-16'
source:
- LIT-010
extends:
- THEORY-431
summary: >-
  Vinjanampathy & Anders (2015/16), [LIT-010](../literature.d/LIT-010.md), read in full in [NOTE-011](../notes.d/NOTE-011.md),
  which reproduces the derivation (Eqs. 24–30). With W_{m,n} = E_m^(τ) −
  E_n^(0), a thermal start and closed unitary evolution, ⟨e^{−βW}⟩ =
  e^{−βΔF} follows from Σ_n p_{m|n} = 1 (Eq. 29), identical in form to the
  classical relation. The identity is exact under its conditions. Its
  classicality is bought by the definition of work: two projective energy
  measurements destroy coherences, which is why the definition is
  contested. It says nothing about work defined without them.
---

<!-- inactive-ok-file: THEORY-416 — Proposed; the sibling account of work notions, named, not leaned on -->

# THEORY-482: For a closed quantum system that starts thermal and is measured projectively in energy before and after a unitary drive, the two-point-measurement work obeys the Jarzynski equality and the Tasaki–Crooks relation in exactly the classical form, because those energy measurements erase the coherences in which a quantum difference could appear

## Source

Vinjanampathy & Anders (2015; *Contemporary Physics* 57, 2016), [LIT-010](../literature.d/LIT-010.md),
§3.2 and §3.6, read in full in [NOTE-011](../notes.d/NOTE-011.md). The review derives the
fluctuation relations in full; the primary sources it cites are Jarzynski,
Crooks and Tasaki, its refs [3]–[5]. The result is standard, and the record
files it on the review's derivation.

## What was actually shown

**Conditions.** The system starts in the thermal state at inverse
temperature β for the initial Hamiltonian. Its evolution between the two
energy measurements is a closed unitary V. Work is the two-point random
variable W_{m,n} = E_m^(τ) − E_n^(0) (Eq. 24), with distribution Eq. 25.

**Result.** The quantum Jarzynski equality ⟨e^{−βW}⟩ = e^{−βΔF} and the
Tasaki–Crooks relation follow (Eqs. 26–30). The proof uses only the
normalisation Σ_n p_{m|n} = 1 of the transition probabilities (Eq. 29).
Jensen's inequality then gives ⟨W⟩ ≥ ΔF. The review notes that these
relations are identical in form to the classical ones (Eqs. 18–21), where
the closed-system proof rests on Liouville's theorem (Eq. 20).

**Why the form is classical.** Each run starts and ends in an energy
eigenstate, so the coherences of the state in the energy basis play no role
in the statistics. The review records that this is exactly why the
two-point definition is contested (§3.6, citing Kammerlander & Anders).
[NOTE-011](../notes.d/NOTE-011.md) grades the formal equivalence strong and its physical reading
dependent on that choice (C3).

**What could have come out otherwise.** A quantum correction term could
have appeared in the exponential average. Under these conditions it
cannot: the proof's only use of V is the normalisation of the transition
probabilities it induces.

## What this does not say

- **That quantum fluctuations of work obey the classical relations in
  general.** The equality holds for this definition of work. For the
  ensemble work of Eq. 2, or for work extracted from coherences (Eq. 12),
  the review gives other results, and it lists the definitions as
  unreconciled ([THEORY-416](THEORY-416.md)).
- **That the relations hold for open evolution.** The derivation assumes a
  closed unitary between the measurements. The Crooks form needs detailed
  balance with the bath (§3.2).
- **That quantum thermodynamics has no new effects.** The review's own §7
  says the field had made few experimentally checkable predictions of new
  effects; this identity is one reason, not a demonstration that none
  exist.
- **That the review is the authority.** It reproduces the derivation; the
  record's LIT entry advises citing the primary papers for formulas.

## Connections

- **Carries further** [THEORY-431](THEORY-431.md), the classical trajectory-level
  fluctuation theorem with Jarzynski's equality as a corollary. This is the
  same identity widened to closed quantum systems under the two-point
  definition of work.
- The four notions of work, and why naming one matters, are
  [THEORY-416](THEORY-416.md).
