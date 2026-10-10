---
status: Active
title: 'The distribution-over-situations criterion compares each language''s own listener posterior, so it needs no correspondence of alternative sets; that a literal rendering can fail it is the criterion detecting a lost implicature, and a target language may admit no rendering that passes'
version: 1
role: thesis
defeated_if: >-
  A case in which two target renderings induce the same target-listener
  posterior over situations, corresponding by τ_z to the source's, and are
  reliably judged to differ in fidelity because of what else a speaker
  could have said in place of each.
tags:
- pragmatics
- probabilistic-modeling
- translation
date: '2026-10-10'
line: 'pragmatic-transport'
grounds:
- THEORY-172
objects_to:
- CLAIM-tmpjuqrl
complements:
- CLAIM-111
- CLAIM-033
summary: >-
  The record's reply, on 2026-10-10, to [CLAIM-tmpjuqrl](CLAIM-tmpjuqrl.md). [CLAIM-111](CLAIM-111.md)'s
  criterion is P_o(z | c_o, u_o) ≈ P_t(τ_z(z) | c_t, u_t). On the
  rational-speech-act model each posterior is computed with its own
  language's alternatives, so comparing the posteriors needs no map
  between the alternative sets. The objection's worked case is right, and
  it shows the criterion rejecting a rendering that keeps the literal
  content and loses a scalar implicature. Active, because it is read off
  the criterion's form and checked by arithmetic. It does not say the
  model is right or that the criterion applies to poems.
---
<!-- inactive-ok-file: CLAIM-tmpjuqrl — Rejected; the objection this claim answers, cited as answered -->
<!-- inactive-ok-file: CLAIM-111 CLAIM-033 — Proposed; the criterion this claim reads and Jakobson's point it extends, cited as open, not settled -->
<!-- inactive-ok-file: THEORY-172 — Proposed; rational speech acts, cited for the form of the model, not as settled -->
<!-- inactive-ok-file: CLAIM-115 CLAIM-139 — Proposed; the central theses, cited only to say this claim is not their premise -->

# CLAIM-tmp9negs: The distribution-over-situations criterion compares each language's own listener posterior, so it needs no correspondence of alternative sets; that a literal rendering can fail it is the criterion detecting a lost implicature, and a target language may admit no rendering that passes

## The claim

This is the record's reply of 2026-10-10 to [CLAIM-tmpjuqrl](CLAIM-tmpjuqrl.md). It is decisive
and checkable: it is read off the form of [CLAIM-111](CLAIM-111.md)'s criterion, and the
arithmetic below is the objection's own, re-derived.

[CLAIM-111](CLAIM-111.md)'s criterion is P_o(z | c_o, u_o) ≈ P_t(τ_z(z) | c_t, u_t),
"where τ_z maps corresponding latent communicative frames across
linguistic environments". Each side is a listener's posterior over
situations: on the left a source-language listener's, given the source
utterance; on the right a target-language listener's, given the rendering.
On the rational-speech-act model of [THEORY-172](../theory.d/THEORY-172.md), each listener's posterior
is computed with that listener's own language's alternatives. The criterion
then compares the two posteriors through τ_z, which maps situations, not
utterances. Nothing in it maps one language's alternatives onto the
other's, and nothing needs to. The objection asked for "a rule for when a
target form with different alternatives counts as matching". The
criterion is that rule: a target form matches when its posterior matches.

## The worked case, re-derived

The objection's case: two meanings, m₁ and m₂, with a uniform prior; the
speaker's rationality α = 1, and no costs. The pragmatic speaker chooses an
utterance u for meaning m in proportion to exp(α log P_Lit(m | u)), which
with α = 1 is in proportion to P_Lit(m | u).

- **Source language**: *a* is true of m₁ and m₂; *b* is true of m₂ only.
  The literal listener gives P_Lit(m₁ | a) = P_Lit(m₂ | a) = 1/2 and
  P_Lit(m₂ | b) = 1. The speaker with m₁ has only *a*, so P_S(a | m₁) = 1.
  The speaker with m₂ weighs *a* at 1/2 and *b* at 1, so
  P_S(a | m₂) = (1/2)/(1/2 + 1) = 1/3 and P_S(b | m₂) = 2/3. The pragmatic
  listener: P_L(m₁ | a) = (1 · 1/2)/(1 · 1/2 + 1/3 · 1/2) = (1/2)/(2/3) =
  3/4.
- **Target language**: one utterance, *a′*, true of m₁ and m₂. Each speaker
  has only *a′*, so P_S(a′ | m₁) = P_S(a′ | m₂) = 1, and
  P_L(m₁ | a′) = (1 · 1/2)/(1 · 1/2 + 1 · 1/2) = 1/2.

Take τ_z as the identity on {m₁, m₂}. The criterion compares 3/4 with 1/2
and, for any tolerance smaller than 1/4, finds *a′* unfaithful to *a*. That
is the right verdict. *a* means "m₁, probably", because a speaker with m₂
had *b* and would likely have used it. *a′* keeps the literal content of
*a* and loses that scalar implicature. The objection's arithmetic stands;
what does not follow from it is that the criterion needs a further
correspondence. It shows the criterion working.

## What follows instead

**The target inventory bounds fidelity.** In this target language every
utterance gives P_L(m₁ | ·) = 1/2, because there is only one. So no
rendering of *a* passes the criterion: the target language cannot say what
the source said by implicature. That is [CLAIM-033](CLAIM-033.md)'s point from Jakobson,
"Languages differ in what they must convey", met here for what a language
*can* convey by implicature. It is a consequence of the criterion, not a gap
in it: a fidelity criterion should report that some source posteriors have
no faithful rendering in a given target.

**Alternatives matter for prediction, not for application.** To *predict*
P_t from a model, one needs the target language's alternatives, as
[THEORY-172](../theory.d/THEORY-172.md)'s model needs any language's. To *apply* the criterion one needs
only the two posteriors, which can be elicited from listeners of each
language without modelling either inventory.

**τ_z is still needed.** The criterion keeps its correspondence of
situations, and how to fix it without building in the preferred notion of
fidelity is [QUESTION-005](../questions.d/QUESTION-005.md). This reply removes only the second
correspondence the objection added.

## What it answers

[CLAIM-tmpjuqrl](CLAIM-tmpjuqrl.md), filed as granted on 2026-10-10, said that matching posteriors
across languages "needs a correspondence between source and target
alternative sets, or a rule for when a target form with different
alternatives counts as matching". The worked case is kept; the conclusion is
answered by the reading above. The objection is Rejected by this claim. Its
role stays as filed, and its history says the concession is withdrawn on
this argument.

## What it does not say

- It does not say the rational-speech-act model is right. [THEORY-172](../theory.d/THEORY-172.md) is
  "Shown for artificial games with given alternatives", and the reply uses
  the model only because the objection did.
- It does not say [THEORY-172](../theory.d/THEORY-172.md)'s evidence shows the criterion applies to
  poems, where the alternatives are neither given nor few. That paragraph
  of the objection stands.
- It does not make [CLAIM-111](CLAIM-111.md) a premise of [CLAIM-115](CLAIM-115.md) or [CLAIM-139](CLAIM-139.md); it is not
  one.
