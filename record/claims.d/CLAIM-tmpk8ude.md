---
status: Proposed
title: 'An adaptive interface need not trade inference latency against perceptual latency: if its learning runs off the input and rendering path and changes the interface''s parameters only between actions, adaptation can take seconds while each response stays as fast as fixed physics; three timescales then come apart, the response, the adaptation and the evaluative horizon at which one can tell whether a command helped, and only the first is bounded by perception'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A study in which an interface whose parameters change only between
  gestures, with learning off the input and rendering path, is perceived
  as laggier or less predictable than the same interface with its
  parameters fixed at matched values, the difference attributable to the
  adaptation and not to the values; or an argument that useful adaptation
  of scrolling needs parameters to change within a gesture, so that the
  separation cannot be kept.
tags:
- control-theory
- learning-theory
- embodied-cognition
date: '2026-11-22'
line:
- will-organization
- distributed-agency
rests_on:
- CLAIM-711
- CLAIM-478
complements:
- CLAIM-787
summary: >-
  A's answer, in A5 and A8 of the exchange "Explain First Contact RL"
  (ChatGPT, 2026-11-22), to the owner's U3 concern that "inference latency
  relative to perceptual latency" might sink a smart scroll interface:
  "the intelligence should operate on a much slower timescale than the
  scrolling itself", so "inference latency can be hundreds of milliseconds
  or even seconds without creating perceptual input lag, provided it never
  blocks the rendering or input path"; and A8's further distinction
  between computational latency and the evaluative horizon, First
  Contact's Δ. It applies CLAIM-711 (slow constraints, fast enforcement)
  and CLAIM-478 (rates separate into constraint and realization) to an
  interface. The wording is A's (ChatGPT, in the exchange of 2026-11-22);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-711 CLAIM-478 CLAIM-787 CASE-tmptzhse — Proposed; the claims this applies and the case it answers -->

# CLAIM-tmpk8ude: An adaptive interface need not trade inference latency against perceptual latency

## The claim

The owner's worry (U3) is that a learned interface puts a model between
the finger and the screen. A's answer is that it need not. Split the
interface in two:

- a **fast loop** that maps each touch sample to motion by the current
  parameters, deterministically, every frame, with no model call;
- a **slow loop** that, between gestures and off the UI thread, reads what
  the user did and nudges the parameters, which are snapshotted at the
  start of each fling and never change during one.

The response is then as fast as fixed physics, and adaptation latency is
unconstrained by perception. What the model learns is "which stable
controller to deploy, not how to generate each movement" (A11 §5): the
parameters are a cached result of the learning.

## Three timescales

A8 separates two latencies the worry runs together, and the case adds the
third:

| Timescale | What bounds it |
|---|---|
| response, per frame | perception: a frame is 8.3 ms at 120 Hz |
| adaptation, between gestures or sessions | the rate at which evidence about the mapping accrues |
| evaluative horizon | how long after a command one must watch to know whether it helped, First Contact's Δ |

The third is CLAIM-787's subject: the horizon at which command-to-outcome
information tracks success is a level of a rate hierarchy. The first two
are this claim's. None need coincide.

## What it rests on

CLAIM-711: a process can be kept open to a slow governing process without
being delayed, if limits are set slowly in advance and enforced by
mechanisms faster than the process. Here the slow process sets the
parameters and the fast loop enforces them. CLAIM-478: where some degrees
of freedom settle faster than others, the slow ones act as constraints on
the fast over the window between the rates; the learned parameters are
such a constraint on the gesture. A8 adds a link to CLAIM-761, the learned
parameters as stored work ("amortized sensorimotor coordination"); that is
noted there as an analogy.

## Limits

The separation removes inference from the frame budget, not every cost:
learning on the main thread can still delay input (A5), and parameter
changes the user notices between gestures can feel like unpredictability
rather than lag, which is why A bounds them tightly. Whether bounded slow
adaptation is perceived as better, not merely as no worse, is the study's
question (CASE-tmptzhse).
