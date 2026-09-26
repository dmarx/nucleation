---
number: 78
status: Read
formerly:
- NOTE-tmpv1zta
paper: LIT-093
title: 'Filip, Notes on the Multiplicative Ergodic Theorem'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:1710.10694v1 ("Revised October 31,
    2017"; arXiv stamp 29 Oct 2017), 46 pp.: §1–5 in full (2.1–2.5, 3.1–3.5,
    4.1–4.5, 5.1–5.4), the acknowledgements and references. Extracted with
    PyMuPDF into raw4/1710.10694.txt; there are no figures, so nothing was
    lost. I followed every proof line by line at the level of its argument.
    I did not collate against the ETDS version (39(5):1153–1189, 2019),
    which the acknowledgement's thanks to "the referee" suggests was revised
    after refereeing; differences are unverified.). Upgraded from `Skimmed`
    to `Read`: the claims table, assumptions and results are new, and the
    skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Expository notes that prove the Oseledets theorem in four ways. §2 uses
  projective invariant measures and a splitting lemma, without Kingman.
  §3.5 checks Kaimanovich's regularity criterion in the symmetric space
  GLₙ/Oₙ, using Kingman. §4 proves the Karlsson–Ledrappier horofunction
  theorem (for µ-a.e. ω there is a horofunction h_ω with
  −(1/N)h_ω(g_ω⋯g_{T^{N−1}ω}x₀) → l) for isometries of proper metric
  spaces. §5 gives an L² "mean" version via Monod's direct integrals of
  CAT(0) spaces and Karlsson–Margulis tracking, with an L² mean Kingman
  theorem. Two of the notes' own derivations do not work as written:
  Proposition 3.4.8(iii) is mis-stated, and the Lemma 5.1.5 step in the
  tracking proof does not apply as claimed. The main theorems are standard
  and not in doubt.
---

# NOTE-078: Filip, Notes on the Multiplicative Ergodic Theorem

## Contribution

These are expository summer-school notes, not new theorems. They add a single, compact path from the classical Oseledets theorem to its geometric generalisations, organised around the idea that the MET is a non-commutative law of large numbers whose "average" lives in a non-positively curved space.
- **§2:** a self-contained proof avoiding Kingman.
- **§3:** Kaimanovich's reformulation, in which Lyapunov exponents and flags correspond to a sequence of metrics tracking a geodesic in GLₙ/Oₙ.
- **§4:** Karlsson–Ledrappier's horofunction theorem, which needs no curvature at all.
- **§5:** a mean (L²) MET for cocycles of isometries of CAT(0) bundles, obtained by applying Karlsson–Margulis to Monod's direct integral, plus an L² Kingman theorem.

The only possibly new item is the presentation of §5 as "reversing Monod's approach to rigidity" (§1). The mean Kingman proof (Prop. 5.4.1, via von Neumann's theorem and two coprime block lengths) may also be original in this form; I have not checked.

## Key insight

A product of matrices sampled along an ergodic system acts on the space of inner products (a symmetric space of non-positive curvature). The MET says the orbit of the base metric moves off to infinity at a linear rate *along a geodesic*: the rate vector is the Lyapunov spectrum, and the geodesic's endpoint is the Oseledets flag. Once stated this way, "linear drift detected by a boundary point" makes sense in any proper metric space via horofunctions (§4). With convexity (CAT(0)) one recovers genuine geodesic tracking (§5). The subadditivity of d(x₀, gₙ⋯g₁x₀) is the engine every time.

## Assumptions

- **Base:** (Ω, µ, T) is ergodic and probability-preserving, and Ω is a separable metric space (§2.1.1).
- **§2 (Thm 2.2.6):**
  - a measurable vector-bundle cocycle T_ω : V_ω → V_{Tω};
  - "for simplicity" invertible (§2.2.3);
  - a fibre metric with ∫ log⁺‖T_ω‖_op dµ < ∞ (2.2.7).
  
  The exponents may include λ_k = −∞. The two-sided splitting (Variant 2.2.10) needs T invertible and the same condition for T⁻¹.
- **§3 (Thm 3.5.1):** both ∫log⁺‖T_ω‖ and ∫log⁺‖T_ω⁻¹‖ finite. Remark 3.5.7 notes the second can be dropped with a weaker notion of regularity, and holds automatically for SLₙ cocycles.
- **§4 (Thm 4.3.1):**
  - a measurable map ω ↦ g_ω ∈ Isom(X), with ∫ d(g_ωx₀, x₀) dµ < ∞;
  - X proper (assumed in §4.1.1, omitted from the theorem statement).
  
  The horofunction h_ω need not be equivariant (Remark 4.3.4).
- **§5:** X a complete CAT(0) space, not necessarily proper. Thm 5.3.1 holds for a single semi-contraction. Cor. 5.3.2 holds for a bundle of CAT(0) spaces with fibrewise isometries and d(σ₀, T*σ₀) < ∞ in L². Prop. 5.4.1 needs fₙ ∈ L², fₙ ≥ 0, and pointwise subadditivity under the Koopman operator.

## Key results

- **Thm 2.2.6 (Oseledets).** There are exponents λ₁ > ⋯ > λ_k and an invariant filtration V^{≤λ_k} ⊊ ⋯ ⊊ V^{≤λ₁} = V with (1/N)log‖T^N v‖ → λ_i for v ∈ V^{≤λ_i} \ V^{≤λ_{i+1}}. It follows from:
  - **Lemma 2.3.1:** either a single exponent, uniform in v, or an invariant proper subbundle;
  - **Lemma 2.3.3:** if λ_E > λ_F in 0 → E → V → F → 0, the sequence splits invariantly, via the explicit series τ_ω = −Σ_{n≥0}(T_E^{n+1})⁻¹U_{Tⁿω}T_Fⁿ, convergent by (λ_F − λ_E) < 0 and ‖U_{Tⁿω}‖ = e^{o(n)}.
- **Exponents of derived bundles (§3.1).** L ⊗ N gives {λ_i + η_j}; the dual gives −λ; Hom gives η_j − λ_i; Λᵏ gives sums of k distinct exponents. For volume-preserving diffeomorphisms the exponents sum to 0. Symplectic cocycles have symmetric spectrum ±λ; a cocycle preserving a form of signature (p, q) has at least p − q zero exponents.
- **Thm 3.3.9 (Kaimanovich).** {xₙ} ⊂ G/K is regular (sublinearly tracks a geodesic) iff d(xₙ, xₙ₊₁) = o(n) and r(xₙ)/n converges in a⁺. Proved here for H² only.
- **Thm 3.5.1.** Under two-sided log-integrability, the metrics ‖v‖_N := ‖T^N v‖ form a regular sequence in the fibre symmetric space. The proof is by Kingman on log σ₁(Λᵏ T^N) for each k, with small steps via Birkhoff.
- **Prop. 4.1.9 (Karlsson).** For a semi-contraction f of a proper X with drift l, there is a horofunction h with h(fᵏx₀) ≤ −lk for all k and −(1/N)h(f^N x) → l for all x.
- **Thm 4.3.1 (Karlsson–Ledrappier).** For isometries: drift l = inf_N (1/N)∫d(g_ω⋯g_{T^{N−1}ω}x₀, x₀) dµ exists as an a.e. limit, and there is a measurable ω ↦ h_ω with −(1/N)h_ω(g_ω⋯x₀) → l, and h_ω ∈ ∂X if l > 0. The proof uses a cocycle F(g, h) = −h(g⁻¹x₀), the maximising-measure Lemma 4.4.1 and measurable selection (§4.4.2). I checked the step from ∫f₁dη ≥ l to the a.e. limit: ergodicity of η is not needed, because (1/n)fₙ ≤ (1/n)Fₙ → l forces the limit to equal l η-a.e.
- **Cor. 4.5.1** (via the metric D(|x−y|) on ℝ, whose horoboundary is {0}). ∫D(|f|) < ∞ implies (1/N)D(|S_N f|) → 0. With D(t) = tᵖ, 0 < p < 1, this gives the Marcinkiewicz–Zygmund-type law S_N/N^{1/p} → 0 for f ∈ Lᵖ.
- **Thm 5.3.1 (Karlsson–Margulis, single semi-contraction).** On a complete CAT(0) space, (1/n)d(Tⁿx₀, γ(An)) → 0 for some ray γ and A ≥ 0. Cor. 5.3.2 gives the L²-mean MET on direct integrals.
- **Prop. 5.4.1 (mean Kingman).** ‖fₙ/n − A‖_{L²} → 0 under fₙ ≥ 0 and L² subadditivity. I checked the proof: nonnegativity lets ‖f_N/N‖² be bounded by the inner product of two block averages, and the non-trivial root-of-unity components for coprime k₁, k₂ are orthogonal.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Oseledets MET without Kingman | moderate | §2 proof. The growth-dichotomy lemma's measure step and the uniformity bookkeeping are cited or implicit (corrections). The theorem itself is classical |
| C2 | Invariant splitting when a subbundle grows faster (Lemma 2.3.3) | strong | explicit convergent series; checkable by a non-specialist with ergodic-theory basics |
| C3 | Kaimanovich's regularity criterion in any G/K | strong (cited) / moderate (here) | proved only for H² via the hyperbolic law of sines; general case cited [Kaĭ87] |
| C4 | MET ⇔ regularity of the metric sequence (Prop. 3.4.8) | weak as printed | condition (iii) mis-stated (needs a log); proof sketched |
| C5 | Karlsson–Ledrappier horofunction MET for isometries of proper spaces | strong | complete proof modulo measurable selection (cited theorems) and Lemma 4.4.1(ii), whose fibred version is "similar" |
| C6 | Marcinkiewicz–Zygmund-type law from the horofunction MET | strong | short derivation (fixable typo in the subadditivity of D) |
| C7 | Karlsson–Margulis tracking for a semi-contraction of CAT(0) | strong (cited) / weak (as argued here) | the §5.3 proof misapplies Lemma 5.1.5 (corrections); refer to [KM99] |
| C8 | Mean (L²) MET for CAT(0) bundles | moderate | immediate from C7 plus Monod's direct-integral facts, which are cited ([Mon06, Prop. 44, Rmk 48]) |
| C9 | Mean Kingman theorem in L² | strong | complete short proof (von Neumann + coprime blocks) |

## Method

The methods are:
- ergodic-theory compactness (invariant measures on the projective bundle);
- explicit splitting series;
- Lie structure theory (KAK, Cartan projection, singular values);
- metric geometry (horofunction bordification, Busemann functions, CAT(0) convexity, uniform convexity);
- Monod's direct integrals.

**What a non-specialist can verify:** the §2 splitting lemma, Remark 2.2.11 (1-dim MET = Birkhoff), the exterior-power/singular-value bookkeeping of §3.1–3.2, the H² case of Kaimanovich, the whole of §4 except the cited measurable-selection theorems, Cor. 4.5.1, and Prop. 5.4.1.

**What needs a specialist or the cited sources:** the fibred weak-* compactness in Lemma 2.3.1, the general-rank Kaimanovich theorem, Monod's description of geodesics and boundaries in direct integrals, and a correct version of the §5.3 tracking argument.

## Concepts

- **Cocycle over T:** a measurable family of linear maps T_ω : V_ω → V_{Tω}.
- **Lyapunov exponents and forward Oseledets filtration V^{≤λ_i}.** With invertibility, the splitting is V = ⊕V^{λ_i}.
- **Cartan projection** r(x) ∈ a⁺: the "vector-valued distance" from the basepoint. For GLₙ it is (log σ_i(g)).
- **Regular sequence** (§3.3.6): d(xₙ, γ(θn)) = o(n) for some geodesic ray γ.
- **Horofunction:** a limit point of hₓ = d(x, ·) − d(x, x₀) in C⁰(X). **Busemann function:** the horofunction of a geodesic ray.
- **Linear drift** l of a semi-contraction or random walk: lim (1/N)d(x₀, f^N x₀).
- **Direct integral** L²(𝒳, µ): measurable sections at L²-distance from a base section. It is CAT(0) if the fibres are.
- **Semi-density:** α ∈ L² with ∫α² = 1.

## Connections

- **Lineage:** Furstenberg–Kesten (1960); Oseledets (1968); Ruelle (1979, 1982; Hilbert spaces); Kaimanovich (1987); Karlsson–Margulis (1999); Karlsson–Ledrappier (2006); Gouëzel–Karlsson (2015, semi-contractions); Monod (2006, direct integrals and rigidity).
- **Applications named:** Pesin theory, Ledrappier–Young, Margulis superrigidity via Zimmer's boundary maps.
- **Textbooks** for the classical theorem: Ledrappier 1984, Katok–Hasselblatt, Mañé, Viana 2014, Bochi's notes. §2 is close to Bochi's treatment; the author credits Walters (1993) and Mañé (Lemma 11.6) for ideas in Lemmas 2.3.1 and 2.3.3.
- **No link to any other work in this record.**

## Bearing on the record

- **No THEORY document is affected.**
- **For ML practice: the notes contain none.** They never mention neural networks, signal propagation, RNNs or learning. The seed's suggestion that they could serve as "a rigorous background source" for Lyapunov-exponent analyses of deep networks should be treated with care. The MET's hypotheses are an ergodic, stationary sampling of the matrices and N → ∞. They match i.i.d. random-weight products at initialisation (where Furstenberg–Kesten already suffices), but not the layer-dependent, finite-depth Jacobian products of trained networks. A document in the Anthology of the SOTA citing Lyapunov exponents for trainability should cite the ML paper that makes the claim, not these notes.

## Limitations

- Expository by design. Several results are proved in special cases (Kaimanovich for H²) or cited (measurable selection, Monod's direct-integral structure, Kingman itself).
- Two of the notes' own derivations are mis-stated or incomplete (Prop. 3.4.8(iii); the §5.3 use of Lemma 5.1.5).
- The equivariance of h_ω (Remark 4.3.4) is asserted to be arrangeable in CAT(0)/hyperbolic settings without proof.
- No infinite-dimensional (Ruelle) or semi-contraction (Gouëzel–Karlsson) proofs; these are only cited.
- The arXiv v1 is pre-referee (the ETDS version thanks a referee). The corrections above may already be fixed in the journal version; I have not checked.

## Open questions

- None posed by the notes.
- **For a reader:** does the ETDS version repair Prop. 3.4.8(iii) and the §5.3 tracking step? Collating the two would settle whether the published notes can be cited for those two points.

## Corrections to the seeded skim

- **"Proved without Kingman" is true only of §2.** The seed says the MET "can be proved geometrically without Kingman's subadditive theorem". That is the §2 proof, which uses the Birkhoff theorem, Krylov–Bogoliubov-type compactness of fibred measures and a splitting lemma. The geometric (Kaimanovich) proof in §3.5 invokes Kingman explicitly (Thm 3.5.2 applied to log‖T^N_ω‖_op and exterior powers). So does the §4 proof (§4.4.7, and Lemma 4.4.1(ii)).
- **Kaimanovich's theorem (Thm 3.3.9) is stated for all G/K but proved only for the hyperbolic plane** ("For simplicity, consider the case of the hyperbolic plane", p. 19). Remark 3.3.12 lists what the general proof needs (curvature comparison and structure theory), without supplying it. So §3's "geometric form" of the MET (Thm 3.5.1) is complete here only in rank one.
- **Proposition 3.4.8(iii) is mis-stated.** It requires |⟨Λ^{−2n}(Tⁿ)†Tⁿv, v⟩| = o(n). A one-dimensional counterexample: take T_ω = e^{λ + g(ω)} with g mean-zero and Birkhoff sums of size √n (a CLT-type fluctuation). Then (i) holds with exponent λ, but ⟨Λ^{−2n}T^{2n}v, v⟩ = e^{2Sₙg}, which is not o(n). The intended condition is presumably (1/n) log|⟨…⟩| → 0, or equivalently log‖·‖ = o(n). The proof of (i) ⇔ (iii) is also only asserted: Λ^{−2n} and (Tⁿ)†Tⁿ do not commute, and the cross terms are not addressed. The equivalence with regularity, (ii) ⇔ (iii), is said to "follow from the definition", which it does only once the logarithm is restored.
- **The §5.3 tracking proof misapplies its own lemma.** The notes say the inequality in §5.3.7, d(x₀, x_N) ≥ d(x₀, xₙ) + [(A−ε)/(A+ε)]·d(xₙ, x_N), "is exactly the almost reverse triangle inequality to which Lemma 5.1.5 will apply". But Lemma 5.1.5 needs the defect (1−ε) on d(x, y) with x = x₀, y = xₙ, and here it sits on d(xₙ, x_N).
  - Swapping the roles (x = x_N) gives a bound in terms of d(xₙ, x_N), not d(x₀, xₙ), as (5.3.9) needs.
  - Converting directly costs 2ε(N_i − N_{i−1}), which is small relative to a_{N_{i−1}} only if N_i/N_{i−1} stays bounded. The notes choose N_i only "> K_{i+1}".
  - Separately, the step uses a_{N−n} ≤ (A+ε)(N−n), which needs N − n ≥ K_i. The notes do not ensure this, though it is fixable by taking N_i larger.

  The theorem (Karlsson–Margulis 1999) is not in doubt. The notes' rendition of it has a gap I could not close from the notes alone; a reader should check [KM99] for the argument.
- **Lemma 2.3.1 (growth dichotomy) and its measure-theoretic step.** The proof takes empirical measures along the orbit of one µ-generic ω and asserts their weak-* limits project to µ. In the measurable, non-compact setting of the theorem, the orbit measures project to empirical measures of ω's orbit, not to µ. The fibred weak-* topology that makes this work is only cited (Viana §4.2.3; Bochi §4), and the "Krylov–Bogoliubov in families" statement is left as Exercise 2.4.2(ii). The notes are honest about citing, but this step is not self-contained.
  - Relatedly, the induction in the proof of Thm 2.2.6 applies Lemma 2.3.3, which needs growth *uniform* over unit vectors, to quotients produced by the inductive hypothesis. The theorem's statement does not carry uniformity. It is recoverable (e.g. by a determinant argument on each single-exponent piece), but this is not said.
- **Minor errors:**
  - §3.2.4 calls the KAK decomposition "polar (or Iwasawa, or KAK)"; Iwasawa is KAN, and KAK is the Cartan decomposition.
  - §3.2.5 orders the singular values increasingly, while the Weyl chamber a⁺ is decreasing.
  - Remark 3.3.10(i) says d(xₙ, xₙ₊₁) = O(n) where o(n) (or O(1)) is meant.
  - Prop. 4.1.9's proof cites "(4.2.6)" for its own limit.
  - Lemma 4.4.1(ii) has "projection to η equal to µ" and "∫F dη" for ∫f dη.
  - §4.4.7 has an index shift (g_{Tω}⋯g_{Tⁿω} for g_ω⋯g_{T^{n−1}ω}).
  - In §4.5 the subadditivity derivation of D is written "assuming t ≤ s", where the displayed step then points the wrong way. The correct one-line proof is D(t+s) = t·D(t+s)/(t+s) + s·D(t+s)/(t+s) ≤ D(t) + D(s).
  - In Lemma 5.1.5 the modulus is applied as g(d(y, y′)/2R) against the definition's g(d/R).
