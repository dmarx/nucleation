---
status: Active
status_note: >-
  read in full 2026-11-14 ([NOTE-tmpmu9w0](../notes.d/NOTE-tmpmu9w0.md)) from the publisher's PDF (CC BY
  4.0), which the owner supplied after pnas.org's Cloudflare check stopped
  this client's fetch the same day. Worth reading as a minimal spatial
  model in which two plant types differ in the range and strength of
  their competition kernels and switch with bistability along resource
  supply, paired with a field survey; the phase-transition vocabulary is
  applied by analogy. The SI and data were not read. The authors'
  code was read and its model rerun (NOTE-tmpmu9w0).
title: 'Phase transition in a dryland shrub–grass ecosystem: Emergence through local trade-offs'
version: 3
history:
- version: 1
  date: '2026-11-14'
  note: >-
    Filed, not read, at the owner's request ("read and file" the PNAS
    URL). Checked against the record first: no LIT held the DOI, the
    title or the first author, and no entry named fairy circles, drylands
    or shrub–grass systems. Citation from Crossref (no mailto): Jingyao
    Sun, Kailiang Yu, Xinrong Li, Max Rietkerk, Paolo D'Odorico, Ning
    Chen, Yanli Wang, Libin Zhang and Guirui Yu, PNAS 123(46) e2618656123,
    journal article; published online 2026-11-11 (print 2026-11-17), the
    online date being `published:`. Status Unfetched: the CC BY copy at
    https://www.pnas.org/doi/pdf/10.1073/pnas.2618656123 returned a
    Cloudflare challenge (HTTP 403) and was not retried; PubMed Central
    did not hold it (ID converter, "Identifier not found in PMC"), Europe
    PMC answered 503, and OpenAlex and Semantic Scholar listed only the
    publisher's copy before their free quotas ran out. Two arXiv
    neighbours (Martinez-Garcia et al. 2023; Zelnik, Meron & Bel 2015)
    were sent to readers as stand-ins.
- version: 2
  date: '2026-11-14'
  note: >-
    Unfetched → Active. The owner uploaded the publisher's PDF the same
    day; it was read in full (NOTE-tmpmu9w0) and the THEORY-tmplznge
    filed. The neighbour readings were stopped before they reported and
    nothing was filed from them. Authors, venue and article type confirmed
    against the PDF (ECOLOGY, research article; received 2026-05-28,
    accepted 2026-10-11, published 2026-11-11; edited by Alan Hastings).
    Summary and body rewritten from the reading; the version-1 status
    note is in this history.
- version: 3
  date: '2026-11-14'
  note: >-
    The same day, at the owner's request, the authors' archived code was
    read and rerun (NOTE-tmpmu9w0, "The authors' code, rerun";
    CASE-tmpjrrhk for the fairy circles). The key-takeaways line that
    Table 1's thresholds are the reverse of the text's is withdrawn: they
    agree under the code's sign convention. It is replaced by what the
    rerun found. The status note now says the code was read.
tags:
- ecology
- complex-systems
date: '2026-11-14'
published: '2026-11-11'
doi: '10.1073/pnas.2618656123'
first_author: 'Sun'
keywords:
- 'phase transition'
- 'dryland'
- 'shrub–grass ecosystem'
- 'self-organization'
- 'Turing-like pattern'
- 'fairy circles'
- 'abrupt shift'
- 'cellular automaton'
- 'resource foraging trade-off'
- 'complex adaptive system'
implementations: []
summary: >-
  Sun, Yu, Li, Rietkerk, D'Odorico, Chen, Wang, Zhang & Yu (2026), PNAS.
  A kernel-based cellular automaton in which shrubs deplete resources
  weakly over a wide radius and grasses strongly over a narrow one (the
  "EI trade-off") gives patterned shrubland, a bistable interval and
  patterned grassland along resource supply, which the authors call a
  first-order phase transition and match to a shrub-to-grass shift within
  180–250 mm of rainfall at the desert margin of northern China. Fairy
  circles, made in the model by contracting the shrub kernel by hand, are
  read as metastable; cover loss at the desert edge, fit by a power law,
  as a continuous transition. The model's bistability is shown; the
  field's is inferred ([NOTE-tmpmu9w0](../notes.d/NOTE-tmpmu9w0.md)).
---

<!-- inactive-ok-file: CASE-tmpjrrhk — Proposed; the assistant's fairy-circle rerun, named in the version-3 history note -->

# LIT-tmpruadv: Phase transition in a dryland shrub–grass ecosystem: Emergence through local trade-offs

Jingyao Sun, Kailiang Yu, Xinrong Li, Max Rietkerk, Paolo D'Odorico, Ning
Chen, Yanli Wang, Libin Zhang and Guirui Yu, "Phase transition in a dryland
shrub–grass ecosystem: Emergence through local trade-offs", *Proceedings of
the National Academy of Sciences* 123(46), e2618656123 (2026),
doi:10.1073/pnas.2618656123. CC BY 4.0.

## Key takeaways

*From the reading, [NOTE-tmpmu9w0](../notes.d/NOTE-tmpmu9w0.md).*

- **The model.** A probabilistic cellular automaton with three states per
  cell. Each plant's influence is a kernel: competition of strength
  c/(n−·s) out to a radius r−, and facilitation out to r+. Shrubs
  compete weakly far out (r− = 20) and grasses strongly close in
  (r− = 3). Along resource supply s it gives patterned shrubland, an
  interval where "either can win by excluding the other" depending on
  the initial configuration, and patterned grassland (Fig. 3C).
- **The field.** On a transect along the desert margin of northern
  China, composition shifts from shrub to grass "within a narrow
  precipitation window of 180 to 250 mm mean annual precipitation
  (MAP)". Plots in the window alternate, and patch size, spacing and
  their skewness change sharply (Fig. 2).
- **The reading.** Precipitation is an "external field" and the shift a
  first-order phase transition, by analogy with the Ising model. Fairy
  circles, hollow shrub rings in grass found only in the window, are
  metastable states near the threshold. The loss of cover at the desert
  edge under disturbance is a continuous, "disorder-driven" transition.
- **The trade-off test.** Patch size and spacing regress on a
  conservative-to-acquisitive trait axis with R² from 0.35 to 0.48. The
  authors call this "empirically validated".
- **Where it is thin.** The kernels are not measured. The fairy circles
  are produced by halving the shrub kernel and turning off dispersal by
  hand. The power law is a free-threshold fit accepted at R² > 0.9.
  The model's bistable interval, rerun from the authors' code, is far
  wider than the narrow window they match to the field.

## Standing in the record

Filed on 2026-11-14 at the owner's request, and read in full from the
copy the owner supplied. It is the record's first work on spatial
self-organization of vegetation, on fairy circles, or on how a spatial
pattern, and not only an aggregate state, changes across a transition.
The nearest holdings are on regime shifts and their warnings (Scheffer &
Carpenter, [LIT-726](LIT-726.md); early-warning signals, [LIT-1956](LIT-1956.md), and critical slowing,
[THEORY-1315](../theory.d/THEORY-1315.md)), on restoration against alternative states ([LIT-2165](LIT-2165.md),
[THEORY-1468](../theory.d/THEORY-1468.md)), on Turing's instability ([THEORY-543](../theory.d/THEORY-543.md)), and, in the record's
own argument, on the transitions by which forms come into being and pass
away ([QUESTION-281](../questions.d/QUESTION-281.md)). Its THEORY bears on that question.

Two questions the abstract left open are now answered. Its "phase
transition" is the physicist's term applied by analogy, with bistability
and hysteresis shown in the model. In the field, the evidence fits a
steep turnover as well as a discontinuity. The pattern mechanism is a
scale-dependent feedback written into competition and facilitation
kernels, not a diffusion-driven instability.

Its claims are leaned on nowhere in the record's argument. The THEORY is
Proposed until the model's bistable interval is reproduced from the
authors' archived code.
