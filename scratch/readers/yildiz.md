# Reader notes: yildiz (arXiv 2402.17400)

## 2026-11-19: copy located and read
- Copy: https://arxiv.org/pdf/2402.17400 (v2, 12 Feb 2025), arXiv PDF, fetched without obstacle. Read in full; appendix figures skimmed (captions only, figures are images).
- Title: "Investigating Continual Pretraining in Large Language Models: Insights and Implications". Authors: Çağatay Yıldız, Nishaanth Kanna Ravichandran, Nitin Sharma, Matthias Bethge, Beyza Ermis.
- Setup: pretrained GPT2-S/M/L/XL, Llama2-7B, RoBERTa-base/large continually pretrained over 159 M2D2 L2 domains (6.6B tokens), one epoch each, batch 16, Adam. Two orders: similar-order (Wiki portion then S2ORC, by Sentence-BERT similarity) and random-order (one shuffle; GPT2-M re-shuffled twice).
- Metrics are perplexity medians: ZS, DAPT (each domain alone from the base model), CPT, LC, FG; backward/forward transfer.
- Main findings: CPT beats DAPT for all models; random order gives better final checkpoint and less forgetting; similar order gives better CPT in larger models and positive backward transfer to recent past only; smaller models learn and forget most; Llama2-7B degrades.
- First doubt for the lead: no cost measure. Nothing is stated in tokens or compute to a threshold; total data is the same across orders (all 159 domains once each), so the order comparison is at fixed total data, but outcome is perplexity, not cost.
