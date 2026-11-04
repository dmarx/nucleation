---
status: Skimmed
paper: LIT-tmpsiib1
title: 'Bogetoft and Hougaard — Rational inefficiencies'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in part on 2026-11-04, as a stand-in for the unread Bogetoft and
    Kerstens (2022), LIT-tmpk02sl, at the owner's request. Copy: Unit of
    Economics Working Papers 2001/14, Food and Resource Economic Institute,
    Royal Veterinary and Agricultural University (KVL), dated September
    2001, revised July 2002, 34 pages, from the series' deposit in AgEcon
    Search, https://ageconsearch.umn.edu/record/24191/files/ew010014.pdf;
    extracted with pdftotext, whose output renders the ligatures ffi, ff and
    fi as the glyphs ±, ® and ¯. Quotes below restore the ligatures; they
    were string-matched after mapping those glyphs back. Read: §1
    Introduction, §2 The Model, §3 planning regimes, §4 the price-based
    regime, §5 the restriction-based regime, §6 on revealed slack trade-offs
    to Proposition 3 and the start of the parameterized aggregators, and §8
    Final Remarks. Skimmed: the rest of §6 (weighted fairness, fair gains and
    Nash aggregators, Corollary 2). Skipped: §7 Applications (planning,
    incentives, productivity measures). The journal version (J. Productivity
    Analysis 20(3), 2003) was not read. Page numbers below are PDF pages.
date: '2026-11-04'
summary: >-
  Measured technical inefficiency, slack, is read as a rational choice: an
  organization valuing off-the-job profit and on-the-job slack uses an
  allocatively efficient underlying plan under price-based control and a
  technically efficient one under restriction-based control, and takes the
  rest as profit and slack. Observed inputs then reveal, partially, how it
  trades profit against slack and one kind of slack against another. Since
  the gains from slack are unknown, inefficiency cannot be concluded to be
  waste; the line between valuable and non-valuable slack is left open.
---
<!-- inactive-ok-file: LIT-tmpk02sl THEORY-tmpj2rdc CLAIM-089 LIT-1324 — Unfetched, Unavailable, Proposed, Rejected or new; the unread paper this reading stands in for, the account filed from it, and a rejected claim it bears on weakly, cited from the reading of Bogetoft and Hougaard (2002) as open -->

# NOTE-tmpb2xb9: Bogetoft and Hougaard — Rational inefficiencies

## Contribution

It brings revealed-preference reasoning in the tradition of Afriat and
Varian into DEA-style productivity analysis. Inefficiency becomes an object
of choice to be explained, following Stigler against Leibenstein's
X-inefficiency, and its composition across inputs becomes partly inferable
from data.

## Key insight

What a productivity analyst measures as excess inputs may be what the
organization wants: slack it values on the job, traded against profit off
it. If so, efficiency targets have costs as well as gains, and observed
input use carries information about the organization's own valuation of
its slack: "So the general idea of the rational choice perspective
advocated here is that there are gains from inefficiency and therefore
costs of improving efficiency." (p. 5).

## Assumptions

- The input requirement set L is non-empty, closed, freely disposable and,
  for exposition, convex.
- The value function U(π, s) is strictly increasing in profit π and slack s;
  for the analysis π and s are preferentially independent, U = V(π, g(s)).
- The unit (DMU) optimizes rationally within a given control regime; in the
  restriction-based regime the acceptable set A is compact and convex.
- Observed slack may proxy for omitted outputs or values; misspecification
  is accepted, not denied.

## Key results

- **Slack as choice (p. 3).** "we see inefficiency and in particular the
  allocation of inefficiency (slack) among different inputs as the result
  of a rational choice made by that firm"; and "There are many possible
  rationales for slack."
- **Organizational slack (p. 4).** After Cyert and March, "organizational
  slack can be interpreted as the existence of excess resources to produce
  a given output (technical inefficiency)", discussed in the literature as
  a buffer for uncertainty, a means of decoupling activities and a source
  of resources for innovation.
- **Not concluded to be waste (p. 5).** "Since we typically are ignorant
  about those gains and costs, we can not conclude that inefficiency as
  such should be eliminated."
- **The split posed, not solved (p. 5).** "The distinction between
  valuable and non-valuable waste is a challenging one."
- **Proposition 1 and Corollary 1 (§4, p. 14).** Under a price-based regime
  (budget b, prices w) the DMU chooses an allocatively efficient underlying
  plan and takes the rest of the budget as profit and slack.
- **Observation and Proposition 2 (§5, p. 17).** Under a restriction-based
  regime the underlying plan is technically efficient, z ∈ F(L), and, with A
  convex, supported by endogenous prices.
- **Proposition 3 (§6).** Observed choices constrain U: there is an s* in
  the observed slack set S* with U(π, s*) ≥ U(π, s) for all s in the
  possibility set S. Sharper identification needs parameterized
  aggregators (skimmed).

## Concepts

- **Slack**: s = x − z, actual inputs minus an underlying production plan
  that weakly dominates them.
- **Slack possibility set**: S(x) = {x − z : z ∈ L, z ≤ x}.
- **Price-based regime**: the unit gets a budget at given input prices.
  **Restriction-based regime**: the unit must keep inputs in an acceptable
  set A.
- **Allocatively efficient underlying plan**: X_a = argmin over L of w·x;
  units in X_a + R^p_+ are potentially allocatively efficient.

## Connections

It follows Stigler (1976) against Leibenstein's X-inefficiency, Cyert and
March (1963) on organizational slack, and Afriat and Varian on revealed
preference; DEA (Charnes, Cooper and Rhodes) supplies the technology.

**As a stand-in for Bogetoft and Kerstens (2022), LIT-tmpk02sl.** It
restates that paper's premise, as its abstract gives it: slack can be
useful, rationally chosen and of value to the organization, with the
organizational motives the abstract also lists (buffer, decoupling,
innovation). It does not restate that paper's results: the Pareto criterion
that spending is wasteful when the same outputs and slack could be had at
lower cost, the measure of how much of total spending is rationalizable,
and the bootstrap estimation and test of slack's usefulness. Here the
useful–wasteful line is explicitly left open, and the authors say drawing
it "probably requires a deeper analysis of the nature of the slack"
(p. 5). It gives the 2022 paper's ancestry, not its findings.

## Bearing on the record

- **The pasted bibliography's description of Bogetoft and Kerstens.** A
  says that paper "explicitly distinguishes useful slack from wasteful
  slack through an optimization framework." The quotation marks are A's;
  the sentence is in neither the 2022 abstract nor this paper, and is A's
  paraphrase. This lineage is consistent with it, slack being a rational
  choice over a production technology, but cannot confirm how the 2022
  paper draws the line.
- **CLAIM-482 (an organization's revealed preference is fitted to one
  regime of authority and does not predict a change of regime).**
  Qualifies. Bogetoft and Hougaard fit a single slack value function U(π,
  s) and use it across control regimes; in §1 they propose using the
  analysis "to predict more precisely the results of changes in the
  control instruments". That assumes the regime-invariant preference
  CLAIM-482 denies for aggregate organizational preference. The paper
  offers no evidence on the point either way; it is an assumption, not a
  finding.
- **CLAIM-089 (Rejected: the governing relations are revealed preferences
  of the organization).** A related revealed-preference reading of an
  organization. Qualifies, weakly; nothing here bears on why it was
  rejected.
- **TERM-055 (operational availability).** Unrelated: slack here is valued
  as held, not deployed for a task.
- **CLAIM-347 and the other codes the bibliography cites.** Unrelated: the
  trade-off between kinds of slack is a value aggregation, not joint
  infeasibility of demands.
- **LIT-1324** (Stigler, The Theory of Economic Regulation) is a different
  Stigler work.
- Filed: THEORY-tmpj2rdc. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- A stylized view of the organization, with one aggregate value function
  whose owner (shareholders or employees) is left open.
- Convexity is needed for key results; identification is only partial
  without parametric aggregators.
- No empirical application in this version; estimation on data is future
  work.
- The useful–wasteful distinction is posed, not solved.
- Read in part: §7 and most of §6's aggregators not read; the 2003 journal
  version not read.
