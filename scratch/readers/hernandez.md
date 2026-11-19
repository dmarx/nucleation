# Reader notes: hernandez (Hernandez, Kaplan, Henighan, McCandlish 2021, "Scaling Laws for Transfer", arXiv 2102.01293)

## 2026-11-19: copy located and read
- arXiv PDF https://arxiv.org/pdf/2102.01293 (v1, 2 Feb 2021, 19 pp.), fetched without obstacle; text extracted with pdftotext (kept outside the repo).
- Read in full: abstract, §1-7, limitations, appendices A-G. Figures known from captions and axis text only.
- Authors confirmed from the title page: Danny Hernandez, Jared Kaplan, Tom Henighan, Sam McCandlish (OpenAI).
- Core: D_T = k (D_F)^alpha (N)^beta in the low-data regime (D_F <= 10% of D(N)); text->python k=1.9e4, alpha=0.18, beta=0.38; text+code->python k=2.1e5, alpha=0.096, beta=0.38.
- D_T is defined against a from-scratch model of the same size; pretraining compute is explicitly ignored ("Ignoring pre-training, fine-tuned models are more compute efficient").
- Ossification: small models in the high-data regime do worse after pretraining.
