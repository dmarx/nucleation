---
number: 2187
status: Proposed
formerly:
- THEORY-tmpc73s5
title: 'Turbulent energy causality runs large to small'
statement: >-
  Martínez-Sánchez, Arranz and Lozano-Durán find that decomposing the
  predictive information that the volume-averaged interscale energy fluxes
  at four inertial-range filter widths of a forced isotropic turbulence
  simulation carry about each other's futures gives unique terms only from
  each scale to the next smaller one, with any small-to-large dependence
  redundant and synergy minor, and read this as directed causality of the
  forward cascade
promote_when: >-
  An independent analysis of a different turbulence dataset, or of local
  rather than volume-averaged fluxes, with lags not chosen to maximize the
  cross unique terms, finds forward unique terms and no small-to-large
  unique term; or a second decomposition, with a different redundancy
  function, applied to the same signals does.
version: 1
tags:
- causality
- information-theory
- natural-sciences
date: '2026-11-22'
source:
- LIT-2965
corroborates:
- CLAIM-335
summary: >-
  Martínez-Sánchez and colleagues, [LIT-2965](../literature.d/LIT-2965.md), read in [NOTE-2275](../notes.d/NOTE-2275.md). SURD
  measures predictive information among time series of a physical flux,
  so it keeps transfer and dependence apart as objects; its "causality" is
  prediction. An instance of [CLAIM-335](../claims.d/CLAIM-335.md)'s point ([ARG-185](../arguments.d/ARG-185.md)), and a fit to
  [CLAIM-810](../claims.d/CLAIM-810.md)'s turbulence row that does not test its separations
  ([ARG-187](../arguments.d/ARG-187.md)).
---
<!-- inactive-ok-file: CLAIM-810 ARG-185 ARG-187 — Proposed or new; the claim this reading bears on and the arguments that weigh it -->

# THEORY-2187: Turbulent energy causality runs large to small

## Source

Álvaro Martínez-Sánchez, Gonzalo Arranz and Adrián Lozano-Durán,
"Decomposing causality into its synergistic, unique, and redundant
components", Nat Commun 15, 9296 (2024), arXiv 2405.12411, [LIT-2965](../literature.d/LIT-2965.md), read
in [NOTE-2275](../notes.d/NOTE-2275.md).

## What was actually shown

- pp. 8–9, Fig. 6: on "the time signals of the volume-averaged energy
  transfer" at four filter widths, unique terms Σ1→Σ2, Σ2→Σ3, Σ3→Σ4; "no
  unique causality is observed from smaller to larger scales, and any
  causality from the backward cascade arises solely through redundant
  relationships"; synergy "a minor role".
- p. 9: leaks of about 47% for Σ2 and 14% for Σ1.
- p. 9: conditional Granger causality and convergent cross-mapping "do not
  support the hypothesis of a forward energy cascade".

What could have failed: a unique term from a smaller to a larger scale, or
no directed pattern at all.

## What this does not say

- Not that energy is transferred forward: the flux's sign and mean are
  physics the paper takes as given; SURD measures prediction among the
  flux signals.
- Nothing about local backscatter, averaged out of the four scalars.
- Not interventional: the paper's "causality" is predictive information
  under stationarity.
