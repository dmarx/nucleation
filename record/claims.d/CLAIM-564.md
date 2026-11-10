---
number: 564
status: Active
formerly:
- CLAIM-tmp7pv9x
title: 'Restricting the demand–configuration Galois connection to the configurations affordable at a budget gives implications among demands that are antitone in the budget: an implication valid at a budget is valid at every lower one, so as the budget rises the compatibility complex grows and the valid implications shrink, and a set of demands no affordable configuration meets implies every demand'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057). THEORY-1379 moved from grounds to corroborated_by
    (ADR-058): the derivation uses only the definitions of the budgeted
    operators and of a valid implication, and cites Ignatov's formal
    concept analysis as the framework it instances, never the Basic
    Theorem that holds that reading back. CASE-212, its other ground,
    was promoted at the same review. The derivation and the
    four-configuration table were re-checked by a second checker with
    python3 -I, with controls (scratch/formal/case212_check.py).
- version: 3
  date: '2026-11-06'
  note: >-
    Dated note added at the twenty-seventh status review (ADR-057), at the
    status review's ruling (the owner delegated these rulings): Ignatov read
    in full (NOTE-1593), THEORY-1379 Active at the same review, and the
    enumeration rechecked. No status change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: with the configurations, the demands' acceptance
  sets and the resource requirement fixed, an implication among demands
  valid among the configurations affordable at b and failing among those
  affordable at some b′ < b; or an error in the enumeration of the
  four-configuration case. Not defeated by implications that change when
  the configurations or the acceptance sets change, which is a change of
  architecture and not of budget.
tags:
- mathematics
- logic
- complex-systems
date: '2026-11-05'
line:
- realizability
- formal-apparatus
grounds:
- CASE-212
complements:
- CLAIM-586
- CLAIM-347
- CLAIM-574
uses:
- TERM-060
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3 §4: the demand and
  configuration operators Ψ and Φ form an antitone Galois connection whose
  closures record "which demands imply which others", and indexing it by
  budget "gives a family of resource-dependent logical closure structures."
  The reader of Ignatov's formal concept analysis showed it is exactly a
  formal context and derived that the family runs opposite to
  [CLAIM-586](CLAIM-586.md)'s complex: fewer affordable configurations can only add
  implications. Rechecked here on [CASE-212](../cases.d/CASE-212.md). The filer's corollary: an
  implication valid with no budget holds at every budget, and one valid
  only at low budgets is a bundling forced by scarcity. The derivation is
  the reader's, from A's construction; adopting it is the owner's call.
---

# CLAIM-564: Restricting the demand–configuration Galois connection to the configurations affordable at a budget gives implications among demands that are antitone in the budget: an implication valid at a budget is valid at every lower one, so as the budget rises the compatibility complex grows and the valid implications shrink, and a set of demands no affordable configuration meets implies every demand

## The claim

A (Response 3 §4) defines, for demands S and configurations U,
Ψ(S) = {q ∈ Q_z : q satisfies every demand in S} and Φ(U) = {i : every
q ∈ U satisfies D_i}, with U ⊆ Ψ(S) ⟺ S ⊆ Φ(U): "This is an antitone
Galois connection." "Your compatibility complex records whether a
collection of demands can be satisfied. The corresponding Galois
connection additionally records which demands imply which others. For
instance, if every configuration satisfying demands A and B necessarily
satisfies C, then C∈Φ(Ψ({A,B}))." Then: "You could index this
construction by resource budget, restricting Q_z to the affordable
configurations Q_z(b). This gives a family of resource-dependent logical
closure structures."

**It is a formal context** (Ignatov; [NOTE-1593](../notes.d/NOTE-1593.md); [THEORY-1379](../theory.d/THEORY-1379.md)).
Configurations are the objects, demands the attributes, and q meeting D_i the
incidence; Ψ and Φ are the derivation operators, ΦΨ and ΨΦ "are closure
operators", and C ∈ Φ(Ψ({A, B})) is the attribute implication {A, B} → C,
which holds when "each object having all attributes from A also has all
attributes from B." The complex of [CLAIM-347](CLAIM-347.md) is the sets S with Ψ(S)
non-empty.

**Antitone in the budget (the reader's derivation, [NOTE-1593](../notes.d/NOTE-1593.md)).** Write
Ψ_b(S) = Ψ(S) ∩ Q(b). An implication S → T is valid at b when
Ψ_b(S) ⊆ Ψ_b(T). If b′ ≤ b then Q(b′) ⊆ Q(b), and intersecting both sides
with Q(b′) gives Ψ_b′(S) ⊆ Ψ_b′(T). So:

1. **An implication valid at b is valid at every lower budget**, and the
   set of valid implications shrinks as the budget rises, while K(b)
   grows ([CLAIM-586](CLAIM-586.md)).
2. **A frustrated set implies everything.** If no affordable configuration
   meets S, Ψ_b(S) is empty and S → T holds for every T, vacuously.
3. **Structural and scarcity implications (the filer's corollary).** Since
   Q(b) ⊆ Q, an implication valid among all configurations, with no
   budget, is valid at every budget. One valid at b and not without a
   budget holds only because the affordable configurations bundle the
   demands, the implication counterpart of [CLAIM-586](CLAIM-586.md)'s split between
   being short of resources and being structurally frustrated. With
   finitely many configurations the implications at every budget above
   the dearest configuration's cost are the unbudgeted ones.

**The worked case** ([CASE-212](../cases.d/CASE-212.md): q₁ at cost 1 meeting {1}, q₂₃ at 1
meeting {2, 3}, q₁₂ at 2, q₁₃ at 3). Implications S → j with j ∉ S, by
enumeration:

| budget | affordable | valid implications | of which vacuous |
|---|---|---|---|
| 1 ≤ b < 2 | q₁, q₂₃ | 2 → 3, 3 → 2, {1, 2} → 3, {1, 3} → 2 | {1, 2} → 3, {1, 3} → 2 |
| 2 ≤ b < 3 | adds q₁₂ | 3 → 2, {1, 3} → 2 | {1, 3} → 2 |
| b ≥ 3 | adds q₁₃ | none | (only the triple, which implies all) |

q₁₂ breaks 2 → 3 and q₁₃ breaks 3 → 2. With no budget no implication
holds among the three, so 2 → 3 and 3 → 2 are bundlings forced by
scarcity, not consequences of the demands. Checked by the filer by
enumeration, agreeing with the reader and with the filer of [NOTE-1593](../notes.d/NOTE-1593.md).

## What it does not say

- **That the implications are logical entailment.** They hold over the
  given configurations; A's "logical consequences among constraints" are
  consequences in this context, as the reading says.
- **That the lattice is a finding.** A concept lattice exists for any
  incidence, "guaranteed by construction" ([THEORY-698](../theory.d/THEORY-698.md)). What carries
  information is its shape and how it changes with the budget.
- **Anything for several resources.** With a vector budget the same
  argument gives antitonicity along the partial order; the implications at
  incomparable budgets need not be comparable.
- **That frustration is relative to budget everywhere.** [TERM-060](../terms.d/TERM-060.md)'s verdict
  of frustration at a budget is resource-relative only for sets outside
  K(b) and inside the unbudgeted complex; the implication form adds which
  demands are tied together at that budget.

## Note of 2026-11-06: Claude, read

Ignatov is now read in full ([NOTE-1593](../notes.d/NOTE-1593.md)), and [THEORY-1379](../theory.d/THEORY-1379.md), which corroborates this claim, is Active at the same review on the re-derivation of the Basic Theorem recorded there. The enumeration on [CASE-212](../cases.d/CASE-212.md) was rechecked independently and matches the table exactly, including that no implication holds with no budget (scratch/formal/fca_basic_theorem_check.py). The tutorial's attribute exploration (§7.1) is a standard use of the same monotonicity: an implication valid in a subcontext can only be refuted by adding objects. Point 1 is therefore a known property of formal contexts applied to budgets; the budget reading and the corollary in point 3 remain the reader's and the filer's. No status change.
