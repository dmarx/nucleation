---
status: Skimmed
paper: 'LIT-tmpe93h7'
title: 'Cumulative cultural evolution in the laboratory'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Skimmed, not read: every section of the main text was covered, but not
    first-hand. PubMed Central (PMC2504810) serves the full text only to a
    browser (curl got a reCAPTCHA page; the E-utilities and Europe PMC
    full-text services return front matter only, the article not being in
    the open-access subset). PNAS, the PNAS PDF and the Edinburgh
    repository copy (research.ed.ac.uk/files/8776820) returned 403. The
    PMC page was reached through the WebFetch tool, which returns a
    model-mediated account and declines verbatim reproduction. Three
    passes were made: Introduction and Methods in detail; results,
    figure captions and Discussion; and short exact quotes, both tables
    in full and the section list with paragraph counts. The figures in
    the tool's accounts agree across passes. Quotes below are those the
    tool returned as exact, unchecked against the page. The two distance
    formulas are images on the page and were described, not seen. The
    Supporting Information (SI Text, Tables S1–S8) was not reached; a
    2017 correction (PNAS 114(12):E2544, PMC5373391) says only that
    Table S7 "appeared incorrectly" and that the SI was corrected online.
date: '2026-10-09'
summary: >-
  Four chains of ten adults each learned a 27-item artificial language
  from 14 items and passed their test output on. Transmission error fell
  and string–meaning structure rose. Unfiltered (Experiment 1), the
  languages collapsed to 2–5 words that systematically underspecified
  meanings (colour lost in every chain). With homonyms filtered from
  training (Experiment 2), they became compositional, with substrings for
  colour, shape and motion. Participants believed they were copying.
---

<!-- inactive-ok-file: LIT-tmp9f0fn — Deferred, no lawful full text; named as the ancestor of the method, not leaned on -->
<!-- inactive-ok-file: THEORY-tmp0w0cu — Proposed; the account this reading produced or bears on -->

# NOTE-tmppvy0t: Cumulative cultural evolution in the laboratory

## Contribution

A laboratory paradigm for iterated learning with human participants,
showing that a language transmitted down a diffusion chain changes
cumulatively, becoming easier to learn and more structured, when no
participant is trying to change it. Before it, the claim that iterated
learning produces linguistic structure rested on computational and
mathematical models, and earlier human diffusion chains (Horner et al.
2006) used tasks with a small set of equally good behaviours, where
cumulative adaptation could not show.

## Key insight

Give each learner only part of a language and test it on all of it. What
it cannot memorize it must generalize, and its generalizations become the
next learner's data. Over generations the language reorganizes so that the
part predicts the whole. Which reorganization wins depends on what else
constrains it: with no pressure against ambiguity, one word per class of
meanings; with ambiguity removed from training, one part of the word per
feature of the meaning.

## Assumptions

- **Participants**: 80 university students without linguistics training
  (46 female, 34 male; mean age 22.5, range 18–40), Edinburgh.
- **Meaning space**: 27 pictures, a coloured object with a motion arrow:
  shape (square, circle, triangle) × colour (black, blue, red) × motion
  (horizontal, bouncing, spiralling).
- **Initial languages**: one random label per picture, 2–4 syllables
  concatenated from a set of 9 consonant–vowel syllables. Later labels are
  whatever participants type.
- **Bottleneck**: each language is split at random into 14 SEEN and 13
  UNSEEN pairs. Three rounds of training, each with two randomized
  exposures to SEEN (string 1 s, then string and picture 5 s) and a test;
  rounds 1–2 test half of each set, round 3 tests all 27, and that final
  output is the next generation's language, re-split at random.
- **Chains**: four per experiment, ten generations each, each starting
  from a different random language.
- **Participants' belief**: told to reproduce the alien language as well
  as possible; not told about the chain; a post-test questionnaire
  suggested many did not notice they were tested on unseen items.
- **Experiment 2 filter**: before training, if a string labels more than
  one picture in SEEN, all but one (chosen at random) are moved to UNSEEN,
  so training data are one-to-one. Described as "an analogue of a pressure
  to be expressive that would come from communicative need".

## Key results

- **Measures.** Transmission error: mean normalized Levenshtein distance
  between a participant's strings and the previous generation's, over
  meanings (0 identical, 1 maximally different). Structure: Pearson
  correlation between pairwise string distances (normalized Levenshtein)
  and pairwise meaning distances (Hamming, over the three features),
  reported as a z-score against 1,000 Monte Carlo reassignments of strings
  to meanings; undefined when the shuffled sample has no variance (two
  cases in Experiment 1).
- **Experiment 1 (Figure 2, Table 1).** Error fell from first to last
  generation (mean decrease 0.748, SD 0.147, t(3) = 8.656, P < 0.002);
  structure rose (mean increase 5.578, SD 2.968, t(3) = 3.7575, P < 0.02).
  Distinct words fell from 27 to 2, 4, 5 and 4 by generation 10. In some
  chains later participants reproduced the language exactly, unseen
  items included. "This underspecification was not random but was
  systematic, in that similar meanings were given the same label."
  Example chain: "tuge" for every horizontal mover by generation 4, "poi"
  for most spiralling ones by generation 6, and by generations 8–10
  horizontal "tuge", spiralling "poi", bouncing split by shape. Colour
  distinctions were lost in all four chains.
- **Experiment 2 (Figure 4, Table 2).** Error fell (mean decrease 0.427,
  SD 0.106, t(3) = 8.0557, P < 0.002); structure rose (mean increase
  6.805, SD 5.390, t(3) = 2.525, P < 0.05). Distinct words stayed between
  10 and 27 across chains and generations (generation 10: 16, 12, 12, 23).
  The circled generation-9 language segments into colour, shape and motion
  morphemes, with irregular items (one string for a bouncing red circle);
  the structure appears by about generation 6 and persists while
  individual morphemes are lost or reanalysed.

## Claims

Not filled: the reading is Skimmed. The paper's claims, as reported, are
that transmission alone made the languages more learnable and more
structured (both experiments, four chains each, t-tests with df = 3); that
the adaptation is "cumulative with respect to learnability and structure
but not with respect to expressivity"; and that this is the "first
experimental validation for the idea that cultural transmission can lead
to the appearance of design without a designer".

## Concepts

- **iterated learning**: acquiring a behaviour by observing it in someone
  who acquired it the same way.
- **diffusion chain**: each participant's output is the next
  participant's input; one participant per generation. "The first
  reported use of this methodology was by Bartlett in 1932."
- **transmission error**: as above; read as the inverse of learnability.
- **structure**: the correlation of string similarity with meaning
  similarity.
- **systematic underspecification**: one string for a class of similar
  meanings, so that a learner can recover the whole language from a
  fragment.

## Connections

- **Bartlett (1932), [LIT-tmp9f0fn](../literature.d/LIT-tmp9f0fn.md)**, is named as the first use of the
  diffusion-chain method. Bartlett's serial reproduction passed a story
  down a chain and watched it drift; this paper passes a language down a
  chain and measures the drift. The paper does not say what Bartlett
  found, and the record has not read him ([LIT-tmp9f0fn](../literature.d/LIT-tmp9f0fn.md) stays Deferred).
- **Griffiths & Kalish (2007), [LIT-tmpdbgz6](../literature.d/LIT-tmpdbgz6.md), read in [NOTE-tmpvzd8x](NOTE-tmpvzd8x.md)**, is
  cited only inside the block of model references [4–13]. The paper does
  not use priors or Bayesian learners. Read against it: the loss of colour
  in every Experiment 1 chain, which the authors tie to the shape bias in
  word learning, is the kind of outcome Griffiths and Kalish predict, a
  learner bias showing through transmission. The Experiment 2 filter is an
  experimenter-imposed selection on the data, outside the learners, which
  is exactly what their analysis assumes away (equal fitness, no
  selection). So Experiment 2 is not a test of convergence to the prior.
  This reading is mine, not the paper's.
- **Kirby (2000)**: the earlier model that removed ambiguous strings from
  the learner's data, the source of the Experiment 2 filter.
- **Galantucci; Garrod et al.; Selten & Warglien**: experiments in which
  participants design a shared communication system on purpose, which
  this design is meant to differ from.
- **Horner et al. (2006)**: diffusion chains in chimpanzees and children
  with a two-technique puzzle box.

## Bearing on the record

- Bears on [THEORY-tmp0w0cu](../theory.d/THEORY-tmp0w0cu.md) (filed from [NOTE-tmpvzd8x](NOTE-tmpvzd8x.md)): consistent with
  it, not a test of it. The chains show bias-shaped outcomes (colour
  dropped, shape and motion kept), but no participant's prior was
  measured, and the filtered condition adds a pressure the theory
  excludes. Recorded there under "what this does not say".
- No instruction for machine-learning practice; not an anthology
  candidate.

## Limitations

- Four chains per experiment; the tests have three degrees of freedom.
- Adult university students who already speak a language. The authors
  concede that "a participant's first language may influence the
  learnability", and argue it cannot explain both the underspecification
  of Experiment 1 and the concatenative morphology of Experiment 2.
- The expressivity pressure in Experiment 2 is an artificial filter
  applied by the experimenter, not communication between participants;
  expressivity and communicative success are not measured.
- Written strings for a 27-item, three-feature meaning space.
- Not checked here: the SI (instructions, full languages in Tables
  S1–S8), and the formulas, which were seen only as described.

## Open questions

- Does the same paradigm with real communication between participants,
  rather than a filter, produce compositional structure?
- Could the learners' biases be measured independently, so that the
  chains' end states can be compared with them (the test [THEORY-tmp0w0cu](../theory.d/THEORY-tmp0w0cu.md)
  asks for)?
- Do the results hold with more chains, larger meaning spaces, or child
  learners?
