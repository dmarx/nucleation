# LEAD-073: tolerances stated before the first real run

Written and committed on 2026-11-23, after the tests on tiny random models
passed and before `measure.py` was run on any released model. QUESTION-149
asks for "a tolerance stated in advance"; these are those tolerances.

## Quantities (NOTE-746)

- F: the row span of f(x), the final-layer-norm output at the last position,
  over all context vectors gathered (random token strings, the model's own
  samples from the end-of-text token, and the relation prompts).
- G: the row span of the pivoted unembeddings g(y) − g(y₀) over the whole
  output vocabulary (equivalently, of the centred unembedding matrix).
- M = Im(P_F P_G), N = ker(P_F P_G)^⊥ (Eq. 7).
- Γ for a relation: the span of g(y) − g(y′) over its one-token replies.
- A_q: ridge fit of P_Γ f(s ⌢ q) = P_Γ A_q f(s) + a_q (Definition 9), ridge
  λ = 1e-2 relative to the mean squared singular value of the centred inputs.
- Γ_q = Im(A_qᵀ P_Γ) (Theorem 14).

## Tolerances

- **Span rank**: a direction is in a numerical span when its singular value
  exceeds rtol × the largest. Primary rtol = 1e-3; sensitivity runs at 1e-2
  and 1e-4. Reported at all three; the verdict is the primary's.
- **M and N**: principal cosines between F and G above 1e-3.
- **Containment S ⊆ T passes** when the worst direction of S has at most
  1% of its squared norm outside T (largest principal angle at most
  about 5.7°).
- **Logit visibility** (descriptive, not a test): a direction of F whose
  token-spread of logits is below 1e-2 of the most visible direction is
  "nearly invisible"; the share of Γ_q's operator energy there is reported.

## What would count

- Both containments pass at the primary tolerance for a relation: the
  relation's linearity, if present, is of the kind Theorem 14 makes shared
  by every distribution-equivalent model (for exact equivalence).
- Γ_q fails Γ_q ⊆ M with a substantial share outside M: the D.1 worry is
  live for that relation.
- Separately, whether the relation is linear at all in the model is read
  from the leave-one-out R² of the fit and the leave-one-out agreement of
  the linear probe with the model's own choice among the replies. Theorem 14
  is conditional on linearity; it says nothing for a relation the model does
  not represent linearly.
