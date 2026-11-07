---
number: 951
status: Read
formerly:
- NOTE-tmp4xxvp
paper: LIT-1200
title: 'Chaudhary et al. — intracortical spelling in a completely locked-in patient'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the publisher's open-access PDF (Nature
    Communications 13:1236, CC BY 4.0, 9 pages), fetched from nature.com
    and extracted with pdftotext -layout: abstract, introduction, Results,
    Discussion, Methods, data and code availability, figure captions,
    acknowledgements and author contributions. The reference list was
    scanned. Figures were read from captions and the numbers in the text;
    the Supplementary Information (Figs. S1–S4, Supplementary Note 1 on
    the EOG analysis, videos) and the peer review file were not read. The
    article page on nature.com and Crossref were checked on 2026-10-16 for
    an editor's note, correction, expression of concern or retraction;
    none was found.
date: '2026-10-16'
summary: >-
  A man with ALS (born 1985), who had used an eye-movement BCI with an
  auditory speller until February 2019 and was judged completely locked-in
  from a few weeks before implantation in March 2019, was given two 64-
  channel arrays in left motor cortex. Attempted and imagined movements
  gave no usable signal; from day 86 he was given auditory feedback of
  firing rate, matched target tones from day 98, and from day 106 spelled
  with the same speller he had used before CLIS. Over days 106–462 he
  produced intelligible text on 44 of 107 days on which spelling was
  attempted, at about 1 character per minute.
---

# NOTE-951: Chaudhary et al. — intracortical spelling in a completely locked-in patient

## Contribution

A single-case report that a person with ALS, classified by the authors as
in the completely locked-in state (CLIS), produced self-chosen words and
sentences through an intracortical BCI. The enabling step was not
decoding of an intended movement, which failed, but operant training: the
patient heard a tone whose pitch followed the firing rate of one to four
channels and learned to raise or lower it, and a held high or low tone
answered "yes" or "no" to letters read out by a synthetic voice.

## Key insight

Communication came back through a newly built contingency. Nothing
pre-existing in the motor cortex carried the patient's intent: "when we
instructed the patient to attempt or imagine hand, tongue, or foot
movements, we could not detect consistent responses". What worked was an
arbitrary neural variable made audible and reinforced, with an "additional
reward sound" when he held the tone on target. The speller itself was the
one he had used while he could still move his eyes, so what he carried
into CLIS was a learned task, re-attached to a new output.

## Assumptions

- **CLIS by the absence of communication.** "no universally accepted
  clinical definition exists to distinguish LIS from CLIS; the current
  standard criteria to differentiate LIS from CLIS is the presence or
  absence of means of communication" (p. 6). Here, extensive EOG
  recordings found no usable neuromuscular output, and caretakers and
  family "denied the existence of any possible reliable communication from
  February 2019 onwards" (p. 6).
- **CLIS was recent.** "we conclude based on our reported measurements
  that the patient described was in a CLIS a few weeks before and also
  after implantation" (p. 6). The last successful EOG-BCI communication
  was in February 2019; implantation was in March 2019 (p. 7).
- **Not excluded.** "even more sensitive measurements of somatic-motor
  control could reveal some form of volitional control, which would render
  the diagnostic statement of CLIS at least for this case inaccurate"
  (p. 6). Post-hoc EOG analysis still found significant yes/no differences
  in eye-movement features after he could no longer use the EOG system
  (p. 6).
- **Intelligibility rated by authors.** Speller output was rated by three
  of the authors (UC, IV, JZ); an intelligible phrase is one whose meaning
  "the family or experimenter identified and agreed upon" (p. 8).

## Key results

- **History before implantation** (Methods, p. 7). Diagnosed August 2015
  (progressive muscular atrophy, a non-bulbar ALS variant); lost speech and
  walking by end of 2015; ventilated since July 2016. Used an eye-tracker
  from August 2016 until August 2017, then a family paper-based scheme on
  eye movements. He "anticipated complete loss of eye control and asked
  for an alternative communication system". From February 2018 he used a
  non-invasive EOG-based BCI with auditory letter selection (Tonin et al.
  2020), "until February 2019". He gave informed consent to surgery
  "using his eye movements for confirmation", before he "transitioned into
  CLIS" (p. 7).
- **Implantation and failure of direct decoding** (p. 2). Two 8×8 arrays
  in hand-area primary motor cortex and supplementary motor area, March
  2019. Eye-movement strategy, attempted and imagined movement: no
  classifiable signal. Passive movement of his fingers, thumb and wrist
  evoked consistent modulation.
- **Neurofeedback** (pp. 2–4). From day 86, auditory feedback (120–480 Hz
  tone mapped from normalized spike rate). He modulated the tone "on his
  first attempt on day 86", matched targets "for the first time on day
  98", and spelled from day 106. In the 281 neurofeedback blocks preceding
  speller blocks (days 123–462), 4936 of 5700 trials (86.6%) were correct;
  median pre-speller accuracy 90.0%, minimum 50.0% (chance); below 80% in
  17.1% of sessions. Firing rates varied considerably within a day,
  "necessitating manual recalibration throughout the day".
- **Spelling** (pp. 4–5). Sessions on 135 days; spelling attempted on 107,
  intelligible output on 44 (Fig. 4); not attempted on 28 for failing the
  neurofeedback criterion. Intelligible messages: 5747 characters in 5338
  minutes, 1.08 characters per minute (range 0.2–5.1); information
  transfer 5.2 bits/minute on average. Spearman correlation of
  neurofeedback accuracy with speller intelligibility 0.282. First copy
  spelling: his own, his son's and his wife's names.
- **What he wrote** (pp. 4–6). Care requests ("head always straight",
  "everybody must use gel on my eye more often"), food, music ("I would
  like to listen to the album by Tool loud"), suggestions for the speller,
  and messages to his four-year-old son ("Do you want to watch Disney's
  Robin Hood with me").
- **Vision** (pp. 2, 7). "With ALS progression, the patient lost the
  ability to open his eyes voluntarily as well as visual acuity"; "the
  patient reported low visual acuity caused by the drying of the cornea".
  The system is "independent of vision". Hearing was intact enough for the
  auditory speller; no audiometry is reported.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A patient without usable eye or muscle output spelled self-generated sentences through an intracortical BCI | moderate | one patient; 44/107 days intelligible; ratings by authors; data and code deposited |
| C2 | The patient was in CLIS | moderate | EOG and family report; authors concede more sensitive measures might find residual control; post-hoc EOG differences remained |
| C3 | Neurofeedback, not movement decoding, made control possible | moderate | attempted/imagined movement failed for 86 days; feedback succeeded on first attempt |
| C4 | Brain-based volitional communication is possible in CLIS, upending extinction and cognitive-dysfunction hypotheses | weak to moderate | inference from C1–C2 for one recently transitioned patient with prior BCI training |
| C5 | Lack of somatic feedback, disease or arousal changes may explain weak, intermittent control | weak | discussion, no test |

## Concepts

- **Spike rate metric (SRM).** Threshold crossings counted in 50 ms bins,
  averaged over the past second, per channel; normalized, mixed over
  selected channels and mapped to tone frequency.
- **Feedback with / without reward.** Tone-matching blocks; in the second,
  holding the tone on target for a set time triggers a 250 ms reward
  sound.
- **CLIS.** As above: by the authors' account, defined clinically by the
  absence of any means of communication.

## Connections

It is the test case for Kübler and Birbaumer's extinction hypothesis
([LIT-1199](../literature.d/LIT-1199.md), read in [NOTE-948](NOTE-948.md)), whose senior author is senior
author here. It continues the group's EOG-based communication work with the
same patient (Tonin et al. 2020, cited as ref. 22; the Methods' "Tonin et
al.21" appears to be a misnumbering, since ref. 21 is Kübler and Birbaumer)
and contrasts itself with intracortical BCIs in people who kept some muscle
control (Jarosiewicz, Pandarinath, Willett, Vansteensel). The decision not
to change the decoder rests on learning principles (Birbaumer, Ruiz and
Sitaram 2013).

## Bearing on the record

- **The extinction hypothesis, in the authors' words.** Introduction
  (p. 2): hypotheses for CLIS failure range "from extinction of
  intentions21 related to protracted loss of sensory input and motor
  output, cognitive dysfunction, particularly when it occurs in
  association with fronto-temporal degeneration. A successful
  demonstration of any BCI enabling an individual without reliable
  eye-movement control and with eyes closed (CLIS) to form a complete
  sentence would upend these hypotheses". Discussion (p. 6): "The present
  BCI communication demonstrates that an individual unable to move for
  protracted periods is capable of meaningful communication." They treat
  the case as refuting it. Three things weigh against that:
  - *The paraphrase drifts.* The 2008 hypothesis was loss of perceived
    response–outcome contingency; here it is "extinction of intentions ...
    related to protracted loss of sensory input and motor output", which
    adds sensory input the 2008 paper said was intact.
  - *The case fits the hypothesis's own proviso.* Kübler and Birbaumer
    predicted that "learning BCI-control or any other contingency before
    onset of CLIS, which can be transferred from LIS to CLIS should prevent
    extinction". This patient used an EOG BCI with an auditory speller for
    a year before CLIS, and "The speller system described here ... is
    identical to the one used previously when he was still in control of
    eye movements" (p. 8). So he is not the 2008 refuter, a patient who
    learns while already in CLIS, but the 2008 prediction confirmed.
  - *CLIS was weeks old, not "protracted".* By the authors' own dating he
    was in CLIS "a few weeks before" implantation, and training began on
    day 86. That is about four months without communication, far from the
    "longer time periods in CLIS" the hypothesis concerns.
  The authors themselves keep the mechanism in play: they did not change
  the decoder because "such a substantial change in the procedure might
  impede or extinguish the successful control" (p. 6), and they suggest
  "Lack of any somatic sensory feedback, especially that from muscles,
  might impede voluntary modulation of neural activity" (p. 7).
- **[CASE-107](../cases.d/CASE-107.md).** "Chaudhary et al.'s patient communicated only once
  neurofeedback restored a contingency between intention and outcome" is
  confirmed by the reading, with two additions: he had a prior BCI history
  in LIS (above), and the restored contingency was not with an intended
  movement but with an arbitrary neural variable, after 86 days in which
  instructed attempts and imagery produced nothing classifiable. The
  CASE's "Extinguished or dormant" bullet says the patient "fits the second
  reading"; on the reading, he fits a third, which the 2008 paper itself
  allows: a contingency learned before CLIS and kept in use. On the
  cautions: the article as published carries no editor's note,
  correction, expression of concern or retraction (nature.com and Crossref,
  2026-10-16). The retractions and outside cautions the LIT reports are
  not mentioned in it and were not checked here.
- **[QUESTION-121](../questions.d/QUESTION-121.md).** It states that hearing survives in CLIS "since
  Chaudhary et al.'s patient was trained on auditory feedback". Right for
  this patient, and vision was failing (corneal drying, eyes closed). The
  question's two things do come apart here: the patient kept receiving
  unselected evidence (people talking to him, his son, music he asked for)
  through the period without communication, while the contingency was
  what had to be rebuilt.
- **[CLAIM-342](../claims.d/CLAIM-342.md).** The patient's training loop is anchored the way the
  claim wants: target tones are set by the experimenter, so his attempt
  is scored against something he did not select. The observers' scoring of
  his spelling is weaker: intelligibility was rated by three authors, and
  a phrase counted as intelligible when "the family or experimenter
  identified and agreed upon their meaning" (p. 8). The question paradigm
  with known answers is mentioned in the Methods but its results are not
  reported in the main text.
- **[CLAIM-339](../claims.d/CLAIM-339.md) and [CLAIM-337](../claims.d/CLAIM-337.md).** The channel that carried his
  judgements is an operant contingency on motor-cortex firing, reinforced
  by a reward tone. That is action in active inference's sense at its most
  inward: no movement, no imagined movement, but an output the patient
  drives and hears back. It supports the CASE's asymmetry: evidence of
  lucidity here could only arrive through a contingency the patient
  controls.
- **[CLAIM-341](../claims.d/CLAIM-341.md).** The content of what he wrote, a judgement about what
  he wants for his son and for supper, is lucid judgement after months
  without a working channel. It is not judgement with no action at all,
  since producing it required the rebuilt contingency. Defeater (b) is not
  tested.
- **For the anthology.** No instruction for machine-learning practice.
  An anthology topic on brain–computer interfaces could hold it; the
  record holds it for the extinction question.

## Limitations

- One patient, in CLIS for weeks rather than years, with prior BCI
  training; residual control below the EOG's sensitivity not excluded.
- Control was intermittent: intelligible output on 44 of 107 attempted
  days, with daily manual recalibration.
- Intelligibility judged by authors and family; no blinded scoring of
  speller output is reported.
- Supplementary materials, including the EOG analysis behind the CLIS
  classification, were not read for this note.

## Open questions

- Would a patient in CLIS for years, with no prior BCI, learn the same
  neurofeedback task? That is the 2008 hypothesis's real test.
- Did the patient's control depend on the reward tone (operant) or would
  plain feedback suffice?
