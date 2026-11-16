---
status: Proposed
title: 'A mutual-maintenance construction: an intact share c repaired through a capacity r that c itself produces, both turning over on a standing supply s, is bistable at s = 1 with a saddle at (0.0955, 0.2764), so its survival threshold is a separatrix in the joint state and not a level of c; a constant outside controller holding r at its maintained value gives the same equilibrium but recovers from c = 0.01, where the mutual system collapses; a founding pulse can be withdrawn and the supply cannot'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- individuation
date: '2026-11-15'
line:
- transient-support
- distributed-agency
illustrates:
- CLAIM-522
- CLAIM-597
- CLAIM-604
bears_on:
- QUESTION-398
- QUESTION-399
summary: >-
  From A5 §§5.1–5.4 of the exchange "Explain String Theory" (2026-11-15).
  Every number was recomputed on filing, and the founding and withdrawal
  runs were added as checks (scratch/formal/soliton_testbed_checks.py).
  Fictional by construction, with illustrative parameters. A calls its
  Proposition C1 ("Matching maintained states does not identify where their
  maintenance is produced") "another explicit witness rather than an
  entirely new proposition" for [CLAIM-522](../claims.d/CLAIM-522.md), which is right, with one
  difference recorded below: A's controller is constant, not [CLAIM-522](../claims.d/CLAIM-522.md)'s
  state-feedback controller, so interventions on state do separate the two
  here. [CASE-189](CASE-189.md) holds a three-unit version of reciprocal production; this
  one is the two-variable extension of [CLAIM-604](../claims.d/CLAIM-604.md)'s one-variable model that
  A names. Proposed because the construction is A's; adopting it is the
  owner's call.
---

# CASE-tmp3ioyf: A mutual-maintenance construction: an intact share c repaired through a capacity r that c itself produces, both turning over on a standing supply s, is bistable at s = 1 with a saddle at (0.0955, 0.2764), so its survival threshold is a separatrix in the joint state and not a level of c; a constant outside controller holding r at its maintained value gives the same equilibrium but recovers from c = 0.01, where the mutual system collapses; a founding pulse can be withdrawn and the supply cannot

## The model

    ċ = −c + 4 s r c (1 − c),
    ṙ = −r + 4 c (1 − r).

c is the intact share of an organization, which deteriorates unless
repaired. Repair needs a maintenance capacity r. The organization produces
r, and r turns over too. The supply s is provided by the environment.

## The numbers, rechecked

At s = 1 there are three equilibria in the unit square:

| | c | r | eigenvalues | |
|---|---|---|---|---|
| collapsed | 0 | 0 | −1, −1 | stable |
| threshold | (3 − √5)/8 ≈ 0.0955 | ≈ 0.2764 | ≈ 0.443, −1.930 | saddle |
| maintained | (3 + √5)/8 ≈ 0.6545 | ≈ 0.7236 | ≈ −1.436, −4.076 | stable |

The positive equilibria come from r = 4c/(1 + 4c) and 16c² − 12c + 1 = 0.

- **The threshold is joint.** Starting from c = 0.12, above the saddle's c,
  the system collapses when r = 0 and is maintained when r = 0.3. A: "The
  survival threshold is a property of a joint organizational state, not a
  scalar amount of intact structure."
- **A constant controller** holding r at r₊ ≈ 0.7236 has the same
  maintained c₊ ≈ 0.6545. From c = 0.01 it recovers to c₊. The mutual
  system started at (0.01, r₊) collapses. Disabling the pathway c → r makes
  the mutual system's r decay, and c follows it. The controlled system is
  untouched.
- **Founding against feeding.** Add h(t)(1 − c) to ċ. A pulse h = 1 on
  [0, 5) takes the collapsed state into the maintained basin, and after it
  is withdrawn the system stays maintained. Setting s = 0 gives ċ = −c, and
  the organization ends.

## What it shows

- **For [CLAIM-522](../claims.d/CLAIM-522.md).** Matched steady states do not identify where
  maintenance is produced. In this construction interventions on state
  do separate the two architectures, because the outside controller is
  constant. [CLAIM-522](../claims.d/CLAIM-522.md)'s ideal controller supplies the production law as
  state feedback, and only interventions on mechanism separate that one.
  The case is therefore a weaker witness than [CLAIM-522](../claims.d/CLAIM-522.md)'s own, and it
  marks where the claim's ideal case begins: a controller that ignores the
  state is found out by perturbing the state.
- **For [CLAIM-597](../claims.d/CLAIM-597.md).** Its split between founding and feeding, in a system
  that produces its own repair capacity. It stays independent of what
  founded it and dependent on what feeds it.
- **For [CLAIM-604](../claims.d/CLAIM-604.md).** An ignition threshold in two variables, where the
  threshold is a separatrix and not a level.
- **For [QUESTION-398](../questions.d/QUESTION-398.md) and [QUESTION-399](../questions.d/QUESTION-399.md).** The founding pulse can be
  withdrawn safely once the joint state is past the separatrix. The
  capacity that makes repair possible is itself regenerated, which is
  [QUESTION-399](../questions.d/QUESTION-399.md)'s self-maintaining nucleus in a minimal form, though on a
  supply it does not control.

## What it cannot show

Whether r is a constitutive constraint in [TERM-088](../terms.d/TERM-088.md)'s sense. A: "Mutual
positive feedback alone is not sufficient to establish every philosophical
or biological meaning of autonomy." The parameters are illustrative.
