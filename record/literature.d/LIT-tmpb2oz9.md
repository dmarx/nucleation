---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmp53s7s](../notes.d/NOTE-tmp53s7s.md)) from the publisher's open-access
  PDF on journals.plos.org; worth reading as the source of the Bayesian
  causal-inference observer for multisensory cue combination: the observer
  infers whether two cues share a cause and averages the fused and the
  separate estimates by that posterior, which fits one dual-report
  ventriloquist experiment (19 analysed subjects, R2 = 0.97 with four
  parameters) better than forced fusion, segregation, a MAP rule or the
  interaction priors of Roach et al. and Bresciani et al. Its limits: one
  task in azimuth only; p_common fixed and fitted, so nothing about how the
  prior is set or learned; the second "experiment" re-models another lab's
  published group data with two parameters imported; no test of
  automaticity and no neural test.
title: 'Causal Inference in Multisensory Perception'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    "Hierarchical probabilistic models in cognitive science", written by
    another assistant (A), which cites it as Körding et al. (2007) in its
    section 2. Citation checked against Crossref: Konrad P. Körding, Ulrik
    Beierholm, Wei Ji Ma, Steven Quartz, Joshua B. Tenenbaum and Ladan
    Shams, PLoS ONE 2(9): e943, published online 26 September 2007, which
    is `published:` and agrees with the article's own "Published September
    26, 2007". A's authors, year and title are right; the sentence A puts
    in quotation marks is A's paraphrase of the abstract, not the paper's.
    Read from the publisher's open-access PDF (CC BY),
    https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0000943&type=printable,
    10 pages, extracted with pdftotext. Not read: Supporting Information
    Text S1 and Figures S1–S2. Status Active.
tags:
- cognition
- probabilistic-modeling
- causality
date: '2026-11-04'
published: '2007-09-26'
doi: '10.1371/journal.pone.0000943'
first_author: 'Körding'
keywords:
- 'causal inference'
- 'multisensory integration'
- 'cue combination'
- 'ventriloquist effect'
- 'ideal observer'
- 'Bayesian model selection'
- 'auditory-visual localization'
implementations: []
summary: >-
  Körding, Beierholm, Ma, Quartz, Tenenbaum & Shams (2007). An ideal
  observer receives noisy visual and auditory measurements and does not know
  whether they came from one source or two. It computes the posterior
  probability of a common cause and, under squared-error cost, reports for
  each modality the average of the fused and the segregated estimate
  weighted by that posterior, so cue integration is nonlinear in the cues.
  Fitted with four parameters to a dual-report ventriloquist experiment, it
  explains the location reports (R2 = 0.97; 0.96 on a held-out half) and
  beats forced fusion, full segregation, a MAP rule and two interaction-prior
  models on likelihood; refitted to the published data of Wallace et al.
  (2004) it reproduces unity judgements and the negative bias on trials
  judged to have two causes. The authors argue, without testing it, that
  perception infers causal structure as cognition does. The paper never
  calls its model hierarchical; that is A's label.
---
<!-- inactive-ok-file: THEORY-769 THEORY-tmpbqbnn — Proposed or new; cited from the reading of Körding et al. (2007) as open -->

# LIT-tmpb2oz9: Causal Inference in Multisensory Perception

Körding, K. P., Beierholm, U., Ma, W. J., Quartz, S., Tenenbaum, J. B. & Shams, L. (2007). Causal Inference in Multisensory Perception. *PLoS ONE* 2(9): e943. doi:10.1371/journal.pone.0000943.

## Key takeaways

*From the reading, [NOTE-tmp53s7s](../notes.d/NOTE-tmp53s7s.md). Page numbers are the PDF's.*

- **Averaging over causal structures.** The observer does not decide
  "one cause" and then fuse; it weights the fused and the separate
  estimates by the posterior probability of a common cause on every trial
  (eqs 9–10). Forced fusion (p_common = 1) and segregation (p_common = 0)
  are special cases.
- **Fit.** "Four parameters were used to fit 250 data points" and "The
  causal inference model accounts for the data very well (R2 = 0.97" (p.
  3); trained on half the data, "we still find an excellent performance
  (R2 = 0.96)" on the other half (p. 8). Forced fusion "fails to explain
  much of the variance in Fig. 2c (R2 = 0.56)" (p. 5).
- **Rivals.** On per-subject log likelihood it beats a MAP rule, full
  integration, full segregation and the Roach et al. and Bresciani et al.
  interaction priors (Table 1, p. 5), and it explains why those priors
  fitted: the causal-inference prior is a mixture of a ridge and an
  independent component.
- **One experiment, not two.** Experiment 2 re-models the published results
  of Wallace et al. (2004), with two parameters taken from a third study:
  "These parameters were not tuned." (p. 9).
- **Method.** Predictions must marginalize over the unobserved internal
  measurements; comparing the posterior directly to response distributions
  is called "a common mistake".

## Standing in the record

Cited in A's synthesis (section 2) as perception estimating "the hidden
causal structure that determines whether averaging is appropriate", and as
hierarchical probabilistic inference in relatively automatic perception.
The first half holds. The paper never calls the model hierarchical: it is a
two-component mixture over causal structure with a fixed prior fitted per
dataset, and nothing is learned at the upper level across contexts.
Automaticity is asserted ("continually and effortlessly"), not tested.

It is the formal common-cause observer that [THEORY-769](../theory.d/THEORY-769.md) borrows for body
ownership, and that [NOTE-997](../notes.d/NOTE-997.md) and [NOTE-992](../notes.d/NOTE-992.md) name as the causal-inference
model the rubber-hand literature wants tested; it shows such a model fitting
localization, not ownership. Its observer is ideal relative to its noisy
measurements, as [THEORY-336](../theory.d/THEORY-336.md) holds. Filed from it: [THEORY-tmpbqbnn](../theory.d/THEORY-tmpbqbnn.md).
