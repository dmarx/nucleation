---
number: 409
status: Read
formerly:
- NOTE-tmprbmx6
paper: 'LIT-501'
title: 'Five Rules for the Evolution of Cooperation'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full, main text only (Science 314: 1560–1563 from the
    University of Chicago course-page copy; text extracted with PyMuPDF).
    All sections, the figure captions, Table 1 and the references read.
    Table 1's matrices and its RD/AD columns did not survive extraction;
    the Supporting Online Material with the derivations was not read. So
    the five ESS conditions below are confirmed by the main text, and the
    RD/AD conditions are known only as "slightly more stringent" for the
    two reciprocity mechanisms and identical for the other three.
date: '2026-10-02'
summary: >-
  A four-page review. Five mechanisms, each with a b/c threshold derived
  from a 2×2 game: kin selection r > c/b, direct reciprocity w > c/b,
  indirect reciprocity q > c/b, network reciprocity b/c > k, group
  selection b/c > 1 + n/m. For kin, network and group mechanisms the
  same condition makes cooperators ESS, risk-dominant and advantageous;
  for the reciprocities RD and AD need more. Derivations are in the
  unread supplement; the review itself proves nothing.
---

<!-- inactive-ok-file: LIT-495 — Deferred, no lawful full text: Alexander 1987, filed in the same batch; named as a neighbour, its content attributed to its publisher and to Nowak -->
<!-- inactive-ok-file: LIT-503 — Proposed: Curry 2016, the statement of morality-as-cooperation filed in the same batch; cited for which sources it credits for each domain -->

# NOTE-409: Five Rules for the Evolution of Cooperation

## Contribution

A unifying presentation, not a new result. Each of five known mechanisms
is cast as a game between cooperators and defectors with a 2×2 payoff
matrix (Table 1), so that one set of criteria (ESS, risk dominance,
advantageousness) can be applied to all, and each rule comes out as "the
benefit-to-cost ratio … greater than some critical value".

## Key insight

In a well-mixed population, selection lowers mean fitness by eliminating
cooperators (Fig. 1: f_C = b(i − 1)/(N − 1) − c, f_D = bi/(N − 1)). Every
mechanism works by making cooperators interact with cooperators more than
chance would (relatives, repeat partners, those of good reputation,
neighbours, groups), and its rule says how much more is needed per unit of
b/c.

## Assumptions

- **Donation game** throughout: cooperation means paying c so another gets b (b > c), "measured in terms of fitness"; reproduction may be genetic or cultural.
- **Kin selection** by Maynard Smith's inclusive-fitness method: "your payoff multiplied by r is added to mine".
- **Direct reciprocity**: TIT FOR TAT against ALL D, expected 1/(1 − w) rounds.
- **Indirect reciprocity**: q is the probability of knowing a recipient's reputation; cooperators help unless the recipient is known to defect.
- **Network reciprocity**: a regular graph with k neighbours; a transformed replicator equation (ref. 54), with weak selection.
- **Group selection**: groups of maximum size n, m groups, splitting and extinction, "weak selection and rare group splitting".
- **AD criterion** holds "in the limit of weak selection".

## Key results

- **Rules (eqs. 1–5):** r > c/b; w > c/b; q > c/b; b/c > k; b/c > 1 + n/m.
- **Measures of success:** with matrix (a, b; g, d) for C v. C, C v. D, D v. C, D v. D: ESS if a > g; risk-dominant if a + b > g + d; advantageous if a + 2b > g + 2d (the "1/3 rule").
- **Comparison:** for kin selection, network reciprocity and group selection the rule makes cooperators *dominate* defectors, so the same condition gives ESS, RD and AD; for direct and indirect reciprocity the rule is the ESS condition and RD and AD need "slightly more stringent conditions".
- **Strategies in direct reciprocity:** TIT FOR TAT declines under errors; generous TIT FOR TAT (forgives with probability 1 − c/b), then win-stay, lose-shift, do better; TIT FOR TAT is "an efficient catalyst … where nearly everybody is a defector".
- **Outside the five:** green-beard models, voluntary participation, and punishment, which "is not a mechanism for the evolution of cooperation" since every model of it rests on indirect reciprocity, group selection or network reciprocity.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Each mechanism reduces to a b/c threshold | strong for the ESS conditions, given each model's assumptions | stated rules, derivations in refs. 19, 41, 51 and the SOM (not read) |
| C2 | Indirect reciprocity requires language and has shaped human intelligence | assertion, "presumably" | ref. 28 (Nowak & Sigmund 2005) |
| C3 | Indirect reciprocity "leads to the evolution of morality and social norms" | assertion | cites Alexander 1987 and two models of norms |
| C4 | Punishment is not a mechanism for the evolution of cooperation | moderate | a survey claim: all models of punishment so far rest on one of the five |
| C5 | Cooperation is a third fundamental principle of evolution | programmatic | closing paragraph |

## Concepts

- **Cooperator / defector** — pays c to give b / pays nothing, gives nothing.
- **Network reciprocity** — clusters of cooperators on a graph outcompete defectors; generalizes "spatial reciprocity".
- **Advantageous (AD)** — fixation probability of a single cooperator above 1/N in a finite population, under weak selection.

## Connections

- **Hamilton 1964** ([LIT-497](../literature.d/LIT-497.md)) is ref. 1 for kin selection.
- **Trivers 1971** ([LIT-510](../literature.d/LIT-510.md)) and **Axelrod & Hamilton 1981** ([LIT-498](../literature.d/LIT-498.md)) are refs. 10 and 12 for direct reciprocity; this paper's w > c/b is Axelrod & Hamilton's condition specialized to the donation game.
- **Alexander 1987** ([LIT-495](../literature.d/LIT-495.md)) is ref. 30, for morality.
- **Price equation.** The closing claim that kin-selection theory based on the Price equation can compare mechanisms bears on Luque ([LIT-205](../literature.d/LIT-205.md), [NOTE-101](NOTE-101.md)).
- **Group selection and units of selection.** Lloyd's entry ([LIT-160](../literature.d/LIT-160.md)) discusses the multilevel debate this paper's fifth rule enters.

## Bearing on the record

- **MAC kin and exchange domains:** grounded (kin selection; direct and indirect reciprocity).
- **MAC group domain:** not grounded as MAC means it. MAC's group domain is coordination to mutual advantage; this paper's network reciprocity and group selection are routes to *altruism*. Group selection does support in-group cooperation and is often cited for loyalty, but the paper says nothing about coordination or loyalty.
- **Hawk, dove, division, possession:** absent; Curry 2016 ([LIT-503](../literature.d/LIT-503.md), Table 3) makes the same observation.
- **No THEORY is indicated.** No instruction for ML practice.

## Limitations

- A review: proofs and parameter regimes are in cited papers and the supplement.
- Only the donation game, so only altruism; no mutualism, coordination or conflict.
- Several rules hold only under weak selection or special structure (regular graphs, rare splitting).

## Open questions

- Are the five mechanisms distinct, or, as the closing paragraph allows, all expressible as kin selection in a broad (Price-equation) sense?
- How do the rules combine when several mechanisms act at once?

## Corrections

- none to a seeded skim (there was no seed)
