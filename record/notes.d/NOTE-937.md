---
number: 937
status: Read
formerly:
- NOTE-tmp9awuq
paper: 'LIT-1162'
title: 'Bertschinger, Rauh, Olbrich, Jost and Ay — Quantifying unique information'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1311.2852v2 (16 Jan 2014), 25 pp.: §§1–6,
    Table 1, Figures 1–2 from captions and prose, Appendices A.1–A.3 and
    references. Nothing skipped. Extracted with pdftotext. I computed the
    measure by convex optimisation over Δ_P (a scratchpad script,
    broja/broja.py, maximising H_Q(X|Y,Z) over the kernel parametrisation
    of Lemma 26, with a dense grid check where Δ_P has dimension ≤ 2) and
    reproduced Example 30 and the Table 1 rows below. A first attempt with
    an unparametrised SLSQP run got AND wrong (SĨ = 0.082 for 0.311), which
    is Example 31's warning in practice. The Entropy version was not
    compared, and Harder, Salge and Polani (LIT-1168) and Williams and
    Beer (LIT-1172), the measures compared, were read separately.
date: '2026-10-17'
summary: >-
  For a target X and sources Y, Z, the unique information of Y is
  UĨ(X : Y \ Z) = min over Q ∈ Δ_P of MI_Q(X : Y | Z), where Δ_P is the set
  of joints with the same (X,Y) and (X,Z) marginals. If unique information
  should depend only on those marginals, this is an upper bound on any such
  measure, and the shared and synergistic information it implies are lower
  bounds. It is zero exactly when the other source is Blackwell-sufficient.
  The measures are non-negative, satisfy the bivariate PI axioms and the
  identity property, and are a convex programme, but are bivariate only.
---

# NOTE-937: Bertschinger, Rauh, Olbrich, Jost and Ay — Quantifying unique information

## Contribution

Before this paper, the bivariate partial information decomposition had
Williams and Beer's I_min, known to give too much redundancy, and Harder,
Salge and Polani's I_red, defined by projections. After it, there is a
decomposition derived from a property, that unique information depends only
on the two source–target channels. That property fixes upper and lower
bounds for every measure that has it, and the bounds are themselves a
decomposition. Their unique information has an operational meaning: it is
zero exactly when one source dominates the other in Blackwell's order.

## Key insight

If unique and shared information depend only on the pair marginals (X,Y)
and (X,Z), then they are constant on Δ_P, and only synergy varies across
it. Synergy cannot be negative, so the joint in Δ_P with the least
information about X sets the bound. Choosing the measure that attains it is
choosing to say that the pair marginals alone never reveal synergy.

## Assumptions

- **Finite alphabets** for X, Y and Z (§1), and X of full support (§2, else
  restrict X to its support).
- **Property (∗):** UI(X : Y \ Z) depends only on p(x) and the channels
  κ = p(y|x), μ = p(z|x). The paper offers decision-theoretic motivation,
  not a proof that every reasonable measure must have it.
- **Continuity** of the decomposition, used in Lemma 3 to extend from
  full-support joints to all of Δ_P.
- **Two sources.** The definitions are for a pair (Y, Z). §6 says the
  shared-information function cannot be extended to three sources on the
  PI lattice.

## Key results

- **Lemma 3.** Under (∗), non-negativity and continuity, any decomposition
  has UI ≤ UĨ, SI ≥ SĨ and CI ≥ CĨ. Equality holds exactly when some
  Q ∈ Δ_P has zero synergy.
- **Lemma 4.** Minimising MI_Q(X : Y | Z), MI_Q(X : Z | Y) or MI_Q(X : (Y,Z)),
  or maximising CoI_Q or H_Q(X | Y,Z), over Δ_P are the same problem, and
  convex.
- **Lemma 5.** UĨ, SĨ, CĨ ≥ 0. SĨ ≥ 0 by the joint Q₀ under which Y ⊥⊥ Z | X.
- **Lemma 6, Corollary 7.** UĨ(X : Y \ Z) = 0 if and only if p(x,y) =
  Σ_z p(x,z)λ(z;y) for a stochastic λ: Y is a garbling of Z with respect to
  X, Blackwell's order.
- **Lemmas 11–13.** Symmetry, the consistency equation (4), the bounds
  SĨ ≤ MI(X:Y) and CĨ ≤ MI(X:Y|Z), and the monotonicity equality when
  X ⊥⊥ Z | Y.
- **Remark 14.** For any binary information decomposition,
  MI(X : Z | Y) = UI(X : Z \ Y) + CI(X : Y; Z). A conditional mutual
  information is unique plus synergistic information, whatever the measure.
- **Proposition 18 (identity property).** For X = (Y, Z), Δ_P = {P},
  CĨ = 0, SĨ = MI(Y : Z), UĨ = H(Y | Z) and H(Z | Y).
- **Lemma 19.** Additivity over independent subsystems. As printed, its
  statement repeats the first subsystem's terms on the right where the
  second's are meant; a typo.
- **Theorems 20, 22.** I_red vanishes exactly when SĨ does, and its unique
  information exactly when UĨ does. On the dice example (Fig. 1) SĨ ≤ I_red,
  with equality at α = 1, 5, 6.
- **Lemma 25.** Unique information cannot grow when sources are added to
  the other side.
- **Example 30 (AND).** UĨ = 0, SĨ = ¾ log(4/3) = 0.311 bits, CĨ = ½ bit.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under (∗), UĨ, SĨ and CĨ bound every non-negative continuous decomposition | strong | Lemma 3, proved |
| C2 | UĨ is zero exactly when the other source is Blackwell-sufficient | strong | Lemma 6 and Blackwell's theorem |
| C3 | The three are non-negative and satisfy the bivariate PI axioms and the identity property | strong | Lemmas 5, 11–13, Proposition 18 |
| C4 | Computing them is a convex programme | strong as stated, weak in practice | Lemma 4; Example 31 shows ill-conditioning; checked here |
| C5 | (∗) is the natural requirement on unique information | interpretive | §2's decision-theoretic argument; not derived |
| C6 | I_min is unreasonably large | moderate | cited to [5], [2]; Table 1's Copy row |
| C7 | The decomposition cannot be extended to three sources on the PI lattice | moderate | cited to [2]; not proved here |

## Method

1. Compute the pair marginals P(X,Y), P(X,Z).
2. Parametrise Δ_P as P plus the kernel of the marginal map, spanned by
   γ_{x;y0,y;z0,z} = δ_{x,y0,z0} + δ_{x,y,z} − δ_{x,y,z0} − δ_{x,y0,z}
   (Lemma 26), within the simplex.
3. Maximise the concave H_Q(X | Y,Z) over that polytope (Lemma 4).
4. At the optimum Q*: UĨ(Y) = MI_{Q*}(X : (Y,Z)) − MI(X : Z),
   UĨ(Z) = MI_{Q*}(X : (Y,Z)) − MI(X : Y), SĨ = MI(X : Y) − UĨ(Y),
   CĨ = MI(X : (Y,Z)) − MI_{Q*}(X : (Y,Z)).

## Checks

Recomputed with broja/broja.py, against I_min from the earlier
te-checks/pid.py. Bits; target first, then the two sources.

| example | BROJA SĨ | UĨ(Y) | UĨ(Z) | CĨ | I_min R | U(Y) | U(Z) | S |
|---|---|---|---|---|---|---|---|---|
| XOR | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| AND | 0.3113 | 0 | 0 | 0.5000 | 0.3113 | 0 | 0 | 0.5000 |
| RDN | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Unq (X = (Y,Z), Y,Z i.i.d.) | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| Copy, P(Y = Z) = 0.9 | 0.5310 | 0.4690 | 0.4690 | 0 | 1 | 0 | 0 | 0.4690 |
| JBC case 1 (target y_t; x_{t−1}, y_{t−1}) | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| WB pair, d = 0.25 (target x_{t+1}; y_t, x_t) | 0 | 0.4564 | 0 | 0.1379 | 0 | 0.4564 | 0 | 0.1379 |
| WB pair, d = 0.5 | 0 | 0.1887 | 0 | 0.3113 | 0 | 0.1887 | 0 | 0.3113 |
| WB pair, d = 0.75 | 0 | 0.0456 | 0 | 0.5488 | 0 | 0.0456 | 0 | 0.5488 |

- Example 30 reproduces: SĨ = 0.3113 = ¾ log₂(4/3), CĨ = ½.
- The Copy row matches Proposition 18: SĨ = MI(Y : Z) = 1 − h(0.1) = 0.5310.
  Table 1 prints its Copy entry as "MI(X : Y)", which for X = (Y,Z) is H(Y),
  1 bit here. Proposition 18 and the computation say MI(Y : Z).
- Table 1's Unq row prints CĨ = 1. Proposition 18 gives CĨ = 0 for
  X = (Y,Z), and so does the computation, with 1 bit unique to each source.
  The row looks transposed or misprinted; I did not check the Entropy
  version.
- I_min gives Unq 1 bit of redundancy and 1 bit of synergy between
  independent sources: the two-bit-copy flaw Harder, Salge and Polani
  report.

## Concepts

- **Δ_P** — the joints sharing P's (X,Y) and (X,Z) marginals, a polytope of
  dimension |X|(|Y| − 1)(|Z| − 1) (Lemma 26).
- **Property (∗)** — unique information depends only on p(x), κ and μ.
- **Property (∗∗)** — the pair marginals alone never reveal synergy.
- **Blackwell order Y ⊒_X Z** — every decision problem about X is solved at
  least as well from Y as from Z.
- **Identity property** — SI((Y,Z) : Y; Z) = MI(Y : Z), proposed as an axiom
  by Harder, Salge and Polani.

## Connections

- **Builds on** Williams and Beer's PI axioms and lattice ([LIT-1172](../literature.d/LIT-1172.md)),
  Harder, Salge and Polani's I_red and their example set ([LIT-1168](../literature.d/LIT-1168.md)),
  and Blackwell (1953) for Lemma 6.
- **The record's transfer-entropy accounts.** Remark 14 is the two-term
  split that [THEORY-712](../theory.d/THEORY-712.md) and [CLAIM-335](../claims.d/CLAIM-335.md) rest on, proved here for
  any bivariate decomposition. Under BROJA the numbers of every
  transfer-entropy example in [THEORY-712](../theory.d/THEORY-712.md) and [THEORY-707](../theory.d/THEORY-707.md) are
  unchanged (table above). That is forced, not a coincidence, by my
  reading: in each example the target's past carries no information about
  the target's next value, MI(X_{t+1} : X_t) = 0. Then any non-negative
  decomposition with (2) has zero shared information and zero unique
  information for the target's past. The split is then fixed by Shannon
  quantities: unique = the time-delayed MI, synergy = TE − time-delayed MI.
  Where MI(X_{t+1} : X_t) > 0 the split would depend on the measure.
- **[THEORY-568](../theory.d/THEORY-568.md) / [LIT-042](../literature.d/LIT-042.md) (Shannon invariants).** Those averages hold for
  any decomposition satisfying the consistency equation. This paper's
  measure is one, so they apply to it. Neither paper draws the link.
- **[NOTE-010](NOTE-010.md) / [THEORY-497](../theory.d/THEORY-497.md) (ΦID).** [NOTE-010](NOTE-010.md) says, of a disagreement with
  the conversion-of-information account, that under a redundancy function
  with the identity property, "e.g. Bertschinger et al.'s", Syn = 0 and the
  two agree. This paper is that property's source (Proposition 18), for two
  sources. ΦID needs more than two sources or targets. By §6 this measure
  does not extend to a non-negative lattice for three, so it cannot be ΦID's
  redundancy function as it stands. That last inference is mine.
- **[NOTE-020](NOTE-020.md) ([LIT-027](../literature.d/LIT-027.md)),** which rests on I_min alone. The Unq and Copy
  rows show I_min's redundancy is not a lower bound on anything sensible,
  so I_min-based synergy for sources that are copied into the target is
  suspect.

## Bearing on the record

- Filed as [THEORY-705](../theory.d/THEORY-705.md).
- [CLAIM-335](../claims.d/CLAIM-335.md) gains a second ground: its decomposition is Remark 14, and
  its examples' numbers do not depend on I_min.
- [CLAIM-335](../claims.d/CLAIM-335.md)'s caveat that "every number beyond the two-term split
  depends on a choice of redundancy function" is too cautious for the
  examples in the record, which the table settles. It stands in general.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Bivariate only.
- Property (∗) is argued, not derived. A measure without it is not shown
  wrong.
- The optimisation is ill-conditioned (Example 31), and this reading's first
  solver attempt failed on AND.
- Table 1 has two entries that conflict with Proposition 18 in the arXiv
  text.
- The dice example compares with I_red by figure only.

## Open questions

- A multivariate decomposition with an operational meaning (the authors'
  own, §6).
- Whether ΦID applications give the same emergence verdicts under a
  bivariate unique-information measure applied pairwise (from [NOTE-010](NOTE-010.md)'s
  open question on robustness across redundancy functions).
