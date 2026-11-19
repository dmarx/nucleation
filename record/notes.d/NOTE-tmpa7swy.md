---
status: Read
paper: LIT-tmpzpom9
title: 'Poole, Lahiri, Raghu, Sohl-Dickstein and Ganguli — Exponential expressivity in deep neural networks through transient chaos'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read in full on 2026-11-19 by a delegated reader from arXiv
    1606.05340v2 (2016-06-17), main text and the supplementary material in
    the same PDF; figures read through their captions. The NIPS 2016
    camera-ready was not compared. The filer rechecked the quotations by
    script against the downloaded text.
date: '2026-11-19'
summary: >-
  Mean-field theory of wide random networks: maps for the length of one
  input and the correlation of two across layers, whose slope χ1 at
  correlation 1 divides the weight and bias variances into an ordered
  phase, where inputs converge, and a chaotic one, where they separate.
  In the chaotic phase a curve's length grows exponentially with depth
  while its curvature holds at a fixed point, so its global curvature
  grows exponentially with depth and not with width; a one-hidden-layer
  network cannot match this.
---
<!-- inactive-ok-file: THEORY-tmpqtb3q THEORY-tmpvtafk — Proposed; entries this reading bears on -->

# NOTE-tmpa7swy: Poole, Lahiri, Raghu, Sohl-Dickstein and Ganguli — Exponential expressivity in deep neural networks through transient chaos

## Contribution

One framework, mean-field theory with Riemannian geometry, for generic
random networks and any nonlinearity: the ordered-to-chaotic phase
diagram, exponential growth of global curvature with depth, a bound on
shallow networks, and random networks as a null model.

## Key results

1. **The transition (Abstract).** "Our results reveal an order-to-chaos
   expressivity phase" transition, and "global curvature grows
   exponentially with depth but not width".
2. **Deterministic at large width (§2).** The random ensemble "constitutes
   a maximum entropy distribution over" deep networks, and propagation
   takes "on an essentially deterministic character". "for any nonzero
   bias σb , the length map has a single stable non-zero fixed point",
   reached "often within only 4 layers".
3. **Correlations are slower (§3).** "Thus correlations typically take
   about 20 layers to approach the fixed point, while lengths need only
   4".
4. **χ1 and chaos (§3).** "Thus we can intuitively understand χ1 as a
   multiplicative stretch factor"; "the logarithm of χ1 is related to the
   well known Lyapunov exponent which is positive" for chaos. Because the
   network stops at a finite depth, "the dynamics are a form of transient
   chaos".
5. **Curvature kept (§4).** "in the chaotic regime, length can increase
   without any decrease in extrinsic curvature"; "extrinsic curvature is
   not lost, but maintained, and ultimately approaches a fixed point";
   so "the global curvature measure L̄G grows exponentially with depth".
6. **Shallow bound (Theorem 1, §5).** "for any choice of W1 and b1 the
   Euclidean length of x1 (θ), satisfies LE ≤ N1 (1 + s)R"; lengths "can
   only expand as the square root of width no matter what shallow network
   is chosen".
7. **Decision boundaries (§6).** "We find, remarkably, that a subset of
   principal curvatures grow exponentially with depth", numerically.
8. **Null model (§7).** Random networks are "an important null model of
   deep signal propagation". SM F names "weight chaos": sensitivity of
   the computed function to weight changes far from the output.

## Assumptions

Infinite width ("the well-known self-averaging assumption"); i.i.d.
Gaussian weights and biases; fully connected feedforward networks;
random initialization only, no training; curvature recursions for a
circle at the fixed-point radius; Theorem 1 for monotone bounded
nonlinearities; simulations with tanh.

## Concepts

Length map and fixed point q*; correlation map and c*; χ1 (stretch) and
χ2; ordered and chaotic phases; transient chaos; extrinsic curvature,
Gauss-map length; principal curvatures of a decision boundary; weight
chaos; random networks as a null model.

## Bearing on the record

- **Edge of chaos.** The paper never says "edge of chaos" or "critical":
  depth's value here lies in the chaotic regime away from χ1 = 1. The
  emphasis on criticality in THEORY-tmpqtb3q and THEORY-tmpvtafk is
  Schoenholz and colleagues'.
- **CLAIM-360.** Theorem 1 against exponential growth with depth is a
  depth separation on one measure, curve length. The abstract's "cannot
  be efficiently computed by any shallow network" goes beyond Theorem 1;
  the link from length to approximation is shown only numerically.
- **QUESTION-281.** The chaotic phase amplifies small differences; the
  ordered phase erases them; new distinctions are made as the curve gains
  turns at a fixed curvature.

## Limitations

arXiv v2, not the camera-ready. Initialization only, infinite width,
fully connected. Decision-boundary curvature is numerical. Theorem 1
bounds length, not approximation.
