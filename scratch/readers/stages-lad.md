# Reader notes: stages-lad (LIT-tmp40ldm)

- 2026-11-21: located https://arxiv.org/pdf/2406.19384 (arXiv, lawful), fetched as PDF, text via pdftotext. Reading.
- Copy read is v3 (16 Jun 2025), 26 pp. Read in full: abstract, secs 1-6 (pp. 1-9), appendix A.1-A.11 text and captions; references skimmed. Fig. 5 (p. 4) read from a rendered image.
- Interventions (drop, adjacent swap) on GPT-2 x4 and Pythia x4 only; stage signatures on 16 models in 5 families (124M-6.9B).
- "relative accuracy" = fraction of top-1 predictions matching the unintervened model (p. 3); 72-95% given in abstract only, not derived in body. Fig 5 by eye: middle ~0.8-0.95, first layer ~0, last-layer swap collapses in Pythia.
- Swaps less harmful than drops (p. 3-4). First layer = "extension of the embedding" (p. 4).
- A.4 (p. 19): stage 2 MLPs show iterative inference; stage 3 MLPs "specialized"; change ~halfway.
- Limitations (p. 9): "Stage boundaries are approximate"; conclusion: "ordered composition of specialized computational regimes".
- Recheck hits: THEORY-1033, THEORY-1030 (Geva, LIT-1576), THEORY-1011 (ROME), THEORY-1024/1026 (Hase), THEORY-1226 (J-space middle band). No hit for prediction/suppression neurons, Gurnee universal neurons, logit-lens LIT, Veit ensembles.
- Draft report next.
- Report drafted and returned 2026-11-21. Verdict: characterization confirmed in substance, with corrections (interventions on 2 families only; "relative accuracy" is agreement with the unintervened model; stage 3 is specialized, not interchangeable; stages hypothesized).
