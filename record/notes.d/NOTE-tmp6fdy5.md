---
status: Read
paper: LIT-tmppcswh
title: 'Pan and others 2023 — What In-Context Learning "Learns" In-Context: Disentangling Task Recognition and Task Learning'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2305.09731 (HTTP 200, 601 KB PDF, arXiv
    v1 of 16 May 2023). Kind of copy: arXiv preprint (step 5, first place to
    look). Date: 2026-11-19. Nothing stopped the fetch. Text extracted with
    pdftotext -layout to dl/text.txt. Read: the whole paper (abstract,
    §§1-6, Limitations, Appendices A-C text and prompt tables). The venue is
    not stated in the copy read. Skipped: references; the appendix figures
    were read by caption only (per-task-type and per-label-type breakdowns).
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-697 CLAIM-tmp1l2s7 THEORY-614 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp6fdy5: Pan and others 2023 — What In-Context Learning "Learns" In-Context: Disentangling Task Recognition and Task Learning

## Contribution

The paper splits what demonstrations do into two abilities and gives a control for each. Task recognition (TR) identifies the task from the input distribution and the label distribution, without using which label goes with which input, and applies the model's pretrained priors. Task learning (TL) acquires an input–label mapping not seen in pretraining. Three settings separate them (§2, Figure 1): GOLD (natural prompt, correct labels; TR + TL); RANDOM (natural prompt, labels sampled uniformly from the label set, as in Min et al. 2022; TR only); ABSTRACT (minimal prompt, labels replaced by numbers, letters or symbols under a fresh random 1–1 mapping per prompt; TL only). Each is traced across model size and number of demonstrations.

## Key results

- §4.1, Figure 2. RANDOM is flat in model size and in number of demonstrations, yet above chance even for the smallest models: "Task recognition is a broader capability across" scales, with about 10 points over chance for GPT-3 ada and 5 for OPT-350M at 8 examples. In the authors' summary, TR does not "scale with increasing parameters or examples."
- §4.1, Figure 2. ABSTRACT rises with both. Small models stay near flat whatever the number of examples; "With only 16 examples, OPT-66B and davinci are" able to match GOLD under a new label mapping. The authors conclude "TL is only enabled by scales and further improves" with more demonstrations.
- §1. With the largest models and 16 or more examples ABSTRACT beats RANDOM, "paradigm shift in in-context learning at scale." The GOLD–RANDOM gap, small for small models (agreeing with Min et al.), widens with size and examples.
- §4.2, Figure 3. The TL trend holds for number, letter and symbol labels; numbers and letters do better than symbols.
- §4.2, Figure 4. On harder tasks (NLI vs sentiment) ABSTRACT scales less, "suggesting that the model relies" more on natural prompts and pretrained priors.
- Limitations. The authors concede that TL may itself be mapping demonstrations back to pretrained concepts: "these mechanisms could be considered an advanced" form of task recognition.

## Assumptions

- RANDOM removes TL and leaves TR; ABSTRACT removes TR and leaves TL. Neither holds exactly: abstract symbols carry pretraining biases (randomized per prompt to cancel them), and random labels still give the label space.
- 16 English classification datasets, single-token answers, three prompt templates each; GPT-3 (non-instruction), LLaMA 7–65B, OPT 350M–66B.
- Sample-based evaluation, with fresh demonstrations per test example (150 examples per dataset for GPT-3, 1,350 for the others).

## Concepts

- **Task recognition (TR)**: performance from the input and label distributions alone, through pretrained priors.
- **Task learning (TL)**: performance from a new input–label correspondence given only in context.
- **GOLD / RANDOM / ABSTRACT**: the three label manipulations that isolate TR + TL, TR and TL.

## Bearing on the record

- **[CASE-tmphsr99](../cases.d/CASE-tmphsr99.md)** (supports its in-context arm, with a caution). These are the controls A56 named. They need a natural label space and a pretrained prior, which the CASE's synthetic families (parity, associative retrieval, two-hop composition) mostly lack: for a family with no pretrained prior, ICL success is TL by construction, and RANDOM is uninformative. Pan's result also predicts that TL, unlike TR, should depend on scale and number of examples; at Pythia-70M/160M it may be near absent, so the in-context arm risks a floor.
- **[THEORY-496](../theory.d/THEORY-496.md)** (qualifies). The small gold–random gap holds for smaller models and fewer examples, as Pan et al. replicate. It widens with model size and with demonstrations, so [THEORY-496](../theory.d/THEORY-496.md)'s finding that label correctness contributes little is scale-dependent. This is the test on unlearned correspondences that [THEORY-496](../theory.d/THEORY-496.md) says was missing, and it finds them learned at scale.
- **[QUESTION-024](../questions.d/QUESTION-024.md)** (premise). RANDOM shows a task frame recovered from demonstrations without accurate input–label examples. That is the first half of the question for lexical classification tasks, not for a stance or a pragmatic frame, and transfer across wordings is not tested.
- **[THEORY-614](../theory.d/THEORY-614.md)** (qualifies). TR is the latent-concept story the authors attribute to Xie et al.; TL at scale is what it does not cover, so the Bayesian concept-selection reading describes small models better than large ones.
- **[CLAIM-697](../claims.d/CLAIM-697.md)** (supports, as an instance). The number of demonstrations is a budget whose payoff depends on the route: flat for TR, rising for TL, and rising only in large models. A disposition elicited by context is conditional on both the budget and the model.
- **[CLAIM-tmp1l2s7](../claims.d/CLAIM-tmp1l2s7.md)** (supports the need for a declared interface). Crediting a model with learning a task in context requires excluding what it recognizes from pretraining; ABSTRACT is such an interface restriction. It does not test the claim's divergence of frontiers.
- **[CLAIM-118](../claims.d/CLAIM-118.md)** (qualifies). What the context supplies works through two routes: selecting a prior the interpreter already has (TR) and carrying new information (TL). Only the second is new signal in the full sense.

## Limitations

- Classification only, single-token labels, English.
- OPT curves have high variance, which the authors suspect comes from under-training; GPT-3 is evaluated on 150 examples per dataset.
- The operational split is not mechanistic, and the authors concede TL may be a form of recognition.
- No instruction-tuned models; the largest OPT (175B) was not run.
