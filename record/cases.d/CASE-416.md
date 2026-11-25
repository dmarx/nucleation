---
number: 416
status: Proposed
formerly:
- CASE-tmpr1f20
title: 'A classifier right on every item of its declared test family because it reads a watermark that, in that family, always accompanies the class: reliable correct output that fails when the cue and the class are separated'
version: 1
standing: fictional
kind: thought-experiment
tags:
- epistemology
- learning-theory
- causality
date: '2026-11-23'
line:
- learned-structure
bears_on:
- QUESTION-493
summary: >-
  The third of the set [LEAD-001](../leads.d/LEAD-001.md) asks for, and the one its title names:
  reliable performance without non-accidental competence. An image
  classifier labels horses correctly on every image of its declared test
  family, because every horse image there came from one archive that
  stamps a watermark, and the classifier reads the watermark. Remove the
  watermark, or stamp it on a cow, and the answers follow the stamp. The
  construction is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: TERM-079 — Proposed; cited as the criterion applied, not relied on -->
<!-- inactive-ok-file: CASE-399 CLAIM-1028 CLAIM-1086 CLAIM-1142 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-416: A classifier right on every item of its declared test family because it reads a watermark that, in that family, always accompanies the class: reliable correct output that fails when the cue and the class are separated

## The case

A classifier is trained and tested on images drawn from the same
collection. In that collection every horse photograph came from one
archive, which stamps a small watermark in a corner; no other photograph
carries it. On the declared test family, ten thousand held-out images
from the collection, the classifier labels horses with 100% accuracy.
Attribution shows its decision rests on the corner.

Two interventions separate the cue from the class:

- watermark removed from horse images: the classifier says "not horse";
- watermark pasted on a cow: it says "horse".

Held fixed: the classifier and the declared family. What varies is
whether the cue and what makes the label true are allowed to separate.
Documented analogues of this profile exist in the literature on shortcut
learning; none is registered or read here, so this case is fictional and
draws on none of them.

## What it separates

- **Reliable correct output without knowledge.** Over the declared family
  the outputs are correct and counterfactually stable under resampling.
  They do not depend on the horse.
- **Belief in the wrong content.** By [TERM-079](../terms.d/TERM-079.md)'s probes, what the
  classifier uses as its premise is the watermark: "stamped", not
  "horse". Its correct label is a true output carried by a belief about
  something else.

## Against the candidate answers

[QUESTION-493](../questions.d/QUESTION-493.md)'s candidate (A73) lists truth, counterfactual reliability
over a declared family, and grounding. The case meets the first two over
the family as declared and fails the third, and A73's second test,
intervention on spurious cues, is the one that shows it. So reliability
over a family drawn as the collection happens to be drawn does not
suffice. The two readings of what grounding then is, filed as
alternatives, part here:

- [CLAIM-1028](../claims.d/CLAIM-1028.md): grounding is a condition beyond reliability, which the
  interventions test;
- [CLAIM-1086](../claims.d/CLAIM-1086.md): grounding is reliability over a family closed under the
  interventions, so the classifier fails reliability once the family is
  declared right.

Both give the same verdict on this case: not knowledge. They differ in
what does the work.

## What it can show

That reliability over a declared family, as declared, can be had by a
cue that accompanies the truth there. Being fictional, nothing about how
common the profile is. [CASE-399](CASE-399.md) is the same failure with time in
place of a watermark. One of the separations [CLAIM-1142](../claims.d/CLAIM-1142.md) collects.
