# Reader notes: Wang, Mittal, Song, Jia, "Data Shapley in One Training Run" (arXiv 2406.11011v3, ICLR 2025)

## 2026-11-19 copy located and read
- arxiv.org/pdf/2406.11011 (v3, 7 Jun 2025), 38 pp, fetched without obstruction. Text extracted to the reader's scratchpad (not committed).
- Read in full: Abstract, Sec 1-6, App A.2-A.3, B, E.1-E.5. Skimmed: proofs (C), ghost techniques (D), E.6.
- What is measured: per-step Shapley value of a training point toward the loss change on a validation point, under a first- or second-order Taylor approximation of the one-step loss change; summed over steps. First-order = TracIN-Ideal ("equivalent to the TracIN-Ideal score", Sec 4.1). Second-order adds a within-batch interaction term.
- Model/data: GPT2 (124M) and Pythia-410M on the Pile; batch 16, seq 1024, AdamW in training but SGD formulas as proxy (App E.1, Remark 7).
- Sec 5.3.2: one math validation corpus, second-order value, domain composition over first 10,000 iterations (figure x-axis to ~5000). ArXiv dominates; Pile-CC "initially shows positive contributions during the first few iterations. However, its value quickly drops to negative and eventually converges to zero." No order intervention.
- App E.4: average per-point value shrinks toward zero over steps; "Data points introduced in later stages of training contribute less".
- Doubt: the intro's "later stages ... domain-specific corpora becomes dominant" overstates Fig 3, where ArXiv dominates from early on; what changes is Pile-CC dropping out. Also ~10k steps x 16 x 1024 is ~164M tokens: very early in training.
- Key structural point for the lead: the measure is local per step (gradient alignment at that step), so it cannot credit early data for making later learning easier; it is not a test of facilitation.
