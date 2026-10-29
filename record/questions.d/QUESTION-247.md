---
number: 247
status: Answered
formerly:
- QUESTION-tmpd1e8g
title: 'If the communicative object is a presheaf of propositions over a category of contexts, is the negation its topos logic gives an orthocomplement or a Heyting pseudo-complement, and what fixes it?'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    CLAIM-038 went Active at the fourteenth status review (ADR-057), at
    the status review's ruling (the owner delegated these rulings), so
    the condition this answer is given under is now held. The answer
    read: "It is conditional: CLAIM-038, which makes the communicative
    object a presheaf over contexts, is Proposed." Whether the object is
    such a presheaf is now QUESTION-tmpdq47o, split off QUESTION-055 and
    Answered by CLAIM-038, and the summary and "What it leaves" say so.
    The answer is otherwise unchanged.
tags:
- logic
- quantum-foundations
- mathematics
date: '2026-10-21'
line: pragmatic-transport
refines:
- QUESTION-055
summary: >-
  The conditional part of [QUESTION-055](QUESTION-055.md), split off under [ADR-049](../decisions.d/ADR-049.md) and
  answered by [THEORY-516](../theory.d/THEORY-516.md) and [THEORY-037](../theory.d/THEORY-037.md). Over a presheaf of contexts the
  truth values are sieves, and negation is the Heyting pseudo-complement
  that the base category fixes, not an orthocomplement. That the
  communicative object is such a presheaf is QUESTION-tmpdq47o, Answered
  by CLAIM-038. Over which base, and whether probes split it into
  sectors, stays with [QUESTION-055](QUESTION-055.md).
answered_by:
- THEORY-037
- THEORY-516
---

# QUESTION-247: If the communicative object is a presheaf of propositions over a category of contexts, is the negation its topos logic gives an orthocomplement or a Heyting pseudo-complement, and what fixes it?

## Answer

A Heyting pseudo-complement, fixed by the base category. This is the part
of [QUESTION-055](QUESTION-055.md) that its question "does the context-indexed form of the
communicative object settle which?" asks, split off on 2026-10-21
([ADR-049](../decisions.d/ADR-049.md)). It is conditional: [CLAIM-038](../claims.d/CLAIM-038.md), which makes the communicative
object a presheaf over contexts, is Active since 2026-10-29, and that
part is QUESTION-tmpdq47o, Answered.

- **The general case.** [THEORY-516](../theory.d/THEORY-516.md) (Active), from Butterfield and Isham
  ([LIT-381](../literature.d/LIT-381.md), [LIT-389](../literature.d/LIT-389.md)). For any presheaf of propositions over a small
  category of contexts, a sieve-valued valuation obeys functional
  composition exactly when it is a subobject of the presheaf. Truth
  values are sieves on the base. Their negation is the pseudo-complement,
  under which only S ∨ ¬S ≤ 1 holds. The base category fixes this logic,
  and global sections do not change it: classical physics has them and
  still gets sieves.
- **The quantum instance.** [THEORY-037](../theory.d/THEORY-037.md) (Active), from Döring and Isham
  ([LIT-335](../literature.d/LIT-335.md), [LIT-343](../literature.d/LIT-343.md)). Over the von Neumann subalgebras, propositions form
  a distributive Heyting algebra, not an orthocomplemented lattice. The
  negation of δ(P) is not δ(1 − P), and excluded middle fails already for
  ℂ². The record re-derives the Heyting laws in [THEORY-037](../theory.d/THEORY-037.md)'s note of
  2026-10-19.

So the context-indexed form does settle it, given the base: the negation
is not an orthocomplement. Whether excluded middle holds depends on the
base. A base with exactly one arrow between any two objects gives
two-valued logic ([THEORY-516](../theory.d/THEORY-516.md)), and the quantum base does not ([THEORY-037](../theory.d/THEORY-037.md)).

## What it leaves to [QUESTION-055](QUESTION-055.md)

[THEORY-516](../theory.d/THEORY-516.md) says the choice of base remains free, and that sieve values
are "among the most natural" valuations, not forced. So this answer
gives the negation once a base is chosen. It does not say whether the
communicative object is a presheaf, which base it has, or whether some
probe family splits it into sectors that no probe connects ([THEORY-042](../theory.d/THEORY-042.md)).
The first is QUESTION-tmpdq47o, Answered by CLAIM-038 on 2026-10-29.
The other two stay with the parent.
