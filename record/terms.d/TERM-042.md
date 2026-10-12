---
number: 42
status: Active
formerly:
- TERM-tmpgok7x
title: 'communicative object, as a context-indexed system of empirical constraints over a cover'
version: 1
tags:
- contextuality
- philosophy-of-language
date: '2026-10-10'
line: pragmatic-transport
supersedes:
- TERM-002
summary: >-
  The assistant found [TERM-002](TERM-002.md) vacuous at A125 §2. At the owner's U41
  request ("double click on this") it rewrote the definition at A129 §2.
  The object is the empirical data over a cover, supports or
  distributions with their restrictions. Whether it is compatible on
  overlaps and whether it extends globally are things to find out, not
  part of the definition.
used_by:
- CLAIM-038
- CLAIM-044
- CLAIM-131
- CLAIM-133
- CLAIM-tmpsxsr8
---
<!-- inactive-ok-file: TERM-002 — Superseded; replaced by this entry, and cited as the history it corrects -->
<!-- inactive-ok-file: CLAIM-038 — Proposed; open, and cited as open: the claim is under test, not settled -->

# TERM-042: communicative object, as a context-indexed system of empirical constraints over a cover

## Definition

A129 §2: "**A communicative observational object is a context-indexed system
of empirically admissible local assignments or distributions, equipped with
restriction relationships. Its global realizability is a property to be
investigated, not part of its definition.**"

A129 keeps three structures apart on an observational scenario (X, M, O):

- the event sheaf ℰ, "All mathematically possible local assignments and
  their restrictions";
- the supports S_C ⊆ ℰ(C), "Which assignments are permitted in each
  context";
- the distributions e_C ∈ D(ℰ(C)), "How probability is allocated among
  local assignments".

The object is the family of supports or distributions, one per context,
with their restrictions. "Then a compatible family of local sections
describes a *realization* of the observational object." When the e_C agree
on overlaps, the family is an empirical model in Abramsky and
Brandenburger's sense ([THEORY-012](../theory.d/THEORY-012.md), [LIT-016](../literature.d/LIT-016.md)). Whether they agree is part of
what the data show. Whether the family has a global extension is the open
question.

## Why [TERM-002](TERM-002.md) is superseded

The event presheaf E(U) = ∏_(x∈U) O_x is a sheaf, and the cover covers X.
So any family of sections that agrees on overlaps glues uniquely to an
assignment on X ([CLAIM-131](../claims.d/CLAIM-131.md)). [TERM-002](TERM-002.md)'s "compatible family of local
sections … with no global assignment presupposed" therefore says nothing at
the level of sections. A125 §2 found this: "**In the ordinary event sheaf, a
compatible family of local sections already glues to a global section.**"
The owner answered at U41, "this is good stuff, double click on this", and
A129 §2 made the correction. It is restated at A151 §2, A173, A178 §4.2,
A203 §11 and A218 §6.

The obstruction lives one level up, and it has three grades
([THEORY-012](../theory.d/THEORY-012.md)):

- **Possibilistic (logical).** Some locally admissible section belongs to
  no compatible family of support sections. A compatible family of support
  sections still glues, because the supports form a subpresheaf of a sheaf.
- **Strong.** No compatible family of support sections exists at all: no
  global assignment satisfies every support. This is what A129 calls the
  "possibilistic extension" question. It tests only the strongest grade.
- **Probabilistic.** A compatible family of distributions has no
  nonnegative global distribution whose marginals are the e_C.

Only at the distribution level does a compatible family fail to glue. The
manuscript §3 sentence quoted in [TERM-002](TERM-002.md) had this right: the question arises
"when empirical supports or distributions rule out the resulting global
assignment". The error was in A78's prose and in [TERM-002](TERM-002.md)'s title.

## What it is not

- Not a compatible family of sections of ℰ, which is already a global
  assignment ([CLAIM-131](../claims.d/CLAIM-131.md)).
- Not [TERM-014](TERM-014.md)'s observational equivalence class, which needs a shared space of
  situations. The two coincide when a global realization exists.
- Not restricted to no-signalling data. The definition does not require
  the e_C to agree on overlaps. Language data signal ([CLAIM-038](../claims.d/CLAIM-038.md), [LIT-842](../literature.d/LIT-842.md)),
  and for them Contextuality-by-Default applies ([LIT-777](../literature.d/LIT-777.md)). A129 does not say
  this. Every contextuality measure the record reads, the contextual fraction
  ([LIT-265](../literature.d/LIT-265.md)) among them, needs no-signalling.
- Not one presheaf. A129 leaves the object as "assignments **or**
  distributions". The support presheaf and the distribution presheaf
  D_R∘ℰ are different objects, and a claim stated in this term should say
  which it means.
