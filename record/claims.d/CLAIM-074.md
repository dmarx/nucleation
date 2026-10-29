---
number: 74
status: Proposed
formerly:
- CLAIM-tmpk2ltq
title: 'Fidelity is relative to the interpreter''s learning history: what the current context supplies and what earlier experience has left in the interpreter are separate histories, told apart by what they carry and not by whether the change sits in activations or in weights, so fidelity under a fixed interpreter, across interpreters and across states of adaptation are different quantities'
version: 3
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Narrowed by the ninth status review to the correction its own body
    made: LIT-796's test-time update and LIT-801's inner weights
    change parameters and discard them, so the two histories are told
    apart by what they carry (A44's 'contextual' and 'adaptational'
    history), not by transience. The old title: Fidelity is relative
    to the interpreter's learning history: a frame given in context is
    transient while an adaptation to it persists, so fidelity under a
    fixed interpreter, across interpreters and across states of
    adaptation are different quantities. CLAIM-244 and CLAIM-258 no
    longer rest on it.
- version: 3
  date: '2026-10-29'
  note: >-
    Tenth status review (ADR-057). The body said the claim 'needs
    stating in terms of where the change happens', which contradicts
    the title; it now says what the change carries. The blocker note
    is updated: CLAIM-118 is restated the same way and is held only by
    the owner's ruling on test-time training. The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  Measured fidelity of the same rendering is the same for interpreters
  with different exposure to the source genre, so that adaptation
  history makes no difference to it.
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
rests_on:
- CLAIM-118
summary: >-
  A44 §4 and A48 §5.5, recovered. Kept to outline v4 (§9.5); absent from
  the manuscript, which keeps the context/interpreter split but not its
  consequence for fidelity. Apparently dropped by inadvertence.
supports:
- CLAIM-049
---
<!-- inactive-ok-file: CLAIM-118 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-074: Fidelity is relative to the interpreter's learning history: what the current context supplies and what earlier experience has left in the interpreter are separate histories, told apart by what they carry and not by whether the change sits in activations or in weights, so fidelity under a fixed interpreter, across interpreters and across states of adaptation are different quantities

## The claim

A44 §4: "A change in frame can be transient, while an adaptation to a frame can
potentially persist across new contexts." Two histories: "**Contextual
history:** What evidence is currently available to the interpreter?
**Adaptational history:** How have previous experiences altered the
interpreter's response function?" The example: "Repeated exposure to underworld
slang ... doesn't merely alter the immediate context. It may also change the
reader's longer-term ability to recognize the social positions performed through
that vocabulary. We therefore have a new problem of translation fidelity across
interpreters with different learning histories." A48 §5.5: "Distinguish:
Fidelity under a fixed interpreter. Fidelity across different interpreters.
Fidelity across different states of adaptation of the same interpreter."

## Where it went

A52 §9.5 kept "learning histories and audience correspondence". The manuscript
keeps audience knowledge K as side information (§5) and the signal/interpreter
distinction ([CLAIM-118](CLAIM-118.md)). It does not say that fidelity itself differs with the
interpreter's history. The opacity question ([QUESTION-023](../questions.d/QUESTION-023.md)) is one case of it.
Experiment 3 of [CASE-005](../cases.d/CASE-005.md) would test it.

## What the in-context-learning readings say

Persistence and the locus of change come apart. Akyürek et al.'s
test-time update ([LIT-796](../literature.d/LIT-796.md)) and Sun et al.'s inner weights
([LIT-801](../literature.d/LIT-801.md)) both change parameters, and both discard the change after
the task or the sequence. So "transient means context, persistent means
adaptation" does not hold as a dichotomy, and the claim needs stating in terms of what the change carries, not of where it sits. The
title now says so (2026-10-29). A parameter change computed from the
current task and discarded after it is part of the contextual history.

## Note of 2026-10-29: what holds it back

Its one premise, CLAIM-118, is Proposed. CLAIM-118 is now stated the same
way as this claim, by what each history carries, and is held only by the
owner's ruling that test-time training whose update is discarded is part of
the signal, against manuscript §5.
