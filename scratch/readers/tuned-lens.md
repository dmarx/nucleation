# Reader notes: tuned-lens (LIT-tmp8pcca)

## Step 1: copy located (2026-11-21)

- https://arxiv.org/pdf/2303.08112 fetched 2026-11-21, PDF, 25 pages, arXiv v6 (11 Nov 2025).
  Kind: arXiv (lawful). Text extracted with pdftotext -layout; not committed.
- Authors on the PDF: Belrose, Ostrovsky, McKinney, Furman, Smith, Halawi, Biderman, Steinhardt
  (the LIT lists six; Biderman and Steinhardt are missing).

## Step 2: sections read (2026-11-21)

Read: abstract, sections 1-6, appendix A (captions), B and B.1 (captions), C and C.1 in full,
D.1, E (skimmed; static analysis, not on brief). Figures read from captions and text only.
Key points:
- Iterative inference framed via Jastrzebski et al. 2017; App. C reproduces Taylor-expansion argument;
  Pythia 6.9B residual-gradient cosine negative >=95% of the time, magnitude <=0.05.
- Trajectory "converge[s] smoothly", "each successive layer achieving lower perplexity" (Sec 1).
- Representational drift (Sec 3): covariance of hidden states drifts apart with layer separation;
  layer 4 outlier dims in Pythia 12B; "smooth representational drift with depth" (Fig 6);
  final-layer covariance changes sharply. Transfer penalties low near diagonal, rho=-0.78 with cov similarity.
- C.1: layer deletion in Pythia 6.9B: only the first layer is crucial.
- Causal: CBE, Spearman 0.89 (Pythia 410M L18); stimulus-response alignment higher at later layers.
- v6 notes earlier lenses "severely undertrained" (Muon); experiments not redone.

## Step 3: draft verdicts and recheck (2026-11-21)

- CLAIM-tmpcvuyr: supports the refinement side (smooth, monotone perplexity decline; residual-gradient alignment),
  and its App. C.1 adds a layer-deletion result (Pythia 6.9B: only layer 1 crucial) not in the claim. Qualifies:
  "refining one representation" — the paper says the basis drifts, hence a per-layer translator.
- CLAIM-tmp2yj4t: representational drift is smooth covariance drift growing with layer separation (Fig 6), plus
  outlier-dim onset at layer 4 and sharp final-layer change; consistent with copied-with-error accumulation but the
  paper measures no rate (no sqrt-depth test). Iterative-inference argument = systematic (loss-aligned) row.
- CLAIM-tmphedau: no bearing on the formal model; the paper's "drift" is a different (basis) notion.
- Recheck hits: THEORY-104, LIT-657 (early exit; overthinking-like result), LIT-850/THEORY-176/CLAIM-126/CLAIM-268
  (model stitching; paper frames lens as intra-model stitching), THEORY-018/THEORY-234 (affine/linear
  identifiability). Anthology: ANTH-LIT-569 is this paper; ANTH-LIT-570 the logit lens; ANTH-THEORY-020 layer deletion.
- Correction for LIT: authors include Biderman and Steinhardt; read v6 (2025-11-11).
