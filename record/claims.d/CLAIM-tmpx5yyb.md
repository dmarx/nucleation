---
status: Proposed
title: 'In the minimal construction of an executive, a reviewer and an enforcer whose agents anticipate enforcement, the first difference between the arrangement in which the executive can condition enforcement and the one in which enforcement is independent comes before execution: at the ruling where the reviewer avoids an order it expects to go unenforced, and at the executive''s own act where the executive anticipates too; so wherever independent enforcement would deter the act, the two arrangements are not alike in routine, and alikeness in routine holds only where that deterrence does not bind'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-168, from the
    runs of CASE-tmpwj1k2, as one of two alternative readings of the
    first difference. The other is CLAIM-tmpr54f9. Choosing which the
    record takes as the lead's answer is the owner's call.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in scratch/studies/lead-168/model.py or study.py whose
  correction leaves the executive's act the same in both arrangements
  at some grid point where the executive would withhold (g > kw) and
  independent enforcement would deter it ((1 - p)g <= pc), or makes the
  reviewer's ruling differ where it does not anticipate; or a payoff
  structure within the construction's terms in which a fully anticipating
  executive disposed to withhold is deterred under conditioned
  enforcement. Not defeated by agents who do not anticipate, which
  CLAIM-tmpr54f9 treats; by real institutions that behave otherwise, about
  which the claim says nothing; or by payoffs outside the two-term form
  stated in the case.
tags:
- society-and-governance
- game-theory
- causality
date: '2026-11-22'
line:
- distributed-agency
- dependence-and-domination
grounds:
- CASE-tmpwj1k2
uses:
- TERM-069
complements:
- CLAIM-tmpr54f9
corroborates:
- CLAIM-462
bears_on:
- QUESTION-278
summary: >-
  One of two alternative readings of where CASE-tmpwj1k2's arrangements
  first differ, filed for LEAD-168; the other is CLAIM-tmpr54f9. Solved
  by backward induction, the first difference moves earlier as
  anticipation deepens: to the ruling where the reviewer would rather
  abstain than issue an order it expects to go unenforced, and to the
  executive's act where the executive anticipates too, exactly where
  (1 − p)g ≤ pc. There the conditioned arrangement shows contestable
  acts the independent one deters, before any challenge, so the premise
  of QUESTION-278's construction, two arrangements alike in routine,
  holds only where independent enforcement would not have deterred the
  act. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpwj1k2 CLAIM-tmpr54f9 — new; the executed study and the alternative reading filed with this claim for LEAD-168 -->

# CLAIM-tmpx5yyb: In the minimal construction of an executive, a reviewer and an enforcer whose agents anticipate enforcement, the first difference between the arrangement in which the executive can condition enforcement and the one in which enforcement is independent comes before execution: at the ruling where the reviewer avoids an order it expects to go unenforced, and at the executive's own act where the executive anticipates too; so wherever independent enforcement would deter the act, the two arrangements are not alike in routine, and alikeness in routine holds only where that deterrence does not bind

## The claim

CASE-tmpwj1k2's part C gives the agents payoffs and solves each arrangement
by backward induction: the executive gains g while a contestable act
stands, loses c if it is reversed and kw if it withholds an order; the act
is challenged with probability p; the reviewer loses u by letting an
unlawful act stand and l by issuing an order that goes unenforced. Where
the executive would not withhold (g ≤ kw), C behaves as I at every depth.
Where it would:

1. **Reviewer anticipates.** Where l > u, the reviewer abstains in C and
   orders in I, so the traces part at the ruling, before any enforcement
   event. A court that weighs the risk of an unenforced order shows the
   conditioning in what it decides, not in what follows.
2. **Executive anticipates too.** The executive takes the contestable act
   in C always, and in I only if (1 − p)g > pc. Where independent
   enforcement deters it, the traces part at the act itself: C shows
   contestable acts, unchallenged, that I does not. On the grid, 566 of
   the 1,540 points where the executive would withhold part there, and
   the boundary matched the analytic one at every point checked.

So the "alike in routine" premise of A9's construction is not free. With
an anticipating executive, two arrangements alike in routine and parting
only under a challenge exist only where independent enforcement would not
have deterred the act anyway. Elsewhere the conditioning shows in the
routine, as what the executive dares to do.

## Why it matters

As a reading of LEAD-168's "first difference", this one says the
difference A9 placed under challenge can come before the challenge, as a
shift in the distribution of the executive's acts; it is the ex ante face
of CLAIM-464, an actor arranging what correction would cost before it
acts. It corroborates CLAIM-462 from the other side: what the arrangement
can correct shapes what is done in it, so a loss of correctability can
show up as bolder effective action rather than as anything visible in
correction. And it marks a limit on CLAIM-414's method for this question:
matched routine trajectories are available only for agents who do not
anticipate, or where deterrence does not bind.

## What it does not say

- That anticipating agents are the right model of real executives or
  courts, or how deep anticipation runs in any case; the depths are
  stipulated.
- That the earlier differences are observable in practice; a shift in the
  rate of contestable acts needs a counterfactual baseline that a single
  arrangement does not supply.
- That this is beyond a conventional game-theoretic model. It *is* one;
  A9 expected the difference to be explainable that way.
