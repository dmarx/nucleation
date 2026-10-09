---
status: Read
paper: 'LIT-tmptn5dr'
title: 'Wang & Busemeyer, the QQ model and QQ equality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the typeset journal PDF (Topics in Cognitive
    Science 5(4):689–710, 22 pp.) on Jerome Busemeyer's Indiana University
    site (jbusemey.pages.iu.edu/quantum/QuestOrdEff.pdf), text extracted
    with pdftotext. Read: abstract, §§1–8, notes 1–3, references and the
    Appendix. The Appendix derivation of the order effect and of the QQ
    equality was followed line by line. Table 1 was checked against the
    PDF without layout, because the layout extraction drops minus signs,
    and its q values were recomputed from the response proportions for
    Clinton–Gore and Rose–Jackson. Figures 1–2 were read from their
    captions and the prose; the images did not survive extraction. The
    Markov-model proof the paper says is "available upon request" was not
    sought.
date: '2026-10-09'
summary: >-
  Derives the QQ equality from a Lüders-projection model of answering
  attitude questions: the probability of answering two questions
  differently is the same in both orders, for any belief state, any
  projectors and any dimension, provided only the first answer changes the
  state before the second. It holds in five of six data sets and fails, as
  the authors predicted, in the sixth, where new information came between
  the questions. The argument that classical models fail it is informal.
---

<!-- inactive-ok-file: THEORY-013 — Proposed; this reading bears on it without settling its promote_when -->
<!-- inactive-ok-file: THEORY-tmp9wyar — Proposed; this reading is one of its sources -->
<!-- inactive-ok-file: LIT-316 — Deferred; the book is unread here -->

# NOTE-tmpp880r: Wang & Busemeyer, the QQ model and QQ equality

## Contribution

Order effects in surveys were known and catalogued (Moore 2002 named four
patterns), and quantum-probability models had been fitted to them, but a
fit says little. This paper derives from the quantum model a constraint
with no free parameters that order effects must meet, the QQ equality,
and tests it on six data sets. It also gives a similarity index h that
sets the direction of the order effect, and argues that Bayesian and
Markov models do not generally impose the constraint.

## Key insight

If the second answer is computed from the state left by the first, as a
projection, then the probability that the two answers agree is a
quadratic form symmetric in the two projectors. Order can move
probability between yes–yes and no–no, and between yes–no and no–yes, but
it cannot move it between "agree" and "disagree". The model's surprise is
in what order cannot change.

## Assumptions

- Belief is a unit vector S in an N-dimensional Hilbert space, the same
  for both orders (in the 2014 paper, a common density matrix across a
  population).
- Each answer is a subspace with an orthogonal projector; the answers to
  one question are mutually orthogonal and their projectors sum to I.
- p(answer) = ‖P S‖², and the post-answer state is P S/‖P S‖ (Lüders'
  rule).
- **The critical one:** "the only factor that changes the context or the
  state for answering a question is answering its preceding question"
  (§4). Information read out between questions breaks it.
- Binary answers. Respondents who gave neither yes nor no are dropped
  (Table 1 note).

## Key results

- **Order effect** (Eq. 1a, Appendix): Γ_C = TP_C − p(Cy) =
  2·Re⟨S|P_G P_C (I − P_G)|S⟩ = 2p(GyCy) − 2h·√p(Cy)·√p(Gy), with
  h = R cos φ, R = |⟨S|P_G P_C|S⟩|/(‖P_C S‖‖P_G S‖) ∈ [0, 1], so
  −1 ≤ h ≤ 1. Commuting projectors give Γ = 0: non-commutativity is
  necessary for an order effect in this model.
- **Same h for both questions**, because
  Re⟨S|P_C P_G|S⟩ = Re⟨S|P_G P_C|S⟩. Eliminating h between Eqs. 1a and 1b
  gives the **QQ equality**: q = [p(AyBn) + p(AnBy)] − [p(ByAn) + p(BnAy)]
  = 0.
- **h is observable** (Eq. 2): h = (0.5·Γ_C + p(GyCy))/√(p(Cy)p(Gy)), and
  likewise from Γ_G; for Clinton–Gore the two estimates are .8397 and
  .8421.
- **Directions of effect** (Table 2): consistency, contrast, additive and
  subtractive effects correspond to h relative to the ratios
  a = p(ByAy)/√(p(Ay)p(By)) and b = p(AyBy)/√(p(Ay)p(By)).
- **Data** (Table 1): q = −.0031 (z = .109), −.0031 (z = .090), −.0189
  (z = .742), .1514 (z = 5.30; χ²(1) = 28.57) for Rose–Jackson, .0757
  (z = 1.216) and .0430 (z = .831). I recomputed Clinton–Gore
  (.2214 − .2246 = −.0032) and Rose–Jackson (.3419 − .1905 = .1514) from
  the proportions.
- **A three-question test** is proposed, not carried out: in a
  two-dimensional model, h_AB and h_BC predict h_AC.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under Lüders-rule projection from a common state, the probability of disagreeing answers is order-invariant for any projectors in any dimension | strong (proof) | Appendix; re-derived independently in [LIT-264](../literature.d/LIT-264.md) §3 |
| C2 | In this model, order effects require non-commuting projectors | strong (proof) | Appendix |
| C3 | Five question-order data sets satisfy the QQ equality | moderate: six data sets, N about 100–500 per order | Table 1, §5 |
| C4 | The equality fails when information is inserted between questions | weak: one case, explained after the model was formulated but stated as a prediction | Rose–Jackson, §5 |
| C5 | Bayesian and Markov models do not generally satisfy the QQ equality | weak: an informal argument; the Markov proof is withheld | §6 |
| C6 | Quantum probability is "a powerful natural explanation" for survey order effects | not established by the evidence here | §8 |

## Method

Not an algorithm. The test is a one-degree-of-freedom comparison: a
z-test of q = p_AB − p_BA against zero with variance 2p(1 − p)/N, and a
likelihood-ratio χ² comparing binomial models of the two 2 × 2 tables
with and without the constraint p_AB = p_BA.

## Concepts

- **non-comparative / comparative context**: a question asked first, or
  second, after the other question (Moore's terms).
- **order effect** Γ: TP(answer asked second) − p(answer asked first).
- **similarity index h**: the normalised real part of ⟨S|P_G P_C|S⟩; the
  cosine between the two "yes" rays in the two-dimensional example.
- **law of reciprocity**: the paper's name, after Peres, for
  |⟨S_B|S_A⟩|² = |⟨S_A|S_B⟩|².
- **compatible / incompatible questions**: commuting or non-commuting
  projectors; incompatible pairs are expected to be new or unusual
  combinations whose answers are constructed on the spot (§8.1).

## Connections

It rests on Moore (2002) for the data and the taxonomy, Peres (1998) for
reciprocity, and Niestegge (2008), who derived the same property for an
axiomatic analysis of quantum theory. The 2014 PNAS paper, [LIT-tmp56yt5](../literature.d/LIT-tmp56yt5.md),
tests the equality on 72 studies. [LIT-264](../literature.d/LIT-264.md) re-derives it in two lines from
P Q P + (I − P)(I − Q)(I − P) = I − (P + Q) + (P Q + Q P) and shows it
implies noncontextuality in the Contextuality-by-Default sense. The
general framework is [LIT-316](../literature.d/LIT-316.md), unread here.

## Bearing on the record

- **Sources [THEORY-tmp9wyar](../theory.d/THEORY-tmp9wyar.md)**, with [LIT-tmp56yt5](../literature.d/LIT-tmp56yt5.md) (primary) and [LIT-264](../literature.d/LIT-264.md).
- **[THEORY-013](../theory.d/THEORY-013.md).** This paper is the model [LIT-264](../literature.d/LIT-264.md) uses to argue that a
  quantum model can predict the absence of contextuality. Nothing here
  speaks to contextuality; the paper does not use the word.
- **On the derivation.** The paper attributes the equality to the law of
  reciprocity for transitions between rays (§4, note 3). The Appendix
  uses less: only Re⟨S|P_G P_C|S⟩ = Re⟨S|P_C P_G|S⟩, which holds because
  projectors are self-adjoint. The equality is a property of
  self-adjoint projectors under Lüders updating from a common state, not
  of rays in particular. This is my reading of the Appendix, and it
  agrees with the re-derivation in [LIT-264](../literature.d/LIT-264.md).
- **On "order sensitivity establishes non-commutativity".** Within the
  model, an order effect needs non-commuting projectors. The paper itself
  (§6) says a Bayesian model with order events and a Markov model with
  memory both produce order effects, so the order effect alone does not
  select the quantum model. What the paper offers in its place is the
  QQ equality.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Six data sets, four of them chosen from a review of order effects.
- The classical alternatives are dismissed rather than tested: the
  Bayesian argument shows only that an order-conditioned model is
  unconstrained, and the Markov proof is not given. A classical model
  constrained to satisfy the equality is not considered here (the 2014
  paper concedes one can be built).
- Rose–Jackson is "predicted" to fail by an explanation stated alongside
  the data; no independent case with inserted information is tested.
- Respondents without a yes/no answer are dropped, which may not be
  random with respect to order.

## Open questions

- Does a classical model with memory and order-dependent updating that
  satisfies the QQ equality also reproduce the order effects observed?
  A worked counterexample would answer C5.
- The three-question prediction of §7 (h_AC from h_AB and h_BC) is
  untested here.
- Whether the Rose–Jackson failure is reproduced by the extended model
  with transformations between questions, fitted without access to the
  q value.
