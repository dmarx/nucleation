---
status: Proposed
promote_when: >-
  The approximate-inverse property of circular correlation, and the
  growth of capacity about linearly in the dimension for independent
  N(0, 1/n) elements, are re-derived or checked numerically (a short
  simulation decoding k bound pairs against m candidate items at an error
  rate q would do), and the noisy decoded vector is shown to need, and to
  be restored by, a nearest-item clean-up.
title: 'Plate represents compositional structure in fixed-width distributed vectors by binding with circular convolution, superposing by addition and decoding with circular correlation, an approximate inverse of convolution whose output is a noisy version of the bound item that a separate item memory must clean up; for independent random vectors the number of pairs a trace can hold grows about linearly with the dimension'
version: 1
tags:
- representation-learning
- compositionality
- cognition
date: '2026-11-15'
source:
- LIT-tmpq18t6
bears_on:
- QUESTION-120
summary: >-
  Plate (1995), [LIT-tmpq18t6](../literature.d/LIT-tmpq18t6.md), read in [NOTE-tmp9vqu3](../notes.d/NOTE-tmp9vqu3.md) from an OCR scan whose
  formulas are noisy. The linear capacity is a fit to an approximation,
  n ≈ 4.5(k + 0.7) ln(m/30q⁴) as transcribed, for independent random
  vectors only. Bears on [QUESTION-120](../questions.d/QUESTION-120.md) as a random-code threshold of a
  further shape; its bearing on [CLAIM-182](../claims.d/CLAIM-182.md), an address that is not a
  location, is analogy and is not filed as a relation. The wording is the
  reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-182 — a Proposed claim, cited as an analogy or as having no bearing -->

# THEORY-tmp713mr: Plate represents compositional structure in fixed-width distributed vectors by binding with circular convolution, superposing by addition and decoding with circular correlation, an approximate inverse of convolution whose output is a noisy version of the bound item that a separate item memory must clean up; for independent random vectors the number of pairs a trace can hold grows about linearly with the dimension

Plate (1995), [LIT-tmpq18t6](../literature.d/LIT-tmpq18t6.md); read in [NOTE-tmp9vqu3](../notes.d/NOTE-tmp9vqu3.md).

## The result

For vectors of dimension n with elements independent N(0, 1/n), the
circular convolution a ⊛ b compresses the outer product of a and b into n
components by summing along trans-diagonals, so a bound pair has the
dimension of its parts and can be bound or superposed again: a binding of
two variables is x ⊛ a + y ⊛ b. Convolving a trace with the involution of
a cue, circular correlation, returns a noisy version of the item bound to
that cue; a separate auto-associative memory holding all items (exhaustive
dot-product lookup in the simulations) returns the nearest one. The exact
inverse gives a lower signal-to-noise ratio on noisy traces unless the
vectors are unitary. Capacity is analysed in §IX: the number of pairs k a
trace can hold, against m candidates at error probability q, is fitted by
n ≈ 4.5(k + 0.7) ln(m/30q⁴), so about linear in n. The paper could have
found that decoding fails beyond a few pairs, or that capacity grows more
slowly than the dimension.

## What it does not show

- Capacity for learned or structured vectors: the analysis assumes
  independent random elements; correlated items raise the error rate.
- A self-sufficient memory: retrieval is exact only through the clean-up
  memory, which must hold every item.
- Optical holography: the "holographic" of the name is the
  convolution–correlation memory literature, not light.
- That HRR models a record's addressability ([CLAIM-182](../claims.d/CLAIM-182.md)). It shows keyed
  recovery from a superposed store, which is an analogy the record may
  draw, not evidence about records.
- The same result as [THEORY-1036](THEORY-1036.md), whose superposition is a learned
  allocation in a toy model; or anything that contradicts [THEORY-272](THEORY-272.md).
- An exact capacity bound: the formula is the reader's transcription of a
  fit through noisy OCR.
