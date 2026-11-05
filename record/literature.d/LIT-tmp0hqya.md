---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmperio5](../notes.d/NOTE-tmperio5.md)) from the PubMed Central HTML of the
  version of record (PMC7261180, a US Government work in the public
  domain in the US), main text, figure captions and tables in full, the
  supplement not read; worth reading as a measurement of the smallest unit
  of origami folding, one staple closing one fold of the scaffold, and for
  its account of what bulk methods cannot tell apart. A fold is more stable
  than the same domain bound bimolecularly, and its melting temperature
  falls with fold distance by more than 10 °C; from this the authors infer,
  untested, a nucleation-and-growth folding order. Its main limits: one fold
  and one melt domain; fluorescence recorded on the melt only, so no
  anneal, hysteresis, kinetics or test of equilibrium; ΔH, ΔS and ΔCp
  resolved only for one scaffold; the supplement (the affine procedure in
  detail, persistence-length estimates, fits, sequences) unread.
title: 'Revealing thermodynamics of DNA origami folding via affine transformations'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 at the owner's request to connect
    the record's realizability inquiry to DNA origami; the work was chosen
    by the assistant. The citation was checked by the reader against
    Crossref (no mailto) and the PMC ID converter (no email): Jacob M.
    Majikes, Paul N. Patrone, Daniel Schiffels, Michael Zwolak, Anthony J.
    Kearsley, Samuel P. Forry and J. Alexander Liddle (NIST), Nucleic Acids
    Research 48(10), 5268–5280; received 14 November 2019, revised 7 April
    2020, accepted 28 April 2020 (also the DOI's registration), published
    online 29 April 2020, which is `published:`, issue 4 June 2020. PMID
    32347943, PMCID PMC7261180. No correction was needed. Read from the
    PubMed Central HTML article page
    (https://pmc.ncbi.nlm.nih.gov/articles/PMC7261180/); NCBI's XML carries
    front matter only and Europe PMC's endpoints returned 503 and 500, each
    tried once. The supplementary PDF was not read: PMC served a reCAPTCHA
    page, where the reader stopped. Status Active.
tags:
- natural-sciences
- thermodynamics
date: '2026-11-05'
published: '2020-04-29'
doi: '10.1093/nar/gkaa283'
first_author: 'Majikes'
keywords:
- 'DNA origami'
- 'DNA melting'
- 'FRET'
- 'affine transformation'
- 'baseline correction'
- 'loop entropy'
- 'heat capacity'
implementations: []
summary: >-
  Majikes, Patrone, Schiffels, Zwolak, Kearsley, Forry & Liddle (2020). A
  minimal single-fold DNA origami system with a modular FRET reporter, the
  fold distance varied over 13 positions and the scaffold's apparent
  persistence length varied by coating oligos, melted in twelve replicates
  per condition; baselines corrected by an affine collapse of the replicate
  curves onto one, with no assumed baseline form. A fold, being
  unimolecular, melts higher than the bimolecular hybridization-only
  control; longer folds melt lower, by more than 10 °C between short and
  long, through loop entropy; short folds show a bending-enthalpy dip; and
  ΔCp is not negligible. The authors infer, without testing it, a
  nucleation-and-growth folding order in which a staple's longest domain
  binds first and short folds follow.
---
<!-- inactive-ok-file: THEORY-tmpynb4z THEORY-1398 CLAIM-557 CLAIM-574 CLAIM-569 CLAIM-567 CLAIM-184 CLAIM-478 — Proposed or new; cited from the reading of Majikes et al. (2020) as open -->

# LIT-tmp0hqya: Revealing thermodynamics of DNA origami folding via affine transformations

Majikes, J. M., Patrone, P. N., Schiffels, D., Zwolak, M., Kearsley, A. J., Forry, S. P. & Liddle, J. A. (2020). Revealing thermodynamics of DNA origami folding via affine transformations. *Nucleic Acids Research* 48(10): 5268–5280. doi:10.1093/nar/gkaa283.

## Key takeaways

*From the reading, [NOTE-tmperio5](../notes.d/NOTE-tmperio5.md) (main text, captions and tables; the supplement unread).*

- **A fold is unimolecular.** "The hybridization-only sample is less
  stable than the others as it involves a bimolecular reaction, at low
  concentration, rather than a unimolecular reaction."
- **Fold distance costs entropy.** "Increasing loop distance depresses the
  Tm, as does increasing persistence length, primarily at short fold
  distances"; "the increase in melt temperature due to a short versus a
  long fold distance can be > 10°C".
- **ΔCp matters** over the processing range, from curvature in the van't
  Hoff plots.
- **The folding order is inferred, not shown.** "Among the sub-sequences on
  a staple, the longest binds first in a bimolecular reaction, consistent
  with the nucleation seed subsequence concept", "although confirming this
  process will require additional testing in systems with multiple folds".
- **Resolution is bought.** Better data "would require equipment with a
  temperature control precision better than 0.3°C, and with a data
  sampling density greater than one measurement per 0.6°C."

## Standing in the record

Filed for the realizability inquiry as a measurement of how stable one
fold is, and of what an observer can resolve at what cost. Its strongest
bearing is on the observing side, [CLAIM-557](../claims.d/CLAIM-557.md) and [CLAIM-574](../claims.d/CLAIM-574.md): bulk methods
cannot single out one staple fold, a designed reporter can, and at the
paper's budget persistence-length differences show in Tm but not in ΔH,
ΔS or ΔCp. It measures the holding side of [CLAIM-569](../claims.d/CLAIM-569.md) and [CLAIM-567](../claims.d/CLAIM-567.md) only:
melts alone, no anneal, no hysteresis, so it supplies no evidence of the
kind [THEORY-136](../theory.d/THEORY-136.md) asks for. Its inferred order, a first-bound domain making
later neighbouring folds cheaper, is a weak and untested instance of
[CLAIM-184](../claims.d/CLAIM-184.md) and a mechanism for [QUESTION-380](../questions.d/QUESTION-380.md); it complements the held
simulation reading, [LIT-2081](LIT-2081.md) and [THEORY-1398](../theory.d/THEORY-1398.md), on local cooperativity, and
says nothing about global traps. Filed from it: [THEORY-tmpynb4z](../theory.d/THEORY-tmpynb4z.md). No
instruction for machine-learning practice.
