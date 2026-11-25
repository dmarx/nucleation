---
number: 1029
status: Active
formerly:
- CLAIM-tmp5wozo
title: 'In a population built on the coupled meaning–influence model, grants indexed by role with the critic role scored by observed relevance leave neither belief factions nor capture, while scalar grants fail one way or the other: scored by agreement they capture the population or split it into factions, and moved by the reward for realized policy they split it into factions that read only their own side; indexing by role without a separate score buys nothing'
version: 3
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): its ground CASE-420 went Active at this
    review; the defeat condition is not met on the rerun. The choice
    between its Readings A and B for CLAIM-281 stays with the owner.
- version: 3
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §13.6. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of the study's code (scratch/studies/lead-190/) in which the
  role scheme with relevance-scored critics forms belief factions or
  captures the population below the stated independence threshold, or in
  which scalar-policy grants do not sort readers to their own side; or a
  derivation showing that the role scheme's fixed point at ζ = 0 depends
  on readers' initial meanings.
tags:
- self-governance
- complex-systems
date: '2026-11-23'
line:
- distributed-agency
grounds:
- CASE-420
corroborates:
- CLAIM-281
complements:
- CLAIM-1150
bears_on:
- QUESTION-089
summary: >-
  The comparison [CLAIM-281](CLAIM-281.md) names, run in a population of 20 operators
  built on [CASE-363](../cases.d/CASE-363.md)'s model. Scored by agreement above the loop's
  threshold, a scalar grant captures the population as one, or, from a
  polarized start on a balanced corpus in mean field, splits it into
  factions. Moved by the reward for realized policy, a scalar grant
  makes every operator read only its own side (gap 1.05, fidelity 0.50).
  Role indexing with critics scored by relevance has no gap and no
  capture, keeps critic weight on opponents at chance and follows their
  competence, and gives opponents no decision authority. It holds while
  the critic score's dependence on agreement stays below
  ζ* = 2(1 − φ′ − φ_s′)/(gσ²). Role indexing scored by agreement is
  identical to the scalar scheme in the meaning layer. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: CLAIM-281 CLAIM-285 — Proposed; the claims tested and the built model, cited as open -->

# CLAIM-1029: In a population built on the coupled meaning–influence model, grants indexed by role with the critic role scored by observed relevance leave neither belief factions nor capture, while scalar grants fail one way or the other: scored by agreement they capture the population or split it into factions, and moved by the reward for realized policy they split it into factions that read only their own side; indexing by role without a separate score buys nothing

## The claim

[CLAIM-281](CLAIM-281.md) holds that indexing grants by role lets an organization "keep disagreement working inside it instead of sorting into factions", and its notes say the population comparison it names had not been run. [CASE-420](../cases.d/CASE-420.md) ran it, in a population of operators that each read the others' retrieval as [CASE-363](../cases.d/CASE-363.md)'s collective does. The model parameters put the loop above [CLAIM-947](CLAIM-947.md)'s threshold when critics are scored by agreement.

1. **Scalar, scored by agreement.** The population fails in one of two ways. It may be captured as one: every reader reads one side, with one-sidedness 0.72 to 0.84 and right on the evidence when the corpus leans. Or it may split into factions: a polarized start on a balanced corpus in mean field gave a gap of 0.76 and own-side reading of 0.72, rising to 1.05 and 0.91 with φ_s = 0.2. At agent level, noise turned the factions into capture.
2. **Scalar, moved by the reward for realized policy.** This is [CLAIM-285](CLAIM-285.md)'s operator holding one grant. Every operator delegated only to its own side, so it read only its own side. The gap was 1.05 and own-side reading 1.00. Each population split down the middle whatever the corpus said: half its operators were wrong at b = 0.05. This held at agent level and at N = 40.
3. **Role, with critics scored by relevance.** There was no gap and no capture in any condition (one-sidedness 0.26, no more than the side lean of competence). Half of each reader's critic weight crossed sides, which is chance, and it followed opponents' relevance (correlation 0.83). No decision grant went to an opponent. Scoring both roles by relevance (scalar-comp) gives the same meanings but hands opponents 53% of decision grants. That is the transfer of authority [CLAIM-281](CLAIM-281.md)'s second defeat clause names, and indexing by role removes it.
4. **Role, with critics scored by agreement.** Its meaning layer equals the scalar-agree scheme exactly. Splitting the grant into two rows does nothing for factions unless the critic row has its own score.
5. **The condition.** With the critic score ζ·agreement + (1 − ζ)·relevance, the symmetric state of the meaning layer stays stable while gζσ²/2 < 1 − φ′ − φ_s′. Above it the population is captured as one. From a polarized start, factions appeared only above the differentiating threshold, gζσ²/2 > 1 − φ′, and somewhat beyond it (ζ ≥ 0.85 against 0.79; ζ ≥ 0.95 against 0.875).

So [CLAIM-281](CLAIM-281.md)'s clause on factions holds in this model on one condition: the critic role has a score that does not read the critic's agreement with the reader, or reads it weakly enough. Its first defeat clause, factions under role-indexed grants as readily as under scalar ones, is met only when role indexing is scored by agreement.

## Two readings for [CLAIM-281](CLAIM-281.md), for the owner

- **Reading A (the assistant's lean): role indexing includes a role-specific score.** A2's example has i back j "as an error detector" for j's "exceptional error-detection capabilities", which is a score of the role, not of agreement. On this reading the comparison supports [CLAIM-281](CLAIM-281.md) as stated, under the condition in item 5. This claim then corroborates it.
- **Reading B: role indexing is the indexing alone.** The grant is split, and how each part is scored is left open. On this reading role indexing as such buys nothing against agreement scoring (item 4). What helps is a separate score for critics. Role indexing still beats the scalar scheme that [CLAIM-285](CLAIM-285.md)'s reward produces (item 2), because the decision row no longer sets whom one reads. [CLAIM-281](CLAIM-281.md) would then need restating to name the scoring. The comparison corroborates only the restated claim.

The results are the same on both readings. What differs is whether [CLAIM-281](CLAIM-281.md)'s "indexed by role" already carries the score.

## What it does not say

- That disagreement in belief survives. Under role indexing the meanings converge to one shared value (spread 0). What survives is disagreement in policy: decision grants stay on each side while evidence crosses. Where that shared meaning lands is [CLAIM-1150](CLAIM-1150.md)'s subject, and it is not always where the evidence points.
- That role boundaries hold under pressure, or that relevance can be observed independently of side. Both are assumed here.
- Anything beyond this model's parameters, two roles and one policy dimension.
