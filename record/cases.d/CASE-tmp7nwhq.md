---
status: Active
title: 'A noncontextual inequality for a pragmatic rendering experiment, derived from its operational equivalences and verified numerically'
version: 1
standing: documented
kind: executed-study
tags:
- contextuality
- quantum-foundations
date: '2026-11-22'
line:
- pragmatic-transport
illustrates:
- CLAIM-tmp59ejz
bears_on:
- QUESTION-067
draws_on:
- THEORY-315
---
<!-- inactive-ok-file: CLAIM-tmp59ejz — new; the claim this study illustrates, filed in the same unit -->

# CASE-tmp7nwhq: A noncontextual inequality for a pragmatic rendering experiment, derived from its operational equivalences and verified numerically

## The case

A computed check, run for [LEAD-103](../leads.d/LEAD-103.md), of the inequality
that [QUESTION-067](../questions.d/QUESTION-067.md) asks for: the one a pragmatic
experiment's operational equivalences imply under generalized (preparation)
noncontextuality, separate from the sheaf criterion. The experiment is
modelled as four renderings R1–R4 of one utterance (preparations) and two
binary relational probes X and Z (measurements), each with outcomes ±1. A
rendering's predictability under a probe is ⟨X⟩ᵢ = p(+|Rᵢ,X) − p(−|Rᵢ,X) ∈
[−1,1].

Two operational equivalences are imposed, matching the record's
[observational equivalence](../terms.d/TERM-014.md) (probe-relative) and
[CLAIM-044](../claims.d/CLAIM-044.md)'s mixed reading of an ambiguous utterance:

- **OE1 (equal-predictability orbit).** |⟨X⟩ᵢ| = x and |⟨Z⟩ᵢ| = z for every
  i, with the four sign patterns R1:(+,+), R2:(−,+), R3:(−,−), R4:(+,−).
- **OE2 (mixture equivalence).** ½R1 ⊕ ½R3 ≈ ½R2 ⊕ ½R4: the two equal
  mixtures give identical statistics for every probe.

Generalized noncontextuality for preparations turns OE2 into the equality
½ν1 + ½ν3 = ½ν2 + ½ν4 of the renderings' distributions over the ontic
space.

The study is four checks, scripted in numpy/scipy (CPU, single-threaded),
with five pytest assertions; the script, tests, per-check results
(`results.jsonl`) and a rerun README are under
`scratch/studies/lead-103/`. It is documented (an executed study), not a
field experiment on human judgements; what it establishes is the formal
inequality and its violability, not that any pragmatic data violate it.

## What it can show

1. **The noncontextual bound, exactly (linear program).** Over
   preparation-noncontextual models on the four deterministic ontic states
   — the reduction is without loss when the measurement effects carry no
   nontrivial operational equivalence (Schmid, Spekkens and Wolfe, via
   [THEORY-315](../theory.d/THEORY-315.md)) — the maximum of each of ±⟨X⟩ ±
   ⟨Z⟩ subject to OE1 and OE2 is exactly 1.0. The four faces are the diamond
   |⟨X⟩| + |⟨Z⟩| ≤ 1.

2. **Non-determinism does not help (corroboration).** For 200 random
   *indeterministic* response-function pairs over six ontic states, the
   linear program that maximises ⟨X⟩ + ⟨Z⟩ over the ontic distributions,
   subject to OE1 and OE2, never exceeded the bound (largest found 0.874).

3. **A quantum realization violates it.** The qubit orbit with Bloch
   vectors (±x, 0, ±z), X = σₓ, Z = σ_z, satisfies OE1 and OE2 exactly —
   the two equal mixtures both equal the maximally mixed state I/2 — and
   reaches ⟨X⟩ + ⟨Z⟩ = √2 ≈ 1.414 at x = z = 1/√2, the maximal violation.
   So the inequality is a genuine (violable) test, not a tautology.

4. **The mixture equivalence is load-bearing.** Dropping OE2 and keeping
   only OE1, a preparation-noncontextual model reaches joint predictability
   x = z = 1 (⟨X⟩ + ⟨Z⟩ = 2): with no equivalence among the renderings
   there is no bound. This is the sense in which the inequality rests on an
   operational *equivalence*, not merely on the probes.

What it cannot show, given its standing: that a pragmatic probe family can
actually make two renderings operationally equivalent over the whole family
(tomographic completeness) or exactly (OE1, OE2 are imposed as exact
equalities). Those conditions, which [QUESTION-067](../questions.d/QUESTION-067.md)
and its note of 2026-10-14 set, are assumptions here, not results. The
study shows the inequality the assumptions imply, and that it is non-trivial
and quantum-violable; whether the assumptions hold of any communicative
experiment is open.

The construction and its interpretation are the assistant's (Claude, in
this session); adopting them is the owner's call.
