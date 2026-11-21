---
status: Read
paper: LIT-tmpi3ty1
title: 'Sun, Pickett, Nain and Jones — Transformer layers as painters'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 2407.09298v4 (12
    Feb 2025; the AAAI 2025 paper with appendix): all body text and
    Appendices A.1–A.9; figures by caption and surrounding text. Running
    notes on the branch claude/readers/layers-painters (ADR-108).
    Quotations the filing leans on rechecked by the filer by script
    against the downloaded text.
date: '2026-11-21'
summary: >-
  Frozen transformers have beginning, middle and ending layers; the middle
  shares a representation space but does different work: skipping,
  reordering or running middle layers in parallel degrades gracefully,
  replacing them with copies of one layer is catastrophic, and math and
  reasoning depend most on order. Pythia is less robust than Llama2 and
  Mistral.
---
<!-- inactive-ok-file: ADR-108 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpcvuyr — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmpekh8j: Sun, Pickett, Nain and Jones — Transformer layers as painters

## Contribution

A broad set of execution interventions on frozen models; cosine-similarity evidence for three classes of layers; task-dependence of order.

## Key results

1. **Shared space** (§3.1): "the middle layers seem to share a common representation space".
2. **Early layers** (Fig. 2): "Skipping early layers has a catastrophic effect, while the model is much more robust to skipping middle layers".
3. **Copies fail** (§3.3): "sharing weights among middle layers is catastrophic, indicating that the middle layers are performing different functions".
4. **Order** (§3.6): "Mathematical and reasoning tasks are more order dependent than 'semantic' tasks."
5. **Summary** (§5): three classes of layers, and "The middle layers have some degree of uniformity (but not redundancy)".
6. **Family differences** (A.5): "Pythia is less robust to modifications, especially modification of the Layer order".

## Assumptions and concepts

Cosine similarity and skip-robustness as evidence of a shared space; frozen models (BERT/GLUE fine-tunes); benchmark medians. Concepts: three classes of layers, execution strategies, uniformity without redundancy.

## Bearing on the record

- **[CLAIM-tmpcvuyr](../claims.d/CLAIM-tmpcvuyr.md)** (supports, with corrections). Defeater (a) is not met for Llama2, Mistral or BERT. Corrections written into version 2: middle layers cannot be "repeated" (copies are catastrophic; only looping a parallel block is benign); "nearly interchangeable" overstates, the paper's phrase is uniformity without redundancy; the loss is graceful, not modest everywhere, steep for math and reasoning and for Pythia.
- **Recheck**: [LIT-657](../literature.d/LIT-657.md) (InfoRidge, held: middle blocks add the most information), [LIT-850](../literature.d/LIT-850.md) and [THEORY-176](../theory.d/THEORY-176.md) (model stitching; a caution on reading skip-robustness as a shared space).

## Limitations

Results plotted, few numbers in text; interventions always keep the first and last layers; few families; cosine similarity inflated by anisotropy; cause left open.
