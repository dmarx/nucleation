# Reader notes: tp6-depth (LIT-tmp4peep)

## Step 1: copy located (2026-11-21)
- https://arxiv.org/pdf/2310.02244 -> HTTP 200 application/pdf, arXiv v5 (12 Oct 2023). Lawful (arXiv). Converted with pdftotext -layout.

## Step 2: sections read (2026-11-21)
Read: abstract, §1 (Table 1, eq.1, block-depth-1 bullets, §1.1 phase list, fn.5), §1.3, §2, §3 (linear warm-up, SGD vs SignSGD/Adam), §4 skimmed (TP setup, Prop 4.2), §5, §6 (Def 6.1, 6.2; setup), §7 in full (Claims 7.1-7.6, Def 7.6 feature diversity), §8, §9 in full, §10.2-10.4 text. Appendix F.1 forward SDE skimmed. Rest of appendices skipped.
Key: Table 1 Depth-µP SGD: a/√depth, η; Adam: a/√depth, η/√depth. p.3: "contribution of the update of each residual block is Θ(1/L) ... highly correlated, so they sum up to Θ(1)". Init: Θ(1/√L) each, independent, sum Θ(1). Claim 7.2: stable & nontrivial iff α+γ=1. Claim 7.5 Depth-µP α=γ=1/2 unique, κ=1/2. F.1: dx = √dλ (Gaussian noise) + dλ (drift).
