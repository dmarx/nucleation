---
status: Read
paper: 'LIT-tmpj84ja'
title: 'Baez & Fong — A Noether theorem for Markov processes'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv v1 (9 March 2012, 9 pages, the only arXiv
    version), every section and proof. Not compared against the J. Math.
    Phys. version. The finite-state counterexample was checked by hand.
date: '2026-10-09'
summary: >-
  For a Markov semigroup exp(tH) on a finite set, an observable O commutes
  with H iff the expectations of O and O² are both constant for every
  initial distribution, iff the expectations of every polynomial in O are,
  iff O is constant on each connected component of H's transition graph.
  Constancy of the mean alone is not enough; a 3-state example shows it.
  On a σ-finite measure space, [O, exp(tH)] = 0 for all t iff the means of
  O and O² are constant, by way of a one-step Markov-chain version proved
  with Chebyshev's inequality.
---

<!-- inactive-ok-file: THEORY-tmpnp46m — Proposed; filed from this reading -->
<!-- inactive-ok-file: THEORY-019 — Proposed; named for operators commuting with a group, a parallel, with no relation claimed -->

# NOTE-tmputmoi: Baez & Fong — A Noether theorem for Markov processes

## Contribution

A characterisation of the observables that commute with the generator of a
Markov process, in the commutator form of Noether's theorem (conserved
quantity iff it commutes with the Hamiltonian). In quantum mechanics a
constant expectation in every state is enough for commutation. The paper
shows that for Markov processes it is not, and that adding a constant
second moment (so a constant variance) is exactly enough. For a finite
state space, it also identifies what such observables are: functions
constant on the connected components of the transition graph.

## Key insight

The derivative of ⟨O, ψ(t)⟩ is ⟨1, [O, H]ψ(t)⟩ in the stochastic case.
Probability enters linearly, so this can vanish for every ψ without the
commutator vanishing. An observable can then have a constant mean while
probability still flows between states where it takes different values,
as long as the flows balance. Requiring the second moment to stay constant
rules that out. Σᵢ (Oⱼ − Oᵢ)² Hᵢⱼ is a sum of non-negative terms, and it
vanishes only if no transition ever connects states with different values
of O. So a commuting observable can only label regions that the process
never leaves.

## Assumptions

- **Finite case** (Sections 1–2): X a finite set; H infinitesimal
  stochastic, with Hᵢⱼ ≥ 0 for i ≠ j and Σᵢ Hᵢⱼ = 0 (columns sum to zero,
  acting on distributions). Master equation dψ/dt = Hψ. An observable is a
  function O : X → ℝ, identified with a diagonal matrix.
- **General case** (Section 3): X a σ-finite measure space; distributions
  are in L¹(X); observables are in L^∞(X), acting by multiplication; U(t)
  is a strongly continuous semigroup of stochastic operators on L¹. Its
  generator is typically unbounded, so the theorem is stated with
  [O, U(t)] and not [O, H].
- **"For every state."** Each equivalence quantifies over all initial
  distributions, not one.

## Key results

- **Theorem 1** (finite X). The following are equivalent: (i) [O, H] = 0;
  (ii) d/dt ⟨f(O), ψ(t)⟩ = 0 for every polynomial f and every solution;
  (iii) d/dt ⟨O, ψ(t)⟩ = d/dt ⟨O², ψ(t)⟩ = 0 for every solution;
  (iv) Oᵢ = Oⱼ whenever i and j lie in the same connected component of
  the transition graph. The graph has an edge j → i iff Hᵢⱼ ≠ 0, and
  components are taken ignoring direction.
- **The mean is not enough.** With H having columns (0, 0, 0), (1, −2, 1),
  (0, 0, 0) and O = diag(0, 1, 2), d/dt ⟨O, ψ⟩ = 0 at ψ(0) = (0, 1, 0) but
  [O, H] ≠ 0. The example is stronger than the paper states. Only column 2
  of H is non-zero, and Σᵢ Oᵢ Hᵢ₂ = 0 − 2 + 2 = 0, so ⟨O, ψ(t)⟩ is
  constant for *every* initial distribution. Meanwhile Σᵢ Oᵢ² Hᵢ₂ =
  −2 + 4 = 2 ≠ 0, so the second moment moves. (Checked by hand.)
- **Theorem 3** (Markov chain, σ-finite X). For a stochastic operator U
  on L¹(X) and O in L^∞: [O, U] = 0 iff ⟨O, Uψ⟩ = ⟨O, ψ⟩ and
  ⟨O², Uψ⟩ = ⟨O², ψ⟩ for every distribution ψ. The proof runs through
  three lemmas. If the moments are preserved, U maps distributions
  supported in O⁻¹(I) to the same set, for every compact interval I
  (Lemma 3, by Chebyshev on a fine partition of O's range). That makes U
  commute with every χ_I(O) (Lemma 2), and hence with O (Lemma 1).
- **Theorem 2** (Markov semigroup). [O, U(t)] = 0 for all t ≥ 0 iff ⟨O,
  U(t)ψ⟩ and ⟨O², U(t)ψ⟩ are constant in t for every distribution ψ. It is
  presented as an easy consequence of Theorem 3, with no separate proof.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In a finite Markov process, commutation with H ⇔ constant mean and second moment in every state ⇔ O constant on transition-graph components | strong | Theorem 1, full proof |
| C2 | Constant mean in every state does not imply commutation | strong | explicit counterexample, Section 1 |
| C3 | The same equivalence (without the component form) holds for Markov chains and semigroups on σ-finite measure spaces | strong for Theorem 3; Theorem 2 asserted as a corollary | Section 3 |
| C4 | Quantum Noether in commutator form: [O, H] = 0 iff ⟨ψ, Oψ⟩ is constant for every solution | strong (standard; bounded operators only) | Section 1, via polarisation |

## Concepts

- **stochastic operator**: linear, positivity-preserving, and
  integral-preserving (⟨1, Uψ⟩ = ⟨1, ψ⟩).
- **infinitesimal stochastic operator**: the generator H of a Markov
  semigroup: non-negative off-diagonal entries, columns summing to zero.
- **Markov semigroup**: U(t) = exp(tH), stochastic for t ≥ 0, continuous
  in t, with U(s + t) = U(s)U(t) and U(0) = I.
- **transition graph**: vertices X, an edge j → i iff Hᵢⱼ ≠ 0; connected
  components are taken ignoring direction.
- **"stochastic mechanics"**: Baez's name for the analogy in which
  probabilities replace amplitudes and the master equation replaces
  Schrödinger's.

## Connections

- **Baez's *Network theory* notes**, the source of the stochastic-mechanics
  analogy, cited as [1] and not held by the record.
- **Noether's theorem.** The paper is explicit that its version is
  "somewhat removed from the original form": it generalises the
  Poisson-bracket and commutator form, not the Lagrangian one.
- **THEORY-019 (Proposed)** says an operator commuting with a group has
  eigenspaces that are the group's isotypic components. In the stochastic
  case of Theorem 1, the commutant of H among diagonal observables is
  exactly the functions constant on the components of the transition
  graph. That is the block structure H is forced to respect. The parallel
  is mine.
- **THEORY-042 (Active)**, the superselection account. A commuting
  stochastic observable labels sectors that no transition connects, as a
  superselected charge labels sectors that no observable connects. The
  parallel is mine, and the two settings differ: one concerns dynamics, the
  other observables.

## Bearing on the record

- **New THEORY filed: THEORY-tmpnp46m**, on what the commuting conserved
  quantities of a Markov process are, and on the gap between a conserved
  mean and commutation.
- No existing THEORY is supported or contradicted directly; THEORY-019 and
  THEORY-042 are parallels, noted above.
- **Anthology.** No instruction for machine-learning practice.

## Limitations

- **Only diagonal observables.** O is a function on states, a
  multiplication operator. Commutation with non-diagonal operators
  (symmetries that permute states) is not treated, so the link to
  symmetries is thinner than the title suggests. The "symmetry" side of
  this Noether theorem is O itself as a generator, and the paper does not
  discuss what exp(sO) means for a Markov process.
- **Theorem 2 is not proved separately** from Theorem 3, and the step
  from a semigroup to every U(t) is left to the reader.
- **The component characterisation (iv)** is given only for finite X.
- **Wording slips.** The text says "the variance is the standard deviation
  of O", meaning its square. In the Chebyshev step, after defining
  ((M/n)/d)², it sets c = (Md)², where (M/d)² is meant. Neither affects the
  result.
- **The quantum version** is stated for bounded operators only.

## Open questions

- Is there a stochastic Noether theorem for non-diagonal symmetries, for
  example permutations of X commuting with H, linking them to conserved
  quantities? The paper does not attempt one.
- What do observables with a constant mean but not a constant variance
  mean in the dynamics, like the counterexample's O? They satisfy Hᵀ O = 0,
  a harmonic or martingale condition, but the paper does not name or study
  them.
- Does (iv) extend to general state spaces, with "connected component"
  replaced by a suitable notion of invariant set?
