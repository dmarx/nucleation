---
status: Proposed
title: 'Liquid types'' refinements {ν : B | φ}, by analogy, show that adding a descriptor is refining, by a predicate, a type its entry already inhabits, and that the descriptors that can be found mechanically are conjunctions from a vocabulary fixed in advance'
version: 1
form: analogy
grounds:
- THEORY-tmp01mu6
rests_on:
- CLAIM-783
concludes:
- CLAIM-tmpnookt
uses:
- TERM-134
- TERM-tmp3mop8
tags:
- logic
- design-rationale
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
summary: >-
  The route by which the reading of Rondon, Kawaguchi and Jhala
  ([THEORY-tmp01mu6](../theory.d/THEORY-tmp01mu6.md)) bears on [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md)'s correspondence of a
  descriptor with a refinement the entry provably inhabits. It holds in the
  form the claim writes, {x : A | φ(x)} with φ a predicate, which Freeman
  and Pfenning's reading ([ARG-tmptph3p](ARG-tmptph3p.md)) could not show. Narrowed in three
  ways: a descriptor to be inferred must be a conjunction from a finite
  qualifier set; a descriptor given is checked only conservatively; and
  nothing is carried with the term. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp01mu6 CLAIM-tmpnookt CLAIM-783 TERM-134 ARG-tmptph3p TERM-tmp3mop8 — Proposed; the reading, the claims, the terms and the earlier argument this one joins -->

# ARG-tmprmcn5: Liquid types' refinements {ν : B | φ}, by analogy, show that adding a descriptor is refining, by a predicate, a type its entry already inhabits, and that the descriptors that can be found mechanically are conjunctions from a vocabulary fixed in advance

## The inference

Source domain, [THEORY-tmp01mu6](../theory.d/THEORY-tmp01mu6.md): {ν : B | e} is "the set of values c of the
base type B such that the predicate [c/ν]e evaluates to true" (p. 160);
every liquid type refines the term's ML type; inference finds, for each
unknown, "the strongest conjunction of qualifiers from Q⋆ that satisfies
all the constraints" (p. 160), starting from all of them and weakening;
the program never changes.

Target, [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md) with [CLAIM-783](../claims.d/CLAIM-783.md) and [TERM-134](../terms.d/TERM-134.md): a descriptor is a
predicate the entry passes when it is added; adding it narrows the
admissible set and moves nothing; descriptors never conflict, the entry
passing them all.

Mapping: ML type to the coarse specification; refinement predicate to
descriptor; conjunction to the intersection of admissible sets; the
inferred type to the strongest descriptor the vocabulary can state; the
qualifier set to the closed vocabulary of descriptors.

## Critical questions

- **Are the two alike in the respects the conclusion needs?** Yes, and
  more closely than Freeman and Pfenning's were ([ARG-tmptph3p](ARG-tmptph3p.md)). The
  refinement is a predicate on values of a type the term already has, the
  claim's own form; and inference ends at a conjunction every qualifier of
  which the term's values pass, by weakening the description, never the
  term. The unique strongest solution (p. 166) is the witness argument of
  [CLAIM-783](../claims.d/CLAIM-783.md): qualifiers each true of what flows to a point can be
  conjoined.
- **Are there differences that defeat it?** Three that narrow it. Where a
  type is inferred, φ must be a conjunction of qualifiers from a finite set
  given in advance, with no disjunction (pp. 160, 164): the record can hold
  any predicate the entry passes as a descriptor, but can find descriptors
  mechanically only from a vocabulary so fixed. Checking is conservative:
  "As the refinement predicates contain arbitrary terms, exact implication
  checking is undecidable" (p. 163), so a predicate the term passes can
  fail to check, and "provably inhabits" means provable by that check. And
  nothing is carried: derivations and solver checks are not kept, so the
  claim's proof-relevant reading ([TERM-tmp3mop8](../terms.d/TERM-tmp3mop8.md)) gets no support. One more:
  for a function's inputs the inferred type is relative to the program's
  calls, and with none it is the strongest the vocabulary states, of no
  witnessed value (p. 167); the record's descriptors are of versions that
  exist, so this costs the record nothing.
- **Is there a counter-analogy?** The algorithm passes through
  descriptions the term fails, every qualifier at the start, and discards
  them rather than moving the term. That is not a conflict among
  descriptors but the search for them, and it agrees with the claim.

## Verdict

Holds for the descriptor as a predicate refinement inhabited, narrowed as
above; does not support the proof-relevant reading. Proposed, as the
inference is the assistant's.
