---
number: 724
formerly:
- CLAIM-tmpbqunx
status: Proposed
title: 'Against a challenged party who can act on the means of correction, correctability is a robust quantity, the chance that a corrective policy reaches its objective against every strategy in a declared class of opposition, and it depends on who moves first, since a corrector that must commit before seeing the opposition can do strictly worse than one that responds to it; judged against the opposition the procedural rules permit, failure shows the institution inadequate, and failure owed to opposition outside them shows a wrong by the opponent as well'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  An argument that the class of opposition an institution must withstand
  cannot be split into permitted and merely available strategies, so that
  failure against the first cannot be told from failure against the
  second; or a showing that for corrective problems of this kind the
  committed and responsive values always coincide, so that the order of
  choice never matters. Not defeated by a case in which an institution
  fails against permitted opposition and the opponent also acts wrongly,
  which the claim allows.
tags:
- game-theory
- society-and-governance
- operations-research
date: '2026-11-17'
line:
- realizability
- dependence-and-domination
uses:
- TERM-085
complements:
- CLAIM-537
- CLAIM-568
- CLAIM-748
bears_on:
- QUESTION-479
summary: >-
  A's, first stated A76 VIII.4 of the exchange "Assess Depp Heard Abuse"
  (2026-11-16) as "Adversarially robust correctability", refined A81 §3
  (2026-11-17) with claimant–institution policies and the split
  Σ_permitted ⊆ Σ_physically available; A90 IX restates it. [TERM-085](../terms.d/TERM-085.md)'s
  correctability has no opponent. The robust quantity is the adversarial
  form, and its quantifier order is the one [CLAIM-537](CLAIM-537.md) found for
  disturbances. The permitted/available split separates an institution's
  inadequacy from an opponent's wrong: "This prevents us from defining
  wrongdoing solely through successful foreclosure." It came out of the
  siege discussion, the owner's U28 (CLAIM-748). The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-748 — filed from the same exchange, Proposed or new -->

# CLAIM-724: Against a challenged party who can act on the means of correction, correctability is a robust quantity, the chance that a corrective policy reaches its objective against every strategy in a declared class of opposition, and it depends on who moves first, since a corrector that must commit before seeing the opposition can do strictly worse than one that responds to it; judged against the opposition the procedural rules permit, failure shows the institution inadequate, and failure owed to opposition outside them shows a wrong by the opponent as well

## The claim

A76 VIII.4 of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b): "The
actor whose conduct is being challenged may itself influence the
resources, timing, evidence, or pathways available for correction." For a
corrective objective J, policies π of the corrector and admissible
strategies σ of the opponent,

    α̲_J = sup_{π ∈ Π_corr} inf_{σ ∈ Σ_opp} Pr^{π,σ}(T_J ≤ H).

"This is a robust-capability quantity, not automatically a game
equilibrium." If the corrector sees the opponent's choice first, the value
is inf_σ sup_π instead. "These need not agree. Information and timing are
themselves resources."

A81 §3 makes the corrector a joint claimant–institution policy and the
opponent's class explicit, and separates two classes:

    Σ_A^permitted ⊆ Σ_A^physically available.

"An institution may be inadequate if legitimate opposition alone
routinely makes justified correction unreachable. An institution may
also be vulnerable to unlawful obstruction that it cannot adequately
prevent or remedy. Those are different problems. And a particular actor
may deserve criticism for using wrongful tactics even if the institution
ultimately resists them successfully."

The claim has three parts:

1. **Robustness.** Where the opponent can act on the means of correction,
   [TERM-085](../terms.d/TERM-085.md)'s α_J overstates what the institution can do; the relevant
   quantity is taken against a declared class of opposition.
2. **Order of choice.** sup inf ≤ inf sup always holds, and the gap can be
   strict. A two-route example: correction succeeds if the corrector takes
   a route the opponent has not blocked, and the opponent can block one of
   two. Committing to a route first gives 0; responding to the block gives
   1; committing to an unobserved fair coin gives 1/2. What the corrector
   can observe, and when, is part of its capability.
3. **Two classes, two verdicts.** Failure against permitted opposition is
   evidence about the institution; failure against opposition outside the
   permitted class adds a wrong by the opponent, and the opponent's wrong
   does not need the institution to fail.

Parts 1 and 3 are A's interpretive proposals; part 2's inequality is a
standard fact about minimax, and the example is the filer's check of A's
"These need not agree".

## How it sits with the record

- **[TERM-085](../terms.d/TERM-085.md)** (Active) defines correctability as sup over the
  arrangement's plans, with no opponent. This claim does not replace it;
  it is its adversarial form, for problems where the defendant is part of
  the environment.
- **[CLAIM-537](CLAIM-537.md)** (Active) found the same quantifier order for a
  configuration against disturbances: one configuration for every
  disturbance (∃x ∀w), one per disturbance (∀w ∃x), and an
  observation-dependent case between. This is the corrective counterpart.
- **[CLAIM-568](CLAIM-568.md)** (Active) sorts four ways a transition fails. A81 §3:
  "Our proposed model adds strategic actors who may influence which
  failure occurs."
- **[CLAIM-748](CLAIM-748.md)** files the owner's siege: an objective made
  unreachable by imposing the costs of pursuing it. This claim gives the
  measure on which a siege succeeds and the split that says whether the
  siege was a wrong.
- **[QUESTION-479](../questions.d/QUESTION-479.md)** asks whether a party under a justified constraint
  may set the cost of making it effective. Part 3 says where the answer
  enters: in what goes into Σ_permitted.

## What it does not say

- Not which strategies belong in Σ_permitted. A81 §3: "It also doesn't
  settle which opposing strategies are legitimate. That is a normative
  question about the permissible exercise of procedural authority."
- Not that an institution must withstand every available strategy. A81
  §11: "No institution can reasonably be expected to withstand every
  conceivable disturbance or opponent capability."
- Not an equilibrium model of litigation. Both values are bounds on what
  a corrector can guarantee, not predictions of what parties do.
