---
status: Proposed
title: 'A toy of exit-driven drift: an organization that sets a practice each period by revenue less a penalty for complaints from its present users, where the practice harms one group, whose members complain and leave at a rate rising with it, raises the practice from 0.05 to 0.223 as that group''s share falls from 0.30 to 0.18, with no act against complaint'
version: 1
standing: stipulated
kind: construction
tags:
- social-science
- society-and-governance
- complex-systems
date: '2026-11-12'
line:
- organizational-normativity
- distributed-agency
illustrates:
- CLAIM-tmphgjbz
bears_on:
- QUESTION-441
summary: >-
  The assistant's construction, built at the owner's acceptance on
  2026-11-12 of the ideas offered after filing the exchange "Medical
  Ethics and Media Enshitification" (2026-11-11). It grounds
  CLAIM-tmpavez3. Run with python3 -I on 2026-11-12; the figures below are
  its output, and the model is stated in full so that it can be rerun.
  Its parameters are arbitrary, and it shows a possibility, not a
  measurement. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpavez3 CLAIM-tmphgjbz CLAIM-tmpvceet — Proposed; filed from the exchange of 2026-11-11 and its follow-up -->

# CASE-tmp34j9u: A toy of exit-driven drift: an organization that sets a practice each period by revenue less a penalty for complaints from its present users, where the practice harms one group, whose members complain and leave at a rate rising with it, raises the practice from 0.05 to 0.223 as that group's share falls from 0.30 to 0.18, with no act against complaint

## The model

Two groups of users. Demanders are harmed by a practice of intensity
x ∈ [0, 1] and complain at rate c·x each; quiet users are not harmed and do
not complain. Each period a_d = 30 demanders and a_q = 70 quiet users
arrive. Demanders leave at rate e0 + e1·x with e0 = 0.1 and e1 = 0.4; quiet
users leave at rate e0.

Each period the organization chooses x to maximize its score on the users
it has now:

S(x) = N·(1 + b·x − g·x²/2) − λ·N_d·c·x, with b = 1, g = 2, λ = 3, c = 1,

so x* = (b − λ·c·s)/g, clipped to [0, 1], where s = N_d/N is the
demanders' share. Nothing in the model acts on complaints: they are
counted honestly, every demander present complains at the same rate, and
no channel is changed.

## What it gives

Starting at the steady state of x = 0 (s = 0.30):

| period | x | demanders' share | recognized complaints |
|---|---|---|---|
| 0 | 0.050 | 0.300 | 15.0 |
| 5 | 0.083 | 0.278 | 22.3 |
| 20 | 0.170 | 0.220 | 33.5 |
| 199 | 0.223 | 0.185 | 35.4 |

A control arm scores the same organization on its initial population, so
that exit is invisible to it. It keeps x = 0.05 throughout.

The drift is general in the model, not tuned. x* falls with s, and s falls
with x through demanders' exit, so the map x ↦ x*(s(x)) is increasing.
Iterated from x*(s0), it climbs to the fixed point x = 0.223, s = 0.185,
whenever e1 > 0 and the optimum is interior.

## What it shows, and what it does not

- The practice rises 4.5-fold, and so does the harm to each arriving
  demander. Recognized complaints rise only 2.4-fold. At the fixed point
  only e0/(e0 + e1·x) = 53% of the demanders the inflow has supplied are
  still present to complain. The measure records a shrinking fraction of
  the harm.
- Recognized complaints do not fall. In steady state they equal
  a_d·c·x/(e0 + e1·x), which increases with x. So the drift is not
  "fewer complaints". It is a falling marginal penalty: λ·c·N_d drops as
  the demanders leave.
- A toy with arbitrary parameters and a myopic optimizer. It shows that the
  route exists, not that any organization follows it.
