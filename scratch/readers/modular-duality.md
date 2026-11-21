# Reader notes: modular-duality (LIT-tmpp6b7j)

## Located copy (2026-11-21)
- https://arxiv.org/pdf/2410.21265 — arXiv, author-deposited preprint; v2 (6 Dec 2024), 12 pp PDF. Fetched without obstruction.

## Sections read
- All of it: abstract, §1-7, Table 1, references. Nothing skipped.
- Linear.dualize = sqrt(dout/din) x UV^T (Ex. 3, Ex. 5, Table 1).
- Prop. 1: steepest-descent step = -(||g||_dual / lambda) x dualize(g); eq. (2) shows fixed LR x dualize.
- NS (§5.3, eq. 15): X0 = G/||G||, X <- 1.5X - 0.5XX^TX; converges to UV^T as t -> inf; no finite-step error bound; zero singular values stay zero; tuned higher-order coefficients mentioned.
- Composition (Def. 6, eq. 11): masses apportion; dualize of composite scales each by mass_i/M.mass, first by 1/M2.sensitivity.
- Nothing on order or speed of learning of directions. §6.4: "all singular values have the same magnitude".
