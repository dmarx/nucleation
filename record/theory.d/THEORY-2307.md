---
number: 2307
status: Proposed
formerly:
- THEORY-tmp62cvo
promote_when: >-
  A published proof, by the author or by others, that the theory as this
  book presents it, with its one universe, is consistent, given by a model
  in which its judgements hold as the meaning explanations say: a set's
  elements are programs that compute its canonical elements, and an element
  of the set of a ∈ A such that B(a) is a pair of such an a with a proof
  of B(a). A proof of consistency alone, by a model that does not interpret
  elements as programs, does not meet this.
title: 'Martin-Löf holds that what is asserted is a judgement, not a proposition, in four forms (A is a set, two sets are equal, a is an element of A, two elements are equal), each explained before any rule: a set is defined by how its canonical elements are formed, an element is a program computing one, and propositions are identified with sets, so that being an element reads alike as proving a proposition, solving a problem and meeting a specification; the existential, and the set of elements such that a property holds, have as elements pairs of a witness and its proof; and universes are sets of codes closed under given set-forming operations, never a set of all sets'
version: 1
tags:
- logic
- philosophy-of-mathematics
date: '2026-11-25'
source:
- LIT-3232
corroborates:
- CLAIM-949
summary: >-
  Martin-Löf (1984), [LIT-3232](../literature.d/LIT-3232.md), read in [NOTE-2419](../notes.d/NOTE-2419.md) for [LEAD-215](../leads.d/LEAD-215.md)
  from a course-hosted scan, Skimmed. The source of the propositions-as-sets
  reading and of the table that reads an element as a program "which meets
  the specification A" (p. 6). It corroborates [CLAIM-949](../claims.d/CLAIM-949.md)'s correspondences
  of a question with a problem, a realization with an inhabitant carried
  with its evidence, and a descriptor with a refinement inhabited
  ([ARG-249](../arguments.d/ARG-249.md), [ARG-253](../arguments.d/ARG-253.md)); it narrows the claim that a question's
  revision is a change of type handled by universes ([ARG-255](../arguments.d/ARG-255.md)). It does
  not bear on the direction of fit as inference against checking.
  Proposed until a model shows the meaning explanations consistent.
---
<!-- inactive-ok-file: ARG-249 ARG-253 ARG-255 CLAIM-1208 CLAIM-1289 CLAIM-949 CLAIM-783 TERM-152 TERM-153 TERM-154 NOTE-2419 — Proposed or Skimmed; the reading, the arguments and claims filed from it, and the entries it bears on -->

# THEORY-2307: Martin-Löf holds that what is asserted is a judgement, not a proposition, in four forms (A is a set, two sets are equal, a is an element of A, two elements are equal), each explained before any rule: a set is defined by how its canonical elements are formed, an element is a program computing one, and propositions are identified with sets, so that being an element reads alike as proving a proposition, solving a problem and meeting a specification; the existential, and the set of elements such that a property holds, have as elements pairs of a witness and its proof; and universes are sets of codes closed under given set-forming operations, never a set of all sets

## Source

Martin-Löf (1984), [LIT-3232](../literature.d/LIT-3232.md), notes by Giovanni Sambin of the Padua
lectures of June 1980; read in [NOTE-2419](../notes.d/NOTE-2419.md) from a scan of the typescript
(pp. i–54, 64, 69–70 and 87–91 closely, pp. 55–86 skimmed).

## The account

Holding a proposition true is a judgement; propositions are what judgements
are about (p. 3). There are four forms, "A set", "A = B", "a ∈ A" and
"a = b ∈ A", each presupposing what comes before it (p. 5). A rule is
justified "by explaining the conclusion on the assumption that the
premisses are known" (p. 4), so the meaning of each form comes first. "a
set A is defined by prescribing how a canonical element of A is formed as
well as how two equal canonical elements of A are formed" (p. 8), and "an
element a of a set A is a method (or program) which, when executed, yields
a canonical element of A as result" (p. 9). Because "a proposition is
defined by laying down what counts as a proof of the proposition" (p. 11),
the two notions are identified: "the formulae-as-types
(propositions-as-sets) interpretation on which intuitionistic type theory
is based" (p. 13). So a ∈ A has four readings: an element of a set, a
proof of a proposition, a method of fulfilling an intention (Heyting), a
method of solving a problem (Kolmogorov), and the last "can be read as 'a
is a program ...' ... which meets the specification A" (pp. 5–6).

Each set-forming operation has formation, introduction, elimination and
equality rules (p. 24). The disjoint union (Σx ∈ A)B(x) is at once the
existential, whose canonical proof "is a pair (a,b), where b is a proof of
the fact that a satisfies B" (p. 42), and the set of a ∈ A such that B(a),
whose elements "are pairs (a,b) with b ∈ B(a)", carrying "the witnessing
information" (p. 53). The witness is recovered from the proof by
projection, which is why the axiom of choice is provable (pp. 45, 50–52).
Writing "A true" suppresses the proof, and cannot be done where what
follows depends on it (pp. 33, 47).

A category, such as the category of sets, is grasped without rules that
form all its objects, and is not a set (pp. 21–22). There is no set of all
sets, "because we are not able to exhibit once and for all all possible
set forming operations"; a universe is "the least set closed under certain
specified set forming operations" (p. 87), of codes for sets (p. 88), can
be followed by a second and a third (p. 89), and does not contain itself,
by Girard's paradox (p. 90).

## What it does not show

That the rules are consistent in any metamathematical sense: consistency is
argued from the meaning of the rules (pp. 69–70). That type checking is
decidable: with this identity type it is not, and the book does not say
so. Anything about inferring types from terms against checking terms
against types: the book gives rules, not an algorithm. That a specification
given by tests on candidates is a set: its sets are given by how their
elements are formed, and the nearest form to a test is the "such that"
set over a base set already given (p. 53).

## Bearing

It corroborates [CLAIM-949](../claims.d/CLAIM-949.md) in three correspondences: a question as a
problem, a realization as an inhabitant carried with the evidence that it
passes, and a descriptor as a refinement the entry inhabits, here with the
evidence carried, which none of the refinement systems read under
[LEAD-215](../leads.d/LEAD-215.md) does ([ARG-249](../arguments.d/ARG-249.md), [ARG-253](../arguments.d/ARG-253.md)). It narrows the fourth, a
question's revision as a change of type handled by universes, to the
revisions a universe already codes ([ARG-255](../arguments.d/ARG-255.md)). It qualifies [TERM-152](../terms.d/TERM-152.md)
([CLAIM-1289](../claims.d/CLAIM-1289.md)) and gives [CLAIM-949](../claims.d/CLAIM-949.md)'s defeater (a) a test
([CLAIM-1208](../claims.d/CLAIM-1208.md)). It sharpens [TERM-153](../terms.d/TERM-153.md) and [TERM-154](../terms.d/TERM-154.md), and parallels
[CLAIM-783](../claims.d/CLAIM-783.md)'s witness argument with the certificate carried.
