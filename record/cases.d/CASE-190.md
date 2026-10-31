---
number: 190
status: Active
formerly:
- CASE-tmpz9u5t
title: 'A kinetic construction of self-maintaining reconstruction: a brief encounter captures a fuel, connector and two-catalyst core into a box that stays invariant under bounded degradation, keeping its copying catalyst regenerated and a grounded teacher and an erasable student within bounded error; with a resource allocator holding reserved minima and a revisable copy rule, the certificate holds for every allocation and rule, because neither the information variables nor the rule feed back into maintenance'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- mathematics
- thermodynamics
date: '2026-10-31'
line: distributed-agency
variant_of:
- 'CASE-189'
illustrates:
- CLAIM-475
- CLAIM-422
summary: >-
  From A17 and A18 of the exchange "Analyze nucleation concepts"
  (2026-10-31), after the owner asked for "one system in which those
  conditions are all physically realized rather than assumed
  independently", and then for an endogenous allocation controller with a
  barrier certificate. The certificates were rechecked by the reader of
  U16–U19, and two of A's error bounds were loose. The simulations A17 and
  A18 report could not be checked: their code was in A's sandbox. A19 later
  said "Our last model explicitly demonstrated the separation" between
  matched successors after a second injury; it did not, and that
  experiment was never run.
---

# CASE-190: A kinetic construction of self-maintaining reconstruction: a brief encounter captures a fuel, connector and two-catalyst core into a box that stays invariant under bounded degradation, keeping its copying catalyst regenerated and a grounded teacher and an erasable student within bounded error; with a resource allocator holding reserved minima and a revisable copy rule, the certificate holds for every allocation and rule, because neither the information variables nor the rule feed back into maintenance

## The six-variable model (A17)

State z = (r, q, c₁, c₂, u, v): fuel r, supplied at rate J; the connector
q of [CASE-189](CASE-189.md); two catalysts producing each other; a teacher u that
tracks a grounded signal θ; and a student v copied from the teacher at
rate k_copy = r q c₂.

Rechecked:
- **Invariance.** The box is positively invariant after the encounter
  ends. The margins are +0.16 at cᵢ = 1, −18 at cᵢ = 6, +0.224 at q = 0.8,
  −1 at q = 1 and +0.568 at r = 0.8. For u and v the margin is 0.05
  against disturbances of 0.02. Fuel stays sufficient when J > 12.16.
- **Copying is kept up.** k_copy ≥ 0.64 throughout the box.
- **Errors.** Teacher error is at most 0.05/0.74 ≈ 0.068. A17 gave 0.135
  for the student; the comparison bound is in fact
  max over k ≥ 0.64 of (0.068k + 0.05)/(k + 0.1) ≈ 0.126.
- **Capture.** An encounter of 0.15 time units brings q to at least
  0.868 and c to at least 1.73, inside the box.
- **Knockout.** Removing c₂'s production sends c₂, then c₁, then q to
  zero.

A17's simulation erased the student and damaged the copying catalyst
within the certified region. Recovery there is guaranteed by construction,
so it does not test whether repair machinery can itself be repaired. A
noise-free rerun of the stated equations agrees with A17's table.

## The twelve-variable extension (A18)

A18 adds a regulatory catalyst s, a copy rule φ with
g_φ(u) = (1 − φ)u + φ/2 (φ = 0 is faithful copying), and
replicator–mutator allocation shares over operation, maintenance,
diagnosis and copying, with reserved minima 0.55, 0.10, 0.10 and 0.05.

Rechecked:
- The margins are 0.416, 0.108, 0.3264 and 1.22, and the upper faces point
  inward.
- The teacher bound is 0.123, and u ∈ [0.5, 0.8] is invariant. The student
  bound of 0.246 is valid but loose; the tight bound is ≈ 0.215, and it
  holds only as φ → 0.
- Not checkable: A18 never states its fuel demand Ψ, so its J > 28.9
  cannot be checked.

**What carries the certificate.** It holds "for every allocation"
because of the reserved minima. A18 called these "constitutive
architecture", so they are an assumption, not something the organization
earned. The certified decay φ̇ ≤ −0.0144φ comes entirely from a
regularizer whose minimum is the faithful rule; the evidence term only
contributes ≥ 0. So the rule's "corrigible" revision is built in. And
because φ and the information variables feed nothing physical, rule
revision is trivially safe.

**A negative result, from an unverified simulation.** Comparing
adaptive allocation, fixed allocation and a frozen copy rule after five
injuries, A18 reported recovery of 0.687, 0.586 and 0.477 at t = 8.125,
and 0.794, 0.794 and 0.544 at t = 30. A18: "An allocator that responds
intelligently to immediate functional error can still perform worse on
recovery if it underinvests in repairing the rule responsible for future
corrections. The fact that an allocation mechanism is endogenous does not
make it optimal."

## What it shows and does not

It shows that, in one stipulated model, the regeneration of a
reconstruction operator's realizer can be part of what an organization
maintains. That is the owner's U17 question in its simplest form. A17's
own limit: "we've demonstrated endogenous reconstruction of the realizer
and availability of an operator, not autonomous invention of an entirely
new operator type".

Three gaps remain:
- **The coupling runs one way.** Copying never feeds maintenance, so the
  loop in which "successful copying is itself required to maintain the
  copying machinery" is not built.
- **The information is thin.** It is one scalar, and grounding is
  stipulated by injecting θ into the teacher's equation.
- **There is no succession.** The student never becomes a teacher.

The motifs are irreversible mass action, as A17 said, "not yet a
finite-affinity, microscopically reversible chemical model". Each face's
inward margin exceeds the disturbance bound (+0.16 to +0.568 against 0.02),
so the box certificate is robust invariance of the box itself, viability in
[THEORY-134](../theory.d/THEORY-134.md)'s sense. Kolathaya and Ames's input-to-state safety
([LIT-1893](../literature.d/LIT-1893.md), [THEORY-1267](../theory.d/THEORY-1267.md)) is the weaker, graded guarantee that would
apply beyond that margin, where the safe set is enlarged by a class-K
function of the disturbance. That organization lowers the cost of further organization
is [CLAIM-475](../claims.d/CLAIM-475.md), which A19 announced as a discovery.
