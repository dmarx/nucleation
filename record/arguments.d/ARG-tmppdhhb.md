---
status: Proposed
title: "Baik, Ben Arous and Péché prove the spiked threshold only for the largest eigenvalue of complex Gaussian samples with at least as many samples as variables, so for claims about real data, eigenvectors or several outliers their paper corroborates and does not ground"
version: 1
form: source
grounds:
- THEORY-tmp0covn
concludes:
- CLAIM-tmp5y856
- CLAIM-tmp8mvx8
- CLAIM-tmpk33au
- CLAIM-tmpqbo50
tags:
- mathematical-statistics
- representation-learning
date: '2026-11-21'
line:
- learned-structure
summary: >-
  CLAIM-tmp5y856, CLAIM-tmp8mvx8 and CLAIM-tmpk33au cited the BBP paper
  (LIT-tmpipm3o) in their grounds, unread, for the threshold β > √(D/N),
  the outlier, the eigenvector overlap and a count of outliers;
  CLAIM-tmpqbo50 uses the same through CLAIM-tmp5y856. Read, the paper
  proves the threshold and outlier for the largest eigenvalue of complex
  Gaussian, centred samples with D ≤ N, and nothing about eigenvectors. The
  claims are about real data, eigenvectors, several outliers, D > N and
  additive models. So the paper moves from their grounds to corroborates,
  and the clauses rest on Baik and Silverstein, Paul, and Benaych-Georges
  and Nadakuditi (ARG-tmpvalfs, ARG-tmpnwmcr, ARG-tmpe2vrk). The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmp5y856 CLAIM-tmp8mvx8 CLAIM-tmpk33au CLAIM-tmpqbo50 THEORY-tmp0covn ARG-tmpvalfs ARG-tmpnwmcr ARG-tmpe2vrk — Proposed; the claims, readings and arguments of 2026-11-21 -->

# ARG-tmppdhhb: Baik, Ben Arous and Péché prove the spiked threshold only for the largest eigenvalue of complex Gaussian samples with at least as many samples as variables, so for claims about real data, eigenvectors or several outliers their paper corroborates and does not ground

## The inference

Each of the four claims states the spiked threshold β > √γ (γ = D/N), the
outlier (1 + β)(1 + γ/β) and the edge (1 + √γ)², and attributes them to
"the BBP transition". Read as a source, THEORY-tmp0covn would carry all of
it.

## Critical questions (source)

**Does the work say this, read in context?** The threshold and the
outlier, yes, after the change of notation (γ_BBP⁻¹ = √γ, ℓ = 1 + β):
Corollary 1.1, "λ1 is separated from the rest of eigenvalues if and only
if at least one eigenvalue of Σ is greater than 1 + γ⁻¹", with
λ_1 → ℓ_1(1 + γ⁻²/(ℓ_1 − 1)). The eigenvector overlap, no: the paper
treats only λ_1.

**Is it said within the scope the claims need?** No, on four counts.
- *Real data.* "We assume that the samples ~y are complex Gaussian"; the
  real case is a "Conjecture" (p. 11), and the method is "not applicable
  to real sample matrices" (p. 13). The claims' constructions and
  simulations are real.
- *Eigenvectors.* CLAIM-tmp5y856's "only then does its eigenvector carry
  information" and the overlap formula are Paul's Theorem 4 and
  Benaych-Georges and Nadakuditi's (10).
- *Several outliers and D > N.* BBP needs M ≥ N (γ ≤ 1) and gives only
  the largest eigenvalue; CLAIM-tmp8mvx8 counts outliers and
  CLAIM-tmpqbo50 has a γ = 4 row. Both are Baik and Silverstein's.
- *Additive models.* BBP's samples are Gaussian with covariance Σ and the
  covariance is centred by the sample mean. A ±1 mixture along v, or a mean
  shift seen in the uncentred second moment (CLAIM-tmpk33au), is a rank-one
  perturbation of the data matrix, which is Benaych-Georges and
  Nadakuditi's.

**Do the claims lean on the reading for more than it holds?** Yes, as
cited. They do not lose anything, because the formulas are right in every
setting they use: each clause has its own source among the three
supplements, and the paper agrees with them where it applies.

## Verdict

LIT-tmpipm3o leaves the grounds of CLAIM-tmp5y856, CLAIM-tmp8mvx8 and
CLAIM-tmpk33au; THEORY-tmp0covn corroborates all four claims. The name "BBP
threshold" can stay, as the field uses it, with the attributions corrected
in dated notes on each entry.
