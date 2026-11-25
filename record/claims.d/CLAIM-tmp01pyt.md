---
status: Proposed
title: 'In Martin-Löf''s type theory a proof may be dropped, writing "A true" for "a ∈ A for some a", only where nothing that follows depends on it; so whether a record of findings is proof-relevant is settled by whether some later step uses a finding''s evidence, and not only the fact that it passes'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) A reading of the book on which a proof can be
  suppressed even where what follows depends on it, so that dependence is
  not Martin-Löf's criterion. (b) A step in the record that uses a
  finding's evidence and whose outcome would be the same if only the fact
  that the finding passes were kept, so that use without dependence
  counts, and the criterion must be dependence of the outcome, not use.
tags:
- logic
- epistemology
- design-rationale
date: '2026-11-25'
line:
- formal-apparatus
- record-as-apparatus
grounds:
- THEORY-tmp62cvo
complements:
- CLAIM-949
uses:
- TERM-153
- TERM-154
summary: >-
  Filed from the reading of Martin-Löf 1984 (THEORY-tmp62cvo,
  NOTE-tmp60upv) for LEAD-215. CLAIM-949's first defeater asks whether
  the record is proof-irrelevant "in the sense that matters"; the book
  supplies the sense: a proof can be suppressed when nothing downstream
  depends on it (p. 33), and cannot be when the conclusion depends on it
  (p. 47). The status reviews that take works out of a claim's grounds
  are a case on the proof-relevant side. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp62cvo NOTE-tmp60upv CLAIM-949 TERM-153 TERM-154 — Proposed or Skimmed; the reading this rests on and the entries it is stated against -->

# CLAIM-tmp01pyt: In Martin-Löf's type theory a proof may be dropped, writing "A true" for "a ∈ A for some a", only where nothing that follows depends on it; so whether a record of findings is proof-relevant is settled by whether some later step uses a finding's evidence, and not only the fact that it passes

## The claim

Martin-Löf keeps the proof by default and lets it go by abbreviation: "we
write in general A true instead of a ∈ A for some a, when A is thought of
as a proposition and we don't care about what its proof (construction) is"
(p. 33). The abbreviation has a limit. From a proof c of (∃x ∈ A)B(x) the
right projection gives q(c) ∈ B(p(c)), and "in case B(x) depends on x, it
is impossible to suppress the construction in the premiss, since the
conclusion depends on it" (p. 47). Likewise a real number's Cauchy proof
cannot be dropped: "Only by means of the proof q(c) do we know how far to
go for the approximation desired" (p. 54).

So proof relevance is not a property of a whole system but of each use: a
proof is relevant where something later is computed from it. CLAIM-949's
defeater (a) asks whether the record is proof-irrelevant "in the sense
that matters", that is, whether an entry's passing is ever "carried with,
or checked against, any evidence beyond the entry itself". Read through
the book, the test is whether any later step of the record depends on the
evidence and not only on the fact that an entry passes.

## A case

The record's status reviews meet the test. Under ADR-058 a work cited in a
claim's `grounds` that the claim turns out not to rest on leaves its
grounds, or becomes corroboration, and the claim's standing is judged
again (CLAIM-470's history, versions 3 and 5, records two works leaving
its grounds, one of them unread). The review reads the evidence, not the
bare fact that the claim held: two claims that both passed would be
treated differently according to what their grounds contain. There the record is proof-relevant in Martin-Löf's
sense. A reader who only consults a claim's status uses the fact of
passing, "A true", and there it is not.

## What it does not say

- Not that the record's grounds are proofs in the formal sense; the
  analogy is between what is kept and what is computed from it.
- Not that every use of the record is proof-relevant: a status read alone
  is the suppressed form.
- Martin-Löf does not state the criterion in general. He states it for the
  projection rule and the reals; the generalization is the filer's.
