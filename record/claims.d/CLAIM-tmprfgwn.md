---
status: Proposed
title: 'Three standards for a communicative distinction come apart: statistical distinguishability of an interpreter''s response profiles, measured locally by the Fisher metric and never raised by a parameter-independent garbling; usability by a bounded receiver, which a transformation can raise; and pragmatic efficacy in the act; and where response models are singular, as Watanabe''s theory treats, a missing response can come from an absent attempt or an unresponsive receiver alike, and only intervention or later dynamics separate them'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A communicative distinction the record cares about whose survival or
  loss across a rendering is fixed by the Fisher information of a
  parameterized response model alone, so that usability by bounded
  receivers and pragmatic efficacy add nothing; or a fitted communicative
  response model in which non-identifiable parameter settings that differ
  in act are always separated by the ordinary probes, so that singularity
  never bears on what can be certified.
tags:
- pragmatics
- information-geometry
- mathematical-statistics
date: '2026-10-24'
line:
- pragmatic-transport
uses:
- TERM-040
- TERM-039
- TERM-064
rests_on:
- CLAIM-199
- CLAIM-115
- CLAIM-223
complements:
- CLAIM-336
- CLAIM-407
- CLAIM-150
- CLAIM-305
grounds:
- THEORY-082
- THEORY-087
- CASE-tmpj2xb7
summary: >-
  The owner's, 2026-10-24, after setting aside the belief–knowledge
  distinction: "forget about that distinction then and let's connect back
  to the communicative act stuff and amari/watanabe theory". Worked through
  the same day (workbench entry of 2026-10-24, U27). Amari's geometry and
  Watanabe's singular learning are given different jobs in one modelling
  architecture, alongside bounded legibility and the communicative-act
  account, rather than read as rival characterizations.
illustrated_by:
- CASE-tmpj2xb7
---

# CLAIM-tmprfgwn: Three standards for a communicative distinction come apart: statistical distinguishability of an interpreter's response profiles, measured locally by the Fisher metric and never raised by a parameter-independent garbling; usability by a bounded receiver, which a transformation can raise; and pragmatic efficacy in the act; and where response models are singular, as Watanabe's theory treats, a missing response can come from an absent attempt or an unresponsive receiver alike, and only intervention or later dynamics separate them

## The claim

The owner, 2026-10-24: "let's connect back to the communicative act stuff
and amari/watanabe theory".

**Distinguishability.** Parameterize an interpreter or communicative
organization by θ and probe it under contexts c drawn from a declared
protocol π ([TERM-039](../terms.d/TERM-039.md)): responses p_θ(y | c). The Fisher metric
G(θ) = E_{c∼π, y∼p_θ}[∇log p · ∇log pᵀ] gives the local statistical
distance, D_KL(p_θ ‖ p_{θ+dθ}) = ½ dθᵀG dθ + o(‖dθ‖²). It answers which
changes of the organization the chosen probes can detect. Amari's natural
gradient uses this metric, and its efficiency result needs G invertible at
the optimum ([THEORY-082](../theory.d/THEORY-082.md)).

If a translation acts on an observation as parameter-independent
stochastic post-processing, Y_source → Y_target, then G_target(θ) ⪯
G_source(θ): the post-processed score is the conditional expectation of the
original, and conditional expectation cannot increase a covariance. A
garbling cannot make a parameter more distinguishable to an unrestricted
observer.

**Usability.** That does not mean a rendering cannot help. [CLAIM-199](CLAIM-199.md): a
bounded receiver can gain from a transformation that makes a distinction
computable for it, with no Shannon information created ([TERM-064](../terms.d/TERM-064.md)). And a
real translation is seldom post-processing of one fixed experiment; it can
change conventions, expectations and the social situation.

**Efficacy.** Whether the act is performed, a promise rather than a
prediction, is fixed by the relational organization of the situation
([TERM-040](../terms.d/TERM-040.md)), not by either statistic.

So statistical distinguishability ≠ usability by a receiver ≠ pragmatic
efficacy. The Fisher metric serves the first; bounded legibility the
second; the communicative-act account the third. This fits [CLAIM-223](CLAIM-223.md)'s
division of labour: what a receiver can recover fixes survival, and what an
analyst can identify fixes what can be certified. Fisher information
belongs to the analyst's side.

**Singularity.** Different internal organizations often produce the same
responses: the parameter-to-distribution map is not one-to-one in latent
and overparameterized models. The regular Bayesian penalty (d/2) log n
then gives way to λ log n − (m − 1) log log n, with λ the real log
canonical threshold and m its multiplicity ([THEORY-087](../theory.d/THEORY-087.md)). [CASE-tmpj2xb7](../cases.d/CASE-tmpj2xb7.md) is
the smallest communicative reading: Y ∼ N(ab, 1), with a the strength of an
attempted influence and b the receiver's responsiveness. "No attempt,
responsive receiver" and "attempt, unresponsive receiver" give the same
response; λ = ½ and m = 2 rather than d/2 = 1. Ordinary probes do not
separate them, and changing b with a held fixed does ([CLAIM-407](CLAIM-407.md)).

## What it does not say

- That statistical singularity shows two parameter settings to be
  different communicative kinds. That needs an independent account of the
  act ([CLAIM-150](CLAIM-150.md): identification is not constitution).
- That resolving the singularity adds observations ([CLAIM-305](CLAIM-305.md)).
- That the information-geometric reading has been applied to any
  communicative data. [CASE-055](../cases.d/CASE-055.md)'s proposed fidelity study is where it would
  be, with a singular-aware comparison in place of the regular BIC.
