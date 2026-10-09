---
number: 674
status: Read
formerly:
- NOTE-tmpi1goy
paper: 'LIT-873'
title: 'Mutual information, neural networks and the renormalization group'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:1704.06279v2, 24
    September 2018, "the accepted (substantially extended) version"; 18
    pp.: main text pp. 1–6, supplementary materials pp. 7–18), text
    extracted with pdftotext. Main text, every section of the supplement
    and the reference list read. The derivation of the mutual-information
    proxy (supplement Eqs. 5–15), the 1D Ising filter comparison (Eqs.
    20–40) and the saturation argument (Eqs. 41–44) followed step by step,
    not re-derived. Figures read as text only: the weight maps and flow
    plots did not survive extraction, so their content is taken from
    captions and text. The publisher's typeset version was not read; the
    authors' label says v2 is the accepted text, but small differences
    from the published version cannot be ruled out.
date: '2026-10-09'
summary: >-
  Makes "the relevant degrees of freedom" of real-space RG an optimizable
  quantity: the coarse variable of a block that carries the most mutual
  information about the system beyond a buffer. Learned from Monte Carlo
  samples, it recovers Kadanoff block spins for 2D Ising and the
  electric-field variables of the dimer model, discards decoupled noise,
  and, iterated, gives the Ising flow and ν ≈ 1.0 ± 0.15, while a
  distribution-fitting RBM keeps the noise. The equivalence with a
  short-ranged effective Hamiltonian is shown only for 1D and quasi-1D.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-185 THEORY-036 THEORY-017 THEORY-194 — Proposed or open; cited as accounts this reading is set beside and what it produced -->

# NOTE-674: Mutual information, neural networks and the renormalization group

## Contribution

Real-space renormalization needs, at every step, a choice of coarse
variables, and that choice has been made by physical insight, case by case.
This paper replaces the insight by an objective: keep the function of a
block that is most informative, in the mutual-information sense, about the
rest of the system once a buffer around the block is excluded. It gives a
sampling-based estimator of that objective for RBM-form coarse-grainings,
shows on the 2D Ising and dimer models that optimizing it from samples
alone recovers the known relevant variables, and shows that iterating it
yields an RG flow from which the critical point and ν can be read. It also
shows, on the same data, that an RBM trained to fit the distribution does
not find them.

## Key insight

What a compression keeps is fixed by what it is asked to stay informative
about. Ask a block's summary to predict the far environment, with the
immediate neighbourhood screened off, and short-range fluctuations,
however strongly patterned, are worth nothing, while the long-wavelength
fields that carry correlations across the buffer are worth everything.
Those fields are the RG-relevant variables. Ask the summary instead to
reproduce the block's own statistics, and the strongest local patterns win,
relevant or not.

## Assumptions

- **Classical lattice systems in equilibrium**, given as Monte Carlo
  samples from P(X) ∝ e^{−βH}. Quantum systems are mentioned only as an
  extension via the quantum-to-classical mapping.
- **Locality and a spatial partition.** X is split into a block V, a
  buffer B and an environment E; the buffer's width is "generally of linear
  extent comparable to V". The method presupposes the lattice geometry
  that defines these regions.
- **RBM-form coarse-graining.** P_Λ(H|V) ∝ exp(Σ_ij v_i λ_ji h_j + Σ_j b_j
  h_j), with conditionally independent binary hiddens; each hidden reads a
  linear functional of the block. P(V, E) and P(V) are replaced by
  contrastive-divergence-trained RBMs, so the objective is computed against
  approximations of the data distribution.
- **The proxy.** P(E) does not depend on Λ, so A_Λ = Σ P_Λ(E, H) log
  [P_Λ(E, H)/P_Λ(H)] is maximized instead of I_Λ. The log of an expectation
  in it is replaced by the expectation of the log (Eq. 13), and that inner
  expectation is estimated from two Monte Carlo samples after burn-in. The
  error of this step is not bounded.
- **Gradients computed by hand.** The Monte Carlo acceptance thresholds
  make parts of A_Λ piecewise constant in Λ, so automatic differentiation
  returns zero; the authors derive the gradients explicitly.
- **Scale.** Ising systems up to 128 × 128, 5,000 samples per temperature,
  up to four RG steps; dimers on 64 × 64 (128 × 128 with the noise spins).
  The training window is three times the block's linear size.

## Key results

- **Kadanoff block spin** (main text, Fig. 2A). 2D Ising, one hidden unit,
  2 × 2 block: uniform coupling to the four spins. With four hiddens on four
  spins, each couples to one spin (Fig. 2B), a sanity check; each may align
  or anti-align, since mutual information cannot tell (supplement, "Multiple
  steps").
- **Boundary weighting** (supplement, Fig. 10). For 4 × 4 and 6 × 6 Ising
  blocks the single filter concentrates on the block's boundary. The
  supplement argues this is what an RG scheme should do: with as many
  hiddens as boundary sites the optimum pins each hidden to a boundary
  spin, decoupling inside from outside.
- **Dimer electric fields** (Fig. 4). On 8 × 8 blocks of the fully packed
  dimer model, two hiddens read the staggered patterns of E_y and E_x + E_y,
  four hiddens add E_x − E_y: low-momentum components of the height-field
  gradient, found without the height mapping. The uniform texture of these
  filters, against the boundary weighting for Ising, is explained as
  coupling to ∇h on the bulk being equivalent to coupling to h on the
  boundary, which dimers do not expose.
- **Noise rejection.** Decoupled, ferromagnetically paired spins on the
  vertices and faces get zero weight (Fig. 4, green).
- **RG flow and ν** (Fig. 5, supplement Figs. 8–9). Effective temperature
  read from a linear fit of A_Λ against β on β/β_c ∈ [0.95, 1.03], or from
  correlations; both agree. Samples starting below T_c flow to lower T,
  above T_c to higher; T_c is located to about 1%. A finite-size collapse
  over four steps and three starting temperatures (all on the paramagnetic
  side) gives ν ≈ 1.0 ± 0.15.
- **1D Ising** (supplement, Eqs. 20–40). For a block of L_V spins with
  buffers of L_B, the proxy is K_{L_B}⟨e_{−1}v_1⟩ for a decimation filter,
  half that for a boundary-majority filter, and vanishing as L_V^{−1/2}
  for a uniform majority filter. Decimation, the known optimal RG for this
  chain, wins among the three; small systems were also checked
  numerically. The full optimum over all filters is not derived.
- **Saturation ⇒ nearest-neighbour Hamiltonian** (supplement, Eqs.
  41–44). In a 1D or quasi-1D system with short-range interactions, if
  adding hiddens no longer raises the mutual information, the effective
  Hamiltonian has no coupling between hiddens attached to different sides
  of V: correlations cannot skip a region, so a residual coupling would
  need an operator on V not yet captured, contradicting saturation.
- **Contrastive divergence fails** (supplement, Fig. 11). A Θ-RBM trained
  on the noisy dimer data uses its first hiddens on the noise pairs; only
  with enough hiddens to absorb them all does it learn dimer textures, and
  those are columnar, which carry zero field, not staggered.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Maximizing a block's coarse variable's mutual information with the environment beyond a buffer recovers the known RG variables of 2D Ising (block spin) and 2D dimers (electric fields) from samples alone | moderate | numerical, two models whose answers were known; Figs. 2, 4, 10 |
| C2 | The learned coarse-graining ignores decoupled short-range noise, however regular | moderate | numerical, one noise model; Fig. 4 |
| C3 | Iterating it reproduces the 2D Ising RG flow, locates T_c to about 1% and gives ν ≈ 1.0 ± 0.15 | moderate | numerical, 128 × 128, four steps, Figs. 5, 8, 9 |
| C4 | RBMs trained to fit the data distribution (KL, contrastive divergence) do not in general perform RG, so Mehta and Schwab's exact mapping does not hold in the generality claimed | moderate | one counterexample, noisy dimers; Fig. 11 and argument |
| C5 | Maximizing this mutual information is equivalent to demanding a compact, short-ranged effective Hamiltonian | weak in general; strong for 1D and quasi-1D nearest-neighbour systems | heuristic argument; 1D filter comparison; saturation argument, Eqs. 41–44 |
| C6 | The procedure is representation-invariant: an invertible re-encoding of the degrees of freedom leaves the optimal coarse-graining unchanged up to that re-encoding | strong for the objective; not for the RBM implementation | invariance of mutual information under bijections, stated in the supplement |
| C7 | Machine learning can become an integral part of theory- and model-building in physics | weak | framing; no result beyond C1–C3 |

## Method

The RSMI algorithm, per RG step: (1) from Monte Carlo samples of (V, B, E),
train two RBMs by contrastive divergence to approximate P(V, E) and P(V);
(2) with those fixed, train a third RBM, the Λ-RBM defining P_Λ(H|V), by
stochastic gradient ascent on a Monte Carlo estimate of the proxy A_Λ; the
a_i parameters drop out and are set to zero; (3) tile the system with
blocks and sample new configurations of H from P_Λ(H|V), halving the
linear size; (4) repeat on the coarse samples. Along the way the stored
samples, Θ-RBMs and values of A_Λ give correlations and an intrinsic
thermometer at each scale.

## Concepts

- **relevant degrees of freedom**: the paper's operational definition is
  the function H of a block V maximizing I(H : E), E the system beyond a
  buffer. It is argued, not proved in general, to coincide with RG's
  notion: the variables that govern long-distance behaviour and keep the
  coarse Hamiltonian short-ranged.
- **buffer (B)**: the region between V and E excluded from the mutual
  information, so that correlations of V with its immediate surroundings,
  "equivalent with short-ranged correlations within V itself", do not
  count.
- **RSMI**: real-space mutual information, the name of both the objective
  and the network that maximizes it.
- **Θ-RBM / Λ-RBM**: the distribution-approximating RBMs and the
  coarse-graining RBM respectively.
- **filter**: the weights λ_ji of a hidden unit, a linear functional of the
  block.

## Connections

The information-theoretic reading of RG it builds on is cited to Gaite and
O'Connor, Preskill, Apenko, Machta et al. and Bény and Osborne; the
objective is presented as a neural implementation of a variant of the
information bottleneck (Tishby, Pereira and Bialek; held here as [LIT-338](../literature.d/LIT-338.md)),
with the environment as the relevance variable. The authors' own extensions
to the quantitative theory, Lenggenhager et al. (Phys. Rev. X 2020) and
Gökmen et al. (Phys. Rev. Lett. 2021), are not held. The paper positions
itself between Mehta and Schwab (2014), who claimed an exact mapping from
deep RBMs to variational RG, and Lin and Tegmark, who denied one; its
resolution is that the cost function decides. Within this record, it
belongs with the treatments of coarse-graining as lossy, scale-relative
description: Rizi on emergence ([LIT-150](../literature.d/LIT-150.md)) and Ladyman on real patterns
([LIT-219](../literature.d/LIT-219.md), [THEORY-036](../theory.d/THEORY-036.md)). It appeared beside García-Pérez, Boguñá and
Serrano's geometric renormalization of networks ([LIT-869](../literature.d/LIT-869.md)), with which
it shares only the theme.

## Bearing on the record

- **Produces [THEORY-194](../theory.d/THEORY-194.md)**: that the variables a coarse-graining keeps
  are fixed by what it must stay informative about, and that for these
  lattice models the far environment selects the RG-relevant ones while
  fitting the block's own distribution does not.
- **[THEORY-036](../theory.d/THEORY-036.md) and [LIT-219](../literature.d/LIT-219.md).** Ladyman's real patterns use RG as the
  example of a scale-relative, lossy description. This paper gives that
  example an operational criterion for which compression counts: the one
  that preserves information about the far field. That is my connection,
  not the paper's; it does not change [THEORY-036](../theory.d/THEORY-036.md).
- **[LIT-150](../literature.d/LIT-150.md).** Rizi's emergence is a predictive many-to-one coarse-graining
  F with no measure of which F is right. RSMI is one: predictive of the
  environment, with a buffer. Again my connection.
- **[THEORY-017](../theory.d/THEORY-017.md).** The supplement claims representation-invariance, since
  mutual information is invariant under bijections of the variables. But
  the method presupposes a spatial split into block, buffer and
  environment, and that split is not invariant under arbitrary bijections
  of X. The parts are supplied from outside, as [THEORY-017](../theory.d/THEORY-017.md) says they must
  be; the invariance holds only for re-encodings that respect the split.
- **[QUESTION-025](../questions.d/QUESTION-025.md) and [THEORY-185](../theory.d/THEORY-185.md).** No direct bearing. There are no
  attributes, no co-occurrence matrix and no lattice. One loose parallel:
  each coarse variable here is a linear functional of its block, and its
  worth is its statistical dependence on distant context, as a word's
  embedding direction draws on its co-occurrence with context words; the
  RG hierarchy is a nesting of such summaries. Nothing in the paper tests
  whether such directions persist when the summarized variables imply one
  another.
- **Anthology.** C4 is a claim about which training objective makes a
  network perform RG, and the paper is ML applied to physical data, which
  the anthology's `physical-sciences` topic could hold; hence
  `anthology-candidate`. It carries no practice instruction this record
  could hold.

## Limitations

- **The 2D evidence is two models with known answers.** Block spins and
  dimer electric fields were rediscovered, not discovered; no system whose
  relevant variables were unknown is attempted, though disordered and
  glassy systems are named as next.
- **The equivalence with RG is proved only in 1D and quasi-1D.** In 2D it
  rests on the numerics and on an argument for the boundary weighting.
- **The 1D comparison is among three hand-picked filters**, not an
  optimization over all; the authors say the exact optimum is hard to find
  analytically.
- **The estimator is rough.** Jensen-type replacement of a log-expectation
  (Eq. 13), two Monte Carlo samples for the inner average, and
  distribution RBMs standing in for P(V, E) and P(V). No error analysis of
  the estimated mutual information is given.
- **ν is estimated from the paramagnetic side only**, three starting
  temperatures, four steps, with an error bar of 15%.
- **The KL counterexample is one dataset**, the noisy dimers; it refutes a
  general mapping but does not characterize when distribution fitting and
  RG agree.
- **Small inconsistencies in the text.** The Ising Hamiltonian is written
  without the minus sign of a ferromagnet (Eq. 3); the abstract promises
  problems "in one and two dimensions" but 1D is treated only analytically;
  Fig. 5's caption plots T against RG step where the text says against
  log₂(ξ₁₂₈/ξ); the supplement refers to its CD-RBM weights as "Fig. 6(A)"
  and its convergence plot as "Fig. 5", which are Figs. 11 and 6.

## Open questions

- Does the objective identify relevant variables where they are not known
  in advance, and do the resulting exponents agree with independent
  methods? A system without an exact solution, checked against
  high-precision Monte Carlo or conformal bootstrap values, would show it.
- Is "maximize information about the environment beyond a buffer"
  provably equivalent to a short-ranged effective Hamiltonian in two or
  more dimensions, and how does the answer depend on the buffer width? The
  authors' later Phys. Rev. X paper is where a proof would be looked for.
- When does a distribution-fitting objective coincide with the
  information-preserving one? A characterization, rather than the one
  counterexample, would settle C4's scope.
