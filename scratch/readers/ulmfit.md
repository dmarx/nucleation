# Reader notes, in flight: ulmfit (removed when filed)

## 1. Identifier and copy (2026-11-19)

- arXiv API, id 1801.06146: latest v5 (2018-05-23), published v1 2018-01-18; comment "ACL 2018, fixed denominator in Equation 3, line 3". Versions v1 18 Jan, v2 14 May, v3 15 May, v4 17 May, v5 23 May 2018 (abs page history).
- ACL Anthology P18-1031, reachable: ACL 2018, Melbourne, pages 328–339, doi 10.18653/v1/P18-1031.
- Read: arXiv PDF v5 (12 pages incl. references), fetched 200, text extracted locally (kept in reader scratchpad, not committed).

## 2. Full read, first pass

- Sample efficiency is §5 "Low-shot learning", Figure 3 (IMDb, TREC-6, AG; supervised and semi-supervised ULMFiT vs training from scratch). Text: supervised, 100 labels "matches the performance of training from scratch with 10× and 20× more data" (IMDb, AG); semi-supervised (50k / 100k unlabelled) "50× and 100× more data on AG and IMDb respectively". TREC-6: no multiple given.
- Doubt: the abstract's "100×" is the semi-supervised IMDb figure. The intro gives IMDb 10× supervised and 100× with 50k unlabelled.
- Doubt: what "training from scratch" in Figure 3 holds fixed (architecture? the fine-tuning tricks?) is not stated.
- Attribution: Table 4 (with/without pretraining) is full-data, not low-shot. "Without pretraining" seems to keep target-task LM fine-tuning (IMDb 5.63 vs 5.00; TREC-6 10.67 vs 5.69; AG 5.52 vs 5.38). Inference, not stated.
- Forgetting: measured only as validation error rising during classifier fine-tuning (Figure 4, 'Full' vs ULMFiT); "knowledge captured through pretraining is lost" is their reading, not a direct probe of the LM.

## 3. Figures and ablations checked (rendered pages 7–9)

- Figure 3 (p. 7) is a plot only; the multiples are the text's. Read off the plot: IMDb supervised at 100 labels about 22% error, from-scratch reaches it near 1,000; semi-supervised about 11%, from-scratch near 10,000+. Consistent with the text.
- No ablation crosses method components with label count. The low-shot comparison is full ULMFiT against from scratch only, so the saving cannot be split between WikiText-103 pretraining and the fine-tuning techniques.
- Table 7 "From scratch" (IMDb 9.93) differs from Table 4 "Without pretraining" (5.63): my inference is that the latter keeps target-task LM training on in-domain text. If so, much of the full-data gain on IMDb comes from LM training on in-domain text, not from general-domain pretraining; TREC-6 is the exception (10.67 vs 5.69).
- Forgetting is never measured on what was pretrained (no LM perplexity, no old-task score). It is read off rising target-task validation error (Figure 4), which the authors also call overfitting. Matters for CLAIM-758, which keeps forgetting and overfitting apart.
- Quotes rechecked by script against the downloaded text (all matched).

## 4. Bearings searched

- Named: CLAIM-756, CLAIM-754, CLAIM-758, CLAIM-757, CASE-294; McDermott (THEORY-tmpkjzqg) and Anguita (THEORY-tmppm9la).
- Others found: THEORY-2006 (Springer), THEORY-2025 (Raghu), THEORY-2046 (MAML), THEORY-997, THEORY-1896, THEORY-331, THEORY-2045, THEORY-246 / QUESTION-236, QUESTION-493, QUESTION-495, TERM-131, CLAIM-303, CLAIM-569. Nothing on record cites ULMFiT except the lead and its ADR.
