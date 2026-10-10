---
status: Proposed
title: 'Blackwell''s order bounds what a rendering makes possible for any receiver, and a given receiver''s access is usable information relative to the rules it can apply, which a garbling can raise for that receiver but never above what the source makes possible'
version: 1
role: thesis
defeated_if: >-
  On renderings made without the situation (garblings of their sources),
  the named receivers never do better than with the source on any task in
  Q, beyond sampling error, in a sample large enough to detect such gains
  at a rate fixed in advance, so that a receiver's access tracks ideal
  informativeness and the distinction does no work.
tags:
- information-theory
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-156
- THEORY-176
complements:
- CLAIM-050
- CLAIM-087
uses:
- TERM-034
summary: >-
  The record's reconciliation, on 2026-10-10, of [CLAIM-tmpdt857](CLAIM-tmpdt857.md). Both
  standards are kept, in different roles: Blackwell's order is the
  ceiling, and [TERM-034](../terms.d/TERM-034.md)'s interpreter-relative fidelity ("relative to an
  interpreter and its available side information") is the receiver's.
  [CLAIM-087](CLAIM-087.md)'s improvement is a gain in usable information. The nearest
  held reading is [THEORY-176](../theory.d/THEORY-176.md)'s "Its loss bounds r's best attainable risk
  for that problem from above", for restricted rules. The example is
  checkable; whether real receivers show such gains is a proposal. The
  usable-information literature is not held. It does not say which rule
  class real readers have.
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-087 — Proposed; the Blackwell thesis and the improvement claim this reconciles, cited as open -->
<!-- inactive-ok-file: THEORY-156 THEORY-176 — Proposed; cited as the readings of Blackwell's order and of restricted decoders, not as settled -->
<!-- inactive-ok-file: CLAIM-115 CLAIM-076 — Proposed; the manuscript's thesis and the blind-captioner design, cited as open -->
<!-- inactive-ok-file: CLAIM-tmpz239h — Proposed; the restated decision term, cited for its garbling step, not as settled -->

# CLAIM-tmp0jq5k: Blackwell's order bounds what a rendering makes possible for any receiver, and a given receiver's access is usable information relative to the rules it can apply, which a garbling can raise for that receiver but never above what the source makes possible

## What it answers

This is the record's reply of 2026-10-10 to [CLAIM-tmpdt857](CLAIM-tmpdt857.md), which the record
concedes and reconciles. The objection is right that the line uses an ideal
decision-maker's standard for its formal ground ([CLAIM-050](CLAIM-050.md)) and a bounded
receiver's for its thesis and tests ([CLAIM-115](CLAIM-115.md)'s "a receiving system",
[TERM-034](../terms.d/TERM-034.md)'s interpreter), and that [CLAIM-087](CLAIM-087.md)'s improved access, in a chain
whose captioners are blind to the situation ([CLAIM-076](CLAIM-076.md)'s design), is
impossible for an ideal receiver. The reply keeps both standards and gives
them different roles. The example below is elementary and checkable. That
real receivers gain from garblings is an empirical proposal, and the defeat
condition tests it.

## The claim

**Two quantities.** For a decision problem about the situation Z:

- **What a rendering makes possible** is the best risk over all decision
  rules that read it. Blackwell's order compares renderings by this
  ([THEORY-156](../theory.d/THEORY-156.md)), and by it a garbling is never better ([CLAIM-tmpz239h](CLAIM-tmpz239h.md), step
  (a)).
- **What a receiver can use** is the best risk over the rules in a class
  the receiver can apply. [TERM-034](../terms.d/TERM-034.md) makes fidelity "relative to an
  interpreter and its available side information". Restricting the rules
  is the same move [THEORY-176](../theory.d/THEORY-176.md) makes for stitched networks: "Its loss bounds
  r's best attainable risk for that problem from above".

For a restricted class, a garbling can lower the receiver's risk, because
the garbling can compute for the receiver something the receiver cannot
compute from the source. It cannot lower it below what the source makes
possible.

**An example.** Let Z be uniform on {0, 1}. Let X₁ be uniform on {0, 1},
independent of Z, and X₂ = Z ⊕ X₁ (addition mod 2). The source is
U = (X₁, X₂).

- Each coordinate alone is independent of Z. For X₁ this is given. For X₂:
  P(X₂ = 1 | Z = z) = P(X₁ = 1 ⊕ z) = 1/2 for each z.
- Take a receiver whose rules read one coordinate of what it is given, and
  the problem "guess Z" with 0–1 loss. From U, whichever coordinate it
  reads is independent of Z, so its risk is 1/2.
- Let the rendering be V = X₁ ⊕ X₂. Then V = X₁ ⊕ Z ⊕ X₁ = Z. V is computed
  from U alone, a deterministic kernel applied to U, so it is a garbling of
  U.
- The same receiver reads V's one coordinate and guesses Z exactly: risk 0.
- An ideal receiver has risk 0 from either: from U it computes X₁ ⊕ X₂. So
  the order is respected, since V is no better than U for the ideal
  receiver, and the bounded receiver gains 1/2 from the garbling.

**The ceiling.** For any receiver and any problem, its risk from V is at
least the best risk from V over all rules, which is at least the best risk
from U over all rules, because V is a garbling of U. So no receiver does
better with the rendering than an ideal receiver does with the source.
Blackwell's order bounds every receiver's gain from a garbling.

**What this does to the two claims.** [CLAIM-087](CLAIM-087.md)'s improvement is a gain in
usable information for receivers whose rules cannot extract the relation
from the text as easily as from the image. It is possible, and it is not a
counterexample to Blackwell's theorem. [CLAIM-050](CLAIM-050.md)'s standard stays the
ceiling. A bounded receiver doing better with a garbling defeats neither,
and [CLAIM-050](CLAIM-050.md)'s restated condition does not count it as a defeat.

## What it does not say

- It does not say which rule class real readers have. The one-coordinate
  receiver is a device to show the gap exists.
- It does not say garblings usually help. They help a receiver only when
  they do work the receiver cannot.
- It does not supply an order for usable information with results of its
  own. Restricting the rules loses Blackwell's garbling theorem, as
  [THEORY-176](../theory.d/THEORY-176.md) shows for stitching, and the literature on usable information
  is not held here.
