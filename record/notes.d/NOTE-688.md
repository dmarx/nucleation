---
number: 688
status: Read
formerly:
- NOTE-tmp0n4ni
paper: 'LIT-887'
title: 'Why does deep and cheap learning work so well?'
version: 2
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v4 (arXiv:1608.08225v4, 3 August
    2017, dated 21 July 2017, 16 pp.), which the authors replaced "to match
    version published in Journal of Statistical Physics"; text extracted
    with pdftotext and kept as paper.txt in the scratchpad download
    directory, with a layout extraction used for the appendix equations.
    Every section, Appendix A and the reference list read. The
    multiplication gate (Eq. 11), the bit-product gate (Eq. 13), Theorem 2
    and Corollary 2 (Eqs. 17–20), the sparse-product cost (Eq. 27) and the
    counterexample discussed below checked by hand; the necessity half of
    Appendix A followed step by step, not re-derived. Figures read from
    captions and text. For the dispute, the renormalization sections and
    appendices of v1 (29 August 2016), v2 (28 September 2016) and v3 (2
    May 2017) were read and compared from their arXiv PDFs; Schwab and
    Mehta's comment on v1 (arXiv:1609.03541v1, 12 September 2016, 2 pp.)
    was read in full; and the relevant passages of LIT-882 (NOTE-683) and
    LIT-873 (NOTE-674) were taken from those readings. The publisher's
    typeset text was not read.
- version: 2
  date: '2026-10-09'
  note: >-
    Corrected: the formula for the trace under the counterexample was
    attributed to Schwab and Mehta's comment; the comment says only that
    the trace is non-constant, and the formula is this reading's. The
    comment is now held as LIT-tmp8t5lj (NOTE-tmpgcp7r).
date: '2026-10-09'
summary: >-
  Argues that cheap networks suffice because physical data have low-order,
  local, symmetric Hamiltonians, and that depth pays because inference must
  compose the sufficient statistics of a Markov generative hierarchy;
  proves that one hidden layer needs exactly 2^n neurons to multiply n
  inputs. On renormalization it is right that a coarse-graining needs a
  stated target, and its early appendix shows that neither a matched
  partition function nor the exact trace condition supplies one; it is
  wrong that the target must come from supervision.
---
<!-- inactive-ok-file: THEORY-202 THEORY-197 THEORY-194 THEORY-201 THEORY-195 THEORY-186 THEORY-185 QUESTION-025 — Proposed or open; cited as what this reading produced, the accounts it is set beside, and the question it bears on -->

# NOTE-688: Why does deep and cheap learning work so well?

## Contribution

It gives a physicist's answer to two questions about neural networks:
why networks with few parameters approximate the functions people care
about, and why deep networks do so more efficiently than shallow ones. The
first answer is constructive: products, and so polynomials, cost a fixed
small number of neurons, and the Hamiltonians of physics are low-order,
local and symmetric polynomials. The second is that data are produced by a
Markov chain of generative steps, so the optimal inference is a
composition of level-wise sufficient statistics, and compositions can be
exponentially costly to flatten; it proves one such cost exactly, 2^n
neurons for an n-fold product in one hidden layer. It also places the
renormalization group as information distillation toward a specified
target, and disputes that RG is unsupervised learning.

## Key insight

A small network can express a function from an astronomically large class
only if the function is special, and the specialness of data is inherited
from the process that made them: few parameters per step, low-order
couplings, locality, symmetry, and a chain of steps. Inference that undoes
such a chain inherits its depth. The same lens makes renormalization a
case of distillation, which is defined only relative to what is to be
predicted.

## Assumptions

- **Expressibility and efficiency only.** Learnability (whether training
  finds the networks shown to exist) is explicitly set aside.
- **Smooth activations** with nonzero Taylor coefficients where needed:
  σ''(0) ≠ 0 after a bias shift for the product gate; σₖ ≠ 0 for 0 ≤ k ≤ n
  for the 2^n lower bound. ReLU, whose higher Taylor coefficients vanish,
  is not covered by either.
- **"Approximate" in the no-flattening theorem** means that the network's
  output and the product have identical Taylor expansions at the origin up
  to degree n (Eq. A1), with inputs scaled down and outputs scaled up;
  accuracy ε → 0 is bought with weights that grow without bound, so "fixed
  size" counts neurons, not weight magnitude or precision. The hidden
  units in Eq. A1 carry no biases.
- **Generative hierarchy.** Data x = yₙ come from a Markov chain y₀ → y₁
  → … → yₙ (Eqs. 15–16); non-Markov steps are absorbed by enlarging the
  state. The authors note this "technically covers essentially all data"
  but "may be an inefficient description", which concedes that the
  assumption alone has no content.
- **Linear no-flattening** counts nonzero weights (synapses) of linear,
  bias-free networks at zero error; neuron counts are trivial there.
- **Notation.** y is the parameter or class and x the data (Fig. 1), but
  Section III, the caption of Fig. 3 and Section III D slip to yₙ = y and
  ŷₙ ≡ y where x is meant; and "their first few Cₖ" in Section III E is
  left over from an earlier draft. The arguments survive the slips.

## Key results

- **Product gate** (Eq. 11; Fig. 2). [σ(u+v) + σ(−u−v) − σ(u−v) −
  σ(−u+v)]/(4σ₂) = uv[1 + O(u² + v²)]; checked: σ(a) + σ(−a) = 2σ₀ +
  σ₂a² + O(a⁴), so the numerator is σ₂[(u+v)² − (u−v)²] = 4σ₂uv plus
  fourth-order terms. Four
  hidden neurons, exact in the limit of scaling A₁ → λA₁, A₂ → λ⁻²A₂.
  Corollary: any multivariate polynomial is approximated to any ε by a
  network whose neuron count is about four per multiplication, independent
  of ε.
- **Bit products** (Eq. 13). ∏_{i∈K} xᵢ = lim_{β→∞} σ(−β(k − ½ − Σ_{i∈K}
  xᵢ)); β > D ln 10 gives D correct decimals. So any function of n bits is
  a three-layer network with one hidden unit per monomial of its
  Hamiltonian, at most 2^n.
- **Parameter counts under priors** (Section II D). Degree d ≤ 4 gives
  O(n⁴) coefficients; nearest-neighbour locality makes the count linear in
  n and caps the degree of a binary Hamiltonian by the coordination
  number; a quadratic, local, translation-invariant 1D Hamiltonian has
  three parameters. Translation-invariant linear maps are convolutions.
- **Theorem 2 and Corollary 2** (Eqs. 17–20). If Tᵢ is a minimal
  sufficient statistic of P(yᵢ | yₙ), then Tᵢ = fᵢ ∘ Tᵢ₊₁ for some fᵢ, and
  P(y₀ | yₙ) = (f₀ ∘ f₁ ∘ … ∘ fₙ)(yₙ). Checked: the backward Markov
  property makes P(yᵢ | yₙ) depend on yₙ only through Tᵢ₊₁(yₙ), so Tᵢ₊₁ is
  sufficient for yᵢ and minimality gives fᵢ.
- **Renormalization as distillation** (Section III E; Eqs. 23–24). For a
  translation- and rotation-invariant quadratic field Hamiltonian
  ∫[y₀φ² + y₁(∇φ)² + y₂(∇²φ)² + …], b × b block averaging sends yᵢ to
  b^(2−2i) yᵢ, so terms with i ≥ 2 die away: "relevant operators" are
  "signal" and irrelevant ones "noise". "Contrary to some claims in the
  literature, effective field theory and the renormalization group have
  little to do with the idea of unsupervised learning and pattern-finding";
  RG is "essentially a feature extractor for supervised learning". A
  footnote grants MERA as an unsupervised variational ansatz whose
  solution is an RG flow, "only possible due to the extra mathematical
  structure".
- **Linear no-flattening** (Section III G). FFT: Cₛ = O(n/log n). Matrix
  multiplication by a fixed matrix via Strassen-type algorithms: Cₛ ≥
  n^0.627 at ω ≈ 2.373. A rank-k n × n map: Cₛ = n/2k. Product of two
  random sparse n × n 0/1 matrices of density p: Cₛ = [1 − (1 − p²)ⁿ]/2p
  (Eq. 27), approaching 1/2p for n ≫ 1/p²; checked.
- **Polynomial no-flattening** (Section III H; Appendix A). With σₖ ≠ 0
  for k ≤ n, 2^n hidden neurons suffice and are necessary in a single
  hidden layer to multiply n inputs: sufficiency by summing σ(Σ sᵢxᵢ) over
  all sign patterns with weights ∏sᵢ, which cancels every monomial
  missing a variable; necessity by showing the 2^n × m matrix of products
  of first-layer weights over subsets has full row rank. A binary tree of
  four-neuron gates needs about 4n (160 neurons against 2³² for n = 32).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Four hidden neurons with any smooth nonlinearity approximate uv arbitrarily well; hence every polynomial is approximated by a network whose neuron count does not grow as ε → 0 | strong, with weights that grow without bound | Eq. 11, corollary; checked |
| C2 | One hidden layer needs exactly 2^n neurons to multiply n inputs, a deep tree about 4n | strong, in the Taylor-matching sense, for smooth σ with σₖ ≠ 0, depth one only | Appendix A proof |
| C3 | Linear networks have no-flattening costs: FFT, fast matrix multiplication, low rank, sparse products | strong (elementary counts; the Strassen case rests on known algorithms) | Section III G; Eq. 27 checked |
| C4 | For a Markov generative chain, the minimal sufficient statistics compose, so optimal inference is a composition of level-wise distillers | strong, and close to immediate | Theorem 2, Corollary 2; checked |
| C5 | Deep networks beat shallow ones on real data because real data come from such hierarchies whose steps are each cheap | weak | C4 plus examples (CMB pipeline, a contrived cat/dog generator); neither cheapness of each fᵢ nor a flattening cost for the composition is shown |
| C6 | Physics favours low-order, local, symmetric Hamiltonians, and this is why cheap networks work on natural data | weak | argument and examples; conceded not to survive marginalization or arbitrary transformation |
| C7 | Renormalization is information distillation toward a specified target; a coarse-graining is accurate only relative to the variables one wants | moderate | the Gaussian toy, the EFT argument; in v1–v2 also the appendix counterexample |
| C8 | RG is a case of supervised, not unsupervised, learning | weak, and too strong as stated | definitional; contradicted in effect by [LIT-873](../literature.d/LIT-873.md) (see below) |

## Method

*(Constructive approximation and elementary proofs; no experiments.)*

## Concepts

- **cheap learning**: approximating a function with exponentially fewer
  parameters than a generic member of its class needs; the "swindle"
  replaces vⁿ by v × n.
- **Hamiltonian**: Hᵧ(x) ≡ −ln p(x|y), the surprisal; p(y|x) is then a
  softmax of −H − µ with µᵧ ≡ −ln p(y) as the bias (Eq. 8).
- **information distiller**: a (nearly) sufficient statistic, retaining
  the mutual information with the target that the data processing
  inequality allows.
- **flattening cost**: Cₙ and Cₛ (Eqs. 25–26), the factor by which the
  best network with fewer hidden layers, within error ε, increases the
  neuron or synapse count; a **no-flattening theorem** shows it exceeds 1.
- **renormalization** (Section III E): a coarse-graining R whose
  Hamiltonian keeps its functional form with changed parameters, so that
  it can be iterated; read as a feature extractor whose features are
  long-wavelength quantities.

## Connections

Its no-flattening results continue Delalleau and Bengio, Mhaskar, Liao and
Poggio (compositional functions), Telgarsky and Eldan and Shamir (depth
separations), and Poole, Raghu et al. (expressivity in random networks);
none is held here. The linear-network setting is Saxe, McClelland and
Ganguli's (2013), whose 2019 sequel is held ([LIT-862](../literature.d/LIT-862.md), [THEORY-186](../theory.d/THEORY-186.md)). The
sufficient-statistic view of a hierarchy is Fisher's, and its
information form is the data processing inequality ([LIT-338](../literature.d/LIT-338.md)'s bottleneck
is the same distillation with a rate penalty). Rolnick and Tegmark's
sequel on deeper networks for natural functions (arXiv:1705.05502) is not
held.

## The dispute with [LIT-882](../literature.d/LIT-882.md) and [LIT-873](../literature.d/LIT-873.md), on all three texts

**What this paper says, by version.**

- **v1 (29 August 2016)**, Lin and Tegmark. Section III E: renormalization
  is "a special case of supervised learning, not unsupervised learning",
  and Appendix A constructs "a counter-example to a recent claim [Mehta
  and Schwab] that a so-called 'exact' RG is equivalent to perfectly
  reconstructing the empirical probability distribution". The
  counterexample: for any H(y) and any non-constant K(y), the joint
  Hamiltonian H(y, y′) = H(y) + H(y′) + K(y) + ln Z̃, with Z̃ = Σ_y
  e^{−H(y)−K(y)}, has Z_tot = Z, yet its marginal e^{−H−K}/Z̃ is not
  p(y). I checked both lines. Since all derivatives of ln Z can be made to
  agree as well, an RG that reproduces every macroscopic observable "can
  fail to accomplish any sort of unsupervised learning".
- **Schwab and Mehta's comment** (arXiv:1609.03541, 12 September 2016)
  agrees that preserving the free energy does not recover the
  distribution, says they "never claimed otherwise", calls the "if and
  only if" of their Eq. 8 a typo, and shows that the counterexample
  violates the trace condition Tr_h e^{T(v,h)} = 1, which it says is
  non-constant there (by this reading's computation, Tr_{y′} e^T =
  Z e^{−K(y)}/Z̃). So it does not touch their
  Eq. 22.
- **v2 (28 September 2016)** keeps the counterexample, records the
  response, and adds the point that matters: even the trace condition is
  not enough to call something renormalization, since "any two systems
  that do not interact with each other will trivially satisfy their trace
  condition", so "a cat in a thermal bath is a renormalized dog".
  Renormalization needs a prescription for which features are relevant,
  which in physics comes from user-specified parameters such as field and
  temperature and in unsupervised learning is by definition absent. It
  also notes that what the variational step minimizes is still the
  mismatch in Z, not the violation of the trace condition.
- **v3 (March 2017, adding Rolnick) and v4, the journal text**, drop the
  appendix and the explicit target. Mehta and Schwab are cited once ("it
  also helps understand the relation between deep learning and
  renormalization") and among five works where "there are significant
  misconceptions"; none is named. The section ends: "calling some
  procedure renormalization or not is ultimately a matter of semantics;
  what remains to be seen is whether or not semantics has teeth".

**Assessment.**

- **Against [LIT-882](../literature.d/LIT-882.md)'s mathematics the paper lands one blow, on a typo.**
  The v1 counterexample is correct and refutes Eq. 8's biconditional,
  which [NOTE-683](NOTE-683.md) also found wrong. It does not touch Eqs. 18–22, which use
  the pointwise trace condition, and Schwab and Mehta's reply on that is
  right. Two consequences for the record: the weakness of Eq. 8 was
  conceded by its authors in 2016, and [NOTE-683](NOTE-683.md)'s free-energy point
  (under the identification, ΔF measures only Z_λ against Z) was made in
  substance in v2 ("what is minimized in the variational step is still
  the mismatch in Z"); [NOTE-683](NOTE-683.md) marks it as in neither of the two papers
  it read, which is true of those two only.
- **The v2 point holds and goes past [THEORY-197](../theory.d/THEORY-197.md).** Under Mehta and
  Schwab's own identification, take E(v, h) = H(v) + H′(h) + ln Z′ with
  Z′ = Tr_h e^{−H′}: then T = −H′(h) − ln Z′, the trace condition holds for
  every v, the visible marginal is the data exactly, and the coarse
  Hamiltonian is H′, which has nothing to do with the system. Mehta and
  Schwab say the identity holds for any Boltzmann machine, so this is
  inside its scope. [THEORY-197](../theory.d/THEORY-197.md) says the correspondence has content only at
  the exact point; this shows the exact point does not select a
  coarse-graining either. (For a restricted Boltzmann machine proper, with
  only bilinear couplings and visible biases, W = 0 gives a product
  marginal and so cannot be exact on interacting data; the cat-and-dog
  construction needs visible–visible terms. That narrows the example, not
  the point: exactness constrains the visible marginal and leaves the
  hidden variables' meaning free.) Filed as [THEORY-202](../theory.d/THEORY-202.md).
- **Its thesis that renormalization needs a stated target is right and is
  what the other two converge on.** Mehta and Schwab concede that short
  of exactness the two use "distinct variational approximation schemes";
  Koch-Janusz and Ringel show the objective decides which variables are
  kept ([THEORY-194](../theory.d/THEORY-194.md)). Lin, Tegmark and Rolnick said so first and most
  generally, but showed it only on a Gaussian toy where the answer is
  textbook.
- **Its conclusion that RG is supervised, not unsupervised, does not
  hold.** [LIT-873](../literature.d/LIT-873.md)'s RSMI uses no labels: the coarse variable of a block is
  chosen to be informative about the environment beyond a buffer, a target
  taken from the data's own spatial structure, and it recovers block spins
  and dimer fields and an Ising flow. That is exactly the "prescription
  for what features are relevant" v2 says unsupervised learning lacks;
  locality supplies it. So the dichotomy is wrong; the correct claim is
  that a coarse-graining is renormalization relative to a relevance
  target, and the target may come from labels, from user-chosen
  parameters, or from structure such as distance. The MERA footnote
  already concedes one unsupervised route. Koch-Janusz and Ringel's own
  gloss, that the denial "holds only for" distribution-fitting
  objectives, is the fair reading.
- **The word "denies" overstates it.** [LIT-873](../literature.d/LIT-873.md) and [LIT-882](../literature.d/LIT-882.md)'s Standing
  describe this paper as denying a link between RG and deep learning. It
  denies one between RG and unsupervised distribution fitting, and
  asserts one between RG and supervised feature extraction, and between
  hierarchical distillation and depth. The journal text, by ending on
  "semantics", denies less than v1 did.
- **Verdict.** Of the three, this paper is right on the narrowest and most
  important point (no condition on preserving the distribution or its
  partition function makes a coarse-graining a renormalization; a
  relevance target must be given), wrong on where the target can come
  from, and weakest on evidence: it ran no network on any lattice model.
  The published version withdrew the part of its argument that was
  checkable against [LIT-882](../literature.d/LIT-882.md).

## Bearing on the record

- **Produces [THEORY-202](../theory.d/THEORY-202.md)**: neither a matched partition function nor
  the exact trace condition makes a coarse-graining a renormalization.
  Sources: this paper's v1–v2 appendix, and [LIT-882](../literature.d/LIT-882.md) for the identity under
  which the trace condition is a perfect fit.
- **[THEORY-197](../theory.d/THEORY-197.md)** ([LIT-882](../literature.d/LIT-882.md)). Supported, and extended by [THEORY-202](../theory.d/THEORY-202.md)
  as above. Its "the paper's Eq. 8 … is too strong" was conceded by Mehta
  and Schwab in their 2016 comment, which the record may wish to cite; its
  free-energy point was anticipated in v2 here.
- **[THEORY-194](../theory.d/THEORY-194.md)** ([LIT-873](../literature.d/LIT-873.md)). Supported on its general claim, that what a
  compression keeps is set by what it must stay informative about, which
  is this paper's C7. This paper does not bear on [THEORY-194](../theory.d/THEORY-194.md)'s mutual
  information criterion, and [THEORY-194](../theory.d/THEORY-194.md) refutes this paper's C8.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** Indirect. The hierarchy here is a causal chain of
  generative steps, not attributes that imply or exclude one another; no
  co-occurrence, PMI or lattice. Two things carry over. (i) Theorem 2 is
  the general reason a top-level variable is reached by composing
  level-wise statistics: nothing says it is a linear function of the raw
  data, and that agrees with Cagnetta and Wyart's remark ([LIT-883](../literature.d/LIT-883.md),
  [THEORY-201](../theory.d/THEORY-201.md)) that a parent is not a linear feature of its input tuple
  until after a nonlinear layer, and with the random hierarchy model's
  need for depth ([LIT-877](../literature.d/LIT-877.md), [THEORY-195](../theory.d/THEORY-195.md)). A derivation for [QUESTION-025](../questions.d/QUESTION-025.md)
  would have to say whether a co-occurrence embedding, being one linear
  map of one statistic, can stand in for that composition. (ii) For
  binary attributes, a conjunction of k bits is one threshold unit (Eq.
  13), so if attributes are thresholded linear directions, a concept's
  extent, the meet of its attributes, is one threshold unit over the
  attribute indicators, an intersection of the attributes' half-spaces in
  the embedding; nothing here bars a non-Boolean lattice from being read
  that way. Both are my
  connections, not the paper's.
- **[THEORY-186](../theory.d/THEORY-186.md)** (Saxe et al.). The linear no-flattening results are about
  cost, not about learned directions; no bearing on its tree wavelets.
- **Anthology.** A theory of why deep networks work, with no practice
  instruction; the anthology's `analysis-and-evaluation` topic could hold
  it, hence `anthology-candidate` on the LIT.

## Limitations

- **The physics priors are argued, not tested.** No measurement shows that
  the Hamiltonians of images, sounds or text are low-order or local, and
  the authors concede that marginalizing or transforming variables
  destroys both, which is the usual situation for observed data.
- **The depth argument has a gap between its theorem and its claim.**
  Theorem 2 is nearly immediate and holds for any Markov chain, including
  ones whose statistics are expensive; the paper neither shows that each
  fᵢ is cheap nor that the composition of minimal sufficient statistics
  is costly to flatten. The no-flattening results are for products and
  linear maps, not for that composition.
- **The 2^n bound is narrow.** One hidden layer, smooth σ with all low
  Taylor coefficients nonzero, approximation in the Taylor-matching sense
  near the origin with unbounded weights. It says nothing about depth two,
  about ReLU, or about uniform approximation on a bounded domain; the
  authors' comparison to TC⁰ concedes the depth-one restriction.
- **"Fixed size" hides precision.** The ε-independent neuron counts are
  bought with weights that scale as λ² → ∞; the paper notes that SGD
  cannot reach arbitrarily large weights.
- **The RG section is a toy.** One Gaussian field with textbook scaling;
  no lattice model, no trained network, no comparison with [LIT-882](../literature.d/LIT-882.md)'s
  experiment. Its strongest argument was cut from the published version.
- **Slips.** The y/x reversal in Section III and Fig. 3; "Cₖ" left over
  from an earlier draft; "course-graining"; Eq. 12's cross term written
  hᵢⱼxᵢyⱼ.

## Open questions

- Is there a lower bound on flattening the composition of minimal
  sufficient statistics of a Markov chain under stated conditions on the
  steps, rather than for products? That would turn C5 into a theorem.
- Within Kadanoff's kernel families, where each hidden spin is coupled to
  a block by a kernel of fixed form, does the trace condition force the
  coarse Hamiltonian to keep the relevant operators? If so, the cat-and-dog
  objection applies only to kernels outside those families, and the
  dispute narrows to which family training searches.
- When the relevance target comes from structure rather than labels, as
  in [LIT-873](../literature.d/LIT-873.md), what structure suffices outside lattices, for instance for
  co-occurrence data where "distance" is not given?
