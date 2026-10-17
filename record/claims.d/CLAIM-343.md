---
number: 343
status: Active
formerly:
- CLAIM-tmpqjpx1
title: 'For three or more parts, no ΦID can use a redundancy function that both satisfies the identity axiom and yields nonnegative atoms, because on the Williams–Beer lattice the two are inconsistent from three sources up; a ΦID verdict on three or more parts therefore rests on which axiom the analyst drops, and should name it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in Rauh et al.'s XORCOPY argument: a demonstration that the
  identity axiom does not force each atom {i}{jk} to 1 bit there, or that
  the total is not 2 bits. Or a ΦID for three or more parts whose source
  lattice is not the Williams–Beer lattice. Or a redundancy function shown
  to satisfy the Williams–Beer axioms, the identity axiom and nonnegative
  atoms on XORCOPY. Disagreement over whether negative atoms are
  meaningful does not bear on it; it bears only on which axiom to drop.
tags:
- information-theory
- complex-systems
date: '2026-10-17'
line:
- formal-apparatus
grounds:
- THEORY-713
- THEORY-714
complements:
- CLAIM-335
summary: >-
  The record's answer to the gap left by the PID filing: no held measure
  gave ΦID an identity-respecting redundancy for more than two sources.
  Rauh et al. show none can, on the lattice ΦID uses, without a negative
  atom ([THEORY-713](../theory.d/THEORY-713.md)). The record's measures split the difference: I_min
  keeps atoms nonnegative by calling independent copied bits redundant,
  and Ince's I_ccs keeps an independent-sources identity and reports a
  −1-bit atom ([THEORY-714](../theory.d/THEORY-714.md)). Two-part ΦID is untouched.
---
<!-- inactive-ok-file: THEORY-714 THEORY-497 — Proposed; cited for what each measure or account computes, not as settled -->

# CLAIM-343: For three or more parts, no ΦID can use a redundancy function that both satisfies the identity axiom and yields nonnegative atoms, because on the Williams–Beer lattice the two are inconsistent from three sources up; a ΦID verdict on three or more parts therefore rests on which axiom the analyst drops, and should name it

## The claim

ΦID decomposes the information a system's past carries about its future
over a product of two Williams–Beer redundancy lattices, one for the
sources and one for the targets ([THEORY-497](../theory.d/THEORY-497.md), [NOTE-010](../notes.d/NOTE-010.md)). With three or more
parts, the source lattice is the three-source lattice or larger.

On that lattice, Rauh et al.'s Theorem 2 rules out any redundancy function
satisfying symmetry, self-redundancy, monotonicity, the identity axiom and
nonnegative atoms together ([THEORY-713](../theory.d/THEORY-713.md)). The case is XORCOPY: Y₁, Y₂
independent bits, Y₃ = Y₁ ⊕ Y₂, target X = (Y₁, Y₂, Y₃). Each Yᵢ is a
function of the other two, so identity gives each atom {i}{jk} 1 bit. The
three come to 3 bits against I(X; Y₁Y₂Y₃) = 2, so {12}{13}{23} is at most
−1. The arithmetic was checked on 2026-10-17 ([NOTE-965](../notes.d/NOTE-965.md)). The proof also
uses two premises the paper does not list as axioms: invariance under
relabelling the target, and identity applied with a pair of variables
treated as one source.

So the deficit lands somewhere, and the record's measures show where:

- **I_min** gives {1}{2}{3} = 1 and {12}{13}{23} = 1, all nonnegative,
  because it does not satisfy identity ([THEORY-706](../theory.d/THEORY-706.md), [THEORY-708](../theory.d/THEORY-708.md)).
- **I_ccs** gives {i}{jk} = 1 each and {12}{13}{23} = −1, exactly at Rauh
  et al.'s bound, keeping only an identity for independent sources
  ([THEORY-714](../theory.d/THEORY-714.md)).
- **Griffith et al.'s I_∧** is defined for any number of sources and is
  nonnegative, but fails identity and has negative atoms already for two
  ([THEORY-715](../theory.d/THEORY-715.md)).
- **I_red and Bertschinger et al.'s measure** are bivariate and do not reach
  three parts ([THEORY-708](../theory.d/THEORY-708.md), [THEORY-705](../theory.d/THEORY-705.md)).

A ΦID verdict on three or more parts therefore rests on which axiom the
analyst gave up. Reported without that, it cannot be compared across
studies that chose differently.

## What it does not say

- **Anything against two-part ΦID.** There the bivariate measures are
  consistent, and the record's transfer-entropy examples give the same
  values under all four two-source measures ([CLAIM-335](CLAIM-335.md)).
- **That no multivariate decomposition can exist.** Rauh et al. leave open
  what one off the Williams–Beer lattice would look like.
- **That negative atoms are meaningless.** Ince reads them as mechanistic
  redundancy. The claim is only that some axiom has to give.
