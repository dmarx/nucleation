# Reader notes: he (He, Zhang, Wu, Du, Chen, arXiv 2601.09049)

## 2026-11-19: copy located and read
- arXiv PDF v1 (14 Jan 2026), https://arxiv.org/pdf/2601.09049, HTTP 200, 10 pages. Read in full: main text (secs 1-7), App. A (Fig. 4), B, C. Figures read from rendered page images.
- Short paper. No tables, no seeds or run counts, no model size in the paper text; architecture named only as the parameter-sharing (recursive) transformer of Jolicoeur-Martineau 2025. The repo README gives TRM settings (not the paper text).
- Design: 2,000 entities, 200 relations, 40,000 atomic facts, 5% OOD; phi = 18.0. Conditions: natural grokking; both-hop full aug; first-hop full aug; second-hop full aug ("fake grokked"); both-hop half aug; "Pretrain"/"Pretraining Control Group" (not defined in the text).
- Fine-tune: 2,000 new atomic facts + 8,000 retained ID facts + their compositions; curves to 40k steps.
- For the lead: (a) later acquisition curves across first-stage regimes, read as curves, no numbers or threshold; no from-scratch baseline described (the control group is undefined). (b) different organizations compared (bridge recovery by logit lens), but first-stage OOD accuracy is NOT matched: Fig. 2 shows natural ~0.7, fake ~0.95, full aug ~1.0 (read off the plot). (c) no intervention; logit lens only.
- Transfer only when the new fact is in the first hop; old+new and new+new compositions stay ~0 for every condition (Fig. 4).
