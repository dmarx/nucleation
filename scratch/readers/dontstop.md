# Reader notes, in flight: dontstop (removed when filed)

## Step 1: copy located (2026-11-19)
- arXiv API (export.arxiv.org, no email): 2004.10964 latest is v3 (updated 2020-05-05), "Don't Stop Pretraining: Adapt Language Models to Domains and Tasks", Gururangan, Marasović, Swayamdipta, Lo, Beltagy, Downey, Smith; comment "ACL 2020".
- Fetched https://arxiv.org/pdf/2004.10964v3 (19 pages, incl. appendices); text extracted with pdftotext -layout. Download kept in scratchpad only.
- Read beforehand: LEAD-tmp5lpoy, CLAIM-756, CLAIM-754, CLAIM-758, TERM-131, CASE-294.

## Step 2: whole paper read (pp. 1-19, main text and appendices A-F)
- Design: RoBERTa-base, second phase of MLM pretraining: DAPT (12.5K steps, one pass over 2-8B tokens of domain text) and TAPT (100 epochs on the task's unlabeled training text), then fine-tuning; 4 domains x 2 tasks; 5 seeds.
- Every main result is end-task F1 at the end of fine-tuning. No learning curve, no steps-to-threshold on the end task. The only cost tables are of the adaptation phases themselves (Table 9: steps, docs, storage for RCT-500).
- Closest to a cost result: §5.1, Curated-TAPT on RCT-500 "achieves 95% of the performance of DAPT + TAPT with the fully labeled RCT corpus (Table 5) with only 0.3% of the labeled data" -- a cross-setting comparison, not a matched curve.
- Irrelevant-domain control (§3.3, Table 3): ¬DAPT "generally" worse than plain RoBERTa: "exposure to more data without considering domain relevance is detrimental".
- Transfer-TAPT (Table 6): TAPT on one task's text hurts a sibling task in the same domain.
- Order: only DAPT then TAPT run; TAPT then DAPT only speculated ("susceptible to catastrophic forgetting"). General pretraining is never ablated: every arm starts from RoBERTa.
- Doubt: dev set (Table 15) shows DAPT below RoBERTa on HYPERPARTISAN (79.1 vs 84.0), test shows the reverse; high variance, degenerate seeds resampled (App. B).
