---
status: Read
paper: LIT-tmpuv16r
title: 'Uncovering mesa-optimization algorithms in Transformers'
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Read from the arXiv v2 PDF (15 Oct 2024, 44 pp.). The main text, the
    Methods with the proofs of Propositions 1 and 2, and Appendices B to H
    were read in full. Appendix A, the weight figures, was read from its
    captions. The Proposition 1 algebra was checked by hand. Proposition
    2's Neumann and Chebyshev construction, Appendix C's backward pass
    and Appendix D's maximum-likelihood derivation were followed but not
    checked line by line. The references and v1 were not read. The
    reading was delegated, and the filer rechecked every quote below
    against a fresh extraction of the same PDF. The filer also checked the
    mesa-layer's small-λ limit numerically with `python3 -I`.
date: '2026-11-26'
summary: >-
  Transformers trained only by next-token squared error on synthetic
  dynamical sequences, with fresh parameters for each sequence, learn in
  context. Their first layer binds consecutive tokens into an in-context
  training set, and their later layers behave as an optimizer of a
  least-squares mesa-objective. That is exactly one gradient step for one
  linear self-attention layer on constructed tokens (Proposition 1). For
  deeper linear and softmax models it is approximately preconditioned
  descent toward ridge regression, judged by matched loss curves, weight
  structure, linear probes and distillation. The paper derives a
  mesa-layer whose output is, by definition, the ridge solution on the
  context, computed by recursive least squares.
---
<!-- inactive-ok-file: THEORY-1871 THEORY-2050 THEORY-990 — Proposed; readings this note bears on, and the one it yields -->

# NOTE-tmpcktnn: Uncovering mesa-optimization algorithms in Transformers

von Oswald et al. (2023), arXiv 2309.05858, v2.

## Contribution

It moves the authors' 2022 result ([LIT-792](../literature.d/LIT-792.md), [NOTE-621](NOTE-621.md)) from meta-trained
in-context regression to plain autoregressive training. It adds a
multi-layer construction, Proposition 2, that preconditions and then takes
one gradient step. And it introduces the mesa-layer, a causal attention
layer that solves regularized least squares on its context at every step.

## Key results

- **Definition (p. 2).** "we refer to this hypothetical acquired process as
  mesa-optimization, to distinguish it from the base-optimization of Eq. 1",
  following Hubinger et al.
- **Proposition 1 (p. 3; proof p. 12).** With tokens [Φ0 s_t, s_t, s_{t−1}]
  and constructed projections, "the transformation of every token e_t by
  one causally-masked linear self-attention head is identical to the
  gradient-induced update". It "is an immediate extension of the main
  result of von Oswald et al. [17]", and it "implements a ‘full-batch’
  gradient step".
- **Proposition 2 (p. 3).** Stacked linear self-attention layers approximate
  the preconditioned inputs "with approximation error decreasing with the
  number of linear self-attention layers k". No rate is given.
- **The mesa-layer (p. 4, Eqs. 4–8).** Each head outputs the regularized
  least-squares solution on its keys and values, read at the query,
  computed by Sherman–Morrison. "As λ_h → 0, we recover a standard linear
  self-attention layer. Thus, the mesa-layer strictly generalizes the
  latter." It "is not parallelizable across time".
- **The delta rule (pp. 4, 11).** Delta-Net is "hardwired to do one gradient
  descent step per time point". "Unlike the mesa-layer, which is optimal at
  every step, the delta rule requires multiple steps to converge".
- **Token binding (p. 6).** The first-layer mechanism "exactly coincides
  with the first layer of the induction head circuit".
- **Trained one-layer models (p. 6).** These match Proposition 1 "in a
  near-exact fashion".
- **Deep linear models (p. 7).** The compressed fit "is difficult to
  interpret it from the lens of mesa-optimization and connect it exactly to
  the theoretical construction of Proposition 2", yet "Base-optimization
  has therefore discovered a hybrid algorithm that descends over layers the
  mesa-objective".
- **Induction heads (p. 8).** "an induction head and the mesa-optimizers
  studied here sit on two opposite extremes".
- **Full Transformers (Fig. 7).** "These two control models accurately
  describe the behavior of actual trained standard Transformers."
- **Few-shot regression (p. 9).** The learned algorithm "is sub-optimal with
  respect to linear regression". The early-ascent phenomenon is traced to
  spurious pairs of a target with the next input.
- **Discussion (pp. 10–11).** The algorithm "can be precisely cast as maximum
  a posteriori inference under the correct Bayesian prior and likelihood
  function", and the mesa-layer is "a locally optimal fast weight
  programmer". The results explain in-context learning "at least in the
  settings we have considered".
- **Controls and scope.**
  - Fixed-teacher training: "we find no evidence for the mesa-optimizers"
    (Appendix E.2).
  - Language models: "Strictly speaking, these results are not sufficient to
    make claims on whether mesa-optimization is occurring within standard
    Transformers" (Appendix G).

## Assumptions

- **Data.** Squared-error next-token prediction on h_{t+1} = W* f*(h_t) + ε
  and s_t = C* h_t + ε. W* is drawn afresh for each sequence, which rules
  out memorization. Systems are fully or partially observed and linear, or
  have an MLP nonlinearity. Context length is 50, or 224 for the
  in-context-learning runs.
- **Theory.** It covers linear self-attention on constructed tokens only.
  Softmax enters empirically.
- **Operationalization.** "Mesa-optimization" is shown by five kinds of
  evidence:
  - agreement of losses or outputs with Proposition 1, or with k tuned
    steps of Proposition 2;
  - weight structure;
  - linear probes for targets and preconditioned inputs;
  - distillation of softmax layers into linear ones;
  - the mesa-layer's own performance.

## Concepts

- **Mesa-optimization and base-optimization**, defined as above.
- **Mesa-objective:** L_t(Φ) = Σ ½‖s_{t′+1} − Φ s_{t′}‖², with a ridge form.
- **Fast weights Φ:** they "live in the short-term memory of a Transformer
  model, not in its learned parameters".
- **Mesa-layer:** an attention layer whose output is defined as an
  optimization's solution, a "declarative node".
- **Token binding:** building "an in-context training set".

## Bearing on the record

- **[LIT-792](../literature.d/LIT-792.md) and [NOTE-621](NOTE-621.md) (extends).** Proposition 1 is the 2022 identity,
  moved to autoregressive training with a nonzero Φ0.
- **[THEORY-169](../theory.d/THEORY-169.md) (supports and extends).** Proposition 1 is a further exact
  conditioning-is-training identity, for causal linear self-attention on
  constructed tokens. The mesa-layer adds a third exact learner layer
  beside batch gradient and kernel regression. The evidence on trained deep
  and softmax models is not exact, which respects [THEORY-169](../theory.d/THEORY-169.md)'s caveat.
- **[QUESTION-159](../questions.d/QUESTION-159.md) (bears on and narrows; does not answer).** The mesa-layer
  is exactly a ridge or recursive-least-squares learner's train-then-predict
  step, but by definition (Eq. 5). That is the same "too immediate"
  question the note of 2026-11-15 raised for the delta rule. The paper's
  statement that Delta-Net does "one gradient descent step per time point"
  matches that note's own arithmetic. Nothing here covers mini-batch inner
  updates, normalized linear attention, or the question's second half.
- **[THEORY-1871](../theory.d/THEORY-1871.md) (extends; a parallel).** Fast-weight learning recast as
  exact optimization at every step, with the delta rule between Hebb and
  the mesa-layer. No new test of [THEORY-1871](../theory.d/THEORY-1871.md)'s capacity clause.
- **[THEORY-2050](../theory.d/THEORY-2050.md) (parallel, consistent).** Both find deeper models behaving
  like ridge or least squares rather than one gradient step. Akyürek's
  Sherman–Morrison construction is realized here as an actual layer.
- **[THEORY-973](../theory.d/THEORY-973.md) and [THEORY-990](../theory.d/THEORY-990.md), from [NOTE-1173](NOTE-1173.md) (qualifies).** The first-layer
  copying mechanism is agreed. The second stage is reinterpreted as a
  least-squares optimizer, not softmax retrieval, but only on synthetic
  continuous data.
- **[LEAD-043](../leads.d/LEAD-043.md) (bears on it).** The paper gives a mechanism for "early
  ascent", spurious target–input pairs, which is the only phenomenon of
  that name the record holds.

- **[CLAIM-118](../claims.d/CLAIM-118.md) (corroborates).** Fast weights are kept in the context ("live
  in the short-term memory ..., not in its learned parameters"). The
  interpreter supplies binding, the optimizer and Φ0. The fixed-teacher
  control moves what is constant into the weights. That is the claim's
  separation by what each carries.
- **[CLAIM-074](../claims.d/CLAIM-074.md), [LEAD-165](../leads.d/LEAD-165.md) and [CASE-005](../cases.d/CASE-005.md) (bear on).** ICL and TTT can share a
  mechanism here, so experiment 3's contrast should be drawn by what is
  retained.
- **[QUESTION-020](../questions.d/QUESTION-020.md) (bears on).** The fixed-teacher control is the limit where
  the interpreter substitutes for the context completely.
- **[QUESTION-161](../questions.d/QUESTION-161.md) (bears on).** MAP under the correct prior, in
  linear-Gaussian tasks: Bayesian, but a point estimate, not a latent-concept
  posterior.
- **[TERM-131](../terms.d/TERM-131.md) (consistent).** Learning on two horizons.
- **[QUESTION-024](../questions.d/QUESTION-024.md) (analogy).** Inducing a map from examples.

These were added on the owner's prompting. The first filing searched the
readings and missed the record's own claims and questions.

## Limitations

- **"Strictly generalizes" holds only up to scale.** The regularizer is
  (1/λ)‖Φ‖², so as λ → 0 the solution tends to zero. It is Φ̂/λ that tends
  to the linear-attention map VKᵀ. The output projection would have to
  absorb a vanishing scale, which the paper does not say. The filer checked
  this with `python3 -I` on random K, V and q: at λ = 1e−6, ‖Φ̂q‖ ≈ 1.4e−5,
  and the relative error of Φ̂q/λ against VKᵀq is 1.5e−5.
- **"Corresponds to gradient-based optimization"** is exact only for one
  linear self-attention layer on constructed tokens, and for the mesa-layer,
  which is built to optimize. For deeper and softmax models the evidence is
  agreement with optimizers whose hyperparameters "are tuned for maximal
  k-step performance and not to reproduce Transformer behavior", together
  with probes and distillation.
- **Probes show decodability, not use.** No intervention on the decoded
  training set or preconditioned inputs is reported.
- **Proposition 2 gives no error bound.** Its norm condition appears only in
  Appendix C.3.
- **The fixed-teacher control.** Its result is called "as predicted by our
  theory", but no prediction is stated before the experiment.
- **"Correct Bayesian prior"** holds only for the linear-Gaussian tasks.
- **Scope.** Small models and synthetic continuous data; the language-model
  results are self-described as insufficient.
- **A misreference.** Appendix G points to "Appendix C.1" for forgetting
  factors, which are in Appendix B.
