---
number: 588
status: Proposed
formerly:
- THEORY-tmpn6aoc
promote_when: >-
  An implemented non-lexicalist production model, with retrieval of stored
  pieces folded into structure building and no fixed unit of storage,
  tested against a lemma model on standard production data (speech
  errors, picture–word interference, structural priming) and on the cases
  argued here (polysynthetic words, separable idioms, object-conditioned
  suppletion). It is promoted if it matches the lemma model on the
  standard data and beats it on these cases. It is refuted if a lemma or
  treelet model with separate retrieval and building stages handles these
  cases without the implausible storage the paper predicts. Further
  verbal analyses of single phenomena, or aphasia data cited as merely
  consistent, cannot settle it.
title: "Lemma-based models of language production build in a lexicalist assumption, and the failure is algorithmic as well as representational: as long as retrieval of stored word-sized units and building of syntactic structure are separate stages, richer stored units cannot handle polysynthetic words, idioms whose parts syntax separates, or suppletion conditioned by an unplanned object"
version: 1
tags:
- linguistics
- cognition
date: '2026-10-16'
source:
- LIT-031
presupposes:
- THEORY-643
summary: >-
  Krauska and Lau (2023), [LIT-031](../literature.d/LIT-031.md), read in full in [NOTE-029](../notes.d/NOTE-029.md). A Hypothesis
  and Theory article with no new data and no implementation. Its
  diagnosis of named models (Levelt, the Consensus Model, lexically sized
  increments, treelets) is strong as textual analysis; the case that they
  fail on Inuktitut, Vietnamese collocations and Hiaki suppletion is
  argued from a few examples each, and Eberhard et al. are conceded to
  handle Hiaki in part. The 8-stage replacement model and its aphasia
  predictions are a verbal sketch, and this account does not rest on
  them.
---
<!-- inactive-ok-file: THEORY-643 — Proposed; the account this one presupposes, open, so this one is Proposed too -->
<!-- inactive-ok-file: LIT-031 — Proposed; the reading that sources this account, which is itself Proposed and says so -->

# THEORY-588: Lemma-based models of language production build in a lexicalist assumption, and the failure is algorithmic as well as representational: as long as retrieval of stored word-sized units and building of syntactic structure are separate stages, richer stored units cannot handle polysynthetic words, idioms whose parts syntax separates, or suppletion conditioned by an unplanned object

## Source

Krauska and Lau (2023), [LIT-031](../literature.d/LIT-031.md) (*Frontiers in Language Sciences* 2,
1125127, Hypothesis and Theory), read in full in [NOTE-029](../notes.d/NOTE-029.md).

## What was actually shown

**Two lexicalist assumptions (p. 2).** (1) Syntactic and morphological
processes differ in kind. (2) Lexical items are triads of sound, meaning
and syntax. A model making either counts as lexicalist, so treelet models,
which drop (1), still count by (2).

**Where the models embed them (§2; C1, strong).** Levelt's lemma and Levelt
and Indefrey (2000), the Consensus Model (Ferreira and Slevc 2007),
incremental planning in "lexically sized units", and treelets (Kempen,
Vosse and Kempen, Ferreira, Matchin and Hickok).

**Where they fail (§2.1; C2–C4, moderate).**
- *Inuktitut.* For *havauti-tuq-ti-taq-niaq-tara*, "I'm going to give her
  medicine frequently", a lemma model must either store a concept per word
  or load the "medicine" lemma with diacritics that are productive, rarely
  used and only linearly ordered, so they cannot express structure inside
  the word.
- *Vietnamese idiomatic collocations* (Noyer 1998). *nhà cửa* 'house' and
  *vườn tược*, where *tược* has no meaning alone, are single concepts whose
  parts syntax can separate. Superlemmas fail, since they require a
  literal lemma for every part.
- *Hiaki suppletion* (Harley 2014). Some verbs supplete for object number
  (*me'a*/*sua* 'kill.sgObj/plObj'), so the verb's form depends on an
  object that word-sized incremental planning has not yet reached (p. 8).
- *Treelets* keep the triad and word- or phrase-sized storage, so they
  still fail on Inuktitut and Hiaki.

**Algorithms, not only representations (§2.2; C5, moderate).** Inserting
lemmas into slots as they are retrieved fails on Vietnamese. Separating
content retrieval from structure building fails on Hiaki, since syntactic
number is not available at morphophonological retrieval. Building
structure after retrieval fails on verbs whose arguments are unplanned
(*devour*). The resolution is "a single unified process of syntactic
structure building" (p. 11).

**What could have come out otherwise.** A treelet model, which already
drops the morphology–syntax split, could have handled the three cases with
stored units alone. On the paper's analysis it does not.

## What this does not say

- **That the paper's own model works.** The 8-stage non-lexicalist model
  is a two-page verbal sketch with no implementation, simulation or data
  (C7, weak). The full model is "in prep." (p. 11). [NOTE-029](../notes.d/NOTE-029.md) says this
  paper would not source a THEORY about that model, and this account does
  not.
- **That the aphasia predictions hold.** Paragrammatism hiding syntactic
  errors and agrammatic inflection as a failure of cognitive control are
  hypotheses (C8, weak). The Kalaallisut data are five case studies cited
  as consistent, and the predictions are hard to falsify as stated.
- **That no lemma-style encoding could work.** The critique covers named
  models on selected phenomena. It concedes that Eberhard et al. (2005)
  can handle Hiaki object suppletion through feature sharing (p. 10).
- **That the linguistic case against lexicalism is made here.** The paper
  declines to argue it (p. 2) and does not mention Müller's 2018 reply to
  Bruening. It takes the conclusion as given; see Connections.
- **That stored units have no fixed size, or that "lemmatization" is an
  implementation-level optimization.** Both are conjectures (C10), framed
  as "an interesting empirical question" (p. 8).
- **That wordhood intuitions come from orthography.** Speculation resting
  on one citation, Hoosain 1992 (C9). [NOTE-029](../notes.d/NOTE-029.md) corrects the seed that
  attributed it to Haspelmath.

## Connections

- **Presupposes [THEORY-643](THEORY-643.md).** The paper's assumption (1) rejected is
  Bruening's single combinatorial component. It takes that conclusion
  from the linguistic literature (Bruening 2018 is in its §1 list) as a
  premise for a claim about processing models. Its assumption (2), the
  triad, comes from Distributed Morphology and Preminger (2021), which the
  record does not hold, and Bruening does not support it.
- It cites Haspelmath ([THEORY-477](THEORY-477.md)) for the absence of empirical
  criteria for wordhood (pp. 2, 15), not for its production argument.
- [NOTE-029](../notes.d/NOTE-029.md) names [ANTH-THEORY-021](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-021.md) and [ANTH-THEORY-022](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-022.md) as touching the
  same theme, that the unit of storage is not the orthographic word. This
  paper is evidence for neither.
