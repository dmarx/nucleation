---
number: 111
status: Proposed
formerly:
- TERM-tmpckwjg
title: 'universality, of resource-bounded constraint systems, and which sense: expressive, that a restricted family implements every member of a class; computational, that one family resource-simulates another with bounded overhead, an equivalence only when the simulation runs both ways; or scaling, that families share asymptotic laws'
version: 1
tags:
- mathematics
- complex-systems
- philosophy-of-science
date: '2026-11-05'
line:
- realizability
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 1 §3, Response 2 §6 and
  Response 3 §§7 and 8: three notions of universality "with different
  mathematical requirements", expressive, computational and scaling;
  resource simulation, κ_𝔄(p̂) ⪯ P_n(κ_𝔅(p)), and its two-way form or a
  resource-aware bisimulation for equivalence; and three levels, solution,
  process and organizational. Filed as a term with senses, like the record's
  terms that say which sense of a word is meant, so a claim of universality
  says which it makes. It carries A's guard, checked by the filer: if
  arbitrary transition graphs may be declared, expressive universality is
  trivial, so the sense informs only relative to restricted primitives. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-034 CLAIM-573 NOTE-1584 QUESTION-008 THEORY-1407 — Deferred or Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->
<!-- inactive-ok-file: CLAIM-473 CLAIM-478 THEORY-812 — Proposed or new; the resource-bounded realizability readings of 2026-11-05, cited as open -->

# TERM-111: universality, of resource-bounded constraint systems, and which sense: expressive, that a restricted family implements every member of a class; computational, that one family resource-simulates another with bounded overhead, an equivalence only when the simulation runs both ways; or scaling, that families share asymptotic laws

## Definition

For families of resource-bounded constraint systems in [TERM-114](TERM-114.md)'s
sense, A separates three notions (Response 3 §7): "I think we should
resist the temptation to define one overarching equivalence relation too
early."

**Expressive.** "A family of systems is expressively universal if it can
represent or implement every member of some specified class of
computational processes or constraint structures." A's example: whether "a
restricted family of origami mechanisms can simulate arbitrary
finite-state transition systems."

**Computational**, by resource simulation. For families 𝔒 = {𝔒_n}, A
defines the decision problem REACH_𝔒 = {(n, s, t, b) : ∃p : s ⇝ t,
κ(p) ⪯ b}. One system 𝔄 resource-simulates another 𝔅 "when there is an
efficiently computable translation of states and processes such that valid
executions of 𝔅 can be realized by 𝔄, with controlled overhead", for
polynomial overhead κ_𝔄(p̂) ⪯ P_n(κ_𝔅(p)) with P_n "an appropriately
bounded, order-preserving resource transformation" (Response 3 §8); and
"The simulation must also preserve the observables and the questions we
care about." Equivalence needs more: "a one-way simulation is not enough
for equivalence", only "an appropriate two-way simulation or a
resource-aware bisimulation". Response 1's first statement is the same
sense: "Two resource-bounded constraint systems belong to the same
computational universality class when they can efficiently simulate one
another in a way that preserves constraint satisfaction, permitted
transformations, and resource requirements up to a specified overhead."
The comparison is "between entire families of systems of increasing size,
not isolated finite objects" ([CLAIM-578](../claims.d/CLAIM-578.md)).

**Scaling.** "Here we'd compare large families of systems and ask whether
their behavior approaches the same scaling laws", for instance whether the
least resource to reach a target scales as B_n* ∼ n^α, or a success
probability changes sharply at some normalized resource level. "It
requires a declared system-size parameter, a class of perturbations or
ensembles, and measurable asymptotic behavior."

**At which level** (Response 2 §6). Each sense can be asked of three
things:

- "Solution universality: Different systems realize equivalent constraint
  structures."
- "Process universality: Different systems support equivalent
  resource-bounded transformations."
- "Organizational universality: Different systems can construct, maintain,
  or regenerate equivalent repertoires of constraints."

Response 1's split of U_comp from U_phys, "two potentially independent
classifications", is the computational sense against the physical one
(energy barriers, error tolerance, precision of control) asked of the same
families.

## What it is not

- **Expressive universality with unrestricted primitives.** A: "If we allow
  arbitrary transition graphs to be declared directly, universality becomes
  nearly trivial." The filer's check: if a member of the family may be any
  finite directed graph with costs, every finite transition system is
  itself a member and is represented by the identity translation, so the
  family is universal for that class by definition. A claim of expressive
  universality says something only relative to stated limits on the
  primitives, A's "bounded crease complexity, local constraints, limited
  actuation, planar construction". The same warning the record keeps for a
  concept lattice that exists for any incidence, "guaranteed by
  construction" ([THEORY-698](../theory.d/THEORY-698.md)). Where the primitives are restricted the
  sense has content: Gopalan et al. ([NOTE-1584](../notes.d/NOTE-1584.md); [THEORY-1407](../theory.d/THEORY-1407.md)) show
  that from a Boolean language that is not tight every relation is
  faithfully expressible, connectivity of solutions included, a theorem
  because the primitives are fixed.
- **Sameness of complexity class.** A: "having the same complexity class
  does not imply having the same transition geometry or resource
  requirements." The filer adds the converse caution: at the level of the
  decision problem alone, families whose reconfiguration is PSPACE-complete
  (Eppstein's flaps and flips, [NOTE-1611](../notes.d/NOTE-1611.md), [THEORY-1372](../theory.d/THEORY-1372.md); Gopalan et
  al.'s languages that are not tight) are already reducible to one another
  in polynomial time by completeness. A computational universality claim
  adds to that only if its simulation carries processes and their costs,
  not only the yes or no of REACH.
- **One-way simulation.** [CLAIM-034](../claims.d/CLAIM-034.md) makes the same split for translation,
  where an adaptive translation calls for one-way simulation rather than
  equivalence; [QUESTION-008](../questions.d/QUESTION-008.md) asks whether pragmatic fidelity is an
  approximate bisimulation. Neither is about resources.
- **The universality of statistical physics alone.** That is the scaling
  sense only, and A expects the senses to come apart: "It's possible that
  origami, constraint networks, and organizational systems could share
  computational universality while belonging to different scaling
  universality classes."

## What would settle it

Adoption by the owner, or a claim of the record's own stated in it.
[CLAIM-573](../claims.d/CLAIM-573.md), A's universality hypothesis, is stated in it.

## Note of 2026-11-05: the resource-bounded realizability readings

The second paste of the pasted synthesis on resource-bounded realizability proposes computational, architectural and regenerative universality: implementing an expressive class of computations, constructing or reconfiguring an expressive class of constraint architectures, and reproducing the capacities for those constructions through turnover. A: "one does not automatically imply the next". It splits this term's organizational level into constructing or reconfiguring and regenerating. A's boundary case: an externally designed crease pattern may implement a computation without producing the pattern or maintaining the machinery that folds it, the gap [CLAIM-566](../claims.d/CLAIM-566.md) keeps between assembling and regenerating.

From [THEORY-1054](../theory.d/THEORY-1054.md), where one arrangement gives a wave or a heat equation by its update semantics, A concludes that a universality class must say whether it classifies constraints, operations, dynamics or a combination; A notes [CLAIM-473](../claims.d/CLAIM-473.md) is Rejected and that what survives, in [CLAIM-478](../claims.d/CLAIM-478.md), is conditional. For the scaling sense A takes [THEORY-391](../theory.d/THEORY-391.md) and [THEORY-812](../theory.d/THEORY-812.md) as the template, with candidate observables such as the least resources to find a compatible configuration or the fraction of reliably reachable targets. No status changes.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

A's fourth paste splits universality into five classifications, constraint, process, resource, observational and organizational, and three regimes for the translation overhead (polynomial, bounded multiplicative distortion, exact interface): "There is no reason to assume these notions coincide." A recommends looking for implications and separations among them; the interface separations are asked in [QUESTION-382](../questions.d/QUESTION-382.md). No status changes.

## Note of 2026-11-06: what holds it back

The definition gives three senses at three levels, and its notes of 2026-11-05 record two later divisions from the same synthesis that it does not place: the second paste's "computational" universality, which the note glosses as "implementing an expressive class of computations", is by that gloss this term's expressive sense under the name the term gives another, and the fourth paste's five classifications and three overhead regimes are not said to be senses, levels or regimes of this term. Until the definition places them or excludes them, a claim citing those pastes cannot say which sense it means; the uses so far, CLAIM-573 and QUESTION-384 in the computational sense, do.
