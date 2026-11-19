---
status: Read
paper: LIT-tmpvfc1j
title: 'Liu, Neubig and Xiong — Midtraining Bridges Pretraining and Posttraining Distributions'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read in full on 2026-11-19 from arXiv 2510.14865v2; figures 4 and 5 read
    off the rendered pages, values approximate. Read on 2026-11-19 by a
    delegated reader, with running notes on the branch claude/readers/data-
    scheduling; quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Controlled midtraining in Pythia-architecture models trained from
  scratch on C4: specialized data mixed in during pretraining, at matched
  total tokens, lowers loss after fine-tuning on distant target domains
  and keeps more general competence; a heavy late mix ends worse than
  none. The outcome is final loss at a fixed fine-tuning budget; the
  plasticity window is inferred from timing and confounded with the
  learning-rate schedule.
---
<!-- inactive-ok-file: CLAIM-757 CLAIM-758 CASE-294 — Proposed; entries this reading bears on -->

# NOTE-tmphfhfu: Liu, Neubig and Xiong — Midtraining Bridges Pretraining and Posttraining Distributions

## Key results

1. **Setup (§3.1).** "We pretrain models from the Pythia family ranging in size from 70M-1B parameters on C4 web data", with a control "continuing C4 pretraining for the same number of tokens, keeping all other training details identical". Fine-tuning runs a fixed four epochs.
2. **Domain-specific gains (§4).** "Mismatched domains provide little benefit, and broad instruction data (FLAN) also shows minimal effect." Forgetting is measured "by evaluating cross-entropy loss on the original pretraining distribution", and "in-domain improvements and C4 retention are strongly aligned".
3. **Timing (§6).** "Early introduction of code with a very high mixture weight (80%) achieves the best in-domain performance", reversing later, "with the high mixture weight (80%) performing substantially worse than the conservative mixture (10%) at 105B tokens". The decline is gradual across start times. The authors: "the model may lack sufficient plasticity to adapt to a high weight of specialized data late in pretraining."
4. **Mostly a better start.** The one learning curve: "The midtrained model starts with a lower training loss, and maintains a slight gap throughout training."
5. **Theory (§2.3).** "Midtraining affects posttraining only through the resulting initialization"; plasticity enters as an assumed nonincreasing function, and "we do not claim that these assumptions hold globally for large language models."

## Bearing on the record

- **[CLAIM-757](../claims.d/CLAIM-757.md).** The nearest thing on record to a deadline in language-model pretraining. Its decline is gradual, with no threshold, which fits the depletion branch more than the disuse branch, but it tests no renewed practice or reset and cannot separate plasticity from the cosine schedule's falling learning rate: a parallel, and a confound the claim's test should name.
- **[CLAIM-758](../claims.d/CLAIM-758.md).** In the base checkpoint series, in-domain loss after fine-tuning is flat after about 40B tokens and general loss after fine-tuning slightly rises late, within the bands: at most a faint version of Springer and colleagues' pattern at small scale.
- **[CASE-294](../cases.d/CASE-294.md).** The same model family and sizes, a checkpoint series each fine-tuned, forgetting scored; but trained from scratch, final loss rather than cost to a threshold, natural targets, no resets.
- **[LEAD-tmp5lpoy](../leads.d/LEAD-tmp5lpoy.md).** The direction runs against the owner's example: specialized data early and mixed beats a long general stretch before heavy specialization.

## Limitations

Small models; one pretraining run per condition; timing studied for code at 70M and 160M only; learning rate and plasticity confounded; continued-pretraining arm confounded by start time.
