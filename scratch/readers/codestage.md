# Reader notes: codestage (Ma et al., arXiv 2309.16298)

## 1. Copy located and read (2026-11-19)
- arXiv PDF https://arxiv.org/pdf/2309.16298 (v2, 30 Sep 2023, 17 pp.), fetched 200; text extracted with pdftotext and read in full, incl. appendices A-H. Figure 2 read from a page render.
- arXiv HTML and abs page also fetched (200). No bot check met.
- Authors from the title page: Yingwei Ma, Yue Liu (co-first), Yue Yu, Yuanliang Zhang, Yu Jiang, Changjian Wang, Shanshan Li.

## 2. What the paper does (first pass)
- Baselines are the *released* PanGu-alpha 2.6B and 13B text models; the authors train only one new model, CodePanGu2.6B, from scratch on 100GB text + ~50GB CodeParrot Python (~42B tokens, CodeParrot 36.1% per Fig. 2), with a different tokenizer (ChatGLM, 130,044 vocab vs PanGu's 40,000).
- Nothing is token- or compute-matched; the code model sees text "with the same scale and source" plus code on top. No seeds, no error bars, one run per arm.
- Dynamic mixing (Tables 5-6) is run at the instruction-tuning stage only; text:code phases for "stepwise decrease" are 5:5, 6:4, 7:3, 7:3. "since experiments in the pre-training phase require a lot of resources, we leave the validation of this phase to later work."
- Doubt: the "CC (2.6B)" column of Table 3 is identical to "Stepwise Decrease" in Table 6, so the CC model appears to be the stepwise-decrease run on CodePanGu2.6B (my inference, not stated).
- Mean code share across the four phases is 37.5% in all three schedules (my arithmetic from Table 5), so schedules are matched on average mix.

## 3. Closer reading of the tables
- Logic accuracies (36.36, 40.90, 45.45, 31.82) are multiples of 1/22, so the Logic set appears to have 22 items: one question separates 36.36 from 40.90 (my inference).
- NL (13B) beats CODE (2.6B) on Logic (45.45 vs 40.90), against the paper's bullet that the 13B model is "still not as effective as CODE (2.6B)".
- Other tasks (Table 7, pretraining): DuReader F1 15.29 -> 8.73 and EM 0.42 -> 0.14 with code; OCNLI and CMNLI drop about 1-1.6 points. "almost without negative transfer" rests on C3 only rising.
- Instruction-tuning corpus: parts named are 52K + 200K text and 150K code = 402K, while the text says 500K. Unexplained.
- No cost-to-threshold measure anywhere: all results are zero-shot end scores.

## 4. Bearings searched
- No LIT for this work in the record (main or this branch); it was pointed to only by the coordinator's search note (wt/ds, search2.md), which called the dynamic-mixing finding "Weak-partial". That characterization is accurate.
- CLAIM-756: background at most; no cost of later acquisition measured, no order compared at fixed total data in pretraining.
- QUESTION-039: background; order tested only in instruction tuning, final scores, single runs.
- TERM-131: no bearing beyond usage.
- THEORY-tmpd6smn (Liu et al.): the nearest parallel. Liu et al. did test code timing in pretraining, the thing Ma et al. leave to later work.
- THEORY-tmpk9cmk, THEORY-tmpd6l4a, THEORY-tmp0lbb1: parallels; Ma et al.'s design is weaker on every control those have.
