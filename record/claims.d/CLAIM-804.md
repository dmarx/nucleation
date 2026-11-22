---
number: 804
status: Proposed
formerly:
- CLAIM-tmp8mvx8
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
- CLAIM-799
bears_on:
- QUESTION-515
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
grounds:
- THEORY-2149
---
<!-- inactive-ok-file: THEORY-tmpehudh — Proposed; the reading of Bak, Tang and Wiesenfeld cited in the note of 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmphbp5a — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: THEORY-2149 THEORY-2148 ARG-151 ARG-145 — Proposed; the readings and arguments of 2026-11-21 -->

# CLAIM-804: If learned signal strengths fall as a power law in rank, the number of directions PCA can separate from the noise bulk grows as a power of the sample-to-dimension ratio and of the signal gain, a cascade of detectability thresholds and not a self-organized critical process, and the power law then belongs to the hierarchy of signal strengths, not to the spectrum, whose bulk with a few outliers is no heavy tail

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

The threshold the count applies is Baik, Ben Arous and Péché's
([LIT-2986](../literature.d/LIT-2986.md)), read on 2026-11-21; the count of several outliers is Baik
and Silverstein's ([LIT-2988](../literature.d/LIT-2988.md)): see the note of 2026-11-21 below. The simulation
counts outliers directly against the edge of the noise bulk, so the check
does not depend on the work.

## Corrections the filing found

- **Which N.** In BBP N is the number of samples on which the covariance is
  estimated, here the probe set. A32 reads it as data acquired ("As we
  acquire more data, weaker directions can emerge"), which conflates the
  probe sample with training data. More training data changes β_j(t) through
  g(t); more probe samples change γ. They are different levers.
- **Sparse regime only.** A hierarchy that keeps growing in K leaves the
  finite-rank regime the formula needs, as row 5 shows.

## Note of 2026-11-21: Baik, Ben Arous and Péché, read

The BBP paper ([LIT-2986](../literature.d/LIT-2986.md), read in [NOTE-2241](../notes.d/NOTE-2241.md); [THEORY-2148](../theory.d/THEORY-2148.md))
**qualifies** the attribution and **supports** both corrections above.

- **The count is not BBP's.** BBP gives the law of the largest eigenvalue
  only. That each spike above threshold gives its own outlier is Baik and
  Silverstein's (1.10), for real or complex samples and a fixed number of
  spikes ([LIT-2988](../literature.d/LIT-2988.md), [THEORY-2149](../theory.d/THEORY-2149.md); [ARG-151](../arguments.d/ARG-151.md)). A hierarchy whose
  rank grows with D is outside both, which row 5 shows: this supports
  "Sparse regime only".
- **Which N.** BBP's M is the number of samples from which the covariance
  is estimated, so the paper supports the correction that N here is the
  probe sample.
- **The invisible margin.** "At finite N an outlier within about
  N^(−2/3) of the edge is invisible" is BBP's Theorem 1.1(a) and 1.2:
  edge fluctuations of order M^(−2/3), and a critical window of width
  M^(−1/3) in the spike (for complex data; the real case is conjectured
  there to scale the same way).

[LIT-2986](../literature.d/LIT-2986.md) leaves `grounds` for [THEORY-2149](../theory.d/THEORY-2149.md) ([ARG-145](../arguments.d/ARG-145.md));
[THEORY-2148](../theory.d/THEORY-2148.md) corroborates.

## Note of 2026-11-22: Park and colleagues, read

Park and colleagues ([LIT-2990](../literature.d/LIT-2990.md), [NOTE-tmpzethm](../notes.d/NOTE-tmpzethm.md), [THEORY-tmphbp5a](../theory.d/THEORY-tmphbp5a.md)): **a
parallel.** Their load α = P/D plays the part of this claim's sample
ratio for the finite-data bulk: "finite-sample fluctuations strongly
deform the bulk spectrum and suppress signal extraction", and the window in
which an aligned outlier appears narrows as the load falls (§IV A). No
relation.

## Note of 2026-11-22: Bak, Tang and Wiesenfeld, read

**Background.** The claim contrasts its cascade of detectability
thresholds with "a self-organized critical process". Bak, Tang and
Wiesenfeld (LIT-2992, NOTE-tmpnl00y, THEORY-tmpehudh), now read, fix what
the contrast term meant at its origin: a spatially extended threshold
system that relaxes to a state with no length scale, with avalanches of
all sizes cut off by the system size (pp. 382–383). The PCA cascade has
none of these: no spatial extent, no avalanches, no relaxation to an
attractor. The contrast stands. No edge. Status unchanged.
