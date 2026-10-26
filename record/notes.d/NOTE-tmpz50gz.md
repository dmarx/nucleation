---
status: Read
paper: LIT-tmpn9ui7
title: 'Bricken, Templeton, Batson, Chen, Jermyn et al. — Towards monosemanticity'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the article's HTML at
    transformer-circuits.pub/2023/monosemantic-features/index.html,
    headed "Published Oct 4, 2023", fetched that day; the text was
    extracted by script (about 165,000 characters) and read whole. Read:
    the introduction and Summary of Results; Problem Setup (features as a
    decomposition, the superposition hypothesis, what makes a good
    decomposition, why not architectural approaches with its one-neuron
    loss example, sparse autoencoders, the setup, how to tell if it works,
    the one-layer model, notation); all four detailed investigations
    (Arabic script, DNA, base64, Hebrew); Global Analysis (manual and
    automated interpretability, activation intervals, caveats, loss
    explained, model versus data with the shuffled-weights control);
    Phenomenology (motifs, feature splitting with the mathematics example
    and the two "bugs", universality, "finite state automata"); Related
    Work; Discussion; Nanda's comment; the author contributions; and every
    appendix (feature proxies, ablations, the interpretability rubric,
    density histograms, transformer training, the three parts of the
    advice on training autoencoders, activation visualization, UMAPs, and
    the automated interpretability appendix with the randomized
    transformer, importance scoring and explanation lengths). All 44
    footnotes were read. The figures are interactive or raster and carry
    numbers only in captions and text, so plots (activation histograms,
    scatter plots, the interpretability histograms, the density
    histograms, the L0–loss frontier, the UMAPs) were read from captions
    and text, not inspected. The feature browsers linked from the article
    were not opened. The one-neuron loss example and the dataset sizes
    were recomputed.
date: '2026-10-26'
summary: >-
  Sparse autoencoders trained on the 512-neuron MLP layer of a one-layer
  transformer, at widths from 512 to 131,072, recover features that one
  blinded author and Claude both rate far more interpretable than neurons,
  that mostly match no neuron, whose effects on the output (which the
  autoencoder never saw) agree with their activations, and that recur in a
  second model trained from another seed. The features split into finer
  families as the dictionary widens, so the authors doubt there is one
  correct number of features. Everything is in one MLP layer of a one-layer
  model, and the detailed cases are chosen to be easy.
---
<!-- inactive-ok-file: THEORY-tmpz7jrx CLAIM-tmpwr001 THEORY-017 CLAIM-135 — Proposed; the account this reading files and the claims it bears on, cited as open -->
# NOTE-tmpz50gz: Bricken, Templeton, Batson, Chen, Jermyn et al. — Towards monosemanticity

## Contribution

It takes the third strategy Toy Models of Superposition (LIT-323) named
for undoing superposition, dictionary learning after training, and shows
in a real if tiny language model that it yields units more interpretable
than the model's neurons. It also argues the first strategy, training
models without superposition, cannot work for language models: neurons
stay polysemantic even when activations are one-hot, because cross-entropy
can prefer an ambiguous neuron. Its standard of evidence for a feature is
the one later work kept: specificity and sensitivity against a proxy,
downstream effects, no matching neuron, and recurrence in another model.

## Key insight

The autoencoder sees only the MLP's activations, never what the rest of
the model does with them. So the feature's effects on the output are an
independent test of whether it is a unit of the model's computation or
only a pattern in the data. The authors use them that way: logit weights,
ablation and "pinned" sampling are checked against the feature's
activations, and a control on a transformer with shuffled weights yields
mostly single-token features and no interpretable effects.

## Assumptions

- **The model.** Two one-layer transformers, "A" and "B", identical but
  for the seed: residual stream 128, one MLP of 512 ReLU neurons, trained
  on 100 billion tokens of the Pile with Adam. The MLP is "the simplest
  language model we profoundly don't understand", and its effect on the
  logits is approximately linear, which the authors say makes linear
  features more likely here and generalization to deeper models less so.
- **The autoencoder.** One hidden ReLU layer, untied encoder and decoder,
  decoder columns of unit norm, a pre-encoder bias tied to the decoder bias
  and initialized at the geometric median. Loss: mean squared error plus an
  L1 penalty on the feature activations. Trained with Adam on 8 billion
  activation vectors (1 million steps of 8,192, drawn without replacement
  from 10 billion collected as 250 tokens from each of 40 million
  contexts), with "neuron resampling" of dead units at four points in
  training.
- **Runs.** Many dictionaries, named A/0 … A/5 at fixed L1 and widths
  from 512 to 131,072; the detailed analyses use A/1, with 4,096 features,
  of which 168 are dead and 292 "ultralow density" and are excluded,
  leaving 3,636.
- **Features as directions.** x ≈ b + Σ f_i(x) d_i, the linear
  representation hypothesis and the superposition hypothesis taken as the
  working frame. The authors are explicitly "agnostic" on whether models
  are "composed of features" or features are "a convenient post-hoc
  description".
- **No metric of success.** The authors searched for one and found none
  ("we have yet to find anything satisfactory"); runs were steered by
  inspection, feature density, reconstruction loss and toy models.

## Key results

- **Neurons are polysemantic without superposition.** In a one-neuron
  model with four exclusive features, firing for A alone costs (3/4)ln 3
  ≈ 0.82 nats and firing for A or B costs ln 2 ≈ 0.69 (both recomputed
  here), so the loss prefers the polysemantic neuron. Experiments with
  activations sparse "to the point of … 1-hot" gave the same. Under MSE,
  as in the autoencoder, the preference does not arise.
- **Four detailed features** (chosen, by the authors' account, because
  proxies are easy to write): Arabic script A/1/3450 (0.13% of training
  tokens but 81% of the tokens where it fires, 98% above activation 5;
  correlation with the proxy 0.74); DNA A/1/2937 (0.8 with a binarized
  proxy); base64 A/1/2357 (0.38, the proxy being too broad); Hebrew
  A/1/416 (0.55). Each has logit weights with a second mode on the
  expected tokens, ablation effects in the expected direction and, for
  Arabic and base64, pinned sampling that produces that script.
- **Not neurons.** For the Arabic feature the most correlated neuron
  responds to many non-English languages, and its three largest neuron
  coefficients are negative, with 27 above 0.1 in magnitude. No neuron has
  Hebrew among its top examples. The base64 feature's best neuron
  correlates 0.18 and does much else.
- **Interpretability across the board.** One blinded author scored 412
  activation intervals over 162 features and neurons on a 0–14 rubric:
  median neuron 0, median feature interval 12. Claude's explanations
  predicted held-out activations better for features than neurons, and
  predicted top logit tokens at 74% for features against 58% for neurons
  (chance 50%; the appendix gives medians, 0.74 against 0.53). Lower
  activation intervals are less consistent with the interpretation.
- **Loss explained.** Splicing A/1's reconstruction in place of the MLP
  recovers 79% of the loss reduction the MLP provides; A/5 (131,072
  features) recovers 94.5%. The authors call the zero-ablation baseline
  "especially bad", so the percentage is "considered an overestimate", and
  note that a small MLP trained from scratch reaches similar figures.
- **Model, not data.** On the shuffled-weights transformer the autoencoder
  finds mostly single-token features and features the authors could not
  interpret; automated scoring rates the randomized model's features
  higher at the median, because single-token features are trivial to
  predict. The non-single-token ones score like polysemantic neurons.
- **Universality.** For each A/1 feature, the most similar feature of B/1
  has a median activation correlation of 0.72, against 0.46 for neurons.
  Logit-weight correlations are much lower (Arabic 0.23 against 0.91 for
  activations; one pair correlates 0.98 in activation and negatively in
  logits), which the authors attribute to "interference" weights on
  irrelevant tokens. Many features echo neurons and features reported
  before (base64, hexadecimal, all-caps in SoLU models; region features).
- **Feature splitting.** Base64 is one feature at 512, three at 4,096 and
  more at 16,384. The three of A/1 are base64 letters, base64 digits
  (predicting non-digits, a tokenizer artifact) and base64 that encodes
  ASCII text. Splits "both split and merge" between levels, "more complex
  than a tree". Single-token features in small dictionaries are read as
  collapsed families.
- **"Finite state automata".** Features chain through the token stream:
  one raises the probability of tokens that trigger the next (HTML tags;
  two-token Unicode characters; IRC transcripts), and a run of features
  memorizes a licence phrase. The authors stress these are not circuits
  the model learned to coordinate.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Sparse autoencoders extract features from a one-layer transformer's MLP that are much more interpretable than its neurons | strong for this model | one blinded rater (162 units), automated scoring of all features, logit prediction |
| C2 | Many such features do not correspond to any neuron | strong for the four cases; moderate in general | correlation and coefficient analyses for four chosen features |
| C3 | The features are units of the model's computation, not only of the data | moderate | logit weights, ablation and pinning agree with activations; shuffled-weights control |
| C4 | The features explain a substantial part of the MLP | moderate | 79% of loss recovered, against a baseline the authors call an overestimate |
| C5 | Features are universal across seeds | moderate | median activation correlation 0.72 vs 0.46; same data and architecture only |
| C6 | Features split into families as the dictionary widens, so there may be no correct number of features | moderate as observation, weak as theory | base64 and mathematics cases, UMAPs; the "idealized features" picture is a conjecture |
| C7 | Language models cannot be made monosemantic by architecture | weak | the one-neuron loss argument and unpublished experiments |
| C8 | Some version of the superposition and linear representation hypotheses is true | weak | "observations … what you would expect from superposition" |

## Concepts

- **Feature (here)**: a column d_i of the decoder with its encoder
  activation f_i(x); "the basic set" of interpretable directions.
- **Monosemantic**: a unit whose activations and effects fit one
  interpretation across its activation spectrum.
- **Feature splitting**: one feature of a narrow dictionary covered by
  several finer features of a wider one, often token-in-context features.
- **Proxy**: a log-likelihood ratio log P(s | context)/P(s) used to score
  a feature's specificity and sensitivity.
- **Dead / ultralow-density features**: autoencoder units that never fire,
  or fire on fewer than one in a million tokens; the authors treat the
  latter as an artifact of training.
- **Interference weights**: the broad central mode of a feature's logit
  weights, which the authors read as the cost of superposition.

## Connections

It is the direct sequel of Toy Models of Superposition (LIT-323,
NOTE-278), whose isotropic picture of features it says was "missing
something crucial": real features clump, by correlated activation and by
similar "output actions". It credits Sharkey et al.'s interim reports and
Cunningham et al. for the same approach in parallel, and Olshausen and
Field's sparse coding stands behind it. The scaled-up sequel is
LIT-tmp8w8uj. Circuits over its features are LIT-tmp5b0z9. The record's
test of such features as causal units is MIB (LIT-tmprlq7z,
THEORY-tmp4lqc8), and its reading of the Gemma Scope autoencoders is
LIT-611 (THEORY-504).

## Bearing on the record

- **CLAIM-tmpwr001.** Two things here bear on the claim that a recovered
  feature is at most a constituent. First, the paper's own test separates
  a feature's activation pattern from its role: the effects on the output
  are checked independently, and the shuffled-weights control shows that
  activation structure alone can come from the data. That is the claim's
  point about features found without the relations that make them work,
  made by the authors as method. Second, the "finite state automata" are
  organizations of features through the token stream that no single
  feature holds, and the authors decline to call them circuits because
  the model never learned them to work together. The paper does not ask
  whether features compose into anything above them inside the model; one
  MLP layer cannot show it.
- **THEORY-017 and THEORY-018.** Feature splitting, with splits that
  merge, makes the feature set a resolution set by width and L1, not the
  model's one basis; the authors say the correct number of features "may
  not be well-posed" (THEORY-tmpz7jrx). That is THEORY-017's thesis that
  parts are fixed by a choice, in a measured case. Under THEORY-018, the
  dictionary is also one choice among many that reconstruct equally; the
  universality across seeds is a check on that choice, not a proof that it
  is unique.
- **THEORY-tmp4lqc8 and LIT-tmprlq7z.** The two do not conflict. This
  paper shows features are more interpretable than neurons by human and
  model judgement; MIB shows they localize supplied causal variables worse.
  Interpretability is not the same test as carrying a hypothesized
  variable.
- **QUESTION-tmpivbso.** The paper's features are of one trained model.
  Nothing tracks them over training. The ultralow-density cluster and the
  dead features are artifacts the question's feature-tracking would have to
  separate from real change.
- **CLAIM-135.** Recovering features is reconstruction and partial
  identification in CLAIM-135's terms; the authors' agnosticism about
  whether models are "composed of features" is the step to constitution
  left open.

No instruction for machine-learning practice is drawn here; the training
advice in the appendices is the anthology's kind of content
(`anthology-candidate`).

## Limitations

- **One layer, one site.** A one-layer model's single MLP, whose output is
  nearly linear in the logits; the authors expect this to make the linear
  picture more likely here and less general.
- **Cherry-picked deep dives.** The four features are chosen because
  proxies are easy to write, as the authors say.
- **One human rater**, an author, on 162 units.
- **The loss figure's baseline** is zero-ablation, which the authors call
  an overestimate.
- **Universality is minimal**: same data, same architecture, another
  seed. Comparisons with the literature are qualitative.
- **No ground truth** for the features, and no agreed metric of success.
- **Small slips.** The feature-ablation appendix writes the subtracted
  term as f_i(x^j)d_j, where d_i is meant. The automated logit result is
  given as a mean (74% against 58%) in the text and as medians (0.74
  against 0.53) in the appendix; not an error, but two statistics for one
  result.

## Open questions

- Do the same features, and the same splitting, appear across training of
  one model, or are they a property of the finished model only?
- Does a wider dictionary converge on a fixed set (the authors' "idealized
  features"), or keep splitting without limit, as a feature manifold would?
- Are token-in-context features the model's local code, or an artifact of
  the L1 penalty pushing a compositional code towards a local one? The
  authors lean to the first and do not test it.
