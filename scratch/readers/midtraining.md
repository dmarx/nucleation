# Reader notes, in flight: midtraining (removed when filed)

## 2026-11-19: copy located and read
- arXiv 2510.14865v2 (revised 2 Feb 2026), PDF and HTML from arxiv.org, no check. Read in full, main text and appendices A-I. Downloads kept outside the worktree.
- ICML 2026: listed on icml.cc (poster 66254, oral 71139) per a web search; the v2 PDF itself says "Preprint. February 3, 2026."
- Design: Pythia-architecture models (70M, 160M, 410M, 1B) pretrained FROM SCRATCH on C4 for 128B tokens (cosine LR), not the released Pythia checkpoints. Midtraining = mixing a specialized share into the remaining pretraining; control = C4 for the same tokens. Then SFT for a fixed 4 epochs.
- Outcome: final SFT validation loss and C4 loss after SFT (forgetting). Not a cost (tokens or steps to a level). Only Fig. 8 (one curve) hints at speed.
- "Plasticity window": inferred from a start-time x mixture-weight grid on code (Fig. 4, starts 12B-105B tokens, weights 10-80%), not measured as plasticity. Late start coincides with lower cosine LR; the paper does not discuss that confound. In the theory, plasticity s(.) is ASSUMED nonincreasing (App. A, Lemma A.6).
- Midtraining vs continued pretraining (Table 3) also differs in start time (12.6B vs 83B tokens for code), which their own Finding 4 says matters.

## 2026-11-19: figures read, quotes checked, bearings searched
- Fig. 4 (read off the plot, approximate): 80% code started at ~12B tokens is best; started at ~105B it is WORSE than pretrain-only on Pycode SFT loss (70M ~2.76 vs ~2.64; 160M ~2.46 vs ~2.38). Decline is gradual across 12-105B, no step.
- Fig. 5 is a checkpoint study (160M, base and 20% Starcoder, checkpoints 20-128B tokens, each fine-tuned on Pycode): base in-domain loss after SFT falls then flat; base C4 loss after SFT lowest near 60B and slightly up after. No overconsolidation in final-loss terms at this scale; a faint Springer-like rise in forgetting, inside noise bands.
- Fig. 8 caption: midtrained model "starts with a lower training loss, and maintains a slight gap" -- the gain is mostly a better start, not faster later learning.
- Doubt: LR for SFT said both "selected ... on the base pretrained checkpoint before midtraining" (App. C) and "hyperparameter search for each checkpoint" (sec. 4).
- 28 quotes checked by script against the PDF/HTML text: all found.
- Bearings searched: CLAIM-756/757/758/754, CASE-294, TERM-131, THEORY-2027 (Dohare), THEORY-2006 (Springer, which the paper cites), THEORY-1353, THEORY-2015, THEORY-1032, THEORY-tmpw8s3h, THEORY-tmppm9la, QUESTION-495.
