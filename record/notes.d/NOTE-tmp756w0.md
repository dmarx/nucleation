---
status: Read
paper: LIT-987
title: 'Huang et al. — internal causal mechanisms predict out-of-distribution behaviour'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (v2 of 10 November 2025, the ICML 2025
    paper, PMLR 267, 22 pages), fetched from arxiv.org/pdf/2505.11770 and
    extracted with pdftotext -layout: §§1–7 and appendices A–D. Tables 2,
    3, 6 and 7 were read value by value; Figures 3–6 from captions and
    surrounding text, since their content does not survive extraction. The
    reference list was scanned. Read after Makelov et al. (LIT-968) and
    the reply (LIT-961); this paper cites neither.
date: '2026-10-14'
summary: >-
  In Llama-3-8B-Instruct, on five tasks and ten task-preserving shifts,
  checking by interchange intervention whether a test input still realizes
  the causal variable located on in-distribution data predicts whether the
  output is correct better than output confidence or probes of other
  internal features, best on 8 of 10 shifts. A probe on the located variable
  beats a probe on its orthogonal complement on 7 of 10. Interchange
  accuracy and predictive power rise together only up to a point.
---
<!-- inactive-ok-file: CLAIM-078 — Proposed; the success criterion this reading is set beside, open -->
<!-- inactive-ok-file: THEORY-tmpuieof THEORY-tmps4hmc — Proposed; the account filed from this reading, and the one it is read against -->

# NOTE-tmp756w0: Huang et al. — internal causal mechanisms predict out-of-distribution behaviour

## Contribution

Interpretability had used internal causal mechanisms to explain success.
This paper uses them to predict it. Given a high-level causal model of a
task and the subspace where DAS localizes its key variable on correct
in-distribution examples, it predicts whether the model will be right on a
new input by checking whether that input still produces a value of the
variable that behaves as the high-level model says. Under shifts that
keep the task but change its surface, this beats output confidence and
probes of features chosen without a causal analysis.

## Key insight

If a model solves a task by a mechanism, then on an input where the
mechanism's key variable is not computed properly, the output is unlikely
to be right. One can test whether the variable is computed properly by
transplanting its value into a verified example and seeing whether the
output follows the high-level model. Because that test reads only the
variable the output depends on, and averages over everything else, it
should survive shifts in what the model was not using.

## Assumptions

- **A known high-level model.** Taken from prior work for each task
  (Figure 5). For MMLU and UnlearnHP only part of the mechanism is known.
- **Linear localization.** DAS finds an orthonormal Q, and the
  intervention is r_inv = (I − QᵀQ)r_base + QᵀQ r_src (Eq. II). The
  authors grant that representations "are neither fully linear nor fully
  non-linear" (App. D).
- **Output depends on its parent.** P(Y | X = x) = P(Y | V =
  GetVal(M(x), V)) when the model implements the high-level model. The
  complement B = V⊥ is treated as background, and P(Y | V) =
  E_B P(Y | V, B), estimated by sampling B from verified examples (Eq. 4).
- **Shift defined by the task.** OOD means a perturbation that leaves the
  task function unchanged and lowers accuracy, not a shift from the
  training distribution (A.1). Perturbations were selected because they
  lower accuracy.
- **Setting.** Llama-3-8B-Instruct for the main results; balanced test
  sets of correct and wrong outputs; AUC-ROC; three folds of
  2048/1024/1024 examples (1024/512/512 for UnlearnHP); invalid outputs
  (under 10%) excluded.

## Key results

- **Counterfactual simulation (Eq. 5, 6).** f(M, x_test) = (1/kn)
  Σᵢ Σₜ −y_cf,t log y_inv,t over k verified bases and the first n tokens,
  or (1/k) Σᵢ 1[τ_out(y_cf) = τ_out(y_inv)] when outputs can be parsed.
  No training beyond localization.
- **Value probing (Eq. 7, 8).** A linear classifier τ over the values of V
  on the verified set; f = maxᵢ τ(x)ᵢ. Low confidence marks inputs near a
  boundary between values or outside all of them.
- **In distribution (Table 2).** Counterfactual simulation with output
  mapping: PriceTag 0.907, IOI 0.999, RAVEL 0.908, MMLU 0.785, UnlearnHP
  0.919. Probing the prompt's last token does as well or better on three
  tasks (PriceTag 0.955, MMLU 0.804, UnlearnHP 0.940). On those three and
  RAVEL the causal-variable probe gives identical numbers, so in
  distribution the two features apparently coincide; under shift they
  differ. Confidence is strong where outputs are constrained (IOI
  0.935, MMLU 0.810).
- **Out of distribution (Table 3).** Task accuracy falls, e.g. IOI 98 →
  83 with Chinese names and 98 → 71 with a rephrased template.
  - Counterfactual simulation (output mapping) is best on 8 of 10 shifts:
    PriceTag 0.856 and 0.875; IOI 0.997 and 0.815; RAVEL 0.939 and 0.931;
    MMLU 0.765 and 0.810; UnlearnHP 0.860 and 0.772. The exceptions are
    MMLU with changed option symbols (value probing 0.777) and UnlearnHP
    with a longer passage (answer-token confidence 0.931).
  - Probing the causal variable against probing its complement B: better
    on 7 of 10 shifts; worse on IOI rephrased (0.665 against 0.749),
    MMLU with a distractor (0.694 against 0.698) and UnlearnHP rephrased
    (0.650 against 0.660).
  - Value probing is uneven: 0.611 on IOI with Chinese names, 0.691 on
    RAVEL with a changed language.
  - Confidence loses most under shift and its best temperature does not
    transfer.
- **IIA and prediction (§6.3, Figure 4).** On RAVEL and IOI, AUC-ROC rises
  with IIA until IIA nears 1, and then stops. Some early-layer
  representations have high IIA and predict correctness weakly, "likely
  because these representations are easily computed by the model
  regardless of whether the final prediction is correct".
- **Scale (Table 6).** On RAVEL in distribution, confidence does not
  improve with model size. Counterfactual simulation was not run on the
  70B model.
- **Size of shift (Table 7).** On RAVEL with two-shot demonstrations from
  one country, as accuracy falls from 89% to 72%, first-token confidence
  falls from 0.903 to 0.693 while counterfactual simulation stays between
  0.89 and 0.94.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Whether a test input realizes the located causal variable predicts output correctness under task-preserving shifts better than confidence or causal-agnostic probes | moderate | Table 3: best on 8 of 10 shifts, one model, three folds, no significance tests |
| C2 | Features of the located variable are more robust than features of its orthogonal complement | weak | Table 3: 7 of 10, with three reversals |
| C3 | Confidence scores degrade under shift while counterfactual simulation does not | moderate | Table 3, Table 7 |
| C4 | Interchange accuracy and predictive power are correlated but not the same | moderate | Figure 4, two tasks |

## Method

1. Take a high-level causal model of the task from prior work.
2. Localize its key variable with DAS on correct in-distribution examples
   (Table 5: e.g. IOI, a 256-dimensional subspace at layers 9–12 on the
   last token of the repeated name; RAVEL, 1024 dimensions at layers
   13–14).
3. For each test input, transplant the variable's value into k verified
   bases and score how well the output matches the high-level model's
   counterfactual (counterfactual simulation), or classify the value
   directly (value probing).
4. Compare with confidence scores and with probes trained on correctness
   labels at heuristic locations or on the background subspace.

## Concepts

- **Causal feature.** A representation that DAS aligns with a variable of
  the high-level model, with high IIA on in-distribution data.
- **Causal-agnostic feature.** One chosen without such an analysis, e.g.
  the last prompt token. It may coincide with a causal feature.
- **Background variable.** B = V⊥, the rest of the representation at the
  same location.
- **OOD (here).** A perturbation of task-irrelevant conditions that keeps
  the task function and lowers accuracy.

## Connections

It applies the causal-abstraction programme (Geiger et al.) and DAS to a
predictive use. Its high-level models come from Wang et al. (IOI), Wu et
al. 2023 (PriceTag), Huang et al. 2024 (RAVEL), Wiegreffe et al. 2025
(MMLU) and Arditi et al. and Thaker et al. (UnlearnHP). It sits in the
literature on predicting correctness from internals (Azaria and Mitchell;
Orgad et al.; Gottesman and Geva). It does not cite Makelov et al. or the
reply, but it localizes in residual streams, the placement both papers
treat as safest, and it validates by IIA, the reply's measure. It does not
check its located subspaces for the disconnected-plus-dormant structure
[LIT-968](../literature.d/LIT-968.md) describes.

## Bearing on the record

- **[QUESTION-030](../questions.d/QUESTION-030.md).** The LIT says "Intervention here separates
  constitutive structure from diagnostic structure". The paper does not
  say that. It separates features located by interchange intervention as
  mediating from features chosen without such an analysis, and from the
  rest of the same representation. It makes no claim about constitution.
  Its comparison features are not all "merely correlated": in
  distribution, on four of five tasks the last-token probe scores exactly
  as the causal-variable probe does (Table 2), and §6.1 grants that the
  last token can lie on the causal path. What the paper shows bears on the empirical half
  of the question in a weaker form. A variable that an intervention
  identifies as mediating keeps predicting behaviour across changes the
  mechanism ignores, better than features identified otherwise. Filed as
  [THEORY-tmpuieof](../theory.d/THEORY-tmpuieof.md).
- **[QUESTION-028](../questions.d/QUESTION-028.md)**, also named in the LIT. A measured case of
  intervention-relevant structure that generalizes independently across
  surface changes. It supports the generalization clause of that
  question's qualifiers, in a model, and says nothing on whether that
  makes a kind real. Figure 4 adds that high interventional fit alone did
  not make a feature predictive.
- **[CLAIM-078](../claims.d/CLAIM-078.md)** takes the theory to succeed if its measures predict
  changes that text similarity misses. This paper is an instance of the
  pattern in another domain: internal causal features predicted
  correctness where output confidence did not. It is not evidence for the
  manuscript's measures.
- **[CLAIM-150](../claims.d/CLAIM-150.md).** Consistent: predictive success under intervention is
  reported, and nothing about constitution is inferred.
- **For the anthology.** The paper's purpose, and §6.2's guidance on which
  method to use when, are practice: correctness estimation for deployed
  models. That belongs to the anthology and is not filed here.

## Limitations

- One model for the main tables; three folds; no significance tests.
- Shifts were selected for lowering accuracy, and each task has two.
- The high-level models are given, and partial for MMLU and UnlearnHP.
- Linear localization only.
- The background comparison is one probe; the reversals on three shifts
  are not discussed.
- Counterfactual simulation needs a verified set and k forward passes per
  input, and its labels for PriceTag rest on a shortcut the authors
  observed in the model (Figure 6).

## Open questions

- Whether the advantage survives shifts that change the task's mechanism
  in part, which the design excludes by construction.
- Whether a located subspace that fails Makelov et al.'s decomposition
  test predicts worse out of distribution. That would join the two
  papers' criteria.
