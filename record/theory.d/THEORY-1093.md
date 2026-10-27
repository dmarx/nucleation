---
number: 1093
status: Active
formerly:
- THEORY-tmpyoeip
title: 'In Di Biagio and Rovelli''s reformulation of relational quantum mechanics a relative fact is a conditional probability concentrated on one value: A is a fact relative to B when the relative information I_{A|B} = I_A + I_{A:B} is maximal; since only commuting variables have a joint distribution, perspectives belong to commutative subalgebras of observables, not to quantum systems, so a qubit has none, and the joint distribution is itself relative to a further system, so the relativity iterates'
version: 1
tags:
- quantum-foundations
- information-theory
date: '2026-10-27'
source:
- LIT-1676
summary: >-
  Di Biagio and Rovelli (2025), [LIT-1676](../literature.d/LIT-1676.md), read from arXiv v2 in
  [NOTE-1214](../notes.d/NOTE-1214.md), §§II–V and IX. Active as a statement of the paper's
  definitions and of what follows from them: eq. (7) is an identity, and
  the restriction to commuting variables follows from the existence of
  joint distributions. It does not say that this resolves the problems the
  authors list, that observers play no role in fixing what counts as a
  fact, or that the choice of subalgebra is given by the physics.
---
<!-- inactive-ok-file: THEORY-621 — Proposed; the earlier statement, cited as open -->

# THEORY-1093: In Di Biagio and Rovelli's reformulation of relational quantum mechanics a relative fact is a conditional probability concentrated on one value: A is a fact relative to B when the relative information I_{A|B} = I_A + I_{A:B} is maximal; since only commuting variables have a joint distribution, perspectives belong to commutative subalgebras of observables, not to quantum systems, so a qubit has none, and the joint distribution is itself relative to a further system, so the relativity iterates

## Source

Di Biagio and Rovelli (2025), [LIT-1676](../literature.d/LIT-1676.md), arXiv 2510.11349v2, §§II–V
(pp. 1–4) and §IX (p. 7); read in [NOTE-1214](../notes.d/NOTE-1214.md). Pages are the PDF's.

## What was actually shown

**The measures.** I_A = I_A^max − H_A (eq. 1). The relative information
I_{A|B} = Σ_b p(b) I_{A|b} is the expected information about A after B's value
is learnt (eq. 6). It satisfies I_{A|B} = I_A + I_{A:B} (eq. 7), which is the
Shannon identity H(A|B) = H_A − I(A:B) in this notation.

**The definitions.** "the value of a variable A is a fact when the
probability distribution p(a) is entirely concentrated on one value"
(p. 2). A is a fact relative to B = b when I_{A|b} = I_A^max (eq. 9), and
relative to B when I_{A|B} = I_A^max (eq. 10). So A can be a fact relative
to B without being a fact relative to us: Robert's location is a fact relative
to Mary, or to his smartphone, when we know only that she knows (pp. 2–3).
"B has information about A" means I_{A:B} ≠ 0, "in this general and nonmental
sense" (p. 3).

**Why the relatum is a commutative subalgebra.** In quantum theory the joint
distribution p_ρ(a, b) = tr Π_a Π_b ρ (eq. 12) exists only for commuting
variables, "so only these can simultaneously be a fact according to our
definitions". A commuting collection is a "classical subsystem", and "the
collection of facts relative to A is the perspective associated to A" (p. 3).
A qubit has non-commuting variables, so "we cannot associate a perspective to
a qubit" (p. 4). The authors call this "a novelty with respect to the RQM
literature", whose earlier attempt "to define facts relative to entire quantum
systems" led "either to ambiguities … or to complementary observables being
facts simultaneously" (p. 4). Among the works cited for that attempt is their
own Stable Facts paper.

**Why the relativity iterates.** "Every fact is a relative fact" (p. 3),
because information is stored in physical variables and accessed by other
systems. The joint distribution behind any relative fact is computed from a
state relative to some classical subsystem: "Every quantum state is a quantum
state of a system relative to some classical … system" (p. 4). "When we say
that a variable B has information about another variable A, we are saying that
this is the case relative to us" (p. 7). The authors accept the iteration and
refuse the regress: it arises "only … if one wishes to exit relationality"
(p. 7).

What could have come out otherwise: a definition of relative fact for a whole
quantum system that avoids the ambiguity. The paper argues that none exists
on these definitions, because complementary variables have no joint
distribution.

## What this does not say

- **That the definitions dissolve RQM's problems.** That is the authors'
  claim ("several previous problems … are dissolved", abstract), and it is
  argued in a paragraph each (pp. 4–5).
- **That observers play no role in what counts as a fact.** Facts are graded
  in practice. Something is a fact "when the information is high enough for
  the level of accessible resolution or confidence needed" (p. 3), and the
  paper does not say what sets that level.
- **That the perspective is fixed by the physics.** A system is "a set of
  physical variables, represented … as distinguished operators" (p. 4). Which
  operators are distinguished, and so which subalgebra holds a perspective,
  is assumed. Decoherence is cited for the classical case (§VIII), not
  derived.
- **That a perspective is an observer.** Any commuting set has one, such as
  the spin-z of an electron, "which is clearly not an observer" (p. 4).
- **That relative facts happen only at interactions.** On these definitions a
  relative fact is a property of the joint distribution at any time, and the
  paper says it "allows talk of relative facts also in-between interactions"
  (p. 7). [THEORY-621](THEORY-621.md), from the 2021 chapter, has facts only at interactions.
