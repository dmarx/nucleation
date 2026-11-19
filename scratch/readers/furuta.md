# Reader notes: furuta (Furuta, Minegishi, Iwasawa, Matsuo, arXiv 2402.16726)

## 2026-11-19 Copy located and read
- arXiv PDF (v4, TMLR 11/2024) and arXiv LaTeX source fetched, HTTP 200, no check. Full text read (main body), appendices C, F, M, N, K, L read; others skimmed.
- Transfer design: a module "pre-grokked" on one op is frozen (embedding W_E alone, or "Transformer" = all weights except W_E and W_U) and a fresh model with that module is trained on another op. Cost = smallest train fraction r (0.3..0.9) at which grokking occurs within 3e5 steps (Table 1), plus test-accuracy-vs-steps curves (Figs 2, 9). p=97, 1-layer transformer, 3 seeds.
- Headline: transfer helps only for some pairs ("limited to specific combinations, such as from elementary arithmetic to linear expressions"); for higher-order polynomials pre-grokked modules "could not accelerate, and they even prevent grokking".
- Doubts: no accuracy threshold for "grokked" stated; pre-grokking fraction not stated; no matched-first-stage or memorizing-vs-generalizing comparison; the only non-learned control is a frozen random embedding (App. F, elementary arithmetic only).

## 2026-11-19 Table 1 tabulated, bearings searched
- Table 1 read from the arXiv LaTeX source (the PDF text garbles check/cross marks). 16 downstream ops x 6 frozen-source conditions vs scratch min fraction: my tally 24 cells lower, 20 equal, 52 higher-or-never. Polynomial rows only (10 ops): 4 lower, 18 equal, 38 higher-or-never. Floor at r=0.3 (lowest tested) hides gains where scratch already groks at 0.3.
- Reader's observation (not the authors' framing): the factorizable rows (a+b)^n, (a-b)^n are literally h(g(a,b)) with g an elementary op. Transferring g's own pre-grokked module gives no gain at floor, and the frozen body often blocks grokking ((a+b)^3: scratch 0.3, add-body never; (a-b)^3: scratch 0.5, sub-embedding 0.6, sub-body never).
- Lead design: (a) yes, sample cost as min train fraction on a 0.1 grid, steps curves qualitative; first-stage cost not counted. (b) no matched first stage, no memorizing/shortcut arm; only source-op differences and a frozen random embedding (App. F, elementary from scratch). (c) transplant (freeze-and-reuse) only; no ablation of the transplanted module.
- Not in the record on main (no LIT); named only in scratch/readers/search.md, accurately.
