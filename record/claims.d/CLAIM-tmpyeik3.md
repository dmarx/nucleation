---
status: Proposed
title: 'Blackwell''s order compares experiments about one parameter, so it does not reach the normal translation case: source and target readers decide about situations with changed coordinates, and where the state is common a translator with context knowledge yields a rendering that is not a garbling of the source, which the order typically leaves incomparable with it and about which the direction the manuscript uses is silent'
version: 1
role: counter
tags:
- mathematical-statistics
- information-theory
- translation
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-091
- CLAIM-074
grounds:
- THEORY-156
- LIT-781
objects_to:
- CLAIM-050
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal and
  structure lenses); no turn of the exchange states it. [CLAIM-050](CLAIM-050.md)'s
  comparison is over one state Z. Compensation ([CLAIM-091](CLAIM-091.md)) changes the
  social coordinates, so the target reader decides about a different
  situation. Where the situation is common, a translator who knows the
  context makes a rendering that depends on Z other than through the
  source, so it is not a garbling. Blackwell's order is still defined
  then, but typically leaves source and target incomparable, and the
  direction the manuscript uses says nothing. It does not say
  decision-relative fidelity is wrong.
---
<!-- inactive-ok-file: CLAIM-050 — Proposed; open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: CLAIM-091 CLAIM-074 CLAIM-034 — Proposed; the compensation, interpreter and adaptive-translation claims this objection rests on or cites, open -->
<!-- inactive-ok-file: CLAIM-115 CLAIM-139 CLAIM-125 CLAIM-128 — Proposed; the theses that rest on CLAIM-050, the open problem beside this one and the profile claim, cited as open -->
<!-- inactive-ok-file: THEORY-156 THEORY-161 — Proposed; cited as the readings of Blackwell and of the decision bound, not as settled -->
<!-- inactive-ok-file: LIT-778 — Deferred; Torgersen, unread here, named as where the quantitative question lies and not leaned on -->

# CLAIM-tmpyeik3: Blackwell's order compares experiments about one parameter, so it does not reach the normal translation case: source and target readers decide about situations with changed coordinates, and where the state is common a translator with context knowledge yields a rendering that is not a garbling of the source, which the order typically leaves incomparable with it and about which the direction the manuscript uses is silent

## The objection

[CLAIM-050](CLAIM-050.md) states the comparison over one state variable: "If P(V₂|Z) =
G P(V₁|Z) for a source-independent garbling G, then V₁ is at least as good
as V₂ for every bounded decision problem over Z". Blackwell's experiments
share their parameter. [THEORY-156](../theory.d/THEORY-156.md): "An experiment is an n-tuple of
probability measures on a common space, one per state", and α is
sufficient for β "if there is a stochastic transformation T with T m_i =
M_i for every state i". The outcome spaces of the two experiments may
differ. The states i must be the same on both sides.

Two features of the translations the line cares about break the comparison
as [CLAIM-050](CLAIM-050.md) states it.

**The situation changes.** [CLAIM-091](CLAIM-091.md) writes translation as
(u, s, a, k, g) → (u′, s, a, k′, g′), achieving pragmatic equivalence "by
compensating for changes in the social coordinates of an utterance through
changes in its linguistic coordinates". The source reader decides about a
situation with coordinates (k, g). The target reader decides about one with
(k′, g′). To compare their experiments one must say which target situation
corresponds to which source situation, and index both by one parameter.
That correspondence is one more that nothing fixes ([QUESTION-005](../questions.d/QUESTION-005.md)). The
readers differ as well: [CLAIM-074](CLAIM-074.md) makes fidelity relative to the
interpreter's learning history.

**Where the situation is common, the rendering is not a garbling.** A
garbling needs the rendering to depend on Z only through the source text,
V ⫫ Z | U. A translator who knows the context breaks that. So does
compensation, which uses what the translator knows about the target
audience. So does the deliberately adaptive translation of [CLAIM-034](CLAIM-034.md), "one-way
simulation where target audiences can reproduce the source utterance's
relevant communicative possibilities". Outside garblings, Blackwell's order
is still defined. But it typically leaves source and target incomparable,
and the direction the manuscript uses ([CLAIM-050](CLAIM-050.md): "garbling implies no
worse") says nothing about them.

A worked case. Let Z be uniform on three situations, 1, 2 and 3.

- The source text tells its reader only whether Z = 1: U = 1 if Z = 1, and
  U = 0 otherwise.
- A translator who knows the setting tells the target reader only whether
  Z = 3: V = 1 if Z = 3, and V = 0 otherwise.

V is not a garbling of U, because given U = 0 it still varies with Z. And
neither experiment is at least as informative as the other. Take the
problem "say whether Z = 3", with loss 1 for a wrong answer. From V the risk
is 0. From U it is 1/3: on U = 1 the answer is certainly no, and on U = 0,
which has probability 2/3, the two remaining situations are equally likely,
so any answer is wrong half the time. For "say whether Z = 1" the risks are
reversed. If either experiment dominated the other, it would do at least as
well in every problem under every prior. So U and V are incomparable in
Blackwell's order. How far apart they are is a question for Le Cam's
deficiency, which [THEORY-156](../theory.d/THEORY-156.md) names and the record has not read
(Torgersen, [LIT-778](../literature.d/LIT-778.md)).

So [CLAIM-050](CLAIM-050.md)'s precision covers garbling transports about an unchanged
situation: a lossy retelling of one story, read by the same kind of
reader. That is not the case the line cares about most. [CLAIM-115](CLAIM-115.md) and
[CLAIM-139](CLAIM-139.md) both rest on [CLAIM-050](CLAIM-050.md) for what makes a distinction
decision-relevant.

**What the record already holds nearby.** [QUESTION-016](../questions.d/QUESTION-016.md) holds the chain
version open: "A garbling of a garbling is a garbling, so sufficiency for Q
can only decline along a pure chain. The open part is the case the
manuscript flags, interpreters with side information". [CLAIM-125](CLAIM-125.md)'s first
part asks for an informativeness order "taken across a change of cover".
Neither says that [CLAIM-050](CLAIM-050.md)'s comparison needs a common parameter, or that
the line's own central cases lack one.

## What it does not say

- It does not say decision-relative fidelity is wrong. [CLAIM-050](CLAIM-050.md)'s first
  half stands. For a common situation, its prior art gives a bound that
  needs no garbling: with total variation, the posterior distortion bounds
  the extra Bayes risk of every bounded-loss decision (Zhao et al., as
  [CLAIM-050](CLAIM-050.md) cites them, [THEORY-161](../theory.d/THEORY-161.md)).
- It does not say Blackwell's order is undefined outside garblings. It is
  defined for any two experiments on one parameter. What applies only to
  garblings is the direction the manuscript uses.
- It does not say compensation makes a translation worse. The worked case
  shows a rendering that is better for one decision and worse for another,
  which is what [CLAIM-128](CLAIM-128.md) expects of fidelity profiles.

## What would answer it

Either of two things.

- A comparison of experiments across a change of parameter, through a
  stated correspondence of situations z ↦ z′ with its own anchoring
  ([QUESTION-005](../questions.d/QUESTION-005.md)), and results for that comparison.
- A restriction of [CLAIM-050](CLAIM-050.md) to decisions about a situation the translation
  does not change, with the side-information case ([QUESTION-016](../questions.d/QUESTION-016.md)) handled by
  a quantitative measure such as deficiency rather than by the order.
