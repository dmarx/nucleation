---
status: Proposed
title: 'A single flat-foldable degree-4 vertex under a footprint budget: its two folding modes meet only at the flat state, so passing between folded states needs the full flat footprint of 1.866, more than twice what either folded state at 150° takes'
version: 1
standing: fictional
kind: construction
tags:
- mathematics
- natural-sciences
- complex-systems
date: '2026-11-05'
line:
- distributed-agency
- formal-apparatus
illustrates:
- CLAIM-tmpbi4ca
- CLAIM-tmp9jvpb
summary: >-
  Filed at the owner's request on 2026-11-05, to file "one or more CASEs
  for origami as a toy model of a resource bounded constraint
  configuration space". The minimal toy: one rigid flat-foldable vertex
  with sector angles 60°, 90°, 120° and 90°, whose configuration space is
  two folding modes meeting only at the flat state, and a declared
  resource, the plan area of the smallest convex tray that holds it.
  Folded states cost 0.75 and 0.875; every switch between them passes the
  flat state, which costs 1 + √3/2 ≈ 1.866, so the bottleneck budget is
  1.866 and the reconfiguration slack 0.991. At a budget of 1.5 the
  sublevel set cuts each branch near flat and both states are held but
  neither reaches the other. It rests on Foschi, Hull and Ku's
  equations as read in [NOTE-tmpt4jsa](../notes.d/NOTE-tmpt4jsa.md), with coefficients the filer
  computed and checked, Abel et al. ([NOTE-tmpj2th4](../notes.d/NOTE-tmpj2th4.md)), Chen and Santangelo
  ([NOTE-tmpwpp63](../notes.d/NOTE-tmpwpp63.md)), Stern, Pinson and Murugan ([NOTE-tmp9dvve](../notes.d/NOTE-tmp9dvve.md)) and Mirth et
  al. ([NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md)). A mechanical toy; its organizational reading is an
  analogy. The construction is the filer's. Adopting it is the owner's
  call.
---
<!-- inactive-ok-file: NOTE-tmpt4jsa — Skimmed; Foschi, Hull and Ku, read in part, the source of the equations' form -->
<!-- inactive-ok-file: CLAIM-tmpbi4ca CLAIM-tmp9jvpb CLAIM-tmpuk8gq TERM-tmp2ysyt CASE-tmpb5t9j — Proposed; the entries filed beside it on 2026-11-05, cited as filed, nothing here rests on their being settled -->

# CASE-tmpe48yq: A single flat-foldable degree-4 vertex under a footprint budget: its two folding modes meet only at the flat state, so passing between folded states needs the full flat footprint of 1.866, more than twice what either folded state at 150° takes

## The case

**The vertex.** Four creases of unit length leave a vertex O at 0°, 60°,
150° and 270° in the flat sheet. The sector angles, in order, are
α = 60°, β = 90°, π − α = 120° and π − β = 90°: opposite sectors sum to π,
so the vertex is flat-foldable, and every sector is below π. The faces are
the triangles O c_i c_(i+1), where c_i is the tip of crease i, and the
base face, between creases 4 and 1, lies fixed on a table. Fold angles
ρ_i lie in (−π, π), valley positive, as in Foschi, Hull and Ku
([NOTE-tmpt4jsa](../notes.d/NOTE-tmpt4jsa.md)). Faces are rigid and may not pass through each other, as
in Abel et al.'s definition of rigid origami ([NOTE-tmpj2th4](../notes.d/NOTE-tmpj2th4.md)).

**Its configuration space.** The filed reading gives the shape. A
rigid-foldable degree-4 vertex has exactly two folding modes, two curves
of fold-angle vectors (Corollary 1). For a flat-foldable one, opposite
fold angles are equal up to sign and adjacent ones are linear in
tan(ρ/2) (Theorem 1). The reading does not give the coefficients, and the
proofs are in appendices it did not read. The filer's coefficients, for
sector angles α, β, π − α, π − β in order:

- **Mode A**: ρ3 = −ρ1, ρ4 = ρ2, and
  tan(ρ2/2) = [sin((α+β)/2) / sin((α−β)/2)] · tan(ρ1/2).
- **Mode B**: ρ3 = ρ1, ρ4 = −ρ2, and
  tan(ρ2/2) = −[cos((α+β)/2) / cos((α−β)/2)] · tan(ρ1/2).

*Working.* The closure condition the reading quotes from belcastro and
Hull is that the product of the rotations R(e_i, ρ_i) about the four
creases is the identity. The filer solved it numerically for ρ2, ρ3, ρ4
at fixed ρ1 on several vertices, read off the two families of ratios
tan(ρ_j/2)/tan(ρ1/2), matched them to the expressions above, and checked
the expressions against the closure condition at 2,000 random
flat-foldable vertices and fold angles, both modes: the largest entry of
the product minus the identity was 2 × 10⁻¹⁵. For this vertex the
coefficients are sin 75°/sin(−15°) = −(2 + √3) for mode A and
−cos 75°/cos 15° = −(2 − √3) for mode B.

**The modes meet only at flat.** A state on both has ρ3 = −ρ1 and
ρ3 = ρ1, so ρ1 = 0, and either relation then gives ρ2 = 0. Each relation
is a bijection of (−π, π) onto itself, so each mode is one curve through
the flat state, and taking the flat state out leaves four half-branches,
each running from flat towards a flat-folded limit. A segment–triangle
test at 3,000 states on each half-branch found no face passing through a
non-adjacent face. This is the single-vertex form of what Chen and
Santangelo ([NOTE-tmpwpp63](../notes.d/NOTE-tmpwpp63.md)) and Stern, Pinson and Murugan ([NOTE-tmp9dvve](../notes.d/NOTE-tmp9dvve.md))
describe: branches meeting at a flat state that is a singular point of
the configuration space.

**The resource, declared.** r(q) is the plan area of the smallest convex
tray that holds the folded vertex with its base face on the tray's floor:
the area of the convex hull of O, c_1, …, c_4 projected onto the table. It
stands for swept clearance or floor space. Flat, it is the inscribed
quadrilateral, ½(sin 60° + sin 90° + sin 120° + sin 90°) = 1 + √3/2 ≈
1.866.

**Two folded states.**

- **A**, on mode A with ρ2 = 150°. Then tan 75° = 2 + √3, so
  tan(ρ1/2) = (2 + √3)/(−(2 + √3)) = −1 and ρ1 = −90°: the fold angles are
  (−90°, 150°, 90°, 150°). The projected points are (0, 0), (1, 0),
  (0.5, 0), (0.75, 0.5) and (0, −1); the hull is (0, −1), (1, 0),
  (0.75, 0.5), (0, 0), and its area by the shoelace formula is
  ½(1 + 0.5) = 0.75.
- **B**, on mode B with ρ1 = 150°. Then
  tan(ρ2/2) = −(2 − √3)(2 + √3) = −1 and ρ2 = −90°: the fold angles are
  (150°, −90°, 150°, 90°). The hull is (0, −1), (0.5, −0.75), (1, 0),
  (0, 0.5), with area ½(0.5 + 0.75 + 0.5) = 0.875.

**The bottleneck.** Every path from A to B passes through the flat state,
where r = 1.866, and on each half-branch r stays below its flat value
(4,000 sampled states each). So the bottleneck budget of
[CLAIM-tmpbi4ca](../claims.d/CLAIM-tmpbi4ca.md) is B*(A, B) = 1 + √3/2 ≈ 1.866, and the reconfiguration
slack ([TERM-tmp2ysyt](../terms.d/TERM-tmp2ysyt.md)) is 1.866 − 0.875 = 0.991, more than either folded
state takes. Popping A to its mirror image (90°, −150°, −90°, −150°), on
the other half of mode A, also passes flat and costs the same 1.866, a
slack of 1.116. That is the snap from popped up to popped down that Abel
et al. describe for a vertex with tripods of both parities.

**The budget cuts each branch.** At a budget of 1.5 a half-branch keeps
only the states whose largest fold angle is at least 54.74°; on both
modes r crosses 1.5 there, by the filer's root-finding. The sublevel set
{q : r(q) ≤ 1.5} is four pieces, each a half-branch with the stretch near
flat cut away. A and B both lie in it and can each be held, and neither
reaches the other. For every budget from 0.875 up to 1.866, A and B lie in
different components, which merge at 1.866: in Mirth et al.'s terms
([NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md)) the bottleneck budget is the level at which the two
components of the sublevel sets first join.

**A different resource moves the bottleneck.** Declare instead a crease
energy with rest angle zero, E = (k/2) Σ ρ_i². Along every half-branch
each |ρ_i| grows with the fold, so E is least at flat. Then
B*(A, B) = max(E(A), E(B)) and the slack is zero. The path is the same;
whether the passage it is forced through is the bottleneck depends on
what is declared scarce.

**Checked** by the filer with python3 -I (numpy and scipy): the closure
check above; the two hull areas, 0.75 and 0.875, and the flat area, to
10⁻¹⁵; the maximum of r on each half-branch, reached only at flat; the
crossings of 1.5 at 54.736° on both modes; and the absence of
self-intersection. The arithmetic for A and B is shown above.

## What it can show

- **A threshold above both endpoints, from a real mechanism's
  equations.** [CLAIM-tmpbi4ca](../claims.d/CLAIM-tmpbi4ca.md)'s example uses an invented r(q) on [0, 1].
  Here the shape of the configuration space comes from the mechanism, two
  curves crossing at one singular point, and the resource is the only
  thing declared. The flat state is a passage every switch must make,
  whatever the resource.
- **Feasible at a budget and not reachable within it**, [CLAIM-tmp9jvpb](../claims.d/CLAIM-tmp9jvpb.md)'s
  first separation: at 1.5 both folded states meet the budget and no path
  within it joins them. That failure is neither [CLAIM-357](../claims.d/CLAIM-357.md)'s structural
  infeasibility, since B meets every requirement, nor a realized
  violation; it is the reachability that [CLAIM-tmp9jvpb](../claims.d/CLAIM-tmp9jvpb.md) places between
  them.
- **That the bottleneck sits where the configuration space is singular
  only if the resource peaks there.** With footprint it does; with crease
  energy it does not. The topology fixes where paths must go; the
  declared resource decides what that costs.
- **An analogy, the filer's.** An organization whose two settled
  arrangements are each compact may have to pass through a fully spread
  arrangement to move between them, and what the spread costs shows in
  neither arrangement. That is a reading laid onto a hinge mechanism, not
  something the mechanism shows about organizations.

## What it cannot show

- **Anything about organizations.** It is a mechanical toy; the reading
  above is an analogy and carries no evidential weight.
- **That footprint is scarce for any real fold.** It is declared, to make
  the comparison exact.
- **Time, energy spent or dynamics.** The resource is a capacity, read
  quasi-statically; nothing is said about how the vertex is driven.
- **Several resources.** Every path from A to B goes through the same
  flat state, so a second resource would give one peak vector and a
  frontier of one point; [CLAIM-tmpuk8gq](../claims.d/CLAIM-tmpuk8gq.md)'s non-convexity needs at least two
  routes, which this vertex does not have.
- **More than one vertex, or a proof.** The coefficients are the filer's,
  checked numerically, not derived in closed form here, and the reading
  they extend is Skimmed. For a vertex whose modes do not meet at all, see
  [CASE-tmpb5t9j](CASE-tmpb5t9j.md).
