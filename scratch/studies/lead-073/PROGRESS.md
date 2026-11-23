# LEAD-073 progress

- Lead: LEAD-073 (measure NOTE-746's M, N and Γ_q in released language models for relations where linearity has been reported).
- Branch: claude/lead-073-pragmatic-geometry (cut from origin/staging 6e3085b75).

## Task as understood

Run forward passes of a small open model on CPU (GPT-2 small, or a small Pythia), compute F, G, M = Im(P_F P_G), N = ker(P_F P_G)^⊥ (NOTE-746, Eq. 7), and for relations where linearity has been reported estimate Γ and Γ_q = Im(A_qᵀ P_Γ) and test Γ ⊆ N, Γ_q ⊆ M with a tolerance stated in advance (QUESTION-149's "What would answer it"). File an executed-study CASE (proposed-study if blocked), CLAIMs, dated notes, changelog fragment.

## Choices made

## Done

- Step 1 (held check): nothing in record/ files a measurement. LEAD-073 is cited only by the backlog curation of 2026-11-19; QUESTION-149 (Open) asks for exactly this measurement and holds no answer. Not held.

## Next

- Check torch/transformers and huggingface.co reachability.
