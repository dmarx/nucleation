---
status: Proposed
title: 'A grammar revision can make an inert distinction consequential'
statement: >-
  How much a distinction matters to a governed record's machinery can be
  measured as the difference its perturbation makes to the findings the
  record's governing rules produce, Δ_M(R, δ) = d(F_M(R), F_M(R ⊕ δ)); and a
  revision of those rules, M → M′, can make a distinction that produced no
  finding produce one, Δ_M = 0 while Δ_M′ > 0, so that changing the grammar
  is a third kind of intervention beside changing an entry and changing a
  relation, one that changes what can become consequential
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A showing that every documented change of the record's rules that
  altered its findings did so only by making a distinction expressible that
  could not be written before, so that no expressible but inert
  distinction was ever made consequential; or that the findings difference
  is not a measure of how much a distinction matters to the machinery,
  because the same findings difference arises from perturbations the
  machinery treats alike.
tags:
- design-rationale
- software-engineering
- epistemology
date: '2026-11-26'
line:
- record-as-apparatus
grounds:
- CASE-131
summary: >-
  A25 §§3–4 and §11 of the exchange "Alignment consequences brainstorm"
  (ChatGPT, 2026-11-26), after the owner's "let's circle back to luria and
  how it ties into all of this" (U14). A writes luria's governing knowledge
  and subject knowledge as M and R (luria's README, M; R ⊢ x), measures a
  distinction by the findings difference under M, and reads the
  `corroborates` decision (ADR-044, CASE-131) as "a new distinction in how
  changes to evidence ought to become consequential". The argument for the
  existence clause is ARG-tmpsis1z, which narrows the instance: ADR-044 made
  a distinction expressible, and ADR-069 made an expressible one
  consequential. A's measure covers only machine findings; A says whether
  they move attention, decisions or action "is a further empirical
  question". The wording is A's (ChatGPT, in the exchange of 2026-11-26);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-tmpsis1z CLAIM-472 CLAIM-181 — Proposed; the argument filed beside this claim, and held claims cited -->

# CLAIM-tmpxl7dc: A grammar revision can make an inert distinction consequential

## The claim

A25 §4. Let F_M(R) be the findings produced by evaluating record R under
governance regime M, and δ a controlled perturbation of the record:

  Δ_M(R, δ) = d(F_M(R), F_M(R ⊕ δ)),

where d "could initially be something as simple as the symmetric difference between
the sets of findings produced". This "measures how much a distinction in the
record matters to the currently implemented governance mechanisms". Since M
can change, one can have Δ_M(R, δ) = 0 while Δ_M′(R, δ) > 0: "A distinction
that was previously mechanically inconsequential becomes mechanically
consequential through the development of the apparatus."

A's three experimental objects:

| Intervention | What it investigates |
|---|---|
| Change an entry | The consequences of subject-level revision |
| Change a relation | The consequences of reorganizing dependencies |
| Change the grammar | The consequences of changing what can become consequential |

## The research programme A builds on it

A25 §11 widens the measure into a profile and an envelope, which the claim
does not assert:

- a record as L = (R, M, Π, A): represented knowledge, governing grammar,
  repertoire of operations and projections, and the organization of
  authority through which findings acquire practical standing;
- a consequentiality profile C_L(δ) = (C_finding, C_attention,
  C_decision, C_action), whether δ produces a finding, receives attention,
  changes a decision, or modifies later activity;
- a developmental envelope Reach_{B,T}(L), the record organizations
  constructible within a declared budget and horizon, and the potential
  consequentiality of δ as the set of its profiles over that envelope.

Only the first component is machine-detectable; A25 §11: "For the human and
organizational parts, we would need observations of actual participation,
adjudication and activity." LEAD-tmpj44my measures the first.

## Its instance

A25 §3 reads CASE-131 and ADR-044 as the instance: before
`corroborates`, a claim filed with `supports` had its converse written as
`rests_on`, so the grammar asserted an inference nobody made; after it,
retiring a corroborating claim lowers support without breaking the
argument. ARG-tmpsis1z finds that this shows a distinction becoming
expressible, and supplies an instance of the stronger thing from ADR-069.

## What it does not say

- That a findings difference is a measure of epistemic importance. A25:
  "The formalization above measures only machine-detectable consequences."
- That a grammar should make every distinction consequential. A25 §14:
  "Some distinctions should be ignored", and §10 warns that every
  configuration "makes some activities easier, some distinctions more
  visible", which is CLAIM-181 and CLAIM-472's point.
