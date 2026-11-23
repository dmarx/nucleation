# LEAD-073 progress

- Lead: LEAD-073 (measure NOTE-746's M, N and Γ_q in released language models for relations where linearity has been reported).
- Branch: claude/lead-073-pragmatic-geometry (cut from origin/staging 6e3085b75).

## Task as understood

Run forward passes of a small open model on CPU (GPT-2 small, or a small Pythia), compute F, G, M = Im(P_F P_G), N = ker(P_F P_G)^⊥ (NOTE-746, Eq. 7), and for relations where linearity has been reported estimate Γ and Γ_q = Im(A_qᵀ P_Γ) and test Γ ⊆ N, Γ_q ⊆ M with a tolerance stated in advance (QUESTION-149's "What would answer it"). File an executed-study CASE (proposed-study if blocked), CLAIMs, dated notes, changelog fragment.

## Choices made

- Access: torch and transformers absent; huggingface.co reachable (2026-11-23). Rather than install torch, the forward passes, safetensors reader and BPE tokenizer were written in numpy (lmnp.py). Validated by per-token NLL on English text (2.64 and 3.25 nats) and causality tests on tiny random models.
- Models: GPT-2 small and Pythia-70m (both, since the lead allows either and they differ in tied vs untied unembeddings). Weights in the session scratchpad only.
- Representation: final-layer-norm output at the last position (what enters the logits). Relations: city in country, country language, country capital (Hernandez et al.'s kinds), one-token replies.
- Γ = span of reply differences; A_q by ridge (λ = 1e-2 relative); Γ_q = Im(A_qᵀ P_Γ).
- Tolerances fixed in PREREG.md before the first real run (rtol 1e-3 primary; pass if ≤1% of the worst direction is outside). A wider sweep was run afterwards and is labelled post hoc.
- Two readings filed as alternatives (exact: trivially yes; tolerance: not settled). Lean: the exact reading, for the question as worded.

## Done

- Step 1 (held check): nothing in record/ files a measurement. LEAD-073 is cited only by the backlog curation of 2026-11-19; QUESTION-149 (Open) asks for exactly this measurement and holds no answer. Not held.
- Code and 15 passing tests (test_geometry.py); PREREG.md committed before the run.
- results/gpt2.json, results/pythia-70m.json (pre-registered), results/*_sweep.json (post hoc), results/summary.md.
- CASE-tmpc7lbu; CLAIM-tmp41bjo (layer-norm span); CLAIM-tmp58rtz and CLAIM-tmpdltg3 (alternative readings).
- Dated notes of 2026-11-23 on LEAD-073, QUESTION-149, QUESTION-027, NOTE-746; changelog fragment record/changelog.d/lead-073.md. Frontmatter/title/H1/excuse checks pass.

## Next

- Nothing on the branch. The lead opens the PR. For the owner: choose between the two readings; whether to file the approximate-equivalence form of QUESTION-149 as its own question; larger models or a middle-layer variant only if the second reading is chosen.
