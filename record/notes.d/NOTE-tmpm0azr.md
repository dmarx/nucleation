---
status: Read
paper: 'LIT-tmpk8n6l'
title: 'Griffith, Chong, James, Ellison and Crutchfield — Intersection information based on common randomness'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1310.1538v3 (10 June 2015), 14 pp.: §§1–7,
    Figs. 1–4, Appendices A–C with all lemmas. Extracted with pdftotext;
    Table 1's check marks did not survive, so the property list below is
    taken from Lemmas 1–6. I recomputed every example, and the measure on
    Harder, Salge and Polani's copy family and a three-source copy, with a
    scratchpad script (griffith/gk_check.py), which finds the common
    random variable as the connected components of the sources' support.
    The Entropy version was not compared.
date: '2026-10-17'
summary: >-
  The redundancy is the information about the target in the Gács–Körner
  common random variable of the sources, I_∧ = I(X_1 ∧ … ∧ X_n : Y): the
  largest I(Q : Y) for Q a function of every source. It is defined for any
  n, satisfies target monotonicity, which no earlier measure did, and lies
  below I_min. But it is zero whenever the sources have full support, so
  it fails identity and continuity, and its synergy goes negative. A
  zero-error variant satisfies identity in zero-error form and goes
  negative too.
---

# NOTE-tmpm0azr: Griffith, Chong, James, Ellison and Crutchfield — Intersection information based on common randomness

## Contribution

Before this paper the candidate redundancies (I_min, I_red, Bertschinger
et al.'s, Griffith and Koch's) were all bivariate or unsatisfactory, and
none had target monotonicity. This paper extends the list of desired
properties to eleven, three of them new (a lower bound, strong
monotonicity, equivalence-class invariance), and proposes the
common-random-variable measure, which satisfies seven, target
monotonicity among them, for any number of sources. It diagnoses its own
main failure precisely.

## Key insight

What is certainly shared between sources is what each of them determines
exactly: the finest variable that is a function of every source, the
Gács–Körner common random variable. Its information about the target is
uncontroversially redundant, so any reasonable redundancy is at least
this much.

## Assumptions

- **Finite variables**; X ≼ Y means X is a function of Y almost surely
  (§2.1). The common random variable is computable for n variables by
  the algorithm of Wolf and Wullschleger (§2.2).
- **The intersection is relative to an information measure** I, Shannon
  or zero-error (§2.3), with I(X : Y) = 0 for constant Y.
- **Redundancy is deterministic shared structure.** This is the choice
  that makes it zero under full support.

## Key results

- **Lemma 8.** I_∧(X_1, …, X_n : Y) = I(X_1 ∧ … ∧ X_n : Y).
- **Lemmas 4–6.** I_∧ satisfies GP, Eq, TM, M₀, S₀, LB and SR. It fails
  LP₀ (ImperfectRdn), Id (Lemma 5: I_∧(X, Y : X ∨ Y) = H(X ∧ Y), not
  I(X : Y)), M₁, S₁ and LP₁. The proof of Lemma 5 has "Y f Y" where
  "X g Y" is meant, by its own argument.
- **Lemmas 1–3.** The zero-error I₀∧ = H(X_1 ∧ … ∧ X_n ∧ Y) satisfies all
  but LP₀ and LP₁, identity included in its zero-error form.
- **Lemma 9.** 0 ≤ I₀∧ ≤ I_∧ ≤ I_min.
- **Examples, recomputed** (bits; synergy derived through Eq. 7):

  | Example | I_∧ | synergy under I_∧ | I_min |
  |---|---|---|---|
  | Unq | 0 | 0 | 1 |
  | RdnXor | 1 | 1 | 1 |
  | ImperfectRdn | 0 | −0.9896 | 0.9896 |
  | Subtle | 0 | −0.2516 | 0.5850 |
  | Xor | 0 | 1 | 0 |
  | And | 0 | 0.1887 | 0.3113 |
  | Rdn | 1 | 0 | 1 |

  The paper's −0.99 and −0.252 reproduce. The zero-error intersection
  H(∧X_i ∧ Y) takes the same value as I_∧ in every example here; its
  decomposition is of zero-error information, which I did not recompute.
- **Copy family** (Harder, Salge and Polani's Z = (X, Y) with correlation
  λ): I_∧ = 1 at λ = 0 and 0 for every λ in (0, 1], against I(X : Y) =
  0.242, 0.046 and 0.003 at λ = 0.25, 0.5, 0.75. The identity property
  fails everywhere strictly inside, and synergy is −I(X : Y) there.
- **Three sources.** With Z = (X, Y, W) copying three correlated bits,
  I_∧ is 1 at full correlation and 0 at λ = 0.5, where every pairwise
  mutual information is 0.046. So for n > 2 it is nonnegative and defined,
  but no closer to identity. My computation.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | I_∧ = I(∧_i X_i : Y), and it is a lower bound on any reasonable redundancy | strong | Lemma 8; the bound is an argument from LB, which is a stipulated property |
| C2 | I_∧ is the first intersection information to satisfy target monotonicity | moderate | Lemma 4 for I_∧; "first" against the four measures in Table 1 |
| C3 | I_∧ fails identity and local positivity | strong | Lemma 5; ImperfectRdn −0.99, recomputed |
| C4 | I_∧ is discontinuous: any noise between the sources sends it to zero | strong | §5.3; copy family recomputed |
| C5 | The zero-error I₀∧ satisfies nine of eleven properties | strong | Lemmas 1–3 |
| C6 | Negative synergy means the intersection is too small | moderate | §6, from Eq. 9 and the existence of functions f_1, f_2 with X_i = f_i(X_1 ∨ X_2) |
| C7 | Within zero-error information, identity and local positivity are incompatible | moderate | Subtle (Fig. 4), and cited result of Bertschinger et al. [4] |

## Concepts

- **Common random variable X ∧ Y (meet)** — the informationally richest
  variable that is a function of both (§2.2); its entropy is the
  zero-error information.
- **Join X ∨ Y** — the poorest variable both are functions of; the pair
  (X, Y) is one instance.
- **The eleven properties** — GP, Eq, TM, M₀, S₀, LB, Id, LP₀, M₁, S₁, LP₁
  (§2.3).

## Connections

- **Builds on** Williams and Beer's lattice ([LIT-1172](../literature.d/LIT-1172.md)), Gács and Körner
  (1973), and Li and Chong's information lattice. Compares itself with
  I_min and Harder, Salge and Polani's I_red ([LIT-1168](../literature.d/LIT-1168.md)).
- **Griffith and Koch ([NOTE-tmp71sln](NOTE-tmp71sln.md)).** I_∧ formalises that paper's v1
  view: redundancy only where the sources share structure, I_∧ ≤ H(X_1 ∧
  X_2) ≤ I(X_1 : X_2). In AND it reproduces v1's answer exactly (0
  redundant, 0.311 unique each, 0.189 synergy), which v6 had withdrawn.
  My observation.
- **Harder, Salge and Polani ([THEORY-708](../theory.d/THEORY-708.md)).** The two are the poles of the
  mechanistic-redundancy dispute: I_red gives AND 0.311 bit redundant,
  I_∧ gives 0.
- **Bertschinger et al. ([THEORY-705](../theory.d/THEORY-705.md)).** Their measure satisfies identity
  and local positivity for two sources. This one gives up both to reach
  any n.
- **[THEORY-568](../theory.d/THEORY-568.md).** The atoms here come from Eq. 7, so they satisfy the
  consistency equations, and the Shannon invariants are unaffected; only
  the individual atoms, which can be negative, change.

## Bearing on the record

- Filed as [THEORY-tmp7uuzn](../theory.d/THEORY-tmp7uuzn.md).
- On the gap "no held measure gives ΦID an identity-property redundancy
  for more than two sources": this measure is defined for any n and is
  nonnegative, but it has no Shannon identity property and gives negative
  atoms already for two sources. It does not close the gap. Its
  zero-error variant has identity only for zero-error information.
- [NOTE-010](NOTE-010.md)'s permutation (X¹, X²) → (X¹ ⊕ X², X¹): the sources share no
  deterministic structure, so I_∧ = 0 and the synergy is 0, agreeing with
  the identity-property measures there.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Zero under full support, so useless on noisy data, which the paper
  says.
- Negative synergy for two sources.
- The eleven properties are a wish list. Some are argued for, not
  derived, and Bertschinger et al. show some are jointly unsatisfiable.

## Open questions

- A continuous measure with target monotonicity and local positivity
  (the authors', §7.3).
- What zero-error overlap I₀∧ misses in Subtle (§7.3).
