---
status: Read
paper: LIT-2253
title: 'Bačić, Schaub, Kurths and Witthaut — Phase locking and multistability in the topological Kuramoto model on cell complexes'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-023 from the arXiv copy (2510.05831v3, 30
    April 2026, 15 pages): Introduction, Results through the rings and
    Platonic solids, the simplex table, Discussion and the stability
    proof in Methods; the worked ring example and the heterogeneous-cube
    section read through their figures. Quotations checked by script.
date: '2026-11-22'
summary: >-
  The phase-locked states of the topological Kuramoto model on a cell
  complex are found in two steps: linear balance conditions (a generalized
  Kirchhoff current law) give a family of candidate flows, and nonlinear
  cycle conditions (a generalized voltage law, sums of inverse sines equal
  to 2πz) select the realizable ones, indexed by winding vectors in both
  dimensions. Since each stable phase difference is below π/2 in size, a
  nonzero winding needs at least five cells in a boundary, so smaller
  boundaries cannot be multistable.
---

# NOTE-tmp7pvg9: Bačić, Schaub, Kurths and Witthaut — Phase locking and multistability in the topological Kuramoto model on cell complexes

## Contribution

A method that finds all phase-locked states of the Kuramoto model with
phases on cells of any dimension, interacting through the cells one
dimension down and up, and a rule for when such states coexist.

## Key results

1. **The model (eq. 4).** dθ/dt = ω − B[n]ᵀK[n] sin(B[n]θ) −
   B[n+1]K[n+1] sin(B[n+1]ᵀθ); for n = 0 the ordinary Kuramoto model.
   Because the boundary of a boundary vanishes, the lower and upper
   interaction variables decouple (eqs. 6–8).
2. **Two-step characterization.** "The generalized KCL yields linear local
   balance conditions, whose solutions define a continuous family of
   candidate solutions. The generalized KVL imposes nonlinear global
   constraints that ensure that phases are single-valued up to integer
   multiples of 2π, thereby selecting a finite set of admissible
   phase-locked states" (Introduction). The free parameters of the first
   step "quantify the amplitude of circulating flows along independent
   cycles of the complex".
3. **Winding numbers do not mean synchrony.** "z[±] = 0 indicates zero
   winding, but does not in general imply complete synchronization of the
   original phase variables θ."
4. **Boundary-size rule (eq. 24).** "multistability can only occur if the
   boundary contains at least five cells"; the reason: "Each reconstructed
   phase difference contributing to a cycle sum is bounded in magnitude by
   π/2, while a nonzero winding requires a total phase accumulation of at
   least 2π. Thus, at least five contributions are required to realize
   nontrivial winding."
5. **Cascades.** Independent windings in the lower and higher sectors
   multiply: "Structural cascades of multistability then arise, with stable
   states inherited from lower and/or upper dimensions"; dual Platonic
   solids show the same patterns (Discussion). Only the tetrahedron among
   the Platonic solids has no cascade (Fig. 6).
6. **Stability (Methods).** Normal states, all phase differences on the
   increasing branch of the sine, are linearly stable; harmonic
   perturbations are neutral.

## Assumptions

Identical natural frequencies in most examples (ω = 0), homogeneous
coupling in the numerics, sine coupling with no phase lag, no noise. The
enumeration is exponential in the number of cells unless restricted to
normal states.

## Concepts

Cell complex; boundary and coboundary operators; Hodge decomposition and
harmonic component; topological nonlinear Kirchhoff conditions; winding
vector; normal phase-locked state; structural cascade of multistability.

## Bearing on the record

- **CLAIM-153.** The same cycle-sum condition the record uses, "the
  accumulated phase differences around each independent cycle must be
  equal to an integer multiple of 2π", generalized to cell complexes, as A
  said. It is the unfrustrated case: the couplings carry no offsets, so
  the monodromy of CLAIM-153 is zero and every obstruction there is
  absent. What it adds is that zero monodromy does not make the coherent
  configuration the only stable one: on a cycle of five or more units,
  stable twisted states with nonzero winding coexist with it. CLAIM-tmp7vutq
  draws the consequence for CLAIM-153's energy readout.
- **THEORY-1082.** Its compatibility condition (phase around every cycle
  zero mod 2π) is the linear, offset version of this paper's voltage law;
  this paper is the nonlinear one with winding and without offsets.
- **QUESTION-282** (background). The cycle parameters here are amounts of
  circulating flow inside a fixed structure, not changes of the structure.

## Limitations

Phase-locked states only, not their basins; a cell complex fixed in
advance; most results for symmetric examples. The rule of five is a
necessary condition for multistability, not a sufficient one.
