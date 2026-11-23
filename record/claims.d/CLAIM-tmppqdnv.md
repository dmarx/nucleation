---
status: Active
title: 'Identity stabilization can be read as temporal filtering: an organizational
  variable that adapts at rate k to a noisily observed demand tracks variation
  slower than k and ignores variation faster, its tracking error grows with
  the demand''s frequency as ω²/(k² + ω²) while the noise it passes grows
  with k as k²/(k² + ω²), so neither the slowest nor the fastest adaptation
  is optimal in general, and the per-frequency optimum S_d/(S_d + λS_n) passes
  variation where genuine demand outweighs noise and holds steady where noise
  outweighs it'
version: 3
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-057: no premise; the transfer functions and
    the per-frequency optimum re-checked (argmin 0.7273 against the
    formula's 0.7273).
- version: 3
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-tmpsfjxu), the owner's
    manuscript from the exchange "Explain First Contact RL": A48 §4 states
    it: identity stabilization as temporal filtering. No other change.
role: thesis
warrant: demonstrated
defeated_if: 'An error in the transfer functions or the optimum. As a reading
  of organizations: an organization whose identity-conserving constraints
  do not act as a frequency-selective response to the demands it observes,
  so that what it absorbs and what it lets reorganize it is not ordered by
  rate.'
tags:
- control-theory
- self-governance
- mathematics
date: '2026-11-23'
line:
- realizability
- will-organization
complements:
- CLAIM-tmph25dl
- CLAIM-tmpx8csq
summary: 'A42 §2 and A44 §3 of the exchange "Explain First Contact RL" (ChatGPT,
  third share of 2026-11-22), at the owner''s U22 and U23. A42 derives the
  trade-off for ż = k(d + n − z) and calls it "a particularly precise version
  of the identity–adaptability tension": "Identity stabilization is temporal
  filtering." A44 gives the non-causal Wiener optimum. Both checked by the
  assistant. The wording is A''s (ChatGPT, in the exchange of 2026-11-22);
  adopting it is the owner''s call.'
works:
- governance-of-possibility
---

<!-- inactive-ok-file: CLAIM-tmph25dl — Proposed; cited in this filing of 2026-11-23 (third share) -->

# CLAIM-tmppqdnv: Identity stabilization can be read as temporal filtering: an organizational variable that adapts at rate k to a noisily observed demand tracks variation slower than k and ignores variation faster, its tracking error grows with the demand's frequency as ω²/(k² + ω²) while the noise it passes grows with k as k²/(k² + ω²), so neither the slowest nor the fastest adaptation is optimal in general, and the per-frequency optimum S_d/(S_d + λS_n) passes variation where genuine demand outweighs noise and holds steady where noise outweighs it

## Derivation (A42 §2, A44 §3), checked

For ż = k(d + n − z), the response to measured demand is H_k(s) = k/(s + k).
The tracking error e = d − z has E/D = iω/(k + iω), with squared gain
ω²/(k² + ω²). Noise reaches z through k/(k + iω), with squared gain
k²/(k² + ω²). Raising k lowers the first at every nonzero frequency and
raises the second. A42's illustrative cost is J(k) = ∫ [S_d ω²/(k² + ω²) +
λ S_n k²/(k² + ω²)] dω.

A44 frees the response operator T: per frequency, S_d|1 − T|² + λ S_n|T|²
is least at T* = S_d/(S_d + λ S_n). Ignoring causality, this is the
Wiener filter. Checked with python3 -I by direct minimization at one
setting (0.7273 against the formula's 0.7273).

## What it shows, and its limits

A42: "It allows an organization to preserve a coherent response to
persistent demands without reorganizing in reaction to every transient
disturbance. But the filter can also suppress genuinely important changes
when they occur faster than the organization can adapt."

A44 qualifies the filter reading in two ways:
- An organization is more selective than a low-pass filter. "it selects
  which variations are allowed to alter which relationships", fast
  restoration transverse to its organizing relations together with slow
  change along them.
- "Fourier spectra cannot fully characterize event-triggered obligations,
  irreversible harms, or response deadlines". Those need [TERM-115](../terms.d/TERM-115.md)'s
  readiness.

Who sets S_n, what counts as noise, is [CLAIM-tmp76xaw](CLAIM-tmp76xaw.md). This complements
[CLAIM-tmph25dl](CLAIM-tmph25dl.md), which says a constraint's adequacy depends on the
demand's timescale. It also complements [CLAIM-tmpx8csq](CLAIM-tmpx8csq.md), which says
persistence does not fix redirectability.

## Note of 2026-11-23: a parallel in the Daodejing

The assistant, answering the owner's "relate the conversation to wuwei" (2026-11-23, this session): Daodejing 60, govern a large state as you would cook a small fish
(paraphrased, not checked), reads naturally as low-gain filtering. If you
don't stir, you don't pass noise into the organization. [CLAIM-tmp76xaw](CLAIM-tmp76xaw.md)
is the limit: not stirring is wu-wei only relative to a classification of
noise. An institution that will not be stirred by objections to its
categories has entrenched its filter. This is an analogy; no edge.
