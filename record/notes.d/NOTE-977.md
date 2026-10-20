---
number: 977
status: Read
formerly:
- NOTE-tmpinykd
paper: LIT-1241
title: 'Shpak, Stadler, Wagner and Altenberg — Simon–Ando decomposability and fitness landscapes'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:q-bio/0403030v1 (22 March 2004, the only arXiv
    version), 91 double-spaced pages. The text was extracted with pdftotext.
    Every displayed equation was read from page images rendered with
    pdftoppm, since the equation fonts do not extract. Read: the
    introduction, the Simon–Ando section with (3.0)–(3.13) and Theorems
    2.1, 2.2a and 2.2b, the mutation–selection set-up (4.0)–(5.5), the
    Hamming-graph section (6.0)–(6.6) with its numerical examples, the
    schema-partition section (6.7)–(6.12), the recombination section
    (7.1)–(7.3), the discussion, the figure captions, the references, and
    the appended manuscript "Generalization of Simon-Ando Decomposability"
    (8.0)–(8.13) with its concluding remarks. The PDF contains no figure
    plots, only their captions, so Figs. 1–4 were read from the captions and
    the text. The published version (Theory in Biosciences 123(2):139–180,
    September 2004) was not compared, and may differ.
date: '2026-10-20'
summary: >-
  States Simon and Ando's (1961) theorem for x(t+1) = (A* + εC)x, with A*
  block-diagonal, as existence statements: as ε → 0 the non-leading
  eigenvectors approach the blocks', and times T0 < T1 < T2 < T3 exist that
  separate within-block relaxation, quasi-equilibrium, aggregate
  cross-block dynamics and global equilibrium. No rate in ε and no bound on
  aggregation error is given. It then applies an entrywise proxy (minimal
  within-class rate ≫ maximal cross-class rate) to mutation–selection on
  hypercubes, which low mutation rates meet trivially, and to recombination,
  which rarely meets it. It concludes that Simon–Ando aggregation is one
  source of dynamical sufficiency among several, distinct from symmetry
  (equitable partitions) and from linkage-equilibrium character
  aggregation.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-331 CLAIM-327 THEORY-257 — Proposed; open claims and readings this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1127 — Unavailable; the theorem's original, cited as not yet read -->

# NOTE-977: Shpak, Stadler, Wagner and Altenberg — Simon–Ando decomposability and fitness landscapes

## Contribution

It is the record's nearest open statement of what Simon and Ando (1961)
proved, which it quotes "without proof" as Theorems 2.1 and 2.2. It then asks
which fitness landscapes and transmission operators induce Simon–Ando
fast–slow dynamics. Under point mutation many do, at a low enough mutation
rate. Under recombination few do, unless recombination itself is rare. Its
conceptual conclusion is the one its companion ([LIT-1242](../literature.d/LIT-1242.md)) only
gestured at: dynamical sufficiency of an aggregate can come from
quasi-equilibrium (Simon–Ando), from symmetry (equitable partitions) or from
product structure (linkage equilibrium), and these are independent.

## Key insight

Simon–Ando aggregation is temporary and conditional. A block's internal
distribution relaxes to its leading eigenvector. After that, and before the
weak cross-block terms have accumulated, the block can be replaced by one
number whose dynamics are given by the cross-block rates weighted by that
eigenvector. "For Simon-Ando systems where aggregation and decomposition are
only approximate and time-dependent, the two properties are actually
decoupled from one another." In t < T0 the system is decomposable and not
aggregable. In T0 < t < T1 it is both. After T2 it is aggregable and no
longer decomposable. Equitable partitions, in contrast, "are exactly
decomposable and aggregable over all time scales". Their classes need not
communicate internally at all. "Members of the equitable partition classes
did not communicate with one another at all under single-point mutation."

## Assumptions

- **The Simon–Ando setting (3.0).** x(t+1) = Ax(t) with A = A* + εC. A* is
  block-diagonal with blocks A*_I of size n_I, and C is "an arbitrary n
  dimensional square matrix", whose off-block entries carry the coupling.
  The paper uses the column convention: A_ij is the rate from j to i.
- **Spectral hypotheses (§ before 3.2).** The eigenvalues of each A*_I are
  distinct and ordered, λ*_1I > λ*_2I > … . The blocks are ordered by their
  leading eigenvalues, λ*_11 > λ*_1I > … > λ*_1M, strictly. (3.2a) defines
  δ* from the within-block spacing; as printed it reads min_{i≠j}
  |λ*_iI − λ*_jI| < δ*, which must mean δ* is that minimum. (3.2b): for any
  δ < δ* there is an ε small enough that |λ_iI − λ*_iI| < δ.
- **Stochastic case.** For column-stochastic A and A*, λ_11 = λ*_11 = λ*_1J
  = 1, so the block leading eigenvalues coincide. This breaks the strict
  ordering above (see Limitations).
- **Landscapes.** Haploid, non-overlapping generations, linearized to
  absolute frequencies (5.4) so that A = WM is linear (A_ij = μ_ij w_j, so
  strictly A = M·diag(w)). Two alleles at n loci on the hypercube, single
  point mutation at rate μ per locus. Partitions are radius-κ balls about
  reference genotypes, or schema classes.
- **Recombination.** The quadratic recombination–selection map (7.1) is
  linearized about an assumed quasi-equilibrium p*, (7.2). The local
  Jacobian A′ stands in for A.

## Key results

- **Theorem 2.1** (Simon and Ando's Thm 4.1, "repeat[ed] here without
  proof"). For any ξ > 0 there is ε_ξ such that for ε < ε_ξ,
  max_{k,l} |Z_kl(i_I) − Z*_kl(i_I)| < ξ for 2 ≤ i ≤ n(I). Here Z(i_I) is
  the outer product of the right and left eigenvectors of A for the i-th
  eigenvalue of block I, and Z* is A*'s. *Holds for:* the non-leading
  eigenvectors only. It is an existence statement, and ξ has no stated
  dependence on ε. The text before it also says λ*_iJ → λ_iJ and
  Z*_iJ → Z_iJ as ε → 0, citing Simon and Ando pp. 118–21.
- **Expansion (3.3)–(3.7).** A^t = Σ λ_iI^t Z_iI. Writing Z = Z* + ξU (3.6),
  the j-th component of block J splits into five terms (3.7b):
  x_jJ(t) = ξS⁽¹⁾ + S⁽²⁾ + ξS⁽³⁾ + S⁽⁴⁾ + ξS⁽⁵⁾. S⁽¹⁾ is the global leading
  mode, S⁽²⁾ block J's own leading mode, S⁽⁴⁾ block J's non-leading modes,
  and S⁽³⁾ and S⁽⁵⁾ the leading and non-leading modes of the other blocks.
- **Theorem 2.2a** (Simon and Ando's Thm 4.2, within-component
  quasi-equilibria). There is T0 such that for t > T0, S⁽⁴⁾/S⁽²⁾ < η0 (3.8).
  For T0 < t < T1, ξ(S⁽¹⁾ + S⁽³⁾ + S⁽⁵⁾)/(S⁽²⁾ + S⁽⁴⁾) < η1 (3.9).
- **Theorem 2.2b** (cross-component equilibrium). There is T2 > T1 such
  that for t > T2, (S⁽⁴⁾ + ξS⁽⁵⁾)/(ξS⁽¹⁾ + S⁽²⁾ + ξS⁽³⁾) < η2 (3.10). There
  is T3 > T2 such that for t > T3, (S⁽²⁾ + ξS⁽³⁾ + S⁽⁴⁾ + ξS⁽⁵⁾)/ξS⁽¹⁾ < η3
  (3.11). *Holds as:* existence of the times, with no expression for any of
  them. The text says the short-run regime lasts "for a time span which
  scales exponentially with the magnitude of δ", which is not derived. "True
  fast-slow behavior occurs when T2 is substantially (perhaps orders of
  magnitude) larger than T0."
- **The aggregate (3.12)–(3.13b).** In T1 < t < T2, x_iI ≈ ν*_iI X_I, with
  ν*_I block I's leading right eigenvector, normalized to sum 1, and X_I the
  block sum. The aggregate rate is P(X_{t+1} = I | X_t = J) ≈
  Σ_{i∈I} Σ_{j∈J} A_ij ν*_jJ (3.13b), the standard Simon–Ando–Courtois
  aggregate. In matrix form it is Â = QAV, with Q the block-indicator rows
  and V the columns ν*_I.
- **Two aggregates disagree.** Â of (3.13) equals neither the least-squares
  aggregate QAQᵀ(QQᵀ)⁻¹ of the companion's Theorem 1.1 nor the version with
  rows ν*_I, except when every block's leading eigenvector is uniform. In
  the paper's numerical work each beats the other in some regime. At μ = 0.1
  on the peak-and-plateau landscape, (1.1) "is completely misleading" and
  (3.13) is roughly right.
- **Landscape criterion (6.0)–(6.1b).** With Â_IJ = Σ_{i∈I}Σ_{j∈J} M_ij w_j
  ν*_jJ and column sums W_J, the near-decomposability requirement is taken
  as Â_JJ ≫ Σ_{I≠J} Â_IJ for each J (6.0). It is strengthened to
  (Â_JJ)_min ≫ (Σ_{I≠J} Â_IJ)_max (6.1b), with the minimum and maximum
  over possibly different classes. This is an entrywise (column-sum)
  proxy. The spectral conditions (3.2) are not checked against it.
- **Balls (6.2)–(6.4).** For a radius-1 ball, Â_JJ = W_J(1 − (n−1)μ) +
  (n−1)μ ν*_0 w_0, which is right. The general-κ form (6.2b) is wrong (see
  Limitations). With equal radii, (6.4b) is W1/(W2(n−κ)(W1+W2)) ≫ μ. For
  W1 ≈ W2 this asks μ ≪ 1/n. With W1 = 1 and W2 = 1 + S, the fitness
  difference must satisfy S ≪ (1 − 2μ(n−κ))/(μ(n−κ)). So a partition class
  cannot be much fitter than the others, and a two-peak landscape with
  low-fitness valleys can be partitioned in essentially one way.
- **Flat landscape.** At low μ, "a 'flat' fitness landscape … will be
  Simon-And[o] decomposable for an arbitrary partitioning". In Fig. 1 (n = 5,
  μ = 0.01, two radius-2 balls) the error is about 0.08 and "doesn't improve
  with lower mutation rates".
- **Schemata (6.5)–(6.6).** For a κ-locus schema, Â_JJ = W_J(1 − κμ) and
  Σ_{I≠J} Â_IJ = W_Jκμ, independent of n. (6.6) gives S ≪ 1/(1 − κμ), so
  for κμ ~ 1/n no more than a twofold difference in marginal fitness.
- **Two-peak numerics (Figs. 2–4).** With n = 5, multiplicative fitness about
  each peak (s = 0.1) and μ = 0.01, the error is of order 10⁻², and 10⁻⁵ at
  μ = 0.001. Peak against plateau (Fig. 4): at μ = 0.1 and 0.01 the
  stationary mass sits on the plateau, the "mutationally robust" genotype,
  and the Simon–Ando estimate is poor (error near 0.2, then just under
  0.1). At μ = 0.001 the mass sits on the peak, and the estimate is good
  (about 10⁻³).
- **Character aggregation (6.7)–(6.12).** Under multiplicative fitness
  W = W1 ⊗ W2 and mutation M = M1 ⊗ M2, a product state x = x¹ ⊗ x² stays a
  product, with x¹(t+1) = W1M1x¹(t) up to normalization. Schema frequencies
  are then dynamically sufficient on all timescales, on the
  linkage-equilibrium manifold. This "is in contrast to the conditions
  under which a schema-based partitioning is decomposable according to the
  Simon-Ando criterion", which generates strong linkage disequilibrium.
- **Recombination (7.1)–(7.3).** Under free recombination,
  Σ_{I≠2} Â_I2 "will be of the same order as" Â_11, so the criterion
  fails. With recombination probability ρ and selfing otherwise, it holds
  for small ρ, "the trivial limiting case". Single-point recombination
  needs positional information, and no closed form is found. Hamming-ball
  partitions under recombination need hypergeometric sums.
- **Valley generalization (appended manuscript, (8.0)–(8.13)).** High-fitness
  blocks are separated by a valley block E whose entries are all of order ε.
  Paths through E are not negligible, so (3.13) fails for transitions to and
  from E. Cross-partition rates are estimated instead as reciprocals of
  expected first-passage times (8.5)–(8.13), "in many cases more costly than
  computing the dynamics of the entire system".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In a nearly decomposable linear system, times T0 < T1 < T2 < T3 exist separating within-block relaxation, block quasi-equilibrium, aggregate cross-block dynamics and global equilibrium | moderate as a report of Simon and Ando; nothing new | Theorems 2.1–2.2 quoted without proof; no rates |
| C2 | In T1 < t < T2 the block sums evolve approximately by Â_IJ = Σ_{i∈I}Σ_{j∈J} A_ij ν*_jJ | moderate | (3.12)–(3.13b), argued from C1; no error bound |
| C3 | Many point-mutation landscapes meet the Simon–Ando condition at low mutation rate, with partition classes of nearly equal mean fitness | weak: what is met is an entrywise proxy, met trivially as μ → 0 even on a flat landscape, where no time-scale separation exists | (6.1b)–(6.6) with Figs. 1–4; see Limitations |
| C4 | Under free recombination the condition fails; it holds only when recombination is rare | moderate for the linearized proxy | (7.3) under uniform crossover; the linearization assumes a quasi-equilibrium it is meant to test |
| C5 | Simon–Ando aggregation, exact aggregation by equitable partitions and character aggregation under linkage equilibrium are independent routes to dynamical sufficiency | moderate | each route shown separately; Hamming classes close with no internal coupling, and product states close on all timescales |
| C6 | Dynamical sufficiency of schema (allele) frequencies supports units of evolution above the genotype, not below it | weak | conceptual argument in §6 and the concluding remarks |
| C7 | Simon–Ando decomposability is a special case of weighted equitable partitioning | weak, and contradicted by the paper's own conclusion | asserted in the schema section; the concluding remarks call this "previous intuition" and say the routes are separate |

## Concepts

- **Simon–Ando system**: A = A* + εC, with A* block-diagonal and ε ≪ 1,
  whose blocks reach internal quasi-equilibria long before the whole reaches
  equilibrium.
- **Quasi-equilibrium of a block**: its subvector proportional to its leading
  eigenvector ν*_I. Reached after T0, kept until T1.
- **Courtois inequality**: the paper's name for (6.1b), the minimal
  within-class rate much larger than the maximal cross-class rate.
- **κ-ball partition**: classes {x : d(x, x0) ≤ κ} about reference genotypes.
- **Schema (character) class**: genotypes sharing alleles at a fixed subset
  of loci.
- **Valley block E**: in the appended manuscript, a residual block of
  uniformly weak entries that is not a Simon–Ando component.

## Connections

It quotes Simon and Ando (1961) and Ando and Fisher (1963). It cites
Courtois (1977/1978) for the aggregate (3.13), and Courtois and Semal (1984)
for bounds on positive eigenvectors under decomposition, which it does not
use. It cites Meyer (1989) on stochastic complementation and Deuflhard et al.
for almost-invariant aggregates. It is the companion of [LIT-1242](../literature.d/LIT-1242.md)
(cited as "Shpak et al 2003 … in review"), and the two appeared in the same
volume of Theory in Biosciences. The character-aggregation section restates
Wagner and Laubichler (2000) and an unpublished derivation by Carter.

**Is it the companion's "Shpak et al., in preparation"?** Very probably. The
companion ([NOTE-979](NOTE-979.md)) writes that fast–slow decomposition "may prove
to be more generally applicable to evolutionary systems (Shpak et al, in
preparation) than the exact aggregation of equitable partitions". This paper
is by the companion's first three authors, takes exactly that question,
cites the companion as in review, and was published in the next issue of the
same volume (123(2) against 123(1)). Neither text names the other as that
reference, so the identification is an inference. One complication: the
appended "Generalization" manuscript carries a different author list (Shpak,
Hermisson, Stadler), the companion's own grouping.

## Bearing on the record

- **[THEORY-661](../theory.d/THEORY-661.md) and [LIT-1127](../literature.d/LIT-1127.md).** This is the statement of the theorem
  the record can now cite in place of the unread original. It supports
  [THEORY-661](../theory.d/THEORY-661.md)'s two propositions in their qualitative form. Short run:
  within-block terms dominate for t < T1. Long run: the block enters only
  through its aggregate for T1 < t < T2. But it does not support the
  sentence "The theorem says it leaves one, to order ε" in [THEORY-661](../theory.d/THEORY-661.md)'s
  "What could have come out otherwise". As quoted here, the theorem gives
  existence for ε below some threshold, with no order in ε. Recommend
  rewording that sentence to "for ε small enough; the version quoted in
  [LIT-1241](../literature.d/LIT-1241.md) states no rate", and adding [LIT-1241](../literature.d/LIT-1241.md) to its Source
  section as the open statement of the theorem.
- **[QUESTION-221](../questions.d/QUESTION-221.md).** The paper gives no bound relating off-block
  coupling to how well the block aggregates are described autonomously.
  Theorem 2.1's ξ has no stated dependence on ε, the T's have no
  expressions, and (3.13) carries no error term. A bound can be had from
  its construction, though. Derived here, not by the paper: with Q the
  block-sum map and V the block leading eigenvectors (QV = I), the one-step
  closure defect of the aggregate (3.13) is exactly
  D = QA − ÂQ = QA(I − VQ).
  It vanishes on the quasi-equilibrium manifold (range V). Splitting
  A = A* + εC gives D = QA*(I − VQ) + εQC(I − VQ). Block I's part of the
  first term is 1ᵀA*_I − λ*_1I 1ᵀ, which is zero iff block I has equal
  column sums: a column-stochastic block, or a cell of a column-equitable
  partition ([THEORY-755](../theory.d/THEORY-755.md)). The identity was checked to machine
  precision. A numerical run in a two-block, ten-state system showed what
  happens after the fast transient. With column-stochastic blocks the
  relative defect ‖Dx‖/‖Qx‖ scaled as ε²: 1.2 × 10⁻⁵, 1.2 × 10⁻⁷ and
  1.2 × 10⁻⁹ at ε = 10⁻², 10⁻³ and 10⁻⁴. With blocks of unequal column
  sums (mutation–selection-like) it scaled as ε: 3.0 × 10⁻⁴, 3.3 × 10⁻⁵
  and 3.3 × 10⁻⁶. Before the transient decays, the defect is O(1) times
  the off-manifold part in the second case and O(ε) times it in the first.
  The reason is that the slow invariant subspace lies O(ε/gap) from range
  V, which is the standard perturbation estimate, assumed here and not
  proved. This is a deterministic closure defect, A5's min_B ‖LA − BL‖
  restricted to B = QAV. It is not yet the Gaussian dynamical dependence
  the question asks for, but it is the noise-free part of that answer.
  Recommend filing the identity, with the scaling, as a CLAIM (warrant:
  demonstrated for the identity, empirical for the orders) that partly
  answers the question.
- **[CLAIM-388](../claims.d/CLAIM-388.md) and [QUESTION-218](../questions.d/QUESTION-218.md).** C5 is a second published
  statement that closure does not need a block. Its sharpest example is the
  Hamming-distance classes, which close exactly while "members … did not
  communicate with one another at all". It also adds a third
  non-block unit for [QUESTION-218](../questions.d/QUESTION-218.md): a marginal (schema frequency), closed
  on the linkage-equilibrium manifold under product fitness and mutation,
  with cross-class rates of the same order as within-class ones (κμ against
  1 − κμ). The abstract's closing remark, that the formalism does not
  extend "to other forms of decomposition and aggregation", is this
  point and not a general negative result.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** C3's limitation bears on what "nearly decomposable"
  should mean there. The entrywise test (small off-block entries) can hold
  while there is no time-scale separation at all. The spectral form, a
  within-block gap that is large against the coupling, is what makes the
  gap-isolated block a unit. [CLAIM-157](../claims.d/CLAIM-157.md)'s wording ("a block whose gap
  beats the Occam factor") is already spectral. A note there could cite this
  paper's flat-landscape case as the reason the entrywise reading is not
  enough.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** The four-stage account (C1) supplies the "aggregate is
  slower" half in the Simon–Ando setting. The flat-landscape case is a
  warning: weak coupling alone does not make the aggregate slower than its
  parts' internal relaxation.
- **[THEORY-733](../theory.d/THEORY-733.md), [THEORY-257](../theory.d/THEORY-257.md).** In Barnett and Seth's terms, the Simon–Ando
  aggregate is approximately dynamically independent only on the window
  T1 < t < T2 and only after the fast transient. The defect identity above
  makes the window's accuracy explicit for the deterministic part.
- **[CLAIM-327](../claims.d/CLAIM-327.md), [QUESTION-217](../questions.d/QUESTION-217.md), [QUESTION-220](../questions.d/QUESTION-220.md), [QUESTION-222](../questions.d/QUESTION-222.md), [QUESTION-219](../questions.d/QUESTION-219.md).**
  Little bearing. The valley manuscript's first-passage-time rates
  (8.5)–(8.13) are one way to aggregate through a non-quasi-absorbing
  region. They are a crude relative of the memory problem in
  [QUESTION-222](../questions.d/QUESTION-222.md), since a valley that is not at quasi-equilibrium makes
  the block-to-block process non-Markovian at the aggregate level. The
  paper does not frame it that way.

No THEORY is filed from this reading. Its theorem statements are quoted
from Simon and Ando without proof and add nothing to [THEORY-661](../theory.d/THEORY-661.md) beyond
a more exact statement of its conditions. Its own landscape results rest on
the entrywise proxy criticised below. The one exact result worth keeping,
the closure-defect identity, is the record's derivation, not the paper's,
so it is recommended above as a CLAIM.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The theorem is quoted, not proved, and has no rates.** Theorem 2.1 is
  existential in ξ and ε. Theorem 2.2 gives existence of T0–T3 without
  expressions. The remark that the short run lasts a time "which scales
  exponentially with the magnitude of δ" is unsupported. In the standard
  analysis the cross-block terms become comparable over a time of
  roughly order 1/ε, not one set by δ.
- **The leading-eigenvector statement is wrong where the paper uses it.**
  The text says Z*_iJ → Z_iJ as ε → 0 for every i, and writes the global
  leading mode's components in other blocks as O(ξ) in (3.7a). That holds
  only when the block leading eigenvalues are distinct and stay apart as
  ε → 0. In the stochastic case, which the paper invokes (λ*_1I = 1 for
  all I), and in its symmetric two-peak landscape, they coincide. The
  global leading eigenvector is then an O(1) mixture of the block
  eigenvectors, fixed by the aggregate. Checked: with two identical
  column-stochastic blocks and coupling ε = 10⁻², 10⁻⁴ and 10⁻⁶, the
  global stationary vector has mass 0.5000 in the second block every time.
  Theorem 2.1 itself is correctly restricted to i ≥ 2.
- **The landscape criterion is not Simon–Ando's.** (6.0)–(6.1b) compare
  column sums of the aggregate: entry sizes. Simon and Ando's condition,
  as (3.2) states it, compares the coupling with the within-block
  eigenvalue gap δ*. Under point mutation both the within-block mixing and
  the cross-block leakage are O(μ), so the entrywise ratio grows as 1/μ
  while the time-scale ratio does not move. Checked on the paper's Fig. 1
  case (flat, n = 5, two radius-2 balls). The within/cross ratio is 71,
  716 and 7170 at μ = 10⁻², 10⁻³ and 10⁻⁴. But the global slow rate,
  1 − λ₂ = 2μ, and the block's internal gap, 1.87μ, stay in ratio 0.94 at
  every μ. The block relaxes no faster than the whole, and there is no
  fast–slow structure. That is why Fig. 1's error "doesn't improve with
  lower mutation rates" (reproduced here: relative squared error 0.12 at
  both μ = 0.01 and 0.001). The authors read this as (6.4b) being
  "sufficient but not necessary". It shows the reverse: (6.4b) holds and
  the approximation fails, so it is not sufficient. C3's "quite a wide
  range of landscapes satisfy the condition (at least trivially)" should
  be read with "trivially" doing most of the work.
- **(6.2b) is wrong for κ ≥ 2.** Only the vertices at distance exactly κ
  leak, each at rate (n − κ)μ. So Σ_{I≠J} Â_IJ = (n − κ)μ Σ_{d(x0,xj)=κ}
  ν*_j w_j, and Â_JJ = W_J − (n − κ)μ Σ_{d=κ} ν*_j w_j. The paper's
  expressions subtract the d = κ sum where the d < κ sum belongs. They
  agree with the correct ones only at κ = 1. Checked with n = 6, κ = 2 and
  random fitnesses: the true cross rate is 0.0537, the paper's formula
  gives 0.0024, and the corrected one gives 0.0537. The qualitative
  conclusions drawn from (6.3)–(6.4) do not depend on the error, since
  they drop the residual sums.
- **A sign slip.** From (6.4a) with W1 = 1 and W2 = 1 + S, the bound is
  S ≪ (1 − μ(2n − κ1 − κ2))/(μ(n − κ2)). The paper prints the numerator as
  1 − 2nμ − μ(κ1 + κ2). Its equal-radius case, (1 − 2μ(n − κ))/(μ(n − κ)),
  is right.
- **The numbers in Figs. 2–4 cannot be reproduced exactly.** The text's
  Fig. 2 landscape (multiplicative, s = 0.1, λ1 = λ2 = 0.990181) differs
  from the caption's (neighbours 0.9, distance-2 genotypes 0.01,
  λ = 0.999). The "mean-square error" is not normalized in any stated way.
  With the text's landscape and A = M·diag(w), the error falls steeply
  with μ (relative squared error 1.4 × 10⁻⁴ at μ = 0.01 and 1.6 × 10⁻¹⁰ at
  0.001), which agrees with the trend reported, not with the values.
- **The recombination analysis tests a linearization about the state whose
  existence is in question.** The authors say so: it can show a system is
  not Simon–Ando, and suggests at most the first stage when it is.
- **C7 against C5.** In the schema section the paper repeats the
  companion's claim that Simon–Ando decomposition is a special case of
  weighted equitable partitioning ([NOTE-979](NOTE-979.md) C7). Its concluding
  remarks retract this as "previous intuition about the 'universality' of
  Simon-Ando or generalized equitable partitions". The retraction is the
  better-supported position, since the Simon–Ando aggregate is
  approximate and time-limited and an equitable partition is exact.
- **Small errors.** The text cites "closure theorem 6.2", which does not
  exist, and "Ando and Franklin (1963)" for Ando and Fisher. Equation
  cross-references (2.3), (2.4a) and (2.9) point to the (3.x) and (5.x)
  equations. The Kronecker product is defined as "(A⊗B)_ij = AB". The
  mutation matrix is called row-stochastic though its columns sum to one.
  (8.6) sums per-target passage times and calls the result "the exact
  value of expected passage times between partitions", which a passage
  time to a set is not.
- **arXiv copy only.** The journal version was not compared.

## Open questions

- What is the rate in Theorem 2.1, in terms of ε, the within-block gap δ*
  and the separation of the block leading eigenvalues? Courtois and Semal
  (1984), cited here and unused, is the likeliest open source for an
  explicit bound. Simon and Ando's own text is [LIT-1127](../literature.d/LIT-1127.md), Unavailable.
- Does the ε against ε² split in the closure defect (equal against unequal
  column sums within blocks) survive in the Gaussian VAR(1) setting of
  [QUESTION-221](../questions.d/QUESTION-221.md), as a bound on the transfer entropy into the block
  sums? A proof of the after-transient orders from the invariant-subspace
  perturbation bound would settle the deterministic part.
- Which landscapes meet the spectral condition, not the entrywise one? A
  landscape whose within-peak mixing is O(1) while cross-valley leakage is
  O(μ) needs fitness differences comparable to 1 within a class, which
  (6.4) forbids between classes. The paper leaves open whether any
  biologically natural landscape has both.
