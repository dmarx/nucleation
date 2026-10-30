---
number: 396
status: Proposed
formerly:
- CLAIM-tmp3gd3i
title: 'Directional information measures between reciprocally coupled units follow the path of a one-sided drive rather than the symmetry of the coupling, so the observed direction of information flow does not by itself reveal which way, or whether both ways, the units are coupled'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Note of 2026-10-30 added at the eighteenth status review: the linear
    Gaussian pair computed with an unrecorded drive. The drive, not the
    coupling, sets the delayed-MI asymmetry there, so the defeated_if's
    second branch is not met; one-way flow is not monotone in the drive;
    and with the drive recorded, conditioned transfer entropy separates a
    symmetric from a one-way pair without intervention. The claim is
    unchanged and stays Proposed.
role: thesis
warrant: interpretive
defeated_if: >-
  A system with a known reciprocal coupling, one unit driven on one side
  at graded strengths, in which transfer-entropy or delayed-MI asymmetry
  stays symmetric under strong drive, or tracks the coupling's symmetry
  without the drive being recorded or intervened on. Or a derivation, in
  the linear Gaussian pair, that the delayed-MI asymmetry
  c_xy(τ)² − c_yx(τ)² is fixed by the coupling and not by the drive.
tags:
- information-theory
- causality
date: '2026-10-20'
line:
- distributed-agency
grounds:
- THEORY-275
summary: >-
  The record's generalization of one study (Das, Manikandan and Banerjee,
  [THEORY-275](../theory.d/THEORY-275.md)) beyond its system, filed under [ADR-047](../decisions.d/ADR-047.md) v4 as the record's
  own claim, since the source makes no general claim. It bears on the
  claims that read peer or hierarchical architecture from the direction
  of coupling.
---

<!-- inactive-ok-file: CLAIM-172 CLAIM-167 — Proposed; the architecture claims this one qualifies, open -->

# CLAIM-396: Directional information measures between reciprocally coupled units follow the path of a one-sided drive rather than the symmetry of the coupling, so the observed direction of information flow does not by itself reveal which way, or whether both ways, the units are coupled

## The claim

In Das, Manikandan and Banerjee's two optically trapped beads ([THEORY-275](../theory.d/THEORY-275.md)),
the hydrodynamic coupling is symmetric by construction, yet delayed mutual
information and transfer entropy read the flow between the beads as two-way
under moderate drive of one trap and as one-way under strong drive. What
changed the reading was the drive, not the coupling. The record generalizes
this: between reciprocally coupled units, a directional information measure
locates where a one-sided drive enters and how strongly it dominates, and
cannot alone distinguish a symmetric coupling with one-sided input from an
asymmetric coupling. Telling them apart needs an intervention on a member.

The record's earlier title for [THEORY-275](../theory.d/THEORY-275.md) asserted this as a general law.
The source asserts it only for its system, which is why it is filed here as
the record's claim, with an interpretive warrant: it is untested beyond one
linear Gaussian pair, and the strong-drive half rests on numerics.

## What it does not say

- That information measures can tell a shared, unrecorded drive from
  coupling. That is [QUESTION-063](../questions.d/QUESTION-063.md)'s case and is untouched.
- That information moves from one unit to another. "Flow" is the direction
  of predictive improvement ([CLAIM-335](CLAIM-335.md)).
- That direction tests are useless. With the drive recorded, they locate
  where it enters.

It bears on [CLAIM-172](CLAIM-172.md) and [CLAIM-167](CLAIM-167.md), which read peer or hierarchical
architecture from whether coupling runs both ways or one: an observational
direction test would class the beads as hierarchical under strong drive.
[QUESTION-186](../questions.d/QUESTION-186.md) asks for the second system that would test the claim.

## Note of 2026-10-30: the linear Gaussian pair, computed

The second branch of the defeated_if asks whether, in the linear Gaussian
pair, delayed-MI asymmetry is fixed by the coupling and not by the drive.
It is not. The eighteenth status review computed exact stationary moments
for a pair with symmetric coupling 0.4, relaxation 1 and unit noise, and an
unrecorded Ornstein–Uhlenbeck drive (rate 0.5) entering x₁ at strength d
(p18/claim396_lgpair.py; controls: no drive gives zero asymmetry, no
coupling gives zero MI and TE, the moments match a simulation).

- With no drive, delayed MI and transfer entropy are symmetric. Any d > 0
  makes both favour x₁ → x₂, and moving the drive to x₂ reverses the sign.
- At d = 4 and lag 0.5 the symmetric pair reads ΔMI = 0.301,
  TE₁→₂ = 0.151 and TE₂→₁ = 0.022. A pair coupled one way, x₁ → x₂, with
  the same drive reads 0.292, 0.150 and 0.024 (p18/claim396_match.py).
  The two are close on all three measures, which is this claim's second
  half for an unrecorded drive.
- One-way flow is not monotone in the drive here. TE₁→₂/TE₂→₁ rises to
  about 230 at d = 2 and falls back to between 4 and 8 for d from 4 to 64,
  because x₂ comes to carry information about the unrecorded drive.
  THEORY-275's one-way reading under strong drive is for a recorded drive
  and the fitted bead model, which this model is not.
- With the drive recorded, transfer entropy conditioned on its past
  separates the two pairs without intervention: TE₂→₁ given the drive is
  0.0067 for the symmetric pair and exactly 0 for the one-way pair
  (p18/claim396_conditioned.py). "Telling them apart needs an intervention
  on a member" holds at most where the drive is unrecorded.

This is THEORY-275's model class, linear, Gaussian and two-body, so it is
not QUESTION-186's second system.

## Note of 2026-10-30: what holds it back

It generalizes one linear Gaussian pair, and the test it names is a second
system with a known reciprocal coupling driven at graded strengths
(QUESTION-186), which has not been found. The computation of 2026-10-30
confirms that the drive sets the direction within that model class and
reaches no further.
