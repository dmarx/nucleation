---
number: 1443
status: Active
formerly:
- THEORY-tmp8ofc7
title: 'Wagenbauer, Wachauf and Dietz show that a 42-helix multilayer DNA origami bundle with 5 or 15 of its 207 staples omitted looks the same as the complete object under negative-stain TEM averaging and agarose-gel mobility, while a gel-based fluorescent de Bruijn probe for unpaired bases tells them apart and, across five bundle designs, estimates that complete reactions still leave 44 to 263 of 7,560 bases unpaired, 96.5% to over 99% quality, depending on design and folding schedule'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings), under ADR-065: the title reports what the
    authors measured, and NOTE-1637 reads the article and its
    supplementary captions in full. The indistinguishability clause is
    narrowed to the one bundle tested (ADR-047 kind 3). The old title
    was 'Wagenbauer, Wachauf and Dietz show that multilayer DNA origami
    with up to 7% of its staples omitted looks the same as the complete
    object under negative-stain TEM averaging and agarose-gel mobility,
    while a gel-based fluorescent de Bruijn probe for unpaired bases
    tells them apart and estimates that complete reactions still leave
    44 to 263 of 7,560 bases unpaired, 96.5% to over 99% quality,
    depending on design and folding schedule'. The condition asked for
    an independent study by another method, and it moves unchanged to
    QUESTION-tmpdtizm, which lists it under this entry's code; this
    entry bears_on it: 'An independent study using a different method,
    such as single-particle super-resolution imaging or sequencing-based
    counts of staple incorporation, finds deficits of the same order
    (about one to six staple equivalents per object) in fully supplied
    multilayer DNA origami, and finds that TEM-level or gel-level shape
    checks do not detect a deficit of that size.'
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2128
bears_on:
- QUESTION-tmpdtizm
summary: >-
  Wagenbauer, Wachauf and Dietz (2014), [LIT-2128](../literature.d/LIT-2128.md), read in
  [NOTE-1637](../notes.d/NOTE-1637.md). The indistinguishability under TEM and gel mobility is
  shown directly; the residual counts are extrapolations from a
  calibration that assumes each omitted staple adds exactly its own
  bases unpaired, with a background floor near the best result. It does
  not say how defects are spread across particles, nor anything about
  misfolds that leave bases paired.
corroborates:
- CLAIM-594
---

# THEORY-1443: Wagenbauer, Wachauf and Dietz show that a 42-helix multilayer DNA origami bundle with 5 or 15 of its 207 staples omitted looks the same as the complete object under negative-stain TEM averaging and agarose-gel mobility, while a gel-based fluorescent de Bruijn probe for unpaired bases tells them apart and, across five bundle designs, estimates that complete reactions still leave 44 to 263 of 7,560 bases unpaired, 96.5% to over 99% quality, depending on design and folding schedule

## Source

Wagenbauer, Wachauf and Dietz (2014), [LIT-2128](../literature.d/LIT-2128.md); read in
[NOTE-1637](../notes.d/NOTE-1637.md).

## What was actually shown

- **Indistinguishability.** A 42-helix bundle with 0, 5 or 15 of 207
  staples omitted gave the same TEM class averages (250 particles each)
  and the same gel mobility. Either could have shown a difference.
- **The probe.** A Cy3-labelled order-3 de Bruijn probe, read on an
  ice-cold gel, brightened with the number of omitted bases, fairly
  linearly up to about 500, for five bundle designs.
- **Residuals.** Extrapolating each titration to zero gave 44 to 263
  unpaired bases in complete reactions, 1.2 to 6.2 staple equivalents,
  against a background floor of about 10 bases.
- **Schedule.** Isothermal folding at 52 °C for hours stayed two to three
  staples short of a 16 h ramp; a 1.5 h three-step protocol matched the
  ramp; a variant with different connectivity folded best at 48 °C.

## What this does not say

- That every particle lacks one to six staples: the measure is an
  ensemble average of the folded band.
- That shape is wrong: misfolds that leave every base paired are
  invisible to the probe.
- That TEM cannot see defects in general: cryo-EM may resolve shared,
  site-specific defects, by the authors' account.
- That the counts are exact: they rest on the one-to-one calibration
  assumption and carry only fit errors.
