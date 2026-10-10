---
number: 131
status: Active
formerly:
- CLAIM-tmp2xpga
title: 'A compatible family of sections of the event sheaf always glues, so where a communicative object lacks a global realization the obstruction lies in its supports or distributions, not in the event sheaf'
version: 1
role: granted
tags:
- contextuality
- mathematics
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-012
- LIT-016
complements:
- CLAIM-037
- CLAIM-038
uses:
- TERM-042
summary: >-
  The assistant at A125 §2 and A129 §2, after the owner's U41 "double
  click on this". It is the standard sheaf property of E(U) = ∏ O_x
  (Abramsky and Brandenburger). Granted, because it is elementary; it is
  used against [TERM-002](../terms.d/TERM-002.md)'s wording, not against [CLAIM-038](CLAIM-038.md)'s thesis, which
  version 2 restates to agree with it.
illustrated_by:
- CASE-037
---
<!-- inactive-ok-file: CLAIM-037 CLAIM-038 — Proposed; open, and cited as open: the claim is under test, not settled -->
<!-- inactive-ok-file: THEORY-171 — Proposed; the non-gluing of causal scenarios, cited for the limit it sets on this claim, not as settled -->
<!-- inactive-ok-file: TERM-002 — Superseded; cited as the wording this claim corrects -->

# CLAIM-131: A compatible family of sections of the event sheaf always glues, so where a communicative object lacks a global realization the obstruction lies in its supports or distributions, not in the event sheaf

## The claim

A125 §2: "**In the ordinary event sheaf, a compatible family of local
sections already glues to a global section.** What may fail to possess a
global section is the *empirically constrained structure*: local support
sets or probability distributions may not admit a jointly satisfying global
assignment or distribution."

A129 §2 shows both halves on X = {A, B, C} with the cover {AB, BC, AC}. The
point sections (A=0, B=1), (B=1, C=0) and (A=0, C=0) agree on overlaps, and
"glue uniquely to s_X=(A=0,B=1,C=0)". The parity supports admit no global
assignment, and "The obstruction arises from the empirically constrained
supports, **not from any failure of the event sheaf's gluing axiom**." The
two contrasts are [CASE-037](../cases.d/CASE-037.md).

In Abramsky and Brandenburger's terms ([THEORY-012](../theory.d/THEORY-012.md), [LIT-016](../literature.d/LIT-016.md)), E(U) = ∏_(x∈U) O_x
is a sheaf on the observables. An empirical model is a compatible family of
sections of the distribution presheaf D_R∘ℰ, and that presheaf is not a
sheaf. So the question whether a communicative object ([TERM-042](../terms.d/TERM-042.md)) has
a global realization is a question about its supports or distributions.

Two extension questions follow, as A129 §2 sets them.

- **Over the supports.** Is there s ∈ ℰ(X) with s|_C ∈ S_C for every
  context C?
- **Over the distributions.** Is there p ∈ D(ℰ(X)) with p|_C = e_C for
  every C?

A negative answer to the first gives a negative answer to the second. A
global p would be supported on sections whose restrictions all lie in the
supports. A129: "Failure of the first is a stronger obstruction than failure
of the second."

The claim is used against [TERM-002](../terms.d/TERM-002.md)'s wording, "a compatible family of local
sections … with no global assignment presupposed", which is vacuous for ℰ.
The manuscript §3 already put the obstruction in "empirical supports or
distributions". It complements [CLAIM-037](CLAIM-037.md), which says contextuality is a
failure of global extension, and [CLAIM-038](CLAIM-038.md), whose version 2 is restated in
these terms. Restated at A151 §2, A173, A178 §4.2 ("A compatible family of
unrestricted event assignments glues."), A203 §11 and A218 §6 ("The event
sheaf glues compatible unrestricted local assignments.").

## What it does not say

It does not say that deterministic local data always glue. In causal
measurement scenarios the strategy presheaf is not a sheaf, and
deterministic strategies that are compatible in every context can fail to
glue ([LIT-843](../literature.d/LIT-843.md) Example 7.2; [THEORY-171](../theory.d/THEORY-171.md); [CLAIM-038](CLAIM-038.md), "A further kind of
non-gluing"). The claim is about the flat event sheaf. A129 §5 recommends
that very paper and proposes "a separate causal layer, not a replacement of
the sheaf layer", without noticing that the causal layer can break this
premise.

It also does not grade the obstruction. Abramsky and Brandenburger have
three levels, probabilistic, possibilistic and strong ([THEORY-012](../theory.d/THEORY-012.md)), and
A129's "possibilistic extension" question tests only the strongest. A model
in which some locally admissible section belongs to no compatible family
(possibilistic contextuality, Hardy's kind) passes A129's first question and
fails its second. So A129's two questions do not separate the possibilistic
grade from the probabilistic one.
