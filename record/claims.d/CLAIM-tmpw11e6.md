---
status: Proposed
title: 'What a system is prevented from rewriting or rejecting bounds what
  it can correct as well as enabling correction: in the record''s simulated
  sensor network a protected beacon that is itself miscalibrated drives the
  network''s error to the beacon''s own error while keeping it internally
  consistent, and the error falls only through a further, rarer protected
  channel that revises the beacon''s calibration, at that channel''s rate;
  so correction is relative to the anchors it answers to, and an anchor''s
  own errors need an anchor of their own'
version: 1
role: counter
warrant: demonstrated
defeated_if: A protected anchor whose own error the system it anchors can
  detect and correct without any further protected channel; or an error in
  the study (study_beacon_bias.py), such as the miscalibrated arm's late error
  not tracking the beacon's miscalibration.
tags:
- society-and-governance
- epistemology
- control-theory
date: '2026-11-23'
line:
- distributed-agency
objects_to:
- CLAIM-tmp4h9rc
grounds:
- CASE-tmp33vf4
complements:
- CLAIM-tmpvqmwc
- CLAIM-184
summary: 'The assistant''s qualification of the owner''s principle ([CLAIM-tmp4h9rc](CLAIM-tmp4h9rc.md)),
  from the arm [LEAD-177](../leads.d/LEAD-177.md)''s network study did not
  run: a beacon the revision can neither rewrite nor refuse, but which is
  miscalibrated. Run over 40 seeds on 2026-11-23 with the study''s own model.
  The wording is the assistant''s (Claude, in this session); adopting it is
  the owner''s call.'
corroborates:
- CLAIM-tmpklggb
---

<!-- inactive-ok-file: CLAIM-184 CLAIM-tmpcag0t — Proposed or Open; cited in this filing of 2026-11-23 -->

# CLAIM-tmpw11e6: What a system is prevented from rewriting or rejecting bounds what it can correct as well as enabling correction: in the record's simulated sensor network a protected beacon that is itself miscalibrated drives the network's error to the beacon's own error while keeping it internally consistent, and the error falls only through a further, rarer protected channel that revises the beacon's calibration, at that channel's rate; so correction is relative to the anchors it answers to, and an anchor's own errors need an anchor of their own

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
anchor's revision runs slower than the system it anchors ([CLAIM-tmpcag0t](CLAIM-tmpcag0t.md)).

## What it does not show

It is one model, with the miscalibration fixed and the survey assumed
correct. It does not show that every protected anchor must be revisable.
A protected anchor that is correct is [LEAD-177](../leads.d/LEAD-177.md)'s main result and needs no
survey.

## Note of 2026-11-23: what holds it back

<!-- inactive-ok-block: CLAIM-tmp4h9rc — Proposed; the owner's claim it qualifies -->
[CASE-tmp33vf4](../cases.d/CASE-tmp33vf4.md) is now Active and the miscalibrated arm reproduces (0.360
against a miscalibration of 0.361). Promoting this claim would make its
concession due on [CLAIM-tmp4h9rc](CLAIM-tmp4h9rc.md), the owner's own claim ([ADR-059](../decisions.d/ADR-059.md)), and
writing it in is the owner's. Its title's 'only through a further protected
channel' also reaches beyond the one model, as its body concedes.
