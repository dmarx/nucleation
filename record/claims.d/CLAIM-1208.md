---
number: 1208
status: Proposed
formerly:
- CLAIM-tmp01pyt
title: 'Proof relevance turns on later use of evidence'
statement: >-
  In Martin-Löf's type theory a proof may be dropped, writing "A true" for
  "a ∈ A for some a", only where nothing that follows depends on it; so
  whether a record of findings is proof-relevant is settled by whether some
  later step uses a finding's evidence, and not only the fact that it passes
version: 2
history:
- version: 2
  date: '2026-11-26'
  note: >-
    A dated note: the exchange 'Alignment consequences brainstorm' (ChatGPT,
    2026-11-26), A27 §1 and A29 §11 (see the note). No other change.
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
- THEORY-2307
complements:
- CLAIM-949
uses:
- TERM-153
- TERM-154
summary: >-
  Filed from the reading of Martin-Löf 1984 ([THEORY-2307](../theory.d/THEORY-2307.md),
  [NOTE-2419](../notes.d/NOTE-2419.md)) for [LEAD-215](../leads.d/LEAD-215.md). [CLAIM-949](CLAIM-949.md)'s first defeater asks whether
  the record is proof-irrelevant "in the sense that matters"; the book
  supplies the sense: a proof can be suppressed when nothing downstream
  depends on it (p. 33), and cannot be when the conclusion depends on it
  (p. 47). The status reviews that take works out of a claim's grounds
  are a case on the proof-relevant side. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2307 NOTE-2419 CLAIM-949 — Proposed or Skimmed; the reading this rests on and the entries it is stated against -->

# CLAIM-1208: Proof relevance turns on later use of evidence

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
proof is relevant where something later is computed from it. [CLAIM-949](CLAIM-949.md)'s
defeater (a) asks whether the record is proof-irrelevant "in the sense
that matters", that is, whether an entry's passing is ever "carried with,
or checked against, any evidence beyond the entry itself". Read through
the book, the test is whether any later step of the record depends on the
evidence and not only on the fact that an entry passes.

## A case

The record's status reviews meet the test. Under [ADR-058](../decisions.d/ADR-058.md) a work cited in a
claim's `grounds` that the claim turns out not to rest on leaves its
grounds, or becomes corroboration, and the claim's standing is judged
again ([CLAIM-470](CLAIM-470.md)'s history, versions 3 and 5, records two works leaving
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

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U15–A29), use-relative fidelity
<!-- inactive-ok-file: CLAIM-tmp5zt7f TERM-tmp3t5jq — Proposed; filed from the same exchange on 2026-11-26 -->

A27 §1 cites this claim correctly for consolidation: "Evidence can be condensed when subsequent reasoning does not depend on the discarded construction." A29 §11 generalizes it: "Some later operations depend on the construction establishing a result. Others depend only on the result. The former require more fidelity than the latter. This gives us a potential theory of use-relative representational fidelity." Fidelity is the third of the separate dimensions A proposes ([CLAIM-tmp5zt7f](CLAIM-tmp5zt7f.md)), and this claim is its formal case: a finding may be kept proof-irrelevantly, as "A true", exactly where nothing later uses its evidence. A29 §9's slices (explanatory, justificatory, correction, developmental, historical; [TERM-tmp3t5jq](../terms.d/TERM-tmp3t5jq.md)) are families of later uses, so a finding can be proof-relevant for one slice and not another. An application; no edge. The note is the assistant's (Claude, in this session). No status change.
