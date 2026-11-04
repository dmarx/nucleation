---
status: Read
paper: LIT-tmpuad7h
title: 'Siemroth — Optimal budget rules against wasteful year-end spending'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read on 2026-11-04 from the February 2022 working paper, not the version
    of record. The publisher's open-access copy,
    https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/iere.12684,
    returned HTTP 403 with a Cloudflare challenge and was not retried. Read
    instead: the author's Essex Economics Discussion Paper of 7 February
    2022 in the University of Essex repository,
    https://repository.essex.ac.uk/32231/1/optimal%20budget%20rules.pdf
    (record type "Monograph (Working Paper)", with a later note
    "International Economic Review, forthcoming"), 48 pages, extracted with
    pdftotext. OpenAlex labels it acceptedVersion; its date and record point
    to the pre-publication working paper, and the published text may differ
    after revision. Read in full: the non-technical summary and §§1–6
    (introduction, literature, model, agent reaction, the principal's
    problem, Propositions 1–4 and Corollary 1, the extensions on endogenous
    budgets, probabilistic audits and the uniform-distribution assumption,
    concluding remarks). Skipped: the appendix proofs; formulas read only as
    stated in the main text. Page numbers below are the working paper's.
date: '2026-11-04'
summary: >-
  A two-year principal–agent model of year-end spending: the agent
  privately observes each year's need and gains α < 1 from spending above
  it. The principal commits to a roll-over share, audit rules and a
  punishment. Some roll-over is weakly better than none and works only if
  the share exceeds α; partial roll-over is optimal in a restricted region,
  full roll-over for most parameters. Audits are threshold rules, or an
  interval rule in year 1; punishment is maximal and never imposed;
  strategic underfunding can be optimal when audit and fund costs are high.
---
<!-- inactive-ok-file: THEORY-tmpn0uzd LIT-1389 THEORY-067 — Proposed, Unfetched or new; the account filed from this reading and the self-control entries checked and found unrelated, cited from the reading of Siemroth (2024) as open -->

# NOTE-tmpm0esa: Siemroth — Optimal budget rules against wasteful year-end spending

## Contribution

It claims the first analysis of the optimal roll-over rule for unused
funds, and of optimal audit rules and how they interact with roll-over, in
the year-end spending setting. It recasts Liebman and Mahoney's
precautionary, no-misuse model as moral hazard with costly state
verification, and finds that roll-over can do some of the work of
auditing.

## Key insight

An agent who knows the need and gains a little from spending beyond it
will spend the whole budget if the remainder is lost. Let it keep a share
of what it saves and saving competes with misuse; when the share is worth
more to it than misuse is (Δ > α), it saves, and the principal can audit
less. Taxing the roll-over (Δ < 1) can force still more saving, which is
why full roll-over is not always best.

## Assumptions

- Two years; risk-neutral principal and agent; needs θ_y i.i.d. U(0, u)
  (§5.3 argues the qualitative results survive other continuous
  distributions).
- Linear utilities. The agent: "The agent receives a high marginal value
  from fulfilling spending needs, and a lower but positive marginal value
  from spending more." (p. 4), 1 per dollar up to need and α ∈ (0,1)
  above. The principal: 1 up to need, 0 above; cost of funds λ ∈ (0,1).
- The principal commits in advance to Δ, deterministic audit rules and a
  punishment p.
- Audits are perfect, at cost c_A; punishment costs the principal p·c_p.
- a_y ≤ b; the budget b is exogenous except in §5.1.
- No within-year structure (fn. 2: an earlier version with subperiods gave
  the same decisions, misuse postponed to year's end).
- Needs are independent across years, so "This model does not exhibit a
  ratchet effect" (p. 7).

## Key results

- **Main result (abstract, p. 1).** "The optimal rules are to allow the
  agent to roll-over a share of the unused funds, but not necessarily the
  full share, in most cases to audit only sufficiently large spending, and
  to exert maximum punishment if fund misuse is detected."
- **Proposition 1, optimal roll-over (pp. 17–18).** "Consequently,
  allowing at least some roll-over of unused funds is weakly better." The
  share "must exceed α for the agent to want to roll-over any funds at all
  and stop misusing funds in year 1". Partial roll-over, Δ* ∈ (Δ_max x̄,
  1), can be optimal when α and b are small and λ large; but "for most
  parameter values allowing a full fund roll-over is optimal" (p. 2).
- **Threshold audits (Lemma 1, p. 6).** "Hence, any audit rule R is in
  outcome equivalent to a threshold rule, where the threshold is the
  largest spending amount that is not audited under R." Proposition 2:
  a₂* = min{c_A/λ, b}, or no auditing in a corner case.
- **Interaction (p. 6; Lemma 2, Proposition 4).** "Hence, the roll-over
  rule non-trivially interacts with the optimal audit rule." In year 1 an
  interval rule audits around the saver's spending b − x̄ and can leave the
  largest amounts unaudited.
- **Punishment (Lemma 3, p. 15).** A punishment p > 2αb, "so that
  punishment never occurs in equilibrium".
- **Underfunding (Proposition 5, Table 1, p. 30).** "strategically
  underfunding the agent can be optimal in many cases, especially if the
  costs of funds and auditing are large".
- **Not precaution (p. 19).** "This is not a precautionary savings motive,
  as the agent is risk neutral"; saving comes from comparing expected
  values.
- **Advice (p. 2).** "Principals should therefore publicly commit to not
  cut budgets if funds are returned or saved."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Some roll-over is weakly better than none | strong, within the model | Proposition 1 |
| C2 | Roll-over induces saving only if the share exceeds the agent's marginal gain from misuse | strong, within the model | Proposition 1, p. 18 |
| C3 | Partial roll-over can be strictly optimal | moderate: restricted parameter region | Proposition 1 |
| C4 | Optimal audits are threshold rules, except an interval rule in year 1 | strong, within the model | Lemmas 1–2, Propositions 2 and 4 |
| C5 | Strategic underfunding can be optimal | weak to moderate: a 12-point numerical grid | Proposition 5, Table 1 |

## Concepts

- **Spending need θ_y**: the spending the principal wants, privately known
  to the agent.
- **Fund misuse**: s_y > θ_y, spending above need; it covers the
  low-value-item, durable-hoarding and personal-perk readings of year-end
  spending.
- **Roll-over rule Δ**: the share of unused funds carried over; 1 − Δ is
  returned.
- **x̄**: what the agent saves absent auditing.
- **Threshold audit rule**: audit if and only if s > a_y. **Interval audit
  rule**: audit s ∈ (a₁, ā₁).
- **Strategic underfunding**: a budget b < u, below the largest possible
  need.

## Connections

It builds on Liebman and Mahoney ([LIT-tmp4kmcg](../literature.d/LIT-tmp4kmcg.md)), keeping their year-end
problem and their commitment point but replacing shared preferences and
precautionary saving with misuse under private information and risk
neutrality; their mechanism is explicitly not this one (p. 19). It draws on
the costly-state-verification literature (Townsend; Border and Sobel) for
the audit rules, and contrasts itself with the ratchet-effect literature.

## Bearing on the record

- **The pasted bibliography's description.** A says: "A formal two-period
  principal–agent model of rollover, private spending needs, misuse, and
  auditing ... the model does not conclude that unlimited rollover is
  always optimal." The quotation marks are A's; the sentence is not in the
  paper, and is A's paraphrase. The model description is accurate and so
  is the second clause, but it hides the headline: some roll-over is always
  weakly better than none, and full roll-over is optimal for most
  parameters; the case for partial roll-over is a restricted one.
  The word unlimited is A's: the paper's Δ is a share, not a cap. A also
  leaves out the audit structure, the maximal punishment, roll-over as a
  substitute for auditing, and underfunding.
- **[TERM-055](../terms.d/TERM-055.md) (operational availability).** Qualifies the term's reach,
  weakly. Roll-over keeps funds available for a later need, and
  underfunding knowingly lowers the chance a need can be met; but the model
  has no cue, no deployment step and no task deadline. An analogy.
- **[CLAIM-347](../claims.d/CLAIM-347.md) (the frustration complex).** Unrelated, though superficially
  close: the conflict is a misalignment over spending above need, not joint
  infeasibility of declared demands.
- **[CLAIM-079](../claims.d/CLAIM-079.md), [CLAIM-517](../claims.d/CLAIM-517.md), [QUESTION-132](../questions.d/QUESTION-132.md), [CLAIM-357](../claims.d/CLAIM-357.md) and [CLAIM-365](../claims.d/CLAIM-365.md).**
  Unrelated. A's gloss of [QUESTION-132](../questions.d/QUESTION-132.md) is wrong.
- **The self-control and precommitment cluster** ([LIT-1389](../literature.d/LIT-1389.md), [THEORY-067](../theory.d/THEORY-067.md),
  [CASE-128](../cases.d/CASE-128.md)). Unrelated in structure: there the commitment binds one's own
  later choice; here a principal commits toward an agent.
- Filed: [THEORY-tmpn0uzd](../theory.d/THEORY-tmpn0uzd.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- Two periods only; the author asks: "How does the optimal roll-over rule
  change in an infinite horizon setting where large savings might
  accumulate?" (p. 33).
- No bound on punishment; deterministic audits only (probabilistic audits
  discussed informally); no ratchet effect; uniform needs for the closed
  forms.
- Partial roll-over is shown optimal only in restricted parameter regions,
  and underfunding numerically on a 12-point grid.
- The author leaves undesirable spending undefined: "this paper does not
  take a strong stance on what is undesirable spending, but investigates
  how to minimize it once it is properly defined" (p. 33).
- No empirical test.
- Read from the 2022 working paper, not the version of record.
