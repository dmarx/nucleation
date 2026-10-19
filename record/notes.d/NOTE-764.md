---
number: 764
status: Read
formerly:
- NOTE-tmp6qamv
paper: LIT-994
title: 'Thrampoulidis et al. — Imbalance Trouble'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv PDF (v1 of 10 August 2022, 66 pages with the
    supplement), fetched from arxiv.org/pdf/2208.05512 and extracted with
    pdftotext, plain and -layout. Read in full: the main text (§§1–6) and
    the parts of the supplement the main claims rest on. Those are Lemma
    A.1, the statement of Lemma A.3 (the SVD of the SEL matrix), F.1–F.2,
    G.1.1–G.1.3 with Tables 2–3, G.2, §H on minority collapse, and I.5.
    The proofs of Theorem 1 (C.1) and of Propositions 1–2 (E.2–E.3) were
    followed as sketched in §3.3 and §4.2, not line by line. The
    closed-form norms and angles of §B were taken as stated. The figures
    were read from their captions and the text.
date: '2026-10-14'
summary: >-
  In the unconstrained-features model with cross-entropy and vanishing
  regularization, the max-margin solutions have logits exactly equal to the
  simplex-encoded label matrix Ẑ (one-hot minus 1/k), whatever the class
  imbalance. The classifier and embedding Gram matrices are VΛVᵀ and UΛUᵀ
  from Ẑ's SVD. This SELI geometry is the simplex ETF only for balanced or
  binary data. Under imbalance, majority classifiers are longer and
  minority classifiers closer together. No finite weight decay gives SELI,
  and SGD approaches it more slowly as imbalance grows.
---
<!-- inactive-ok-file: THEORY-083 THEORY-209 THEORY-286 — Proposed; the record's statement of collapse, its account of limiting dynamics, the MSE account filed beside this reading, and the account filed from it -->

# NOTE-764: Thrampoulidis et al. — Imbalance Trouble

## Contribution

Neural collapse's simplex ETF was a statement about balanced data. This
paper finds the geometry that the unconstrained-features model prefers at
any step imbalance. The geometry is explicit, and it reduces to the ETF
when classes are balanced or there are two of them. It also shows that
under imbalance, unlike the balanced case, the regularized solution depends
on the regularization strength. It gives the minority-collapse threshold in
closed form.

## Key insight

What stays fixed across imbalance is not the shape of the means but the
logits. At the max-margin solution every logit is 1 − 1/k for the true
class and −1/k for the others: the label's simplex encoding, every margin
equal. The vectors' geometry is whatever factorization of that matrix
costs least, which is its SVD. Imbalance changes the SVD, so it changes
norms and angles, but it never changes the logits.

## Assumptions

- **Unconstrained features.** H (d × n) and W (d × k) are free, with
  d ≥ k − 1. Equivalently a two-layer linear net on one-hot inputs.
- **No bias** in the theory, and the deep-net experiments also disable
  the biases of fully connected layers.
- **(R, ρ)-STEP imbalance.** (1 − ρ)k majority classes of R·n_min
  examples and ρk minority classes of n_min. The main formulas use
  ρ = 1/2.
- **Vanishing regularization.** Theorem 1 is about the UF-SVM, the
  direction that gradient descent on unregularized cross-entropy converges
  to *if* it converges to a global minimizer. GD is known to reach only KKT
  points of the non-convex UF-SVM (Lyu & Li; Ji et al.). The authors call
  convergence of GD to SELI conjecture C1.

## Key results

- **Theorem 1 (UF-SVM).** Let (Ŵ, Ĥ) solve
  min ½‖W‖²_F + ½‖H‖²_F subject to (w_(y_i) − w_c)ᵀh_i ≥ 1 for all c ≠ y_i.
  Then p* = ‖Ẑ‖_* = ‖Ĥ‖²_F = ‖Ŵ‖²_F, and:
  - (i) ŴᵀĤ = Ẑ, where Ẑ[c, i] = 1 − 1/k if c = y_i and −1/k otherwise;
  - (ii) ĤᵀĤ = UΛUᵀ and ŴᵀŴ = VΛVᵀ, from the compact SVD Ẑᵀ = UΛVᵀ;
  - (iii) Ŵ = RᵀΛ^(1/2)Vᵀ and Ĥ = RᵀΛ^(1/2)Uᵀ for a partial orthonormal R.

  *Holds:* any (R, ρ), d ≥ k − 1. The proof shows Ẑ is the unique
  minimizer of the nuclear-norm relaxation, via a strictly feasible
  dual B̂ = UVᵀ, and that the relaxation is tight when d ≥ k − 1.
- **Corollary 1.1.** Embeddings collapse to class means (NC) at any
  imbalance. Corollary 1.3: for R = 1 or k = 2, SELI is the ETF, Ŵ = M̂ and
  M̂ᵀM̂ = I − (1/k)11ᵀ.
- **Lemma 3.1 (norms, ρ = 1/2).**
  ‖w_maj‖²/‖w_min‖² = [(1 − 2/k)√R + √((R+1)/2)/k] / [(1 − 2/k) + √((R+1)/2)/k]
  and ‖h_maj‖²/‖h_min‖² = [(1 − 2/k)/√R + 1/(k√((R+1)/2))] / [(1 − 2/k) + 1/(k√((R+1)/2))].
  Majority classifiers are longer and majority embeddings shorter, with
  equality iff R = 1 or k = 2. The bracketing of these two formulas was
  restored by eye from the -layout extraction.
- **Angles (Eq. 4, ρ = 1/2).**
  Cos(w_min, w_min′) = (R − 7)/(R − 7 + 2k(2 + √((R+1)/2))). This is
  −1/(k−1) at R = 1, rises with R, and is below 1 for every finite R.
  Minority collapse happens for the UF-SVM only as R → ∞ (Remark 3.2,
  §H).
- **Theorem 2 (from Zhu et al., extended to imbalance and d > k − 1).**
  With ridge λ > 0, every stationary point of the regularized
  cross-entropy UFM is a strict saddle or a global minimizer. The global
  minimizers' Gram matrices come from the SVD of
  Ẑ_λ = argmin_Z L(Z) + λ‖Z‖_*.
- **Proposition 1.** With imbalance and k > 2, *no* finite λ > 0 gives a
  (scaled) SELI solution. The reason is that SELI would force all singular
  values of Ẑ to be equal, which holds only when the data are balanced.
- **Proposition 2.** As λ → 0, ŴλᵀĤλ/(½‖Ŵλ‖²_F + ½‖Ĥλ‖²_F) → Ẑ/‖Ẑ‖_*.
- **Minority collapse (§H, Lemma D.4).** For the regularized UFM, there
  is no minority collapse at finite R when λ < 1/2; the solution
  separates the training data. Collapse requires R > f(λ, ρ), with f
  increasing in ρ and decreasing in λ. That explains Fang et al.'s
  observation that collapse needs R > 1000 at weight decay 5 × 10⁻⁴.
- **§4.4.** A one-layer linear classifier under ridge cross-entropy is
  proportional to Ẑ at every λ. The two-layer factorization is what makes
  the solution λ-dependent under imbalance.
- **UFM, SGD (Figure 5).** k = 4, n ≈ 400, learning rate 0.4, batch 4, no
  weight decay, 10⁵ epochs. Distance to SELI decreases and is below the
  distance to ETF. Convergence is "rather slow", worse with larger R, and
  worse for embeddings than for classifiers.
- **Regularization path (Figure 4).** Solved by CVX. The distance to
  SELI is non-zero at every finite λ and goes to zero as λ → 0, slowly,
  and more slowly at larger R.
- **Deep nets (Figures 2, 6, 7, 13; Tables 2–3).** ResNet-18 and VGG-13 on
  STEP-imbalanced MNIST, Fashion-MNIST and CIFAR10, R ∈ {1, 5, 10, 100},
  n = 25,250. SGD with momentum 0.9, weight decay 5 × 10⁻⁴, 350 epochs, no
  augmentation.
  - NC1, tr(Σ_W Σ_B†)/k, falls at every R (Figure 13).
  - The distance to SELI falls and stays below the distance to ETF, for
    classifiers, centred means and logits.
  - Convergence slows with R, and is worse for embeddings than
    classifiers and for angles than norms.
  - The classifier norm ratio agrees with Lemma 3.1 (Figure 7).
  - Balanced test error on minority classes is high and rises with R.
    For CIFAR10 with ResNet the minority error is 13.76%, 41.08%, 58.78%
    and 98.1% at R = 1, 5, 10 and 100, while majority error falls from
    19.18% to 9.68% (Table 3).
  - Under the experiments' weight decay, a λ-dependent geometry
    ("λ-SELI") is closer still (G.2, F.1).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | UF-SVM solutions have logits equal to the SEL matrix and Gram matrices from its SVD, at any STEP imbalance | strong | Theorem 1, App. C.1 |
| C2 | SELI equals the ETF only for balanced or binary data | strong | Corollary 1.3, Lemma A.3 |
| C3 | Under imbalance no finite ridge gives SELI; the regularized geometry depends on λ | strong | Proposition 1 |
| C4 | The ridge path converges in direction to SELI as λ → 0 | strong | Proposition 2, App. E.3 |
| C5 | GD on the unregularized UFM converges to SELI | weak | conjecture C1; Figure 5 suggests it, slowly |
| C6 | Deep nets trained past zero error approach SELI more closely than ETF under imbalance | moderate | Figures 2, 6, 7; one seed per cell shown, weight decay on |
| C7 | Approach to the preferred geometry slows as imbalance grows | moderate | Figures 4, 5, 2, 6; no rate is derived |
| C8 | Minority collapse needs R above a threshold rising with ρ and 1/λ | strong for the UFM | Lemma D.4, §H |

## Method

Reduce the non-convex UF-SVM to the nuclear-norm program
min ‖Z‖_* s.t. Z[y_i, i] − Z[c, i] ≥ 1. Re-parametrize its dual so that Ẑ
appears in the objective. Prove that B̂ = UVᵀ is its unique, strictly
feasible maximizer, using an explicit construction of Ẑ's singular factors
for STEP imbalance. Complementary slackness then makes every primal
constraint active, so Ẑ is the unique primal solution. Tightness for
d ≥ k − 1 carries this back to (W, H).

## Concepts

- **SEL matrix Ẑ.** The k × n matrix whose column i is e_(y_i) − (1/k)1_k.
  It has rank k − 1, and its k distinct columns with the origin form a
  simplex.
- **SELI geometry.** For some α > 0, [Wᵀ; Hᵀ][W H] = α[VΛVᵀ, Ẑ; Ẑᵀ, UΛUᵀ].
  The model interpolates a scaling of the SEL matrix.
- **UF-SVM.** The min-norm max-margin problem over (W, H). It is the
  direction that unregularized cross-entropy gradient descent would take,
  if it found the global optimum.
- **λ-SELI.** The geometry of the ridge-regularized minimizer, from the
  SVD of Ẑ_λ.
- **Minority collapse (Fang et al.).** Minority classifiers become
  parallel.

## Connections

It extends the balanced-data UFM analyses of Zhu et al. (2021), whose
landscape result it carries over to imbalance (Theorem 2), and of Ji et al.
(2021). It recovers Fang et al.'s minority collapse as a limit. It
generalizes Wang, Muthukumar & Thrampoulidis's simplex-encoding
interpolation from a convex SVM to the non-convex UFM (I.5). The phenomenon
it revises is [LIT-618](../literature.d/LIT-618.md)'s. Kothapalli & Tirer ([LIT-985](../literature.d/LIT-985.md)) cite it among the
UFM analyses that see the data only through labels.

## Bearing on the record

- **[QUESTION-051](../questions.d/QUESTION-051.md).** It answers a piece of the question's first half that
  the record lacked. Under cross-entropy the preferred last-layer geometry
  is set by the labels' simplex encoding. So the simplex ETF is a special
  case of balance, not the general answer. On the second half it bears
  indirectly: the geometry it predicts gives minorities shorter
  classifiers that sit closer together, and the measured minority test
  error is high (Table 3). The paper does not connect the two.
- **[THEORY-083](../theory.d/THEORY-083.md) (a mismatch).** Its promote_when lists "class imbalance"
  among the conditions under which measurements of NC1 *and NC2* would
  promote it. It says the claim is refuted if training "leaves the centred
  class means far from equiangular". Under imbalance this paper proves
  that the preferred geometry is not equiangular, unless k = 2. It measures
  deep nets staying further from the ETF than from SELI. NC1 does hold
  under imbalance (Corollary 1.1, Figure 13). So [THEORY-083](../theory.d/THEORY-083.md)'s title and
  promote_when should restrict the ETF part to balanced classes. Under
  imbalance the prediction to test is SELI, not equiangularity. As it
  stands, an imbalanced replication would count as refuting [THEORY-083](../theory.d/THEORY-083.md) for
  the wrong reason. [THEORY-083](../theory.d/THEORY-083.md) already says "it covers balanced classes" in
  "What this does not say". The fix is to its promote_when.
- **[THEORY-083](../theory.d/THEORY-083.md)'s "the dynamics are unexplained".** The paper gives no
  dynamics either. Its theorem is about the endpoint gradient descent
  would reach if it reached a global optimum.
- **[QUESTION-080](../questions.d/QUESTION-080.md).** Two findings bear on it. First, with weight decay and
  imbalance the last-layer geometry at the regularized minimum depends on
  λ (Proposition 1). So the "fixed geometry" the question asks about is a
  function of the regularizer, not a property of the task alone. Second,
  convergence toward it is slow and slows with imbalance (Figures 4, 5).
  Measured geometry then depends on when training stops, which is the
  question's second branch.
- **Filed.** [THEORY-286](../theory.d/THEORY-286.md) states the result at the strength shown.
- No instruction for machine-learning practice is relied on. The paper's
  outlook on loss adjustments for imbalanced training is practice.

## Limitations

- STEP imbalance only; general class-size profiles are not treated.
- The UFM: features are free, so the data enter only through class sizes.
- The link from gradient descent to the UF-SVM's *global* minimizer is
  conjectured (C1), not shown. KKT points of the non-convex problem need
  not be global.
- The deep-net runs use weight decay 5 × 10⁻⁴, under which Proposition 1
  says the target is λ-SELI, not SELI. The authors show SELI is
  nevertheless closer than ETF.
- One run per cell, so no seeds or intervals. Biases are disabled, and
  there is no augmentation.

## Open questions

- Does gradient descent on the unregularized UFM reach SELI (conjecture
  C1)? At what rate, as a function of R?
- Why does the approach slow with imbalance, and why more for embeddings
  than for classifiers? The authors point to the regularization path as a
  possible link.
- Do the SELI norms and angles predict the minority classes' test error?
