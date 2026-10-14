---
number: 11
status: Active
formerly:
- THEORY-tmp28873
title: 'Generalized contextuality is strictly broader than Kochen–Specker contextuality: a qubit already has no preparation-noncontextual model, though no Kochen–Specker argument with sharp measurements exists in dimension two'
version: 3
history:
- version: 2
  date: '2026-10-14'
  note: >-
    LIT-266 was read in full (NOTE-tmpqr65v). The §IV case analysis was
    checked step by step and is complete, and the §III dimension argument
    is stated and elementary, which is what the promotion condition asked,
    so the status moved from Proposed to Active and the condition was
    removed. The title and the first "does not say" bullet now restrict
    the dimension-two claim to sharp measurements: Cabello's 2003 POVM
    argument is a Kochen–Specker-style proof for a qubit, which Spekkens
    rejects (footnote 1, §VIII) because it assumes outcome determinism for
    unsharp measurements. The "Leibnizian methodological principle"
    wording is re-attributed to Schmid, Selby and Spekkens (LIT-945,
    §VI.C; NOTE-tmp5ey9r); LIT-266 argues from ontological economy and
    Einstein's equivalence principle (§VII) and does not name Leibniz.
    LIT-945 added as a source. LIT-263 is still unread.
- version: 3
  date: '2026-10-14'
  note: >-
    The choice-of-notion caveat now points to THEORY-tmpecylf, filed today
    from LIT-945, for what the Leibnizian principle does in a no-go. A
    sentence added that LIT-266 also proves transformation contextuality
    for a qubit (§VI), as read in NOTE-tmpqr65v.
tags:
- contextuality
- quantum-foundations
date: '2026-09-27'
source:
- LIT-266
- LIT-263
- LIT-945
summary: >-
  Spekkens (2005), [LIT-266](../literature.d/LIT-266.md), §III and §IV, read in full in NOTE-tmpqr65v;
  restated in Budroni et al. ([LIT-263](../literature.d/LIT-263.md), §IV.E, unread). Corrects the
  reading that contextuality needs dimension three. The dimension-two
  limit holds for sharp measurements only.
extends:
- THEORY-012
answers:
- QUESTION-067
---
<!-- inactive-ok-file: LIT-263 — Deferred: filed and skimmed on 2026-09-27; cited as a restatement of LIT-266, which was read in full, and not leaned on -->
<!-- inactive-ok-file: THEORY-tmpecylf — Proposed; named in the choice-of-notion caveat, not leaned on -->

# THEORY-011: Generalized contextuality is strictly broader than Kochen–Specker contextuality: a qubit already has no preparation-noncontextual model, though no Kochen–Specker argument with sharp measurements exists in dimension two

## Source

Spekkens (2005), [LIT-266](../literature.d/LIT-266.md), §III, §IV (Eqs. 13–36), footnote 1, §VIII, §IX ([NOTE-tmpqr65v](../notes.d/NOTE-tmpqr65v.md)). Schmid, Selby and Spekkens, [LIT-945](../literature.d/LIT-945.md), §VI.C, for the Leibnizian principle ([NOTE-tmp5ey9r](../notes.d/NOTE-tmp5ey9r.md)). Budroni et al. (2022), [LIT-263](../literature.d/LIT-263.md), §IV.E.1–4 (restatement; the experimental report of Mazurek et al. 2016 is cited there, not read).

## What was actually shown

Six pure qubit states give five decompositions of the maximally mixed state; distinguishable preparations cannot overlap in their ontic supports, and preparation noncontextuality then forces every distribution to vanish (§IV). Traditional Kochen–Specker proofs need dimension at least three, because a two-dimensional projective measurement has no non-trivial fine-grainings (§III). Budroni et al. restate the proof and note that Bell's and Kochen & Specker's own qubit models are preparation contextual (§IV.E.1, §IV.E.4; [LIT-266](../literature.d/LIT-266.md) §IX already deems them contextual under its definition), and cite an experiment reporting a violation of the noncontextual bound (§IV.E.2–3).

Spekkens ([LIT-266](../literature.d/LIT-266.md)) also proves transformation contextuality for a qubit (§VI, App. A): six rotations about one axis give five convex decompositions of one map, and transformation noncontextuality then reproduces the §IV constraints ([NOTE-tmpqr65v](../notes.d/NOTE-tmpqr65v.md)).

## What this does not say

- That a qubit is Kochen–Specker contextual in the traditional sense, with sharp measurements; it is not. Cabello's 2003 Kochen–Specker argument for a single qubit uses POVMs. Spekkens rejects it, not as mathematics, but because it assumes outcome determinism for unsharp measurements, which no assumption of noncontextuality justifies (footnote 1, §VIII).
- That preparation contextuality has been shown loophole-free; tomographic completeness is assumed (Budroni et al. §IV.E.3). [LIT-266](../literature.d/LIT-266.md)'s proofs assume exact operational equivalence and perfectly distinguishable pairs, and give no noise-robust inequality (§IX).
- Which notion is the right criterion of classicality. [LIT-266](../literature.d/LIT-266.md) motivates it by ontological economy, with Einstein's equivalence principle as the example (§VII), and does not name Leibniz. The later programme grounds it in a Leibnizian methodological principle ([LIT-945](../literature.d/LIT-945.md), §VI.C). A reader may reject either. [THEORY-tmpecylf](THEORY-tmpecylf.md) states what that principle does in a no-go: within classical realism, a noncontextuality no-go refutes Leibnizian representations, not realist ones as such.
