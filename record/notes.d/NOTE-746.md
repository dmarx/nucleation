---
number: 746
status: Read
formerly:
- NOTE-tmpo5k5s
paper: LIT-950
title: 'Marconato et al. — All or None: identifiable linear properties of next-token predictors'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v2 of 15 March 2025, the AISTATS 2025
    version, 37 pages), fetched from arxiv.org/pdf/2410.23501 and extracted
    with pdftotext -layout: the main text (§§1–7), the checklist, and all of
    appendices A–E with every proof (B.1–B.7, C.1–C.4, D.1–D.2, E.1–E.2).
    The reference list was scanned, not read. The extraction loses some
    tildes, subscripts and primes; the expressions below were restored by
    eye from the surrounding definitions.
date: '2026-10-14'
summary: >-
  Two next-token predictors of the form p(y | x) ∝ exp(f(x)ᵀg(y)) induce the
  same distribution exactly when they are related by an invertible linear map
  on the subspaces M and N that enter the logit dot product, with arbitrary
  distortion allowed off them. Relational linearity, and with it linear
  probing and linear subspaces, then holds in all such models or none when
  Γ ⊆ N and Γ_q ⊆ M. Parallelism survives only inside N. There are no
  experiments.
---
<!-- inactive-ok-file: QUESTION-027 QUESTION-052 CLAIM-209 CLAIM-193 CLAIM-142 THEORY-175 — Open or Proposed; the question this work was registered for and the entries it is set beside, open -->

# NOTE-746: Marconato et al. — All or None: identifiable linear properties of next-token predictors

## Contribution

The paper characterizes exactly which next-token predictors of the softmax
form induce the same conditional distribution, without the diversity
condition and without equal representation dimensions that earlier linear
identifiability results (Roeder et al. 2021; Khemakhem et al. 2020) needed.
It then defines relational versions of linear properties of language models
(relational linearity, linear subspaces, linear probing, linear steering)
in terms of the quantities that the characterization fixes. It proves that,
under a containment condition, relational linearity holds in every
distribution-equivalent model or in none. Parallelism of difference vectors
is preserved only inside one subspace. The paper is theory only.

## Key insight

Only the part of each representation that enters the logit dot product is
fixed by the distribution. Project the embeddings onto M and the
unembeddings onto N, and any two equivalent models are related there by an
invertible linear map. Off those subspaces they can differ by any
distortion at all. A linear property is therefore shared by all equivalent
models exactly when it lives in those subspaces. A property that uses the
rest of the representation is a fact about one model, not about the
distribution.

## Assumptions

- **Model form.** p_{f,g}(x_{t+1} | x_{1:t}) = exp(f(x_{1:t})ᵀ g(x_{t+1})) / Z(x_{1:t}),
  with f : Seq(A) → ℝᵈ and g : A → ℝᵈ nonparametric (Eq. 1). Appendix A
  shows a decoder-only transformer's last-token state with its unembedding
  and bias has this form.
- **Exact equality of distributions.** Every result is about p_{f,g} = p_{f̃,g̃}
  on all of Seq(A) and every next token, not approximate equality.
- **A shared vocabulary A.** Different vocabularies are left as a hypothesis
  (§3.4).
- **Trained models (§3.4).** The step to trained models assumes both reach the
  global maximum of the likelihood and both can represent the data
  distribution p_D exactly. The authors note that this fails in practice.
  The softmax gives positive mass to every sequence, while p_D gives zero to
  many, so the model class is "inherently misspecified" there. Optimisation
  issues such as local minima are set aside (footnote 2).
- **For Theorem 14:** the property is stated on a subspace Γ ⊆ N, and its
  image Γ_q := Im(A_qᵀ P_Γ) lies in M.

## Key results

Notation. F := SIm(f) and G := SIm(g₀) are the spans of the embeddings and
the pivoted unembeddings, where g₀(y) := g(y) − g(y₀) for a fixed pivot
token y₀. M := Im(P_F P_G) and N := ker(P_F P_G)^⊥ (Eq. 7). dim(M) is
called the model's *effective complexity*.

- **Lemma 2.** dim(M) = dim(N) = dim(F) − dim(F ∩ G^⊥). M ⊆ F and N ⊆ G.
  f(x)ᵀ g₀(y) = (P_M f(x))ᵀ P_N g₀(y) (Eq. 8). So components outside M
  and N do not contribute to any logit difference.
- **Definition 3 (extended linear equivalence, ∼EL).** (f, g) ∼EL (f̃, g̃)
  when dim(M) = dim(M̃) and there are full-rank M, N ∈ ℝ^{d×d̃}, invertible
  from M̃ to M and from Ñ to N, with Mᵀ N = P_M̃ P_Ñ and
  P_M f(x) = M P_M̃ f̃(x), P_N g₀(y) = N P_Ñ g̃₀(y) for all x and y
  (Eqs. 9–10). Appendix B.3 proves it is an equivalence relation.
- **Theorem 5 (identifiability).** For all (f, g), (f̃, g̃) ∈ Θ, of any
  dimensions d and d̃: p_{f,g} = p_{f̃,g̃} ⇔ (f, g) ∼EL (f̃, g̃). Hence
  p_{f,g} = p_{f̃,g̃} ⇒ dim(M) = dim(M̃) (Eq. 13), so effective complexity is
  a property of the distribution. The proof (B.6) pivots out the
  normaliser, solves for M with pseudo-inverses on spanning sets of tokens
  and sequences, and bounds ranks to show rank(M) = rank(N) = dim(M).
- **Corollary 6 (Roeder et al., adapted).** If d = d̃ and (f, g) satisfies
  diversity, SIm(f) = SIm(g₀) = ℝᵈ, then f(x) = M f̃(x) and
  g₀(y) = M^{−ᵀ} g̃₀(y) for an invertible M (Eqs. 14–15). The proof relaxes
  Roeder et al.'s condition SIm(f₀) = ℝᵈ on pivoted embeddings to
  SIm(f) = ℝᵈ, and needs it of one model only.
- **Counterexample without diversity (B.5).** With g(y₀) = (1, 0),
  g(y₁) = (1, 1), g(y₂) = (1, −1), so that G = span(e₂), the embedding
  f̃(x) = (f₁(x) + 0.2 cos(40 a₁/π), f₂(x)) gives the same distribution and
  is not a linear transform of f.
- **Lemma 8 (parallelism is a distributional statement).** g(y₁) − g(y₀) and
  g(y₃) − g(y₂) are parallel in N, that is P_N γ = β P_N γ′ with β ≠ 0
  (Definition 7), if and only if
  log p(y₀ | s)/p(y₁ | s) = β · log p(y₂ | s)/p(y₃ | s) for every s ∈ Seq(A)
  (Eq. 16).
- **Definition 9 (relational linearity of a query q on Γ ⊆ SIm(g₀)).**
  There are A_q and a_q with P_Γ f(s ⌢ q) = P_Γ A_q f(s) + a_q for every
  context s (Eq. 17). Propositions 11 and 13 derive the relational linear
  subspace (Definition 10) and relational linear probing (Definition 12,
  softmax(W f(s) + b)ᵢ = p(yᵢ | s ⌢ q; Y_P)) from it. Proposition 19
  (C.1) gives relational linear steering under a non-nesting condition on
  the Γ_q of several queries.
- **Theorem 14 (all or none).** If (f, g) ∼EL (f̃, g̃), f linearly represents
  q on Γ ⊆ N and Γ_q ⊆ M, then f̃ linearly represents q on Γ̃ ⊆ Ñ, with
  Γ̃ = Im(N⁺ P_Γ). By Propositions 11 and 13 the same holds for linear
  subspaces and linear probing. Under the diversity condition M = N = ℝᵈ,
  so the containment holds automatically.
- **When Γ_q ⊄ M (D.1).** The components of f in F ∖ M "can be arbitrarily
  chosen", for example as squares of f̃'s coordinates. An equivalent model
  then has a non-linear dependence of f̃(s ⌢ q) on f̃(s) whenever
  P_{Γ_q}(P_F − P_M) ≠ 0. So without the condition the property can hold in
  one model and fail in an equivalent one.
- **Theorem 15 (parallelism).** For ∼EL-equivalent models, γ and γ′ are
  parallel within N if and only if γ̃ and γ̃′ are parallel in Ñ. Parallelism
  in the whole space is not preserved.
- **Appendix E.** A paraphrase q₂ of q₁ (proportional log-odds over paired
  replies, Definition 21) forces P_{Γ₁} f(s ⌢ q₁) = β O P_{Γ₂} f(s ⌢ q₂)
  for an invertible O (Proposition 22), under Γᵢ ⊆ SIm(f)_{qᵢ}. A tautology,
  a query whose replies ignore the context, is trivially relationally linear:
  P_G f(s ⌢ q) = P_G a_q (Proposition 24).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Softmax next-token predictors induce the same distribution iff they are ∼EL-equivalent, at any dimensions and without diversity | strong | Theorem 5, proof in B.6 |
| C2 | Effective complexity dim(M) is fixed by the distribution | strong | Eq. 13, from Theorem 5 |
| C3 | Without diversity, equivalent models need not be linearly related | strong | counterexample, B.5 |
| C4 | Parallelism in N is equivalent to proportional log-odds over all contexts, and only parallelism in N is shared | strong | Lemma 8; Theorem 15 |
| C5 | Relational linearity, linear subspaces and linear probing hold in all or none of the equivalent models when Γ ⊆ N and Γ_q ⊆ M | strong | Theorem 14; Propositions 11, 13 |
| C6 | Without Γ_q ⊆ M the property can fail in an equivalent model | moderate | construction in D.1, shown up to proportionality, not as a worked model |
| C7 | The parallelism that PCA shows in trained models is not explained by identifiability, so training biases select within the equivalence class | weak | informal argument, §6, no measurement |

## Concepts

- **Distribution-equivalent models.** Two predictors with
  p_{f,g} = p_{f̃,g̃} on all sequences and tokens.
- **Effective complexity.** dim(M) = dim(N), the dimension of the part of
  the representation that enters the logits. It is at most d.
- **Diversity condition.** SIm(f) = SIm(g₀) = ℝᵈ: one model's embeddings and
  pivoted unembeddings span the whole space (Definition 1).
- **Context–query–reply string.** x = s ⌢ q ⌢ y, with s the context
  ("subject"), q the query ("relation") and y one reply token ("object"),
  for example s = "Rome", q = "is the capital of", y = "Italy".
- **Relational linearity.** As in Definition 9 above. The information in
  f(s ⌢ q) that bears on replies in Γ is an affine function of f(s). It
  refines Paccanaro and Hinton's linear relational embedding and Hernandez
  et al.'s relation decoding, and uses only the quantities that Theorem 5
  fixes.

## Connections

The identifiability result generalizes Roeder et al. (2021) and Khemakhem
et al. (2020), whose pivoting argument it follows, and Lachapelle et al.
(2023) for the corollary. Its taxonomy of linear properties is Park, Choe
and Veitch's ([LIT-304](../literature.d/LIT-304.md)), recast relationally. Park et al. introduce latent
binary concepts, while this paper is "agnostic to assumptions on the
data-generating process" and posits no latent variables. Jiang et al.
(2024) explain linearity from latent variables, which this paper declines to
do. The authors' later work with Nielsen and Dittadi asks when *approximate*
equality of distributions forces representational similarity ([LIT-253](../literature.d/LIT-253.md),
held here unread). Picozzi ([LIT-936](../literature.d/LIT-936.md)) cites this paper as the theoretical
characterisation of identifiable properties of next-token predictors. §6
compares the shared-property hypothesis to the principle of covariance in
physics, which says laws should be coordinate-free.

## Bearing on the record

- **[QUESTION-027](../questions.d/QUESTION-027.md).** The paper is a clean, proved instance of a signature
  identified when the full latent model is not. Theorem 5 is the
  characterisation of the observational equivalence classes, and Theorem 14
  names properties that are constant on them. But it is the case that
  [QUESTION-027](../questions.d/QUESTION-027.md)'s "What is already known" calls answered. The observation is
  the whole conditional distribution on every sequence in Seq(A), so there
  are no unobserved probes. Lemma 8 makes this explicit: parallelism in N
  is equivalent to proportional log-odds over all contexts, a property of
  the observed law itself. Nothing in the paper concerns decisions outside
  the observed probes, interventions or transport, where [QUESTION-027](../questions.d/QUESTION-027.md) puts
  its content. [LIT-950](../literature.d/LIT-950.md)'s status note says the paper "proves which linear
  properties hold in every next-token predictor that induces the same
  distribution". It does so only under Γ ⊆ N and Γ_q ⊆ M, and it gives
  sufficient conditions, not a characterisation of all shared properties.
  The LIT body's "That is the question's pattern" holds only for the
  unrestricted form.
- **[CLAIM-148](../claims.d/CLAIM-148.md).** The paper refines the gauge that [CLAIM-148](../claims.d/CLAIM-148.md) describes. For a
  bilinear softmax model, the gauge is an invertible linear map only under
  diversity and equal dimensions (Corollary 6). Without diversity it is an
  invertible linear map on M and N, plus arbitrary, even non-linear,
  distortion off them (B.5, D.1). [CLAIM-148](../claims.d/CLAIM-148.md)'s point stands, and gains a
  case: a property of one fitted model that depends on components outside M
  is not a property of the data.
- **[CLAIM-209](../claims.d/CLAIM-209.md).** The paper supports only the unrestricted second sentence,
  which [CLAIM-209](../claims.d/CLAIM-209.md)'s "Where its content is" already grants. It gives nothing
  for the restricted clause.
- **[CLAIM-193](../claims.d/CLAIM-193.md) and [CLAIM-142](../claims.d/CLAIM-142.md).** Relational linear probing (Definition 12) is
  shared only for replies whose difference vectors lie in N. That is a
  concrete case of "what the probes cannot see they cannot separate": a
  probe trained on one model reads structure that an equivalent model need
  not carry, unless the structure lies in N.
- **[THEORY-175](../theory.d/THEORY-175.md) and the cross-model agreement it records.** §6 bears on how to
  read agreement between trained models. The parallelism that PCA displays
  is not shared across the equivalence class. So where trained models agree
  on it, the agreement comes from inductive biases of training or
  architecture, not from the distribution. Agreement between independently
  trained models is therefore not by itself evidence that a structure is
  identified.
- **Curation of 2026-10-14.** The triage table calls this work "the
  identifiability half of the relational-signature question". That
  overstates it. It is the identifiability half of the unrestricted form
  only.
- No instruction for machine-learning practice. An anthology topic on
  representation learning could hold it, as the `anthology-candidate` flag
  says. It is held here for [QUESTION-027](../questions.d/QUESTION-027.md) under [ADR-013](../decisions.d/ADR-013.md).

## Limitations

- There are no experiments, and no check that any trained model satisfies
  Γ ⊆ N or Γ_q ⊆ M. Whether the relational properties reported by Hernandez
  et al. and others fall under Theorem 14 is not tested.
- Exact distributional equality only. The authors grant that trained models
  are misspecified and are not global maximisers, so the bridge to real
  models (§3.4) is conditional. Approximate equivalence is left to later
  work.
- One vocabulary only.
- Footnote 5 says that if Γ ⊄ N, relational linearity "would be trivially
  satisfied" because γᵀ f(x) = 0. The reasoning fits Γ ⊆ N^⊥, not every
  Γ ⊄ N, so the footnote is loosely stated. Theorem 14 is not affected.
- The D.1 construction is shown only up to proportionality ("∝"), not as a
  worked pair of models.
- §6's explanation of PCA-visible parallelism by inductive bias is a
  hypothesis. The authors offer it as a framework for future empirical work.

## Open questions

- Do trained language models satisfy Γ ⊆ N and Γ_q ⊆ M for the relations in
  which linearity has been reported? A measurement of M, N and Γ_q in
  released models would settle it.
- What survives under approximate equivalence, for models with small but
  non-zero divergence (the question [LIT-253](../literature.d/LIT-253.md) takes up)?
- Which selection within the ∼EL class does training make, and is the
  selected subset the same across architectures? A result there would turn
  §6's hypothesis into a claim.
- For [QUESTION-027](../questions.d/QUESTION-027.md): are there properties that are not functions of the
  observed law, yet are shared by every model that a stated training
  procedure produces? Those would be signatures identified by the procedure
  rather than by the data.
