---
number: 5
status: Read
formerly:
- NOTE-tmp6kxo3
paper: LIT-028
title: 'Spectral dimensions of bundled networks'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (I read the full text of arXiv:2510.20520v2 (31 Aug 2026),
    13 pp. That is main text pp. 1–5, including all three figures and the
    reference list, plus the Supplemental Material S1–S7, SM pp. 1–8,
    including Figs. S1–S3. Figures 1–3 were rendered and inspected as
    images. I checked every step of the SM derivation (S2, S3, S5, S6, S7)
    by hand. I also ran a numerical check on the Dirac comb: the exact
    spectrum through the per-mode impurity decomposition, for L = 40–320
    (scratchpad g1_check.py). I read the full text of arXiv v1 (23 Oct 2025,
    "Unveiling the Dimensionality of Networks of Networks", 7 pp. including
    End Matter) and compared it with v2 section by section. I could not get
    the typeset PRE Letter (journals.aps.org returned 403). Crossref
    confirms the title, the author list and PRE 114, L022301, published
    online 2026-08-18. v2 was posted after that date under the published
    title, so it is presumably the accepted text, but I have not verified
    that it is identical. Extraction used PyMuPDF (no pdftotext on this
    host); the PDFs are in raw4/2510.20520v1.pdf and v2.pdf.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper studies a "bundled" network, meaning a fiber graph attached at
  one node to every node of a base graph, with base and fiber growing with
  the same length L. For such a network, first-order perturbation theory
  (SM Eq. 10) gives the low spectrum as λ = ℓ^b/N_f, and from that the gap
  ("Fiedler") dimension d_g = 2(d_f,f + d_f,b)/(d_f,f + 2d_f,b/d_g,b),
  while the spectral dimension stays d_s = d_s,f. The two therefore differ
  unless d_g,b = 2 or the fiber is finite. For example, the ring-of-rings
  comb has d_s = 1 but d_g = 4/3, and the 2D-base brush has d_s = 1 but
  d_g = 2. The rule holds only while the base-induced gap lies below the
  fiber's own gap (SM Eq. 14).
---

# NOTE-005: Spectral dimensions of bundled networks

## Contribution

The paper gives a closed-form rule for how the spectral-gap exponent of a bundled network (the "Fiedler dimension", λ_1 ∼ N^{−2/d_g}) follows from the Hausdorff and Fiedler dimensions of its base and fiber:

d_g = 2(d_f,f + d_f,b)/(d_f,f + 2d_f,b/d_g,b), valid in the base-controlled regime.

The known result d_s = d_s,f (Cassi–Regina; Burioni–Cassi) gives the other exponent, so the two dimensions differ generically. Concrete cases are the comb (d_s = 1, d_g = 4/3) and a d-dimensional lattice base with ring fibers (d_s = 1, d_g = 2(1+d)/3). v2 adds two finite-size consequences, for Rouse-type relaxation and for Debye heat capacity: intermediate-time or bulk exponents are set by d_s, and terminal times or crossovers by d_g.

## Key insight

Diagonalize the base first. The bundled Laplacian then splits into N_b independent copies of the fiber, each with a single-site "impurity" at the attachment node whose strength is one base eigenvalue ℓ^b. The whole low spectrum is the base spectrum divided by the fiber size, λ ≈ ℓ^b/N_f. So the gap inherits the base's gap exponent, diluted by N_f. The density of states, however, is dominated by the N_b·N_f fiber modes and inherits the fiber's d_s. The asymptotic exponent (d_s) and the finite-size exponent (d_g) therefore measure different parts of the graph: the bulk of the fibers and the base respectively.

## Assumptions

- **Graph class.** The main result is proved for exactly one class: bundled networks, a single fiber graph attached at node i_2 = 0 to every base node. The Laplacian decomposes exactly as L = L_f ⊗ I + L_b ⊗ P_0, SM Eq. 6. No other composite architecture is treated analytically, despite the title and the outlook.
- **Scaling of the parts.** N_b ∼ L^{d_f,b}, N_f ∼ L^{d_f,f}, N ∼ L^{d_f,b+d_f,f}, with a single common length L, and ℓ^b_1 ∼ N_b^{−2/d_g,b} (SM p. 4). A base that grows at a different rate is absorbed into d_f,b (SM S4).
- **First-order perturbation.** The perturbation parameter is ℓ^b_{n1}, and only the fiber ground state (the constant vector) is expanded (SM Eqs. 8–10). No bound on the error is given. The ring-fiber exact solution shows the expansion holds for ℓ^b ≪ L^{−1} (SM S5).
- **Base-controlled gap.** The gap comes from the base sector only if the fiber-controlled inequality fails: 2d_f,f/d_g,f ≤ d_f,f + 2d_f,b/d_g,b (SM Eq. 14).
- **Homogeneous parts cannot be fiber-controlled.** v2 asserts this with no argument. v1 gave the reason, the bound 2d_f/(d_f + 1) ≤ d_s ≤ d_f, which puts the LHS at ≤ d_f,f + 1 and the RHS at ≥ d_f,f + 2.
- **Finite Hausdorff dimension** of the parts (p. 3). The BA base does not satisfy it: its d_f,b is undefined, and the case is covered only because d_g,b = 2 makes Eq. 6 independent of the Hausdorff dimensions.
- **SM S6–S7 scaling forms.** These assume the low-λ density near λ_1 follows d_s,b, i.e. the base is homogeneous with d_g,b = d_s,b. This is used, not stated.
- **Estimating d_s and d_g numerically.** d_s is read from plateaus of C(τ), which assumes a power-law ρ(λ) at small λ. d_g is read from gap-versus-N fits over finite sizes (Fig. 2a, up to ∼10^7 nodes).

## Key results

- **C(τ) plateau (Eq. 2, p. 2).** C(τ) ≡ −dS/d log τ = −τ² d⟨λ⟩_τ/dτ equals d_s/2 on a scaling plateau when ρ(λ) ∼ λ^{d_s/2−1}, and vanishes for τ ≳ λ_1^{−1}. I checked the identity: S = log Z + τ⟨λ⟩.
- **Homogeneous fractals (p. 2; SM S1; v1 p. 2).**
  - Sierpinski gasket: plateau d_s/2 = 0.684(2) and gap d_g/2 = 0.683(1), against the exact log 3/log 5 ≈ 0.683.
  - Sierpinski carpet: d_s/2 = 0.915(4) and d_g/2 = 0.906(4), against the literature value ≈ 0.903 (d_s ≈ 1.806).
  - The error bars appear only in v1. v2 gives "≃ 0.684 / ≃ 0.683" and "≃ 0.9".
- **Impurity reduction (SM Eq. 7).** Σ_j L^f_{i,j} ψ̃_{n1,j} + ℓ^b_{n1} δ_{i,0} ψ̃_{n1,i} = λ ψ̃_{n1,i}. This is exact.
- **Perturbative low spectrum (SM Eq. 10).** λ_{n1} = ℓ^b_{n1}/N_f, to first order. The derivation sums Eq. 9 over the fiber nodes; the Laplacian columns sum to zero, which gives A = 1/N_f. The derivation is correct.
- **Gap exponent (SM Eqs. 11–12 = main Eqs. 5–6).** λ_1 ∼ N^{−(d_f,f + 2d_f,b/d_g,b)/(d_f,f + d_f,b)} and d_g = 2(d_f,f + d_f,b)/(d_f,f + 2d_f,b/d_g,b).
  - The algebra is correct.
  - d_g = d_g,b if and only if d_f,f(2 − d_g,b) = 0, i.e. d_g,b = 2 or the fiber is finite. The main text states the "only when" correctly.
  - More generally d_g > d_g,b exactly when d_g,b < 2, and d_g → 2 as d_f,f → ∞. Both statements appear only in v1 (p. 4).
  - Comb: d_g = 4/3, stated only in v1. My numerics give a local exponent of 1.349 over L = 40–320.
- **Validity (SM S3, Eq. 14).** The fiber gap λ_{1,f} ∼ N^{−(2/d_g,f)·d_f,f/(d_f,f+d_f,b)} is the smaller one iff 2d_f,f/d_g,f > d_f,f + 2d_f,b/d_g,b. The direction of the inequality is correct.
- **Inhomogeneous comb (SM S4, Fig. S2).** The base has L^α nodes and the fibers have L. The fiber-controlled regime is α < 1/2: at α = 1/3 there is no base plateau, and at α = 4/5 a base plateau appears.
- **Ring fiber, exact (SM S5).**
  - The even modes satisfy 2 sin ω = ℓ^b cot(ωL/2), with λ = 2(1 − cos ω). I re-derived this.
  - For ℓ^b ≪ L^{−1}, ω ≃ √(ℓ^b/L) and λ ≃ ℓ^b/L, which recovers Eq. 10.
  - For ℓ^b ≳ L^{−1}, which is the typical case since most base eigenvalues exceed 1/L, the solution is ω ≈ π/L and λ ≈ π²/L². This gives an extensive quasi-degeneracy, which the paper blames for the size-divergent peak in C(τ). That attribution is an informal argument ("one can show", v1 p. 7). No calculation of C(τ) from the degeneracy is given.
- **Relaxation (p. 3; SM S6).**
  - G(t) = N^{−1} Σ e^{−λ_k t}. It decays as t^{−d_s/2} at intermediate t and is cut off at τ_eq ∼ λ_g^{−1} ∼ N^{2/d_g}.
  - The homogeneous finite-size form (SM Eq. 24) is correct.
  - The composite form (SM Eq. 25) has the wrong prefactor; the correct one is N^{−1}. See corrections.
- **Debye heat capacity (p. 4; SM S7).**
  - C_V ∼ T^{d_s} at low T in the thermodynamic limit, with a finite-size crossover at T_c ∼ N^{−1/d_g}.
  - The homogeneous form (SM Eq. 28) is correct.
  - The composite form (SM Eq. 29) has the wrong prefactor; the correct one is N^0. See corrections.
- **Numerical validation of Eq. 6 (Fig. 2).**
  - Lattice bases of d = 1–4 with ring fibers fall on the curve 2(1+d)/3. Fig. 2(a) shows the local-exponent deviation still at ∼10^{−2} to 3·10^{−2} at 10^6–10^7 nodes for d = 3 and 4, and decreasing.
  - "Fractal-tree bases" with ring fibers (triangles) lie at d_g ≈ 1.5–1.6 for d_f,b ≈ 2–3. The trees' construction and their d_g,b are not given anywhere, in either version.
  - BA bases give d_g ≈ 2.0 with either fiber.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In a bundled network the low Laplacian spectrum is λ_{n1} = ℓ^b_{n1}/N_f to first order | strong | Derivation, SM S2 Eqs. 6–10. Exact in the ring case for ℓ^b ≪ 1/L (SM S5). My numerics give a ratio to the exact gap of 0.92→0.99 over L = 40–320 on the comb |
| C2 | Composite Fiedler dimension d_g = 2(d_f,f + d_f,b)/(d_f,f + 2d_f,b/d_g,b) | strong within the base-controlled regime; the main text states it without that condition | Algebra from C1 plus the scaling assumptions (SM Eqs. 11–12). The validity condition is SM Eq. 14 |
| C3 | d_s = d_s,f for bundled networks | moderate | Cited prior work [15, 25], plus an informal impurity argument (p. 3). C(τ) plateaus in Figs. 1 and 2 are consistent with it |
| C4 | Spectral and Fiedler dimensions coincide in homogeneous networks (gasket, carpet) | moderate | Numerics (SM S1, v1 errors ±0.001–0.004) and cited [16, 22]. Two examples, not a proof |
| C5 | Homogeneous base and fiber can never be fiber-controlled (Eq. 14 cannot hold) | moderate in v1 (a one-line argument from 2d_f/(d_f+1) ≤ d_s ≤ d_f); assertion in v2 | v1 End Matter p. 6; v2 SM S3 |
| C6 | Numerical gap scaling agrees with Eq. 6 "in all cases" across lattice-, tree- and BA-based families | moderate | Fig. 2. Finite-size deviations are still ∼10^{−2} for d = 3, 4. The tree bases are unspecified, so that series cannot be reproduced |
| C7 | BA bases have "effective d_g,b = 2", so d_g is unchanged | weak | Asserted (p. 3). The BA parameters are not given. Fig. 2(b) inset shows d_g ≈ 2.0, and its caption mislabels it as d_s |
| C8 | The size-divergent peak in C(τ) comes from the extensive quasi-degeneracy at λ ≈ π²/L² | weak | Informal argument (SM S5; v1 "one can show") for ring fibers only |
| C9 | Relaxation G(t) ∼ t^{−d_s/2} at intermediate times, with equilibration τ_eq ∼ N^{2/d_g} | strong for the exponents | Laplace asymptotics (SM Eqs. 22–23) and the definition of d_g. Fig. 3 comb vs brush |
| C10 | Composite finite-size forms: G ∼ N^{−d_s,b/d_g} t̄^{−d_s,b/2}Γ(·) and C_V ∼ N^{1−d_s,b/d_g} T̄^{d_s,b} f(T̄) | weak; the prefactors are incorrect | SM Eqs. 25, 29. The correct prefactors are N^{−1} and N^0 (my derivation, and numerics on the comb). The t̄ and T̄ scaling variables and the d_s,b exponents are right |
| C11 | "Networks with identical thermodynamic exponents can exhibit parametrically different equilibration dynamics" (abstract) | strong as an existence claim | Comb vs brush: d_s = 1 for both, with d_g = 4/3 vs 2 |
| C12 | The decoupling is "a generic geometric property of composite architectures rather than a feature of specific models" (p. 3) | weak | Shown only for bundled graphs (one fiber per base node, single attachment point). The generalization is an assertion, and the outlook itself calls the construction "a minimal controlled setting" (p. 5) |
| C13 | The mechanism explains multimodal and double-scaling relaxation seen in polymer rheology [47–51] | weak | Suggested by analogy (p. 4). No polymer data is analysed |

## Method

1. **Spectral heat capacity.** Compute C(τ) from the full Laplacian spectrum (LRG density matrix, Eqs. 1–2), and read d_s from its plateaus and λ_g from its large-τ cutoff.
2. **Gap scaling.** Fit λ_1 against N over a family of sizes to get d_g.
3. **Analysis of the bundled Laplacian.** Rotate into the base eigenbasis to get N_b independent fiber-with-impurity problems (SM Eq. 7). Then do first-order perturbation in the impurity strength, summing the eigen-equation over fiber nodes (SM Eqs. 8–10). Insert the power-law scaling of N_b, N_f and ℓ^b_1 (Eqs. 11–12). Compare with the fiber's own gap to get the validity regime (Eq. 14). Check against the exact ring solution (SM S5).
4. **Physical consequences.** Plug the two-sector spectrum into Rouse / generalized-Gaussian-network relaxation and a Debye model (SM S6–S7).

## Concepts

- **Spectral dimension d_s** — defined by ρ(λ) ∼ λ^{d_s/2−1} as λ → 0 in the thermodynamic limit.
- **Fiedler (gap) dimension d_g** — defined by λ_1 ∼ N^{−2/d_g} as N grows. The paper attributes it to Fiedler 1973 [21]; the exponent name is the authors'.
- **Asymptotic vs mesoscopic** (v2 title) — "asymptotic" means d_s (the N → ∞ spectral density); "mesoscopic" means d_g (finite-N gap scaling).
- **Bundled network** — a copy of the fiber graph glued at its node 0 to each base node [Cassi–Regina 1996].
  - **Dirac comb**: a ring of rings.
  - **Dirac brush**: a 2D periodic lattice base with ring fibers.
- **Spectral heat capacity C(τ)** — −dS/d log τ for the Laplacian density matrix ρ(τ) = e^{−τL}/Z. v1 also calls it the "entropic susceptibility".
- **d_f,b, d_f,f** — the Hausdorff (fractal) dimensions of base and fiber in terms of the common length L. In SM S4, d_f,b is redefined as the base growth exponent α.
- **Fiber-controlled regime** — the fiber's own gap is below ℓ^b_1/N_f (SM Eq. 14). Eq. 6 then fails and the gap is fiber-set.

## Connections

The paper builds on the Parma group's work on bundled structures and their spectral dimension:
- Cassi–Regina 1996 and 1997: d_s = d_s,f.
- Burioni–Cassi 1996 and 2005, on spectral dimension on graphs.
- Burioni et al. 2000–2002, on the base-diagonalized eigen-equation.

It is also built on the CREF group's Laplacian Renormalization Group (Villegas et al., Nat. Phys. 2023; PRR 2022, 2025). It relies on Villegas PRE 2025 and Poggialini et al. PRL 2025 for "C(τ) plateau = d_s/2" and for "d_g = d_s in homogeneous networks". The gap-dilution mechanism λ ≈ ℓ^b/N_f is a first-order projection onto the fiber's zero mode, like a star-product or "attached graph" argument. Its novelty lies in extracting the scaling rule and naming the resulting exponent split.

**What changed from v1 to v2** (v1: 23 Oct 2025, 7 pp.; v2: 31 Aug 2026, 13 pp.):

- **Title and framing.** "Unveiling the Dimensionality of Networks of Networks" became "Asymptotic versus mesoscopic spectral dimensions in networks and inhomogeneous structures".
  - The v1 abstract's "by composing scale-invariant networks, we show how tinkering decouples Fiedler and spectral dimensions, hitherto considered identical" became "modular compositions generically decouple the spectral and Fiedler dimensions, so that networks with identical thermodynamic exponents can exhibit parametrically different equilibration dynamics".
  - v1 said "we provide evidence"; v2 says "we show"/"demonstrate".
  - v2 adds a single-parameter-scaling framing: the thermodynamic and long-time limits "need not commute".
- **Structure.**
  - v1's End Matter became SM S2, S3, S4 and S5: the perturbation theory, the validity condition, the inhomogeneous comb (Fig. 4 → Fig. S2) and the ring fiber.
  - v1 Fig. 1 (Sierpinski) moved to SM Fig. S1 and SM S1.
  - v1 Figs. 2 and 3 became v2 Figs. 1 and 2.
- **New in v2.**
  - Main-text paragraphs on Rouse / generalized-Gaussian relaxation and on Debye heat capacity, with a new Fig. 3 (G(t) for comb vs brush and its finite-size collapse).
  - SM S6 and S7 (Eqs. 19–29, Fig. S3).
  - The claim that Eq. 6 is "independent of the microscopic details" given finite Hausdorff dimension.
  - The closing caveat that the construction is "a minimal controlled setting".
  - The polymer-rheology connection [47–51].
- **Removed in v2.**
  - The error bars on the fractal estimates.
  - The worked comb value d_g = 4/3.
  - The general statement that d_g ≷ d_g,b as d_g,b ≶ 2.
  - The large-d_f,f limit d_g → 2.
  - The v1 justification (2d_f/(d_f+1) ≤ d_s ≤ d_f) for why homogeneous parts cannot be fiber-controlled; v2 only asserts it.
  - The ring-fiber discussion of odd modes (sin(ωi_2), unaffected by the impurity).
  - v1's claims of "a rigorous analysis" and "the first evidence of an anomalous Fiedler dimension".
  - The applied outlook (neuromorphic circuits, modular software).
  - v1's claim that "recursive application of Eq. (6) can capture the dimension of hierarchical composite structures". v2 softens this to "suggests a natural extension".
- **Fixed in v2.** v1's text said Figs. 3(a,b) compare the "spectral dimension" with Eq. 6. v2 correctly says "spectral gap".
- **Introduced or retained in v2.**
  - The "d_s = log 3/log 5" typo in the main text is new.
  - The Fig. 2(b) inset is still captioned as spectral dimension.
  - The pointer for tree bases now goes to "SI4 and SI5", which contain nothing on trees; v1 pointed to "end matter", which did not either.
  - The SM still carries v1's outdated affiliations (INFM; the old Parma address).
  - N_carpet(n) = 2^{n+3} (Fig. S1 caption, also in v1) cannot describe a carpet whose node count grows about 8-fold per generation. Probably a typo; unverified.
- **Unchanged.** The core derivation (Eqs. 3–7 of v1 = SM Eqs. 6–12 of v2) is unchanged apart from notation.

## Bearing on the record

This is [LIT-028](../literature.d/LIT-028.md); the existing skim is NOTE-005, which this reading replaces. The nucleation record has no THEORY documents yet. A theory this paper could source would be: "A Laplacian's gap exponent and its density-of-states exponent are distinct invariants, and they coincide only in homogeneous geometries." It would be restricted, as the paper's proof is, to bundled graphs in the base-controlled regime.

**For ML practice: nothing.**
- The paper makes no ML claim, and no instruction for practice follows from it.
- The closest anthology material uses a spectral gap to set a mixing timescale ([ANTH-THEORY-056](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-056.md), on statistics of long random sequences). This paper's message is consistent with that: the gap sets terminal equilibration, not intermediate-time decay. But it neither supports nor bears on that document.
- Any link to graph-diffusion or spectral-GNN practice (graph size dependence of oversmoothing or diffusion time, say) would be the reader's extrapolation, not something the paper shows.

Record hygiene: none needed on dates. [LIT-028](../literature.d/LIT-028.md)'s `published: '2025-10-01'` is the arXiv posting month, which is what the field records (v1 was posted 23 Oct 2025).

## Limitations

- **Narrow analytic scope.** The analysis covers one fiber type per base node, a single attachment point, no disorder, and a common scaling length. "Networks of networks" and "inhomogeneous structures" in the titles, and "generic geometric property of composite architectures" (p. 3), claim more than this.
- **Validity condition kept in the SM.** The main text states Eq. 6 without the condition in SM Eq. 14. v2 asserts, without an argument, that the condition cannot be violated for homogeneous parts.
- **Wrong finite-size prefactors.** The finite-size scaling functions for composites (SM Eqs. 25, 29) have wrong N prefactors, off by N^{1−d_s,b/d_g} (for the comb, N^{1/4}). The brush example cannot detect this because there d_s,b = d_g.
- **Unreproducible numerics.** The fractal-tree bases and the BA parameters are unspecified. The BA base has no finite Hausdorff dimension, and its "effective d_g,b = 2" is asserted.
- **No real-world network or experimental data.** The polymer-rheology and vibrational links are suggestions.
- **Caption and label errors.** The Fig. 2(b) inset is mislabeled as spectral dimension. Fig. 3's axis reads "G(t)/N" where the plotted quantity appears to be N·G, and its legend has "t^{d_s,B/2}" missing a minus sign. The main text has the gasket d_s typo.
- **C(τ) peak.** The diverging-peak explanation is informal.

## Open questions

- Eq. 6 for multiple attachment points, heterogeneous or random fibers, or fibers whose size varies across the base. Would a distribution of N_f change the gap exponent?
- Does recursive (hierarchical) composition really produce the "hierarchy of effective dimensions" the outlook suggests? Applying Eq. 6 recursively would need the composite's own d_g and its fiber-dominated d_s ≠ d_g as inputs. The single-base assumption d_g,b = d_s,b used in S6–S7 then fails.
- A rigorous error bound on λ_{n1} = ℓ^b_{n1}/N_f beyond the ring case. The Rayleigh upper bound holds generally. A matching lower bound in terms of the fiber gap would make C2 a theorem.
- Corrected finite-size scaling forms for composites, prefactors N^{−1} and N^0, checked on a case with d_s,b ≠ d_g such as the comb.
- A specification of the tree and BA bases used in Fig. 2, including BA's m, and whether BA's d_g,b = 2 holds or its gap stays open for m ≥ 2.

## Corrections to the seeded skim

- **Composition rule.** The dossier's formula is correct and matches both versions (main Eq. 6 = SM Eq. 12 = v1 Eq. 7). The main text's "λ_k ∼ ℓ^b_k/N_f" is an equality at first order in the SM (Eq. 10). The Rayleigh quotient of the constant fiber vector also makes it an exact upper bound on each sector's lowest eigenvalue. That bound is my observation, not the paper's. On the comb, λ_1/(ℓ^b_1/N_f) = 0.92, 0.96, 0.98, 0.99 for L = 40, 80, 160, 320 (my numerics).
- **Validity condition.** The dossier asked whether Eq. 6 survives when base and fiber do not grow together. It does, as long as the base sector sets the gap. SM S4 handles a base growing as L^α by treating α as d_f,b. Eq. 6 fails in the "fiber-controlled" regime of SM Eq. 14, 2d_f,f/d_g,f > d_f,f + 2d_f,b/d_g,b. For the comb that regime is α < 1/2, and there the base plateau in C(τ) disappears (Fig. S2). The main text never states this condition. It says only that the rule "applies to controlled modular compositions" provided the parts have finite Hausdorff dimension (p. 3).
- **Finite-size scaling prefactors.** The dossier summarizes SM S6–S7 as "equilibration time ∼ N^{2/d_g}". That part is right. But the finite-size scaling forms given there, SM Eq. 25, G(t,N) ∼ N^{−d_s,b/d_g} t̄^{−d_s,b/2} Γ(d_s,b/2, t̄), and Eq. 29, C_V ∼ N^{1−d_s,b/d_g} T̄^{d_s,b} f(T̄), have the wrong N prefactor for a composite network:
  - My derivation from the paper's own Eq. 10 and Eq. 21 gives N^{−1} for G and N^0 for C_V. This assumes a homogeneous base, d_g,b = d_s,b, which the paper also uses implicitly.
  - Numerics on the comb confirm it. At fixed t̄ = λ_1 t, N·G is constant (0.831, 0.795, 0.783, 0.778 at t̄ = 1 for L = 40…320) while N^{3/4}·G is not.
  - The paper's prefactors are the homogeneous ones with d_s replaced by d_s,b. They agree with the correct ones only when d_s,b = d_g, which is true of the brush that SM Fig. S3 plots, so the figure cannot expose the error.
  - Main-text Fig. 3(b) labels its y-axis "G(t)/N", but its values (∼1 at t̄ ≈ 0.1) look like N·G, which is the correct collapse.
- **Fig. 2(b) inset.** The caption (and v1's) calls the inset "spectral dimension for BA networks … confirming that d_s is fiber-controlled". The inset's y-axis is d_g, and its value is ≈ 2.0 for both ring and random-tree fibers. A ring fiber has d_s = 1, so the inset shows the Fiedler dimension, as v1's text says (the "special case d_g,b = 2"). It does not show d_s being fiber-controlled.
- **Published date.** v1 was posted on 23 Oct 2025, which [LIT-028](../literature.d/LIT-028.md) records at month precision as `2025-10-01`, per the field's convention; the PRE Letter was published online 18 Aug 2026.
- **Gasket value.** The main text (v2 p. 2) states the gasket's "exact value d_s = log 3/log 5". That is d_s/2. SM Eq. 3 and v1 correctly give d_s = 2 log 3/log 5 ≈ 1.365. This typo was introduced in v2.
