---
number: 499
status: Read
formerly:
- NOTE-tmpdsg4z
paper: LIT-644
title: 'Distinct ventral stream and prefrontal cortex representational dynamics'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the PMC author manuscript (CC BY) as JATS XML:
    every section of the main text and the STAR Methods, with the
    exemplar-reliability (IR, GR) formulas skimmed. Figures and the
    supplementary figures and tables were not seen; their content is
    taken from the text. Predictions attributed to IIT and GNWT are taken
    as the paper reports them from the COGITATE protocol.
date: '2026-10-03'
summary: >-
  In 430 visually responsive subdural electrodes from 10 patients, HFA
  (70–150 Hz) amplitude and category selectivity fell about 80% from peak
  by 800–900 ms while images stayed on. Ventral temporal decoding stayed
  near ceiling (face–watch AUC 99.8%), generalised across time, and ended
  about 230–450 ms after offset at every duration. Prefrontal and parietal
  decoding (peak AUC 84–86%) was confined to about 150–600 ms and ignored
  duration. Exemplar geometry was sustained only in ventral temporal
  cortex.
---

<!-- inactive-ok-file: THEORY-023 — Proposed; named as an account this reading bears on, not tested -->

# NOTE-499: Distinct ventral stream and prefrontal cortex representational dynamics

## Contribution

Most searches for the neural correlates of consciousness look at onsets
or at seen-versus-unseen contrasts with degraded stimuli. This paper
varies how long a clearly seen image stays on, with no report on the
analysed trials, and follows the *content* of activity over time and not
only its magnitude. It shows that sustained content lives in a stable
population code in ventral visual cortex while local activity decays,
and that prefrontal content is a transient onset burst.

## Key insight

Amplitude and content come apart. A region can quiet down by four fifths
while keeping a pattern that a fixed readout decodes as well at the end
as at the start. So "the response faded" does not mean "the
representation faded". What lasts as long as the percept is a fixed
direction in population space, which the authors call an "experience
subspace", and not the level of firing.

## Assumptions

- **Participants**: 10 patients with intractable epilepsy (4 female, age
  19–65), 64–128 subdural electrodes each, 8 of 10 right hemisphere only;
  electrode placement clinical.
- **Stimuli and task**: greyscale images about 5° in size, of faces (about
  30%), watches (about 30%), other objects, animals and rare targets;
  durations 300–1,500 ms. Patients pressed a key only for targets
  (clothing, or a late blur in a dual task, together about 10% of trials);
  target trials were not analysed.
- **Signal**: HFA, 70–150 Hz, the mean of eight normalised 10 Hz
  Hilbert-amplitude bands, baseline-corrected and smoothed over 50 ms,
  taken as a proxy for local firing.
- **Electrode selection**: responsive if HFA differs from baseline in any
  of four 200 ms windows for any category (Bonferroni across windows, FDR
  across electrodes), without regard to category or timing: 430 of 907
  noise-free electrodes.
- **Pooling**: the main multivariate analyses pool electrodes across
  patients into one pseudo-population per region, with single-patient
  checks in the supplement.
- **Decoding**: regularised LDA per time point, five-fold cross-validation
  repeated five times, AUC, cluster-based and max-statistic permutation
  tests; 92 images seen by all patients for 900 ms or more.

## Key results

- **Attenuation** (Fig. 1). Mean attenuation of HFA from peak to
  800–900 ms is 81.8% ± 1.1% across Occ, VT, Par and PFC; category
  selectivity (η²) falls 77.4% ± 1.1%. Of 430 responsive electrodes, 236
  are category selective.
- **Trajectories** (Fig. 2). Multivariate distance from baseline falls by
  about 80%, but in VT and Occ it separates by duration shortly after the
  shorter stimulus ends; PFC and Par trajectories do not.
- **Category decoding** (Fig. 3). Peak AUC: VT 99.6%, Occ 98.1%, PFC
  84.1%, Par 86%. Face–watch AUC averaged over 100–900 ms: VT 99.8%, Occ
  92.4%. In PFC and Par significant decoding is mostly 150–600 ms. The
  temporal generalisation matrix is square in VT (time-invariant code),
  not in PFC or Par. Controls for ocular-muscle artefacts (on OFC
  electrodes), using all PFC electrodes rather than responsive ones, and
  subsampling VT and Occ to PFC electrode counts leave the pattern
  unchanged. Category information is stronger in OFC than in LPFC.
- **Duration** (Fig. 4). VT information outlasts offset by about 450 ms
  for 300 ms images and 230 ms for 900 and 1,500 ms images; 900−300 and
  1,500−900 contrasts are significant in VT and Occ (cluster p < 0.006)
  and not in PFC or Par (p > 0.2).
- **Exemplars** (Fig. 5). On 60 images seen at least twice by 5
  patients, item and geometry reliability are sustained and stable in VT
  through 900 ms, also after partialling out category models; less robust
  in Occ; transient and weaker in PFC and Par (IR significant in both; GR
  only in Par, not after removing category structure).
- **Theory predictions**. IIT (stable, duration-long posterior
  representation) and GNWT (transient prefrontal onset ignition without a
  sustained component, absent report) are both met. GNWT's predicted
  offset ignition was not seen.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In ventral temporal cortex, category and exemplar content of a seen image is represented in a time-invariant population code for as long as the image is on, while amplitude falls about 80% | strong for VT categories; moderate for exemplars (5 patients, 60 images); weaker in Occ | Figs. 1, 3–5 |
| C2 | Prefrontal and parietal cortex carry category and exemplar content transiently after onset, without report and not tracking duration | moderate: few PFC electrodes, mostly one hemisphere; absence of sustained PFC coding is a null result | Figs. 3–5; Limitations |
| C3 | The multi-duration predictions of IIT and GNWT for this paradigm are both confirmed, and are not adversarial | moderate as stated; GNWT's offset ignition was not found | Discussion |
| C4 | Sustained experience may rely on sensory representation and discrete updating on frontoparietal representation | weak: a conditional interpretation | Discussion, Conclusion |
| C5 | Perceptual quality is fixed by the population's position in a stable "experience subspace", not by response amplitude | speculative: a proposal | Discussion |

## Concepts

- **HFA (high-frequency activity)**: 70–150 Hz broadband amplitude, a
  proxy for local firing.
- **temporal generalisation matrix (TGM)**: decoding accuracy for every
  pair of training and testing times; a square block means a stable code.
- **item reliability (IR) / geometry reliability (GR)**: the paper's
  repetition-based measures of whether each exemplar's position, and the
  whole dissimilarity structure, recur across presentations.
- **experience subspace**: the authors' name for the stable subspace of
  population activity that keeps category and exemplar distinctions while
  other dimensions vary.
- **no-report**: analysed trials need no response; here they were still
  task-relevant, since each image had to be judged a non-target.

## Connections

- **Dennett & Kinsbourne 1992 ([LIT-431](../literature.d/LIT-431.md), [NOTE-367](NOTE-367.md)).** Cited as the
  paper's ref. 2, for colour phi and postdiction. The paper sets discrete
  against continuous perception; [NOTE-367](NOTE-367.md) records Dennett and
  Kinsbourne's argument that the Orwellian and Stalinesque readings of
  colour phi cannot be told apart, which this paradigm does not address.
- **Oizumi et al. 2014 ([LIT-445](../literature.d/LIT-445.md)).** IIT 3.0. The paper tests a COGITATE
  prediction attributed to IIT (a sustained posterior hot zone), not Φ or
  any postulate.
- **Butlin et al. 2023 ([LIT-056](../literature.d/LIT-056.md)).** Its GWT indicators derive from the
  workspace theory whose ignition prediction holds here.
- **Verzhbinsky et al. 2026 ([LIT-633](../literature.d/LIT-633.md)).** Also human intracranial
  high-frequency signals, but about co-occurrence across regions, not
  representation within them.

## Bearing on the record

- **[THEORY-023](../theory.d/THEORY-023.md).** It holds that theory-derived indicators presuppose the
  disputed theory. This reading shows two rival theories making
  compatible predictions in one paradigm; the predictions were tested, but
  the theories were not discriminated. It neither supports nor contradicts
  [THEORY-023](../theory.d/THEORY-023.md)'s claim about AI.
- A candidate THEORY: in human visual cortex the content of a sustained
  percept is carried by a stable population code, not by sustained
  activity level. One source; a second (Podvalny et al. 2017, cited here,
  not in the record) would strengthen it.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Sparse and lateralised PFC coverage**; the authors warn that the
  absence of sustained prefrontal activity should be taken "with more
  caution than the presence of activity".
- **Only seen stimuli.** Without unseen or rivalrous stimuli, nothing
  shows that the sustained VT code is specific to experience; the
  authors propose binocular rivalry as the next test.
- **One frequency band.** PFC could hold the percept in low-frequency
  activity or silent synaptic states, which HFA does not measure.
- **Pooled pseudo-populations** across patients for the main analyses.
- **"Representation" is correlational** in the authors' own definition:
  patterns that correlate with stimulus descriptors, with no mechanistic
  role implied.
- **Task relevance.** Analysed trials needed no response but needed a
  non-target judgement, so they are not task-free.

## Open questions

- Does the VT code track the percept when percept and input come apart,
  as in rivalry, or when an image is present but unseen?
- Is there a sustained prefrontal representation in bands or sites not
  sampled?
- How does an "experience subspace" relate to representational drift over
  longer timescales, which the authors raise and leave open?

## Corrections

- none to a seeded skim (there was no seed)
