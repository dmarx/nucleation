---
status: Read
paper: LIT-tmpozu5y
title: 'Lush — Demand characteristics confound the rubber hand illusion'
version: 1
history:
- version: 1
  date: '2026-10-18'
  note: >-
    Read in full from the author's accepted manuscript, the PDF file of
    OSF preprint mpncv (version of 10 April 2020, 32 pp., headed with the
    published citation), extracted with pdftotext: abstract, introduction,
    method, preregistered and exploratory results, discussion, references
    and back matter. Figures 1–2 were read from their captions and the
    text; the plotted values were recomputed. The publisher's PDF
    (online.ucpress.edu) returned a bot check, and the Sussex repository
    copy returned nothing, so the typeset version was not compared. Also
    read: the AsPredicted preregistration (osf.io/89m7j, registered 14
    November 2019) through the OSF API; the questionnaire text, the
    codebook and the supplement (osf.io/9c8mq); the JASP output for both
    analyses. The 62-second video was not watched. From the posted data
    (32 rows) a scratchpad script (readerC_scripts/lush_check.py)
    reproduced the exclusions, the sample, every mean, SD, t and Cohen's
    d, and the item means. It also computed tests the paper does not
    report. The Bayes factors were recomputed with the closed form for a
    normal likelihood and a half-normal prior with SD 1
    (readerC_scripts/bf_variants.py). The cited preprint (Lush et al.
    2019), which supplies the hypnotisability slopes, was not read, nor
    were Riemer et al. (2019) or Orne (1969).
date: '2026-10-18'
summary: >-
  People told about the rubber-hand procedure and shown it, but not given
  it, expect the "illusion" statements far more than the "control"
  statements and the illusion far more after synchronous than asynchronous
  stroking. So neither standard control rules out demand characteristics.
  Preregistered, n = 20; every t and mean reproduces from the posted data,
  which also show the statement-by-synchrony interaction the paper does
  not test. The paper shows unmatched controls, not a suggestion effect,
  and says so. Its abstract and discussion lean further.
---
<!-- inactive-ok-file: LIT-tmpe5zsa — Unavailable, no lawful full text reached; named as the founding rubber-hand study whose controls Lush tests, not leaned on -->
<!-- inactive-ok-file: LIT-tmpz3i32 — Unavailable, no lawful full text reached; named as the drift study whose measure Lush argues is unvalidated, not leaned on -->
<!-- inactive-ok-file: THEORY-tmp5h02h — Proposed; named as this batch's account of body ownership that this result bears on, not leaned on -->
<!-- inactive-ok-file: THEORY-tmpugoyc — Proposed; named as this batch's account of body ownership that this result bears on, not leaned on -->

# NOTE-tmptyehi: Lush — Demand characteristics confound the rubber hand illusion

## Contribution

Before this paper, rubber-hand studies controlled for suggestion by
contrast. Ownership and referred-touch statements were compared with
"control" statements, or synchronous stroking with asynchronous, and the
difference was read as experience not owed to demand. Nobody had measured
whether participants expect those statements or conditions equally. This
paper measures it, with Orne's quasi-control. They do not expect them
equally, by a wide margin, in the direction of the published results.

## Key insight

A contrast controls for demand only if the two sides carry the same
demand. Brush strokes that match in time are an obvious cue for "you will
feel the touch on the rubber hand", and much less for "your hand will turn
rubbery" or "the rubber hand will start to look like yours". So the gap
between illusion and control statements, or between synchronous and
asynchronous stroking, is what expectancy alone would produce. On its own
it cannot tell a multisensory effect from a suggestion effect.

## Assumptions

- **Quasi-control validity.** Ratings of what one *would* expect, made
  after a text and a video, stand in for the expectancies real
  participants form during the procedure (Orne 1969). The paper's check
  is a post hoc question to 7 participants in another study. All 7 could
  say how the two conditions differed (supplement). Those 7 came from
  the top and bottom 20% of a phenomenological-control screen.
- **Expectancy can drive experience, not only compliance.** This is the
  premise that turns unmatched demand into a confound of *experience*.
  Orne and Scheibe, Kirsch, and the hypnosis literature are cited.
- **A student sample is the relevant population.** Of the 20, 11 had heard
  of the procedure. The preregistered analysis kept them, on the grounds
  that rubber-hand participants are typically psychology undergraduates.
- **Fixed statement order.** Each statement was rated for both conditions
  on one page, in Botvinick and Cohen's order. A reviewer raised order
  effects. The defence is that about 80% of the 20 most-cited studies
  used a fixed order (supplement).
- **The rating scale.** The scale is −3 "I am certain I won't feel any
  effect" to +3 "I am certain I will feel some effect". It measures
  expected occurrence, not agreement with the statement. It is matched to
  Botvinick and Cohen's agreement scale in range only.

## Key results

- **Sample.** 32 completed the online study and 12 were excluded under the
  preregistered rules: 6 who read the information page for under 10 s,
  and 6 more of 8 who had taken part in a similar experiment (2 of the 8
  were also too fast). That leaves n = 20 (17 women, mean age 20.8).
  The stopping rule (BF > 6 or < 1/6 after 20) was met at the first look.
  *Checked* from the data. No one fell under the preregistered 4 s per
  statement; the fastest mean was 8.7 s.
- **Illusion against control, synchronous** (preregistered): M 1.68 (SD
  0.91) against −0.03 (1.29), t(19) = 6.24, p < .001, dz 1.40.
- **Synchronous against asynchronous illusion** (preregistered): 1.68
  against 0.43 (1.30), t(19) = 4.68, p < .001, dz 1.05.
- **Intervals** (preregistered prediction: control negative, illusion
  positive). Synchronous illusion [1.26, 2.11]. Synchronous control
  [−0.64, 0.57] and asynchronous illusion [−0.17, 1.04] both span zero.
  The control prediction failed. The paper reports the intervals and
  reads them as the "neither agree nor disagree" pattern of real studies.
  It does not say the prediction failed.
- **Never heard of it** (exploratory, n = 9): 1.93 against −0.15, t(8) =
  6.90, dz 2.30; synchronous against asynchronous illusion 1.93 against
  0.70, t(8) = 5.05, dz 1.68.
- **Item means** (synchronous / asynchronous): S1 2.15 / 0.90, S2 1.40 /
  0.00, S3 (ownership) 1.50 / 0.40; C1 (real hand drifting) 0.20 /
  −0.55, C2 0.40 / −0.55, C3 0.15 / 0.00, C4 −0.15 / −1.10, C5 −0.10 /
  −0.70, C6 −0.70 / −1.35. *Recomputed*, the paper's Figure 2.
- **Not in the paper, from its data.** The illusion-minus-control gap is
  larger for synchronous than for asynchronous expectancies: 1.72 against
  1.14, difference 0.58, t(19) = 3.01, p = .007, dz 0.67. This is the
  interaction that factorial rubber-hand designs treat as the illusion,
  and expectancy shows it. In the n = 9 subsample it is 0.52, t(8) =
  1.93, p = .09. Control expectancies also differ by synchrony (−0.03
  against −0.71, t(19) = 4.25). Among single items, expected drift of the
  real hand (C1) is higher for synchronous stroking (t(19) = 2.32, p =
  .03).
- **Bayes factors.** For the first test the half-normal formula with the
  raw SE gives 3.93 × 10⁷, as reported. The others do not reproduce under
  one method. Synchronous against asynchronous gives 1.43 × 10⁴ against
  the reported 1.14 × 10⁴. The exploratory pair gives 1.6 × 10⁹ and 8.0
  × 10⁴ against the reported 1.48 × 10⁵ and 444.67. With Dienes's
  small-sample SE correction they come to 1.1 × 10⁵ and 503, near the
  reported values. So the method seems to differ between analyses. The
  upper limits of the robustness regions (hundreds) were not reproduced.
  No conclusion depends on it, since every variant is above 100.
- **Free responses.** Asked what the procedure is supposed to cause, most
  of the 20 named felt touch or confusion about it. About five named
  ownership of the fake hand. The ownership expectancy (S3 synchronous,
  16 of 20 above zero) appears when the statement is put to them.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | People who know the procedure expect Botvinick and Cohen's illusion statements more than the control statements under synchronous stroking | strong | preregistered, dz 1.40, n = 20; replicated in n = 9 naïve; reproduced from the data |
| C2 | They expect the illusion more under synchronous than asynchronous stroking | strong | preregistered, dz 1.05; also in the naïve 9; reproduced |
| C3 | So neither standard control rules out demand characteristics in illusion reports | strong as stated, given C1–C2 and the assumption that quasi-control expectancies track real ones | the logic of matched demand; the 7-participant check |
| C4 | The expectancy pattern resembles published post-induction reports | weak | described against Botvinick and Cohen's Figure 1; no numerical comparison |
| C5 | The illusion may be partly or wholly a suggestion effect (phenomenological control) | weak here | not tested in this study; rests on the cited preprint's hypnotisability slopes |
| C6 | Proprioceptive drift and skin conductance are open to the same confound | weak | argument and citations (voluntary and suggested electrodermal change); the drift item's expectancy (C1 above) is the only data, and it is the record's computation |
| C7 | Valid controls must match expectancy and suggestion difficulty | moderate as argument | the hypnosis analogy (magnetic hands 77% against mosquito 26%) |

## Concepts

- **demand characteristics** — "the totality of cues which convey an
  experimental hypothesis to the subject" (Orne 1962).
- **quasi-control / quasi-experiment** — participants given information
  about a procedure, not the procedure, report what they expect (Orne
  1969).
- **phenomenological control** — a general ability to meet expectancies
  by top-down control of experience that is felt as involuntary, in or
  out of hypnosis. Hypnotisability is that ability in a hypnotic context.
- **illusion and control statements** — Botvinick and Cohen's three
  statements (S1–S2 referred touch, S3 ownership) and six others (C1–C6),
  in the paper's Table 1.

## Connections

It applies Orne's quasi-control to a paradigm that never had one. It
draws on Riemer et al.'s (2019) methods review for the observation that
the control items were never validated. It extends the author's group's
preprint (Lush et al. 2019), which reports hypnotisability predicting
rubber-hand ownership reports (slope 0.76 per SWASH point, n = 353) and
drift (0.53 cm per point). Those figures are quoted, not checked.

It names the paradigms its argument reaches: the full-body illusion
(Lenggenhager et al. 2007), enfacement, the tongue illusion, the magnetic
touch illusion, and fMRI correlates (Ehrsson et al. 2005). It compares the
magnetic touch illusion's brushes, moved near the body, to mesmeric
passes.

## Bearing on the record

- **Filed as [THEORY-tmpa88hs](../theory.d/THEORY-tmpa88hs.md).**
- **[NOTE-372](NOTE-372.md), C6** ("Body ownership can be manipulated by multisensory
  conflict"). That row rates the manipulation "moderate ... cited". This
  paper says the paradigm's standard evidence for it does not separate
  the manipulation of the stimulus from the manipulation of expectancy. The
  synchronous/asynchronous contrast that would show multisensory conflict
  doing the work is exactly what expectancy predicts. C6's manipulation
  should be read as "reports and drift shift with visuotactile
  synchrony", and the mechanism as undecided between multisensory
  integration and expectancy. The "simplest form of self-awareness" half
  of C6 is untouched; it was asserted before and remains so.
- **Metzinger ([LIT-450](../literature.d/LIT-450.md), [LIT-568](../literature.d/LIT-568.md)).** The self-model theory cites the
  bodily illusions as showing that global body ownership is the content
  of a transparent self-model that multisensory input can update. If the
  reports are partly or wholly expectancy-driven, they would still show
  that the phenomenal body can be reshaped by context. But they would
  not show that bottom-up multisensory conflict reshapes it, which is the
  use the theory makes of them. The reading is mine; the paper does not
  discuss Metzinger.
- **Active inference ([LIT-1181](../literature.d/LIT-1181.md)).** Expectancy driving felt experience is
  close kin to prediction driving perception. A prior that "I will feel
  the touch on the rubber hand" could pull the percept, and an
  active-inference model has a place for it. So the paper does not tell
  against predictive accounts as such. It tells against using
  visuotactile synchrony alone as their evidence, because synchrony also
  supplies the expectation. My observation.
- **Other works in this batch.** The full-body illusion ([LIT-tmpeggnf](../literature.d/LIT-tmpeggnf.md),
  [THEORY-tmpahbbc](../theory.d/THEORY-tmpahbbc.md)) and body swapping ([LIT-tmp4qdyy](../literature.d/LIT-tmp4qdyy.md), [THEORY-tmpvh682](../theory.d/THEORY-tmpvh682.md)) rest
  on the same questionnaire-against-control-item and
  synchronous-against-asynchronous design, and the paper names the
  full-body illusion. Their implicit measures (walking error, skin
  conductance after threat) are, by this note's claim C6, open to the same confound and untested for it. The
  review's causal-inference account ([LIT-tmpt4bij](../literature.d/LIT-tmpt4bij.md), [THEORY-tmp5h02h](../theory.d/THEORY-tmp5h02h.md)) and
  the free-energy self ([LIT-tmpetw17](../literature.d/LIT-tmpetw17.md), [THEORY-tmpugoyc](../theory.d/THEORY-tmpugoyc.md)) take synchrony to
  be the cause that evidence integrates. This paper says the paradigm's
  data do not yet rule out that synchrony works as a cue to expectation.
  The two founding studies, Botvinick and Cohen ([LIT-tmpe5zsa](../literature.d/LIT-tmpe5zsa.md)) and
  Tsakiris and Haggard ([LIT-tmpz3i32](../literature.d/LIT-tmpz3i32.md)), could not be read.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- **Expectancy is not report.** Nothing here measures what anyone
  experienced, and the author agrees.
- **Similarity to real data is asserted, not computed.** No induction data
  are set beside the expectancies. Expected control ratings sit near 0,
  where Lush describes post-induction control ratings as at or below it.
- **The task makes the contrast salient.** Both conditions for each
  statement were on one page. The introductory text told participants the
  procedure is "used in psychological experiments to generate changes in
  experience". That sentence is in the posted questionnaire, not in the
  passage the paper quotes. A real participant meets the conditions in
  separate blocks.
- **Small, informed sample.** n = 20, 11 of whom had heard of the
  illusion; the naïve subsample is 9. The effects are large enough that
  this hardly matters for C1–C2.
- **Preregistration drift.** The prereg names "five 'control'
  statements", while six were used. Its second hypothesis repeats the
  control-statement wording by slip. The paper writes the control mean as
  "S4-9", "C1-C6" and once "C1-C9". The failed negative-interval
  prediction is not called a failure.
- **The supplement's tally.** The list of "sixteen" fixed-order studies
  names all twenty, including the four it says randomised.
- **The motivating account is elsewhere.** The case that the illusion *is*
  phenomenological control rests on the 2019 preprint, not read here.

## Open questions

- Do expectancies measured *before* a real induction, in the same people,
  predict their synchronous–asynchronous difference in ownership reports
  and drift, and does any difference survive conditioning on them? The
  author's proposed control is to match statements on expectancy and on
  suggestion difficulty, then test. The later published version of the
  2019 preprint and the replies to this paper (Ehrsson's group among
  them) are known to exist and are not in the record.
- Does an implicit measure exist whose expectancy is flat across
  synchronous and asynchronous stroking? The posted data say expected
  drift is not flat.
