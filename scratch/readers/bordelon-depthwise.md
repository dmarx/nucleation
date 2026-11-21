# Reader notes: bordelon-depthwise (LIT-tmpu5m2v)

## Step 1: copy located (2026-11-21)

- https://arxiv.org/pdf/2309.16620 — arXiv, author preprint; HTTP 200, PDF,
  resolves to v2 (8 Dec 2023). Text extracted with pdftotext (not committed).

## Step 2: sections read (2026-11-21)

Read: abstract, §§1–6 and Table 1, eq. 1–7; App. C, D.1–D.2, E.1–E.7 (main
derivation), H intro, I, J, K.2.1, K.4, K.5, L, M (other depth limits,
α ≥ 1/2, "ODE" α=1 vs "SDE" α=1/2). Skimmed: D.3 path integral, F, G, H.1–H.2,
experiment details A–B.

Key finds:
- eq. 3: η = η0 γ0² N, no depth factor in the LR for α = 1/2.
- eq. 17–18: dW/dt ∝ 1/√(LN); per-block forward = (1/√(NL)) W(0)φ [random]
  + (η0γ0/L)∫… [learned].
- E.3: random sources "uncorrelated across layers" → Brownian motion;
  learned double sum O(1) because skips give long-range gradient
  correlations across layers.
- E.4: "feature learning term ... adds a drift term ... compared to the
  diffusion term from the initial weights."
- K.5: "random (uncorrelated across layers) field χ has a scale of 1/√L ...
  feature learning update ... (strongly correlated across layers) has the
  correct 1/L scaling".
- M: any α ≥ 1/2 works with η = η0γ0² L^(2α−1) N; α=1 "ODE", α=1/2 "SDE".

## Step 3: draft verdict (2026-11-21)

- CLAIM-tmp2yj4t rows (a) diffusive and (b) systematic 1/L: confirmed in the
  paper's own words (E.3, E.4, K.5). Defeater (b) not met for this paper.
- Qualification: 1/√L is the smallest α that keeps the random part O(1);
  App. M allows any α ≥ 1/2 with η ∝ L^(2α−1); α = 1 "ODE" (diffusion
  vanishes). The learned per-block O(1/L) holds for every α.
- LR at α = 1/2 has no depth factor (eq. 3); per-block weight change
  O(1/√L) (eq. 17), contribution to h O(1/L) after the branch scale.
- No-skip contraction (THEORY-2041): not addressed; paper says only that
  non-residual networks' gradients are independent across layers (E.3) and
  finite-width variances accumulate linearly in L (H).
- Recheck: CLAIM-tmpqwoxz (γ0 lazy limit, App. J/M), THEORY-187/LIT-864
  (LR falls with depth in deep linear nets) are bearing entries.
