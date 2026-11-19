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
