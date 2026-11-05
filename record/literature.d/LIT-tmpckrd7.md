---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmpbpr6m](../notes.d/NOTE-tmpbpr6m.md)) from the author's arXiv deposit of the
  2012 conference paper; worth reading as a short analytic account of why
  the passive rimless wheel's gravity-powered gait is stable: the impact
  posture and the energy restored each step are fixed by geometry, so the
  return map's eigenvalue is cos²α whatever the step period, and the gait
  exists only above a minimum slope. Registered as a neighbour standing in
  for McGeer (1990), [LIT-tmpv6ctd](LIT-tmpv6ctd.md), on the rimless wheel only. Its main
  limits: a linearised, planar, one-degree-of-freedom model, so the result
  does not by itself extend to walkers with a swing leg, and the upper slope
  limit is not identified.
title: 'Stability principle underlying passive dynamic walking of rimless wheel'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 as a stand-in for the unread McGeer
    (1990), LIT-tmpv6ctd, at the owner's request; McGeer's paper is cited
    by the owner's pasted synthesis on FACT, rigidity, compliant mechanisms
    and origami (the pasted synthesis on constraint architectures, written
    by another assistant, A, in the same exchange as the
    emergency-readiness bibliography, pasted 2026-11-04). This work is not
    cited there; it cites McGeer (1990) as its ref. [1]. Citation checked
    against Crossref: Fumihiko Asano (Japan Advanced Institute of Science
    and Technology), 2012 IEEE International Conference on Control
    Applications (CCA), pp. 1039–1044, doi:10.1109/CCA.2012.6402345,
    conference paper. Crossref gives only October 2012, so `published:` is
    2012-10-01. Not held before (no hit for the DOI, the arXiv id,
    "rimless" or "Asano"). Copy: the author's arXiv deposit,
    arXiv:2604.13530v1 (posted 15 April 2026, listing the DOI), 6 pp.,
    https://arxiv.org/pdf/2604.13530v1, extracted with pdftotext -layout.
    Status set to Active.
tags:
- control-theory
- complex-systems
date: '2026-11-05'
published: '2012-10-01'
arxiv: '2604.13530'
doi: '10.1109/CCA.2012.6402345'
first_author: 'Asano'
keywords:
- 'rimless wheel'
- 'passive dynamic walking'
- 'asymptotic stability'
- 'Poincaré return map'
- 'restored mechanical energy'
implementations: []
summary: >-
  Asano (2012). A rimless wheel rolling down a slope loses a fixed fraction
  of its kinetic energy at each impact, ε = cos²α for leg angle α, and
  regains a fixed amount from gravity each step, so the step-to-step
  energy converges to a single value: the gait is asymptotically stable and
  period-1. A linearised stance phase gives the return map's eigenvalue as
  cos²α, fixed by the wheel's geometry and independent of the step period,
  a closed form for the step period, and a minimum slope, tan²(α/2) in the
  linearised model, below which the wheel cannot pass over mid-stance. On
  steep slopes walking turns to running or skipping.
---
<!-- inactive-ok-file: LIT-tmpv6ctd THEORY-tmpbbt2m — Unavailable or Proposed, and new; cited from the reading of Asano (2012) as open -->

# LIT-tmpckrd7: Stability principle underlying passive dynamic walking of rimless wheel

Asano, F. (2012). Stability principle underlying passive dynamic walking of rimless wheel. *2012 IEEE International Conference on Control Applications (CCA)*, pp. 1039–1044. doi:10.1109/CCA.2012.6402345. arXiv:2604.13530.

## Key takeaways

*From the reading, [NOTE-tmpbpr6m](../notes.d/NOTE-tmpbpr6m.md). Page numbers are the arXiv copy's.*

- **The simplest passive walker.** "Rimless wheels are known as the
  simplest model for passive dynamic walking." (abstract, p. 1).
- **Always stable.** A gait "generated only by gravity effect always
  becomes asymptotically stable and 1-period" (abstract, p. 1).
- **Geometry fixes the rate.** The stance-phase error ratio "is equal to
  cos α; the stability property is determined only by the configuration."
  (§IV-B, p. 4).
- **A window of slope.** The energy margins for passing mid-stance "must be
  positive in stable passive-dynamic gaits" (p. 4), which sets a minimum
  slope; on steep slopes the wheel begins "to jump as the slope becomes
  steep, that is, the generated motion changes from walking to running or
  skipping." (§V, p. 5).

## Standing in the record

Registered as a neighbour standing in for McGeer (1990), [LIT-tmpv6ctd](LIT-tmpv6ctd.md),
which could not be reached. It cites McGeer for the rimless wheel and
restates that model: a gait powered only by gravity on a slope, stable
because impact loss and restored energy are constant. The analysis is
Asano's own, not McGeer's. Against the pasted synthesis's gloss of McGeer,
"stable gait cycles driven by gravity and their own dynamics", it agrees for
the rimless wheel and adds the bounds: the stable cycle exists only in a
window of slope. Filed from it: [THEORY-tmpbbt2m](../theory.d/THEORY-tmpbbt2m.md).
