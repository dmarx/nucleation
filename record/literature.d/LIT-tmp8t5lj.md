---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpgcp7r](../notes.d/NOTE-tmpgcp7r.md)); worth reading as Mehta and Schwab''s own statement of how far their mapping ([LIT-882](LIT-882.md)) reaches, made in reply to the counterexample in arXiv v1 of Lin and Tegmark ([LIT-887](LIT-887.md)). It concedes two things: that preserving the free energy does not recover the distribution ("we entirely agree with this statement and never claimed otherwise"), and that the "if and only if" of [LIT-882](LIT-882.md)''s Eq. 8 is a typo, since the trace condition implies ΔF = 0 but not conversely. It argues one: that exact variational RG means the trace condition Tr_h e^T = 1 for every v, which the counterexample violates (checked), so the mapping''s Eq. 22 is untouched. That reply is right against v1. It locates the mapping''s content at the trace condition alone, which is the scope [THEORY-197](../theory.d/THEORY-197.md) gives it, and it does not answer the point Lin and Tegmark added in their v2 a fortnight later, that the trace condition is also met by hidden variables that do not interact with the system ([THEORY-202](../theory.d/THEORY-202.md)). The "typo" did work in [LIT-882](LIT-882.md): its Section I derives the exactness condition from ΔF = 0 through the direction the comment withdraws.'
title: 'Comment on "Why does deep and cheap learning work so well?"'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 as one of the works cited
    by the batch on hierarchy and hyperbolic geometry (nucleation#115, via
    LIT-887 and NOTE-683) that neither record held: the reading of Lin,
    Tegmark and Rolnick's "Why does deep and cheap learning work so
    well?" (LIT-887, NOTE-688) read this comment and named it as held in
    neither, and NOTE-683 and THEORY-197 cite its concession by arXiv id.
    Read in full the same day (NOTE-tmpgcp7r) from the arXiv PDF of v1,
    the only version (2 pp.), text extracted with pdftotext; the copy
    downloaded for this filing is byte-identical to the one the LIT-887
    reader used. Checked against the arXiv abstract page and API record
    (arXiv:1609.03541 [cond-mat.dis-nn], cross-listed cs.LG and stat.ML;
    David J. Schwab and Pankaj Mehta; v1 submitted 12 September 2016, no
    later version, no journal reference; arXiv comment "Comment on
    arXiv:1608.08225") and DataCite for the arXiv DOI
    10.48550/arXiv.1609.03541 (no related identifiers). The arXiv
    metadata title appends "[arXiv:1608.08225]"; the title above is the
    one the PDF carries. Two Crossref bibliographic searches (by title,
    and by the authors with the subject) returned no journal or
    proceedings version; the only relevant hit was Lin, Tegmark and
    Rolnick's own journal article. So it was never published outside
    arXiv, as far as these sources show. `published:` is the arXiv v1
    date, 12 September 2016 (ADR-002). Not held in nucleation before this
    filing: a grep of record/ for the identifier found only the
    citations in LIT-887, NOTE-688, NOTE-683, THEORY-197 and THEORY-202.
    Not held in the Anthology of the SOTA as far as its clone shows: a
    grep of its record/ (clone at commit d8b5ba5, 9 October 2026,
    possibly stale) for the identifier, "cheap learning" and "Schwab"
    found nothing. Like LIT-882, whose mapping it defends, it is theory of
    what deep networks compute, which the anthology's
    `analysis-and-evaluation` topic could hold; hence
    `anthology-candidate`. `corrects` names LIT-887 for its v1 claim that
    the appendix counterexample invalidates the mapping, and LIT-882 for
    its own Eq. 8, an erratum by the same authors.
tags:
- representation-learning
- natural-sciences
- anthology-candidate
date: '2026-10-09'
published: '2016-09-12'
arxiv: '1609.03541'
first_author: 'Schwab'
keywords:
- 'variational renormalization group'
- 'deep belief networks'
- 'trace condition'
- 'free energy'
- 'comment'
implementations: []
corrects:
- LIT-887
- LIT-882
summary: >-
  Schwab and Mehta (2016), arXiv comment, never published elsewhere. Reply
  to the appendix counterexample of Lin and Tegmark's arXiv v1
  ([LIT-887](LIT-887.md)): agrees that preserving the free energy does not recover the
  distribution, calls the "if and only if" of [LIT-882](LIT-882.md)'s Eq. 8 a typo
  (the trace condition implies ΔF = 0, not conversely), and shows that the
  counterexample violates the trace condition, so the mapping's exact
  step is untouched. It does not reach the later objection that the trace
  condition fails to select the coarse variables.
---
<!-- inactive-ok-file: THEORY-197 THEORY-202 THEORY-194 QUESTION-025 — Proposed or open; cited as the accounts this reading bears on and the question it does not answer -->

# LIT-tmp8t5lj: Comment on "Why does deep and cheap learning work so well?"

David J. Schwab and Pankaj Mehta (2016), arXiv preprint — [ARXIV-1609.03541](https://arxiv.org/abs/1609.03541)

## Key takeaways

- **Conceded: a preserved free energy is not a preserved distribution.**
  Lin and Tegmark's v1 appendix builds a joint Hamiltonian with the right
  partition function and the wrong marginal. The comment accepts this in
  full, says the authors "never claimed otherwise", and quotes Kadanoff,
  Houghton and Yalabik (1976) that variational bounds pertain to the free
  energy and give "no guarantee that the derivatives will be accurate".
- **Conceded: Eq. 8 of [LIT-882](LIT-882.md) is one-directional.** The trace condition
  Tr_h e^{T(v,h)} = 1 for every v implies ΔF = 0; the converse fails, and
  the "⟺" is called "the typo in eq. (8)". It was more than a slip of
  notation: [LIT-882](LIT-882.md) writes "Thus, for any exact RG transformation, we
  know that" the trace condition holds, inferring it from ΔF = 0 through
  the withdrawn direction. With exactness defined as the trace condition
  instead, nothing downstream of Eq. 9 changes.
- **Argued, and right: the counterexample violates the trace condition.**
  Under T = −E + H the counterexample has −T(y, y′) = H(y′) + K(y) + ln Z̃,
  so Tr_{y′} e^T = Z e^{−K(y)}/Z̃, which is constant only if K is. It
  therefore says nothing about [LIT-882](LIT-882.md)'s Eq. 22, which assumes the trace
  condition.
- **Asserted: the trace condition is how variational RG keeps more than
  the free energy.** It "implies that the microscopic probability
  distribution is unperturbed by the introduction of the auxiliary
  variables". True, but it constrains only the visible marginal, and the
  comment does not say what makes the hidden variables a coarse-graining.
  It declines to address Lin and Tegmark's other claims about RG and
  neural networks.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works cited by
the batch on hierarchy and hyperbolic geometry that neither record held
(nucleation#115, via [LIT-887](LIT-887.md) and [NOTE-683](../notes.d/NOTE-683.md)). The reading of Lin, Tegmark and
Rolnick ([LIT-887](LIT-887.md), [NOTE-688](../notes.d/NOTE-688.md)) read it and named it as held in neither, and
the reading of Mehta and Schwab's mapping ([NOTE-683](../notes.d/NOTE-683.md)) and [THEORY-197](../theory.d/THEORY-197.md) cite
its concession by arXiv id. Read on its own merits ([NOTE-tmpgcp7r](../notes.d/NOTE-tmpgcp7r.md)),
with the record's description of the concession checked against the
text.

It is the middle move of a three-step exchange: Lin and Tegmark's v1
counterexample (29 August 2016), this reply (12 September 2016), and Lin
and Tegmark's v2 (28 September 2016), which accepts the reply and adds
that the trace condition is met by systems that do not interact at all.
The reply wins the step it answers and does not reach the next one;
[THEORY-202](../theory.d/THEORY-202.md) holds that next step. The record's descriptions of the
concession in [NOTE-683](../notes.d/NOTE-683.md) and [THEORY-197](../theory.d/THEORY-197.md) are accurate.

It does not bear on [QUESTION-025](../questions.d/QUESTION-025.md): it concerns the exactness condition of
a spatial coarse-graining, not attributes that imply one another.
