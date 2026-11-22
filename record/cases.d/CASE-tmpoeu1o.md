---
status: Active
title: 'Informative-across-buffer variable versus the gap-isolated block in a non-lattice coupled-agent system'
version: 1
standing: documented
kind: executed-study
tags:
- individuation
- complex-systems
- information-theory
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-065
illustrates:
- CLAIM-tmpzdcl1
---
<!-- inactive-ok-file: CLAIM-tmpzdcl1 — new; the finding this study grounds, filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-164 THEORY-198 THEORY-205 — Proposed; the block criterion, the joint-mode unit and the readings this study operationalizes -->

# CASE-tmpoeu1o: Informative-across-buffer variable versus the gap-isolated block in a non-lattice coupled-agent system

## The case

A computation, run for [LEAD-137](../leads.d/LEAD-137.md), of the comparison
[QUESTION-065](../questions.d/QUESTION-065.md) asks for in a system that is not a lattice: do the
variables a region keeps because they are most informative about its far
environment across a buffer coincide with [CLAIM-157](../claims.d/CLAIM-157.md)'s gap-isolated block?

**System.** A linear Gaussian VAR(1) of coupled agents,
`x_{t+1} = A x_t + ξ`, `ξ ~ N(0, I)`, on a modular, non-lattice coupling
graph: `K = 4` communities laid on a path (community `c` couples only to
`c-1` and `c+1`), each community a sparse Erdős–Rényi subgraph of `n = 8`
agents (`p_in = 0.5`), so there is no lattice regularity inside a community.
The path-of-communities supplies locality: the region `R` (community 0)
reaches the far environment `E` only through the buffer `B` (community 1, and
community 2 when the buffer is two wide). `A` is scaled to spectral radius
`ρ`, and the stationary covariance `Σ` solves the discrete Lyapunov equation
`Σ = AΣAᵀ + I`.

**The two variables of `R`, each a unit direction.** The *informative-
across-buffer* variable `u_info` is the direction `w` whose coarse variable
`w·x_R` carries the most information about `x_E`; for jointly Gaussian
variables the mutual information is monotone in the squared canonical
correlation, so `u_info` is the top canonical-correlation direction of
`(x_R, x_E)` under `Σ` — the finite, non-lattice analogue of [THEORY-205](../theory.d/THEORY-205.md)'s
leading transfer-matrix eigenvector and of [THEORY-198](../theory.d/THEORY-198.md)'s coarse-graining
that keeps information about the far environment. The *gap-isolated block*
variable `u_block` is `R`'s slow collective mode, the leading eigenvector of
the dynamics restricted to `R` (`A_RR`): the projector onto the block's joint
mode ([CLAIM-164](../claims.d/CLAIM-164.md)). The match is measured by `overlap = |⟨u_info, u_block⟩|`
in `[0, 1]`, with the stationary-metric correlation of the two coarse
variables as a check.

**Sweep.** Coupling symmetric or asymmetric (one-way, upstream driving
downstream); `ρ ∈ {0.5, 0.8, 0.95}`; cross-community weight `0.1` (strongly
modular) or `0.5` (weakly modular); buffer one or two communities wide; a
lattice-like control in which every node of a community couples uniformly to
the next (a homogeneous slab boundary) beside the generic sparse boundary;
and twenty seeds each. 960 systems. Across the generic cases `R` is a genuine
block, clearing Simon near-decomposability (within-over-across coupling) by
factors of 130 to 650.

## What it can show

Being a documented computation on an explicit model, it shows what the model
does, not what a physical collective does.

- **The lattice coincidence is reproduced, then isolated as a boundary
  effect.** Under the lattice-like homogeneous boundary the two variables
  coincide: overlap mean `0.986`, coarse-variable correlation `0.990`. This
  is the result [QUESTION-065](../questions.d/QUESTION-065.md) starts from, recovered here.
- **In a generic non-lattice system they come apart.** Over the generic
  boundary overlap falls to mean `0.739` and as low as `0.19`; only 42% of
  systems reach overlap `0.9`. The divergence is sharpest with symmetric
  coupling (mean `0.527`); one-way drive keeps them aligned (mean `0.950`).
- **Modularity is not what decides it.** Strong and weak modularity give the
  same overlap (`0.739` vs `0.738`), though `R` clears the block test by two
  to three orders of magnitude throughout. Clearing the gap test does not
  make the block's mode the informative variable. Sharper gaps (`ρ` toward 1)
  raise the coarse-variable correlation only mildly (`0.71` to `0.87`).
- **Mechanism.** In the generic symmetric case `u_info` places `0.89` of its
  mass on the roughly `24%` of `R`-nodes that bridge to the buffer — it is a
  boundary mode — while `u_block` is spread (border mass `≈ 0.23`, the border
  fraction) — it is the collective mode. They agree only when every node is a
  boundary node (the homogeneous slab, where a lattice lives) or under pure
  one-way drive, where `R` as a source has no incoming boundary coupling to
  localize `u_info`.

The study and its wording are the assistant's (Claude, in this session);
adopting it is the owner's call.
