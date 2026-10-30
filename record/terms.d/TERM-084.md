---
number: 84
status: Active
formerly:
- TERM-tmpoy9w4
title: 'descent, and which sense: provenance, lineage, common ancestry or causal descent'
version: 3
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Adopted by the owner on 2026-10-27: status Proposed → Active. The
    claims that use the word in one of its senses now name the term in
    `uses`, and CLAIM-191 is moved from provenance to lineage, which is
    what its "by descent, by its code" means. The definition is unchanged.
- version: 3
  date: '2026-10-30'
  note: >-
    CLAIM-420's quotation in sense 4 updated to that claim's narrowed
    title of 2026-10-30 ("can descend"). The definition is unchanged.
tags:
- individuation
- social-ontology
- translation
date: '2026-10-27'
line: distributed-agency
complements:
- TERM-008
- TERM-071
summary: >-
  "Descent" carries at least four historical senses in the record's
  claims, and they differ in what the claims turn on: whether the relation
  is directed, whether it carries a fidelity, and whether it implies
  continuation. [CLAIM-210](../claims.d/CLAIM-210.md) and [CASE-054](../cases.d/CASE-054.md) had let two of them meet, which the
  owner's review of 2026-10-27 resolved; this term lists the senses so a
  claim says which. It does not cover descent in optimization (gradient or
  common descent directions). Adopted by the owner on 2026-10-27.
---

# TERM-084: descent, and which sense: provenance, lineage, common ancestry or causal descent

## Definition

A claim that one thing descends from another says which of these it
means.

1. **Provenance.** One realization was made from another: a single
   transport ([TERM-008](TERM-008.md)) from a given source. Directed. It is the relation
   a fidelity profile is defined for ([TERM-043](TERM-043.md)), so the descendant has a
   fidelity to its source, high or low. [CLAIM-210](../claims.d/CLAIM-210.md)'s "T was made from S",
   whose sentence was revised on 2026-10-27 to call this provenance;
   [CLAIM-246](../claims.d/CLAIM-246.md)'s objection, and [CLAIM-204](../claims.d/CLAIM-204.md)'s account of direction, which
   points to [CLAIM-210](../claims.d/CLAIM-210.md)'s answer.
2. **Lineage.** Continuity of transmission across successive carriers: a
   retelling of a retelling, a fandom carried through a generation, an
   institution across its branches. Directed, and transitive along the
   chain. It is [CLAIM-002](../claims.d/CLAIM-002.md)'s "continuity of transmission" ("descent is not
   similarity"), [TERM-071](TERM-071.md)'s historical persistence, and what [CLAIM-329](../claims.d/CLAIM-329.md) says
   persistence through total turnover consists in; [CLAIM-191](../claims.d/CLAIM-191.md)'s later
   entries that "reach the claim by descent, by its code", and [CLAIM-417](../claims.d/CLAIM-417.md)'s
   "Historical descent". [CLAIM-287](../claims.d/CLAIM-287.md)'s caution
   applies: it "is not automatically an equivalence relation", since
   lineages can branch and merge.
3. **Common ancestry.** Two realizations descend, each by lineage, from one
   ancestor, and neither from the other. Symmetric between the two. No
   transport runs between them, so neither has any fidelity to the other.
   [CASE-054](../cases.d/CASE-054.md)'s Crow and Hidatsa joking relations, from a parent tribe; the
   paragraph [CLAIM-210](../claims.d/CLAIM-210.md) gained on 2026-10-27.
4. **Causal descent.** The later thing exists because of the earlier one's
   activity, with nothing of it passed on. Directed, with no fidelity and no
   continuation. [CLAIM-420](../claims.d/CLAIM-420.md): "a movement founded to oppose someone can descend
   from them without continuing their perspective", so "causal descent is
   not perspectival inheritance". [CLAIM-329](../claims.d/CLAIM-329.md)'s note of 2026-10-26 gives
   the limiting case: every training checkpoint is causally descended from
   the last, so causal descent alone cannot tell continuation from
   replacement.

What separates them:

| sense | directed | fidelity | continuation |
|---|---|---|---|
| provenance | yes | the descendant to its source | no |
| lineage | yes | open: see below | the candidate for persistence |
| common ancestry | no | none between the pair | no |
| causal descent | yes | none | no |

## What it is not

- **Similarity.** None of the four is resemblance, and resemblance is
  evidence for none of them without a route ([CLAIM-002](../claims.d/CLAIM-002.md), [CLAIM-329](../claims.d/CLAIM-329.md)). Two
  realizations can share a kind with no descent at all ([CLAIM-210](../claims.d/CLAIM-210.md)'s I).
- **Kind-sharing.** Kind-sharing is symmetric and carries no history
  ([TERM-040](TERM-040.md)); descent in senses 1, 2 and 4 is directed, and common ancestry
  is a fact about history that kind-sharing is not.
- **Identity.** A lineage can continue an organization in one respect and
  not another, and several later collectives can each descend from one
  ([CLAIM-328](../claims.d/CLAIM-328.md)); numerical identity is a further question ([QUESTION-118](../questions.d/QUESTION-118.md)).
- **Descent in optimization.** "Gradient descent" and the "common descent
  direction" of [CLAIM-347](../claims.d/CLAIM-347.md), [CLAIM-351](../claims.d/CLAIM-351.md) and [CLAIM-366](../claims.d/CLAIM-366.md) are unrelated uses of the
  word.

## What it leaves open

Whether a lineage is provenance composed along a chain, so that each
branch has a fidelity relative to its ancestor. The record treats serial
reproduction that way ([CASE-068](../cases.d/CASE-068.md), [CLAIM-056](../claims.d/CLAIM-056.md): local transport errors
propagate through later reconstructions), and [CASE-054](../cases.d/CASE-054.md) leaves it open for
the reproduction of an institution, which is re-enacted rather than
rendered from a token. If lineage is composed provenance, common ancestry
gives each sibling a fidelity to the ancestor and still none to the
other. [ADR-056](../decisions.d/ADR-056.md)'s proposed kinds would class this term as a
disambiguation.
