---
status: Read
paper: LIT-tmporx78
title: 'Davoudabadi, Makui and Rasouli — Introducing a predictive-oriented multi-stakeholder recommender system model'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read: Europe PMC REST full-text
    JATS XML of PMC13230954 (publisher version, gold OA),
    `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13230954/fullTextXML`,
    fetched 2026-11-12. - Read: abstract, Introduction, Related work,
    Preliminaries (peak-end rule, prospect theory), Proposed methodology
    (user-side steps 1–4, organization-side steps 1–3, aggregation),
    complexity analysis, simulation, comparative analysis, conclusion.
    Skipped / not legible: equation bodies (Eqs 1–10 came through as
    MathML/TeX placeholders), full Table 2–4 contents, figures; references.
    Outcome as the reader gave it: **Read** (full text; equations not
    rendered in the text extraction, so the formulas were read from their
    surrounding prose only; tables partly garbled).
date: '2026-11-12'
summary: >-
  The authors propose a recommender that scores each candidate item for a
  user by combining (a) a user-side score and (b) an organization-side
  score. User side: a reference point built from the user's peak and most
  recent purchase utilities (peak-end rule), item distances to it split into
  gains and losses with a prospect-theory-style value function (the EXPTODIM
  method), and a "user flexibility" index from the diversity of the user's
  past purchases. Organization side: "organizational expectations" (target
  values on operational features such as workshop capacity), the similarity
  between the organization's projected state after an item is chosen and
  that target, and an "organizational flexibility" index from the Euclidean
  gap between current and ideal state. A weight adjustment function, bounded
  so neither side is ignored, gives more weight to the organization the more
  flexible the user is, and more to the user the more flexible the
  organization is. Evaluated by simulation only: a hypothetical manufacturer
  with 30 products (4 attributes), 3 workshops with capacity limits, and 100
  synthetic users; compared with a "customer-driven" strategy, it reduces
  over- and under-use of workshop capacity, reported as a 17.6% average
  improvement in capacity utilization.
---
<!-- inactive-ok-file: CLAIM-tmpcv1pg CLAIM-tmpifp69 — Proposed; filed from the same exchange -->

# NOTE-tmp64zjh: Davoudabadi, Makui and Rasouli — Introducing a predictive-oriented multi-stakeholder recommender system model

## Contribution

A scoring scheme in which an organization's operational state, and both parties' "flexibility", set the trade-off between user preference and organizational need, intended to steer demand toward items the organization can supply.

## Key results

1. Abstract: "A weight adjustment function balances user and organizational influence based on these indices."
2. Abstract: "higher user flexibility increases organizational preference weights, and higher organizational flexibility increases user weights."
3. Methodology, aggregation: "even if a user possesses the highest level of flexibility among all users, their preferences should not be entirely disregarded."
4. User flexibility: "the more diverse their purchase history, the greater their capacity to accept and adapt to new recommendations."
5. Comparative analysis: under the customer-driven strategy Workshops 1 and 2 need expansions of "approximately 54.5% and 36.9%"; Workshop 3 is 34.8% idle. Under the proposed model, 18.7%, 17.1% and 18.8%.
6. Comparative analysis: "the proposed RS model achieves an average increase of 17.6% in organizational capacity utilization".
7. Introduction: conventional systems perform "what can be described as “Post-Dict” rather than forecasting future ratings."

## Assumptions

- Users' evaluations are reference-dependent, with the reference point a weighted mix of peak and end experiences; loss aversion as in prospect theory.
- Diversity of past purchases measures willingness to accept steering ("flexibility").
- Organizational expectations can be stated as target values on features; deviations are non-compensatory and penalized by Euclidean distance.
- Simulated users accept recommendations, so recommended items translate into workshop load (no user response model is estimated).

## Concepts

Multi-stakeholder recommendation (consumers, providers, system/organization); demand shaping via recommendations under supply-chain constraints ("nudge" to shift inventory); peak-end rule; prospect theory, reference point, gain/loss domains; user and organizational flexibility as "leading indicators"; weight adjustment with lower and upper bounds; capacity leveling.

## Bearing on the record

**On the LIT's and the exchange's characterization.** A's account ("a model in which users' changing expectations and organizations' operational requirements both enter recommender design") is **accurate but generous**. What the paper does is weigh two scores by flexibility indices and test it on synthetic data only. Its evaluation measures only the organization's side (capacity use); user satisfaction under the steered recommendations is not measured or simulated, so "neither stakeholder is ignored" is a design constraint (bounded weights), not a demonstrated outcome. The headline 17.6% is not derived in the text I could read: the per-workshop gains given (35.8, 19.8 and 16 points) average about 23.9, so the filer should not repeat 17.6% without the caveat that its computation is not shown.

- **CLAIM-347** (frustration among an organization's demands is ordinal; relief is strict enlargement of the jointly-satisfiable complex for the same declared demands; dropping or suppressing a demand is not relief): **leaves open; serves at most as a contrast case.** The model resolves user–organization conflict by a weighted sum whose weights are set by "flexibility", i.e. by discounting whichever party can bend. In CLAIM-347's terms that is suppression by weighting, not relief: the set of jointly satisfiable demands is not enlarged, the user's demand is down-weighted when the user is judged flexible. The paper offers no ordinal or complex-based account, and it does not measure whether the steered user is satisfied. It is an example of the practice the claim distinguishes from relief, not evidence for or against the claim.
- **CLAIM-351** (found on recheck: a zero aggregate gradient does not show the aggregated demands are reconciled): bears in the same way: a single combined score that ranks items cannot show that user and organization are reconciled rather than traded.
- **CLAIM-tmpifp69 / CLAIM-tmpcv1pg** (found on recheck: demand-weighted selection in content industries): only loosely; this is a recommender that openly lets supply-side state steer what users are offered, a benign manufacturing-capacity version of the steering those claims are about.
- **LIT-tmpfkveo** (found on recheck: "De-centering the (Traditional) user: Multistakeholder evaluation of recommender systems", Deferred): a held work on the same multi-stakeholder topic; it would be the better general reference.

Searched record/ (batch ref) for the DOI, "multi-stakeholder/multistakeholder", "peak-end", "prospect theory", "scalariz/weighted sum". Not held under another LIT. Related: LIT-tmpfkveo (Deferred), LIT-1448 (Kahneman et al., experienced utility, Active; the peak-end source), QUESTION-266, CLAIM-351, CLAIM-357.

## Limitations

Simulation only, with one hypothetical manufacturer, 30 items, 3 workshops, 100 synthetic users; no real data, no user-response model, no user-side outcome; no comparison with existing multi-stakeholder recommenders (only with a purely customer-driven baseline); the reported average improvement is not reconstructed in the text; equations not legible in the extraction I read.
