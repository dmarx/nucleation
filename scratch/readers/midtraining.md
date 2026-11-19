# Reader notes, in flight: midtraining (removed when filed)

## 2026-11-19: copy located and read
- arXiv 2510.14865v2 (revised 2 Feb 2026), PDF and HTML from arxiv.org, no check. Read in full, main text and appendices A-I. Downloads kept outside the worktree.
- ICML 2026: listed on icml.cc (poster 66254, oral 71139) per a web search; the v2 PDF itself says "Preprint. February 3, 2026."
- Design: Pythia-architecture models (70M, 160M, 410M, 1B) pretrained FROM SCRATCH on C4 for 128B tokens (cosine LR), not the released Pythia checkpoints. Midtraining = mixing a specialized share into the remaining pretraining; control = C4 for the same tokens. Then SFT for a fixed 4 epochs.
- Outcome: final SFT validation loss and C4 loss after SFT (forgetting). Not a cost (tokens or steps to a level). Only Fig. 8 (one curve) hints at speed.
- "Plasticity window": inferred from a start-time x mixture-weight grid on code (Fig. 4, starts 12B-105B tokens, weights 10-80%), not measured as plasticity. Late start coincides with lower cosine LR; the paper does not discuss that confound. In the theory, plasticity s(.) is ASSUMED nonincreasing (App. A, Lemma A.6).
- Midtraining vs continued pretraining (Table 3) also differs in start time (12.6B vs 83B tokens for code), which their own Finding 4 says matters.
