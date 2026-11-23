---
status: Proposed
title: When demands are predicates on histories with deadlines, the sets of
  them an organization can jointly meet under its response architecture and
  budget form a downward-closed complex contained in the complex of the same
  demands without deadlines, so two demands can be compatible statically and
  incompatible in time, and a change in the response architecture, faster
  actuation, different sequencing, staged capacity or a new method, can enlarge
  the temporal complex without weakening any demand
version: 1
role: thesis
warrant: demonstrated
defeated_if: A set of deadline-indexed demands that some admissible history
  meets while a subset is met by none (the complex would not be downward closed),
  or one met in time but not met at all without deadlines (it would not be
  contained).
tags:
- operations-research
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- realizability
rests_on:
- CLAIM-347
- CLAIM-tmpk4bou
summary: 'A44 §8 of the exchange "Explain First Contact RL" (ChatGPT, third
  share of 2026-11-22): the compatibility complex of CLAIM-347 indexed by
  deadlines and response architecture. A44 asserts that it is downward closed.
  The containment in the deadline-free complex, and so the possibility of
  static compatibility with temporal incompatibility, is the assistant''s
  derivation. The idea is A''s (ChatGPT, in the exchange of 2026-11-22); the
  containment step and the wording are the assistant''s (Claude, in this session);
  adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-tmpk4bou CLAIM-tmpx9nrj — Proposed; cited in this filing of 2026-11-23 (third share) -->

# CLAIM-tmpdvgrf: When demands are predicates on histories with deadlines, the sets of them an organization can jointly meet under its response architecture and budget form a downward-closed complex contained in the complex of the same demands without deadlines, so two demands can be compatible statically and incompatible in time, and a change in the response architecture, faster actuation, different sequencing, staged capacity or a new method, can enlarge the temporal complex without weakening any demand

## The construction (A44 §8)

Let each demand D_i be a predicate on histories over [0, H_i]. For a
response architecture θ and budget B, K_{θ,B} is the set of J ⊆ I for
which some admissible policy meets every D_j, j ∈ J. Admissibility
includes deadlines, resource limits and safety conditions.

## Derivation

- **Downward closed:** a history meeting every demand in J meets every
  demand in any subset of J. So K_{θ,B} is a simplicial complex, as in
  CLAIM-347.
- **Contained in the deadline-free complex:** let D_i⁰ be the same
  acceptance condition with no deadline. Every history meeting D_i by
  H_i meets D_i⁰. So K_{θ,B} ⊆ K⁰_B, the complex of the deadline-free
  demands under the same budget and safeguards.
- **Strict containment is possible:** A44's factory can cut emissions
  and keep production but "lack the capacity to complete the conversion
  within the regulatory deadline while meeting uninterrupted supply
  requirements". The pair is a face of K⁰ and not of K_{θ,B}.
- **Retuning can enlarge it:** a change of θ that adds attainable
  histories (faster actuation, resequencing, staged capacity, a new
  method) can enlarge K_{θ,B} for the same demands. By CLAIM-tmpk4bou that
  requires a change of dynamics, not a hard constraint added at fixed
  dynamics. A44 rightly adds that this is "one possible mechanism, not a
  guarantee of monotone expansion".

Under stochastic dynamics the existence test becomes a probability of
joint satisfaction, as in CLAIM-tmpx9nrj.
