---
number: 837
status: Active
formerly:
- THEORY-tmp6l5uw
title: 'In Besley and Prat''s model of an incumbent who can pay n identical outlets to suppress verifiable bad news, where one outlet''s report informs every voter, each outlet''s price for silence is what it would earn as the only one to break the story, so the media are captured exactly when n·τa < r; under capture voters, though fully rational and not deceived, learn nothing and never remove a bad incumbent'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-1031. The condition is the working paper's
    Proposition 1 and its appendix proof; it is re-derived below step by
    step, which meets the condition for Active under ADR-047 v2. The
    observation that capture works without deception, and the contrast
    with persuasion, are the record's.
tags:
- society-and-governance
- game-theory
- social-science
date: '2026-10-21'
source:
- LIT-1333
summary: >-
  Besley and Prat (2006; read in the 2005 LSE working paper),
  [LIT-1333](../literature.d/LIT-1333.md), read in [NOTE-1031](../notes.d/NOTE-1031.md). Plurality protects because news is
  non-rival: silencing the press means silencing every outlet, each at its
  monopoly price. A static, hard-news model. It says nothing about soft
  news, partial bribing, or capture that feeds back on the market that
  permits it, and its cross-country evidence is a raw comparison of means.
supports:
- CLAIM-404
---

# THEORY-837: In Besley and Prat's model of an incumbent who can pay n identical outlets to suppress verifiable bad news, where one outlet's report informs every voter, each outlet's price for silence is what it would earn as the only one to break the story, so the media are captured exactly when n·τa < r; under capture voters, though fully rational and not deceived, learn nothing and never remove a bad incumbent

## Source

Besley and Prat, "Handcuffs for the Grabbing Hand? Media Capture and
Government Accountability", *American Economic Review* 96(3) (2006),
[LIT-1333](../literature.d/LIT-1333.md), read in full in [NOTE-1031](../notes.d/NOTE-1031.md) from the LSE working paper
of 2005 (PEPP/7). The result is its Proposition 1, proved in its appendix.
The derivation below is the record's.

## What was actually shown

**Setup.** The incumbent is good with probability γ, else bad. If she is
bad, all n outlets receive the same verifiable signal s = b with
probability q > 0; otherwise they see s = ∅. Only verifiable news can be
printed. An outlet reporting news earns a/m when m outlets report it. The
incumbent sees the signal and makes private offers tᵢ ≥ 0, each costing her
tᵢ and worth tᵢ/τ to the outlet. She receives r from re-election, minus
what she paid. If any outlet reports s = b, every voter learns it.

**Step 1, voting.** After s = b the posterior is 0 < γ, so voters replace
her (strictly dominant). Suppose voters also replaced her after s = ∅.
Then a bad incumbent gains nothing by paying, no one is paid, the media
report truthfully, and
Pr(good | ∅) = γ / (γ + (1 − γ)(1 − q)) > γ,
so voters should keep her after ∅, a contradiction. In every pure-strategy
equilibrium she is re-elected iff no outlet reports.

**Step 2, all or none.** Since one report informs every voter, paying
fewer than all informed outlets buys nothing. She pays all n or none.

**Step 3, the price.** Take a profile in which all n are silenced. An
outlet that rejects its offer becomes the only one reporting, m = 1, and
earns a. It therefore accepts iff tᵢ/τ ≥ a, so the cheapest offer that
works is tᵢ = τa, and not τa/n. Conversely no outlet can earn more than a,
so any offer worth at least a is accepted.

**Step 4, the condition.** Silencing costs nτa and gains r. The bad
incumbent buys silence iff nτa < r, that is n < r/(τa), and is indifferent
at equality.

**Consequences.** Under capture s = ∅ always, so Pr(good | ∅) = γ: the
voters' posterior equals the challenger's prior, they are indifferent, and
by Step 1 they keep the incumbent. Turnover is 0 and expected voter utility
is γ in each period. Without capture a bad incumbent is caught with
probability q, turnover is q(1 − γ), second-period utility is
γ + q(1 − γ)γ, and audience revenue is qa rather than 0.

What could have failed: the price could have been the outlet's share,
a/n, as a reimbursement of lost revenue would suggest. Then the total cost
would be a, independent of n, and plurality would not protect. It fails
because the deviation payoff of a lone reporter is a.

## What this does not say

- **Not that voters are fooled.** Under capture the voters' inference is
  correct: silence is uninformative and they know it. The incumbent wins
  because the tie goes to her, not because anyone believes something false.
  This is the record's gloss, and it is what separates the model from
  Bayesian persuasion ([THEORY-404](THEORY-404.md)), where a receiver who knows the design
  is moved.
- **Not about soft news or partial capture.** With unverifiable news, or
  readers who see one outlet only, buying some outlets can pay. The
  paper's segmented-audience extension needs to silence only enough
  outlets to keep half the voters uninformed, and the plurality result
  then holds cleanly only when at least half the viewers switch outlets.
- **Not dynamic.** Capture is a one-shot comparison. Nothing in the model
  lets capture change n, a, τ or r later, so it has no
  interpretation–authority loop.
- **Not an empirical finding.** The paper's Table 1 compares means across
  88 countries and is called "crude" and non-causal by its authors.
- **Not the published text.** The working paper was read. Its appendix
  writes the acceptance threshold once as a, not τa, a slip that does not
  affect the conclusion.

## Connections

- **[THEORY-851](THEORY-851.md) and [THEORY-850](THEORY-850.md).** The two empirical readings of
  this batch take the model as their frame. Di Tella and Franceschelli's
  transfers are advertising, and Szeidl and Szucs's δ, the government's
  ability to reward slant, plays the part of τ.
- **[THEORY-404](THEORY-404.md).** Two ways to govern a rational evaluator through its
  evidence: commit to a signal that moves it, or remove the signal and
  leave it at its prior.
