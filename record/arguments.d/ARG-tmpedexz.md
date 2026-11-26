---
status: Proposed
title: 'The filing rule, generalized from admission to availability, prices an entry''s tier'
statement: >-
  The cost accounting by which the record prices filing an argument, with
  the recognition cost that grows with the store, generalizes to the choice
  of how readily a kept entry is reached, provided the attention an entry
  costs is priced over the working corpus and not entry by entry; the
  per-entry form holds only where that cost is additive over entries
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed 2026-11-26 by the assistant, with the claim it argues, from the
    exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26).
form: generalization
rests_on:
- CLAIM-303
- CLAIM-314
concludes:
- CLAIM-tmpg2wk1
tags:
- databases
- operations-research
date: '2026-11-26'
line:
- records-of-inquiry
- nucleating-argument
summary: >-
  A27 §7 of the exchange "Alignment consequences brainstorm" extends
  [CLAIM-303](../claims.d/CLAIM-303.md)'s pricing of filing to a per-entry cost of each availability
  tier ([CLAIM-tmpg2wk1](../claims.d/CLAIM-tmpg2wk1.md)). The generalization holds for maintenance,
  reactivation, unavailability and transition, which are the entry's own;
  it fails for retrieval noise, which [CLAIM-314](../claims.d/CLAIM-314.md) makes a property of the
  corpus. Supported in the narrowed form, with the noise term taken over
  the hot set. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpg2wk1 CLAIM-314 — Proposed; the claim this argues and the held premise that narrows it -->

# ARG-tmpedexz: The filing rule, generalized from admission to availability, prices an entry's tier

## The inference

Premises: [CLAIM-303](../claims.d/CLAIM-303.md) (Active), filing is worth it only when expected
reuse covers the cost of filing, indexing, tracking dependencies and
checking currency; [CLAIM-314](../claims.d/CLAIM-314.md) (Proposed), reusing a filed argument has a
recognition cost that grows with the store, so per-item decisions are not
independent. Conclusion ([CLAIM-tmpg2wk1](../claims.d/CLAIM-tmpg2wk1.md)): a tier can be chosen by a cost
over a horizon, with the terms A27 §7 lists.

## Critical questions

1. **Are the cases representative?** [CLAIM-303](../claims.d/CLAIM-303.md) prices one decision, file
   or not, at the time of filing. A tier is chosen repeatedly over an
   entry's life and can be reversed. The terms carry over (maintenance is
   [CLAIM-303](../claims.d/CLAIM-303.md)'s "checking it is still current"; reactivation is its
   reconstruction), and two are added, unavailability and transition, that
   a one-shot filing decision does not need. The generalization is to a
   larger decision, not a different one.
2. **Is there a counterexample?** Yes, to the per-entry form. Take two
   entries that restate one principle. Each alone in default retrieval
   adds little noise; both together make each other's hits redundant, so
   the noise of either depends on whether the other is hot. No assignment
   of a fixed noise cost to each entry reproduces that, and a per-entry
   minimization can keep both hot when keeping one is cheaper. [CLAIM-314](../claims.d/CLAIM-314.md)'s
   growth of recognition cost with the store is the general form of the
   same dependence.
3. **Is the feature constitutive or merely common?** That kept work must be
   paid for by what it saves is constitutive of both [CLAIM-303](../claims.d/CLAIM-303.md) and the
   tier rule. That the payment can be computed entry by entry is not.

Verdict: supported in the narrowed form. The tier rule generalizes
[CLAIM-303](../claims.d/CLAIM-303.md) when retrieval noise is priced over the hot set as a whole; the
per-entry J_e(k) is the special case of additive noise.
