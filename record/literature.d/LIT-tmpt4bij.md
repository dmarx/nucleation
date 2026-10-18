---
status: Active
status_note: 'read in full 2026-10-18 ([NOTE-tmpy8fky](../notes.d/NOTE-tmpy8fky.md)), from the publisher''s open-access PDF; worth reading as an organised review of what induces body ownership illusions, from the rubber hand to full bodies in virtual reality, sorted by trigger (visuotactile, visuomotor, visuoproprioceptive) and by the semantic constraints on the fake body (shape, texture, posture, visual perspective, structure), and as the proposal that ownership is Bayesian causal inference over whether one body part or two caused the seen and felt signals. Read it knowing that the review grades evidence mainly by questionnaire scores and never discusses demand characteristics or response bias; that the causal-inference model is two equations and a qualitative mapping, fitted to no data, with an arbitrary threshold and a prior that absorbs suggestibility and previous exposure, so that as stated few results could count against it; that its own predictions are listed as untested; and that it classes the out-of-body illusions of Lenggenhager et al. apart from ownership illusions and reports third-person views abolishing full-body ownership. Filed as [THEORY-tmp5h02h](../theory.d/THEORY-tmp5h02h.md).'
title: 'Over my fake body: body ownership illusions for studying the multisensory basis of own-body perception'
version: 1
history:
- version: 1
  date: '2026-10-18'
  note: >-
    Filed at the owner's request ("file some body ownership illusion
    material"), with the batch that checks the sources of NOTE-372's C6.
    Citation checked against Crossref and OpenAlex on 2026-10-18: Front.
    Hum. Neurosci. 9:141, doi 10.3389/fnhum.2015.00141; Crossref's
    published-online and issued, OpenAlex's publication date and the
    article itself all give 24 March 2015. Not held in the Anthology of the
    SOTA: a grep of its record/ (clone of 2026-10-18, commit d1573d2) for
    "Kilteni", "Maselli", "Over my fake body", "body ownership", "rubber
    hand" and the DOI found nothing. Read in full the same day from the
    publisher's PDF (20 pp., CC BY).
tags:
- self
- neuroscience
- probabilistic-modeling
date: '2026-10-18'
published: '2015-03-24'
doi: '10.3389/fnhum.2015.00141'
first_author: 'Kilteni'
keywords:
- 'body ownership'
- 'rubber hand illusion'
- 'multisensory perception'
- 'body semantics'
- 'causal inference'
implementations: []
summary: >-
  Kilteni, Maselli, Körding & Slater (2015), a review. Body ownership illusions need seen and felt (or seen and moved) events to agree in time, within about 300 ms for touch and below about 500 ms for movement, and at homologous places on the body; a realistic fake body seen in the real body's place can be owned with no such agreement. Spatial offsets are tolerated near the midline and attenuate further out; non-body shapes, implausible postures and a third-person view inhibit the illusion, while size, length, texture and number of limbs are partly tolerated. The authors propose that ownership is Bayesian causal inference: a posterior that one hand (C = 1) caused the visual, proprioceptive, tactile and semantic evidence, crossing a threshold. The model is qualitative and unfitted, and the evidence is graded mainly by questionnaire.
---

<!-- inactive-ok-file: THEORY-tmp5h02h — Proposed; named as this batch's account of body ownership drawn from the review, not leaned on -->

# LIT-tmpt4bij: Over my fake body: body ownership illusions for studying the multisensory basis of own-body perception

Kilteni, K., Maselli, A., Kording, K. P. & Slater, M. (2015). *Frontiers in Human Neuroscience* 9:141. doi:10.3389/fnhum.2015.00141.

## Key takeaways

*From the reading, [NOTE-tmpy8fky](../notes.d/NOTE-tmpy8fky.md).*

- **Three classes of body illusion.** Distortions (Pinocchio, phantom
  nose), out-of-body illusions that move felt self-location toward a body
  seen from behind (Lenggenhager et al. 2007; Ehrsson 2007), and
  ownership illusions, in which a non-bodily object is felt as part of
  one's body and as the source of its sensations.
- **Triggers.** Visuotactile and visuomotor agreement in time and place
  are sufficient for ownership. Delays under about 300 ms (touch) still
  work; delays of about 500 ms or more (movement) and touch or movement at
  non-homologous places abolish it.
- **Position.** Offsets of 10 to over 40 cm are tolerated toward the
  midline; outward offsets and a vertical gap of 43 cm attenuate it. A
  realistic body seen where one's own is can be owned under asynchronous
  touch, or by sight alone, so agreement is "not a necessary prerequisite"
  there.
- **Semantics.** Non-body shapes inhibit; texture modulates; implausible
  postures (a hand rotated 180°) and a third-person view of a body at 40 to
  100 cm abolish full-body ownership; size, a long arm up to three times
  normal, and extra limbs are partly tolerated.
- **The model (Eqs. 1–2).** p(C = 1 | m_V, x_V, x_P, s_V, s_T), with the
  evidence conditionally independent given C, and the illusion felt when
  the posterior crosses a threshold. The prior includes the midline,
  "personality traits including suggestibility to illusory perceptions"
  and previous exposure. It is not fitted to any data.

## Standing in the record

The record's survey of the body-ownership literature as of 2015, filed
to place the batch's primary experiments. It reads Petkova and Ehrsson
([LIT-tmp4qdyy](LIT-tmp4qdyy.md)) as the founding full-body illusion and reports the later
third-person tests that paper lacked. Its classification separates the
self-location illusions [NOTE-372](../notes.d/NOTE-372.md)'s C6 cites from ownership, and its
model is the probabilistic counterpart, without the free-energy
machinery, of the predictive-coding accounts it cites as "conceptual"
(Apps and Tsakiris; Friston). Filed as [THEORY-tmp5h02h](../theory.d/THEORY-tmp5h02h.md). It carries no
instruction for machine-learning practice.
