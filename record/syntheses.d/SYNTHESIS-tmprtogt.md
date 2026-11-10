---
status: Proposed
title: 'What classification training leaves in a network''s last layers, and what it costs for tasks it was not trained on, is open: collapse onto class means is measured in one protocol and derived only for squared error or as an endpoint, its cost is measured for new classes at the penultimate layer, and whether it holds beyond its first settings, under lazy training, and while the parameters keep moving are questions of their own'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the learned-structure line (the last-layer structure
  classification training leaves, and its cost) left out without a
  reason given; or a link this account states that no component states.
  Its standing is its components'.
tags:
- representation-learning
- learning-theory
date: '2026-11-10'
line:
- learned-structure
integrates:
- QUESTION-051
- QUESTION-080
- QUESTION-181
- QUESTION-192
- QUESTION-202
- QUESTION-236
bears_on:
- QUESTION-051
---
<!-- inactive-ok-file: ADR-083 THEORY-286 — Proposed; components, citations and the decisions this account follows, with their standing -->

# SYNTHESIS-tmprtogt: What classification training leaves in a network's last layers, and what it costs for tasks it was not trained on, is open: collapse onto class means is measured in one protocol and derived only for squared error or as an endpoint, its cost is measured for new classes at the penultimate layer, and whether it holds beyond its first settings, under lazy training, and while the parameters keep moving are questions of their own

*A part account of the learned-structure line (ADR-083); the line's account is built over it and its sibling parts. Every component is a question.*

## The account

- **The root.** QUESTION-051 (filed in the fourth synthesis pass, the
  record's; Open) asks what structure training for one classification
  task leaves in the last layers and what it costs elsewhere. Its body
  holds collapse measured (THEORY-083), derived under squared error with a
  re-whitened flow (THEORY-278) or as an endpoint under imbalance
  (THEORY-286), absent under lazy training (THEORY-294), and its cost for
  new classes at the penultimate layer (THEORY-246). It says "The
  derivation for cross-entropy asked for below is still open".
- **Its refinements.** Five questions refine QUESTION-051. Four hold the
  promotion conditions of the readings named: QUESTION-202 (THEORY-083,
  collapse outside its first protocol, and a derivation for
  cross-entropy), QUESTION-181 (THEORY-278, whether trained networks
  follow the renormalized flow), QUESTION-192 (THEORY-294, lazy training
  beyond the proportional-kernel case) and QUESTION-236 (THEORY-246,
  transfer against separation beyond ImageNet-trained ResNet-50s).
  QUESTION-080 (the assistant's, from reading Kunin et al., filed at the
  owner's request) asks what stays fixed while a converged network's
  parameters keep moving, and whether collapse does; its summary says
  "Nothing in the record relates them".

Outside this part, QUESTION-164 (SYNTHESIS-tmpexmgz) says it bears on QUESTION-080,
"since motion along a symmetry changes no function". No other relation or
mention joins this part to the line. QUESTION-051's summary says it bears
on QUESTION-010 (pragmatic-transport) and CLAIM-164 (distributed-agency).

## The components

- QUESTION-051, the record's (2026-10-12), Open.
- QUESTION-080, the assistant's, filed at the owner's request, Open.
- QUESTION-181, QUESTION-192, QUESTION-202 and QUESTION-236, promotion
  conditions moved from THEORY-278, THEORY-294, THEORY-083 and
  THEORY-246 (2026-10-19 and 2026-10-20), Open.

## Links tested as claims

None. The links are `refines` and one mention, and no component offers an
integration to test.

## Not stated on the record

- **QUESTION-202 and QUESTION-051's derivation.** QUESTION-202's second
  half, whether gradient descent on cross-entropy provably reaches
  collapse, is the derivation QUESTION-051's "What would answer it" asks
  for. QUESTION-202 refines QUESTION-051, and neither says the one is
  the other's.

## What it does not say

- That collapse holds outside its first protocol, or that training
  reaches it for a stated reason.
- That the cost of separation for new classes is general (QUESTION-236).
- Anything with standing of its own.
