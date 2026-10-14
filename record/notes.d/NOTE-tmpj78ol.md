---
status: Read
paper: LIT-251
title: 'Tosh, Krishnamurthy & Hsu — contrastive learning, multi-view redundancy and linear models'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v2 PDF (arxiv.org/pdf/2008.10150, 27 pp.,
    dated 16 April 2021), text extracted with pdftotext: §1–5, the
    references, Appendix A (every proof, A.1–A.10) and Appendix B (the
    transfer-learning results, Lemmas 14–16 with proofs). Figure 1 was
    seen only through its caption. The PMLR version (ALT 2021, PMLR
    132:1179–1206) was not compared line by line.
date: '2026-10-14'
summary: >-
  When two views X and Z are redundant for a label, the predictor that
  infers Z from X and then predicts, µ(x) = E[E[Y|Z]|X=x], is within
  εX + 2√(εXεZ) + εZ of the Bayes predictor. µ is linear in the density
  ratio g*(x,·) = p(x,z)/(p(x)p(z)), the optimum of the logistic
  contrastive problem, so m random landmark evaluations of g* support a
  linear predictor whose extra error falls as 1/m, scaled by a variance
  that is at most E[g*²] for bounded labels. Nothing requires the views
  to be exchangeable.
---
<!-- inactive-ok-file: THEORY-001 THEORY-005 THEORY-009 THEORY-tmpqpbhy THEORY-tmp1iy33 — Proposed; the accounts this reading bears on, and the one filed from it -->

# NOTE-tmpj78ol: Tosh, Krishnamurthy & Hsu — contrastive learning, multi-view redundancy and linear models

## Contribution

The paper gives downstream guarantees for contrastive learning from a
redundancy assumption on the label instead of conditional independence of
the views. It shows that, when each view alone predicts the label almost
as well as both together, the predictor obtained by inferring one view
from the other is near Bayes-optimal. That predictor is an integral of the
contrastive optimum, the density ratio of joint to product, against
E[Y|Z]. So linear functions of a landmark embedding built from the ratio
are near-optimal, with explicit dimension and error-propagation bounds.

## Key insight

The logistic contrastive problem learns g*(x,z) = p(x,z)/(p(x)p(z)), and
g*(x,·) is the change of measure from p_Z to p_(Z|X=x). Any target of the
form E[h(Z)|X=x] is therefore ∫ h(z) g*(x,z) p_Z(z) dz, a linear
functional of g*(x,·). Redundancy says the Bayes predictor is close to
such a target with h = E[Y|Z]. So the label never enters the
representation; it enters only through how redundant the two views are
about it.

## Assumptions

- **Two views and a label** (X, Z, Y) with a joint density or mass
  function. X and Z may live in different spaces. Nothing assumes they
  are exchangeable or that the joint is symmetric.
- **Redundancy**, not formalized at a scale: εX = E[(E[Y|X] − E[Y|X,Z])²]
  and εZ = E[(E[Y|Z] − E[Y|X,Z])²] are small. The conditional means need
  not be linear.
- **The contrastive distribution** (§2.2): a fair coin chooses between a
  same-datum pair (X, Z, +1) and an independent pair (X, Z̃, −1).
- **Optimization over all functions** for f* and g*; estimation and
  function-class error are handled only through the excess loss in §5.
- **Bounded labels**, Y ∈ [−1, 1], for Propositions 4, 5, 8, 9 and
  Theorem 10.
- **A bounded density ratio** for the error propagation of §5:
  g_max = sup g* over supp(p_X ⊗ p_Z) is finite, and the learned g, or
  ηᵀψ, is bounded by the same g_max.
- **A hidden variable H** with X ⊥ Z | H for the direct-embedding results
  of §4. One always exists (H = (X, Z)); the bounds are useful only when a
  simpler one does.

## Key results

- **Optimum of the logistic problem (§2.3, Eq. 1).** Over all functions,
  f* = argmin E[log(1 + exp(−Y_c f(X_c, Z_c)))] is the pointwise mutual
  information f*(x,z) = log p(x,z)/(p(x)p(z)), and g* = exp f* is the
  ratio. Stated ("Note that"), not derived; it is the standard Bayes
  logit with equal priors.
- **Lemma 1.** µ(x) := E[E[Y|Z] | X = x] satisfies
  E[(µ(X) − E[Y|X,Z])²] ≤ εX + 2√(εXεZ) + εZ =: εµ. The proof is Jensen
  and AM/GM (App. A.1). *Holds for* any joint law with finite second
  moments.
- **Change of measure (§2.4).** µ(x) = ∫ E[Y|Z=z] g*(x,z) p_Z(z) dz. In
  the paper's words, "g⋆ provides the change-of-measure from the marginal
  distribution of Z to the conditional distribution of Z given X = x",
  and "g⋆ … does not depend on Y at all".
- **Lemma 2 and Theorem 3 (landmarks).** With landmarks Z_1, …, Z_m drawn
  i.i.d. from p_Z and φ*(x) = (g*(x,Z_1), …, g*(x,Z_m)), with probability
  1 − δ some w has E[(wᵀφ*(X) − µ(X))² | Z_1..m] ≤ εlm :=
  2 var(E[Y_1|Z_1] g*(X,Z_1)) / ⌊m/log₂(1/δ)⌋, and
  E[(wᵀφ*(X) − E[Y|X,Z])²] ≤ εµ + 2√(εµεlm) + εlm. The proof is a
  median-of-means block argument (App. A.2).
- **Topic model (Prop. 4).** Disjoint topics, two-token documents,
  Dirichlet(α) mixing: εlm = O(log(1/δ)/m) for α = Θ(1) as K → ∞, and
  O(K² log(1/δ)/m) for α ≤ 1/K.
- **Gaussian model (Prop. 5).** H ∼ N(0, σ²), X, Z | H ∼ N(H, 1):
  E[g*(X, Z̃)²] = (1 + σ²)²/(1 + 2σ²) for independent X, Z̃, so
  εlm = O((log(1/δ)/m)(1 + σ⁴/(1 + 2σ²))) for every σ² > 0.
- **Discrete hidden variable (§4.1).** If H takes |S| values,
  g*(x,z) = η*(x)ᵀψ*(z) exactly, with η*(x) = (Pr(H=h|X=x))_h and
  ψ*(z) = p(z|h)/p_Z(z), and a linear function of η* reproduces µ.
- **Lemma 6.** For any η, ψ there is w with
  E[(wᵀη(X) − µ(X))²] ≤ E[Y²]·E[(η(X)ᵀψ(Z̃) − g*(X,Z̃))²], with
  (X, Z̃) ∼ p_X ⊗ p_Z.
- **Lemma 7.** For any H with X ⊥ Z | H and any m, some η, ψ: X, Z → Rᵐ
  approximate g* in that sense with error
  (1/m)·var(p(X|H̄)p(Z̃|H̄)/(p(X)p(Z̃))). Existence only; it does not say
  that minimizers of the direct loss reach it.
- **Props. 8–9.** The topic-model bound matches Prop. 4. In the Gaussian
  model the construction needs σ² < 1/2, giving
  ε_direct ≤ (1/m)(1 + σ²)²/√(1 − 4σ⁴).
- **Theorem 10 (landmark error propagation).** For a learned f with
  g = exp f ≤ g_max, R(φ) ≤ 2εlm + 4(1 + g_max)²√(2ε_opt,lm εlm) +
  16(1 + g_max)⁴ ε_opt,lm, where ε_opt,lm is the excess logistic loss.
  The proof goes through Bernoulli KL and Pinsker (App. A.9).
- **Theorem 11 (direct embeddings).** R(η) ≤ E[Y²](1 + g_max)⁴
  ε_opt,direct, where the direct loss (Eq. 2) is the cross-entropy with
  prediction log(η(x)ᵀψ(z)), so its minimizer is the ratio g* itself and
  not its logarithm (§5: "the minimizer of Llm is the log-odds ratio
  function log ◦g⋆, and the minimizer of Ldirect is the odds ratio
  function g⋆").
- **Appendix B (transfer).** If p(z|x) = q(z|x), landmarks drawn from q_Z
  give the same kind of bound under q, with the variance reweighted by
  p_Z/q_Z (Lemma 15). No other landmark distribution improves on q_Z by
  more than var_q(E_q[Y|Z]) (Lemma 16).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The logistic contrastive problem is solved over all functions by the PMI, so g* is the joint-to-product density ratio | strong | §2.3, stated; standard |
| C2 | Under redundancy, inferring Z from X and then predicting is within εX + 2√(εXεZ) + εZ of Bayes | strong | Lemma 1, proved |
| C3 | That predictor is a linear functional of g*(x,·), which does not depend on Y | strong | §2.4, a one-line identity |
| C4 | m random landmarks suffice for linear prediction, with error O(var/m) | strong | Lemma 2, Theorem 3 |
| C5 | With a finite hidden variable, the ratio factorizes exactly at rank |S| | strong | §4.1, an identity |
| C6 | Low-dimensional direct embeddings that approximate g* exist, with error 1/m times a variance | moderate | Lemma 7, existence only, not reached by any stated procedure |
| C7 | Downstream risk degrades smoothly with excess contrastive loss | moderate | Theorems 10–11, under a uniform bound g_max on the ratio |

## Concepts

- **Redundancy (εX, εZ).** Mean squared gaps between each single-view
  Bayes predictor and the two-view one.
- **Contrastive distribution.** The fair mixture
  ½ p_(X,Z) + ½ p_X ⊗ p_Z, labelled by which component a pair came from.
- **Landmark embedding.** φ(x) = (g(x, Z_1), …, g(x, Z_m)) for landmarks
  drawn from p_Z: a random-feature expansion of the integral operator with
  kernel g*.
- **Direct (bivariate) embedding.** η: X → Rᵐ and ψ: Z → Rᵐ trained so
  that η(x)ᵀψ(z) predicts the odds ratio.
- **µ.** The "infer, then predict" function E[E[Y|Z] | X = x]. It is not
  the Bayes predictor; it is close to it when the views are redundant.

## Connections

The paper sets itself after the CCA analyses of Kakade and Foster (2007)
and Foster et al. (2009), with redundancy in place of their linear
version. It modifies Tosh et al. (2020) on landmark embeddings, and
contrasts with Arora et al. (2019) on latent classes and Lee et al. (2020)
on reconstruction. It places the mutual-information reading of NCE below
redundancy, citing Tschannen et al. and McAllester and Stratos. HaoChen
et al. ([LIT-249](../literature.d/LIT-249.md)) later set themselves against its conditional-independence
style of assumption ([NOTE-740](NOTE-740.md)). Johnson et al. ([LIT-258](../literature.d/LIT-258.md), App. B.2) take
the logistic optimum from here. Zhai ([LIT-975](../literature.d/LIT-975.md), [THEORY-tmp1iy33](../theory.d/THEORY-tmp1iy33.md)) works with
the same conditional-expectation operator between two spaces and gets the
top singular functions as the minimax span. This paper does not take
singular functions at all: it reads µ off the full ratio by random
landmarks.

## Bearing on the record

- **[THEORY-001](../theory.d/THEORY-001.md) cites §2.3 for the logistic optimum, and the citation is
  right**, with two qualifications. The PMI optimum is stated, not
  derived. And it holds for general densities on two possibly different
  spaces, which is wider than [THEORY-001](../theory.d/THEORY-001.md)'s finite augmentation space.
- **[THEORY-001](../theory.d/THEORY-001.md) quotes §2.4 inexactly.** Its quotation "the change-of-measure
  from P_Z to P_(Z|X=x)" is not in the paper. The paper's words are
  "g⋆ provides the change-of-measure from the marginal distribution of Z
  to the conditional distribution of Z given X = x". The sense is right;
  the quotation marks are not.
- **[THEORY-001](../theory.d/THEORY-001.md)'s "does not say" has published support here.** It says
  that InfoNCE and skip-gram fit the log of the ratio while the spectral
  loss fits the ratio itself. §5 makes the same contrast for this paper's
  two losses: the logistic loss is minimized by log g*, the direct loss
  with prediction log(ηᵀψ) by g*. [THEORY-001](../theory.d/THEORY-001.md) could cite it there.
- **[THEORY-005](../theory.d/THEORY-005.md) describes µ as "the Bayes predictor under redundancy".** It
  is not. µ is the infer-then-predict function, within
  εX + 2√(εXεZ) + εZ of the Bayes predictor E[Y|X,Z] (Lemma 1). The
  integral is the paper's; calling it an operator is the record's. The
  paper has no L² setting, no spectrum and no eigenfunctions.
- **For [THEORY-005](../theory.d/THEORY-005.md)'s integrability condition.** The quantity that controls
  the landmark bound is var(E[Y|Z]g*(X,Z̃)) ≤ E[g*(X,Z̃)²] for |Y| ≤ 1,
  with X and Z̃ independent. That expectation is ∫∫ g*² dp dp = 1 + χ²
  of the joint against the product, the same Hilbert–Schmidt quantity
  [THEORY-005](../theory.d/THEORY-005.md) asks for. In the Gaussian model, Prop. 5 computes it as
  (1 + σ²)²/(1 + 2σ²) = 1/(1 − ρ²) with ρ = σ²/(1 + σ²). The identity
  with χ² is my algebra; the paper names neither χ² nor Hilbert–Schmidt.
  The error-propagation theorems need more than this: a uniform bound
  g_max, like HaoChen et al.'s Assumption F.1. So the paper is a
  published use of finite E[g*²] as the operative condition, for landmark
  features. It is not the operator eigenfunction formulation that
  [THEORY-005](../theory.d/THEORY-005.md)'s promote_when asks for, and it does not meet it.
- **For [QUESTION-052](../questions.d/QUESTION-052.md) and [THEORY-009](../theory.d/THEORY-009.md).** The guarantee needs no symmetry:
  X and Z may be different spaces with a non-exchangeable joint. For
  linear decisions about redundant labels, the full density-ratio kernel
  is sufficient without any eigen- or singular decomposition. This
  answers the directed half of [QUESTION-052](../questions.d/QUESTION-052.md) in part, for the full kernel
  rather than for a low-dimensional signature.
- **Filed from this reading:** [THEORY-tmpqpbhy](../theory.d/THEORY-tmpqpbhy.md), the redundancy account.
- The landmark construction and the direct loss are methods; nothing here
  is ML-practice advice beyond them, and they are not filed as practice.

## Limitations

- Population-level throughout. Section 5 relates downstream risk to excess
  contrastive loss but leaves estimation and function-class error inside
  that excess, and the bounds carry (1 + g_max)⁴, which is large when the
  views are informative about each other.
- The direct-embedding results are existence results (Lemma 7). The paper
  says they "do not guarantee that there exist useful minimizers of (2)
  for any given dimension".
- The contrastive problem is the logistic one with a single negative. It
  is not InfoNCE with many negatives.
- Redundancy is assumed, not measured, and the examples (topic and
  Gaussian models) are illustrations.
- Theorem 10 writes f: X × X → R where X × Z is meant.

## Open questions

- Can the landmark bound be stated directly in terms of χ² of the joint
  against the product, and does the top-d singular truncation of g*
  ([THEORY-tmp1iy33](../theory.d/THEORY-tmp1iy33.md)) give a dimension bound under redundancy that improves
  on the random-landmark rate?
- What replaces g_max in Theorems 10–11 when the ratio is unbounded but
  square-integrable?
