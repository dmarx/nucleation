---
status: Active
title: 'The parity triangle with uniform weights: a no-signalling, strongly contextual model beside a family of point sections that glues'
version: 1
standing: stipulated
tags:
- contextuality
- mathematics
date: '2026-10-10'
line: pragmatic-transport
illustrates:
- CLAIM-tmp2xpga
- CLAIM-037
- CLAIM-105
variant_of:
- CASE-035
summary: >-
  [CASE-035](CASE-035.md)'s constraints given probabilities, at A129 §2, and set beside a
  deterministic family on the same cover that glues to (0, 1, 0). It
  shows that the obstruction is in the supports, not in the event sheaf.
  It appears three times (A129 §2, A161, A178's negative control), so it
  gets a code.
---
<!-- inactive-ok-file: CLAIM-037 CLAIM-105 CLAIM-009 — Proposed; open, and cited as open: the claim is under test, not settled -->
<!-- inactive-ok-file: THEORY-165 — Proposed; continuity of the contextual fraction, cited for what it implies here, not as settled -->

# CASE-tmpg6rwh: The parity triangle with uniform weights: a no-signalling, strongly contextual model beside a family of point sections that glues

## The case

A129 §2, on X = {A, B, C} with the cover {AB, BC, AC} and binary outcomes:

- The supports are S_AB = S_BC = {(0,0), (1,1)} and S_AC = {(0,1), (1,0)}.
  These are [CASE-035](CASE-035.md)'s constraints (S = M, M = H, H ≠ S) under new letters.
- Each allowed outcome has probability 1/2: "if each context assigns
  probability 1/2 to both allowed outcomes, the marginal of each individual
  observable is uniform across its two contexts. Thus these local
  probability distributions are overlap-consistent." So the model is
  no-signalling.
- "Yet no global assignment satisfies all three support conditions",
  because A = B = C contradicts A ≠ C. The model is strongly contextual, and
  its contextual fraction is 1.
- Beside it, the point sections s_AB = (A=0, B=1), s_BC = (B=1, C=0) and
  s_AC = (A=0, C=0) agree on overlaps and "glue uniquely to
  s_X=(A=0,B=1,C=0)".

The same model returns twice. A161: "In the three-context parity example,
replacing each deterministic assignment with a probability distribution
does not produce a nonnegative global joint distribution matching the
specified pairwise laws." A178 §7 uses it as a negative control: "Pairwise
consistent binary empirical distributions may lack a nonnegative global
joint extension."

## What it can show

That the obstruction is in the supports, not in the event sheaf
([CLAIM-tmp2xpga](../claims.d/CLAIM-tmp2xpga.md)): the same cover carries a family of point sections that glues
and a family of supports that admits no global assignment. It makes
[CLAIM-037](../claims.d/CLAIM-037.md)'s failure of global extension concrete for a model that does not
signal.

It also gives the pair [CLAIM-105](../claims.d/CLAIM-105.md) lost. This is the reader's own addition
(R1), not the exchange's. Change S_AC to {(0,0), (1,1)}, still at 1/2 each.
Two of the three contexts are unchanged, and so is every single-observable
marginal. The new model has the global distribution that puts 1/2 on
(0,0,0) and 1/2 on (1,1,1), so its contextual fraction is 0. The fraction
falls from 1 to 0 within one scenario. The two AC tables have disjoint
supports, a total-variation distance of 1 in one context, so the jump is
consistent with [THEORY-165](../theory.d/THEORY-165.md)'s Lipschitz bound.

## What it cannot show

That pragmatic judgements behave this way ([CLAIM-009](../claims.d/CLAIM-009.md)). The weights are
stipulated, as [CASE-035](CASE-035.md)'s constraints are: "This parity example demonstrates
an obstruction, not a claim about actual judgments." It also cannot show
anything about the possibilistic grade between the two: a model with a
locally possible section that extends to no global assignment, while other
sections do, is a different case.
