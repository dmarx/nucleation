---
number: 79
status: Skimmed
formerly:
- NOTE-tmpwli33
paper: LIT-036
title: 'Ouazan-Reboul et al. 2023, non-reciprocal metabolic cycles'
version: 1
date: '2026-09-25'
summary: >-
  Catalysts that chemotactically respond to each other's substrates and products interact non-reciprocally. Arranged in a metabolic cycle, such interactions alone make metabolically linked partners cluster together exponentially fast. Cycles with an even number of species separate by parity into two static "clusters of clusters", while odd cycles cannot pair up and give long-lived, system-wide oscillations.
---

<!-- inactive-ok-file: LIT-036 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-079: Ouazan-Reboul et al. 2023, non-reciprocal metabolic cycles

## Contribution

How metabolic cycles first formed so soon after the Earth did is an open origin-of-life question. Most work has relied on externally imposed non-equilibrium conditions such as temperature or proton gradients. The authors propose instead that non-reciprocal interactions arise naturally between catalysts that are partners in a cyclic reaction, and that these interactions recruit the catalysts into self-organized functional structures. They find several classes of self-organized cycles that form through exponentially fast coarsening. Which class forms depends on whether the cycle has an odd or even number of species and on the interaction motifs.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Model (Fig. 1): M catalytic species, where species m turns substrate m into product m+1. Each species responds to both chemicals through mobilities μ(s) and μ(p), giving self-attraction or self-repulsion and non-reciprocal "chasing" or cross-repelling motifs between neighbours in the cycle.
- Even M = 2K (Eqs. 7–8, Fig. 3a): the dominant eigenvalue is real, so the instability does not oscillate. Species of the same parity aggregate and separate from the other parity. Brownian dynamics shows the mean cluster size saturating at half the population.
- Odd M = 2K+1 (Eqs. 9–10, Fig. 4): the dominant eigenvalues are a complex-conjugate pair. Parity pairing is impossible ("a third will systematically come to break them apart"), giving oscillations or oscillatory steady states. For M = 5 the cluster size saturates at population/M.
- Stability diagrams (Fig. 2): the phases include static clusters, self-propelled or rotating "molecules" and oscillations, depending on the chasing strength |μ(s)+μ(p)| relative to the self-attraction strength |μ(p)−μ(s)|.
- Discussion: long-range gradient-mediated interactions could get around the slowness of random encounters and glassy condensates. They would select metabolically linked partners using the information encoded in the reaction network. The authors speculate that odd-membered cycles might be favoured (the citric acid cycle has 11 members). They suggest experiments with catalytic colloids, enzymes and RNA fragments.

## Open questions

- A crisp example of non-reciprocal interactions producing structure and oscillation. The same mathematics, non-Hermitian interaction matrices, comes up in non-reciprocal active matter and in some learning dynamics.
- The odd/even parity result is analytic at linear order. Check how far the nonlinear simulations bear out the long-time phases, especially the claimed "explosive oscillatory stationary state".
- The link to the origin of life is suggestive, not tested. The citric-acid-cycle remark is explicitly speculative.
