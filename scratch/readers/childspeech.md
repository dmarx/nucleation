# Reader notes, in flight: childspeech (removed when filed)

## Step 1: copy located (2026-11-19)
- Feng, Goodman, Frank, "Is Child-Directed Speech Effective Training Data for Language Models?", arXiv 2408.03617.
- arXiv abs page: v1 2024-08-07, v2 2024-10-08 (latest). Comments: "EMNLP 2024" (venue confirmed from the arXiv comment).
- Read: https://arxiv.org/pdf/2408.03617v2, 17 pages, pdftotext. Download kept in the scratchpad, not here.
- Named codes read: LEAD-tmp5lpoy, CLAIM-756, CLAIM-754, CLAIM-605, TERM-131.

## Step 2: paper read in full (main text, appendices A-L)
- Design: GPT-2 small (124M) and RoBERTa-base (125M) from scratch on ~29M words each (24.5M train) of CHILDES, TinyDialogues (GPT-4 synthetic), Wikipedia, OpenSubtitles, BabyLM subsample. Evals: Zorro (syntax minimal pairs) and word similarity (WS). Outcome is final performance (best-val-loss epoch, or final model for bucket runs), not a cost to a threshold.
- Global order (age / reverse / random) only within CHILDES or within TD, via "repeated buckets" (A^n B^n C^n). GPT-2 only; RoBERTa bucket runs "did not converge properly" and are not interpreted. 3 seeds GPT-2.
- Result: "global ordering has a negligible effect on GPT-2 performance" (p.4). Local utterance shuffling hurts CHILDES, little effect on TD.
- No condition trains on one kind of data then a different kind: no conversational-then-domain transfer measured. Every model is evaluated on the same two benchmarks after training on one corpus.
- Doubts: effects small vs seed sd; nulls not powered (3 seeds, t-tests on per-example Zorro give p=0 everywhere, so significance is mostly uninformative); epoch-level repetition (n=10) can wash out order.

## Step 3: quotes checked, bearings searched
- 25 quotes checked by script against the downloaded text (whitespace-normalized); one line-break-dehyphenated quote replaced.
- Figures 4-8 (loss curves) viewed at low resolution only; validation loss is on the mixed-age validation split, not per bucket, so no later-acquisition cost can be read off them.
- Detail worth flagging: Table 3 CHILDES Zorro is lowest for age order (75.62 vs 77.63 reverse, 76.87 random) and the paper's per-example t-test calls all Zorro pairs significant (p=0); the authors still read the global effect as negligible. With seed SDs of 1.1-1.3 points and 3 seeds, the null is weakly powered either way.
- Record search: no entry holds the work or mentions child-directed-speech training data for LMs. Related: LEAD-tmp5lpoy (direct), CLAIM-756, CLAIM-754, QUESTION-039, NOTE-319/LIT-371 (Zucchet: subset-first warm-up helps fact learning; a positive curriculum result, single seed), THEORY-279 (low-order statistics first), CASE-113 and QUESTION-275 (curriculum as training exposure, background). CLAIM-605 and TERM-131: background only.
- Verdict so far: a different question from the owner's recollection, not a counter-example. It orders within one conversational corpus by child age and measures final performance on general benchmarks; it never trains conversational then domain text, and never measures the cost of a later acquisition.
