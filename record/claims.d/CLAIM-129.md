---
number: 129
status: Proposed
formerly:
- CLAIM-tmp1xaiq
title: 'A factorization recovers only the structure visible in the relations it is fitted to, so a topic can survive a transformation that changes the communicative act, and a kind must be tested against probe families chosen for their bearing on the act'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-tmp3lv11: naturally occurring
    items added, so that the act is not only the item writers', and a
    margin. Topic-only factorization stays the comparator, since the
    claim is about factorizations of a relation family; the strong
    text-model rival is in CLAIM-tmp3wo5j. Version 1's condition read:
    "On held-out, correlation-breaking items of a design that crosses
    topic with act (CASE-040), a topic-only factorization of lexical
    co-occurrence recovers the act distinction as well as factorizations
    fitted to interpretive-judgement or uptake data do."
role: thesis
defeated_if: >-
  On held-out, correlation-breaking items of a design that crosses topic
  with act (CASE-040), and on naturally occurring items whose act is
  labelled by raters who did not write or select them, a topic-only
  factorization of lexical co-occurrence recovers the act distinction as
  well, within a margin fixed in advance, as factorizations fitted to
  interpretive-judgement or uptake data do.
tags:
- pragmatics
- representation-learning
- translation
date: '2026-10-10'
line: 'pragmatic-transport'
rests_on:
- CLAIM-004
- CLAIM-061
- CLAIM-142
grounds:
- CASE-040
complements:
- CLAIM-115
uses:
- TERM-014
summary: >-
  The assistant's, at A210 §5 after the owner's U58, and again at A214
  §3–§4. It recurs from U56 (A203 §37) to U60 (A218 H3), so it gets a
  code. It is [CLAIM-004](CLAIM-004.md)'s distinction between changing the frame and
  changing the act, in a factorization, and [TERM-014](../terms.d/TERM-014.md)'s relativity to a
  family of measurements, stated for factorizations. It does not say
  lexical structure is irrelevant to the act, or that a richer
  factorization cannot capture acts.
illustrated_by:
- CASE-040
objected_by:
- CLAIM-tmp3lv11
---
<!-- inactive-ok-file: CLAIM-tmp3wo5j — Proposed; the revised October thesis, cited in the history as where the strong text-model rival is placed -->
<!-- inactive-ok-file: CLAIM-004 CLAIM-061 CLAIM-142 — Proposed; open, and cited as the claims this one stands on, under test, not settled -->
<!-- inactive-ok-file: CLAIM-115 — Proposed; open, and cited as the thesis this claim complements -->

# CLAIM-129: A factorization recovers only the structure visible in the relations it is fitted to, so a topic can survive a transformation that changes the communicative act, and a kind must be tested against probe families chosen for their bearing on the act

## The claim

A topic model fitted to document–word co-occurrence recovers what a text
is about. It does not thereby recover what the text does. A210 §5: "A
document can remain about spending, romance, or morality while changing
from affectionate complicity to reprimand." So in a translated corpus the
outcome A210 calls "especially important" is possible: "Topic associations
appear stable while pragmatic or causal relationships change
substantially." It "would show that recovering thematic structure is not
the same as recovering communicative-act structure."

A214 §3 gives the reason in general form. "A two-topic model might capture
the first extremely well and ignore the second", where the first is topic
(spending against relationships) and the second is stance (affectionate
joking against moral condemnation). Low rank "does not tell us whether
those dimensions correspond to constitutive relations." The failure is
"treating *one recovered structure* as exhaustive of the object." Its
boxed statement: "Relational kinds are identified relative to a family of
interactions and probes. A factorization recovers structure visible
through that family, not automatically every relation constituting the
phenomenon."

The record holds both halves already, in other terms.

- That renderings can share a situation model and differ in footing and
  force is [CLAIM-061](CLAIM-061.md), and that a difference between translations can
  change the act and not only the frame is [CLAIM-004](CLAIM-004.md). A topic is a
  coarser thing to share than a situation model.
- That identity is relative to the family of probes is [TERM-014](../terms.d/TERM-014.md)'s
  "relative to a chosen family of measurements", and that agreement on a
  restricted family is not structural identity is [CLAIM-142](CLAIM-142.md).

What this claim adds is the consequence for method. A communicative kind
must be tested against probe families chosen for their bearing on the
act, not inferred from whichever matrix is to hand. A214 §4 names such
families: document × word, realization × interpreter, realization ×
pragmatic judgement, realization × possible response, realization ×
narrative event, intervention × judgement change. [CASE-040](../cases.d/CASE-040.md) is the
test. It crosses topic with act so that the two are not confounded, and it
scores each factorization on items that break their usual correlation.

The claim recurs across the stretch. A203 §37 lists it as the first thing
a strong result would show: "the model distinguishes shared subject matter
from shared communicative identity". A214 §8 builds the laboratory on it.
A218 makes it hypothesis H3: "Topic-preserving transformations will
sometimes reduce pragmatic or causal fidelity". It is a factorization-side
form of what [CLAIM-115](CLAIM-115.md) says survives translation, which is distinctions
a receiver can act on, not wording or proposition.

## Shared and private factors

A214 §4 proposes fitting the probe families jointly, with a shared and a
private part, X_j ≈ Z_shared H_j + Z_private,j B_j. "The shared component
is a *candidate* structural invariant." And: "An English utterance and a
French rendering will necessarily possess language-specific structure.
Fidelity should not require erasing it."

The proposal needs a caveat A214 does not give. The split between shared
and private parts is identified only under constraints, such as the
orthogonality of the shared and private subspaces in JIVE-type models.
Without them, components can be traded between the shared and private
terms. And with unconstrained real factors, a shared Z keeps the same
general-linear gauge, now acting on all views together ([CLAIM-148](CLAIM-148.md)).
Coupling the views does not remove it. So "candidate structural
invariant" means nothing until the constraint is stated.

## What it does not say

It does not say lexical structure is irrelevant to the act. It says that
lexical structure is not sufficient evidence of the act. It does not say
that a richer factorization, of task-indexed judgements or of uptake,
cannot capture acts. The claim concerns what one family of relations makes
visible. Nor does it say that a shared component found across probe
families is an invariant of the kind.
