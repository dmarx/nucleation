---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmpb8ud3), in full, from the publisher''s PDF; worth reading as the first laboratory test of iterated learning against an inductive bias known before the experiment: in 32 chains of nine human learners each passing a function-learning task down the line, 28 converged within a few generations to a positive linear function whatever the first learner was trained on (positive linear, negative linear, U-shaped or random pairings), as Bayesian agents sampling from a prior that favours positive linear functions would. The prior was not measured in the experiment but taken from earlier function-learning studies; 3 families ended on the negative linear function and 1 did not converge, and the authors say more data would be needed to show the chains had reached a stationary distribution. Bears on THEORY-155.'
title: 'Iterated learning: Intergenerational knowledge transmission reveals inductive biases'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmpb8ud3) from the publisher's
    PDF (link.springer.com/content/pdf/10.3758/BF03194066.pdf, served
    without a login), every section, the appendix and the reference list.
    Details checked against Crossref (Psychonomic Bulletin & Review
    14(2):288–294, April 2007; authors Michael L. Kalish, Thomas L.
    Griffiths, Stephan Lewandowsky). `published:` is 1 April 2007:
    Crossref gives only the month. Not held in the Anthology of the
    SOTA: a grep of its record/ (clone of 2026-10-09, commit d8b5ba5)
    for the authors, the DOI, the title and "iterated learning" found
    nothing (its only Lewandowsky is a different paper, Bak-Coleman et
    al. 2025).
tags:
- cognition
- probabilistic-modeling
- linguistics
date: '2026-10-09'
published: '2007-04-01'
doi: '10.3758/BF03194066'
first_author: 'Kalish'
keywords:
- 'iterated learning'
- 'cultural transmission'
- 'inductive biases'
- 'function learning'
- 'serial reproduction'
- 'Bayesian inference'
implementations: []
summary: >-
  Kalish, Griffiths & Lewandowsky (2007), Psychonomic Bulletin & Review
  14(2):288–294. Human chains of function learners, each trained on the
  previous learner's test responses, converged in a few generations to a
  positive linear function in 28 of 32 families, whatever function
  trained the first learner, as Bayesian iterated learning predicts for
  a prior favouring positive linear functions. The prior was inferred
  from earlier studies, not measured; stationarity was not shown.
---

<!-- inactive-ok-file: THEORY-155 — Proposed; named as the account this experiment bears on, not settled by it -->
<!-- inactive-ok-file: LIT-768 — Deferred; named as the classical case the paper re-reads, not leaned on -->

# LIT-tmpj7bvq: Iterated learning: Intergenerational knowledge transmission reveals inductive biases

Michael L. Kalish, Thomas L. Griffiths and Stephan Lewandowsky (2007),
*Psychonomic Bulletin & Review* 14(2):288–294 — DOI-10.3758/BF03194066

## Key takeaways

- **The prediction.** If learners share a prior p(h) and each samples a
  hypothesis from the posterior given the previous learner's data, the
  chain of hypotheses is a Markov chain whose stationary distribution is
  the prior, so "the stimuli provided for learning are completely
  irrelevant in the long run" (citing Griffiths and Kalish, LIT-769). A
  simulation with Bayesian linear regression (appendix) shows the
  convergence in a few generations.
- **The test.** 288 undergraduates in four conditions; each condition
  formed eight "families" of nine generations. The first learner in each
  family was trained on 50 points from y = x, y = 101 − x, a U-shaped
  sine function or a random one-to-one pairing; each later learner was
  trained on the previous learner's 50 test responses (25 old and 25 new
  x values), without contact and without knowing their responses would
  be passed on.
- **The result.** 28 of 32 families converged within a few generations
  to a positive linear function. All eight negative-linear families, and
  three others, produced a negative linear function for at least one
  generation; three families ended on it and one did not converge. The
  median correlation with y = x rose across generations in every
  condition except the positive linear one, which was at ceiling from the
  start.
- **Where the prior came from.** The bias toward positive linear
  functions was taken from earlier function-learning studies (initial
  responses, ease of learning, a fitted model), not measured on these
  participants. The authors call the stationary distribution "apparently
  complex" and say significantly more data would be needed to confirm
  convergence and map it against prior estimates.
- **The claims drawn.** Iterated learning can be used as a method to
  reveal implicit inductive biases; and the result is said to "validate"
  serial-reproduction studies such as Bartlett's (LIT-768) as revealing
  biases, and to suggest that "languages, legends, religious concepts, and
  social norms" are tailored to them. Neither extrapolation is tested.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request: the manuscript
considered it and dropped it from the final reference list. It is read here
on its own merits. See the curation entry of that day.

Read on 2026-10-09 (NOTE-tmpb8ud3). It is the empirical companion of
Griffiths and Kalish's analysis (LIT-769) and the closest thing the record
holds to a test of THEORY-155: a human chain run against a bias stated
before the experiment. It does not meet that theory's `promote_when`,
since the prior was not measured or set independently on the learners and
stationarity was not shown. It stands beside Kirby, Cornish and Smith's
chains (LIT-771), which measured no prior at all.
