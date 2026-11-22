---
status: Active
status_note: >-
  read in full 2026-11-22 ([NOTE-tmp16xnt](../notes.d/NOTE-tmp16xnt.md)), from the arXiv
  copy. Worth reading as a short, rigorous treatment of the value of
  information and its (non)concavity: it checks the Radner–Stiglitz
  nonconcavity that [CLAIM-572](../claims.d/CLAIM-572.md) cites as unverified and shows the
  nonconcavity to be an artifact of how the amount of information is
  measured. Registered and read for LEAD-145.
title: 'Call the Dentist! A (Con-)Cavity in the Value of Information'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Registered and read in one pass for LEAD-145, from arXiv 2404.01190v1
    (submitted 1 April 2024, the only version), fetched 2026-11-22; text
    extracted with `pdftotext -layout`. Citation checked against the arXiv
    API. `published:` is the arXiv v1 date (ADR-002). Author Mark
    Whitmeyer (Arizona State University). Through it the Radner–Stiglitz
    citation of CLAIM-572 is checked: Radner, R. & Stiglitz, J. (1984), "A
    nonconcavity in the value of information", Bayesian Models in Economic
    Theory, 5:33–52. Not checked against the Anthology of the SOTA. The
    summary is written from the text.
tags:
- information-theory
- mathematics
- epistemology
date: '2026-11-22'
published: '2024-04-01'
arxiv: '2404.01190'
first_author: 'Whitmeyer'
keywords:
- 'value of information'
- 'nonconcavity'
- 'Radner-Stiglitz'
- 'Bayesian persuasion'
- 'convex divergence'
- 'rational inattention'
- 'max-min expected utility'
implementations: []
summary: >-
  Whitmeyer (2024). The classical nonconcavity of the value of information
  — that its marginal value at zero can be zero, so small amounts are
  worthless — "originates with Radner and Stiglitz (1984)". The reason:
  with finitely many undominated actions, the beliefs at which an action
  is optimal form a convex body, so for a prior in the interior, "any
  information that does not move the prior much is worthless." Whitmeyer
  argues the nonconcavity depends on how the amount of information is
  measured. Quantifying the amount by a convex divergence of the
  posterior and selecting the *efficient* (optimal) experiment of each
  amount, the value of information is concave with strictly positive
  marginal value at zero (Prop. 2.3–Cor. 2.4); selecting the *worst*
  experiment of each amount, it is almost never concave (Prop. 2.6); and a
  max-min decision-maker's value of information is concave too (Prop. 3.3).
---


# LIT-tmpkun97: Call the Dentist! A (Con-)Cavity in the Value of Information

Whitmeyer, M. (2024). Call the Dentist! A (Con-)Cavity in the Value of Information. arXiv:2404.01190.

## Key takeaways

- The Radner–Stiglitz (1984) nonconcavity — marginal value of information
  zero at zero — holds because the belief regions on which an action is
  optimal are convex bodies with non-empty interior.
- Whether the value of information is concave in its "amount" depends on how
  the amount is measured and which experiment of a given amount is chosen.
- Under a convex-divergence measure and *efficient* acquisition, the value
  of information is concave and its marginal value at zero is strictly
  positive (Prop. 2.3, Cor. 2.4).
- Under *inefficient/adversarial* acquisition it is almost never concave
  (Prop. 2.6); for a max-min decision-maker it is concave (Prop. 3.3).

## Standing in the record

Registered and read under LEAD-145 as a standard treatment of the value of
information. It verifies the Radner–Stiglitz nonconcavity that
[CLAIM-572](../claims.d/CLAIM-572.md) names as an unchecked citation, and reframes it: the
nonconcavity is a property of the chosen quantification, not of the value
of information itself ([NOTE-tmp16xnt](../notes.d/NOTE-tmp16xnt.md)).
