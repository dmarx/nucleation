---
number: 728
status: Read
formerly:
- NOTE-tmpafm8e
paper: LIT-1035
title: 'Brémaud & Massoulié — Stability of nonlinear Hawkes processes'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the publisher's typeset PDF (Annals of Probability
    24(3), pp. 1563–1588, 26 pp.), which Project Euclid serves open access
    (OpenAlex and Unpaywall: bronze, publishedVersion). Project Euclid's
    bot protection refused direct requests from this environment, so the
    copy was the Internet Archive's capture of that same Project Euclid
    PDF URL (web.archive.org/web/20260425231255/https://projecteuclid.org/journals/annals-of-probability/volume-24/issue-3/Stability-of-nonlinear-Hawkes-processes/10.1214/aop/1065725193.pdf).
    The page range 1563–1588 is printed on the first page. Text extracted
    with pdftotext; the extraction loses absolute-value bars and the
    symbol Λ, so the statements of Theorems 1, 2, 3, 4 and 7 were checked
    against page images. Read: all six sections, every theorem, lemma,
    remark and proof, and the reference list. Nothing skipped. Hawkes
    (1971, LIT-1036) and Hawkes & Oakes (1974, LIT-1028), whose
    results this paper generalizes, were not read, so what it says they
    proved is its account of them. Every quotation below was checked
    against the extracted text by script, with whitespace normalised.
date: '2026-10-13'
summary: >-
  Sufficient conditions for a Hawkes process with a nonlinear rate function
  to have a unique stationary version and for any suitably started version
  to converge to it, in distribution or in variation. The main conditions
  are a Lipschitz rate function with Lipschitz constant times the kernel's
  absolute mass below one (a spectral radius below one for a network), or a
  bounded Lipschitz rate with no limit on the kernel's size. Kernels may be
  negative, so inhibition is allowed. Kernels are fixed in time, the
  conditions are sufficient and not necessary, and nothing is said about
  cascade sizes or about what happens past the threshold.
---
<!-- inactive-ok-file: LIT-1036 LIT-1028 — Unavailable, no lawful full text found; the linear results this paper generalizes, described as it describes them -->
<!-- inactive-ok-file: QUESTION-091 CLAIM-163 CLAIM-286 — Proposed or open; the codes this reading was filed for, tested and not settled -->

# NOTE-728: Brémaud & Massoulié — Stability of nonlinear Hawkes processes

## Contribution

Hawkes and Oakes had proved existence, uniqueness and stability for the
linear, excitatory Hawkes process, with arguments "where the linearity of φ
is crucial". This paper drops linearity and the sign restriction on the
kernel. The rate becomes φ(∫h(t−s)N(ds)) with φ nonnegative and h of either
sign, and the paper gives conditions under which a stationary version exists,
is unique, and attracts versions started from a given past. Because "both
types of arguments (linear or branching) are not available in the generality
we have placed the problem", the proofs use stochastic intensities, Poisson
embedding (thinning) and coupling instead of the cluster representation.

## Key insight

What makes a self-exciting process settle is not that it is linear or
excitatory but that its rate is a contraction of its past. If φ moves by at
most α per unit of input, and the kernel's total absolute weight is h, then
α∫|h| < 1 makes each pass of the past through the dynamics shrink
differences, and a Picard-style iteration converges to the one stationary
regime. In the linear excitatory case this is exactly the branching ratio
being below one. And if φ is bounded, no such limit on the kernel is needed
at all: a bounded rate cannot run away.

## Assumptions

- **Simple point processes on the whole real line**, with an
  F_t-intensity λ(t) = φ(∫_(−∞,t) h(t−s) N(ds)) (eq. 1), φ: ℝ → ℝ⁺,
  h: ℝ⁺ → ℝ. The multivariate form (eq. 2) has one φ_i per component and a
  kernel h_ji from j to i, with no common points.
- **Time-invariant kernels and rate functions.** h and φ do not change with
  time or state beyond the dependence written in eq. 1. Nothing in the
  paper covers kernels that are themselves modulated.
- **No marks**, except a remark in the conclusion that independent marks
  are a straightforward extension (worked out in Massoulié's thesis, not
  here).
- **Stability** is the paper's own term (Definition 1): a stationary
  solution exists, and versions started from a past satisfying a stated
  initial condition converge to it in distribution or in variation. "Our
  use of the term stability in the title of this article does not seem to
  be standard in the theory of stochastic processes."
- **Uniqueness is among stationary solutions with finite average
  intensity** (Theorems 1 and 7). Remark 6 notes that if φ(0) = 0 the empty
  process is a solution.
- **All conditions are sufficient.** No theorem gives a necessary
  condition, and none describes the process when the conditions fail.

## Key results

Notation: α is a Lipschitz constant of φ, Λ a bound on the rate.

- **Theorem 1 (unbounded Lipschitz dynamics).** If φ is α-Lipschitz and
  α∫_ℝ⁺ |h(t)| dt < 1: (a) there is a unique stationary distribution with
  finite average intensity; (b) the dynamics are stable in distribution
  from any past whose direct influence on the future vanishes (initial
  conditions (i) or (ii), in a.s. or in mean); (c) if also
  ∫ t|h(t)| dt < ∞, they are stable in variation from any past whose total
  direct influence ∫ dt ∫_(−∞,0) |h(t−s)| N(ds) is a.s. finite (iii).
  *Holds when:* φ Lipschitz, h of either sign. The paper calls it "a strict
  generalization" of Hawkes and Oakes, whose linear case is φ(x) = ν + x,
  ν > 0, h ≥ 0, ∫h < 1, with stability proved only from an empty past.
- **Remark 6.** With φ(0) = 0 and ∫h < 1 in the linear case, there is no
  stationary process except the empty one, and any transient process
  "eventually dies out in distribution or in variation". A self-exciting
  process below threshold needs an immigrant rate (ν > 0) to persist.
- **Theorem 2 (bounded Lipschitz dynamics).** If φ is α-Lipschitz and
  bounded by Λ, ∫|h| < ∞ and ∫ t|h(t)| dt < ∞, there is a unique stationary
  distribution, and the dynamics are stable in variation from any past
  whose influence on the far future tends to zero (eq. 5). There is no
  condition on the size of h. "at the expense of a boundedness condition"
  the L¹ limit is avoided. A steep ramp approximating a threshold is
  covered; the pure threshold is not: "Strictly speaking, however, this
  limiting case is not in the scope of Theorem 2." The authors note that
  Kerstan (1964) had this result: "Our Theorem 2 is therefore of the same
  generality as the corresponding result of Kerstan, but does not contain
  more."
- **Theorem 3 (bounded memory dynamics).** If the rate depends only on the
  last A time units of the past and is bounded by Λ, there is a unique
  stationary distribution, stability in variation holds "irrespective of
  the initial condition", and convergence is exponentially fast. Compactly
  supported kernels give bounded memory. The proof uses the gaps longer
  than A in a dominating Poisson process of rate Λ as regeneration points.
- **Theorem 4 (increasing kernel).** If φ is nonnegative, nondecreasing,
  left-continuous and φ(x) ≤ λ + αx, and h ≥ 0 with α∫h < 1, a stationary
  process exists. No Lipschitz condition. Existence only: "it is not clear
  whether the stationary law for N is unique" (Remark 7). The construction
  gives the smallest stationary solution, and the largest when φ is
  continuous.
- **Theorem 5.** The multivariate form of Theorem 3: bounded rates with
  bounded memory give a unique stationary law, stable in variation from any
  past, exponentially fast.
- **Theorem 6 (two neurons, monotone).** For two components with bounded
  nondecreasing φ_i, nonnegative self-kernels, and cross-kernels that are
  both excitatory or both inhibitory, a stationary law exists. Existence
  only. Remark 9 extends this to K components split into two groups,
  excitatory within groups and inhibitory between them.
- **Theorem 7 (multivariate Lipschitz).** If each φ_i is α_i-Lipschitz and
  the K × K matrix A with entries a_ij = α_i ∫_0^∞ |h_ji(t)| dt has spectral
  radius strictly below one, there is a unique stationary law with finite
  average intensity, stable in distribution under (i′) or (ii′), and in
  variation under ∫ t|h_ji(t)| dt < ∞ and (iii′). The paper calls this "a
  strict extension of Hawkes and Oakes [7] results on linear mutually
  exciting point processes."
- **Theorem 8 (multivariate bounded Lipschitz).** Bounded α_i-Lipschitz φ_i
  and integrable kernels with ∫ t|h_ij(t)| dt < ∞ give a unique stationary
  law, stable in variation from any past whose far-future influence
  vanishes (eq. 39). Again no condition on the size of the kernels.
- **Examples.** An M/D/K/0 loss queue (Example 1); threshold neurons, in
  which "Multivariate Hawkes processes also model neuronal activity and we
  shall therefore occasionally call them neural networks" (Example 2); and a
  network in which any recent spike silences a neuron (Example 3), which
  Theorem 7 covers because potentials are integer-valued (Example 5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Lipschitz φ, signed h, α∫\|h\| < 1 give a unique stationary law (finite mean intensity), stable in distribution, and in variation with a first-moment condition on h | strong | Theorem 1, proved |
| C2 | Bounded Lipschitz φ gives a unique stationary law, stable in variation, with no limit on the size of h | strong | Theorem 2, proved (and Kerstan 1964) |
| C3 | Bounded rate with bounded memory gives a unique stationary law and exponentially fast convergence from any past | strong | Theorem 3 and Theorem 5, proved |
| C4 | Monotone φ with linear growth and h ≥ 0, α∫h < 1, gives a stationary law; uniqueness open | strong (existence only) | Theorem 4, proved; Remark 7 |
| C5 | For networks, a spectral radius below one of the matrix α_i∫\|h_ji\| suffices for a unique, stable stationary law | strong | Theorem 7, proved |
| C6 | Mixed excitation and inhibition with monotone bounded φ admits a stationary law when cross-connections are sign-structured | strong (existence only) | Theorem 6, proved for two components; Remark 9 sketches K |
| C7 | The linear-case proofs depend on linearity, and the branching argument does not reach the nonlinear signed case | moderate | stated in §2, not proved as an impossibility |

## Method

- **Poisson embedding.** A process with intensity λ(t) is built as the
  points of a homogeneous Poisson process on ℝ² lying under the curve
  t ↦ λ(t) (Lemma 3), or by thinning a rate-Λ Poisson process (Lemma 2).
  Lemma 4 runs the other way: every process with a predictable intensity
  can be embedded so.
- **Iteration.** Start from λ⁰ ≡ 0, feed each process into eq. 1 to get the
  next. Under the Lipschitz condition the expected differences shrink
  geometrically (Theorem 1, eq. 16; Theorem 7, eq. 35, with the matrix A),
  "analogous in some way to Picard’s existence proof for ordinary
  differential equations". Under monotonicity the iterates increase
  (Theorem 4).
- **Coupling.** The stationary and the transient process are built from
  the same Poisson process, and convergence in variation is shown by their
  coinciding after an a.s. finite time (Lemma 5).

## Concepts

- **Nonlinear Hawkes process.** A point process with intensity
  φ(∫h(t−s)N(ds)). Hawkes's process is the case φ(x) = ν + x with h ≥ 0.
- **Excitation function φ, transfer function h.** The paper's names, from
  the neural reading. h_ji is the transfer function from j to i.
- **Initial condition.** A property of the past N restricted to (−∞, 0),
  typically that its direct influence on the future vanishes or sums to a
  finite amount.
- **Stability in distribution / in variation.** Convergence of the shifted
  future to the stationary process, weakly or in total variation.
- **Bounded memory.** The rate depends on the past only through the last A
  time units.

## Connections

It generalizes Hawkes (1971; [LIT-1036](../literature.d/LIT-1036.md)) and Hawkes and Oakes (1974;
[LIT-1028](../literature.d/LIT-1028.md)), both unread here. By its account, Hawkes and Oakes proved
existence by "constructing the corresponding stationary point process as a
Poisson branching process or cluster Poisson process", and uniqueness and
stability from an empty past. Its Theorem 2 is Kerstan's (1964) result with
a shorter proof. Theorems 3 and 5 follow from Lindvall (1988) and the
authors' own earlier work on random memory. The constructions are those of
Lewis and Shedler (1976) and Ogata (1981) for simulation.

## Bearing on the record

**On [QUESTION-091](../questions.d/QUESTION-091.md): the formal half of the question has a precise form
here, and the empirical half is untouched.**

- The record's question asks whether the allocation of influence moves
  cascades nearer to or further from criticality, "as a branching ratio
  would show". For the linear excitatory case the branching ratio below one
  is Theorem 1's condition with α = 1. For a network it is Theorem 7's
  spectral radius. So the quantity the question names is the stability
  margin of a known theorem.
- For the exchange's model, with signed kernels and a nonlinear rate, the
  same matrix with |h_ji| and the Lipschitz constants gives a *sufficient*
  condition. It is not a branching ratio. The process has no cluster
  representation in general (the paper says the branching argument is not
  available), and inhibition enters through |h|, so it counts toward
  instability in the bound, not against it. The spectral radius of this
  matrix being near one does not mean the process is near anything; the
  bound may be loose.
- **Bounded rates have no threshold.** Theorems 2, 3, 5 and 8 give
  stability for any kernel size once φ is bounded. If the processes in the
  record's model have saturating influence, as any psychological rate
  plausibly does, then "distances from criticality" has no meaning supplied
  by these results. A question about distances from criticality needs an
  unbounded or effectively unbounded regime, and the record should say
  which it assumes.
- **The kernels here are fixed.** The question and A6's hypothesis are
  about an influence canvas that changes the kernels. Nothing in this paper
  covers kernels that vary with time or with state. A slowly varying
  kernel could be treated as a sequence of fixed regimes, and the paper's
  general initial conditions are meant for that: "such general conditions
  are needed to take into account the previous behavior of the system
  before a change in the parameters". But a kernel that the process itself
  modulates is a different model, and its stability is not proved here.

**On [CLAIM-163](../claims.d/CLAIM-163.md): a Hawkes model supplies a coupling and a control parameter,
not an order parameter, and not for valuations.**

- [CLAIM-163](../claims.d/CLAIM-163.md) asks for a coupling, an order parameter and transitions. In a
  multivariate Hawkes model the coupling is explicit: the kernels h_ji by
  which events of one component change another's rate.
- The spectral radius of A is a function of the couplings and the rate
  functions. It is a *control* parameter, set before the dynamics run. An
  order parameter is a collective variable read off the state (the
  relative phase, in [CLAIM-163](../claims.d/CLAIM-163.md)'s own example). Of the paper's quantities,
  the stationary average intensity is the nearest thing, and the paper
  only bounds it (Theorem 4's proof). So the record's wording in
  [QUESTION-091](../questions.d/QUESTION-091.md), that "the branching ratio is the coupling and order
  parameter", runs the two together.
- Transitions: the paper proves results only on the stable side. It says
  nothing about what happens at or past spectral radius one, and Theorem 2
  shows that a bounded rate removes the transition altogether. So it does
  not supply [CLAIM-163](../claims.d/CLAIM-163.md)'s third part.
- The coupling is between streams of events, not between an agent's
  valuations, and it is excitation, not phase-locking. So a Hawkes model
  could meet [CLAIM-163](../claims.d/CLAIM-163.md)'s demand for cascades of activity, as the QUESTION
  says, and does nothing for the synchronization reading the claim is
  about. It neither supports nor weakens [CLAIM-163](../claims.d/CLAIM-163.md).

**On [CLAIM-286](../claims.d/CLAIM-286.md).** The thesis needs models with signed, mixed
interactions among many processes to be well posed. Theorems 6 and 7 show
that some such models are: with Lipschitz or monotone bounded rates and the
stated conditions, a stationary regime exists, and under Theorem 7 it is
unique. That is a precondition for fitting the thesis's model, not
evidence for the thesis. Distinct "regimes" in that thesis's sense
(habit, rumination) would need multiple stationary laws or slow changes of
parameters; under Theorems 1, 2, 7 and 8 the stationary law is unique, so
under those conditions the model has one regime per parameter setting.
Theorem 4 and 6 leave uniqueness open, and Remark 7's smallest and largest
solutions are where multiple regimes could live.

## Limitations

- Sufficient conditions only. The Lipschitz-weighted |h| bound can be far
  from sharp when excitation and inhibition offset.
- No result on cluster or cascade sizes, the distribution of the number of
  events an event triggers, or the spectrum (Hawkes 1971's subject).
- Kernels and rate functions are fixed; no time-varying or state-modulated
  kernels, and no learning.
- Uniqueness is open under monotone dynamics without Lipschitz conditions
  (Remark 7); the multivariate monotone case is "more delicate" and
  proved only for two components.
- Pure threshold rate functions are outside Theorem 2, inside Theorem 3
  only with bounded memory.
- No statistical content: nothing on estimating kernels or testing which
  regime holds.

## Open questions

- When excitation and inhibition coexist, what is the sharp condition for a
  unique stationary regime? A necessary condition would turn the bound
  into a threshold.
- What happens when the kernels are modulated by the process's own history
  (an influence canvas)? A stability theorem for such a model, or a
  counterexample, would say whether [QUESTION-091](../questions.d/QUESTION-091.md)'s "distances from
  criticality" are well defined there.
- Under monotone dynamics, can the smallest and largest stationary
  solutions differ? If so, the model has more than one stationary regime
  for one parameter setting, which is what a regime-switching reading of
  [CLAIM-286](../claims.d/CLAIM-286.md) would need.
