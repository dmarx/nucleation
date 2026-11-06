---
number: 563
status: Active
formerly:
- CLAIM-tmp7bxc0
title: 'When process costs compose by a monotone operation, the processes costing at most b are closed under composition whenever b composed with itself is at most b, and not otherwise once two composable processes each cost b: at every budget for a peak capacity composed by maximum, and for a cumulative expenditure composed by sum only at budgets 0 and infinity'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-fifth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). THEORY-1435 moves
    from grounds to corroborated_by (ADR-058): the peak case is an
    instance of Marsden and Zwart's quantale-enriched resource theories,
    with max a step the readers took, and the argument does not use it.
    THEORY-1376 leaves grounds: the body cites Lawvere for his additive
    base, an attribution, and the reading of Lawvere is skimmed
    (NOTE-1585, still cited in the body). Steps 1 to 5, the quantale check
    and the reserve instance were re-derived at the review. TERM-105 and
    TERM-114 are adopted in the same review. No objection is on file, and
    nothing meets the defeat condition. The claim is unchanged.
- version: 3
  date: '2026-11-06'
  note: >-
    Corrected at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), on the full reading
    of Lawvere (NOTE-1585): the body said "Lawvere's own base is addition",
    with the max quantale the readers' check; Lawvere gives R_cart, with max
    as tensor, as a closed category (p. 152). THEORY-1376, Active at the
    same review, is added to corroborated_by (ADR-058); the claim does not
    rest on it. No status change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: with costs in an ordered monoid whose operation
  is monotone and a composite costing the operation of its parts, two
  processes each costing at most b, where b composed with itself is at most
  b, whose composite costs more than b; or, under sum, a budget strictly
  between 0 and infinity at which two composable processes each costing b
  compose within b. Not defeated by composites that cost less than the
  operation of their parts (shared setup), where the condition stays
  sufficient and stops being necessary, nor by replenishable reserves,
  which the claim sets aside as having no such law.
tags:
- mathematics
- compositionality
- operations-research
date: '2026-11-05'
line:
- realizability
- formal-apparatus
corroborated_by:
- THEORY-1435
- THEORY-1376
complements:
- CLAIM-571
- CLAIM-585
uses:
- TERM-105
- TERM-114
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 2 §2 and Response 3 §2:
  resource composition is "part of the mathematical specification", peak
  capacity composing by maximum and expenditure by addition, and "the
  collection of b-affordable processes need not itself be a category under
  ordinary composition." The sharper statement is the reader's derivation,
  in the reading of Marsden and Zwart, checked by the filer: closure holds
  exactly when b ⊗ b ≤ b, so always for maximum and, for sum, only at 0
  and infinity. Under maximum the affordable processes form a category at
  every budget and the least cost between two configurations is
  [CLAIM-571](CLAIM-571.md)'s threshold; under sum the cost must be carried as a grade
  that composes, as A proposes. The wording is A's, sharpened by the
  reader; adopting it is the owner's call.
---

# CLAIM-563: When process costs compose by a monotone operation, the processes costing at most b are closed under composition whenever b composed with itself is at most b, and not otherwise once two composable processes each cost b: at every budget for a peak capacity composed by maximum, and for a cumulative expenditure composed by sum only at budgets 0 and infinity

## The claim

A (Response 2 §2): "For instantaneous-capacity constraints, sequential
composition uses the maximum requirement along a path; for cumulative
expenditure, it uses addition. Replenishable reserves require tracking an
evolving state. So I'd treat resource composition as part of the
mathematical specification, not assume one universal notion of cost."
And (Response 3 §2), for a profile κ(p) = (c_p, e_p) of peak and
expenditure, "(c_p,e_p)⊙(c_q,e_q) = (max(c_p,c_q), e_p+e_q)", with the
qualification: "For peak-capacity budgets, processes executable within b
can often be composed without exceeding b. For cumulative budgets, two
processes costing at most b each may together cost 2b. Thus the collection
of b-affordable processes need not itself be a category under ordinary
composition."

**The sharper statement (the reader's derivation, [NOTE-1602](../notes.d/NOTE-1602.md)).** Let
costs lie in an ordered monoid (R, ⪯, ⊗, 0) with ⊗ monotone in each
argument, and let a composite cost the ⊗ of its parts:
κ(g ∘ f) = κ(f) ⊗ κ(g).

1. **Sufficient.** If κ(f) ⪯ b, κ(g) ⪯ b and b ⊗ b ⪯ b, then
   κ(g ∘ f) ⪯ b ⊗ b ⪯ b. Identities cost 0 ⪯ b. So the processes costing
   at most b form a subcategory.
2. **Necessary, given a witness.** If b ⊗ b ⋠ b and two composable
   processes each cost exactly b, their composite costs b ⊗ b and is not
   affordable.
3. **Peak capacity**, ⊗ = max on [0, ∞]: max(b, b) = b at every b, so the
   affordable processes form a category at every budget.
4. **Cumulative expenditure**, ⊗ = + on [0, ∞]: b + b ≤ b only for b = 0
   or b = ∞. At every finite positive budget the affordable processes are
   not closed, as soon as two composable ones each cost more than b/2.
5. **A's pair law** (max, +) at a budget (c, e) is closed only when e is 0
   or ∞: the expenditure component decides it.

Checked by the filer. So A's "need not" becomes: is not, at every finite
positive budget, once there are processes to compose; and A's remedy is
the right one: compose the grades, then let a budget select. In the
reader's words, A's resource-graded process category matches a graded
category, C_x(a, b) × C_y(b, c) → C_{x⊗y}(a, c), which keeps every process
with its grade, as against an enriched category, which keeps only the best
grade between two objects.

**The peak case is the record's threshold.** The readers of Lawvere and of
Marsden and Zwart ([NOTE-1585](../notes.d/NOTE-1585.md), [NOTE-1602](../notes.d/NOTE-1602.md)) check that ([0, ∞], inf,
max) satisfies the definition of a quantale, since max(a, inf_i b_i) =
inf_i max(a, b_i). The least cost of going from q to q′ in the free
category it enriches is the infimum over paths of the largest cost along
the path, [CLAIM-571](CLAIM-571.md)'s bottleneck budget B*. Lawvere's central base is
addition, the "familiar additive shortest-path model" A names, and he also
gives this one: R_cart, with max as tensor, a closed category whose
categories are the ultrametric spaces (Lawvere 1973, p. 152; [NOTE-1585](../notes.d/NOTE-1585.md)).

**Order-dependent costs.** A: "For replenishable resources, the cost may
even depend on the order of operations." The filer's instance: a reserve
starting at 0, replenished by 1 before each step; p spends 2 in one step
and q spends 0. Then q followed by p is feasible and p followed by q is
not, though each spends the same in total. No commutative composition law
on the two processes' costs can tell the orders apart; the reserve has to
be carried in the state, as A says, or in a grade that records more than
totals.

**Parallel composition.** A: "running two processes simultaneously may
require adding their peak demands rather than taking their maximum." The
reading of Raussen ([LIT-2073](../literature.d/LIT-2073.md)), on concurrent programs sharing resources
of given capacities, is a model in which exactly this holds: simultaneous
use adds demands, and the states where a capacity is exceeded are removed
from the state space.

## What it does not say

- **That one law fits a resource.** Which law composes a cost is a fact
  about the resource and the process: shared setup can make a composite
  cost less than the sum, and then the condition is sufficient only.
- **That several capacities compose into one number.** A product of two
  quantales is a quantale, but its least cost is the componentwise
  infimum, which no single path need attain: for [CLAIM-585](CLAIM-585.md)'s two paths
  needing (3, 1) and (1, 3) it gives (1, 1), which suffices for neither.
  Keeping the frontier needs up-sets of budgets as costs (the reader's,
  [NOTE-1602](../notes.d/NOTE-1602.md)), the form [CLAIM-585](CLAIM-585.md) already uses.
- **That Coecke, Fritz and Spekkens state the law.** In their framework
  transformations are free and the costly things are resources; their
  contrast of sum and maximum is a contrast of how resources combine in
  parallel ([NOTE-1591](../notes.d/NOTE-1591.md)), not of how process costs compose in sequence.

## Note of 2026-11-05: the resource-bounded realizability readings

The third paste of the pasted synthesis on resource-bounded realizability reaches this claim from Yoneda: "simply deleting all morphisms that exceed a fixed cumulative budget generally does not yield an ordinary presheaf closed under precomposition", and A asks for a graded law κ(f∘g) ⪯ κ(f)⊙κ(g). In this claim's terms, as the filer's derivation: the morphisms into an object costing at most b are closed under precomposition by probes costing at most b whenever b ⊗ b ⪯ b, and, where costs compose exactly, not once two composable morphisms each cost b and b ⊗ b ⋠ b. If probe morphisms are free, costing 0, they are closed at every budget, since κ(f) ⊗ 0 = κ(f). The peak-capacity case is worked on a degree-4 vertex in [CLAIM-590](CLAIM-590.md), whose max-enriched category puts the two folded states about 1.866 apart. No status changes.

## Note of 2026-11-06: Claude, read

Lawvere 1973 is now read in full ([NOTE-1585](../notes.d/NOTE-1585.md)). "Lawvere's own base is addition" was half the story, and the body is corrected: R, with sum, is his "central example" (p. 145), and he also gives R_cart, "u ⊗ v = max(u, v)", cartesian closed, whose categories are the ultrametric spaces (p. 152). That a closed structure on [0, ∞] with max exists is therefore his statement, and the check that max distributes over infima is the closedness he asserts, since in a closed category the tensor preserves colimits in each variable (p. 141). The peak-capacity reading and the composition-at-budget argument stay the readers'. [THEORY-1376](../theory.d/THEORY-1376.md) corroborates. No status change.
