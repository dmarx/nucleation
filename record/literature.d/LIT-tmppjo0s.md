---
status: Active
status_note: 'read 2026-10-23 ([NOTE-tmpj1twd](../notes.d/NOTE-tmpj1twd.md)): in full, from the authors'' accepted manuscript in Ghent University''s repository (biblio.ugent.be 8560097). Worth reading as the one study here that tests whether appraisal acts on the other emotion components linearly. It re-analyses the GRID data, culturally shared semantic profiles of 24 emotion words rated in 34 samples from 27 countries. It fits multivariate adaptive regression splines from seven appraisal factors to eleven motivation, physiology and expression factors. Goal compatibility is the main effect. Agency and norm compatibility act only in interactions, and some responses need splines. Its "threshold effects" are hinges in a continuous piecewise-linear fit. The data are word meanings, not episodes, and have no time, so they cannot bear on continuity or hysteresis in choice.'
title: 'Interaction and threshold effects of appraisal on componential patterns of emotion: A study using cross-cultural semantic data'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: the authors' accepted manuscript ("not the copy of
    record", revision of 4 March 2018, 45 pp.), Ghent University Academic
    Bibliography 8560097, linked by OpenAlex as open access. Page
    references are the manuscript's; the published article is Emotion
    19(3):425–442. Figures were seen only as captions, and Table 1 in
    extraction. The supplementary tables were not read. Details checked
    against Crossref (DOI 10.1037/emo0000449): Ben Meuleman, Agnes
    Moors, Johnny Fontaine, Olivier Renaud, Klaus Scherer, Emotion
    19(3):425–442, April 2019, online 7 June 2018. `published:` is the
    first of the issue month, Crossref giving no day. The KU Leuven Lirias
    copy reset the connection. Not checked against the Anthology of the
    SOTA. Quotations checked by script against the extracted text.
tags:
- emotion-and-affect
- psychometrics
date: '2026-10-23'
published: '2019-04-01'
doi: '10.1037/emo0000449'
url: 'https://biblio.ugent.be/publication/8560097'
first_author: 'Meuleman'
keywords:
- 'appraisal'
- 'component process model'
- 'GRID'
- 'multivariate adaptive regression splines'
- 'appraisal interactions'
- 'threshold effects'
- 'semantic profiles'
implementations: []
summary: >-
  Meuleman, Moors, Fontaine, Renaud & Scherer (2019), Emotion 19:425–442.
  Re-analyses the GRID cross-cultural data on the meaning of 24 emotion
  words (34 samples, 27 countries) to test whether appraisal acts on
  motivation, physiology and expression through interactions and
  nonlinear effects. PCA reduces items to 7 appraisal and 11 response
  factors. Multivariate adaptive regression splines (MARS) select
  third-order interactions and hinges. Goal compatibility is the main
  effect, agency and norm compatibility pure modifiers. The strong
  hierarchy of appraisal decision trees is not found. Simulated patterns
  matched to words form a coherent map.
---
<!-- inactive-ok-file: CLAIM-tmp83ge2 — Proposed; the continuity claim this reading was checked against -->
<!-- inactive-ok-file: NOTE-tmpj1twd — draft filed in the same tranche -->

# LIT-tmppjo0s: Interaction and threshold effects of appraisal on componential patterns of emotion: A study using cross-cultural semantic data

Ben Meuleman, Agnes Moors, Johnny Fontaine, Olivier Renaud & Klaus R.
Scherer (2019), *Emotion* 19(3):425–442 — DOI-10.1037/emo0000449

## Key takeaways

- **The target** (abstract, ms p. 3). Appraisal research has mostly fitted
  linear effects of appraisal on feelings, but "a linear model is not
  compatible with the idea held by many appraisal theorists that appraisal
  criteria interact to produce emotional responding."
- **The data** (§2.1). In the GRID study 4,948 respondents "rated the
  typicality of 144 items for 24 common emotion words" (ms p. 16): how
  likely, when a speaker uses the word, is each appraisal, action
  tendency, bodily change or expression. Averaged by sample and word,
  this gives 816 cases. These are semantic profiles, not episodes.
- **The model** (§2.2). PCA gives 7 orthogonal appraisal factors and 11
  oblique response factors. MARS fits them jointly with piecewise-linear
  hinges and automatically selected interactions.
- **Results** (§3.2, §4). Third-order interactions were selected. Goal
  compatibility is the main effect throughout. Agency and norm
  compatibility "appeared exclusively in interactions, without having a
  corresponding main effect" (ms p. 34). Explained variance (cross-validated)
  runs from 89.0% (appetitive vs defensive) to 7.3% (intervention vs
  disengagement). Arousal, temperature, jaw drop and vocal energy are
  fitted as well by a linear additive model.
- **Hierarchy only in part** (ms p. 34). "Nevertheless, the strong
  hierarchical interactivity proposed by Roseman (2001) and Scherer (2001)
  could not be substantiated." Instead "models were found to be partly
  additive and partly hierarchical."
- **Thresholds** (ms p. 34). "In some cases the spline effects suggested
  that an appraisal criterion must reach a certain threshold value before
  it can affect emotional responding", and in others a slope reverses at
  the hinge.
- **No time** (ms p. 38). "A second limitation of the current study is the
  omission of time from our emotion model."

## Standing in the record

Filed on 2026-10-23 and read against two of the record's questions, as
set out in [NOTE-tmpj1twd](../notes.d/NOTE-tmpj1twd.md). It gives no measure of component
synchronization; "synchronization" appears only in its review of
Scherer. Its threshold effects do not bear on [CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md)'s
continuous-versus-threshold contrast. They are kinks in a continuous
fitted function, MARS cannot represent a jump, and the inputs are
appraisals of word meanings, not costs and resources traded in choice.
What it does show is that in emotion knowledge an additive structure
and a gated one (pure modifiers) coexist in one mapping.

It concerns emotion psychology and uses machine-learning regression as a
tool. It is not an instruction for machine-learning practice.
