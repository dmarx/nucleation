---
status: Proposed
title: "A pragmatic rendering experiment's operational equivalences, equal probe predictabilities in the four sign patterns plus one mixture equivalence among renderings, imply a generalized-noncontextuality inequality bounding the sum of the two probe predictabilities by one, a preparation-contextuality test separate from and invisible to the sheaf criterion"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A demonstration that the probe families a pragmatic experiment can field
  can never make two renderings operationally equivalent over the whole
  family, or never exactly, so that the mixture equivalence OE2 cannot be
  instantiated and only the sheaf or Kochen–Specker notion has a
  non-vacuous test; or a fault in the derivation of the diamond from the
  two equivalences under preparation noncontextuality.
tags:
- contextuality
- quantum-foundations
- philosophy-of-language
date: '2026-11-22'
line:
- pragmatic-transport
rests_on:
- CLAIM-044
- CLAIM-046
- CLAIM-142
grounds:
- THEORY-315
- CASE-tmp7nwhq
complements:
- CLAIM-037
uses:
- TERM-014
- TERM-031
bears_on:
- QUESTION-067
- QUESTION-001
---
<!-- inactive-ok-file: CLAIM-044 CLAIM-142 — Proposed; premises this claim rests on, open and cited as open -->
<!-- inactive-ok-file: CLAIM-009 CLAIM-037 — Proposed; the global-extension claims this one is the preparation counterpart to, open -->
<!-- inactive-ok-file: CASE-tmp7nwhq — new; the executed study that grounds this claim, filed in the same unit -->

# CLAIM-tmp59ejz: A pragmatic rendering experiment's operational equivalences, equal probe predictabilities in the four sign patterns plus one mixture equivalence among renderings, imply a generalized-noncontextuality inequality bounding the sum of the two probe predictabilities by one, a preparation-contextuality test separate from and invisible to the sheaf criterion

## The claim

[QUESTION-067](../questions.d/QUESTION-067.md) asks for the operational
equivalences a pragmatic experiment would assume among renderings, and the
noncontextual inequality they imply, separate from the sheaf criterion.
Here is one such statement and its inequality, in the record's own voice.

Model the experiment as four renderings R1–R4 of a single utterance
(preparations) and two binary relational probes X and Z (measurements),
outcomes ±1. A rendering's predictability under a probe is
⟨X⟩ᵢ = p(+|Rᵢ,X) − p(−|Rᵢ,X). Two equivalences are assumed:

- **OE1 (equal-predictability orbit).** |⟨X⟩ᵢ| = x and |⟨Z⟩ᵢ| = z for every
  i, with the four sign patterns R1:(+,+), R2:(−,+), R3:(−,−), R4:(+,−).
  This is [observational equivalence](../terms.d/TERM-014.md) in magnitude
  across renderings a probe pair cannot separate except by sign
  ([CLAIM-046](../claims.d/CLAIM-046.md), [CLAIM-142](../claims.d/CLAIM-142.md)).
- **OE2 (mixture equivalence).** ½R1 ⊕ ½R3 ≈ ½R2 ⊕ ½R4: two equal mixtures
  of renderings are operationally indistinguishable. This is the form
  [CLAIM-044](../claims.d/CLAIM-044.md)'s ambiguous utterance takes when it is
  read as a mixture of readings in two different ways — one mixed preparation
  with two decompositions.

Generalized noncontextuality for preparations (Spekkens): operationally
equivalent preparations get the same distribution over ontic states, so OE2
becomes ½ν1 + ½ν3 = ½ν2 + ½ν4. Under this assumption, **every such model
satisfies the diamond |⟨X⟩| + |⟨Z⟩| ≤ 1.** A rendering ensemble that
violates it is preparation-contextual.

This is Catani, Leifer, Scala, Schmid and Spekkens's inequality
([THEORY-315](../theory.d/THEORY-315.md)) stated for the pragmatic experiment.
The record's contribution is the mapping — renderings as preparations,
relational probes as measurements, the ambiguity mixture as the Eq.-11
equivalence — and an independent numeric verification
([CASE-tmp7nwhq](../cases.d/CASE-tmp7nwhq.md)): the linear program over
preparation-noncontextual models returns the bound exactly on all four
faces; a qubit orbit with Bloch vectors (±x,0,±z) satisfies OE1 and OE2 and
violates it, up to √2.

## Why the inequality rests on the equivalence, not the probes

One rendering's predictabilities alone are not bounded below 2: for
deterministic ontic states λ ∈ {++, +−, −+, −−} and ν1 = (a,b,c,d),
⟨X⟩1 + ⟨Z⟩1 = 2(a − d) ≤ 2. It is OE2 — the equality ½ν1 + ½ν3 = ½ν2 + ½ν4
linking all four renderings — that cuts the reachable region to the diamond.
Dropping OE2 restores the full x = z = 1 corner (verified). So the test is
of an operational *equivalence* among renderings, and this is exactly why no
sheaf or Kochen–Specker test sees it: X and Z are never asked together, the
measurement cover {X}, {Z} has no overlap, and a global-section obstruction
is vacuous there. The contextuality lives in the preparations, not in any
incompatible context of measurements ([CLAIM-037](../claims.d/CLAIM-037.md)
is the global-extension notion; this complements it).

## What it does not say

- **Not that any pragmatic data are contextual.** OE1 and OE2 are imposed as
  exact equalities over the whole probe family (tomographic completeness),
  the two conditions [QUESTION-067](../questions.d/QUESTION-067.md)'s note of
  2026-10-14 names. Whether a communicative experiment can realize them is
  open; that is why this bears on, and does not answer,
  [QUESTION-067](../questions.d/QUESTION-067.md). The interpretive weight is
  in the mapping and the realizability, not in the inequality, whose proof is
  a theorem ([THEORY-315](../theory.d/THEORY-315.md), verified in
  [CASE-tmp7nwhq](../cases.d/CASE-tmp7nwhq.md)); the warrant is set to
  interpretive for that reason.
- **Not that it supports [CLAIM-009](../claims.d/CLAIM-009.md) or
  [CLAIM-037](../claims.d/CLAIM-037.md) as worded.** Both are stated in the
  global-extension sense. A violation here is not a failure of global
  extension; it is the preparation version those claims do not state, which
  this claim supplies ([NOTE-825](../notes.d/NOTE-825.md) flagged the gap).
- **Not that one binary judgement suffices.** The witness needs two probes
  never made together and four renderings; data from a single binary probe
  always admit a preparation-noncontextual model
  ([NOTE-825](../notes.d/NOTE-825.md)).

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
