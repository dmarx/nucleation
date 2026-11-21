# Reader notes: semicontraction-depasquale (LIT-tmpru0xs)

## Step 1: copy located (2026-11-21)
- https://arxiv.org/pdf/2201.03103 -> HTTP 200, application/pdf, arXiv v3 (20 Dec 2022), 14 pages. Lawful (arXiv). Converted with pdftotext.

## Step 2: read in full (2026-11-21)
All 14 pages read (abstract, I-VII, appendices I-II, refs). Text extraction scrambles some equations; formulas reported only where legible.
Key points: Def 8 projection |||x|||proj,p = ||Pi_perp x||_p vs distance |||x|||dist,p = min_{u in K}||x-u||_p; Thm 16 duality; Thm 18 tau_q(K,A) = |||A^T|||proj,q = |||A|||dist,p (ergodic coeff = induced seminorm); Lemma 28 time-varying affine, sup_k tau < 1; Thms 29/30 cascade decompositions (invariance: x_par driven by x_perp; conservation: x_par autonomous, perp contraction perturbed by l*d_K(x_par,y_par)). Lit review: semicontraction lets distance grow along kernel directions. No noise, no information measure, no approximate invariance, no explicit statement of the limit value.

## Step 3: draft report (2026-11-21)
Verdict on characterization: partly confirmed, partly corrected. One theory (seminorms with kernel K) covers averaging (DeGroot) and Markov flows, related by duality, same tau_1. But it states only contraction of the part perpendicular to K; what the limit keeps is not stated, and the kernel part may grow; "kept exactly" needs the conservation property with a trivial parallel map, which the paper sets up (x_par autonomous) without saying so. No noise, information, approximate invariance.
Recheck extras: CLAIM-260, CLAIM-056, CLAIM-386, CLAIM-388, THEORY-661, QUESTION-221, THEORY-155, CLAIM-tmp4qvx2, LIT-tmpavt0i (= paper's ref [17]), LIT-070 (scrambling).
