---
number: 907
status: Proposed
formerly:
- CLAIM-tmpmov06
title: 'For three evaluative contexts whose transports are derived by orthogonal fit on the commitments each overlap shares, contexts that represent one configuration in different local frames have trivial holonomy, so perspectival plurality does not imply curvature; when every overlap fits exactly and determines its fit, the holonomy is trivial exactly when the three representations glue into one configuration up to frames, so a nontrivial one is a gauge-invariant discrepancy among the contexts'' own comparisons, and it occurs; an overlap that does not span leaves the holonomy to the modeller'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-067 by delegation.
    The proof is the assistant's; the constructions are checked numerically
    under scratch/studies/lead-067/ (18 tests, and the study of the case
    filed beside it).
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof of the null, of covariance, or of the gluing
  criterion, or a counterexample to them: three contexts with exact,
  determined overlap fits whose representations glue into one
  configuration up to O(d) frames and whose derived holonomy is not the
  identity, or the converse. A finding that real evaluative contexts do not
  have spanning overlaps, or that their changes of coordinates are not
  orthogonal, limits where the claim applies and does not defeat it.
tags:
- mathematics
- ethics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
bears_on:
- QUESTION-130
complements:
- CLAIM-495
- CLAIM-148
---

<!-- inactive-ok-file: LIT-038 — Rejected; cited as the record's rejection that this claim's last clause makes exact -->
<!-- inactive-ok-file: CASE-339 — Proposed; the study filed with this claim -->

# CLAIM-907: For three evaluative contexts whose transports are derived by orthogonal fit on the commitments each overlap shares, contexts that represent one configuration in different local frames have trivial holonomy, so perspectival plurality does not imply curvature; when every overlap fits exactly and determines its fit, the holonomy is trivial exactly when the three representations glue into one configuration up to frames, so a nontrivial one is a gauge-invariant discrepancy among the contexts' own comparisons, and it occurs; an overlap that does not span leaves the holonomy to the modeller

## The claim

This is A19 §8's finite construction, which [QUESTION-130](../questions.d/QUESTION-130.md) names as what would count as an answer, built as [LEAD-067](../leads.d/LEAD-067.md) asks.

**The setting.** There are three contexts, A, B and C. Context c holds a vector xₙᶜ ∈ ℝᵈ for each commitment n in its set S_c, in its own coordinates. The overlap of a and b is S_ab = S_a ∩ S_b. A change of c's local coordinates is xᶜ ↦ g_c xᶜ with g_c ∈ O(d). That change preserves every inner product c holds, so it preserves every comparison c makes among its commitments, and it is a gauge in [CLAIM-148](CLAIM-148.md)'s sense.

**The transport is derived, not chosen.** T_ba is the orthogonal map that best carries a's representations of the shared commitments onto b's:

T_ba = argmin over R ∈ O(d) of Σ_{n ∈ S_ab} ‖R xₙᵃ − xₙᵇ‖².

This is orthogonal Procrustes. Its minimizer is the polar factor of M_ab = Σ xₙᵇ xₙᵃᵀ, and it is unique exactly when M_ab is nonsingular. Call the overlap determined when it is. The holonomy at A is H_A = T_AC T_CB T_BA. Under a change of frames, M_ab goes to g_b M_ab g_aᵀ. So T_ba goes to g_b T_ba g_aᵀ, and H_A goes to g_A H_A g_Aᵀ. The holonomy's class functions, such as ‖H − I‖ and its eigenvalue angles, are therefore invariant.

**(i) The null.** Suppose each context represents one configuration w in its own frame, so that xₙᶜ = g_c wₙ, with the g_c arbitrary and different. Then M_ab = g_b K_ab g_aᵀ, with K_ab = Σ wₙwₙᵀ. The overlap is determined exactly when the shared commitments span ℝᵈ, and then T_ba = g_b g_aᵀ. Hence H_A = g_A g_Cᵀ g_C g_Bᵀ g_B g_Aᵀ = I. The contexts disagree in every coordinate of every shared commitment, and the holonomy is still trivial. So perspectival plurality does not imply nontrivial curvature. That is the first target of [QUESTION-130](../questions.d/QUESTION-130.md), met by construction.

**(ii) The gluing criterion.** Suppose every overlap fits exactly (T_ba xₙᵃ = xₙᵇ on S_ab) and is determined. Then the three representations are one configuration in three frames exactly when H_A = I.

- If they are, (i) gives H_A = I.
- Conversely, suppose H_A = I. Set g_A = I, g_B = T_BA and g_C = T_CB T_BA, and put wₙ = g_cᵀ xₙᶜ for any context c that holds n.
  - On S_AB and S_BC this is well defined by the exact fits.
  - On S_CA it needs T_AC = T_AB T_BC, which is H_A = I.

So, under exact and determined overlaps, a nontrivial holonomy certifies that no single configuration realizes all three contexts' comparisons together, although each context is coherent and each pair agrees on what it shares. The certificate is gauge-invariant and not an artefact of coordinates. It also predicts a discrepancy. A commitment n that B holds and A does not can be imported into A directly, as T_AB xₙᴮ, or by way of C, as T_AC T_CB xₙᴮ = H_A T_AB xₙᴮ. The comparison A then makes of it with any commitment m that A holds, ⟨xₘᴬ, ·⟩, is gauge-invariant and depends on the route unless H_A fixes the imported vector.

**(iii) It occurs, with no transport specified.** Take d = 2. Each overlap is a pair of commitments of the same shape in both contexts that hold it, so every fit is exact and determined. Inside context c, the pair c shares with one neighbour and the pair it shares with the other sit at a relative angle θ_c. That angle is a comparison c itself holds: the cosine between corresponding commitments of the two pairs is cos θ_c. The derived holonomy is then a rotation by θ_A + θ_B + θ_C, up to the sign an orientation-reversing frame gives it. It is trivial only when the sum vanishes mod 2π. Each context is internally consistent and every pair of contexts agrees exactly, yet the three comparisons cannot be realized in one plane.

**(iv) Underdetermination returns the choice to the modeller.** If an overlap does not determine its fit, the minimizers form a family that fits equally well. For example, one shared commitment u in ℝ³ admits T·Rot_u(φ) for every φ. The holonomy then runs over a range as the free part is chosen. In the worked example, ‖H − I‖ runs from 0.006 to 2.83 with every fit exact. This is the arbitrariness of [LIT-038](../literature.d/LIT-038.md) ([NOTE-050](../notes.d/NOTE-050.md)), stated exactly: the connection counts as derived only where every overlap is determined.

Every part is checked numerically in scratch/studies/lead-067/: 18 tests, and the study filed as [CASE-339](../cases.d/CASE-339.md). The study also gives a noise null for a test on measured representations, and a curved-chart example whose holonomy matches a spherical excess.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

## What it does not say

- **That evaluative contexts have such representations.** That commitments are vectors, that a context's changes of coordinates are orthogonal, and that overlaps are rich enough to determine the fit are modelling assumptions. Whether any measured contexts meet them is the open part of [QUESTION-130](../questions.d/QUESTION-130.md). With a larger gauge group (GL(d), or affine maps), the fit changes, and only the null carries over unchanged.
- **That a nontrivial holonomy is normative curvature.** By (ii), it is a discrepancy among the contexts' comparisons. That discrepancy may be an error in one of them. It may be "substantive state evolution" if the contexts were measured at different times. Or it may be a change of viewpoint that alters what is evaluated, which [QUESTION-130](../questions.d/QUESTION-130.md) excludes from gauge. The holonomy says that the three cannot all hold. It does not say which fails or why.
- **That the obstruction is [CLAIM-038](CLAIM-038.md)'s.** What fails to glue here is the configuration up to frames, not a set of local judgments of fixed value. Whether the two obstructions coincide in some formulation is not settled here.
- **That a nonzero measured holonomy is a finding.** With noisy representations, the holonomy of the null is not I. With few anchors per overlap, noise can flip a fit's orientation and give ‖H − I‖ ≥ 2 (the study). A test needs the noise null.
- **Anything new in mathematics.** The covariance and the gluing criterion are the standard fact that an O(d)-valued edge assignment on a graph comes from vertex frames exactly when its holonomy around every cycle is trivial; the three contexts' graph has one cycle. What is the record's own is deriving the connection by fit on shared commitments, and the conditions under which it counts as derived.
