---
status: Open
title: "Does the heat kernel of a metric tree satisfy the Hellinger Hölder and separation bounds of the multiscale hyperbolic diffusion theorem, with which Hölder exponent, and when does the diffusion operator of sampled data approximate a latent tree's heat kernel?"
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: learned-structure
summary: >-
  The promotion condition formerly on [THEORY-478](../theory.d/THEORY-478.md), moved here unchanged
  when [THEORY-478](../theory.d/THEORY-478.md) was narrowed on 2026-10-19 to the conditional
  equivalence under two Hellinger bounds, with the admissible range
  α < θ/β. Whether a metric tree's heat kernel meets those bounds, with
  which θ, and whether sampled data yield such a kernel, is not settled
  by anything the record holds.
---

# QUESTION-tmpeikcb: Does the heat kernel of a metric tree satisfy the Hellinger Hölder and separation bounds of the multiscale hyperbolic diffusion theorem, with which Hölder exponent, and when does the diffusion operator of sampled data approximate a latent tree's heat kernel?

## Why it is a question

[THEORY-478](../theory.d/THEORY-478.md), narrowed and promoted on 2026-10-19 under [ADR-047](../decisions.d/ADR-047.md) v2, makes
a conditional statement. Suppose the diffusion densities' Hellinger
distances obey a Hölder bound with exponent θ in d_T / t^(1/β), and a
separation bound once d_T exceeds a multiple of t^(1/β). Then for
0 < α < θ/β the multiscale hyperbolic diffusion distance of [LIT-870](../literature.d/LIT-870.md) is
two-sided equivalent to min{1, d_T^(αβ)}.

Two things are left unsettled.

- **The tree heat kernel.** [LIT-870](../literature.d/LIT-870.md) takes β = 2 and θ = 1 for the heat
  kernel of a metric tree. It cites the Gaussian and Hölder kernel bounds
  (Lemmas C.4–C.6) without proof. Its passage to a Hellinger bound for
  close points (Proposition C.5) holds as written only for d_T ≥ 1, and
  [NOTE-675](../notes.d/NOTE-675.md)'s repair gives θ = 1/2. So the range of α for which the
  theorem applies to trees is not fixed.
- **The data bridge.** That the diffusion operator of a sampled point
  cloud with a hidden hierarchy approximates a tree's heat kernel is
  assumed, by analogy with the manifold limit of diffusion maps.

It bears on [QUESTION-025](QUESTION-025.md). Whether hierarchy shows in co-occurrence
statistics through a multiscale distance needs the second bridge.

## What would answer it

The condition formerly on [THEORY-478](../theory.d/THEORY-478.md), unchanged. A complete proof that
the heat kernel on a metric tree meets the Gaussian upper, lower and
Hölder bounds the theorem uses, with the Hölder step of Proposition C.5
repaired for close points. Also a stated condition under which the
diffusion operator of sampled data approximates a tree's heat kernel.
The equivalence to a thresholded snowflake would then be a theorem on its
stated range of α, and the bridge from data to it an assumption with
content. Better benchmark scores, or more datasets where the method has
the best mean average precision, cannot settle it. Neither can the
experiments at α = 1/2, which lie outside the theorem's range.
