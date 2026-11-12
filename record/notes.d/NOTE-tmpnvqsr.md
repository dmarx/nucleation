---
status: Skimmed
paper: LIT-tmpzbm28
title: 'Gan (2022) — Gacha Game: When Prospect Theory Meets Optimal Pricing'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read: the arXiv PDF,
    https://arxiv.org/pdf/2208.03602v3 (61 pp.), downloaded by the earlier
    med-3 reader to `dl/med-3/n-gacha/arxiv.pdf`; text re-extracted and
    quotes checked against it. - Read: title page and abstract; §1
    Introduction in full, including the literature review; the start of §2
    (environment and the buyer's CPT payoff). - Skipped: the rest of §2 (the
    sophisticated-buyer design problem and its proofs), §3 (including the
    §3.5 comparison of the optimal mechanism with real pity systems), §4
    (RDEU and private values), the naive-buyer section, §6 (applications,
    salience theory), the appendices. Outcome as the reader gave it:
    **Skimmed** (2026-11-12).
date: '2026-11-12'
summary: >-
  A seller sells one good to a buyer with cumulative prospect theory
  preferences whose value is known. Probability weighting makes the buyer
  dynamically inconsistent. If she is naive, the unique optimum is a
  stationary loot box (a constant chance of the good per paid period); if
  sophisticated, the optimum adds worst-case insurance: after enough
  failures she can buy the good outright, which resembles the "pity system"
  of gacha games. With payments restricted to be non-negative (no paying the
  buyer), profit is bounded; with negative prices allowed, as in gambling,
  it is not, which Gan offers as a theoretical line between loot boxes and
  gambling and a reason to watch resale markets.
---
<!-- inactive-ok-file: CASE-tmpmw3hc CLAIM-tmpcv1pg — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: LIT-1209 — Unavailable; cited as on the record -->

# NOTE-tmpnvqsr: Gan (2022) — Gacha Game: When Prospect Theory Meets Optimal Pricing

## Contribution

A revenue-maximization rationale for loot boxes and for pity systems that does not rely on
screening buyers of different values: randomization pays because of probability weighting alone.

## Key results

- Abstract: "If the buyer is naive, the uniquely optimal mechanism is to sell a “loot box” that
  delivers the good with some constant probability in each period." And: "if the buyer is
  sophisticated, the uniquely optimal mechanism introduces worst-case insurance".
- §1: "This mechanism, termed the ”pity system,” originated with Granblue Fantasy in 2016" (quotation
  marks as in the PDF).
- §1: "I assume that her valuation of the unit good is publicly known in most parts of this paper";
  "Focusing on this simple setting highlights that introducing randomization has nothing to do with
  screening the private types of the buyer."
- §1: "The naive buyer always believes that she will try her luck just one last time and quit
  thereafter."
- §1: "If the price can be arbitrarily negative, as it is in the gambling industry, then the seller
  can extract infinite profit"; the profit difference "suggests a theoretical distinction between
  stochastic pricing processes and gambling".

## Assumptions

One buyer, one good, known value; CPT with reverse-S probability weighting (Tversky-Kahneman
parameterization for all numerics); seller commits; one-sided payments; for the sophisticated case,
continuous-time design approximated by a discrete process.

## Concepts

Cumulative prospect theory; probability weighting; dynamic inconsistency; naive vs. sophisticated
buyer; dynamic individual rationality; loot box; pity system (worst-case insurance); one-sided
payment.

## Bearing on the record

**How far it stands in.** Partly: same object (revenue-optimal randomized sale) and the conclusion that loot boxes can be
optimal for the seller; different model (single CPT buyer, dynamic; Han et al. per their abstract:
price plus multi-item drop probabilities under a player choice model) and none of Han et al.'s
algorithmic or hardness results. It restates none of them.

- **[CASE-tmpmw3hc](../cases.d/CASE-tmpmw3hc.md)** (does a high-spending minority's weight select loot-box design?). **Qualifies
  the inference the case relies on.** Gan derives the stationary loot box and the pity system as
  revenue-optimal for a single buyer whose value is known, so a design moving toward pity
  guarantees (the case's own "guarantee at draw 90" example) can be explained by revenue
  optimization against a homogeneous behavioural buyer, with no spending tail. The case's H1/H2
  test needs a control for this: design drift toward a revenue-optimal mechanism is not by itself
  evidence that a minority selected it. Gan does not address heterogeneous spenders or "whales".
- Bears on **[CLAIM-tmpcv1pg](../claims.d/CLAIM-tmpcv1pg.md)** only through the case, and not on its escalation half.
- Duplicate check: no LIT on the branch holds arXiv 2208.03602, "gacha" or "pity system"; [LIT-1209](../literature.d/LIT-1209.md)
  is the only "prospect theory" hit and is unrelated.

## Limitations

Skimmed: the main theorems were not checked; the claim that real pity systems approximate the optimum
(§3.5) was not read. Theory only, no data. Known value and a single buyer exclude exactly the spender
heterogeneity the record's case is about.
