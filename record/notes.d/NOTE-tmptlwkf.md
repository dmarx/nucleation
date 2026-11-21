---
status: Read
paper: LIT-2960
title: 'Amari, Park & Ozeki 2006 — singularities of neuromanifolds and the plateaus of gradient learning'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    From the published MIT Press version (Neural Computation 18,
    1007–1065, 59 pp.) on the RIKEN Brain Science Institute publication
    database, https://bsi-ni.brain.riken.jp/database/file/274/280.pdf, the
    first and third authors' institute (ADR-074); the first fetch was reset
    mid-transfer by the proxy, the second returned HTTP 200, 2026-11-21.
    Converted with pdftotext. Read in full: abstract and §§1–7 (pp.
    1007–1052), all theorems; appendix proofs skimmed; references skipped.
    Figures not in the extraction; their captions read. The extraction
    drops some symbols, notably ≠; quotes are corrected only where the
    sense is unambiguous. Read by a reader subagent; filed by a second one,
    which rechecked every quote used here against the extraction.
date: '2026-11-21'
summary: >-
  A review of the authors' work on singular statistical models
  (multilayer perceptrons, gaussian mixtures, a toy cone model), with a new
  analysis of learning in a gaussian mixture. Parameters giving the same
  distribution form a critical set on which the Fisher matrix
  degenerates, "not isolated but form a continuum", at finite parameter
  values; in the space of distributions it becomes a cone apex or a point
  joining two components. Consequences: the MLE is not asymptotically
  gaussian, model-selection criteria lose their justification, a smooth
  prior favours singular points "with an infinitely large factor". In
  gradient learning the critical set is a Milnor attractor even for a
  regular truth: fast attraction to a slow manifold, then slow motion
  along it, the plateau; natural gradient is repelled and has none.
---
<!-- inactive-ok-file: CLAIM-811 CLAIM-844 CLAIM-834 ARG-131 ARG-142 TERM-140 THEORY-2009 THEORY-tmpbobud ARG-tmp1klwj ARG-tmpewh6z — Proposed or Rejected; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" or from this reading, or Proposed readings -->
<!-- inactive-ok-file: LIT-tmp5rr3p LIT-tmpme3im — Deferred, registered 2026-11-21 from these readings, unread -->

# NOTE-tmptlwkf: Amari, Park & Ozeki 2006 — singularities of neuromanifolds and the plateaus of gradient learning

## Contribution

A unified picture of where singularities come from in hierarchical models
and what they break, with toy models solved explicitly; a fast and slow
manifold analysis of gradient learning near a gaussian-mixture
singularity; and generalization and training errors showing that in a
singular model generalization depends on the prior.

## Key insight

In a network, the points where the Fisher matrix degenerates are not at
the edge of anything: they are whole sets of ordinary, finite parameter
values (a unit switched off, two units identical), which the map to
distributions collapses to a pinch point. Gradient learning is drawn
towards such a set even when the truth is elsewhere and then crawls along
it; that crawl is the plateau.

## Assumptions

- Averaged (deterministic) learning equations, small learning rate,
  online gradient; gaussian output noise, so squared error is the
  negative log likelihood.
- Toy models: one hidden unit, a two-unit committee, a cone in ℝ^(d+2),
  a two-component one-dimensional mixture with known mean.
- The mixture analysis is a small-u expansion with v(1 − v) bounded away
  from 0, so it does not cover the v → 0, 1 branches of the critical set.
- §6 assumes the truth at the singularity.

## Key results

- **Degeneracy on a continuum** (p. 1009): the "Riemannian metric
  degenerates at such singular points, which are not isolated but form a
  continuum." For one hidden unit (p. 1013), the Fisher matrix
  "degenerates, and its inverse G⁻¹(θ) does not exist in the set C : vw =
  0. The Cramér-Rao theorem is no longer valid at the critical set C."
  For k units the critical set adds wᵢ = ±wⱼ (Eq. 2.25): "the Fisher
  information matrix degenerates, and its inverse diverges to infinity".
- **Where it sits in the space of distributions.** One hidden unit
  (p. 1012): identifying equivalent points, "the critical set C is reduced
  to a single point. … It consists of two components connected by a
  single point". Two units (p. 1020): a cone, "and the apex is the singular
  point". Cone model (p. 1022): "The apex ξ = 0 is the singularity." In
  general (p. 1025) the image is a cone whose apex is the true
  distribution: "This is called the tangent cone." The word "boundary"
  does not occur in the paper.
- **A Milnor attractor** (p. 1018): "the critical set C works as a
  pseudo-attractor (the Milnor attractor) even when the true distribution
  is at a regular point far from it. The singular point resembles a black
  hole in the dynamics of learning". Reporting Fukumizu & Amari 2000
  ([LIT-tmp5rr3p](../literature.d/LIT-tmp5rr3p.md)), p. 1033: the perceptron "is truly attracted to the line
  and stays inside the line … until it finds a place from which it can
  escape. This explains the plateau phenomenon"; and "The problem of
  plateau cannot be resolved by simply increasing" the learning rate.
- **Fast and slow manifolds** (p. 1035): "a slow manifold emerges around
  the critical set to which the state is quickly attracted by fast
  dynamics, and then the state escapes toward the optimal point slowly in
  the slow manifold. This is a universal feature of the plateau
  phenomenon."
- **Truth at the singularity** (§5.3, Eq. 5.13, p. 1040): u̇ = −ηc₂(v)²u³
  and v̇ of order u⁴; "When u is small, v̇ is of O(u4) and is much smaller
  than u̇, which is of order u3 … u converges to 0 without significantly
  changing v." The paper states no rate. **The reader's derivation, checked
  by the filer:** u̇ = −au³ gives u(t) = u₀/√(1 + 2au₀²t), so u ∝ t^(−1/2).
  And where the flow enters (p. 1034): "the component of the flow entering
  C is extremely slow near C, the flow component parallel to C is
  relatively strong."
- **Natural gradient** (p. 1034): near C "the infinitely strong repulsive
  force works in the direction of escape from C"; in the cone model "no
  slow manifolds appear" (p. 1036).
- **Priors** (p. 1029): "the Bayesian smooth prior is in favor of singular
  points (perceptrons with a smaller number of hidden units) with an
  infinitely large factor."
- **Three cases** (§4): the truth at, near, or far from the singularity;
  "the effect of the singularity is not negligible when the true
  distribution is at, or near, the singularity C" (p. 1018).
- **Algebraic geometry** is "Another general framework … which we do not
  summarize here" (p. 1024).

## Concepts

- **Neuromanifold**; **critical set** C; the reduced space of
  distributions, with a cone-type singularity and its **tangent cone**
  (after Dacunha-Castelle and Gassiat).
- **Milnor (pseudo-)attractor**; **slow and fast manifolds**; **plateau**.
- **Natural gradient**, repelled from C.
- **Cone model**: G = diag(1 + c², c²ξ²), rank one at ξ = 0.

## Connections

Generalized by Wei et al. 2008 ([LIT-3000](../literature.d/LIT-3000.md), [NOTE-tmpl89m0](NOTE-tmpl89m0.md)) from a truth at
the singularity to any truth. Rests on Fukumizu & Amari 2000
([LIT-tmp5rr3p](../literature.d/LIT-tmp5rr3p.md)) and cites Saad & Solla 1995 ([LIT-tmpme3im](../literature.d/LIT-tmpme3im.md)), both
registered Deferred. Cited by Transtrum, Machta and Sethna 2011 ([LIT-3009](../literature.d/LIT-3009.md),
[NOTE-2247](NOTE-2247.md)) for "metric singularities (i.e. model boundaries)" in network
training; the paper itself speaks of critical sets and cone apices. A
modern restatement of the critical set as an attractor of SGD is
[THEORY-2009](../theory.d/THEORY-2009.md). Amari's 1998 natural-gradient paper is [THEORY-082](../theory.d/THEORY-082.md)'s source.

## Bearing on the record

Filed as [THEORY-tmpbobud](../theory.d/THEORY-tmpbobud.md). Dated notes of 2026-11-21 on each entry below.

- **[CLAIM-811](../claims.d/CLAIM-811.md)** — supports its first part: Eq. 5.13 is the claim's
  quartic case (k = 2) in a real model, and the flow reaches the critical
  set at a generic point, as in the claim's qualification. Silent on the
  learning coefficient. [ARG-tmp1klwj](../arguments.d/ARG-tmp1klwj.md).
- **[CLAIM-844](../claims.d/CLAIM-844.md)** — qualifies: slow phases near singularities are real, but
  these plateaus are transients ending in escape; no power law, no
  distribution of timescales.
- **[CLAIM-834](../claims.d/CLAIM-834.md)** — background, supporting A37's "dynamics are separate":
  the dynamics use the Fisher metric and slow manifolds, never resolution.
- **[TERM-140](../terms.d/TERM-140.md)**, **[NOTE-2247](NOTE-2247.md)**, **[ARG-131](../arguments.d/ARG-131.md)** — in networks the singular sets
  are interior and at finite parameters, cone apices rather than edges, so
  "regular inside and singular at the edges" holds for the Transtrum
  group's models and not for networks. [ARG-tmpewh6z](../arguments.d/ARG-tmpewh6z.md).
- **[ARG-142](../arguments.d/ARG-142.md)** — supports its "relevant difference": the Fisher matrix of a
  perceptron degenerates on continua at finite parameters, where
  regular-model theory fails.
- **[THEORY-082](../theory.d/THEORY-082.md)** — supports: the same rank loss at vᵢ = 0, with the
  w = 0 and wᵢ = ±wⱼ components and the Cramér–Rao failure stated directly.
- **[THEORY-2009](../theory.d/THEORY-2009.md)** — parallel: the same critical sets, as invariant and
  attracting sets of SGD.
- **[THEORY-740](../theory.d/THEORY-740.md)** — parallel: its stagewise plateaus wait at the origin
  of a product parameterization, a singular point of the same kind
  (w = 0, v = 0).
- **[QUESTION-363](../questions.d/QUESTION-363.md)**, **[QUESTION-039](../questions.d/QUESTION-039.md)** — background, without a dated note
  here: plateaus as dwelling near a smaller model's critical set, "the
  smaller one forms a critical set within the larger neuromanifold"
  (p. 1030).

Nothing here is an instruction for machine-learning practice.

## Limitations

- A review: the Milnor attractor, the repulsion under natural gradient
  and the entry point of the flow are reported from earlier papers, not
  derived here.
- Toy models with two effective parameters; the mixture analysis is local
  in u; no plateau lengths or escape rates are derived, only shown in
  figures.
- What happens exactly on C under natural gradient, where G⁻¹∇L is
  "0 × ∞", is not addressed.
