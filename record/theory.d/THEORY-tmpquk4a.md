---
status: Proposed
promote_when: >-
  Tests in neural recordings, outside olfaction and the hippocampus, that
  set a hyperbolic geometry against null geometries other than uniform
  Euclidean samples (in particular a Euclidean space with an exponential
  spread of scales, which an exponential count of states also produces),
  and that recover the hierarchy the account says is being represented
  rather than only the curvature. Promoted if hyperbolic geometry wins
  against those nulls in several systems, and if a model links it to the
  representation's function; refuted if a Euclidean model with
  multiscale sampling fits as well. Further Zipf-like rank distributions,
  or more Betti-curve matches against uniform Euclidean cubes alone,
  cannot settle it.
title: "Neural circuits that must represent hierarchically organised states in few dimensions use a hyperbolic geometry, three-dimensional where it has been measured, because hyperbolic space holds exponentially many well-separated states within a small radius; the argument from Zipf's law to this geometry does not hold, and the evidence is two Betti-curve studies tested only against uniform Euclidean nulls"
version: 1
tags:
- neuroscience
- complex-systems
- mathematics
date: '2026-10-16'
source:
- LIT-875
- LIT-872
- LIT-876
extends:
- THEORY-192
- THEORY-191
summary: >-
  Sharpee (2019), [LIT-875](../literature.d/LIT-875.md), read in [NOTE-670](../notes.d/NOTE-670.md): a four-page programmatic review
  with no new result, whose reading filed no THEORY because its claims are
  conjectures. Filed here as Proposed because the record holds two tests of
  the conjecture, odour statistics ([LIT-872](../literature.d/LIT-872.md), [THEORY-191](THEORY-191.md)) and CA1 place-cell
  correlations ([LIT-876](../literature.d/LIT-876.md), [THEORY-192](THEORY-192.md)), and no general statement. The Zipf
  step shows a shared exponential count of states, which any system with
  extensive entropy has, not a shared metric, and the rigidity argument for
  three dimensions cites Mostow's theorem, which concerns finite-volume
  manifolds and says nothing about noisy point clouds.
---
<!-- inactive-ok-file: THEORY-191 THEORY-192 — Proposed; the two findings this account extends, open like it -->
<!-- inactive-ok-file: THEORY-188 — Proposed; the hyperbolic random-graph account, named in Connections and not leaned on -->
<!-- inactive-ok-file: LIT-270 — Rejected; named as the reading that shows Zipf curves arise without meaning, not leaned on -->

# THEORY-tmpquk4a: Neural circuits that must represent hierarchically organised states in few dimensions use a hyperbolic geometry, three-dimensional where it has been measured, because hyperbolic space holds exponentially many well-separated states within a small radius; the argument from Zipf's law to this geometry does not hold, and the evidence is two Betti-curve studies tested only against uniform Euclidean nulls

## Source

Tatyana O. Sharpee (2019), "An argument for hyperbolic geometry in neural
circuits", *Current Opinion in Neurobiology* 58:101–104, [LIT-875](../literature.d/LIT-875.md), read in
[NOTE-670](../notes.d/NOTE-670.md). [NOTE-670](../notes.d/NOTE-670.md) filed no THEORY: the paper's claims are conjectures and
its one finding belongs to its ref. 4. The evidence this account argues
from is that finding and the later test in neural activity:

- Zhou, Smith and Sharpee (2018), [LIT-872](../literature.d/LIT-872.md), read in [NOTE-672](../notes.d/NOTE-672.md), filed as
  [THEORY-191](THEORY-191.md);
- Zhang, Rich, Lee and Sharpee (2022), [LIT-876](../literature.d/LIT-876.md), read in [NOTE-668](../notes.d/NOTE-668.md), filed as
  [THEORY-192](THEORY-192.md).

## What was actually shown

**The argument ([LIT-875](../literature.d/LIT-875.md)).** A hierarchy has exponentially many states at
each further level. A low-dimensional hyperbolic space holds exponentially
many well-separated points within a radius. So a system that must
represent a hierarchy in few dimensions would be expected to use a
hyperbolic metric. In hyperbolic random graphs, density growing
exponentially with radius and degree falling exponentially with it give a
power-law degree distribution (Krioukov et al., Fig. 1), the paper's one
derived link between the geometry and a power law.

**Stimuli ([LIT-872](../literature.d/LIT-872.md)).** In four natural odour sources the rank order of
compound-concentration correlations gives Betti curves that match points
near the surface of a 3D hyperbolic ball and reject uniform Euclidean cubes
of any dimension tried; human descriptor profiles for 127 odorants match a
full 3D hyperbolic ball.

**Neurons ([LIT-876](../literature.d/LIT-876.md)).** Pairwise correlations of a few dozen CA1 cells per
session match points sampled uniformly from a 3D hyperbolic ball and fail
to match low-dimensional uniform Euclidean cubes or shuffled spikes; the
fitted radius grows with the logarithm of exploration time.

**What could have come out otherwise.** In both tests the Betti curves
could have matched a Euclidean cube. They did not.

## What this does not say

- **That Zipf's law signals hyperbolic geometry.** Eq. 2 rewrites
  P(s) ∝ 1/r(s) as a count of states growing as e^E. Any rank power law
  gives an exponential count, and so does any system with extensive
  entropy; the unit slope that makes Zipf special plays no part in the
  step to geometry, and no metric on a circuit's states is proposed
  ([NOTE-670](../notes.d/NOTE-670.md)).
- **That three dimensions are privileged.** Mostow rigidity concerns the
  hyperbolic structure of finite-volume manifolds in every dimension from
  3 up, and says nothing about the stability of a point embedding under
  noise. Three is what the two tests found.
- **That a tree was found.** Neither test recovers the hierarchy: odour
  compounds do not cluster by chemical class, and the CA1 "hierarchy" is
  one of nested place-field sizes.
- **That hyperbolic beats every alternative.** The only null geometry in
  either test is uniform Euclidean sampling. A Euclidean space with an
  exponential spread of scales is the confound [THEORY-192](THEORY-192.md) and [NOTE-670](../notes.d/NOTE-670.md) name.
- **That hyperbolic networks are "maximally responsive to perturbations".**
  The abstract says so; the body only sets two cited literatures side by
  side.

## Connections

- **[THEORY-191](THEORY-191.md)** (odour statistics) and **[THEORY-192](THEORY-192.md)** (CA1 correlations)
  are the two instances, filed as findings with their own limits. This
  account widens them to neural circuits in general, so it `extends` both,
  and falls with them.
- **Hyperbolic random graphs** ([THEORY-188](THEORY-188.md), from [LIT-865](../literature.d/LIT-865.md)) derive the power
  law from two exponentials in the radius; here the same shape is asserted
  for state probabilities without a model.
- **Zipf without meaning** ([LIT-270](../literature.d/LIT-270.md), [NOTE-243](../notes.d/NOTE-243.md)): Zipf-like curves arise in
  text with no semantic structure, so a Zipf curve alone does not identify
  a mechanism.
- **[QUESTION-025](../questions.d/QUESTION-025.md)** asks whether hierarchical attributes keep linear
  directions in an embedding. This account bears on it only through the
  general point that a hierarchy may live in a radial coordinate; [NOTE-670](../notes.d/NOTE-670.md)
  finds nothing toward either answer, so no `answers` is declared.
