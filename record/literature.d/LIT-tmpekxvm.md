---
status: Unavailable
status_note: >-
  filed 2026-10-16 from the PubMed abstract (42617381); no lawful full text was reached on 2026-10-16, so it is not read and no NOTE is filed. Where the reader looked: Unpaywall and OpenAlex (both "closed", no repository copy); Europe PMC ("Subscription required", not in PMC); ScienceDirect (PII S1550830726001941, 403 to this client, and paywalled); the Elsevier text-mining API Crossref lists (rate-limited, and it needs a subscriber key); Crossref posted-content and web searches for a preprint on PsyArXiv, OSF or ResearchGate (none found); OSF's API and search for a preregistration or data project (OSF returned 503 throughout, so this is unsettled); the University of Virginia Division of Perceptual Studies publications page (no copy listed); Entangled Labs' site (connection reset); and press coverage (News-Medical, WHSV), which links only to the ScienceDirect abstract and mentions no preprint, preregistration or data. A failure of availability, not merely of access, except for OSF, which should be rechecked. It stays Unavailable until a copy is supplied, not on merit. Registered at the owner's request (U9 of the exchange of 2026-10-16 on active inference). OSF was retried on 2026-10-17 and was down for scheduled maintenance, so a preregistration there is still unchecked.
title: 'Assessing correspondence between subjective reports and visual targets during attempted out-of-body experiences'
version: 2
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed, not read. Citation checked against Crossref and OpenAlex on 2026-10-16. The work is online ahead of print (Explore 22(6):103506). Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-16, commit d1573d2) for the authors and the title found nothing.
- version: 2
  date: '2026-10-16'
  note: >-
    A lawful full text was sought and not reached (where, in the status
    note), so the status moved from Deferred to Unavailable under ADR-041.
    The full PubMed abstract was read, and the summary now carries three
    points from it the first filing left out: the rank-based test against
    each trial's decoys was the primary analysis; the targets were unknown
    to researchers as well as participants; and the control analyses "do
    not establish sensitivity to naturalistic human language". The press
    release adds that the two adjacent-room reports were not predefined
    outcomes. "Why this is here" now says what the null can and cannot
    show.
tags:
- consciousness
- psychometrics
date: '2026-10-16'
published: '2026-08-12'
doi: '10.1016/j.explore.2026.103506'
first_author: 'Weiler'
keywords:
- 'out-of-body experience'
- 'veridical perception'
- 'anomalous cognition'
- 'semantic similarity'
- 'language-model embeddings'
implementations: []
summary: >-
  Weiler, Abraham, Acunzo & Hermansson (2026), from the abstract and press coverage only. Twenty-one people affiliated with an OBE-training institute tried to perceive a target picture, drawn from a standardized database and unknown to participants and researchers, displayed in a separate, inaccessible room. Ten reported an OBE; thirteen gave descriptions. Each description and the target captions were embedded with a pretrained language model, and the correct target's cosine similarity was ranked against 100 candidates per trial (primary analysis; z-scores secondary). No trial and no combined rank test exceeded chance. Controls showed the pipeline finds targets when semantic correspondence is present, but, the authors say, not that it is sensitive to naturalistic human language. Two participants spontaneously reported accurate details of the experimenters' locations and activities in an adjacent room, which were not predefined outcomes.
---

# LIT-tmpekxvm: Assessing correspondence between subjective reports and visual targets during attempted out-of-body experiences

Weiler, M., Abraham, D., Acunzo, D. J. P. & Hermansson, N. (2026). *Explore* 22(6):103506. doi:10.1016/j.explore.2026.103506. PMID 42617381.

Not read: no lawful full text was reached (see the status note). The
summary is drawn from the PubMed abstract and the press coverage. A
reading should check it first.

## Why this is here

Registered at the owner's request (U9). It bears on [CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md) and [QUESTION-tmpr5tck](../questions.d/QUESTION-tmpr5tck.md). An attempted OBE is a judgement–observation loop with action on the world removed by design: the participant reports an observation that no sensory channel delivered. Scoring blind against concealed targets is independent scoring in [CLAIM-330](../claims.d/CLAIM-330.md)'s sense. The null result is what [CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md) predicts when such a loop runs without evidence it did not produce. How much the null shows is limited by the authors' own caveat that the controls "do not establish sensitivity to naturalistic human language": a pipeline that may not register a correct but loosely worded description cannot tell absence of correspondence from failure to detect it. The two adjacent-room reports were spontaneous and, per the press coverage, not predefined outcomes; nothing seen says they were scored blind against decoys, so as reported they are not independent scoring in [CLAIM-330](../claims.d/CLAIM-330.md)'s sense. From the abstract alone, it is not known how they were recorded or what the participants could have known.
