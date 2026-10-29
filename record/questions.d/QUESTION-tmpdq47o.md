---
status: Answered
title: 'Is the communicative object a presheaf over contexts?'
version: 1
tags:
- logic
- mathematics
date: '2026-10-29'
line: pragmatic-transport
refines:
- QUESTION-055
answered_by:
- CLAIM-038
summary: >-
  The first remaining part of [QUESTION-055](QUESTION-055.md), split off by the fourteenth
  status review under [ADR-049](../decisions.d/ADR-049.md) because [CLAIM-038](../claims.d/CLAIM-038.md) (Active since
  2026-10-29) settles it: a communicative object is a context-indexed
  system of empirical constraints over a cover of contexts, supports or
  distributions with their restrictions ([TERM-042](../terms.d/TERM-042.md)), which is a presheaf
  over contexts. Which base category it has, and whether some probe
  family splits it into sectors, stays [QUESTION-055](QUESTION-055.md)'s.
---

# QUESTION-tmpdq47o: Is the communicative object a presheaf over contexts?

## Why it was a question

[QUESTION-055](QUESTION-055.md) asks what fixes the negation of a communicative category.
After its split of 2026-10-21, [QUESTION-247](QUESTION-247.md) answered the conditional
part: over a presheaf of contexts the negation is the Heyting
pseudo-complement the base category fixes. What [QUESTION-055](QUESTION-055.md) kept began
with whether the communicative object is such a presheaf at all, which
then rested on [CLAIM-038](../claims.d/CLAIM-038.md), a Proposed thesis. This part now has an answer
the record holds; the rest does not, so they are filed apart ([ADR-049](../decisions.d/ADR-049.md)).

## The answer

Yes, by [CLAIM-038](../claims.d/CLAIM-038.md) and the definition it states in [TERM-042](../terms.d/TERM-042.md)'s terms. The
object is the empirical data over a cover of contexts, supports or
distributions, together with their restrictions to smaller contexts.
That is a presheaf over the contexts. Whether the data agree on overlaps
and whether they extend to one global interpretation are things to find
out, not part of the definition, and [CLAIM-038](../claims.d/CLAIM-038.md) says they need not
extend.

The answer does not say which category of contexts is the base, and so
does not fix whether excluded middle holds for communicative categories
([QUESTION-247](QUESTION-247.md)). It does not say whether a probe family splits the object
into sectors ([THEORY-042](../theory.d/THEORY-042.md)). Both stay with [QUESTION-055](QUESTION-055.md).
