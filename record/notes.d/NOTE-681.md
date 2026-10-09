---
number: 681
status: Read
formerly:
- NOTE-tmp0zdr4
paper: 'LIT-878'
title: 'Statistical Physics through the Lens of Real-Space Mutual Information'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v3 (arXiv:2101.11633v3, 19
    October 2021, "Version accepted for publication in Physical Review
    Letters"; 16 pp.: main text pp. 1–5, Supplemental Material
    Appendices A–C pp. 6–13, references), text extracted with pdftotext.
    Main text, all three appendices, the tables and the reference list
    read. The InfoNCE derivation (Eqs. A4–A7) and the height-field
    reduction of the staggered filters (Eqs. C3–C9) followed step by
    step, not re-derived. Figures read as text only: the filter maps and
    plots did not survive extraction, so their content is taken from
    captions and text. The v1 PDF (31 pp.) was opened for its title page
    only; its longer text was not read. The publisher's typeset version
    was not read; small differences from v3 cannot be ruled out. The
    companion paper (arXiv:2103.16887) and the cited optimality theorem
    (Gordon et al., Phys. Rev. Lett. 126, 240601) were not read.
date: '2026-10-09'
summary: >-
  Makes the real-space mutual-information principle a single-shot
  operator finder: a CNN coarse-graining co-trained against a neural
  InfoNCE bound, optimized once at a large buffer, returns on the
  interacting dimer model the order parameters below the BKT transition
  and the electric fields above it, and one fitted scaling dimension
  (1.00037 against 1). The maximal information is log 4 in the ordered
  phase and decays algebraically with the buffer in the critical one.
  The model's operators were known; the optimality theorem is cited.
---
<!-- inactive-ok-file: THEORY-194 THEORY-017 THEORY-036 QUESTION-025 THEORY-185 LIT-246 LIT-256 LIT-247 — Proposed, Deferred or open; cited as accounts this reading is set beside and the estimator papers it rests on -->

# NOTE-681: Statistical Physics through the Lens of Real-Space Mutual Information

## Contribution

[LIT-873](../literature.d/LIT-873.md) proposed choosing a block's coarse variable to maximize its mutual
information with the distant environment, but its RBM-based estimate of
that quantity was slow and rough, and its use was to iterate a
coarse-graining. This paper does two things. It replaces the estimator by
a differentiable neural lower bound (InfoNCE) trained jointly with a
convolutional coarse-graining, which makes the optimization fast and
stable on large systems. And it changes what the optimum is used for:
instead of iterating an RG map, the filters optimized once at a large
buffer are read directly as lattice forms of the most relevant operators,
across a phase diagram. It demonstrates this on the interacting dimer
model, where the relevant variables change qualitatively across a BKT
transition.

## Key insight

Information that crosses a wide buffer can only be carried by the
operators whose correlations decay slowest, so the best compression of a
block with respect to the far environment is a compression onto those
operators. Widening the buffer then does what iterating the RG does,
without accumulating the errors of a repeated rule: it filters out every
contribution but the leading ones, and the optimal filters are the
leading operators written in the microscopic variables.

## Assumptions

- **A probability distribution over a spatially extended system**,
  sampled; Monte Carlo samples here. A Hamiltonian is not needed; the
  paper says the method needs only a distribution and so extends to
  non-equilibrium steady states, but the formal link to operators is
  stated only for the equilibrium case.
- **A spatial partition supplied in advance.** Block V (here L_V = 8),
  buffer B (L_B ∈ {2, 4, 6, 8}) and environment E. The main text defines E
  as the remainder of the system; Table III gives it a thickness L_E = 4,
  so in the computation E is a shell.
- **Translation invariance**, so one filter Λ serves all blocks;
  disorder is said to need block-wise filters.
- **The form of H is fixed beforehand**: here a two-component binary
  vector {±1, ±1}, imposed by a Gumbel-softmax layer annealed from 0.75
  to 0.1. The paper says the right dimension "can be found
  systematically", in the companion paper.
- **The coarse-graining is linear before discretization**: h = τ ∘ (Λ ·
  v), a single convolutional layer; the authors say any expressive ansatz
  would do.
- **InfoNCE is a lower bound.** Optimizing it optimizes I_Λ only as far
  as the bound is tight. The paper argues it is usable because RSMI is
  small (Eq. A2: I_Λ(H : E) ≤ I(V : E) ≤ H(V) ≤ N_V log n), and two bits
  of H cap I_Λ at log 4 in any case. Batch size and the bound's log K
  ceiling are not discussed.
- **The optimality theorem**: that in critical systems the formal
  solutions of the RSMI problem are determined by the most relevant
  operators is cited to Gordon et al. (2021) and was "proven in part".

## Key results

- **Speed and scale** (Appendix A). About 30 s per run, three to four
  orders of magnitude faster than [LIT-873](../literature.d/LIT-873.md)'s estimator, tested up to
  256 × 256. No benchmark table is given.
- **Information marks the phases** (Fig. 2b). With optimal filters,
  I_Λ(T) is constant and equal to log 4 for T < T_BKT: the information
  shared across the buffer is which of the four columnar states the
  system is in. Above T_BKT it decays algebraically with L_B, the mark of
  a critical phase (the companion paper contrasts the exponential decay
  in the 2D Ising paramagnet). Transitions appear as non-analyticities in
  I_Λ(T).
- **Low T: order parameters** (Figs. 2d–f, Table I, Eqs. 4–5, Appendix
  C2). Independent runs return columnar (C) and plaquette (P1, P2)
  filters. Any pair bijectively labels the four columnar ground states,
  so they are degenerate in the ordered phase. The columnar filter alone
  is the dimer symmetry-breaking (DSB) order parameter of Alet et al.; in
  height-field terms (Λ_P1, Λ_P2) ∘ φ = (cos(φ + 3π/4), sin(φ + 3π/4)) and
  Λ_C ∘ φ = cos 2φ, the electric charge operators O_n for n = 1 and 2.
- **Above T_BKT: the degeneracy lifts** (Appendix C3, Table IV). The
  scaling dimensions of O_n grow as n² (at T_BKT, d₁ = 1/8 and d₂ = 1/2;
  at T → ∞, d₁ = 1 and d₂ = 4, quoted from Papanikolaou, Luijten and
  Fradkin), so O₂, the columnar filter, decays faster and is no longer
  found; plaquette filters persist. A plaquette order parameter keeps a
  non-zero value in finite systems above T_BKT, which the authors say
  vanishes in the thermodynamic limit and relate to plaquette phases of
  the quantum dimer model.
- **High T: electric fields** (Appendix C3, Eqs. C3–C9). The optimal
  filters are staggered; with the expansion of dimer densities in the
  height field, their block sums reduce to τ ∘ ∇⟨φ⟩ over the block, the
  coarse-grained electric field. Any rotation of the pair recovers the
  same information, read as the emergent U(1) symmetry of free dimers.
  The plaquette filter retains more information than the staggered one
  until well above T_BKT (Fig. 2c), a finite-size effect the authors
  attribute to plaquette correlations.
- **A filter's scaling dimension** (Fig. 4, Appendix B). The correlator
  of two plaquette-filter networks on 128 × 128 samples at T → ∞, with
  4 × 4 filters, fits r^(−2.00074), so d₁ = 1.00037 against the predicted
  1; the columnar correlator is "consistent with" r⁻⁸ but not fitted.
  Appendix B gives the same number "already at system size of 64 × 64";
  Appendix C3 and the Fig. 4 caption say 128 × 128.
- **Buffer and block** (Appendix B). L_B separates long from short range
  and needs only to be large enough that the second-most relevant
  operator's correlations fall below sampling noise; larger L_B adds
  nothing and eventually drowns the signal. L_V is the support of the
  operator and controls block averaging.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A CNN coarse-graining co-trained with a neural InfoNCE bound optimizes RSMI fast and stably on large systems | moderate | timings and system sizes stated in Appendix A; no comparison table |
| C2 | On the interacting dimer model the RSMI-optimal filters are the order parameters (columnar/DSB, plaquette) below T_BKT and the electric fields at high T | moderate | numerical, one model whose operators were known; Fig. 2, Table I, Eqs. 4–5, C3–C9 |
| C3 | The maximal RSMI as a function of T, and its decay with the buffer, reveal the phase structure (log 4 plateau in the ordered phase, algebraic decay in the critical phase) | moderate | Fig. 2b; non-analyticity at transitions asserted with references to earlier mutual-information studies |
| C4 | RSMI-optimal filters are lattice representations of the most relevant scaling operators and can be used as operators, e.g. to fit scaling dimensions | moderate for this model; the general statement is cited, not shown | one fitted dimension (1.00037 vs 1); disappearance of the n = 2 filter above T_BKT; theorem cited to Gordon et al. 2021 |
| C5 | The rotation invariance of the information under mixing of the staggered filters reveals the emergent U(1) symmetry | weak | stated in Appendix C3; details deferred to the companion paper |
| C6 | The method works in any dimension, under disorder and out of equilibrium, without a Hamiltonian | weak | asserted; only a 2D equilibrium example here; the non-equilibrium case is in the companion paper, and its formal understanding is said to be missing |
| C7 | The approach makes machine learning in physics formally interpretable and paves the way to automated theory building | weak | framing; rests on C2–C4 |

## Method

RSMI-NE, per point of the phase diagram: from Monte Carlo samples, cut
each configuration into V, a discarded buffer B and E. Map V to H by the
convolutional filters Λ and the Gumbel-softmax layer τ. In each
mini-batch of K samples, form the K × K score matrix F_ij = v(h_i)ᵀu(e_j),
whose diagonal holds joint pairs and whose off-diagonal holds independent
ones, and take the InfoNCE estimate (Eq. A10, plus log K). Ascend it in Λ
and Θ together with Adam, same learning rate, over epochs to convergence;
the RSMI estimate is a moving average of the mini-batch values. Repeat
over independent runs to get an ensemble of filters, and read the
ensemble: pristine components, their overlaps with the filters at each T
(Fig. 2e), and the order parameters and correlators the filters define.

## Concepts

- **RSMI**: I_Λ(H : E), the mutual information between a block's coarse
  variables and its environment beyond a buffer (Eq. 1).
- **RSMI-NE**: the neural-estimation algorithm and its code.
- **pristine filters**: the columnar, plaquette and staggered filters
  found in the low- and high-temperature limits; mutually orthogonal, and
  the components into which filters at intermediate T are decomposed.
- **relevant operator**: here, the scaling operators of lowest scaling
  dimension, those that dominate correlations at large distance; the
  paper identifies them with what dominates RSMI at large buffer.
- **electric charge operators**: O_n(φ) = (cos nφ, sin nφ) on the height
  field, with dimensions proportional to n² in the critical phase.

## Connections

It is the third step of a programme: the RSMI principle and RBM
algorithm (Koch-Janusz and Ringel, [LIT-873](../literature.d/LIT-873.md)), its formal optimality and
relation to the information bottleneck (Lenggenhager et al., Phys. Rev.
X 2020, not held), and the theorem tying the optimum to the most relevant
operators (Gordon et al., Phys. Rev. Lett. 2021, not held). The estimator
comes from the machine-learning literature on variational bounds of
mutual information: Barber–Agakov, Nguyen–Wainwright–Jordan, MINE
([LIT-256](../literature.d/LIT-256.md)), Poole et al.'s unifying account ([LIT-246](../literature.d/LIT-246.md)) and van den Oord et
al.'s InfoNCE ([ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md)). The physics is Alet et al.'s interacting
dimer model and Papanikolaou, Luijten and Fradkin's sine-Gordon
treatment of it. The companion paper (arXiv:2103.16887) carries the
Ising, symmetry and non-equilibrium examples.

## Bearing on the record

- **[THEORY-194](../theory.d/THEORY-194.md).** That account, sourced on [LIT-873](../literature.d/LIT-873.md), says that for 1D and
  2D Ising and 2D dimers the coarse-graining that maximizes information
  with the far environment is the RG-relevant one. This reading extends
  the evidence to the interacting dimer model across a BKT transition,
  with an independent estimator and one fitted scaling dimension. It does
  not meet [THEORY-194](../theory.d/THEORY-194.md)'s `promote_when`: every operator found was known
  from the field theory, and the paper uses that theory as its dictionary.
  It is a candidate second source for [THEORY-194](../theory.d/THEORY-194.md), or for a widened title
  covering this model; I have not edited [THEORY-194](../theory.d/THEORY-194.md).
- **[THEORY-017](../theory.d/THEORY-017.md).** Two observations bear on it. The spatial partition into
  block, buffer and environment is again supplied before anything is
  learned. And the objective fixes less than a basis: in the ordered phase
  any pair of columnar and plaquette filters carries the same two bits, and
  at high T any rotation of the staggered pair carries the same
  information. What the information determines is a subspace of filters;
  the basis within it is left to symmetry or to chance across runs, which
  is why the paper reads an ensemble. This is my connection, not the
  paper's.
- **[QUESTION-025](../questions.d/QUESTION-025.md) and [THEORY-185](../theory.d/THEORY-185.md).** No direct bearing: no attributes, no
  co-occurrence matrix, no concept lattice. The loose parallel of [NOTE-674](NOTE-674.md)
  holds here too, with one addition: in this model the information
  objective identifies the relevant directions only up to rotation where
  the symmetry is continuous, so "a linear direction per variable" is a
  choice of basis on top of what the statistics fix. Nothing here tests
  whether such directions survive when the variables imply one another.
- **[THEORY-036](../theory.d/THEORY-036.md) and [LIT-219](../literature.d/LIT-219.md).** As for [LIT-873](../literature.d/LIT-873.md): an operational criterion
  for a scale-relative description, here with the scale set by the buffer
  width rather than by iteration. My connection.
- **[LIT-246](../literature.d/LIT-246.md), [LIT-256](../literature.d/LIT-256.md), [LIT-247](../literature.d/LIT-247.md).** The record's estimator papers are held
  deferred, with skims. This paper is a use of InfoNCE where the quantity
  bounded is small and capped (two bits of H), which is the regime where
  Poole et al. say the log K ceiling does not bite; the paper does not
  state K.
- **Anthology.** A machine-learning method for physical data, built from
  estimators the anthology reads; its `physical-sciences` topic could hold
  it, hence `anthology-candidate`. It carries no practice instruction this
  record could hold.

## Limitations

- **One model, known answers.** The interacting dimer model's operators
  and their dimensions were known; the paper uses the field theory to
  identify what was found. No system with unknown relevant operators is
  attempted here.
- **The central theorem is elsewhere.** That RSMI optima are the most
  relevant operators is cited to Gordon et al. and described as "proven
  in part", for critical systems; the off-critical claims rest on this
  model alone.
- **One fitted exponent**, at T → ∞, with no error bar; the columnar
  correlator is not fitted.
- **The bound's tightness is not assessed.** No comparison of the InfoNCE
  estimate with a known value of I_Λ, and no mini-batch size stated.
- **Small text inconsistencies.** The main text cites a plaquette order
  parameter in "Fig. 2.g", but Fig. 2 has panels a–f; the system size for
  the fitted dimension is 64 × 64 in Appendix B and 128 × 128 in Appendix
  C3 and the Fig. 4 caption; Appendix B says buffers "of a dozen sites" suffice while the
  runs use L_B ≤ 8; the main text defines E as the rest of the system
  while Table III gives it a thickness of 4. The arXiv listing's abstract
  is v1's longer one, not the v3 PDF's.

## Open questions

- Does RSMI-NE find relevant operators, and correct dimensions, in a
  system where they are not known? A model whose critical theory is open,
  checked against high-precision Monte Carlo or the conformal bootstrap,
  would show it.
- How tight is the InfoNCE bound in these runs, and how does the answer
  depend on batch size? A comparison with an exactly computable I_Λ on a
  small system would settle it.
- Off criticality, what is the formal status of the optimal filters? The
  cited theorem is for critical systems; the order-parameter results are
  numerical.
- Can the representation-dependence of the input (the spatial partition,
  the fixed alphabet of H) be removed, or is it what makes the operators
  identifiable?
