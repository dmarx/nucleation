---
number: 450
status: Proposed
formerly:
- CLAIM-tmprfgwn
title: 'Three standards for a communicative distinction come apart: statistical distinguishability of an interpreter''s response profiles, measured locally by the Fisher metric and never raised by a parameter-independent garbling; usability by a bounded receiver, which a transformation can raise; and pragmatic efficacy in the act; and where response models are singular, as Watanabe''s theory treats, a missing response can come from an absent attempt or an unresponsive receiver alike, and only intervention or later dynamics separate them'
version: 4
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: the garbling inequality applied to authority shares
    (CASE-159), and information design set against efficacy. The claim
    is unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Rests on CLAIM-220 in place of CLAIM-115, which it superseded.
    This claim needs only that survival is fixed by what receivers can
    recover, which CLAIM-220 keeps.
- version: 4
  date: '2026-10-29'
  note: >-
    No longer rests on CLAIM-220. Version 3 said this claim needs only
    that survival is fixed by what receivers can recover; CLAIM-223,
    on which it already rests, states that, and CLAIM-220's comparison
    of predictors, which waits on CASE-055, is not used here. Version
    3's rests_on read: CLAIM-199, CLAIM-223, CLAIM-220. The claim is
    unchanged.
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
- CLAIM-223
complements:
- CLAIM-336
- CLAIM-407
- CLAIM-150
- CLAIM-305
grounds:
- THEORY-082
- THEORY-087
- CASE-152
summary: >-
  The owner's, 2026-10-24, after setting aside the belief–knowledge
  distinction: "forget about that distinction then and let's connect back
  to the communicative act stuff and amari/watanabe theory". Worked through
  the same day (workbench entry of 2026-10-24, U27). Amari's geometry and
  Watanabe's singular learning are given different jobs in one modelling
  architecture, alongside bounded legibility and the communicative-act
  account, rather than read as rival characterizations.
illustrated_by:
- CASE-152
- CASE-159
---
<!-- inactive-ok-file: THEORY-665 — Proposed; cited in the note of 2026-10-25, nothing here rests on their being settled -->

# CLAIM-450: Three standards for a communicative distinction come apart: statistical distinguishability of an interpreter's response profiles, measured locally by the Fisher metric and never raised by a parameter-independent garbling; usability by a bounded receiver, which a transformation can raise; and pragmatic efficacy in the act; and where response models are singular, as Watanabe's theory treats, a missing response can come from an absent attempt or an unresponsive receiver alike, and only intervention or later dynamics separate them

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
canonical threshold and m its multiplicity ([THEORY-087](../theory.d/THEORY-087.md)). [CASE-152](../cases.d/CASE-152.md) is
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

## Note of 2026-10-25: information design is not efficacy

From A29, A30 and A31 of the exchange of 2026-10-24, continued.

- **Garbling applied to authority.** When an organization's response is
  the authority-weighted mixture of its processes', this claim's garbling
  inequality bounds what responses can say about the shares: the response
  metric is the pullback of the metric on the shares and never exceeds it
  ([CASE-159](../cases.d/CASE-159.md)).
- **Information design against efficacy.** Information design
  ([THEORY-844](../theory.d/THEORY-844.md)) characterizes what can be induced by controlling what
  participants learn, with incentives and standing held fixed. This
  claim's third standard, efficacy, concerns acts that change standing,
  commitments or rules. A30: "A speaker can persuade someone to volunteer,
  or can acquire authority to assign them a duty. The observed behavior
  might be identical. But an intervention challenging the speaker's
  standing could separate the mechanisms," and "Observing someone comply
  with a statement is not sufficient evidence that the statement
  constituted an authoritative command." A31's proposed test is the same
  utterance ("I'll submit the report tomorrow") as a prediction or as an
  accepted commitment, with actual and told role crossed ([CLAIM-130](CLAIM-130.md)),
  scored on held-out responses to withdrawal, role transfer and
  repudiation. Brandom's scorekeeping ([THEORY-665](../theory.d/THEORY-665.md)) is the normative state
  such a test needs. A31: "the simulation designer has to stipulate which
  procedures generate which commitments."

The claim is unchanged.
