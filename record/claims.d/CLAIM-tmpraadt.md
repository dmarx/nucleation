---
status: Active
title: 'Sampling the toy model of superposition''s tempered posterior exp(−nL) under Chen et al.''s N(0, 1) prior does not confirm the critical sample sizes the free-energy formula gives for the training chain: 5 → 5⁺ falls near n = 780, not 1,600–2,500, the first two steps have no crossing above n ≈ 1, and 5 → 6 falls near 270, not 601, which matches Chen et al.''s sampled 600–700 only because their likelihood carries a factor ½ that their formula does not'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Proposed to Active at the status review's ruling (the owner delegated
    these rulings): reproduced from the committed chains; the factor-of-
    one-half reading is hedged. It weakens what THEORY-1275's title says
    of the rising order, which THEORY-1275's note of 2026-11-22 records.
role: thesis
warrant: empirical
defeated_if: >-
  An independent sampler of the same target (population loss, N(0, 1)
  prior, exp(−nL) with L = E‖x − f‖²) placing the 5 → 6 occupancy
  crossing within 20% of 601 or the 5 → 5⁺ free-energy crossing above
  1,600; or a reading of Chen et al.'s App. F showing that their NUTS
  target had no factor ½, or that their formula's L does.
tags:
- mathematical-statistics
- learning-theory
- loss-landscapes
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-363
grounds:
- CASE-tmpgqbyq
- THEORY-1275
summary: >-
  The posterior half of [LEAD-175](../leads.d/LEAD-175.md), run in [CASE-tmpgqbyq](../cases.d/CASE-tmpgqbyq.md). It is the
  "posterior sampling across n that confirms the chain's critical sample
  sizes" that [QUESTION-363](../questions.d/QUESTION-363.md)'s note of 2026-11-06 asked for. Tempering and
  region-confined sampling with thermodynamic integration agree to 0.13
  nats and reproduce Table 1's learning coefficients. The formula's
  critical sizes for the chain 4⁺⁺⁻ → 4⁺ → 5 → 5⁺ (190, 370, 1,600–2,500)
  are not found. Their rising order survives only trivially, with the
  first two steps already settled at the prior. [THEORY-1275](../theory.d/THEORY-1275.md)'s statement
  that the posterior favours the 6-gon at n = 1,000 holds on either scale.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-tmpgqbyq — new, filed with this claim -->

# CLAIM-tmpraadt: Sampling the toy model of superposition's tempered posterior exp(−nL) under Chen et al.'s N(0, 1) prior does not confirm the critical sample sizes the free-energy formula gives for the training chain: 5 → 5⁺ falls near n = 780, not 1,600–2,500, the first two steps have no crossing above n ≈ 1, and 5 → 6 falls near 270, not 601, which matches Chen et al.'s sampled 600–700 only because their likelihood carries a factor ½ that their formula does not

## The claim

[THEORY-1275](../theory.d/THEORY-1275.md) computed the Bayesian antecedents of the training chain
4⁺⁺⁻ → 4⁺ → 5 → 5⁺ from Chen et al.'s formula
f_α(n) = nL_α + λ_α log n + c_α. It used Table 1's L, Table K.1's λ̂ and
Table C.2's constants c_α, which are the prior's −log φ at each critical
point alone. It found n ≈ 190, 370 and 1,600–2,500, rising with training.

**What sampling finds.** [CASE-tmpgqbyq](../cases.d/CASE-tmpgqbyq.md) sampled the target of that formula,
exp(−nL)·N(0, I), with L the population loss. Each region's free energy
was obtained by thermodynamic integration from the prior. Its log-odds
agree with a parallel-tempering run's occupancy to 0.13 nats rms, and the
local learning coefficients at n = 10,000 are 7.2, 8.5 and 8.6 for the
5-, 5⁺- and 6-gon, against Table 1's 7, 8.5 and 8.5. On this scale:

- 4⁺ is more probable than 4⁺⁺⁻ at every n sampled, from 0.5, and 5 than
  4⁺ from about n = 1. The chain's first two antecedents are settled by
  the prior's volumes, not at 190 and 370.
- 5⁺ overtakes 5 at n ≈ 780, not 1,600–2,500.
- 6 overtakes 5 at n ≈ 265–279, not 601.

**The scale.** Chen et al.'s likelihood (Eq. 3) is exp(−½‖x − f‖²). Their
NUTS runs (App. F) sample its posterior, exp(−(n/2)L_n)φ. Their formula
(App. F.1) uses nL with Table 1's L = E‖x − f‖², which has no ½. On the
NUTS scale, the sampled 5 → 6 is at n ≈ 530–560. That is consistent with
the 600–700 of their Fig. 2, which used finite datasets, and it is the
only one of the four steps the paper checked by sampling. The formula's
601 meets it only across the factor of two.

**What it changes.**

- **The posterior's favourite.** [THEORY-1275](../theory.d/THEORY-1275.md)'s "the posterior at n = 1,000
  favours the 6-gon" stands on either scale: the 6-gon holds 96% of the
  mass by n = 480 on the formula's scale.
- **The rising order.** [THEORY-1275](../theory.d/THEORY-1275.md)'s antecedent sizes, and the rising
  order they show, rest on the formula with prior-only constants. Sampling
  keeps the order only in the weak sense that the first two steps come
  first, at the prior. The order's support is therefore weaker than
  [THEORY-1275](../theory.d/THEORY-1275.md) says. Its note of 2026-11-06 already found the order
  fragile under the λ̂ spread.

## What it does not say

- **The finite-dataset posterior.** The target uses the population loss.
  Chen et al.'s NUTS posterior includes a dataset term this one leaves
  out.
- **The 4-gon family's critical points.** The 4-gon-family regions, as
  classified, are not dominated by their critical points at large n. Their
  free energies are those of Chen et al.'s regions W_{k,σ}, which their
  Fig. 2 counts, not of the critical points whose L_α the formula uses.
- **That Chen et al. erred.** The ½ is read from their Eq. 3, App. F and
  Table 1. A convention stated elsewhere in the paper, or in their code,
  could reconcile them. The record has not seen their code.
