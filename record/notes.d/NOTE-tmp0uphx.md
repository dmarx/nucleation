---
status: Read
paper: 'LIT-tmpeurmb'
title: 'Rauh, Bertschinger, Olbrich and Jost — Reconsidering unique information'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1404.3146v1 (11 Apr 2014), 5 pp.: §§I–V,
    Theorems 1–2, Lemmas 3–4 with their proofs, Fig. 1 (the three-source
    lattice) and the references. Nothing skipped. Extracted with
    pdftotext. I checked Theorem 2's counterexample by hand and its
    information values with a scratchpad script
    (scratchpad/iccs/rauh.py), and computed the same system's atoms under
    I_min and I_ccs. The ISIT version was not compared.
date: '2026-10-17'
summary: >-
  Theorem 2: no redundancy function on the Williams–Beer lattice satisfies
  symmetry, self-redundancy, monotonicity, non-negative atoms and the
  identity axiom. In XORCOPY (two independent bits, their XOR, and the
  target their joint copy) identity forces three 1-bit atoms {i}{jk}
  under a 2-bit total, so {12}{13}{23} ≤ −1. Bertschinger et al.'s
  bivariate measures cannot be extended to that lattice. Their unique
  information is monotone in each argument as expected; their shared and
  synergistic information violate left monotonicity.
---

<!-- inactive-ok-file: THEORY-497 — Proposed; named as the account the theorem bears on, as the record's inference -->

# NOTE-tmp0uphx: Rauh, Bertschinger, Olbrich and Jost — Reconsidering unique information

## Contribution

Before this paper, the identity axiom (Harder et al.) and non-negative
atoms on the Williams–Beer lattice were both standing desiderata for a
redundancy measure. Bertschinger et al. had a bivariate decomposition
satisfying both. After it, the two are known to be incompatible from three
sources on. Any multivariate decomposition that keeps identity must leave
the partial-information lattice or accept negative atoms.

## Key insight

XOR makes every pair of the three variables a relabelling of the whole.
Identity then says each single variable shares exactly its mutual
information with each pair, 1 bit, three times over. But all three pairs
together carry only the 2 bits there are. The lattice's Möbius inversion
has to pay the third bit back with a negative atom.

## Assumptions

- **The Williams–Beer axioms** (§III): symmetry; self-redundancy,
  I∩(X: A) = MI(X: A); monotonicity, I∩(X: A1;…;Ak+1) ≤ I∩(X: A1;…;Ak),
  with equality if some Ai ⊆ Ak+1.
- **Local positivity**: the Möbius-inverted atoms I∂ are non-negative
  (the name is from Bertschinger et al. 2013).
- **The identity axiom**: I∩((Y, Z): Y; Z) = MI(Y: Z). The proof uses it
  with Y a single variable and Z a pair, I∩((Yi,Yj,Yk): Yi; {Yj,Yk}) =
  MI(Yi: {Yj,Yk}).
- **Unstated: invariance under relabelling the target.** The proof sets
  I∩(X: Yi; Yj) = I∩({Yi,Yj}: Yi; Yj) because X = (Y1,Y2,Y3) is a bijective
  image of any pair. That is a property of every measure the paper
  discusses, but it is not among the listed axioms.
- **Finite state spaces** throughout.

## Key results

- **Theorem 1** (restating Bertschinger et al.) — any non-negative
  bivariate decomposition with unique information constant on Δ_P and some
  Q ∈ Δ_P with zero synergy is S̃I, ŨI, C̃I.
- **Theorem 2** — no I∩, I∂ satisfy the Williams–Beer axioms, local
  positivity and identity. *Proof:* XORCOPY as above. I∩(X: Yi; Yj) = 0,
  so the lower two levels vanish; I∂(X: Yi; {Yj,Yk}) = 1 for each of the
  three; I∩(X: {12}{13}{23}) ≤ 2; so I∂ ≤ −1. *Checked:* MI(Yi; Yj) = 0,
  MI(Yi; YjYk) = 1, MI(X; Y1Y2Y3) = 2, and the three nodes {i}{jk} are all
  below {12}{13}{23} and above only zero nodes.
- **Lemma 3** — ŨI(X: Y \ (Z, Z′)) ≤ ŨI(X: Y \ Z); ŨI(X: (Y, Y′) \ Z) ≥
  ŨI(X: Y \ Z); ŨI((X, X′): Y \ Z) ≥ ŨI(X: Y \ Z). Proved by extending a
  Q ∈ Δ_P with a conditionally independent component.
- **Lemma 4** — S̃I(X: (Y, Y′); Z) ≥ S̃I(X: Y; Z), by the coinformation chain
  rule.
- **§IV-B, §IV-C** — no monotone relation for S̃I or C̃I in the target, and
  none for C̃I in a source. AND: S̃I(Z: X; Y) ≈ 0.311 > 0 = S̃I((X, Y): X; Y).
  XOR: C̃I(X: Y; Z) = 1 > 0 = C̃I((Y, Z): Y; Z). So none satisfies a chain
  rule of the form SI((X, X′): Y; Z) = SI(X: Y; Z) + SI(X′: Y; Z | X).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Identity, the Williams–Beer axioms and non-negative atoms are jointly inconsistent for three sources | strong | Theorem 2; a four-line proof, checked; rests also on relabelling invariance |
| C2 | So a consistent multivariate extension of S̃I, ŨI, C̃I cannot be a partial information decomposition | strong | from C1 |
| C3 | ŨI is monotone in all three arguments in the expected directions | strong | Lemma 3, proved |
| C4 | S̃I increases with a source | strong | Lemma 4, proved |
| C5 | S̃I and C̃I violate left monotonicity, and this is due to the identity axiom | moderate | AND and XOR examples; "strict" for C̃I, "more subtle" for S̃I (§V) |
| C6 | MI minus the sum of unique informations is non-negative | conjecture | §V; would follow from a stated superadditivity of ŨI |

## Concepts

- **Local positivity** — non-negativity of every partial-information atom
  I∂ on the lattice.
- **Left monotonicity** — SI((X, X′): Y; Z) ≥ SI(X: Y; Z), shared information
  not decreasing as the target grows.
- **XORCOPY** — the counterexample system; Ince calls it by that name
  ([NOTE-tmprcqzl](NOTE-tmprcqzl.md), §6.2.2).

## Connections

- **Builds on** Bertschinger et al. 2014 ([LIT-1162](../literature.d/LIT-1162.md), [NOTE-937](NOTE-937.md)), whose
  measures it tries to extend, the lattice of Williams and Beer 2010
  ([LIT-1172](../literature.d/LIT-1172.md), [NOTE-936](NOTE-936.md)), and the identity axiom of Harder, Salge and
  Polani ([LIT-1168](../literature.d/LIT-1168.md), [NOTE-944](NOTE-944.md)). The proof idea is credited to Bertschinger,
  Rauh, Olbrich and Jost 2013 (ECCS), not held.
- **What other measures do with XORCOPY**, computed here
  (scratchpad/iccs/rauh.py, checks.py). I_min keeps non-negativity by
  failing identity: its non-zero atoms are {1}{2}{3} = 1 and {12}{13}{23} = 1,
  so it calls the independent Y1 and Y2 redundant. Ince's I_ccs keeps
  identity for independent sources and pays with the negative atom:
  {i}{jk} = 1 each and {12}{13}{23} = −1, matching the bound exactly. My
  computation; Ince reports the same I_ccs values.
- **[THEORY-497](../theory.d/THEORY-497.md) and [NOTE-010](NOTE-010.md).** ΦID decomposes over a product of
  Williams–Beer lattices, one for the parts' past and one for their
  future ([NOTE-010](NOTE-010.md): 4 × 4 = 16 atoms for two parts). So this theorem bears
  on it whenever a system has three or more parts. With two parts each
  factor is the bivariate lattice, where Bertschinger et al.'s measures
  are consistent. That is my inference: the paper does not mention ΦID,
  which came later.

## Bearing on the record

- Filed as [THEORY-tmp06heo](../theory.d/THEORY-tmp06heo.md).
- The gap the PID filing named, a multivariate identity-property
  redundancy for ΦID, is shown impossible as stated, not merely unfilled.
  The record should say so in its own voice.
- [NOTE-010](NOTE-010.md)'s remark that Bertschinger et al.'s and Harder et al.'s measures
  are bivariate, so neither serves as ΦID's redundancy as it stands, is
  sharpened. No measure with identity can, on that lattice, without
  negative atoms.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- An impossibility for one framework. It says nothing about decompositions
  that leave the Williams–Beer lattice, which the paper calls for without
  giving one.
- The relabelling-invariance premise is used and not stated.
- The proof uses identity with a pair as one of the two sources. A weaker
  identity restricted to single variables is not ruled out by this
  argument. My observation; the paper does not discuss it.
- Five pages: the bivariate lemmas are proved, the conjecture is not.

## Open questions

- What structure should a multivariate decomposition have once the lattice
  is given up (the authors' own, §V)?
- The superadditivity conjecture for ŨI (§V).
