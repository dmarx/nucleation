---
status: Active
title: 'Empowerment is the channel capacity from an agent''s next n actions to its sensor n steps later, an open-loop, interventional measure of how many perceptibly different futures the agent can bring about, which counts no control the agent cannot perceive; given side information about the channel''s state it is never lower, so it is ordered by what the agent can read, from full state through its own sensor history to none'
version: 1
tags:
- information-theory
- agency
date: '2026-11-03'
source:
- LIT-tmpd2pdj
- LIT-tmp3h572
summary: >-
  Klyubin, Polani and Nehaniv (2005, 2008), LIT-tmpd2pdj and LIT-tmp3h572,
  read in full in NOTE-tmpeeo19 and NOTE-tmpgoetm. Active as definitions
  and one inequality, re-derived. It does not say empowerment is what
  organisms maximize, which the authors offer as a hypothesis in a weak
  form only, nor that it prices control cost or viability.
---
<!-- inactive-ok-file: THEORY-tmpoy5a7 — Proposed; the cart-pole result, cited for what this definition does not say -->

# THEORY-tmpuw92f: Empowerment is the channel capacity from an agent's next n actions to its sensor n steps later, an open-loop, interventional measure of how many perceptibly different futures the agent can bring about, which counts no control the agent cannot perceive; given side information about the channel's state it is never lower, so it is ordered by what the agent can read, from full state through its own sensor history to none

## Source

Klyubin, Polani and Nehaniv (2005), LIT-tmpd2pdj, eq. 3; (2008),
LIT-tmp3h572, eqs. 1–3. Read in NOTE-tmpeeo19 and NOTE-tmpgoetm.

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
  cart-pole the maxima are not (THEORY-tmpoy5a7).
- That it measures cost, viability or closed-loop control.
- That it is a universal drive in organisms.
