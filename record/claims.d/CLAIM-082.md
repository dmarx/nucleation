---
number: 82
status: Proposed
formerly:
- CLAIM-tmpnt2nd
title: 'A sign''s communicative significance is fixed by its contrasts within a system rather than by correspondence to a referent'
version: 1
role: thesis
defeated_if: >-
  A reading of Saussure or of the structuralist tradition that shows
  value to be fixed by reference, or a case where a term's communicative
  role is unchanged when its contrasts with coexisting terms are
  changed.
tags:
- linguistics
- philosophy-of-language
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- THEORY-159
- LIT-775
- THEORY-175
summary: >-
  The manuscript's structuralist premise (§2), citing Saussure and Lévi-
  Strauss. [CLAIM-072](CLAIM-072.md) corrects how it states Saussure.
objected_by:
- CLAIM-072
supports:
- CLAIM-115
- CLAIM-036
illustrated_by:
- CASE-019
---
<!-- inactive-ok-file: THEORY-175 — Proposed; cited as a reading that qualifies this claim, not as settled -->

# CLAIM-082: A sign's communicative significance is fixed by its contrasts within a system rather than by correspondence to a referent

## The claim

§2: "Saussure's account of linguistic value makes the significance of a sign
depend upon contrasts within a system, rather than on intrinsic correspondence
to a referent." Lévi-Strauss is cited for extending relational and
transformational analysis to myth. The manuscript uses the premise to motivate
relational identity, with the proviso that not every transformation is a
symmetry.

## What it does not say

It is a motivating premise, not a result the manuscript relies on formally.
Lévi-Strauss is unread here ([LIT-775](../literature.d/LIT-775.md)), so his part of it rests on a work cited
without a reading.

## A qualification from experiment

Bergen, Goodman and Levy ([LIT-809](../literature.d/LIT-809.md)), Experiment 1: a novel symbol's
interpretation is fixed by its contrast with the alternative the speaker
could have used. But the contrast works only because one alternative is
tied to an object by resemblance. Read against this claim, it is contrast
together with reference, not contrast instead of it.

## A qualification from machine representations

Moschella and colleagues' relative representations ([LIT-849](../literature.d/LIT-849.md), read in
[NOTE-652](../notes.d/NOTE-652.md)) are a working case of the premise in one respect. Each input is
represented only by its cosine similarities to a set of anchor inputs from
the same system, and a decoder trained on those similarities transfers,
untrained, between independently trained encoders ([THEORY-175](../theory.d/THEORY-175.md)). Identity by
relations within a system is enough to carry a decoder across systems that
share no coordinates.

The reading adds two qualifications, and both point the same way as the one
from experiment above.

- **Across systems, contrast needs a correspondence.** Between languages or
  modalities, the anchors must be matched from outside: translated reviews,
  sentences aligned in WikiMatrix. Within one system relations suffice; for
  transport between systems they work only once something ties the anchor
  in one to the anchor in the other. That is contrast together with
  correspondence, as in Bergen, Goodman and Levy.
- **The relational encoding is lossy and approximate.** Independently
  trained encoders agree in their relative vectors only approximately: the
  vectors correlate highly, but most nearest neighbours differ. Where a
  shared absolute space already exists (a multilingual encoder), the
  relational encoding transfers worse than the absolute one in every
  language pair tested.

The analogy has a limit of its own. A cosine to an anchor is a metric
relation in a vector space, invariant only to cosine-preserving maps. Saussure's
value is opposition among coexisting terms, and [THEORY-159](../theory.d/THEORY-159.md) does not make it
a similarity. The case shows that relational identity can be engineered and
carried between systems. It does not show that this is Saussure's value.
