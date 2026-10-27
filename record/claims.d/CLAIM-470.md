---
number: 470
status: Proposed
formerly:
- CLAIM-tmpalzo4
title: 'Inquiry is a form of specification: a question fixes which differences would count as an answer, an inquiry adds the operations that make those differences accessible, and what it finds can stabilize into a specification that constrains later inquiry; so inquiry stands to its findings as a specification to its realizations, with one difference, that an inquiry can revise what an answer could be'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) That every reformulation of a question the
  record or a science has made is a choice among distinctions its earlier
  specification already admitted, so that inquiry only selects answers and
  never changes the answer space; the last clause would then be false, and
  inquiry would be a specification with a search procedure attached. (b)
  That findings once stabilized constrain later inquiry no differently
  from findings held loosely, so that stabilization does no work. Not
  defeated by laws of nature that no inquiry made: the claim is about the
  specifications through which inquiry investigates, not about what they
  are specifications of.
tags:
- epistemology
- philosophy-of-science
- design-rationale
date: '2026-10-27'
line:
- nucleating-argument
rests_on:
- CLAIM-477
complements:
- CLAIM-476
grounds:
- LIT-988
- LIT-1645
- LIT-1652
uses:
- TERM-065
summary: >-
  The owner's, U15 of the exchange of 2026-10-27: "inquiry is a form of
  specification." It carries [CLAIM-477](CLAIM-477.md)'s analogy into inquiry:
  question and finding stand as specification and realization, and a
  stabilized finding becomes a specification for the next inquiry. A15
  and A16 found Dewey and Collingwood the nearest predecessors, and
  counterexample-guided abstraction refinement the nearest formal case.
  [TERM-065](../terms.d/TERM-065.md) already keeps a description apart from the regime it is judged
  under; the claim adds that the regime is itself a product of inquiry
  and can be its object. It does not say that inquiry makes what it
  investigates.
---
<!-- inactive-ok-file: THEORY-1084 — Proposed, Open or Rejected; cited in the note on the U15–U23 readings, as open -->
<!-- inactive-ok-file: CLAIM-477 CLAIM-476 CLAIM-419 CLAIM-475 — Proposed; the claims this rests on and sits beside, cited as open -->
<!-- inactive-ok-file: LIT-1645 LIT-1651 LIT-1652 LIT-1675 LIT-1641 LIT-1665 LIT-1637 — Deferred or Unavailable; registered from the exchange, unread, cited for what they are standardly cited for -->

# CLAIM-470: Inquiry is a form of specification: a question fixes which differences would count as an answer, an inquiry adds the operations that make those differences accessible, and what it finds can stabilize into a specification that constrains later inquiry; so inquiry stands to its findings as a specification to its realizations, with one difference, that an inquiry can revise what an answer could be

## The claim

The owner, at U15, after the dynamics of transitions ([QUESTION-281](../questions.d/QUESTION-281.md)):
"inquiry is a form of specification."

A specification constrains what can count as an admissible realization
([CLAIM-477](CLAIM-477.md)). A question does the same for answers. A15: "A question is
therefore not merely a request for information about an independently
specified object. It can be **a partial specification of the space in which an
answer—and sometimes the object of inquiry itself—can become determinate**."
Formally, a question q: Ω → A_Q partitions states into those it cannot tell
apart. An experiment adds interventions and observations, so A15 wrote an
inquiry as (A, 𝓘, 𝓞, 𝓚): answer space, admissible interventions,
observations and criteria of evaluation. A16 added the language Σ and the
resource bounds 𝓑. Neither called this a standard definition.

Three parts, with what supports each:

- **A question is a partial specification.** "Is this system stable?" does
  not yet say which system, which perturbations, which stability or which
  horizon (A16 §1). Belnap and Steel's logic of questions and van Fraassen's
  contrast classes ([LIT-1637](../literature.d/LIT-1637.md), Unavailable) make the point formally; A16
  cited both, and neither is read here.
- **A finding can stabilize into a specification.** A result reliable enough
  becomes a theory, method, instrument or rule that governs the next inquiry
  (A15 §3). Collingwood's logic of question and answer ([LIT-1651](../literature.d/LIT-1651.md)) is the
  epistemic form: an answer established once becomes a presupposition of the
  next question. Rheinberger's epistemic things becoming technical objects
  ([LIT-1665](../literature.d/LIT-1665.md)) is the experimental form.
- **An inquiry can revise its answer space.** This is where inquiry is more
  than a specification. A16 §4: a question about which equilibrium a system
  occupies has no adequate answer once a Hopf bifurcation leaves a stable
  limit cycle, and must become a question about which attracting set
  organizes the dynamics. Dewey ([LIT-1645](../literature.d/LIT-1645.md)) puts the formulation of the
  problem inside inquiry.

## What the exchange added

**[TERM-065](../terms.d/TERM-065.md) already holds half of it.** The effective-description regime
ℛ = (X, 𝒬, ℐ, ℬ, ε, τ) keeps a candidate description apart from the
conditions it is judged under, so descriptions can be compared without
moving the goalposts. A16 §2 drew the second operation from it: "Evaluate T
under ℛ" and "Evaluate or revise ℛ". "**Inquiry becomes reflexive when its own
conditions of evaluation become objects of inquiry.**" [TERM-065](../terms.d/TERM-065.md) treats ℛ as
supplied; this claim says ℛ is itself made by inquiry and can be remade by it.

**The formal case is counterexample-guided abstraction refinement**
([LIT-1652](../literature.d/LIT-1652.md)). A model checker runs on an abstraction that merges states.
When a counterexample proves spurious, the abstraction is refined to separate
the states whose merging produced it. A16 §6 read luria's DP-016 ([CLAIM-419](CLAIM-419.md)
here) as "the same *epistemic pattern*": failure under a specification,
diagnosis of a missing distinction, refinement. It also gave the limit: CEGAR
refines the abstraction for a fixed property, and "does not automatically
recognize that the verification property itself is misguided." That is the
line between refining within a framework and revising it, and the claim's last
clause is about the second.

**Precision is not correctness.** Expected information gain (Lindley,
[LIT-1675](../literature.d/LIT-1675.md)) is relative to the hypothesis space already specified. A16 §7:
"The inquiry can become increasingly precise without becoming correct." The
record has the empirical form in Devezer et al. ([LIT-988](../literature.d/LIT-988.md), read in [NOTE-792](../notes.d/NOTE-792.md)):
sound model comparisons need not lead a community to the true model, because
which alternatives are proposed constrains what it can discover. A15 §6: "So
specification is not epistemically innocent." [TERM-056](../terms.d/TERM-056.md)'s question drift is a
case of it. A15 drew a criterion from it, with Chang's pragmatist realism
([LIT-1641](../literature.d/LIT-1641.md)) beside it: a healthy apparatus "must support not only the
evaluation of admissible answers, but the detection and revision of
inadequate conditions of admissibility."

**Two kinds of failure.** A16 §10 separated a failure of realization (the
inquiry is adequate and this attempt failed) from a failure of specification
(the right kind of answer cannot be expressed). "**the same observed failure
can demand entirely different responses**", and deciding which it was is
itself inquiry. A16 §14 counted three things an inquiry can find: an answer
it did not know, a distinction it did not know how to make, and a limit of
the practice by which it decides what is knowable.

## What it does not claim

- That inquiry makes what it investigates. A16 §9: "This doesn't imply every
  law of nature is produced by scientific inquiry. It means the *epistemic
  specification through which we investigate a law* can be historically
  constituted."
- That inquiries undergo bifurcations. A15's table pairing anomalies with
  instabilities and paradigm entrenchment with persistent organization is "a
  structural comparison, not an assertion that inquiries literally undergo
  physical pitchfork bifurcations". Whether the dynamics of inquiry can be
  modelled with the same mechanisms is open.
- That the regime should float while descriptions are compared. Keeping ℛ
  fixed for a comparison is a local methodological commitment (A17 §8), and
  this claim does not loosen [TERM-065](../terms.d/TERM-065.md).

## Why it bears on the record

[CLAIM-476](CLAIM-476.md) says luria is an apparatus for a record's objects whose grammar
the record's own inquiry revises. This claim is the general form: any inquiry
specifies, and its stable products are specifications. A16 §11 read luria's
split between editing a record and revising its schema as "working within an
inquiry regime and investigating the regime itself". [CASE-178](../cases.d/CASE-178.md) measured
the second in this record: it happens rarely, on demand and by decision.
[CLAIM-475](CLAIM-475.md), the owner's next turn, adds that specifying is itself bounded
by resources.

## What would test it

A16 §12 proposed one study. A synthetic system can be stationary or
oscillatory, and investigators start with a schema that knows only kinds of
equilibrium. Three regimes are compared on the same external benchmarks:
- fixed (update answers only);
- refinable (add distinctions within the ontology);
- revisable (change questions, variables and evaluation).
If the revisable regime finds the oscillation no sooner and no more reliably
than the refinable one, the last clause loses its point. The common
benchmarks are what keep the comparison from rewarding moved goalposts.

## Note of 2026-10-27 (evening): the readings of the U15–U23 works

- **CEGAR** ([NOTE-1231](../notes.d/NOTE-1231.md); [THEORY-1064](../theory.d/THEORY-1064.md), [THEORY-1094](../theory.d/THEORY-1094.md)) supports the
  claim's first part. The property's atoms build the initial abstraction,
  and no abstraction may merge states that disagree on them (Thm 1, p. 5),
  so the question fixes which differences may never be merged. Its loop has
  the exact shape of defeater (a). Every refinement is a split between the
  first abstraction and the concrete state space, and nothing touches the
  property. CEGAR is therefore a worked case of refining within a fixed
  answer space, as the body said. It does not count against the claim's
  last clause, which is about inquiry in general. The coarsest split that
  removes a counterexample is NP-hard to find (Thm 3).
- **Simon** ([NOTE-1232](../notes.d/NOTE-1232.md)) gives a partial case of the last clause.
  Chess "involves continually redefining what the problem is" (p. 186). In
  design, requirements are evoked mid-process and need not be specified in
  advance (pp. 190–191). But most of his revision is selection, "generated
  from, or dredged from" memory (p. 188), which leans toward defeater (a).
