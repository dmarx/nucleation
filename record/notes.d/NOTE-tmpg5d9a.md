---
status: Read
paper: LIT-tmptmqyy
title: 'Gururangan and colleagues — Don''t Stop Pretraining: Adapt Language Models to Domains and Tasks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 from arXiv 2004.10964v3, main text and appendices;
    the reference list skipped. Read on 2026-11-19 by a delegated reader,
    with running notes on the branch claude/readers/data-scheduling;
    quotations rechecked by the filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  A second phase of masked-LM pretraining on domain text or task text
  before fine-tuning raises end-task F1 on eight tasks in four domains; an
  irrelevant domain or another task's text does worse than none. Results
  are final performance at a fixed fine-tuning budget; the only data-cost
  statement compares across settings; general pretraining is never
  removed; general-domain loss rises after domain adaptation.
---
<!-- inactive-ok-file: CLAIM-756 CLAIM-758 THEORY-tmpkjzqg — Proposed; entries this reading bears on -->

# NOTE-tmpg5d9a: Gururangan and colleagues — Don't Stop Pretraining: Adapt Language Models to Domains and Tasks

## Key results

1. **Relevance, not volume (§3.2–3.3).** "DAPT improves over RO BERTA in all domains"; against an irrelevant-domain control, "exposure to more data without considering domain relevance is detrimental to end-task performance".
2. **Order tried (§4.1).** "We begin with RO BERTA and apply DAPT then TAPT"; "combined domain- and task-adaptive pretraining achieves the best performance on all tasks". The reverse is speculation: "TAPT followed by DAPT would be susceptible to catastrophic forgetting of the task-relevant corpus".
3. **Sibling tasks hurt (§4.1).** "TAPT optimizes for single task performance, to the detriment of cross-task transfer."
4. **The nearest cost statement (§5.1).** Curated task-adaptive pretraining with 500 labels reaches "95% of the performance of DAPT + TAPT with the fully labeled RCT corpus (Table 5) with only 0.3% of the labeled data", across settings, not a curve.
5. **Amortization (§5.3).** "once the LM has been adapted to a broad domain, it can be reused for multiple tasks within that domain".
6. **Held competence (App. E).** Masked-LM loss on general text rises after every domain adaptation (from 1.19 to between 1.33 and 2.07, Table 12) while end-task results improve.

## Bearing on the record

- **[CLAIM-756](../claims.d/CLAIM-756.md).** A weak parallel in performance terms; ULMFiT's cost-to-level remains the stronger case. Irrelevant adaptation shows the converse: an earlier acquisition making a later one turn out worse.
- **[CLAIM-758](../claims.d/CLAIM-758.md).** Collateral loss of general competence after further training is measured, but on a shifted distribution, not continued stabilization: not a case.
- **[THEORY-tmpkjzqg](../theory.d/THEORY-tmpkjzqg.md).** Independent support for relevance deciding transfer, by another method.

## Limitations

One model and one adaptation length; no learning curves; significance claimed without a stated test; development and test disagree on one task.
