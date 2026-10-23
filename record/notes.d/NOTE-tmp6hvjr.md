---
status: Read
paper: 'LIT-tmpzp314'
title: 'Bigand et al. — The geometry of interpersonal synchrony in human dance'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full on 2026-10-23 from PubMed Central (PMC11266842), fetched
    as Europe PMC full-text JATS XML and converted to text by script. It is
    the publisher's text of Current Biology 34(13), 3011–3019.e4, published
    online 21 June 2024, CC BY 4.0. Read: the summary, highlights, all of
    Results and Discussion, the captions of Figures 1–4 and Videos S1–S2,
    and all of the STAR Methods. Figure 2 was viewed as an image (from
    Europe PMC's supplementary-files archive), which names the ten
    movements in each synchrony category. Document S1 was read: the
    captions of Figures S1–S4 and Tables S1–S2. Figures 1, 3 and 4 and S1–S4
    were taken from their captions; the videos were not viewed. The
    reference list was not read. The article has no page breaks in the
    XML, so references below are to sections and figures.
date: '2026-10-23'
summary: >-
  In 35 dyads of untrained dancers facing each other, shared music and
  visual contact were varied independently. Each raised interpersonal
  synchrony, in different principal movements and with no interaction:
  lateral and hand movements synchronized through seeing the partner,
  anteroposterior movements such as head bobs through the shared music,
  and vertical bounce through both. Which factor drove a movement's
  synchrony could be read from its spatial direction (100% classification)
  and not from its periodicity. The direction of coupling between partners
  was not estimated.
---
<!-- inactive-ok-file: THEORY-tmpcd7cz CLAIM-172 CLAIM-167 CLAIM-157 QUESTION-063 QUESTION-084 CASE-045 THEORY-520 THEORY-275 — Proposed or Open; the accounts, claims and questions this reading bears on, named, not leaned on -->

# NOTE-tmp6hvjr: Bigand et al. — The geometry of interpersonal synchrony in human dance

## Contribution

A factorial experiment that separates the two standard explanations of
collective synchrony, response to a shared external cue and adaptation
between individuals, inside one naturalistic human behaviour. Shared music
was switched on or off (same song, or songs 8.5% apart in tempo) and,
independently, visual contact between the two dancers (a curtain). Both
factors raise synchrony, but in different movement components, and their
effects do not interact. The authors also show that the timing of the
synchrony does not reveal which factor produced it; its spatial direction
does.

## Key insight

Synchrony between two bodies is not one quantity. Decompose the movement
and different components are synchronized by different causes at the same
time: "within the same dyad, multiple synchronization processes can occur
simultaneously, exploiting either the presence of a shared sensory input,
or interpersonal adaptation" (Discussion). A measure that sees only timing
treats them as one: "Yet examining (movement) temporal features alone,
social synchrony might appear as a unitary, indivisible phenomenon, even
when it is not."

## Assumptions

- **Linear decomposition of posture.** The 66-dimensional posture vectors
  (22 markers × 3 axes), standardised per trial and pooled over all
  participants, are decomposed by PCA into principal movements (PMs). The
  first 15 explain over 95% of the variance; an autoencoder did little
  better (95.6% against 96.5%). Synchrony is then measured per PM, so the
  result is relative to this basis.
- **Synchrony as period locking.** Synchrony is cross-wavelet power
  between the two partners' PM velocity series, averaged over periods from
  0.5 to 16 beats. It is symmetric between the two partners: it says that
  they are locked, not who follows whom.
- **The manipulations isolate the channels.** "Music-driven" is the main
  effect of hearing the same song; "partner-driven" is the main effect of
  removing the curtain. Partners heard their music through earphones. The
  paper does not say whether other cues between partners (sound of
  movement, floor vibration) were controlled; any such channel would be
  present in both vision conditions and would not affect the contrast.
- **Untrained, familiar pairs.** 40 dyads were recruited and 5 lost to
  recording failure, leaving 70 participants; all were laypersons
  "without dance training", and "All pairs of participants were familiar
  with each other". They stood 2.5 m apart, each in a 0.5 × 0.7 m space,
  facing each other, without touching.
- **Short, structured stimuli.** Eight rearranged songs of 20 bars (about
  40 s), with instruments entering every four bars; synchrony and the
  differences between conditions were greatest in the full refrain.

## Key results

- **Main effects, no interaction.** By time-resolved 2 × 2 ANOVAs per PM,
  Bonferroni-corrected across PMs and cluster-corrected across time, ten
  of 15 PMs showed a main effect. Partner-driven (visual contact): PM1 side
  sway, PM3 twist with hands, PM5 side hands, PM11 side shuffle.
  Music-driven (same music): PM2 vertical hands, PM4 front-back sway, PM8
  upper-body rock, PM9 twist, PM14 head bob. Both: PM10 bounce (Figure 2).
  "we found no evidence of an interaction between musical input and visual
  contact, and this was so for all PMs."
- **The authors' reading of independence.** "even when participants were
  presented with non-synchronous music, some PMs would still synchronize
  with the movements of the dancing partner, just as when participants
  were presented with synchronous music. Conversely, another group of PMs
  would keep synchrony with music, even if the partner was visible and
  moving at a different pace."
- **Geometry.** The main axis of the partner-driven PMs was lateral, of the
  music-driven anteroposterior, of the hybrid vertical (Figure 3A). A
  second-layer PCA over the ten PMs' spatial maps, blind to category,
  gave six eigendirections; four of them (1, 2, 5, 6) predicted the
  synchrony category "with 100% accuracy" under leave-one-participant-out
  cross-validation (Figure 4B).
- **Timing fails.** The same analysis on the periodicity of synchrony gave
  five eigenperiods that "failed to capture any temporal pattern
  characteristic of music- or partner-driven synchronies"; the model on
  the two informative eigenperiods "confused 48% of the data associated
  with music-driven synchrony with partner-driven synchrony" (Figure 4D).
  "Hence, the independence between music- and partner-driven synchrony is
  achieved solely through a spatial, not temporal, organization."
- **Bounce.** Bounce alone synchronized through both factors, alone
  synchronized at the beat (eigenperiod 4), and alone grew in quantity of
  movement when the partners could see each other (Figure S1).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Shared music and visual contact each raise interpersonal movement synchrony in dyadic dance | strong | 2 × 2 within-dyad design, 35 dyads, cluster-corrected ANOVAs (Figure 2, S2) |
| C2 | They act on different movement components, with one (bounce) affected by both | strong for this sample and decomposition | Figure 2A; depends on the PCA basis |
| C3 | The two effects are independent: no movement shows an interaction | moderate: an absence of evidence, not an equivalence test | Figure S2C |
| C4 | The spatial direction of a movement predicts which factor drives its synchrony | strong within the sample | second-layer PCA and classifier, 100% cross-validated (Figure 4B) |
| C5 | The periodicity of synchrony does not distinguish music-driven from partner-driven synchrony | moderate: a negative result for one temporal representation | eigenperiod PCA and classifier (Figure 4D) |
| C6 | The geometry arises from contextual constraints (lateral moves are visible to a facing partner) or from fixed functional roles of body parts | weak: speculation, stated as such | Discussion |
| C7 | Bounce is a "supramodal pacesetter" of interpersonal synchrony | weak to moderate: three converging observations, mechanism proposed | Figures 2D, 4E, S1; Discussion |

## Concepts

- **Principal movement (PM)**: a one-dimensional component of whole-body
  posture from PCA, "reminiscent of common dance moves".
- **Music-driven, partner-driven, hybrid synchrony**: a PM whose
  interpersonal synchrony shows a main effect of same music, of visual
  contact, or of both.
- **Eigendirection / eigenperiod**: a component of a second-layer PCA over
  the PMs' spatial maps (body part × axis) or over their synchrony
  periodicity profiles.
- **Geometry of synchrony**: the allocation of distinct synchronies to
  distinct spatial axes and body parts.

## Connections

It cites ethology, psychology, musicology and neuroscience for the
theoretical distinction between shared input and inter-individual
adaptation, and contrasts the two in one behaviour. It builds on the
authors' earlier use of PCA to extract movement primitives from dance and
point-light displays (Bigand's PLmocap). Data are public (IIT Dataverse,
doi:10.48557/UR2GBG) and the code is on GitHub.

## Bearing on the record

- **QUESTION-063** asks what measurement tells a shared drive from
  coupling. This study runs, in a human dyad, the design the question
  names: the shared drive and the coupling channel are each removed
  independently, and the components that follow each are identified. It
  also gives the negative half of an answer: the timing of synchrony does
  not discriminate, "when (unlike where) participants move does not
  reflect whether synchrony is established through music or partner
  vision." What it does not supply is the other half of the question's
  design, perturbing one member and measuring the other, so direction is
  not estimated. Filed as THEORY-tmpcd7cz.
- **CASE-045** (the dancing couple) proposes measuring lead→follow and
  follow→lead coupling with the music's beat as an exogenous input. Bigand
  et al. show the music must indeed be treated as a separate driver, and
  that it drives some components and not others: a VAR on joint
  kinematics with the beat as input should expect the pair's block to be
  carried by particular components, not the whole body. Their setting
  differs (no touch, no lead and follow, untrained dancers), and they
  estimate no direction, no perturbation response and no block gap.
- **CLAIM-172** says mutual entrainment marks a combined form of peers,
  and its 2026-10-14 note that "shared timing alone is not the mark". This
  reading supports the latter: two kinds of synchrony, one from a common
  cause and one from coupling, are indistinguishable in their timing.
  Visual contact is mutual by design here, but the study does not show
  that the partner-driven synchrony is mutual entrainment rather than one
  partner following.
- **LIT-933** (Nowak et al.) counts synchrony from mutual influence and
  from a common external signal as one functional unit, the conflation
  QUESTION-063 names. This study shows the two coexisting in different
  components of the same pair, which makes the conflation costly.
- **THEORY-520** (participatory sense-making): the partner-driven
  component is a measured, manipulable instance of movement coordinated
  through the interaction. Nothing here tests the autonomy of the
  interaction.

## Limitations

- **Direction is not measured.** Cross-wavelet power is symmetric; nothing
  says whether one partner led.
- **Independence rests on null interactions.** The paper reports no
  interaction; it does not bound one.
- **The categories depend on the decomposition.** A different basis could
  split or merge components and move the boundaries between categories.
- **Narrow sample and setting.** Untrained familiar pairs, face to face at
  2.5 m, no physical contact, 40-second songs; the authors say whether the
  geometry "remains adaptable to changing environmental constraints is
  yet to be determined", and that side-by-side dancing might reorganize it.
- **The geometric explanation is speculative.** Visibility or fixed
  functional roles of body parts are both offered; neither is tested.
- **Effect sizes per movement are not reported in the text**, only
  significant clusters and colour-scaled F-values.

## Open questions

- Is the partner-driven synchrony mutual or led? A perturbation of one
  dancer, or a directional measure on the partner-driven components,
  would say.
- Does the geometry hold in a partner dance with touch and with lead and
  follow roles, as in CASE-045? There the haptic channel carries the
  coupling.
- Does the allocation reorganize when the partners' relative position
  changes, as the authors suggest for side-by-side dancing?
