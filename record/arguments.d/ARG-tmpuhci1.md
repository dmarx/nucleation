---
status: Proposed
title: "Mitzenmacher's survey supports the history of cumulative advantage and the linear-kernel case, but not the claim that the kernel's form decides whether a power law appears, so it corroborates the claim and does not ground it"
version: 1
form: source
grounds:
- THEORY-tmp23821
concludes:
- CLAIM-tmpepx9m
tags:
- network-science
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  [CLAIM-tmpepx9m](../claims.d/CLAIM-tmpepx9m.md) cited Mitzenmacher's review ([LIT-tmpwdtfj](../literature.d/LIT-tmpwdtfj.md)) in its grounds,
  beside A3's "preferential attachment alone does not guarantee this
  result". Read, the review supports the claim's history (Yule, Simon, the
  Web models) and its linear case with entry, including a shifted linear
  kernel that moves the exponent, which the claim's defeated_if allows. It
  has nothing on sublinear or superlinear kernels or on attachment without
  entry. So it moves from grounds to corroborates; the kernel regimes rest
  on Krapivsky, Redner and Leyvraz and on the filing's simulations. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpepx9m CLAIM-tmply70l THEORY-tmp23821 — Proposed; the claim and the reading this argument joins -->
<!-- inactive-ok-file: LIT-tmp959qu — Deferred; the kernel-regime work, registered and unread -->

# ARG-tmpuhci1: Mitzenmacher's survey supports the history of cumulative advantage and the linear-kernel case, but not the claim that the kernel's form decides whether a power law appears, so it corroborates the claim and does not ground it

## The inference

[CLAIM-tmpepx9m](../claims.d/CLAIM-tmpepx9m.md) says cumulative advantage gives a power law only with linear
attachment and continual entry, and that other kernels give other tails.
Its body quoted A3, "preferential attachment alone does not guarantee this
result", and added "A3 cites Mitzenmacher's review". Read as a source for
the claim, [THEORY-tmp23821](../theory.d/THEORY-tmp23821.md) would carry that sentence.

## Critical questions (source)

**Does the work say this, read in context?** In part. §3 (pp. 230–233)
derives the power law for a growing Web graph in which each new page links
uniformly with probability α and by indegree otherwise, c_j ∼
c·j^(−(2−α)/(1−α)): linear (shifted) attachment with a new page at every
step. It traces the argument to Yule, "the first similar argument dates
back to at least 1925", and to Simon. It nowhere varies the kernel's
exponent, nor removes entry, nor says that attachment alone is not enough.

**Is it said within the scope the claim needs?** Only for the linear case.
The claim's distinctive content is the other three regimes (exponential,
stretched exponential, condensation) and the need for entry. Those are
Krapivsky, Redner and Leyvraz's ([LIT-tmp959qu](../literature.d/LIT-tmp959qu.md)) and the filing's own
simulations; the need for entry is also [CLAIM-tmply70l](../claims.d/CLAIM-tmply70l.md)'s derivation.

**Does the claim lean on the reading for more than it holds?** It did, by
listing the review in its grounds next to A3's sentence. The review is
independent evidence that linear attachment with entry gives a power law,
with an exponent set by the mix, which the claim's `defeated_if` already
allows. That is corroboration of one clause, not a ground for the claim.

## Verdict

[LIT-tmpwdtfj](../literature.d/LIT-tmpwdtfj.md) moves from the claim's grounds to `corroborates` on
[THEORY-tmp23821](../theory.d/THEORY-tmp23821.md), and the body's attribution is corrected in a dated note on
[CLAIM-tmpepx9m](../claims.d/CLAIM-tmpepx9m.md).
