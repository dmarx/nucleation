---
status: Proposed
title: "Chesson's 2011 restatement of his measures for MacArthur's model, read as a source and carried through the fast-resource reduction, shows that his overlap and fitness are the cosine and the normed zero-abundance marginal value of symmetric resource competition's niche vectors"
version: 1
form: source
rests_on:
- CLAIM-369
grounds:
- THEORY-tmpac7iw
concludes:
- CLAIM-tmpv65bg
tags:
- ecology
- mathematics
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
summary: >-
  Filed by the lead run of 2026-11-22. The claim's algebra is the
  assistant's and is checked; what it takes from the reading is the
  definitions of Chesson's ρ, s and κ for MacArthur's model, from Table 1
  of the 2011 chapter. This argument answers the source form's questions
  for that step. Whether the chapter also tells what the 1990 paper
  defined is the open part, and two readings of it are filed on CASE-118.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpac7iw CLAIM-tmpv65bg — Proposed, filed by the lead run of 2026-11-22 -->
<!-- inactive-ok-file: LIT-1826 — Unfetched; Chesson 1990, not read, the paper the chapter stands in for -->

# ARG-tmpyjmij: Chesson's 2011 restatement of his measures for MacArthur's model, read as a source and carried through the fast-resource reduction, shows that his overlap and fitness are the cosine and the normed zero-abundance marginal value of symmetric resource competition's niche vectors

## The inference

THEORY-tmpac7iw gives Chesson's Table 1: the model, s_j, κ_j and ρ. CLAIM-369
gives the class A = UᵀU, r = Uᵀb − c, with L and its gradient. The
fast-resource reduction of the model, under u_jl = c_jl √(v_l K_l / r_l)
and b_l = √(v_l K_l r_l), lands in that class. Substituting the map into
Table 1's formulas gives s_j = ‖u_j‖, ρ = cos(u_j, u_k) and
κ_j = r_j/‖u_j‖, and CLAIM-369's invasion fitness against a lone resident
factors as ‖u_i‖(κ_i − ρκ_j). That is CLAIM-tmpv65bg.

## The source form's questions

- **Does the work say this, read in context?** It gives the three
  formulas in Table 1 (p. 45, read from the rendered page because the
  extraction lost the Greek letters), the reduction in words (p. 46),
  and eq. (1) (p. 47). It does not write the map to niche vectors or the
  cosine; those are derived here, and the record script checks them
  against the model. So the argument leans on the work for the
  definitions only.
- **Is it said within the scope the claim needs?** Yes for two species
  and the Lotka–Volterra reduction, which is the claim's scope. The
  chapter does not state that the reduction needs positive resources;
  the claim adds that condition itself, from Marsland, Cui and Mehta
  (LIT-1230) and the record script.
- **Does the claim lean on the reading for more than it holds?** Only in
  the word "Chesson's". The chapter is Chesson's own, and it cites the
  1990 paper (its [28]) for the reworking of MacArthur it tabulates. If
  the 1990 paper defines its overlap otherwise, the attribution in
  the claim's title would need "as Chesson states it in 2011", and the
  algebra would be unchanged. The claim's `defeated_if` says so. LIT-1826
  stays Unfetched; CASE-118's note of 2026-11-22 files the two readings of
  how far this settles the case's question.
