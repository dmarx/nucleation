---
status: Read
paper: LIT-tmpg77d0
title: 'Yıldız and colleagues — Investigating Continual Pretraining in Large Language Models: Insights and Implications'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2402.17400v2 (PDF,
    12 Feb 2025): §§1–7 in full and appendix A in part; figures from
    captions only. Running notes on the branch claude/readers/scheduling-
    followups (the procedure proposed in pull request 537). Quotations
    rechecked by the filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  Continual pretraining over 159 domains in similar or random order: order
  changes final perplexity and forgetting at fixed data; forward transfer
  measured zero-shot, never as cost.
---
<!-- inactive-ok-file: CLAIM-756 THEORY-tmpd6l4a — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmp4noj0: Yıldız and colleagues — Investigating Continual Pretraining in Large Language Models: Insights and Implications

## Key results

1. "Continual pretraining outperforms domain-adaptive pretraining across
   all model families and sizes" (§1); the earlier domains' tokens are not
   counted.
2. "Randomizing the order of training domains enables positive transfer
   and reduced forgetting." (§1)
3. Similar order: "larger models seem to attain better CPT perplexity in
   similar order training than random order" (§4.3).
4. Forward transfer after a few similar domains is negative: "pretraining
   on a handful of domains leads to significantly worse performance
   compared to zero-shot" (§4.4).
5. Llama2-7B: "additional training (including domain adaptation) always
   degrades the perplexity" (§4.1).

## Bearing on the record

- **CLAIM-756**, weak background: earlier domains leave a later domain
  better after the same budget on it, with the earlier cost uncounted; some
  earlier acquisitions make later ones start worse, in zero-shot loss.
- **THEORY-tmplutfz** (Gururangan and colleagues), qualifies and extends
  domain-adaptive pretraining.
- **THEORY-tmpd6l4a**, agreeing in direction: a similarity sequence ends
  worse than random.
- **THEORY-tmprqq7k**, contrast: here order changes final perplexity.
- **THEORY-2006**, **CLAIM-758**, **CLAIM-757**: analogies on long
  pretraining and later degradation; nothing measured as a budget.

## Limitations

One run per condition; learning rate unstated; perplexity medians only;
base models with different pretraining.
