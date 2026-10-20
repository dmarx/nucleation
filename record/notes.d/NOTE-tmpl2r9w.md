---
status: Read
paper: LIT-tmp6vpg9
title: 'Shpak, Stadler, Wagner and Hermisson — Aggregation of variables and system decomposition'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the copy in Leipzig University's repository (Qucosa,
    qucosa:31929, attachment ATT-0), text extracted with pdftotext. The copy
    is the authors' manuscript, a Mathematica notebook export headed "Copy
    of DecompPaper.nb", not the typeset Theory in Biosciences article, and
    it was not compared with the published version or with its 2005
    erratum. Read: the introduction, §1 on linear aggregation (1.0)–(1.11),
    Theorem 1.1, Results 1.1–1.2 and Lemma 1.0, §2 on equitable partitions
    with Theorem 2.1, the single-peak, two-peak and multipeak landscapes
    with their two Results and proofs, the discussion, the appendix on
    multiple alleles and the figure captions. Many displayed equations
    were garbled by extraction. Where the prose states the result they are
    reconstructed from it, and the key ones are re-derived in
    THEORY-tmpj32n2. The figures were read from captions and text.
date: '2026-10-20'
summary: >-
  Separates aggregation of variables, a lower-dimensional map y = Qx whose
  dynamics close, from decomposition into non-interacting subsets: either
  can hold without the other. For a linear system the aggregate operator
  must satisfy ĀQ = QA. For a partition, the block sums close for every
  state exactly when the partition is column-equitable. Equitable partitions
  of mutation–selection matrices reduce single- and two-peak fitness
  landscapes exactly, and fail for three or more peaks unless the classes
  are refined to overlap classes. Simon–Ando aggregation is treated as the
  approximate limiting case, without error bounds.
---
<!-- inactive-ok-file: CLAIM-157 THEORY-607 — Proposed; open claims and readings this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1127 LIT-tmp6rgoj — Unavailable or Deferred; works not yet read, cited as open -->
# NOTE-tmpl2r9w: Shpak, Stadler, Wagner and Hermisson — Aggregation of variables and system decomposition

## Contribution

It puts the existing linear results on aggregability on one footing and
names the distinction the record's individuation line lacked. A system is
**decomposable** when its variables split into non-interacting (or weakly
interacting) subsets. It is **aggregable** when some y = f(x) with fewer
variables evolves autonomously. "Aggregativity need not imply
decomposability, nor vice-versa." For linear systems and partitions, it
identifies the exact condition for aggregation, column-equitability, and
applies it to mutation–selection on fitness landscapes.

## Key insight

The question "can these variables be summarized?" is not "do these
variables form a module?". A macrostate can be a function of every
microstate, as temperature is of every molecule, and still be dynamically
sufficient. For a partition of the variables, the summaries of the blocks
close exactly when every member of a block has the same total influence on
each other block. That is a symmetry condition (an equitable partition,
which the orbits of a symmetry group always give), not a weak-coupling
condition. Blocks can interact as strongly as they like.

## Assumptions

- Linear, discrete-time dynamics x(t+1) = Ax(t) with A constant, and linear
  aggregation y = Qx with Q an m × n matrix, m < n, of full row rank. The
  stochastic case adds row or column stochasticity.
- For the partition results, Q is a matrix of (possibly weighted)
  characteristic vectors of a partition of the variables.
- For the landscape applications: binary (or, in the appendix, suitably
  ordered multi-allele) genotypes on a Hamming graph, point mutation only
  (multiple mutations neglected at low rate), equal rates at all loci, and
  a linearized mutation–selection operator A = WM on absolute frequencies,
  with W the diagonal fitness matrix.
- The "best approximation" of Theorem 1.1 is in the Frobenius norm, read as
  an expected error over state vectors distributed isotropically (equal
  variances, no cross-covariance) about a uniform point.

## Key results

- **(1.1)–(1.2).** Exact aggregation by Q requires ĀQ = QA. If QQᵀ is
  invertible, Ā = QAQᵀ(QQᵀ)⁻¹. The converse does not hold: this Ā need not
  satisfy (1.1) for an arbitrary Q.
- **Theorem 1.1.** B = QAQᵀ(QQᵀ)⁻¹ minimizes ‖BQ − QA‖ in the Frobenius
  norm, so Ā is the best approximate aggregate operator for a given Q even
  when no exact one exists. *Holds when:* error averaged over an isotropic
  distribution of states.
- **Result 1.1.** Every n × n matrix, n ≥ 2, has an aggregation with m < n:
  take Q to be an eigenvector. **Result 1.2.** A symmetric matrix has one
  at every m, from any m of its n real eigenvectors. Such aggregations
  generally need every microstate to compute each macrostate.
- **Lemma 1.0.** For a positive stochastic A, the aggregate Ā is
  stochastic iff the columns of Q sum to one, which every partition
  satisfies.
- **(1.10)–(1.11).** For a partition Q of characteristic vectors, a given
  state x aggregates exactly when it is uniform within each block. The
  aggregation is exact for every x, and an aggregable state stays
  aggregable, iff A is **column-equitable**: for every pair of blocks I, J,
  Σ_{i∈I} A_ij is the same for every j ∈ J. With weights, a weighted
  version holds.
- **Equitable partitions** (Schwenk, McKay, Godsil; Stadler and Tinhofer).
  The orbits of any subgroup of a graph's automorphism group form an
  equitable partition. **Theorem 2.1** (cited, not proved here): the
  spectra of the row and column structure matrices R and S coincide and are
  contained in Spec(A), and R's characteristic polynomial divides A's when
  A is diagonalizable. So Ā keeps a subset of A's eigenvalues.
- **Simon–Ando as a limiting case.** For a nearly block-diagonal system,
  once each block is within ε of its own equilibrium, the rows of Q are the
  leading eigenvectors of the blocks and Ā_II is each block's leading
  eigenvalue. No error bound is given. Simon and Ando (1961) is cited, not
  reproduced.
- **Fitness landscapes.**
  - The point-mutation matrix on the hypercube has nested equitable
    partitions, by allele at one locus, two loci and so on.
  - On a multiplicative single-peak landscape, the Hamming-distance classes
    are equitable. That reduces 2ⁿ variables to n + 1, keeps every
    eigenvalue with its multiplicity dropped to one (Fig. 1, n = 5: e.g.
    0.7366 has multiplicity 5), and reproduces Eigen et al.'s error
    threshold (Fig. 2).
  - With two reference peaks, pairs of Hamming distances are equitable,
    giving (n − D₁₂ + 1)(D₁₂ + 1) classes.
  - **With three or more peaks, distance classes are not equitable.** The
    counterexample is four loci with peaks 1110, 1101 and 1011. Both 1000
    and 0111 lie at distances (2, 2, 2), but only 1000 has a neighbour,
    0000, at (3, 3, 3). This was checked here.
  - Refining to **overlap classes**, which split the loci by which subset of
    peaks shares their allele, restores equitability (a Result, with
    proof). Fig. 4 compares the two: a squared error of about 10⁻² with
    distance classes and about 10⁻¹⁶ with overlap classes, over ten steps.
- **Nonlinear aggregation.** Wagner and Laubichler's character
  decomposition aggregates genotypes by allele at a locus, under
  "pi-additive" fitness and generalized linkage equilibrium. It is
  dynamically sufficient but not an equitable partition, and it exists only
  in the relative-frequency (nonlinear) representation.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Aggregation (a closed lower-dimensional description) and decomposition (non-interacting subsets) are independent: each can hold without the other | strong for "aggregation without decomposition", asserted for the converse | definitions in the introduction; the thermodynamic example; Results 1.1–1.2 give aggregations that mix all variables. No example of decomposition without aggregation is given |
| C2 | A linear aggregation Q is exact iff some Ā satisfies ĀQ = QA, and Ā = QAQᵀ(QQᵀ)⁻¹ is the Frobenius-best approximate operator otherwise | strong | (1.1)–(1.2), Theorem 1.1 with derivation |
| C3 | Every matrix has an aggregation with m < n; a symmetric one at every m | strong over ℂ; Result 1.1 needs a qualification over ℝ | eigenvector argument; see Limitations |
| C4 | For a partition, the block sums aggregate exactly for every state iff A is column-equitable | strong | (1.10)–(1.11); re-derived in [THEORY-tmpj32n2](../theory.d/THEORY-tmpj32n2.md) |
| C5 | Hamming-distance classes give exact aggregation for one or two fitness peaks and not for three or more; overlap classes give it for any number | strong | two Results with proofs; the counterexample; Figs. 3–4 |
| C6 | Dynamically sufficient aggregate classes are candidate units of evolution, and equivalence under selection alone does not make one: the classes must also be equivalent under transmission | moderate | argued from C5, citing Lewontin (1970) on dynamical sufficiency |
| C7 | Any aggregation of a linear system is some form of (weighted) equitable partition, and Simon–Ando systems are one | weak | asserted in the discussion; in tension with C3 (see Limitations) |
| C8 | Linear aggregability is "probably a necessary (but not sufficient)" condition for aggregability in the nonlinear representation | weak | conjecture; its own Wagner–Laubichler example appears to contradict it (see Limitations) |

## Concepts

- **Decomposable**: A is block-diagonal under some ordering, so each block
  evolves alone. "Approximately decomposable" when the off-block entries
  are small (Simon and Ando).
- **Aggregable**: some y = f(x) with m < n variables obeys
  y(t+1) = Φ̄(y(t)), "dynamically sufficient". Nothing restricts which
  microvariables each yᵢ depends on.
- **Column-equitable partition**: within each block of A, every column sums
  to the same value. Row-equitable is the same for rows; equitable is
  both.
- **Structure matrix**: the matrix R (or S) of those block sums, the
  "quotient graph". Ā is a normalized structure matrix.
- **Overlap class**: for k reference genotypes, the loci whose alleles are
  shared by exactly a given subset of the references.

## Connections

It builds on Simon and Ando (1961) and Ando and Fisher (1963) for
near-decomposability, on graph-theoretic equitable partitions (Schwenk
1974; McKay; Godsil) and Stadler and Tinhofer (2000) for their spectral
properties, and on Eigen, McCaskill and Schuster (1989), whose quasispecies
computation it re-derives by aggregation. Its nonlinear contrast is Wagner
and Laubichler (2000). A companion preprint by Shpak, Stadler, Wagner and
Altenberg applies the Simon–Ando criteria themselves to landscapes
([LIT-tmp6rgoj](../literature.d/LIT-tmp6rgoj.md), registered unread).

## Bearing on the record

- **[THEORY-733](../theory.d/THEORY-733.md).** For deterministic x(t+1) = Ax, exact aggregation (1.1) is
  ĀQ = QA. That is [THEORY-733](../theory.d/THEORY-733.md)'s criterion L A = B L for a VAR(1), with
  L = Q. So in a linear Gaussian VAR(1), Shpak et al.'s exact aggregation
  and Barnett and Seth's exact dynamical independence are the same
  condition on the coarse map. [THEORY-733](../theory.d/THEORY-733.md) supplies the necessity under
  Gaussian noise. The join is the record's: neither paper cites the other.
- **[CLAIM-tmpkoi6k](../claims.d/CLAIM-tmpkoi6k.md).** C1 is the claim's slogan, with temperature as the
  natural example. C4 sharpens it. Under uniform coupling every partition
  of the units is column-equitable (each cross-block column sum is β times
  the block size), so the vector of block sums closes for every partition,
  though a single block's sum does not. Re-checked here: with six units
  split three and three, the transfer entropy into the pair of block sums
  is 0 to machine precision, and into one block sum 5.0 × 10⁻² at
  (α, β) = (0.2, 0.1). A non-uniform equitable matrix also closes, while a
  random one does not (3.1 × 10⁻¹). So grouping the members does find
  closed objects in that system, and they are not blocks. The claim
  stands as stated, and a note on it records this.
- **[QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md)** gains a third candidate unit, between "a subset of
  members" and "a function of the whole state": an equitable partition,
  whose groups interact strongly but whose group summaries jointly close.
- **[QUESTION-tmpt64jh](../questions.d/QUESTION-tmpt64jh.md).** Theorem 1.1's ‖ĀQ − QA‖_F is A5's closure defect,
  unweighted. For states with covariance Σ the least-squares operator is
  QAΣQᵀ(QΣQᵀ)⁻¹, the weighted version A5 asked for (a one-line derivation
  here, not the paper's). The paper relates neither defect to coupling
  strength, so the question stays open.
- **[THEORY-661](../theory.d/THEORY-661.md), [LIT-1127](../literature.d/LIT-1127.md).** The paper paraphrases the Simon–Ando result
  and supplies no error bound. The record still needs the 1961 paper,
  which is Unavailable.
- **[THEORY-607](../theory.d/THEORY-607.md).** C6 proposes dynamically sufficient classes as units of
  evolution, which is Bourrat's question at another grain (classes of
  genotypes, not collectives of particles). Its exact criterion has no
  cost term, so the identity partition passes it too, and it does not meet
  [THEORY-607](../theory.d/THEORY-607.md)'s promote_when.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** An equitable partition groups members whose cross-group
  coupling may be strong. It is a partition, as [CLAIM-157](../claims.d/CLAIM-157.md)'s grouping is,
  but it is not a gap-isolated block.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Result 1.1 over the reals.** The proof takes "at least one eigenvector"
  of A. A real matrix may have none: a plane rotation has no real
  eigenvector. With real Q the result holds for n ≥ 3, since a real matrix
  always has a real invariant subspace of dimension one or two, with
  m ≤ 2 < n. It fails for some 2 × 2 matrices. This is the same correction
  [THEORY-733](../theory.d/THEORY-733.md) made to Barnett and Seth's count for VAR(1).
- **C7 is overstated.** The discussion says "any aggregation of variables
  in a linear system will be some form of equitable partition". But
  Results 1.1–1.2 build aggregations from eigenvectors that mix all
  variables and correspond to no partition. The statement holds only if
  "weighted equitable partition" is stretched to any Q, which empties it.
- **C8 against its own example.** The authors conjecture that linear
  aggregability is necessary for nonlinear aggregability, then present the
  Wagner–Laubichler classes. Those aggregate in the relative-frequency
  representation and, by their own account, not in the linear one. Read
  literally, the example is a counterexample. They may mean something
  narrower, and the text does not say what.
- **No near-equitable theory.** Exactness only. The authors name the
  approximate case, nearly equitable partitions over stated timescales, as
  future work.
- **Simon–Ando is paraphrased, not derived.** There is no error bound and
  no statement of the timescale.
- **Theorem 2.1 is cited** from Stadler and Tinhofer, not proved.
- **The landscapes are special.** Exact aggregation needs fitness functions
  with symmetries concordant with the mutation graph. The overlap-class
  fitness function that makes three peaks work is "highly unnatural and
  contrived", in the authors' words.
- **Manuscript copy.** The published text and the 2005 erratum were not
  compared.

## Open questions

- When is a partition nearly equitable, and over what timescale does its
  aggregate track the full system? A bound in terms of the departure from
  column-equitability would answer it. With Simon–Ando's bound, it would
  answer [QUESTION-tmpt64jh](../questions.d/QUESTION-tmpt64jh.md) for partitions.
- Is there a decomposable linear system with no nontrivial partition-based
  aggregation? C1's "nor vice-versa" asserts the converse direction and
  gives no example. A block-diagonal A always lets each block's own
  eigenvector aggregations close, so the claim needs a narrower reading.
- Which nonlinear aggregations have no linear counterpart? C8 makes this
  open.
