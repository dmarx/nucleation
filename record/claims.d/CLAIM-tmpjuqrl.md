---
status: Rejected
title: 'Under the rational-speech-act model the distribution-over-situations thesis grounds on, a form''s interpretation depends on what else the speaker could have said, so matching source and target posteriors needs a correspondence of alternative sets that translation changes and no entry names'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Rejected on 2026-10-10 by CLAIM-tmp9negs, and the concession made
    when it was filed as granted is withdrawn on that claim's argument.
    Its role is left as filed. The worked case stands, and the
    conclusion does not follow: CLAIM-111's criterion compares each
    language's own listener posterior, so it needs no correspondence of
    alternative sets. The case shows the criterion rejecting a literal
    rendering that loses a scalar implicature. The body below is
    unchanged.
role: granted
tags:
- pragmatics
- translation
- probabilistic-modeling
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-172
objects_to:
- CLAIM-111
summary: >-
  Found in the record's audit of the line on 2026-10-10 (empirical lens);
  no turn of the exchange raises it. [CLAIM-111](CLAIM-111.md) makes a translation
  faithful when the target's posterior over communicative situations
  matches the source's, and its worked model, [THEORY-172](../theory.d/THEORY-172.md), makes that
  posterior depend on the set of alternative utterances. A translation
  replaces the source language's alternatives with the target's, so a
  rendering with the same literal content can carry a different
  posterior. Granted, because it follows from the model as the record
  states it. It does not say the model is wrong or [CLAIM-111](CLAIM-111.md) false.
objected_by:
- CLAIM-tmp9negs
---
<!-- inactive-ok-file: CLAIM-111 — Proposed; open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: CLAIM-115 CLAIM-139 — Proposed; the central theses, cited only to say this claim is not their premise -->
<!-- inactive-ok-file: THEORY-172 — Proposed; rational speech acts, cited for the form of the model and the limits of its evidence, not as settled -->

# CLAIM-tmpjuqrl: Under the rational-speech-act model the distribution-over-situations thesis grounds on, a form's interpretation depends on what else the speaker could have said, so matching source and target posteriors needs a correspondence of alternative sets that translation changes and no entry names

## The objection

[CLAIM-111](CLAIM-111.md) (A45 §6): P_o(z | c_o, u_o) ≈ P_t(τ_z(z) | c_t, u_t), "where τ_z
maps corresponding latent communicative frames across linguistic
environments". Its defeat condition tests renderings "whose
inferred-situation posteriors match those of the source". Its worked model
is the rational-speech-act listener of [THEORY-172](../theory.d/THEORY-172.md), "a posterior over what
the speaker meant, given the utterance and its alternatives" ([CLAIM-111](CLAIM-111.md)).

[THEORY-172](../theory.d/THEORY-172.md)'s title says what that costs: "the interpretation of a fixed
form depends on what else the speaker could have said". Its model:
P_L(m|u) ∝ P_S(u|m)P(m), where P_S chooses among the utterances true of m
in proportion to exp(α[log P_Lit(m|u) − c(u)]), and P_Lit conditions the
prior on literal truth. The normalization of P_S runs over the set of
alternative utterances. A translation does not keep that set: it moves the
utterance into another language, whose alternatives are different.

**A worked case.** Two meanings, m₁ and m₂, with a uniform prior; α = 1 and
no costs.

- Source language: two utterances. *a* is true of m₁ and m₂; *b* is true of
  m₂ only. Then P_Lit(m₁|a) = P_Lit(m₂|a) = 1/2 and P_Lit(m₂|b) = 1. The
  speaker: P_S(a|m₁) = 1, since *a* is the only utterance true of m₁; and
  P_S(a|m₂) = (1/2)/(1/2 + 1) = 1/3, P_S(b|m₂) = 2/3. The listener:
  P_L(m₁|a) = (1 · 1/2)/(1 · 1/2 + 1/3 · 1/2) = 3/4.
- Target language: one utterance, *a′*, true of m₁ and m₂, with no
  counterpart of *b*. Then P_S(a′|m₁) = P_S(a′|m₂) = 1, and
  P_L(m₁|a′) = 1/2.

*a′* has exactly the literal content of *a*, and the posteriors differ, 3/4
against 1/2. This is the scalar case ("some" read as "not all" because
"all" was available). Whether a rendering matches the source's posterior
depends on the alternatives each language offers, so [CLAIM-111](CLAIM-111.md)'s τ_z,
which maps frames, is not enough: the criterion also needs a
correspondence between source and target alternative sets, or a rule for
when a target form with different alternatives counts as matching. That
is one more correspondence that has to be fixed from outside both
languages, of the kind [QUESTION-005](../questions.d/QUESTION-005.md) asks about. A search of the claims for
"alternative set" and "could have said" on 2026-10-10 finds no entry that
names it.

**The evidence.** [THEORY-172](../theory.d/THEORY-172.md) is "Shown for artificial games with given
alternatives". Its `promote_when` says what exists cannot settle it: "A
high correlation of condition means with a parameter-free model, which is
what exists, cannot settle it." So it is a worked model of [CLAIM-111](CLAIM-111.md)'s
criterion, not evidence that the criterion applies to poems, where the
alternatives are neither given nor few.

## What it does not say

It does not say the rational-speech-act model is wrong, nor that [CLAIM-111](CLAIM-111.md)
is false. It says that, on the model [CLAIM-111](CLAIM-111.md) adopts, matching posteriors
across languages needs a correspondence of alternatives that the record
has not stated. It is minor for the argument: [CLAIM-111](CLAIM-111.md) is not a premise of
[CLAIM-115](CLAIM-115.md) or [CLAIM-139](CLAIM-139.md).
