# Reader notes: hernandez (Hernandez, Kaplan, Henighan, McCandlish 2021, "Scaling Laws for Transfer", arXiv 2102.01293)

## 2026-11-19: copy located and read
- arXiv PDF https://arxiv.org/pdf/2102.01293 (v1, 2 Feb 2021, 19 pp.), fetched without obstacle; text extracted with pdftotext (kept outside the repo).
- Read in full: abstract, §1-7, limitations, appendices A-G. Figures known from captions and axis text only.
- Authors confirmed from the title page: Danny Hernandez, Jared Kaplan, Tom Henighan, Sam McCandlish (OpenAI).
- Core: D_T = k (D_F)^alpha (N)^beta in the low-data regime (D_F <= 10% of D(N)); text->python k=1.9e4, alpha=0.18, beta=0.38; text+code->python k=2.1e5, alpha=0.096, beta=0.38.
- D_T is defined against a from-scratch model of the same size; pretraining compute is explicitly ignored ("Ignoring pre-training, fine-tuned models are more compute efficient").
- Ossification: small models in the high-data regime do worse after pretraining.

## 2026-11-19: quotes checked, bearings searched
- 50 quotes checked by script against the extracted text; all match (one hyphenation split shortened).
- Recomputed §6.2 from eq. 1.1: GPT-3 size, 1 char -> ~3.6e8 chars (paper 3.7e8); 300 chars x2.8; text+code ~3.9e9 (paper 4.1e9), x1.7. Consistent.
- Fig. 1's "~1000x" at 40M, 3e5 chars is read off the curve; eq. 1.1 gives ~475x there. A factor-of-two gap between fit and the labelled point, not explained.
- Not in the record: no LIT for 2102.01293; LEAD-tmpjdtrl lists it as unread.
- Bearings: CLAIM-756 (premise in cost terms, but pretraining cost explicitly not counted, so weaker than Hu et al. on that axis), CLAIM-758 / CLAIM-754 (ossification: same pretraining lowers cost at small D_F, raises it for small models at large D_F), CLAIM-303 / CLAIM-761 (pretraining cost set aside by reuse), THEORY-tmpw8s3h (ULMFiT, same measure: from-scratch data equivalent), THEORY-tmpd6smn (code mix), QUESTION-039 (background only).
- No order comparison at fixed total data; no seeds stated; pretraining length not stated.
