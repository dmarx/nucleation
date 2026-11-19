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
