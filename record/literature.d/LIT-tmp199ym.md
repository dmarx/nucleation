---
status: Active
status_note: >-
  read 2026-11-04 ([NOTE-tmptsczp](../notes.d/NOTE-tmptsczp.md)) from the publisher's typeset PDF posted
  on the first author's lab publications page; worth reading as the neural
  follow-up to Collins and Frank (2013), [LIT-tmpe9iv8](LIT-tmpe9iv8.md), and as a worked
  case of corroborating a latent, individually built rule structure with
  several observables at once. It re-analyses that paper's Experiment 2
  participants (N = 35), so it is not an independent sample; the
  late lateral-prefrontal switch negativity tracked each participant's
  context dimension but did not predict transfer, the early positivity
  that did was absent at group level, the two predictive markers agree
  only marginally, several topographic tests are uncorrected, and every
  contrast rests on a reaction-time switch-cost assignment.
title: 'Human EEG Uncovers Latent Generalizable Rule Structure during Learning'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    "Hierarchical probabilistic models in cognitive science", written by
    another assistant (A), which cites it only as "A related 2014 EEG
    study", with no authors or title, inside a sentence it presents as a
    quotation of Collins and Frank (2013) and which is A's paraphrase.
    Identified as Anne G. E. Collins, James F. Cavanagh and Michael J.
    Frank, The Journal of Neuroscience 34(13), 4677–4685, doi
    10.1523/JNEUROSCI.3900-13.2014, PMID 24672013, PMCID PMC3965790, and
    checked against Crossref and OpenAlex. Crossref gives 2014-03-26 as both
    the online and the print date, which is `published:`; the article
    prints received 11 September 2013, accepted 26 February 2014; there is
    no preprint. The authors are three, not Collins and Frank alone. Read
    in full (NOTE-tmptsczp) from the publisher's typeset PDF, pp. 4677–4685,
    posted on the publications page of the first author's lab
    (https://ccn.berkeley.edu/pdfs/papers/CollinsCavanaghFrank_2014JN_EEG_StructureLearning.pdf);
    the journal's own PDF met a Cloudflare challenge and was not retried.
    Not read: the reference list, scanned only.
tags:
- neuroscience
- learning-and-conditioning
- cognition
date: '2026-11-04'
published: '2014-03-26'
doi: '10.1523/JNEUROSCI.3900-13.2014'
first_author: 'Collins'
extends:
- LIT-tmpe9iv8
keywords:
- 'prefrontal cortex'
- 'task-set'
- 'reinforcement learning'
- 'rules'
- 'EEG'
implementations: []
summary: >-
  Collins, Cavanagh & Frank (2014). EEG recorded during the
  structure-transfer task of Collins and Frank (2013), in that paper's
  Experiment 2 participants (N = 35), over three blocks. Each participant's
  context dimension was read online from reaction-time switch-costs. A late
  cue-locked negativity over right lateral prefrontal cortex was larger for
  switches of that dimension than for stays, with no effect for the other
  dimension, but did not predict transfer. An early switch positivity,
  absent at group level, and a classifier trained on a separate attention
  localizer, which decoded attention to each participant's context
  dimension, each correlated across participants with later positive
  transfer (ρ = 0.5 and ρ = 0.35); the two agreed only marginally.
---
<!-- inactive-ok-file: THEORY-tmpiosxd THEORY-484 — Proposed or new; cited from the reading of Collins, Cavanagh and Frank (2014) as open -->

# LIT-tmp199ym: Human EEG Uncovers Latent Generalizable Rule Structure during Learning

Collins, A. G. E., Cavanagh, J. F. & Frank, M. J. (2014). Human EEG Uncovers Latent Generalizable Rule Structure during Learning. *The Journal of Neuroscience* 34(13): 4677–4685. doi:10.1523/JNEUROSCI.3900-13.2014.

## Key takeaways

*From the reading, [NOTE-tmptsczp](../notes.d/NOTE-tmptsczp.md). Page numbers are the journal's.*

- **The same participants as the 2013 Experiment 2.** Forty recruited,
  two lost to software problems and three excluded, N = 35, as in
  [LIT-tmpe9iv8](LIT-tmpe9iv8.md)'s Experiment 2; first-block behaviour "were reported by
  Collins and Frank, 2013" (p. 4679).
- **A switch potential for the context dimension only.** The late
  negativity "is sensitive only to change in high-level TS and not to the
  stimulus or action" (p. 4681). It did not predict transfer.
- **Two markers of later transfer.** The early switch positivity "was not
  evident across the entire group of subjects" (p. 4681) but correlated
  with positive transfer (ρ = 0.5, p = 0.003); decoded attention to the
  context dimension did too (ρ = 0.35, p < 0.05). They correlated with each
  other only marginally (ρ = 0.33, p = 0.068).
- **Correlational and proxy-bound.** Each participant's structure is
  assigned from behavioural switch-costs; "predictive" is a cross-subject
  correlation, not out-of-sample prediction.

## Standing in the record

The pasted synthesis mentioned it unnamed, as having found neural signals
for participants' inferred rule structures that predicted later
generalization. That is right in outline and overstated in detail: only
two of the three markers predicted transfer, neither the headline one,
and the sample is the 2013 paper's own. Filed from it: [THEORY-tmpiosxd](../theory.d/THEORY-tmpiosxd.md).
It is more correlational evidence of task-set coding in lateral
prefrontal cortex, the kind [THEORY-484](../theory.d/THEORY-484.md)'s promotion condition says cannot
settle that theory, and a case for [QUESTION-276](../questions.d/QUESTION-276.md) of corroborating a latent
structure through several observables. No instruction for
machine-learning practice.
