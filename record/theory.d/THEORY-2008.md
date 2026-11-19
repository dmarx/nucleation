---
number: 2008
status: Proposed
formerly:
- THEORY-tmp3vfqj
title: 'Masumori and colleagues show that a growing neural cellular automaton trained to regenerate keeps its formed pattern not at a fixed point but on a recurrent attracting state sustained by persistent, spatially structured fluctuations, that damage displaces it from that state and it returns over hundreds of steps, and that suppressing small updates across most of the pattern impairs the return'
version: 1
source:
- LIT-2788
tags:
- complex-systems
- information-theory
date: '2026-11-19'
bears_on:
- QUESTION-491
promote_when: >-
  The suppression result reproduced on other seeds, targets or
  architectures, with a control that blocks the same number of updates
  chosen at random rather than by magnitude, and with recovery impaired in
  the same way; and the absence of a fixed point confirmed by a dynamical
  measure such as a largest Lyapunov exponent or recurrence
  quantification.
summary: >-
  From the reading of [LIT-2788](../literature.d/LIT-2788.md) in [NOTE-2091](../notes.d/NOTE-2091.md). Masumori, Sato and
  Ikegami (2026), Entropy 28(8):893, DOI 10.3390/e28080893; read as the
  authors' arXiv preprint 2607.12403. In a growing neural cellular
  automaton trained to regenerate (Mordvintsev et al., [LIT-2798](../literature.d/LIT-2798.md)), the
  formed pattern is kept not at a fixed point but on a recurrent
  attracting state, with persistent fluctuations concentrated in a few
  "fluctuation cores" near the shape's boundaries; damage displaces the
  system and it returns over hundreds of steps, and blocking small updates
  outside a disc holding less than about 74% of the cells impairs the
  return. Transfer entropy and information decomposition describe inward
  corrective and outward propagating predictive asymmetries during repair,
  which the authors do not read as causal flow. Here because A15 of the
  exchange "Topological protection explained" cited it beside Mordvintsev
  et al. for [CLAIM-566](../claims.d/CLAIM-566.md); it shows persistence and repair in this system as
  one precarious activity, not two mechanisms. Read in its NOTE.
---

# THEORY-2008: Masumori and colleagues show that a growing neural cellular automaton trained to regenerate keeps its formed pattern not at a fixed point but on a recurrent attracting state sustained by persistent, spatially structured fluctuations, that damage displaces it from that state and it returns over hundreds of steps, and that suppressing small updates across most of the pattern impairs the return

## The account

After a damage-trained neural cellular automaton has grown its lizard, its hidden channels keep fluctuating even with fully synchronous updating. The fluctuations are spatially correlated beyond the 3×3 perception range and gather in a few channel-invariant cores near the shape's boundaries and protrusions. The system-level trajectory does not settle at a point but moves on a compact recurrent region; damage throws it far away and it returns slowly. When updates of magnitude at most 0.01 are blocked outside a disc around the damage, repair is impaired until the disc holds about 74% of the cells. At rest transfer entropy is highest near the cores and points outward; after damage it points inward near the wound and outward beyond. Spatial PID shifts from synergy toward redundancy during repair.

## What it does not show

- That fluctuation cores, rather than small updates in general, are needed for repair.
- That transfer entropy here measures causal flow: the authors disclaim it.
- Anything outside one architecture and training regime, or for the growth phase.
- Regeneration by constraints the pattern produces: the rule and alive mask are fixed.
