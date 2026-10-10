---
number: 39
status: Active
formerly:
- TERM-tmp6ohuk
title: 'measurement context, as the elicitation protocol that enters the response and not the situation'
version: 1
tags:
- causality
- psychometrics
date: '2026-10-10'
line: pragmatic-transport
summary: >-
  The third of the three roles that "frame" was split into at A125 §1,
  after the communicative situation ([TERM-030](TERM-030.md)) and the framing
  intervention ([TERM-018](TERM-018.md)): the conditions under which a judgement is
  elicited. In A129 §1's model it enters the judgement, not the
  interpreter's state. It appears five times, so it gets a code. Its
  name collides with [TERM-031](TERM-031.md)'s.
used_by:
- CLAIM-127
---
<!-- inactive-ok-file: CLAIM-127 — Proposed; open, and cited as open: the claim is under test, not settled -->

# TERM-039: measurement context, as the elicitation protocol that enters the response and not the situation

## Definition

The conditions under which a judgement is elicited: which question is put to
the interpreter, in what form and in what order. A125 §1 named it beside the
situation and the intervention, as C ∈ ℳ: "*'The speaker is a friend'* can
describe a communicative situation, while telling a reader that the speaker
is a friend is an intervention. Asking the reader to rate friendliness
introduces a measurement context."

A129 §1 gave it a place in a structural model. It introduced "an
interpreter state R, a measurement protocol C, and a judgment Y", with

- R′ = f_R(R, Z, I, ε_R), and
- Y = f_Y(R′, Z, C, ε_Y).

Here Z is the communicative situation and I the framing information. C
enters the equation for the judgement and not the update of the
interpreter's state. In A129 §5's system it indexes the cover ℳ, and the
empirical law in context C under intervention a is e_C^a = P(Y_C | do(a))
([CLAIM-127](../claims.d/CLAIM-127.md)).

A151 §3 restates the three-way split: "A speaker actually being a friend, a
reader being told the speaker is a friend, and a reader being asked whether
the speaker sounds friendly are not equivalent manipulations."
A203 §15 and A218 Ch10.1 restate it again.

## What it is not

- **Not [TERM-031](TERM-031.md),** despite [TERM-031](TERM-031.md)'s title. [TERM-031](TERM-031.md) is A24's situation
  tuple C = (u, s, a, k, g), an index on judgement distributions, and
  [TERM-030](TERM-030.md) superseded it. A125's table misread [TERM-031](TERM-031.md) as "The conditions
  under which particular observations or judgments are obtained", which is
  this sense.
- **Not [TERM-030](TERM-030.md),** the configuration of the situation itself.
- **Not, or not obviously, a framing intervention ([TERM-018](TERM-018.md)).** Whether
  eliciting a judgement is also an intervention is open, and the exchange
  answers it both ways. A35 §6, quoted in [TERM-018](TERM-018.md): "forcing a participant
  to make an explicit judgment is itself an intervention." A39 §3.2: "Asking
  a reader to consider an utterance as affectionate is another
  intervention." A125 §1 goes the other way, and A129's graph gives C an
  arrow into Y only, never into f_R.

The answer decides where signalling in elicited data would come from:
from C's direct influence on Y, or from a change of state carried forward
to the next judgement ([CLAIM-127](../claims.d/CLAIM-127.md), "Two routes to signalling"). Sequential
designs, where one judgement is elicited before another, separate the two
readings. Under the first, an earlier question cannot change a later
judgement, because it never reaches the interpreter's state. Under the
second it can, because it changes the state the later judgement is drawn
from.
