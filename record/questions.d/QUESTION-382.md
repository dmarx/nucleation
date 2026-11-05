---
number: 382
status: Open
formerly:
- QUESTION-tmpe05jc
title: 'At what interface, and under which interactions, is a system individuated as one component rather than another, when black-boxing erases internal distinctions that composition preserves and creates relations the parts lacked, and when does equivalence at an interface fail once implementation cost, maintenance or internal control is counted?'
version: 1
tags:
- individuation
- mathematics
- complex-systems
date: '2026-11-05'
line:
- realizability
refines:
- QUESTION-393
summary: >-
  A's question, from the owner's paste of 2026-11-05 (fourth), A's "Toward a
  resource-sensitive Yoneda theory of individuation" §8, with the third
  target result of §11 and two separations of §9: "At what interface, and
  under which interactions, is a system individuated as one component
  rather than another?" A keeps two operations apart, black-boxing,
  "mechanism → external behavior", and composition, "components →
  assembled mechanism", and warns that "black-box equivalence alone is not
  evidence of dynamical individuality or autonomy". The record holds the
  theorem ([THEORY-1063](../theory.d/THEORY-1063.md): black-boxing is a functor, not faithful), the
  effective constraint composition creates ([CLAIM-480](../claims.d/CLAIM-480.md)) and two questions on
  what coupling generates and what vocabulary it needs ([QUESTION-390](QUESTION-390.md),
  [QUESTION-283](QUESTION-283.md)); neither asks which interface individuates a component,
  or when interface equivalence fails under cost or maintenance. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-202 CLAIM-566 TERM-088 TERM-111 TERM-116 — Proposed; A's proposals of 2026-11-04 and 2026-11-05 and the entries filed beside them, and the record's open term for the senses of individuation, cited as filed, nothing here resting on their being settled -->

# QUESTION-382: At what interface, and under which interactions, is a system individuated as one component rather than another, when black-boxing erases internal distinctions that composition preserves and creates relations the parts lacked, and when does equivalence at an interface fail once implementation cost, maintenance or internal control is counted?

## Why it is a question

A (§8): "A circuit may have a complicated internal construction, but an
external observer sees only its admissible terminal currents and
potentials. Black-boxing preserves composition: BB(M_2∘M_1) =
BB(M_2)∘BB(M_1). Yet the black-box functor is not faithful. Different
internal mechanisms can have identical external behavior." For origami:
"Imagine two origami mechanisms with identical external motion at their
attachment points but different internal crease patterns. They might be
interchangeable as components in a larger mechanical assembly. But they
could differ in their folding histories, internal stresses, failure
modes, and requirements for maintenance."

The two operations, as A separates them: "Black-boxing can erase internal
distinctions. Composition can create effective relationships that weren't
present at the component level. Their interaction may supply a
mathematical account of how some organizations become identifiable as
higher-level units." And: "This isn't merely a question about how we
observe an independently existing object. The interface can participate
causally in forming the effective constraint structure of the assembled
system." The guard: "black-box equivalence alone is not evidence of
dynamical individuality or autonomy. Two interchangeable mechanisms may
differ radically in their persistence and maintenance properties."

**What the record holds.** [THEORY-1063](../theory.d/THEORY-1063.md) (Baez and Fong): black-boxing a
passive linear circuit is a functor whose composite behaviour is fixed by
the parts' black boxes, so circuits with the same behaviour "are
interchangeable in every composite", and it is not faithful. [CLAIM-480](../claims.d/CLAIM-480.md):
eliminating an equilibrated interior leaves a boundary coupling neither
part has, and "The interior has effectively become apparatus."
[QUESTION-390](QUESTION-390.md) asks which constraint structures joining origami modules
generates and whether the boundary relation stays in the modules'
vocabulary; [QUESTION-283](QUESTION-283.md) asks when composition forces a richer
vocabulary. Those ask what an interface carries. This asks which
interface, and which interactions at it, make a system one component, and
what an interface equivalence leaves out.

**What interface equivalence leaves out.** Three of A's cases, each a
separation:

- **Maintenance or internal control** (§11, third target result): "identify
  a compositional equivalence at an external interface that fails when
  maintenance or internal control is included." [TERM-116](../terms.d/TERM-116.md)'s maintenance
  profile, and [CLAIM-566](../claims.d/CLAIM-566.md)'s separation of persisting from
  regenerating, are where the failure would show.
- **Cost** (§9): "can two systems possess the same compositional external
  behavior but require asymptotically different computational resources
  to realize it? Yes, at least as a broad possibility: the interface
  semantics alone need not preserve implementation costs." This is the
  interface form of [TERM-111](../terms.d/TERM-111.md)'s separation of senses of universality.
- **Autonomy** (§9): "Can two systems have equivalent resource-bounded
  processes but different organizational autonomy? Also plausibly yes:
  one may depend on external maintenance while the other helps reproduce
  its enabling constraints."

A small instance of the first kind, the filer's: a 2 Ω resistor and two
1 Ω resistors in series have one black box in [THEORY-1063](../theory.d/THEORY-1063.md)'s sense, so
they are interchangeable in every composite, and the second has two parts
that can fail, so its failure modes and maintenance differ.

## What would answer it

For a stated class of composable mechanisms with a declared interface
semantics: a criterion saying which interface, and which interactions,
fix a component's identity in the descriptive sense of [TERM-088](../terms.d/TERM-088.md), with
examples where a coarser interface merges and a finer one separates; and,
for each of A's three separations, either an example of interface
equivalence that fails under the added count (cost, maintenance, or
autonomy) with the failure measured, or a condition under which it
cannot fail. [CASE-202](../cases.d/CASE-202.md)'s study is a design that could supply the
maintenance example.

## What would not answer it

- **Black-box equality alone.** It is the premise, not the answer; A: it
  "is not evidence of dynamical individuality or autonomy".
- **Interfaces chosen after the comparison.** [CLAIM-322](../claims.d/CLAIM-322.md): probes chosen to
  produce a classification show only that they can be selected.
- **A verdict that interface individuation constitutes the component.**
  Whether it does is [QUESTION-284](QUESTION-284.md)'s question.
