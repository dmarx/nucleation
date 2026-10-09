---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpohmuz](../notes.d/NOTE-tmpohmuz.md)); worth reading as the one-page origin of the rational speech act model''s quantitative test: a listener who inverts, by Bayes'' rule, a speaker who chooses words in proportion to their informativeness (exp of minus surprisal under a literal listener, which reduces to the size principle |w|⁻¹), combined with an empirically measured salience prior, predicts mean listener bets in three-object reference games at r = .99 with no fitted parameters (α set to 1). Read it knowing that the fit is to means over seven context types, that the prior is measured in a separate group, and that the speaker and listener groups never interact. Source of [THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md).'
title: 'Predicting Pragmatic Reasoning in Language Games'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmpohmuz) from Noah Goodman's posted
    copy (web.stanford.edu/~ngoodman/papers/FrankGoodman-Science2012.pdf:
    the author manuscript of the one-page Brevia with its figure and the
    Supplementary Materials). The typeset Science page was not used.
    Details checked against Crossref (Science 336(6084):998, 25 May 2012)
    and PubMed (PMID 22628647). No arXiv version. `published:` is 25 May
    2012, the only full date Crossref gives. Not held in the Anthology of
    the SOTA: a grep of its record/ (clone of 2026-10-09, commit d8b5ba5)
    for the authors, the DOI and the title found nothing.
tags:
- pragmatics
- linguistics
- cognition
- probabilistic-modeling
date: '2026-10-09'
published: '2012-05-25'
doi: '10.1126/science.1218633'
first_author: 'Frank'
keywords:
- 'pragmatics'
- 'reference games'
- 'informativeness'
- 'Bayesian inference'
- 'rational speech act'
implementations: []
summary: >-
  Frank & Goodman (2012), Science 336(6084):998. In one-shot
  three-object reference games on Mechanical Turk, speakers' word bets
  match a speaker who chooses words in proportion to their specificity
  (r = .98), and listeners' referent bets match the Bayesian inversion of
  that speaker with an empirically measured salience prior (r = .99),
  though salience and listener bets alone are uncorrelated (r = .19).
  The founding quantitative test of what was later called the rational
  speech act model.
---
<!-- inactive-ok-file: THEORY-tmprknoj — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# LIT-tmpkwn2g: Predicting Pragmatic Reasoning in Language Games

Michael C. Frank and Noah D. Goodman (2012), *Science* 336(6084):998 —
DOI-10.1126/science.1218633

## Key takeaways

- **The listener.** P(r_S|w, C) ∝ P(w|r_S, C) P(r_S): the prior is
  contextual salience, measured in a separate group who bet on the
  referent of an unknown word; the likelihood is a model of the speaker.
- **The speaker.** P(w|r_S, C) ∝ exp(α U), U = log w̃_C(r_S) − D(w), with
  w̃_C the literal listener (uniform over the objects the word is true
  of). With α = 1 and constant cost this is |w|⁻¹ normalized over the true
  words: the size principle. So the model has no free parameters.
- **The data.** 745 participants (206 speaker, 276 salience, 263
  listener), one trial each, three objects varying on two of colour,
  shape and texture, seven context types.
- **The result.** Speaker bets against the model r = .98; listener bets
  against prior × likelihood r = .99, and r = .87 with predictions of 0
  and 100 removed; salience and listener bets themselves r = .19.
- **The framing.** Grice, Sperber and Wilson, and Clark give informal
  accounts; the contribution is a quantitative prediction from an
  information-theoretic informativeness plus measured common ground.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the manuscript
bibliography of 2026-10-09 (work `what-survives-translation`): one of the
works the manuscript considered and dropped from its final reference list.

Read on 2026-10-09 ([NOTE-tmpohmuz](../notes.d/NOTE-tmpohmuz.md)); with [LIT-tmpcsywp](LIT-tmpcsywp.md) and [LIT-tmphavsf](LIT-tmphavsf.md) it
is the source of [THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md). A later reanalysis exists (Sikos,
Venhuizen, Drenhaus and Crocker 2021, "Reevaluating pragmatic reasoning
in language games", PLOS ONE, DOI-10.1371/journal.pone.0248388); the
record does not hold it and it was not read.
