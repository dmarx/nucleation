---
status: Read
paper: LIT-tmpyahtz
title: 'Iqbal and others 2026 — Spontaneous symmetry breaking and Goldstone modes for deep information propagation'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read in full from the arXiv PDF v1 (https://arxiv.org/pdf/2605.14685v1,
    28 pp.), text layer; figures as captions only. Read by a delegated
    reader on 2026-11-19 as a stand-in for LIT-tmp01nqp; the filer
    rechecked every quotation below against the PDF text.
date: '2026-11-19'
---
<!-- inactive-ok-file: CLAIM-606 CLAIM-694 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: LIT-tmp01nqp — Unfetched; cited in this filing of 2026-11-19 -->

# NOTE-tmpsdqio: Iqbal and others 2026 — Spontaneous symmetry breaking and Goldstone modes for deep information propagation

## Contribution

Equivariance is used as an architectural device for propagating
information through depth, whatever the symmetry of the task. A
mean-field phase diagram for an equivariant network, and a protected
Jacobian component derived by an argument in the manner of Goldstone's
theorem.

## Key results

- **Transition.** Middle layers equivariant under U(1) (complex weights,
  radial nonlinearity) or O(k) (block weights). At initialisation and
  large width, "The phase transition is at σW = 1" (§2.3). Below it,
  activations vanish; above it the order parameter c → c* > 0, with a
  mean-field exponent near the transition.
- **Conserved phase, protected Jacobian.** In the broken phase the
  relative phase of two inputs' covariance does not change across layers,
  while its magnitude still decays; "a certain component of the Jacobian
  always remains O(1), no matter how deep the network" (§2.2).
- **No fine-tuning.** "here stable trainability emerges over a wide range
  of parameters provided we are in the symmetry-broken phase" (§2.4),
  unlike the edge of chaos. 100-layer equivariant MLPs train without
  LayerNorm or skip connections.
- **The dissociation.** For generic weights with the same nonlinearity
  the order parameter still turns on above the transition, "but it is not
  accompanied by any performance gain" (Fig. 10): the gain needs the
  equivariance.
- **Recurrent.** Equivariant RNNs and GRUs beat matched baselines on a
  variable-delay copy task and on permuted sequential MNIST.
- **Defects.** A convolutional U(1) RNN grows vortices in ± pairs that
  annihilate on contact, during the storage period of a copy task. "While
  we have yet to demonstrate convincingly that these vortices are used to
  store memory in the model", they persist over the sequence (App. D.3).
- **The workshop paper.** Cited as "Related work in the context of a
  discrete symmetry", "where it was seen that topological defects play a
  role that is somewhat analogous to the Goldstone modes", and as
  "preliminary investigations" (pp. 2–3, 9).

## Assumptions

Large width; i.i.d. Gaussian weights; initialisation only; a smooth
bounded nonlinearity; exact equivariance in the middle layers, broken at
input and output. The order parameter is not long-range order between
neurons, as the authors say.

## Concepts

Spontaneous symmetry breaking; Goldstone mode; order parameter; edge of
chaos; protected Jacobian component; effective rank floor (k for O(k));
winding number and vortex.

## Bearing on the record

- **LIT-tmp01nqp** (the owner's U6 example). Stands in for its thesis,
  not its results: no Z2 analysis, no domain walls, no noise or scaling.
- **QUESTION-125** (does a boundary change coincide with a bifurcation?).
  A clean coincidence and dissociation: the onset of training coincides
  with the transition in equivariant networks, while in generic networks
  the same transition carries no functional gain. Whether a dynamical
  transition has a functional consequence depends here on whether the
  symmetry lets the order parameter be modulated.
- **QUESTION-392.** Relative to architectures without stabilisers,
  equivariance makes very deep training reachable; relative to
  architectures with residuals or normalisation, it is another route to a
  held capability. The verdict turns on the declared space, as the
  question anticipates.
- **QUESTION-281** (amplification, nucleation, bifurcation). A
  supercritical, pitchfork-like onset; what is retained is the input's
  phase on the symmetry orbit.
- **CLAIM-606** and **CLAIM-694.** Vortices end by pair annihilation, as
  CLAIM-606's topological route expects, and come in ± pairs whose count
  varies by channel while net charge stays near zero, which fits the kind
  and token split.
- **TERM-088.** The vortices are individuated descriptively and
  dynamically; the authors claim no constitutive or functional role. The
  owner's "informative computational features" is shown for the Goldstone
  mode, not for the defects.
- **THEORY-187** and **QUESTION-166** (depth in deep linear networks).
  A mechanism that sidesteps the edge of chaos.

## Limitations

Simple benchmarks, by the authors' own account; theory at initialisation
only; defect evidence qualitative, two channels of one model; GRU
comparisons confounded by runtime.
