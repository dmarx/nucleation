# Reader notes: akter (arXiv 2510.03264)

## 2026-11-19, copy located and read
- arXiv HTML (v1, CC BY 4.0) fetched from arxiv.org/html/2510.03264, HTTP 200; abs page HTTP 200. Only v1 listed.
- Title: "Front-Loading Reasoning: The Synergy between Pretraining and Post-Training Data". Authors: Syeda Nahida Akter, Shrimai Prabhumoye, Eric Nyberg, Mostofa Patwary, Mohammad Shoeybi, Yejin Choi, Bryan Catanzaro (NVIDIA, CMU, BU, Stanford).
- Read body in full; appendices B and C read (tables 7-9, Figure 2 text).

## First findings
- One 8B hybrid Mamba-Transformer, pretrained from scratch 1T tokens, four arms: 80% base + 20% reasoning data (SHQ, LDQ, LMQ) vs base only. Then SFT (4.8M samples), then GRPO on two arms only.
- Pretraining token count fixed (1T); total reasoning data NOT fixed: baseline gets ~0 reasoning tokens in pretraining vs ~200B for the others. The paper's Eq. 2 states a budget constraint but no experiment holds it.
- The "catch-up" test doubles SFT for the baseline (34.01 vs 37.33 for M_SHQ+SFT). That doubling is far smaller than the 20% of 1T given to reasoning data in pretraining; no matched-data comparison.
- No seeds or repeat runs stated; no limitations section; no cost or saving stated in compute or data.
- Doubt: Table 4's baseline row (26.62; math 34.48) does not match the D_SHQ baseline in Tables 5 and 8 (29.92; math 42.79), though Table 4's text says all models were finetuned on D_SHQ.
