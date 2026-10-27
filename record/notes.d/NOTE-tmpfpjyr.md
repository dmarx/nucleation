---
status: Read
paper: LIT-tmp8w8uj
title: 'Templeton, Conerly, Marcus, Lindsey et al. — Scaling monosemanticity'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the article's HTML at
    transformer-circuits.pub/2024/scaling-monosemanticity/index.html,
    headed "Published May 21, 2024", fetched that day; the text was
    extracted by script (about 146,000 characters) and read whole. Read:
    the introduction and Key Results; Scaling Dictionary Learning (sparse
    autoencoders, the three runs, scaling laws); Assessing Feature
    Interpretability (the four example features with specificity and
    steering, the code-error and addition features, features against
    neurons); Feature Survey (the Golden Gate Bridge, immunology and inner
    conflict neighbourhoods, feature completeness, the person, country,
    code and list-position categories); Features as Computational
    Intermediates (the emotional and multi-step inference examples);
    Searching for Specific Features; every Safety-Relevant Features
    section, including the deception case study and the self-representation
    features; Comparison to Other Approaches; the Discussion
    (safety, generalization, limitations); Related Work; the author
    contributions; and the appendices (dataset examples, feature steering,
    comparison with few-shot probe steering, ablations and attributions,
    and the table of further safety-relevant features). All 16 footnotes
    were read. The figures (the scaling-law plots, specificity histograms,
    the automated interpretability histograms, the completeness curves,
    the steering transcripts, the neighbourhood maps and the image
    examples) are images or interactive and were read from captions and
    text; numbers that appear only in a figure are not used. The feature
    browsers were not opened.
date: '2026-10-26'
summary: >-
  Sparse autoencoders of about 1M, 4M and 34M features on the middle-layer
  residual stream of Claude 3 Sonnet, trained to a compute-optimal loss,
  explain at least 65% of its variance and yield features that are
  multilingual and multimodal, that mostly match no neuron, and that steer
  the model's output when clamped, including features for unsafe code,
  bias, sycophancy and deception. Whether a concept has its own feature
  depends on its training frequency relative to the number of live
  features. The interpretability and steering evidence is shown on selected
  features, and the most strongly active features are mostly not those that
  matter to an answer.
---
<!-- inactive-ok-file: THEORY-tmp14ee2 THEORY-tmpz7jrx CLAIM-tmpwr001 — Proposed; accounts this reading files or bears on, cited as open -->
# NOTE-tmpfpjyr: Templeton, Conerly, Marcus, Lindsey et al. — Scaling monosemanticity

## Contribution

It answers the question its predecessor ([LIT-tmpn9ui7](../literature.d/LIT-tmpn9ui7.md)) left: whether
sparse autoencoders work on a frontier model. On Claude 3 Sonnet they
yield millions of features, many abstract, and the paper's evidence that
these are used by the model is steering: clamping a feature changes what
the model says in the feature's direction. It adds scaling laws for the
autoencoder's own loss, a frequency law for which concepts get a feature,
and a survey of features the authors call safety-relevant.

## Key insight

Two of its findings cut against the simple reading of a feature as a
concept the model holds. First, steering usually needs a feature clamped
far outside its observed range ("typically requires clamping feature
activations to values outside their observed range"), which the authors
explain by features being "co-active with several correlated features
with related meanings". Second, the features that matter to an answer are
mostly not the most active ones: on the Kobe Bryant prompt, three of the
ten most active features are among the ten with the largest ablation
effect, and activation correlates 0.12 with ablation effect where
attribution correlates 0.81. A feature's activity does not give its role.

## Assumptions

- **The model and site.** Claude 3 Sonnet (3.0, the fine-tuned
  production model of March 2024). Its size, some plot units and the
  tokenizer are withheld or simplified. The autoencoders read the residual
  stream "halfway through the model", chosen as smaller than the MLP and
  less affected by "cross-layer superposition".
- **The autoencoder.** Activations normalized so their mean squared norm
  is the residual dimension; encoder ReLU(W_enc x + b_enc); loss MSE plus
  λ Σ f_i ‖W_dec,i‖ with λ = 5, so that the decoder norm enters the
  penalty and the feature activation is f_i ‖W_dec,i‖. One epoch on text
  similar to pre-training data, with no Human/Assistant data and no
  images.
- **Three runs.** 1,048,576, 4,194,304 and 33,554,432 features; fewer than
  300 active per token; at least 65% of variance explained; dead features
  (inactive over 10⁷ tokens) about 2%, 35% and 65%, so the 34M run has
  "only about 12M alive features" (35% of 33.6M is 11.7M, checked here).
- **Scaling laws** for the autoencoder's loss at λ = 5, which the authors
  treat as a proxy for quality while doubting it is optimal.
- **Interpretation** relies on Claude: Claude 3 Opus scores specificity on
  a 0–3 rubric, and Claude writes the labels that guide feature search.

## Key results

- **Scaling laws.** At compute-optimal settings the loss falls roughly as
  a power law in compute, and the optimal number of features grows
  somewhat faster than the optimal number of steps. The figures carry the
  exponents; the text does not.
- **Four example features** (Golden Gate Bridge 34M/31164353, brain
  sciences 34M/9493533, monuments 1M/887839, transit 1M/3), chosen to
  have straightforward interpretations. Their strongest activations are
  rated consistent with the label; specificity falls at weak activation.
  Sensitivity was not measured "in a scalable, rigorous way". The Golden
  Gate feature fires on the bridge's Wikipedia sentence in several
  languages and on images, although the autoencoders saw only text.
  Clamped at 10× its maximum, it makes the model call itself the bridge.
- **Sophisticated features.** A code-error feature (1M/1013764) fires on
  bugs across languages but not on prose typos; clamped high it makes the
  model hallucinate an error message, clamped negative it predicts the
  bug-free output and, with a delicate prompt, rewrites the code. An
  addition feature (1M/697189) fires on functions that add, including by
  composition, and not on ones that multiply.
- **Features against neurons.** For 82% of a random sample of 1M features,
  no neuron in any earlier layer correlates above 0.3. On 100 random
  features and 100 random neurons, the features are "significantly more
  interpretable" and more specific; the numbers are in figures only.
- **Feature completeness.** Coverage of a category rises with dictionary
  size, but the 34M dictionary has features for about 60% of London
  boroughs although the model can name all of them. Across elements,
  cities, animals and foods (100–200 concepts each), the frequency at which
  a concept is more than 50% likely to have a feature is "consistently
  slightly lower than the inverse of the number of alive features", and
  the three curves overlap when rescaled by it ([THEORY-tmplbzq5](../theory.d/THEORY-tmplbzq5.md)).
- **Computational intermediates.** On "John says, 'I want to be alone
  right now.' John feels" the top features by attribution and ablation are
  "need to be alone" and "sadness". On the Kobe Bryant capital prompt the
  top five by ablation are Kobe Bryant, California, capital, Los Angeles
  and the Lakers, which rank 70th to 162nd by activation; the biggest-rival
  prompt implicates Kobe and the Lakers but not California
  ([THEORY-tmph7ceb](../theory.d/THEORY-tmph7ceb.md)). The authors call the example "somewhat
  cherry-picked", and for other prompts found nothing intermediate at this
  layer.
- **Safety-relevant features.** Features for unsafe code, backdoors, bias,
  sycophancy, deception, power-seeking, dangerous content and the model's
  self-representation, each shown with steering examples. The authors warn
  that their existence says nothing about how dangerous models are, and
  that "the present work does not show that any features are actually
  useful for safety".
- **Against few-shot probes.** In seven cases where feature steering
  worked, a difference-of-means vector from the same one or two positive
  and negative examples steered as well twice and failed five times. The
  authors limit this to the few-shot regime.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Sparse autoencoders produce interpretable features for a large production model | moderate | selected features, rubric scoring by Claude 3 Opus, a 100-feature comparison with neurons |
| C2 | SAE features are mostly not neurons | strong for the sample | 82% of sampled features have no neuron correlated above 0.3 |
| C3 | Features are abstract: multilingual, multimodal, concrete and abstract | moderate as existence | examples, chiefly the Golden Gate and code-error features |
| C4 | Features causally influence behaviour in the direction of their labels | moderate as existence, weak as generality | steering transcripts for selected features, usually clamped beyond their observed range |
| C5 | Whether a concept has a feature is set by its frequency relative to the number of live features | moderate | four categories, three dictionaries, one collapsed curve |
| C6 | Attribution finds the features that matter to an answer; activation does not | moderate | two prompts with every active feature ablated (0.81 against 0.12) |
| C7 | Scaling laws guide autoencoder training | moderate | sweeps; the loss is a proxy whose relation to interpretability is unknown |
| C8 | Features are better steering handles than few-shot probes | weak | seven hand-tuned cases, chosen where features worked |
| C9 | Safety-relevant features exist and can be found and steered | moderate as existence; nothing on usefulness, as the authors say | examples |

## Concepts

- **Feature activation (here)**: f_i(x)·‖W_dec,i‖, the encoder output
  scaled by the decoder column's norm.
- **Clamping / feature steering**: replace the reconstruction with one in
  which a feature is fixed, keep the reconstruction error, run the rest of
  the model; values are in multiples of the feature's maximum over the
  training data.
- **Attribution**: gradient of a logit difference with respect to the
  residual stream, dotted with the feature vector, times the activation;
  attribution patching with a zero baseline.
- **Cross-layer superposition**: a feature spread across several layers'
  outputs, which an autoencoder on one layer cannot isolate.
- **Live (alive) features**: features active at least once in 10⁷ tokens.

## Connections

The direct scale-up of [LIT-tmpn9ui7](../literature.d/LIT-tmpn9ui7.md). It cites Marks et al. ([LIT-tmp5b0z9](../literature.d/LIT-tmp5b0z9.md))
under "sparse feature circuits" as the next step, Cunningham et al. and
Tamkin et al. as parallel work, and Gemma Scope's open autoencoders
belong to the same programme ([LIT-611](../literature.d/LIT-611.md)). The probe and steering literature
it compares itself with is the representation-engineering and
linear-probe line. Its splitting at 1M, 4M and 34M is a second case for
[THEORY-tmpz7jrx](../theory.d/THEORY-tmpz7jrx.md). Its feature visualizations are reused by the attribution
graphs of Circuit Tracing (LIT-tmpsuo6l), which replace its residual-stream
dictionary with cross-layer transcoders, and so by their companion, the
Biology paper (LIT-tmpjvwet).

## Bearing on the record

- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** Three findings support the claim's point that a
  recovered feature is at most a constituent. Activity does not identify
  role: the features that carry an answer are found by intervention
  (ablation, attribution), not by activation, and correlate with it at
  0.12 ([THEORY-tmph7ceb](../theory.d/THEORY-tmph7ceb.md)). A single feature usually moves the model only
  when pushed past anything it does in use, which the authors put down to
  correlated features acting together. And the authors say that lacking a
  dedicated feature "does not mean that the reconstructed activations do
  not contain information about that concept, as the model can use
  multiple related features compositionally". What the claim calls the
  organized relationship among features is, in this paper, the circuit the
  authors say "a truly satisfactory analysis would likely involve" and do
  not give.
- **[THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md) and [LIT-tmprlq7z](../literature.d/LIT-tmprlq7z.md).** The paper's comparison with
  probes is few-shot, hand-tuned and chosen where features worked; MIB's
  comparison is fixed in advance, on held-out counterfactuals, with known
  causal variables, and finds SAE features worse than neurons. They answer
  different questions, and the thesis that SAE features are a large model's
  working units ([THEORY-tmp14ee2](../theory.d/THEORY-tmp14ee2.md)) has to meet MIB's result.
- **[THEORY-504](../theory.d/THEORY-504.md).** Like Gemma Scope's worst site by loss, these are
  residual-stream autoencoders, explaining at least 65% of variance. Steering
  keeps the reconstruction error, so a third or more of the activation
  rides along unexplained in every intervention.
- **[THEORY-tmpz7jrx](../theory.d/THEORY-tmpz7jrx.md).** Splitting at 1M, 4M and 34M, and coverage set by
  live-feature count ([THEORY-tmplbzq5](../theory.d/THEORY-tmplbzq5.md)), make the feature set depend on the
  dictionary.
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** The autoencoders are of one finished, fine-tuned
  model at one layer. The cross-layer superposition the authors describe
  would also confound a feature model fitted to one layer across
  checkpoints.
- The safety findings and the steering comparisons are for the anthology
  and for safety work; nothing is drawn here as an instruction.

## Limitations

- **Selected evidence.** The example, sophisticated and safety features,
  and the steering cases, are chosen; the random-sample comparisons
  (82%; 100 features against 100 neurons) are the unselected part.
- **Proprietary model.** Size, some units and the tokenizer withheld; no
  replication possible outside the authors' lab.
- **Reconstruction.** At least 65% of variance explained, with 2%, 35% and
  65% dead features; "orders of magnitude short" of all features, by the
  authors' estimate.
- **Specificity without sensitivity.** Sensitivity was not measured at
  scale.
- **Two prompts** for the activation–attribution–ablation comparison.
- **Shrinkage** from the L1 penalty, which the authors believe
  "significantly harms" performance.
- **Small slips.** In the appendix table of safety-relevant features,
  1M/954062 ("harm and abuse, including drug-related harm, credit card
  theft…") sits under "Power-seeking behavior", and an opinion-stance
  feature (34M/12576250) under "Deception and social manipulation"; the
  categories look misplaced. The ablation–attribution correlation is "0.8"
  in the text and "about .81" in the appendix, which agree.

## Open questions

- Do features found at the middle layer form circuits that explain the
  intermediate steps the authors see (Kobe → California → Sacramento)?
- Would a systematic, non-selected steering evaluation, with supervised
  baselines given more than a few examples, keep features ahead?
- How much of a steering effect is the feature, and how much the
  reconstruction error that rides along?
