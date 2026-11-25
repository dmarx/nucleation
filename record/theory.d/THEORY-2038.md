---
number: 2038
status: Proposed
formerly:
- THEORY-tmpohouk
title: 'Kink counts predictable before freeze-out'
statement: >-
  Suzuki, Li and Zurek show, in simulations of a noisy, overdamped
  one-dimensional φ⁴ field quenched through its symmetry-breaking
  transition, that a recurrent network given short stretches of the field's
  evolution predicts the number and locations of the final kinks from data
  taken near the critical point, well before the freeze-out time, and that
  the onset of this predictability collapses across quench rates when time
  is rescaled by the Kibble–Zurek freeze-out time
version: 1
source:
- LIT-2833
tags:
- natural-sciences
- complex-systems
date: '2026-11-19'
bears_on:
- QUESTION-281
corroborates:
- CLAIM-694
promote_when: >-
  An independent rerun of the stated simulation, or an independent
  predictor applied to it, finds the number and locations of the final
  kinks predictable from windows near the critical point and before
  freeze-out, with the onset collapsing in t/t̂ across quench rates.
summary: >-
  From the reading of [LIT-2833](../literature.d/LIT-2833.md) in [NOTE-2112](../notes.d/NOTE-2112.md). Suzuki, Li and Zurek
  (2026), Physical Review Letters 137, 157301, DOI 10.1103/fstv-lsvh;
  arXiv 2508.20347 v2. In simulations of a noisy, overdamped 1D φ⁴ field
  quenched through its symmetry-breaking transition, a recurrent network
  (and an LSTM and a Transformer) predicts the number and locations of the
  final kinks from short windows of the field's evolution near the
  critical point. That is well before the freeze-out time and while the
  seeds are exponentially small. The onset of predictability scales with
  the Kibble–Zurek freeze-out time. It is here because it dates when a
  future individual becomes determined. Creation (near the critical point)
  and stabilization (at freeze-out) come apart in time ([QUESTION-281](../questions.d/QUESTION-281.md)). It
  also shows that kink locations are set by history, not by the charge
  ([CLAIM-694](../claims.d/CLAIM-694.md)). Read in its NOTE.
---
<!-- inactive-ok-file: CLAIM-694 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2038: Kink counts predictable before freeze-out

## The account

A real scalar field obeys overdamped Langevin dynamics in a φ⁴ potential whose control parameter ε = t/τQ is ramped through zero. Noise imprinted near the critical point, where the potential is flat, is amplified once the potential inverts. Fluctuations from earlier are attenuated and erased. Long-wavelength structure laid down near t = 0 grows into the final domains, so the kink pattern is determined long before it becomes visible at freeze-out. A recurrent network, and also an LSTM and a Transformer, trained on 11-step windows predicts the final field, and the number and locations of the kinks, from windows taken just after the critical point. There is partial information even shortly before it. The prediction-error curves for τQ = 128, 256 and 512 coincide when time is measured in units of the freeze-out time.

## What it does not show

- That the result holds beyond one dimension, for underdamped dynamics, for vortices, or in experiment.
- That no information exists before the critical point: the network's accuracy is a lower bound.
- The attenuation–instantiation–amplification mechanism itself, which comes from the authors' earlier "deconstruction" paper and is invoked here, not derived.
- Anything about the kinks' persistence after ε = 1.
