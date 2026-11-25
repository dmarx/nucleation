---
number: 353
status: Proposed
formerly:
- CASE-tmp943kt
title: 'Judgement–observation loop with five anchors'
statement: >-
  A simulated single-mind judgement–observation loop with action held fixed,
  built so that it locks in without anchors and given the five candidate
  anchors one switch each: with all present it never locks in and no single
  removal makes it; in the loops left minimal, removing commitment before
  evidence, processing signals or exogenous capture makes it lock in, while
  removing a channel of unselected input, the body or testimony only leaves
  it blind
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-020 at the owner's
    triage of leads it could handle on its own. The code, tests and result
    files are committed beside it under scratch/studies/lead-020/.
standing: documented
kind: executed-study
tags:
- cognition
- agency
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-099
- CASE-106
bears_on:
- QUESTION-121
illustrates:
- CLAIM-342
summary: >-
  The run [LEAD-020](../leads.d/LEAD-020.md) asks for, from [QUESTION-121](../questions.d/QUESTION-121.md): "A loop that does not lock in,
  with action held fixed, and a demonstration that removing a given
  candidate makes it lock in." [CASE-099](CASE-099.md)'s meaning–authority loop is built
  as a bounded simulation inside one mind. Authority sets attention and so
  attenuates readings against it, and it is scored against the dominant
  interpretation. The world switches every 300 steps, and nothing the loop
  does changes the world or when inputs arrive. With sensory input alone
  the loop locks in on every seed. The question's five candidates are
  added as switches, each with its stated objection built in. The
  sensory candidate is split into its channel and exogenous capture. With
  all present the loop follows every switch, and no single removal makes
  it lock in. In the minimal loops, removing commitment before evidence,
  processing signals or exogenous capture makes the loop lock in. Removing
  an evidence channel (the senses, the body, testimony) leaves it blind,
  unless capture goes with it. Over 19 parameter variants, a loop with
  evidence avoided lock-in when it had one of those three anchors in 37 to
  42 of 44 configurations per variant. The exceptions are stated. A
  fictional model, by construction; the numbers are of this model. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-662 — Proposed; the reading candidate 4 is taken from, as QUESTION-121 cites it -->

# CASE-353: Judgement–observation loop with five anchors

## The construction

The code is in scratch/studies/lead-020/ (`loop.py`; tests in
`test_loop.py`, eleven, passing; README says how to rerun).

- **The loop.** As in [CASE-099](CASE-099.md), with m = tanh(u) the interpretation's
  lean toward hypothesis A and a = tanh(v) the authority of the A-favouring
  sub-process over the B-favouring one, both bounded.
  - Authority shapes interpretation (β) in two ways: by a small direct
    push, and through attention. A reading r that favours the side with
    authority gets weight 1 + ζ|a|, and one against it 1 − ζ|a|, clipped
    to [0, 2]. This is the loop selecting its own evidence with no action,
    the attenuation of [THEORY-285](../theory.d/THEORY-285.md).
  - Interpretation shapes conferral (γ). Without commitment, authority is
    scored against the dominant interpretation, as in [CASE-092](CASE-092.md)'s Regime A.
  - Then u ← 0.9u + 0.05a + 0.15 Σ wᵢrᵢ and v ← 0.9v + η·score.
- **Action held fixed.** The hidden state h = ±1 switches every 300 steps.
  Nothing the loop does changes h, or when or whether an input arrives. A
  test checks that the world's sequence is the same whatever the loop.
- **Lock-in.** The loop fails a switch if it does not hold sign(m) = h for
  20 consecutive steps within the block. Only switches away from the
  interpretation held at the switch are counted, so a loop stuck on one
  side scores 1. A loop that does not follow the world even in the first
  block has no evidence, and is counted as **blind**, not locked in.
  - The default η = 0.5 was chosen so that the bare loop, sensory input
    alone, locks in on every seed. It is a loop that would lock in without
    anchors.
- **The candidates** of [QUESTION-121](../questions.d/QUESTION-121.md), each with the objection the question
  gives it:
  1. *Unselected input*, split into two switches.
     - The channel: an input every step, x = h + noise, read as
       r = x + κ₁m (the reading runs through the interpretation) and
       attenuable by attention.
     - *Exogenous capture*: a raw input surprising enough against the
       interpretation, |x − m| > θ, is attended at full weight whatever
       authority says.
  2. *The body.* A second input tied to h, noisier, read with a larger
     bend κ₂, since interoception is predicted, and attenuable. It has no
     capture.
  3. *Commitment before evidence.* The sub-processes commit predictions
     p_A = s + κ̄m and p_B = −s + κ̄m before the evidence arrives, and are
     scored by squared error against the evidence as attended and read,
     as in [CASE-106](CASE-106.md). This replaces Regime A's score.
     - "Without commitment" has two readings. The default is Regime A.
       The other has predictions revised after the evidence, which gives
       no score at all ([CLAIM-340](../claims.d/CLAIM-340.md)). Both were run.
  4. *Processing signals.* A content-free disfluency: the running mean of
     unsigned prediction error, averaged with attention weights, so that
     attenuation hides it. This is the objection from [THEORY-662](../theory.d/THEORY-662.md).
     Disfluency above its expected level shrinks u and v together.
  5. *Other people.* Testimony about h, arriving unasked on 5% of steps,
     read through the interpretation (κ₅). It is weighted by a trust
     learned from agreement with the interpretation, so whom to believe is
     selected.
- **The runs.** All 48 valid combinations of the six switches (capture
  needs the channel), and the 24 without commitment under the post-hoc
  reading. Each was run for 20 seeds of 3000 steps, under the default and
  18 one-at-a-time changes: η 0.3 and 1.0; ζ 0.5; κ₁ 0 and 0.5; κ₂ 0.4
  and 1.2; κ̄ 0, 0.2 and 0.8; θ 2 and 3; the disfluency gain 0.25 and 1;
  testimony rate 0.02 and 0.2; trust rate 0.2; sensory noise 2. That is
  1368 cells, in `results.jsonl`, summarised in `summary.txt`.

## What it shows

1. **The full loop does not lock in, and is redundant.** With every
   candidate present, the lock-in rate is 0 in all 19 variants. No single
   removal raises it above 0.05 in any variant. So no candidate is needed
   when the others are present.
2. **A removal that makes the loop lock in.** The loops that do not lock
   in, but would if any one switch were removed, are each one evidence
   channel plus one anchor. Over the 19 variants:
   - sense + commitment (17 variants), body + commitment (18) and
     testimony + commitment (19): removing commitment gives lock-in 1.0 at
     the default;
   - sense + processing signals (17) and body + processing signals (18):
     removing processing signals locks in;
   - sense + capture (16): removing capture locks in.
   Removing the channel from any of them leaves the loop blind. Counted
   over every non-locking loop of every variant, removing commitment made
   the loop lock in 159 times in 418, processing signals 137 in 400, and
   capture 32 in 266. Removing the senses did so 27 times in 498, each
   time taking capture with it or leaving testimony alone. Removing the
   body did so 5 times in 348, and removing testimony never (0 in 346).
3. **Evidence keeps the loop sighted; a score that the interpretation
   does not run anchors it.** In the Regime A loop the rule is: a loop
   with evidence avoids lock-in if and only if it has commitment,
   processing signals or capture. The rule held in 41 of the 44 non-blind
   configurations at the default, and in 37 to 42 of 44 per variant. The
   senses, the body and testimony, alone or together, lock in at the
   default: their arrival is unselected, but they are attended through
   the authority the interpretation confers.
4. **The exceptions.**
   - *Capture with the body present locks in*: 0.77 at the default, 0.51
     to 0.99 across variants. Capture frees only the sensory reading. The
     body's reading, attended and bent toward the interpretation,
     outweighs it. This is [CLAIM-342](../claims.d/CLAIM-342.md)'s caveat, that an independent
     channel anchors only as far as it outweighs the selected one, inside
     one mind. A lower threshold θ = 2 or noisier senses reduce it to
     0.12 to 0.17.
   - *Processing signals with testimony alone* are partial (0.39), or lock
     in when testimony is rare, trust is quick, or the gain is low.
   - *At weak attention coupling* (ζ = 0.5) the bare channels do not lock
     in at all, so there is nothing for an anchor to do.
   - At θ = 3, capture is rarely triggered, and sense + capture is
     partial (0.07).
5. **With revision after the evidence, nothing locks in.** Under the
   post-hoc reading of "without commitment", every non-blind configuration
   is free in every variant. Authority is never scored, so it never moves:
   no capture, and no learning of who predicts well ([CLAIM-340](../claims.d/CLAIM-340.md)).
6. **κ̄ did not bind here.** [CLAIM-340](../claims.d/CLAIM-340.md) says that, near symmetry,
   commitment couples interpretation to conferral with the sign of
   κ′ − κ̄. The variants κ̄ = 0, 0.2 and 0.8 gave the same outcomes. That
   includes body + commitment, where the body's κ₂ = 0.8 exceeds κ̄ = 0.
   The evidence gain of the committed score, 4ηs times the reading,
   outweighed the coupling it brings. Why was not diagnosed further.

## What it does not show

- That any of these mechanisms exists in a mind, or in the form given
  here. Each candidate is built to the question's description, and which
  removals lock the loop in follows from that design. The three anchors
  share a structure: each scores or weights the loop by something its
  authority does not set. The three evidence channels lack it by
  construction, since each is attenuable by authority or (for testimony)
  weighted by trust learned from agreement. The result shows that this
  difference is what decides here, not that minds are built so.
- That candidate 3 is equivalent to Regime B. That is [CLAIM-340](../claims.d/CLAIM-340.md)'s
  question, and this model does not linearize.
- Anything about contingency between intention and outcome, the other
  half of what [QUESTION-121](../questions.d/QUESTION-121.md) separates in the locked-in case. Action is
  absent throughout. The model has no intentions whose outcomes could be
  contingent.
- Robustness beyond one-at-a-time changes of 18 parameters, 20 seeds,
  and blocks of 300 steps.
