---
status: Skimmed
paper: LIT-tmps6lx4
title: 'Observational entropy meets maximum entropy'
version: 1
date: '2026-09-25'
summary: >-
  A single coarse-grained entropy, S^τ_M(ρ) = S(τ) − D_M(ρ‖τ), which combines a measurement M (observational entropy) with a max-entropy prior τ set by physical constraints (Jaynes), recovers most entropies used in physics as special cases and admits general second-law theorems.
---

<!-- inactive-ok-file: LIT-tmps6lx4 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpbih3l: Observational entropy meets maximum entropy

## Contribution

The authors define a coarse-grained entropy that merges two traditions: measurement-based observational entropy and Jaynes-style maximum-entropy coarse-graining. The bridge is to treat physical constraints as information-theoretic priors. The new quantity contains most physically relevant entropies as special cases, supports new entropy-increase theorems with links to thermodynamics, and removes pathologies that traditional observational entropy has in infinite dimensions. They illustrate its dynamics in a quantum random-matrix model and a classical hard-sphere gas, and propose it as a basis for a general approach to statistical mechanics.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Motivation (§I): traditional observational entropy is discontinuous and can be infinite in infinite-dimensional quantum systems. Repairing it forces the question of how constraints and priors should enter, which leads to combining a Jaynes prior τ with a measurement M.
- Definition (§IV, eqs 10–13): S^τ_M(ρ) = S(τ) − D_M(ρ‖τ), the prior entropy minus the measured relative entropy. Equivalently it is −Σ p_x log(p_x/V_x), with effective macrostate volumes V_x = Tr(τM_x)·e^{S(τ)}, and it decomposes as Shannon entropy over macrostates plus mean Boltzmann entropy. With canonical or microcanonical τ, the textbook equilibrium entropies appear as maxima.
- Special cases (§V): Jaynes MaxEnt, traditional observational entropy (τ ∝ 1), Boltzmann, Shannon over outcomes, diagonal, entanglement (as a minimum), canonical and stochastic-thermodynamic entropies.
- Second laws (§VII) and mathematical properties (§VIII), including the fix for infinite dimensions. Worked examples are a hard-sphere gas and a random-matrix model (§IX, Apps A–B).
- Conclusions (§X): the entropy is objective, but it takes M and τ as arguments. Which entropy is relevant is a modelling choice. The second laws say entropy increase is generic across many (M, τ), not that "the" entropy increases. Driven Hamiltonians and thermodynamic cycles are left open.

## Open questions

- This is foundations of statistical mechanics. Its tie to the anthology is the relative-entropy/prior structure, which resembles coarse-grained information measures used in learning theory. There is no ML content.
- A deeper reading should check the precise statements of the second laws in §VII (which regimes, which assumptions on τ) and whether the paper has since been published.
