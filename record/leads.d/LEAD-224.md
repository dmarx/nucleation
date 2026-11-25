---
number: 224
status: Open
formerly:
- LEAD-tmplps4n
title: 'Run a staged smart-scroll study: instrument default scrolling, adapt one friction parameter from correction statistics, then optimize a First Contact score over gesture windows, and ask whether the friction that minimizes corrections is the friction that maximizes the score'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- information-theory
- control-theory
- learning-theory
date: '2026-11-22'
line:
- will-organization
- distributed-agency
advances:
- CLAIM-1191
- CLAIM-1122
- CLAIM-788
operationalized_in:
- CASE-419
summary: >-
  From A5 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-22),
  on the owner's proposal (U2, U3): stage the smart-scroll study so that the
  behavioural signal is validated before the information-theoretic one is
  added. The divergence test is A's: "does optimizing correction frequency
  actually produce the same friction setting as optimizing mutual
  information?" The wording is A's (ChatGPT, in the exchange of
  2026-11-22); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1191 CLAIM-1122 CLAIM-788 CASE-419 — Proposed; the claims this would test and the case holding its design -->

# LEAD-224: Run a staged smart-scroll study: instrument default scrolling, adapt one friction parameter from correction statistics, then optimize a First Contact score over gesture windows, and ask whether the friction that minimizes corrections is the friction that maximizes the score

## What to do

The design is part 3 of [CASE-419](../cases.d/CASE-419.md).

1. **Passive.** Record touch and scroll traces under default physics with
   known targets; test whether reversals, pauses and repeated gestures
   predict independently measured difficulty.
2. **One parameter.** Adapt post-release friction within ±15 % from
   correction statistics, between gestures only, off the UI thread.
3. **The score.** Optimize an estimate of First Contact's score over
   gesture windows, the estimate taken from realized gestures under each
   setting, not computed from the physics ([CLAIM-1191](../claims.d/CLAIM-1191.md)).
4. **Compare** the friction each stage settles on, and both against fixed
   physics, on target acquisition, corrections and rated predictability.

## What it would move

- **[CLAIM-1191](../claims.d/CLAIM-1191.md)**: an interior optimum of the score over friction is
  evidence that the user's commands depend on the setting; no optimum, or
  a drift to the extreme, is what the claim predicts at fixed behaviour.
- **[CLAIM-1122](../claims.d/CLAIM-1122.md)**: stage 2 is its direct test, adaptation with no
  perceptual cost.
- **[CLAIM-788](../claims.d/CLAIM-788.md)**: whether command-to-outcome information picks out a usable
  channel in a continuous motor task, as it did for a cursor rotation.

## Cost

A native mobile prototype with an adjustable deceleration parameter (A5
names iOS's `decelerationRate` and Android's `OverScroller`), a gesture
logger and a small user study; the MI estimator only at stage 3.
