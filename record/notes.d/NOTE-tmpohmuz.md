---
status: Read
paper: LIT-tmpkwn2g
title: 'Predicting pragmatic reasoning in language games'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from Noah Goodman's posted author manuscript
    (web.stanford.edu/~ngoodman/papers/FrankGoodman-Science2012.pdf, 10
    pages): the online abstract, the Brevia text, its ten references, the
    figure and its legend, and the Supplementary Materials (Materials and
    Methods; Supplementary Text with the model derivation, Eqs. S1–S4).
    The derivation S1–S4 was followed and its reduction to Eq. 2 checked.
    The figure's panels were read from the extracted text and the legend,
    so individual data points were not inspected.
date: '2026-10-09'
summary: >-
  A listener who inverts, by Bayes' rule, a speaker choosing words by
  informativeness to a literal listener, combined with an empirically
  measured salience prior, predicts mean listener bets in simple
  three-object reference games at r = .99 with no fitted parameters, and
  the speaker model predicts speaker bets at r = .98.
---
<!-- inactive-ok-file: THEORY-tmprknoj — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# NOTE-tmpohmuz: Predicting pragmatic reasoning in language games

## Contribution

Gricean, relevance-theoretic and common-ground accounts explained
communicative inference informally. This paper gives a model with no
fitted parameters that predicts graded human judgements in a controlled
reference game: an informative speaker, defined from surprisal under a
literal listener, and a Bayesian listener who inverts that speaker with a
measured prior. It separates the two ingredients experimentally, by
collecting speaker, salience and listener judgements in different groups.

## Key insight

Interpretation is inference about why the speaker chose this word rather
than another word that was also true of the referent. If the speaker
prefers words that pick out fewer objects, a word true of several objects
is evidence for the one that has no more specific word available.

## Assumptions

- **Shared context and vocabulary.** C = {o₁, …, o_n}; each word is a
  Boolean function on objects, shared by speaker and listener.
- **Rational speaker.** P(w|r_S, C) ∝ exp(α U(w; r_S, C)) with
  U = I(w; r_S, C) − D(w); α = 1 (Luce choice); cost D(w) constant,
  because the words are randomized and roughly matched.
- **Informativeness as negative surprisal** under the literal listener
  w̃_C, uniform over objects the word is true of: I = log w̃_C(r_S) =
  −log|w|.
- **Prior as salience**, measured empirically by asking a separate group
  which object a speaker using an unknown word meant.
- **One step of recursion**: the listener reasons about a speaker who
  reasons about a literal listener.

## Key results

- **Eq. 1.** P(r_S|w, C) = P(w|r_S, C)P(r_S) / Σ_{r′∈C} P(w|r′, C)P(r′).
- **Eq. 2 / S4.** P(w|r_S, C) = |w|⁻¹ / Σ_{w′ true of r_S} |w′|⁻¹, the size
  principle of Xu and Tenenbaum. Checked: exp(−(−log|w|⁻¹)) = |w|⁻¹.
- **Design.** Three objects, each with a colour, shape and texture; two
  dimensions vary, one is constant; the number of objects sharing each
  of the target's two values (1, 2 or 3) gives seven context types (two
  distinct 2/2 types). 50 random trials per numerical condition per
  group; one trial per participant after a manipulation check.
- **Fits.** Speaker r = .98 (p < .001); listener r = .99 (p < .0001),
  r = .87 without the 0 and 100 predictions; salience vs listener r = .19
  (p = .40).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Speakers' word choices in these games follow choice in proportion to specificity | strong (for these games) | speaker condition, r = .98 over context-type means |
| C2 | Listeners' interpretations follow the Bayesian inversion of that speaker with a measured salience prior | strong (for these games) | listener condition, r = .99; r = .87 excluding 0/100 |
| C3 | Neither prior nor likelihood alone explains listeners; their combination does | moderate | salience–listener r = .19; a likelihood-only comparison is not reported |
| C4 | Information-theoretic informativeness plus measured common knowledge can capture pragmatic inference in context generally | weak | the authors' concluding suggestion; one game type |

## Method

Model derivation in the Supplementary Text: speaker choice by softmax of
utility (S1), utility as informativeness minus cost (S2), literal
listener (S3), giving S4, which reduces to Eq. 2. Listener predictions
multiply measured salience by S4 and normalize. Participants bet $100
across options; mean bets per term or object per context type are
correlated with model predictions.

## Concepts

- **contextual salience**: the prior probability that an object would be
  referred to, standing for perceptual, social and conversational
  common ground; measured, not computed.
- **informativeness**: negative surprisal of the intended referent under
  the literal interpretation of the word.
- **size principle**: a word's likelihood is inversely proportional to the
  number of objects it applies to.
- **language game**: Wittgenstein's term, used here for one-shot
  reference games.

## Connections

The authors place it after Rosenberg and Cohen's disambiguation models,
game-theoretic signalling models (Benz, Jäger and van Rooij), and Dale and
Reiter's generation of referring expressions; the size principle is Xu
and Tenenbaum's. The general framework it starts is surveyed in Goodman
and Frank ([LIT-tmphavsf](../literature.d/LIT-tmphavsf.md)) as the rational speech act model, and Bergen,
Goodman and Levy ([LIT-tmpcsywp](../literature.d/LIT-tmpcsywp.md)) extend the same recursion with costs and
lexical uncertainty.

## Bearing on the record

- **Produces, with [LIT-tmpcsywp](../literature.d/LIT-tmpcsywp.md) and [LIT-tmphavsf](../literature.d/LIT-tmphavsf.md), [THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md)**: that
  interpretation in reference games is predicted by inverting an
  informative speaker, so it depends on the alternatives the speaker had.
- The listener's output is a posterior over referents given an utterance
  and a context: a distribution over what was meant, not a single
  meaning. That is the formal object the record would need for any
  account of a text as supporting a distribution over situations.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Correlations are over a small number of aggregated points (terms and
  objects by context type), several at 0 or 100 by construction; the
  r = .87 with those removed is the more telling number.
- Speaker, salience and listener judgements come from different people,
  and no pair communicates; the listener is asked to imagine a speaker.
- The words are single features of artificial objects, chosen so that
  cost can be taken as constant; no natural-language alternatives.
- α = 1 is set, not tested; the absence of free parameters depends on it
  and on the measured prior.
- No comparison model (likelihood only, literal listener with prior) is
  reported.

## Open questions

- Does the fit hold for listeners who must infer the speaker's
  alternatives rather than being shown them?
- Does it hold with deeper recursion or a fitted α? Goodman and Frank
  ([LIT-tmphavsf](../literature.d/LIT-tmphavsf.md)) report that deeper recursion is seen in only some
  participants.
- The 2021 reanalysis by Sikos et al. (not held, not read) bears on how
  robust the fit is.
