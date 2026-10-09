---
status: Read
paper: 'LIT-tmpionqf'
title: 'Getting to the Bottom of Noether''s Theorem'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv v5 (2 November 2025, text dated 15 February
    2022, 37 pages): the introduction and warning on topologies, Sections
    1–5 and the reference list. Every proof given in the paper followed
    (Theorems 2–4, 6–8, 10, and the sketch of Theorem 12's "if"
    direction); Theorems 5, 9 and 12 are quoted or sketched by the paper
    and their full proofs (C*-algebra exponentials; Gleason–Yamabe and
    Lie's theorems; Alfsen and Shultz's Theorem 23) were not read. Not
    compared with the Cambridge chapter. The dimension counts for real
    and quaternionic matrices were checked by hand.
date: '2026-10-09'
summary: >-
  Noether's theorem in Hamiltonian form, "a generates symmetries of b iff
  b generates symmetries of a", follows in Poisson algebras, complex
  *-algebras and Banach–Lie algebras from the antisymmetry of the bracket
  plus uniqueness of solutions; for a bilinear bracket antisymmetry is
  self-conservation, {a, a} = 0. What carries content is the map from
  observables (a Jordan algebra) to generators (a Lie algebra): i in
  complex quantum mechanics, none in the real or quaternionic case, and
  Alfsen–Shultz's dynamical correspondence for JB-algebras.
---

<!-- inactive-ok-file: THEORY-tmp3dh4x — Proposed; filed from this reading -->
<!-- inactive-ok-file: THEORY-158 — Proposed; compared as the Markov-process case, not leaned on -->
<!-- inactive-ok-file: CLAIM-tmpuwwjx — Proposed; named for the bearing reported, not edited -->

# NOTE-tmpjlwej: Getting to the Bottom of Noether's Theorem

## Contribution

The paper adds no new theorem; it says so. What it adds is an analysis of
which assumption carries the symmetry–conservation equivalence in the
algebraic (Hamiltonian) setting. Its answer is that the equivalence itself
is the antisymmetry of a bracket, equivalently the self-conservation of each
generator, and that the substantive assumption is that observables can be
turned into generators. It then connects the existence of that map, via
Alfsen and Shultz, to why quantum mechanics uses the complex numbers, and
reads Alfsen and Shultz's second condition as the link between time
evolution and thermal reweighting.

## Key insight

"a leaves b fixed iff b leaves a fixed" is, once a and b both live in one
structure with an antisymmetric bracket, the same fact as {a, b} = 0 ⇔
{b, a} = 0. For groups it is "g commutes with h iff h commutes with g". So
Noether's theorem is cheap for generators and expensive only where the
theory must say which observable generates which transformation. A theory
whose observables cannot be read as generators has no Noether theorem of
this form.

## Assumptions

- **Poisson algebra** (Section 1): a commutative algebra with a Lie bracket
  satisfying the Leibniz law; "a generates a one-parameter family" means
  Hamilton's equation d/dt F_t(b) = {a, F_t(b)}, F_0(b) = b, has a unique
  solution for each b. The group law is not assumed.
- **Complex *-algebra** (Section 2): observables O are self-adjoint,
  generators L skew-adjoint, ψ(a) = ia; flows by Heisenberg's equation with
  unique solutions.
- **Theorem 8**: only a vector space, a bilinear bracket, unique flows, and
  F_t^a(a) = a. No Jacobi identity, no multiplication.
- **Section 4**: O a unital JB-algebra (Banach Jordan algebra with
  ‖a²‖ = ‖a‖², ‖a ∘ b‖ ≤ ‖a‖‖b‖, ‖a²‖ ≤ ‖a² + b²‖), L its skew-adjoint
  order derivations, δ_H b = H ∘ b the self-adjoint ones.
- Topologies on the spaces where derivatives are taken are left loose by
  design ("Warning"): any locally convex topology making the bracket
  separately continuous for Theorems 3, 4 and 8; C^∞ for Theorem 2; norm for
  Theorems 5 and 10.
- Every flow is a one-parameter *group* of reversible transformations;
  dissipative or stochastic dynamics are outside the paper.

## Key results

- **Theorem 2.** On a compact Poisson manifold every element generates a
  one-parameter group of Poisson-algebra automorphisms.
- **Theorem 3 (Poisson Noether).** If a, b generate one-parameter
  families, F_t^a(b) = b ∀t ⇔ {a, b} = 0 ⇔ {b, a} = 0 ⇔ F_t^b(a) = a ∀t.
  The step {a, b} = 0 ⇒ F_t^a(b) = b uses uniqueness: the constant path is
  a solution.
- **Bilinearity remark.** {a, a} = 0 for all a, with bilinearity, gives
  {a, b} + {b, a} = {a + b, a + b} − {a, a} − {b, b} = 0.
- **Theorem 4.** The same equivalence in any complex *-algebra, for
  self-adjoint a, b with Heisenberg flows.
- **Theorem 5.** In a C*-algebra every self-adjoint element generates
  F_t^a(b) = e^{ita} b e^{−ita}, preserving all the structure (sketched).
- **Theorems 6 and 7.** A real *-algebra is the same as a pair (O, L)
  with a symmetric product ∘ and antisymmetric bracket {,} across the four
  pairings, satisfying a Leibniz law and an associator identity
  (a ∘ b) ∘ c − a ∘ (b ∘ c) = {a, {b, c}} − {{a, b}, c}; the Jordan and
  Jacobi identities follow. For complex *-algebras everything can be put
  on O with {a, b} = (i/2)(ab − ba) (sign of the associator identity
  flips).
- **Theorem 8.** Bilinear bracket + unique flows + self-conservation ⇒
  Noether's equivalence.
- **Theorem 9 (quoted).** Hilbert's fifth problem: a connected locally
  compact group with no small subgroups is a Lie group; Lie's theorems.
- **Theorem 10.** In any Banach–Lie algebra, F_t^a = exp(t ad_a) exists, is
  unique, preserves the bracket, and Noether's equivalence holds.
- **Dimension count.** For n × n matrices, real: dim O = n(n+1)/2,
  dim L = n(n−1)/2; quaternionic: dim O = 2n² − n, dim L = 2n² + n. No
  nonzero O(n)- or Sp(n)-invariant linear map O → L exists.
- **Theorem 12 (Alfsen–Shultz, quoted with proof sketch).** A unital
  JB-algebra is the self-adjoint part of a C*-algebra iff it admits a
  dynamical correspondence ψ : O → L with (A) ψ_a(a) = 0 and
  (B) [ψ_a, ψ_b] = −[δ_a, δ_b]; then ab = a ∘ b − iψ_a(b).
- **Section 5.** exp(−βδ_H) b = e^{−βH/2} b e^{−βH/2}; applied to the
  Gibbs states ω_γ of the trace state, exp(−βδ_H)ω_γ = (Z(β)/Z(γ))ω_{β+γ},
  a translation in inverse temperature. Condition (B), in the C*-case,
  reduces to [ia, ib] = −[a, b], i.e. i² = −1.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In a Poisson algebra, with unique flows, a generates symmetries of b iff b generates symmetries of a | strong (proof) | Theorem 3 |
| C2 | The same holds in any complex *-algebra and any Banach–Lie algebra | strong (proof) | Theorems 4, 10 |
| C3 | For a bilinear bracket, antisymmetry is equivalent to self-conservation, and self-conservation with unique flows gives Noether's equivalence without Jacobi or multiplication | strong (proof) | remark after Theorem 3; Theorem 8 |
| C4 | In real and quaternionic quantum mechanics observables cannot be identified with generators by an invariant linear map | moderate | dimension count, stated; invariance claim asserted without proof |
| C5 | A unital JB-algebra is the self-adjoint part of a C*-algebra iff it has a dynamical correspondence | strong (cited) | Theorem 12, Alfsen and Shultz (1998), proof sketched |
| C6 | Condition (B) expresses "inverse temperature is imaginary time" | weak (interpretation) | Section 5, by example in matrix algebras; the author says "We do not have a completely satisfactory answer" |

## Concepts

- **generates symmetries of / is conserved by**: F_t^a(b) = b for all t.
- **self-conservation principle**: each observable is conserved by the
  one-parameter group it generates; {a, a} = 0, or ψ_a(a) = 0.
- **observable / generator**: elements of a Jordan algebra O and of a Lie
  algebra L respectively; self-adjoint and skew-adjoint in a *-algebra.
- **order derivation**: a bounded δ on O with exp(tδ) an order
  automorphism; skew-adjoint ones (derivations of ∘) form L, self-adjoint
  ones are δ_H b = H ∘ b.
- **dynamical correspondence**: a linear ψ : O → L satisfying (A) and (B).

## Connections

Rests on the Jordan–von Neumann–Wigner programme and its classification of
finite-dimensional formally real Jordan algebras, on Alfsen and Shultz's
operator-algebra work (1998, 2003), and on the Jordan–Lie–Banach line
(Grgin and Petersen; Landsman; Emch). Points to generalized probabilistic
theories (Barnum, Mueller and Ududec; Barnum and Hilgert) as finite-
dimensional analogues that do not assume condition (B), and to Leifer and
Spekkens' quantum Bayesian product as a reading of the thermal maps.

## Bearing on the record

- **THEORY-158 (Baez & Fong, Markov processes).** The two papers fit
  together, though neither says so. Here the equivalence rests on an
  antisymmetric bracket between observables and on reversible flows. A
  Markov generator H acting on a diagonal observable O supplies neither:
  [O, H] is not a bracket of two observables, and exp(tH) is a semigroup.
  That is why the Markov theorem needs the second moment conserved as well
  as the mean, and why mean conservation alone does not give a symmetry.
  This is my connection, not the paper's; it does not change THEORY-158.
- **New THEORY.** The reading produces THEORY-tmp3dh4x: in the algebraic
  Hamiltonian setting the symmetry–conservation equivalence is the
  antisymmetry (equivalently, given bilinearity, the self-conservation) of
  the bracket together with uniqueness of flows, so its content lies in the
  map from observables to generators.
- **CLAIM-tmpuwwjx** (the manuscript's Noether-type conservation criterion
  for a Markov reconstruction kernel). This paper bears on it only by
  contrast: the conditions that make "symmetry ⇔ conservation" hold here
  (antisymmetry, reversible one-parameter groups, observables as
  generators) are absent in a Markov kernel, so the Baez–Fong theorem, not
  this one, is the relevant Noether theorem for that setting.
- No instruction for machine-learning practice.

## Limitations

- Nothing new is proved; the paper is an argument about which known
  hypotheses matter.
- Analysis is downplayed: existence and uniqueness of flows is assumed in
  Theorems 3, 4 and 8 and is where unbounded generators would bite.
- The Lagrangian formulation, in which Noether stated her theorem, is set
  aside; the paper does not show that its algebraic form recovers the
  variational one.
- The reading of condition (B) as "inverse temperature is imaginary time" is
  illustrated in matrix algebras and acknowledged as incomplete.
- Theorem 6's text refers to "Condition 1 in Theorem 7" just after
  Theorem 6, apparently meaning Theorem 6; a typo, harmless.

## Open questions

- An infinite-dimensional version of the Barnum–Hilgert and
  Barnum–Mueller–Ududec results that, like them, avoids condition (B).
- A physical meaning for (B) that does not presuppose the complex numbers,
  which the author says is still lacking.
