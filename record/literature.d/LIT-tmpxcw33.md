---
status: Active
status_note: >-
  read 2026-10-16 ([NOTE-tmp24z3z](../notes.d/NOTE-tmp24z3z.md)) in full, from the NIH author manuscript in PubMed Central. Worth reading as the source of the extinction hypothesis for the completely locked-in state: none of seven patients who began BCI training already in CLIS reached yes/no communication, and the authors propose that losing the perceived contingency between a response and its consequences, with reward blunted by artificially held homeostasis, extinguishes goal-directed thinking while passive sensory processing stays intact. Read it knowing that the hypothesis rests on seven heterogeneous patients and an analogy with curarized rats whose result failed to replicate, that it is stated as "might be responsible", and that it predicts its own exception: a contingency learned before CLIS and carried into it should prevent extinction.
title: 'Brain–computer interfaces and communication in paralysis: Extinction of goal directed thinking in completely paralysed patients?'
version: 2
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed, not read. Citation checked against Crossref and OpenAlex on 2026-10-16. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-16, commit d1573d2) for the authors and the title found nothing.
- version: 2
  date: '2026-10-16'
  note: >-
    Read in full (NOTE-tmp24z3z) from the NIH author manuscript in PubMed
    Central (PMC2644824), fetched as XML through NCBI E-utilities because
    the PMC page returned a bot check. Status moved from Deferred to
    Active. The summary is rewritten from the reading: the seven CLIS
    patients were in CLIS when training began, the mechanism is lost
    response–outcome contingency plus blunted reward, passive sensory
    processing is said to be intact, and the hypothesis carries its own
    proviso about contingencies learned before CLIS. The abstract-only
    caveat is replaced by takeaways, and "Why this is here" is corrected
    accordingly. PMC gives the e-publication date as 27 September 2008;
    `published` keeps the Crossref date.
tags:
- neuroscience
- learning-and-conditioning
- cognition
date: '2026-10-16'
published: '2008-09-28'
doi: '10.1016/j.clinph.2008.06.019'
first_author: 'Kübler'
keywords:
- 'brain–computer interface'
- 'locked-in syndrome'
- 'completely locked-in state'
- 'amyotrophic lateral sclerosis'
- 'extinction'
- 'goal-directed thinking'
implementations: []
summary: >-
  Kübler & Birbaumer (2008). Across 35 patients trained with EEG BCIs, paralysis explained performance (η² = .40) only because of the seven in the completely locked-in state, none of whom, having entered training already in CLIS, reached yes/no communication; without them η² = .12, n.s. Evoked potentials showed hearing and some semantic processing intact. The authors propose that lost perception of the contingency between a response and its consequences, with reward blunted by artificially held homeostasis, extinguishes goal-directed thinking; predict that a contingency learned before CLIS and carried into it should prevent this; and say one CLIS patient who learns to communicate would disprove it.
supports:
- CLAIM-tmpki5gp
---

# LIT-tmpxcw33: Brain–computer interfaces and communication in paralysis: Extinction of goal directed thinking in completely paralysed patients?

Kübler, A. & Birbaumer, N. (2008). *Clinical Neurophysiology* 119(11):2658–2666. doi:10.1016/j.clinph.2008.06.019. Open copy: PMC2644824 (NIH author manuscript).

## Key takeaways

*From the reading, [NOTE-tmp24z3z](../notes.d/NOTE-tmp24z3z.md).*

- **The pattern.** Performance is flat from minor impairment to the
  locked-in state and collapses in CLIS: 5 of 7 CLIS patients at chance,
  2 at 59% and 62%, below the 70% needed for yes/no. All seven were in
  CLIS "at the beginning of training".
- **What survives.** All CLIS patients had the N1-P2 auditory response; all
  but one discriminated oddball tones; two lacked the semantic N400. Vision
  was not assessed.
- **The mechanism.** Patients in CLIS "may loose the perception of the
  contingency between the required physiological behaviour ... and its
  consequences", and reward loses value because feeding and ventilation
  keep the body from homeostatic imbalance. "passive sensory information
  processing is intact in CLIS"; "It is the complete lack of motor control
  and feedback which might be responsible for the cessation of voluntary
  cognitive activity, goal directed thinking and imagery".
- **Its own exception.** "learning BCI-control or any other contingency
  before onset of CLIS, which can be transferred from LIS to CLIS should
  prevent extinction in CLIS."
- **Refutation condition.** "A single CLIS patient who learns to
  communicate with a BCI or any other communication method will disprove
  our hypothesis."

## Why this is here

The empirical form of [CLAIM-tmpki5gp](../claims.d/CLAIM-tmpki5gp.md) and the hinge of [CASE-tmpxgcq2](../cases.d/CASE-tmpxgcq2.md). The reading confirms the split [QUESTION-tmpr5tck](../questions.d/QUESTION-tmpr5tck.md) draws: the hypothesis concerns contingency between a response and its outcome, and the authors say outright that passive sensory processing, the arrival of evidence the patient did not select, survives. So it is evidence that action carries the contingency that keeps goal-directed activity going, not that action is the loop's route to unselected evidence. It is weaker than [CLAIM-tmpki5gp](../claims.d/CLAIM-tmpki5gp.md)'s paragraph suggests: a hypothesis ("might be responsible") from seven patients, one probably in a disorder of consciousness, by analogy with a curarized-rat result that failed to replicate. And it does not test [CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md)'s defeater (b), since what failed was acquiring a new operant skill, with consciousness not shown to be otherwise preserved. Chaudhary et al. ([LIT-tmpzuemc](LIT-tmpzuemc.md)) is the case that answers it, but that patient had learned a BCI before CLIS, which is the exception this paper predicts.
