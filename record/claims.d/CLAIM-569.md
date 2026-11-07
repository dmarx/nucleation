---
number: 569
status: Active
formerly:
- CLAIM-tmpancvu
title: 'A form has at least three resource requirements, to construct it, to maintain it, and to move into or out of it, and none fixes another: a capability can be cheap to keep and dear to acquire, so having enough to sustain it is not having enough to acquire it'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-sixth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). Its premises,
    CLAIM-571 and TERM-105, are Active, and no objection is on file. The
    construction was re-checked step by step: X's construction and
    maintenance costs (24, 2) and Y's (6, 4) rank in opposite orders; X's
    upkeep of 2 fits the surplus of 3 while its construction of 24 exceeds
    the surplus and the budget of 10 within a year and takes 8 years at 3;
    Y is built from two years' surplus and its upkeep of 4 exceeds 3; the
    conversion cost of 14 is below 24. The DNA origami readings in which
    construction and maintenance rank alike (Aksel et al., Shirt-Ediss et
    al.) are what its defeat condition excludes. TERM-106 is cited in the
    body in its two-sided sense and takes no edge.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: capabilities whose stated construction
  and maintenance costs do not rank in opposite orders, a surplus of 3 a
  year that does not cover a maintenance cost of 2 or does cover a
  construction cost of 24 within the year, or a conversion cost that
  equals the construction cost under the stated reuse. Not defeated by
  organizations in which the three requirements happen to coincide or
  rank alike; the claim is that none of them fixes another.
tags:
- operations-research
- society-and-governance
- mathematics
date: '2026-11-05'
line:
- readiness
- realizability
rests_on:
- CLAIM-571
uses:
- TERM-105
bears_on:
- QUESTION-395
- QUESTION-386
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: "An
  organizational form has at least three different resource
  requirements: the resources needed to construct it, the resources
  needed to maintain it, and the resources needed to transition into or
  out of it." [CLAIM-571](CLAIM-571.md) already separates holding a configuration
  from moving into it; the new content is construction as a third,
  separate requirement. Demonstrated by the filer's numbers: a capability
  costing 24 to build and 2 a year to keep, against one costing 6 and 4,
  under a surplus of 3 a year. The first can be sustained and not
  acquired, the second acquired and not sustained. The construction is
  the filer's, from A's three resource requirements of a form; adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CASE-200 CASE-210 CASE-211 — Proposed; A's proposals of 2026-11-04 and the entries filed beside them, cited as filed -->
<!-- inactive-ok-file: TERM-116 — Proposed or new; entries of 2026-11-05 from A's fourth paste and the assistant, cited as open -->

# CLAIM-569: A form has at least three resource requirements, to construct it, to maintain it, and to move into or out of it, and none fixes another: a capability can be cheap to keep and dear to acquire, so having enough to sustain it is not having enough to acquire it

## The claim

A: "An organizational form has at least three different resource
requirements: the resources needed to construct it, the resources needed
to maintain it, and the resources needed to transition into or out of
it. These requirements can be radically different." And: "A capability
can be inexpensive to sustain but expensive to acquire."

**What is already held, and what is not.** [CLAIM-571](CLAIM-571.md) shows that
moving into a configuration can need more than holding it: the bottleneck
budget exceeds the endpoints' requirements by the reconfiguration slack
of [TERM-106](../terms.d/TERM-106.md). That is maintenance against transition. The third
requirement, constructing the form, is separate from both: it is paid
once, it is usually cumulative ([TERM-105](../terms.d/TERM-105.md)), and it is paid by an
organization that does not yet have the form, where a transition is
paid by one moving from a form it has.

**The construction (the filer's numbers).** An organization has a budget
of 10 a year and spends 7 on what it already does, leaving 3.

- **Capability X** (a heavy rescue squad, say): building it, recruiting,
  training and equipping, costs 24 once; keeping it, recurrent training
  and upkeep, costs 2 a year.
- **Capability Y**: costs 6 to build and 4 a year to keep.

Then:

- **Construction and maintenance rank in opposite orders**: X is dearer
  to build (24 > 6) and cheaper to keep (2 < 4). So neither cost fixes the
  other, nor even its rank.
- **X can be sustained and not acquired.** Its upkeep, 2, fits in the
  surplus of 3. Its construction, 24, exceeds the surplus and the whole
  budget within any one year. Saving the surplus with full carry-over,
  it takes 8 years ([CASE-200](../cases.d/CASE-200.md)'s rollover, at a longer horizon).
- **Y can be acquired and not sustained.** Two years' surplus builds it;
  its upkeep, 4, exceeds the surplus of 3.
- **Moving into a form is not building it.** If the organization holds a
  form whose staff and equipment carry over into X, converting costs less
  than 24: say 14. And moving into X's deployed configuration, mobilizing
  four trained members within ten minutes, is a capacity with a deadline
  ([CASE-211](../cases.d/CASE-211.md)), which no annual sum buys.

Checked by the filer.

A's closing: "a system can have enough resources to sustain a capability
without having enough resources—or the right arrangement of
constraints—to acquire it." The construction gives the first case. The
second, an arrangement of constraints that forecloses acquisition at any
budget, is the disconnection of [CLAIM-571](CLAIM-571.md)'s infinite threshold.

## What it does not say

- **That the three are always far apart.** Where a form is bought ready
  and kept by contract, they may nearly coincide.
- **That these are the only three.** Leaving a form, disbanding or
  converting it, has costs of its own; A counts them with entry.
- **That a capability cheap to sustain is worth sustaining.** That it is
  dear to rebuild is one reason to keep it; whether the reason is good
  depends on what it is for, the question of telling a warranted reserve
  from waste ([QUESTION-395](../questions.d/QUESTION-395.md)). [CASE-210](../cases.d/CASE-210.md) is the record's case of a
  maintained squad never used in ordinary operation.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

[TERM-116](../terms.d/TERM-116.md) prices this claim's three requirements per configuration: the incoming profile for constructing, the outgoing for moving out, and a maintenance profile that, in A's words, "is not supplied by Yoneda itself". A: a system "may be easy to assemble but hard to change once assembled"; in [CASE-199](../cases.d/CASE-199.md), L is cheap to reach from U and dear to leave for R. No status changes.

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Rothemund, "Folding DNA to create nanoscale shapes and patterns".** Rothemund (2006), [LIT-2120](../literature.d/LIT-2120.md), read in [NOTE-1631](../notes.d/NOTE-1631.md), supports the separation as a suggestion:
construction needs staple excess (at 1:1 about 1% of structures were rectangles), while "excess
staple strands might be recycled" once folding is complete, so perhaps not needed to hold. The
recycling is untested and the holding conditions were not measured.

**Sobczak, "Investigations of the DNA origami folding process".** Sobczak's dissertation (2018), [LIT-2138](../literature.d/LIT-2138.md), read in part in [NOTE-1644](../notes.d/NOTE-1644.md), supports the claim
directly: between the folding window and the melting transition 5–10 °C above it, a folded object
persists while an unfolded one does not form on laboratory timescales (the brick at 56 °C), and
construction also needs a transient high-temperature step. It leaves open the brick's melting
temperature, which the text read does not give, and whether a melted object returned into the band
stays unfolded, which is inferred, not measured.

**Wagenbauer, Wachauf and Dietz, "Quantifying quality in DNA self-assembly".** Wagenbauer, Wachauf and Dietz (2014), [LIT-2128](../literature.d/LIT-2128.md), read in [NOTE-1637](../notes.d/NOTE-1637.md), support the
construct-maintain split loosely: construction needs a 65 °C heat shock and a tuned temperature
schedule, while products are kept cold. Nothing about maintenance is measured.

**Marras, Zhou, Su and Castro, "Programmable motion of DNA origami mechanisms".** Marras et al. (2015), [LIT-2118](../literature.d/LIT-2118.md), support the claim with three requirements that are visibly separate in one system:
- Construct: a two-day thermal anneal at tenfold staple excess, then gel purification.
- Maintain: bound strands or locking staples, with holding force and torque curves for the joints in pN and pN·nm/rad.
- Transition: about a minute of strand addition (closing strands at twofold excess) or strand displacement (at twentyfold excess).

None fixes another. The paper leaves open how they compare, since it puts them on no common scale.

**Majikes et al., "Revealing thermodynamics of DNA origami folding via affine transformations".** Majikes et al. (2020), [LIT-2117](../literature.d/LIT-2117.md), give partial support on the maintain side. A single fold's melting temperature and free energy are measured on their own and depend on architecture: shorter folds and a less stiff scaffold are more stable, by more than 10 °C from short to long folds. Construction and transition are not measured: fluorescence is recorded on the melt ramp only, so the paper leaves open how the holding requirement relates to the other two.

**Dannenberg, Dunn, Bath, Kwiatkowska, Turberfield and Ouldridge, "Modelling DNA origami self-assembly at the domain level".** Dannenberg and colleagues ([LIT-2129](../literature.d/LIT-2129.md), [NOTE-1645](../notes.d/NOTE-1645.md)) support the separation in a model: halving
or doubling the loop prefactor moves the annealing temperature from 65.3 to 68.2 °C while
hysteresis, the cost of crossing, stays near 1.6-1.9 °C (Table II), and staple concentration moves
construction (annealing) and not dissolution (melting). Maintenance as an ongoing cost is not
modelled, and the evidence is simulation of one tile.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Douglas, Bachelet and Church, "A Logic-Gated Nanorobot".** Douglas, Bachelet and Church (2012), [LIT-2136](../literature.d/LIT-2136.md), support the claim's
three-cost structure cleanly. Construction pays a distinct extra cost not
paid in operation: two guide staples added at folding (raising closed-state
yield 48% to 97.5%) and then removed by toehold-mediated displacement.
Transition (opening) is paid in antigen-key concentration, set by lock
length and independent of what holds the shape. Holding cost is not
measured. None of the three fixes another.

**Douglas et al., "Self-assembly of DNA into nanoscale three-dimensional shapes".** Douglas et al. (2009), [LIT-2130](../literature.d/LIT-2130.md), support the construct-much-greater-than
-maintain gap qualitatively: a week-long thermal ramp to fold, against 24 h
incubations at 30–50 °C or a gel on ice that the folded product survives.
Transition is not studied, and the costs are put on no common scale. No
status changes.

**Aksel, Navarro, Fong and Douglas, "Design principles for accurate folding of DNA origami".** Aksel et al. (2024), [LIT-2125](../literature.d/LIT-2125.md), qualify the claim. A hold-type quantity, the equilibrium stability of each staple at 50 °C, predicts construction yield across their 8 designs (R² = 0.86). In this design family, the cost of keeping the form and the cost of making it co-vary. The paper is a datum that the two can track each other, not a case that separates them. Its model omits kinetics, so it leaves open where they come apart.

**Majikes, Hasni, Haridas, Robertson, Pintar, Zwolak and Liddle, "Complex cooperativity in DNA origami revealed via design-dependent defectivity".** Majikes et al. (2026), [LIT-2127](../literature.d/LIT-2127.md), give mild support. Concentration and anneal time, the constructing resource, are what the authors cut to provoke defects. Measured thermal stability, the maintaining side, enters their predictor as a separate term with about a third of the weight. It correlates with low defectivity rather than coming apart from it.

**Ni, Zhou, Zhu, Bershadsky, Ai, Wang, Sha, Seeman and Chaikin, "Cooperativity, entropy, and effective concentration in DNA origami self-replication".** Ni et al. (2026), [LIT-2124](../literature.d/LIT-2124.md), support the claim:
- Making a copy costs about 21 h of slow cooling and a UV crosslink.
- Keeping it is nearly free once it is covalent.
- Moving out of the template complex needs heating to about 50 °C, a step bounded above by the tile's own unravelling.

No maintenance cost is measured over time.

No status changes.

## Note of 2026-11-05: A's second synthesis on DNA origami

From the second synthesis on DNA origami by another assistant (A), pasted by the owner on 2026-11-05.

A adds a distinction the claim's three requirements imply: "The architecture that supports a completed organization and the architecture that assembles it need not be the same thing." A's example is scaffold routing, which fixes how the chain traverses the target, and so the loop costs of forming it, apart from the target's geometry. Aksel et al. 2024 ([NOTE-1642](../notes.d/NOTE-1642.md)) qualify the example: in their family, the equilibrium stability of the finished staples, a holding quantity, predicts construction yield, and their model ignores kinetics. A's phrase "optimizing a developmental mechanism" goes beyond that paper.

No status changes.

## Note of 2026-11-05: Shirt-Ediss et al., "Optimising DNA origami assembly by reducing off-target interactions", read

Cited in A's third synthesis on DNA origami, pasted by the owner on 2026-11-05.

**Shirt-Ediss, Torelli et al., "Optimising DNA origami assembly".** Shirt-Ediss, Torelli et al. (2026), [LIT-2123](../literature.d/LIT-2123.md), read in [NOTE-1627](../notes.d/NOTE-1627.md), give weak support: construction
yield and persistence over 4 to 5 days at 4 °C are reported separately, and the band of the off-target-prone
rectangle disappeared on storage, a failure of maintenance. Here construction and maintenance rank the
variants the same way, so the reading does not dissociate them, and whether the lost band was misfolded
product or the structure itself is not resolved.

No status changes.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Cumberworth, Frenkel and Reinhardt, "Design-dependent nucleation barriers"; Scheckenbach et al., "Self-regeneration and self-healing".** Both support the claim's separation of resources.
- In Cumberworth et al.'s free-energy calculations ([LIT-2134](../literature.d/LIT-2134.md)), a three-row origami just below Tm is stable but sits behind a barrier of about 10–20 kBT. Design and temperature set the cost to enter apart from the cost to hold.
- In Scheckenbach et al. ([LIT-2139](../literature.d/LIT-2139.md)), maintenance is a standing strand pool at room temperature (22.5 nM per staple), while re-entry from a 12HB missing nine staples took a 300× excess and an anneal from 50 °C, and stayed incomplete (63 % → 32 % defective).
- Winfree and Bekbolatov ([LIT-2119](../literature.d/LIT-2119.md)) add a construction cost, K² tile species and K-fold size, separate from the conditions that hold the crystal.

Left open: the costs are not priced against one another in any of the three.

**Zhou, Sha, Ni, Seeman and Chaikin, "Mutations in artificial self-replicating tiles".**

- In Zhou et al. (2021) the three requirements come apart.
- Constructing a copy costs a full cycle: a 22 °C hold for an hour, 20 min of UV and fresh monomers.
- Holding it is a covalent CNVK bond.
- Moving the daughter off the template needs a 48 °C peak.
- The paper measures none of these as resource costs, so their relative sizes are left open.

No status changes.

## Note of 2026-11-06: Sobczak re-read

Chapter 3 of Sobczak's thesis ([LIT-2138](../literature.d/LIT-2138.md)), re-read in full at the twenty-ninth status review, measures
persistence above the folding window directly: folded structures were "directly jumped to different final
temperatures at which we incubated the folded structures for 2 hours" and unfolded only 5–10 °C above
folding (p. 22). With the brick forming nothing in 48 hours at 56 °C (p. 25), the claim's example rests on
two measurements, not an inference, though the thesis does not pair them at one temperature and gives the
brick's melting temperature only in a figure. [THEORY-1440](../theory.d/THEORY-1440.md) is narrowed to say so. The paragraph on Sobczak
above stands otherwise; no status change.

## Note of 2026-11-07: technical debt as a transition cost, from "Individuation, Possibility, and Disposition"

A, at A32 §7 of the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07), cites this claim rightly for a viable product with no affordable path to a successor, and adds a gloss: "This suggests that *technical debt* can sometimes be understood as an increase in the cost or decrease in the reliability of organizational transitions, rather than simply a reduction in current software quality." That is this claim's requirement to move into or out of a form, named in software terms: cheap to keep, dear to change. A says it "isn't a complete definition of technical debt". The wording is A's. No status changes.
