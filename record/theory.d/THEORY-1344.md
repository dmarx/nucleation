---
number: 1344
status: Active
formerly:
- THEORY-tmpuw92f
title: 'Empowerment is the channel capacity from an agent''s next n actions to its sensor n steps later, an open-loop, interventional measure of how many perceptibly different futures the agent can bring about, which counts no control the agent cannot perceive; given side information about the channel''s state it is never lower, so it is ordered by what the agent can read, from full state through its own sensor history to none'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11, by topic (probability and
    information), ADR-091. corroborates CLAIM-354, whose note of
    2026-11-03 (later) weighs empowerment against the claim's defeat
    condition and finds it "does not collapse this claim's profile to a
    scalar", because it is "open-loop, depends on the horizon and
    ignores cost and viability". The claim does not need it. No other
    change.
tags:
- information-theory
- agency
date: '2026-11-03'
source:
- LIT-1965
- LIT-1951
summary: >-
  Klyubin, Polani and Nehaniv (2005, 2008), [LIT-1965](../literature.d/LIT-1965.md) and [LIT-1951](../literature.d/LIT-1951.md),
  read in full in [NOTE-1511](../notes.d/NOTE-1511.md) and [NOTE-1514](../notes.d/NOTE-1514.md). Active as definitions
  and one inequality, re-derived. It does not say empowerment is what
  organisms maximize, which the authors offer as a hypothesis in a weak
  form only, nor that it prices control cost or viability.
corroborates:
- CLAIM-354
---
<!-- inactive-ok-file: THEORY-1336 — Proposed; the cart-pole result, cited for what this definition does not say -->

# THEORY-1344: Empowerment is the channel capacity from an agent's next n actions to its sensor n steps later, an open-loop, interventional measure of how many perceptibly different futures the agent can bring about, which counts no control the agent cannot perceive; given side information about the channel's state it is never lower, so it is ordered by what the agent can read, from full state through its own sensor history to none

## Source

Klyubin, Polani and Nehaniv (2005), [LIT-1965](../literature.d/LIT-1965.md), eq. 3; (2008),
[LIT-1951](../literature.d/LIT-1951.md), eqs. 1–3. Read in [NOTE-1511](../notes.d/NOTE-1511.md) and [NOTE-1514](../notes.d/NOTE-1514.md).

## What was actually shown

**Definition.** ℰ = max_{p(aⁿ)} I(Aⁿ_t; S_{t+n}), with the actions drawn from
an independent source so the channel p(s_{t+n} | âⁿ) is the causal effect
(2008, pp. 2–3). Open-loop: actions are not chosen on sensor feedback.

**Perceived control only.** "We define what an agent does solely in terms of
what it perceives" (2005, p. 129); control visible to an outside observer
but not to the agent's sensors adds nothing.

**Contextual empowerment.** ℰ(· | C) = Σ_c p(c) ℰ(· | C = c), the capacity
with side information at sender and receiver; never below the context-free
value (2008, eq. 3). Re-derived: with A independent of C,
I(A; S | C) = I(A; S, C) ≥ I(A; S). The best context is the global state;
the agent's own history "constitutes an upper limit on what the agent can
possibly know" (2008, p. 4).

## What this does not say

- That a high-empowerment state is reachable or sustainable: in the
  cart-pole the maxima are not ([THEORY-1336](THEORY-1336.md)).
- That it measures cost, viability or closed-loop control.
- That it is a universal drive in organisms.
