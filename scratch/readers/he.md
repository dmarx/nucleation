# Reader notes: he (He, Zhang, Wu, Du, Chen, arXiv 2601.09049)

## 2026-11-19: copy located and read
- arXiv PDF v1 (14 Jan 2026), https://arxiv.org/pdf/2601.09049, HTTP 200, 10 pages. Read in full: main text (secs 1-7), App. A (Fig. 4), B, C. Figures read from rendered page images.
- Short paper. No tables, no seeds or run counts, no model size in the paper text; architecture named only as the parameter-sharing (recursive) transformer of Jolicoeur-Martineau 2025. The repo README gives TRM settings (not the paper text).
- Design: 2,000 entities, 200 relations, 40,000 atomic facts, 5% OOD; phi = 18.0. Conditions: natural grokking; both-hop full aug; first-hop full aug; second-hop full aug ("fake grokked"); both-hop half aug; "Pretrain"/"Pretraining Control Group" (not defined in the text).
- Fine-tune: 2,000 new atomic facts + 8,000 retained ID facts + their compositions; curves to 40k steps.
- For the lead: (a) later acquisition curves across first-stage regimes, read as curves, no numbers or threshold; no from-scratch baseline described (the control group is undefined). (b) different organizations compared (bridge recovery by logit lens), but first-stage OOD accuracy is NOT matched: Fig. 2 shows natural ~0.7, fake ~0.95, full aug ~1.0 (read off the plot). (c) no intervention; logit lens only.
- Transfer only when the new fact is in the first hop; old+new and new+new compositions stay ~0 for every condition (Fig. 4).

## 2026-11-19: figures read, bearings searched
- Fig. 4 (App. A), read off the plot: new+old compositions reach ~1.0 within ~5-10k steps for natural, both-hop full and first-hop full; second-hop full ("fake") ~0.35 at 40k; "Pretrain" ~0.3; both-hop half ~0.4-0.5, noisy. old+new and new+new stay ~0 in every row. The "Pretrain" and "Both Hop Half Aug" rows are not described anywhere in the text.
- The "(ii) substantially more finetuning data" remedy is asserted; no run with more fine-tuning data or a second grokking phase is shown.
- The record holds no LIT for this work or for Wang et al. 2024 (grokked transformers). The search notes' tag "(a qualitative, b approximate, no weight intervention)" holds; "b approximate" is generous, since first-stage OOD accuracy differs (~0.7 natural vs ~0.95 fake vs ~1.0 full).
- Bearings: LEAD-tmphfbq0 (partial match: b by organization, a as curves, no c), CLAIM-596/QUESTION-397/TERM-117 (no with-and-without rate), CLAIM-519 (logit lens is observational), CASE-294 (two-hop family), THEORY-039, THEORY-984, THEORY-2035, QUESTION-360, CLAIM-756, CLAIM-758, CLAIM-754.
