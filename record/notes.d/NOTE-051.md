---
number: 51
status: Read
formerly:
- NOTE-tmpek3wm
paper: LIT-030
title: 'Cairo, counterexample to the Mizohata-Takeuchi conjecture'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2502.06137v2 (12 Mar 2025), 15 pp.: §1
    (1.1–1.9), §2 (Theorem 2.1 and its proof), §3 (3.1–3.4: reduction,
    "white lie" proof, incidence lemma, rigorous proof), §4 (Lemma 4.1,
    heuristics, Lemmas 4.3–4.4, Remark 4.5, §4.4) and the references.
    Extracted with PyMuPDF into raw4/2502.06137.txt; nothing was skipped. I
    checked the exponent bookkeeping of the construction by hand (below). To
    answer the dossier's question about follow-ups, I read the arXiv
    abstracts (not the papers) of Cairo–Zhang arXiv:2512.08064 (8 Dec 2025)
    and Fenves arXiv:2606.27020 (25 Jun 2026).). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  For every C² hypersurface Σ ⊂ ℝᵈ not lying in a hyperplane (implicitly:
  one with a point of non-zero curvature; see corrections), and every
  large R, there are f ∈ L²(Σ) and a weight w = |ĥ|² with supp ĥ ⊂ B_{CR}
  such that ∫|Ef|²w ≳ log R · ‖f‖²₂ · sup_ℓ ∫_ℓ w (Thm 1.2 via Prop. 3.1).
  So the Mizohata–Takeuchi conjecture and Stein's conjecture (Conj. 1.4)
  are false as stated, and the CHV route to loss-free endpoint multilinear
  restriction is closed. The mechanism is a lattice Q of middle-layer
  subset sums of N ≍ log R points on Σ, chosen so that no hyperplane meets
  more than 2^{d−1} of the R⁻¹-balls around Q (Lemma 3.5).
---

# NOTE-051: Cairo, counterexample to the Mizohata-Takeuchi conjecture

## Contribution

Before this paper, Mizohata–Takeuchi (Conj. 1.1) was believed true. It had been proven for radial weights (Barceló–Ruiz–Vega), with R^{1/4+ε} loss for the cone in ℝ³ (Ortiz), and with R^{(n−1)/(n+1)+ε} loss in general (Carbery–Iliopoulou–Wang). It was a proposed route both to loss-free endpoint multilinear restriction (via CHV) and, through Stein's conjecture plus Kakeya, to restriction. After this paper it is false for every curved hypersurface, with at least a log R loss. Stein's conjecture (Conj. 1.4), which implies Mizohata–Takeuchi in one line (p. 2), is false too.

## Key insight

Take a weight that looks, on the Fourier side, like R⁻¹-balls placed on a set Q of subset sums of N points of Σ. Convolving with f dσ, a sum of bumps at the N points, maps Q largely back into Q or into its neighbouring layer. So ‖h * f dσ‖² gains a factor N² over the trivial count. The X-ray side, ‖P_νh‖²_{L²(L¹)}, only sees how many balls a hyperplane can hit. Choosing the N points along a dyadically spaced, moment-curve-like sequence on Σ makes no hyperplane hit more than O(1) balls (Lemma 3.5). The ratio is N ≍ log R. Curvature is exactly what lets the ν-projections of the points lie in separated dyadic scales for all directions ν simultaneously; a flat surface projects to a point in its normal direction.

## Assumptions

- Σ ⊂ ℝᵈ is a compact C² hypersurface with surface measure dσ, not contained in a hyperplane. It must be connected, or have a point with non-degenerate curvature in at least one direction (see corrections).
- The weight is w = |ĥ|² with supp ĥ ⊂ B_{CR}, so w is "locally constant at scale 1" (following CIW). The counterexample is on B_R(0), i.e. **for each R** there are f = f_R and w = w_R. The loss is log R as R → ∞; there is no single (f, w) violating (1.1) by an infinite factor.
- Implicit constants depend on d and Σ.

## Key results

- **Theorem 2.1** (X-ray estimate). For w = |ĥ|² ≥ 0 and p ∈ [1, ∞], ‖X_νw‖_{Lᵖ(ν^⊥)} ≤ ‖P_νh‖²_{L²(L^q(ν^⊥))} with q = 2p/(2p−1). At p = ∞ this is ‖X_νw‖_∞ ≤ ‖P_νh‖²_{L²(L¹)}, sharp when h ≥ 0. The proof is Plancherel in the ν-direction (projection–slice), then Minkowski, then Hausdorff–Young on ν^⊥.
- **Proposition 3.1** (⇒ Theorem 1.2). For each R ≥ 1 there are f ∈ L²(Σ) and h with supp ĥ ⊂ B_{CR} such that ‖h * f dσ‖²₂ ≳ log R · ‖f‖²₂ · ‖P_νh‖²_{L²(L¹)} for every ν ∈ S^{d−1}.
- **Construction.**
  - N ≍ log R points ξ₁, …, ξ_N ∈ Σ, R⁻¹-separated.
  - f = Σ S_i, normalised bumps at ξ_i, so ‖f‖₁ ~ N and ‖f‖²₂ ~ N R^{d−1} (3.1).
  - Q = {c⃗·ξ⃗ : c⃗ ∈ {0,1}^N, Σc_i = ⌊N/2⌋}, with |Q| = C(N, ⌊N/2⌋) ~ N^{−1/2}2^N.
  - h = h₀ * η_R with h₀ = Σ_{q∈Q} δ_q.
- **Estimates.**
  - ‖h * f dσ‖² ≳ N²|Q|R^d (3.6), because at least a quarter of the translates q + ξ_i − ξ_j land back in Q (3.8), and R⁻¹-separation bounds the overlap (3.9).
  - ‖P_νh‖² ≲ R²‖K_ν‖₁‖K_ν‖_∞ ≲ R|Q|, where K_ν(λ) counts balls meeting the plane λν + ν^⊥ and ‖K_ν‖_∞ ≲ 2^{d−1}.
  - **Ratio:** N²|Q|R^d / (N R^{d−1} · R|Q|) = N ≍ log R. I checked this bookkeeping.
- **Lemma 3.5 / 4.1** (incidence). The points can be chosen so that no hyperplane passes through more than 2^{d−1} of the R⁻¹-balls around the subset sums. Equivalently, for every ν the projections π_ν(ξ_n − ξ₀) lie in distinct dyadic scales except for a set S_ν of at most d − 1 "bad" n.
  - **Lemma 4.3** proves this for the moment curve M_d(t) = (t, …, t^d) with t_n = c^{−n}. The proof is by induction on d via the projective map φ(x) = (x₂, …, x_d)/x₁, which sends M_d to M_{d−1} and hyperplanes to hyperplanes.
  - **Lemma 4.4** transfers it to a curved Σ by taking ω_n = (c^{−n}, c^{−3n}, …, c^{−dn}) in graph coordinates.
- **Conjecture 1.5** (local Mizohata–Takeuchi, R^ε loss) and **Conjecture 3.2** (its Fourier-side form) are proposed as replacements. See corrections for their current status.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | ‖X_νw‖_p ≤ ‖P_νh‖²_{L²(L^q)}, sharp at p = ∞ for h ≥ 0 | strong | proof, Thm 2.1: Plancherel + Minkowski + Hausdorff–Young. A non-specialist with Fourier analysis can check it |
| C2 | Mizohata–Takeuchi fails with log R loss for every curved C² hypersurface | strong (modulo the incidence lemma) | Prop. 3.1 via §3.4. The counting reduction is checkable, and I checked the exponent bookkeeping |
| C3 | No hyperplane meets more than 2^{d−1} of the balls (Lemma 3.5) | moderate | proof, §4. It is an induction on d whose constants (b′, b₂, b₃, b₄ ~ b) are tracked only up to "∼". Checking it needs an expert; I followed the logic but could not verify every containment |
| C4 | Stein's conjecture (Conj. 1.4) is false as stated | strong | one-line implication Stein ⇒ Mizohata–Takeuchi (p. 2) + C2 |
| C5 | The CHV route to loss-free endpoint multilinear restriction is closed | strong (as a statement about that route) | CHV's implication + C2; it says nothing about Conj. 1.3 itself |
| C6 | The theorem holds for every C² hypersurface not in a hyperplane | weak as literally stated | the proof needs a curved point. Counterexample to the literal statement: finite unions of flat pieces, where Mizohata–Takeuchi holds with constant k (my argument, corrections) |
| C7 | Local Mizohata–Takeuchi (R^ε loss) may be the right reformulation | conjecture | §1.7. Since refuted for a C^k-dense family, including many convex C² hypersurfaces, by Cairo–Zhang 2025 (abstract only) |
| C8 | The polynomial-partitioning alternative to Lemma 4.1 cannot easily give the sharp d − 1 bad points | assertion | Remark 4.5 |

## Method

The construction uses:
- a Fourier-side reformulation, E_w(f, f) = ‖h * f dσ‖² with |ĥ|² = w;
- a "white lie" heuristic proof using the locally constant principle, followed by a rigorous version with a Schwartz kernel η_R;
- an incidence-geometry lemma proved by induction on dimension along the moment curve, with a projective map φ that commutes with the moment curve's scaling symmetry L_c.

**What a non-specialist can verify:**
- Thm 2.1;
- the reduction Thm 1.2 ⇐ Prop. 3.1 (Plancherel);
- the counting that turns |Q|, N and R into the log R ratio;
- the one-line Stein ⇒ Mizohata–Takeuchi;
- the claim that the construction fails for flat surfaces.

**What a non-specialist cannot verify:**
- Lemma 4.3's induction (the box-containment claims U_{b,c,n} − U_{b,c,k} ⊂ U_{b′,c,n} and φ(U^d) ⊂ U^{d−1}, with unspecified constants);
- the o(|t|²) transfer in Lemma 4.4;
- the rigorous overlap bounds (3.8)–(3.9). The first is argued as a probability ("≥ 1/4 probability that q + ξ_i − ξ_j will lie in Q") and needs the middle-layer structure of Q to be made exact.

## Concepts

- **Extension operator:** Ef(x) = ∫_Σ e^{−2πi⟨x,ς⟩} f(ς) dσ(ς).
- **X-ray transform:** Xw(ℓ) = ∫_ℓ w. X_νw(z) = ∫_{ℝν+z} w for z ∈ ν^⊥.
- **Mizohata–Takeuchi (Conj. 1.1):** ∫|Ef|²w ≲ ‖f‖²₂ ‖Xw‖_∞ for all non-negative weights w.
- **Stein's conjecture (Conj. 1.4):** the same bound with ‖Xw‖_∞ replaced by the f-weighted average of sup over lines parallel to the normal N(ς).
- **P_νh:** the restriction of h to the slices λν + ν^⊥, as a function ℝ → Lᵠ(ν^⊥).
- **K_ν(λ):** the number of R⁻¹-balls of h meeting the slice at height λ.
- **Bad set S_ν:** the indices n whose ν-projection shares a dyadic scale with a later one. |S_ν| ≤ d − 1.

## Connections

- **Lineage it refutes or blocks:** Takeuchi (1974, 1980) and Mizohata (1985) on L²-well-posedness of first-order Schrödinger perturbations; Stein (1979); Barceló–Ruiz–Vega (1997, radial case); Carbery (2009, tube occupancy); CHV (2018/2023, multilinear duality); Shayya (2023); Ortiz (2023); CIW (2024, R^{(n−1)/(n+1)+ε}); Bennett–Gutierrez–Nakamura–Oliveira (2024, phase-space version); Guth's 2022 talk (decoupling axioms alone cannot beat the CIW loss).
- **Follow-ups (abstracts only):** Cairo–Zhang arXiv:2512.08064 (power-loss counterexamples to Conj. 1.5 on a dense family of C^k hypersurfaces, matching CIW for C² up to the endpoint, via a projected higher-rank lattice); Fenves arXiv:2606.27020 (a new proof via cusp excursions and random unimodular lattices, with power loss generic in C^k).
- **No link to any other work in this record.**

## Bearing on the record

- It stands alone. No THEORY document is affected.
- **No bearing on ML practice.** Nothing here carries an instruction for the Anthology of the SOTA. It is in the reading list as a notable result, and the correct summary is that it disproved Mizohata–Takeuchi and Stein's conjecture, with its proposed local replacement since refuted for many surfaces.

## Limitations

- The loss is only log R. Whether the true loss is a power was left open here; it was answered for many surfaces by Cairo–Zhang, but not (as far as I checked) for the sphere or paraboloid.
- The hypothesis needs "connected" or "curved somewhere" (C6).
- The incidence lemma's proof is terse, with constants tracked only up to ∼. As of the arXiv record, the paper has no journal version (the dossier's Crossref check; I did not recheck).
- The paper does not address what happens to the PDE application (§1.4) beyond noting the historical link.

## Open questions

- **The sharp loss in Mizohata–Takeuchi for the sphere and paraboloid.** Is it log R, a power, or the CIW exponent (n−1)/(n+1)?
- **Whether a corrected Stein-type inequality** (with the loss built in) still combines with Kakeya to give restriction.
- **What survives of the CHV approach** to endpoint multilinear restriction once a power-loss Mizohata–Takeuchi is the best available.

## Corrections to the seeded skim

- **The hypothesis is broader than the proof supports.** Thm 1.2 says "any C² hypersurface Σ that is not a plane" (abstract: "does not lie in a hyperplane"). The proof, Lemma 4.4, writes Σ locally as a graph Φ(ω) = C(ω, ω) + o(|ω|²) and normalises the largest-magnitude eigenvalue of C to 1. That needs **a point where the second fundamental form is non-zero**.
  - A *connected* C² hypersurface not contained in a hyperplane has such a point, so the theorem is fine under the usual convention that hypersurfaces are connected.
  - A compact Σ made of flat pieces lying in different hyperplanes does not. For it, Mizohata–Takeuchi actually holds with constant k (the number of pieces). My argument: Ef = Σᵢ Eᵢfᵢ, |Σ aᵢ|² ≤ k Σ|aᵢ|², and each flat piece gives ∫|Eᵢfᵢ|²w ≤ ‖fᵢ‖² sup_ℓ ∫_ℓ w by Plancherel on the plane.
  
  So "not lying in a hyperplane" should read "connected and not lying in a hyperplane" or "somewhere curved". This is a statement-level slip, not a flaw in the counterexample.
- **The dossier's §1 summary compresses what "closes" means.** The paper's claim (§1.1) is only that the approach of Carbery–Hänninen–Valdimarsson [CHV23] cannot be used. CHV showed that Mizohata–Takeuchi plus Guth's endpoint multilinear Kakeya implies endpoint multilinear restriction without R^ε loss. The paper does not claim endpoint multilinear restriction (Conj. 1.3) is false or harder; it says Conj. 1.3 "cannot be sharpened directly by the Mizohata–Takeuchi conjecture".
- **The dossier's "the local version could still work" (§1.3) needs a date.** The paper leaves Conj. 1.5 (Mizohata–Takeuchi with R^ε loss) open. It says it is "unclear" whether it holds or an R^{(n−1)/(n+1)}-loss counterexample exists (§1.7). Cairo–Zhang (arXiv:2512.08064, abstract only, read 2026-09-26) find a C^k-dense family of compact hypersurfaces, including many strictly convex C² ones, on which Conj. 1.5 **fails with power loss R^α for any α < (n−1)/(n−1+k)**. For C² that is α < (n−1)/(n+1), which matches the Carbery–Iliopoulou–Wang upper bound up to the endpoint. Fenves (arXiv:2606.27020, abstract only) gives another proof and shows that power loss is generic in C^k. So "if Stein's conjecture were true locally, then the Kakeya maximal conjecture would still imply the restriction conjecture" (p. 3) is now a conditional on a hypothesis known to fail for many surfaces. I have not checked whether it fails for the sphere or paraboloid specifically.
- **The dossier's lattice size "|Q| ~ N^{−1/2}2^N" is correct**, but the white-lie estimate (3.5) uses ‖K_ν‖₁ ~ R⁻¹2^N, dropping the N^{−1/2}. The rigorous §3.4 uses |Q| consistently (‖P_νh‖² ≲ R|Q|), and the final ratio is N ≍ log R either way.
- **Typos in the constructions:**
  - S_i is defined with 1_{B_R(ξ_i)} for 1_{B_{R⁻¹}(ξ_i)}.
  - Lemma 3.5(i) lists "c₁(ξ₁−ξ₀) + ⋯ + c_N(ξ₁−ξ₀)" for c_N(ξ_N−ξ₀).
  - Lemma 4.1(i) uses both ξ_m − ξ₁ and ξ_n − ξ₀, and an undefined partition "U₁(1)".
  - Lemma 4.3(ii) has "log_c π_ν(c_{c,n})" for x_{c,n}.
  - "M̃_d(t) = Φ(t, t³, …, t^d)" writes the scalar Φ where the graph point with Φ in the second coordinate is meant.
  - The final sentence of §4.3 reads "proving that R⁻¹ ∼ R⁻¹".
  
  None affects the argument once read charitably.
