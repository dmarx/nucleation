---
status: Proposed
title: 'Effortless action has a direction as well as a timing: the least quadratic
  effort to move a controlled system by Δx is ΔxᵀW⁻¹Δx with W its controllability
  Gramian, so a change of given size is cheap along W''s strong directions,
  costly along its weak ones and impossible outside its range, and acting
  effortlessly is acting along the directions the system already affords,
  as Cook Ding''s knife follows the spaces between the joints'
version: 1
role: thesis
warrant: demonstrated
defeated_if: 'An error in the cost formula. As a reading of wu-wei: a case
  of reported effortless action in which the change made lies along a direction
  the actor''s means reach only weakly, at high cost, and yet is felt as effortless;
  or the finding that it only restates CLAIM-541 and CLAIM-345 with nothing
  added by the direction of action.'
tags:
- self-governance
- control-theory
- mathematics
date: '2026-11-23'
line:
- will-organization
- realizability
rests_on:
- CLAIM-345
- CLAIM-541
complements:
- CLAIM-tmpx8csq
summary: The assistant's answer to the owner's "relate the conversation to
  wuwei" (2026-11-23, this session), after the exchange "Explain First Contact
  RL". [CLAIM-541](CLAIM-541.md) reads wu-wei as control placed and timed where a system's
  own dynamics do most of the work. This adds direction from [CLAIM-345](CLAIM-345.md)'s Gramian,
  and reads A44's split, fast restoration across a system's organizing relations
  with slow change along them, as the same picture. The Zhuangzi passage is
  cited from common knowledge of it and not checked against a translation.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

<!-- inactive-ok-file: CLAIM-541 CLAIM-tmpk8ude CLAIM-tmpx8csq LIT-1994 — Proposed or Unavailable; cited in the assistant's answer of 2026-11-23 on wu-wei -->

# CLAIM-tmp0doyo: Effortless action has a direction as well as a timing: the least quadratic effort to move a controlled system by Δx is ΔxᵀW⁻¹Δx with W its controllability Gramian, so a change of given size is cheap along W's strong directions, costly along its weak ones and impossible outside its range, and acting effortlessly is acting along the directions the system already affords, as Cook Ding's knife follows the spaces between the joints

## The claim

By [CLAIM-345](CLAIM-345.md), the least ∫‖u‖² that moves ẋ = Ax + Bu from 0 to Δx by time
H is ΔxᵀW_H^†Δx when Δx lies in the range of the Gramian W_H, and
infinite otherwise. Write Δx = r·q with q a unit vector. If q is an
eigenvector of W_H with eigenvalue σ, the cost is r²/σ. The same size of
change is then cheap along strong directions (large σ), dear along weak
ones (small σ), and impossible outside the range. [CLAIM-tmpx8csq](CLAIM-tmpx8csq.md) is the
one-mode case: persistence (γ) is not redirectability (b).

## The reading

[CLAIM-541](CLAIM-541.md) gives wu-wei a timing: small perturbations timed by the
system's own wandering, as in Ott–Grebogi–Yorke control. This gives it a
direction. Effortless action moves along the directions the system and
the actor's means already afford. Strain is forcing a change along a
direction they reach only weakly. The Zhuangzi's Cook Ding, whose knife
stays sharp because it follows the spaces between the joints, is the
image (cited from common knowledge of the passage, not checked against a
translation).

A44 of the exchange "Explain First Contact RL" split perturbations into
those across an organization's organizing relations, restored fast, and
those along them, changed slowly. Its "identity-preserving adaptability"
is this picture applied to an organization. The scroll interface's
design ([CLAIM-tmpk8ude](CLAIM-tmpk8ude.md)) is effortless in the same sense for its user:
learning runs where it adds no lag, and the user meets a surface that
already moves as expected.

## Admission ([ADR-075](../decisions.d/ADR-075.md))

*A derivation.* The cost ordering by direction follows from [CLAIM-345](CLAIM-345.md)'s
formula by the eigendecomposition of W_H. [CLAIM-541](CLAIM-541.md) states timing, not
direction. Neither entry states the ordering by direction, and it is
what the reading uses. The reading itself is interpretive. It is
defeated by its `defeated_if`. Under the owner's ruling ([CLAIM-tmpwjpc8](CLAIM-tmpwjpc8.md))
the sinological reading, unread ([LIT-1994](../literature.d/LIT-1994.md)), bears on whether the name
fits, not on the account.

## Note of 2026-11-23: what holds it back

Its premise [CLAIM-541](CLAIM-541.md) is Proposed: the timing it adds a direction to rests
on Ott, Grebogi and Yorke's method, which no reading or demonstration in the
record holds. The direction half follows from [CLAIM-345](CLAIM-345.md) (Active) alone.
