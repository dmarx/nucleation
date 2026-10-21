---
status: Read
paper: LIT-tmptzsyg
title: 'Rubenstein et al. — Causal consistency of structural equation models'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from arXiv:1707.00819v1 (4 July 2017, the only arXiv
    version), text extracted with pdftotext in raw and layout modes. Read:
    the abstract, §1 with §1.1 on cholesterol, §2 (Definition 1, Example
    2), §3, §4.1–4.5 (Definition 3, Lemmas 4–5, Theorem 6, Examples 7–8),
    §5 (Theorems 9–12), §6, and Appendices A–D with every proof and Lemmas
    13–15. Many displayed equations were garbled by extraction; they are
    reconstructed from the prose and the layout-mode text, and Theorem
    11, the one the record leans on, is re-derived in THEORY-tmpj5zq1. The
    figures were read from captions and text. The PMLR R15 reissue was not
    compared.
date: '2026-10-21'
summary: >-
  Defines an exact transformation between structural equation models: a
  map τ on states and a surjective, order-preserving map ω on a declared
  set of perfect interventions such that pushing each low-level
  interventional distribution forward by τ gives the high-level model's
  distribution under the image intervention. It proves that marginalising
  childless or never-intervened variables, averaging linear
  micro-variables when every column of the coupling matrix has the same
  sum, and taking the equilibrium of a contracting linear process with
  constant noise are each exact, and stresses that each is exact only for
  the intervention set declared.
---
<!-- inactive-ok-file: TERM-tmpf5k7x TERM-tmpdxajb — Proposed; terms filed from the same exchange that this reading bears on, cited as open -->

# NOTE-tmp6b7dr: Rubenstein et al. — Causal consistency of structural equation models

## Contribution

It gives the first general definition, for structural equation models, of
when two models at different levels of detail are causal models of the same
system: they must agree on the effect of every declared intervention, and
the correspondence between interventions must respect how interventions
compose. Marginalisation, micro-to-macro averaging and the passage from a
dynamical process to its equilibrium are shown to be instances. The authors
single out the partial order on interventions as the new idea: "An important
novel idea of this paper is to explicitly make use of a natural ordering on
the set of interventions."

## Key insight

A coarse model is causally consistent with a fine one relative to a list of
interventions, not absolutely. "Observe that in each of the following
examples, the particular set of interventions considered is important. If we
were to allow larger sets of interventions 𝑋 in the SEM 𝑋, the
transformations given would not be exact." The test compares distributions:
the coarse model must reproduce the push-forward, under the coarse-graining,
of each interventional distribution of the fine one. So it asks whether a
macro model predicts what macro observers would see under each intervention,
not whether the macro state carries everything that determines a particular
system's response.

## Assumptions

- **SEMs in a wide sense** (Definition 1): structural equations
  Xᵢ = fᵢ(X, Eᵢ), a declared subset of perfect interventions with the natural
  partial order (i ≤ j iff j intervenes on a superset of i's variables,
  setting them to the same values), and an exogenous law ℙ_E. Exogenous
  variables may be dependent, cycles are allowed, and the only condition is
  a unique solution under every declared intervention with ℙ_E-probability
  one.
- **Only perfect interventions** do(X_S = x_S). A change to a mechanism that
  is not the fixing of a variable is not modelled.
- **Theorem 10** needs acyclicity. **Theorem 11** needs a linear SEM in which
  the W's are exogenous and Z = AW + F, interventions that set all of W, all
  of Z or both, and equal column sums of A. **Theorem 12** needs
  X_{t+1} = AX_t + E_t with A a contraction and the same noise at every time,
  E_t = E, and interventions that hold a variable fixed at all times.

## Key results

- **Definition 3 (exact transformation).** M_Y is an exact τ-transformation
  of M_X if there is a surjective, order-preserving ω from M_X's
  interventions to M_Y's with ℙ^i_{τ(X)} = ℙ_Y^{do(ω(i))} for every i, the
  left side being the push-forward of ℙ_X^{do(i)} by τ. ω need not be
  injective: "this would imply that ω is injective, and hence also bijective.
  This would constrain the ways in which M_Y can be 'simpler' than M_X."
- **Lemmas 4–5.** Relabelling is exact; exact transformations compose
  (ω_ZX = ω_ZY ∘ ω_YX).
- **Theorem 6.** Order preservation makes the square of interventions
  commute: if i ≤ j then ω(i) ≤ ω(j), so an intervention performed after
  another at the fine level has a counterpart performable after its
  counterpart at the coarse level.
- **Examples 7–8.** Without order preservation, an observational
  distribution can be matched by an interventional one (ω(∅) = do(Y₁ = 0)),
  and even with ω(∅) = ∅ a composite intervention can map to one that
  conflicts with its parts.
- **Theorem 9.** Marginalising childless variables is exact.
- **Theorem 10.** In an acyclic SEM, marginalising variables no declared
  intervention touches is exact, with the marginalised variable substituted
  into its children and its noise merged into theirs. This needs dependent
  noise: "marginalising out a common parent node will in general result in
  its children having dependent exogenous variables."
- **Theorem 11 (micro to macro).** With W exogenous, Z = AW + F, every column
  of A summing to a, and interventions setting all of W, all of Z or both,
  the averages (Ŵ, Ẑ) form an exact transformation, with
  Ẑ = (an/m)Ŵ + F̂ (the coefficient as the record computes it; see
  Limitations). The equal-column-sum condition is also necessary, the
  record's re-derivation in [THEORY-tmpj5zq1](../theory.d/THEORY-tmpj5zq1.md).
- **Theorem 12 (equilibrium).** For a contracting linear process with
  constant noise, the limit map is an exact transformation onto the cyclic
  SEM Yⁱ = Σ_{j≠i} A_ij Yʲ/(1 − A_ii) + Fⁱ/(1 − A_ii), with interventions
  that hold variables fixed for all time mapped to interventions on their
  limits.
- **§1.1 and §6.** Total cholesterol as a cause of heart disease is the
  motivating failure: diets raising LDL or HDL raise TC by the same amount
  with opposite effects, so TC is not an exact transformation of (LDL, HDL).
  The authors read Spirtes and Scheines' ambiguous manipulations as
  "arising due to the application of an inexact transformation".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Exact transformation, with ω surjective and order-preserving, is a sound formalisation of causal consistency between levels | moderate | Definition 3, Theorem 6, Examples 7–8 for why each condition is needed; no argument that it is not too permissive (Beckers and Halpern later show it is) |
| C2 | Marginalising childless or never-intervened variables is exact | strong | Theorems 9–10, proved in Appendix B |
| C3 | Averaging linear micro-variables is exact when every column of A has the same sum | strong | Theorem 11, proved in Appendix C; necessity re-derived here |
| C4 | The equilibrium of a contracting linear process with constant noise is an exact transformation onto a possibly cyclic SEM, which gives cyclic SEMs a causal reading | strong within the assumptions | Theorem 12 and Lemmas 13–15 |
| C5 | Exactness is relative to the declared interventions; enlarging the set can destroy it | strong as a remark | stated in §5 for every example; Theorem 11's restriction to whole-block interventions is an instance |
| C6 | Only when a macro model is an exact transformation are macro causal statements such as "LDL causes heart disease" meaningful | weak | asserted in §4.4 ("Only if this is the case, causal statements ... are meaningful"); not argued |

## Concepts

- **Perfect intervention** do(X_S = x_S): replace the structural equations of
  X_S by constants.
- **Natural partial order on interventions:** i ≤ j when j sets a superset of
  i's variables to the same values; it "corresponds to the ability to
  compose physical implementations of interventions".
- **Poset of distributions** 𝒫_X: the family ℙ_X^{do(i)} indexed by the
  declared interventions, ordered as they are.
- **Exact τ-transformation**: Definition 3 above.

## Connections

It builds on Bongers, Peters, Schölkopf and Mooij (2016) for marginalisation
and cycles, on Chalupka, Perona and Eberhardt (2015, 2016) for learned macro
variables, on Iwasaki and Simon (1994) and Simon and Ando (1961) for
aggregation, on Hoel, Albantakis and Tononi (2013), and on Spirtes and
Scheines (2004) for ambiguous manipulations. Beckers and Halpern
([LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md), read in [NOTE-tmp1bdcu](NOTE-tmp1bdcu.md)) take Definition 3 as the weakest of
their notions and show it too permissive; Beckers, Eberhardt and Halpern
([LIT-tmp0p7xl](../literature.d/LIT-tmp0p7xl.md), [NOTE-tmpqfl95](NOTE-tmpqfl95.md)) carry out the "softening" this paper's §6
proposes.

## Bearing on the record

- **[CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md), [CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md) and [TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md).** Exact
  transformation does not contain the hidden-governance-bit point, and
  accepts the coarse-graining the case rejects. Write the case as an
  acyclic SEM: K = E_K, Y_t = E_t, H = E_H, Y_{t+1} = (1 − H)E_{t+1} + HK,
  with the declared interventions ∅, do(H = 0) and do(H = 1). K is never
  intervened on, so by Theorem 10 marginalising it is exact: the coarse SEM
  Y_{t+1} = (1 − H)E′₁ + HE′₂, with fair noises, reproduces the law of
  (Y_t, H, Y_{t+1}) under every declared intervention. Over several steps
  under a held do(H = 1), the marginalised K reappears as noise shared
  across time, which Definition 1 allows. Yet Γ(Y_t) = ρ(h = 1) bits. The
  reason is that Definition 3 compares push-forward distributions, while
  governance-response sufficiency compares the response kernels of
  individual states, P(Y^(i) | S = s), across the fibres of T. A merged
  difference that only redistributes the response among states with the
  same coarse value is invisible to the first and is exactly what Γ
  measures. Rubenstein et al.'s cholesterol case is the nearest anticipation
  of the qualitative point (a macro variable merging micro-states whose
  interventional consequences differ), and their remark that enlarging the
  intervention set breaks exactness is [CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md)'s relativity to I.
  The coexistence of exact closure under the ordinary dynamics with that
  failure is not in this paper.
- **[TERM-043](../terms.d/TERM-043.md).** Its D_causal, Σ_a π(a) d(T_# P_o(Y | do(a)),
  P_t(Y′ | do(τ(a)))), is Definition 3's condition made graded: with π of
  full support, D_causal = 0 exactly when the push-forward of each source
  interventional law equals the target's under the corresponding
  intervention. It drops the requirement that the correspondence on
  interventions be surjective and order-preserving, which is what Theorem 6
  and Examples 7–8 show to be needed for composed interventions. By the
  same token D_causal is zero for the hidden bit, where Γ is not, so
  [TERM-tmpf5k7x](../terms.d/TERM-tmpf5k7x.md)'s governance-response sufficiency is not D_causal with τ
  the identity, as that term's "Why it narrows [TERM-043](../terms.d/TERM-043.md)" says. See
  [NOTE-tmp1bdcu](NOTE-tmp1bdcu.md) for the exact relation.
- **[THEORY-755](../theory.d/THEORY-755.md) and [THEORY-733](../theory.d/THEORY-733.md).** Theorem 11's condition is [THEORY-755](../theory.d/THEORY-755.md)'s
  column-equitability, for the one pair of blocks (rows of Z, columns of W)
  through which the SEM couples them: Σ_{i∈Z} A_ij is the same for every j
  in W. [THEORY-755](../theory.d/THEORY-755.md) states it for a dynamical x(t+1) = Ax and the vector of
  block sums; here it is a one-shot SEM, averages rather than sums, and a
  causal rather than a dynamical criterion. The algebra is the same
  QA = ĀQ. The join is the record's: neither paper cites the other's
  literature.
- **[TERM-tmpdxajb](../terms.d/TERM-tmpdxajb.md).** Its ℐ is this paper's declared intervention set, and
  C5 is the regime-relativity the term records, proved for one notion of
  adequacy.
- **[CLAIM-350](../claims.d/CLAIM-350.md).** Its causal bullet's "intervention-consistent
  coarse-graining for a declared family of interventions" is, in the
  literature, this paper's exact transformation; but it is a distributional
  notion, not the fibre-wise factorization [CLAIM-350](../claims.d/CLAIM-350.md) proves.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Theorem 11's coefficient.** By direct computation,
  (1/m)Σᵢ Σⱼ A_ij Wⱼ = (a/m)Σⱼ Wⱼ = (an/m)Ŵ. In this copy the extracted text of
  both the statement and its proof shows the coefficient of Ŵ as "a" over
  "m"; whether the printed text lacks n or the extraction lost it could not
  be told. Beckers and Halpern's restatement (their Example 3.3) has an/m,
  which agrees with the computation.
- **Sufficiency only.** Theorem 11 states the column condition as sufficient.
  It is also necessary for the averaging τ with these interventions
  ([THEORY-tmpj5zq1](../theory.d/THEORY-tmpj5zq1.md)); the paper does not say so.
- **Permissive.** Nothing in Definition 3 rules out matches won by the choice
  of distribution or of a sparse intervention set. Beckers and Halpern's
  Example 3.4 makes two unrelated models exact transformations of each
  other.
- **Perfect interventions only,** and no counterfactuals, which the authors
  name as not discussed.
- **No choice among exact transformations,** and no approximation; the §6
  "softening" is future work.
- **Theorem 12's constant noise** (E_t = E for all t) is a strong modelling
  assumption, adopted to give cyclic SEMs a reading.
- **C6 is asserted,** not argued.

## Open questions

- Which coarse-grainings are exact for every intervention a class of
  physical implementations allows, rather than for a chosen list?
- For governance in particular: when a mechanism change is modelled as a
  perfect intervention on a regime variable H, which coarse-grainings of the
  pre-intervention state are exact transformations and governance-response
  sufficient at once? The marginalisation of K shows the first does not
  imply the second.
