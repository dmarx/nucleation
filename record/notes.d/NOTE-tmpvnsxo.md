---
status: Read
paper: LIT-tmp07k7g
title: 'Xu, Zhao, Song, Stewart and Ermon — A theory of usable information under computational constraints'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from arXiv:2002.10689v1 (24 pages, headed "Published as
    a conference paper at ICLR 2020"), text extracted with pdftotext.
    Read: §§1–8, Appendix A (the proofs of Propositions 1–2, Lemmas 3–4,
    Theorem 1, Corollary 1.1 and Theorem 2), Appendix B (the CPC and NWJ
    estimators), C (Algorithm 1), D (experimental setup), E (minimality of
    the predictive family) and F (limitations). Absolute-value bars and
    some subscripts were lost in extraction and are restored from the
    proofs' use of them. The figures were read from captions and text.
    The XOR example, the linear-Gaussian case, the bound by Shannon
    information and its counterexample were re-derived here and checked
    numerically.
date: '2026-10-21'
summary: >-
  Defines predictive V-information, I_V(X → Y) = H_V(Y | ∅) − H_V(Y | X),
  where each V-entropy is the least expected log loss a predictor in the
  family V can reach. With V unrestricted it is Shannon mutual
  information; with linear-Gaussian V it is R² times the variance. It is
  non-negative and zero under independence because V must be able to
  ignore its input. Unlike Shannon information it can be asymmetric and can
  be raised by computing on X, and its empirical estimate is within
  4R(G_V) + 2B√(2 log(1/δ)/N) of the truth with probability 1 − 2δ. It is
  not bounded by Shannon information unless V's input-free predictions
  can match the marginal of Y.
---
<!-- inactive-ok-file: CLAIM-199 CLAIM-081 CLAIM-087 CLAIM-050 CLAIM-326 — Proposed; the claims this reading bears on, cited as open -->
<!-- inactive-ok-file: THEORY-156 — Proposed; the reading of Blackwell's order, named for contrast -->

# NOTE-tmpvnsxo: Xu, Zhao, Song, Stewart and Ermon — A theory of usable information under computational constraints

## Contribution

It gives information a definition relative to an observer's predictive
power. A predictive family V is the set of predictors an agent may use.
The V-entropy of Y is the least expected log loss reachable in V, with or
without side information X, and V-information is the drop between them.
Shannon's quantities are the case V = Ω, all predictors. Restricting V
loses the data-processing inequality, which the authors present as a
feature, and gains estimability: bounds on V's complexity become PAC
bounds on estimating V-information. They apply it to structure learning
(a directed Chow–Liu tree), gene-network inference, ordering video frames
and fair representations.

## Key insight

Information "usable" by an observer is a property of the pair (data,
observer's rule class), and computation by someone else can increase it.
"Unlike Shannon's mutual information and in violation of the data
processing inequality, V-information can be created through
computation." The encrypted message has full Shannon information about the
plan and none a bounded reader can use; decryption raises the usable
information without raising the Shannon information.

## Assumptions

- Densities or mass functions exist with respect to the underlying
  measure; ∅ ∉ X (footnote 1).
- **Optional ignorance** (Definition 1): for every f ∈ V and every P in
  f's range, V contains an f′ with f′[x] = P for every x and f′[∅] = P.
  The agent can always ignore X. Appendix E shows that without it
  V-information can be negative, or positive for independent X and Y.
- Log loss throughout: H_V(Y | X) = inf_{f∈V} E[−log f[X](Y)].
- Theorem 1: |log f[x](y)| ≤ B for every f ∈ V, x and y. Corollary 1.1
  adds bounded inputs and outputs (‖x‖ ≤ k_x, ‖y‖ ≤ k_y) and a linear
  Gaussian family with ‖(W, b)‖₂ ≤ 1.
- Theorem 2: one predictive family per ordered pair of variables, samples
  per pair, and Theorem 1's bound.

## Key results

- **Definitions 1–3.** Predictive family; H_V(Y | X) and H_V(Y) = H_V(Y | ∅);
  I_V(X → Y) = H_V(Y | ∅) − H_V(Y | X).
- **Proposition 1.** (1) V = Ω gives Shannon entropy, conditional entropy
  and mutual information. (3) Gaussians N(µ, ½I) with free mean give
  tr Cov(Y) + (d/2) log π. (4) A minimal exponential family gives the
  maximum Shannon entropy under the same expected sufficient statistics.
  (5) Linear means with Σ = ½I give I_V(X → Y) = R² · tr Cov(Y), "the
  (unnormalized) maximum coefficient of determination". Re-derived here:
  each −log density is ‖y − µ‖² plus a constant, so the difference of the
  two infima is the explained sum of squares.
- **Proposition 2.** Monotonicity (V ⊆ U gives H_V ≥ H_U), non-negativity
  and zero under independence, each from optional ignorance.
- **§3.2, no theorem.** Computing on X can raise V-information:
  I_V(t(X) → Y) > I_V(X → Y) ≈ 0 for t a decryption. Argued from RSA and
  representation learning. The record's exact instance is in
  [THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md).
- **§3.3, no theorem.** If h is one-way and V is polynomial-time
  predictors, I_V(X → h(X)) ≫ I_V(h(X) → X).
- **Theorem 1.** For log-likelihoods in [−B, B] and δ ∈ (0, 0.5), with
  probability at least 1 − 2δ,
  |I_V(X → Y) − Î_V(X → Y; D)| ≤ 4R_|D|(G_V) + 2B √(2 log(1/δ) / |D|),
  with G_V the class of log-likelihood functions of V. Typically
  R_N(G_V) = O(N^(−1/2)).
- **Corollary 1.1.** For the bounded linear-Gaussian family, with
  M = (k_x + k_y)² + log 2π, the error is at most
  (M / √(4|D|)) (1 + 4√(2 log(1/δ))).
- **Theorem 2.** The directed tree built from estimated V-information on
  each edge has total weight within 2(m − 1) max_{i,j}{…} of the optimal
  directed tree, with probability at least 1 − 2m(m − 1)δ. The authors
  add that a larger C(g) "does not necessarily lead to better Chow-Liu
  trees".
- **Appendix B.** CPC is at most log N (batch size N). At its optimum the
  NWJ estimator has variance at least (e^{I(X;Y)} − 1)/N.
- **Experiments (§6).** Chow–Liu trees on synthetic 10-dimensional
  variables (7 to 20 nodes), ten repeats: the Gaussian family "only
  requires about 100 samples to recover the ground-truth Chow-Liu tree in
  simulation-A". DREAM5 in-silico gene network (20 genes, 660 points):
  higher AUC than KDE, KSG, mixed KSG and partitioning. Moving-MNIST:
  PixelCNN++ V-information falls with frame distance and recovers the
  order, and for deterministic dynamics up to distance about 9, where every
  pair of frames has the same Shannon information. Fairness (Adult, German,
  Heritage): features trained against one adversary family leak to
  another.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | V-information generalizes Shannon information, R² and other notions of predictability | strong | Proposition 1, with proofs; (5) re-derived here |
| C2 | Optional ignorance is what makes V-information non-negative and zero under independence, and it cannot be dropped | strong | Proposition 2; Appendix E's converse constructions |
| C3 | Computation can create usable information, against the data-processing inequality | moderate as argued, strong as a fact | informal examples in §3.2; an exact instance is re-derived in [THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md) |
| C4 | V-information can be asymmetric, as with one-way functions | moderate | §3.3, argued from the definition of one-way functions, no theorem |
| C5 | V-information can be estimated with PAC guarantees set by V's Rademacher complexity | strong | Theorem 1 and Lemmas 3–4, a standard symmetrization argument; checked in [THEORY-tmp9m1g4](../theory.d/THEORY-tmp9m1g4.md) |
| C6 | Chow–Liu with V-information recovers trees better than Shannon estimators in high dimension | moderate | §6.1, synthetic, ten repeats; Theorem 2 bounds the objective, not the tree |
| C7 | Fair representations trained against one discriminator family need not hide the attribute from another | moderate | §6.4 and Fig. 3b, three datasets, three families |
| C8 | Representation learning "can be justified in the information theoretic context" by V-information | weak | an interpretation of C3 |

## Concepts

- **Predictive family V**: a set of maps from X ∪ {∅} to distributions on
  Y, closed under optional ignorance.
- **V-entropy, H_V(Y | X)**: inf over f ∈ V of E[−log f[X](Y)]. H_V(Y) is
  the same with ∅ in place of X.
- **Predictive V-information, I_V(X → Y)**: H_V(Y | ∅) − H_V(Y | X). It is
  directed, and the arrow matters.
- **Empirical V-information**: the same with the empirical distribution of
  a sample in place of the joint law.

## Connections

It extends Shannon (1948) and Cover and Thomas, and puts itself beside
H-entropies (DeGroot 1962; Grünwald and Dawid 2004; Duchi et al. 2018).
The difference, by its account, is the emphasis on bounded computation and
on estimability. Its estimation argument follows Bartlett and Mendelson
(2001), and Corollary 1.1 follows Kakade, Sridharan and Tewari (2008). The
structure-learning application builds on Chow and Liu (1968) and Chu and
Liu (1965). It argues against the variational Shannon estimators CPC (van
den Oord et al. 2018), NWJ (Nguyen et al. 2010) and MINE (Belghazi et al.
2018).

## Bearing on the record

- **[CLAIM-199](../claims.d/CLAIM-199.md).** The claim's "usable information relative to the rules it
  can apply" is V-information under log loss, with V the receiver's rule
  class. Its XOR example (Z = X₁ ⊕ X₂, one-coordinate receiver) holds
  exactly in Xu et al.'s terms, and also for the linear predictive
  families the paper studies: linear logistic and linear-Gaussian V give
  I_V(X → Z) = 0 and I_V(X₁ ⊕ X₂ → Z) = log 2 (or R² · Var = 1/4), while
  I(X; Z) = I(X₁ ⊕ X₂; Z) = log 2 ([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)). The claim's ceiling,
  stated for risk, holds as stated. Stated for V-information, it holds
  only when V's input-free predictions include the marginal of Z, as the
  one-coordinate receiver's do. Otherwise V-information can exceed
  Shannon information ([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)'s counterexample). The claim's "the
  literature on usable information is not held here" is now out of date.
- **[TERM-tmp5lqn0](../terms.d/TERM-tmp5lqn0.md).** A22's score L_{o,𝒬,B}(T) is a negative V-entropy for
  log loss, with Π_{o,B} as V. A22's "legibility need not be monotone in
  informational refinement for bounded observers" is Xu et al.'s failure
  of the data-processing inequality. A22's caution that "the loss function
  and task family must be specified independently" is sharpened by §6.4:
  a representation tuned to be illegible to one family V_i stays legible
  to another V_j. So what an observer cannot read depends on which observer
  you have in mind.
- **[CLAIM-225](../claims.d/CLAIM-225.md).** Its objection, that Blackwell's order measures an ideal
  decision-maker and not a given receiver, is Xu et al.'s distinction
  between I_Ω and I_V. The paper does not mention Blackwell.
- **[CLAIM-081](../claims.d/CLAIM-081.md) and [CLAIM-270](../claims.d/CLAIM-270.md).** "A message can become more legible while
  becoming less informative about what originally happened": in V-terms,
  I_V(t(X) → Y) can rise while I(t(X); Y) falls. The paper does not
  construct such a case. Its examples keep Shannon information fixed.
- **[QUESTION-110](../questions.d/QUESTION-110.md).** V-information fixes two of A18's three parameters, a
  class of procedures and a success criterion (log loss), and recovers
  [CLAIM-199](../claims.d/CLAIM-199.md)'s rule-class case. It has no cost of recovery, only a class,
  so it does not answer the question as posed. [CLAIM-304](../claims.d/CLAIM-304.md)'s computational
  case corresponds to V a class of efficient predictors, which §3.3
  gestures at without a theorem.
- **[QUESTION-111](../questions.d/QUESTION-111.md)** gains a measurable quantity. Theorem 1 says when it can
  be estimated from samples.
- **[NOTE-820](NOTE-820.md) and [THEORY-281](../theory.d/THEORY-281.md)** (concept erasure). Their remark that
  "empirical leakage is a lower bound" is §6.4's finding. Erasure certified
  against one family of probes is not erasure against another.

The paper is about machine learning but carries no instruction for
practice. It is flagged `anthology-candidate` on its LIT.

## Limitations

- **The data-processing violation has no theorem.** §3.2 argues from RSA
  and from image features. The authors give no example worked out in
  numbers. [THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md) supplies one.
- **No bound by Shannon information.** Nothing in the paper says
  I_V ≤ I. Because H_V(Y) can exceed H(Y), V-information can exceed
  Shannon information ([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)). The paper neither claims the
  bound nor warns against assuming it.
- **Proposition 1.2.** The infimum over µ of E‖Y − µ‖ is the deviation
  about the geometric median, not about E[Y] as the proof's "MAD" is
  defined.
- **Additivity is lost.** Appendix F: the chain rule
  H(X, Y) = H(X) + H(Y | X) "does not hold true for general V-Information".
- **Theorem 2 bounds the tree's weight, not its edges.**
- **The experiments are small.** Ten repeats, synthetic trees of up to 20
  nodes, one gene dataset of 660 points and three fairness datasets.
- **Typography.** Proposition 1.1 writes I_Ω(Y → X) where X → Y is meant
  (harmless for Ω). Lemma 3 states the constant 2B where its proof gives
  B, so the stated bound is looser than the one proved.

## Open questions

- Which predictive families keep V-information bounded by Shannon
  information? Containing the marginal of Y in the input-free predictions
  is sufficient ([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)). Is it necessary?
- Is there a garbling ordering for a fixed V, analogous to Blackwell's,
  that says when one representation is more V-informative than another
  for every Y? Restricting rules loses Blackwell's theorem ([THEORY-176](../theory.d/THEORY-176.md)), and
  the paper offers no replacement.
- Can a family of V's indexed by a computational budget recover
  [CLAIM-304](../claims.d/CLAIM-304.md)'s pseudorandom construction as a theorem?
