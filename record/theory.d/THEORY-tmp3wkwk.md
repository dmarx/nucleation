---
status: Proposed
promote_when: >-
  The derivation reproduced independently from the stated update rules
  (softmax choice over reward memories with decay, every action's memory
  updated with its average reward, learning slow relative to play), and the
  version of record checked for the sign of the decay term, which v2
  prints inconsistently between Eq. 6 and Eq. 14. It is refuted by an error
  in the limit. Results for Q-learning in which only the chosen action is
  updated are a different rule (THEORY-tmpar5jw) and neither promote nor
  refute this.
title: 'Two softmax reinforcement learners whose reward memories decay at rate α follow coupled replicator equations plus a term α Σ x_j log(x_j / x_i) toward uniform play; without decay the dynamics are conservative, Hamiltonian in zero-sum games, and with decay they are dissipative'
version: 1
tags:
- game-theory
- learning-theory
- complex-systems
date: '2026-10-24'
source:
- LIT-tmpxlow9
summary: >-
  Sato & Crutchfield (arXiv 2002; PRE 2003), [LIT-tmpxlow9](../literature.d/LIT-tmpxlow9.md), read in full from
  arXiv v2 in [NOTE-tmp8ra24](../notes.d/NOTE-tmp8ra24.md), Eqs. 1–13. The entropy-like term is what memory
  decay becomes under softmax choice; re-derived in the reading. The model
  updates every action's memory at the same rate, so it is the
  full-information case, not Q-learning as usually run.
---
<!-- inactive-ok-file: NOTE-tmp8ra24 THEORY-tmpar5jw THEORY-tmphhvqf THEORY-tmpev90a CLAIM-443 CLAIM-444 — Proposed or new; the source and the accounts this bears on, named -->

# THEORY-tmp3wkwk: Two softmax reinforcement learners whose reward memories decay at rate α follow coupled replicator equations plus a term α Σ x_j log(x_j / x_i) toward uniform play; without decay the dynamics are conservative, Hamiltonian in zero-sum games, and with decay they are dissipative

## Source

Yuzuru Sato and James P. Crutchfield, "Coupled replicator equations for the
dynamics of learning in multiagent systems", *Physical Review E* 67:015206
(2003), [LIT-tmpxlow9](../literature.d/LIT-tmpxlow9.md), read in full in [NOTE-tmp8ra24](../notes.d/NOTE-tmp8ra24.md) from arXiv:nlin/0204057v2,
Eqs. 1–13 (pp. 1–2).

## What was actually shown

- **The rule.** Memories Q_i(n + 1) − Q_i(n) = R_i − αQ_i(n), choice
  x_i ∝ exp(βQ_i).
- **The limit.** With learning slow relative to play, so R_i is action i's
  average reward against the other's current mix,
  ẋ_i/x_i = β[R_i − Σ_j x_j R_j] + α Σ_j x_j log(x_j/x_i) (Eq. 6). The
  derivation is three lines, and the reading re-derived it: the decay term
  −αβ(Q_i − x·Q) is −α(log x_i − x·log x) under softmax.
- **Structure.** For bilinear rewards the phase volume in log-ratio
  coordinates contracts at rate (N − 1)(α_X + α_Y) (Eq. 10). At α = 0 the
  system is conservative, and Hamiltonian if the game is zero-sum
  (Eq. 11); the time average of an interior orbit is the Nash equilibrium
  (p. 2, citing Schuster et al.).

## What this does not say

- **That this is Q-learning.** No states, no bootstrapping, and every
  action's memory updated each step whether chosen or not. Kaisers and
  Tuyls show that the same equation describes Q-learning only after a
  frequency adjustment ([THEORY-tmpar5jw](THEORY-tmpar5jw.md)).
- **What the rest points are.** It does not say so, but with α > 0 the
  interior rest points of Eq. 8 satisfy β(Ay)_i − α log x_i = const, that
  is, x is a softmax best response to y at temperature α/β: logit
  equilibria, not Nash equilibria. This is my reading of the equations.
- **Anything for more than two agents** beyond the linear three-agent
  extension.

## Connections

- **[THEORY-tmphhvqf](THEORY-tmphhvqf.md).** The contrast that matters. Cross learning has no
  forgetting term and is absorbed in a vertex. Here forgetting is a force
  towards uniform play, and the boundary is repelling.
- **[CLAIM-443](../claims.d/CLAIM-443.md).** The schematic rule's forgetting term −λE has this
  reading under softmax selection: decay of a learned bias is pressure
  towards equal authority, and its rate sets how hard the system
  re-explores.
- **[CLAIM-444](../claims.d/CLAIM-444.md).** The coupled, two-population case of the replicator
  reading, derived for learners.
