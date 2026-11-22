---
status: Proposed
title: 'In Freeman and Pfenning''s refinement types, checking a term against a type given in advance moves nothing: an annotation is accepted only when the refinement inferred for the term already lies below it, and a term that fails it is not given that type and is left for the programmer to change; so whether an annotation describes the term or requires something of it is settled by whether the term already passes, not by whether its type was inferred or checked'
version: 1
role: counter
warrant: interpretive
defeated_if: >-
  A rule of the paper, or of the system it describes, that changes a term,
  inserts a coercion or otherwise moves a term to fit a refinement type it
  failed; or a reading of the paper in which an annotation can be
  accepted for a term whose inferred refinement does not lie below it.
  A bidirectional system in which checking does more than accept or reject
  would not defeat this claim, which is about this paper's system; it
  would restore the correspondence it objects to for that system.
tags:
- logic
- philosophy-of-language
- software-engineering
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
objects_to:
- CLAIM-tmpnookt
grounds:
- THEORY-tmp1mruk
uses:
- TERM-tmp8b1yl
- TERM-134
summary: >-
  Filed from the reading of Freeman and Pfenning ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md), [NOTE-tmpew427](../notes.d/NOTE-tmpew427.md)) for
  [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md), answering its question of what is inferred and what is
  checked. It objects to one correspondence of [CLAIM-tmpnookt](CLAIM-tmpnookt.md), the
  direction of fit as bidirectional typing's split between inferring a type
  and checking a term against one given, for the one refinement system the
  record has read: there checking is word to world, as inference is. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmp1mruk CLAIM-tmpnookt TERM-tmp8b1yl TERM-134 CLAIM-tmpmk056 — Proposed; the reading this rests on, the claim it objects to, and the terms and claim it is stated against -->

# CLAIM-tmp764wb: In Freeman and Pfenning's refinement types, checking a term against a type given in advance moves nothing: an annotation is accepted only when the refinement inferred for the term already lies below it, and a term that fails it is not given that type and is left for the programmer to change; so whether an annotation describes the term or requires something of it is settled by whether the term already passes, not by whether its type was inferred or checked

## The claim

[CLAIM-tmpnookt](CLAIM-tmpnookt.md) reads the direction of fit ([TERM-tmp8b1yl](../terms.d/TERM-tmp8b1yl.md)) as the split in
bidirectional typing: inference reads a type off a term (word to world, a
descriptor), checking holds a term to a type given in advance (world to
word, a requirement), and the move that makes a term fit is elaboration.

In Freeman and Pfenning's system ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md)), refinement types "will be
inferred and printed by type inference, or can be used by the programmer
to annotate expressions" (p. 3). The only rule for an annotation is
RESTRICT (Figure 2, p. 8): (e : D′) has type D′ when e has the inferred
type D and D ≤ D′. So an annotation is accepted exactly when the term
already passes it, which makes it a descriptor ([TERM-134](../terms.d/TERM-134.md)). A term that
fails has no derivation at that type. No rule changes a term: "we do not
extend the language of programs for ML (only the language of types)"
(p. 1). The change that would make the term pass is the programmer's,
outside the system.

So in this system both modes ask the same thing, whether the term as it
stands fits a type, and differ only in who wrote the type. Whether an
annotation is a description or a requirement is settled by the term when
the annotation is written, which is [TERM-tmp8b1yl](../terms.d/TERM-tmp8b1yl.md)'s own criterion, and
not by the mode. Requirement, the world-to-word direction, appears only
when the term fails and someone changes it; that is [CLAIM-tmpmk056](CLAIM-tmpmk056.md)'s
performative update, and it is outside the type system.

## What it does not say

- Not that the correspondence fails for bidirectional systems. This paper
  is not one; whether checking there does anything that would count as
  fitting a term to a type is for the lead's reading of Dunfield and
  Krishnaswami ([LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md)).
- Not that type checking never imposes. A programmer who writes an
  annotation the code does not yet meet, and then changes the code, is
  using the type as a requirement; the claim is that the checker's part
  in that is the same as in describing.

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-tmp01mu6 CLAIM-tmpcmt21 — Proposed; filed from the reading for LEAD-tmp3xevc -->

A second system where the same holds (parallel; this claim is about
Freeman and Pfenning's system, so the reading is not evidence for it and
takes no edge). In liquid types (THEORY-tmp01mu6; NOTE-tmpnd1kd), a
predicate refinement system whose paper cites Freeman and Pfenning as the
origin of refinements (p. 169), types given in advance are checked
through the same subtyping constraints as inferred ones, a program with no
type gets Failure (Theorem 2, p. 166), and no rule changes a program.
CLAIM-tmpcmt21 widens this claim to that system and adds what it could not
say: there a failure to check need not be the term's, since the qualifier
set or the conservative checker may be at fault (p. 160). The claim
stands.
