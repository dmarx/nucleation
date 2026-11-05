---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmpescek](../notes.d/NOTE-tmpescek.md)) from the authors' arXiv version (CC BY
  4.0); worth reading as a dynamical-systems explanation of why passive
  walkers are hard to make walk: the basin of attraction of the simplest
  walking model is small, thin and fractal-like because its upright
  equilibrium is a saddle, and as the slope grows the gait goes through
  period doubling to chaos and is destroyed by a boundary crisis.
  Registered as a neighbour standing in for McGeer (1990), [LIT-tmpv6ctd](LIT-tmpv6ctd.md), on
  the idea of passive dynamic walking and the later findings on its
  stability. Its main limits: one idealised model in a singular limit,
  basin membership by finite-step numerics, and a mechanism argued from a
  linearisation and figures rather than proved.
title: 'Formation mechanism of a basin of attraction for passive dynamic walking induced by intrinsic hyperbolicity'
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
    cited there; it credits McGeer with proposing passive dynamic walking.
    Citation checked against Crossref: Ippei Obayashi, Shinya Aoi, Kazuo
    Tsuchiya and Hiroshi Kokubu, Proceedings of the Royal Society A 472,
    article 20160028 (June 2016), doi:10.1098/rspa.2016.0028, research
    article. `published:` is 2014-07-22, the arXiv v1 submission of
    arXiv:1407.5720. Not held before (no hit for the DOI, the arXiv id or
    "Obayashi"). Copy: the authors' arXiv v3 (11 January 2016), 17 pp., CC
    BY 4.0, https://arxiv.org/pdf/1407.5720v3, extracted with pdftotext
    -layout; the published version was not compared. Status set to Active.
tags:
- mathematics
- complex-systems
- control-theory
date: '2026-11-05'
published: '2014-07-22'
arxiv: '1407.5720'
doi: '10.1098/rspa.2016.0028'
first_author: 'Obayashi'
keywords:
- 'passive dynamic walking'
- 'basin of attraction'
- 'hyperbolicity'
- 'saddle'
- 'simplest walking model'
- 'boundary crisis'
implementations: []
summary: >-
  Obayashi, Aoi, Tsuchiya & Kokubu (2016). In Garcia et al.'s simplest
  walking model, two massless legs with point masses on a slope and no
  control, the set of initial states that take at least one step, pulled
  back through the step map, gives nested sets whose intersection is the
  basin of attraction of the gait. The basin is very small, thin and
  V-shaped, with fractal-like slits and stripes. The authors trace this to
  the upright equilibrium, a saddle-centre: the stance leg behaves as an
  inverted pendulum, and regions pulled back near the saddle's stable
  manifold are thinned and folded. As the slope grows, the attractor goes
  through period doubling to chaos and then meets the basin boundary and
  disappears.
---
<!-- inactive-ok-file: LIT-tmpv6ctd THEORY-tmpabuss — Unavailable or Proposed, and new; cited from the reading of Obayashi et al. (2016) as open -->

# LIT-tmpw9g80: Formation mechanism of a basin of attraction for passive dynamic walking induced by intrinsic hyperbolicity

Obayashi, I., Aoi, S., Tsuchiya, K. & Kokubu, H. (2016). Formation mechanism of a basin of attraction for passive dynamic walking induced by intrinsic hyperbolicity. *Proceedings of the Royal Society A* 472: 20160028. doi:10.1098/rspa.2016.0028. arXiv:1407.5720.

## Key takeaways

*From the reading, [NOTE-tmpescek](../notes.d/NOTE-tmpescek.md). Page numbers are the arXiv v3's.*

- **McGeer's idea.** "This system walks down a shallow slope without an
  actuator or controller; it does this by balancing the energy dissipation
  due to foot contact with the energy generation due to the gravitational
  potential energy." (§1, p. 2).
- **A tiny basin.** "The basin of attraction is very small and thin, and it
  has a fractal-like shape" (abstract).
- **The cause.** "Due to the properties of the saddle point in the
  governing dynamics, an inverted pendulum falls down easily." (§1, p. 2).
- **The basin by construction.** "We define the domain D as the collection
  of initial conditions for which the model takes at least one step."
  (§2b, p. 4); its inverse images under the step map hold the states that
  take at least n + 1 steps.
- **Loss of the gait.** With growing slope "the attractor breaks down, and
  the model no longer continues walking." (§4d, p. 14).

## Standing in the record

Registered as a neighbour standing in for McGeer (1990), [LIT-tmpv6ctd](LIT-tmpv6ctd.md),
which could not be reached. It credits McGeer with passive dynamic walking
and states the idea; it restates no specific result of his, and the model
it analyses is Garcia et al.'s later simplification. Against the pasted
synthesis's gloss of McGeer, "stable gait cycles driven by gravity and their
own dynamics", it agrees on the idea and adds what A's use omits: the
stable cycle has a very small, thin basin and exists only over a narrow
range of slope. Passive gait is stable but not robust. Filed from it:
[THEORY-tmpabuss](../theory.d/THEORY-tmpabuss.md).
