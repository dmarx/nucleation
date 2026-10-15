---
number: 105
status: Open
formerly:
- QUESTION-tmpga1fv
title: What is the least an evolving inquiry must retain to support a stated family
  of future revisions, and does the optimal retained state look like provenance,
  dependencies and defeated alternatives, or like something else?
version: 1
tags:
- epistemology
- information-theory
date: '2026-10-15'
line: nucleating-argument
refines:
- QUESTION-003
summary: >-
  A5's first question, A2's closing question ("the minimal persistent representation
  that preserves an agent's epistemic competence") and A4's rate-distortion form,
  from the exchange of 2026-10-14. [QUESTION-003](QUESTION-003.md) asks the same thing of a translation
  and a fixed family of communicative decisions. This asks it of an inquiry whose
  decisions are revisions.
answered_by:
- CLAIM-294
- THEORY-347
- THEORY-353
- THEORY-362
- THEORY-373
- THEORY-387
---

# QUESTION-105: What is the least an evolving inquiry must retain to support a stated family of future revisions, and does the optimal retained state look like provenance, dependencies and defeated alternatives, or like something else?

## Why it is a question

A4 and A5 posed it as a decision-relative compression problem. With H an
inquiry's history, M what is kept, and Q a family of future revision
decisions, find the least I(H; M) such that sup over q in Q of
R_q(M) − R_q(H) stays within ε. A5: "The question is whether this
optimization yields recognizable structures corresponding to evidence
provenance, premise dependencies, alternative hypotheses, and revision
histories."

It is [QUESTION-003](QUESTION-003.md)'s problem with a different decision family. The
exchange's own results bound it from both sides: [CLAIM-294](../claims.d/CLAIM-294.md) shows current
conclusions can fall short, and [CLAIM-300](../claims.d/CLAIM-300.md) shows a sufficient state makes
the rest redundant for a fixed family. Neither says what the optimum looks
like for a family of revisions.

An answer characterizes the optimal retained state for a non-trivial
family of synthetic inquiries and compares it with explicit record
formats. A5: "The interesting result might be that justification graphs
are sometimes approximately sufficient—or that they are systematically
missing crucial information. Either outcome would advance the theory."
The belief-revision literature has a one-step answer for full belief, and
it narrows the question rather than starting it. A closed belief set does
not fix its own revision: AGM adds a selection function or ordering
([LIT-1050](../literature.d/LIT-1050.md), read in [NOTE-874](../notes.d/NOTE-874.md)), and Hansson's survey shows two bases
with the same closure revising to opposite conclusions ([LIT-1072](../literature.d/LIT-1072.md), read
in [NOTE-866](../notes.d/NOTE-866.md)). Two retained states do the job there, a base marking
which beliefs are held in their own right, or an ordering on the closed
set. Neither is provenance, dependencies or defeated alternatives, which
are what this question asks about, and both results concern single
revisions. For iterated revision Hansson reports that "opinions differ
widely". The structures the question names are nearer to Doyle's truth
maintenance systems, which the survey mentions only historically.

**Database readings, 2026-10-15.** Three readings answer the question for
revisions given as changes to base facts under a fixed program. For
acyclic support, one count of derivations per conclusion suffices
(Gupta, Mumick and Subrahmanian 1993, [LIT-1114](../literature.d/LIT-1114.md), [NOTE-915](../notes.d/NOTE-915.md), [THEORY-362](../theory.d/THEORY-362.md)); for cyclic
support, nothing beyond base, rules and stored results is kept, and
support is rechecked at revision time ([THEORY-387](../theory.d/THEORY-387.md)). Provenance polynomials
(Green, Karvounarakis and Tannen 2007, [LIT-1110](../literature.d/LIT-1110.md), [NOTE-913](../notes.d/NOTE-913.md)) suffice for every
revision that re-scores existing inputs in a commutative semiring, for
positive queries ([THEORY-373](../theory.d/THEORY-373.md), [THEORY-380](../theory.d/THEORY-380.md)); why-provenance as a witness basis
(Buneman, Khanna and Tan 2001, [LIT-1104](../literature.d/LIT-1104.md), [NOTE-920](../notes.d/NOTE-920.md), [THEORY-367](../theory.d/THEORY-367.md)) keeps one witness per
derivation. None covers added facts, defeat or contraction, and none
proves minimality, so the question's optimum is still open. The
retained structures are provenance and dependencies, not defeated
alternatives.
