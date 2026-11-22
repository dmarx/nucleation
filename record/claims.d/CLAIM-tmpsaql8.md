---
status: Proposed
title: 'In a queueing model whose overseer keeps the same authority, information and reviewers at every speed, making the acting institution''s actions irreversible sooner lowers the share of objectionable actions stopped in time gradually and from before the timing condition fails at the means; at the settings run, precommitted limits win back the share they foresee and automatic suspension the share detected in time, each delaying only what it holds, while a pause wins back capacity only by giving up the speed, and wins back none when speed also multiplies the volume of actions'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-068, from the
    runs of CASE-tmp8riid.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in scratch/studies/lead-068/model.py or study.py whose
  correction reverses one of the claim's orderings at the settings run:
  the fast arm's intercepted share not below the slow arm's; limits'
  restored share departing from their coverage by more than sampling;
  suspension restoring more than the share detected before
  irreversibility; or a pause restoring as much of the gap as limits or
  suspension while keeping as much of the benefit. Or, in the same model,
  a setting of the fixed oversight within the ranges of the study's
  section D under which the fast arm stops as large a share as the slow
  arm. Not defeated by real institutions that behave otherwise, about
  which the claim says nothing; by limits of low coverage, which the claim
  allows; or by settings far outside those run, such as limits whose false
  positives hold most benign actions, where the claim does not say which
  remedy keeps more benefit.
tags:
- society-and-governance
- operations-research
- probabilistic-modeling
date: '2026-11-22'
line:
- distributed-agency
- dependence-and-domination
grounds:
- CASE-tmp8riid
corroborates:
- CLAIM-462
- CLAIM-706
bears_on:
- QUESTION-278
summary: >-
  The assistant's, from carrying out LEAD-068, the simulation arm of
  CASE-285. Over 20 seeds: at ten times the speed the share of
  objectionable actions stopped before irreversibility fell from 0.994 to
  0.396, already 0.711 at five times, where A23 §3's condition still holds
  at the means; with volume multiplied too, to 0.043. In the fast arm,
  limits restored their coverage of the gap keeping 0.92 to 0.99 of the
  speed's benefit, suspension at most the 0.54 detected in time keeping
  0.91 to 0.99, and pauses restored half the gap for a third of the
  benefit and none of it under the volume reading. It is a demonstration
  in an invented model: it shows that speed alone can separate an
  institution's action from its correction (CLAIM-462) and that a step
  which holds what it catches and delays nothing else can carry
  intervention opportunity without impedance (CLAIM-706), not that any
  institution works so. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp8riid — new; the study this claim rests its evidence on, filed with it -->
<!-- inactive-ok-file: CASE-285 CLAIM-706 CLAIM-710 CLAIM-711 CLAIM-730 TERM-125 — Proposed; the design carried out and the entries the result bears on -->

# CLAIM-tmpsaql8: In a queueing model whose overseer keeps the same authority, information and reviewers at every speed, making the acting institution's actions irreversible sooner lowers the share of objectionable actions stopped in time gradually and from before the timing condition fails at the means; at the settings run, precommitted limits win back the share they foresee and automatic suspension the share detected in time, each delaying only what it holds, while a pause wins back capacity only by giving up the speed, and wins back none when speed also multiplies the volume of actions

## The claim

CASE-tmp8riid carries out CASE-285's design as a queueing model. The
overseer's authority (an objection suspends), information (detection
delay) and resources (four reviewers, fixed evaluation time) are the same
at every speed; only the time before an action becomes irreversible
changes, and in a second reading the volume of actions with it. The claim
is what the runs show, in four parts.

1. **Speed alone lowers intervention capacity, gradually.** From 0.994 at
   s = 1 to 0.711 at s = 5 and 0.396 at s = 10. A23 §3's timing condition
   read deterministically at the means predicts a step at s ≈ 8; the
   spread of detection, review and irreversibility makes the loss start
   long before it. Lower in all ten other settings of the fixed oversight
   tried.
2. **Limits win back what they foresee.** The share of the gap restored
   equals their coverage q, at a cost in delay paid only by the benign
   actions they hold.
3. **Suspension wins back what is seen in time.** Its ceiling is the share
   of objectionable actions detected before they are irreversible, 0.72 at
   s = 10, so 0.54 of the gap.
4. **Pauses win back capacity only as speed.** Every action waits, so the
   benefit kept falls as the gap restored rises (0.49 restored for 0.65
   kept, 1.0 for none). Where speed also multiplies volume, a fixed review
   capacity stays saturated however long the pause, and none is restored.

The argument for the parts beyond the construction is the runs; parts 2
and 3 are also near identities of the model, checked in its tests (full
coverage stops everything, full flagging stops exactly what is detected
in time).

## What it does not say

- That any real overseer loses effect this way, or that real limits foresee
  much. The rates are invented; that speed lowers capacity is built into
  the timing condition the model embodies. The claim is about the model's
  shape and the remedies' comparison.
- That precommitted limits are always the better remedy. Under the volume
  reading their false positives saturate the same reviewers, and held
  benign actions wait months; with fp = 0.30 they kept 0.69 of the benefit.
- Whether a limit is friction. The model's limits hold what they catch and
  delay nothing else, which is CLAIM-706's gate without impedance; whether
  that defeats CLAIM-710's "characterizes" reading or is CLAIM-711's
  friction relocated turns on TERM-125, which stays open.
- Anything about CLAIM-730's first clause, which needs an affected party
  and a slow rule that could be revised, neither of which the model has.
