---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmp059hz](../notes.d/NOTE-tmp059hz.md)) from the authors' manuscript deposited in
  the Sorbonne Université HAL archive (hal-01623551v1), main text, figure
  captions, references and the full supplement, the staple sequence list
  and the image-processing procedure in detail skipped, figure images not
  viewed; worth reading as a direct observation of where a DNA origami
  starts folding and of a change to that place made by staple
  concentration alone, with the sequences unchanged. Under standard
  conditions Rothemund's tall rectangle nucleates at its top and bottom
  ends and grows toward the centre; raising the central staples and
  cutting the edge staples moves the start to the centre, which the
  authors read as thermodynamic control by the staples' melting
  temperatures. Its main limits: one design; the two concentration changes
  made together, with the total stock raised and the ramp slowed; no yield
  or defect count under the altered allocation; the snapshot method needs
  adsorption and drying and resolves states only at 59 °C and below.
title: 'Observing and Controlling the Folding Pathway of DNA Origami at the Nanoscale'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's paste of A's
    synthesis on DNA origami, which cites the work. The citation was
    checked by the reader against Crossref (no mailto), PubMed and Europe
    PMC: Jonathan Lee Tin Wah, Christophe David, Sergii Rudiuk, Damien
    Baigl and André Estévez-Torres, ACS Nano 10(2), 1978–1987; published
    online 27 January 2016 (Crossref and PubMed epub), which is
    `published:`, issue 23 February 2016. PMID 26795025; no PMCID. The
    first author's family name is "Lee Tin Wah" (Crossref); PubMed indexes
    it as "Wah JL", and A writes "Lee Tin Wah and colleagues", so no
    correction was needed beyond filing the family name whole. Read from
    the authors' manuscript with its supplement, deposited in HAL
    (https://hal.sorbonne-universite.fr/hal-01623551), to which Europe PMC
    points as the open copy; not the ACS typeset version, so page numbers
    in the reading are the manuscript's. Status Active.
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
published: '2016-01-27'
doi: '10.1021/acsnano.5b05972'
first_author: 'Lee Tin Wah'
keywords:
- 'DNA origami'
- 'folding pathway'
- 'atomic force microscopy'
- 'nucleation'
- 'staple concentration'
- 'melting temperature'
- 'hysteresis'
implementations: []
summary: >-
  Lee Tin Wah, David, Rudiuk, Baigl & Estévez-Torres (2016). Rothemund's
  tall rectangle is folded on a slow cooling ramp and sampled at each
  temperature by adsorbing it onto mica and imaging by AFM. Folding runs
  between about 65 and 55 °C through distinct intermediates, nucleating at
  the top and bottom ends and growing toward the centre, with 85 % of
  particles defect-free at the end. Raising the central staples to 670 nM
  while cutting the outermost edge-row staples to 1.2 nM makes folding
  start at the centre instead, with no change of sequence. Melting retraces
  folding down to 61 °C and departs from it above, through
  out-of-equilibrium chain-like structures. The authors attribute the
  pathway to the distribution of staple melting temperatures over the
  structure, under thermodynamic rather than kinetic control.
---
<!-- inactive-ok-file: CASE-tmpu0s44 CLAIM-184 CLAIM-557 CLAIM-567 THEORY-1398 THEORY-tmp7qfc2 — Proposed, Unavailable, Skimmed or new; cited from the reading of Lee Tin Wah et al. (2016) as open -->

# LIT-tmps9gx3: Observing and Controlling the Folding Pathway of DNA Origami at the Nanoscale

Lee Tin Wah, J., David, C., Rudiuk, S., Baigl, D. & Estévez-Torres, A. (2016). Observing and Controlling the Folding Pathway of DNA Origami at the Nanoscale. *ACS Nano* 10(2): 1978–1987. doi:10.1021/acsnano.5b05972.

## Key takeaways

*From the reading, [NOTE-tmp059hz](../notes.d/NOTE-tmp059hz.md) (main text, captions and supplement; figure images not viewed).*

- **Folding starts at fixed places.** "In standard conditions folding was
  initiated at the edges of the rectangle and progressed towards the
  center"; folded portions "appeared always on the top and bottom ends of
  the tall rectangle, and not in the middle, indicating that folding is not
  random but starts at well-defined positions".
- **Concentration alone moves the start.** With the central and border
  staples "changed from 52 nM to, respectively, 670 and 1.2 nM ... the
  folding pathway was dramatically changed and proceeded this time from the
  center towards the edges", done "without modifying the sequence of
  neither the scaffold nor the staples".
- **The authors' account is equilibrium.** "the pathway is primarily
  defined by the distribution of the melting temperature of staples bound
  to the scaffold, the origamis folding from high to low melting
  temperature area". In their mass-action model more of a staple helps a
  site fold only while K1 S0 < 1; beyond that a second copy blocks it.
- **The final object under the change is barely characterized.** Only
  "normal rectangles were observed on top of a rugged surface, probably due
  to staple adsorption", and in bulk "the final fluorescence signal was
  also reduced".
- **Melting is not folding reversed above 61 °C**: "a new type of
  structure, called chain-like, was observed", read as out of equilibrium.

## Standing in the record

Filed for the realizability inquiry, and as the work A's synthesis cites
for the claim that the allocation of resources can set a developmental
path. The reading supports the narrower point: with sequences fixed, a
change of staple concentrations reroutes where folding starts and the
same kind of rectangle still forms. It does not show a fixed stock
reallocated (the total rose, the ramp slowed) and does not measure the
final-form distribution, so it bears on [QUESTION-tmpg0j9y](../questions.d/QUESTION-tmpg0j9y.md) and
[CASE-tmpu0s44](../cases.d/CASE-tmpu0s44.md) as a partial instance only. It qualifies [CLAIM-567](../claims.d/CLAIM-567.md) (the
target's reliability is quantified under one allocation only) and
[CLAIM-184](../claims.d/CLAIM-184.md) (early nuclei set the path but, by the authors' account, do not
lock in the outcome), gives an observed nucleus location for [QUESTION-380](../questions.d/QUESTION-380.md),
and illustrates [CLAIM-557](../claims.d/CLAIM-557.md) with observables that split the intermediates
two, four or six ways. Its equilibrium account sits beside the kinetic
traps of the held simulation reading, [LIT-2081](LIT-2081.md) ([THEORY-1398](../theory.d/THEORY-1398.md)), which it
neither contradicts nor tests: a 2D rectangle shows no global trap.
Filed from it: [THEORY-tmp7qfc2](../theory.d/THEORY-tmp7qfc2.md). No instruction for machine-learning
practice.
