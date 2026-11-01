---
status: Proposed
promote_when: >-
  Data from tissue or animals in which peripheral circadian oscillators
  are classed by an isolation test, as self-sustained (still oscillating
  when cut off from the SCN) or damped. Both classes must then be put
  through the same phase shift of the light schedule, and their
  resynchronization must differ as the coupled-oscillator models predict
  (the damped ones regaining phase faster, the self-sustained ones slower
  or by a long delay), or must fail to. Further simulations, or isolation
  results without the phase-shift comparison, do not settle it.
title: 'Whether a coupled oscillator sustains its own rhythm or is a damped oscillator driven from outside is settled directly by removing the drive, and, because the two arrangements are not dynamically equivalent, may also show in how they respond to a shift of phase: in Leise and Siegelmann''s model, damped peripheral clocks regain their phase relation to the central clock quickly, while self-sustained ones take longer, need strong coupling, and sometimes resynchronize by a long delay instead of an advance'
version: 1
history:
- version: 1
  date: '2026-11-01'
  note: >-
    Filed Proposed from NOTE-tmpbljat, the reading of Bechtel and
    Abrahamsen in full. The signatures are outputs of one model, reported
    second-hand. Neither the model paper (Leise and Siegelmann 2006) nor
    Davidson et al. (2004) is held. The paper itself calls the empirical
    question open as of 2010.
tags:
- philosophy-of-biology
- complex-systems
date: '2026-11-01'
source:
- LIT-tmppbuqq
bears_on:
- QUESTION-086
summary: >-
  Bechtel and Abrahamsen (2010), [LIT-tmppbuqq](../literature.d/LIT-tmppbuqq.md), §3.6, p. 328, read in
  [NOTE-tmpbljat](../notes.d/NOTE-tmpbljat.md). Peripheral clocks were once taken for "slaves" of the
  SCN, damping without it. Later evidence suggested they keep oscillating
  and lose synchrony, so the SCN is "a conductor" rather than "a
  ringmaster". The paper's reading is that models of both kinds "can
  reveal the empirical signatures that each may leave". This is a
  biological instance of the record's question where maintenance is
  realized. It is also a case outside [CLAIM-522](../claims.d/CLAIM-522.md)'s ideal limit: the
  outside drive does not reproduce the inside law, so a perturbation of
  state may tell them apart.
---

# THEORY-tmpnzjca: Whether a coupled oscillator sustains its own rhythm or is a damped oscillator driven from outside is settled directly by removing the drive, and, because the two arrangements are not dynamically equivalent, may also show in how they respond to a shift of phase: in Leise and Siegelmann's model, damped peripheral clocks regain their phase relation to the central clock quickly, while self-sustained ones take longer, need strong coupling, and sometimes resynchronize by a long delay instead of an advance

## Source

Bechtel and Abrahamsen (2010), [LIT-tmppbuqq](../literature.d/LIT-tmppbuqq.md), §3.6, p. 328, and §3.5,
p. 327; read in [NOTE-tmpbljat](../notes.d/NOTE-tmpbljat.md). It reports Davidson et al. (2004) and
Leise and Siegelmann (2006), neither held here.

## What was actually shown

- **The question (p. 328).** "It was long assumed that these peripheral
  oscillators were unable to sustain oscillations (rather, their
  oscillations dampened) without input from the SCN; accordingly, they
  were regarded as slaves to the SCN. More recently, evidence suggests
  that they maintain oscillations, but lose synchrony." The paper does
  not say what that evidence was. The direct test, by definition of the
  two kinds, is to remove the drive: a damped oscillator then decays, and
  a self-sustained one keeps its rhythm.
- **The model (p. 328).** Each oscillator has two variables,
  dX/dt = r_X/(1 + Y²) − q_X X and dY/dt = r_Y X²(t − τ_lag) − q_Y Y,
  "whose biochemical interpretation they left unspecified". The six
  oscillators are SCN core, SCN shell and four peripheral populations,
  coupled by thresholds. Light is a lowered r_Y.
- **The signatures (p. 328).** After a simulated six-hour advance,
  "When the choice of parameter values rendered the peripheral oscillators
  as damped oscillators, they recovered their phase relation relatively
  quickly, but when they were self-sustained this took longer and required
  a strong degree of coupling. Under some conditions, the peripheral
  oscillators restored phase relations by delaying fifteen hours rather
  than advancing six hours."
- **The paper's reading.** Given "the current uncertainty as to whether
  peripheral oscillators are damped oscillators or merely unsynchronized
  when they receive no input from the SCN, modeling phase advances (and
  delays) with both kinds of oscillators can reveal the empirical
  signatures that each may leave ... and so guide empirical attempts to
  answer this question."
- **A neighbouring case (p. 327).** In To et al.'s SCN model, about 60% of
  cells become arrhythmic without the coupling peptide VIP. For those
  cells the oscillation is maintained through the coupling, not within
  the cell.

## What this does not say

- **That the signatures have been observed.** They are model outputs, and
  "different patterns of restoration resulted from different assumptions
  built into the model" (p. 328).
- **That a state probe always separates inside from outside maintenance.**
  It separates these two arrangements because they obey different
  equations. A drive that reproduced the oscillator's own law exactly, the
  ideal case of [CLAIM-522](../claims.d/CLAIM-522.md), would leave no such signature.
- **That "self-sustained" settles where the rhythm is maintained.** A
  self-sustained peripheral cell still depends on its own substrates and
  on the organism. The distinction is relative to a declared boundary, the
  cell or the tissue, as every such distinction in the record is.

## Connections

- **[QUESTION-086](../questions.d/QUESTION-086.md).** It asks for an intervention short of removing the
  controller that tells self-maintenance from outside maintenance. This
  is a candidate answer, with its condition: a perturbation of state,
  here a phase shift, can do it when the outside arrangement is not
  dynamically equivalent to the inside one. That fits A44's prediction,
  filed in [QUESTION-086](../questions.d/QUESTION-086.md)'s note of 2026-10-18, that "the way coherence is
  achieved predicts how coherence fails". It is a biological case, not
  a construction. The signatures are unconfirmed.
- **[CLAIM-522](../claims.d/CLAIM-522.md).** It marks the edge of the claim's ideal limit, which the
  claim's own defeated_if anticipates: a controller with lag, saturation
  or a different law "may be detectable by state probes, and that is not a
  counterexample". Here the outside arrangement differs in law, not only
  in lag.
- **[CLAIM-414](../claims.d/CLAIM-414.md).** Its maintenance pair, closed production against outside
  reset, is told apart by a single perturbation of state. This case is
  the same structure in a biological model. Same structure, not shown
  same mechanism.
- **[CLAIM-521](../claims.d/CLAIM-521.md).** In To et al.'s cells, coupling carries maintenance. That
  is the feedback [CLAIM-521](../claims.d/CLAIM-521.md)'s construction excludes.
