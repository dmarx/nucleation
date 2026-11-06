---
status: Active
status_note: >-
  read in part 2026-11-06 (NOTE-tmpt6qk4) from arXiv:1911.03340v1, as a
  neighbour of Copeland, Gleiser & Müller (1995), LIT-tmpfxol8; worth
  reading as the long later account of why oscillons end: apart from the
  1+1 sine-Gordon breather no real-scalar oscillon is exactly periodic, all
  radiate at a rate exponentially small in their amplitude parameter but
  nonzero, and in 3+1 dimensions they are stable only above a minimum
  amplitude, so that slow radiation carries them below it and they suddenly
  decay, while in 1 and 2 space dimensions they never decay. Its main
  limits: a 216-page review built on the author's own D.Sc. thesis, partly
  his own results; only the introduction, the history, the numerical
  chapters on Gaussian data and near-periodic states, the start of the
  numerical-radiation section and the summary were read, not the
  asymptotic and Borel derivations nor most of the self-gravitating part;
  and the question whether fine-tuned oscillons are permanent is left
  against a contrary claim.
title: 'A review on radiation of oscillons and oscillatons'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Registered and read in part on 2026-11-06 at the owner's suggestion
    that soliton dynamics bear on the record's questions of individuation
    and persistence (works chosen by the assistant), as a neighbour of
    Copeland, Gleiser & Müller (1995), LIT-tmpfxol8, read for the later
    account of oscillon lifetimes and decay. Citation checked against the
    arXiv API by the reader (no email sent): Gyula Fodor, Wigner Research
    Centre for Physics, Budapest, arXiv:1911.03340 [hep-th], v1 submitted
    2019-11-08, which is `published:`; the arXiv metadata gives no DOI or
    journal reference, and Crossref was not consulted, so `arxiv:` is the
    only source. The title page describes it as a review based on the
    English translation of the author's D.Sc. thesis for the Hungarian
    Academy of Sciences. Copy from arXiv, arxiv.org/pdf/1911.03340v1, 216
    pages, text extracted by pdftotext; the figures were not legible.
tags:
- natural-sciences
- mathematics
date: '2026-11-06'
published: '2019-11-08'
arxiv: '1911.03340'
first_author: 'Fodor'
keywords:
- 'oscillons'
- 'oscillatons'
- 'scalar field radiation'
- 'breathers'
- 'sine-Gordon'
- 'quasibreathers'
- 'Borel summation'
implementations: []
summary: >-
  Fodor (2019). A review, from the author's D.Sc. thesis, of long-lived
  oscillating localized states of a real scalar field: oscillons on a fixed
  background and oscillatons when self-gravitating, mainly of the small but
  nonzero radiation they emit. Only the 1+1 sine-Gordon breather is exactly
  periodic; every other oscillon radiates, at a rate exponentially small in
  the amplitude parameter, computed by spectral numerics or by complex
  extension, asymptotic matching and Borel summation. Oscillons form from
  generic initial data. Stability follows from whether energy rises with
  central amplitude; 3+1 dimensional oscillons are stable only above a
  minimum amplitude and, carried below it by radiation, suddenly decay after
  a few thousand oscillations, while lower-dimensional ones never decay.
  The author's independent code reproduces the Gaussian-data results of
  Gleiser and of Copeland, Gleiser & Müller.
---
<!-- inactive-ok-file: THEORY-tmp6zy9r CLAIM-600 — Proposed or new; cited from the reading of Fodor (2019) as open -->

# LIT-tmpbn6ad: A review on radiation of oscillons and oscillatons

Fodor, G. (2019). A review on radiation of oscillons and oscillatons. arXiv:1911.03340 [hep-th]. ARXIV-1911.03340.

## Key takeaways

*From the reading, NOTE-tmpt6qk4, of arXiv v1, in part. Page and section numbers are the preprint's.*

- **Only one exact breather.** "The 1 + 1 dimensional sine-Gordon theory
  is also very special in the sense that it is the only theory involving a
  real scalar field where an exactly time-periodic localized breather can
  exist" (Ch. 1); "Apart from the exceptional sine-Gordon breather, all
  oscillon solutions emit energy slowly by the radiation of scalar field".
- **Generic.** "they are not exceptional states, they evolve from quite
  general initial data" (Ch. 1), including "randomly chosen not spherically
  symmetric initial data".
- **Stability from energy against amplitude.** "If increasing the central
  amplitude the total energy of the system also increases, then the system
  is stable, otherwise it is unstable" (Ch. 1).
- **Dimension decides the end.** "3 + 1 dimensional oscillons are stable
  only if their amplitude is above a certain limit. If their amplitude
  decreases below that value because of the radiation loss, then they
  suddenly decay"; in 1 and 2 dimensions, "Since the energy loss rate
  decreases exponentially when the amplitude decreases, these lower
  dimensional oscillons never decay" (Ch. 1).
- **A reproduced lifetime (§2.6.4).** One Gaussian oscillon "performs
  approximately 1240 similar oscillations"; "at around t = 5800 the
  radiation becomes more intense, and the oscillon begins to decay", and
  within about 25 oscillations it is no longer localized.
- **Permanence contested.** The lifetime peaks found under fine-tuning
  were shown to be oscillons that "necessarily radiate in a detectable way"
  (Ch. 1); Gleiser & Krackow (2019), not cited in the review, argue the
  opposite. Left unresolved.

## Standing in the record

Registered as a neighbour of Copeland, Gleiser & Müller (1995),
LIT-tmpfxol8, which was itself read in full; this stands in not for the
paper but for the later literature on its decay. It carries CGM's minimum
amplitude and sudden end, generalized as a stability criterion and
contrasted with lower dimensions, and an independent reproduction of their
kind of Gaussian result; it does not explain CGM's upper radius bound. For
the record it adds that one leak gives two shapes, an abrupt end in three
dimensions and a never-ending slowing in one and two, which bears on
CLAIM-600's slow reversion. Filed from it: THEORY-tmp6zy9r. No instruction
for machine-learning practice.
