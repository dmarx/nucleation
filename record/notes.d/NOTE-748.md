---
number: 748
status: Read
formerly:
- NOTE-tmpqr65v
paper: LIT-266
title: 'Spekkens — Contextuality for preparations, transformations, and unsharp measurements'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (quant-ph/0406166v3, 18 March 2005,
    18 pp.), text extracted with pdftotext: §§I–IX, all footnotes, and
    Appendix A (the Kraus-operator proof of Eqs. 56–60). The §IV case
    analysis and the §VIII.A proof were checked step by step. The
    published PRA version was not compared. Quotations were checked against
    the extracted text by script. Replaces the skim in NOTE-238, which
    was filed when the work was seeded.
date: '2026-10-14'
summary: >-
  Noncontextuality, redefined operationally so that operationally
  equivalent procedures get equivalent representations, fails for a qubit's
  preparations, transformations and unsharp measurements, where no
  traditional Kochen–Specker proof exists. Preparation noncontextuality
  over the full set of quantum states implies outcome determinism for sharp
  measurements, so the old Kochen–Specker proofs refute universal
  noncontextuality. Measurement noncontextuality alone is consistent with
  quantum theory.
---
<!-- inactive-ok-file: THEORY-011 THEORY-015 QUESTION-067 CLAIM-044 CLAIM-046 CLAIM-142 — Proposed or Open; the theories, question and claims this reading bears on, open -->
<!-- inactive-ok-file: NOTE-238 — Superseded; the seeding skim this reading replaces -->

# NOTE-748: Spekkens — Contextuality for preparations, transformations, and unsharp measurements

## Contribution

The paper gives a definition of noncontextuality that applies to any
operational theory, to every kind of procedure, and to ontological models
whose outcomes are only probabilistically fixed by the ontic state. It
then proves three no-go theorems in a two-dimensional Hilbert space: one
each for preparations, unsharp measurements and transformations. It shows
how the traditional Kochen–Specker notion sits inside the new one. Before
it, contextuality was a property of sharp measurements in dimension three
or more. After it, it is a property of the representation of any
procedure, and a qubit already has it.

## Key insight

A context is whatever about a procedure is not fixed by its operational
equivalence class: "A noncontextual ontological model of an operational
theory is one wherein if two experimental procedures are operationally
equivalent, then they have equivalent representations in the ontological
model." Wherever the operational formalism has a freedom of
decomposition, there is a context, and "one can develop a proof of
contextuality that is based on this freedom". Mixed states have many
convex decompositions even for a qubit, so preparation contextuality needs
no third dimension and no assumption about measurements.

## Assumptions

- **Operational equivalence quantifies over every procedure the theory
  allows.** Preparations P and P′ are equivalent if
  p(k|P, M) = p(k|P′, M) for all M (Eq. 1); measurements likewise over all
  P (Eq. 2); transformations over all P and M (Eq. 3).
- **The ontological model framework (Eq. 4).** Each preparation is a
  normalised density µ_P(λ); each measurement a set of indicator functions
  ξ_{M,k}(λ) ∈ [0,1] with Σ_k ξ_{M,k}(λ) = 1; each transformation a
  stochastic transition matrix Γ_T(λ′, λ); and
  p(k|P,T,M) = ∫dλ′dλ ξ_{M,k}(λ′) Γ_T(λ′,λ) µ_P(λ) reproduces the theory
  exactly.
- **Feature 1.** Preparations distinguishable with certainty in one shot
  have nonoverlapping distributions: µ(λ)µ′(λ) = 0 (Eq. 11).
- **Feature 2.** A convex mixture of procedures is represented by the
  same convex mixture of representations (Eq. 12, and its analogues for
  measurements and transformations).
- **Noncontextuality, per kind.** µ_P = µ_{e(P)} (Eq. 5), ξ_{M,k} =
  ξ_{e(M),k} (Eq. 6), Γ_T = Γ_{e(T)} (Eq. 7), where e(·) is the
  equivalence class. "Universally noncontextual" means all three.
- **Outcome determinism** for a measurement means idempotent indicator
  functions, χ(λ)² = χ(λ). The §V proofs assume it for sharp measurements
  only; the paper says so: those "proofs of contextuality" "are contingent
  on the assumption of outcome determinism for sharp measurements".
- **§VIII.A uses the full set of quantum preparations.** The ontic space
  is defined as Ω = {λ | µ_ρ(λ) > 0 for some ρ} (Eq. 85), and the proof
  needs that "every density operator ρ appears in some convex decomposition
  of the completely mixed state I/d".
- **Exact equivalence.** The definitions apply only when two procedures
  are exactly operationally equivalent; §IX concedes that finite precision
  may mean this never happens in practice.

## Key results

- **Traditional noncontextuality as a special case (§III).** For sharp
  measurements with outcome determinism, independence of the
  representation from the fine-graining of the PVM "is just the
  traditional notion of noncontextuality". Measuring A with B or with C is
  a choice of fine-graining of A's PVM. Traditional proofs need
  dimension ≥ 3 "because there are no fine-grainings of non-trivial PVM
  measurements in a 2d Hilbert space".
- **Preparation contextuality for a qubit (§IV, Eqs. 13–36).** Six pure
  states a, A, b, B, c, C at 60° intervals on a great circle of the Bloch
  sphere give five decompositions of I/2: ½(a + A), ½(b + B), ½(c + C),
  ⅓(a + b + c), ⅓(A + B + C) (Eqs. 19–23). Orthogonal pairs give
  µ_aµ_A = µ_bµ_B = µ_cµ_C = 0 (Eqs. 24–26). Preparation noncontextuality
  sets all five mixtures equal to one ν(λ) (Eqs. 32–36). At each λ, the
  eight ways of zeroing one of each pair all force the all-zero solution.
  Two cases are worked; the other six follow by 60° and 120° rotations,
  which I checked (the three mixed cases of each kind are rotations of one
  another, and a 60° rotation swaps the triangles). No normalised solution
  exists. The proof uses no measurement assumption beyond Feature 1. (The
  text defines P_abc as a mixture of P_a, P_b and P_C; Eq. 22 shows that
  P_c is meant.)
- **Unsharp-measurement contextuality (§V.A, Eqs. 37–52).** Mixing the
  three sharp measurements {P_a, P_A}, {P_b, P_B}, {P_c, P_C} with weight ⅓
  gives the POVM {½I, ½I}, operationally a fair coin, so measurement
  noncontextuality demands indicator functions {½, ½}. Outcome determinism
  for the sharp ones allows only {0,1}, {1,0}, {⅔,⅓} or {⅓,⅔}.
  Contradiction.
- **Gleason-type version (§V.B, Eq. 53).** Measurement noncontextuality
  for all POVMs plus Busch's and Caves et al.'s 2d Gleason theorem give
  ξ_E(λ) = Tr(ρ_λ E). Then χ_P(λ) = Tr(ρ_λ P) cannot be idempotent for
  every projector.
- **Transformation contextuality for a qubit (§VI, Eqs. 54–66; App. A).**
  Six rotations about the y axis by multiples of π/3 give five convex
  decompositions of the map that projects the Bloch ball onto the y axis.
  Transformation noncontextuality then reproduces the §IV constraints on
  the images of µ_a. Appendix A proves the decompositions by unitary
  remixing of Kraus operators (Eqs. A4, A5). Footnote 11: by the
  Jamiołkowski isomorphism this is a preparation-contextuality proof in
  four dimensions. The proof is due to Rudolph.
- **Outcome determinism for unsharp measurements is excluded outright
  (§VIII).** The POVM {I/2, I/2} must be represented by {1/2, 1/2}, which is
  not idempotent.
- **Preparation noncontextuality implies outcome determinism for sharp
  measurements (§VIII.A, Eqs. 77–88).**
  - For a rank-1 PVM {P_k}, the states ρ_k = P_k are orthogonal, so their
    supports Ω_k are disjoint (Eq. 79).
  - Tr(ρ_k P_k′) = δ_kk′ forces ξ_k = 1 on Ω_k and 0 on the other supports
    (Eq. 82).
  - Σ_k (1/d) ρ_k = I/d, and every ρ lies in some decomposition of I/d.
    So preparation noncontextuality gives Σ_k (1/d) µ_k(λ) = µ_{I/d}(λ)
    (Eq. 88), and ∪_j Ω_j = Ω (Eq. 84).
  - Hence the ξ_k are idempotent everywhere. Coarse-graining extends this
    to every PVM.
  - "The old proofs are vindicated insofar as they remain proofs of the
    impossibility of universal noncontextuality".
- **Measurement noncontextuality alone is consistent with quantum theory
  (§VIII.B, Eqs. 89–92).** The Beltrametti–Bugajski model takes Ω to be the
  rays of Hilbert space, µ_ψ′(ψ) = δ(ψ − ψ′) and ξ_{Q_k}(ψ) =
  Tr(Q_k|ψ⟩⟨ψ|). It depends only on the POVM, so it is measurement
  noncontextual. It is not outcome deterministic for sharp measurements,
  and it is preparation contextual.
- **Conclusion (§IX).** "One can confine all the contextuality into the
  preparations and transformations if one likes … On the other hand, one
  cannot confine all the contextuality into the measurements". The models
  Bell and Kochen–Specker gave for 2d "are deemed contextual" under the new
  definition.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The traditional notion is measurement noncontextuality for sharp measurements plus outcome determinism | strong | definitional argument, §III |
| C2 | No preparation-noncontextual ontological model of a qubit exists | strong | proof, §IV, Eqs. 13–36 |
| C3 | No transformation-noncontextual ontological model of a qubit exists | strong | proof, §VI and Appendix A |
| C4 | No qubit model is noncontextual for unsharp measurements and outcome-deterministic for sharp ones | strong | proofs, §V.A and §V.B |
| C5 | Preparation noncontextuality over all quantum states implies outcome determinism for sharp measurements | strong | proof, §VIII.A, Eqs. 77–88 |
| C6 | Measurement noncontextuality alone is consistent with quantum theory | strong | the Beltrametti–Bugajski model, §VIII.B |
| C7 | Noncontextuality for preparations, transformations and unsharp measurements is as well motivated as for sharp ones | moderate | argument from ontological economy, §VII |
| C8 | Every classical theory is noncontextual for all procedures | weak | asserted in footnote 6, not proved; an opposing view is cited |
| C9 | A failure of local causality in a separable model implies measurement contextuality; the Beltrametti–Bugajski model is nonlocal by nonseparability instead | moderate | informal argument, §IX |

## Concepts

- **Operational equivalence.** Two procedures are equivalent when they give
  the same statistics with every procedure of the other kinds (Eqs. 1–3).
- **Context.** "Those that are not specified by specifying the equivalence
  class". Polaroid versus calcite for a polarisation measurement is the
  paper's example. By definition, knowing the context does not improve
  prediction.
- **Ontological model.** Ontic states λ in Ω with the representations of
  Eq. 4. It may have no hidden variables. The Beltrametti–Bugajski model's
  ontic states are the quantum states.
- **Indicator function.** ξ_{M,k}(λ), the probability of outcome k given
  λ. It is called idempotent, written χ, when it takes only the values 0
  and 1.
- **Outcome determinism.** A measurement represented by idempotent
  indicator functions. It is distinguished from determinism of the
  underlying dynamics: the weighted-dice example (§III) is deterministic
  classical mechanics without outcome determinism.
- **Universal noncontextuality.** Noncontextuality for preparations,
  transformations and measurements together.
- **Ontic and epistemic views of a set S of states (Eqs. 67–68).** In the
  ontic view, distinct states have disjoint distributions. In the epistemic
  view, only orthogonal ones do. An ontic view of pure states makes
  preparation noncontextuality fail trivially (Eqs. 69–76).

## Connections

The paper generalises the Bell–Kochen–Specker notion (Bell 1966;
Kochen and Specker 1967, both cited, not held). It sets itself against
Cabello's 2003 Kochen–Specker theorem for a single qubit using POVMs. That theorem
assumes outcome determinism for unsharp measurements, which the
{I/2, I/2} argument shows is inconsistent with measurement
noncontextuality anyway. Its notion of measurement noncontextuality
follows Bell's move from local determinism to local causality (footnote
5). Its motivation is "ontological economy", with Einstein's equivalence
principle as the example (§VII). It does not name Leibniz. The later
programme does: Schmid, Selby and Spekkens ([LIT-945](../literature.d/LIT-945.md)) recast the
definition process-theoretically and derive it from a principle of
Leibnizianity. The positive-quasiprobability characterisation in
[LIT-003](../literature.d/LIT-003.md), the epistemically restricted theories of [LIT-007](../literature.d/LIT-007.md) and the
interference argument of [LIT-019](../literature.d/LIT-019.md) all use the definition given here.
Budroni et al. ([LIT-263](../literature.d/LIT-263.md), §IV.E) restate §IV.

## Bearing on the record

- **[THEORY-011](../theory.d/THEORY-011.md): supported, and its `promote_when` is met
  for the Spekkens half.** §IV's case analysis is complete and correct. The
  proof needs only Features 1 and 2 and preparation noncontextuality, as
  the THEORY says. The §III dimension argument is stated, not proved, but
  it is elementary: a rank-1 projector has no non-trivial fine-graining.
  Two corrections:
  - The title's "no Kochen–Specker argument exists in dimension two" is
    true of the traditional notion, which uses sharp measurements. Cabello's
    2003 POVM argument for a single qubit is a Kochen–Specker-style proof.
    Spekkens rejects it, because it assumes outcome determinism for
    unsharp measurements, not because it fails as mathematics. The THEORY
    should say "for sharp measurements".
  - The THEORY's "What this does not say" ties the choice of notion to
    "Spekkens's Leibnizian methodological principle". This paper argues
    from ontological economy and Einstein's equivalence principle, and
    does not mention Leibniz. The Leibnizian framing is in [LIT-945](../literature.d/LIT-945.md).
    The substance is the same; the citation for the wording is not this
    paper.
- **[THEORY-015](../theory.d/THEORY-015.md): supported, with its own caveat confirmed.**
  The THEORY's account of §III, §VIII.A–B and §IX is accurate, and the
  quotation from §IX is exact. The proof does need the full preparation
  set: Ω is defined through all density operators (Eq. 85), and Eq. 86
  holds only because every ρ appears in a decomposition of I/d. In a
  fragment with fewer preparations, the step from Eq. 83 to idempotence
  fails as written. Two small precisions:
  - The paper extends from rank-1 PVMs to all PVMs by coarse-graining.
    That is a statement about measurements implemented by coarse-graining.
    The same support argument, run directly on ρ_k = P_k/rank(P_k), covers
    the rest. So the THEORY's "every projective measurement" stands.
  - What the old proofs refute is preparation plus measurement
    noncontextuality. Universal noncontextuality includes both, so the
    THEORY's wording is right. A reader should not take it to mean that
    they refute preparation noncontextuality alone. That needs §IV.
  The join to the sheaf form ([LIT-016](../literature.d/LIT-016.md)) remains the record's own, as
  [THEORY-015](../theory.d/THEORY-015.md) says.
- **The seeding checks.**
  - The first, §VIII.A's reliance on the full preparation set, is
    confirmed above.
  - The second is confirmed in the paper's own words: §V's proofs are
    "contingent on" outcome determinism for sharp measurements. §VIII says
    that neither Bell's, nor Kochen and Specker's, "nor any of the proofs
    of these types including those presented in section V" rule out
    measurement noncontextuality. They are proofs against preparation plus
    measurement noncontextuality.
  - The third is confirmed: "By our definition, any classical theory is
    necessarily noncontextual for all experimental procedures" is a
    footnote assertion with no proof, and it cites an opposing view
    (Bacciagaluppi).
- **[QUESTION-067](../questions.d/QUESTION-067.md).** The paper bears on the question in three ways.
  - **It supports the question's premise.** Preparation contextuality
    shows in a scenario with no overlapping measurement contexts. §IV
    uses six preparations and needs nothing from measurements beyond
    single-shot distinguishability. A sheaf test cannot see it.
  - **It sharpens the condition.** Operational equivalence is defined
    over *all* measurements (Eq. 1). An equivalence over a restricted probe
    family, such as the one [CLAIM-142](../claims.d/CLAIM-142.md) and [CLAIM-046](../claims.d/CLAIM-046.md) define, is Spekkens's
    relation only if that family is tomographically complete for the
    renderings. Otherwise two renderings the probes cannot separate may
    still be operationally inequivalent, and the assumption does not apply.
  - **It names the obstacle a pragmatic test would meet.** Finite
    precision "might imply that in practice no two experimental procedures
    are found to be operationally equivalent". The paper's proposed fix is that operationally
    similar procedures get similar representations. It leaves that
    without a measure of similarity.
- **Feature 1 matters for the mixed-preparation reading.** [QUESTION-067](../questions.d/QUESTION-067.md),
  after [CLAIM-044](../claims.d/CLAIM-044.md), reads an ambiguous utterance as a mixed preparation
  with several decompositions. The §IV proof needs the two members of each
  two-element decomposition to be perfectly distinguishable (orthogonal
  states). Readings that are only probably distinguishable do not give
  Eqs. 24–26. A pragmatic version would need either such pairs, or a
  noise-robust inequality, which this paper does not supply.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- All results are about exact operational equivalence and exact
  distinguishability. There is no inequality and no noise tolerance. §IX
  names the finite-precision problem and leaves it open.
- §VIII.A is proved for quantum theory with every density operator
  available as a preparation. It is not shown for subtheories or for
  general operational theories.
- That classical theories are always noncontextual (footnote 6) is
  asserted. The claim that contextuality is therefore nonclassicality rests
  on it.
- The motivation for noncontextuality (§VII) is an argument from
  ontological economy and from the "conspiratorial" look of
  context-dependence that averages out. It is not a derivation, and the
  paper notes that Bell and Mermin judged the matter differently.
- The promised conversion of a preparation-contextuality proof into a
  nonlocality proof is deferred to another paper (Rudolph and Spekkens,
  "in preparation").
- Transformation contextuality is proved only through its reduction to the
  §IV structure.

## Open questions

- A noise-robust form: what replaces exact equivalence? Answered later in
  the programme by noncontextuality inequalities, which the record does not
  hold.
- Does §VIII.A survive in fragments that lack some preparations, such as
  stabilizer or interferometric fragments ([LIT-019](../literature.d/LIT-019.md))? It would be
  settled by a proof of outcome determinism from the preparations a given
  fragment contains, or a fragment with a preparation-noncontextual model
  that is not outcome deterministic for its sharp measurements.
- Can contextuality be shown to power a quantum computational advantage?
  §IX speculates that it might.
