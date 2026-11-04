---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmpazn9q](../notes.d/NOTE-tmpazn9q.md)) from the version of record
  posted on the first author's site; worth reading as the paper that made
  learning an inductive constraint, Goodman's overhypothesis, a matter of
  inferring the higher-level parameters of a hierarchical Bayesian model,
  with the shape bias as its flagship case and a Chinese-restaurant
  extension that discovers ontological kinds. A computational-level
  modelling paper with no new experiments: its fits to published data are
  qualitative, the only rival fitted is a fixed-prior Bayesian model, the
  hierarchy and its top-level prior are given by hand, and the model does
  not account for Smith et al.'s no-name condition.
title: 'Learning overhypotheses with hierarchical Bayesian models'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    on hierarchical probabilistic models in cognitive science, written by
    another assistant (A), where it is item A of the cited works.
    Citation checked against Crossref and OpenAlex: Charles Kemp, Amy
    Perfors and Joshua B. Tenenbaum, Developmental Science 10(3),
    307–321, in its Bayesian Special Section; PubMed 17444972. Crossref
    gives online 17 April 2007, which is `published:`, and the issue May
    2007. Corrected from the registries: Crossref and OpenAlex both give
    the second author as "Andrew Perfors"; the paper's byline reads "Amy
    Perfors", which is kept. Read in full (NOTE-tmpazn9q) from the
    publisher's typeset PDF of the version of record, 15 pages, posted on
    Charles Kemp's own site
    (https://www.charleskemp.com/papers/KempPTDevSci.pdf) and linked from
    its publication list. OpenAlex also lists green copies at CMU
    KiltHub, the Adelaide repository (hdl 2440/55320) and CiteSeerX, not
    used. Not read closely: the reference list. The authors' code is
    listed at charleskemp.com/code/ohexternal.tar.gz, not downloaded.
tags:
- cognition
- probabilistic-modeling
- learning-and-conditioning
date: '2026-11-04'
published: '2007-04-17'
doi: '10.1111/j.1467-7687.2007.00585.x'
first_author: 'Kemp'
keywords:
- 'overhypotheses'
- 'hierarchical Bayesian models'
- 'shape bias'
- 'word learning'
- 'ontological kinds'
- 'Dirichlet-multinomial'
- 'Chinese restaurant process'
implementations: []
summary: >-
  Kemp, Perfors & Tenenbaum (2007). Learning needs overhypotheses,
  constraints on the hypotheses a learner considers; some must be innate,
  but a hierarchical Bayesian model can learn others while it learns the
  categories they constrain. In a Dirichlet-multinomial model of
  Goodman's bags of marbles, each category's feature distribution sits
  under two higher-level parameters, the within-category variability α
  and the population distribution β of each feature. Learned from a few
  labelled exemplars, low α for shape gives the shape bias, including
  generalization to a novel category from one exemplar, which matches
  Smith et al.'s (2002) training data qualitatively; the model also
  covers Nisbett et al.'s Barratos judgments, which a fixed-prior model
  does not. A Chinese-restaurant prior over kinds of categories discovers
  objects and substances, each with its own variability. Two stated
  predictions: two exemplars per category teach the bias best, and the
  abstract level can be learned faster than the concrete one.
---
<!-- inactive-ok-file: THEORY-tmpi143z NOTE-596 — Proposed or new, or Skimmed; cited from the reading of Kemp, Perfors and Tenenbaum (2007) as open -->

# LIT-tmplu70i: Learning overhypotheses with hierarchical Bayesian models

Kemp, C., Perfors, A. & Tenenbaum, J. B. (2007). Learning overhypotheses with hierarchical Bayesian models. *Developmental Science* 10(3): 307–321. doi:10.1111/j.1467-7687.2007.00585.x.

## Key takeaways

*From the reading, [NOTE-tmpazn9q](../notes.d/NOTE-tmpazn9q.md). Page numbers are the journal's.*

- **The thesis.** "Inductive learning is impossible without overhypotheses,
  or constraints on the hypotheses considered by the learner" (p. 307);
  hierarchical Bayesian models "explain how overhypotheses can be acquired"
  (p. 309).
- **What the higher level is.** Level 2 is (α, β): how variable each
  feature is within categories, and the population distribution of its
  values. A feature is diagnostic, as shape is, because its α is low.
- **The shape bias.** After Smith et al.'s brief training on four
  categories, "shape matches are preferred in both cases", first- and
  second-order generalization (p. 314).
- **Two predictions.** With the number of exemplars fixed, the best way to
  teach the bias is "to provide just two exemplars per category"; and
  "learning can sometimes be faster at level 2 than at level" 1 (p. 314).
- **Flat models can mimic it.** A conventional Bayesian model "could mimic
  the predictions of our model if it used the" right prior on the θ_i, but
  that prior would be very complicated (p. 318). The claim is parsimony and
  learnability of the prior, not that a flat model cannot do it.
- **A misfit, admitted.** The model predicts that the no-name condition,
  where children got no category labels, "should not have been impaired";
  children showed first- but not second-order generalization (p. 315).

## Standing in the record

Registered from the owner's pasted synthesis of 2026-11-04, which cites it
as the clearest case of a hierarchy that flat Bayesian models cannot
explain as naturally. The reading keeps "as naturally" and drops the rest:
the authors concede a flat model with the right prior could mimic theirs.
It is the record's first entry on the shape bias, on Goodman's
overhypotheses and on hierarchical Bayesian models as psychological
theories of learning to learn. Its successor in causal learning is
[LIT-tmp6aw6y](LIT-tmp6aw6y.md). Its Chinese-restaurant extension partitions categories into
kinds without fixing their number, which bears weakly on [QUESTION-276](../questions.d/QUESTION-276.md); it
does not allow overlap. Complementary to [LIT-820](LIT-820.md) and [NOTE-596](../notes.d/NOTE-596.md), which
measure a learner's inductive bias where this paper accounts for how one
could be learned. Filed from it: [THEORY-tmpi143z](../theory.d/THEORY-tmpi143z.md). No instruction for
machine-learning practice; not an anthology candidate.
