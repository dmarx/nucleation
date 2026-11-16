---
status: Active
status_note: >-
  Read 2026-11-16 in arXiv 1706.09847v3 (the extended FAT* 2018 version),
  arxiv.org. Note and THEORY filed from the reading.
title: 'Runaway Feedback Loops in Predictive Policing'
version: 2
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Filed, not read, from the exchange "Assess Depp Heard Abuse" (2026-11-15). Identifier checked on 2026-11-15 (arXiv, DataCite, doi.org, PubMed, Open Library or Crossref), no email address sent to any service. Not held: no hit for the identifier, the title or the first author in record/literature.d. published: 2017-06-29 (arXiv v1; proceedings 2018 (PMLR 81, FAT*)).
- version: 2
  date: '2026-11-16'
  note: >-
    Read on 2026-11-16 by a delegated reader, in arXiv 1706.09847v3 from arxiv.org, §1–§6 in full (figures from captions). Summary rewritten from the reading; status Active. The bearing on CLAIM-tmpnfjln, from A19's analogy, is withdrawn; the reading bears on CLAIM-277 and CLAIM-406.
tags:
- society-and-governance
- philosophy-of-technology
- anthology-candidate
date: '2026-11-15'
published: '2017-06-29'
arxiv: '1706.09847'
first_author: 'Ensign'
keywords: []
implementations: []
summary: >-
  Ensign, Friedler, Neville, Scheidegger and Venkatasubramanian (2018), PMLR
  81 (FAT*). In a Pólya-urn model of predictive policing that learns only from
  incidents its own patrols discover, deployment converges on the region that
  started ahead when crime rates are equal and on the higher-rate region
  however slight the difference when they are not; reported incidents
  attenuate but do not remove the effect; discarding discovered incidents in
  proportion to patrol probability restores convergence to the true rates.
  Simulations of PredPol on Oakland data reproduce both. Read 2026-11-16. It
  corroborates the record's entrenchment loop ([CLAIM-277](../claims.d/CLAIM-277.md)) and its structural
  form in [CLAIM-406](../claims.d/CLAIM-406.md). Cited in the exchange "Assess Depp Heard Abuse" (A19 §6),
  accurately; A's extension to effects of treatment on people is not the
  paper's.
---
<!-- inactive-ok-file: CLAIM-tmpnfjln — filed from the same exchange, Proposed, or Unavailable -->

# LIT-tmpi9cwn: Runaway Feedback Loops in Predictive Policing

Ensign, Friedler, Neville, Scheidegger, Venkatasubramanian (2018). *Runaway Feedback Loops in Predictive Policing*. Proceedings of the 1st Conference on Fairness, Accountability and Transparency, PMLR 81. arXiv 1706.09847.

## Key takeaways

*Read on 2026-11-16; see the reading below.*

## Standing in the record

Registered from the exchange "Assess Depp Heard Abuse" (https://chatgpt.com/share/6afa2a8d-2598-83ea-8d1a-d9ceb992a99c), A19 §6, on how algorithmic systems hide or reproduce their own upstream choices. It bears on [CLAIM-tmpnfjln](../claims.d/CLAIM-tmpnfjln.md). Read on 2026-11-16; see the reading below.

## Reading of 2026-11-16

Read in arXiv v3. The paper proves, in a two-region urn with patrols that discover crime at its true rate, that a system retrained on its own discovered incidents learns where it looked rather than where crime is: under equal rates the outcome is a draw fixed by the initial counts (Lemma 2), under unequal rates it goes wholly to the higher-rate region (Lemma 4, a "go with the winner" problem). Reported incidents help only if discovered ones are down-weighted (§3.4.1). A rejection-sampling filter on discovered incidents repairs it (§3.5), and PredPol simulations on Lum and Isaac's Oakland data show both the runaway and the repair (§5). The authors' own limit: crime "reporting is noisy and skewed by area and by type of crime", and then "the solutions might not continue to work" (§6). What the exchange says (A19 §6) is accurate; its further claim that such algorithms turn effects of institutional treatment into properties of people is A's, since in this model policing changes nothing about the people. See the NOTE and THEORY filed from this reading.
