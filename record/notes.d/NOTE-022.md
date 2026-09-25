---
number: 22
status: Read
formerly:
- NOTE-tmpowjkv
paper: LIT-017
title: 'Spectral Networks and Betti Lagrangians'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2504.08144v1 (10 Apr 2025; still the
    only arXiv version when checked 2026-09-25), 150 PDF pp., extracted with
    PyMuPDF into raw4/2504.08144.txt (no pdftotext on this host). Read end
    to end: §1 (Theorems 1–5), §2.1–2.7, §3.1–3.6 (proofs of Theorem
    1(i)/(ii), Lemmas 3.19, 3.23), §4.1–4.3 (Propositions 4.3, 4.13),
    §5.1–5.4 (Proposition 5.20, Theorem 5.24, both halves of the proof of
    Theorem 2), §6.1–6.4 (Propositions 6.6, 6.19, Theorem 6.12, the §6.4.2
    conjecture), §7.1–7.3 (all five worked examples) and Appendix A.1–A.3
    (every step of Theorem A.3). Figures 1–28 came through only as captions,
    so the flowline-to-term matchings in §7.3 and the local models in
    Figures 2, 6, 9–12, 18 are pictorial claims I could not see. The
    121-entry bibliography was checked for structure and for the entries the
    arguments rely on (Ekh07, Nho24, GMN13b, GPS20, GPS24b, EHK16, Kuw24). I
    am not a Floer-theory specialist; the check/can't-check boundary is
    under Limitations.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-25'
summary: >-
  For any rank n, and for Lagrangians with non-algebraic (positive-braid)
  asymptotics, spectral networks exist and are characterised by
  pseudo-holomorphic strips in the adiabatic limit (Theorems 1–2). For
  exact Betti Lagrangians, a Family Floer functor equals
  Gaiotto–Moore–Neitzke non-abelianization in the adiabatic limit (Theorem
  3, i.e. 5.24) and is realised by A∞-operations in wrapped and partially
  wrapped Fukaya categories of T*S (Theorem 4). The analysis in §§4–5
  leans on Ekholm 2007 and on the second author's 2024 preprint, and
  Theorem 5 (spectral networks from Demazure weaves) is recorded without a
  written proof.
---

<!-- inactive-ok-file: LIT-017 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-022: Spectral Networks and Betti Lagrangians

## Contribution

The paper moves spectral networks, in physics defined for meromorphic spectral curves in the holomorphic cotangent bundle of a Riemann surface, into real symplectic topology.

- **A new setting.** It defines Betti surfaces (a punctured surface with a Legendrian positive-braid link at each puncture) and Betti Lagrangians (Lagrangian n-fold branched covers of S in T*S with those asymptotics). It also defines Morse spectral networks as gapped limits of consistent extensions of pre-spectral networks (Definitions 2.3, 2.6, 3.5, 3.10–3.12).
- **Five results about that setting:**
  - existence of such networks (Theorem 1);
  - their characterisation by pseudo-holomorphic strips in the adiabatic limit (Theorem 2);
  - a Family Floer functor equal to GMN non-abelianization for exact Betti Lagrangians (Theorem 3);
  - an A∞-categorical upgrade: the Yoneda module µ^{1|1} and the partially wrapped µ² recover the non-abelian parallel transport (Theorem 4);
  - a combinatorial construction of spectral networks from Demazure weaves, whose flowlines match the terms of the Legendrian DGA augmentation (Theorem 5, with worked examples in §7.3).
- **Side results:**
  - an invariance theorem for soliton classes over Reeb paths (Theorem 5.8);
  - a generation result for W(T*S, Λ) by an interior fibre and fibres at infinity (Proposition 6.19);
  - an appendix proving a truncated reverse isoperimetric inequality (Theorem A.3), which patches a gap the authors identify in Ekholm 2007.

## Key insight

A spectral network is the adiabatic shadow of Floer theory. Scale the Lagrangian L ⊂ T*S by ε → 0. Pseudo-holomorphic strips between εL and a cotangent fibre T*_zS then degenerate to gradient flow trees of the sheet-difference functions (D₄⁻-trees). A point z lies on a wall of the network exactly when such a strip exists in the limit.

Once walls are Floer-theoretic, GMN's "detour" corrections to parallel transport become continuation-strip counts in Family Floer cohomology. Their invariance, well-definedness and categorical structure then follow from Floer theory, rather than from hand-checked combinatorics (§1 B–C, §5).

## Assumptions

- **Betti surface** (Definition 2.3). S is a smooth closed oriented surface with marked points m. Each puncture carries a Legendrian link in T^∞S that is the circular closure of an n-stranded positive braid. After a C^∞-small isotopy, Reeb chords and front double points occur at distinct angles (§2.2).
- **Betti Lagrangian** (Definitions 2.6–2.7):
  - a weakly bounded Lagrangian multigraph whose projection to S is a degree-n simple branched cover with finitely many branch points;
  - near each branch point it is locally the real part of {(λ_C − c)² = z dz²}, i.e. the D₄⁻ germ (§2.3, p. 19);
  - its smooth sheets are assumed holomorphic near branch points, with a Kähler metric there (§3.1.1).
- **The two classes:**
  - (i) exact, with conical ends of the form (x(θ), f(r)y(θ), r, f′(r)z(θ)), f linear at infinity (Definitions 2.8–2.9);
  - (ii) meromorphic spectral curves with O(−1)-ends: sheet differences grow at least like z⁻¹ (Definition 2.10, Eq. 9).
- **Metrics:**
  - polar r²dθ² + dr² near punctures in the exact case;
  - |z|⁻²|dz|² near poles in the meromorphic case;
  - perturbed generically (open dense) to remove tangencies and trajectories passing through other branch points (§3.3, via [Ekh07, §3.2] and Smale);
  - in §6, rescaled so that inj(g) > 2 and modified to be a product near a good cover (§6.2.1).
- **Theorem 1(ii):** generic phase θ in a countable intersection of open dense subsets of S¹. Only holomorphic perturbations and θ-rotations are allowed (§3.4).
- **Theorems 3–4 and most of §§5–6:** exact Betti Lagrangians. In the proofs the spectral network is also finite and creative (Definition 5.29, Proposition 5.30).
- **§6.4:** Legendrians at infinity are Reeb-positive with finitely many Reeb chords.
- **§7:** S = S² with one puncture and braid βδ(β), δ(β) = w₀, with a right-bent Demazure weave.
- **Lemma 5.13:** Betti Lagrangians are Maslov 0, used for vanishing Floer differentials (Proposition 5.12(4)). Twisted local systems (monodromy −1 around the circle fibre) are used throughout §5, and spin structures in §6 (Appendix A.3).

## Key results

- **Theorem 1 (existence).**
  - (i) Every exact Betti Lagrangian with an adapted metric admits a *finite* Morse spectral network, which the proof produces with creation vertices only.
  - (ii) For a meromorphic spectral curve with O(−1)-ends and a dense set of phases θ, e^{iθ}Σ admits a (gapped) WKB spectral network.
  - The proof runs as follows:
    - flow out of each branch point along the three initial rays;
    - repeatedly add the flowline born at each inconsistent vertex (consistent extension);
    - show gappedness: a rigid D₄⁻-tree with |V(Γ)| internal vertices has flow-energy E > ⌊|V(Γ)|/N⌋ℏ, since chain-interaction trees near a branch point have at most N internal vertices (Propositions 3.17–3.18);
    - show finiteness from exactness, since the primitive of λ_st on L is bounded (Proposition 3.18).
  - In case (ii), the claim is that GMN's heuristic procedure terminates and outputs a gapped network (p. 8).
- **Theorem 2 (Floer characterisation).** Given a spectral network W compatible with a Betti Lagrangian Σ, p lies on an active wall of W iff there is a broken pseudo-holomorphic strip between T*_pS and Σ in the adiabatic limit.
  - (i) Its relative class is the soliton class determined by W, and the strip degenerates into W.
  - (ii) For exact Σ the strip is unbroken.
  - "⇐" comes from Theorem 4.2: z ∉ W means uniformly disk-free, and z ∈ W means uniformly Stokes. That in turn rests on Proposition 4.3: ε-strips converge to *trimmed* D₄⁻-trees.
  - "⇒" is §5.4: via Proposition 5.30 in the exact case, via Propositions 5.35–5.37 in the meromorphic case.
- **Theorem 3 (= Theorem 5.24).** For exact L:
  - (1) the Family Floer functor F : Loc†(L) → Loc†(S) is well defined and invariant under compactly supported Hamiltonian isotopy;
  - (2) in the adiabatic limit, F ≃ Φ_W, the GMN non-abelianization, where Φ_W is defined.
  - Corollary (Theorem 5.8): the soliton classes over Reeb paths are invariants of L up to compactly supported Hamiltonian isotopy.
- **Theorem 4 (= Proposition 6.1, Theorem 6.3, Corollary 6.4, Theorem 6.12, Corollary 6.13).**
  - (i) There is an A∞-module Y_(L,V) over the wrapped category W(T*S) with H*(Y(P)) ≅ HF*(P,(L,V)), and µ^{1|1}([α_zw], ·) = Φ_W(V)(α_zw) for the minimal-geodesic generator of a W-adapted pair. Hence Y_(L,V) ≃ Φ_W(V) as modules, using Abouzaid's prior equivalence W(T*S)-mod ≅ C_{−*}(Ω_zS)-mod.
  - (ii) For the cylindrization L° ∈ W(T*S, Λ), µ²(i_*[α_zw], ·) = Φ_W(V)(α_zw) and Y_(L°,V) ∘ i_* ≃ Y_(L,V).
- **Proposition 6.19.** W(T*S, Λ) is generated by an interior cotangent fibre and the fibres at infinity F_m, for Reeb-positive Λ. Here Y_(L°,V) vanishes on the F_m and equals ℤ on each linking disk.
- **Theorem 5 (= Proposition 7.5).** For a Demazure weave w, the combinatorial "augmentation forest" W_w (Definition 7.4) is a finite, creative Morse spectral network compatible with the weave filling L_w. Its flowlines are the adiabatic D₄⁻-tree limits of the rigid strips counted by the augmentation ε_w.
  - Worked examples (§7.3):
    - β = σ₁⁶, with ε_w given term by term;
    - the σ₁³ mutation, checked against the cluster exchange relation A₁A₁′ = 1 + (z₂z₃ − 1) ⇒ A₁′ = z₃;
    - the Berk–Nevins–Roberts network;
    - a Reidemeister-III cancellation pair (Ψ_R3(z₂) = z₂ ± z₁z₃);
    - β = (σ₂σ₁)³σ₂, the max-tb trefoil in 3 strands, with ε_w in Eq. 41.
- **§6.4.2 (conjecture and a claimed consequence).**
  - The authors conjecture a commuting triangle between W(T*S, Λ), Loc(L) and Stokes local systems.
  - They then say it commutes for Reeb-positive Λ "by Theorem 6.12", and that the non-abelianization functor is injective on objects, "which was conjectured by the original works [GMN12; GMN13a]".
  - The injectivity argument is two sentences: HW*((L°,V),(L°,V′)) is Morse cohomology twisted by V*⊗V′.
- **Theorem A.3.** A truncated reverse isoperimetric inequality: boundary length outside N_{2δ}(K) is ≤ T·E for J-holomorphic curves of energy ≤ E with boundary on L ∪ K.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every exact Betti Lagrangian admits a finite (creative) Morse spectral network | moderate–strong | proof §3.3 (Propositions 3.17–3.18); relies on [Ekh07, §3] for chain-tree bounds and on generic metric perturbation |
| C2 | For a dense set of phases a meromorphic spectral curve admits a gapped WKB spectral network (GMN's procedure terminates) | moderate | §3.4, Lemma 3.19 (θ-deformation removes tangencies); says Proposition 3.18 "also works in this setting", though its Proposition 3.17 step used a C^∞ perturbation of L that §3.4 says is not allowed; see also [Kuw24] |
| C3 | Points off W are uniformly disk-free; on W, only soliton classes occur (Theorem 4.2) | moderate | §4 proof via Proposition 4.3; the technical steps are by reference to [Ekh07, §5] and [Nho24, §5]; limits are only *trimmed* trees (footnote 13); a gap in [Ekh07, Lemma 5.4] is patched by Theorem A.3 |
| C4 | On every wall there is a strip in the adiabatic limit (Theorem 2 "⇒") | moderate (exact) / weak–moderate (meromorphic) | §5.4.1 via creativity and nonvanishing BPS indices; §5.4.2 open–closed argument, the "closed" step citing [Nho24, Proposition 4.4] for non-emptiness |
| C5 | Family Floer functor F ≃ Φ_W for exact L, adiabatically | moderate | Theorem 5.24; the proof at creation joints is a short paragraph ("the trivial loop … is contractible"); assumes finite creative W |
| C6 | Soliton classes over Reeb paths are Hamiltonian invariants | moderate | Theorem 5.8 via Theorem 5.24 and [EHK16] flow-tree/disk bijection + Maslov 0 (Lemma 5.13) |
| C7 | Non-abelian parallel transport = µ^{1|1} on the Yoneda-type module (wrapped) and µ² on the cylindrization (partially wrapped) | moderate | Theorems 6.3, 6.12 via Proposition 6.6 (explicit Hamiltonians H_k, action argument) and GPS sectorial descent; Proposition 6.11's proof is two sentences |
| C8 | W(T*S, Λ) is generated by interior + infinity fibres | moderate | Proposition 6.19 via GPS wrapping exact triangle and Lemma 6.21 grading/locality |
| C9 | Weave-built W_w is a Morse spectral network whose flowlines are adiabatic limits of augmentation strips (Theorem 5) | weak | Proposition 7.5 stated without proof; supported by worked examples whose flowline-to-term matching is shown in figures |
| C10 | W_{w_bnr} coincides with the Berk–Nevins–Roberts network | weak | visual comparison of Figure 22 with [BNR82, Fig. 1] |
| C11 | Non-abelianization is injective on objects (GMN conjecture) | weak | two-sentence argument in §6.4.2, inside a section whose main diagram is conjectural |
| C12 | [Ekh07, Lemma 5.4] has a gap; Theorem A.3 fills it | moderate | Remark 4.10(i); proof of Theorem A.3 in Appendix A.2 (coarea + plurisubharmonicity), four steps |
| C13 | Betti Lagrangians are Maslov 0 | weak–moderate | Lemma 5.13, a three-sentence argument (εL is nearly holomorphic on compacta) |

## Method

1. **Flow trees and networks (§§2–3).**
   - Model flowlines of sheet differences f_i − f_j: 1D near Reeb chords (Lemmas 2.15–2.16), and near D₄⁻ branch points, with three initial rays at angles 0, ±2π/3.
   - Control ends with a trapping lemma (Lemma 2.18 conical; Lemma 2.26 meromorphic, via the cameral cover and quadratic-differential results of Strebel).
   - Build networks by iterated consistent extension. Bound the energy via chain-interaction trees. Obtain transversality either from metric perturbation (exact case) or from θ-deformations of flat coordinates (Lemma 3.19, meromorphic case).
2. **Adiabatic analysis (§4).**
   - Reparametrise ε-strips on slit domains Δ_m(ε).
   - Cover the domains by regions with |∇u_ε| = O(ε) or with image near branch points, following [Ekh07, §5] and [Nho24, §5].
   - New step: near a branch point b, a Stokes-theorem computation (Eqs. 22–24) forces the limiting cusp-cusp flowline to satisfy ±z(v)^{3/2} ∈ ℝ₊, hence to lie on an initial ray (Proposition 4.13).
3. **Family Floer (§5).**
   - Stalks CF(T*_zS, εL) = ⊕ V_{z_i}, concentrated in degree 0 by Maslov 0.
   - Parallel transport by counting deformed continuation strips with a moving fibre boundary (Eq. 27), oriented via sphere-bundle lifts (twisted local systems).
   - Small strips are cobordant to trivial ones (Lemma 5.28); off W, only small strips (Proposition 5.30(i)); across W, only detour classes (Proposition 5.30(ii)).
   - Match with Φ_W via the 2d Hori–Vafa wall-crossing recursion (Definition 3.20).
4. **Fukaya categories (§6).**
   - Add L formally as the most negative object in the GPS poset construction (Proposition 6.1).
   - Compute wrapped morphisms between nearby fibres with explicit quadratic-then-linear Hamiltonians, so the minimal geodesic survives wrapping (Proposition 6.6).
   - Cylindrize L via a Weinstein neighbourhood of the surgered zero section plus conormal circles (Definition 6.14).
   - Compare stopped and unstopped wrapping by an action filtration (Proposition 6.18).
5. **Weaves (§7).** Scan the trivalent vertices bottom-to-top, emit three flowlines per vertex, route them along weave edges, and add creation flowlines to make each stage consistent (Definition 7.4).

## Concepts

- **Betti surface / Betti Lagrangian** — as under Assumptions. "Betti" refers to the Betti side of wild non-abelian Hodge theory: the Legendrian links are the contact-topological form of Stokes data (Example 2.5).
- **D₄⁻-singularity** — the real part of the holomorphic cusp {w² = z}, i.e. a simple branch point of L → S. It has three "initial rays".
- **D₄⁻-tree** — a rooted Morse flowtree whose leaves end on initial rays at branch points. Its root is a branch point (a "4d BPS state"), a fibre point z (a "vanilla 2d-4d BPS state"), or a Reeb chord (an "augmented D₄⁻-tree", the authors' own term). Its relative cycle is its **soliton class**.
- **Pre-spectral network** — a finite directed graph of ij-flowlines with initial, interaction (creation or 6-valent), non-interaction and inconsistent vertices, which is flow-acyclic.
- **Consistent extension** — adding the new walls born at inconsistent vertices. **Gapped:** the minimal soliton energy of the new points grows at least like ⌊m/M⌋ℏ.
- **Morse spectral network** — a gapped sequence of consistent extensions. **Finite** if it stabilises; **creative** if every interaction vertex is a creation vertex.
- **Active wall** — a wall with non-zero vanilla 2d-4d BPS index µ (Definition 3.20).
- **Adiabatic limit** — ε → 0 under fibrewise scaling εL. **Uniformly disk-free / uniformly Stokes** (Definition 4.1).
- **Detour path** — the homotopy class that follows ρ to a wall, runs around the soliton and continues (Definition 5.5).
- **Augmentation forest W_w** — the combinatorial network built from a Demazure weave (Definition 7.4).

## Connections

The paper:
- formalises Gaiotto–Moore–Neitzke's spectral networks and non-abelianization [GMN12–14];
- extends the rank-2, quadratic-differential results of Casals–Murphy [CM18] and Nho [Nho24] to all ranks using Legendrian weaves [CZ22];
- adapts Ekholm's flow-tree/holomorphic-disk correspondence [Ekh07] to the non-generic D₄⁻ front singularity (Lemma 3.23, "sneaky trees");
- uses the Ganatra–Pardon–Shende partially wrapped Fukaya categories [GPS20, GPS24a, GPS24b] and Abouzaid's generation and loop-space results [Abo11a, Abo12];
- connects to cluster structures on braid varieties [Cas+24, Cas+25], so that Donaldson–Thomas / BPS-monodromy computations can be read off weaves.

Kuwagaki's sheaf-quantization existence result [Kuw24] is cited as parallel work for the WKB case of Theorem 1(ii).

Within this record it has no technical neighbours. It shares the word "spectral" with [LIT-011](../literature.d/LIT-011.md) (spectral sets) and [LIT-028](../literature.d/LIT-028.md), and a "quantum/physics" filing with [LIT-010](../literature.d/LIT-010.md), but no mathematics with any of them.

## Bearing on the record

No THEORY document in this record is supported or contradicted by it. It carries nothing for ML practice: no instruction, no method, no empirical content. Nothing belongs in the Anthology of the SOTA.

Its only value to this record is as a well-scoped pointer into a research frontier: rigorous symplectic foundations for class-S BPS physics. §1 is the part a non-specialist reader should take away.

## Limitations

**What a non-specialist can check, and what I checked:**
- **The elementary flowline analysis:**
  - the energy identity (Lemma 2.14);
  - the 1D qualitative lemmas (Lemmas 2.15–2.17);
  - the trapping argument (Lemma 2.18);
  - the metric-change pushforward in Lemma 2.20, where I checked φ_*(∂_r) = rτ∂_τ; the lemma's labelling of which metric goes with which vector field is loose (the proof writes "dτ" for "dτ²").
- **Change of variables in the ODE examples.** For the Airy and Berk–Nevins–Roberts equations in z = 1/x (Example 2.12), I recomputed z⁴f″ + 2z³f′ = z⁻¹f and z⁶f‴ + 6z⁵f″ + (6z⁴ − 3z²)f′ − z⁻¹f = 0, and both match the text.
- **The BNR front parametrisation (Example 2.12(3)) does not match as printed.** The first two components σ(u,v) = (u³−3uv², 3u²v−v³) are Re and Im of η³. The third, 3(u³v − uv³ − uv), is Im ∫η dx for x = η³ − 3η. For the stated Σ = {η³ − 3η + x = 0} the base coordinates should be those of x = 3η − η³. This is probably a typo and does not affect any theorem.
- **Two BNR braids I could not reconcile.** Example 2.12(3) gives the braid (σ₁σ₂)²; §7.3.3 uses βδ(β) = (σ₂σ₁)⁴. Both (−1)-closures are smoothly unknots, but the text does not say they are Legendrian isotopic.
- **The combinatorics:**
  - Proposition 3.7 (extracting D₄⁻-trees from a pre-spectral network);
  - the BPS-index recursion (Definition 3.20, the Hori–Vafa formula Eq. 21);
  - the dimension count 0 = −2 + 2 + 1 − 1 for the sneaky tree in Lemma 3.23, given Ekholm's index formula;
  - the complex-analytic transversality argument of Lemma 3.19 (determinant (1/ϕ)((l₂+s₂)/ϕ − (l₁+s₁)), zero set discrete).
- **The exchange relation in §7.3.2**, A₁A₁′ = 1 + (z₂z₃ − 1) ⇒ A₁′ = z₃, is arithmetic.
- **Appendix A.1–A.2:**
  - the Christoffel-symbol and second-fundamental-form computations for the curve (log Q, Q);
  - the four-step coarea / plurisubharmonicity chain behind Theorem A.3. Its last step, choosing T so that a(r)T ≥ rl, is terse.

**What a non-specialist cannot check:**
- **The analytic core:**
  - convergence of ε-strips to trimmed trees (Propositions 4.3, 4.13), whose adapted-cover construction is taken from [Ekh07, §5] and [Nho24, §5] by citation;
  - Gromov compactness and transversality for deformed continuation strips with a moving fibre boundary (§5.2.3, citing [Oh15], [Nho24, Proposition 3.37], [Sei08b]);
  - the orientation conventions (Remark 5.19, proof of Proposition 5.20);
  - the GPS-categorical arguments (Propositions 6.1, 6.6, 6.18, 6.19, Lemma 6.21).
- **Correctness depends on Nho24**, the second author's own 2024 preprint, cited for about ten lemmas. Its refereed status was not checked.
- **The figures.** Whether each figure's flowlines really match each augmentation term in §7.3 (Eqs. before Figure 19; Eq. 41) is asserted pictorially and could not be seen in text extraction.

**Where the paper's statements outrun its proofs:**
- **Creative networks.** Theorem 3 / Theorem 5.24 and the exact case of Theorem 2 are stated for any adapted spectral network but proved using finite creative ones.
- **Non-exact case.** Theorem 2's extra hypothesis appears only in prose. F is not constructed at all (Remark 5.10).
- **Trimmed limits.** Proposition 4.3 gives only trimmed limits (footnote 13).
- **Theorem 5 / Proposition 7.5** has no written proof.
- **§3.4 invokes Proposition 3.18 "in this setting"** without addressing its reliance on a non-holomorphic perturbation of L (§3.3.1).
- **The injectivity-of-non-abelianization claim** sits in a conjectural section and is argued in two sentences (§6.4.2).
- **The main categorical statement (Theorem 4(i))** includes, as "in particular", an equivalence W(T*S)-mod ≅ C_{−*}(Ω_zS)-mod that is prior work (Abouzaid), not proved here.

**Drafting slips, consistent with a v1:**
- the Figure 5 caption calls the trapping lemma "Lemma 2.26" (it is Lemma 2.18; 2.26 is the meromorphic version);
- an unresolved bibliography key "[higher˙algebra]" on p. 69;
- "Bers–Nevins–Roberts" for Berk–Nevins–Roberts (§7.1, Figure 21);
- Theorem 3 says "compatible with Σ" where L is meant;
- §3.3 has "flow-acyclicity of F3. as above".

**Scope:**
- the categorical and generation results assume Reeb-positive Legendrians at infinity (§6.4);
- the weave construction is only for S² with one puncture (§7);
- the authors leave non-exact Family Floer, D₄⁻-graphs (Remark 3.4), central charges (footnote 1), concave ends (Remark 7.3) and the Stokes-local-system triangle (Eq. 40) to future work.

## Open questions

- **Does Theorem 3 extend to general, non-exact Betti Lagrangians** (p. 11; Remark 5.10)? Closed by constructing F for meromorphic spectral curves beyond short segments.
- **Does Proposition 4.3 upgrade from trimmed to genuine (broken) D₄⁻-trees** (footnote 13)?
- **Does diagram (40) commute in general**, i.e. is the partially wrapped Yoneda functor compatible with Stokes local systems? Is M an equivalence, with inverse given by Family Floer (§6.4.2, Remark 6.22(2))?
- **Can central charges be incorporated** in the real setting (footnote 1)? What is the Floer meaning of general D₄⁻-graphs, i.e. 4d BPS states not given by trees (Remark 3.4)?
- **How do Lusztig cycles of Demazure weaves relate to finite webs**, i.e. 4d BPS states for degenerate networks (Remark 7.6(2))? And what about weaves with concave ends (Remark 7.3(1))?
- **For this record:** whether the paper survives refereeing unchanged. That would settle its status here.

## Corrections to the seeded skim

- **Two main results are narrower in the body than the dossier (and §1) suggests.**
  - Theorem 3 (Family Floer = non-abelianization) is stated and proved only for *exact* Betti Lagrangians. Remark 5.10 says the functor F is *not* constructed for the non-exact (WKB/meromorphic) case, "though we essentially compute it for infinitesimally short line segments".
  - Its proof (Definition 5.29, Proposition 5.30, proof of Theorem 5.24) assumes an "adapted finite *creative* Morse spectral network" and treats only creation joints. The theorem statements, however, say "a spectral network compatible with Σ" (Theorem 3) and "an adapted Morse spectral network" (Theorem 5.24).
  - For exact L this does not bite, because the construction in §3.3 produces creative, finite networks (§1, after Theorem 1). As written, though, a general Morse network with 6-valent joints is not covered.
- **Theorem 2's "⇒" direction for exact L also uses creativity.** The existence direction (§5.4.1) rests on "the 2d-4d BPS counting indices … are non-zero at all walls of W, as W is creative".
  - The non-exact case adds a hypothesis that appears only in prose, not in the theorem: "we demand Σ to be meromorphic outside some compact subset" (p. 8).
  - The "⇐" direction proceeds via Proposition 4.3, which proves convergence only to *trimmed* D₄⁻-trees. Footnote 13 says upgrading to genuine trees "would add even more technicality and pages … we have not pursued this".
- **Theorem 5 has no written proof.** Proposition 7.5, which "implies Theorem 5", is stated with a closing □ and justified by one sentence: "The adiabatic degeneration results in Section 3 … imply that …" (p. 121). Theorem 5(1)'s claim that the combinatorial W_w is a finite, creative Morse spectral network is not argued anywhere in §7.
  - The Berk–Nevins–Roberts match (§7.3.3) is "we can readily see that the spectral network … coincides", a comparison of figures.
  - The dossier's "claims to prove physics conjectures, including … higher-order Stokes phenomena such as the Berk–Nevins–Roberts example" therefore overstates the support for the BNR part.
- **Scope of the "non-algebraic" generalisation.** The dossier (following §1.1) stresses asymptotics by arbitrary positive braids. The body restricts in places:
  - Proposition 6.19 and §6.4 assume each Legendrian at infinity is Reeb-positive with finitely many Reeb chords at distinct angles;
  - §7 treats only S² with one puncture and braid βδ(β).
- **Setting.** The dossier's "real Lagrangian fillings in T*C for a smooth surface C" should read T*S for a smooth surface S. The holomorphic cotangent bundle T*S is used only in the meromorphic (WKB) case.
- **The authors flag a gap in prior work that their results depend on.** Remark 4.10(i) says the construction of domain-adapted covers in [Ekh07, §5] "has a gap in the proof of [Ekh07, Lemma 5.4]". They repair it with their Appendix Theorem A.3, a truncated reverse isoperimetric inequality. The dossier's "correctness rests on §4" is right, and this is one of the specific places it rests.
- The dossier's section outline, the GMN context, the Casals–Murphy 2018 / Nho 2024 lineage and "no ML link" all check out.
