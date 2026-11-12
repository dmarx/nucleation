---
status: Skimmed
paper: LIT-2321
title: 'Liu, Huang, Hu, Zhou and Tan — HypoBench: Towards Systematic and Principled Benchmarking for Hypothesis Generation'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Skimmed on 2026-11-12 from https://arxiv.org/pdf/2504.11524. **Skimmed**
    (abstract, §1, §5 results, §8 limitations read; §§2–4 and appendices
    skimmed or skipped). Read 2026-11-12. A delegated reader drafted the
    reading; quotations were rechecked by script against the downloaded copy,
    and any that did not match were kept as paraphrase without quotation
    marks.
date: '2026-11-12'
summary: >-
  HypoBench defines hypothesis generation as producing natural-language
  explanations of observed phenomena, distinguishes it from research
  ideation, and builds a benchmark of 7 real-world and 5 synthetic task
  families (194 datasets). Real-world tasks are scored by practical utility
  (accuracy of predictions made from the hypotheses, in and out of
  distribution) plus LLM-rated novelty, plausibility and clarity; synthetic
  tasks, whose generating rules are known, are scored by hypothesis
  discovery rate (HDR). Four LLMs × six methods are compared.
---

# NOTE-tmpv5794: Liu, Huang, Hu, Zhou and Tan — HypoBench: Towards Systematic and Principled Benchmarking for Hypothesis Generation

## Contribution

- A definition separating hypothesis generation (explaining observations) from ideation
  (proposing research directions from literature), and putting explanatory power before
  novelty.
- Synthetic tasks with controlled difficulty (number of features, compositional depth,
  outcome noise, distractors, subtlety) giving ground truth for discovery rate.

## Key results

1. Abstract: "HypoBench includes 7 real-world tasks and 5 synthetic tasks with 194 distinct
   datasets."
2. Abstract: "as task difficulty increases, performance significantly drops, with best
   models and methods only recovering 38.8% of the ground-truth hypotheses."
3. §1, p. 2: we define hypothesis generation as generating natural language
   theories/explanations about observed phenomena; ideation, by contrast, "aims to generate
   new research directions, primarily from existing scientific literature."
4. §1, p. 3: "we argue that explanatory power of hypotheses should be the first-order
   consideration."
5. §5, Table 5 (p. 9): Literature + Data has the best OOD accuracy for every model
   (e.g. 78.0 for Qwen). Text: "Literature + Data achieves the best performance,
   highlighting the complementary benefits of integrating both literature knowledge and
   empirical data".
6. §5, Table 7 discussion (p. 10): literature-only hypotheses score highest on plausibility
   and lowest on novelty; "balancing plausibility and novelty is a challenging task for
   hypothesis generation methods, and there is no single method that excels in both
   metrics."
7. §5, synthetic (pp. 10–11): DeepSeek's HDR at base difficulty is 93.8%, falling to 40.0%
   with outcome noise and 38.3% with distractors; at interaction depth 3–4 "the best model
   DeepSeek, in this configuration, only achieves HDR score of 38.8%."
8. §5, key findings list (p. 9): "Model priors substantially influence hypothesis generation quality, with
   models performing significantly worse on counterintuitive settings."
9. §8: novelty/plausibility/clarity ratings had no human validation and "should be
   interpreted as preliminary signals rather than definitive assessments"; HDR is
   "a recall-oriented metric rather than a comprehensive measure of explanatory power".

## Assumptions

- A hypothesis's value can be measured first by the predictive accuracy it affords an LLM
  that reasons from it ("practical utility"), on binary classification tasks.
- LLM-as-judge feature matching approximates whether a ground-truth hypothesis was recovered
  (κ = 0.71 reported for one component).
- Synthetic difficulty dimensions are diagnostic of capabilities relevant to real discovery,
  not predictive of real-world performance (§8 says so).

## Concepts

hypothesis generation vs ideation; inductive vs abductive reasoning; practical utility;
hypothesis discovery rate (HDR); feature discovery rate; relationship correctness;
compositionality / interaction depth; distractor features; subtlety; model priors and
counterintuitive settings.

## Bearing on the record

The LIT records only that it was cited (A14, the exchange's survey of AI-assisted theory
generation). Nothing in the record states a finding from it, so there is nothing to
correct. The curation left A14's survey framing unfiled for want of reading; this reading
supplies the work's own account.

The LIT names no code and no new entry cites [LIT-2321](../literature.d/LIT-2321.md). Bearings found:
- **[LIT-2307](../literature.d/LIT-2307.md)** (Deferred; "From Scientific Observations to Mechanisms: Benchmarking
  Hypothesis Generation"): a sibling benchmark from the same exchange; HypoBench's
  observation-to-explanation definition is the same framing. Leaves open.
- **[LIT-tmpsxqr6](../literature.d/LIT-tmpsxqr6.md)** (Si et al., Deferred) and **[LIT-2329](../literature.d/LIT-2329.md)** (Li et al.): HypoBench
  explicitly separates its task from Si et al.'s ideation (result 3), which matters for how
  the record groups the "AI theory-building" works: Si et al. rate ideas, HypoBench and
  Li et al. score explanations against data.
- **[CLAIM-266](../claims.d/CLAIM-266.md)** (Active; probes that train cannot certify): *leaves open*, but HypoBench's
  own caution that LLM-judged novelty is unvalidated (result 9) is an instance of the
  measurement problem [CLAIM-266](../claims.d/CLAIM-266.md)'s line is about; no optimization against the probes occurs
  here.
- **[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md) / tmp7a7l4 / tmpxq2sb**: no bearing found.

## Limitations

Skimmed: the formal definition (§2) and benchmark construction (§3) were not checked in
detail; appendix figures not read; numeric values in Figures 2–3 read from the text, not
the plots. No venue version located.
