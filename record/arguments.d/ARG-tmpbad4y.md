---
status: Proposed
title: 'Stringer and colleagues'' Supplementary Theorems 4 and 5, applied to the participation-ratio computation, ground its smoothness bound only as a strict bound on the asymptotic tail, so the finite-width table holds for a pure power law at the bound as the limit of smooth codes and does not follow from the bound alone'
version: 1
form: formal-application
grounds:
- THEORY-tmpwtoad
concludes:
- CLAIM-848
uses:
- TERM-136
tags:
- representation-learning
- mathematics
- neuroscience
date: '2026-11-22'
line:
- learned-structure
summary: >-
  CLAIM-848 took Stringer's bound from A29 §7 unread, as "α ≥ 1 + 2/m" for
  a differentiable code, and tabulated participation ratios of a pure
  power law from rank 1 at that exponent. The reading (THEORY-tmpwtoad,
  NOTE-tmp923nm) supports the bound and corrects it twice: Theorem 5 gives
  λ_n = o(n^(−1−2/d)), strict, so a spectrum exactly at the exponent is
  the limit of smooth codes; and the theorems constrain the tail only. The
  table's numbers stand for what they compute; what the bound licenses is
  narrower. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-848 THEORY-tmpwtoad TERM-136 ARG-130 — Proposed or new; the claim this argues, the reading it applies and the argument it qualifies -->

# ARG-tmpbad4y: Stringer and colleagues' Supplementary Theorems 4 and 5, applied to the participation-ratio computation, ground its smoothness bound only as a strict bound on the asymptotic tail, so the finite-width table holds for a pure power law at the bound as the limit of smooth codes and does not follow from the bound alone

## The inference

CLAIM-848 premises: a differentiable code of an m-dimensional stimulus
manifold has α ≥ α_c = 1 + 2/m, so codes "at Stringer's bound" have a pure
rank power law j^(−α_c) from rank 1, whose participation ratio at width 768
is 13 to 29 for m from 10 to 100.

The reading gives the bound's exact form. Theorem 5: "If the expected
derivative magnitude of φ is finite ... then λn = o(n−1−2/d)". Theorem 4,
the fractal bound: for all d′ > d, O(n^(−1−2/d′)); "α ≥" is its limit d′ ↓ d.
In Example 2, at the critical exponent "the dimension is still 1, even
though" the code is not differentiable. So:

1. **Strict.** A pure power law at α_c is not a smooth code; it is the
   limit of smooth codes. Smooth codes have α > α_c, or a tail that decays
   faster than any power at α_c.
2. **Tail only.** The theorems are asymptotic in rank and in the number of
   neurons (SI §3). They leave the head and any finite range free;
   Stringer's own fit skips ranks 1 to 10.

## Critical questions

- **Does the mapping premise hold?** For (1), the table is the limit of
  admissible codes, and it is continuous in α. Computed with `python3 -I`
  (direct sums at D = 768, checked against Hurwitz-zeta partial sums): at
  α_c the participation ratios are 13.17, 19.85 and 28.76 for m = 10, 20
  and 100, as tabulated; at α_c + 0.05 they are 10.97, 16.05 and 22.71. The
  conclusion that they are a few tens and nearly independent of m
  survives. For (2), it does not hold: the bound does not fix the head. With
  the tail at α_c and the top ten eigenvalues set equal to the tenth, the
  ratio at width 768 is 89.2, 112.4 and 137.2 for m = 10, 20 and 100; with
  the top eigenvalue multiplied by ten it is 1.8, 2.1 and 2.5. So the table
  describes pure power laws, not every code the bound allows.
- **Are the model's assumptions met in the new domain?** The theorems need
  many more neurons than the manifold's dimension; Stringer's heuristic of
  about 10d neurons gives some 1,000 for m = 100, above width 768, so the
  m = 100 row sits at the edge of where the bound is claimed to apply.
  Whether a network layer is a smooth code of a stimulus manifold at all is
  the application's assumption, not the theorem's.

## Verdict

The reading supports CLAIM-848's premise in corrected form: the bound is
strict and constrains the tail. CLAIM-848 and ARG-130 are corrected in
place (2026-11-22): codes at the bound are the limit of smooth codes, and
the table's numbers are for pure power laws from rank 1. The claim's three
consequences stand for such spectra; for a measured spectrum D_PR must be
computed from its eigenvalues, as the claim already said. Proposed.
