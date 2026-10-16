---
status: Active
title: "In Kolmogorovian probability, joint distributedness is transitive, so representing a measurement by one random variable in every context it occurs in already puts all measurements of a connected system on one probability space; within that representation a Kochen–Specker or Bell contradiction refutes the context-independent identification of measurements, not the existence of a joint distribution"
version: 1
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-16'
source:
- LIT-836
answers:
- QUESTION-067
summary: >-
  Dzhafarov & Kujala (2017), [LIT-836](../literature.d/LIT-836.md), read in full in [NOTE-623](../notes.d/NOTE-623.md). The
  transitivity step is an elementary proof; the reading of the reductio
  is an argument that rests on it. It binds the random-variable
  representation only: the sheaf account keeps one variable per
  measurement and asks whether marginals glue, and a reader who holds
  that view is not bound by it. The paper also proves that a coupling of
  a binary connection is multimaximal iff adjacent pairs, ordered by
  their means, are maximally coupled (Theorem II.3).
---

<!-- inactive-ok-file: THEORY-013 THEORY-168 — Proposed; named for the Contextuality-by-Default accounts this one sits beside, nothing here rests on them -->

# THEORY-tmpjwpuk: In Kolmogorovian probability, joint distributedness is transitive, so representing a measurement by one random variable in every context it occurs in already puts all measurements of a connected system on one probability space; within that representation a Kochen–Specker or Bell contradiction refutes the context-independent identification of measurements, not the existence of a joint distribution

## Source

Dzhafarov & Kujala (2017), "Probabilistic Foundations of Contextuality",
*Fortschritte der Physik*, arXiv 1604.08412v4, [LIT-836](../literature.d/LIT-836.md), read in full in
[NOTE-623](../notes.d/NOTE-623.md). The Kochen–Specker incidence matrices of Fig. 1 were not
checked.

## What was actually shown

**Transitivity (§I.3).** A random variable is a triple of domain
probability space, codomain and measurable function, and two random
variables are jointly distributed iff their domain spaces coincide (Eq.
7). If X, X′ are jointly distributed and so are X′, X″, then X, X″ are,
since all three share X′'s domain. So if the graph of contexts linked by
shared variables has a path through every context, the traditional
system has an overall joint distribution. The paper exhibits such paths
for KCBS, KS-4D and KS-3D.

**The reductio (§I.4).** A contextuality contradiction shows that no
joint distribution of the measurements has the observed context
marginals. In the traditional representation such a joint distribution
exists by transitivity. So what fails is the premise that made the
contexts overlap: that a measurement of q is one random variable
whatever else is measured with it ("Noncontextual Identification").

**What follows (§II).** Index each variable by content and context.
Contextuality is then whether some coupling of the now-disjoint
contexts makes each content's copies satisfy a property C. For binary
systems C is multimaximality, and Theorem II.3 shows that a coupling of
one content's copies is multimaximal iff each adjacent pair, ordered by
Pr[R = 1], is maximally coupled.

What could have come out otherwise: joint distributedness could have
failed to propagate along chains of contexts. It is forced by the
definition of a random variable.

## What this does not say

- **That the sheaf account is mistaken.** Abramsky & Brandenburger
  ([THEORY-012](THEORY-012.md)) keep one variable per measurement and ask whether context
  marginals glue to a global section; that is a statement about a
  presheaf over a cover, not about random variables on one space. The
  argument targets the random-variable reading and does not engage the
  sheaf formulation ([NOTE-623](../notes.d/NOTE-623.md), Limitations). Under consistent
  connectedness the two accounts agree ([NOTE-600](../notes.d/NOTE-600.md)).
- **That contextuality is an artefact.** Under Contextuality-by-Default
  consistently connected Kochen–Specker and Bell systems are still
  contextual; the account moves the refuted assumption, not the
  phenomenon.
- **That inconsistent connectedness is universal outside physics.** Cited,
  not shown here (C6, weak).
- **That the §II.4 properties are proved.** Heredity, reduction to the
  traditional notion and agreement on cyclic systems are asserted as
  trivial.

## Connections

- [QUESTION-067](../questions.d/QUESTION-067.md) asks which noncontextuality assumption a test of pragmatic
  judgements would refute. This account answers part of it for the
  random-variable reading: what fails is the identification of a
  judgement with one variable regardless of what it is made with. It
  says nothing about Spekkens's preparation notion, which the question
  also names.
- [THEORY-168](THEORY-168.md) (in Contextuality-by-Default the verdict depends on the
  couplings imposed) uses the multimaximality that Theorem II.3
  characterises; [CLAIM-069](../claims.d/CLAIM-069.md) cites this paper for it.
- [THEORY-013](THEORY-013.md) (behavioural data show no contextuality once marginals are
  separated) rests on the same programme.
