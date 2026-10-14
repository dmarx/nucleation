---
number: 824
status: Read
formerly:
- NOTE-tmp5aqd2
paper: LIT-252
title: 'Pfau et al. — Spectral Inference Networks'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v3 PDF (arxiv.org/pdf/1806.02215, 26 pp.,
    headed "Published as a conference paper at ICLR 2019"), text extracted
    with pdftotext: §1–6, Appendix A (the symmetry-breaking strategies, the
    correctness argument for the masked gradient and its derivation, line
    by line), Appendix B (the TensorFlow pseudocode) and Appendix C (the
    training details and the Arcade Learning Environment comparison).
    Figures 1–11 were seen only through their captions, so the quality of
    the recovered eigenfunctions and of the Atari features was not judged.
date: '2026-10-14'
summary: >-
  For a symmetric kernel k on a space with a sampling density p, the span
  of the top N eigenfunctions of K[f](x) = E_x′[k(x,x′)f(x′)] maximizes
  Tr(Σ⁻¹Π) over functions, with Σ = E[uuᵀ] and Π = E[k(x,x′)u(x)u(x′)ᵀ];
  a Cholesky-masked gradient orders them and moving averages of Σ and its
  Jacobian remove the minibatch bias. Slow Feature Analysis is the
  graph-Laplacian case. The ordering argument is informal by the authors'
  own statement, and the paper never considers contrastive kernels or
  positive pairs.
---
<!-- inactive-ok-file: THEORY-009 THEORY-239 — Proposed; the accounts this reading bears on -->
<!-- inactive-ok-file: NOTE-231 — Superseded; the seeded skim this reading replaces, named for a wording it corrects -->

# NOTE-824: Pfau et al. — Spectral Inference Networks

## Contribution

The paper turns the variational characterization of a symmetric
operator's top eigenspace into a stochastic objective that a neural
network can optimize from samples, without a Nyström extension. It adds
two devices: a masked gradient that makes the network's outputs converge
to ordered eigenfunctions rather than an arbitrary basis of their span,
and a two-timescale scheme that replaces the biased minibatch estimate of
Σ and its Jacobian by moving averages. It shows the method recovering the
known eigenfunctions of a two-dimensional hydrogen atom, and learning
slow features from synthetic video.

## Key insight

The eigenproblem never needs the operator as a matrix. With the inner
product ⟨f, g⟩ = E_p[fg], the top-N eigenspace is the maximizer of a ratio
of two expectations, Tr(E[uuᵀ]⁻¹ E[k u uᵀ]), and both can be estimated from
samples of x and x′. The ratio is invariant to any invertible linear map of
the features, so plain optimization gives the span; order has to be put in
by hand.

## Assumptions

- **A symmetric kernel**: "a symmetric (not necessarily positive definite)
  kernel k(x, x′)" (§3.2), so that K is self-adjoint on L²(p).
  Algorithm 1 takes "given symmetric kernel k" as input.
- **A proper sampling distribution** p from which data are drawn, with
  each output of u integrable under it. An improper density is allowed in
  principle only.
- **Pointwise kernel evaluation** on pairs. Π is estimated as
  (1/N) Σ k(x_i, x′_i) u(x_i)u(x′_i)ᵀ over sampled pairs (Algorithm 1,
  line 6). For local operators (the Laplacian, the Hamiltonian) the double
  expectation collapses to a single one.
- **For the ordering claim**: the true eigenfunctions lie in the function
  class, and the masked-gradient ascent reaches a stationary point that is
  a maximum (App. A.2, Claim 2).
- **For the bias correction**: the two-timescale step-size conditions of
  Borkar (1997), Eqs. 15–16. The experiments use constant rates instead.

## Key results

- **Finite case (§3.1, Eqs. 1–5).** For symmetric A, the top eigenvector
  maximizes the Rayleigh quotient uᵀAu/uᵀu, and the top-N subspace
  maximizes Tr((UᵀU)⁻¹UᵀAU) (Edelman et al. 1998). The objective "is
  invariant to right-multiplication of U by an arbitrary matrix".
- **Function space (§3.2, Eqs. 6–7).**
  max_u Tr(E_x[u(x)u(x)ᵀ]⁻¹ E_(x,x′)[k(x,x′)u(x)u(x′)ᵀ]), equivalently
  max Tr(Π) subject to Σ = I. Stated by analogy with Eq. 5, not proved for
  infinite-dimensional spaces.
- **Kernels (§3.3, Eqs. 8–9).** With k the graph Laplacian on a
  neighbourhood graph, k(x,x′)u(x)u(x′)ᵀ is replaced by
  (u(x) − u(x′))(u(x) − u(x′))ᵀ over neighbouring pairs (citing Sprekeler
  2011). With adjacent video frames as neighbours this is Slow Feature
  Analysis, so "SFA is a special case of SpIN". Eq. 9 gives the continuum
  limit, the differential Laplacian. For these operators the useful
  eigenfunctions are at the bottom of the spectrum, and the experiments
  minimize the quotient.
- **Ordering (§4.1, Eqs. 10–12; App. A).** With L the Cholesky factor of
  Σ and Λ = L⁻¹ΠL⁻ᵀ, the upper-left n × n block of Λ depends only on
  u_1..n (Claim 1, shown). Masking the gradient of Λ_ii to u_i alone makes
  each u_i ascend Λ_ii, and v = L⁻¹u is claimed to be the ordered
  eigenfunctions (Claim 2, by induction). The authors say these arguments
  "are not meant as mathematically rigorous proofs". At an extremum,
  E_x′[k(x,x′)u*(x′)] = ΠΣ⁻¹u*(x) (Eqs. 21–24), so diagonalizing
  L⁻¹ΠL⁻ᵀ after training is an alternative; they found it numerically
  fragile.
- **Bias correction (§4.2).** Eq. 14 is linear in Π and J_Π but not in Σ
  and J_Σ, so those two are replaced by moving averages, making training a
  two-timescale bilevel problem. Each step needs the Jacobian of Σ, about
  N² backward passes.
- **Hydrogen atom (§5.1, Fig. 1).** Nine eigenfunctions of
  H = −∇² + 1/|x| in two dimensions, batch size 128. Without the moving
  average (β = 1) the eigenfunctions and eigenvalues are wrong. With
  β = 0.01 the eigenvalues converge to the closed-form values
  −1/(2n + 1)² with multiplicity 2n + 1, up to rotation inside the nearly
  degenerate multiplets.
- **Bouncing balls (§5.2, Fig. 2).** Twelve slow features of synthetic
  video, most of them encoding ball positions and one a joint
  configuration. None encodes velocity.
- **Atari (App. C.3).** SpIN features, with the SFA kernel, are compared
  with successor-feature eigenpurposes by averaging the 100 most and least
  activating frames. The comparison is qualitative.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The top-N eigenspace of a symmetric operator on L²(p) maximizes Tr(Σ⁻¹Π) | strong | the finite-dimensional result of Edelman et al., carried over by analogy (§3.1–3.2) |
| C2 | SFA is SpIN with the graph-Laplacian kernel on adjacent frames | strong | Eq. 8 with Sprekeler (2011) |
| C3 | The masked gradient yields ordered eigenfunctions | weak | an informal induction (App. A.2) that assumes realizability and a reached maximum |
| C4 | Moving averages of Σ and J_Σ remove the bias of minibatch gradients | moderate | the two-timescale theory under schedules not used, plus the β ablation on the hydrogen atom (Fig. 1) |
| C5 | SpIN recovers true eigenfunctions | moderate | one problem with a closed-form solution (Fig. 1) |
| C6 | SpIN finds interpretable features from video and Atari | weak | qualitative inspection of synthetic video and averaged frames |

## Method

1. Draw minibatches of x and x′. Compute
   Σ̂ = ½(mean of u(x)u(x)ᵀ + mean of u(x′)u(x′)ᵀ) and
   Π̂ = mean of k(x, x′)u(x)u(x′)ᵀ.
2. Update the moving averages Σ̄ and J̄_Σ, and take the Cholesky factor L̄
   of Σ̄.
3. Ascend the masked gradient of Tr(Λ), Eq. 14, using Π̂ and J_Π from the
   minibatch and Σ̄, J̄_Σ from the averages.
4. Read off the eigenfunctions as v(x) = L̄⁻¹u(x).

## Concepts

- **Spectral Inference Network.** Any method that (1) optimizes Eq. 6
  end-to-end by stochastic optimization, (2) over a parametric class,
  (3) with the masked gradient of Eq. 14, and (4) with bilevel
  optimization against minibatch bias (§4.3).
- **Σ, Π.** The feature second moment E[uuᵀ] (called "covariance") and
  the kernel-weighted cross moment E[k(x,x′)u(x)u(x′)ᵀ].
- **Slow Feature Analysis.** Minimizing the expected squared change of
  features between adjacent frames under unit second moment; here, the
  bottom eigenfunctions of the temporal-neighbour graph Laplacian.

## Connections

The finite-dimensional objective is Edelman, Arias and Smith's (1998). The
SFA case rests on Sprekeler's (2011) equivalence of SFA with Laplacian
eigenmaps. The paper relates the method to variational quantum Monte Carlo
(Foulkes et al.; Carleo and Troyer; Choo et al.), to proto-value
functions (Mahadevan and Maggioni) and to Machado et al.'s eigenoptions.
Balestriero and LeCun ([LIT-228](../literature.d/LIT-228.md)) later name it, with Sprekeler, as "a
perhaps more direct connection" for spectral SSL ([NOTE-752](NOTE-752.md)). Johnson et al.
([LIT-258](../literature.d/LIT-258.md), App. E.2) name it and NeuralEF as ways to extract the
eigenfunctions of K⁺, and use NeuralEF ([NOTE-751](NOTE-751.md)).

## Bearing on the record

- **[THEORY-007](../theory.d/THEORY-007.md) says that SpIN "learn the same objects directly (eqs.
  6–7)".** That overstates the paper. Eqs. 6–7 are for a generic symmetric
  kernel evaluated pointwise on sampled pairs, and the paper never
  mentions K⁺, positive pairs or contrastive learning. Applied with
  k = K⁺, Π becomes E over positive pairs of u(a)u(a′)ᵀ, so the objective
  can be estimated from positive pairs without knowing K⁺. That step is
  the record's, not the paper's, and the paper's own correctness argument
  for recovering the ordered eigenfunctions is informal. It should read:
  SpIN would learn these eigenfunctions if given K⁺, or positive pairs in
  place of kernel-weighted independent pairs; the paper shows recovery
  only for the two-dimensional hydrogen atom.
- **[THEORY-009](../theory.d/THEORY-009.md) quotes §5.2 accurately** ("the time dynamics are
  reversible, and hence the transition function is a symmetric
  operator"), but **its summary overstates the paper.** It groups the
  paper with those whose symmetry is "the symmetry of the positive-pair
  distribution". In SpIN, symmetry is a precondition placed on k (§3.2,
  Algorithm 1). The SFA kernel actually trained, through
  (u(x) − u(x′))(u(x) − u(x′))ᵀ (Eq. 8), is symmetric in its two
  arguments by construction, whatever the dynamics. The reversibility
  sentence is an aside that no derivation uses. On this point the paper
  is nearer to Simon et al. (symmetric by the form of the objective) than
  to Johnson et al. or HaoChen et al. It has no notion of a positive-pair
  distribution. Like them, it never mentions Riesz, so [THEORY-009](../theory.d/THEORY-009.md)'s claim
  that the adjoint is never invoked in earnest holds here.
- **[NOTE-231](NOTE-231.md) (the seeded skim) called §5.2 "the paper's explicit use of
  self-adjointness to license the method".** That is too strong, for the
  same reason.
- **On the seed's question about non-reversible dynamics.** The paper does
  not say what fails. App. C.3 compares against successor features
  qualitatively only and says nothing about asymmetry.
- **No THEORY filed.** The paper's mathematical content is the
  variational characterization of a symmetric operator's top eigenspace,
  which is Edelman et al.'s and is already used by [THEORY-007](../theory.d/THEORY-007.md), and the SFA
  identity, which is Sprekeler's. Its own contributions are an algorithm
  (the masked gradient and the bilevel scheme) with an informal
  correctness argument. As a training method, that belongs to the
  anthology's subject, not to an account of what is true.

## Limitations

- The ordered-eigenfunction claim is argued informally, assuming the true
  eigenfunctions are realizable and a maximum is reached.
- The infinite-dimensional objective is carried over from the matrix case
  by analogy. No conditions (compactness, a discrete spectrum) are given
  for the top eigenspace to exist.
- The cost is N² backward passes per step for the Jacobian of Σ, which the
  authors name as the bottleneck.
- Only one experiment has ground truth. The video and Atari results are
  judged by eye.
- The learning-rate schedules the convergence theory needs are not the
  ones used.

## Open questions

- What does the method compute when k is not symmetric, for example the
  transition kernel of non-reversible dynamics, where the natural object
  is a singular value decomposition ([THEORY-009](../theory.d/THEORY-009.md), [THEORY-239](../theory.d/THEORY-239.md))?
- Is there a rigorous version of Claim 2, under what conditions on the
  function class and the optimizer?
