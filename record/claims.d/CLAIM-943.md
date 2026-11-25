---
number: 943
status: Proposed
formerly:
- CLAIM-tmpmk056
title: 'Descriptors inform, impositions perform'
statement: >-
  A descriptor and an imposition are an informative and a performative
  update: adding a predicate an entry already passes restricts the
  admissible versions to those where it holds, which is informative update,
  and enforcing one it fails moves each version to a nearest version where
  it holds, which is performative update when minimal change is read as
  nearness in a metric; so the record's two kinds of predicate are the two
  directions of fit
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either identification: in informative update c + inform(φ)
  being the intersection of c with the φ-versions; or in performative
  update c + perform(φ), each index replaced by its minimal φ-changed
  successor, being nearest-point projection onto the φ-versions once
  minimal change is read as least distance in a metric on versions.
tags:
- logic
- philosophy-of-language
- design-rationale
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
rests_on:
- CLAIM-783
grounds:
- THEORY-162
uses:
- TERM-134
complements:
- CLAIM-942
summary: >-
  Filed under the dialectic regime on 2026-11-22, answering the owner's
  "tell me about our current account of specification". The join is
  between Krifka's performative updates ([LIT-835](../literature.d/LIT-835.md), read in [THEORY-162](../theory.d/THEORY-162.md)) and
  the record's predicates as constraints ([CLAIM-783](CLAIM-783.md), [TERM-134](../terms.d/TERM-134.md)). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-2310 CLAIM-1327 — Proposed; the reading of Dunfield and Krishnaswami (2021) and the entries filed from it, or the entries it bears on -->
<!-- inactive-ok-file: CLAIM-783 TERM-134 THEORY-162 — Proposed; the claims, term and reading this joins, and the claim filed with it -->

# CLAIM-943: Descriptors inform, impositions perform

## The claim

Krifka ([LIT-835](../literature.d/LIT-835.md)) formalizes the difference between describing and bringing
about. Over a context set c of indices:

- **informative update** restricts c to the indices where φ holds,
  c + inform(φ) = {i ∈ c | φ(i)}, always a subset of c;
- **performative update** replaces each index by its minimal φ-changed
  successor, which is not in general in c and is applied when φ is false
  throughout c.

The record's reading notes that this is Searle's direction of fit made
formal. [CLAIM-783](CLAIM-783.md) (part 5) and [TERM-134](../terms.d/TERM-134.md) sort an entry's predicates the same
way, by whether the entry passes a predicate when it is added:

- a **descriptor**, one the entry passes, restricts the admissible versions
  A to A ∩ A_φ and moves nothing. That is informative update with c the
  admissible versions.
- an **imposition**, one it fails, is enforced by moving the entry to the
  nearest version that passes, the projection P_φ. That is performative
  update, provided "minimal φ-changed successor" is read as the φ-version
  at least distance in a metric on versions. Krifka's minimal change is an
  ordering of similarity; the metric reading is one instance of it.

So a descriptor fits the predicate to the entry (word to world) and an
imposition fits the entry to the predicate (world to word).

## What it does not say

- Not that every similarity ordering is a metric. Where minimal change is
  only a preorder, performative update is a selection of minimal elements,
  and [CLAIM-783](CLAIM-783.md)'s convex projection results (fixed points, the soft limit)
  need not carry over; the identification of the two kinds does.
- Not that a filer always knows which kind a predicate is. That is decided
  by the entry as it stands when the predicate is added.

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-2259 CLAIM-965 — Proposed; filed for LEAD-215 -->

A contrast, from Freeman and Pfenning's refinement types ([THEORY-2259](../theory.d/THEORY-2259.md);
[NOTE-2350](../notes.d/NOTE-2350.md)): a type system with informative update only. Inference and
accepted annotations narrow what a term may be taken to have, and "we do
not extend the language of programs for ML (only the language of types)"
(p. 1): no rule moves a term. Performative update, changing a term to
pass a type it fails, lies with the programmer, outside the system
([CLAIM-965](CLAIM-965.md)). No change.

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-2260 CLAIM-974 — Proposed; filed for LEAD-215 -->

A contrast, again, from Davies and Pfenning's bidirectional checker
([THEORY-2260](../theory.d/THEORY-2260.md); [NOTE-2351](../notes.d/NOTE-2351.md)): informative update only inside the
system, checking accepting or rejecting and ascriptions erased; the
performative update that makes a failing term pass is the programmer's
([CLAIM-974](CLAIM-974.md)). One addition: such an edit can change behaviour.
η-expanding a non-value to meet the value restriction "only alters the
semantics of the program when effects are involved" (p. 5), which is to
say it does then. No change.

## Note of 2026-11-22: Dunfield and Krishnaswami, read

A qualification, from a contrast case. In bidirectional typing ([THEORY-2310](../theory.d/THEORY-2310.md),
read in [NOTE-2421](../notes.d/NOTE-2421.md)) checking a term against a type given is a requirement in
the authors' word (§4.4) and a test that moves nothing whether the term
passes or fails (§1, §9.1). By this claim's criterion a requirement the
term already meets is a descriptor; by Searle's it is still world to
word. So the closing clause, "the record's two kinds of predicate are the
two directions of fit", holds for enforced predicates and not for a
requirement already met. [CLAIM-1327](CLAIM-1327.md) files the objection. The two
identifications with Krifka's updates are untouched.
