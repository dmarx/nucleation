---
number: 110
status: Active
formerly:
- CASE-tmpfusdm
title: 'Two members, one total: a coarse-graining by total output preserves an institution''s performance, its survival and every prediction it makes, and still merges a state in which a member works within the agreed cap with one in which that member works far past it'
version: 1
standing: fictional
kind: construction
tags:
- society-and-governance
- ethics
date: '2026-10-18'
line: distributed-agency
supports:
- CLAIM-348
- CLAIM-405
summary: >-
  A22's Construction C of the exchange of 2026-10-17, "Institutional
  performance versus constituent capability", which A22 proposed and did
  not write out, from A21 §5 and §16; written out here in its smallest
  form. Two members share twelve hours of work. Total output decides the
  institution's performance and its survival, so the total is sufficient
  for every institutional judgment, and the policies (6, 6) and (10, 2)
  have the same total. A member's claim not to work past an agreed cap of
  eight hours tells them apart, so by [CLAIM-350](../claims.d/CLAIM-350.md) no judgment on the
  total recovers it. Fictional by construction; it shows a possibility,
  not how often institutions are like this.
---

# CASE-110: Two members, one total: a coarse-graining by total output preserves an institution's performance, its survival and every prediction it makes, and still merges a state in which a member works within the agreed cap with one in which that member works far past it

## The construction

A22: "Construct a small institutional system with two policies that preserve
the same aggregate performance statistic but distribute opportunities or
burdens differently among members. Demonstrate that the aggregate
representation preserves the institutional performance judgment but not the
relevant member-level evaluation." A21 §16 gave the schema (J_inst(a) =
J_inst(b) and J_i(a) ≠ J_i(b)). This is the smallest version.

- **States.** An institution has two members. A state is x = (w₁, w₂), the
  hours each works in a period, with w₁, w₂ ∈ {0, 1, …, 12}. Each hour
  produces one unit.
- **The institution's coarse description.** C(x) = w₁ + w₂, total output.
- **The institution's judgments.** Performance is adequate when output
  reaches the quota: J_inst(x) = [w₁ + w₂ ≥ 12]. The institution survives
  to the next period exactly when its performance is adequate: S(x) =
  J_inst(x).
- **A member's claim.** The members agreed a cap of eight hours. Member 1's
  claim is respected when w₁ ≤ 8: J₁(x) = [w₁ ≤ 8].
- **Two policies.** a sets x_a = (6, 6). b sets x_b = (10, 2).

## What it shows

1. **C preserves every institutional judgment.** J_inst and S are functions
   of w₁ + w₂, so each is constant on C's fibres and factors through C
   ([CLAIM-350](../claims.d/CLAIM-350.md)). Any prediction of the institution's future that runs
   through its output runs through C. By stability, prediction and
   aggregate performance, C is a complete description of this institution.
2. **C merges states the member's claim distinguishes.** C(x_a) = C(x_b) =
   12, while J₁(x_a) = 1 and J₁(x_b) = 0. J₁ is not constant on the fibre
   C = 12, so by [CLAIM-350](../claims.d/CLAIM-350.md) there is no j with J₁ = j∘C. No judgment
   made on total output can say whether member 1's claim was respected.
3. **The adequate description is fixed by the target.** C′(x) = (w₁ + w₂,
   [w₁ ≤ 8], [w₂ ≤ 8]) preserves J_inst, S and both members' claims. The
   identity preserves everything. So the failure is not that no
   coarse-graining works. It is that the one chosen because it serves the
   institution does not serve the member.
4. **Nothing at the institution's level registers the difference.** Both
   policies meet the quota and the institution survives under both. The
   difference lies in a distinction the institutional description has
   discarded.

## What it does not show

- **Which policy is right.** That member 1's claim should prevail is a
  normative premise built into J₁, not shown. A21: "the evaluative target
  must not be justified solely by the coarse-graining that preserves it."
  The construction does not justify J₁ either.
- **That institutions in fact discard such distinctions,** or how often.
- **A22's optional extension**, a collective judgment rule that changes
  which evaluations acquire institutional authority. A22 marks it "an
  interpretive extension concerning institutional legitimacy", and it is
  not built here. It is where [CLAIM-271](../claims.d/CLAIM-271.md) and [THEORY-127](../theory.d/THEORY-127.md) would enter.
- **Anything a richer institution could not repair.** An institution whose
  survival depends on member 1's continued membership, and member 1's on
  the cap, would make J₁ bear on S. Then C would no longer be sufficient for
  survival. The construction depends on the claim being idle for the
  institution's persistence, which is [CLAIM-060](../claims.d/CLAIM-060.md)'s case.
