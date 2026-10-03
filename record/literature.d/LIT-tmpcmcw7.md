---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmp2cxrv](../notes.d/NOTE-tmp2cxrv.md)), from the author manuscript in PubMed Central; worth reading as the canonical statement of the diffusion decision model and of what it is for. Two-choice RT and accuracy are decomposed into drift rate (quality of evidence), boundary separation (caution), starting point (bias) and non-decision time, plus across-trial variability in drift, starting point and non-decision time. Three new motion-discrimination experiments show each manipulation landing on its own parameter: difficulty on drift, speed–accuracy instructions on boundaries, stimulus proportion mainly on starting point. Its closing claim, that diffusion models have come "as near to provid[ing] a solution to simple decision making as is possible in behavioral science", is the authors'' assessment, not a result.'
title: 'The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the NIH author manuscript in PubMed Central
    (PMC2474742, NIHMS49330, https://pmc.ncbi.nlm.nih.gov/articles/PMC2474742/),
    all eleven sections, Tables 1–2, the footnote and the figure captions;
    the reference list was scanned. The first request to PMC met a
    reCAPTCHA page, which I did not try to pass; a plain retry some seconds
    later returned the article. The MIT Press version of record was not
    seen, so page numbers are not given; citations below are to sections.
    Crossref confirms title, authors, Neural Computation 20(4):873–922,
    April 2008, and the DOI; `published:` is the first of April 2008, as no
    day is given. Not held in the Anthology of the SOTA: a grep of its
    record for "Ratcliff", "diffusion decision" and the DOI found nothing.
tags:
- cognition
- behavioral-integration
- neuroscience
- probabilistic-modeling
date: '2026-10-03'
published: '2008-04-01'
doi: '10.1162/neco.2008.12-06-420'
url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2474742/'
first_author: 'Ratcliff'
keywords:
- 'diffusion model'
- 'drift rate'
- 'boundary separation'
- 'response time distributions'
- 'speed-accuracy trade-off'
- 'quantile probability plots'
- 'motion discrimination'
- 'sequential sampling models'
implementations: []
summary: >-
  Ratcliff & McKoon (2008), Neural Computation 20(4):873–922. A review of
  the diffusion decision model for fast two-choice tasks, with three new
  motion-discrimination experiments. Noisy evidence accumulates from a
  starting point z to one of two boundaries (0, a) at drift v, plus
  non-decision time and across-trial variability in v, z and Ter. The model
  fits accuracy and full correct and error RT distributions, and maps
  difficulty to drift, speed–accuracy instructions to boundary separation
  and stimulus proportion mainly to starting point. Applications cover
  aging, aphasia and links to neural firing.
extended_by:
- LIT-tmp15yr3
---

<!-- inactive-ok-file: THEORY-056 — Proposed; named only to say this reading does not bear on it -->

# LIT-tmpcmcw7: The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks

Roger Ratcliff and Gail McKoon (2008), *Neural Computation* 20(4):873–922 — DOI-10.1162/neco.2008.12-06-420

## Key takeaways

- The diffusion model separates three things that RT and accuracy confound: the quality of the evidence (drift rate), how much evidence is required (boundary separation), and everything outside the decision (non-decision time). With across-trial variability in drift and starting point it also predicts when errors are slower than correct responses and when they are faster.
- Its constraints come from distribution shape. A drift change moves the .9 RT quantile about four times as much as the .1 quantile; a boundary change moves them in roughly a 2:1 ratio. Across conditions only location and spread change, not shape. In the three experiments (14 to 17 participants each) difficulty was fitted by drift alone, speed and accuracy instructions by boundaries alone, and a 75:25 stimulus proportion mainly by starting point, about a third of the way toward the likelier boundary.
- Fitted to individuals, the parameters dissociate. Across 18 data sets accuracy correlated with drift and mean RT with boundary separation. Older adults' slowing was mostly wider boundaries, not poorer evidence, and aphasic patients' slowing was mostly boundaries and longer non-decision time.

## Standing in the record

Filed on 2026-10-03 at the owner's request, as the record's statement of the
single-process diffusion model, beside its competing-accumulator rival (Usher
and McClelland, [LIT-tmp2p2lh](LIT-tmp2p2lh.md)), the analysis that relates the two and ties both
to the sequential probability ratio test (Bogacz et al., [LIT-tmp93b13](LIT-tmp93b13.md)), and the
Bayesian estimation package built on it (HDDM, [LIT-tmp15yr3](LIT-tmp15yr3.md)). It is chosen
over Ratcliff's original 1978 paper because it is a lawfully readable, current
statement of the full model with its variability parameters and its uses.
The 1978 paper is not filed.

It is a model of a cognitive process in people and monkeys, and it gives no
instruction for machine-learning practice, so it belongs here rather than in
the anthology. It is tagged `behavioral-integration` for the vocabulary's
"evidence accumulation to a decision", and `probabilistic-modeling` because it
is used, above all, as a statistical measurement model that turns RT
distributions into parameters.

Its relation to the record's other readings is mainly through [LIT-tmp93b13](LIT-tmp93b13.md) and
[LIT-tmp15yr3](LIT-tmp15yr3.md). It does not bear on the record's emotion-regulation theory
([THEORY-056](../theory.d/THEORY-056.md)) or its free-will theories.

No relation is declared. The paper runs no comparison against another filed
model: its §6 judges, from other work, that recent accumulator models "may be
as successful as" the diffusion model, and its §7.1 objects that Bogacz et
al.'s account of criterion setting cannot explain calibration from verbal
instruction or without feedback. That is a limitation it alleges, not a
correction of a claim.
