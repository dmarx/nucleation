---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp8z8c5](../notes.d/NOTE-tmp8z8c5.md)); worth reading as the model in which a word learner infers the speaker''s referential intention and the lexicon jointly: words are generated from an unobserved intended referent (a subset of the objects present, possibly empty) through the lexicon, or non-referentially, and the MAP lexicon is found by search. On two ten-minute CHILDES videos it learns a far more precise lexicon than association and translation baselines (F .55 against at most .22), and it reproduces mutual exclusivity, Xu''s word-driven object individuation and Baldwin''s intention-reading result. Read it as a word-learning paper: it has no model of an informative speaker; Bergen, Goodman and Levy (2012) cite a different 2009 paper, by Frank, Goodman, Lai and Tenenbaum, for that.'
title: 'Using Speakers'' Referential Intentions to Model Early Cross-Situational Word Learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmp8z8c5) from the authors' posted
    copy of the typeset article (langcog.stanford.edu, Frank's lab, 8
    pages, Psychological Science 20(5):578–585). The online supporting
    information (technical appendix, model code) was not read. Details
    checked against Crossref (Psychological Science 20(5):578–585; online
    1 May 2009, print May 2009) and PubMed (PMID 19389131). No arXiv
    version. `published:` is 1 May 2009, the earliest full date Crossref
    gives. Identity checked: this is the 2009 Frank, Goodman and Tenenbaum
    paper (Crossref and PubMed agree on title, authors and venue). The
    2009 CogSci paper by Frank, Goodman, Lai and Tenenbaum, which RSA work
    cites for the informative speaker, is a different work. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone of 2026-10-09, commit d8b5ba5) for the authors, the
    DOI and the title found nothing.
tags:
- cognition
- linguistics
- probabilistic-modeling
date: '2026-10-09'
published: '2009-05-01'
doi: '10.1111/j.1467-9280.2009.02335.x'
first_author: 'Frank'
keywords:
- 'word learning'
- 'cross-situational learning'
- 'referential intentions'
- 'mutual exclusivity'
- 'Bayesian modeling'
implementations: []
summary: >-
  Frank, Goodman & Tenenbaum (2009), Psychological Science
  20(5):578–585. A Bayesian word learner that infers the speaker's
  intended referents and the lexicon together, with words uttered
  referentially or not, beats association and IBM Model 1 baselines on
  hand-annotated child-directed video (lexicon precision .67, F .55) and
  predicts mutual exclusivity, one-trial learning, word-driven object
  individuation and intention-guided mapping without principles built in
  for them.
---

# LIT-tmpgto9c: Using Speakers' Referential Intentions to Model Early Cross-Situational Word Learning

Michael C. Frank, Noah D. Goodman and Joshua B. Tenenbaum (2009),
*Psychological Science* 20(5):578–585 — DOI-10.1111/j.1467-9280.2009.02335.x

## Key takeaways

- **Joint inference.** The corpus is a set of situations, each with the
  objects present O, an unobserved intention I ⊆ O (possibly empty) and
  the words W. P(L|C) ∝ P(C|L)P(L), with P(L) ∝ e^(−α|L|) and
  P(W|I,L) = Π_w [γ Σ_{o∈I} P_R(w|o,L)/|I| + (1 − γ) P_NR(w|L)]. A word
  is referential (chosen uniformly among the lexicon's words for an
  intended object) or not (drawn from the vocabulary, with lexicon words
  down-weighted by κ).
- **Corpus result.** On two CHILDES Rollins videos, annotated by the
  authors, the MAP lexicon has precision .67, recall .47, F .55; the best
  baseline (IBM Model 1, word|object) reaches F .22. The intentions
  inferred have F .58 against at most .48. The advantage holds across the
  three free parameters and when two are set by empirical Bayes.
- **Where the precision comes from.** Words can be uttered
  non-referentially, and an utterance can have an empty intention, so
  inconsistent co-occurrence is explained away rather than learned.
- **Behavioural coverage.** Mutual exclusivity emerges as a soft
  preference for one-to-one lexicons (shared with simple baselines). Xu's
  (2002) individuation result comes out as a crossover in surprisal: two
  words make two objects less surprising. Baldwin's (1993) result follows
  once the speaker's intention is given to the model; a salience model
  cannot get it.
- **Not an informative-speaker model.** The speaker here picks uniformly
  among the words linked to a referent; nothing makes her choose words to
  be informative. Bergen, Goodman and Levy ([LIT-tmpcsywp](LIT-tmpcsywp.md)) cite Frank,
  Goodman, Lai and Tenenbaum's 2009 CogSci paper, not this one, for that
  step; the Lai paper was not read.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the manuscript
bibliography of 2026-10-09 (work `what-survives-translation`): one of the
works the manuscript considered and dropped from its final reference list.

Read on 2026-10-09 ([NOTE-tmp8z8c5](../notes.d/NOTE-tmp8z8c5.md)). If the bibliography meant the paper
that founds the informative-speaker likelihood of the RSA line
([LIT-tmpkwn2g](LIT-tmpkwn2g.md), [LIT-tmphavsf](LIT-tmphavsf.md)), it is the CogSci paper with Lai, which the
record does not hold; this one is the word-learning model.
