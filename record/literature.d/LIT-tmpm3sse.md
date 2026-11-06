---
status: Active
status_note: >-
  read in full 2026-11-06 ([NOTE-tmpgvg9r](../notes.d/NOTE-tmpgvg9r.md)) from arXiv:1211.0733v3 (27 June
  2013), the authors' last arXiv version, not the version of record; worth
  reading as the first observation of temporal dissipative Kerr solitons in
  a microresonator and as a clean physical case of a supplied localized
  structure: held by a continuous pump against cavity loss, existing only in
  a window of detuning, formed spontaneously from noise during a laser
  sweep, countable from discrete steps in transmission, and lasting "until
  the pump laser is switched off". Its main limits: one resonator;
  simulations without the thermal effects central to the experiment; the
  existence window from approximate analytics on an infinite domain;
  path dependence of formation shown, but hysteresis not named and no
  reverse sweep reported; no decay after switch-off measured; and the
  run-to-run variation in soliton number reported for simulations only.
title: 'Temporal solitons in optical microresonators'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Registered and read on 2026-11-06 at the owner's suggestion that
    soliton dynamics bear on the record's questions of individuation and
    persistence (works chosen by the assistant). Citation checked against
    Crossref (no mailto) at api.crossref.org/works/10.1038/nphoton.2013.343:
    T. Herr, V. Brasch, J. D. Jost, C. Y. Wang, N. M. Kondratiev, M. L.
    Gorodetsky and T. J. Kippenberg, Nature Photonics 8(2), 145–152,
    published online 22 December 2013, print February 2014; no correction
    needed. `published:` is the arXiv v1 submission date, 4 November 2012
    (v2 28 March 2013, v3 27 June 2013), from the arXiv abstract page. Copy
    from arXiv, arxiv.org/pdf/1211.0733v3, 23 pages: main text, Methods,
    figure captions and a ten-section Supplementary Information. The
    published version was not consulted. Text extracted by pdftotext; the
    extraction drops square roots in the equations, so the Supplementary
    Information's equations (eqs. 14–20, p. 14) were taken from a rendered
    image of the page.
tags:
- natural-sciences
- complex-systems
date: '2026-11-06'
published: '2012-11-04'
arxiv: '1211.0733'
doi: '10.1038/nphoton.2013.343'
first_author: 'Herr'
keywords:
- 'temporal dissipative cavity solitons'
- 'Lugiato-Lefever equation'
- 'optical microresonators'
- 'Kerr frequency combs'
- 'bistability'
- 'thermal self-stability'
- 'MgF2 whispering-gallery resonator'
implementations: []
summary: >-
  Herr, Brasch, Jost, Wang, Kondratiev, Gorodetsky & Kippenberg (2014). A
  continuous-wave laser swept down in frequency over a resonance of a MgF2
  microresonator, from the upper onto the lower branch of its Kerr
  bistability, produces a series of discrete steps in transmission.
  Simulations of the coupled-mode (Lugiato-Lefever) equations and the
  approximate analytic soliton solution identify each step as a state with
  a definite number of temporal dissipative solitons, about 200 fs pulses
  on a cw background, fewer at each step; in repeated simulated scans the
  number varies with the random seeding. The solitons exist only for a
  normalized detuning between √3 and π²f²/8, have a shape fixed by the
  resonator and pump, and once formed persist until the pump is switched
  off; with solitons present the usually unstable red-detuned regime is
  thermally self-stable.
---
<!-- inactive-ok-file: THEORY-tmp4fe10 CLAIM-597 CLAIM-600 CLAIM-604 LIT-1642 — Proposed, Unfetched or new; cited from the reading of Herr et al. (2014) as open -->

# LIT-tmpm3sse: Temporal solitons in optical microresonators

Herr, T., Brasch, V., Jost, J. D., Wang, C. Y., Kondratiev, N. M., Gorodetsky, M. L. & Kippenberg, T. J. (2014). Temporal solitons in optical microresonators. *Nature Photonics* 8(2): 145–152. doi:10.1038/nphoton.2013.343. [ARXIV-1211.0733](https://arxiv.org/abs/1211.0733).

## Key takeaways

*From the reading, [NOTE-tmpgvg9r](../notes.d/NOTE-tmpgvg9r.md), of arXiv v3. Page numbers are the preprint's.*

- **Supply is constitutive.** "Their dissipative nature requires them to be
  continuously in contact with an external energy source" (p. 1); the
  solitons rest on a "double balance between parametric gain and resonator
  loss on the one hand and nonlinearity and diffraction or dispersion on
  the other hand" (p. 1).
- **A window, not a threshold.** Solitons need the cw bistability, ζ0 > √3,
  and exist only up to ζ0max = π²f²/8 (SI eq. 18, p. 14, read from the
  page image), f the normalized pump.
- **Formation is path dependent.** They form on tuning "into the lower
  branch ... after previously following the upper branch" (p. 2); the
  state reached depends on the sweep, not only on the final detuning. The
  paper does not use the word hysteresis and shows no reverse sweep.
- **Counted by steps.** Each step in transmission is a state with fewer
  solitons; "The intracavity power changes discontinuously with the number
  of solitons" (p. 3). The number and height of steps "fluctuate in
  repeated numerical scans as a result of random seeding of the optical
  modes (corresponding to vacuum fluctuations)" (p. 3); for the experiment
  the paper asserts agreement but gives no statistics.
- **Form fixed, history in number and place.** In the multi-soliton
  solution "The complex numbers C1 and C2 are fully determined by the
  resonator parameters and the pump conditions" (p. 3); only the number N
  and the positions φj are free.
- **No supply, no soliton.** "Once generated, the solitons remain stable
  until the pump laser is switched off" (p. 3), "stable for hours" (SI
  §VI, p. 15). No decay after switch-off is measured.

## Standing in the record

Filed for the owner's suggestion that soliton formation bears on the
record's questions of individuation and persistence. It is the record's
first reading on dissipative solitons; the nearest held neighbour is
Knobloch's review of spatial localization in dissipative systems, [LIT-1642](LIT-1642.md),
registered but not read. The reading is a physical case of supplied
upkeep, [CLAIM-597](../claims.d/CLAIM-597.md), and of support that must stay a standing input,
[CLAIM-600](../claims.d/CLAIM-600.md), and it qualifies [CLAIM-604](../claims.d/CLAIM-604.md): thresholds, collapse outside a
window and path-dependent formation here come from a nonlinear Kerr
response under a supply that does not depend on the structure's state.
Filed from it: [THEORY-tmp4fe10](../theory.d/THEORY-tmp4fe10.md). No instruction for machine-learning
practice.
