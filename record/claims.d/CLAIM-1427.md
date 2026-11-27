---
number: 1427
status: Proposed
formerly:
- CLAIM-tmpnf6q4
title: 'A condensation is correction-safe only if no correction separates what it merges'
statement: >-
  For a declared family of queries and of corrections, each a map on
  records, a condensation can be kept in place of the records it condenses,
  answering every query after every sequence of corrections applied to the
  condensed form, exactly when it never merges two records that some
  sequence of those corrections, followed by some query, tells apart; the
  least condensation that is safe is the quotient by the largest such
  indistinguishability, so a condensation that preserves every present
  consequence, as logical forgetting does, is unsafe whenever two records
  agree now and a declared correction separates them
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A condensation, a query family and a correction family, all as defined
  here, for which corrected condensed forms answer every query as the
  corrected originals would and yet two merged records are told apart by
  some sequence of corrections and a query, or the converse; that is, an
  error in the derivation. A showing that the record's corrections are not
  maps on records (that what a correction does depends on more than the
  record it is applied to) would leave the derivation standing and its
  application unmade.
tags:
- logic
- mathematics
- databases
date: '2026-11-26'
line:
- records-of-inquiry
- formal-apparatus
bears_on:
- QUESTION-105
- QUESTION-552
summary: >-
  The assistant's fill for a gap in A29 §§10–11 of the exchange "Alignment
  consequences brainstorm" (ChatGPT, 2026-11-26). A shows by example that
  "Entailment-preserving forgetting is not necessarily correction-preserving
  forgetting" and asks, for a consolidation C and a correction U_δ, that
  C(U_δ(K)) agree on the declared queries with U′_δ(C(K)) for an
  "appropriately" corrected U′, without saying when such a U′ exists. It
  exists exactly when C's merges lie inside the largest congruence for the
  corrections that the queries respect, the Myhill–Nerode construction
  applied to records. A's example, checked by truth tables, is a pair the
  condensation merges and a retraction separates. Checked by brute force
  on 400 random finite systems with python3 -I. It answers [QUESTION-105](../questions.d/QUESTION-105.md)
  for deterministic correction families at zero tolerance and leaves its
  information-theoretic form open. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-182 LIT-3307 — Proposed or Deferred; filed from the same exchange on 2026-11-26 -->

# CLAIM-1427: A condensation is correction-safe only if no correction separates what it merges

## The gap

A29 §10 gives the logical sense of forgetting: K′ over a reduced vocabulary
Σ with K ⊨ φ iff K′ ⊨ φ for every φ over Σ. Its example: K = {P, P → Q,
Q → R} and Σ = {Q, R} give K′ = {Q, Q → R}. Then: "What if we subsequently
discover that P was false or unjustified? The condensed representation no
longer contains the original reason for believing Q." A29 §11 asks for
C(U_δ(K)) ≡_Q U′_δ(C(K)), "condensing after correcting the original record
should agree, for a declared family of queries, with appropriately
correcting the condensed record", and leaves "appropriately" undefined.
The gap is when such a U′ exists. [TERM-182](../terms.d/TERM-182.md)'s test of a consolidation
needs the answer.

## The result

Let 𝓡 be a set of records, Q a set of queries (maps from 𝓡 to answers), Δ a
set of corrections (maps U_δ from 𝓡 to 𝓡), and U_w the composite for a word
w over Δ. Call K₁ ~ K₂ when q(U_w K₁) = q(U_w K₂) for every q in Q and every
word w, the empty word included. ~ is the largest equivalence that refines
agreement on Q and is preserved by every U_δ.

Let C map 𝓡 to condensed forms. Say C is **correction-safe** when there are
maps U′_δ on condensed forms and answer maps q′ with
q′(U′_w(C K)) = q(U_w K) for all K, q and w.

**C is correction-safe if and only if C K₁ = C K₂ implies K₁ ~ K₂.**

*Only if.* If C K₁ = C K₂, then for every q and w,
q(U_w K₁) = q′(U′_w(C K₁)) = q′(U′_w(C K₂)) = q(U_w K₂).

*If.* Fix for each condensed form c one record K_c with C K_c = c. Set
q′(c) = q(K_c) and U′_δ(c) = C(U_δ K_c). If C K = c then K ~ K_c, since C
merges only ~-equivalent records. By induction on w, U′_w(C K) = C(K_w)
for some K_w ~ U_w K: the empty word is K_w = K; and if it holds for w,
U′_δ(C K_w) = C(U_δ K*) with K* ~ K_w ~ U_w K, so U_δ K* ~ U_{wδ} K, ~
being preserved by U_δ (if K₁ ~ K₂ then U_δ K₁ ~ U_δ K₂, since every word
after δ is a word). Then q′(U′_w(C K)) = q′(C K_w) = q(K_c) for the chosen
K_c with C K_c = C K_w, so K_c ~ K_w ~ U_w K, and ~ refines agreement on Q,
so this is q(U_w K).

So the least correction-safe condensation is the quotient 𝓡/~, and any
coarser one fails. It is the Myhill–Nerode construction, records as states
and corrections as inputs.

## A's example, checked

K₁ = {P, P → Q, Q → R} and K₂ = {Q, Q → R}. Over Σ = {Q, R} they have the
same consequences: each has the single model Q = R = 1 on Σ. So logical
forgetting of P maps both to K′ = {Q, Q → R}. Let the correction be the
retraction of the base item P (it removes P where present). After it, K₁
becomes {P → Q, Q → R}, which does not entail Q; K₂ is unchanged and does.
So K₁ ≁ K₂ for the query "is Q entailed?", and by the result no correction
of K′ alone can answer both. Checked with `python3 -I` by truth tables.

## The check

A brute-force search over 400 random systems (2 to 4 records, 1 or 2
corrections, a two-valued query, a random C) compared the condition with a
direct search for maps U′ and q′; they agreed in all 400. The script is in
the filing session's scratchpad; it enumerates every choice of U′ on C's
image and checks q′ for consistency over all reachable pairs.

## What it settles and what it leaves

- **[QUESTION-105](../questions.d/QUESTION-105.md)** asks for the least an inquiry must retain to support a
  family of revisions. For a declared deterministic family at zero
  tolerance, the answer is 𝓡/~: what must be kept is exactly what some
  sequence of declared corrections could later make visible to a query.
  Its information-theoretic form, with tolerance ε and I(H; M), is open.
- **Declared corrections only.** A correction not in Δ can separate records
  C merged. If Δ includes the retraction of each base item and Q can see
  the effect, few merges are safe; [CLAIM-294](CLAIM-294.md) is the case of a single
  marginal belief. A29 VIII's "developmental root set" is the same limit:
  no condensation is safe against corrections nobody has declared.
- **Logical forgetting** (LETHE, [LIT-3307](../literature.d/LIT-3307.md), unread) preserves Q for the
  empty word only. It is correction-safe when no declared correction
  reaches the forgotten vocabulary.
