# Reader notes: layers-painters (LIT-tmpi3ty1)

## Step 1: copy located (2026-11-21)
- https://arxiv.org/pdf/2407.09298 — arXiv, author preprint; fetched OK; resolves to v4 (12 Feb 2025), 6 pp (AAAI-format). Extracted with pdftotext.

## Step 2: read (2026-11-21)
- Read v4 in full (13 pp incl. appendix A.1-A.9); figures read from captions/text only (results are plotted, few numbers in text).
- Key: three similarity classes (begin/middle/end); skip graceful; Middle Repeat catastrophic ("middle layers are performing different functions"); reverse/random graceful, random > reverse; parallel graceful except GSM8K; looped parallel best; math/reasoning more order-dependent; Pythia-6.9B less robust (A.5); ending layer fixed at one in Pythia (A.3).

## Step 3: draft report (2026-11-21)
- Verdict: LIT summary confirmed (abstract quoted correctly). CLAIM-tmpcvuyr qualified/corrected: "repeated with modest loss" is wrong for Middle Repeat (catastrophic); "nearly interchangeable" overstated (authors: "uniformity (but not redundancy)", "performing different functions"); early layers sensitive confirmed (Fig 2), final layers asserted, not separately tested.
- Defeater (a): not met for Llama2/Mistral/BERT; partial pressure from Pythia-6.9B (A.5) and GSM8K under Parallel; early-vs-middle compared directly only for single-layer skip (Fig 2).
- Recheck: LIT-657 (InfoRidge, mid-depth peak), LIT-850 + THEORY-176 (stitching), LIT-678/THEORY-104, LIT-tmp40ldm (Lad et al., cited by this paper as closest).
