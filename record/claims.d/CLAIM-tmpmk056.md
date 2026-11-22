---
status: Proposed
title: 'A descriptor and an imposition are an informative and a performative update: adding a predicate an entry already passes restricts the admissible versions to those where it holds, which is informative update, and enforcing one it fails moves each version to a nearest version where it holds, which is performative update when minimal change is read as nearness in a metric; so the record''s two kinds of predicate are the two directions of fit'
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
- CLAIM-tmp5rv9x
summary: >-
  Filed under the dialectic regime on 2026-11-22, answering the owner's
  "tell me about our current account of specification". The join is
  between Krifka's performative updates (LIT-835, read in THEORY-162) and
  the record's predicates as constraints (CLAIM-783, TERM-134). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-783 TERM-134 THEORY-162 CLAIM-tmp5rv9x — Proposed; the claims, term and reading this joins, and the claim filed with it -->

# CLAIM-tmpmk056: A descriptor and an imposition are an informative and a performative update: adding a predicate an entry already passes restricts the admissible versions to those where it holds, which is informative update, and enforcing one it fails moves each version to a nearest version where it holds, which is performative update when minimal change is read as nearness in a metric; so the record's two kinds of predicate are the two directions of fit

## The claim

Krifka (LIT-835) formalizes the difference between describing and bringing
about. Over a context set c of indices:

- **informative update** restricts c to the indices where φ holds,
  c + inform(φ) = {i ∈ c | φ(i)}, always a subset of c;
- **performative update** replaces each index by its minimal φ-changed
  successor, which is not in general in c and is applied when φ is false
  throughout c.

The record's reading notes that this is Searle's direction of fit made
formal. CLAIM-783 (part 5) and TERM-134 sort an entry's predicates the same
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
  and CLAIM-783's convex projection results (fixed points, the soft limit)
  need not carry over; the identification of the two kinds does.
- Not that a filer always knows which kind a predicate is. That is decided
  by the entry as it stands when the predicate is added.
