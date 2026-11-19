# Reader notes: yildiz (arXiv 2402.17400)

## 2026-11-19: copy located and read
- Copy: https://arxiv.org/pdf/2402.17400 (v2, 12 Feb 2025), arXiv PDF, fetched without obstacle. Read in full; appendix figures skimmed (captions only, figures are images).
- Title: "Investigating Continual Pretraining in Large Language Models: Insights and Implications". Authors: Çağatay Yıldız, Nishaanth Kanna Ravichandran, Nitin Sharma, Matthias Bethge, Beyza Ermis.
- Setup: pretrained GPT2-S/M/L/XL, Llama2-7B, RoBERTa-base/large continually pretrained over 159 M2D2 L2 domains (6.6B tokens), one epoch each, batch 16, Adam. Two orders: similar-order (Wiki portion then S2ORC, by Sentence-BERT similarity) and random-order (one shuffle; GPT2-M re-shuffled twice).
- Metrics are perplexity medians: ZS, DAPT (each domain alone from the base model), CPT, LC, FG; backward/forward transfer.
- Main findings: CPT beats DAPT for all models; random order gives better final checkpoint and less forgetting; similar order gives better CPT in larger models and positive backward transfer to recent past only; smaller models learn and forget most; Llama2-7B degrades.
- First doubt for the lead: no cost measure. Nothing is stated in tokens or compute to a threshold; total data is the same across orders (all 159 domains once each), so the order comparison is at fixed total data, but outcome is perplexity, not cost.

## 2026-11-19: bearings searched, quotes checked
- 38 quotes checked by script against the downloaded text: all found.
- No LIT for the work yet; the record names it only in LEAD-tmpjdtrl ("Yıldız and colleagues on domain order in continual pretraining").
- CLAIM-756: background at most. CPT-vs-DAPT is the nearest thing: domain i reached at lower perplexity after earlier domains than from the base model, same one epoch on domain i; but outcome is perplexity after a fixed budget, not cost to a threshold, and the earlier domains' tokens are not counted. Forward transfer is zero-shot perplexity on unseen domains, not cost of later learning.
- Order comparison IS at fixed total data (all 159 domains, one epoch each), but one similar order, one random order (two extra shuffles for GPT2-M CPT only), one run each.
- QUESTION-039: parallel (order of data, not order of acquisition of structure).
- THEORY-tmplutfz (Gururangan): extends it (CPT beats DAPT; relevance decides; recency).
- THEORY-tmpd6l4a: parallel; random/mixed beats sequential-by-similarity for final performance, agrees in direction.
- THEORY-tmprqq7k (Feng et al.): parallel; here order matters for final perplexity, unlike there.
- THEORY-tmpd6smn, THEORY-tmp0lbb1, THEORY-tmpk9cmk: background/parallel only.
- THEORY-2006 (Springer), CLAIM-758, CLAIM-757, THEORY-2027: Llama2-7B degrading and later checkpoints forgetting more are parallels in the forgetting sense; no acquisition budget measured.
- Doubt: Figure 3 numbers are images; I have only the text's statements and the GPT2-M CPT medians (16.4, 16.78, 16.69).
