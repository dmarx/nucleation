---
number: 472
status: Active
formerly:
- THEORY-tmp99ydy
title: 'A speaker who chooses words to minimise the information lost about a single intended referent, with words'' literal meanings uniform over their extensions, picks each true word with probability inversely proportional to a power of its extension, so the size principle follows from informative communication; in one betting experiment, learners who knew the referent bet on a novel word''s meaning in line with the inversion of that speaker (r = .93 on condition means), and in one free-description study speakers'' word use followed it only weakly (r = .19)'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-472 (batch 025, ADR-047 v2 for the derivation, v3 for the
    experiments). The derivation is re-derived in the decision file. NOTE-627
    read the paper in full, and the title's numbers are in its text. The
    title now names the uniform-literal-meaning assumption and the two
    studies. The promote_when asked for an experiment that discriminates
    between an informative-speaker learner and a plain size-principle
    learner, which tests a claim the body disclaims. It moves unchanged to
    QUESTION-167.
tags:
- pragmatics
- cognition
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-824
summary: >-
  Frank, Goodman, Lai and Tenenbaum (2009), [LIT-824](../literature.d/LIT-824.md), read in full in
  [NOTE-627](../notes.d/NOTE-627.md). The derivation (utility −D_KL from intended to literal
  meaning gives P(w) ∝ |w|^(−α) for a point referent) is a proof under its
  assumptions. Learners' bets track the parameter-free inversion at
  r = .93 on condition means (700 web participants); speakers' tag-word use
  in free descriptions correlates at r = .19, .51 without colour terms and
  .02 for them. In these displays the informative-speaker learner and a
  plain size-principle learner coincide by construction, so the fit does
  not show that learners reason about the speaker.
extended_by:
- THEORY-172
---
<!-- inactive-ok-file: LIT-1041 — Unavailable; Grice 1975, read only at pp. 45–47, named as the informal ancestor and not leaned on -->
<!-- inactive-ok-file: THEORY-172 — Proposed; the rational-speech-act account this one is set beside, not leaned on -->

# THEORY-472: A speaker who chooses words to minimise the information lost about a single intended referent, with words' literal meanings uniform over their extensions, picks each true word with probability inversely proportional to a power of its extension, so the size principle follows from informative communication; in one betting experiment, learners who knew the referent bet on a novel word's meaning in line with the inversion of that speaker (r = .93 on condition means), and in one free-description study speakers' word use followed it only weakly (r = .19)

## Source

Frank, Goodman, Lai and Tenenbaum (2009), [LIT-824](../literature.d/LIT-824.md) (Proceedings of CogSci
31, pp. 1228–1233), read in full in [NOTE-627](../notes.d/NOTE-627.md) from the authors' posted
copy. The derivations of Eqs. 8–10 and 12 were checked by hand.

## What was actually shown

**The speaker (Eqs. 4–6).** Meanings are distributions over the objects in
a context C. A word's literal meaning w̃_C is uniform over its extension.
The speaker chooses w with P(w | M_S, C) ∝ exp(α U), where
U = −D_KL(M_S ‖ w̃_C) + F, and F (other costs) is 0 here.

**The size principle (Eqs. 8–10; C1, a derivation).** If the intended
meaning is a point mass on the referent, D_KL(M_S ‖ w̃_C) = log |w|, so
P(w | M_S, C) = |w|^(−α) / Σ |w′|^(−α) over the words true of the
referent, and 0 for false ones.

**The learner (Eq. 12).** A learner who knows the referent, with two
features and two candidate lexicons under a uniform prior, infers that the
word names f₁ with probability |f₁|⁻¹ / (|f₁|⁻¹ + |f₂|⁻¹): 2/3 for "red"
in the display with one red object and two circles.

**Experiment 1 (C2, moderate).** 700 participants from MIT mailing lists
split $100 between two candidate meanings of a novel word across
six-object displays. Mean bets against the parameter-free model (α = 1):
Pearson r = .93, Spearman .92. Bets sat near $50 when the features were
equally frequent, and the Figure 1 case gave $70 against a predicted $67.

**Experiment 2 (C3, weak).** 44 participants wrote descriptions of 50 of
304 Flickr superball photos so that someone could pick each out. Use of a
ball's tag-words against Eq. 10: r = .19 overall, .51 without basic colour
terms, .02 for colour terms alone (p = .63). A Google-Images frequency
estimate of F moves these to .22 and .52.

**What could have come out otherwise.** Bets could have ignored feature
frequency, and speakers could have used words with no relation to their
extension. The first did not happen. The second nearly did for colour
terms.

## What this does not say

- **That learners reason about the speaker.** With point referents and
  uniform literal meanings, the informative-speaker learner and a plain
  size-principle learner make the same predictions "by construction"
  ([NOTE-627](../notes.d/NOTE-627.md), Open questions). Experiment 1 fits both. No competing model
  was fitted, and the within-condition spread in Figure 2 is not
  addressed.
- **That speakers are informative.** Experiment 2 is the record's only
  test of production on this model, and it is weak: one album owner's
  tags as features, extensions counted over all 304 photos though each
  ball was described alone, bag-of-words scoring, and a post-hoc account
  of the colour failure (C4, a conjecture).
- **Anything about listeners inferring a referent.** There is one speaker
  and a learner who inverts it once, with the referent given. The
  listener who infers a referent, and the recursion, are Frank and
  Goodman 2012 ([LIT-821](../literature.d/LIT-821.md)) and the papers behind [THEORY-172](THEORY-172.md).
- **That the framework covers implicature or anaphora.** Claimed in the
  discussion (C5), not modelled.

## Connections

- **[THEORY-172](THEORY-172.md)** (listeners invert an informative speaker, so a fixed
  form's interpretation depends on the alternatives) is the later and
  wider account. This is its precursor, in the word-learning form: the
  lexicon is inferred given the referent. Experiment 1's evidence is of
  the kind that THEORY's `promote_when` says cannot settle it. [THEORY-172](THEORY-172.md)
  `extends` this account: the same mechanism, widened from the lexicon to
  the referent. It does not cite this paper among its sources.
- Grice's maxim of Quantity ([LIT-1041](../literature.d/LIT-1041.md), read only at pp. 45–47) is the
  informal ancestor the paper names. Grice himself calls the second
  Quantity maxim "disputable".
- The companion *Psychological Science* paper ([LIT-815](../literature.d/LIT-815.md)) infers referential
  intentions and has no informative speaker. [NOTE-627](../notes.d/NOTE-627.md) confirms that RSA
  work cites this paper, not that one, for the informative speaker.
