---
status: Read
paper: 'LIT-tmpb2oz9'
title: 'Körding et al. — Causal inference in multisensory perception'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in full on 2026-11-04 from the publisher's open-access PDF (CC BY)
    of the version of record,
    https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0000943&type=printable,
    10 pages, text extracted with pdftotext. Read: abstract, Introduction,
    Results (the model, Experiment 1, Table 1, Experiment 2), Discussion,
    Materials and Methods (paradigm, generative model, equations 1–16, data
    analysis), acknowledgements and author contributions; reference list
    scanned. Not read: Supporting Information Text S1 (a .doc file) and
    Figures S1–S2, which hold more detail on the simulation and the
    comparison with the interaction priors. Page numbers below are the
    PDF's.
date: '2026-11-04'
summary: >-
  An ideal observer that infers whether a visual and an auditory cue share
  a cause, and averages the fused and the separate location estimates by
  the posterior probability of a common cause, fits one dual-report
  ventriloquist experiment (19 subjects; R2 = 0.97 with four parameters,
  0.96 on a held-out half) better than forced fusion, segregation, a MAP
  rule or two interaction-prior models, and reproduces another lab's
  published unity and bias data. The paper never calls the model
  hierarchical; that is A's label.
---
<!-- inactive-ok-file: THEORY-769 THEORY-827 THEORY-tmpbqbnn — Proposed or new; cited from the reading of Körding et al. (2007) as open -->

# NOTE-tmp53s7s: Körding et al. — Causal inference in multisensory perception

## Contribution

Earlier cue-combination models either forced fusion (one cause, linear
weighting by reliability) or fitted an ad hoc "interaction prior" over
pairs of locations. This paper gives a normative observer that infers
whether the cues share a cause and contains both fusion and segregation as
special cases. It explains why the interaction priors fitted, since the
causal-inference prior is a mixture of a diagonal ridge and an independent
component, and it predicts location estimates and judgements of common
cause with one model. It also corrects a method: predictions must
marginalize over the unobserved internal measurements, and comparing the
posterior directly with response distributions is "a common mistake".

## Key insight

The observer does not commit to a causal structure and then act on it. On
each trial it computes p(C = 1 | x_V, x_A) and, under squared-error cost,
reports the posterior-weighted average of the fused and the segregated
estimate (eqs 9–10). Because that weight depends nonlinearly on the
disparity, integration is strong for nearby cues and fades for distant
ones, and the response distribution keeps one peak whose position and skew
move. Inferring the common cause "amounts to a Bayesian model selection
problem" solved by the observer.

## Assumptions

- **Generative model (Methods).** C = 1 with probability p_common; then one
  location, or two independent ones, from a central Gaussian prior
  N(0, σ_P) shared by both structures; Gaussian, unbiased, independent
  sensory noise σ_V, σ_A. Azimuth only.
- **p_common is a constant** within the experiment. Outside the lab it
  would depend on "temporal delays, visual experience, context, and many
  other factors", and so "will not be constant".
- **Squared-error cost**, so the report is the posterior mean; the key
  press is the button nearest the estimate.
- **Fitting.** Four parameters (σ_V, σ_A, σ_P, p_common) by maximum
  likelihood to response histograms, obtained by simulating the observer
  over its internal noise. Unimodal trials set aside for the main fit
  "because of potential attentional differences".

## Key results

- **The claim (abstract, p. 1).** "This model accurately predicts the
  nonlinear integration of cues by human subjects in two auditory-visual
  localization tasks."
- **Experiment 1 (pp. 3–5).** Twenty naive Caltech undergraduates, one
  excluded as "effectively deaf" for the task; brief visual and auditory
  stimuli at five azimuths, both locations reported. "Four parameters were
  used to fit 250 data points"; "The causal inference model accounts for
  the data very well (R2 = 0.97". Forced fusion "fails to explain much of
  the variance in Fig. 2c (R2 = 0.56)."
- **Parameters (pp. 3–4).** σ_V = 2.14 ± 0.22°, σ_A = 9.2 ± 1.1°,
  σ_P = 12.3 ± 1.1°, p_common = 0.28 ± 0.05: "The average probability of
  perceiving a common cause for visual and auditory stimuli is relatively
  low".
- **Rivals (Table 1, p. 5).** Log likelihood relative to causal inference:
  MAP rule −11 ± 3, full integration −311 ± 28, full segregation −25 ± 7,
  Roach et al. −18 ± 6, Bresciani et al. −22 ± 6, all "considered decisive
  evidence in favor of the causal inference prior, even when correcting
  for the number of parameters".
- **Split half (Methods, p. 8).** Fitted on half the data, R2 = 0.98, and
  "when we transfer the optimized parameters to the second set of data, we
  still find an excellent performance (R2 = 0.96)".
- **Experiment 2 is not new data (pp. 5, 9).** "We compare the predictions
  of the causal inference model with the reported data from this
  experiment", that of Wallace et al. (2004). Unity: "It explains 72% of the
  variance in human performance"; bias: it "explains 87% of the variance of
  the bias", including the negative bias on trials judged to have two
  causes, which the authors read as a selection effect. σ_motor and σ_A came
  from a third study: "These parameters were not tuned."; p_common and σ_P
  were fitted by least squares.
- **Method (p. 8).** "The traditional way of studying the system by only
  measuring linear weights is not sufficient to fully describe a system
  that performs causal inference."

## Concepts

- **Causal inference**: inferring "whether the signals have a common cause
  (C)" as well as where the sources are; formally a mixture model, "but one
  of a very specific form".
- **Disparity**: "Such a distance or inconsistency is called disparity."
- **Interaction prior**: "a joint prior distribution that defines how
  likely each combination of visual and auditory stimuli is in the absence
  of any evidence."
- **Forced fusion**: the single-cause model, the special case p_common = 1.
- **Auditory bias**: the visual position's pull on the perceived auditory
  position, (ŝ_A − s_A)/(s_V − s_A).

## Connections

It generalizes the reliability-weighted fusion models and recasts the
interaction priors of Roach et al. and Bresciani et al. as approximations to
the causal-inference prior. It opens with Helmholtz's unconscious inference.
The authors acknowledge an independent, similar model by Yoshiyuki Sato and
colleagues. Its descendant for body ownership, Samad et al. (2015), is not
held.

## Bearing on the record

- **A's characterization (synthesis, section 2).** Right: a latent variable
  for one cause or two, fusion if common and separate estimates if not,
  perception estimating the causal structure that decides whether averaging
  is appropriate, nonlinear integration. Four corrections.
  - **"Hierarchical" is A's label, not the paper's.** The word does not
    occur in the paper. The model has two levels of latent variable
    (C, then locations), but its upper level is one fixed prior, p_common,
    fitted per dataset; nothing is shared or learned across contexts, so it
    is not hierarchical in the sense of A's section 1.
  - **Averaging, not deciding.** The observer mixes the two estimates by
    the posterior; it does not choose one structure and then fuse or
    segregate.
  - **One experiment.** The sentence A puts in quotation marks, "The model
    successfully predicted nonlinear patterns of auditory-visual
    integration across two human localization experiments", is A's
    paraphrase, not in the paper. The abstract's "two auditory-visual
    localization tasks" is accurate; "two experiments" suggests two new
    datasets, where only Experiment 1 was run by the authors and Experiment
    2 re-models Wallace et al. (2004).
  - **Automaticity is asserted.** The abstract says causal inference "is
    also performed continually and effortlessly in perception", and the
    Discussion offers the link to cognition as "an intriguing link"; no
    load, timing or awareness manipulation tests it.
- **[THEORY-769](../theory.d/THEORY-769.md) (body ownership as a graded belief in a common cause).**
  Supports the model class, not the claim: this is the formal common-cause
  observer [THEORY-769](../theory.d/THEORY-769.md) borrows, shown to fit localization, and it says
  nothing about ownership. Its split-half test against all-or-none rivals is
  a template for the result [THEORY-769](../theory.d/THEORY-769.md)'s promote_when asks for, not an
  instance of it.
- **[NOTE-997](NOTE-997.md) and [NOTE-992](NOTE-992.md).** Both name this paper's lineage (Körding et al.
  2007; Samad et al. 2015) as the causal-inference model the rubber-hand
  literature should test; filing it gives those mentions a target.
- **[THEORY-827](../theory.d/THEORY-827.md) (the rubber hand illusion is multisensory integration, not
  expectation).** No bearing on its question: there are no expectation or
  demand controls here.
- **[THEORY-336](../theory.d/THEORY-336.md) and [LIT-1055](../literature.d/LIT-1055.md) (an ideal observer is optimal relative to the
  information it is given).** Supports. The observer is ideal relative to
  the noisy measurements x_V, x_A, not the stimuli, and the insistence on
  simulating over those measurements is the same point in practice. The
  authors: "there is no reason why the nervous system should be optimal
  under all circumstances".
- **[QUESTION-276](../questions.d/QUESTION-276.md) (identifying latent higher-level structure, without fixing
  its number in advance, from coactivity a common cause produces).**
  Qualifies, as a minimal case: here common-cause inference is Bayesian
  model selection between two structures fixed in advance, which shows it
  can be read from behaviour but not with the number of structures left
  open.
- **[LIT-620](../literature.d/LIT-620.md) and [NOTE-487](NOTE-487.md) (post hoc Bayesian model selection).** Related in
  method only: here the observer does the model selection, not the analyst.
- Filed: [THEORY-tmpbqbnn](../theory.d/THEORY-tmpbqbnn.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **One task**: azimuth, five positions, 19 analysed subjects, brief
  stimuli.
- **p_common is fitted, not explained**: the model says nothing about how
  the prior over causal structure is set or learned.
- **Experiment 2 is weaker evidence**: a fit to another lab's group data
  with two parameters imported and two fitted by least squares.
- **Rival decision rules**: only a MAP response rule is compared; a rule
  that commits to the more probable structure, or probability matching, is
  not in Table 1. Comparison is by likelihood ratio with AIC/BIC, apart
  from the split-half check.
- **Optimality is a modelling stance**, and there is no neural test; the
  Discussion calls a neural implementation "an important step".

## Open questions

- Does an averaging observer predict held-out conditions better than one
  that commits to the more probable causal structure? A per-subject
  comparison including that rule would tell.
- How is p_common learned across contexts? That is where a model of this
  kind would become hierarchical in A's section 1 sense.
