---
number: 640
status: Proposed
formerly:
- CLAIM-tmpsh6jv
title: 'Where viable regimes exchange symmetrically and fail into an absorbing state at small hazards, the survivors settle at the spectral gap of the exchange among the viable regimes to within the largest hazard, so the separation between settling and dying out is a dissipative coupling''s, and it depends on how the regimes are connected: for regimes in a line it shrinks as their number grows, and for regimes all connected it grows'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a finite chain with symmetric exchange
  rates among its viable states and hazards no larger than ε into an
  absorbing state, in which the gap between the two least eigenvalues of
  the restricted generator differs from the exchange Laplacian's λ₂ by
  more than ε, or the extinction rate exceeds ε. Also defeated as a
  separate entry if CLAIM-612, CASE-231, ARG-056 or CLAIM-481 already
  states that the survivors' mixing rate is the exchange Laplacian's gap,
  or states how the separation depends on the exchange graph. Not
  defeated by a chain with asymmetric or irreversible exchange, which the
  claim leaves out, nor by one whose hazard is comparable to the gap,
  where it predicts the separation fails.
tags:
- probabilistic-modeling
- mathematics
- complex-systems
date: '2026-11-11'
line:
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-612
- CLAIM-481
summary: >-
  An integration across the stability part of the formal-apparatus line,
  drafted at its synthesis review. [CLAIM-612](CLAIM-612.md) says the survivors' statistics
  settle on the mixing time and die out far later, and [CASE-231](../cases.d/CASE-231.md) finds the
  ratio about 4k/ε; [CLAIM-481](CLAIM-481.md) says coupling separates time scales where it
  dissipates relative differences, at rates a Laplacian's spectrum sets.
  For symmetric exchange the restricted generator is the exchange
  Laplacian plus a diagonal of hazards, so by Weyl's inequality the
  survivors' relaxation rate is the Laplacian's gap to within the largest
  hazard. That makes the ratio of the two times about nλ₂/ε, which is
  4k/ε for [CASE-231](../cases.d/CASE-231.md)'s two regimes, falls as about π²k/(nε) for n regimes
  in a line and grows as n²k/ε for n regimes all connected. The wording
  is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-612 CASE-231 ARG-056 ADR-075 — Proposed; the claim this rests on, its case and its argument, and the test this claim passed -->

# CLAIM-640: Where viable regimes exchange symmetrically and fail into an absorbing state at small hazards, the survivors settle at the spectral gap of the exchange among the viable regimes to within the largest hazard, so the separation between settling and dying out is a dissipative coupling's, and it depends on how the regimes are connected: for regimes in a line it shrinks as their number grows, and for regimes all connected it grows

## The claim

Take a continuous-time chain on n viable states and one absorbing state
D. Viable states i and j exchange at a symmetric rate k_ij ≥ 0, and state i
fails into D at a hazard ε_i, with 0 ≤ ε_i ≤ ε. Let L be the weighted
Laplacian of the exchange graph, connected, with gap λ₂(L) > 0. Then:

- the generator restricted to the viable states is −(L + E), with E the
  diagonal of hazards;
- the extinction rate λ₁, the least eigenvalue of L + E, lies in [0, ε],
  and to first order in ε/λ₂ it is the mean hazard, (1/n)Σε_i;
- the survivors' relaxation rate, the gap λ₂(L + E) − λ₁(L + E), lies
  within ε of λ₂(L).

So the survivors' statistics settle at the rate the exchange among the
viable regimes dissipates their relative differences, which is [CLAIM-481](CLAIM-481.md)'s
rate for a Laplacian flow, and they die out at about the mean hazard. The
ratio of the two times is, to first order, nλ₂(L)/Σε_i. [CLAIM-612](CLAIM-612.md)'s
separation holds where λ₂(L) is much larger than ε, and how large it is
depends on the exchange graph, not only on the exchange rate:

- **Two regimes** ([CASE-231](../cases.d/CASE-231.md), one hazard ε, rate k): λ₂ = 2k, ratio about
  4k/ε, as [CLAIM-612](CLAIM-612.md) states.
- **n regimes in a line,** rate k, one end failing: λ₂ = 2k(1 − cos(π/n)),
  about π²k/n² ([CLAIM-481](CLAIM-481.md)'s chain), ratio about π²k/(nε). The survivors
  settle more slowly as the line grows, and the separation shrinks as 1/n.
- **n regimes all connected,** rate k, one failing: λ₂ = nk, ratio about
  n²k/ε. The separation grows as n².

## Derivation

With p the row vector of probabilities on the viable states,
ṗᵢ = Σⱼ k_ij(pⱼ − pᵢ) − εᵢpᵢ, that is ṗ = −p(L + E). L + E is symmetric. E
is positive semidefinite with largest eigenvalue max εᵢ ≤ ε, so by Weyl's
inequality λⱼ(L) ≤ λⱼ(L + E) ≤ λⱼ(L) + ε for every j. With λ₁(L) = 0 this
gives λ₁(L + E) ∈ [0, ε] and λ₂(L + E) − λ₁(L + E) ∈ [λ₂(L) − ε,
λ₂(L) + ε]. The least eigenvector of L is the constant vector of norm
one, entries 1/√n, so first-order perturbation gives
λ₁(L + E) ≈ Σεᵢ/n. The law conditioned on survival converges to the
quasi-stationary distribution at the rate λ₂(L + E) − λ₁(L + E), as in
[CASE-231](../cases.d/CASE-231.md), where it is 2.0001.

## Checked

Computed (numpy) for k = 1, one failing state:

| exchange graph | n | ε | λ₁ | gap | λ₂(L) | ratio | first order |
|---|---|---|---|---|---|---|---|
| line | 2 | 0.02 | 0.00995 | 2.0001 | 2 | 201.0 | 200 |
| line | 5 | 0.02 | 0.003905 | 0.3853 | 0.3820 | 98.7 | 95.5 |
| line | 10 | 0.02 | 0.001891 | 0.0999 | 0.0979 | 52.8 | 48.9 |
| line | 20 | 0.02 | 0.000888 | 0.0257 | 0.0246 | 29.0 | 24.6 |
| line | 10 | 0.002 | 0.000199 | 0.0981 | 0.0979 | 493.2 | 489.4 |
| all connected | 5 | 0.02 | 0.003987 | 4.9960 | 5 | 1253 | 1250 |
| all connected | 10 | 0.02 | 0.001996 | 9.9980 | 10 | 5008 | 5000 |

The Weyl bounds held in every row. The two-state row reproduces
[CASE-231](../cases.d/CASE-231.md)'s eigenvalues −0.00995 and −2.01005, its gap 2.0001 and its ratio
201. The first-order ratio is worse where ε approaches λ₂, as at n = 20
in a line.

## What it does not say

- That exchange of probability between regimes is the same thing as
  physical coupling between units. The identification is formal: the
  master equation of a symmetric chain is a Laplacian flow, so [CLAIM-481](CLAIM-481.md)'s
  statement about Laplacian spectra applies to it.
- Anything about asymmetric or irreversible exchange. A reversible chain
  can be symmetrized and gives the same conclusion; a chain with a net
  circulation is left out.
- That [CLAIM-612](CLAIM-612.md)'s "can be" fails anywhere. As ε falls the ratio grows
  without bound for every fixed exchange graph.
- That the survivors' statistics are evidence of persistence. The claim
  says what sets the time to settle, not what the settled values show
  ([ARG-056](../arguments.d/ARG-056.md)).

## Admission

Tested by [ADR-075](../decisions.d/ADR-075.md)'s step 5 at the synthesis review of the formal-apparatus
line, stability part.

- **Route: derivation.** Valid by Weyl's inequality and first-order
  perturbation, checked numerically above. No entry holds it: [CLAIM-612](CLAIM-612.md)
  and [CASE-231](../cases.d/CASE-231.md) give the two-state numbers and the ratio 4k/ε, [ARG-056](../arguments.d/ARG-056.md)
  shows the gap stays near 2 as ε varies and that the separation needs the
  hazard well below the gap, and [CLAIM-481](CLAIM-481.md) lists metastability as a source
  of time scale separation apart from coupling ("Conservation laws,
  metastability, critical slowing near an instability and imposed time
  scales give it too"). None says that this metastable separation is
  itself a Laplacian gap.
- **Route: discriminating prediction.** The components leave open what
  sets the mixing time beyond the exchange rate. The claim predicts that
  with the hazard and exchange rate fixed, the separation falls as 1/n for
  regimes in a line and grows as n² for regimes all connected.
- **Free parameter.** None found: the exchange graph, the rates and the
  hazards are all given, and "small" is closed by the bound ε.
- **A realistic case against its own `defeated_if`.** A line of n = 20
  regimes with ε = 0.02 has a hazard close to the gap: the first-order
  ratio is off by 15%, while the Weyl bounds hold. It does not show the
  claim false; it is the case the claim says the separation weakens in.
- **What it adds.** A rate for [CLAIM-612](CLAIM-612.md)'s "quickly reached", and its
  dependence on the exchange graph. Whether that is enough for a code is
  the owner's call: the mathematics is textbook, and the content is the
  joining of the part's two strands.
