---
number: 834
status: Read
formerly:
- NOTE-tmpcc47a
paper: LIT-257
title: 'Harvey, Lipshutz & Williams — What Representational Similarity Measures Imply about Decodable Information'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2411.08197v1, the only version, 21
    pages), text extracted with pdftotext in reading-order and layout
    modes: abstract, §§1–5, Table 1, the captions of Figs. 1–2, and the
    whole appendix (A.1 the proof of Proposition 3 with Lemmas 1–2, A.2 the
    random ensembles of Fig. 2, A.3 the M → ∞ argument). Propositions 1–2,
    Corollary 1, the four entries of Table 1 (linear CKA, GULP, CCA, ENSD),
    eq. (21), Lemma 2 and the inversion of the A.1 inequalities into eq.
    (25) were re-derived by hand. The Procrustes–Bures identity is cited
    to Harvey, Larsen & Williams ([16], LIT-250) and was not re-proved
    here. The plots of Fig. 2 were read from their captions. Replaces the
    seeded skim NOTE-225.
date: '2026-10-14'
summary: >-
  For a linear readout that maximizes zᵀXw/M − ½wᵀG(X)w, the decoded signal
  is K_X z with K_X = XG(X)⁻¹Xᵀ/M, so the task-averaged agreement of two
  representations is Tr(K_X K_z K_Y). With K_z = I that is linear CKA,
  mean squared CCA, ENSD or the GULP distance, for particular G. Procrustes
  distance and average decoding distance bound each other only through the
  participation ratio of K_X − K_Y. The population limit (App. A.3) is an
  outline that requires b > 0 and a trace-class task covariance, and it
  does not reach the K_z = I case.
---
<!-- inactive-ok-file: THEORY-002 THEORY-301 CLAIM-193 CLAIM-269 NOTE-225 — Proposed or Superseded; the accounts and claims this reading bears on, the account filed from it, and the skim it replaces -->

# NOTE-834: Harvey, Lipshutz & Williams — What Representational Similarity Measures Imply about Decodable Information

## Contribution

The paper shows that several representational similarity measures,
usually justified by their geometric invariances, are statistics of
optimal linear decoders. With a quadratic weight penalty set by a matrix
G(X), the optimal readout's output is a fixed linear map, K_X, applied
to the target. Averaging the agreement of two networks' readouts over
targets with E[zzᵀ] = I gives linear CKA, mean squared canonical
correlation, ENSD or the GULP distance, according to G. It also proves
two-sided bounds between the Procrustes distance of normalized
representations and the average decoding distance, set by a
participation ratio.

## Key insight

Everything a regularized linear readout outputs passes through one
matrix: Xw* = K_X z, where K_X = XG(X)⁻¹Xᵀ/M. Two representations with
the same K_X decode every target identically, so comparing K_X and K_Y
is comparing what the representations make linearly available. The
choice of G decides which comparison results: a weight penalty gives
the raw Gram matrix (CKA), an activity penalty gives the projection onto
the column space (CCA), and ridge interpolates (GULP).

## Assumptions

- **Finite conditions.** X ∈ R^{M×N_X}, Y ∈ R^{M×N_Y}, M stimulus
  conditions, columns centred (§2).
- **Decoder objective (eq. 1).** maximize (1/M)zᵀXw − ½wᵀG(X)w, with
  G(X) symmetric positive definite. Most results take G(X) = aC_X + bI
  with C_X = XᵀX/M and a, b ≥ 0 (eqs. 4–5).
- **Task distribution.** Proposition 2 needs only K_z = E[zzᵀ]. Corollary 1
  and every identification in §3 need K_z = I: uncorrelated targets of
  unit variance across conditions.
- **CCA (eq. 17)** needs N_X = N_Y and C_X, C_Y invertible, so M ≥ N.
- **Proposition 3** needs the Procrustes–Bures equivalence of [16], and
  zero-padding to N_X = N_Y. Lemma 2's bound R_Δ ≥ 2 needs
  Tr K_X = Tr K_Y.
- **App. A.3.** Stimuli u_i i.i.d. from P_u; f, g with bounded responses
  (written "∥f(u_i)∥₂ ≤ ∞", meaning < ∞; footnote 4); target functions
  η ∼ GP(q); Fubini assumed (eq. 63); operator-norm concentration of the
  empirical G asserted (eqs. 70–71); b > 0 (eqs. 72–73).

## Key results

- **Optimal readout (eqs. 2, 7–8).** w* = (1/M)G(X)⁻¹Xᵀz, so
  ⟨Xw*, Yv*⟩ = zᵀK_X K_Y z with K_X := (1/M)XG(X)⁻¹Xᵀ. Ridge regression is
  G = C_X + λI (eq. 3). *Holds when:* G(X) positive definite.
- **Proposition 1.** max and min over ‖z‖ = 1 of ⟨Xw*, Yv*⟩ are the largest
  and smallest eigenvalues of ½(K_X K_Y + K_Y K_X). Proof: only the
  symmetric part of a quadratic form survives.
- **Proposition 2 (eq. 13).** E⟨Xw*, Yv*⟩ = Tr(K_X K_z K_Y), K_z := E[zzᵀ].
  Proof: zᵀK_X K_Y z = Tr(K_X zzᵀ K_Y), then linearity. *Holds when:* any
  target distribution with finite second moments. Gaussianity is not
  needed.
- **Corollary 1 (eqs. 15–16).** With K_z = I: E⟨Xw*, Yv*⟩ = Tr[K_X K_Y]
  and E‖Xw* − Yv*‖² = ‖K_X − K_Y‖²_F.
- **Table 1 and §3**, each re-derived:
  - *Linear CKA*, G = bI, b > 0: Tr[K_X K_Y]/(‖K_X‖_F‖K_Y‖_F). This is a
    ratio of expectations, the average similarity normalized by the
    average self-similarities. It is not an average of normalized
    similarities. b cancels.
  - *GULP*, G = C_X + λI: E‖Xw* − Yv*‖² = ‖K_X − K_Y‖²_F, "the plug-in
    estimate of the squared GULP distance". This is a distance, not a
    similarity.
  - *Mean squared CCA*, G = C_X: K_X is the orthogonal projection onto
    col(X), and the normalized similarity is (1/N)Σρ_i² (eq. 17).
  - *ENSD*, G = (Tr[C_X²]/Tr[C_X])I: E⟨Xw*, Yv*⟩ = ENSD(X,Y) (eqs. 18–19),
    with no further normalization.
  - *Inverse participation ratio*, G = Tr[C_X]I: E‖Xw*‖² = 1/R(C_X)
    (eq. 21).
- **Orthogonal invariance (eqs. 22–23).** G(XR)⁻¹ = RᵀG(X)⁻¹R for
  orthogonal R, "whenever G(X) is parameterized as in eq. (4)", so
  K_{XR} = K_X. Only for G = C_X (CCA) is K_X invariant under every
  invertible linear map of the columns.
- **Proposition 3 (eqs. 25–26; App. A.1).** With α = Tr K_X, β = Tr K_Y,
  R_Δ = R(K_X − K_Y) the participation ratio (Σσ)²/Σσ², and
  X̃ = XG(X)^{−1/2}/√M, so that X̃X̃ᵀ = K_X:
  (α + β) − √((α + β)² − R_Δ E‖Xw* − Yv*‖²) ≤ P(X̃, Ỹ)² ≤ √(R_Δ E‖Xw* − Yv*‖²),
  equivalently P⁴/R_Δ ≤ E‖Xw* − Yv*‖² ≤ (2(α + β)P² − P⁴)/R_Δ.
  *Holds when:* K_z = I, and the Procrustes distance of [16] equals the
  Bures distance of the kernels.
  - *Lower bound on P² (A.1.1).* Lemma 1:
    ‖αuu† − βvv†‖_* = √((α + β)² − 4αβ|⟨u,v⟩|²) for unit u, v. Choose X, Y
    within their orthogonal orbits so that |⟨vec X, vec Y⟩| equals the
    fidelity F (Uhlmann; F = ‖XᵀY‖_*). Monotonicity of the trace norm
    under partial trace gives ‖K_X − K_Y‖_* ≤ √((α + β)² − 4F²) (eq. 39).
    Then ‖·‖_* = √R_Δ ‖·‖_F and F = ½(α + β − d_B²) give eq. 42. I checked
    the inversion: it uses d_B² ≤ α + β, which holds.
  - *Upper bound on P² (A.1.2).* d_B² = min_Q ‖K_X^{1/2} − K_Y^{1/2}Q‖²_F ≤
    ‖K_X^{1/2} − K_Y^{1/2}‖²_F ≤ ‖K_X − K_Y‖_* (Powers–Størmer) =
    √R_Δ‖K_X − K_Y‖_F (eqs. 51–53).
  - *Lemma 2.* R(K_X − K_Y) ≥ 2 when Tr K_X = Tr K_Y. The printed proof
    expands the ratio and asserts the bracket is ≥ 1 "by inspection". A
    shorter proof: the trace-zero difference has positive and negative
    eigenvalue sums both equal to S, so ‖Δ‖_* = 2S and
    ‖Δ‖²_F ≤ S² + S² = 2S², hence R ≥ 4S²/2S² = 2. The lemma holds.
  - *Reading.* "when the Procrustes distance between normalized
    representations is small, then the average decoding distance must
    also be small", since R_Δ ≥ 1 always. The converse holds "only … when
    the participation ratio of the difference … is also small". Fig. 2
    fills the allowed regions with random PSD pairs (M = 50, A.2). Its
    "upper left-hand corner" (large decoding distance, small Procrustes
    distance) is empty.
- **App. A.3, the population version.** Kernels
  k(u,u′) = f(u)ᵀG(f)⁻¹f(u′) with G(f) = aE[f fᵀ] + bI (eqs. 56–57),
  integral operators K, H on L²(P_u), and η ∼ GP(q) with covariance
  operator Q. E_η⟨Kη, Hη⟩ = Tr[KQH] (eqs. 61–64). The plug-in
  (1/M³)Tr(K̂QĤ) = (1/M)Tr(K_X K_z K_Y), with K_z = Q the Gram matrix of q
  at the samples, converges to Tr[KQH] (eqs. 80–83). The argument:
  - ‖G(X)⁻¹ − G(f)⁻¹‖_op is bounded by a multiple of
    ‖XᵀX/M − E[f fᵀ]‖_op (eq. 76), using λ_min(G) ≥ b. So b > 0 is
    required, which excludes CCA (a = 1, b = 0).
  - Eq. 77 restates eq. 76 as (|a|/b²)‖G(X) − G(f)‖_op. Since
    G(X) − G(f) = a(XᵀX/M − E f fᵀ), the factor |a| is counted twice. The
    correct form is (1/b²)‖G(X) − G(f)‖_op. This does not affect
    convergence.
  - Operator-norm concentration of G(X) (eqs. 70–71) is asserted, "can be
    shown", not shown.
  - (1/M³)Σ_{ijk}K_ij Q_jk H_ki → Tr[KQH] is cited to "the strong law of
    large numbers". It is a V-statistic limit, which needs integrability
    of the kernels but holds for bounded ones.
  - The section calls itself a brief discussion "leaving a full
    investigation to future work", and §5 says "a rigorous exploration of
    the M → ∞ regime … could be an important topic of future work".
  - *What A.3 does not reach.* The K_z = I case of Corollary 1, where CKA,
    CCA, GULP and ENSD live, is the γ → 0 limit of the RBF covariance
    (eq. 55). There q is a Kronecker delta, whose integral operator on
    L²(P_u) is zero for a non-atomic P_u, so Tr[KQH] = 0, and indeed
    (1/M³)Tr(K̂ I Ĥ) = (1/M)Tr(K_X K_Y) → 0. The non-degenerate population
    form of the K_z = I identities needs the normalization
    (1/M²)Tr(K̂Ĥ) → Tr[KH], the Hilbert–Schmidt inner product of the
    kernel operators. A.3 does not state it. It is the population
    counterpart, which A.3 cites to [3], of GULP and CKA.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The optimal regularized linear readout's output is K_X z, so it depends on X only through K_X | strong | eqs. 2, 7–8, a closed form |
| C2 | Best- and worst-case readout alignment are the extreme eigenvalues of ½(K_X K_Y + K_Y K_X) | strong | Prop. 1 |
| C3 | Task-averaged readout alignment is Tr(K_X K_z K_Y) | strong | Prop. 2 |
| C4 | With K_z = I, linear CKA, mean squared CCA, ENSD and the GULP distance are normalized averages, averages or average distances of optimal readouts for particular G | strong | Cor. 1, eqs. 17–19, Table 1, re-derived |
| C5 | K_X is invariant under orthogonal maps of the columns when G = aC_X + bI | strong | eqs. 22–23 |
| C6 | Procrustes distance and average decoding distance bound each other, with constants set by the participation ratio of K_X − K_Y | strong | Prop. 3, App. A.1; the Procrustes–Bures equivalence is imported from [16] |
| C7 | With equal traces, R(K_X − K_Y) ≥ 2 | strong | Lemma 2, re-proved |
| C8 | The finite-M decoding similarity converges to an operator trace Tr[KQH] as M → ∞ | weak | App. A.3: a sketch with b > 0, a trace-class Q, asserted concentration, and no treatment of K_z = I |

## Concepts

- **Decoding similarity** — ⟨Xw*, Yv*⟩ for one target z (eq. 7).
- **Average decoding similarity / distance** — its expectation over
  targets, and E‖Xw* − Yv*‖² (eqs. 11, 16).
- **Normalized kernel K_X** — XG(X)⁻¹Xᵀ/M. It depends on the penalty G
  and is suppressed from the notation.
- **Participation ratio** — R(A) = (Σσ_i)²/Σσ_i² = ‖A‖²_*/‖A‖²_F, a
  continuous effective rank, between 1 and rank(A).
- **Bures distance / fidelity** — d_B² = Tr K_X + Tr K_Y − 2F,
  F = Tr[(K_X^{1/2}K_Y K_X^{1/2})^{1/2}] (eqs. 27–28).

## Connections

It extends Kornblith et al. ([LIT-254](../literature.d/LIT-254.md)), who relate R²_CCA, linear
regression and CKA as differently weighted eigen-overlaps, by giving the
whole family a decoding reading. It takes the Procrustes–Bures
equivalence from Harvey, Larsen & Williams ([16], [LIT-250](../literature.d/LIT-250.md), [THEORY-004](../theory.d/THEORY-004.md)),
whose CKA–NBS envelope ([THEORY-233](../theory.d/THEORY-233.md)) is a bound of the same kind. GULP
(Boix-Adsera et al., [3]) supplies the population version of the ridge
case. The paper formalizes the observation of Cloos et al. ([5]) that
high Procrustes similarity implied high CKA similarity in practice.

## Bearing on the record

- **[THEORY-008](../theory.d/THEORY-008.md)'s promote_when has two clauses, and this reading meets
  one.**
  - *Met: "confirming Prop. 2 and Cor. 1".* Both are proved in full in
    the paper and re-derived here, as are all four rows of Table 1.
  - *Failed: "including the population version in App. A.3".* A.3 is an
    outline, by its own account. It asserts the concentration step and
    needs b > 0, so the CCA member is not covered. It also mis-states one
    constant (eq. 77). Above all, it treats a trace-class task covariance
    Q. The K_z = I case, the one in which the record's identities hold,
    is the white-noise limit, where A.3's limit is zero. No reading of
    this paper can meet that clause. It needs either a different source
    for the population identities, such as GULP's population analysis
    ([3], not held), or a rewording that confines the claim to finite M.
- **[THEORY-008](../theory.d/THEORY-008.md)'s text, against the paper.**
  - "it equals linear CKA, GULP, mean squared CCA or ENSD". Precisely:
    CKA and mean squared CCA are the average similarity normalized by
    the self-similarities, a ratio of expectations. GULP is the average
    decoding *distance*. Only ENSD is the average similarity itself.
  - "K_X, which is invariant under orthogonal transformations of X
    (eqs. 22–23)". The paper adds "whenever G(X) is parameterized as in
    eq. (4)". [THEORY-008](../theory.d/THEORY-008.md) should keep that condition.
  - [THEORY-008](../theory.d/THEORY-008.md)'s summary, "the probe's output is fixed by the kernel,
    whatever basis the representation is written in", overstates. The
    output is fixed by K_X, which is invariant under orthonormal changes
    of basis for G = aC_X + bI. Under a general change of basis it is
    invariant only for G = C_X. For CKA's G = bI it is not.
  - "Anything about nonlinear readouts or classifiers (named as future
    work in the source's §5)". §5 names *linear* classifiers (SVMs,
    multi-class logistic regression) as future work, not nonlinear
    readouts. Nonlinear readouts are simply outside the paper.
  - "Proposition 3 … is a separate, weaker result, and its proof was not
    read." It is now read and holds, given the imported Procrustes–Bures
    equivalence. It is not weaker but of a different kind: two-sided
    inequalities rather than identities. [THEORY-301](../theory.d/THEORY-301.md) is filed from
    it.
- **[THEORY-004](../theory.d/THEORY-004.md).** Proposition 3 uses its Procrustes–Bures half as a
  premise and does not re-prove it. This reading adds nothing to
  [THEORY-004](../theory.d/THEORY-004.md)'s promote_when.
- **[THEORY-233](../theory.d/THEORY-233.md).** Prop. 3 is the decoding-distance analogue of
  [THEORY-233](../theory.d/THEORY-233.md)'s CKA–NBS envelope. The constant here is the participation
  ratio of the difference, not the ranks of the kernels, and both bounds
  come from the same Fuchs–van de Graaf route. A Connections line would
  join the two.
- **[CLAIM-193](../claims.d/CLAIM-193.md) and [CLAIM-269](../claims.d/CLAIM-269.md)** (supported by [THEORY-008](../theory.d/THEORY-008.md)) are supported at
  finite M only, as [THEORY-008](../theory.d/THEORY-008.md) is.
- **The skim's question about A.3 ([NOTE-225](NOTE-225.md)).** A.3 is "where the
  GNS/L²(P) reading would live". It does introduce integral operators on
  L²(P_u) and an inner product ⟨ηK, ηH⟩_{L²}. The identities it proves
  there are for a smoothing task covariance, not for the identity.
- The paper carries no instruction for ML practice. It does not argue
  for any one similarity measure. The `anthology-candidate` flag set at
  seeding is unchanged by this reading.

## Limitations

- Linear regression readouts only. Linear classifiers are named as
  future work (§5), and nonlinear readouts are not discussed.
- The task distribution enters only through K_z, and the §3
  identifications all fix K_z = I. Which task distribution is
  appropriate is left open (§5).
- Finite M throughout the main text. The population version is a sketch
  (A.3).
- Prop. 3 rests on an equivalence proved in another paper ([16]). Its
  bounds are tight only at rank 1 (lower) and for commuting kernels
  with {0,1} spectra (upper).
- Fig. 2 populates the bounds with random PSD matrices, not with trained
  networks or neural data.
- A workshop paper (UniReps 2024). The venue line is from the PDF.

## Open questions

- A rigorous M → ∞ theory for K_z = I, i.e. convergence of
  (1/M²)Tr(K̂Ĥ) with estimated G, at a rate. GULP's population analysis
  may already supply it for ridge.
- The analogue for linear classifiers, where the optimal readout has no
  closed form linear in z.
- Which task covariance K_z makes decoding similarity track
  behaviourally relevant function, the paper's motivating question.
