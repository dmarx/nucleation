---
number: 844
status: Active
formerly:
- THEORY-tmpetatd
title: 'A designer who commits to how players are informed, and may condition on the state and on their prior information but cannot choose their actions, can bring about exactly the Bayes correlated equilibria, the joint distributions of states and actions in which no player told his recommended action wants to deviate, a polytope cut out by linear constraints; with one uninformed receiver who would lose 1 by investing in the bad state and gain x < 1 in the good, the most investment attainable is certain investment in the good state and investment with probability x in the bad'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-1034. The characterization is Bergemann and
    Morris's Proposition 1 (proved in their 2016 paper, stated in the
    survey), the example their §3.1 (Kamenica and Gentzkow's). Both
    directions of Proposition 1, the example and its informed-receiver
    extension were re-derived below, and the two-firm case solved by
    linear programming, which meets the condition for Active under
    ADR-047 v2.
tags:
- game-theory
- information-theory
date: '2026-10-21'
source:
- LIT-1313
- LIT-1021
summary: >-
  Bergemann and Morris (2019), [LIT-1313](../literature.d/LIT-1313.md), read in [NOTE-1034](../notes.d/NOTE-1034.md), from
  the accepted manuscript. What control over information alone can
  achieve, among Bayesian players with a common prior, is a set computable
  by linear programming, whoever the designer is, and read
  metaphorically it bounds what any information structure could produce.
  It assumes commitment, a designer who picks the equilibrium, and
  Bayesian players; it says nothing about bounded receivers.
supports:
- CLAIM-404
---
<!-- inactive-ok-file: THEORY-853 — Proposed; filed from the same reading, the incentive order, cited as open -->
<!-- inactive-ok-file: CLAIM-404 — Proposed; filed from the same exchange, the claim this account bears on, cited as open -->

# THEORY-844: A designer who commits to how players are informed, and may condition on the state and on their prior information but cannot choose their actions, can bring about exactly the Bayes correlated equilibria, the joint distributions of states and actions in which no player told his recommended action wants to deviate, a polytope cut out by linear constraints; with one uninformed receiver who would lose 1 by investing in the bad state and gain x < 1 in the good, the most investment attainable is certain investment in the good state and investment with probability x in the bad

## Source

Bergemann and Morris (2019), *Journal of Economic Literature* 57(1),
[LIT-1313](../literature.d/LIT-1313.md), read in [NOTE-1034](../notes.d/NOTE-1034.md) from Cowles Discussion Paper 2075R3:
Definition 1, Proposition 1 (whose proof the survey cites from Bergemann
and Morris 2016a) and §§3.1–3.3. The example is Kamenica and Gentzkow's
(2011), [LIT-1021](../literature.d/LIT-1021.md). The re-derivations are the record's.

## What was actually shown

A decision rule σ(a | t, θ) is **obedient** if for every player i, type
t_i, recommended a_i and alternative a′_i,

Σ_{a₋ᵢ, t₋ᵢ, θ} [u_i((a_i, a₋ᵢ), θ) − u_i((a′_i, a₋ᵢ), θ)] σ((a_i, a₋ᵢ) | t, θ) π(t | θ) ψ(θ) ≥ 0.

**If.** Let the designer draw a ∼ σ(· | t, θ) and tell each player a_i
privately. Given that the others obey, player i of type t_i told a_i
compares a_i with a′_i using exactly the conditional law in the
inequality. So obeying is a Bayes Nash equilibrium that induces σ.

**Only if.** Let a communication rule φ(m | t, θ) and an equilibrium b
induce σ(a | t, θ) = Σ_m φ(m | t, θ) Π_j b_j(a_j | t_j, m_j). Wherever
b_i(a_i | t_i, m_i) > 0, a_i is a best reply to (t_i, m_i). Multiply that
inequality by b_i(a_i | t_i, m_i) and sum over m_i. The result is the
obedience inequality for (t_i, a_i): relabelling messages by the actions
they lead to loses no incentive.

The constraints are linear in σ, so the set is a polytope, and maximizing
any designer objective V(σ) = Σ v(a, θ) σ π ψ over it is a linear program.

**The example.** One receiver, states B and G equally likely, invest pays
−1 in B and x ∈ (0, 1) in G, not investing pays 0. A decision rule is
(p_B, p_G), the investment probabilities. Obedience after "invest" is
½p_B(−1) + ½p_G x ≥ 0, that is p_G ≥ p_B/x. After "not invest" the
constraint is slack because x < 1. So the most investment is p_G = 1,
p_B = x: invest is recommended in the good state always and in the bad
state with probability x, which leaves the receiver exactly indifferent.
Total investment (1 + x)/2, against 0 without information and ½ with full
information.

**Prior information.** If the receiver sees a signal correct with
probability q, the "not invest" constraint for the good signal binds
once q ≥ 1/(1 + x), and with p_B = 0 it gives p_G ≥ q − (1 − q)/x, which
rises to 1 as q → 1. Below 1/(1 + x) the set is the uninformed one. So
prior information shrinks what the designer can do, and only once it
would change the receiver's decision by itself.

**Two receivers**, with ε added if both invest, solved as a linear
program over the full joint rule. For ε > 0 the optimum is public:
p_B = r_B = (x + ε)/(1 − ε) (0.7222 at x = 0.55, ε = 0.1, as the paper
says). For ε < 0 it minimizes joint investment in B. The paper's
p_B = x + ε, r_B = 0 is right when x + ε ≤ ½. For x + ε > ½, which the
paper's own assumption x > ½, |ε| ≤ x − ½ gives, that rule is not a
probability distribution, and the optimum is p_B = x/(1 − 2ε) with
r_B = 2p_B − 1.

What could have failed: an indirect rule with richer messages could have
attained outcomes no recommendation rule can. The "only if" direction
shows it cannot, as long as the designer may pick the equilibrium.

## What this does not say

- **Not when the worst equilibrium is played.** The revelation principle
  then fails, and the attainable set is smaller (§7).
- **Not without commitment.** A designer who chooses messages after seeing
  the state is in cheap talk, which this does not cover.
- **Not for designers who cannot condition on players' types.** §6 gives
  the smaller sets, with and without elicitation.
- **Not for bounded or non-Bayesian receivers.** Obedience is computed
  with Bayes's rule and a common prior.
- **Not that a designer exists.** Read metaphorically the set bounds all
  information structures, with no designer.

## Connections

- **[THEORY-404](THEORY-404.md)** is the one-receiver, no-prior case: concavification and
  BCE give the same optimum in the example.
- **[CLAIM-404](../claims.d/CLAIM-404.md).** Its evidential route has exactly this reach for
  Bayesian procedures. Its evaluative route, changing how evidence is
  weighed, changes u_i, which information design holds fixed.
- **[THEORY-853](THEORY-853.md)** orders information structures by the size of this
  set.
