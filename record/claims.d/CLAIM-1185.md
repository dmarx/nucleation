---
number: 1185
status: Active
formerly:
- CLAIM-tmpw11e6
title: 'What a system is prevented from rewriting or rejecting can bound what it can correct as well as enable correction: in the record''s simulated sensor network a protected beacon that is itself miscalibrated drives the network''s error to the beacon''s own error while keeping it internally consistent, the network''s own revision does not lower it, and in the runs it fell only when a further, rarer protected channel revised the beacon''s calibration, at that channel''s rate'
version: 4
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §13.7. No other change.
- version: 3
  date: '2026-11-24'
  note: >-
    Title narrowed at the owner's word of 2026-11-24 ("handle the fixes
    for the twelve ... use your best judgement", under the dialectic
    regime; ADR-057, ADR-047's narrowing rule), as the promotion table
    of that date and the note of 2026-11-23 asked: "only through a
    further protected channel" and the closing generalization reached
    beyond the one model, as the body's "What it does not show"
    conceded. The title now says what the 40-seed study shows, with
    "bounds" made "can bound". Old title: "What a system is prevented
    from rewriting or rejecting bounds what it can correct as well as
    enabling correction: in the record's simulated sensor network a
    protected beacon that is itself miscalibrated drives the network's
    error to the beacon's own error while keeping it internally
    consistent, and the error falls only through a further, rarer
    protected channel that revises the beacon's calibration, at that
    channel's rate; so correction is relative to the anchors it answers
    to, and an anchor's own errors need an anchor of their own". The
    dropped generalization, "so correction is relative to the anchors it
    answers to, and an anchor's own errors need an anchor of their own",
    is the record's own extrapolation and is filed as the Proposed
    interpretive claim CLAIM-1282, resting on this one, with this
    entry's old general defeater, "A protected anchor whose own error
    the system it anchors can detect and correct without any further
    protected channel" (status-review README, narrowing kind 2). The
    defeated_if is restated for the model.
- version: 4
  date: '2026-11-24'
  note: >-
    Promoted to Active at the same word (ADR-057): it has no premise,
    its ground CASE-390 is Active and its miscalibrated arm was rerun at
    that case's promotion on 2026-11-23 (late error 0.360 against a
    miscalibration of 0.361), no objection targets it, and nothing meets
    its narrowed defeated_if. A counter: its status is credence in
    itself (ADR-059), so promoting it makes its concession due on the
    owner's CLAIM-1024, which is the owner's to write (A53's wording is
    a candidate, in CLAIM-1024's note of 2026-11-24). Listed for the
    owner in the pull request.
role: counter
warrant: demonstrated
defeated_if: >-
  An error in the study (study_beacon_bias.py), such as the miscalibrated
  arm's late error not tracking the beacon's miscalibration; or, in its
  model, a run in which the miscalibrated beacon's error is lowered without
  the survey channel that revises its calibration, or in which that channel
  lowers it faster than its rate allows.
tags:
- society-and-governance
- epistemology
- control-theory
date: '2026-11-23'
line:
- distributed-agency
objects_to:
- CLAIM-1024
grounds:
- CASE-390
complements:
- CLAIM-1183
- CLAIM-184
summary: 'The assistant''s qualification of the owner''s principle ([CLAIM-1024](CLAIM-1024.md)),
  from the arm [LEAD-177](../leads.d/LEAD-177.md)''s network study did not
  run: a beacon the revision can neither rewrite nor refuse, but which is
  miscalibrated. Run over 40 seeds on 2026-11-23 with the study''s own model.
  The wording is the assistant''s (Claude, in this session); adopting it is
  the owner''s call.'
corroborates:
- CLAIM-1125
works:
- governance-of-possibility
---

<!-- inactive-ok-file: CLAIM-184 CLAIM-1070 — Proposed or Open; cited in this filing of 2026-11-23 -->

# CLAIM-1185: What a system is prevented from rewriting or rejecting can bound what it can correct as well as enable correction: in the record's simulated sensor network a protected beacon that is itself miscalibrated drives the network's error to the beacon's own error while keeping it internally consistent, the network's own revision does not lower it, and in the runs it fell only when a further, rarer protected channel revised the beacon's calibration, at that channel's rate

## The result

[LEAD-177](../leads.d/LEAD-177.md)'s network (scratch/studies/lead-177/network.py) is unchanged by
default; its committed arms reproduce exactly. Two options were added and
run over 40 seeds (`study_beacon_bias.py`, `results/beacon_bias_summary.md`):

- **anchored, beacon correct:** late error 0.044, radius 0.114 (as
  published).
- **anchored, beacon miscalibrated by δ = (0.3, −0.2), |δ| = 0.361:**
  late error 0.360 (0.328 to 0.393), radius 0.114. The network converges
  on the beacon's error. It is as internally consistent as with a correct
  beacon, and its error approaches the uncorrected arms' (fixed 0.399,
  self 0.402).
- **the same, with a survey every 100 steps:** late error 0.122 (0.086 to
  0.151). The survey is a rarer protected event read through the beacon's
  channel, used only by a slower revision of the beacon's calibration.
- **the same, with a survey every 500 steps:** late error 0.293.

## What it shows

Protection that makes correction possible also fixes what correction
answers to. An unrewritable, unrefusable anchor imports its own error
whole, and nothing inside the system can see it, since consistency is
unaffected. Correcting the anchor needs evidence about the anchor that
does not pass through it: a further protected channel. Recovery is
bounded by that channel's rate. This is [CLAIM-342](CLAIM-342.md) again, one level up.
The regress stops at whatever is not itself revised. That is the
entrenchment [CLAIM-184](CLAIM-184.md) warns of, now with a measured cost. It is also the
response-spectrum point from the exchange "Explain First Contact RL": the
anchor's revision runs slower than the system it anchors ([CLAIM-1070](CLAIM-1070.md)).

## What it does not show

It is one model, with the miscalibration fixed and the survey assumed
correct. It does not show that every protected anchor must be revisable.
A protected anchor that is correct is [LEAD-177](../leads.d/LEAD-177.md)'s main result and needs no
survey.

## Note of 2026-11-23: what holds it back

<!-- inactive-ok-block: CLAIM-1024 — Proposed; the owner's claim it qualifies -->
[CASE-390](../cases.d/CASE-390.md) is now Active and the miscalibrated arm reproduces (0.360
against a miscalibration of 0.361). Promoting this claim would make its
concession due on [CLAIM-1024](CLAIM-1024.md), the owner's own claim ([ADR-059](../decisions.d/ADR-059.md)), and
writing it in is the owner's. Its title's 'only through a further protected
channel' also reaches beyond the one model, as its body concedes.
