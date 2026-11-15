---
status: Skimmed
paper: 'LIT-tmpmo0vh'
title: 'Braun et al. — Erased but not forgotten'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Skimmed on 2026-11-15 by a delegated reader from arXiv:2504.21072v4
    (2026-10-03), https://arxiv.org/pdf/2504.21072v4 (24 pp.), text by
    pdftotext. Read: the abstract, §1 with the contributions list, the §2
    terminology, §4.6 Outlook and Remedies and §5 Conclusion. Skimmed: §3
    (attack variants) and the §§4.1–4.4 results, through the abstract and
    the introduction's figures. Not read: the appendices and the
    per-table values. The code, github.com/multimodal-ai-lab/EEB, is named
    in the paper and was not fetched. The filer rechecked every quotation
    below against a fresh text extraction of the same PDF; all were found.
date: '2026-11-15'
summary: >-
  A trigger bound to a concept before erasure still elicits it after six
  text-to-image concept-erasure methods, including three built to resist
  circumvention, on SD v1.4, SD v2.1 and FLUX: 71.6% evasion on average
  and up to 94.4% for the deepest attack. Skimmed: framing, summary
  numbers and conclusion.
---

# NOTE-tmpo4g79: Braun et al. — Erased but not forgotten

## Contribution

The Erasure Evasion Backdoor (EEB): a supply-chain attack on concept
erasure. Before a model is sanitized, an adversary binds a trigger (for
example "tree") to the concept to be erased (nudity, a celebrity, an
object). The binding is made by dirty-label data poisoning (black box),
by the RICKROLLING or EVILEDIT weight edits, or by a new score-level
attack, EEBdeep, with LoRA across all U-Net layers. Tested against ESD,
UCE and MACE and the robust RECE, RECELER and ADVUNLEARN, on SD v1.4,
SD v2.1 and the DiT-based FLUX.

## Key insight

An erasure method removes the links to a concept that it looks for. A
link planted where it does not look survives, even when the method
searches adversarially for residual representations, because its search
is bounded by what it is given.

## Assumptions

- The adversary acts before erasure; the defender applies erasure unaware
  of the trigger.
- The targets are celebrity identities, objects and explicit content.

## Key results

- **Abstract**: "an adversary binds a backdoor trigger to a concept
  slated for removal, and this malicious link survives subsequent
  erasure"; across six methods, "up to 82% success against
  celebrity-identity unlearning, up to 94% for object erasure, and up to
  16× amplification of explicit-content exposure."
- **§1**: EEBdeep "circumvents erasure in 71.6% of the cases on average,
  and in up to 94.4%". Without model access: "up to 80.2% success in the
  celebrity erasure, up to 92.7% success in the object erasure, and a 6×
  increase in explicit content".
- **§1**: it holds "even against erasure methods that claim adversarial
  robustness and explicitly search for residual trigger-to-target
  representations".
- **§5**: "modifications that are spread across a larger set of
  parameters make backdoors harder to erase"; "attacks exploiting similar
  architectural components as the erasure technique achieve
  disproportionate success"; poisoned models "can be flagged through
  inference-time activation monitoring".

## Concepts

- **Erasure target vs erasure scope**: the concept removed against what
  the method checks.
- **Trigger**: the token bound to the concept before erasure.
- **EEB shallow, surface and deep**: the attack variants, by how much of
  the model they touch.
- **Robust erasure**: methods that search adversarially for residual
  representations.

## Bearing on the record

- **TERM-064**: the erasure procedure is itself an observer with a bounded
  search, and the trigger is illegible to it; robust methods that search
  for "alternative representations" still miss an association they were
  not given.
- **CLAIM-407**: by analogy only. On ordinary prompts the erased model
  behaves as clean, and the trigger is the input-side intervention that
  exposes the retained mechanism.
- **THEORY-425** (a connecting path trained on clean data removes a
  backdoor; LIT-668): a contrast, not a conflict. There clean-data
  training between two backdoored classifiers removes the backdoor; here
  erasure fine-tuning leaves it. The settings differ, classifier mode
  connectivity against diffusion concept erasure.
- **THEORY-281** and **QUESTION-010**: no direct bearing.

## Limitations

Skimmed: the framing and summary numbers, not the tables. Diffusion
models only. An attack paper; the remedies are sketched (§4.6).
