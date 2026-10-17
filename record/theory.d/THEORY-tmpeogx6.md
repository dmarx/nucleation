---
status: Active
title: "Any redundancy function defined on the lattice of antichains of sources, ordered so that a collection precedes another when every source of the latter contains one of the former, has a Möbius inverse that decomposes the information a set of sources gives about a target into partial-information atoms summing to every subset's mutual information; for the I_min redundancy, the expected minimum specific information over sources, every atom is nonnegative, and interaction information is a signed mixture of atoms, synergy minus redundancy for three variables"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-tmpmva6y
summary: >-
  Williams & Beer (2010), [LIT-tmpmva6y](../literature.d/LIT-tmpmva6y.md), read in full in [NOTE-tmp8kqax](../notes.d/NOTE-tmp8kqax.md).
  The lattice, the inversion and the nonnegativity proofs are exact and
  were followed; the lattice sizes and the 3-parity and three-copies
  cases were checked. What is not shown is that I_min measures shared
  information: it gives two independent copied bits 1 bit of redundancy
  (Harder, Salge and Polani).
---

# THEORY-tmpeogx6: Any redundancy function defined on the lattice of antichains of sources, ordered so that a collection precedes another when every source of the latter contains one of the former, has a Möbius inverse that decomposes the information a set of sources gives about a target into partial-information atoms summing to every subset's mutual information; for the I_min redundancy, the expected minimum specific information over sources, every atom is nonnegative, and interaction information is a signed mixture of atoms, synergy minus redundancy for three variables

## Source

Williams & Beer (2010), "Nonnegative Decomposition of Multivariate
Information", arXiv 1004.2515v1, [LIT-tmpmva6y](../literature.d/LIT-tmpmva6y.md), read in full in
[NOTE-tmp8kqax](../notes.d/NOTE-tmp8kqax.md). An unrefereed preprint.

## What was actually shown

**The lattice.** Antichains of nonempty source sets, with α ≼ β iff every
B ∈ β contains some A ∈ α, form a lattice. It has 4 nodes for two
sources and 18 for three (checked).

**The inversion.** For a redundancy function I∩ on the lattice, define the
atoms by I∩(S; α) = Σ_{β≼α} Π(S; β). Then I(S; A) = Σ_{β≼{A}} Π(S; β) for
every source A. For two sources: redundancy, two unique terms, synergy.

**I_min.** I_min(S; α) = Σ_s p(s) min_{A∈α} D_KL(p(a|s) ‖ p(a)). It is
monotone on the lattice and its atoms are nonnegative (Theorems 2–5).

**Interaction information.** I(S; R₁; R₂) = Π{12} − Π{1}{2}. The
four-variable version is a signed mixture of nine atoms, one counted
twice, and is +1 bit both for 3-parity (only Π{123} = 1) and for three
copies of S (only Π{1}{2}{3} = 1). Both checked.

What could have come out otherwise: the Möbius inverse of an arbitrary
redundancy function can be negative. For I_min it cannot, and that had to
be proved.

## What this does not say

- **That I_min measures information the sources share.** It compares
  amounts per outcome, not content. For Z = (X, Y) with X, Y independent
  bits it gives 1 bit of redundancy ([THEORY-tmpim3f9](THEORY-tmpim3f9.md)).
- **That the atoms have one meaning whatever the redundancy function.** The
  labels (redundancy, synergy) are fixed by the lattice; the amounts are
  not.
- **That nonnegativity holds for other redundancy functions.** It must be
  proved for each.
- **Anything about estimation from data**, or about continuous variables.
- **That the decomposition is computable for many sources.** Its size is a
  Dedekind number.

## Connections

- [THEORY-tmpt4nh7](THEORY-tmpt4nh7.md) is the inversion applied to transfer entropy. Its two-term
  split uses only the inversion; its numbers use I_min.
- [THEORY-568](THEORY-568.md) states what is fixed whatever the redundancy function, which is
  the part of this account that does not depend on I_min.
- [THEORY-581](THEORY-581.md)'s synergy bias is computed with I_min.
- [THEORY-tmpim3f9](THEORY-tmpim3f9.md) corrects I_min for two sources.
