---
number: 692
status: Read
formerly:
- NOTE-tmpu0mur
paper: 'LIT-889'
title: 'Symmetries and phase diagrams with real-space mutual information neural estimation'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v3 (arXiv:2103.16887v3, 18
    October 2021, "Accepted version", 27 pp.: main text pp. 1–17,
    Supplemental Material Appendices A–C pp. 18–26, references), text
    extracted with pdftotext. Main text, all three appendices, the two
    tables and the reference list read. The bound derivations (Eqs. 2–10,
    A4–A14) and the Gumbel-max lemma (Eqs. B3–B7) followed step by step,
    not re-derived; the directed-loop Monte Carlo appendix (C) read for
    what it does, not checked. Figures read as text only: the plots and
    filter maps did not survive extraction, so their content is taken
    from captions and text. Fractions in the extraction were flattened;
    "12 log 2" in Sec. III D 2 and Fig. 11 is read as ½ log 2. The v1 PDF
    (22 pp., titled "Phase diagrams with real-space mutual information
    neural estimation") was opened for its title page and searched for
    keywords only: it already has the chipping model and the PCA of the
    filter ensemble, and the symmetry projections appear to be the v3
    addition the arXiv comment names. The publisher's typeset version was
    not read. LIT-878 and NOTE-681 were read first, so this note records
    what the companion adds. The cited optimality theorem (Gordon et al.,
    Phys. Rev. Lett. 126, 240601) was not read.
date: '2026-10-09'
summary: >-
  The long companion of [LIT-878](../literature.d/LIT-878.md). Derives the RSMI-NE estimator and shows
  that the maximal real-space information counts ordered sectors (1 bit
  for the Ising ferromagnet, 2 for columnar dimers), decays exponentially
  with the buffer off criticality and algebraically at it, and that the
  ensemble of optimal filters from independent runs maps a degenerate
  subspace whose projections show broken lattice symmetries and the
  dimers' emergent U(1). All the models' answers were known; the
  non-equilibrium example is one figure.
---
<!-- inactive-ok-file: THEORY-194 THEORY-017 THEORY-019 THEORY-002 THEORY-036 QUESTION-025 THEORY-185 LIT-246 LIT-256 THEORY-198 — Proposed, Deferred or open; cited as accounts this reading is set beside and the estimator papers it rests on -->

# NOTE-692: Symmetries and phase diagrams with real-space mutual information neural estimation

## Contribution

[LIT-878](../literature.d/LIT-878.md) announced the neural estimator for real-space mutual information
(RSMI) and used it on one model. This paper is the full account of the
algorithm and adds three things. It tests the information value itself
as a phase diagnostic on a second model, the 2D Ising model, with a
buffer-scaling analysis that separates ordered, critical and disordered
phases. It introduces the ensemble of optimal filters from independent
runs as an object of study, and shows that its geometry carries the
system's symmetries, broken and emergent, and that PCA of it recovers the
pristine operators from data where they never appear alone. And it gives
a procedure for the number of coarse variables, and a first run out of
equilibrium.

## Key insight

The RSMI objective does not pick out one filter; it picks out a set of
equally good ones, and the shape of that set is information about the
system. Where a symmetry acts on the filters and leaves the information
unchanged, independent optimizations scatter over the symmetry's orbit,
so the scatter of many runs, projected onto the right basis, draws the
representation of the symmetry: a discrete cycle for a broken lattice
symmetry, a circle for an emergent continuous one.

## Assumptions

- **Everything in [NOTE-681](NOTE-681.md)** carries over: a sampled distribution, a
  block–buffer–environment partition fixed in advance, translation
  invariance (one Λ for all blocks), a linear filter before
  discretization, and InfoNCE as a lower bound. Here the bound's
  ceiling is stated: InfoNCE ≤ log K, so it cannot be tight when
  e^I > K (Eq. A10). With K = 100 (Ising) and 400 (dimers) the ceiling is
  about 4.6 and 6.0 nats against at most log 4. Tightness below the
  ceiling is still not measured.
- **Geometry per model** (Table I). Ising: L_V = 4 (ferromagnet) or 5
  (antiferromagnet), L_B from 0 to 8, environment shell L_E = 10, one
  binary component, 64 × 64 lattice. Dimers: L_V = 8, L_B ∈ {2, 4, 6, 8},
  L_E = 4, two binary components, 64 × 64 lattice, 32 400 samples.
- **The coarse variable's alphabet is chosen** (binary). Its number of
  components is chosen by the saturation procedure of Sec. III D 2, not
  fixed blind.
- **The optimality theorem is cited**: that RSMI optima are the most
  relevant operators was "formally proven, at least for critical systems
  in equilibrium", in Gordon et al. (2021). Off criticality and out of
  equilibrium the identification is by example.
- **The symmetry readings need a basis.** The projections of Fig. 9 are
  onto the pristine filters (P₁, P₂) and (E_x + E_y, E_x − E_y), which
  were identified using the known field theory.

## Key results

- **Ising phase diagram from the information** (Figs. 3, 6). Below T_c
  the maximal I_Λ is exactly 1 bit at every buffer: it counts the two
  ferromagnetic sectors. At T_c it shows a step that sharpens as L_B
  grows. In the paramagnet it decays exponentially with L_B and is
  numerically zero for L_B ≥ 2 at T = 4. At the critical point it decays
  algebraically, fitted exponent υ ≈ 0.09.
- **Dimer phase diagram** (Figs. 5a, 6c). log 4 below T_BKT; algebraic
  decay above it, I_Λ(T → ∞) ~ L_B^(−υ) with υ ≈ 1.16. The authors read
  the continuity of the filters' T-dependence above T_BKT as a further
  sign of a BKT-type transition.
- **Ising filters** (Figs. 3c, 7). Uniform at low T (the magnetization),
  staggered for the antiferromagnet, random at high T; at T_c they couple
  to the block's boundary, because at criticality the shared information
  scales with the interface area (citing Wilms, Troyer and Verstraete,
  and Wolf et al.). The boundaryness ratio (Eq. 19) peaks at T_c and
  sharpens with L_B; for T slightly below and above T_c the filters
  separate with growing L_B toward the ferromagnetic and paramagnetic
  fixed points, "consistent with" the repulsive Ising fixed point. The
  transformations are not iterated.
- **Dimer filters** (Fig. 5b). As in [LIT-878](../literature.d/LIT-878.md): columnar and plaquette at
  low T, staggered (electric fields) at high T, and in between a
  continuous interpolation between plaquette and staggered filters,
  attributed to the competition of the cosine and gradient terms of the
  sine-Gordon action in a finite system.
- **PCA of the ensemble** (Fig. 8). On filters from 0.7 < T < 3.7, where
  no pristine filter appears alone, the leading principal components are
  the pristine plaquette and staggered filters, so the operators are
  recoverable from a parameter window that never isolates them.
- **Broken symmetries in the ensemble** (Fig. 9a–c; 500 runs per
  temperature). Below T_BKT the projection onto (P₁, P₂) has four
  peaks (±P₁, ±P₂) and a central one (±C). C4 acts as a Z4 cycle on the
  peaks; translations T_x, T_y act on ±P₁,₂ as Z2 × Z2; ±C is invariant,
  a trivial representation. Columnar and plaquette pairs appear with
  equal frequency, reflecting their equal information. Just above T_BKT
  the central peak vanishes (C4 restored) and four diagonal peaks
  appear: the filters X = P₁ − P₂, Y = P₁ + P₂, which read site parity
  and give a second, one-dimensional representation of the broken
  translation. As T rises the ±P₁,₂ peaks broaden and go.
- **Emergent U(1)** (Fig. 9d–g). At T = 15 the projection onto the
  electric-field pair is approximately invariant under continuous
  rotations, and RSMI is constant in the rotation angle ϑ of
  (cos ϑ E_x − sin ϑ E_y, sin ϑ E_x + cos ϑ E_y). Below T_BKT the
  filters do not overlap the fields; just above it the U(1) has not yet
  emerged, because of plaquette correlations in the finite system.
- **Why a continuous symmetry survives a discrete H** (Sec. III D 1,
  Fig. 10, Eqs. 20–22). The filter acting on dimer bonds equals the
  lattice gradient of the block-averaged height, and block averaging
  turns the four-valued lattice height into a quasi-continuous field like
  the sine-Gordon one. The same filters are obtained without
  discretization; τ matters only in the ordered phase, where it shrinks
  the search space, an "a posteriori entropy cut-off".
- **How many components** (Fig. 11). Information rises with the number
  of binary components until it saturates: two for dimers in both limits
  (log 4 below T_BKT, about ½ log 2 at T → ∞ for L_B = 4), one for Ising.
  One dimer component gives half the two-component value with a filter
  equal to one of the pair; extra components converge to filters linearly
  dependent on the first two.
- **Chipping and aggregation** (Sec. IV, Fig. 12). On the 1D model of
  Rajesh and Majumdar at density 1 (L = 256, L_B = 8), the optimal filter
  averages the block mass at every w; the maximal information saturates
  at different values in the two phases and peaks slightly at the
  transition.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In ordered phases the maximal RSMI equals the log of the number of symmetry-broken sectors (1 bit Ising, 2 bits columnar dimers) | moderate | two models, Figs. 3a, 5a; the sector-counting reading is argued, not proved |
| C2 | The scaling of maximal RSMI with the buffer distinguishes exponential (disordered) from algebraic (critical) correlations | moderate | Ising paramagnet vs Ising T_c and free dimers, Fig. 6; two fitted exponents, no error bars |
| C3 | At the Ising critical point the optimal filter couples to the block's boundary, and the boundaryness peak locates T_c more sharply as the buffer grows | moderate | Figs. 3c, 7; area-law explanation cited |
| C4 | The ensemble of optimal filters from independent runs maps an RSMI-degenerate subspace whose structure carries the symmetries, broken and emergent | moderate for this model | Fig. 9, 500 runs per T; dimer model only; projections onto bases chosen from the known operators |
| C5 | PCA of the ensemble over an intermediate window recovers the pristine operators | moderate | Fig. 8; one window, one model |
| C6 | Discretizing H does not prevent a continuous symmetry from appearing in the ensemble and regularizes the ordered-phase search | moderate | Eqs. 21–22, Fig. 10; "the same filters are obtained" without discretization, stated without a figure |
| C7 | The number of coarse components at which RSMI saturates is the number of relevant operators carrying the long-range information | moderate | Fig. 11, dimers in two limits; Ising asserted |
| C8 | RSMI-NE detects a non-equilibrium phase transition from configurations alone | weak | one 1D model, one figure; the filter is mass averaging throughout; formal understanding said to be missing |
| C9 | The physical interpretability comes from RSMI being a well-defined physical quantity, not from architectural choices | weak | asserted; architecture insensitivity stated, not shown |

## Method

As in [NOTE-681](NOTE-681.md), with the details this paper adds. Per mini-batch of K
samples: coarse-grain each block, form the K × K score matrix F_ij =
f_Θ(h_i, e_j), and ascend log Q + log K (Eq. 16) in Λ and Θ by Adam at
learning rate 5 × 10⁻³. The Gumbel-softmax relaxation ε is annealed
exponentially, ε_t = max(ε_min, ε_max e^(−rt)), with r = 5 × 10⁻³ and
(ε_max, ε_min) = (0.5, 0.1) for Ising, (0.75, 0.1) for dimers. Training
stops when successive epoch estimates differ by less than a threshold,
with optional smoothing and an optional BFGS refinement of Λ alone.
Dimer samples come from a directed-loop Monte Carlo started from
Propp–Wilson random coverings, with bounce probabilities minimized by
linear programming (Appendix C). The ensemble analyses repeat the
optimization many times at each temperature and study the distribution
of the returned filters: PCA over a temperature window, and projections
onto pairs of pristine filters.

## Concepts

- **ensemble of filters**: the distribution of RSMI-optimal Λ over
  independent runs at fixed physical parameters; introduced here as "a
  novel concept".
- **RSMI-degenerate subspace**: the set of filters attaining the same
  maximal RSMI; the ensemble samples it.
- **pristine filters**: columnar C, plaquette P₁,₂ and staggered S₁,₂
  (electric fields), found alone in the low- and high-T limits.
- **boundaryness**: |Σ_boundary Λ_i| / |Σ_bulk Λ_i| over the block (Eq. 19).
- **compression rate**: here set by the number and alphabet of H's
  components; the relevant information is the system's, not the user's.
- **site parity**: which of two translation-related columnar states a
  region is in; read by the filters X = P₁ − P₂, Y = P₁ + P₂.

## Connections

The algorithmic half reviews the variational bounds of Barber–Agakov,
Nguyen–Wainwright–Jordan, MINE ([LIT-256](../literature.d/LIT-256.md)) and InfoNCE, following Poole et
al. ([LIT-246](../literature.d/LIT-246.md)); the van den Oord et al. source of InfoNCE is held in the
anthology ([ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md)). The coarse-graining uses the Gumbel-softmax of
Jang, Gu and Poole and Maddison et al. The physics rests on Koch-Janusz
and Ringel ([LIT-873](../literature.d/LIT-873.md)), Lenggenhager et al. ([LIT-881](../literature.d/LIT-881.md)) and Gordon et al.
(not held), and on Alet et al.'s interacting dimers. The PRL ([LIT-878](../literature.d/LIT-878.md)) is
the short paper; this one shares its method and dimer results, as the
arXiv listing's "substantial text overlap" note says. For symmetries
from learned objects it cites Bondesan and Lamacraft (not held).

## Bearing on the record

- **[THEORY-194](../theory.d/THEORY-194.md).** Adds the 2D Ising model with a buffer-scaling analysis
  and a flow of filters toward the fixed points without iteration. All
  variables found were known, and the paper uses that knowledge to name
  them; no exponent is checked against an independent method. It does
  not meet `promote_when`. A candidate further source; I have not edited
  [THEORY-194](../theory.d/THEORY-194.md).
- **[THEORY-019](../theory.d/THEORY-019.md).** That account says symmetry forces degeneracy but
  degeneracy does not identify a symmetry. This paper reads symmetries
  off a degeneracy of the RSMI objective. It is consistent with
  [THEORY-019](../theory.d/THEORY-019.md) rather than against it: the symmetries it reports were
  known from the field theory, and they are drawn by projecting onto
  bases already identified with that theory's operators; the paper
  claims to observe them, not to identify an unknown group from the
  ensemble alone. A case where the ensemble's geometry identified a group
  nobody knew would test [THEORY-019](../theory.d/THEORY-019.md)'s converse. My connection, not the
  paper's.
- **[THEORY-017](../theory.d/THEORY-017.md) and [THEORY-002](../theory.d/THEORY-002.md).** [NOTE-681](NOTE-681.md) noted that the information
  objective fixes a subspace of filters and leaves the basis to symmetry
  or chance. Here the authors say so themselves ("an RSMI-degenerate
  subspace for the kernels") and make the subspace the object of study.
  The basis remains an extra supplied from the known operators, as
  [THEORY-017](../theory.d/THEORY-017.md) says a basis is; and like [THEORY-002](../theory.d/THEORY-002.md)'s kernels, the
  objective determines its optima only up to the symmetry group of what
  it sees.
- **[QUESTION-025](../questions.d/QUESTION-025.md) and [THEORY-185](../theory.d/THEORY-185.md).** No direct bearing. The one transferable
  observation: the number of coarse variables is chosen by where the
  information stops growing, and extra components come out linearly
  dependent on the first ones, so "how many independent directions" is
  answered by saturation, not assumed. Nothing here involves attributes
  that imply each other.
- **[THEORY-036](../theory.d/THEORY-036.md).** As for [LIT-873](../literature.d/LIT-873.md) and [LIT-878](../literature.d/LIT-878.md): the buffer width is an
  explicit scale relative to which a description is real. My connection.
- **[LIT-881](../literature.d/LIT-881.md) and [THEORY-198](../theory.d/THEORY-198.md).** Sector counting (C1) is a case of the full
  capture [LIT-881](../literature.d/LIT-881.md) analyses: in the ordered phase two bits capture
  everything the block shares with the far environment.
- **[LIT-246](../literature.d/LIT-246.md), [LIT-256](../literature.d/LIT-256.md).** States the log K ceiling and the batch sizes
  [NOTE-681](NOTE-681.md) found missing, and shows the ceiling does not bind here.
- **Anthology.** A machine-learning method for physical data, built from
  estimators the anthology reads; its `physical-sciences` topic could
  hold it, hence `anthology-candidate`. No practice instruction.

## Limitations

- **Known answers throughout.** Ising, antiferromagnet and dimer
  variables were all known; the symmetry projections use bases chosen
  from them.
- **Two exponents, no error bars**, and neither compared with a
  prediction: υ ≈ 0.09 for the Ising critical point and υ ≈ 1.16 for
  free dimers.
- **One window, one model** for the PCA and symmetry analyses; the
  Ising ensemble is not analysed.
- **The non-equilibrium example is thin.** One 1D model whose steady
  state is reached quickly; the optimal filter is mass averaging at every
  w; the transition is marked by "a slight peak".
- **Bound tightness unmeasured.** The log K ceiling is cleared, but no
  comparison with an exactly known I_Λ is made.
- **Small inconsistencies.** The Fig. 2 caption says the RSMI of the
  antiferromagnet "at the critical point" converges to log 2, which sits
  oddly with the main text's exactly 1 bit only below T_c and a step at
  T_c (it may be a small-buffer value); Sec. III B 1 says the Ising
  block is 4 × 4, Table I gives L_V = 5 for the antiferromagnet; the
  ensemble space for "8 × 8 two-component filters" is called
  64-dimensional; one citation in Appendix B is printed "[30?]".

## Open questions

- Does the ensemble's geometry identify a symmetry nobody knew, without
  projecting onto bases taken from the theory? That would test the
  converse [THEORY-019](../theory.d/THEORY-019.md) denies in general.
- How tight is InfoNCE here below its ceiling? An exactly computable
  I_Λ on a small Ising system would show it.
- What do the optimal filters mean out of equilibrium, and does a
  temporal buffer, which the authors propose, change the answer on a
  model far from equilibrium?
- Does the saturation count of components equal the number of relevant
  operators in a model where that number is not known?
