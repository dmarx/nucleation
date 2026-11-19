---
status: Read
paper: LIT-tmpd6tw2
title: 'Akyürek and others 2023 — What learning algorithm is in-context learning? Investigations with linear models'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2211.15661 (HTTP 200, 1.3 MB PDF, arXiv
    v3 of 17 May 2023; header "Published as a conference paper at ICLR
    2023"). Kind of copy: arXiv preprint of the published paper (step 5,
    first place to look). Date: 2026-11-19. Nothing stopped the fetch. Text
    extracted with pdftotext -layout to dl/text.txt. Read: the whole main
    text (abstract, §§1-6), Theorems 1-2 statements, Figures 1-4 captions.
    Skipped: references and the appendices (proofs of Lemma 1 and Theorems
    1-2, hyperparameters, probe details, extra probing plots).
date: '2026-11-19'
---

# NOTE-tmppc03e: Akyürek and others 2023 — What learning algorithm is in-context learning? Investigations with linear models

## Contribution

On linear regression, the paper asks how a trained transformer learns in context, not what it can learn. The hypothesis is that "in-context learners encode an implicit, context-" dependent model in their activations and train it on the examples as they are processed. Three lines of evidence follow: constructions showing a transformer can implement one step of gradient descent or of closed-form ridge regression; behavioural matching of trained models against standard estimators as depth, width, noise and prior vary; and probes for the intermediate quantities those estimators compute. Published at ICLR 2023.

## Key results

- §3, Theorem 1. "A transformer can compute Eq. (11)", the prediction after one gradient-descent step on an in-context example, with constant depth and O(d) hidden size.
- §3, Theorem 2. One Sherman–Morrison rank-one update of the ridge solution takes constant depth and O(d²) hidden size; n steps take about n times the layers.
- §4.3, Figure 1. A 16-layer, 512-wide trained learner matches ordinary least squares on noiseless data: "SPD and ILWD are small between the transformer and OLS predictor", while one-step GD, one-pass SGD and nearest neighbours fit worse. Below d examples it follows the minimum-norm solution.
- §4.3, Figure 2. With label noise σ² and prior variance τ², the best-fitting ridge parameter tracks σ²/τ², "the one that minimizes Bayes risk": the learner behaves as the Bayes-optimal predictor.
- §4.3, Figure 3. Capacity changes the algorithm. As depth grows, "shallow models (1L) are best approximated by a single step of gradient descent" (though not well), "Slightly deeper models (2L-4L) are best approximated by ridge", and 8+ layers match OLS. So ICL does "not necessarily involve minimum-risk prediction". Ridge-like behaviour needs less width than the O(d²) construction.
- §5, Figure 4. The moment vector XᵀY (around layer 7) and the least-squares weights (around layer 12) can be decoded from hidden states, but an MLP probe beats a linear one, so "these targets are encoded nonlinearly", unlike the constructions.

## Assumptions

- Models are trained from scratch on the ICL objective for linear regression (40 examples, Gaussian inputs and weights), following Garg et al.
- Agreement is measured behaviourally (squared prediction difference, implied linear weights). Matching algorithm A means matching A's outputs, Marr's computational level.
- Probing success is read as encoding; the probes are trained per prefix length.

## Concepts

- **Implicit model in activations**: a context-dependent predictor whose parameters are held in hidden states and updated as examples arrive.
- **Squared prediction difference (SPD)** and **implicit linear weight difference (ILWD)**: output-level and parameter-level agreement between two learners.
- **Algorithmic phase transition**: the best-fitting classical algorithm changes with depth or width.

## Bearing on the record

- **THEORY-169** (qualifies). Theorem 1 is a softmax-transformer counterpart of von Oswald et al.'s one-step construction held there. Trained models are matched by one GD step only at one layer, and then poorly; deeper ones match ridge, then OLS. This measures the record's caution that trained transformers are not shown to do gradient descent.
- **CLAIM-118** (supports). The learned algorithm is in the weights (the interpreter); the implicit model it trains is per-sequence and discarded (the signal). Which algorithm the interpreter runs depends on its capacity (§4.3), so improving the interpreter can change how the same signal is used. It fits the distinction and does not test its defeat condition.
- **THEORY-481** (consistent). THEORY-481 has a linear-attention layer converge to the estimator preconditioned by the inverse input covariance. Here trained softmax transformers converge to OLS or Bayes ridge at enough capacity. Both are learned estimators, not hand-set ones.
- **QUESTION-159** (leaves open). The constructions are existence results for chosen weights, not identities of a layer class, so they do not answer the question.
- **THEORY-614** (bears on). In this setting ICL behaves as the Bayes predictor for the training prior, a measured case of the Bayesian reading, where the prior is the meta-training distribution and not a latent concept in text.

## Limitations

- Linear regression only, trained from scratch: the authors propose but do not run the method on language models.
- The probing evidence is "preliminary" in the authors' word, and the probes find nonlinear encodings that the constructions do not predict.
- Behavioural fits measure output agreement, not mechanism.
- The phase picture rests on a hyperparameter grid for one noise-free setting at d = 8 and d = 16.
