---
status: Answered
title: 'Do the Johnson–Lindenstrauss threshold for distances and the k log(N/k) threshold for sparse recovery rest on one concentration-of-measure argument, a tail bound for each fixed vector''s norm with a union bound over a family, both for sufficiency and for necessity?'
version: 1
tags:
- mathematics
- learning-theory
- neuroscience
date: '2026-10-21'
line: formal-apparatus
refines:
- QUESTION-120
summary: >-
  The part of [QUESTION-120](QUESTION-120.md) its readings on distances and sparse recovery
  settle, split off under [ADR-049](../decisions.d/ADR-049.md). For sufficiency, yes: one per-vector
  tail and a union bound give both, over pairs for distances ([THEORY-397](../theory.d/THEORY-397.md))
  and over net points on every sparse support for recovery ([THEORY-390](../theory.d/THEORY-390.md)).
  For necessity, no: the distance lower bounds are encoding and
  bit-counting arguments ([THEORY-395](../theory.d/THEORY-395.md), [THEORY-399](../theory.d/THEORY-399.md)), recovery's rests on
  Gelfand widths, and its sharp location on face counting ([THEORY-391](../theory.d/THEORY-391.md)).
  Random features, superposition and expand-and-threshold stay with
  [QUESTION-120](QUESTION-120.md).
answered_by:
- THEORY-390
- THEORY-391
- THEORY-395
- THEORY-397
- THEORY-399
---

# QUESTION-tmpqzznf: Do the Johnson–Lindenstrauss threshold for distances and the k log(N/k) threshold for sparse recovery rest on one concentration-of-measure argument, a tail bound for each fixed vector's norm with a union bound over a family, both for sufficiency and for necessity?

## Answer

For sufficiency, yes. For necessity, no. This is the part of [QUESTION-120](QUESTION-120.md)
that its readings on the first two uses settle, split off on 2026-10-21
([ADR-049](../decisions.d/ADR-049.md)).

- **Sufficiency for distances.** [THEORY-397](../theory.d/THEORY-397.md) (Active). A random linear map
  into k ≥ 4(ε²/2 − ε³/3)⁻¹ ln n dimensions keeps every pairwise squared
  distance within 1 ± ε. Each difference vector's squared length
  concentrates, and a union bound over the pairs costs ln n. The proofs
  cover a random subspace, Gaussian entries and zero-mean ±1 or
  √3·{+1, 0, −1} entries.
- **Sufficiency for sparse recovery.** [THEORY-390](../theory.d/THEORY-390.md) (Active). The only
  assumption is the same per-vector tail. A union bound over (12/δ)^k net
  points on each of the (eN/k)^k supports, and a step from the net to the
  whole support, give the restricted isometry property for
  k ≤ c₁n/log(N/k). Any distribution that yields JL embeddings yields RIP
  matrices.
- **Necessity for distances.** [THEORY-395](../theory.d/THEORY-395.md) (Active) shows that some n-point
  set needs Ω(ε⁻² lg(ε²n)) dimensions under any map, by an encoding
  argument that counts the supports of k-sparse vectors. [THEORY-399](../theory.d/THEORY-399.md)
  (Active) carries the bound to every ε ≥ 2/√n by counting the bits of a
  distance sketch. Neither is a tail bound on a random map, and neither
  could be: they bound every map.
- **Necessity for sparse recovery.** [THEORY-390](../theory.d/THEORY-390.md) records that the paper
  takes it from Garnaev–Gluskin's Gelfand widths of the ℓ₁ ball, which is
  geometry, not concentration. [THEORY-391](../theory.d/THEORY-391.md) (Active) gives the sharp
  location of ℓ₁ recovery as a limit from counting faces of projected
  polytopes. A union bound gives only its order.

So the two sufficiency proofs are one argument over two families. Both
thresholds are the log of the family's size over a squared tolerance, and
recovery's family adds a k log(12/δ) term. The necessity proofs are
different arguments from that one and from each other. [THEORY-395](../theory.d/THEORY-395.md)'s count
ends at m = Ω(k lg(d/k)), the form of the recovery bound, but that is a
reader's observation in [NOTE-925](../notes.d/NOTE-925.md), not a shared proof.

## What it leaves to [QUESTION-120](QUESTION-120.md)

The answer covers distances and sparse recovery for random matrices.
Whether the superposition toy model is limited by recovery or by
incoherence, and whether its phase changes are the Donoho–Tanner
transition, stay with the parent. So do random features, whose threshold
counts features against samples, and expand-and-threshold maps, which go
up in dimension. Whether log(2 + ε²n)/ε² dimensions suffice for one set,
as [THEORY-393](../theory.d/THEORY-393.md) shows for two, is also open.
