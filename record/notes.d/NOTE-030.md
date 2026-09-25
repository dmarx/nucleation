---
number: 30
status: Read
formerly:
- NOTE-tmp2gcwm
paper: LIT-062
title: 'Pusey, Barrett & Rudolph, reality of the quantum state (PBR)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:1111.3328v3 (arXiv stamp 18 Nov 2012;
    the PDF's own dateline reads "April 11, 2012"), 8 pp. I read the main
    text (pp. 1–5), references [1]–[26], Appendix A (the measurement
    circuit), Appendix B (the noise-tolerant bound) and Appendix C
    (numerical results). I extracted the text with PyMuPDF into
    raw4/1111.3328.txt; pdftotext is not on this host. Figures 1–5 came
    through as labels only, so I read their captions. I checked two things
    numerically in scratchpad/check_pbr.py: the Eq. 1 basis {ξ1..ξ4} is
    orthonormal and each ξ_k is orthogonal to exactly the product state the
    text names; and the Appendix A circuit yields zero-probability outcomes
    for (θ, n) = (π/3, 2) and (π/4, 2), with β = 2.186 for θ = π/3, matching
    the closed form given for n = 2. I did not compare the typeset Nature
    Physics version.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  Take pure states |ψ0⟩, |ψ1⟩ with |⟨ψ0|ψ1⟩| = cos θ. Assume (a) a model
  assigns each preparation a distribution µ_i(λ) over physical states, (b)
  n independent preparations yield the product distribution
  µ_{x1}(λ1)⋯µ_{xn}(λn), and (c) outcome probabilities depend only on (λ1,
  …, λn). If the model's predictions are within ε of quantum theory, then
  D(µ0, µ1) ≥ 1 − 2ε^{1/n} for any n with 2^{1/n} − 1 ≤ tan(θ/2) (Eq. 7,
  App. B). At ε = 0 the distributions for distinct pure states cannot
  overlap on a set of non-zero measure, so Harrigan–Spekkens ψ-epistemic
  models are ruled out.
---

# NOTE-030: Pusey, Barrett & Rudolph, reality of the quantum state (PBR)

## Contribution

PBR prove the first no-go theorem against ψ-epistemic ontological models in Harrigan and Spekkens' sense. Before it, whether any ontological model could reproduce quantum theory while letting distinct pure states share ontic states was open; the question had been posed by Hardy and formalised by Harrigan–Spekkens (p. 4). After it, the answer is no for every model satisfying preparation independence, and the paper gives:
- an explicit n-qubit measurement that witnesses this for every non-orthogonal pair (App. A);
- a noise-robust version, Eq. 7, which turns the statement into an experimentally testable bound on overlap (App. B).

## Key insight

Put n independently prepared systems in the overlap region, which happens with probability ≥ qⁿ > 0. Then the joint physical state is compatible with all 2ⁿ product preparations |ψ_{x1}⟩⊗⋯⊗|ψ_{xn}⟩. Now choose an entangled measurement in which every outcome is forbidden by quantum theory for at least one of those preparations (a "Post-Peierls-incompatible" set, after Caves–Fuchs–Schack, p. 3). On such a run the apparatus must still produce some outcome, and whichever it produces is forbidden for one preparation it cannot exclude. Overlap therefore forces a non-zero rate of quantum-forbidden outcomes. Formally, the overlap of the product distributions factorises, ω({µ_x⃗}) = ω(µ0, µ1)ⁿ (B7), while the measurement's forbidden outcomes bound it by 2ⁿε (B10).

## Assumptions

Stated formally on pp. 3–4 and in App. B:
- **Real physical state.** A system prepared in isolation in a pure quantum state has a physical state λ in a measure space Λ, "objective and independent of the observer" (p. 1). The assumption is needed only for systems "isolated, and not entangled with other systems" (p. 1). Preparation of |ψ_i⟩ yields λ ~ µ_i(λ). Only pure states are treated ("assume for simplicity that it is a pure state", p. 2).
- **Preparation independence.** n systems prepared independently in |ψ_{x1}⟩, …, |ψ_{xn}⟩ have physical states (λ1, …, λn) distributed as the product µ_{x1}(λ1)⋯µ_{xn}(λn) (Eq. 4, B3). As written, the joint system's physical state *is* the tuple (λ1, …, λn) (see corrections).
- **Response depends only on λ.** Outcome k of measurement M has probability p(k|λ1, …, λn) = ξ_{M,k}(λ⃗) ∈ [0, 1], summing to 1 over k (Eq. 5, B1, B10). This is ordinary ontological-models form: classical, nonnegative probabilities.
- **Target.** The model reproduces the Born rule for every outcome of the chosen measurement, exactly (ε = 0) or within ε (Eq. 7).
- **Not assumed.** Determinism ("Neither theorem assumes underlying determinism", p. 4). Locality in Bell's sense for entangled systems is not assumed either; the entangled *measurement* is allowed any dependence on the joint λ⃗.
- **Experimental reading.** High-fidelity gates without post-selection, since post-selection would let the device "escape the zero-probability outcomes" (p. 4).

## Key results

- **Simple case (p. 2–3, Eq. 1).** Take |ψ0⟩ = |0⟩, |ψ1⟩ = |+⟩ and two copies. The basis |ξ1⟩ = (|01⟩ + |10⟩)/√2, |ξ2⟩ = (|0−⟩ + |1+⟩)/√2, |ξ3⟩ = (|+1⟩ + |−0⟩)/√2, |ξ4⟩ = (|+−⟩ + |−+⟩)/√2 has ⟨ξ1|00⟩ = ⟨ξ2|0+⟩ = ⟨ξ3|+0⟩ = ⟨ξ4|++⟩ = 0. Hence any overlap of µ_0 and µ_+ contradicts quantum theory, "without saying anything about the value of q per se" (p. 3).
- **General measurement (App. A, Eq. A3, A7–A11).** For |ψ0,1⟩ = cos(θ/2)|0⟩ ± sin(θ/2)|1⟩, 0 < θ < π/2, and n with 2 arctan(2^{1/n} − 1) ≤ θ, there exist α, β such that U_{α,β} = H^{⊗n} R_α Z_β^{⊗n} followed by a computational-basis measurement gives outcome |x⃗⟩ zero probability on |Ψ(x⃗)⟩, for every x⃗. For n = 2, β = arccos[(1 − 4t² − t⁴)/(4t³)] with t = tan(θ/2). The minimum angle falls with n: 90°, 45°, 29.1°, 21.4°, 16.9° for n = 1…5 (my computation from A3).
- **Main theorem, noise-tolerant (Eq. 7 = B2).** If every outcome probability of this measurement is within ε of quantum theory, then D(µ0, µ1) = ½∫|µ0 − µ1| dλ ≥ 1 − 2ε^{1/n}, equivalently ω(µ0, µ1)ⁿ ≤ 2ⁿε (B11). *Holds when:* n satisfies A3, and the assumptions above hold. At ε = 0, ω = 0: the supports' intersection has measure zero, and |ψ⟩ is a function of λ almost surely.
- **Partial bounds below the threshold (App. C, Fig. 5).** When (C1) fails, the α = π, β = 0 circuit gives ω(µ0, µ1)ⁿ ≤ σ, bounding overlap without excluding it. This rests on numerical SDP solutions.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under the three assumptions, distinct pure states have distributions over λ whose supports intersect in measure zero (ψ-ontic in Harrigan–Spekkens' sense) | strong | App. A (construction) + App. B (proof); at ε = 0 |
| C2 | Noise-robust: approximate agreement to ε forces D(µ0, µ1) ≥ 1 − 2ε^{1/n} | strong | App. B, Eqs. B3–B11 |
| C3 | The App. A measurement uses the fewest systems possible for each θ | weak | Numerical SDP over "a variety of values of θ and n" (App. C); no proof |
| C4 | Dropping preparation independence permits ψ-epistemic models | moderate (citation) | p. 4, citing Lewis–Jennings–Barrett–Rudolph [16]; not shown here |
| C5 | Models that drop preparation independence (or measurement independence in Bell's case) "appear extremely contrived" | assertion | p. 4, no argument given |
| C6 | Abstract: "any model in which a quantum state represents mere information about an underlying physical state … must make predictions which contradict those of quantum theory" | moderate as stated | The body proves this only for "mere information" *defined as* support overlap (p. 2, "can justifiably be regarded as 'mere' information") and only for pure states. The abstract's informal wording is broader than the theorem; this is the gap [LIT-090](../literature.d/LIT-090.md) exploits |
| C7 | Accepting the conclusion makes collapse a physical process, or else makes every macroscopic branch real | informal argument | p. 4, discussion |
| C8 | The experiment is "challenging but not unrealistic" for small n | assertion | p. 4 |

## Method

A proof by construction. (1) Formalise "ψ is a physical property" as pairwise disjointness of the µ_ψ, following Harrigan–Spekkens and Hardy (Fig. 1, p. 2). (2) Build a joint measurement on n product preparations in which every outcome has zero Born probability on one preparation (App. A: a phase rotation Z_β on each qubit, an n-qubit gate R_α that phases only |0…0⟩, then Hadamards; α, β exist by an intermediate-value argument on the unit circle). (3) Bound the product-overlap ω({µ_x⃗}) = ωⁿ by the summed probability of the forbidden outcomes (App. B).

## Concepts

- **Physical property.** A label L such that the distributions {µ_L(λ)} are pairwise disjoint, so λ fixes L (Fig. 1, p. 2).
- **"Mere information".** ψ is mere information if µ0 and µ1 overlap for at least one pair of distinct states (p. 2). This is the Harrigan–Spekkens ψ-epistemic condition. The paper's informal gloss ("the quantum state represents mere information") is broader than this definition.
- **Overlap** ω(µ0, µ1) = ∫ min{µ0, µ1} dλ = 1 − D(µ0, µ1) (B4).
- **Post-Peierls incompatibility.** A set of states admitting a measurement in which each outcome is impossible on one of them (Caves–Fuchs–Schack [11], p. 3).
- **Preparation independence.** See Assumptions. The paper uses the name on p. 4 ("our assumption of preparation independence") without further gloss.

## Connections

- **Harrigan–Spekkens and Spekkens 2005/2007.** PBR take the ψ-ontic/ψ-epistemic formalisation from Harrigan–Spekkens [10], Spekkens [17] and Hardy [18] (p. 4), and list Spekkens' 2007 toy theory among the "less than real" proposals ([8], p. 1). The theorem is aimed squarely at the model class that toy theory inhabits.
- **[LIT-007](../literature.d/LIT-007.md) (Quasi-quantization; reading in reads/14.md).** [LIT-007](../literature.d/LIT-007.md) cites PBR as [31] among works in the "much debate" over whether a ψ-epistemic model of full quantum theory is possible (§I.C, p. 7). It then *declines* that programme: such a model "could always circumvent any no-go theorems by violating their assumptions" but would still have to be nonlocal and contextual. It proposes instead a programme that rejects the ontological-models framework, specifically classical probability for epistemic states, "but where one holds fast to the notion that a quantum state is epistemic" (p. 7).

  So on [LIT-007](../literature.d/LIT-007.md)'s own terms, PBR does not touch its epistricted models. Those are ψ-epistemic models of *subtheories* (Gaussian, quadrature, odd-d stabilizer). For odd d the models compose as products (Ω_AB = Ω_A × Ω_B, per reads/71.md) and reproduce the subtheory exactly. By PBR's own argument, then, no PBR-type measurement can exist *inside* those subtheories.

  The measurements PBR actually give are indeed not stabilizer operations. For |0⟩, |+⟩ the Eq. 1 basis is not a stabilizer basis: among two-qubit Paulis only Y⊗Y is diagonal in it (my check, check_pbr.py). In the App. A parametrisation the states cos(θ/2)|0⟩ ± sin(θ/2)|1⟩ are non-stabilizer for generic θ.

  What PBR does constrain is any attempt to extend these models to full quantum theory *within* the ontological-models framework and with product composition. That is the route [LIT-007](../literature.d/LIT-007.md) already disavows.

  The pairing has a cost. [LIT-007](../literature.d/LIT-007.md)'s strongest evidence for the epistemic view is the ψ-epistemic character of those models (p. 7). Under PBR's assumptions that character cannot survive to the full theory, so what remains of the epistemic view is the claim about a not-yet-specified non-classical-probability framework.
- **[LIT-003](../literature.d/LIT-003.md) (structure theorem; reads/71.md).** [LIT-003](../literature.d/LIT-003.md) shows that PBR's preparation independence follows from diagram preservation (its §4.4, Eq. 105, and Prop. 4.6: Λ_AB = Λ_A × Λ_B), citing a categorical PBR in its ref. [36]. So in the diagram-preserving framework the Spekkens school uses for noncontextuality, PBR's composition assumption is not an extra: any diagram-preserving ontological model of full quantum theory is caught by PBR. This is [LIT-003](../literature.d/LIT-003.md)'s observation, not PBR's.
- **[LIT-019](../literature.d/LIT-019.md) (interference paper; reads/17.md).** Its footnote 39 (p. 31) names PBR among principles "from which the assumption of ψ-ontology can be derived", says "the naturalness of these principles is disputed by some of the authors", and says all standard no-go theorems "including … PBR — assume the framework of ontological models", which is what it proposes to reject. Its toy field theory, a ψ-epistemic model of a quantum *fragment*, is outside PBR's reach in the same way as [LIT-007](../literature.d/LIT-007.md)'s models.
- **[LIT-016](../literature.d/LIT-016.md) (Abramsky–Brandenburger; reads/75.md).** No direct connection in the text. PBR's framework is ontological-models/measure-theoretic, not sheaf-theoretic, and the PBR measurement is a single context, so contextuality plays no role in the argument.
- **[LIT-054](../literature.d/LIT-054.md) (c16) and [LIT-090](../literature.d/LIT-090.md) (c19)** position themselves against this paper; see their readings.
- **Later work** named in the paper: Lewis–Jennings–Barrett–Rudolph [16] (a ψ-epistemic model that violates preparation independence); Hardy [20] and Montina [21, 22] on the size of Λ; Fuchs's QBism [24] as the "information about outcomes, not about an objective state" option left open (p. 5).

## Bearing on the record

- The record's quantum-foundations cluster should cite this as the source for "ψ-epistemic ontological models of full quantum theory are ruled out, given preparation independence". It should not be cited for "the quantum state is real" without that qualification, and not for "epistemic views are refuted": the paper itself leaves the QBist option (p. 5) and model-with-failed-assumptions option open.
- A THEORY candidate the cluster can now source properly: "In the ontological-models framework with product composition (preparation independence), pure quantum states are ψ-ontic; the ψ-epistemic models that exist ([LIT-007](../literature.d/LIT-007.md)'s epistricted theories) are of subtheories that lack PBR-type measurements, or else violate preparation independence." Sources: this paper (App. A–B), [LIT-007](../literature.d/LIT-007.md) §I.C, [LIT-003](../literature.d/LIT-003.md) §4.4. The subtheory half is my inference (a product-composing ψ-epistemic model that reproduces a subtheory exactly implies, by PBR's own proof, that the subtheory contains no PBR witness). None of the three papers states it.
- Nothing here bears on ML practice. No ANTH- document is implicated.

## Limitations

- **Pure states only**, and only the Harrigan–Spekkens definition of "epistemic". The abstract's informal wording outruns the formal result (C6).
- **Preparation independence carries the weight**, in the strong product-space form (Eq. 5). The authors concede that dropping it permits ψ-epistemic models [16] and answer only by calling such models "contrived" (C5).
- **The framework is classical-probabilistic** (nonnegative µ, ξ). Anything outside ontological models (QBism, [LIT-007](../literature.d/LIT-007.md)'s proposed non-classical epistemic framework) is untouched, as the paper says (p. 5).
- **Minimality of n** is numerical (C3).
- **No experiment** is reported. Feasibility is asserted (C8).

## Open questions

- Whether a *weaker* compositional assumption than Eq. 5 (for example, statistical independence without the joint state being exactly (λ1, …, λn)) still yields ψ-ontology. The paper does not separate the two.
- A proof, not an SDP survey, that the App. A measurement is optimal in n (App. C).
- Whether any ψ-epistemic model of full quantum theory with preparation independence survives outside the ontological-models framework, and what "ψ-epistemic" would then mean. [LIT-007](../literature.d/LIT-007.md) §I.C points at this; [LIT-090](../literature.d/LIT-090.md) disputes the definition itself.

## Corrections to the seeded skim

- The dossier gives the extent as "5+3 pp." and names Appendices A and B. v3 has three appendices, and the dossier omits **Appendix C (numerical results, p. 8)**. There the authors solve the SDP (C2) to show numerically that the Appendix A measurement uses the fewest systems possible: σ = 0 exactly when (C1) 2 arctan(2^{1/n} − 1) ≤ arccos|⟨ψ0|ψ1⟩| holds. When (C1) fails, the optimal measurement is the same circuit with α = π, β = 0, and it still gives the partial bound ω(µ0, µ1)^n ≤ σ (Fig. 5). This minimality is **numerical only** ("it appears that the measurement in Section A uses the smallest possible number of systems"). It is not proved.
- The dossier states the preparation-independence assumption as "independently prepared systems have independent physical states". The formal statement (p. 3–4, Eqs. 4–5; App. B, Eq. B3) is stronger in two respects the dossier does not record:
  - the joint physical state of n systems is *exactly* the list (λ1, …, λn) ∈ Λ^n, with no further joint variable;
  - the measurement's response function p(k|λ1, …, λn) depends on nothing else.

  Statistical independence of the λ_i alone would not give Eq. 5. The paper itself phrases the second part as "the outcome of the measurement can only depend on the physical states of the two systems at the time of measurement" (Fig. 2 caption). This matters because [LIT-003](../literature.d/LIT-003.md) later derives the same product form from diagram preservation (its Prop. 4.6, Eq. 105; see Connections).
- The dossier describes the circuit as "Z_β, then a phase gate R_α on |0…0⟩, then Hadamards". This is correct as a circuit order (U_{α,β} = H^{⊗n} R_α Z_β^{⊗n}, p. 6). The operative condition, though, is that for each preparation x⃗ the outcome |x⃗⟩ has zero probability. This requires e^{iα} + (1 + e^{iβ} tan(θ/2))^n − 1 = 0 (A8). The existence argument is a continuity/intermediate-value argument on f(β) = 1 − (1 + e^{iβ} tan(θ/2))^n, and it is given only for 2 arctan(2^{1/n} − 1) ≤ θ ≤ π/2 (p. 6).
- Minor: the dossier's "angle θ" should be read as |⟨ψ0|ψ1⟩| = cos θ (Eqs. 2, A1–A2), not |⟨ψ0|ψ1⟩|² = cos θ. So the simple case |⟨ψ0|ψ1⟩| = 1/√2 is θ = π/4, which is exactly the n = 2 boundary (tan(π/8) = √2 − 1). There the circuit has β = 0, α = π (my check). The simple case is thus the boundary instance of the general construction, not a separate trick.
