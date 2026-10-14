---
status: Read
paper: LIT-973
title: 'Cogitate Consortium — Adversarial testing of GNWT and IIT'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the open-access PDF at nature.com (21 pages),
    text extracted with pdftotext: abstract, introduction, the three
    prediction sections, Discussion, Methods (participants, design,
    acquisition, preprocessing, decoding, duration models, RSA,
    connectivity, gPPI, putative NCC), and the captions of Figs. 1–4,
    Extended Data Figs. 1–7 and Extended Data Tables 1–3. Figure panels
    and the bodies of the Extended Data tables were not read as images.
    The Supplementary Information was not read, including sections 12–13,
    where the two theories' proponents give their own interpretations.
    The preregistration (OSF 92tbg) was not read.
date: '2026-10-14'
summary: >-
  A preregistered adversarial test of IIT and GNWT in 256 people (fMRI,
  MEG, iEEG) viewing clearly seen images. Category, identity and
  orientation were decodable in posterior cortex; prefrontal cortex held
  category, no identity, and orientation only weakly in MEG. No prefrontal
  site showed the predicted offset ignition. Sustained gamma
  synchronization within posterior cortex, IIT's distinctive prediction,
  was not found. Each theory passed some predictions and failed others.
---
<!-- inactive-ok-file: QUESTION-061 — Deferred; the question this work was filed for, on a set-aside line -->
<!-- inactive-ok-file: THEORY-102 THEORY-096 THEORY-098 THEORY-094 THEORY-023 THEORY-tmp7j1bc THEORY-tmpztbz7 — Proposed; the onset-transient finding this result replicates in part, the workspace and sensory accounts it tests, the accounts of what consciousness evidence can settle, and the two accounts filed from this reading -->

# NOTE-tmpuu1fr: Cogitate Consortium — Adversarial testing of GNWT and IIT

## Contribution

This is the first large preregistered adversarial collaboration on
theories of consciousness. The proponents of integrated information
theory (IIT) and of global neuronal workspace theory (GNWT) agreed in
advance on divergent predictions, pass and fail criteria and
interpretations. Theory-neutral teams then collected and analysed data in
three modalities across several laboratories. The results challenge one
central prediction of each theory: IIT's sustained posterior
synchronization, and GNWT's offset ignition and prefrontal representation
of all conscious content. They confirm others.

## Key insight

A theory of consciousness meets data through its proposed biological
implementation, not through its core. IIT's core is integrated
information and GNWT's is the global workspace. What can be tested are
the claims that the maximum of integrated information lies in posterior
cortex, and that prefrontal cortex is the workspace hub. So a failed
prediction challenges an implementation, and "theorists could respond to
challenging data by modifying the proposed biological implementation
while retaining the mathematical or computational core". The design gets
its force from clear signals. Every stimulus was clearly seen and fully
attended, so a missing effect cannot be blamed on weak input.

## Assumptions

- **Suprathreshold, clearly seen stimuli.** Faces, objects, letters and
  false fonts, 20 identities each, in three orientations (front, left,
  right) and three durations (0.5, 1.0, 1.5 s). Seeing was confirmed in a
  separate experiment with a surprise memory test.
- **Experience tracks the stimulus.** The design assumes the experience
  has the stimulus's category, identity and orientation for as long as it
  is on. The Mona Lisa example (Fig. 1b) states it. Percept and stimulus
  never come apart.
- **Task relevance as the control for report.** Participants reported
  only rare targets. Analyses focus on task-irrelevant stimuli, and
  orientation and duration were always task-irrelevant.
- **Theory-defined ROIs.** Posterior "hot zone" for IIT and prefrontal
  cortex for GNWT, fixed in advance with the proponents.
- **Signals.** High gamma (70–150 Hz) for iEEG as a proxy for spiking,
  source-reconstructed MEG, and BOLD.
- **Lenient falsification.** "Evidence for any tested feature ... was
  sufficient to rule out failure, rather than requiring consistency across
  all features."

## Key results

Samples: fMRI n = 120 (73 in the replication set), MEG n = 102 (65), iEEG
n = 34 patients (29 to 31 per analysis). MEG and fMRI analyses were
tuned on one third and run on the remaining two thirds. iEEG was not
split.

**Prediction 1, decoding of content.**
- *Category* (faces against objects) generalised across tasks in both
  regions. iEEG: more than 95% in posterior ROIs for about the stimulus
  duration, about 70% in prefrontal ROIs but limited to about 0.2–0.4 s.
  fMRI searchlight: about 75% in striate, extrastriate, ventral temporal
  and intraparietal cortex, about 60% in middle and inferior frontal
  cortex.
- *Orientation* of faces, always task-irrelevant: decoded in posterior but
  not prefrontal ROIs.
  - iEEG: about 95% with pseudotrials; prefrontal null, BF01 = 5.11–8.65.
  - fMRI: about 45% posterior, chance 33%. 34–55% of prefrontal voxels
    support the null (BF01 3–71.5), and only 1–9% the alternative.
  - MEG: about 75% posterior, a weak 35% prefrontal, "with a possibility
    of signal leakage from posterior regions".
- *Adding prefrontal ROIs* to posterior ones did not improve decoding and
  sometimes reduced it. iEEG BF01 = 1.94 × 10⁴ (face–object), 1.91 × 10⁵
  (letter–false font), 1,205 (orientation). MEG BF01 3.05–4.70.

**Prediction 2, maintenance over time.**
- *Activation* (iEEG high gamma, LMMs on three windows).
  - 25 of 657 posterior electrodes tracked duration: 12 independent of
    category, mostly early visual, and 13 category-specific, mostly in
    ventral temporal cortex. Only 8 of 53 face-selective electrodes (15%)
    were sustained; most were transient at onset.
  - Prefrontal: 99 electrodes gave non-selective onset responses and 24
    category-selective ones. "None of the 655 electrodes measured the
    temporal profile predicted by GNWT (that is, onset and offset)", with
    BF01 > 3 for every prefrontal electrode. The same model found the
    onset–offset pattern in 10 striate or extrastriate electrodes, so the
    null is not a failure of the analysis.
  - An exploratory decoding of duration found one inferior frontal sulcus
    electrode with the GNWT pattern, at 0.15 s rather than 0.3–0.5 s.
- *Representation* (cross-temporal RSA, 1.5-s trials, iEEG).
  - Posterior: a sustained face–object distinction, fitting the IIT model
    better than the GNWT model. Object identity sustained (also letters
    and false fonts), but not face identity. Face orientation appeared
    weakly at onset and decayed after about 0.5 s, "contrary to the
    predictions of IIT".
  - Prefrontal: category transient at onset, none at offset, even in the
    task-relevant condition. No identity information at all. No
    orientation information.
  - MEG supported neither theory on category, identity or orientation.

**Prediction 3, interareal connectivity.**
- *PPC (preregistered).*
  - iEEG: category-selective sites synchronised with V1/V2 early and
    briefly (under 0.75 s), at 2–25 Hz, "mostly explained by the
    stimulus-evoked response". Gamma-band sustained synchrony was absent
    (BF01 = 1.15–4.9). There was no content-selective PPC with prefrontal
    cortex (BF01 = 2.62–5.32).
  - MEG: early, low-frequency, evoked; gamma BF01 > 3.
  - "Supported neither theory."
- *DFC (exploratory, evoked response removed).*
  - iEEG: brief object-selective coupling with V1/V2, mainly gamma. Face
    coupling with V1/V2 scarce (BF01 = 1.3). Gamma coupling of prefrontal
    cortex with both face- and object-selective sites in GNWT's window.
  - V1/V2 had only 12 electrodes against 472 in prefrontal cortex.
- *fMRI gPPI.* FFA showed face-selective coupling with V1/V2, inferior
  frontal gyrus and intraparietal sulcus, "consistent with predictions from
  both theories". LOC showed none, and 62–94% of prefrontal voxels
  supported the null (BF01 3–7.75).

**The consortium's verdict (Discussion, Extended Data Fig. 7).**
- *IIT.* "The lack of sustained synchronization within posterior cortex
  represents the most direct challenge", being "incompatible with IIT's
  claim that the state of the neural network, including its activity and
  connectivity, specifies the degree and content of consciousness". IIT
  passed the duration prediction, but orientation was not sustained.
- *GNWT.* "The most substantial challenge ... the lack of ignition at
  stimulus offset", "especially surprising given the change in conscious
  experience at the onset of the blank fixation screen". And no identity
  in prefrontal cortex, with orientation only in MEG, "raises the question
  of whether PFC is involved in broadcasting all conscious content ... or
  only a subset".
- No verdict. "We invite readers to weigh the evidence themselves."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Category of a clearly seen image is decodable in both posterior and prefrontal cortex, independent of task | strong | three modalities, cross-task generalisation, Fig. 2 |
| C2 | Face orientation and object identity are represented in posterior cortex and not detectably in prefrontal cortex | strong | iEEG and fMRI with Bayesian support for the null; MEG weak above chance with possible leakage |
| C3 | Prefrontal cortex adds no decodable content beyond posterior cortex | strong | iEEG and MEG model comparison with large BF01 |
| C4 | No prefrontal site shows an onset-and-offset response to a sustained image | strong | 655 electrodes, BF01 > 3 each, with a positive control elsewhere |
| C5 | Posterior cortex sustains a category representation for the stimulus duration, and a minority of its sites track duration | moderate | iEEG RSA and LMMs; MEG did not replicate |
| C6 | Content-specific synchronization between category-selective cortex and V1/V2 is brief and low-frequency, not sustained gamma | moderate | iEEG and MEG PPC with Bayesian support; sparse V1/V2 iEEG coverage |
| C7 | Brief content-specific gamma coupling between prefrontal and category-selective cortex occurs in GNWT's window | weak | exploratory DFC only; preregistered PPC found none |
| C8 | Each theory passes some and fails some preregistered critical predictions | moderate | the integration rules of Extended Data Table 1, applied by the consortium |

## Method

1. Proponents and consortium jointly preregister three predictions with
   pass/fail criteria, weighted by centrality (Extended Data Table 1).
2. Theory-neutral teams collect data in two or three laboratories per
   modality, with one shared paradigm.
3. Optimisation on one third of MEG and fMRI data; the frozen pipelines
   run on the rest. iEEG electrodes pooled across patients into a "super
   participant" for multivariate analyses.
4. Prediction 1: linear SVM decoding with cross-task generalisation,
   searchlight for fMRI, and posterior-against-combined model comparison.
5. Prediction 2: LMMs comparing null, duration, time-window, IIT and GNWT
   models by BIC; cross-temporal RSA correlated with theory-predicted
   matrices.
6. Prediction 3: PPC (preregistered), DFC by Gaussian-copula mutual
   information (exploratory), gPPI in fMRI.
7. Bayes factors throughout to support nulls.

## Concepts

- **Ignition.** In GNWT, brief content-specific prefrontal activity,
  "approximately 0.3–0.5 s" after a change in conscious content, at onset
  and offset, with "activity-silent information maintenance in between".
- **Posterior hot zone.** IIT's proposed site of the maximum of integrated
  information, a "temporo–parietal–occipital" region.
- **Critical prediction.** One whose failure counts against a theory under
  the preregistered weighting; others are "non-critical".
- **Task-irrelevant trial.** A stimulus from the categories not being
  searched for in the block, used to isolate perception from task.
- **Lenient falsification.** One passing feature is enough to avoid
  failure.

## Connections

The design and paradigm come from the consortium's protocol (Melloni et
al. 2023, PLoS ONE) and from Melloni et al. (2021) on adversarial
collaboration. The multi-duration paradigm is shared with Vishne, Gerber,
Knight and Deouell (2023), [LIT-644](../literature.d/LIT-644.md), which the paper cites as one of "two
independent studies using comparable methods" whose prefrontal results
agree with its own. The GNWT predictions follow Dehaene and Changeux; the
IIT ones follow Tononi, Boly, Massimini and Koch (2016) and IIT 4.0
(Albantakis et al. 2023). Tononi, Koch and Dehaene are co-authors, and
the paper declares their commercial interests.

## Bearing on the record

- **[THEORY-102](../theory.d/THEORY-102.md) is replicated in part, and its title is too broad.**
  - [THEORY-102](../theory.d/THEORY-102.md)'s promote_when names "the COGITATE multi-duration
    results" as the obvious second recording. This paper is that: an
    independent intracranial cohort (28 patients for RSA) with 576
    prefrontal electrodes, and it finds what [THEORY-102](../theory.d/THEORY-102.md) states for
    category. A sustained posterior category representation, and
    prefrontal category content confined to onset with nothing at offset.
  - It does not hold for every dimension. Face identity was not sustained
    in posterior cortex, and face orientation decayed after about 0.5 s
    though the image stayed on. [THEORY-102](../theory.d/THEORY-102.md)'s title says "the content of a
    clearly seen, unchanging image is carried for as long as it stays on".
    On this cohort that holds for category and object identity, not
    orientation or face identity.
  - Also, only 15% of face-selective electrodes were sustained; most were
    transient. That fits [THEORY-102](../theory.d/THEORY-102.md)'s "amplitude decays", but the paper
    did not test a stable population code against decaying amplitude in
    the way Vishne et al. did.
  - [THEORY-102](../theory.d/THEORY-102.md) should say "category and object identity", and name
    orientation as not sustained in COGITATE. Its first promote_when kind
    is partly met: replicated for category, not for every dimension.
- **[THEORY-096](../theory.d/THEORY-096.md).** Its promote_when says the account needs "the COGITATE
  results". They count against two clauses as stated.
  - *"Broadcasts that one content."* Prefrontal cortex held the category
    of a clearly seen image but not its identity, and orientation at most
    weakly. The paper asks whether prefrontal cortex broadcasts "all
    conscious content ... or only a subset".
  - *Ignition at a change of content.* No prefrontal site responded at
    offset, though the experience changed there.
  - The "sustains" tension recorded on [THEORY-096](../theory.d/THEORY-096.md) (2026-10-12) is
    confirmed. The proponents predicted activity-silent maintenance
    between onset and offset, and no sustained prefrontal content was
    found.
  - None of this tests ignition without differential post-perceptual
    cognition, the kind of result [THEORY-096](../theory.d/THEORY-096.md)'s promote_when asks for
    first. The stimuli were all seen.
- **[THEORY-098](../theory.d/THEORY-098.md)** (a recurrent sensory basis, prefrontal causal at most).
  The paper is consistent with it. Content in all three dimensions sits in
  posterior cortex, and prefrontal adds nothing decodable. But IIT's
  prediction of sustained posterior gamma synchrony failed, and that
  prediction is about recurrence between high-level areas and V1/V2. So
  the data do not support sustained recurrent coupling as the carrier.
- **[QUESTION-061](../questions.d/QUESTION-061.md).**
  - *The filing overstated it.* [LIT-973](../literature.d/LIT-973.md) was filed as "direct evidence on
    whether access is one all-or-none broadcast". It is not direct. No
    dimension's access was measured, and there was no report on identity
    or orientation.
  - *What it does give.* Posterior cortex carries a seen image's
    orientation and object identity, while the hub carries only its
    category. That is evidence that the prefrontal hub does not receive
    every dimension of a conscious content.
  - *What it cannot say.* Whether an unrepresented dimension is "not
    accessed", in the question's sense, is not tested.
- **[QUESTION-048](../questions.d/QUESTION-048.md).**
  - The design is task-based no-report evidence. The authors concede that
    "some might argue our approach tracks stimulus processing rather than
    consciousness". Percept and stimulus never came apart, so nothing
    here separates experience from processing, much less from access.
    That is [THEORY-094](../theory.d/THEORY-094.md)'s limit.
  - The paper's own reading of what a theory test can do supports
    [THEORY-023](../theory.d/THEORY-023.md)'s evidential point. Tests reach biological
    implementations, not cores, and the field lacks "a formal framework
    ... to quantitatively integrate evidence".
- **Filed from this reading:**
  - [THEORY-tmp7j1bc](../theory.d/THEORY-tmp7j1bc.md): prefrontal cortex carried category but not identity
    or (detectably) orientation, and no site responded at offset.
  - [THEORY-tmpztbz7](../theory.d/THEORY-tmpztbz7.md): no sustained content-specific posterior
    synchronization with early visual cortex.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

The authors name these:
- residual task engagement with category (not with orientation or
  duration);
- no single units;
- a phenomenal richness the design "still falls short of";
- sparse V1/V2 iEEG coverage, 12 electrodes;
- MEG results sensitive to parameter choices, with possible leakage.

The reading adds these:
- iEEG electrodes are pooled across patients, so the region-level
  multivariate results are a pseudo-population.
- Patients with epilepsy, and three below the behavioural criteria, were
  kept.
- The proponents' replies in the Supplementary Information were not read.
- The connectivity result for GNWT depends on which metric is used:
  preregistered PPC found nothing, and exploratory DFC found gamma
  coupling.

## Open questions

- Is orientation maintained by any signal over the image's duration? The
  authors leave it open for IIT.
- Does prefrontal cortex carry identity or orientation in other bands, or
  in single units? The authors point to a separate animal collaboration.
- Would the same tests with percept and stimulus dissociated (rivalry,
  masking) move the results? That is what [THEORY-102](../theory.d/THEORY-102.md), [THEORY-094](../theory.d/THEORY-094.md) and
  [QUESTION-061](../questions.d/QUESTION-061.md) all need.
- How should results be integrated across modalities and predictions?
  The authors call for a quantitative framework and do not provide one.
