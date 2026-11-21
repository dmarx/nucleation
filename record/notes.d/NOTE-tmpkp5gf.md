---
status: Read
paper: LIT-tmp7sbn6
title: 'Dambre, Verstraeten, Schrauwen and Massar, Information Processing Capacity of Dynamical Systems, read for the bound on total capacity and its conditions'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader, the text from Europe PMC's
    documented full-text interface (PMC3400147, fullTextXML; ADR-101), the
    equations (eqs 2–8 and 10) from the publisher's open-access page
    (nature.com/articles/srep00514, CC BY-NC-SA), and the publisher's
    Supplementary Information in full (8 pp.: the proofs, the centred
    capacities, estimation). Read: the whole main text, the figure
    captions, the supplement. Skipped: the figures themselves, eqs 11–17
    (the systems' equations) and Methods detail beyond the text. The
    supplement is part of the article and has no entry of its own. Running
    notes on the branch claude/readers/lit-tmp7sbn6 (ADR-108). Every
    quotation below rechecked by the filer by script against the
    downloaded text.
date: '2026-11-21'
summary: >-
  A normalized measure of how well a linear readout of a driven system's N
  observed variables reconstructs each function of its past inputs, and two
  theorems: capacities for orthogonal functions sum to at most N for i.i.d.
  input and infinite data (Theorem 4), and to exactly N over a complete
  basis when the system also has fading memory and N linearly independent
  variables (Theorem 7). Noise counts as a further input. Simulations show
  the total near N up to the undriven system's edge of stability and a
  memory–nonlinearity trade-off as input scaling grows.
---
<!-- inactive-ok-file: THEORY-tmpr5fuq CLAIM-tmpask80 CLAIM-tmpd1shn ARG-tmpubyzo ARG-tmp53559 ARG-tmpr04sw CLAIM-tmpyy261 THEORY-1431 — Proposed; the reading, and the entries it bears on -->

# NOTE-tmpkp5gf: Dambre, Verstraeten, Schrauwen and Massar, Information Processing Capacity of Dynamical Systems, read for the bound on total capacity and its conditions

## Contribution

A normalized, implementation-independent measure of all the computation,
linear and nonlinear, short and long memory, that a driven system does
with a linear readout, and the theorem that its total is fixed by the
number of independent observed variables. It generalizes Jaeger's (2002)
linear memory capacity to a complete basis of functions of the input
history. The reading is THEORY-tmpr5fuq.

## Key results

- **The measure.** C[X, z] = 1 − min MSE/⟨z²⟩ for the best linear readout
  (no bias) of the N observed variables, normalized to 0 ≤ C_T ≤ 1
  (Proposition 3), which the supplement says holds "also for dynamical
  systems that are not fading memory" (§1.2, note 1).
- **The bound** (Theorem 4). For any finite set of orthogonal functions
  y_l of past inputs with finite fourth moments, "in the limit of an
  infinite data set T → ∞, the sum of the capacities for these functions
  is bounded by the number N of output functions (independently of h, of
  the set Y_L, or of its size)". Fading memory is not among its
  conditions.
- **Equality** (Theorem 7). With fading memory (Definition 6), N linearly
  independent variables (full-rank correlation matrix) and Y_L tending to a
  complete orthogonal basis, the sum "tends towards the number N of output
  functions". Abstract: the total is "bounded by the number of linearly
  independent state variables of the dynamical system, equaling it if the
  system obeys the fading memory condition".
- **Universality**: all systems with fading memory and linearly
  independent internal variables "have in principle the same total
  normalized capacity to process information"; "information is not lost
  inside these networks but merely transformed in various non-linear
  ways". And "Some systems may carry out more interesting computations
  than others".
- **At the edge** (Fig. 1): "For very small input scaling, the capacity
  CTOT remains close to N up to the bifurcation point of the undriven
  system and then drops off rapidly. As the input scaling increases, the
  loss of capacity becomes less abrupt, but its onset shifts to lower
  values." The drop is put down partly to truncation of the basis and
  partly to loss of fading memory.
- **The trade-off** (Fig. 3): "on one end of the scale they store the
  information but then are linear, while on the other end they immediately
  process the input in a highly non-linear way, but then have small linear
  memory." The parameter swept is the input scaling ι (an echo state
  network at spectral radius 0.95, the logistic map at 2.5) and the
  sampling period, not distance from the edge.
- **Noise as input**: with signal u and noise v both i.i.d. inputs, "It is
  only over the full space that Theorem 7 holds and that the capacities
  will sum to N. However since v is unknown, the capacities which are
  measurable are those which depend only on u … these capacities will not
  sum to N." With K equal-power inputs, "for a strictly linear system …
  the capacity for a single input should equal N/K" (Fig. 4).
- **Non-i.i.d. input**: a basis "is often not feasible", so "the upper
  bound on total capacity is largely a theoretical insight" there.
- **The edge as an assumption**: the echo state network is set "close to
  the edge of stability, a region in which the most useful processing
  often occurs", citing Langton (Fig. 2 caption).

## Assumptions

Stationary i.i.d. input from a fixed distribution; a linear readout of N
observed variables, with no bias (a centred variant, supplement §2, keeps
both theorems); infinite data and washout; finite fourth moments. For
equality also: fading memory (the state is a limit of functions of
finitely many past inputs, independent of the initial condition), full rank,
a complete basis, and a basis covering every input, noise included.

## Concepts

Capacity C[X, z]; the Hilbert space of fading-memory functions; the
fading-memory dynamical system; linear memory capacity and nonlinearity as
summaries of the capacity profile; Legendre-product bases; noise as an
unobserved input; the link to Wiener-series system modelling.

## Bearing on the record

- **CLAIM-tmpask80** (supports strand 2, qualifies the thesis). The bound
  and the redistribution between linear memory and nonlinearity are here.
  But the total is *constant* at N throughout the fading-memory regime and
  *falls* past the edge (Fig. 1), so for this measure nearness to the edge
  cannot raise capacity, which is stronger than the claim. The
  redistribution the paper shows is driven by input scaling at a fixed
  spectral radius, not by distance from the transition; and its edge is the
  undriven system's loss of linear stability, not a collective critical
  point. ARG-tmp53559.
- **ARG-tmpubyzo** (supports, and closes its stated gap). The conditions it
  had not checked are: for the bound, i.i.d. input, a linear readout and
  infinite data; for equality, fading memory and rank N, with noise
  counted as an input. "Raises nothing in total" holds for every
  fading-memory system with N independent variables; how the allocation
  moves with distance from the edge is not studied.
- **CLAIM-tmpd1shn** (an instance of Theorem 7). The scalar reservoir with
  |a| < 1 has fading memory and N = 1. With η as the paper's second input
  v, x lies in the span of the degree-one functions of u and η, so over the
  full basis the capacities sum to 1 at every a; the u-functions take
  s²/(s² + σ²). At σ² = s² the u-share is ½ = N/K with K = 2, the paper's
  linear benchmark. The claim's "scalar case of the bound" understates it:
  it is the equality case. The readout-noise result is not in the paper.
  ARG-tmpr04sw.
- **QUESTION-tmp2hhlc** (answers the first part). A capacity measure and its
  bound, for i.i.d.-driven systems with a linear readout; not the
  allocation against distance from a transition. The i.i.d. input is
  chosen "so that any measured structure will be due to the dynamical
  system itself", so the paper cannot speak to point 3, the environment.
- **CLAIM-tmpyy261** (bears on it). The paper's edge is the stability edge
  of a deterministic map: neither chaos in the strict sense nor branching
  criticality.
- **THEORY-1431, NOTE-1907, NOTE-1988** (a parallel, a background and a
  contrast; no edges). The origami reservoir is a physical system with a
  trained linear readout to which the measure would apply; Andrieu and
  colleagues' contraction is the condition that gives fading memory;
  Schlag and colleagues' fast weights have a capacity bounded by dimension
  that is written, not driven.

## Limitations

- Theory only for i.i.d. input, and only for a linear readout.
- Asymptotic in the data length; equality needs a complete basis, never
  reached numerically, so measured totals are lower estimates, truncated
  by a threshold and by polynomial degree.
- The drop past the edge in Fig. 1 mixes loss of fading memory with
  truncation, and the paper does not separate them: a gap in its own
  argument for reading the drop as a property of the system.
- One echo-state network instance; no study of allocation against
  spectral radius; readout noise is not treated apart from noise as input.
- Every orthogonal function counts equally, so equal totals say nothing
  about usefulness for a given task, as the authors say.
