---
status: Read
paper: 'LIT-tmpmubrk'
title: 'Informative communication in word production and word learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the authors' posted copy (langcog.stanford.edu,
    FGLT-cogsci2009.pdf, 6 pages, dated 1 February 2009 in the PDF
    metadata), extracted with pdftotext: abstract, introduction, the
    framework section with Equations 4–12, Experiments 1 and 2, general
    discussion, acknowledgements and references. Figures 2 and 4 lost
    their layout in extraction and were followed from the captions and
    the prose. The derivations of Equations 8–10 and 12 were checked by
    hand. The proceedings typeset version (pp. 1228–1233) was not seen;
    the posted copy is the authors' camera-ready-era file and may differ
    in small ways.
date: '2026-10-09'
summary: >-
  Writes the informative speaker down: utility is −D_KL(intended meaning
  ‖ literal word meaning), so a speaker referring to one object picks a
  true word with probability ∝ |extension|^(−α), the size principle from
  communicative premises. Learners who know the referent and invert this
  speaker bet on novel-word meanings as predicted (r = .93); speakers'
  free descriptions follow informativeness only weakly (r = .19), and
  colour terms not at all.
---

<!-- inactive-ok-file: THEORY-tmprknoj — Proposed; the account this reading bears on, discussed not leaned on -->

# NOTE-tmpiudi2: Informative communication in word production and word learning

## Contribution

It gives the Gricean maxim of quantity a formal, quantitative form for
simple reference: a speaker's utility is the negative KL divergence from her
intended meaning to the literal meaning of the word she chooses. Inverting
that speaker gives a learner who can infer what a novel word means from the
context it was used in. Two experiments test the two sides: learners'
graded judgements (well fit) and speakers' free productions (weakly fit).

## Key insight

A word is informative to the degree that it narrows the context to the
intended object. If speakers choose words that way, the choice of word is
itself evidence. A learner who sees a speaker point at the one red circle
among blue shapes and say "lipfy" should lean towards "red", because "red"
singles the object out and "circular" does not. The size principle, which
had been justified as a rule about generalisation, here becomes a
consequence of the speaker's goal.

## Assumptions

- A fixed context C of objects. Meanings are distributions over C.
- Words have Boolean, truth-functional meanings. A word's literal meaning
  w̃_C is uniform over its extension and 0 elsewhere (Eq. 4).
- The speaker soft-maximises U(w; M_S, C) = −D_KL(M_S ‖ w̃_C) + F with
  decision noise α (Eqs. 5–6). α = 1 and F = 0 throughout the model
  predictions.
- The intended meaning is a point mass on the referent in both
  experiments. The framework allows vague meanings, but they are not
  tested.
- The learner knows the referent (ostensive learning), and in Eq. 12 there
  are exactly two candidate lexicons with a uniform prior.

## Key results

- **Eq. 8–10.** For M_S = δ_{o_S}, D_KL(M_S ‖ w̃_C) = −log w̃_C(o_S) =
  log |w|. So P(w | M_S, C) = |w|^(−α) / Σ_{w′ true of o_S} |w′|^(−α) over
  the true words, and 0 for words false of the referent.
- **Eq. 12.** For two features and two candidate lexicons,
  P(L₁ | w₁, M_S, C) = |f₁|⁻¹ / (|f₁|⁻¹ + |f₂|⁻¹). In the Figure 1 display
  (one red object, two circles) this gives 2/3.
- **Experiment 1.** 700 participants from MIT mailing lists, three trials
  each, six objects varying on two binary dimensions. They split $100
  between the two features the novel word could name. Mean bets against
  model predictions: Pearson r = .93, Spearman .92, p < .0001. Bets were
  near $50 on the diagonal (equal counts), and the Figure 1 case gave $70
  against a predicted $67.
- **Experiment 2.** 44 participants saw all 304 superball photos, then
  wrote descriptions of 50 so that someone could pick each out, about ten
  descriptions per ball. Each description was treated as a bag of words.
  Tag-words never used for a ball were excluded. The probability of using a
  tag-word against Eq. 10's prediction: r = .19 (p < .0001), r = .02 for
  basic colour terms (p = .63), r = .51 for the rest. A word-frequency
  estimate of F from Google Images moves these to .22 and .52.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Minimising KL from intended to literal meaning yields, for a single referent, word choice ∝ \|extension\|^(−α) | strong (derivation) | Eqs. 7–10 |
| C2 | Learners inferring a novel word's meaning from a known referent behave as if inverting such a speaker | moderate | Experiment 1: r = .93 on condition means, one-shot web survey, no competing model fitted |
| C3 | Speakers' word choice in free description is related to informativeness | weak | Experiment 2: r = .19 overall, .51 excluding colour terms; tags not chosen for this task |
| C4 | Colour-term use fails because of how well a colour applies to the object, not production cost | weak (conjecture) | Experiment 2 discussion; adding a frequency proxy for F barely changes the fit |
| C5 | The framework can handle scalar implicature, anaphora and other phenomena | not supported here | general discussion; no such case is modelled |

## Method

The model is a one-step speaker, P(w | M_S, C) ∝ exp(−α D_KL(M_S ‖ w̃_C)),
inverted once by Bayes' rule for a learner who knows M_S and is uncertain
about the lexicon. The predictions in Experiment 1 have no free parameters
(α = 1, uniform prior). Experiment 2 applies Eq. 10 to the ball's tags,
read as its features, with extensions counted over the whole 304-photo set.

## Concepts

- **meaning**: a probability distribution over the objects in the context.
- **literal meaning of a word (w̃_C)**: uniform over the word's extension
  in C.
- **informativeness**: the negative KL divergence from the intended meaning
  to the word's literal meaning, i.e. the information about the intended
  meaning that the word fails to carry.
- **F**: a residual term in the utility for other factors, such as
  utterance complexity. It is set to 0 in the model and estimated from
  word frequency in one post-hoc analysis.
- **ostensive learning**: learning where the referent is known and only
  the word's meaning is inferred.

## Connections

It builds on Grice's maxim of quantity, Sperber and Wilson's relevance and
Clark's common ground, and gives them a formal analogue. The size principle
it re-derives is Shepard's (1987), as used by Tenenbaum and Griffiths
(2002) and Xu and Tenenbaum (2007). It cites Shafto and Goodman's
pedagogical sampling (2008) as the teacher's side of the same idea. The
authors place it next to game-theoretic pragmatics (Benz, Jäger and van
Rooij 2005) and distinguish it by having no recursion. Their companion
word-learning model (cited "in press", now [LIT-tmpgto9c](../literature.d/LIT-tmpgto9c.md)) handles the case
where the referent is also unknown.

## Bearing on the record

- **[THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md).** That account (listeners invert an informative
  speaker, so a fixed form's interpretation depends on the alternatives)
  is sourced from Frank and Goodman 2012, Bergen, Goodman and Levy 2012
  and Goodman and Frank 2016. This paper is its precursor and supports
  it in a neighbouring form: the inference is about the lexicon, given
  the referent, not about the referent. Experiment 1's r = .93 is again a
  correlation of condition means with a parameter-free model, which is
  exactly the kind of evidence that THEORY's `promote_when` says cannot
  settle it. It adds support, not promotion.
- **On the speaker side.** [THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md) explicitly does not say speakers
  are rational. Experiment 2 is the record's only direct test of
  production, and it shows a weak relation that fails for colour terms.
  It does not warrant a THEORY of its own: one corpus of tags, chosen by a
  photo owner, a bag-of-words scoring and a post-hoc account of the
  failure.
- **On the LIT for the Psychological Science paper.** [LIT-tmpgto9c](../literature.d/LIT-tmpgto9c.md)'s status
  note says that RSA work cites this paper, not that one, for the
  informative speaker. This reading confirms it: the informative speaker is
  here (Eqs. 5–10), and the *Psychological Science* paper has none.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Single-referent intended meanings only, with Boolean word meanings and
  uniform literal distributions. The framework's claimed generality is
  not exercised.
- Experiment 1 tests condition means against one model with no
  alternative model fitted. The histograms in Figure 2 show wide spread
  within conditions, which the mean fit does not address.
- Experiment 2's "features" are an album owner's tags. Extensions are
  counted over all 304 photos, though participants described each ball
  alone. The bag-of-words scoring ignores what a description was about.
- The fit in Experiment 2 is weak, and the explanation for colour terms is
  not tested.
- α is fixed at 1 rather than estimated.

## Open questions

- Does a model with estimated α and a cost term, fitted on part of the data
  and tested on the rest, predict production better than frequency alone?
- Does the learner's inference survive when the referent is uncertain? The
  companion model treats that case, but without an informative speaker.
- Can the KL formulation with non-uniform literal meanings, or vague
  intended meanings, separate this account from a plain size-principle
  learner? Here the two coincide by construction.
