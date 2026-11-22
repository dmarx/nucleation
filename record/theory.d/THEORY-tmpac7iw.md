---
status: Proposed
promote_when: >-
  A second reading or an independent derivation confirms, for MacArthur's
  consumer–resource model in its fast-resource Lotka–Volterra reduction,
  that α_ij/α_jj = ρ κ_j/κ_i with ρ and κ as Table 1 defines them, and that
  two species are then mutually invasible exactly when
  ρ < κ₁/κ₂ < 1/ρ. A reading of Chesson (1990) that states this would do;
  so would a derivation from the model's equations. Evidence that the
  measures are useful in the field, or that they extend to many species,
  is not asked for.
title: "On Chesson's account of MacArthur's consumer-resource model, the ratio of interspecific to intraspecific competition is a niche overlap, a weighted cosine of two species' consumption vectors, times a ratio of average fitnesses, so the two coexist, each recovering from low density, exactly when their fitness ratio lies strictly between the overlap and its reciprocal"
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed Proposed from NOTE-tmp6d961, a reading of Chesson (2011), the
    stand-in for Chesson (1990). The chapter states Table 1's measures
    and eqs. (1) and (2) without derivation. A record script
    (scratch/studies/lead-196/chesson_overlap.py) derived the
    fast-resource reduction and checked eq. (1), the reading of ρ as a
    weighted cosine, and the two-species invasion growth against the full
    consumer–resource model; that is a check by the same session, not an
    independent reading, so the entry stays Proposed.
tags:
- ecology
- mathematics
date: '2026-11-22'
source:
- LIT-tmp7sngn
bears_on:
- QUESTION-132
- QUESTION-083
summary: >-
  Chesson (2011), restating his 1990 reworking of MacArthur. With
  consumption rates c_jl, resource values v_l, carrying capacities K_l,
  renewal rates r_l and maintenance requirements μ_j, define
  s_j = √(Σ_l c_jl² v_l K_l / r_l), κ_j = (Σ_l c_jl K_l v_l − μ_j)/s_j and
  ρ = Σ_l c_jl v_l K_l c_kl / r_l / (s_j s_k). Then κ_j ρ / κ_i = α_ij/α_jj,
  and two species coexist when ρ < κ₁/κ₂ < 1/ρ. The overlap is unaffected by
  the heights of the consumption curves, which go into κ. Stable
  coexistence means each species recovers from low density; neutral
  models are ρ = 1 with equal κ.
---
<!-- inactive-ok-file: LIT-1826 LIT-1219 — Unfetched and Unavailable; the 1990 paper the source stands in for, and the 2000 review it cites, not read -->

# THEORY-tmpac7iw: On Chesson's account of MacArthur's consumer-resource model, the ratio of interspecific to intraspecific competition is a niche overlap, a weighted cosine of two species' consumption vectors, times a ratio of average fitnesses, so the two coexist, each recovering from low density, exactly when their fitness ratio lies strictly between the overlap and its reciprocal

Chesson (2011), LIT-tmp7sngn, read in NOTE-tmp6d961, restating Chesson
(1990), LIT-1826, which was not reached.

## The account

MacArthur's consumers feed on logistic resources. When resources are fast,
the model reduces to Lotka–Volterra competition. Chesson splits each
competition coefficient ratio into two factors:

- **niche overlap ρ**, between 0 and 1, the similarity of the two
  species' resource use, weighted by v_l K_l / r_l, so a slowly renewed
  resource counts more. It is the cosine of the consumption vectors
  under that weighting, and "a specific measure of the degree of
  separation of those feedback loops" (p. 48);
- **average fitness κ**, the net maximum harvesting rate over the
  sensitivity s, which ranks the species' adaptedness within the guild.

Eq. (1): κ_j ρ / κ_i = α_ij/α_jj. Each species invades the other when its
expression (1) is below 1, which for two species is ρ < κ₁/κ₂ < 1/ρ
(eq. 2). The lower the overlap, the larger the fitness difference that
coexistence tolerates. With ρ = 1 and equal κ the model is neutral: no
species tends to increase from low density.

## What could have come out otherwise

The decomposition is algebra on the reduced model, and the record
script's check could have failed: ρ might not have been a cosine (it is
one only because the same c_jl sets both a species' impact on a resource
and its benefit from it), or eq. (1) might have needed a different κ.
Neither happened.

## What it does not show

- **That ρ and κ decide coexistence among many species.** Eqs. (1) and
  (2) are pairwise. The chapter cites the generalization to [5] and [29]
  and does not show it.
- **That the reduction always holds.** It needs every resource positive;
  where a resident exhausts one, the coefficients change and Table 1's ρ
  no longer gives them.
- **What "stabilizing" and "equalizing" mean.** The chapter does not use
  those words. They are Chesson (2000), LIT-1219, Unavailable.
