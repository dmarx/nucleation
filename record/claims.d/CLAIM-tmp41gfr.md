---
status: Proposed
title: 'In a high-dimensional representation space a thin radial shell, nearly orthogonal random directions and nearly equal pairwise distances arise with no interaction at all, so they are a null baseline and not evidence of learned attraction, order or collapse; a thin annulus is not a low-dimensional manifold, and meaningful locality may be something learning has to produce'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A shell, near-orthogonality or distance concentration that does not
  arise in the stated null (independent isotropic Gaussian or uniform
  spherical vectors) at the stated dimension, so that observing it would
  after all discriminate learned structure from the null; or an error in
  the formulas below. Not met by trained representations that depart from
  the null, which is what the claim says to look for.
tags:
- representation-learning
- mathematics
- probabilistic-modeling
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-tmpvu6cb
uses:
- TERM-tmplplcf
grounds:
- THEORY-366
- THEORY-369
summary: >-
  A29 §5A and A30 §1–§3, §6 and §8 of the exchange "Rich Get Richer Power
  Laws" (2026-11-21), developing the owner's U19 (CLAIM-tmpfwwfy): "A
  high-dimensional representation can be strongly concentrated
  geometrically while remaining highly dispersed informationally." The
  annulus, near-orthogonality and equal distances are what the null already
  does, so learning shows only as departure from them. One worked number of
  A30's is corrected below. The wording is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A29 and A30); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpfwwfy TERM-tmplplcf CLAIM-tmpy688z CLAIM-tmpqqngq — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# CLAIM-tmp41gfr: In a high-dimensional representation space a thin radial shell, nearly orthogonal random directions and nearly equal pairwise distances arise with no interaction at all, so they are a null baseline and not evidence of learned attraction, order or collapse; a thin annulus is not a low-dimensional manifold, and meaningful locality may be something learning has to produce

## The claim

**Radius.** A30 §1: for z ∼ N(0, σ²I_D), p(R) ∝ R^(D−1) e^(−R²/2σ²), so R
concentrates near σ√D with a standard deviation that tends to σ/√2, and
SD(R)/E[R] ≈ 1/√(2D). "The particles can occupy a thin shell **without any
attractive interaction among them**." Written as an effective potential,
V_eff(R) = R²/2σ² − (D − 1) ln R, minimized at σ√(D − 1), the log term "is an
*entropic contribution* from radial volume. It isn't an additional physical
force", so shell occupancy must not be read as learned attraction.

**Direction.** A30 §2–§3: radius and direction are independent, the
direction stays uniform on S^(D−1), Var(uᵀv) = 1/D, and ‖u − v‖² = 2 − 2uᵀv
concentrates at 2. "Radially concentrated particles with nontrivial angular
dynamics."

**Locality.** A30 §3: for a kernel exp(−‖z_i − z_j‖²/2ℓ²) and isotropic
Gaussian embeddings, ‖z_i − z_j‖² ≈ 2D. A fixed ℓ makes most interactions
exponentially weak; ℓ² ∝ D makes them nearly identical, a mean field. The
system escapes the dilemma only if learning creates nonrandom neighbourhoods:
"the emergence of meaningful locality could itself be one of the phenomena
that learning produces."

**Typical set and manifold.** A30 §6: "**A thin annulus is not necessarily a
low-dimensional manifold.** A sphere in ℝ^D has intrinsic dimension D − 1"
(TERM-tmplplcf). Concentration removes one radial degree of freedom; a
20-dimensional semantic manifold in 4,096 dimensions is a different thing,
and a representation can have both.

**Three concentrations.** A30 §8: probability mass in a narrow range of
radii (the annulus); variance in a subset of directions (spectral
concentration, CLAIM-tmpy688z); and a broad hierarchy of slow or correlated modes
(collective criticality), which "is not concentration itself". A sharp
annulus can mask soft angular modes, so a featureless norm histogram is no
evidence against collective structure.

## Checked, and one correction

Computed in this session (python3 -I, scipy):

- The annulus. Exact SD(R)/E[R] for σ = 1 is 0.178, 0.089, 0.0255 and
  0.0110 at D = 16, 64, 768 and 4,096, against A30's table of 17.7%, 8.8%,
  2.6% and 1.1% from 1/√(2D): the table is right to its rounding.
- κ for the von Mises–Fisher example is in CLAIM-tmpqqngq.
- **Correction.** A29 §5A and A30 §3 give the largest cosine among N random
  unit vectors as ≈ √(2 log N/D), and A30 works it for D = 768 and N = 10⁶:
  "max_j u_iᵀu_j ≈ 0.19 … That's an angle of about 79 degrees." 0.190 is the
  leading-order asymptotic. From the exact distribution of a cosine on the
  sphere, P(uᵀv ≥ x) = ½ I_(1−x²)((D − 1)/2, ½), the median of the maximum is
  0.173 (80.0°), and 90% of draws fall between 0.162 and 0.190. The leading
  term sits at the top of that range because it omits the
  (log log N)/√(log N) correction. The point A30 makes, that the nearest of
  a million random directions is nearly perpendicular, is unchanged.

## Gap: which ensemble

The annulus and near-orthogonality are statements about an ensemble of
independent isotropic vectors. A trained representation is a deterministic
function of a fixed dataset, so "concentration" there needs a stated
ensemble: inputs drawn from the data distribution (the pushforward of
A29 §12), random initialisations, or seeds. A30 uses initialisation
isotropy without saying so. With a nonzero mean μ the squared norm is
‖μ‖² + 2μᵀε + ‖ε‖², and relative concentration is then sharper still, so
the centred covariance is the one to use (CLAIM-tmpy688z).

## What the record holds

THEORY-366 (Beyer and colleagues): relative contrast between nearest and
farthest distances vanishes when the distance's relative variance does, and
data on a low-dimensional subspace or queries inside well-separated clusters
escape it. That is this claim's null and its escape route, in the setting of
nearest-neighbour search; THEORY-369 holds the consequence for indexing.
What the record lacked is the null read as a baseline for representation
dynamics, and the entropic reading of the shell.
