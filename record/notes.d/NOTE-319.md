---
number: 319
status: Read
formerly:
- NOTE-tmpq5vw7
paper: LIT-371
title: 'How do language models learn facts? Dynamics, curricula and hallucinations'
version: 1
history:
- version: 1
  date: '2026-09-30'
  note: >-
    Read in full (Full text of arXiv 2503.21676 v2 (24 Jul 2025; the arXiv
    comment says "Accepted at the 2nd Conference on Language Modeling
    (2025)"), 41 pp. Read everything: §§1–5, Limitations, references, and
    Appendices A–G, including all hyperparameter tables (G.1–G.5) and all
    figure captions. Text was extracted with PyMuPDF. The figures are images
    and were read from their captions, axis labels and the text, so numbers
    that are only visible in the plots are not quoted. v1 (27 Mar 2025) was
    not read. `published:` is the v1 date. The paper is already held in the
    Anthology of the SOTA as ANTH-LIT-450 (Active, with a NOTE reading it).
    Dual holding (nucleation ADR-013): nucleation holds it for the
    phases-of-training question behind THEORY-035 and beside LIT-345,
    as a mechanistically measured three-phase trajectory in a language
    model; the anthology holds it for data-schedule and fine-tuning
    practice.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-30'
summary: >-
  'An 8-layer, 44M-parameter decoder-only transformer trained with AdamW
  on synthetic biographies (64k individuals by default) learns factual
  recall in three phases. It first fits the marginal attribute-value
  distribution, then sits on a plateau exactly at the no-knowledge
  baseline, then acquires individual-specific associations. Plateau end
  grows with population as 0.43·N^0.81 (R² = 0.998, N = 4k–256k, 5 seeds).
  Attention patching from post-plateau checkpoints removes the plateau,
  and attention from the recall position to name tokens rises through it,
  so the plateau is when the attention extraction circuit forms. Nothing
  in the three phases is a compression of input information: the last
  phase adds individual-specific information.'
---

# NOTE-319: How do language models learn facts? Dynamics, curricula and hallucinations

## Contribution

The paper adapts Allen-Zhu & Li's synthetic-biography task so that every attribute-value token is a factual-recall prediction and knowledge can be read off a loss. It uses the task to show three things:

- **Three learning phases.** Factual recall is learned in three phases, and the middle one is a plateau during which the attention circuit that extracts attributes from the name forms (§2).
- **A data-distribution trade-off.** Imbalanced individual frequencies shorten the plateau, and a subset-first "warm-up" beats every fixed distribution tried (§3).
- **Hallucination and fine-tuning.** Hallucination on unseen individuals begins with knowledge acquisition, and fine-tuning on new individuals rapidly corrupts stored associations, an effect reproduced in a one-hidden-layer MLP key–value memory (§4).

## Key insight

**Knowledge storage has to wait for the recall circuit.** The last-layer attention must route the error at the attribute token back to the name tokens before the MLP key–value memory can learn individual-specific associations. Until then, "errors are spread across irrelevant tokens" (§2.2), and the loss sits at the best achievable value for a model that knows only marginal statistics.

**The plateau is hidden progress on a different component.** It is not a stall.

**Its length is set by data statistics.** It grows with the number of individuals, which the authors read as supporting a "statistical" account (an individual must be seen several times) over a saddle-point account.

## Assumptions

- **The task (§1.2; App. B.2).** A population of N individuals, each with a unique three-part name and six atomic attributes: birthdate, birthplace, university, major, company, location.
  - There are 25 LLM-generated templates per attribute, 20 for training and 5 for evaluation, split per individual.
  - Sentences are permuted, and a fresh biography is sampled for every sequence, so biographies are never repeated.
  - The name and attribute type always precede the value.
- **Knowledge vs memorisation (§1.1, §1.3).** Knowledge is "information … abstracted from the specific form in which it was encountered". It is measured on held-out templates for seen individuals.
- **Metrics (App. B.3).** Attribute loss is the cross-entropy summed over each attribute value's tokens, averaged over the 6 attributes and the batch. Attribute accuracy requires every value token to be right. The no-knowledge baseline is "the average logarithm of the number of possible attribute values".
- **Model and training (§1.4; Table 1).** Chinchilla-style decoder: 8 layers, d_model 512, d_hidden 2048, 8 heads of size 64, 44M non-embedding parameters. AdamW with β = (0.9, 0.95) and weight decay 0.1. Cosine schedule with no warm-up, peak learning rate 4·10⁻⁴ swept over 10⁻⁴…1.6·10⁻³. Batch 128, sequence length 512, 16k steps, SentencePiece 32k vocabulary, TPUv3.
- **Seeds.** 5 seeds for Fig. 2 and 1 seed elsewhere (App. B.3).
- **Mechanistic prior (§2.2; App. D, Fig. E).** Recall is taken to work as in Geva et al. 2023 and Nanda et al. 2023b: early attention groups name tokens, MLPs act as key–value memory, and the final attention extracts the attribute. The attention analysis "relies on simplified mental models" and is "purely correlational" (App. D.2).

## Key results

- **Three phases (§2.1; Fig. 2).**
  1. A very short phase learning the attribute-value marginal, ending exactly at the no-knowledge baseline.
  2. A plateau at that baseline, with near-zero attribute accuracy.
  3. "Knowledge emergence": the loss goes below the baseline, and accuracy leaves zero.
  - Plateau end vs population: y = 0.43·x^0.81, R² = 0.998, over N = 4k–256k, 5 seeds.
  - The pattern is qualitatively robust to learning rate, weight decay (0.01–1), batch size (32–512), model size (50M/150M/400M) and replacing attention by Hawk recurrence (Fig. C).
- **Attention patching (§2.2; App. D.1; Figs. 3, D).**
  - Setup: train a reference model; restart from the same initialisation, feeding the reference checkpoint's attention patterns (the softmax of the logits, with gradients stopped) so that only token-wise computations learn.
  - Patterns from later reference checkpoints give lower final loss, and most of the improvement happens during the plateau. "The plateau disappears when providing the model with learned attention patterns (i.e. post-plateau patterns)."
  - Patterns from steps 500 and 1k are "significantly worse than the pre-learning ones".
  - Freezing attention at a checkpoint (start = reference step) gives the same conclusion.
- **Attention signatures (§2.2; App. D.2; Fig. F).**
  - At the first attribute-value token, attention to name tokens relative to template text is low in phase 1 and rises through the plateau.
  - The first-layer name-grouping circuit forms "within a few hundred steps".
  - Attention entropy falls progressively from uniform, "with a slight increase in sharpness starting around the end of the plateau".
  - The authors state that the results "do not provide any mechanistic insights regarding how models acquire individual-specific knowledge".
- **Data distribution (§3.1; Fig. 4; App. E).**
  - Individuals are sampled ∝ i^(−α) with α ∈ {0,…,1}, on a 16k-step budget.
  - The plateau shortens as α rises up to an optimum of 0.6–0.8 for every N. Beyond that, "excessive increases are detrimental, likely due to overfitting".
  - The α minimising final attribute loss grows with N and with shorter budgets.
  - A "celebrities" distribution gives comparable benefits (App. E.2).
- **Warm-up schedule (§3.2; App. E.2).**
  - Training uniformly on a subset first, then on all individuals, improves final knowledge most when N is large (Fig. 4 right, Fig. J).
  - For 128k individuals the grid optimum lies at the grid edge.
  - Control: a uniform run on 83k individuals gets 97.72% on them, i.e. 63.26% measured on 128k, against 94.92% for the warm-up.
- **Hallucination (§4.1; App. F.2; Fig. M).**
  - On 16k held-out individuals, the loss rises *above* the no-knowledge baseline as soon as the knowledge phase begins: the model becomes confidently wrong.
  - Its max-probability is lower and its entropy higher than on seen individuals, so hallucinations "can be detected to some extent".
- **Fine-tuning (§4.2; App. F; Figs. 5, N, P).**
  - Setup: fine-tune the default model at a constant learning rate of 3·10⁻⁵ on 1k–16k new individuals.
  - Pre-training attribute loss collapses within "the first few hundred steps", while new knowledge comes slowly. Some pre-training accuracy survives even when the loss nears the baseline.
  - Replay (weights 2…1/32) "partially mitigates the final performance drop, but not the initial decline".
  - Attention patterns stay "remarkably stable" (Fig. O).
  - A 256-unit one-hidden-layer ReLU MLP on 8,192 random key–value pairs (30 classes) reproduces the pattern (App. F.4), so the authors locate the damage in the feed-forward associative memory.
  - Fine-tuning on rare *seen* individuals is net-positive: about 50% → about 70% accuracy (Fig. P).
- **Sequential groups (App. F.5).**
  - New groups get easier to learn over training, which the authors attribute to better attention (Fig. W).
  - Forgetting is faster than learning.
  - Frequent distribution changes early, at a high learning rate, reduce later plasticity.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Factual-recall learning has three phases (marginal statistics → plateau at the no-knowledge baseline → knowledge acquisition) | experiment | Fig. 2, 5 seeds; Fig. C ablations, one seed each, qualitative |
| C2 | Plateau length grows nearly linearly with population, favouring a statistical over a saddle-point explanation | experiment (fit) + inference | Fig. 2 right: exponent 0.81; the inference to "statistical" is argued, not tested against a saddle model |
| C3 | The plateau is when the attention-based recall circuit forms; lack of this circuit is what stalls learning | experiment (intervention) + correlational signature | attention patching (Figs. 3, D) plus attention-to-name curves (Figs. 3, F); the credit-assignment mechanism itself is argued (§2.2, §5) |
| C4 | Imbalance shortens the plateau (optimum α 0.6–0.8) and the final-loss-optimal α grows with population / shrinks with budget | experiment, single seed | Fig. 4, grid α ≤ 1 |
| C5 | Plateau length tracks the most frequent individuals; acquisition speed tracks the least frequent | informal argument | §3.1; not isolated experimentally |
| C6 | A subset-first warm-up beats the best fixed distribution | experiment, single seed, tuned in the evaluation setting | Fig. 4 right, J–L; 83k control |
| C7 | Hallucinations emerge with knowledge and are less confident than grounded predictions | experiment | Figs. 5 left, M |
| C8 | Fine-tuning on new individuals rapidly corrupts pre-trained associations, mainly in feed-forward memory | experiment + toy-model analogue | Figs. 5, N, O, Q, R; attention stability rules out one alternative |
| C9 | "Data used before the end of the plateau is not retained in the final model" (§5) | assertion | not directly measured; it is a reading of the three-phase picture |
| C10 | Grokking may be networks first finding a memorising "shortcut" before the circuit and abandoning it under regularisation (§5) | speculation | no experiment |

## Method

1. Generate the synthetic population and templates.
2. Track attribute loss and accuracy on held-out templates against the entropy baseline.
3. Run the attention-patching intervention through a twin architecture, with stop-gradient on the attention scores and the optimiser reset at patch start.
4. Track per-layer attention mass: last name token → name tokens, and first attribute token → name vs text. Also track attention entropy normalised by log t.
5. Sweep the sampling distributions (power law, celebrities, warm-up, sequential groups).
6. Fine-tune with and without replay, and build a toy MLP key–value analogue.

## Concepts

- **Attribute loss / attribute accuracy; no-knowledge baseline.** The entropy of the attribute-value marginal.
- **Knowledge vs memorisation.** Recall across held-out phrasings vs recall of seen sequences.
- **Name-grouping circuit, extraction circuit, key–value (MLP) memory.**
- **Attention patching.** Imposing a reference model's attention patterns during training.
- **Inverse power-law, celebrities and warm-up distributions.**
- **Hallucination.** Attribute loss above the no-knowledge baseline on unseen individuals, i.e. overconfidence.

## Connections

- **[THEORY-035](../theory.d/THEORY-035.md) and [LIT-324](../literature.d/LIT-324.md) (IB account).** Orthogonal to all three IB claims. The paper measures no mutual information and no information plane, and it does not vary the gradient noise as such (batch size is ablated only qualitatively). But its phase structure is instructive for the question "is the later phase a simplification?"
  - **Phase 1** fits the marginal p(value | attribute type), a low-information predictor.
  - **Phase 3** *adds* information: the network must come to distinguish individuals and store their specific values.
  - Read in IB terms (my reading, not the paper's), the representation at the recall position must *gain* information about which individual is named for I(T;Y) to rise above the baseline. For atomic facts with no redundancy, a sufficient statistic of the name for the attributes is close to the identity itself, so there is little to compress.
  - The only "sharpening" measured is attention entropy falling, which is a property of routing, not I(X;T).
  - The paper's rhetorical line that learning "acts as a lossy compression algorithm" (introduction) is not an IB claim, and nothing is measured under it.
- **[LIT-345](../literature.d/LIT-345.md) (Nanda et al., grokking), [NOTE-283](NOTE-283.md).** The two three-phase pictures invert each other.
  - *Nanda:* memorisation → circuit formation → cleanup. The circuit forms while train loss is already low, and the last phase is a *simplification of the weights* (weight norm falls, Fourier sparsity rises) that coincides with generalisation.
  - *Zucchet:* marginal statistics → circuit formation (loss flat) → storage. The circuit forms *before* the individual-specific learning it enables, and the last phase is *acquisition*, not simplification.
  - What they share is a flat loss hiding circuit formation, exposed by a mechanistic measure: restricted/excluded loss there, attention patching and attention mass here.
  - Zucchet's §5 speculates that grokking networks find a memorising shortcut before the circuit and abandon it under regularisation. That is compatible with [NOTE-283](NOTE-283.md)'s reading, but it is not tested here.
- **[LIT-341](../literature.d/LIT-341.md) (Power et al.).** Named only through §5's speculation. Unlike grokking, Zucchet's plateau is a *training*-loss plateau with no memorisation preceding it, and its length depends on data frequency rather than on regularisation (weight decay 0.01–1 leaves the pattern intact; Fig. C).
- **Saxe et al. 2018 (this batch).** Both papers show that a two-phase-looking trajectory can arise from something other than the proposed mechanism. The gradient-SNR drift/diffusion transition that Saxe et al. find generic is not measured here.
- **Anthology of the SOTA.** Held as [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md) (Active; read in the anthology NOTE on it). The anthology's related theory and practice (per [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md): [ANTH-THEORY-028](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-028.md), [ANTH-SOTA-267](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-267.md)) were not read here.

## Bearing on the record

- **For [THEORY-035](../theory.d/THEORY-035.md).** Nothing for or against the IB account directly. It is a counterexample only in the weak sense that a well-instrumented three-phase trajectory in a real transformer needs no compression phase at all: the late phase is information acquisition.
- **For the phases question.** This paper establishes a *circuit-first, storage-second* phase structure in a 44M transformer on synthetic factual recall. It is measured by the attribute loss against an exact entropy baseline, with an attention-patching intervention and attention-mass signatures. The later phase is not a simplification of weights, function or representation. If any simplification occurs it is in attention routing (entropy falls), and that is not IB compression of I(X;T). The phase boundaries are set by data statistics (population size, frequency skew), not by an optimiser-noise transition.
- **ML practice.** Held in the anthology for that (data warm-up, fine-tuning for knowledge). See corrections: the anthology's power-law exponent claim needs fixing there.

## Limitations

- **Synthetic setting.** Synthetic biographies, 44M parameters by default (ablations to 400M), 16k steps. Nothing is measured on natural text; §5's generalisation to "natural text and its multi-task nature" is speculation.
- **Single seeds.** Everything beyond Fig. 2 is single-seed, including the curriculum comparisons, which are also tuned on the setting they are evaluated in. The warm-up's best cell for 128k individuals lies at the edge of its grid.
- **Inferred mechanisms.** The credit-assignment mechanism (errors not reaching the name tokens) is inferred from the patching result and from correlational attention statistics. Gradient flow to the name tokens is not measured. The paper says its analysis "ignores the impact of the values".
- **Saddle vs statistical.** The account is decided by the population scaling alone, with no loss-landscape measurement.
- **Headline wording.** The abstract's "imbalanced distributions lead to shorter plateaus" omits the overfitting cost above α ≈ 0.8. The intro's "data curricula benefit (self-)supervised learning" rests on one warm-up family in one task.
- **Slips.** App. D's Fig. D caption labels two panels "(right)". App. B.2 cites "Section 1.1" (which has no such material) alongside App. F.5 for time-dependent distributions. Fig. O's caption reads "remain remarkably relatively".

## Open questions

- Does gradient flow from attribute tokens to name tokens, measured directly, rise through the plateau as the credit-assignment account requires?
- Is the plateau length's population scaling (exponent 0.81) robust across seeds and model sizes, and does it bend toward the linear "statistical" prediction at larger N?
- Does the circuit-first ordering hold on natural corpora, where population size is not defined? The authors' suggestion that pre-plateau data "is not retained" would be testable by ablating early data in a real pre-training run.
- In IB terms, what does I(X;T) at the recall position do across the three phases under a network-intrinsic noise model? The prediction would be a rise in phase 3, the opposite of a compression phase.

## Corrections to the seeded skim

- There was no nucleation seed or dossier. Disagreements with the anthology's [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md) and its NOTE (anthology [NOTE-199](NOTE-199.md), the reading of [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md)), reported per nucleation [ADR-013](../decisions.d/ADR-013.md) and not fixed:
- **"Optimal fixed imbalance is an inverse power law with exponent between 1 and 2" ([ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md) takeaways; the NOTE's Key results) is not in the paper, and it contradicts the paper.**
  - The swept exponent is α ∈ {0, 0.2, 0.4, 0.6, 0.8, 1} (Table G.4), where α = 1 is Zipf, so nothing above 1 was tried.
  - The text says "the optimal α minimizing plateau length lies between 0.6 and 0.8, irrespective of the population size" (§3.1).
  - The α minimising *final attribute loss* rises with population and with fewer steps (Fig. 4 middle). Its values are only shown in the plot.
- **The NOTE's "optimal fixed imbalance … roughly independent of population size" conflates two optima.** It is the *plateau-minimising* α that is population-independent (0.6–0.8). The *final-loss-minimising* α is not; it grows with population (§3.1, Fig. 4).
- **"Start imbalanced and flatten" ([ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md); R1) is a loose description of what was tested.**
  - The "warm-up" trains *uniformly on a subset* of individuals (indiv_warmup ∈ {2k…32k}) for epochs_warmup ∈ {1, 2, 4, 8} epochs, then uniformly on everyone (App. B.2, G.4).
  - It is not a skewed distribution annealed to flat, and no α schedule was run.
  - The warm-up also leaves most individuals unseen during the warm-up, so it is closer to "shrink the population, then grow it". The paper's own App. E.2 check makes this point: a uniform run on 83k individuals scores 97.72% on them, which is 63.26% on 128k, against 94.92% for the warm-up.
- **The anthology's claims that "plateau length is set by the frequency of the *most* common individuals" and "acquisition speed … by the *least* common" are presented as measured. They are the paper's argument (§3.1, "we can already develop an intuition").** What was measured is plateau end and final loss as functions of α, N and the step budget (Fig. 4). Neither frequency dependence is isolated experimentally.
- **"Plateau length grows almost linearly".** The paper says so (§2.1). Its own fit is y = 0.43·x^0.81 (Fig. 2 right), which is sublinear.
- **Five seeds applies to Fig. 2 only.** App. B.3: "we … ended up using a single seed for the rest of the experiments". The NOTE's C3–C6 support columns do not say that the curriculum, hallucination and fine-tuning results are single-seed.
- **R3, "Do not add knowledge by fine-tuning", omits the paper's counter-result.** Fine-tuning on rare individuals that were *seen in pre-training* raises their accuracy from about 50% to close to 70%, without the fast collapse (App. F.3, Fig. P; also the alternating-groups Fig. V). Only *new* individuals cause the rapid corruption. Replay "partially mitigates" the collapse (§4.2).
- **"Hallucinations arrive exactly when knowledge does."** The main text says "simultaneously" (§4.1). App. F.2 says they "appear shortly after the plateau phase". The model is *less* confident on unseen individuals than on seen ones (Fig. M), which the anthology does not mention and which bears on its R4.
- **The anthology NOTE's C1 support says "measured across population sizes, five seeds".** That is correct. The robustness ablations (learning rate, weight decay 0.01–1, batch 32–512, model size 50M/150M/400M, attention vs Hawk/RG-LRU recurrence; Fig. C) are qualitative, one seed each.
- Otherwise the anthology matches the text, including the patching result, the early attention patterns being worse than the untrained ones, the attention to name tokens rising through the plateau, the fine-tuning asymmetry and the "rare case where a curriculum helps" framing.
