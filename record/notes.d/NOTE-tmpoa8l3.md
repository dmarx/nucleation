---
status: Read
paper: LIT-tmpnbrst
title: 'Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin et al. — Causal scrubbing: results on a paren balance checker'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27: the post fetched from the Alignment
    Forum's own API (post kjudfaQazMmC74SbF, postedAt 2022-12-03,
    about 9,100 words) and converted from its HTML body to text. Read:
    the introduction, setup (model, dataset, the algorithm and the
    informal hypothesis), methodology, the summary table, Experiments
    0–4, future work, conclusion, the appendix sections (dataset, code,
    sampling unimportant inputs, the analysis of head 0.0, p_adj and its
    proof, attribution results, breaking up Experiment 3 by term) and all
    eleven footnotes. The post's diagrams and plots are images and were
    read from their captions and the surrounding text only. The table's
    percentages, the class mixture and the additivity remark were
    re-computed (record script, 2026-10-27).
date: '2026-10-27'
summary: >-
  Causal scrubbing applied to a small transformer that classifies
  parenthesis strings as balanced. Saying which three heads carry which
  test recovers 88–93% of the loss; adding how the heads compute their
  tests brings the combined hypothesis to 72%, the excess losses of its
  two halves roughly adding. Splitting one head's input into separately
  resampled terms raised the score from 77% to 81–84%, which the authors
  say is an artefact of resampling, not a better explanation.
---
<!-- inactive-ok-file: THEORY-802 CLAIM-454 — Proposed; the account and claim this reading bears on, cited as open -->

# NOTE-tmpoa8l3: Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin et al. — Causal scrubbing: results on a paren balance checker

## Contribution

It is the long form of the first of the two applications the main post
(LIT-1549, NOTE-1168) summarizes in one table. It shows causal
scrubbing used as an instrument for iterating on a hypothesis about a
model whose task has a known algorithm. Each refinement is scored with a
standard error, and the post reports where the score misled the authors:
where it barely penalized a wrong feature, and where it rose for a reason
they reject.

## Key insight

A hypothesis can be refined in two directions that move the score in
opposite ways. Making it more *accurate* (a feature closer to what the
component computes) should raise the score. Making it more *specific*
(saying how a component computes its feature, which permits more swaps)
generally lowers it if the addition is imperfect. "Scores are not
obviously good or bad, only better or worse relative to others."

## Assumptions

- **Model.** A three-layer transformer, two heads per layer, pre-layernorm,
  bidirectional attention (no causal mask). Strings of up to 40
  parentheses, with [BEGIN] at position 0, where the classification is
  read, and [END] after them.
- **Training data.** 100k sequences, about 92% randomly generated
  even-length strings with balanced ones upsampled to about 26%, plus
  special cases and adversarial examples for other models. The model and
  the dissection that produced the informal hypothesis are unpublished.
- **What is explained.** Low loss on the random, non-adversarial subset
  only (model loss 0.0003, accuracy 99.99%).
- **The metric.** "% loss recovered" = 1 − (L − L₀ₐ)/L₀ᵦ, where L₀ₐ is the
  model's loss and L₀ᵦ the loss with outputs shuffled across inputs
  (4.30, accuracy 61%). Every experiment uses 2,000 scrubbed inputs drawn
  from the 100,000 sequences.
- **The algorithm hypothesized.** Scanning right to left, track the
  proportion pᵢ of open parentheses in each suffix. The count( test asks
  that p₁ = 0.5 and that the first parenthesis is open. The horizon test
  asks that pᵢ ≤ 0.5 at every i. A string is balanced exactly when both
  pass.

## Key results

The table (summary of experimental results):

| # | hypothesis | loss ± s.e. | % recovered | accuracy |
|---|---|---|---|---|
| 0a | the model, unscrubbed | 0.0003 | 100% | 100% |
| 0b | outputs shuffled | 4.30 ± 0.12 | 0% | 61% |
| 1a | 1.0 and 2.0 carry the equal-count test, 2.1 the horizon test | 0.52 ± 0.04 | 88% | 88% |
| 1b | 1a with the count( test | 0.30 ± 0.03 | 93% | 91% |
| 2a | 1b, saying 1.0 and 2.0 read 0.0's output at position 1 | 0.55 ± 0.04 | 88% | 87% |
| 2b | 2a, with 0.0's output at position 1 written ϕ(p) + residual | 0.53 ± 0.04 | 88% | 87% |
| 3a | 1b, with 2.1's input resampled position by position | 0.97 ± 0.06 | 77% | 85% |
| 3b | 3a with the adjusted proportion p_adj | 0.68 ± 0.05 | 84% | 88% |
| 3c | 3a, with 2.1's input at each position split into terms | 0.69 ± 0.05 | 84% | 87% |
| 3d | 3a, with layer 1's term at each position resampled at random | 0.81 ± 0.05 | 81% | 87% |
| 4 | 2b and 3b together | 1.22 ± 0.07 | 72% | 82% |

- **A correlated feature is barely penalized (1a → 1b).** The equal-count
  test and the count( test differ only on strings that start with ")" and
  have equal counts. Using the wrong one costs five points (88% against
  93%), mostly on balanced references (loss 1.31 → 0.65). "If one had
  only the results of experiment 1a, it would not be clear that such an
  improvement needed to be made." The authors: "causal scrubbing is not
  legibly punishing when the feature you claimed correspondance with is
  highly correlated with the 'true feature'".
- **Specificity costs, and the costs add (2, 3, 4).** Saying how 1.0 and
  2.0 compute their test drops 1b's 93% to 88%. Resampling 2.1's input
  separately at each position drops it to 77%. A single position's
  unbalanced signal suffices for 2.1 to flip a prediction, and up to 40
  independent inputs are drawn. The combined hypothesis loses roughly the
  sum of the two halves' losses: 0.53 + 0.68 = 1.21 against 1.22.
- **The linear reading of head 0.0 holds (2b).** Rewriting 0.0's output as
  ϕ(p) = (2p − 1)(h̄_open − h̄_close)/2 plus a residual, and resampling the
  residual freely, leaves the score unchanged. The authors note this adds
  no confidence about which p the head computes, since 2a already tested
  that. The value vectors at open and at close parentheses have cosine
  −0.995 with each other and at least 0.994 with their own means.
- **A better feature recovers loss (3b).** Head 0.0's attention is "quasi
  upper triangular". A proportion p_adj that weights the prefix by a
  fixed b_{q,n} < (q − 1)/n gives a horizon test that agrees with the
  original on every string passing the count test. The appendix proves
  this, and the score rises from 77% to 84%.
- **Two refinements score higher for the wrong reason (3c, 3d).** Splitting
  2.1's input at each position into separately resampled terms raises 3a's
  77% to 84% (3c) or 81% (3d). Resampling the terms separately "washes
  out" the unbalanced signal that a single resampled input carries. "Are
  the results of experiment 3c and 3d legitimate then? We think not." A
  hypothesis that permits sampling terms separately also permits sampling
  them together, and an adversary allowed to ask for the latter would
  recover 3a. Their appendix confirms that sampling layer 1's terms
  together "hurt our scrubbed model's loss".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Two heads carry an equal-count-and-starts-open test and one head the horizon test, to 93% of the loss | strong for this model | Exp. 1b, s.e. 0.03 on the loss |
| C2 | Using a correlated but wrong feature (equal count for count() lowers the score only to 88% | strong | Exp. 1a against 1b |
| C3 | Head 0.0 writes the open proportion along one direction | strong | Exp. 2b, and the cosines of the appendix |
| C4 | p_adj's horizon test agrees with the original on strings passing the count test | demonstrated | appendix proof, checked by the record |
| C5 | More specific hypotheses that resample terms separately can score higher than the hypothesis they refine | demonstrated in one model | Exp. 3c, 3d against 3a (THEORY-tmpnu6ih) |
| C6 | The excess losses of the two halves of the combined hypothesis roughly add | observed once | Exp. 4 against 2b and 3b |

## Concepts

- **count( test**: equal counts and a first parenthesis that is open.
- **Horizon test**: no suffix with more open than close parentheses.
- **p_adj**: the open proportion weighted as head 0.0's measured attention
  weights prefix and suffix.
- **Accuracy and specificity**: the two directions of refinement, which
  move the score in opposite directions.

## Connections

It applies the method of LIT-1549 and shares its definitions with the
appendix post (LIT-tmpt2u54), whose §4.1 points here as the case where
sampling unimportant inputs separately matters. The induction results
(LIT-tmpkdyqt) are the other application.

## Bearing on the record

- **THEORY-978.** Experiment 1a is the authors' measured instance of
  the limit the account derives. The score depends only on the partition
  a feature induces, so a feature that partitions the data almost as the
  true one does scores almost as well: 88% for the wrong test against 93%
  for the right one. The account is about exact ties. This is the
  near-tie it does not bound, measured once.
- **NOTE-1168, C4 and C6.** C4 can now be read against its source: the
  main post's four rows are 1b, 2b, 3b and 4 of this table. C6 (breaking a
  correlation can raise the score) has here its measured case, 3c and 3d.
- **CLAIM-454 and THEORY-802.** What passes is a partition of the
  data. The authors expect "all our claims, while highly correlated with
  the truth, will miss some nuance in the exact boundaries represented
  by the model".

No instruction for machine-learning practice is recorded here
(`anthology-candidate`).

## Limitations

- **One model, unpublished.** The model, its training and the dissection
  that produced the informal hypothesis are not public, and the code was
  "planned" for release.
- **One run per hypothesis.** Standard errors are given for the losses;
  run-to-run variation over the 2,000 scrubbed samples is not.
- **A restricted dataset.** Adversarial strings, on which the model
  struggles, are excluded. The authors say it would have been cleaner to
  train on the random subset only.
- **Errors in the post.**
  - The horizon test is stated backwards twice. Passing is glossed as
    "checking whether there is at least one open parenthesis that has not
    been later closed", which describes failing. In proportions, "if the
    proportion is less than 0.5 at any point, this test is failed" should
    read greater than 0.5, as the appendix's proof has it (a failure is
    p_suffix > 0.5).
  - Experiment 2b's loss is 0.56 in the text and 0.53 in the table (87%
    against 88% recovered).
  - Row 2a's loss of 0.55 gives 87.2% by the post's formula; the table
    prints 88%.
  - The dataset appendix calls the training set "class-balanced", while
    the same appendix upsamples balanced strings to "about 26%".
  - The proof's last line drops "> 0.5" ("⇔ p_adj, q ⇔").
- **The metric's normalization.** The post divides by L₀ᵦ, where the
  appendix post's definition divides by L₀ᵦ − L₀ₐ. With L₀ₐ = 0.0003 the
  two agree to a tenth of a point. The other rows re-compute from the
  stated losses (record check). The 26% mixture is borne out by the
  shuffled baseline's 61% accuracy (0.26² + 0.74² = 0.615) and by the
  split losses of 1a and 1b (0.26 × 1.31 + 0.74 × 0.25 = 0.53; 0.26 ×
  0.65 + 0.74 × 0.18 = 0.30).

## Open questions

- Would the adversary the authors propose, asked to sample 3c's terms
  together, give back 3a's 77% exactly, as they argue it must?
- How far below 93% would a feature have to fall before a reader without
  the true algorithm would notice it is wrong? That is the near-tie
  THEORY-978 leaves unbounded.
