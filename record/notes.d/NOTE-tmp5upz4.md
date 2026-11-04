---
status: Read
paper: 'LIT-tmpsj5c6'
title: 'Ratliff, Dong, Sekar and Fiez — A perspective on incentive design'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read on 2026-11-04 from the authors' manuscript on co-author Shreyas
    Sekar's own site
    (https://sekarshre.github.io/publication/survey-incentivedesign/survey-incentivedesign.pdf),
    after Ratliff's University of Washington copy returned HTTP 403
    ("Request forbidden by administrative rules"), not retried. It is a
    37-page manuscript in the Annual Reviews template, with a placeholder
    citation line and a TeX date of 2019-01-08, not the typeset version, so
    page numbers below are the manuscript's 1–37, not the journal's
    305–338. Text extracted by pdftotext. Read in full: §§1–5 (pp. 1–30),
    with Examples 1–4 and the footnotes. Scanned only: the list of 153
    references, looked through for particular names (it cites no ratchet
    paper and not Freixas, Guesnerie and Tirole).
date: '2026-11-04'
summary: >-
  A perspective, not a results paper. Incentive design is set on one
  principal–agent template and reviewed in economics (static, model-based
  screening and moral-hazard contracts), control theory (reverse
  Stackelberg games with dynamics and adaptive estimation) and online
  learning (regret bounds under i.i.d. or stationary agents). Each handles
  part of the problem; designing incentives for returning agents whose
  behaviour evolves with the principal's own actions is named open, with
  bounded rationality, information design, fairness, competing principals
  and counterfactual evaluation as further directions.
---
<!-- inactive-ok-file: THEORY-tmp30jgj THEORY-853 LIT-tmpfzy5q NOTE-tmpoec9n — Proposed, Unfetched or Skimmed, or new; cited from the reading of Ratliff et al. (2019) as open -->

# NOTE-tmp5upz4: Ratliff, Dong, Sekar and Fiez — A perspective on incentive design

## Contribution

The paper maps three literatures onto one principal–agent template and
names their joint open problem: incentive design with agents who return,
whose behaviour changes in response to the principal's own past actions,
under hidden types or hidden actions, budget or market constraints and
physical dynamics. Its framing is "three core communities—economics,
control theory, machine learning" (abstract, p. 1). It proves no theorems.

## Key insight

Each community drops a different part of the problem. Economics has the
strategic agent but is static and needs a strong prior; control has the
dynamics but assumes known structure and gives asymptotic results; online
learning needs little prior knowledge but assumes the agents do not change
because of what the principal does. Non-stationarity that the principal
causes is the gap between them.

## Assumptions

- **The template (§2.1).** Two roles, principal and agent (possibly several
  of each). The principal moves first, announcing γ: U → V from agent
  actions or signals to its own actions; the agent best-responds,
  u*(γ) ∈ argmax J_A(u, γ(u)).
- **In the economics reviewed**: rational expected-utility agents, a known
  prior over types, single-crossing.
- **In the control reviewed**: known or parameterized dynamics and noise,
  often linear-quadratic.
- **In the online learning reviewed**: finite action sets, i.i.d. or
  adversarial nature, regret against the best fixed action.

## Key results

Claims of a review, not theorems. Pages are the manuscript's.

- **Economics is static (§1.1, p. 4).** "approaches from this domain
  largely focus on designing incentives in static environments", and they
  "are very heavily model-based."
- **Adverse selection and moral hazard (§3.1, p. 10).** "adverse selection
  arises when the preferences of the agent are not known to the principal";
  moral hazard when the principal "is unable to observe the action u ∈ U
  chosen by the agent".
- **Gaming a baseline (§3.1, Example 1, p. 10).** "an energy consumer may
  artificially inflate their baseline just prior to a demand response
  program event in order to receive larger payouts under the program."
- **The control framing (§3.2, pp. 14, 17).** "the principle is the
  controller and the agent is the plant" (sic); the reverse-Stackelberg
  structure "lead to defining the term incentive controllability".
- **Control's adaptive results (§3.2.2, p. 18).** "Under the assumptions of
  zero-mean, finite-variance, i.i.d. noise and stable and persistently
  exciting dynamics—the latter of which is very difficult to verify—such
  results can be obtained."
- **Online learning (§1.1, p. 5).** Its guarantees "come in the form of
  regret bounds or worst-case competitive ratios", under i.i.d. and
  stationary assumptions, "both of which are far removed from reality."
- **A ratchet-like agent (§3.3.2, p. 23).** "an agent who interacts with
  the principal for multiple rounds may seek to benefit by resorting to low
  effort levels if it can influence the payment mechanism offered in
  subsequent rounds."
- **The central open problem (§4, p. 24).** "it is still an open problem to
  solve incentive design with repeatedly returning agents whose
  decision-making processes evolve with time", those processes being
  functions of the principal's actions.
- **Uncertainty can help (§4.2, p. 25).** "Surprisingly, in a number of
  settings, uncertainty does help in the design of more effective
  incentives", with Braess-type routing as the example.
- **Counterfactual evaluation (§4.6, p. 30).** "the design of incentives
  for multi-agent systems with self-interested users whose behavior may
  evolve with time remains uncharted territory."

## Concepts

- **Incentive design**: "the design of mechanisms for shaping the behavior
  of autonomous agents" (§1, p. 4).
- **Incentive mapping** γ ∈ Γ = {γ : U → V}, sought so that the desired
  agent action maximizes J_A(u, γ(u)) and "γ realigns the preferences of
  the agent with those of the principal" (§2.1, p. 7).
- **Incentive compatibility and individual rationality**: truthful choice
  of one's own contract, and participation against an outside option
  (eqs. 1–2, §3.1).
- **Reverse Stackelberg game; incentive controllability** (§3.2).
- **Regret** R_T against the best fixed action in hindsight (eq. 3, §3.3).

## Connections

It draws on the screening and moral-hazard textbook literature for
economics, on Ho, Luh and Olsder's reverse-Stackelberg work and adaptive
control for the control strand, and on bandits and online learning for the
third. Of the dynamic-contracting literature with limited commitment it
cites nothing, although its §3.3.2 remark is that literature's central
phenomenon: the ratchet effect of Freixas, Guesnerie and Tirole
(LIT-tmpfzy5q, unread), restated for long relationships by Gerardi and
Maestri (LIT-tmpbit9m, NOTE-tmpoec9n).

## Bearing on the record

- **The pasted bibliography's gloss.** A writes, in quotation marks, that
  it "links principal–agent problems, dynamic systems, and online
  learning". That string is not in the paper: it is A's paraphrase, fair to
  the paper's three-community framing. "Links" overstates it, since the
  paper reviews the three side by side and calls for joining them; it does
  not supply a joint framework. Where A places it, under budgeting,
  ratchets and incentives, it can serve only as a pointer to the dynamic
  and learning version of the problem: it never uses the words ratchet,
  budgeting or year-end, its "budget" is the principal's incentive budget
  in online learning, and it has nothing on slack, readiness or rarely
  exercised capability.
- **CLAIM-357 and CLAIM-365 (governance regret).** Qualifies. Both concern
  a governor choosing updates for constituents with several demands. The
  claims' regret is the minimax suboptimality of an actual update; this
  paper's (eq. 3) is the online-learning regret of a principal's sequence
  of incentives. Same word, different objects, to be kept apart if cited
  together.
- **CLAIM-347 (frustration as an ordinal complex).** Qualifies, loosely.
  Incentive design repairs a two-party misalignment by changing the agent's
  payoff, not by enlarging what can jointly be satisfied, which is a
  different repair from the claim's relief.
- **CLAIM-535 (a policy acceptable in every circumstance).** Qualifies: it
  is the observation-limited design problem without strategic agents, a
  baseline for the moral-hazard case, where the principal cannot observe
  the action.
- **LIT-1336 (performative prediction, NOTE-1044)** sharpens the central
  open problem: a deployed rule that shifts the distribution it faces is
  the paper's principal-caused non-stationarity without explicit agent
  utilities.
- **LIT-1313 and LIT-1021 (information design, Bayesian persuasion)** are
  the theory behind §4.2; THEORY-853, that more information shrinks what a
  designer can induce, qualifies its "uncertainty does help".
- **LIT-1528 and LIT-1524 (partial monitoring)** generalize the feedback
  classification of §3.3; **LIT-1518 (peer prediction)** fits its
  crowdsourcing and truthful-elicitation thread; **LIT-1326 (algorithmic
  monoculture)** qualifies §4.4 on competing principals; **LIT-1330
  (rankings and reactivity)** is the sociological account of measured
  parties reacting to the measure, as in the baseline example; **LIT-1880
  (information before commitment in safe adaptive control)** is the
  control-side adaptive design of §3.2.2, without strategic agents.
- **TERM-055, CLAIM-079, CLAIM-517, QUESTION-132**: unrelated. QUESTION-132
  asks when equivalent adaptive operators differentiate into specialists
  with positive growth when rare, not, as A glosses it, about capabilities
  whose contribution shows in rare contexts.
- Filed: THEORY-tmp30jgj. One strand is online learning, but the paper's
  subject is incentive design for human-in-the-loop systems, not an
  instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The authors'.** "The works in these fields are too numerous to cover
  all of them in this short perspective" (p. 8); the behavioural models
  proposed are "rather simplistic" in their present validation (§4.1,
  p. 25); robust incentives "tend to result in very conservative
  strategies" (p. 25).
- **A perspective.** No new theorems, no empirical tests; the examples are
  illustrative.
- **A gap in the economics review.** Textbook-level, and silent on dynamic
  contracting with limited commitment (the ratchet effect, renegotiation),
  though §3.3.2 raises its central phenomenon.
- **A manuscript.** An unresolved citation in §4.2 and "principle" for
  "principal"; the journal text may differ.
