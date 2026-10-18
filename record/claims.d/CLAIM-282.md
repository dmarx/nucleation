---
number: 282
status: Active
formerly:
- CLAIM-tmppy0ey
title: 'Forbidding self-endorsement does not stop an operator from amplifying its own authority: once endorsement can carry authority more than one hop, reciprocal and cyclic endorsements recycle it, and only one-hop allocation within an epoch makes an operator''s authority independent of its own endorsements'
version: 1
role: granted
warrant: demonstrated
tags:
- self-governance
- social-ontology
date: '2026-10-13'
works:
- self-as-recursive-ecology
line:
- distributed-agency
- formal-apparatus
summary: >-
  A2's own analysis of the owner's U2 design, conceded in the exchange
  and checked here. With damped recursive delegation (a PageRank-like
  fixed point), two operators that endorse each other pass authority back
  and forth, so each one's authority depends on its own outgoing
  endorsements even though neither endorses itself. With one-hop
  allocation from budgets fixed independently of outgoing endorsements,
  that dependence is exactly zero. No accounting rule removes the slower
  route: an operator can change its authority by changing what others
  endorse.
complements:
- CLAIM-277
supports:
- CLAIM-285
- CLAIM-tmpp9ox0
illustrated_by:
- CASE-077
---
<!-- inactive-ok-file: CLAIM-277 CLAIM-285 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# CLAIM-282: Forbidding self-endorsement does not stop an operator from amplifying its own authority: once endorsement can carry authority more than one hop, reciprocal and cyclic endorsements recycle it, and only one-hop allocation within an epoch makes an operator's authority independent of its own endorsements

## The claim

A2 §5 set up the recursive rule g = (1 − η)b + ηEᵀg, with 0 ≤ η < 1, base
budgets b, a row-stochastic endorsement matrix E and E_ii = 0. Its solution
is g = (1 − η)(I − ηEᵀ)⁻¹b. A2: "Suppose D₁ endorses D₂, and D₂ endorses D₁.
Even though neither endorses itself directly, their reciprocal relationship
can recycle delegated authority between them." And: "The constraint
E_ii = 0 therefore prevents **direct self-endorsement**, but not indirect
amplification."

This is right, and it is a fact about the fixed point, not about any
psychology. In the two-operator case each endorses only the other, so
g₁ = (1 − η)b₁ + ηg₂ and g₂ = (1 − η)b₂ + ηg₁. Then
g₁ = (b₁ + ηb₂)/(1 + η). Operator 1's authority depends on its partner's
endorsement, which returns operator 1's own contribution after two hops.
With more operators, any cycle through i makes g_i depend on E_ij. So the
condition [CLAIM-285](CLAIM-285.md) needs, |∂g_i/∂E_ij| ≈ 0, fails.

A3 §4 gave the case where it holds. Under one-hop allocation,
I_j = I_j⁰ + Σ_{i≠j} b_i E_ij, where the budgets b and baseline I⁰ are fixed
independently of outgoing endorsements. Then I_i depends on what others
endorse and not on E_i·. A3: "For the one-hop aggregation above, this
condition holds exactly if budgets and baseline authority are fixed
independently of outgoing endorsements. Other agents' responses can still
change I_i later." Its proposal: "one-hop authority allocation within a
governance epoch, with endorsements updated between epochs."

A2 also named the route no accounting rule closes: "an agent could
influence its own authority indirectly by causing *other* agents to change
their endorsements. That is a genuine social feedback effect, not an
accounting loop. It cannot be eliminated by cycle prevention alone."

A6 §4 restated the principle for nested organizations, where the
constituents of a higher-level operator legitimately endorse it: "Authority
may circulate, but its accounting cannot multiply through circulation
alone." That calls for tracking where delegated authority came from, not for
banning every return to its source. It is held here as A6's slogan, not as a
result. A2's own path-based rule with origin tags admits it "needs an
explicit convention for the length-zero path and for authority terminated
at cycle boundaries; the total amount of authority actually arriving need
not remain constant under this rule."

## Why it is granted and Active

The record states the limit of the design it files as [CLAIM-285](CLAIM-285.md).
The algebra is elementary and was checked above. It holds whatever any line
concludes, so it carries `formal-apparatus` as a second line ([ADR-040](../decisions.d/ADR-040.md)).

## What it does not say

- It does not say multi-hop delegation is useless. It says multi-hop
  delegation and insensitivity to one's own endorsements cannot both be had
  from cycle bans alone.
- It does not say the slower social route is a defect. A5 and the owner
  hold that durable trust is how authority should arise ([CLAIM-277](CLAIM-277.md)).
  The same route is also how authority is captured.
