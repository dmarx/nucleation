---
status: Read
paper: 'LIT-tmp7sngn'
title: 'Chesson — Ecological Niches and Diversity Maintenance'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 from the publisher's own open-access PDF
    (https://www.intechopen.com/chapter/pdf-download/21528, 20 pages,
    pp. 43–62, CC BY 3.0), text extracted with pdftotext. Table 1 (p. 45)
    and eq. (1) (p. 47) lost their Greek letters in extraction and were
    read from the pages rendered as images. Read: §§1–5 and the captions
    of Figs. 1–4; the reference list was read for the works cited in §2.1
    only. No number was taken from a figure. Read as the stand-in for
    Chesson (1990), LIT-1826, Unfetched (ADR-114). Checked by a record
    script (scratch/studies/lead-196/chesson_overlap.py, 51 tests):
    Table 1's ρ, s and κ against the fast-resource Lotka–Volterra
    reduction, eq. (1), and the invasion growth of a rare species against
    a lone resident in the full consumer–resource model.
date: '2026-11-22'
summary: >-
  A review chapter. Chesson restates his 1990 reworking of MacArthur's
  consumer–resource model: the competition-coefficient ratio α_ij/α_jj is
  the fitness ratio κ_j/κ_i times a niche overlap ρ, a weighted cosine of
  the two consumption vectors, so two species coexist, each recovering
  from low density, when ρ < κ₁/κ₂ < 1/ρ. Neutral models are ρ = 1 with
  equal κ. Predators extend ρ and κ as apparent competition, and the κ
  ratio organizes the chapter's conservation advice.
---
<!-- inactive-ok-file: LIT-1826 LIT-1219 — Unfetched and Unavailable; the 1990 paper this reading stands in for, and Chesson's 2000 review the chapter cites as [5], not read -->

# NOTE-tmp6d961: Chesson — Ecological Niches and Diversity Maintenance

## Contribution

A short review of how coexistence theory separates two kinds of
similarity between species, worked through MacArthur's consumer–resource
model "as reworked by Chesson [5, 28]" (p. 44). Reference [28] is
Chesson (1990), [LIT-1826](../literature.d/LIT-1826.md), and [5] is Chesson (2000), [LIT-1219](../literature.d/LIT-1219.md). The
chapter gives, in one table, the overlap and fitness measures that
the 1990 paper defines for this model, then extends them to predators
and to variation in time and space, and draws conservation advice.

## Key results

- **The model** (Table 1, p. 45). Consumers: (1/N_j) dN_j/dt =
  Σ_l c_jl R_l v_l − μ_j. Resources: (1/R_l) dR_l/dt =
  r_l^R (1 − α_l^R R_l) − Σ_j N_j c_jl, with α_l^R = 1/K_l^R.
- **The measures** (Table 1). Sensitivity s_j = √(Σ_l c_jl² v_l K_l^R /
  r_l^R). Average fitness κ_j = (Σ_l c_jl K_l^R v_l − μ_j)/s_j, "Harvesting
  ability" less "Maintenance requirement", over sensitivity. Overlap
  ρ = Σ_l c_jl v_l K_l^R c_kl / r_l^R, divided by s_j s_k.
- **The reduction** (p. 46): "when resource dynamics are fast relative to
  consumer dynamics ... the MacArthur consumer-resource model reduces to
  the Lotka-Volterra competition model defined by these competition
  coefficients".
- **Eq. (1)** (p. 47): κ_j ρ / κ_i = α_ij / α_jj, with ρ "on a scale from 0
  to 1". "The difference in the heights of the consumption rate curves
  does not affect the overlap, but is a factor explaining the difference
  between the fitnesses, κ." Worked: "if ρ = 2/3, then the fitness ratio
  needs to be more than 3/2, rather than just more than 1."
- **Eq. (2)** (p. 48): two species coexist when ρ < κ₁/κ₂ < 1/ρ: "the more
  similar the species are in resource use (the closer ρ is to 1), the
  more similar they have to be in average fitness for coexistence to
  occur."
- **Feedback loops** (p. 48): "it is separation of these feedback loops
  that makes it possible for intraspecific competition to exceed
  interspecific competition, the key to coexistence. With the MacArthur
  model, the measure ρ is a specific measure of the degree of separation
  of those feedback loops."
- **Stable coexistence** (§2.2, p. 49) is recovery from low density, not a
  stable equilibrium: "the requirement is recovery of each species from
  low density, which is fully compatible with fluctuating coexistence".
  Neutral models have equal κ and every ρ = 1, so expression (1) equals 1,
  and "there is no tendency for either species to increase from low
  density".
- **Predators** (§2.3, pp. 50–52). With predators the coefficients become
  coefficients of density dependence, "the relationship (1) between
  competition coefficient ratios, fitness ratios and niche overlap still
  holds", and "the reciprocal of the renewal rate of a resource weights
  its importance in the overlap measure" (p. 52).
- **Supply** (§3, p. 54): "ρ would decrease with an increase in the
  carrying capacity of a resource that only one species uses."

## Assumptions

- Linear consumer responses and logistic resources; per-capita growth
  rates linear in densities (§3, p. 53).
- The Lotka–Volterra reduction assumes fast resources. The chapter does
  not state that it also needs every resource to stay positive.
- Eqs. (1) and (2) are for two species. That the findings "generalize to
  others" is cited to [5] and [29] (Haygood), not shown.
- Populations closed on an ecological timescale, for κ to be meaningful
  (§2, p. 44).

## Concepts

- **Average fitness κ**: a species' adaptedness relative to its guild, not
  an individual's or a genotype's fitness (§2, p. 44).
- **Niche overlap ρ**: similarity in way of life, measured as the
  separation of feedback loops; in MacArthur's model, similarity of
  resource use.
- **Two sorts of similarity** (p. 48): similarity in κ favours
  coexistence; similarity in niche, high ρ, constrains how different the
  κ values can be.
- **Stable coexistence** as recovery from low density, beside neutral
  coexistence, and beside fluctuation-dependent coexistence (§2.2).
- **Apparent competition**: feedback through shared predators, entering ρ
  and κ like feedback through resources (Holt).

## Connections

- **What it restates of Chesson (1990), [LIT-1826](../literature.d/LIT-1826.md).** The overlap measure
  and fitness measure for MacArthur's model, in its Lotka–Volterra
  reduction, and the two-species coexistence condition. It does not
  restate whatever else the 1990 paper's measures of association
  between utilization functions cover, nor its derivations.
- **Letten, Ke and Fukami**, [LIT-1237](../literature.d/LIT-1237.md) ([NOTE-1377](NOTE-1377.md)), use ρ = √(α₁₂α₂₁/α₁₁α₂₂)
  and f₂/f₁. For MacArthur's model that ρ is this Table 1's ρ, and their
  fitness ratio is κ₂/κ₁ (checked by the record script).
- **Marsland, Cui and Mehta**, [LIT-1230](../literature.d/LIT-1230.md) ([NOTE-1352](NOTE-1352.md)): the reduction holds
  only while every resource stays positive, which the chapter leaves
  unstated. The record script shows the mismatch when a resident
  exhausts a resource.

## Bearing on the record

- **[CASE-118](../cases.d/CASE-118.md)** (direct). The case calls ρ, the inner product of two unit
  feature vectors, the components' overlap, and its note of 2026-10-29
  asks whether Chesson's overlap for MacArthur's model is that cosine.
  It is: Table 1's ρ is the cosine of u_j and u_k with
  u_jl = c_jl √(v_l K_l / r_l), and s_j = ‖u_j‖. The case's unit vectors
  are the case s_j = 1.
- **[CLAIM-369](../claims.d/CLAIM-369.md)** (direct). The reduction is the claim's class:
  A = UᵀU with that U, r = Uᵀb − c with b_l = √(v_l K_l r_l) and c = μ.
  Then κ_j = r_j/‖u_j‖ = −∂_j L(0)/‖u_j‖, and a rare component's growth
  against a lone resident is ‖u_i‖(κ_i − ρκ_j). Filed as [CLAIM-tmpv65bg](../claims.d/CLAIM-tmpv65bg.md).
- **[QUESTION-132](../questions.d/QUESTION-132.md)** (direct, on its first outcome). The chapter defines
  stable coexistence as each species' recovery from low density, which
  is the question's test, λ_i > 0. It does not use the words
  "stabilizing" or "equalizing"; those come from [LIT-1219](../literature.d/LIT-1219.md), still
  Unavailable.
- **[QUESTION-083](../questions.d/QUESTION-083.md)** (direct, on its recommendation). Its notes ask that
  Chesson be read before a negative-frequency-dependence criterion gets
  stronger standing. For two species in MacArthur's model, the chapter's
  criterion is ρ < κ₁/κ₂ < 1/ρ.
- **[CLAIM-279](../claims.d/CLAIM-279.md)** (a parallel). A46's line that two operators "with
  different overall success can stay complementary because they do well
  in different circumstances" is the chapter's p. 48: "Differences in
  performance under specific conditions lead to tolerance of average
  performance differences."

## Limitations

- A review: formulas without derivations, and the multispecies case only
  by citation.
- **A gap in its argument**: the reduction's need for positive resources
  is unstated (above). Where a resource is exhausted, the effective
  overlap changes, and Table 1's ρ no longer gives the coefficients.
- The derived Lotka–Volterra equations in Table 1 use r_1, r_2 without
  defining them; from the consumer equation they are the net maximum
  harvesting rates Σ_l c_jl K_l v_l − μ_j (checked by the record script).
- The extension to predators is asserted with a citation to Chesson and
  Kuang ([16]), not shown.
- The conservation section is qualitative.
