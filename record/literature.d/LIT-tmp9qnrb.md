---
status: Active
status_note: 'read 2026-10-23 ([NOTE-tmpocnqb](../notes.d/NOTE-tmpocnqb.md)): in full, from the published version (CC BY 4.0) in the Archive ouverte UNIGE (unige:170302). Worth reading as the first attempt to recover the component process model''s components from brain and behaviour together. Twenty participants watched 40 film clips during fMRI and then rated 119 salient 12-second events on 32 CoreGRID features. Heart and respiration rate were recorded. Partial least squares correlation found six brain–behaviour latent variables, read as valuation, novelty, hedonic impact, goal monitoring, caring for others and approach/avoidance. For the record, the result is two distinct valence-like networks: a "wanting"-like valuation process and a "liking"-like hedonic one. Each event gets a feature vector, but no within-episode synchronization is computed.'
title: 'Brain networks subserving functional core processes of emotions identified with componential modeling'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: the published version, Cerebral Cortex 33(12):7993–8010,
    deposited in the Archive ouverte UNIGE (unige:170302) under CC BY 4.0,
    with Table 1 and the figure captions. The figures and the supplementary
    material were not seen. PubMed Central (PMC10267645) returned a bot
    check to this client. Details checked against Crossref (DOI
    10.1093/cercor/bhad093): Gelareh Mohammadi, Dimitri Van De Ville,
    Patrik Vuilleumier, Cerebral Cortex 33(12):7993–8010, advance access
    22 March 2023. A bioRxiv preprint exists (10.1101/2020.06.10.145201,
    June 2020) and was not read. Not checked against the Anthology of the
    SOTA. Quotations checked by script against the extracted text.
tags:
- emotion-and-affect
- neuroscience
- psychometrics
date: '2026-10-23'
published: '2023-03-22'
doi: '10.1093/cercor/bhad093'
url: 'https://archive-ouverte.unige.ch/unige:170302'
first_author: 'Mohammadi'
keywords:
- 'component process model'
- 'CoreGRID'
- 'fMRI'
- 'partial least squares correlation'
- 'functional core processes'
- 'wanting and liking'
- 'naturalistic film'
implementations: []
summary: >-
  Mohammadi, Van De Ville & Vuilleumier (2023), Cerebral Cortex
  33:7993–8010. Twenty participants watched 40 film clips during fMRI and
  rated 119 salient events (12 s each) on 32 CoreGRID features, and heart
  and respiration rate were recorded. Partial least squares correlation
  between event-wise brain maps and feature ratings yields six latent
  variables, the "functional core processes": valuation (wanting-like),
  novelty, hedonic impact (liking-like), goal monitoring, caring for
  others ("being moved") and approach/avoidance. No arousal process
  emerges, and the processes mix components rather than mapping one to
  one.
---
<!-- inactive-ok-file: THEORY-tmp0bbxk CLAIM-tmpe0iew CLAIM-tmpz8lli — Proposed; the wanting-without-liking objection and the proposal it presses, which this reading bears on -->
<!-- inactive-ok-file: NOTE-tmpocnqb — draft filed in the same tranche -->

# LIT-tmp9qnrb: Brain networks subserving functional core processes of emotions identified with componential modeling

Gelareh Mohammadi, Dimitri Van De Ville & Patrik Vuilleumier (2023),
*Cerebral Cortex* 33(12):7993–8010 — DOI-10.1093/cercor/bhad093

## Key takeaways

- **Design** (pp. 7995–7997). "Twenty participants watched 40 emotional
  clips and rated 119 emotional moments in terms of 32 component features
  defined by a previously validated componential model" (p. 7993). The
  ratings came after each scan session, on re-viewing, for pre-selected
  events "between 1 and 4 events per each video, with mean of 2.9 and
  duration of 12-s per event" (p. 7996). "This allowed us to ensure
  ratings corresponded to a precise event, and not more global judgments
  about the video" (p. 7996). Heart and respiration rate were recorded in
  the scanner. Electrodermal activity and facial EMG were lost to noise.
- **Method** (p. 7998). Partial least squares correlation (PLSC) between
  event-wise whole-brain contrast maps (2,276 events) and the 34 features.
  Significance by permutation, stability by bootstrap over subsets of
  subjects.
- **Six functional core processes** (pp. 8002–8006). LV1 valuation
  (unpleasantness, standards, wanting to continue or stop, feeling good
  or bad; vmPFC, OFC, amygdala, VTA vs insula, cingulate). LV2 novelty.
  LV3 hedonic impact (expression and pleasant, intense feeling;
  sensorimotor operculum, SMA, posterior insula, ventral pallidum). LV4
  goal monitoring. LV5 caring for others or "being moved" (DMN). LV6
  approach/avoidance and curiosity.
- **Two valences** (p. 8005). FCP-1 "may relate to the theoretical construct
  of “wanting” (or not wanting; Berridge 2009), rather than to the hedonic
  experience of" pleasure. FCP-3 is "reminiscent of the “liking” rather
  than “wanting” aspect of valence (Berridge 2009)" (p. 8006).
- **No arousal process** (p. 8007). "a striking aspect of our results is
  the absence of a FCP linking behavioral features and brain networks
  corresponding to the construct of arousal". The feeling items alone give
  two latent variables, valence and arousal, and explain less covariance.
- **Mixed components.** Most processes "include mixed features that do
  not purely correspond to 1 unique component as traditionally
  distinguished in CPM" (p. 8005).

## Standing in the record

Filed on 2026-10-23 and read for two questions, as set out in
[NOTE-tmpocnqb](../notes.d/NOTE-tmpocnqb.md). On measuring ascendancy ([QUESTION-tmpsqwu5](../questions.d/QUESTION-tmpsqwu5.md)) it
gives no synchronization index. Its latent variables are defined per
observation, so each 12-second event has a signed score on each process.
The paper does not report those scores. They would be a per-episode
measure of componential pattern, though not of which ordering wins. On the
three-layer operationalization of felt valence ([QUESTION-tmp0oife](../questions.d/QUESTION-tmp0oife.md)) it
is more useful. It finds in human brain and report the wanting/liking
split that [THEORY-tmp0bbxk](../theory.d/THEORY-tmp0bbxk.md) and [CLAIM-tmpe0iew](../claims.d/CLAIM-tmpe0iew.md) press against the
record's proposal ([CLAIM-tmpz8lli](../claims.d/CLAIM-tmpz8lli.md)). The valuation process carries the
action tendencies (continue, stop, undo), and the hedonic one carries
feeling and expression.

It is affective neuroscience, not an instruction for machine-learning
practice.
