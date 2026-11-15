---
status: Proposed
promote_when: >-
  An independent evaluation, or a run of the released code, showing at
  least one text-attack-robust erasure method regenerating its concept
  under a probe that does not search over text inputs on SD 1.4, and the
  same for most of the seven methods.
title: 'On Lu and colleagues, most of seven concept-erasure methods applied to Stable Diffusion 1.4 over 13 concepts can be made to regenerate the erased concept by at least one probe that does not search over text inputs, such as inpainting, diffusion completion, added noise along the trajectory or latent classifier guidance, including methods robust to text-based attacks, which the authors read as steering guidance away from a concept rather than removing it'
version: 1
tags:
- representation-learning
date: '2026-11-15'
source:
- LIT-tmpokxet
summary: >-
  Lu, Kriplani, Gandikota, Pham, Bau, Hegde & Cohen (2025), [LIT-tmpokxet](../literature.d/LIT-tmpokxet.md),
  read in [NOTE-tmpsiphf](../notes.d/NOTE-tmpsiphf.md), tables through the prose. The reading of the
  result as avoidance rather than destruction is the authors'
  interpretation, not a measurement. The wording is the reader's;
  adopting it is the owner's call.
---

# THEORY-tmpyppq1: On Lu and colleagues, most of seven concept-erasure methods applied to Stable Diffusion 1.4 over 13 concepts can be made to regenerate the erased concept by at least one probe that does not search over text inputs, such as inpainting, diffusion completion, added noise along the trajectory or latent classifier guidance, including methods robust to text-based attacks, which the authors read as steering guidance away from a concept rather than removing it

## Source

Lu et al. (2025), [LIT-tmpokxet](../literature.d/LIT-tmpokxet.md); read in [NOTE-tmpsiphf](../notes.d/NOTE-tmpsiphf.md).

## The result

- §3.6: GA, Task Vectors, STEREO and RECE "appear robust to text-based
  attacks", yet Task Vectors and RECE resurfaced the concept under
  inpainting and diffusion completion; UCE, ESD-x and ESD-u concepts
  "could be recovered with minor stochastic perturbations"; under
  classifier guidance "many models, including STEREO, could regenerate
  erased concepts".
- §3.6: "most current erasure methods operate through guidance-based
  avoidance rather than true destruction of underlying representations".

## What it does not show

- That the recovered concept was held rather than induced by the probe:
  §5 names the limit for optimization-based probes.
- Anything beyond SD 1.4 and its 13 concepts.
- That any method destroys a concept: the destruction model is described,
  not shown to be reached.
