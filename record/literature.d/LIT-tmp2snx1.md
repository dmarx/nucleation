---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmp5es2s](../notes.d/NOTE-tmp5es2s.md)) in full, from arXiv:0909.2386v1; worth reading for its exact band-pass decomposition of kinetic energy with smooth filters (a multiscale Germano identity, in which each band's energy changes by the flux in minus the flux out), for a compact statement of when and why the energy flux across a scale is local in scale ([THEORY-tmpfcxzq](../theory.d/THEORY-tmpfcxzq.md)), and for the account of why the rigorous 2/3 exponent is weaker than Kraichnan's 4/3. Read it knowing that the rigorous bounds are proved in Eyink (2005), [LIT-tmpko78q](LIT-tmpko78q.md), and only sketched here; that they are conditional on a scaling hypothesis for velocity increments (exponents strictly between 0 and 1) and a non-zero mean flux, neither proved for Navier–Stokes; that the 4/3 argument is heuristic and its one simulation brackets rather than confirms it; that the band decomposition's non-negativity holds only after integration for the kernels it needs; and that locality here is in scale, for one field, and says nothing about units.
title: 'Localness of energy cascade in hydrodynamic turbulence. I. Smooth coarse graining'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-19. `published:` is arXiv v1, 13 September 2009, per ADR-002. The exchange gave the title as "Localness of energy cascade in hydrodynamic turbulence, I"; the published title is above. Part II (Aluie & Eyink, arXiv:0909.2451, doi:10.1063/1.3266948) is a separate paper and is not filed. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the authors, title and identifiers found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmp5es2s) from arXiv:0909.2386v1. Status Deferred → Active. THEORY-tmpfcxzq is filed from the reading. The summary is corrected: the paper does not itself prove the locality bounds, which are Eyink (2005)'s, and its own new results are the band decomposition and the decorrelation account. The body's "Not read" paragraph is replaced, and "Why this is here" now says what the reading found.
tags:
- natural-sciences
- mathematics
date: '2026-10-19'
published: '2009-09-13'
arxiv: '0909.2386'
doi: '10.1063/1.3266883'
first_author: 'Eyink'
keywords:
- 'turbulence'
- 'energy cascade'
- 'scale locality'
- 'filtering'
- 'subgrid stress'
implementations: []
summary: >-
  Eyink & Aluie (2009). Builds an exact decomposition of kinetic energy into band-pass contributions from smooth, graded filters on a geometric sequence of scales, with band budgets whose fluxes telescope, and carries over Eyink's (2005) bounds: if velocity increments scale with exponents strictly between 0 and 1, the mean energy flux across a scale ℓ takes from scales above Δ or below δ at most a power of the scale ratio, 2/3 at K41 scaling. The bounds are sketched here and proved in the 2005 paper. A heuristic decorrelation argument and one 512³ simulation account for Kraichnan's faster 4/3 decay of the signed contributions.
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpko78q — Deferred; the paper holding the original proofs, registered unread, cited as open -->
# LIT-tmp2snx1: Localness of energy cascade in hydrodynamic turbulence. I. Smooth coarse graining

Eyink, G. L. & Aluie, H. (2009). Localness of energy cascade in hydrodynamic turbulence. I. Smooth coarse graining. *Physics of Fluids* 21(11): 115107. doi:10.1063/1.3266883. Preprint: arXiv:0909.2386 (13 September 2009).

Read in full on 2026-10-20 in [NOTE-tmp5es2s](../notes.d/NOTE-tmp5es2s.md), from the arXiv copy.

## Why this is here

A3 put it at the centre of the turbulence readings: a proof that coupling across a hierarchy of scales is local, which is not the same as the hierarchy being nearly decomposable. Bears on [QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md) and [CLAIM-157](../claims.d/CLAIM-157.md).

The reading qualifies A3's description. The proof is Eyink (2005)'s, [LIT-tmpko78q](LIT-tmpko78q.md), and it is conditional on a scaling hypothesis for velocity increments. What it establishes, in that form, is that coupling between scales decays as a power of the scale ratio, with no gap: the whole energy throughput crosses every inertial scale. So the scales are not weakly coupled blocks, which is the record's contrast with [THEORY-661](../theory.d/THEORY-661.md), not the paper's ([THEORY-tmpfcxzq](../theory.d/THEORY-tmpfcxzq.md)). Nothing in the paper concerns units or individuation.
