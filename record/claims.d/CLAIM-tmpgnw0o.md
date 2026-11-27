---
status: Proposed
title: 'An engine steers toward a stable point by lowering publishers'' responsiveness'
statement: >-
  On the convergence condition for repeated retraining, the engine's lever
  is the sensitivity of the web to its ranking, ε, more than its own loss;
  penalties for detected manipulation, delays between a change and its
  reward, and opacity about what the ranking reads each lower ε, by raising
  the cost or lowering the speed of publishers' response, and so move the
  game toward the regime in which retraining converges; and an engine that
  anticipated the response instead of retraining on it, aiming at the
  performative optimum, would choose to read signals that are costly to
  manipulate, which is the escape condition of CLAIM-tmpe27ub
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Evidence that penalties, delays and opacity do not reduce the shift in
  published content per change of ranking; or an engine that anticipates
  publishers' response and still does best by reading cheaply manipulable
  signals.
tags:
- learning-theory
- economics
date: '2026-11-27'
line:
- learned-structure
answers:
- QUESTION-tmpqba7g
rests_on:
- CLAIM-tmph131t
- CLAIM-tmpe27ub
- CLAIM-tmpcrves
grounds:
- THEORY-861
summary: >-
  Filed at the owner's "relate SEO to performative prediction"
  (2026-11-27). THEORY-861's condition, ε < γ/β, has two sides; this claim
  says the engine works mostly on ε. That anticipating the response, as in
  strategic classification, leads to signals costly to manipulate is the
  assistant's reading, not a result the record holds. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmph131t CLAIM-tmpe27ub CLAIM-tmpcrves QUESTION-tmpqba7g — Proposed, Open or new; the claims it rests on and the question -->

# CLAIM-tmpgnw0o: An engine steers toward a stable point by lowering publishers' responsiveness

## The claim

THEORY-861: retraining converges when ε < γ/β. Here ε is how far the
distribution moves per change of the model, and γ/β is a property of the
loss. An engine can change its loss somewhat. It can change ε much more,
through three tools:

| Tool | How it lowers ε |
|---|---|
| Penalties for detected manipulation | raise the expected cost of responding, so less of the web responds |
| Delay between a change and its reward (sandboxing new pages, slow trust) | make each round's response smaller |
| Opacity about what is read (CLAIM-tmpcrves) | slow publishers' learning of the ranking, so they track it less closely |

On this reading, the engine's anti-spam practice is less a set of moral
sanctions than control of the distribution map's sensitivity.

## The other route

Retraining on the response reaches a stable point at best. An engine that
*anticipated* the response could aim at the performative optimum instead,
the ranking that does best given how publishers will react. That optimum
would favour signals publishers cannot move cheaply, since a signal that
moves under manipulation costs the engine accuracy at the next round. That
is CLAIM-tmpe27ub's escape condition, reached as the engine's own optimum.

## What it does not say

That lowering ε is costless. Opacity and penalties fall on honest publishers
too (CLAIM-tmpcrves).
