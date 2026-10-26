---
status: Read
paper: LIT-tmpe7b5o
title: 'Olsson et al. — In-context learning and induction heads'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF of 2209.11895 (v1, the
    only version), text extracted with pdftotext. The PDF is a 61-page
    browser print of the Transformer Circuits article, which is headed
    "PUBLISHED Mar 8, 2022" and carries a change log entry of 2022-09-20.
    Read: the abstract and introduction, Key Concepts (in-context
    learning, the in-context learning score, the definition of induction
    heads, per-token loss analysis), all six Arguments with their
    strength tables, the Model Analysis Table's prose, Model Details,
    Unexplained Curiosities, Discussion, Related Work, the two external
    Comments & Replications (Scherlis; Lieberum), the change log, all 31
    footnotes, the references, and the appendix sections on where
    induction heads form, score distributions, validation of the
    evaluators, data collection (the ablation methods and the four head
    measurements) and the analyses. The paper's figures and the Model
    Analysis Table are interactive in the HTML; in the PDF they are
    static images. The strength tables, the phase-change and ablation
    figures of Arguments 1–3, the smeared-key figure, the Argument 4 head
    table and the small attention-only rows of the Model Analysis Table
    were read from page renderings (pp. 8–10, 16–20, 25, 30–33). The
    interactive token visualizations of Argument 4 were not available
    and are taken from the text. Not compared with the current HTML.
date: '2026-10-26'
summary: >-
  In 34 transformer language models, in-context learning (loss at token
  500 minus loss at token 50) appears abruptly in one early window of
  training, together with induction heads, the only non-convex bump in the
  loss curve and a turn in the models' per-token-loss trajectory; one-layer
  models show none of it. Letting one layer express induction (smeared
  keys) moves the jump, and ablating induction heads removes nearly all
  in-context learning in small attention-only models. The case is causal
  for small attention-only models and correlational or by analogy for large
  models with MLPs, as the authors grade it themselves.
---
<!-- inactive-ok-file: THEORY-tmpkd3fq THEORY-783 THEORY-481 THEORY-039 THEORY-279 — Proposed; accounts this reading files or bears on, cited as open -->
<!-- inactive-ok-file: CLAIM-329 CLAIM-427 CLAIM-286 CLAIM-287 CASE-tmplcm41 — Proposed; the record's own claims and the construction this reading bears on, cited as open -->
# NOTE-tmpabelf: Olsson et al. — In-context learning and induction heads

## Contribution

It ties a macroscopic event in training, an abrupt rise in in-context
learning visible as a bump in the loss, to a circuit that can be read off
the weights: the induction head, which completes [A][B] … [A] → [B]. It
grades its own evidence by model class, and the grading is the main thing
to keep. For small attention-only models the link is causal (ablation,
co-perturbation, reverse engineering). For large models with MLPs it is
co-occurrence, a few examples, and extrapolation. The authors call the
first case for any phase change of training that has a mechanistic
account: "As far as we know, induction heads are the first case where a
mechanistic account has been provided for a phase change in machine
learning."

## Key insight

Measure in-context learning as a property of the loss, not of chosen
tasks: how much better the 500th token is predicted than the 50th. Then
what changes all at once can be seen. In every model with more than one
layer the score jumps once, early, and then stays put, and the heads that
do prefix-matching and copying appear in the same window. A circuit that
needs two layers to compose explains why one-layer models never make the
jump. An architectural change that lets one layer compose makes them make
it.

## Assumptions

- **In-context learning** is "decreasing loss at increasing token
  indices", operationalized as the in-context learning score: "the loss
  of the 500th token in the context minus the average loss of the 50th
  token in the context, averaged over dataset examples". The score is
  negative, and the authors speak of its size ("roughly 0.4 nats").
  Few-shot learning is treated only through examples (Argument 4).
- **Induction head** is defined behaviourally, on repeated random token
  sequences: prefix matching (the head attends to tokens that followed
  earlier copies of the current token) and copying (its direct effect
  raises the logit of the attended token). The scores are continuous, and
  "there is a clear subset of heads which exhibit these properties with
  much greater than random chance". The definition was corrected after
  publication (change log, 2022-09-20).
- **Models.** 34 decoder-only transformers, one training run each, in four
  series: small attention-only (1–6 layers), small with MLPs (1–6
  layers), both with d_model = 768, 12 heads per layer, 10,000 steps (about
  10¹⁰ tokens) and 200 snapshots; full-scale models with MLPs from 4
  layers and 13M to 40 layers and 13B non-embedding parameters, with 14
  or 15 snapshots at steps 2⁵…2¹⁷; and one- and two-layer smeared-key
  models. The context window is 8192 tokens, but every measurement uses
  10,000 examples of 512 tokens. Positional information is not added to
  the residual stream (a Shortformer-like variant).
- **Data.** Filtered Common Crawl and internet books with about 10% Python
  code, plus a books-only set for some small models. "All models trained
  on a given dataset saw the same examples in the same order."
- **Ablation.** Head ablations were run on the small models only, "pattern
  preserving": attention patterns are frozen at their unablated values and
  the head's result vector is zeroed. In an attention-only model the logits
  are then, up to LayerNorm rescaling, a sum of per-head terms and a
  direct path that depends only on the present token (footnotes 19 and 30).
- No optimizer is named. The only scheduled changes are a learning-rate
  warm-up over the first 1.5 × 10⁹ tokens, which overlaps the small
  models' phase change, and a weight-decay reduction at about 5 × 10⁹
  tokens, which comes after it.

## Key results

- **Argument 1, co-occurrence (all model classes; "Medium,
  Correlational").** In-context learning "develops abruptly in a narrow
  window early in training (roughly 2.5 to 5 billion tokens) and then is
  constant for the rest of training". "Before this window there is less
  than 0.15 nats of in-context learning, after it there is roughly 0.4
  nats", and the after value is about the same at every size from two
  layers to 13B. In the same window induction heads form (prefix-matching
  scores jump), the loss shows a bump, "the only place in training where
  the loss is not convex (monotonically decreasing in slope)", and the
  models' trajectories in a PCA of per-token losses turn. The one-layer
  models show none of the four. Over the window, tokens in repeated
  sequences get easier and tokens that break an earlier pattern get harder
  (the "Mrs Potter" example). The authors list the confounds themselves:
  15 snapshots for the large models, a shared latent cause such as
  learning to compose layers, and a constant score that may hide changing
  mechanisms.
- **Argument 2, co-perturbation ("Medium, Interventional" for small
  models, "Weak" for large).** Smeared keys,
  k_j = σ(α)k_j + (1 − σ(α))k_{j−1} with a trainable α per head, let a
  single layer attend by the previous token. One-layer smeared-key models
  then show the jump, and two-layer ones show it earlier. The authors
  read this as showing "that induction heads are the minimal mechanism for
  greatly increased in-context learning", and not that it is the whole
  story in larger models. (In the rendered figure, the one-layer smeared
  model's score overshoots to about −0.38 and settles near −0.32, short of
  the two-layer models' −0.4.)
- **Argument 3, ablation (small models only; "Strong, Causal").** "In
  fact, almost all the in-context learning in small attention-only models
  appears to come from these induction heads! This begins at the start of
  the phase change, and remains true through the end of training."
  Ablating most other heads increases the score (footnote 17). With MLPs
  the inference weakens, because head ablations interact with MLP
  computation and redundant heads can mask each other. The authors'
  conclusion: induction heads are "the primary mechanism for in-context
  learning in small attention-only models", and the evidence is "only
  suggestive for the MLP case".
- **Argument 4, generality (large models; "Plausibility").** Three heads
  of the 40-layer, 13B model score as induction heads and also copy
  literally, translate between English, French and German, and match an
  abstract four-template pattern ("about 65% of its attention from the
  colons to the correct positions"). Anecdotal by design.
- **Argument 5, mechanism (small models; "Strong, Mechanistic" for some
  in-context learning, "Weak" for most).** Copying is an OV circuit with
  positive eigenvalues. Prefix matching is K-composition with an earlier
  previous-token head, a QK term Id ⊗ h_prev ⊗ W with W positive. In GPT-2
  a second, "pointer-arithmetic" mechanism through positional embeddings
  and Q-composition was seen. An induction head works as an "in-context
  nearest neighbor" over the context, so it lowers later-token loss
  whenever it fires. No such reverse engineering exists for models with
  MLPs.
- **Argument 6, continuity ("Analogy").** Every measurement looks alike
  from small to large models. The strongest alternative the authors see:
  "If all 'composition heads' form simultaneously during the phase change,
  then it's possible that above some size, non-induction composition heads
  could together account for more of the phase change and in-context
  learning improvement than induction heads do."
- **Curiosities.** The in-context learning score after the change is the
  same at every size, because large models gain their advantage in the
  first ten tokens. Larger models' loss falls more slowly than smaller
  ones' before the change and faster after it. A non-induction head in the
  six-layer attention-only model develops late, and ablating it looks
  like reversing the phase change. Some heads in full-scale models above 16
  layers prefix-match and anti-copy.
- **Replications.** Scherlis (Redwood Research) found induction heads in
  two-layer attention-only models with the described K-composition;
  idealized previous-token attention recovered 99% of that head's ablation
  effect, and an idealized induction pattern about 65%. Lieberum found
  candidate induction heads in GPT-2 and GPT-Neo, mostly from mid-depth.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In multi-layer transformer language models, in-context learning (by the 500-minus-50 score) appears abruptly in one early window and is then constant | strong for the models measured | Argument 1, Model Analysis Table; 200 snapshots for small models, 14–15 for large |
| C2 | Induction heads form in the same window, together with a bump in the loss and a turn in per-token-loss space; one-layer models show none of it | strong as co-occurrence | Argument 1; same table |
| C3 | Making induction expressible in one layer brings the jump to one-layer models and moves it earlier in two-layer models | moderate (two sizes, one run each) | Argument 2, smeared-key models |
| C4 | In small attention-only models, induction heads produce nearly all the in-context learning from the phase change to the end of training | strong | Argument 3, pattern-preserving ablations; Argument 5 |
| C5 | In small models with MLPs, induction heads produce much of it | moderate | Argument 3, with the MLP caveats |
| C6 | Induction heads, generalized to fuzzy matching, are the mechanism of most in-context learning in large transformers | weak | Arguments 1, 4 and 6; correlational, anecdotal and by analogy, as the authors grade them |
| C7 | The same heads that copy literal random sequences also translate and match abstract patterns | moderate as existence, anecdotal as generality | Argument 4, three heads in one model |
| C8 | The phase change links mechanistic interpretability to learning dynamics and scaling-law exceptions (one-layer models' different scaling) | weak | Discussion and Related Work; conjecture |

## Concepts

- **In-context learning score**: Loss(token 500) − Loss(token 50), averaged
  over 10,000 examples of 512 tokens.
- **Induction head**: a head that prefix-matches and copies on repeated
  random tokens; in small models, K-composition with a previous-token head
  plus a copying OV circuit.
- **Previous-token head**: a head that attends to the token immediately
  before the present one; the earlier half of the induction circuit.
- **Phase change**: the authors' name for the window in which the score,
  the heads, the loss bump and the PCA turn change together, "perhaps
  analogous to e.g. ice melting". No order parameter or critical quantity
  is defined.
- **Per-token loss vector**: a model snapshot's log-likelihoods on a fixed
  set of 10,000 tokens, treated as a point in function space.
- **Before-and-after vector**: the normalized change in the per-token loss
  vector across the phase change; a head's ablation is scored by its dot
  product with it.
- **Pattern-preserving ablation**: zero a head's output with all attention
  patterns frozen, so only downstream value computations change.

## Connections

It builds on Elhage et al.'s mathematical framework for transformer
circuits (2021), from which the induction head and its K-composition
mechanism come, on Kaplan et al.'s per-position loss as the measure of
in-context learning, and on Erhan et al. (2010) for the function-space
view of per-token losses. It places the phase change beside grokking
(Power et al., [LIT-341](../literature.d/LIT-341.md)) as a change over training rather than scale, and
points to Saxe et al.'s independent paths in deep linear networks as a
possible circuit view of learning dynamics. The same team's superposition
paper is [LIT-323](../literature.d/LIT-323.md). Later developmental work starts from it: Wang et al.'s
refined learning coefficients study the same two-layer attention-only
setting ([LIT-tmpa32mr](../literature.d/LIT-tmpa32mr.md)), and Bayazit et al. track features across
checkpoints in larger models ([LIT-tmpuuwok](../literature.d/LIT-tmpuuwok.md)). The record already used it
second-hand: [LIT-153](../literature.d/LIT-153.md) ([NOTE-106](NOTE-106.md)) rests its induction-head example on it.

## Bearing on the record

- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** This is the question's induction setting, and
  the reply's account of it at T24 is accurate. What the paper gives that
  the question can use:
  - *A circuit-only baseline over checkpoints already exists.* Per-head
    prefix-matching and copying scores, the QK eigenvalue trace for the
    previous-token term, and per-head ablation attributions to the
    before-and-after vector are all computed at every snapshot. The
    question's circuit-only arm should be at least this.
  - *The partial capacity before the circuit is a named component.* An
    induction head needs a previous-token head to compose with, so the
    circuit has a precursor that a feature-allocation model could track.
    The paper does not report when the previous-token heads form relative
    to the induction heads; Wang et al. report it for their model (LM3
    before LM4).
  - *A fourth intervention arm.* Smeared keys change the architecture and
    move the transition. The question lists optimizer, learned state and
    training exposure; architecture is a further arm with a known effect.
  - *A caution for the prospective test.* All the paper's models of one
    dataset saw the same tokens in the same order, so co-occurrence across
    sizes cannot separate the data order from the architecture. And the
    small models' phase change falls during learning-rate warm-up.
- **[THEORY-253](../theory.d/THEORY-253.md), [THEORY-783](../theory.d/THEORY-783.md), [QUESTION-193](../questions.d/QUESTION-193.md).** The paper changes no optimizer,
  and names none, so it has nothing on sign descent. Its timing evidence
  is of the other kind [THEORY-253](../theory.d/THEORY-253.md) leaves out and [THEORY-783](../theory.d/THEORY-783.md) names: a
  capability that waits on a component it composes with. Removing the
  dependency (smeared keys) moves the onset earlier, which is direct
  evidence that dependency sets the moment of this transition. It is
  evidence for [THEORY-783](../theory.d/THEORY-783.md)'s "beside dependence between skills", not for its
  optimizer clause.
- **[QUESTION-039](../questions.d/QUESTION-039.md).** A new partial answer to "what sets the moment":
  for in-context learning in transformers, the moment is set by when a
  two-head composition becomes available ([THEORY-tmp8cat0](../theory.d/THEORY-tmp8cat0.md)). It also
  bears on "one kind of event or several": the authors themselves
  suspect a shared latent event (learning to compose through the residual
  stream) of which induction is one product.
- **[THEORY-169](../theory.d/THEORY-169.md).** The paper's in-context learning is conditioning with
  fixed weights, as [THEORY-169](../theory.d/THEORY-169.md)'s is, and it reports "no evidence of
  mesa-optimizers". Its description of an induction head as an
  "in-context nearest neighbor" is the same shape as [THEORY-169](../theory.d/THEORY-169.md)'s softmax
  attention as kernel regression over stored context. The join is the
  record's, and holds only as an analogy: the induction head's kernel
  matches on the previous token through K-composition, which a single
  softmax layer cannot do.
- **[THEORY-039](../theory.d/THEORY-039.md) and [THEORY-279](../theory.d/THEORY-279.md).** The phase change is one well-measured
  transition with a mechanism. It does not show that other reported phases
  are the same kind of event; the authors place grokking beside it, not
  under it.
- **[CLAIM-329](../claims.d/CLAIM-329.md) and [TERM-071](../terms.d/TERM-071.md).** The constant in-context learning score
  after the transition is a state persistence; the authors warn that it
  need not mean the mechanism persists ("a lot could be changing during
  training even as the in-context learning score remains constant"). This
  is [TERM-071](../terms.d/TERM-071.md)'s state–dynamical distinction, made by the authors for the
  record's own example.
- **[LIT-153](../literature.d/LIT-153.md) / [NOTE-106](NOTE-106.md).** [NOTE-106](NOTE-106.md)'s C3 says the abstract overstates
  and the body calls the link speculated. The source agrees with the body:
  the authors write "preliminary and indirect evidence" and grade the
  large-model case correlational.
- **Accounts filed.** [THEORY-tmp8cat0](../theory.d/THEORY-tmp8cat0.md) (Active): the small-model result as
  measured. [THEORY-tmpkd3fq](../theory.d/THEORY-tmpkd3fq.md) (Proposed): the paper's wider thesis for large
  models with MLPs.

No instruction for machine-learning practice; the anthology may want the
work as a reading (`anthology-candidate`).

## Limitations

- **The large-model case is not causal.** No ablations of the full-scale
  models, 14–15 snapshots, and one run per model. The authors' own tables
  grade it "Medium, Correlational" at best.
- **The measure fixes what counts.** In-context learning is loss
  improvement with position, not task learning; a model could improve its
  in-context learning score by getting worse at ordinary prediction
  (footnote 17).
- **The window's dates disagree in the text.** Argument 1 gives "roughly
  2.5 to 5 billion tokens"; Model Details gives "approximately 1-3 billion
  tokens in the small models". The figures show the small models' windows
  under 3 × 10⁹.
- **Internal slips.** The Argument 4 table puts the pattern-matching head
  at "8 / 40", the text at "layer 26 of our 40-layer model"; Argument 5
  refers to "the induction heads we saw in Argument 2", meaning Argument 4.
- **Shared data order** across all models of a dataset (footnote 11).
- **Warm-up overlaps the small models' window**, which the authors note
  and do not test.
- **The direct path's exclusion** (footnote 19) assumes that a predictor
  depending only on the present token does equally well at positions 50
  and 500, which needs the token statistics to be the same at both.

## Open questions

- Is the phase change one event (learning to compose) with induction heads
  as one product, or does induction itself drive it? A model in which
  composition is possible but induction is blocked would separate them.
- What forms first, and from what? The paper does not report the order of
  previous-token and induction heads or what the heads did before.
- Does the after-score stay constant because one mechanism stays, or
  because changing mechanisms balance against harder marginal bits
  (footnotes 13–14)?
