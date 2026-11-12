---
status: Proposed
title: 'A demonstrated claim whose argument rests on an explicit construction carries it as a construction case: `grounds` when the construction is what demonstrates the claim, `illustrates` when it is a worked instance of a general proof'
version: 1
tags:
- record
date: '2026-11-12'
summary: >-
  On 2026-11-08 the owner told another assistant, about two claims it had
  proved by explicit constructions, to "make sure you connect the CLAIMs
  using those explicit constructions to CASEs describing them". The
  record has a construction kind of case (ADR-042), with 68 cases of it,
  but on 2026-11-12, 159 of its 221 demonstrated claims had no case
  grounding or illustrating them, and some of those carry a specific
  construction only in their body: CLAIM-571's barrier at 1.3 is one, with
  two variants filed as cases and the example they alter filed as none. A
  construction in a claim's body cannot be cited, varied or reused by
  another entry. The decision: such a construction is filed as a case of
  kind construction, linked by `grounds` when it is what demonstrates the
  claim (an existence or separation claim) and by `illustrates` when the
  claim has a general proof the construction instances; a case that
  grounds a claim gets an ARG of form existence (ADR-061). Taken up at a
  claim's next filing or review, not swept. Applied first to CLAIM-571.
  Rejected: a sweep of all 159 now; leaving constructions in bodies; a
  case for every proof; always `grounds`. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-198 CASE-200 — Proposed; the variants of CLAIM-571's construction, filed as cases before it was -->
<!-- inactive-ok-file: CASE-tmpwln61 ARG-tmpmqot9 — Proposed; this decision's first application -->

# ADR-tmpq0fhi: A demonstrated claim whose argument rests on an explicit construction carries it as a construction case: `grounds` when the construction is what demonstrates the claim, `illustrates` when it is a worked instance of a general proof

## Context

ADR-042 gave CASE a kind, and `construction` is "a formal or
mathematical object built to exhibit or refute a property, whose facts
are its definition". ADR-043 gave CLAIM a warrant, and `demonstrated`
covers support "by proof or construction". Nothing joins the two. A
construction is filed as a case when the filer thinks to, and otherwise
lives in the body of the claim it proves.

On 2026-11-08, in the exchange "Identify Synthesis Opportunities"
(https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), the
owner told the assistant drafting two claims proved by explicit
constructions: "make sure you connect the CLAIMs using those explicit
constructions to CASEs describing them" (U5). The assistant linked them
by `grounds`, because the constructions "establish the claims'
mathematical results" (A14). That instruction was about two claims; this
decision makes it a rule.

The cost of not having it shows in CLAIM-571. Its body builds the
example the readiness and realizability lines reuse, r(q) = 0.7 +
2.4q(1 − q) on [0, 1], a transition with threshold 1.3 between
configurations that each cost 0.7. CASE-198 and CASE-200 alter that
example (a staging architecture, carry-over of a budget), and CASE-200's
title quotes its numbers. But the example itself has no code, so neither
case can say what it is a variant of, and a reader of either has to find
the construction inside a claim.

A count on 2026-11-12: 221 claims are demonstrated, 68 cases are
constructions, and 159 demonstrated claims have no case that grounds or
illustrates them. Many of the 159 are general proofs with no specific
object; how many carry a construction in their body was not counted.

## Decision

1. **A demonstrated claim whose argument uses an explicit construction**
   (a specific object, model or example built to exhibit or refute a
   property) has that construction filed as a CASE of kind
   `construction`, standing `fictional` unless it is a real object.
2. **The link says what the construction does.**
   - `grounds`, when the construction is what demonstrates the claim: an
     existence or separation clause ("need not", "can", "come apart"),
     where one coherent case is the proof. The support is then
     load-bearing, so an ARG of form `existence` carries it (ADR-061).
   - `illustrates`, when the claim has a general proof and the
     construction is a worked instance of it.
3. **Cases that alter a construction name it** by `variant_of`.
4. **Not swept.** The rule applies when a claim is filed, and when an
   existing claim is next revised or reviewed. A review that meets a
   construction in a body files the case then.
5. **The claim's body keeps its proof.** The case holds the object; the
   claim says what it shows.

## Alternatives considered

- **Sweep all 159 now.** Most are general proofs with nothing to file,
  and telling which are not means reading each. The sweep is a review of
  its own; taking them as they come costs little.
- **Leave constructions in bodies.** Then a variant cannot name what it
  varies, a construction used by two claims is stated twice, and the
  cases view under-reports what the record has built.
- **A case for every demonstrated claim.** A general proof is not an
  object; a case for it would be the claim restated.
- **Always `grounds`.** A worked instance of a general proof is not what
  the claim stands on, and calling it a ground would make the claim look
  as if it rested on an example.

## Consequences

- First application, in the same change: CLAIM-571's barrier example is
  filed as CASE-tmpwln61, grounding the claim's "need not equal" (an
  existence clause), with ARG-tmpmqot9. CLAIM-571 takes `grounds` and a
  history note. CASE-198 and CASE-200 take `variant_of` it.
- The read-and-file and synthesis-review skills could carry a line
  pointing here, once the owner adopts it.
- Proposed until the owner adopts it.
