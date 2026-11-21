# Reader notes: spectral-condition (LIT-tmpj34ir)

## Step 1: copy located (2026-11-21)
- https://arxiv.org/pdf/2310.17813 -> arXiv v2 (14 May 2024), PDF, 23 pages. Fetched without obstruction.

## Step 2: sections read
- Read in full: abstract, sec 1-8 (pp. 1-13), App. A (experimental details), App. B (tensor programs theory, Thm 1, Props 1-4, Thm 2), App. D (biases), App. E (natural norms). Skimmed App. C (empirical checks of Assumptions 1-3; restated assumptions only). References skipped.
- Condition 1: ||W_l||_* = Θ(sqrt(n_l/n_{l-1})) and ||ΔW_l||_* = Θ(sqrt(n_l/n_{l-1})), l = 1..L.
- Desideratum 1: ||h_l||_2 = Θ(sqrt n_l) and ||Δh_l||_2 = Θ(sqrt n_l), l = 1..L-1 (entries Θ(1)).
- Parametrization 1: σ_l = Θ(1/sqrt(n_{l-1}) min(1, sqrt(n_l/n_{l-1}))), η_l = Θ(n_l/n_{l-1}).
- Thm 1 (App B): μP satisfies Condition 1 for a.e. learning rate; unique stable abc-parametrization with this property.
- Sec 3.4: Condition 1 is "the unique maximal scaling"; ||ΔW_l||=0 at layers 2..L also satisfies Desideratum 1.
- Nothing on time scales, per-layer rates across training time, or equal rates across singular directions. Updates are low stable rank (Fig 1, Lemma 1) -- argument is about the top singular direction / alignment.
- Big-Θ hides depth, learning-rate schedule, global prefactor (sec 2).

## Step 3: draft report -- in final reply to the caller.

## Step 3: recheck and draft (2026-11-21)
- Recheck hits not in CLAIM-tmpqwoxz grounds: THEORY-212 (Dominé et al., lazy-to-rich via relative layer scale, LIT-943), THEORY-086 (kernel regime eigenspace rates), THEORY-1874 (fine-tuning updates near low-rank). No held THEORY on μP, spectral norm scaling or this work.
- Verdict: characterization confirmed in substance (Condition 1 = sqrt(fan-out/fan-in) on ||W|| and ||ΔW||; equivalence to μP, Thm 1). Qualify CLAIM-tmpqwoxz: the paper's equal-order statement is per step at each layer in width, not a statement about rates or time scales; nothing on singular directions moving equally (bears on CLAIM-tmpmugkp: none; paper's updates are low stable rank, uses spectral normalization of gradient (eq 17), not polar factor).
- Draft report returned to caller.
