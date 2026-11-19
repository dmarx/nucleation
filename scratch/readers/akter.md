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

## 2026-11-19, numbers checked and bearings searched
- Headline figures do not all reproduce from the tables: Table 3 gives 56.66 vs 37.92 (18.74 points; text says 18.57%); AIME mean gap from Table 3 is about 25 points, text says 39.32%. Doubt, not a finding: the text may use another aggregation.
- The arXiv abs-page abstract omits the HTML abstract's "when the token counts are controlled".
- Verdict for the lead: not order at fixed data. Pretraining tokens fixed at 1T, so the reasoning arms displace 20% general data. Reasoning tokens differ between arms by about 200B, and no arm puts the same reasoning tokens late. No data or compute saving is stated; the "compute-efficient" in the conclusion is not measured.
- Bearings: CLAIM-756 (weak, qualifies: final-performance gain, earlier cost not counted as a cost); QUESTION-039 (background); TERM-131 (background); THEORY-tmpd6smn (parallel, early specialized data better, also at matched total tokens); THEORY-tmpk9cmk, -tmpd6l4a (contrast: they count cost); THEORY-tmplutfz, -tmp0lbb1 (parallel, final performance); THEORY-2006 and CLAIM-758 (contrast: no overconsolidation seen at 1T/8B, single run); CLAIM-754 (developmental frontier, parallel); QUESTION-495 (background).
- Quotes checked by script against the downloaded text: all 25 found.
