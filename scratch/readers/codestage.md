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
