---
status: Proposed
title: 'If learned signal strengths fall as a power law in rank, the number of directions PCA can separate from the noise bulk grows as a power of the sample-to-dimension ratio and of the signal gain, a cascade of detectability thresholds and not a self-organized critical process, and the power law then belongs to the hierarchy of signal strengths, not to the spectrum, whose bulk with a few outliers is no heavy tail'
version: 1
role: supposed
warrant: demonstrated
tags:
- representation-learning
- mathematical-statistics
- complex-systems
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-tmp5y856
bears_on:
- QUESTION-tmpvu6cb
grounds:
- LIT-tmpipm3o
summary: >-
  A32 §5 of the exchange "Rich Get Richer Power Laws" (2026-11-21): with
  spikes β_j = C j^(−α), applying the BBP threshold to each gives
  K_det ∼ (C/√γ)^(1/α) = C^(1/α)(N/D)^(1/(2α)) detectable directions, and
  with a gain g(t) a succession of thresholds as learning proceeds; "a
  cascade of spectral detectability transitions, not necessarily a
  dynamically propagating avalanche or self-organized critical process."
  Supposed: it holds while the spikes are few against D; the filing's
  check shows where it fails. The wording is A's (the other assistant in
  the exchange "Rich Get Richer Power Laws", A32); adopting it is the
  owner's call.
---

# CLAIM-tmp8mvx8: If learned signal strengths fall as a power law in rank, the number of directions PCA can separate from the noise bulk grows as a power of the sample-to-dimension ratio and of the signal gain, a cascade of detectability thresholds and not a self-organized critical process, and the power law then belongs to the hierarchy of signal strengths, not to the spectrum, whose bulk with a few outliers is no heavy tail

## The claim

A32 §5 supposes training builds a hierarchy Σ = I + Σ_(j≤K) β_j v_j v_jᵀ with
orthogonal v_j and β_j = C j^(−α), and that "the signal rank remains
sufficiently sparse for a conventional spiked-covariance approximation to be
useful". Each spike yields its own outlier when β_j > √γ, so

K_det ∼ (C/√γ)^(1/α) = C^(1/α) (N/D)^(1/(2α)),

and if learning scales the hierarchy as β_j(t) = g(t) C j^(−α), then
K_det(t) ∼ (g(t)C/√γ)^(1/α): "progressively weaker semantic directions become
observable as learning proceeds."

Two readings follow. First, it is a cascade of detectability thresholds, not
a self-organized critical process. Second, "the background Marchenko–Pastur
distribution has compact spectral support. A bulk with a few detached
outliers is not itself a power-law tail. Nevertheless, the *hierarchy of
signal strengths* could follow a power law. That may be the more relevant
object."

## Checked, and where it fails

Simulated in this session (python3 -I, D = 500, four draws each), counting
eigenvalues above the edge (1 + √γ)² plus a finite-size margin of three
times edge·N^(−2/3):

| γ | C | α | K | K/D | spikes with β_j > √γ | of those, beyond the margin | observed outliers |
|---|---|---|---|---|---|---|---|
| 0.25 | 8 | 1 | 50 | 0.1 | 15 | 11 | 12 |
| 0.25 | 8 | 2 | 50 | 0.1 | 3 | 3 | 3 |
| 0.25 | 30 | 1 | 200 | 0.4 | 59 | 44 | 43 |
| 0.25 | 8 | 0.5 | 20 | 0.04 | 20 | 20 | 20 |
| 0.25 | 8 | 0.5 | 200 | 0.4 | 200 | 143 | 84 |

The count works while the spikes above threshold are few against D (rows 1
to 4; the top outliers sit within 1 to 3% of the per-spike formula). It fails
when many spikes crowd the threshold and K is a sizeable share of D (row 5:
84 seen against 143 predicted), because the population spectrum is then no
longer the identity plus a finite-rank perturbation, and the bulk itself
moves. And at finite N an outlier within about N^(−2/3) of the edge is
invisible, so the formula overcounts near threshold even in the sparse
regime (rows 1 and 3).

## Corrections the filing found

- **Which N.** In BBP N is the number of samples on which the covariance is
  estimated, here the probe set. A32 reads it as data acquired ("As we
  acquire more data, weaker directions can emerge"), which conflates the
  probe sample with training data. More training data changes β_j(t) through
  g(t); more probe samples change γ. They are different levers.
- **Sparse regime only.** A hierarchy that keeps growing in K leaves the
  finite-rank regime the formula needs, as row 5 shows.
