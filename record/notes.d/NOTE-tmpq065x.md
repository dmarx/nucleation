---
status: Read
paper: LIT-tmpuuwok
title: 'Bayazit, Mueller and Bosselut — Crosscoding through time'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF of 2509.05291v2 (30
    April 2026, 25 pages), text extracted with pdftotext in both plain and
    layout modes. v1 (5 September 2025) was not compared. Read: the
    abstract, §§1–8 (introduction, related work, preliminaries on
    crosscoders and indirect effects, the method with RelIE, the
    experimental setup, checkpoint selection and crosscoder quality, the
    monolingual and multilingual results), limitations, conclusion,
    acknowledgements and ethics, and appendices A (sparse autoencoders),
    B (datasets and preprocessing), C (models), D (crosscoder training and
    statistics, Table 6), E (the RelIE-against-RelDec ablation, Table 7),
    F (integrated gradients and the annotation protocol) and the
    annotation tables of F–G as far as extraction allowed. Figures 3 and 4
    and Tables 1 and 2 were read from page renderings (pp. 6–7); the other
    figures from captions and text. The released code and annotations were
    not opened.
date: '2026-10-26'
summary: >-
  Trains one sparse crosscoder jointly on the mid-layer activations of two
  or three pretraining checkpoints, so features share an index across
  them, and scores each feature's causal importance for subject–verb
  agreement at each checkpoint (Relative Indirect Effect). In Pythia-1B,
  OLMo-1B and BLOOM-1B the important features move, by the authors'
  annotation, from token-specific detectors to grammatical-category ones,
  and in BLOOM from language-specific to crosslingual ones for Latin-script
  languages; importance keeps shifting after accuracy plateaus. A method
  for describing which features emerge, persist and lose importance, not
  for predicting it.
---
<!-- inactive-ok-file: THEORY-tmpt45mh THEORY-279 — Proposed; the account this reading files and a neighbouring one, cited as open -->
<!-- inactive-ok-file: CLAIM-329 CLAIM-263 CLAIM-427 CASE-tmplcm41 CLAIM-tmpwr001 — Proposed; the record's own claims and the construction this reading bears on, cited as open -->
# NOTE-tmpq065x: Bayazit, Mueller and Bosselut — Crosscoding through time

## Contribution

The first use of crosscoders across pretraining checkpoints, where earlier
work had used them only between a base and a post-trained model. One sparse
dictionary is learned for several checkpoints at once, so a feature has the
same index at each, with a separate decoder per checkpoint. A new score,
the Relative Indirect Effect (RelIE), says at which checkpoint a feature
matters causally for a task. Applied to subject–verb agreement in three
1B-parameter model families, it describes which features appear, stay and
lose their role, and the authors read the trend as token-level detectors
giving way to abstract grammatical ones.

## Key insight

Separate a feature's presence from its use, and both from time. A joint
dictionary gives each feature a decoder at every checkpoint, so its
presence can be compared (decoder norms, RelDec). An attribution at each
checkpoint gives its effect on the task there, so its use can be compared
(RelIE). A feature can be present at two checkpoints and matter at only
one.

## Assumptions

- **Crosscoder.** f = ReLU(Σ_c W_enc^c x^c + b_enc), x̂^c = W_dec^c f + b_dec^c,
  loss Σ_c ‖x^c − x̂^c‖² + Σ_c Σ_i f_i ‖W_dec,i^c‖ (Eqs. 1–3), with a shared
  encoder bias. 2¹⁴ features, trained on about 400M tokens of the model's
  own pretraining data (the Pile, Dolma, or mC4 in ROOTS's top-ten language
  proportions), Adam at 5 × 10⁻⁵, the ℓ1 coefficient ramped to 2, three
  seeds.
- **Site.** The output of the middle transformer block only: layer 8 of
  Pythia-1B and OLMo-1B, layer 12 of BLOOM-1B.
- **Checkpoints**, chosen where task accuracy or the mean cosine
  similarity of mid-layer activations shifts: Pythia {128M, 1B, 4B, 286B}
  tokens, OLMo {2B, 4B, 33B, 3T}, BLOOM {550M, 6B, 55B, 341B}. Crosscoders
  are trained on pairs and triplets of these.
- **Indirect effect.** m(x) = log p(t_wrong | x) − log p(t_correct | x) on
  minimal pairs with a single-token difference; a feature's IE is the
  change in m when it is zero-ablated, approximated by integrated gradients
  over 10 steps, averaged over the batch and thresholded at 0.1.
- **RelIE.** Two-way: |IE^{c2}| / (|IE^{c1}| + |IE^{c2}|). Three-way: the
  vector of each checkpoint's |IE| over their sum. RelDec is the same with
  decoder norms in place of IEs, and is task-agnostic.
- **Tasks.** Subject–verb agreement from BLiMP (four subtasks), MultiBLiMP
  (number, person and gender in six languages) and CLAMS (English and
  French).
- **Annotation.** The top-10 IE features per checkpoint are described by
  the authors from top-activating pretraining sequences, blind to their
  RelIE values, with translators and a native speaker for languages the
  authors do not speak.

## Key results

- **Crosscoders reconstruct early checkpoints too.** Across three seeds,
  splicing the reconstruction in raises cross-entropy mostly by under 0.2
  nats, about 0.35 when the checkpoints are far apart, with more dead
  features (Table 6).
- **Checkpoints.** Pythia-1B goes from near chance (about 50%) to above
  90% on BLiMP agreement between 128M and 4B tokens, with a smaller step at
  1B. OLMo-1B moves at 2B and 4B and consolidates near 33B. BLOOM-1B jumps
  at 6B. In all three "activations continue refining" after accuracy
  plateaus (Fig. 2).
- **Token detectors to categories (Pythia, Table 1, Fig. 3).** Early
  important features detect particular tokens and subtokens ("-ans",
  "woman") or are uninterpretable; by 4B they detect groups such as
  multi-word nouns in scientific writing or nouns for groups of people;
  between 4B and 286B, detectors such as deverbal nominalizations
  "continue to emerge and strengthen". Of the top-5 and bottom-5 features
  tracked from 1B to 286B, low-level or unannotated ones fall in IE and
  grammatical ones rise. OLMo shows the same over a longer horizon
  (appendix G).
- **Importance redistributes after the plateau (Fig. 4).** In the
  three-way RelIE of Pythia's top-100 IE features at 1B, 4B and 286B,
  high-importance features are mostly shared by 4B and 286B, but "many
  features also cluster near the 4B- and 286B-specific corners, indicating
  that even after performance plateaus, the model's internal concepts
  continue to evolve". Features shared by 1B and 286B alone are few and
  less interpretable. No counts are given.
- **Monolingual to crosslingual (BLOOM, Table 2, Fig. 5).** At 6B many
  important features are language-specific, the crosslingual ones being
  punctuation and delimiters. By 341B the overlap of top-10 features for
  number agreement rises across English, French, Spanish and Portuguese,
  after a dip at 55B. Hindi and Arabic overlap little, and much of what
  they share is punctuation; Hindi's important features encode verbal
  aspect and the object.
- **RelIE against RelDec (appendix E, Table 7).** For the top-10 IE features
  per BLiMP subtask, ablated one at a time, the ratio of the ablation's
  effects at the two checkpoints correlates with RelIE at Spearman ρ 0.945
  (Pythia) and 0.952 (OLMo) on average, and with RelDec at 0.787 and 0.843.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A crosscoder trained jointly on two or three pretraining checkpoints, including early ones, reconstructs their mid-layer activations with small loss in next-token prediction | strong | Table 6, three seeds |
| C2 | RelIE tracks which checkpoint a feature matters for better than RelDec does | moderate | Table 7; the ablation and RelIE are both indirect effects, so the agreement partly checks the integrated-gradient approximation |
| C3 | Features important for agreement shift from token-specific to abstract grammatical detectors over pretraining | moderate | authors' annotation of top-10 features, Tables 1, 8, 11; Fig. 3 |
| C4 | Causal importance keeps redistributing among features after task accuracy plateaus | moderate | Fig. 4, a scatter without counts; Fig. 2's activation similarity |
| C5 | In a multilingual model, language-specific features consolidate into crosslingual ones for languages with similar agreement systems, while Hindi and Arabic keep language-specific ones | moderate | Fig. 5, Table 2, Tables 13–15; one layer of one model |
| C6 | The approach is architecture-agnostic and scales to billion-parameter models | moderate | three 1B families; the authors note difficulty beyond 7B |

## Concepts

- **Sparse crosscoder**: a sparse autoencoder with one encoder and decoder
  per source (here, per checkpoint) and one shared latent space, with a
  sparsity penalty weighted by the sum of the decoder norms.
- **RelDec**: a feature's decoder norm at one checkpoint over the sum at
  both; task-agnostic presence.
- **RelIE**: the same ratio on absolute indirect effects for a task;
  task-specific use.
- **Emergence, maintenance, discontinuation**: in practice, a feature's
  RelIE concentrated on the later checkpoint, spread over several, or
  concentrated on the earlier one. "Discontinuation" is loss of effect on
  the task, not removal from the dictionary.

## Connections

It extends Lindsey et al.'s crosscoders (2024) from layers and from base
against post-trained models to pretraining checkpoints, and takes its
indirect effects and integrated-gradient approximation from Marks et al.'s
sparse feature circuits. Its checkpoint selection follows work on phase
transitions in accuracy or loss (Chen et al. 2024, cited also by
[LIT-tmpa32mr](../literature.d/LIT-tmpa32mr.md)) and Kangaslahti et al.'s POLCA. The sparse-autoencoder line
behind it is in the record through Gemma Scope ([LIT-611](../literature.d/LIT-611.md)), and the
superposition hypothesis it presupposes, features as directions, through
[LIT-323](../literature.d/LIT-323.md). Olsson et al. ([LIT-tmpe7b5o](../literature.d/LIT-tmpe7b5o.md)) is cited as a task-proxy method that
"only reveal[s] when changes occur".

## Bearing on the record

- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** This is the "crosscoders" comparator the reply
  named, and the reply's description at T24 is accurate. For the question:
  - *The feature-only arm has a published form.* A joint dictionary across
    checkpoints, with per-checkpoint attributions, is a feature-only
    description of development that the coupled model must out-predict.
    It covers two or three checkpoints at a time, chosen after the fact, at
    one layer, and it predicts nothing.
  - *It is what the question's allocation model would be without a
    temporal prior.* Shared features and per-checkpoint decoders are a
    deterministic, sparse stand-in for the dynamic feature allocation; the
    question's temporal prior is what would let it predict.
  - *Feature identity across checkpoints is by construction.* Two
    checkpoints share a feature because the joint dictionary assigns them
    one index. The question's own condition, that births and splits be
    told apart from the model's free symmetries, applies here too: a
    crosscoder can split one direction into checkpoint-specific copies or
    merge two, depending on the sparsity penalty ([CLAIM-263](../claims.d/CLAIM-263.md)'s quotient).
- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md) (having against using).** The case found that its model
  cannot tell holding a feature from using it, from outputs alone. This
  paper separates the two in a transformer by measuring them differently:
  presence by decoder norm, use by an intervention on the task. That is a
  worked answer to the case's confound, available where interventions are.
- **[CLAIM-329](../claims.d/CLAIM-329.md), [TERM-071](../terms.d/TERM-071.md).** A "maintained" feature is one whose decoder
  directions at two checkpoints are tied by a jointly trained index, which
  is continuity by resemblance in the state sense. The paper cannot say
  whether a feature at 286B is the 4B feature carried forward or a new one
  in the same place. The reply's §6 question ("Can we distinguish a
  continuing computation from a newly learned replacement with similar
  output behavior?") is not answered by this method.
- **[THEORY-279](../theory.d/THEORY-279.md).** Token-specific detectors giving way to category detectors
  is low-level-first, at the level of features and in large models. It is
  an annotation trend, not a measure of statistical order.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** The features here are constituents measured one at a
  time. The authors list "from individual features to circuits" as future
  work, which is the question's coupling, not yet done.
- **[THEORY-504](../theory.d/THEORY-504.md).** The same fidelity caution applies: reconstruction loss and
  variance explained can disagree, and this paper reports only the first.
- **Account filed.** [THEORY-tmpt45mh](../theory.d/THEORY-tmpt45mh.md) (Proposed).

No instruction for machine-learning practice.

## Limitations

- **Annotation.** The trend from token to abstract features rests on the
  authors' descriptions of top-10 features, which they call subjective.
- **One layer, few checkpoints.** The middle block only, and two or three
  checkpoints per crosscoder, chosen at transitions. Nothing is said about
  the path between them.
- **Integrated gradients, not interventions.** The IEs are approximations;
  the appendix E check compares them with single-feature ablations on the
  top-10 features only.
- **No null for redistribution.** Whether two checkpoints of equal accuracy
  close together in training would also show many checkpoint-specific
  features, from crosscoder training noise alone, is not tested.
- **BLiMP-style minimal pairs** with single-token differences, which the
  authors say limit generality.

## Open questions

- How much of the post-plateau redistribution survives a null of nearby
  checkpoints and different crosscoder seeds?
- Do features that "consolidate" across languages descend from the
  language-specific ones, or replace them? A crosscoder over many closely
  spaced checkpoints, or a test of causal dependence between them, would
  be needed.
- Extended from features to circuits, as the authors propose, would the
  description predict later checkpoints?
