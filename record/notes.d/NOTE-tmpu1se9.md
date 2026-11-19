---
status: Read
paper: LIT-tmpdvkoo
title: 'Feng, Goodman and Frank — Is Child-Directed Speech Effective Training Data for Language Models?'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read in full on 2026-11-19 from arXiv 2408.03617v2; loss-curve figures
    seen at low resolution, no values taken from them. Read on 2026-11-19 by
    a delegated reader, with running notes on the branch
    claude/readers/data-scheduling; quotations rechecked by the filer by
    script against the downloaded text.
date: '2026-11-19'
summary: >-
  Controlled rearing of small language models on child-directed
  conversation: ordering conversations by child age, in reverse or at
  random leaves final syntax and semantics about the same, while shuffling
  utterances within a conversation hurts on CHILDES. Conversational data
  helps syntax at equal tokens; a mixed corpus is best overall for GPT-2.
  It measures final general competence after one corpus, never a later
  domain.
---
<!-- inactive-ok-file: CLAIM-756 — Proposed; the entry this reading bears on -->

# NOTE-tmpu1se9: Feng, Goodman and Frank — Is Child-Directed Speech Effective Training Data for Language Models?

## Key results

1. **Global order barely matters (p. 5).** "global ordering has a negligible effect on GPT-2 performance"; abstract: "The local properties of the data affect model results, but surprisingly, global properties do not." For RoBERTa the global-order runs "seemed unable to converge properly", so the result is GPT-2 only.
2. **Weak power.** Differences of one or two points beside seed spreads of similar size, three seeds; each age bucket repeated ten times, which the authors note "can potentially wash away global ordering effects".
3. **Local order matters (p. 5).** "Disrupting discourse coherence negatively affects Zorro and WS for CHILDES."
4. **Data source (p. 4).** "Overall, conversational data seems essential for better grammar and syntax learning across architectures." "In general, more diverse datasets (e.g. general conversation data or a mixture of different data sources) may result in better learning than homogeneous child-directed data."
5. **Scope (p. 2).** "Our goal is not to assess curriculum learning more generally but to measure the extent to which the specific developmental curriculum that children are exposed to is helpful."

## Bearing on the record

- **LEAD-tmp5lpoy.** A different question from the owner's recollection, not a counter-example: it orders within one conversational corpus and measures final general competence; no conversational-then-domain sequence and no later cost. At most a weak instance of order not mattering at fixed data, for within-corpus age order.
- **CLAIM-756.** Background: no later acquisition is measured.

## Limitations

Small models and data; two benchmarks; GPT-2 only for global order; pseudo-replicated tests; heavy repetition; a GPT-4-generated corpus.
