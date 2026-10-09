---
number: 682
status: Read
formerly:
- NOTE-tmp2hvr8
paper: 'LIT-881'
title: 'Optimal Renormalization Group Transformation from Information Theory'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:1809.09632v2, 1 October
    2019; 27 pp.: main text pp. 1–13, references pp. 13–16, Appendices
    A–F pp. 16–27), text extracted with pdftotext. Main text, all six
    appendices and the reference list read. The Lemma and Propositions 1
    and 2 (Appendix B, Eqs. B1–B22) followed step by step; the cumulant
    machinery and the transfer-matrix expressions for the mutual
    information (Appendices C and D) read, not re-derived. One number
    checked independently: the share of I(V : E) that decimation keeps in
    the 1D Ising example at K = 0.1 with a one-site buffer, computed from
    the four-spin marginal, is 0.505. Figures read as text only: the
    density plots and curves did not survive extraction, so their content
    is taken from captions and text. Read after LIT-873 and NOTE-674, to
    place it without repeating them. The published Physical Review X
    version (open access) was not read; small differences from v2 cannot
    be ruled out.
date: '2026-10-09'
summary: >-
  Proves that a block coarse-graining keeping all of the block's mutual
  information with the system beyond a buffer makes the coarse measure
  factorize across the block, so a finite-range Hamiltonian gains no range
  (1D; D dimensions with an extra assumption) and 1D disorder gains no
  correlations across it. Where the condition fails, as it does for its
  own examples, it shows on two-spin blocks of 1D Ising chains that
  longer-range, many-spin and disorder-correlation terms shrink as more
  information is kept. Explains decimation in 1D and majority rule in 2D
  by the cost of encoding into one binary spin.
---
<!-- inactive-ok-file: LIT-039 — Deferred; named as an unread neighbour, not leaned on -->
<!-- inactive-ok-file: THEORY-198 THEORY-194 THEORY-073 THEORY-017 QUESTION-025 — Proposed or open; cited as what this reading produced, accounts it bears on, and the question it does not answer -->

# NOTE-682: Optimal Renormalization Group Transformation from Information Theory

## Contribution

[LIT-873](../literature.d/LIT-873.md) showed numerically that the coarse variable of a block chosen to
carry the most information about the far environment recovers known
renormalization-group variables. This paper supplies a reason. It proves
that if a coarse variable keeps all of that information, the coarse
probability measure factorizes across the block, which forbids the
renormalized Hamiltonian from coupling the two sides, and, for 1D
disorder, forbids correlations across the block in the renormalized
disorder distribution. It then studies coarse-grainings that keep only
part of the information, and decomposes the information lost into a
choice-of-mode part and an encoding part, which accounts for why the best
rule differs between one and two dimensions.

## Key insight

With short-range interactions, a region of finite width mediates every
correlation between its two sides. If the region's summary keeps
everything the region knows about the sides, the summary mediates them
too, and nothing on one side can depend on the other except through it.
That screening is what a short-ranged effective Hamiltonian is, so
"keep all the information about the far field" and "do not generate
long-range couplings" are, under perfect capture, the same demand.

## Assumptions

- **Classical lattice systems with finite-range Hamiltonians**, at
  equilibrium, P(X) ∝ e^{K[X]}; blocks taken large enough that only
  neighbouring blocks interact.
- **Block RG.** The coarse-graining factorizes over blocks, P(X′|X) =
  Π_j P_Λ(H_j|V_j). The partition into block, buffer, environment (and an
  outer region O, for algorithmic reasons) is fixed in advance.
- **Full information capture** for the theorems: I(H₀ : E₀) = I(V₀ : E₀),
  the upper bound. The authors concede that with the number and type of
  coarse variables chosen in advance a rule meeting it need not exist.
- **In D dimensions, an extra assumption.** The proof runs on
  (D − 1)-dimensional hyperplanes of blocks, each block still with its own
  coarse variable; it needs full capture for the hyperplane to be
  equivalent to full capture by each block separately, "reasonable for a
  short-ranged Hamiltonian, at least in the isotropic case".
- **No fine-tuning.** Factorization of the measure is turned into "no
  next-nearest-neighbour terms" by excluding the case in which integrating
  out the buffer exactly cancels pre-existing longer couplings.
- **Disorder**, for Proposition 2: 1D, a product distribution over
  nearest-neighbour couplings, and changes confined to one environment.
- **For the calculations**: the RBM rule P_Λ(h|V) = 1/(1 + e^{−2h Σ λᵢvᵢ}),
  no bias by Z₂ symmetry; blocks of two spins into one; periodic chains;
  K = 0.1 and a one-site buffer for the plotted cases; cumulant expansion
  in powers of K, to tenth order (clean) or ninth (disordered, 16 spins).
  The physically meaningful rules are the large-|Λ| limit, where the rule
  becomes deterministic.

## Key results

- **Bounds** (Eqs. 7, 8, 22). 0 ≤ I_Λ(H : E) ≤ H(H); I_Λ(H : E) ≤
  I(V_Λ : E) ≤ I(V : E), from the Markov chain E → V → V_Λ → H, where V_Λ
  is the normalized linear combination Σ λᵢⱼvⱼ a hidden reads.
- **Lemma** (Appendix B). Full capture gives I(E₀ : X₀ | X₀′) = 0;
  locality gives I(E_L : E_R | X₀) = 0; together, P(E_L, E_R | X₀′) =
  P(E_L | X₀′) P(E_R | X₀′). Translation invariance is not used.
- **Proposition 1 and Corollaries 1–2.** The coarse measure factorizes:
  P(X′_{≤−2}, X′_{≥2} | X₀′) = P(X′_{≤−2} | X₀′) P(X′_{≥2} | X₀′), with the
  coarse buffer integrated out. Hence no effective terms couple the two
  sides, and a perfect RSMI step does not increase the range of a
  finite-range Hamiltonian; in D dimensions under the extra assumption.
- **Proposition 2 and Corollary 3.** In 1D with product disorder, the
  optimal rule of a block and the factorization survive any disorder
  change confined to one environment, so no disorder correlations are
  generated across the block, and the optimal rule depends only on the
  disorder near the block.
- **1D Ising, arbitrary two-spin rules** (Sec. IV, Figs. 3–5, 10–12).
  Information kept is largest near (±λ, 0) and (0, ±λ), decimation, and
  least at majority rule. The rangeness ratio K′₂(2)/K′₂(1) and the
  m-bodyness ratio K′₄(1,1,1)/K′₂(1) vanish at the maximum for large |λ|;
  for the RSMI solution, two-point couplings decay exponentially with
  distance and m-point couplings with m. The perturbative nearest-neighbour
  coupling converges to the exact decimation value K′ = ½ log cosh 2K as
  the order rises. The maximum saturates in |λ| (little difference between
  λ = 3 and λ = 1000). At that maximum decimation keeps only about half of
  I(V : E): 0.505 by my calculation at K = 0.1 with a one-site buffer, the
  value Fig. 5's axis appears to reach. Full capture is not attained.
- **Not globally monotonic** (Appendix D). Rangeness is a monotonic
  function of the information only locally; a global maximum of the
  information is a global minimum of rangeness, possibly with equivalent
  solutions (for three-spin blocks, decimation to the centre spin is as
  good for the Hamiltonian as to an edge spin, though the information
  prefers the edges). Ratios also vanish accidentally elsewhere, so the
  authors advise watching the information saturate, not a coefficient.
- **Dilute random Ising chain** (Sec. VI, Fig. 9). Distance correlation
  and KL divergence between neighbouring renormalized couplings, and the
  centre of mass of the distribution outside the nearest-neighbour
  two-body plane, all vanish where the information is maximized, at
  decimation.
- **Encoding loss** (Eq. 24, Sec. V). I_Λ(H : E) = I(V_Λ : E) −
  I(V_Λ : E | H). Majority rule's V_Λ takes three values, which a binary H
  cannot encode unless V_Λ = 0 has probability zero. In a four-spin 1D toy
  model (Eq. 25, Fig. 6) majority rule has the larger I(V_Λ : E) but
  decimation has the larger I(H : E) throughout; greedy maximization of
  I(V_Λ : E) followed by encoding is therefore not optimal. Coupling the
  two environment spins (Appendix E, Fig. 13) narrows the gap. In a 2D
  toy model (four spins coupled to one environment variable with nine
  states, Fig. 7), majority rule, and coupling to three spins, keep more
  than decimation or any two-spin rule at every K_V.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A coarse-graining keeping all of a block's information about the environment beyond a buffer makes the coarse measure factorize across the block, so a finite-range Hamiltonian gains no range | strong in 1D; moderate in D dimensions | proof, Appendix B; the D-dimensional case adds a per-block capture assumption and excludes fine-tuned cancellation |
| C2 | Under the same condition in 1D with product disorder, no correlations are generated across a block in the renormalized disorder distribution, and the optimal rule depends only on local disorder | strong, for its hypotheses | proof, Proposition 2 |
| C3 | When full capture is not attained, longer-range and many-spin couplings decrease as the information kept increases | weak in general; moderate for two-spin blocks of the 1D Ising chain | perturbative calculation, Figs. 4, 5, 10–12; only locally monotonic |
| C4 | Disorder correlations and couplings outside the nearest-neighbour plane decrease as the information kept increases | moderate for the dilute random Ising chain | perturbative calculation, 16 spins, Fig. 9 |
| C5 | Decimation is the information-optimal two-spin rule in 1D and majority rule in 2D, because a binary coarse spin cannot encode an average, and a connected environment reduces that loss | moderate | exact calculation on four-spin toy models, Figs. 6, 7, 13 |
| C6 | RSMI maximization is a model-independent variational principle defining the optimal RG coarse-graining | weak | framing over C1–C5; the authors call it "strongly" supported |

## Method

Analytical throughout. The Lemma and Propositions are proved from the
chain rule for mutual information, locality and the block factorization.
The effective Hamiltonian of an arbitrary rule is obtained by splitting
K into intra- and inter-block parts, writing the renormalized Hamiltonian
as an intra-block average of e^{K₁}, and expanding in cumulants, which
factorize into three block parameters (a₁, a₂, b) for the Ising chain; the
resulting polynomial is brought to a canonical form by eliminating
non-canonical terms. The mutual information of an arbitrary rule is
computed exactly by transfer matrices in the thermodynamic limit. No
learning is done; the RBM is only a differentiable family of rules.

## Concepts

- **RSMI**: I_Λ(H : E), the mutual information between a block's coarse
  variables and the environment beyond a buffer, as in [LIT-873](../literature.d/LIT-873.md).
- **full information capture**: I(H₀ : E₀) = I(V₀ : E₀), the upper bound,
  called a "perfect" RSMI coarse-graining.
- **V_Λ**: the linear combination of the block's spins a hidden couples
  to under an RBM rule; what the rule chooses to look at, as opposed to
  how it encodes it.
- **mismatch**: I(V_Λ : E | H), the information about the environment
  carried by V_Λ that the coarse variable fails to encode.
- **rangeness / m-bodyness**: the ratios K′₂(2)/K′₂(1) and
  K′₄(1,1,1)/K′₂(1), used as measures of the renormalized Hamiltonian's
  complexity.
- **dCOM**: the norm of the mean of the renormalized disorder
  distribution's components outside the nearest-neighbour two-body
  couplings.

## Connections

It is the theoretical companion to Koch-Janusz and Ringel ([LIT-873](../literature.d/LIT-873.md), read
in [NOTE-674](NOTE-674.md)), whose saturation argument for 1D and quasi-1D chains it
turns into the Lemma and extends; its 1D findings match that paper's
three-filter comparison (decimation best) and its 2D finding matches that
paper's 2 × 2 block spin. It presents RSMI as the information bottleneck
([LIT-338](../literature.d/LIT-338.md)) with a compressed variable of fixed type and size and the
environment as the relevance variable. It sets itself against fixed
schemes, citing van Enter, Fernández and Sokal on the pathologies of
real-space RG and Kennedy on majority rule, and, in Appendix F, against
perfect actions (Hasenfratz and Niedermayer) and coarse-grained PDE
schemes, where optimality is error against a known continuum problem.
Rigorous treatment of the RSMI measure is left open; Kupiainen's comment
on rigorous RG ([LIT-039](../literature.d/LIT-039.md)) is held here unread.

## Bearing on the record

- **Produces [THEORY-198](../theory.d/THEORY-198.md)**: full capture forbids range growth, and
  the theorem's hypothesis is not met in the cases that illustrate it.
- **[THEORY-194](../theory.d/THEORY-194.md).** Supports it on the point it was thinnest: why the
  information-maximizing coarse-graining should give a short-ranged
  effective Hamiltonian. It does not meet its `promote_when`: the proof is
  for perfect capture, not for the constrained maximizer, the
  D-dimensional version adds an assumption, and the partial-capture
  evidence is 1D. The 2D toy model is consistent with [THEORY-194](../theory.d/THEORY-194.md)'s
  majority-rule finding but is a four-spin model, not a lattice.
- **[THEORY-073](../theory.d/THEORY-073.md).** The Lemma is a screening statement: the block's summary
  plays the role of a blanket between the two environments. The block,
  buffer and environment are fixed before any information is computed,
  as [THEORY-073](../theory.d/THEORY-073.md) says a blanket's placement is. My connection, not the
  paper's; it neither supports nor weakens [THEORY-073](../theory.d/THEORY-073.md).
- **[THEORY-017](../theory.d/THEORY-017.md).** As in [NOTE-674](NOTE-674.md): the information is invariant under
  re-encodings, the partition is not, and here the theorems depend on the
  partition through the locality assumption.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** No direct bearing; no attributes, embeddings or
  lattices. The encoding-loss decomposition is the nearest thing to a
  transferable result: what a summary of fixed type can keep depends on
  whether the quantity it should read fits that type.
- **Anthology.** No training, no practice instruction; the RBM is a
  parametrization. Not flagged.

## Limitations

- **The theorems' hypothesis is not met by the examples.** Decimation of
  two-spin blocks keeps about half the block's information, yet gives an
  exactly nearest-neighbour Hamiltonian; the exactness there comes from
  the 1D chain's structure, not from Proposition 1.
- **"Monotonic decay" is local.** The abstract speaks of decay as a
  function of information retained; Appendix D says it is monotonic only
  locally, with accidental zeros elsewhere.
- **All partial-capture evidence is 1D, two-spin blocks, weak coupling**
  (K = 0.1), perturbative, with 16 spins for the disordered case. The 2D
  evidence is a four-spin toy model with a single environment variable.
- **The D-dimensional proof rests on an assumption stated as
  "reasonable"**, not proved, and on excluding fine-tuned cancellations.
- **Proposition 2 is 1D.** Generalization to higher dimensions is said
  to follow "similarly", not shown.
- **Small inconsistencies in the text.** Appendix E calls the 1D toy
  model "Eq. (6)", which is the RSMI definition; the toy model is Eq. 25.
  Appendix D's "Fig. (4c)" for crossings along paths of fixed |λ| appears
  to mean Fig. 5. "Course-graining" for coarse-graining twice.

## Open questions

- Does the constrained maximizer, not the perfect one, provably bound the
  range or decay of the effective couplings, in two or more dimensions?
  The authors name this as what a rigorous result would need.
- Can the number and type of coarse variables themselves be optimized,
  so that the encoding loss is not fixed by a choice made in advance? The
  authors pose it.
- Does the per-block capture assumption of the D-dimensional proof hold
  for any 2D model that can be checked, such as the 2D Ising model with
  2 × 2 blocks?
