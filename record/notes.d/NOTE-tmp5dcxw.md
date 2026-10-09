---
status: Read
paper: 'LIT-tmpbq8zx'
title: 'The power of deeper networks for expressing natural functions'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:1705.05502v2, 27 April
    2018, 14 pp.), which the authors replaced "to match version published
    at ICLR 2018"; text extracted with pdftotext and kept as paper.txt in
    the scratchpad download directory (dl/reg-rolnick2017/). Every
    section, the appendix (proofs of Theorems 4.1 to 4.4) and the
    reference list read. Proposition 3.3, the upper bound of Theorem 3.4,
    Proposition 4.5, the square-and-multiply construction of Proposition
    4.6, the necessity proof of Theorem 4.2, the counting step of Theorem
    4.3 and the neuron sum of Theorem 5.1 checked by hand; the Lagrange
    recursion (Eq. 5) not re-derived. The uniform-approximation step in
    the proofs of Theorems 4.1 and 4.4 examined and found unsupported (see
    Limitations). Figures read from captions and text. v1 (16 May 2017)
    compared for its theorem statements only. LIT-887's reading (NOTE-688)
    read first, so that this note records what the sequel adds.
date: '2026-10-09'
summary: >-
  Proves that a single hidden layer of smooth, bias-free units needs
  exactly ∏(rᵢ+1) neurons to Taylor-approximate x₁^r₁⋯xₙ^rₙ while a deep
  network needs O(Σ log rᵢ), extends the gap to sparse and univariate
  polynomials, and bounds a product of n inputs at depth k by about
  2^(n^(1/k)). Its uniform-approximation lower bounds rest on an unproved
  step, the depth-k tightness is a conjecture, and the gap is set by
  degree, so bounded-degree polynomials show none.
---
<!-- inactive-ok-file: THEORY-tmppv845 THEORY-195 THEORY-201 THEORY-183 THEORY-186 QUESTION-025 CLAIM-042 CLAIM-119 — Proposed or open; cited as what this reading produced, the accounts it is set beside, and the question and claims it bears on -->

# NOTE-tmp5dcxw: The power of deeper networks for expressing natural functions

## Contribution

[LIT-887](../literature.d/LIT-887.md) proved one depth separation: one hidden layer needs 2^n neurons to
Taylor-approximate the product of n inputs, a deep tree about 4n. This
paper makes that a family. Any monomial x₁^r₁⋯xₙ^rₙ costs exactly ∏(rᵢ+1)
neurons in one hidden layer and O(Σ log rᵢ) in a deep network; a sparse
polynomial costs at least 1/c of its dearest monomial; xᵈ is linear
against logarithmic; and depth k brings the cost of an n-fold product
down to about 2^(n^(1/k)), with a conjecture that this is tight. It also
shows that a fixed number of neurons suffices for any ε, so the
separations are between finite limits, not rates.

## Key insight

A one-hidden-layer network of bias-free units is a sum of powers of
linear forms, Σⱼ wⱼ σₖ (aⱼ·x)ᵏ at each degree k; to produce a monomial it
must span all the monomial's partial derivatives, and a monomial with
many distinct variables has exponentially many. Depth sidesteps this by
squaring and multiplying, a few neurons per step. So the cost of
flattening is the dimension of a polynomial's space of partial
derivatives, and that grows with degree in distinct variables.

## Assumptions

- **Network model without biases**: N(x) = A_k σ(⋯σ(A₁σ(A₀x))⋯), no
  bias in any layer or at the output. Constants are made by units with
  zero input weight (the square gate's −2σ(0) is a third neuron), so
  counts would shift with biases; the paper does not treat them.
- **Smooth σ with nonzero Taylor coefficients at 0**: up to degree d for
  the Taylor-sense results, up to 2d for the uniform lower bounds, only
  the d-th for Theorem 4.4. ReLU is excluded explicitly (Theorem 3.4 is
  false for it); tanh, odd with vanishing even coefficients, fails the
  hypotheses too.
- **Two notions of approximation.** Taylor: p is the degree-d Taylor
  polynomial of N at 0. Uniform: sup over (−R, R)ⁿ of |N − p| < ε, for all
  ε, with the neuron count fixed and the weights free (they grow as δ⁻ᵈ
  with δ → 0, as in [LIT-887](../literature.d/LIT-887.md)).
- **Neurons counted, not weights.** Size is hidden units; magnitude and
  precision are free. Synapse counts appear only in the conclusion's
  remark on locality.
- **"Natural"** means monomials, sparse polynomials and xᵈ. Nothing in
  the paper ties these to data.

## Key results

- **Proposition 3.3.** If N Taylor-approximates a homogeneous p of degree
  d, then N(δx)/δᵈ ε-approximates p on (−R, R)ⁿ for small δ, with the
  same layer widths. Checked: the remainder is Σ_{i>d} δ^(i−d) Eᵢ(x).
  The converse fails.
- **Theorem 3.4.** For σ with nonzero Taylor coefficients to degree d,
  lim_{ε→0} m_k(p) is finite for every degree-d polynomial: sum one
  Taylor-approximating network per monomial, each rescaled to ε/s.
- **Theorem 4.1** (uniform; σ nonzero to degree 2d): m₁(p) = ∏(rᵢ+1);
  m(p) ≤ Σ(7⌈log₂ rᵢ⌉+4). **Theorem 4.2** (Taylor; σ nonzero to degree d):
  the same two bounds. Sufficiency from [LIT-887](../literature.d/LIT-887.md)'s sign-pattern sum, of
  which only ∏(rᵢ+1) terms are distinct once copies of xᵢ are merged.
  Necessity: the matrix A_{S,j} = ∏_{h∈S} a_{hj}, over the ∏(rᵢ+1)
  sub-multisets S, has full row rank. Checked for Theorem 4.2: take
  derivatives by each S; a dependence among rows of maximal |S| yields a
  vanishing combination of the distinct monomials ∂_S p.
- **Theorem 4.3** (sparsity c): m₁(p) ≥ (1/c)·maxⱼ m₁(qⱼ) and
  m(p) ≤ Σⱼ m(qⱼ), uniform and Taylor. The lower bound follows from "m₁ is
  at least the rank of p's partial derivatives", asserted by analogy, and
  a counting step (each ∂p has at most c monomials and contains a
  distinct ∂q), checked.
- **Theorem 4.4.** With only σ_d ≠ 0, m₁(p) ≥ (1/d)∏(rᵢ+1), and at least the
  largest coefficient of ∏ᵢ(1 + y + ⋯ + y^rᵢ). (v1 stated this, for a
  product, as m₁ ≥ C(n, ⌊n/2⌋) ~ 2ⁿ/√(πn/2).)
- **Propositions 4.5 and 4.6.** Any univariate degree-d polynomial: m₁^Taylor
  ≤ d+1 with input weights fixed at distinct a₀, …, a_d (a Vandermonde
  argument, checked). For xᵈ: m₁ = d+1, and m ≤ 7⌈log₂ d⌉ by repeated
  squaring with a three-neuron square gate and a four-neuron product
  gate per binary digit.
- **Theorem 5.1.** For x₁⋯xₙ at depth k, grouping factors b₁⋯b_k = n gives
  m_k^Taylor ≤ Σᵢ (n/∏_{j≤i} bⱼ)·2^(bᵢ), and bᵢ = n^(1/k) gives
  O(n^((k−1)/k)·2^(n^(1/k))); checked. The optimal bᵢ grow slowly with i
  (Eq. 5, Fig. 1).
- **Conjecture 5.2.** m_k(x₁⋯xₙ) = 2^Θ(n^(1/k)). Evidence: Fig. 2, a heat
  map of error for trained dense networks on n = 20, inputs uniform on
  [0, 2], tanh, AdaDelta, absolute-error loss; ReLU "similar". No numbers
  are reported beyond the figure.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A fixed number of neurons approximates any polynomial to every ε, for smooth σ with nonzero Taylor coefficients | strong, with unbounded weights | Proposition 3.3, Theorem 3.4; checked |
| C2 | One hidden layer needs exactly ∏(rᵢ+1) neurons to Taylor-approximate x₁^r₁⋯xₙ^rₙ; a deep network O(Σ log rᵢ) | strong, bias-free networks only | Theorem 4.2 and its proof; checked |
| C3 | The same lower bound holds for uniform approximation | weak as proved | Theorem 4.1; the proof assumes uniform closeness forces closeness of Taylor coefficients, which is false in general |
| C4 | A polynomial with c monomials costs one hidden layer at least 1/c of its dearest monomial | strong in the Taylor sense | Theorem 4.3; counting checked, rank lemma by analogy with Theorem 4.2 |
| C5 | xᵈ costs d+1 shallow, O(log d) deep | strong in the Taylor sense | Propositions 4.5, 4.6; checked |
| C6 | A product of n inputs costs at most O(n^((k−1)/k)·2^(n^(1/k))) at depth k | strong (construction) | Theorem 5.1; checked |
| C7 | That bound is tight, 2^Θ(n^(1/k)) | weak | Conjecture 5.2; one figure at n = 20, with activations outside the theorems |
| C8 | About log₁₀ n layers suffice to keep layers near 2¹⁰ wide | weak; a corollary of C7 | Eq. 6 |

## Method

*(Constructive approximation and linear-algebraic lower bounds; one
small training experiment.)*

## Concepts

- **ε-approximation**: uniform approximation on a box (−R, R)ⁿ.
- **Taylor approximation**: p is N's degree-d Taylor polynomial at 0.
- **m_k^uniform(p), m_k^Taylor(p)**: the least number of hidden neurons of
  a depth-k network that approximates p in that sense, for all ε (the
  limit of Theorem 3.4); m(p) is the minimum over k.
- **square, product and identity gates**: three neurons for x², four
  for uv ([LIT-887](../literature.d/LIT-887.md)'s), one to pass a value forward ("equivalent to the skip
  connections in residual nets").
- **sparsity c**: the number of monomials of a polynomial.

## Connections

The direct predecessor is [LIT-887](../literature.d/LIT-887.md), whose Appendix A gives the 2ⁿ case and
the sign-pattern construction used here. The tree construction and the
appeal to compositionality are Mhaskar, Liao and Poggio's and Poggio et
al.'s; the paper answers Mhaskar et al.'s question whether functions with
tight depth lower bounds must be pathological, though only for depth one.
Other cited separations (Telgarsky, Eldan and Shamir, Daniely, Montúfar et
al., Cohen, Sharir and Shashua) are not held here. The rank of the space
of partial derivatives is the standard measure for lower bounds on depth-3
arithmetic circuits (Nisan and Wigderson), unnamed in the paper. v1 also bounded m₁ below by
the symmetric tensor (Waring) rank of each homogeneous part (Proposition
II.7), dropped in v2; the dimension of partial derivatives is a lower
bound for that rank. As I recall it, not checked here, Carlini,
Catalisano and Geramita's Waring rank of a monomial over the complex
numbers omits the factor for the smallest exponent, (1/(r_min+1))∏(rᵢ+1);
if so, the paper's extra factor comes from requiring every lower-degree
term to vanish, a cost of bias-free units with nonzero low-order
coefficients rather than of the monomial. The paper notes that the TC⁰ versus TC¹ question
for Boolean circuits is independent of these real-valued results.

## Bearing on the record

- **Produces [THEORY-tmppv845](../theory.d/THEORY-tmppv845.md)**: the depth gap for polynomials is
  set by a monomial's degree in distinct variables, exponential for
  products of many inputs and absent for bounded degree; proved in the
  Taylor sense for bias-free networks.
- **[LIT-887](../literature.d/LIT-887.md) and [NOTE-688](NOTE-688.md).** Confirms and generalizes [NOTE-688](NOTE-688.md)'s C2.
  Bears on its C6 against the paper's own framing: [LIT-887](../literature.d/LIT-887.md) argues that
  natural Hamiltonians are polynomials of degree 2 to 4, and for those
  this paper's shallow cost is at most c·2⁴, so the exponential depth
  advantage it proves does not arise for the functions [LIT-887](../literature.d/LIT-887.md) calls
  natural. Depth's advantage there must come from [LIT-887](../literature.d/LIT-887.md)'s other
  argument, composition along a generative hierarchy, which this paper
  does not address. [NOTE-688](NOTE-688.md)'s first open question (a flattening cost for
  composed sufficient statistics) stays open.
- **[THEORY-195](../theory.d/THEORY-195.md), [THEORY-200](../theory.d/THEORY-200.md), [THEORY-201](../theory.d/THEORY-201.md)** (random hierarchy model). Those
  are about examples needed to learn; this is about neurons needed to
  express. Complementary, no bearing either way.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** Indirect. The exponential cost is for products of
  real-valued variables; for binary attributes a conjunction of k bits
  is one threshold unit ([LIT-887](../literature.d/LIT-887.md), Eq. 13), so a meet in an attribute
  lattice stays cheap. If attributes are continuous ([THEORY-183](../theory.d/THEORY-183.md)) and
  interact multiplicatively in co-occurrence, a direction for a high-order
  interaction would be costly for a shallow map; nothing here says
  whether co-occurrence has such terms. The connection is mine, not the
  paper's. Likewise no bearing on [CLAIM-042](../claims.d/CLAIM-042.md) or [CLAIM-119](../claims.d/CLAIM-119.md) beyond that.
- **Anthology.** Theory of deep networks' expressivity; the closing rule
  of thumb (C8) is advice on network depth, ML practice. The anthology's
  `analysis-and-evaluation` topic could hold it, hence
  `anthology-candidate` on the LIT.

## Limitations

- **The uniform lower bounds are not proved.** The proofs of Theorems 4.1
  and 4.4 say that because sup|N − p| → 0, "the coefficients of each
  E_k(x) go to 0". Uniform smallness on a box does not bound Taylor
  coefficients of a non-polynomial: ε·tanh(x/ε²), one bias-free unit, is
  within ε of 0 everywhere with first coefficient 1/ε. So Theorems 4.1(i)
  and 4.4, and Theorem 4.3(i) in its uniform form, need an argument the
  paper does not give. The Taylor-sense versions stand. I have not found
  whether the uniform claims are true.
- **No biases.** All lower bounds are for bias-free networks. A bias moves
  each unit's expansion point and an output bias makes constants free, so
  the counts are not those of standard networks; whether the exponential
  gap survives biases is not addressed.
- **Smooth σ only.** The theorems exclude ReLU; the experiment's tanh and
  ReLU both fall outside them, and the experiment presumably used biases
  (not stated). So Fig. 2 does not test the theorems.
- **Depth k is an upper bound.** The interpolation from exponential to
  linear is proved only from above.
- **Weights unbounded.** As in [LIT-887](../literature.d/LIT-887.md), fixed neuron counts are bought
  with weights scaling as δ⁻ᵈ; nothing on precision or learnability, which
  the conclusion sets aside.
- **"Natural" is a name.** Sparse high-degree products are not shown to
  be what data contain. The upper bounds of Theorem 4.1(ii) also leave
  uncounted the identity neurons needed to align chains of different
  depth.

## Open questions

- Is Theorem 4.1's uniform lower bound true? A proof would have to work
  with the closure of m-neuron networks under uniform limits; a
  counterexample would be a family of bias-free networks with fewer than
  ∏(rᵢ+1) neurons converging uniformly to the monomial.
- Does the ∏(rᵢ+1) bound survive biases?
- Conjecture 5.2: a matching lower bound for depth k ≥ 2.
- For [LIT-887](../literature.d/LIT-887.md)'s question: is there a flattening cost for functions of
  bounded degree built by composition, where this paper's degree-based
  bound gives nothing?
