---
status: Proposed
title: 'First Contact''s score is information under the user''s realized commands, empowerment the capacity of the same kind of channel maximized over commands; the score is at most the capacity, so an interface can offer high capacity, precise control in principle, through commands its user does not or cannot produce, and the score, unlike empowerment, registers that shortfall'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A case where First Contact's control term, taken under the user's actual
  command distribution, exceeds the capacity of the interface's
  command-to-state channel at the same horizon; or a showing that the
  score as the paper estimates it is not taken under the realized command
  distribution, so that the contrast with a maximum over commands does not
  hold.
tags:
- information-theory
- control-theory
- agency
date: '2026-11-22'
line:
- will-organization
- distributed-agency
grounds:
- THEORY-1344
- THEORY-2147
summary: >-
  A's, A8 §2D of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-22): empowerment, max over p(a) of I(A; S′), asks what a channel
  could transmit under a suitable action distribution; MIMI's I(X; (S, S′))
  measures information under the user's actual behaviour, so "a physics
  model may permit very precise positioning in principle, but require
  gestures that are awkward or difficult to reproduce". [NOTE-2236](../notes.d/NOTE-2236.md) records
  the contrast as influence without intuitiveness; this states its formal
  reason. The inequality is textbook. The wording is A's (ChatGPT, in the
  exchange of 2026-11-22); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2147 — Proposed; the First Contact reading -->

# CLAIM-tmpcfo3s: First Contact's score is information under the user's realized commands, empowerment the capacity of the same kind of channel maximized over commands; the score is at most the capacity, so an interface can offer high capacity, precise control in principle, through commands its user does not or cannot produce, and the score, unlike empowerment, registers that shortfall

## The contrast

Empowerment ([THEORY-1344](../theory.d/THEORY-1344.md)) is the channel capacity from an agent's next n
actions to its sensor n steps later: C = max over p(a) of I(A; S′). It is
a property of the channel. First Contact's score ([THEORY-2147](../theory.d/THEORY-2147.md)) is
I(x_t; (s_t, s_{t+Δ})) estimated from the commands the user actually
issues under the interface, a property of the channel *and* the user's
behaviour on it.

For a fixed command-to-state channel at a fixed horizon, its control term
I(x_t; s_{t+Δ} | s_t) under the user's distribution is at most the
capacity of that channel, by the definition of capacity as the maximum
over input distributions. The gap between them is the part of the
interface's capacity the user's behaviour does not use.

## What it adds

[NOTE-2236](../notes.d/NOTE-2236.md) records that the paper cites empowerment as an objective for
assistants that preserve a user's ability to reach states, and that MIMI
"differs in scoring intuitiveness as well as influence". The inequality
says where the intuitiveness enters: an interface can raise capacity, by
permitting fine positioning through precise gestures, while lowering the
score, if those gestures are ones the user does not reproduce. A design
that maximized empowerment would accept that trade; one that maximizes the
score would not. A8's synthesis, to optimize "usable, behaviorally
realized control" rather than movement range, is this contrast as a design
rule.

The capacity also bounds the score's ceiling for any user: a score near
capacity says the user's commands nearly exhaust what the interface can
carry.
