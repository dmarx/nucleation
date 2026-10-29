---
number: 346
status: Active
formerly:
- CLAIM-tmp442x9
title: 'Feasibility, aggregation and epistemic coordination are independent obstructions to an organization''s realizing its demands: each can occur with the other two absent'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A flaw in one of the three constructions: that the two-objective case
  hides an aggregation or information failure, that the Condorcet profile
  hides an infeasibility of the constituents' own acceptance conditions,
  or that some protocol guarantees coordinated attack over a channel that
  can lose any message. Not defeated by recoding one obstruction as
  another with different demands, for example by adding a demand on the
  procedure itself, which the body states and the claim excludes.
tags:
- society-and-governance
- mathematics
- epistemology
date: '2026-10-18'
line:
- distributed-agency
- formal-apparatus
grounds:
- THEORY-027
complements:
- CLAIM-368
- CLAIM-353
- CLAIM-449
uses:
- TERM-060
summary: >-
  Owner-seeded, U36 of the exchange of 2026-10-17: Arrow's theorem, then
  cryptography and "the two generals problem". A36 placed them: "Arrow's
  theorem belongs in the theory of endorsement, not directly in the
  geometry of feasible updates", and the two generals add "epistemic
  frustration". Three elementary constructions, each with one obstruction
  and not the others, are given in the body. The sharp edge: the
  independence is relative to fixing the demands as the constituents' own
  acceptance conditions; that no remedy for one removes another is A36's
  further reading, argued in the body and not part of the claim.
---

# CLAIM-346: Feasibility, aggregation and epistemic coordination are independent obstructions to an organization's realizing its demands: each can occur with the other two absent

## The claim

The owner, at U36, on the residual of A35: "your account of frustration
measured relative to options for an update to meet or fail requirements
has me wondering if Arrow's Impossibility Theorem might be useful to us."
And: "Maybe also cryptography? Reminds me of the two generals problem." A36
relocated Arrow ("I would locate it slightly differently from the
frustration residual") and drew a table of three obstructions:

- **Feasibility:** no admissible transformation lies in every
  constituent's acceptance set ([TERM-060](../terms.d/TERM-060.md)).
- **Aggregation:** the organization's rule for combining constituents'
  rankings of the admissible transformations yields no coherent choice:
  under pairwise majority, an alternative that no other beats.
- **Epistemic coordination:** an admissible, unanimously preferred joint
  action cannot be guaranteed under the participants' information and
  communication constraints.

Each can occur without the other two.

## The three constructions

**1. Feasibility alone.** [CASE-115](../cases.d/CASE-115.md): two operators share one parameter
θ, with demands L₁ = (θ − 1)² < 1 and L₂ = (θ + 1)² < 1. Since L₁ + L₂ =
2θ² + 2 ≥ 2, no θ meets both. Everything is known to both, and nothing is
communicated. The aggregation is coherent: with two operators, pairwise
majority strictly prefers x to y only when both do, which is the Pareto
relation, and it is acyclic, so on any finite menu of updates some update
is unbeaten. A36: "A system can have no common improving update and still
have a perfectly coherent rule for choosing among compromises."

**2. Aggregation alone.** A36 §2A's profile: operators 1, 2, 3 rank
updates A, B, C as A ≻ B ≻ C, B ≻ C ≻ A and C ≻ A ≻ B. Each operator's
acceptance condition is that the update be one of A, B, C, so all three
lie in every acceptance set and the demands are jointly realizable.
Pairwise majority prefers A to B, B to C and C to A (two to one each
time), so every option is beaten and the rule yields no choice.
Information is complete and the operators share one site.

**3. Epistemic coordination alone.** Only operator 1 learns whether the
moment to act has come. Both rank "act together when it has, and neither
act otherwise" above every other outcome, and acting together is
admissible. The only channel between them can lose any message. The
coordinated attack result (Akkoyunlu et al. (1975); Halpern and Moses
(1990) in terms of common knowledge) says no protocol guarantees that both
act or neither does while also acting in some run. The argument, in brief:
take a run in which the moment has come, every message is delivered and
both act, with k messages delivered before acting. Remove the last
delivered message. Its sender cannot tell the two runs apart, so it still
acts, and so, to keep agreement, must the other. Repeat k times to reach a
run with no message delivered in which both act. Operator 2's view in that
run is the same as in the run where the moment has not come and nothing is
delivered, in which neither may act; so operator 2 acts there too, which
the protocol forbids. There is no infeasibility and no disagreement to
aggregate.

## A36's further reading, not part of the claim

A36 §5: "Some obstructions are not interchangeable, and some cannot be
eliminated by additional computing power. For example, more accurate
gradients do not resolve a genuine conflict of authority. A better voting
rule cannot make an infeasible combination of objectives achievable. And
better encryption does not overcome an unreliable channel's lack of
guaranteed delivery." That no remedy for one obstruction removes another is
argued from the independence, not shown by it: a remedy might act on two
at once. It is interpretive and held here as A36's.

Two points bear on it.

- **Information escapes Arrow but not every aggregation failure.** A36
  §2D read Sen ([NOTE-263](../notes.d/NOTE-263.md)) as saying the dual mapping model should
  "explicitly represent which kinds of information endorsement procedures
  may use", since interpersonal comparability breaks Arrow's
  impossibility. [THEORY-027](../theory.d/THEORY-027.md) shows a failure it does not break: decisive
  jurisdiction for two constituents, weak Pareto and an unrestricted
  domain conflict "even when choice need only yield a best element", and
  comparability does not remove it. That is [CLAIM-353](CLAIM-353.md).
- **Commitments fix timing only.** A36 §4: a cryptographic commitment
  solves "the timing and integrity of the prediction", not the scoring,
  which is [CLAIM-340](CLAIM-340.md).

A36 also named Arrow's theorem (Arrow (1950)): with three or more
alternatives and an unrestricted domain, no rule gives a complete
transitive social ordering satisfying weak Pareto, independence of
irrelevant alternatives and nondictatorship. Construction 2 is its
standard witness, not its proof. The record holds Arrow only through Sen
([NOTE-263](../notes.d/NOTE-263.md)) and O'Donnell's Fourier proof ([LIT-346](../literature.d/LIT-346.md)).

## What it does not say

- **That the three are independent under every choice of demands.** An
  aggregation failure can be recoded as a feasibility failure by adding a
  demand on the procedure, "the choice is beaten by no majority", which no
  option meets in construction 2. The independence holds when the demands
  are the constituents' own acceptance conditions and the procedure is
  held separately, as A37 recommended: "treat the selection of one actual
  action as a separate governance operation."
- **That they do not interact.** A36: "They can reinforce each other, but
  they are analytically independent."
- **That the operators are agents with rights.** A36: "Network modules
  aren't automatically moral agents, and their optimization preferences
  are not equivalent to individual rights."

## Note of 2026-10-29: Halpern and Moses, read

Halpern and Moses, [LIT-1213](../literature.d/LIT-1213.md), is now read ([NOTE-1381](../notes.d/NOTE-1381.md)). Construction 3's
argument is their informal induction of §4 and the formal one of Theorem
5. Two precisions.

- **The right result.** The construction demands "both act or neither
  does", with no simultaneity. That is their Proposition 10's eventual
  case, with Theorem 9, not Corollary 6's simultaneous one. Both hold over
  a lossy channel, so the construction is covered, but the citation should
  be Proposition 10 with Theorem 9.
- **The attribution.** The paper credits the problem to Gray (1978) and
  cites Gallager (1979) and Yemini and Cohen (1979) for proofs. It does not
  cite Akkoyunlu, Ekanadham and Huber (1975), [LIT-1214](../literature.d/LIT-1214.md), which the record
  files as the standard first source. The 1975 attribution above rests on
  later usage, not on this paper. [LIT-1214](../literature.d/LIT-1214.md) is Unfetched, so it has not
  been checked.

Their Theorem 8 strengthens the obstruction: unreliable channels are not
needed, since any uncertainty in timing blocks common knowledge and with
it any guaranteed simultaneous action. The claim is unchanged.

## Note of 2026-10-29: Akkoyunlu, Ekanadham and Huber, read

Akkoyunlu, Ekanadham and Huber, LIT-1214, which the note above calls
Unfetched, is now read (NOTE-tmpsfusn). They do state the problem. Their
Appendix tells it as two groups of gangsters and a messenger who may be
mugged on any trip, with a goal that the plan is delivered and that "both
parties know that they are in mutual agreement" that it was, and proves by
a shortest-sequence argument that no finite exchange reaches it: "The
sequence is infinite even when none of the messages are actually lost."
So the body's citation of Akkoyunlu et al. (1975) is right as to priority
over Gray (1978). This corrects the note above, which said the 1975
attribution rests on later usage: it rests on the paper. One precision.
Their goal is mutual knowledge of delivery, with action only as motive,
so the step from it to "no protocol guarantees that both act or neither
does" is Halpern and Moses's (LIT-1213), not theirs. The claim is
unchanged.
