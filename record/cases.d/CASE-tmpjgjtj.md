---
status: Proposed
title: 'Blind irreducible recovery from a group-composition network trained on S3 and S4'
version: 1
standing: documented
kind: executed-study
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-11-22'
illustrates:
- CLAIM-135
bears_on:
- QUESTION-058
line:
- learned-structure
---

# CASE-tmpjgjtj: Blind irreducible recovery from a group-composition network trained on S3 and S4

## The case

A numpy study carried out for [LEAD-114](../leads.d/LEAD-114.md) (branch
`claude/lead-114-blind-irrep`, `scratch/studies/lead-114/`). A small network
is trained to compute a non-abelian group's multiplication, and its
irreducible representations are then recovered from the trained network
*without the group being supplied*, against a *group-supplied control*.

**Task, with no matrix representation imposed.** Each group element is a
one-hot index over `|G|` arbitrary labels; the network never sees any matrix
representation of the group. Input is the concatenation of the one-hot codes
of `g` and `h`; the target is the class `g·h`. Architecture: a shared
embedding `E` (`|G|×d`), one hidden ReLU layer, an unembedding, softmax
cross-entropy with weight decay, trained by momentum gradient descent. The
permutation realisation of the group is used only to generate the
multiplication table; its matrices never touch the network or the recovery.

**Three regimes.** S3 with a 25% held-out split (`S3-mem`); S3 trained on the
whole table (`S3-fit`); S4 with a 20% held-out split (`S4-grok`), three seeds
each.

**Blind recovery.** The binary operation the network computes is read off by
`argmax` over all pairs (`T_net[g,h]`). From `T_net` alone — never the true
table — the pipeline checks it is a group (closure, identity, inverses,
associativity), then recovers the irreducibles by a group-name-agnostic
algorithm: the class-sum operators of the reconstructed table span the group
algebra's centre; a generic Hermitian combination's eigenspaces are the
Peter–Weyl isotypic blocks, giving the number of irreducibles, each dimension
`d_ρ = √(dim block)`, and the full character table. The learned embedding's
group-Fourier power spectrum is then the fraction of its squared norm lying in
each isotypic block. **Control:** the same recovery run on the true Cayley
table.

## What it can show

Being an executed study (standing documented), its measured outcomes are
fact; what trained networks do in general is not settled by three groups at a
few seeds.

- **Generalising networks learn the group.** `S4-grok` reaches test accuracy
  1.0; its reconstructed operation `T_net` equals the true table exactly and
  is a valid group. `S3-mem` memorises (test accuracy ≈ 0); its `T_net`
  agrees with the true table on ≈ 0.75 of entries and is *not* a group
  (associativity fails). `S3-fit` fits the whole table and reconstructs it
  exactly.
- **The irreducibles are recovered blind, exactly, when the network learned
  the group.** For `S4-grok` the blind path returns dimensions
  `[1,1,2,3,3]` and S4's full character table; for `S3-fit`, `[1,1,2]` and
  S3's. Both match the group-supplied control to orthogonality residual
  ≈ 10⁻¹⁴. When the network only memorised (`S3-mem`), `T_net` is not a group
  and the blind path refuses — the limit is the network, not the method, which
  is exactly what the control establishes.
- **The weights carry the irreducibles.** The embedding's group-Fourier power
  concentrates on the *faithful* irreducibles: the trivial (constant)
  component is ≈ 0, the sign representation is smallest, and S3 puts ≈ 78% of
  its non-trivial power on the 2-dimensional standard irreducible while S4
  puts ≈ 78% on its two 3-dimensional irreducibles. Which non-trivial
  irreducible dominates varies with the seed.
- **Scope.** Recovery is up to isomorphism: characters, dimensions and the
  isotypic projectors are pinned down; explicit per-element matrices `ρ(g)`
  are fixed only up to a change of basis within each isotypic block — the
  identification-up-to-stated-ambiguities of [CLAIM-135](../claims.d/CLAIM-135.md), [CLAIM-148](../claims.d/CLAIM-148.md).

Rerun: `scratch/studies/lead-114/README.md`. Tests in
`test_lead114.py` (10, passing) check the recovery on S3, S4 and ℤ/5 and the
model's gradients.
