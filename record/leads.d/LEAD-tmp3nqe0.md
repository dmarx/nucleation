---
status: Open
title: 'Test in a repeated-judgement task whether an anchor''s or a frame''s influence persists after it is withdrawn and challenged, depends on the path by which later evidence arrives and transfers to judgements it never touched, to tell anchoring by nucleation from insufficient adjustment and selective accessibility'
version: 1
stage: idea
priority: low
method:
- empirical
tags:
- cognition
- complex-systems
date: '2026-11-24'
line:
- nucleating-argument
advances:
- CLAIM-tmpggu4v
- CLAIM-315
summary: >-
  From A11 §7 of the exchange "Memes, Contracts, and Systemic Normativity"
  (2026-11-24), which names the evidence that would separate the three
  mechanisms of anchoring, "persistence, transfer, hysteresis or
  organizational transformation", and gives no design. The plan is a gap
  fill ([ADR-137](../decisions.d/ADR-137.md)). The wording of the plan is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpggu4v CLAIM-315 — Proposed or new; the claims this lead tests -->

# LEAD-tmp3nqe0: Test in a repeated-judgement task whether an anchor's or a frame's influence persists after it is withdrawn and challenged, depends on the path by which later evidence arrives and transfers to judgements it never touched, to tell anchoring by nucleation from insufficient adjustment and selective accessibility

## Why a new task

The comparative anchoring paradigm ([CLAIM-315](../claims.d/CLAIM-315.md), [THEORY-335](../theory.d/THEORY-335.md), [THEORY-337](../theory.d/THEORY-337.md)) asks
one estimate once. Nothing in it can persist, show hysteresis or transfer,
so it cannot separate the third mechanism A11 proposes from the two it
already has.

## The plan

1. **A maintained judgement.** A series of related estimates over several
   sessions, for instance repeated valuations or risk ratings in one
   domain, in which a response organization can form.
2. **Anchor, then withdraw.** An anchor in the first session only; in later
   sessions, evidence that moves the true value up and then back down
   (and, in another arm, down then up).
3. **Read three things.** Decay: does the anchor's influence fall with each
   session of adjustment (insufficient adjustment)? Hysteresis: at the same
   evidence, does the judgement differ by the path that led there ([CASE-111](../cases.d/CASE-111.md)'s
   fold; [CLAIM-463](../claims.d/CLAIM-463.md))? Transfer: does the anchored scale carry into related
   judgements the anchor never touched?
4. **Measure accessibility apart.** A recognition or retrieval measure of
   anchor-consistent knowledge in each session, so that persistence carried
   by accessibility (selective accessibility) is told from persistence
   that outlasts it, mindful of [THEORY-335](../theory.d/THEORY-335.md)'s finding that this measure has
   so far found nothing.
5. **The framing arm.** The same series with a gain or loss frame in the
   first session (A11 §8's "transient frame activation" against "durable
   perspectival transformation").

## What it would settle

Whether [CLAIM-tmpggu4v](../claims.d/CLAIM-tmpggu4v.md)'s third mechanism occurs at all; its `defeated_if`
is a null on decay, hysteresis and transfer together.
