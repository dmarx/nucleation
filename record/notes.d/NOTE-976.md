---
number: 976
status: Read
formerly:
- NOTE-tmpik4fl
paper: LIT-1240
title: 'Shalizi and Crutchfield — Information bottlenecks, causal states and statistical relevance bases'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:nlin/0006025v1 (16 June 2000, the only arXiv
    version), text extracted with pdftotext: all three pages, Sections
    I–VI, the five footnotes, the acknowledgements and the references. The
    note has no figures, and its few equations extracted cleanly. The
    published text (Advances in Complex Systems 5(1):91–95, 2002) was not
    compared. The arXiv comment says the note was first submitted to PRE as
    a brief report. The β → ∞ limit, which the paper calls evident, and the
    claim that every finite-β optimum factors through the causal states are
    the record's derivations, checked numerically in the scratchpad and
    written out in THEORY-743.
date: '2026-10-20'
summary: >-
  A three-page note. For memoryless transduction X → Y, the causal states
  are the cells of the partition of inputs by p(y|x). Among partitions that
  keep all information about Y, they have the least entropy. The note
  asserts, calling it evident, that these are what the information
  bottleneck delivers as β → ∞, and that Salmon's statistical relevance
  basis is the same construction. It proves neither, and it says nothing
  about the IB solutions at finite β, nor whether they nest. The record
  supplies the proof of the limit and shows that every finite-β optimum is
  a stochastic coarsening of the causal partition ([THEORY-743](../theory.d/THEORY-743.md)).
---
<!-- inactive-ok-file: THEORY-157 THEORY-163 THEORY-194 — Proposed; readings this note connects to, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1126 LIT-1238 — Deferred; works registered unread, cited as open -->
# NOTE-976: Shalizi and Crutchfield — Information bottlenecks, causal states and statistical relevance bases

## Contribution

It names a correspondence between three constructions from three
literatures, each the same object in the finite memoryless case. They are
the information bottleneck of Tishby, Pereira and Bialek ([LIT-338](../literature.d/LIT-338.md)),
computational mechanics' causal states, and Salmon's statistical relevance
basis. The object is the partition of the inputs X by their conditional
distribution p(y|x). The note proves none of the identifications. The IB
one it calls "evident", and the Salmon one it defers ("These proofs will
appear elsewhere").

## Key insight

Ask for the most compressed variable that loses nothing about Y. You get
one partition: put x and x′ together exactly when Pr(Y|X = x) =
Pr(Y|X = x′). The order of the two optimizations matters. Maximize
prediction first and then minimize size, and you get the causal states.
Minimize size first, and "the opposite sequence of optimizations … is
trivial, since it produces a single-state model". The IB's β interpolates
between the two orders, and the causal states sit at its β → ∞ end.

## Assumptions

- **Memoryless transduction.** Y depends on the current input X alone. The
  case with memory "requires a somewhat more complicated construction",
  which is not given.
- **Discrete variables, implicitly.** Entropies H[Y|ε(X)] and H[ε(X)] are
  used throughout, and footnote 3 adds the measure-zero qualification for
  uniqueness.
- **The rivals are partitions.** Eqs. (4)–(5) compare ε with other
  partitions η, η̂ of the inputs, which are deterministic functions. The IB
  allows stochastic X̃ = g(X, Ω) (footnote 1). The note does not say why a
  stochastic rival cannot beat ε in the limit. It cannot ([THEORY-743](../theory.d/THEORY-743.md)).

## Key results

- **The IB functional (1).** F = I[X̃; X] − β I[X̃; Y], minimized over
  p(x̃|x), β > 0. "As β → 0, we lose interest in prediction in favor of
  compression; whereas as β → ∞, predictive ability becomes paramount."
- **Causal states of a stationary process (2).** Histories are equivalent
  iff Pr(S→^L = s^L | past) agree for all s^L and all L. They minimize
  H[S→^L | ε(past)] for all L, and among the functions that do, they
  minimize H[ε(past)]. They are unique up to measure zero (footnote 3,
  citing Crutchfield and Shalizi 1999, [LIT-1260](../literature.d/LIT-1260.md)).
- **Memoryless transduction (3)–(5).** x ~ x′ iff Pr(Y = y|X = x) =
  Pr(Y = y|X = x′) for all y. Then H[Y|ε(X)] ≤ H[Y|η(X)] for every
  partition η, and H[ε(X)] ≤ H[η̂(X)] for every η̂ attaining the minimum
  ("it can be shown"; no proof is given).
- **The IB limit (Section IV, asserted).** The causal states "are precisely
  what should be delivered by the information-bottleneck method in the
  limit where β → ∞". The authors flag that "it is not immediately obvious
  that the iterative procedure of [1] is still valid in this limit".
- **Statistical relevance basis (Section V, asserted).** Salmon's
  construction is "identical in its essentials with that of causal states
  for memoryless transducers". "If a nontrivial sufficient partition of the
  input variables exists, then the relevance basis is the minimal
  sufficient partition."
- **Finite β (Section VI).** The bottleneck "generally throws away some
  predictive information. It trades one bit less statistical complexity for
  1/β bits less predictive information." The authors call the linear
  trade-off and the value of β "ad hoc choices".

**What the record adds** ([THEORY-743](../theory.d/THEORY-743.md), derived here, not in the paper):

- The β → ∞ claim holds in the strong sense. Fix a finite alphabet for X̃
  with at least as many symbols as causal states. Every limit point of IB
  optima as β → ∞ is the causal partition, up to relabelling and up to
  splitting a cell's label by noise independent of X.
- At every finite β, every IB optimum gives the same encoder p(x̃|x) to all
  inputs in one causal state, so X → ε(X) → X̃ is a Markov chain. The proof
  averages the encoder over a cell. That leaves p(x̃, y) unchanged, and by
  strict concavity of entropy it strictly lowers I(X̃; X) unless the rows
  were already equal. In 2,000 random encoders on a five-input example,
  averaging never raised F (largest change −1.0 × 10⁻²).
- The limit need not be reached at any finite β. Take X uniform on {0, 1}
  and Y = X through a binary symmetric channel with flip probability 0.1.
  Moving the identity encoder to a BSC(δ) lowers F for small δ at every β,
  because dI(X̃;X)/dδ → −∞ while dI(X̃;Y)/dδ stays finite. The optimal δ is
  about 1.5 × 10⁻⁴ at β = 5 and 2.3 × 10⁻⁸ at β = 10, and the gain in F is
  about 2.2 × 10⁻⁴ and 3.4 × 10⁻⁸. The plain iterative algorithm
  nevertheless converges to the identity at β ≥ 10. Its multiplicative
  updates cannot leave a zero, which is the authors' worry about the
  procedure, in a different form.
- When Y is a function of X, the limit is reached at every β > 1, and the
  trivial encoder is optimal at every β < 1. This is because
  I(X̃; X) ≥ I(X̃; Y) by data processing, so
  F ≥ (1 − β) I(X̃; Y) ≥ (1 − β) H(Y), with equality at ε.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For memoryless transduction, the causal states are the partition of inputs by Pr(Y\|X = x) | definitional | Eq. (3) |
| C2 | No partition of the inputs predicts Y better, and among those that predict as well, the causal states have least entropy | strong in substance, unproved here | Eqs. (4)–(5), "it can be shown". It is the classical fact that the minimal sufficient partition is a function of every sufficient one |
| C3 | The IB delivers the causal states as β → ∞ | asserted ("evident"); true | Section IV. Proved in [THEORY-743](../theory.d/THEORY-743.md), including against stochastic encoders, which the note does not consider |
| C4 | Salmon's statistical relevance basis is identical in essentials with the causal states for memoryless transducers, and is the minimal sufficient partition | asserted, proof deferred | Section V and footnote 5. Salmon's construction is not stated in the note |
| C5 | The IB trades one bit of statistical complexity for 1/β bits of predictive information | overstated | Section VI. True only at the margin, as the slope 1/β of the IB curve at the optimum ([NOTE-300](NOTE-300.md), eq. 35). And I(X̃; X) is the statistical complexity only for a deterministic encoder |
| C6 | Causal states suit representing a process's intrinsic structure, and the IB suits lossy compression | opinion | Section VI |

## Concepts

- **Causal state (memoryless transducer)**: an equivalence class of inputs
  x under x ~ x′ iff Pr(Y|X = x) = Pr(Y|X = x′). ε maps an input to its
  class.
- **Prescient rival**: a partition η̂ of the inputs with
  H[Y|η̂(X)] = H[Y|ε(X)]. These are the sufficient statistics of X for Y,
  as the note says ("prescient rivals … are sufficient statistics").
- **Statistical complexity**: H[ε(·)], the entropy of the causal-state
  variable.
- **Statistical relevance basis**: Salmon's construction (1971, 1984), not
  defined in the note. As Salmon gives it, it partitions a reference class
  into cells, each homogeneous for the attribute to be explained, with
  cells separated only where the attribute's probability differs. In the
  finite case that is the partition by Pr(Y|X = x), which is the note's
  point. The gloss is from Salmon's standard statement, not the note.
- **Information bottleneck**: minimize I[X̃; X] − β I[X̃; Y] over stochastic
  encoders p(x̃|x).

## Connections

It is a gloss on [LIT-338](../literature.d/LIT-338.md) (Tishby, Pereira and Bialek, posted two months
earlier), read in [NOTE-300](NOTE-300.md). [NOTE-300](NOTE-300.md)'s C6, that "almost all relevant
information can be kept at finite β", is consistent with the binary
symmetric example above: almost all, not all. The causal-state theory is
cited from [LIT-1260](../literature.d/LIT-1260.md) (read in [NOTE-978](NOTE-978.md)) and from Crutchfield and
Young (1989). The authors' later "Computational Mechanics" ([LIT-1126](../literature.d/LIT-1126.md),
unread) gives the full proofs for processes. The Salmon proofs promised
here are not in this note.

## Bearing on the record

- **[QUESTION-220](../questions.d/QUESTION-220.md).** The note says nothing about the IB at finite β:
  no solution path, no nesting, no refinement chain. Its only finite-β
  statement is C5. The record's derivation ([THEORY-743](../theory.d/THEORY-743.md)) gives part of
  an answer. Every finite-β optimum is a stochastic coarsening of the
  β → ∞ optimum, the causal partition. So nesting holds between any finite
  budget and the top one, and the IB never resolves a distinction inside a
  causal state at any β. It leaves open the question asked, whether optima
  at two finite budgets nest.
  - Two consequences for A2's proposed search. First, with Y a function of
    X the path has only two points, the trivial encoder for β < 1 and ε
    for β > 1, so it cannot show reorganization. The search needs a
    stochastic p(y|x). Second, IB optima at finite β are stochastic in
    general (the binary symmetric example), so enumerating deterministic
    encoders solves the deterministic IB, a different problem, as the
    question already notes.
  - The question's Markov-chain form of nesting, X → Z₂ → Z₁, is the right
    one, since finite-β optima are not partitions.
- **[CLAIM-152](../claims.d/CLAIM-152.md).** A direct instance. The partition is fixed only once Y is
  fixed, and the note's own remark that minimizing size first "is trivial"
  is the reason a minimality criterion picks out nothing without a target.
  Recommended as a supporting note on [CLAIM-152](../claims.d/CLAIM-152.md).
- **[THEORY-157](../theory.d/THEORY-157.md).** For finite X and Y with p(y) > 0, the causal partition is
  the classical minimal sufficient statistic of the model y ↦ p(x|y). That
  is because p(x|y)/p(x′|y) is constant in y iff p(y|x) = p(y|x′). So it is
  the FinStoch case Fritz treats, with the target Y as parameter. The note
  does not make this link (it says sufficient statistics, not models); the
  identification is the record's. Bahadur's theorem then says that a
  complete sufficient statistic, if one exists, is this partition. Nothing
  here bears on [THEORY-157](../theory.d/THEORY-157.md)'s promote_when, which concerns the
  measure-theoretic case.
- **[THEORY-194](../theory.d/THEORY-194.md).** Same family of results: what a compression keeps is fixed
  by what it must stay informative about.
- **[THEORY-668](../theory.d/THEORY-668.md)** gets nesting by restricting encoders to prunings of a
  fixed hierarchy. [THEORY-743](../theory.d/THEORY-743.md) gets nesting with the top of the
  hierarchy without that restriction.

No instruction for machine-learning practice; nothing for the anthology.
The anthology holds [LIT-338](../literature.d/LIT-338.md)'s reading for IB as practice. This note is
read here for sufficiency and for the nesting question.

## Limitations

- **C3 is asserted.** "That ε is the partition satisfying their original
  constraints is evident." The note does not distinguish the minimizers of
  the limiting problem from the limit of the minimizers. Nor does it rule
  out stochastic encoders. Both gaps close ([THEORY-743](../theory.d/THEORY-743.md)), but not
  here.
- **"The cells of the 'bottleneck' partition in the limit β → ∞"** reads
  as if IB optima were partitions. At finite β they are generally
  stochastic encoders, and the limit is a partition only up to splitting a
  cell's label by independent noise.
- **C4 is unproved.** Salmon's construction is not stated, so the
  "identical in its essentials" cannot be checked from the note. The
  qualifier "if a nontrivial sufficient partition … exists" is unexplained.
  In the finite case the minimal sufficient partition always exists, even
  when it is the identity.
- **C5** misstates a marginal rate as a global exchange rate (see the
  Claims table).
- **The transducer-with-memory construction** (Section IV's properties
  (i)–(iii)) is announced, not given.
- **The memoryless case only**, and discrete. Nothing is said about
  continuous X, where sufficiency needs the measure-theoretic care
  [THEORY-157](../theory.d/THEORY-157.md) records.

## Open questions

- Do IB optima at two finite β nest, X → Z_{β₂} → Z_{β₁}? Not addressed.
  [THEORY-743](../theory.d/THEORY-743.md) settles it only for β₂ = ∞. An example of incomparable
  optima at finite β, or a condition on p(y|x) that rules it out, would
  answer [QUESTION-220](../questions.d/QUESTION-220.md).
- How fast does the IB optimum approach the causal partition as β grows?
  In the binary symmetric example the gap in F decays like 2^(−cβ). Is
  exponential approach general when the cells' conditionals are strictly
  positive?
- Salmon's relevance basis with memory: is it the transducer causal state,
  as Section IV implies?
