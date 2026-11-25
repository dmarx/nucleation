---
number: 853
status: Proposed
formerly:
- CLAIM-tmp6odrj
title: 'Inverse covariance moves energy to the tail'
statement: >-
  Multiplying a vector by the inverse of a covariance moves its energy
  toward that covariance's spectral tail: in the eigenbasis the energy
  fractions are reweighted by the inverse squared eigenvalues, so the
  cumulative energy falls at every cut and any measure that integrates it
  against cumulative variance falls with it
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A covariance Σ with positive eigenvalues and a vector v whose image
  Σ⁻¹v has, at some cut k of the eigenvalues taken in descending order, a
  larger share of its energy in the top k eigendirections than v has.
tags:
- mathematics
- representation-learning
date: '2026-11-21'
line:
- learned-structure
summary: >-
  The inequality that [CLAIM-852](CLAIM-852.md) uses, split off as a claim of its own
  so that its demonstrated part is held apart from that claim's
  interpretive identification (the owner's "adopt" of [ADR-140](../decisions.d/ADR-140.md); filer
  B's suggestion, readings batch 2). For a covariance Σ with positive
  eigenvalues λ₁ ≥ … ≥ λ_d and any vector v, write e_i for v's energy
  fractions in Σ's eigenbasis. Σ⁻¹v has fractions proportional to
  e_i/λ_i², a reweighting by weights that do not decrease down the
  spectrum, so its cumulative energy C(k) is at most v's at every k, with
  equality at every k only when the weights are constant on v's support.
  Any measure that integrates cumulative energy against cumulative
  variance, such as the Gini deviation of Acharya, Rimal and Dhakal,
  falls with it. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-852 — Proposed or new; the claim this serves and the decision behind the split -->

# CLAIM-853: Inverse covariance moves energy to the tail

**Statement.** Let Σ have eigenvalues λ₁ ≥ λ₂ ≥ … ≥ λ_d > 0 with orthonormal eigenvectors u_i, and let v ≠ 0 have components v_i = u_iᵀv and energy fractions e_i = v_i²/Σ_j v_j². Then Σ⁻¹v has components v_i/λ_i and energy fractions e'_i = (e_i/λ_i²)/Σ_j(e_j/λ_j²). For every k, C'(k) = Σ_{i≤k} e'_i ≤ C(k) = Σ_{i≤k} e_i.

**Proof.** The weights w_i = 1/λ_i² do not decrease in i. Reweighting a distribution by non-decreasing weights and renormalizing moves mass toward later indices: the reweighted distribution first-order stochastically dominates the original in i. Directly, C'(k) ≤ C(k) is equivalent to Σ_{i≤k} e_i w_i · Σ_{j>k} e_j ≤ Σ_{i≤k} e_i · Σ_{j>k} e_j w_j. That holds because every w_i with i ≤ k is at most every w_j with j > k. Equality at every k requires w constant on the support of e. A Gini-type deviation, the signed area of C against cumulative variance, is an integral of C, so it falls too, strictly when equality fails somewhere.

**Checked** with `python3 -I`, scratchpad `checks/park_ineq.py`: 5,000 random spectra (d from 2 to 299) and vectors, no case with C' > C beyond rounding (largest excess 1.6×10⁻¹⁵). Filer B's independent check (`filerB/mono.py`) found the same on 4,000 cases.

**Use.** [CLAIM-852](CLAIM-852.md) rests on it, adding the interpretive step that the measured activation-side concept vectors are, to a good approximation, Σ⁻¹ images of their unembedding-side contrasts, as Park, Choe and Veitch's unification ([THEORY-018](../theory.d/THEORY-018.md)) would have them.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
