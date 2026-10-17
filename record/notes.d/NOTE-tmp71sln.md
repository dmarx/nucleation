---
status: Read
paper: 'LIT-tmpx01yr'
title: 'Griffith and Koch — Quantifying synergistic mutual information'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1205.4265v6 (31 March 2014), 25 pp.: §§1–8,
    Table 1, Appendices A–F; figures from their captions and the PI-diagram
    labels that survived extraction. Versions 1 (18 May 2012) and 2 (28
    October 2012) were read only for the AND example and the passage on
    independent predictors, which v6 withdraws. Extracted with pdftotext.
    Every Table 1 value except S_VK for three predictors was recomputed
    with a scratchpad script (griffith/gk_check.py), which takes S_VK for
    two predictors from the BROJA solver (broja/broja.py), the same
    optimisation. I did not check the proof of S_VK ≤ S_max (Appendix
    E.2.1) line by line. The book chapter was not compared.
date: '2026-10-17'
summary: >-
  Synergy is the whole minus the union of its parts. S_VK = I(X_1…n : Y)
  − I_VK, where the union information I_VK is the least I*(X_1…n : Y)
  over joints that keep every source–target marginal. It sits between
  WholeMinusSum and S_max, which respectively subtract redundancy and
  count unique bits as synergy, and correlational importance measures
  something else. Versions 1–2 held that independent predictors share no
  information about the target; v6 withdraws it. For two predictors I_VK
  is Bertschinger et al.'s optimisation, so S_VK is their CI.
---

# NOTE-tmp71sln: Griffith and Koch — Quantifying synergistic mutual information

## Contribution

Before this paper, synergy was measured as Williams and Beer's S_max, as
WholeMinusSum (a difference of total correlations) or as correlational
importance ΔI. Each misreads some binary circuit. The paper sets out a
suite of circuits with intuitive answers, shows where each measure fails,
and proposes "whole minus union", S_VK, with an optimisation-defined union
information. In its last version it also records a change of position:
independent predictors can carry redundant information about a target.

## Key insight

The parts' union should be what the singletons' joint relations with the
target fix and no more. So keep every Pr(X_i, Y), let everything else
vary, and take the least information the whole could then carry. What
the actual whole carries beyond that is synergy.

## Assumptions

- **Discrete, finite variables**; all examples deterministic, the method
  stated to apply generally (§1).
- **The union is determined by the singleton–target marginals** (Eq. 13
  and fn. 9). The looser constraint I*(X_i : Y) = I(X_i : Y) is
  considered and rejected, to preserve "the same bits".
- **Intuition about the examples** is the test. Each circuit has an
  intended answer stated before the measures are applied.
- **Monotonicity (M) of the derived intersection information** is
  assumed, not proved, for invariance to duplicated predictors
  (Appendix E.1).

## Key results

- **Eq. 13, I_VK.** min over Pr* with Pr*(X_i, Y) = Pr(X_i, Y) of
  I*(X_1…n : Y). The product Pr(y)ΠPr(x_i|y) satisfies the constraints,
  so the minimum exists, and that product's information is an analytic
  upper bound on I_VK (Appendix D). *Checked:* for AND the bound gives
  S_VK ≥ 0.2704, the paper's 0.270.
- **Eq. 15, bounds.** max(0, WMS) ≤ S_VK ≤ S_max. Proved in Appendix E.2;
  the S_max half writes I_VK as an expectation of per-state minima, a step
  I could not reconstruct, since I*(X : Y) couples the states of Y
  through H*(X). Every example checked satisfies the bounds.
- **§6, properties of I_VK.** Global positivity, self-redundancy, weak
  symmetry, weak local positivity (two predictors) and strong identity
  I_VK(X : X_1…n) = H(X_1…n) are proved (Appendix C). Monotonicity and
  target monotonicity are listed among the satisfied properties; I found
  no proof of either. Strong symmetry is disproved.
- **Table 1, recomputed** (bits):

  | Example | S_max | WMS | ΔI | S_VK |
  |---|---|---|---|---|
  | Rdn | 0 | −1 | 0 | 0 |
  | Unq | 1 | 0 | 0 | 0 |
  | Xor | 1 | 1 | 1 | 1 |
  | XorDuplicate | 1 | 1 | 1 | not computed (bound ≥ 1) |
  | XorLoses | 0 | 0 | 0 | 0 (I_VK ≥ I(X_3 : Y) = 1) |
  | RdnXor | 1 | 0 | 1 | 1 |
  | And | 0.5 | 0.1887 | 0.1038 | 0.5000; paper: [0.270, 0.5] |
  | AndDuplicate | 0.5 | −0.1226 | 0.0380 | not computed (bound ≥ 0.130) |

  All the paper's values match. For AndDuplicate the product-distribution
  bound gives only S_VK ≥ 0.130. The paper's [0.270, 1/2] there is And's
  interval carried over by its duplicate-invariance argument, which
  assumes (M) for the derived intersection (Appendix E.1).
- **The AND value the paper leaves open.** For two predictors, I_VK's
  constraint set is Bertschinger et al.'s Δ_P, and minimising
  I*(X_1X_2 : Y) there is maximising H*(Y | X_1X_2), since H(Y) is fixed
  by the marginals. So S_VK = CI_BROJA and I_VK = I − CI_BROJA. For AND,
  S_VK = 0.5 bit: the upper end of the paper's interval. The derived
  redundancy is 0.311 bit, equal to I_min and I_red. *My derivation*; the
  paper does not make it, and Bertschinger et al. call their quantity a
  union information without citing this definition for it.
- **The reversal (Fig. 11's note).** v1 §4 and v2: "because X1 and X2 are
  independent, I(X1 : X2) = 0 bits, there must be zero redundant
  information". So AND was 0.311 unique each, 0.189 synergy, 0
  redundancy. v6: "Previous versions … erroneously asserted independent
  predictors could not convey redundant information", and the analytic
  bound gives redundancy at least 0.082.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | S_max counts unique information as synergy whenever two or more predictors carry it | strong | Unq, 1 bit, and the two-unique-bits argument (§4.1); recomputed |
| C2 | WholeMinusSum is synergy minus redundancy for n = 2, and double-subtracts for n > 2 | strong | PI-diagram algebra (Fig. 8); RdnXor 0 recomputed |
| C3 | ΔI does not measure synergy: it can exceed I, falls below WMS in AND, and drops under duplication | strong | And 0.104, AndDuplicate 0.038, recomputed; the excess case is cited, not shown |
| C4 | max(0, WMS) ≤ S_VK ≤ S_max | moderate | Appendix E.2; the upper half rests on a step I could not reconstruct; holds in every example |
| C5 | I_VK satisfies GP, SR, S0, LP0 (n = 2) and strong identity | strong | Appendix C proofs, read |
| C6 | I_VK satisfies monotonicity and target monotonicity | weak | listed in §6, no proof found |
| C7 | Duplicating a predictor leaves S_VK unchanged | weak | conditional on (M) for the derived intersection, which is not proved (Appendix E.1) |
| C8 | Independent predictors can carry redundant information about a target | moderate | v6 Fig. 11: redundancy ≥ 0.082 in AND by the analytic bound; reverses v1–v2 |
| C9 | A single target state can carry redundant, unique and synergistic information at once | strong | RdnXor, RdnUnqXor (Fig. 12), by construction |

## Concepts

- **PI-diagram** — Williams and Beer's lattice drawn as nonnegative
  regions summing to I(X_1…n : Y) (§1.2).
- **Union information I_VK** — Eq. 13; I_∪ in the later literature.
- **S_VK** — whole minus union, Eq. 14.
- **S_max, WMS, ΔI** — the three prior measures (§4).
- **Strong identity (Id₁)** — I_VK(X : X_1…n) = H(X_1…n); for two
  predictors it gives the intersection I(X_1 : X_2), Harder, Salge and
  Polani's identity property.

## Connections

- **Builds on** Williams and Beer's lattice ([LIT-1172](../literature.d/LIT-1172.md)), and on Maurer and
  Wolf's intrinsic conditional information for the idea of the
  minimisation. It takes the identity property from Harder, Salge and
  Polani ([LIT-1168](../literature.d/LIT-1168.md)) as "sufficient but not necessary" for Unq.
- **Harder, Salge and Polani ([NOTE-944](NOTE-944.md)).** Their "Griffith [15]" quote
  is v1's text, accurately quoted. Their "mechanistic redundancy" is
  their own term for what v1 denied. Their [16] is this paper's v1,
  whose measure they describe as "based on intrinsic conditional
  information … similarities with an information bottleneck"; that is a
  fair description of the minimisation, though it is not a bottleneck.
  v6 concedes their point. The characterisation is fair to v1 and dated
  by v6. That reading is mine.
- **Bertschinger et al. ([NOTE-937](NOTE-937.md), [THEORY-705](../theory.d/THEORY-705.md)).** For two predictors their
  optimisation and this one are the same, so their proofs of nonnegativity
  and of the identity property cover S_VK there. My derivation.
- **Griffith et al. ([NOTE-tmpm0azr](NOTE-tmpm0azr.md)).** The common-randomness measure is
  the formal version of v1's position: zero redundancy whenever the
  sources share no deterministic structure.

## Bearing on the record

- Filed as [THEORY-tmpims74](../theory.d/THEORY-tmpims74.md).
- [THEORY-708](../theory.d/THEORY-708.md) calls mechanistic redundancy "a position". It is the
  position that won between these two papers, by the opposing author's
  own revision, and under the identity-property measures the record holds
  AND's redundancy is 0.311 bit three ways (I_min, I_red, BROJA/I_VK).
- On the gap of a redundancy for ΦID beyond two sources: I_VK is defined
  for any n and keeps strong identity, but whether the intersection it
  induces gives nonnegative atoms for n > 2 is not shown, and the paper
  says it was "blocked" there (Appendix C).
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Intuition about circuits is the only test, and the intended answers are
  stipulated (AND's is left open).
- No algorithm is given for I_VK beyond a starting point for numerical
  optimisation.
- Several properties of the derived I∩ are unproved for n > 2, among them
  local positivity and monotonicity.
- The S_max bound's proof has a step I could not follow.

## Open questions

- Do I_VK's induced atoms stay nonnegative for three predictors? Rauh et
  al.'s result on identity and local positivity bears on it
  ([LIT-tmpeurmb](../literature.d/LIT-tmpeurmb.md)).
- S_VK for AndDuplicate, which needs a three-marginal optimisation.
