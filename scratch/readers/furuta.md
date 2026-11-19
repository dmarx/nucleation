# Reader notes: furuta (Furuta, Minegishi, Iwasawa, Matsuo, arXiv 2402.16726)

## 2026-11-19 Copy located and read
- arXiv PDF (v4, TMLR 11/2024) and arXiv LaTeX source fetched, HTTP 200, no check. Full text read (main body), appendices C, F, M, N, K, L read; others skimmed.
- Transfer design: a module "pre-grokked" on one op is frozen (embedding W_E alone, or "Transformer" = all weights except W_E and W_U) and a fresh model with that module is trained on another op. Cost = smallest train fraction r (0.3..0.9) at which grokking occurs within 3e5 steps (Table 1), plus test-accuracy-vs-steps curves (Figs 2, 9). p=97, 1-layer transformer, 3 seeds.
- Headline: transfer helps only for some pairs ("limited to specific combinations, such as from elementary arithmetic to linear expressions"); for higher-order polynomials pre-grokked modules "could not accelerate, and they even prevent grokking".
- Doubts: no accuracy threshold for "grokked" stated; pre-grokking fraction not stated; no matched-first-stage or memorizing-vs-generalizing comparison; the only non-learned control is a frozen random embedding (App. F, elementary arithmetic only).
