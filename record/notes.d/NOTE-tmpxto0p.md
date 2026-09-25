---
status: Skimmed
paper: LIT-tmpqnwy0
title: 'Barnum, Gaebler & Wilce, ensemble steering and self-duality'
version: 1
date: '2026-09-25'
summary: >-
  In any probabilistic theory where every system can steer its own states (universal self-steering), state spaces are homogeneous and weakly self-dual. Upgrade weak to strong self-duality and add local tomography and qubits, and Koecher–Vinberg plus Hanche-Olsen force finite-dimensional complex C*-algebraic quantum theory.
---

<!-- inactive-ok-file: LIT-tmpqnwy0 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpxto0p: Barnum, Gaebler & Wilce, ensemble steering and self-duality

## Contribution

A bipartite state steers its marginal if, for any decomposition of that marginal into an ensemble, some measurement on the other side prepares exactly that ensemble with the right probabilities. Schrödinger observed that pure quantum states always allow this. The authors show that for weakly self-dual state spaces (isomorphic to their duals, though not canonically), requiring every state of a system to be steerable from a composite of two copies of it amounts to requiring that the state cone be homogeneous. If the space is genuinely self-dual, the Koecher–Vinberg theorem makes it the self-adjoint part of a formally real Jordan algebra, which is very close to quantum mechanics.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1: the motivation is to find properties of entangled states that are parochially quantum and not generic to non-classical theories. Steering is a candidate: it is what Schrödinger found "discomforting", and it is what breaks quantum bit commitment (Bennett–Brassard).
- The proof structure runs §2 (ordered linear spaces formalism), §3 (weak self-duality), §4 (purification: every interior state has a purification in A♦⊗max A, with an ancilla that depends on the state) and §5 (steering). Appendix A has examples and Appendix B covers the "steering product".
- §6 states the route: uniform universal steering gives homogeneity, and self-steering gives homogeneity plus weak self-duality. Strong self-duality then gives, via Koecher–Vinberg and the Jordan–von Neumann–Wigner classification, formally real Jordan algebras. Local tomography plus a qubit then gives, via Hanche-Olsen, C*-algebraic QM with superselection sectors.
- §6 says the chain is "interrupted by a gap" between weak and strong self-duality. The authors float either bridging it or building a consistent theory from weakly-but-not-strongly self-dual homogeneous spaces.

## Open questions

- It is a clean example of a reconstruction strategy: pick an information-theoretic feature (steering) and derive geometry (homogeneous, self-dual cones). It is relevant to the GPT cluster (c21) and to ψ-ontology debates (c20, c19).
- Check whether the weak/strong self-duality gap has since been closed (the authors cite one strategy as [32]) and whether the 2013 journal version differs from arXiv v2.
