---
number: 694
status: Read
formerly:
- NOTE-tmpgcp7r
paper: 'LIT-891'
title: 'Comment on "Why does deep and cheap learning work so well?"'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v1, the only version
    (arXiv:1609.03541v1, 12 September 2016, 2 pp.), text extracted with
    pdftotext and kept as paper.txt in the scratchpad download directory,
    with a layout extraction used for the appendix formulas. Main text,
    appendix and the three references read; the appendix computation
    checked by hand under LIT-882's identification T = −E + H. For what
    it answers and what it concedes, LIT-882's Section I (Eqs. 6–9 and
    the sentence after Eq. 8) was re-read from the arXiv text the
    LIT-882 reader used, and Lin and Tegmark's v1 and v2 appendices were
    taken from NOTE-688. The Kadanoff, Houghton and Yalabik passage the
    comment quotes (J. Stat. Phys. 14, 171, 1976) was not checked against
    its source.
date: '2026-10-09'
summary: >-
  Schwab and Mehta concede that a preserved free energy does not give a
  preserved distribution and that the "iff" of [LIT-882](../literature.d/LIT-882.md)'s Eq. 8 should be
  one-directional, and show that Lin and Tegmark's v1 counterexample
  violates the trace condition, so the mapping's exact step stands. Right
  against v1; it places all of the mapping's content at the trace
  condition, and says nothing to the later point that the trace condition
  does not select the coarse variables.
---
<!-- inactive-ok-file: THEORY-197 THEORY-202 THEORY-194 QUESTION-025 — Proposed or open; cited as the accounts this reading bears on and the question it does not answer -->

# NOTE-694: Comment on "Why does deep and cheap learning work so well?"

## Contribution

A two-page reply by the authors of [LIT-882](../literature.d/LIT-882.md) to the appendix of Lin and
Tegmark's arXiv v1 ([LIT-887](../literature.d/LIT-887.md)). It settles what the mapping claimed about
exactness: exact variational RG means the pointwise trace condition, not
a matched free energy, and the authors withdraw the converse direction of
their Eq. 8. It shows that Lin and Tegmark's counterexample fails the
trace condition, and so does not touch the mapping's exact step. It adds
no new result; its value is that it fixes, in the authors' own words,
the scope [NOTE-683](NOTE-683.md) and [THEORY-197](../theory.d/THEORY-197.md) later reached by reading [LIT-882](../literature.d/LIT-882.md).

## Key insight

The trace condition Tr_h e^{T(v,h)} = 1 for every v and the condition
ΔF = 0 are different strengths of the same requirement: the first is
pointwise and preserves the whole visible distribution, the second is a
single number. The first implies the second, not conversely. Lin and
Tegmark's counterexample lives in the gap, and the mapping does not.

## Assumptions

- **Kadanoff's variational RG** with a coupling operator T(v, h) between
  visible and hidden variables; the coarse Hamiltonian is defined by
  e^{−H^RG(h)} = Tr_v e^{T(v,h) − H(v)}, as in [LIT-882](../literature.d/LIT-882.md) Eq. 6.
- **The identification** T = −E + H of [LIT-882](../literature.d/LIT-882.md), applied by the comment to
  Lin and Tegmark's joint Hamiltonian, read as E(y, y′).
- **Exact RG** is taken to mean the trace condition (Eq. 1 of the
  comment, Eq. 9 of [LIT-882](../literature.d/LIT-882.md)), not ΔF = 0.

## Key results

- **Agreement.** "A coarse-graining transformation that preserves the
  free energy does not suffice to reconstruct the empirical (microscopic)
  probability distribution … We entirely agree with this statement and
  never claimed otherwise." Supported by a quoted passage from Kadanoff,
  Houghton and Yalabik (1976) that the variational principles pertain to
  the free energy and do not guarantee its derivatives.
- **The trace condition implies a preserved free energy.** Stated without
  proof; it is one line: Tr_h Tr_v e^{T−H} = Tr_v e^{−H} Tr_h e^T = Z.
  And it leaves the visible distribution unchanged: the joint
  e^{T−H}/Z marginalizes over h to e^{−H}/Z. Both checked.
- **Eq. 8 withdrawn in one direction.** "It is possible to preserve the
  free energy while violating the trace condition (note the typo in eq.
  (8) of [1] – it is not a biconditional. This typo possibly contributed
  to this misunderstanding)."
- **The counterexample fails the trace condition** (Appendix). With
  H(y, y′) = H(y) + H(y′) + K(y) + ln Z̃ and T = −H(y, y′) + H(y),
  −T(y, y′) = H(y′) + K(y) + ln Z̃, so Tr_{y′} e^T = Z e^{−K(y)}/Z̃, which
  is not constant when K is not. The comment says only that it is
  "non-constant"; the closed form is mine. Checked.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Preserving the free energy does not suffice to recover the distribution | strong (agreed by both sides; Lin and Tegmark's construction) | [LIT-887](../literature.d/LIT-887.md) v1 Appendix A, accepted here |
| C2 | The trace condition implies ΔF = 0, but ΔF = 0 does not imply it; [LIT-882](../literature.d/LIT-882.md)'s "⟺" is wrong | strong | one-line derivation; the counterexample |
| C3 | Lin and Tegmark's counterexample violates the trace condition, so it does not refute the mapping's Eq. 22 | strong | Appendix, checked |
| C4 | The misreading was Lin and Tegmark's, a "misunderstanding of the variational RG procedure" | weak | [LIT-882](../literature.d/LIT-882.md)'s own text infers the trace condition from ΔF = 0 (see below); the misreading followed the paper |
| C5 | Through the trace condition, variational RG preserves more of the distribution than the free energy, as any reasonable RG must | moderate as stated; it preserves the visible marginal, not a choice of coarse variables | asserted; see Assessment |

## Concepts

- **trace condition**: Tr_h e^{T(v,h)} = 1 for every visible
  configuration v; Kadanoff's exactness condition, and [LIT-882](../literature.d/LIT-882.md)'s Eq. 9.
- **preserving the free energy**: ΔF = F^h − F^v = 0, i.e. the coarse
  partition function equals the original one.

## Connections

It answers Lin and Tegmark's arXiv v1 ([LIT-887](../literature.d/LIT-887.md), read in [NOTE-688](NOTE-688.md)), and
is in turn answered by their v2 of 28 September 2016, which records the
reply, keeps the counterexample, and adds that "any two systems that do
not interact with each other will trivially satisfy their trace
condition". The v3 and journal versions of [LIT-887](../literature.d/LIT-887.md) drop the appendix and
with it the exchange. It defends [LIT-882](../literature.d/LIT-882.md) ([NOTE-683](NOTE-683.md)) on its own terms.

## Assessment

- **Against Lin and Tegmark's v1, the reply is right.** The
  counterexample refutes the "⟺" of Eq. 8 and nothing else; Eq. 22 is
  derived from the pointwise trace condition, which the counterexample
  fails. [NOTE-688](NOTE-688.md) reaches the same verdict.
- **The "typo" carried weight in [LIT-882](../literature.d/LIT-882.md).** [LIT-882](../literature.d/LIT-882.md) introduces the
  exactness condition by inference: "∆F = 0 ⟺ Tr e^T = 1 (8). Thus, for
  any exact RG transformation, we know that Tr e^T = 1 (9)". "Thus" runs
  through ΔF = 0 ⇒ trace condition, the direction the comment withdraws.
  Read as [LIT-882](../literature.d/LIT-882.md) wrote it, an exact RG step was one with ΔF = 0, and Lin
  and Tegmark's counterexample was aimed at exactly that reading. So C4
  overreaches: the misunderstanding the comment blames on Lin and
  Tegmark followed the paper's text. The repair is simple and costs
  nothing downstream: define exactness as Eq. 9, and Eqs. 18–22 stand.
- **What the reply concedes about the approximate regime.** Its own
  quotation from Kadanoff says the variational principle pertains to the
  free energy. So short of exactness, the criterion variational RG
  optimizes is ΔF, and the trace condition is what is approximated.
  Under the identification T = −E + H, [NOTE-683](NOTE-683.md) found that ΔF reduces to
  log Z − log Z_λ, a normalization only. The comment does not take this
  up, and by placing all of the mapping's force on the trace condition it
  leaves the mapping with content only at the exact point, which is what
  [THEORY-197](../theory.d/THEORY-197.md) says.
- **What the reply does not answer.** C5 says the trace condition
  preserves "more information about the distribution", and it does: the
  whole visible marginal. But the question Lin and Tegmark raised next is
  what makes h a coarse-graining of v, and the trace condition is silent
  on that: hidden variables independent of v satisfy it ([THEORY-202](../theory.d/THEORY-202.md)).
  The comment itself frames RG as aiming "to preserve the long wavelength
  part of a distribution", a stated target, which is the thesis of
  [LIT-887](../literature.d/LIT-887.md) and [THEORY-194](../theory.d/THEORY-194.md); it does not say how the trace condition or an
  RBM's training supplies that target.
- **Small errors.** The Northwestern affiliation carries the postcode
  08854, which is New Jersey's, not Evanston's. No bearing on the
  content.

## Bearing on the record

- **The record's description of the concession checks out.** [NOTE-683](NOTE-683.md)
  (v2 history) says the authors "conceded Eq. 8's 'iff' as a typo in
  arXiv 1609.03541", and [THEORY-197](../theory.d/THEORY-197.md) (v2) that "Mehta and Schwab conceded
  the '⟺' as a typo". Both are accurate: the comment says Eq. 8 "is not a
  biconditional" and calls that a typo. Two refinements, neither an
  error: the comment does not concede [NOTE-683](NOTE-683.md)'s further point that
  under the identification ΔF measures only normalization; and its
  "typo" label understates, since [LIT-882](../literature.d/LIT-882.md) inferred its exactness
  condition through the withdrawn direction. The comment is by Schwab
  and Mehta, in that order.
- **[THEORY-197](../theory.d/THEORY-197.md)**: supported. The mapping's own authors locate its
  content at the trace condition, and their quotation from Kadanoff puts
  the approximate criterion at the free energy, the criterion [NOTE-683](NOTE-683.md)
  shows degenerates under the mapping. It could join [THEORY-197](../theory.d/THEORY-197.md)'s
  sources as the authors' statement of scope.
- **[THEORY-202](../theory.d/THEORY-202.md)**: the comment is the position its second half answers.
  It shows why the first half (a matched partition function is not
  enough) was accepted by both sides, and it asserts, without argument,
  that the trace condition is enough for "any reasonable RG procedure",
  which [THEORY-202](../theory.d/THEORY-202.md) denies. Nothing here weakens [THEORY-202](../theory.d/THEORY-202.md).
- **[THEORY-194](../theory.d/THEORY-194.md)**: consistent; "preserve the long wavelength part" is a
  stated relevance target, and the comment gives no unsupervised source
  for it.
- **[QUESTION-025](../questions.d/QUESTION-025.md)**: no bearing. There are no attributes, co-occurrence
  statistics or lattices.
- **No THEORY.** The reading yields no claim the record does not already
  hold in [THEORY-197](../theory.d/THEORY-197.md) and [THEORY-202](../theory.d/THEORY-202.md).
- **Anthology.** Theory of what Boltzmann machines compute, with no
  practice instruction; the `analysis-and-evaluation` topic could hold
  it, as for [LIT-882](../literature.d/LIT-882.md).

## Limitations

- A two-page comment: no new derivation beyond the appendix check, and
  the free-energy implication is stated, not shown.
- It addresses only the v1 appendix and explicitly declines Lin and
  Tegmark's other claims about RG and neural networks.
- It does not engage what the variational criterion becomes under the
  RBM parametrization, or whether the trace condition selects a
  coarse-graining.
- Never published outside arXiv; no later version.

## Open questions

- Is there a condition, stronger than the trace condition and weaker
  than a stated target, that makes the hidden variables of an exact step
  a coarse-graining rather than an unrelated system? [THEORY-202](../theory.d/THEORY-202.md) says the
  trace condition is not it; the comment assumes it is.
- Did the authors ever correct Eq. 8 in [LIT-882](../literature.d/LIT-882.md) itself? arXiv shows no
  v2 of [LIT-882](../literature.d/LIT-882.md), so as of this reading the correction lives only here.
