---
status: Read
paper: LIT-3000
title: 'Wei, Zhang, Cousseau, Ozeki & Amari 2008 — orbits of gradient learning near overlap and elimination singularities'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    From the published version (Neural Computation 20, 813–843, with the
    journal header and page numbers), on SciSpace (typeset.io, redirecting
    to scispace.com), a scholarly third-party site (ADR-074), fetched
    2026-11-21 and extracted with pdftotext. Read in full: abstract,
    §§1–5, appendix, references; figures from captions and the surrounding
    text only. Other copies located and not needed: CiteSeerX (redirected
    to the Wayback Machine, which reset the connection), the Teikyo
    University repository (metadata only), RIKEN (no response). Read by a
    reader subagent; filed by a second one, which rechecked every quote
    used here against the extraction.
date: '2026-11-21'
summary: >-
  For two-layer networks (RBF networks, perceptrons, gaussian mixtures)
  trained by averaged online gradient descent, the flow near the overlap
  singularity (two hidden units equal) has to leading order a closed first
  integral, so the orbits are universal across these models; its constant
  decides whether an orbit meets the overlap line or passes on to the
  elimination singularity (an output weight zero), which "in most cases"
  it does. Two plateaus follow: on the singularity, a noise-driven random
  walk along the stable part of a line of equivalent models, a
  "Milnor-like attractor"; near it, a shorter crossing where the loss
  changes at order u⁴. It derives orbits, not time courses.
---
<!-- inactive-ok-file: CLAIM-811 CLAIM-844 CLAIM-834 CLAIM-807 THEORY-2009 THEORY-tmpg4aat ARG-tmp0cg6w — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" or from this reading, or Proposed readings -->
<!-- inactive-ok-file: LIT-tmpxs1ua LIT-tmp5rr3p LIT-tmpme3im — Deferred, registered 2026-11-21 from these readings, unread -->

# NOTE-tmpl89m0: Wei, Zhang, Cousseau, Ozeki & Amari 2008 — orbits of gradient learning near overlap and elimination singularities

## Contribution

Universal trajectories near overlap singularities for any teacher, not
only one on the singularity as in Amari, Park and Ozeki ([LIT-2960](../literature.d/LIT-2960.md)), in
the original gradient rather than a reparametrized one; and the
separation of two kinds of plateau by how the orbit meets the singular
set.

## Key insight

Near two coinciding hidden units the averaged gradient flow conserves a
quantity, so where an orbit goes is fixed by where it starts: most orbits
never reach the coincidence and instead switch one unit off. Those that
do reach it land on a line of models that all compute the same function,
and there nothing in the averaged flow moves them; noise does, by a random
walk, until they reach the unstable part and leave. That walk, not a slow
decay, is the long plateau.

## Assumptions

- Two layers, one linear output; smooth activation (Taylor expansion to
  O(u⁴)); squared loss with additive zero-mean gaussian noise.
- Online gradient descent replaced by its averaged equation (stochastic
  approximation).
- The other parameters held at the best fit with one unit fewer: the
  orbits are projections (Remark 1). Small u, leading order only.
- Experiments: two-unit RBF teacher and student, two-dimensional gaussian
  inputs, η = 0.05.

## Key results

- **Two singular types** (§2.3): R(i) "is called the elimination
  singularity" (unit i eliminable), R(i, j) "the overlap singularity" (two
  units identical); with their intersections, "the only singular regions in
  RBF networks and gaussian mixture systems where the Fisher information
  matrix degenerates" (citing Fukumizu 1996).
- **Stability of the critical line** (Theorem 1, p. 825): "When the
  teacher is on the singularity R∗1, the whole critical line of R∗1 is
  stable. When H has both positive and negative eigenvalues, all points on
  the critical line R∗1 are saddles. Otherwise the line R∗1 is divided into
  stable and unstable parts."
- **A first integral** (Theorem 2, Eq. 3.10): with u = J_b − J_a and
  z = (w_a − w_b)/(w_a + w_b), h(u) = ½uᵀu = (2w∗²/3) log((z² + 3)²/|z|) +
  C along orbits.
- **The constant decides** (Eq. 3.15): at C = C₀ = −(8w∗²/3) log 2 "the
  trajectory is tangential to R∗1. Otherwise, if C < C0, the trajectory has
  two intersection points with R∗1; if C > C0, the trajectory is totally
  above R∗1 and certainly passes the elimination singularity R∗2".
- **Generic destination** (§3.2, p. 829): "the basin of attraction of R∗1
  is limited in the regions that |z| is small or |z| is large. So in most
  cases, the model parameter reaches R∗2."
- **On-singularity plateau** (§4.1, p. 832): "the state is first attracted
  to the stable interval of R∗1; then it undergoes a long period of random
  walk on R∗1; finally it leaves R∗1"; "the singularity is completely
  different from the saddle point and is a Milnor-like attractor"; "the
  fluctuations due to the noise and the random sampling of input play an
  important role". Of its length only: "it might take a long time for the
  system to escape the singularity."
- **Near-singularity plateau** (§4.2): near z ≈ ±1, Ė(ξ) "is of order
  O(u4). This tells us that if u is small, E(ξ) remains almost unchanged
  when the model parameter crosses the lines z = ±1."
- **The difference** (p. 839): "In the case of the on-singularity plateau,
  Ė(ξ) = 0 on average … during the period of the near-singularity plateau,
  Ė(ξ) < 0 always holds, although its value is very small."
- **Left open** (§5): "The dynamics of learning near the elimination
  singularities far away from the overlap singularities still remains
  unknown."
- **No rates.** The paper derives no time scaling, power law or
  relaxation exponent: "algebraic" occurs only of the singularities
  themselves and in reference titles.

## Concepts

- **Overlap** and **elimination singularities**; the **critical line**
  R₁* of equivalent models.
- **Milnor-like attractor**: a set with a basin of positive measure that
  is not asymptotically stable.
- **On-singularity** and **near-singularity plateaus**.
- **First integral** of the averaged flow.

## Connections

Generalizes Amari, Park and Ozeki 2006 ([LIT-2960](../literature.d/LIT-2960.md), [NOTE-tmptlwkf](NOTE-tmptlwkf.md)): "first
studied in the case of a gaussian mixture in Amari et al. (2006)". Its
coordinates are Fukumizu and Amari's ([LIT-tmp5rr3p](../literature.d/LIT-tmp5rr3p.md)); its perceptron
companion is Cousseau, Ozeki and Amari 2008 ([LIT-tmpxs1ua](../literature.d/LIT-tmpxs1ua.md)); it cites Saad
and Solla 1995 ([LIT-tmpme3im](../literature.d/LIT-tmpme3im.md)). All three are registered Deferred from
these readings. [THEORY-2009](../theory.d/THEORY-2009.md) (Chen, Kunin, Yamamura and Ganguli) treats the
same two sets as invariant sets of SGD, with noise again deciding
attraction.

## Bearing on the record

Filed as [THEORY-tmpg4aat](../theory.d/THEORY-tmpg4aat.md). Dated notes of 2026-11-21 on each entry below.

- **[CLAIM-811](../claims.d/CLAIM-811.md)**, **[CLAIM-844](../claims.d/CLAIM-844.md)** — the paper is not a source of algebraic
  relaxation: it derives orbits, not time courses. It leaves [CLAIM-811](../claims.d/CLAIM-811.md)'s
  exponent open, parallels its caveat (a conserved quantity decides
  whether the flow reaches the more singular set, and the generic start
  ends where an output weight is zero), and gives [CLAIM-844](../claims.d/CLAIM-844.md) a third rival
  explanation of slow training: a noise-driven walk along a flat line of
  equivalent models. Moved out of their grounds by [ARG-tmp0cg6w](../arguments.d/ARG-tmp0cg6w.md).
- **[CLAIM-834](../claims.d/CLAIM-834.md)** — supports A37's "dynamics are separate": the same
  singular set is reached, crossed or left according to H's signature and
  C. No account of transitions as resolutions.
- **[THEORY-082](../theory.d/THEORY-082.md)** — consistent: it names [THEORY-082](../theory.d/THEORY-082.md)'s set the elimination
  singularity and adds the overlap one.
- **[THEORY-2009](../theory.d/THEORY-2009.md)** — parallel and close: the same two sets.
- **[CLAIM-807](../claims.d/CLAIM-807.md)** — contrast: an algebraic decay at a threshold, which this
  paper does not have.
- **[THEORY-740](../theory.d/THEORY-740.md)**, **[QUESTION-166](../questions.d/QUESTION-166.md)** — contrast: deep linear plateaus are an
  escape from a saddle at the origin in a time of order log(1/scale); this
  paper's on-singularity plateau is a walk on a line.

Nothing here is an instruction for machine-learning practice.

## Limitations

- Leading order in u, averaged dynamics, projection with the other
  parameters frozen at their optimum.
- In the redundant case H = 0, so the leading-order flow of Eqs. 3.6–3.7
  vanishes, yet Eq. 3.14 is stated; the higher-order justification was
  not found in the text.
- Experiments are two-unit RBF networks in two dimensions; the
  near-singularity experiment replaces the random walk by a stationary
  gaussian process.
- No plateau length is derived; elimination singularities away from
  overlaps are left open.
