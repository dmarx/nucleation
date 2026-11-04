---
status: Read
paper: LIT-tmplu70i
title: 'Kemp, Perfors and Tenenbaum — Learning overhypotheses with hierarchical Bayesian models'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in full on 2026-11-04 from the publisher's typeset PDF of the
    version of record, 15 pages, posted on Charles Kemp's own site
    (https://www.charleskemp.com/papers/KempPTDevSci.pdf) and linked from
    the publication list at https://charleskemp.com/. Text extracted by
    pdftotext. Read: the abstract, the whole main text, the figure
    captions and the Appendix (the model equations, the CRP prior and the
    MCMC details). Skimmed: the reference list. Not consulted: the
    precursor conference paper (Kemp, Perfors & Tenenbaum 2006, CogSci)
    and the authors' code. The byline reads "Amy Perfors"; Crossref and
    OpenAlex give "Andrew Perfors" in error. Page numbers below are the
    journal's.
date: '2026-11-04'
summary: >-
  A computational-level modelling paper with no new experiments. A
  Dirichlet-multinomial hierarchy learns each category's feature
  distribution and, at the same time, each feature's within-category
  variability α and population distribution β; low α for shape is the
  shape bias, which lets one exemplar of a novel category license
  generalization by shape. It matches Smith et al.'s (2002) training data
  and Nisbett et al.'s Barratos judgments qualitatively, extends by a
  Chinese-restaurant prior to discover ontological kinds, predicts that
  two exemplars per category teach the bias best, and fails on the
  no-name condition.
---
<!-- inactive-ok-file: THEORY-tmpi143z CLAIM-543 CASE-165 NOTE-596 — Proposed or new, or Skimmed; cited from the reading of Kemp, Perfors and Tenenbaum (2007) as open -->

# NOTE-tmpazn9q: Kemp, Perfors and Tenenbaum — Learning overhypotheses with hierarchical Bayesian models

## Contribution

The paper recasts learning an inductive constraint as posterior inference
over the higher-level parameters of a hierarchical Bayesian model (HBM),
at Marr's computational level. One simple HBM reproduces the shape bias
after Smith et al.'s brief training, including second-order
generalization to novel categories; a nonparametric extension discovers
ontological kinds and their kind-specific variability without being told
how many kinds there are. It answers the objection that a Bayesian model
succeeds only by the modeller's "ability to choose the right prior"
(p. 317): the higher levels can be learned.

## Key insight

"Inductive learning is impossible without overhypotheses, or constraints
on the hypotheses considered by the learner" (p. 307), but the constraint
need not be innate. Put it one level up in a hierarchy and the same
evidence that teaches the categories teaches the constraint, sometimes
faster. Abstract knowledge "may appear to be innate only because it is
acquired" much faster than lower-level knowledge (p. 318).

## Assumptions

- **The structure is given.** The hierarchy, the generative process at
  each level and the prior at the top are fixed; only parameter values are
  learned. "we do not claim that overhypotheses can be" generated "out of
  thin air" (p. 318).
- **The model.** Level 1, θ_i, the feature distribution of category i;
  level 2, (α, β), within-category variability and the population feature
  distribution; level 3, λ, an exponential prior on α, with λ = 1
  throughout.
- **Independent feature dimensions**, each with its own α and β; within a
  category, observations are exchangeable multinomial draws.
- **Category membership is given.** The learner knows which objects belong
  together; the model learns overhypotheses about known categories, and,
  in the extension, kinds of categories, not the categories themselves.
- **The kinds prior** is a Chinese restaurant process with γ = 0.5,
  favouring few kinds.
- **Computational level only.** The implementation is not "intended as a
  process model" (p. 312); MCMC and numerical integration are
  conveniences.

## Key results

- **What HBMs add (p. 309).** They "explain how overhypotheses can be
  acquired" by statistical inference.
- **The Barratos task (pp. 312–313).** After one member of a tribe, people
  judge skin colour homogeneous and obesity not. A "conventional Bayesian
  model" with (α, β) fixed gives the same inference for both; "our model
  alone accounts" for the difference (p. 313).
- **The shape bias (p. 314).** Trained on Smith et al.'s four categories,
  "shape matches are preferred in both cases", first- and second-order
  generalization, as children chose shape 88% and 70% of the time.
- **Teaching (p. 314).** With the total number of exemplars fixed, "our
  model predicts that the best way to teach the shape bias is to provide
  just two exemplars per category"; the marbles simulation (Fig. 6a) gives
  the U-shaped curve, called "a novel prediction".
- **Abstract before concrete (p. 314).** "learning can sometimes be faster
  at level 2 than at level" 1, which separates the HBM from bottom-up
  accounts in which level 1 must be secure first.
- **The no-name condition (pp. 314–315).** Without labels, children showed
  first- but not second-order generalization; the model predicts that
  learning "should not have been impaired". The authors call it a
  discrepancy for further work.
- **Ontological kinds (p. 316).** "Figure 7d confirms that the model
  correctly groups" the categories into objects and substances, using both
  β (characteristic features such as solidity) and α (within-kind
  variability): a shape bias for solids, a material bias for non-solids.
- **Flat models can mimic (p. 318).** A conventional Bayesian model "could
  mimic the predictions of our model if it used the" right prior on the
  θ_i; specified directly, that prior would be very complicated. The
  hierarchy specifies it indirectly.

## Concepts

- **Overhypothesis**: any form "of abstract knowledge that sets up a
  hypothesis space" at a less abstract level (p. 308), broader than
  Goodman's sense and covering theories, schemata and scripts (fn. 1).
- **Over-overhypothesis**: λ, an overhypothesis about (α, β).
- **Level 1, 2, 3 knowledge**: the θ_i; their distribution (α, β); the
  prior on (α, β).
- **Hypothesis space**: in the static, computational sense, every state
  reachable under any input, not the set a learner currently entertains.
- **Conventional Bayesian model**: one with a fixed prior, level 2 fixed
  and only level 1 learned.
- **First- and second-order generalization**: extending a label within a
  trained category, and to a novel category.

## Connections

It builds on Goodman's (1955) overhypotheses and bags of marbles, on
Tenenbaum and Xu's Bayesian word learning, and on Smith et al. (2002),
Jones & Smith (2002), Samuelson (2002) and Nisbett et al. (1983) for the
data. Colunga & Smith's connectionist account is discussed, not fitted.
Tree-structured ontologies (Keil's M-constraint) are named as future work,
the direction the nested CRP of LIT-1542 takes. Its successor in causal
learning is LIT-tmp6aw6y.

## Bearing on the record

- **The synthesis's description.** A, in the owner's pasted synthesis,
  gets the attribution right and the flagship example right; HBMs explain
  how overhypotheses are learned, and the paper does address where a
  Bayesian learner's priors come from (p. 317).
  - **A's paraphrase in quotation marks.** "It demonstrated computationally
    how broad inductive constraints, or overhypotheses, could themselves be
    learned" and "The framework also addressed the problem of where a
    Bayesian learner's priors come from" are not in the paper. They are A's
    paraphrase.
  - **Imprecise.** A says the higher level holds "which features tend to be
    informative across categories". It holds within-category variability
    and the population distribution; low variability is what makes a
    feature diagnostic. A fair consequence, not what the parameters are.
  - **Overstated.** A calls it "one of the clearest examples of why
    genuinely hierarchical models can explain cognitive phenomena that flat
    Bayesian models cannot explain as naturally". The paper concedes a flat
    model could mimic it with the right prior (p. 318). "As naturally" is
    the defensible part.
  - **Missing.** No new experiments; the ontological-kinds extension, half
    the paper; the two predictions; the no-name misfit; the given
    structure. "Transfer between concepts" is fair as second-order
    generalization, a word the paper does not use.
- **QUESTION-276 (overlapping higher-level perspectives, number not
  fixed).** Qualifies, weakly. The kinds model infers groupings of
  categories without fixing their number, but by partition: each category
  has one kind. A precedent for a number not fixed, not for overlap, which
  is the Indian-buffet work of LIT-1623, LIT-1556 and CASE-165. Nothing on
  interventions. Dated note added.
- **CLAIM-543 (hierarchy is not organization).** Supports its first half.
  The model is hierarchical and its categories are exchangeable given
  (α, β): a hierarchy that is organizationally flat in the claim's sense.
  The kinds extension adds a partition, not components conditioning one
  another. Dated note added. CLAIM-536 is not touched.
- **CASE-165.** Unrelated in substance: partition, not feature allocation.
- **LIT-1542 and THEORY-969 (nested CRP).** The lineage: a flat CRP over
  kinds, with trees named as future work.
- **LIT-563, NOTE-466 and THEORY-475 (HDDM).** The same machinery for
  another aim: there partial pooling estimates parameters, here it is the
  psychological theory.
- **LIT-820, LIT-769 and NOTE-596 (iterated learning; the shape bias in
  transmission chains).** Complementary: they measure or infer a learner's
  fixed prior; this paper accounts for how such a bias could be learned.
- **THEORY-1012 (features made dependent through a layer of
  categories).** Structurally cognate, in a feature-allocation formalism.
- Filed: THEORY-tmpi143z. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The authors' own.** The no-name misfit (pp. 314–315); the hierarchy,
  generative process and top prior set by hand (p. 318); computational
  level only; teaching shape and material biases together untested in
  children.
- **Qualitative fits.** Bar patterns against published data, with no
  goodness-of-fit statistic and no model comparison.
- **One rival fitted**, the fixed-prior Bayesian model; the connectionist
  alternative is answered in argument only.
- **Discrete, independent features**, and categories given.

## Open questions

- Does second-order generalization from one exemplar track the
  within-category variability of features in training, as the learned α
  predicts, rather than only how often features occur? A training study
  that varies the two separately would tell.
- Does the two-exemplars-per-category optimum hold in children?
