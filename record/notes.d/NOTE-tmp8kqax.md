---
status: Read
paper: 'LIT-tmpmva6y'
title: 'Williams and Beer — Nonnegative decomposition of multivariate information'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1004.2515v1 (14 April 2010), 14 pp.: §§I–VI,
    Appendices A–D (the proofs of Theorems 1–5 followed step by step),
    Appendix E's supplementary figures from captions only, references.
    Extracted with pdftotext; Figs. 2–5 came through as captions and I
    read the lattices and PI-diagrams from the prose. I recomputed the
    Fig. 4A values (from a distribution I reconstructed from the text),
    XOR, AND, three-variable copy, 3-parity and three copies, and the
    lattice sizes, with a scratchpad script (pid-checks/pid2.py). I could
    not reconstruct Fig. 4B's distribution from the text, so its values are
    unchecked.
date: '2026-10-17'
summary: >-
  Redundancy is I_min(S; A₁…A_k) = Σ_s p(s) min_i I(S = s; A_i), the
  expected minimum specific information. Restricted to antichains of
  sources and ordered by α ≼ β iff every source of β contains one of α,
  the collections form a lattice. The Möbius inverse of I_min on it gives
  partial-information atoms that are nonnegative (Theorem 5) and sum to
  I(S; R). Interaction information is synergy minus redundancy for three
  variables and a signed mixture for four, which explains its negativity
  and its +1 bit for both 3-parity and three copies.
---

# NOTE-tmp8kqax: Williams and Beer — Nonnegative decomposition of multivariate information

## Contribution

Before this paper, the standard multivariate extension of mutual
information was interaction information, which can be negative and mixes
redundancy with synergy. After it there is a general scheme: choose a
redundancy function on the lattice of antichains of sources, invert it,
and the information that a set of sources gives about a target splits
into atoms. One atom per lattice node: redundancy, unique information,
synergy and, from three sources on, mixtures such as "redundancy between
a single source and a pairwise synergy". The paper also gives one
redundancy function, I_min, for which every atom is provably
nonnegative.

## Key insight

Mutual information is an average over outcomes of the target. Two sources
can give the same average information while informing about different
outcomes, so redundancy should be measured outcome by outcome and then
averaged. Once redundancy is defined on the lattice, everything else
follows by inclusion–exclusion on the lattice, not on sets.

## Assumptions

- **Discrete variables**, with a joint distribution known exactly. No
  estimation is discussed.
- **A distinguished target S.** The decomposition is asymmetric: the
  synergy of R₁, R₂ about S is not that of S, R₂ about R₁ (§IV, Fig. 4A).
- **Specific information** in the DeWeese–Meister form
  I(S = s; A) = Σ_a p(a|s)[log 1/p(s) − log 1/p(s|a)] = D_KL(p(a|s) ‖ p(a))
  (Eq. 2, Theorem 1). It is the only nonnegative specific information
  (Appendix A, citing DeWeese and Meister).
- **The redundancy function is a choice.** The lattice and the inversion do
  not depend on I_min. Nonnegativity of the atoms does, and is proved
  only for I_min.

## Key results

- **Eq. 3, I_min**, with properties: nonnegative; at most I(S; A_i) for
  every source, with equality iff all sources give equal specific
  information about every outcome; I_min(S; {A}) = I(S; A).
- **Eqs. 4–5, the redundancy lattice.** A(R) = antichains of nonempty
  subsets of R, ordered by α ≼ β ⇔ ∀B ∈ β ∃A ∈ α, A ⊆ B. Its size for n − 1
  sources is the (n − 1)-th Dedekind number: 1, 4, 18, 166, 7579.
  *Checked:* 4 and 18 by enumeration.
- **Eqs. 6–8, the PI-function.** I_min(S; α) = Σ_{β≼α} Π(S; β), so Π is the
  Möbius inverse; closed form Π(S; α) = I_min(S; α) − Σ_s p(s) max_{β∈α⁻}
  min_{B∈β} I(S = s; B) (Theorem 4, via the maximum–minimums identity).
- **Theorem 2.** I_min is monotone on the lattice. **Theorem 5.** Π ≥ 0.
- **Eqs. 10–11, two sources.** I(S; R₁) = Π{1} + Π{1}{2};
  I(S; R₁, R₂) = Π{1} + Π{2} + Π{1}{2} + Π{12}.
- **Fig. 4A.** S ∈ {0, 1, 2}, three equiprobable outcomes. Unique 1/3 bit
  each, redundancy log 3 − log 2 = 0.585 bit, synergy 1/3 bit.
  *Checked* on the distribution (R₁, R₂) → S: (0,0) → 0, (0,1) → 1,
  (1,0) → 2, which fits the text's description ("given knowledge of R₁,
  one can determine conclusively whether or not outcome S = 2 occurs"):
  0.333, 0.333, 0.585, 0.333.
- **Eq. 14.** I(S; R₁; R₂) = Π{12} − Π{1}{2}: positive means more synergy than
  redundancy, not synergy alone.
- **Eq. 15, four variables.** I(S; R₁; R₂; R₃) = Π{123} + Π{1}{2}{3} − the
  three {i}{jk} − the three {ij}{ik} − 2Π{12}{13}{23}. *Checked:* 3-parity
  has the single nonzero atom Π{123} = 1 and three copies the single atom
  Π{1}{2}{3} = 1, and the four-variable interaction information is +1 bit
  for both.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Antichains of sources under ≼ form a lattice whose size is a Dedekind number | strong | Appendix C, citing Crampton and Loizou; sizes checked |
| C2 | Any redundancy function on the lattice has a Möbius inverse that sums to the mutual informations | strong | Eqs. 6–9; standard order theory |
| C3 | Under I_min every atom is nonnegative | strong | Theorems 2–5, proofs followed |
| C4 | I_min measures redundancy in the intended sense: information common to all sources | weak | argued from its properties (§III); Harder, Salge and Polani give a counterexample (LIT-tmpgtytt) |
| C5 | Interaction information confounds redundancy and synergy, and four-variable interaction information cannot tell pure synergy from pure redundancy | strong | Eqs. 14–15; checked on 3-parity and three copies |
| C6 | Every atom has a "clear interpretation" as redundancy among synergies | interpretive | §IV; follows from the lattice, but what the atoms mean depends on the redundancy function |

## Concepts

- **Specific information I(S = s; A)** — the average reduction in surprise
  of the outcome s given A (Eq. 2).
- **Source** — a nonempty subset of R; a collection of sources is an
  antichain if none contains another.
- **Redundancy lattice** — ⟨A(R), ≼⟩ (Fig. 2).
- **PI-atom Π(S; α)** — the information provided redundantly by the
  sources of α and by no collection below α.

## Connections

- **Builds on** McGill's interaction information, Bell's co-information,
  DeWeese and Meister's and Butts's specific informations, and Crampton
  and Loizou's lattice of antichains.
- **[LIT-tmpsbhb4](../literature.d/LIT-tmpsbhb4.md) (Williams and Beer 2011, [NOTE-tmpr176u](NOTE-tmpr176u.md))** applies this
  decomposition to transfer entropy. Its two-term split of a conditional
  mutual information is Eqs. 10–11 rearranged, and holds for any
  redundancy function that satisfies them.
- **[LIT-tmpgtytt](../literature.d/LIT-tmpgtytt.md) (Harder, Salge and Polani, [NOTE-tmpsow60](NOTE-tmpsow60.md))** shows C4 fails:
  two independent bits copied into S get 1 bit of I_min redundancy.
  *Checked:* I_min = 1 for every correlation between the copied bits.
- **[LIT-tmp5b2vz](../literature.d/LIT-tmp5b2vz.md) (Bertschinger et al.)** gives a unique-information
  measure for two sources with the same consistency equations.
- **[LIT-042](../literature.d/LIT-042.md) (Shannon invariants, [NOTE-045](NOTE-045.md), [THEORY-568](../theory.d/THEORY-568.md))** takes this
  lattice and asks what is fixed whatever the redundancy function. Its
  invariants depend only on C2, not on I_min.
- **[LIT-027](../literature.d/LIT-027.md) (Varley and Hoel, [NOTE-020](NOTE-020.md), [THEORY-581](../theory.d/THEORY-581.md))** computes its
  synergy bias with I_min. Its numbers therefore inherit C4's problem. Its
  authors acknowledge I_min's critiques and try no other measure.
- **[LIT-025](../literature.d/LIT-025.md) (ΦID review, [NOTE-010](NOTE-010.md), [THEORY-497](../theory.d/THEORY-497.md))** extends this lattice
  to the product of a past lattice and a future lattice; it needs a
  redundancy function too and names none.

## Bearing on the record

- Filed as [THEORY-tmpeogx6](../theory.d/THEORY-tmpeogx6.md), the account of what is general (C1–C3, C5) and
  what is I_min's (C4).
- [THEORY-tmpt4nh7](../theory.d/THEORY-tmpt4nh7.md) and [CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md) rest on C2 only, as they say. The
  numbers past the two-term split rest on I_min; recomputed under
  Harder, Salge and Polani's I_red they do not change (NOTE-tmpsow60).
- [NOTE-tmpr176u](NOTE-tmpr176u.md) and [LIT-tmpsbhb4](../literature.d/LIT-tmpsbhb4.md) say this paper is not held; now it is.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- C4 is argued from properties, not tested against cases where the answer
  is independently known. The copy example breaks it.
- The paper is a preprint; I found no refereed version.
- Fig. 4B could not be reconstructed from the text. A distribution matching
  its description gave redundancy ½ but synergy 1, not the ½ the paper
  states, so the guess was wrong, not the paper; its values stay
  unchecked.
- The lattice grows as the Dedekind numbers, so the full decomposition is
  impractical beyond four or five sources (§VI).

## Open questions

- Which redundancy function, if any, satisfies the authors' axioms, the
  identity property and nonnegativity for three or more sources? Harder,
  Salge and Polani's is bivariate only.
