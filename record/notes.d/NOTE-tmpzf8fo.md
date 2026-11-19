---
status: Read
paper: LIT-tmpyyhs0
title: 'Biderman and others 2023 — Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL: https://arxiv.org/pdf/2304.01373 (HTTP 200, 2026-11-19; resolved to
    arXiv v2, 31 May 2023, 34 pages). Kind of copy: arXiv preprint posted by
    the authors (step 5: arXiv); the header carries the ICML 2023 (PMLR 202)
    proceedings line. Date: 2026-11-19. Nothing stopped the fetch. Text
    extracted with pdftotext to dl/text.txt (Table 1, Table 5 and Table 6
    checked against a -layout extraction of the same PDF). Read: abstract,
    §1–§4 in full (suite design, data, architecture, training and
    checkpoints, evaluation, release, the three case studies, conclusion);
    appendices B (v0 to v1 corrections), D (GPU hours), E (full
    configuration), F (design considerations, including F.2 on seeds).
    Skimmed: appendix C (case-study plots and tables). Skipped: appendix A
    (author contributions, glanced), G (benchmark score tables and graphs),
    references. Note: checkpoint and deduplication facts below are as the
    paper states them; the Hugging Face listing itself was not consulted.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp THEORY-1004 THEORY-997 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmpzf8fo: Biderman and others 2023 — Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling

## Contribution

A suite of 16 decoder-only language models, eight sizes from 70M to 12B parameters, each trained once on the Pile and once on a deduplicated Pile, all seeing the same data in the same order, with 154 public checkpoints per model and tools to reconstruct the exact batches seen up to any checkpoint. Its aim is controlled science on training dynamics and scale, not performance. Three case studies show what it enables: retraining the last part of a run with gendered pronouns swapped, a test of whether training order affects memorization, and the emergence over training of the link between term frequency and few-shot accuracy.

## Key results

- **The suite (abstract).** "a suite of 16 LLMs all trained on public data seen in the exact same order and ranging in size from 70M to 12B parameters", with "154 checkpoints for each one of the 16 models".
- **Deduplicated copies (§1, §2.2).** "We train 8 model sizes each on both the Pile" and "the Pile after deduplication"; deduplication by MinHashLSH at threshold 0.87 leaves "approximately 207B tokens".
- **Checkpoints (§2.4).** Saved "at initialization and every 2,097,152,000 tokens (or 1,000 iterations), resulting in 144 checkpoints evenly spaced", plus log-spaced early checkpoints "at iterations {1, 2, 4, 8, 16, 32, 64, 128, 256, 512}".
- **Epochs (§2.4).** All models are trained for about 300B tokens; "The deduplicated Pile only contains 207B tokens, so we run for ≈1.5 epochs on it", which lets users compare "models shortly before the epoch boundary to those slightly after".
- **Exact data per checkpoint (§2.7).** A script "can be used to reproduce the exact dataloader used by our models during training, so that the contents of each batch at each training step can be read out".
- **Schedule (Appendix E, Table 6).** Adam, 1% warmup, cosine decay over 143,000 iterations to "0.1 ∗ optimizer.params.lr"; batch 1024 × 2048 tokens for every size.
- **One run per size (Appendix F.2).** Several seeds were rejected as too costly: "we felt that the way to make the biggest impact with the resources we had available was to train one copy of each model."
- **v0 and v1 (Appendix B).** The suite was retrained with uniform batch size, the extra early checkpoints and a uniform minimum learning rate; the preliminary version was overwritten on March 31, 2023 and models were renamed (e.g. 70M was 19M).
- **Deduplication (§2.6).** "deduplication of our training data has no clear benefit on language modeling performance."
- **Bias intervention (§3.1).** Resuming from a checkpoint "and optimizer state 21B tokens (7%) prior to the end of training" with pronouns swapped reduces measured gender bias, most at larger sizes, with little cost on LAMBADA.
- **Memorization (§3.2).** "a Poisson model fits the data extremely well (Figure 3), indicating that training order has little impact on memorization."
- **Term frequency (§1, §3.3).** "a significant phase change occurs after 65,000 training steps (45% through training): the models with 2.8 billion parameters or more start to exhibit a correlation between task accuracy and occurrence of task-relevant terms"; models below 1B do poorly at the tasks regardless.

## Assumptions

- One architecture recipe across sizes (parallel attention and MLP, rotary embeddings, untied embeddings) chosen for consistency rather than best performance.
- One training run per size and dataset; checkpoint differences mix training progress with position on the learning-rate schedule.
- The Pile as the training set; the standard models see about 300B of its 334B tokens.

## Concepts

- **Model suite with training provenance**: public models, known and consistent data order, checkpoints linked to the exact data seen.
- **Deduplicated vs standard Pile copies**: the same eight sizes trained on each.
- **Counterfactual retraining (intervention)**: resuming a checkpoint on altered data to the end of training.
- **(k, ℓ)-memorization**: a k-token prompt from training data yields the next ℓ tokens exactly (k = ℓ = 32 here).

## Bearing on the record

- **[CASE-tmphsr99](../cases.d/CASE-tmphsr99.md)**: supports its feasibility, with three cautions. The models it names exist: Pythia-70M-deduped and Pythia-160M-deduped, each with checkpoints at step 0, at steps 1–512 log-spaced and every 1,000 steps to 143,000, so eight steps from early to final can be chosen, and the data each checkpoint has seen can be reconstructed. Cautions the design should carry: (1) the learning rate falls on a cosine schedule to a tenth of its peak, so later checkpoints sit at lower learning rates as well as later in training, the schedule confound the case already names; (2) the deduplicated models start a second epoch partway through (by the paper's figures, 207B of about 300B tokens, so at roughly two-thirds of the run), so late deduped checkpoints have seen their data twice; (3) there is one pretraining run per size (F.2), which the case already says. The paper says the bias study resumed from a checkpoint with its optimizer state; it does not say whether optimizer states are public, so the case's fresh-optimizer rule stands.
- **[CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)**: leaves open. The suite is the testbed, not the test; nothing here measures the cost of acquiring new tasks across checkpoints. The term-frequency case is a developmental change late in training (after 45% of the run, at 2.8B and above) that the overconsolidation reading would have to sit beside.
- **[THEORY-1004](../theory.d/THEORY-1004.md), [THEORY-996](../theory.d/THEORY-996.md), [THEORY-997](../theory.d/THEORY-997.md), [THEORY-1005](../theory.d/THEORY-1005.md), [THEORY-1007](../theory.d/THEORY-1007.md)** (and others using Pythia models): this LIT is the suite entry they lacked. Readers of those entries should note the v0/v1 renaming: a 19M or 125M Pythia in older work is today's 70M or 160M, and v0 checkpoints differ.

## Limitations

The case studies are demonstrations, each on few tasks or one benchmark; English only; one seed per configuration; performance is "on par" with OPT rather than state of the art; evaluations in appendix G not checked here.
