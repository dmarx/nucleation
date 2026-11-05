---
status: Proposed
title: 'Indexing the compatibility complex by a resource budget gives a complex that grows with the budget and never exceeds the complex with no budget, so a set of demands outside the unbudgeted complex is frustrated at every budget, and one inside it but outside the complex at budget b is short of resources at b, not frustrated'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: budgets b ≤ b′ and a set of demands that is a
  face of the complex at b and not at b′; a face of the complex at some
  budget that is not a face of the unbudgeted complex; or, with finitely
  many demands and a finite-valued resource requirement, a face of the
  unbudgeted complex that no finite budget admits. Not defeated by a
  change of the configurations or of the demands' acceptance sets, which
  is a change of architecture and not of budget, nor by resources that
  buy such a change; the claim holds them fixed.
tags:
- mathematics
- operations-research
- complex-systems
date: '2026-11-05'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-347
complements:
- CLAIM-tmpal9mc
uses:
- TERM-060
bears_on:
- QUESTION-131
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: K(b) = { S :
  ∃ q ∈ Q, R(q) ≤ b, q ∈ ∩_{i∈S} D_i }. A: "no amount of additional
  actuation budget eliminates a genuine geometric incompatibility while
  the geometric constraints remain unchanged." Shown here: K(b) is a
  complex, monotone in b, contained in the complex of Q with no budget,
  and with finitely many demands equal to it from some finite budget on.
  So a missing face is either short of resources at b or structurally
  frustrated, and the unbudgeted complex tells which. [CLAIM-347](CLAIM-347.md) already
  indexes its complex to a budget; the monotonicity, the bound and the
  split are what is new. The wording is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-tmpsbhp8 CLAIM-tmpal9mc CLAIM-tmpuk8gq CLAIM-555 — Proposed; the case and claims filed beside this one from A's synthesis of 2026-11-04, and a held claim, cited as filed -->
<!-- inactive-ok-file: NOTE-tmplptka CLAIM-tmp7pv9x CLAIM-tmpsbz28 CLAIM-tmplysd0 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# CLAIM-tmpuxuo4: Indexing the compatibility complex by a resource budget gives a complex that grows with the budget and never exceeds the complex with no budget, so a set of demands outside the unbudgeted complex is frustrated at every budget, and one inside it but outside the complex at budget b is short of resources at b, not frustrated

## The claim

A: "The resource inequality describes quantities. The equality
constraints describe which configurations are structurally possible.
Both are needed." And: "Increasing a resource budget can enlarge the
complex when the relevant feasible sets are nested. But no amount of
additional actuation budget eliminates a genuine geometric
incompatibility while the geometric constraints remain unchanged." A's
mechanical case is a flat-foldable vertex, where Kawasaki's condition
fixes the sector angles a fold needs: "The geometry cannot be fixed by
simply applying more force or increasing the actuation budget."

**The construction.** Fix an architecture. Let Q be its configurations,
the solutions of its equality constraints F(q) = 0; D_1, …, D_N ⊆ Q the
configurations meeting each demand; and R : Q → ℝ^m the resources holding
q takes, finite everywhere. For a budget b ∈ ℝ^m,

  K(b) = { S ⊆ {1, …, N} : some q ∈ Q has R(q) ≤ b and q ∈ ⋂_{i∈S} D_i },

and K_Q = { S : Q ∩ ⋂_{i∈S} D_i ≠ ∅ }, the compatibility complex of
[CLAIM-347](CLAIM-347.md) for this architecture with no budget.

1. **K(b) is a complex.** If q witnesses S, it witnesses every subset of S.
2. **Monotone.** If b ≤ b′ componentwise and q witnesses S at b, then
   R(q) ≤ b ≤ b′, so q witnesses S at b′: K(b) ⊆ K(b′). A's qualifier
   "when the relevant feasible sets are nested" is met automatically: the
   sets {q ∈ Q : R(q) ≤ b} grow with b because Q and R are held fixed.
3. **Bounded.** A witness at b lies in Q ∩ ⋂_S D_i, so K(b) ⊆ K_Q.
4. **Attained.** With finitely many demands K_Q has finitely many faces.
   Pick a witness q_S for each and let b̄ be the componentwise maximum of
   the R(q_S). Then K(b) = K_Q for every b ≥ b̄, and the union of K(b)
   over all budgets is K_Q.

Checked by the filer. [CASE-tmpsbhp8](../cases.d/CASE-tmpsbhp8.md) is a worked instance: three demands,
whose pairs enter at budgets 1, 2 and 3 and whose triple never does.

**So a missing face is one of two things.** For S ∉ K(b):

- **Short of resources** when S ∈ K_Q. Some larger budget admits it, and
  raising the budget to that level is relief in [CLAIM-347](CLAIM-347.md)'s sense, a
  strict enlargement of the complex for the same declared demands.
- **Structurally frustrated** when S ∉ K_Q. No budget admits it while Q
  and the D_i are fixed. The minimal non-faces of K_Q are the conflicts
  only a change of architecture can relieve.

A: "That is a clean mechanical way to separate resource scarcity from
structural frustration." [TERM-060](../terms.d/TERM-060.md) already records that a budget on
admissible updates can turn strain into frustration, and that the verdict
is then relative to the budget. This claim says how to read that verdict:
frustration at budget b that is absent from K_Q is resource-relative, and
the rest is not. [CLAIM-365](CLAIM-365.md)'s worked case, where no budget helps, is a
non-face of K_Q; [CLAIM-357](CLAIM-357.md) separates the same structural infeasibility
from governance regret.

A's organizational reading: "An organization may have adequate total
staffing yet lack the right combinations of skills at the right locations
and times." Adequate totals put the budget high; the missing combination
is a non-face of K_Q, or a face whose witness costs more in some one
resource than the budget allows.

## What it does not say

- **That raising a budget never changes the architecture.** Money can buy
  new configurations, new acceptance sets, a different Q. That is a change
  of architecture, and the claim says nothing about it. A's qualifier,
  "while the geometric constraints remain unchanged", is load-bearing.
- **That one scalar budget suffices.** With several resources the budgets
  admitting a face form an up-set that need not be convex
  ([CLAIM-tmpuk8gq](CLAIM-tmpuk8gq.md)), so being short of resources can mean short in the wrong
  resource.
- **Anything about reaching a witness.** K(b) asks whether some affordable
  configuration meets the demands, not whether the organization can get
  there; transitions and their obstructions are [CLAIM-tmpal9mc](CLAIM-tmpal9mc.md)'s.
- **That the complex is the finest invariant.** [CLAIM-555](CLAIM-555.md) holds the
  complex a coarse summary beside finer ones.

## Note of 2026-11-05: the resource-bounded realizability readings

The reading of Ignatov's introduction to formal concept analysis (NOTE-tmplptka, read in part), filed beside the pasted synthesis on resource-bounded realizability, shows that A's demand–configuration connection is the derivation-operator connection of a formal context, with configurations as objects and demands as attributes. K(b) is then the sets of demands with a nonempty extent among the configurations affordable at b. Restricting the objects to those configurations gives implications among demands that are antitone in the budget while K(b) grows. That is the reader's derivation, rechecked by the filer on CASE-tmpsbhp8 and filed as CLAIM-tmp7pv9x.

Two entries filed from the same paste mark what the complex does not carry, in line with this claim's own disclaimer about reaching a witness. CLAIM-tmpsbz28 gives two systems with the same complex, move rule and costs that differ in reachability, and CLAIM-tmplysd0 holds that one organization's complex, a single fixed instance, has no computational complexity. No status changes.
