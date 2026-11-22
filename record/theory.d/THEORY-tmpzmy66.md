---
status: Proposed
promote_when: >-
  All three hold: the rate-equation recursion and its solution
  2m(m+1)/[k(k+1)(k+2)] are confirmed (checked here exactly in fractions
  for m = 1 to 3); the nonlinear-kernel regimes are confirmed against
  Krapivsky, Redner and Leyvraz or another independent derivation; and the
  measured attachment exponents are confirmed as the chapter's report of
  Jeong, Néda and Barabási (2003). The title asserts the measurements only
  as reported, and the routes to linear attachment only as the chapter
  reads them, so neither a remeasurement nor a rival reading of those
  routes meets or defeats it.
title: "Barabási's Network Science chapter on the Barabási–Albert model derives a degree exponent of 3 from arrival at equal steps and the exact degree distribution 2m(m+1)/[k(k+1)(k+2)], shows that dropping growth or preferential attachment loses the scale-free property or stationarity, states after Krapivsky, Redner and Leyvraz that only linear attachment gives a pure power law, reports measured attachment exponents near 1, and reads link selection, copying and optimisation as routes that generate linear attachment"
version: 1
tags:
- network-science
- complex-systems
date: '2026-11-22'
source:
- LIT-2968
bears_on:
- QUESTION-505
summary: >-
  Barabási (2016), LIT-2968, read in the author's web edition in
  NOTE-tmpnpqc8. A secondary source for the kernel regimes of CLAIM-817
  and CLAIM-806 beside THEORY-tmpmsncg, and the record's source for the
  measured attachment exponents (α ≈ 1 for the Internet and citations,
  0.9 ± 0.1 for co-authorship and actors). The sharp edge: its claim that
  preferential attachment is "necessary and sufficient", and that "all
  known models and real systems that are scale-free" have it, is a
  framing that reads geometric and optimisation models as generating
  attachment, which the record does not adopt (CLAIM-817, THEORY-188).
---
<!-- inactive-ok-file: CLAIM-817 CLAIM-806 THEORY-tmpmsncg THEORY-188 — Proposed; the claims this reading bears on and the readings beside it -->

# THEORY-tmpzmy66: Barabási's Network Science chapter on the Barabási–Albert model derives a degree exponent of 3 from arrival at equal steps and the exact degree distribution 2m(m+1)/[k(k+1)(k+2)], shows that dropping growth or preferential attachment loses the scale-free property or stationarity, states after Krapivsky, Redner and Leyvraz that only linear attachment gives a pure power law, reports measured attachment exponents near 1, and reads link selection, copying and optimisation as routes that generate linear attachment

## Source

Barabási (2016), *Network Science*, Chapter 5, "The Barabási-Albert
Model", LIT-2968, read in the web edition on the author's site in
NOTE-tmpnpqc8.

## What was actually shown

k_i = m(t/t_i)^(1/2): "hubs are large because they arrived earlier, a
phenomenon called first-mover advantage" (§5.4). Continuum theory gives
γ = 1/β + 1 = 3, and the rate equation the exact
p_k = 2m(m+1)/[k(k+1)(k+2)], since the continuum theory "fails to
accurately predict the pre-factors" (§5.5). Model A gives an exponential
and Model B a non-stationary distribution tending to a complete graph:
"if one of them is absent, either the scale-free property or stationarity
is lost" (§5.11). After Krapivsky, Redner and Leyvraz, "Π(k) needs to
depend strictly linearly on the degrees for the resulting network to have
a pure power law" (§5.8). Measured: "For the Internet and citation
networks we have α ≈ 1", and "For the co-authorship and the actor network
the best fit provides α=0.9±0.1" (§5.7). Link selection, copying and
optimisation "lead to linear preferential attachment" (§5.9).

## What this does not say

- Not that the measured α settle the mechanism: the measurement conditions
  on degree alone, so fitness and age are confounded, and it counts "only
  ... links added through the arrival of new nodes".
- Not that geometric models need attachment in the sense of a built-in
  rule. The chapter's claim is that every known scale-free model
  *generates* linear attachment, a framing, not a derivation for each.
- Not that real networks have γ = 3: "the degree exponent of real networks
  varies between 2 and 5".
