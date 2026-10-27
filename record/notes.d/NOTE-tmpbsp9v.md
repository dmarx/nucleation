---
status: Read
paper: LIT-tmptgo43
title: 'Dunefsky, Chlenski and Nanda — Transcoders find interpretable LLM feature circuits'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF of 2406.11944v2 (6
    November 2024, the NeurIPS 2024 camera-ready, 29 pages), text extracted
    with pdftotext. Read: the abstract, §§1–7 with the limitations and
    impact statements, the references, and Appendices A–H (assets, compute,
    SAE details, the derivations of D.1–D.5 with Algorithms 1 and 2,
    training details, the interpretability comparison, the greater-than
    details, and all nine case studies with Tables 3 and 4). Figures 3–5
    are plots whose points could not be read reliably from the extracted
    text; their content is taken from the captions and the text. Figure 6
    (feature dashboards) is described from its caption.
date: '2026-10-26'
summary: >-
  A transcoder replaces one MLP sublayer with a wide sparse ReLU MLP trained
  on its input–output pairs. With attention patterns frozen and LayerNorm
  linearized, the attribution between two transcoder features factors into
  the earlier feature's activation times the input-invariant dot product of
  its decoder with the later feature's encoder, so circuits through MLPs can
  be read partly off the weights. On GPT2-small, Pythia-410M and Pythia-1.4B
  transcoders sit on or above the SAE sparsity–loss frontier, under one
  learning rate and one seed; in nine blind case studies on GPT2-small the
  method recovered the feature's meaning in five, mostly in two and failed
  in two.
---
<!-- inactive-ok-file: CLAIM-tmpwr001 THEORY-022 THEORY-802 — Proposed; the record's own claim and neighbouring accounts this reading bears on, cited as open -->
# NOTE-tmpbsp9v: Dunefsky, Chlenski and Nanda — Transcoders find interpretable LLM feature circuits

## Contribution

It makes MLP layers passable for feature-level circuit analysis. A sparse
autoencoder (SAE) on an MLP's input or output gives interpretable features,
but the map between pre-MLP and post-MLP SAE features still runs through
every neuron's nonlinearity, so any attribution is local to one input. A
transcoder learns the MLP's map itself as a sparse sum of features, and
then the connection between two features has a part that does not depend
on the input at all. The authors' own claim: "the only such approach that
cleanly disentangles input-invariant information from input-dependent
information".

## Key insight

Replace what the MLP does, not what it outputs. If a sparse ReLU layer
stands in for the MLP, then everything between one feature's output and
a later feature's input is linear, once attention patterns and LayerNorm
scales are held fixed, and the attribution is (activation) × (decoder ·
encoder). The second factor is a weight of the replacement model. It
says how one feature would drive the other on any input, and it can be
inspected without running a prompt.

## Assumptions

- **Architecture (Eqs. 3–5).** z(x) = ReLU(W_enc x + b_enc), TC(x) =
  W_dec z(x) + b_dec, with x the MLP input and the loss
  ‖MLP(x) − TC(x)‖² + λ₁‖z(x)‖₁. Width is 32 × d_model throughout (App. E).
- **The factorization (Eq. 7, App. D.2)** holds when the later feature is
  active (so its ReLU can be dropped), its encoder bias is ignored, and the
  transcoder is substituted for the MLP, "if the layer l transcoder is a
  sufficiently good approximation". It is an identity of the replacement,
  not of the original model.
- **Attention (Eq. 8, App. D.3)** is handled by freezing the QK scores at
  their values on the prompt and attributing only through OV circuits: "this
  does prevent us from understanding the extent to which transcoder
  features contribute to phenomena such as QK composition".
- **LayerNorm** is treated as multiplication by a constant estimated from
  the ratio of pre- and post-norm norms (App. D.4).
- **Training (App. E).** Adam, learning rate 2 × 10⁻⁵ for SAEs and
  transcoders alike, chosen by a sweep on transcoders; λ₁ swept separately
  for each; 60M tokens of OpenWebText in contexts of 128; one seed (42),
  so all runs saw the data in the same order; no neuron resampling. SAEs
  for the fidelity comparison are trained on MLP outputs, the SAE for the
  interpretability comparison on MLP inputs.

## Key results

- **Fidelity and sparsity (§4.2, Fig. 3).** Transcoders and MLP-output SAEs
  on GPT2-small layer 8, Pythia-410M layer 15 and Pythia-1.4B layer 15,
  evaluated on the same 3.2M tokens: "In all cases, transcoders are equal
  to or better than SAEs. In fact, the gap between transcoders and SAEs
  seems to widen on larger models." The authors add that the shared
  learning rate "might not be optimal for SAEs" and that other
  hyperparameters "could have allowed SAEs to surpass transcoders".
- **Interpretability (§4.1, Table 1, App. F).** 50 random features each
  from a Pythia-410M layer-15 transcoder (L0 44.04, 3.35 nats) and an
  MLP-input SAE (L0 47.85, 3.36 nats), shuffled and rated blind from
  top-activating examples: 41 / 8 / 1 interpretable / maybe /
  uninterpretable for the transcoder, 38 / 8 / 4 for the SAE; 6 and 16 of
  the interpretable ones were "context-free". One rater (the text says
  "we"), no inter-rater check.
- **Blind case studies (§5.1, App. H, Table 4).** Nine features of the
  GPT2-small layer-8 transcoder were interpreted from circuits and
  de-embeddings without seeing prompt tokens; seven of them under the
  stricter "restricted" rule that also forbids input-dependent layer-0
  information. Outcomes by Table 4: five successes (the semicolon-in-
  citations feature tc8[355], "All", "told/said in an interview",
  "though/although", a largely uninterpretable Cyrillic feature), two
  mostly successes ("caught", "not offering things") and two failures (a
  local-context feature, and "biology" for "scientific subjects").
- **Greater-than (§5.2, Figs. 4–5).** On the 100 prompts "The war lasted
  from 17YY to 17", the transcoder confirms Hanna et al.'s attribution to
  MLP10 through head 9.1. The three highest-variance MLP10 features fire on
  ranges of YY and boost the logits of later years, and their
  input-invariant de-embeddings through head 9.1 pick out two-digit tokens.
  Keeping only the top k transcoder features outperforms keeping the top k
  neurons for k < 24; the 24th feature, tc10[5315], boosts all years
  equally and drops performance, and without it a handful of features
  recovers most of the probability-difference metric. The full transcoder
  does not recover the original model's performance.
- **The "caught" case (App. H.1.2)** shows the replacement diverging: in
  the model the feature fires at 19.97 on "He was caught" and 0.81 on "He
  caught the ball"; with all earlier MLPs replaced by transcoders, 16.45
  and 9.00. "Transcoders were not accurately modeling this particular
  nuance."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With frozen attention and linearized LayerNorm, the attribution of an active transcoder feature to a later one is its activation times an input-invariant decoder–encoder dot product | strong (derivation, under the stated approximations) | Eq. 7, App. D.2; re-derived in [THEORY-tmp9ii0y](../theory.d/THEORY-tmp9ii0y.md) |
| C2 | Transcoders are on or above the SAE sparsity–fidelity frontier on GPT2-small, Pythia-410M and Pythia-1.4B | moderate (one layer per model, one learning rate tuned on transcoders, one seed) | §4.2, Fig. 3 |
| C3 | Transcoder features are about as interpretable as SAE features | weak to moderate (50 features each, one model and layer, one rater) | §4.1, Table 1 |
| C4 | Circuit analysis with transcoders can recover a feature's meaning without seeing the prompts | moderate as existence (5 of 9 full successes) | §5.1, App. H, Table 4 |
| C5 | MLP10 of GPT2-small computes greater-than mainly through a few features that fire on ranges of years and boost later ones | moderate | §5.2, Figs. 4–5 |
| C6 | Transcoders are "an improvement over" SAEs on MLP outputs for feature-level interpretability of MLPs | weak as a general claim | Conclusion; rests on C2–C3 |

## Method

Greedy path finding (Algorithm 1): from a target feature at one token, list
the attribution of every earlier transcoder feature, every attention head
(through its OV circuit at each source token, giving a new "pulled-back"
feature vector) and the embedding; keep the top N; recurse L times; merge
the paths into a graph without double counting (Algorithm 2). Error nodes
can be added following Marks et al.; the paper does not use them.
De-embedding a feature, W_Eᵀ f_enc, scores every vocabulary token by its
direct effect on the feature.

## Concepts

- **Transcoder**: a sparse ReLU MLP trained to map an MLP's input to its
  output; "predicting future activations" and "MLP stretchers" in earlier
  notes.
- **Input-invariant / input-dependent**: the weight factor f_dec · f_enc
  and the activation factor of an attribution.
- **De-embedding**: W_Eᵀ f_enc, the direct effect of each token embedding on
  a feature.
- **Blind case study**: interpreting a feature from circuits without seeing
  the tokens of its prompts; "restricted" adds a ban on input-dependent
  layer-0 information.

## Connections

It builds on Elhage et al.'s framework ([LIT-tmp9dono](../literature.d/LIT-tmp9dono.md): frozen QK, OV circuits,
the residual stream as a sum), on Dunefsky and Cohan's observable propagation for the
backward feature vectors, on Marks et al.'s sparse feature circuits ([LIT-tmp5b0z9](../literature.d/LIT-tmp5b0z9.md)) for the
error-node idea, and on Hanna et al. for the greater-than circuit. Its
interpretability rating follows Bricken et al. ([LIT-tmpn9ui7](../literature.d/LIT-tmpn9ui7.md)), and the
sparse autoencoders it is measured against are those of Bricken et al.
and their scale-up ([LIT-tmp8w8uj](../literature.d/LIT-tmp8w8uj.md)). Gemma
Scope ([LIT-611](../literature.d/LIT-611.md), read in [NOTE-482](NOTE-482.md)) trained transcoders on Gemma 2 2B and
found them worse than MLP-output SAEs at fixed L0, "reversing the GPT-2
Small finding of Dunefsky et al.", with implementation error among the
causes it lists. Ameisen et al. ([LIT-tmpsuo6l](../literature.d/LIT-tmpsuo6l.md)) take the attribution rule
from here, "essentially the same as that of Dunefsky et al.", and extend it
to cross-layer transcoders.

## Bearing on the record

- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** The paper is a case of the claim's distinction made
  technical. A feature recovered from activity (an SAE latent) does not by
  itself say what it does to later features; a transcoder feature comes
  with its downstream weights. But the weights are those of a replacement
  trained to match outputs, and the "caught" case shows the replacement
  computing a feature differently from the model. Recovering a unit is not
  recovering the mechanism that uses it.
- **[THEORY-802](../theory.d/THEORY-802.md) and [QUESTION-234](../questions.d/QUESTION-234.md).** The dictionary fixes the decomposition
  into units, and the factorization is relative to it. The paper does not
  ask whether another dictionary with the same fidelity would give other
  circuits.
- **[LIT-611](../literature.d/LIT-611.md) / [NOTE-482](NOTE-482.md) / [THEORY-504](../theory.d/THEORY-504.md).** [NOTE-482](NOTE-482.md)'s transcoder result and C2
  here disagree, on different models. Neither settles which holds where.
  [THEORY-tmptjiep](../theory.d/THEORY-tmptjiep.md) is scoped to the three models measured here, so the two
  do not contradict.
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** Transcoder weights are one candidate for the
  "circuit-only" description the question compares against: a
  checkpoint's circuit as a weighted graph over features. The paper trains
  on one checkpoint per model and does not say how features would be
  matched across training.
- **Accounts filed.** [THEORY-tmp9ii0y](../theory.d/THEORY-tmp9ii0y.md) (Active): the factorization, as a
  derivation under its approximations. [THEORY-tmptjiep](../theory.d/THEORY-tmptjiep.md) (Active): the SAE
  comparison, as measured.

The method is interpretability practice, not an instruction for training
models; the anthology may want it as a reading (`anthology-candidate`).

## Limitations

- **Attention is frozen.** The method attributes through OV circuits only
  and says nothing about why a head attends where it does. The authors list
  this first.
- **The comparison with SAEs is thin.** One layer per model, one seed, a
  learning rate tuned for transcoders and reused for SAEs, and a single
  blind rater for 100 features. Gemma Scope's reversal on Gemma 2 2B is
  not discussed (it came later).
- **The replacement is not the model.** The factorization is exact only for
  the transcoder. Transcoder error is not measured in the circuits, and the
  error nodes the method allows are not used.
- **Counting slips.** §5.1 says "nine blind case studies" and then "six of
  the eight case studies that we carried out were restricted blind case
  studies"; Tables 3 and 4 list nine, seven of them restricted. In App.
  H.2.2, "21 features activating above a threshold" means 21 prompts. In
  App. H.1.2 the second input analysed is (6299, 39) twice where the
  heading names (817, 63). The introduction cites Hanna et al.'s
  greater-than paper as [26], which is their "Have Faith in Faithfulness";
  §5.2 cites it correctly as [25].

## Open questions

- Does the transcoder–SAE comparison hold at matched learning-rate sweeps
  and several seeds, and why does it reverse on Gemma 2 2B?
- How much of a circuit's attribution sits in transcoder error, prompt by
  prompt?
- Can the QK side be brought into the same factored form?
