---
status: Read
paper: LIT-tmp8l2rx
title: 'Li et al. — PhotoMaker'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read from arXiv v1 (2312.04461, 7 December 2023, the only version), text extracted with pdftotext. Read: abstract, §§1–5, Table 1, the ablations (Table 2, Fig. 7) and appendices F and G. Other appendix galleries skimmed; references skipped. Table 1 was read from a layout extraction of the PDF. Quotes rechecked against the extracted text by script.
date: '2026-11-12'
summary: >-
  A tuning-free personalization model for SDXL, trained once on an ID-grouped dataset for two weeks on 8 A100s, stacks embeddings of several photos of one person in place of the class word and personalizes in about 10 s on a V100, against 1284 s for DreamBooth and 2400 s for Textual Inversion, with the highest CLIP-I and DINO of the five methods compared and face similarity second to IP-Adapter's. Feed-forward, tuning-free identity personalization from any number of photos, with an ID-grouped training-data pipeline.
---
<!-- inactive-ok-file: CASE-tmp40vka CASE-tmp3isyl CLAIM-tmpnwq8a — Proposed; filed on the same branch -->

# NOTE-tmpul1vj: Li et al. — PhotoMaker

## Contribution

Feed-forward, tuning-free identity personalization from any number of photos, with an ID-grouped training-data pipeline.

## Key results

- **Method.** Abstract: it "encodes an arbitrary number of input ID images into a stack ID embedding"; §3.2 also trains "the LoRA [2, 25] residuals" of the attention layers, so the module is itself tied to SDXL.
- **Table 1** (25 IDs, 40 prompts; speed "on a single NVIDIA Tesla V100 GPU"):

  | method | CLIP-T | CLIP-I | DINO | Face Sim. | Speed (s) |
  |---|---:|---:|---:|---:|---:|
  | DreamBooth | 29.8 | 62.8 | 39.8 | 49.8 | 1284 |
  | Textual Inversion | 24.0 | 70.9 | 39.3 | 54.3 | 2400 |
  | FastComposer | 28.7 | 66.8 | 40.2 | 61.0 | 8 |
  | IP-Adapter | 25.1 | 71.2 | 46.2 | 67.1 | 12 |
  | PhotoMaker | 26.1 | 73.6 | 51.5 | 61.8 | 10 |

- **A discrepancy.** §4.2 says PhotoMaker has "the largest CLIP-T and DINO scores, and the second best Face Similarity". By Table 1 the largest CLIP-T is DreamBooth's (29.8 against 26.1); PhotoMaker has the largest CLIP-I and DINO. The record cites the table.
- **The maker's cost.** §4.1: trained on "8 NVIDIA A100 GPUs for two weeks with a batch size of 48".
- **The tuned route's human cost.** §1: data for fine-tuning "each time requires manual collection".

## Assumptions

Human identity only, SDXL as the base, a benchmark of the authors' own. "Speed" counts per-use personalization; for DreamBooth and Textual Inversion it includes their per-subject training, and it excludes PhotoMaker's own two weeks of training.

## Concepts

- **stacked ID embedding** — embeddings of N photos, each fused with the class word's text embedding, stacked in its place.
- **tuning-free personalization** — no per-subject optimization at use.

## Bearing on the record

- **[CASE-tmp40vka](../cases.d/CASE-tmp40vka.md): supports, with numbers.** For human identity on one base in late 2023, trained routes cost 1284–2400 s per subject and reference routes 8–12 s per image, at equal or better identity metrics. The numbers are the method's own authors'.
- **[CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md):** gives F for DreamBooth and a per-use cost for the reference routes on one GPU type, but not DreamBooth's per-image cost after training, so n* cannot be computed. The rankings change with the metric, which is the study's main threat.
- **[CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md): corroborates the caveat.** The reference route rests on a module trained once against one base by its maker.
- **[QUESTION-095](../questions.d/QUESTION-095.md):** amortization moved to another party, the maker paying a fixed cost once so users pay only per use.

## Limitations

Authors' own benchmark and baselines; DreamBooth's configuration on SDXL is not described. Text and table disagree on CLIP-T.
