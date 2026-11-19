---
status: Read
paper: LIT-tmpqgxkn
title: 'Li and Webb 2026 — What drives the emergence of symbolic mechanisms in large language models?'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read from the arXiv PDF v1 (https://arxiv.org/pdf/2611.13270, 20 pp.),
    text layer: §§1–7 and Appendices A–E. Not read: figure content beyond
    captions and axis text. Read by a delegated reader on 2026-11-19; the
    filer rechecked every quotation below against the PDF text.
date: '2026-11-19'
---

# NOTE-tmp70cux: Li and Webb 2026 — What drives the emergence of symbolic mechanisms in large language models?

## Contribution

A token-invariant rule representation, measured by whether swapping a
mean-difference rule vector flips a model's answer to the other rule's
(the flip rate), develops or fails to develop according to the diversity
of the training data. It appears in attention-free MLPs as well, so the
transformer's architectural features are not needed for it at high
diversity. The transformer's mechanism is identified; the MLP's is not.

## Key results

- **Task and circuit.** GPT-2-small transformers (12 layers, 12 heads)
  trained from scratch on one-example ABA/ABB completion with fresh
  arbitrary tokens. Layer-1 "symbol abstraction heads" attend from the
  third token to the first (ABA) or second (ABB). The answer is produced
  not by the symbolic induction and retrieval heads found in pretrained
  LLMs but "via a rule-dependent subspace rotation" (§2.3).
- **Examples.** "Flip rate was near 0% with 200 examples and reached 100%
  from 100k examples" (§3.2), but "In these low-diversity conditions the
  models did not generalize": at 200 examples the low flip rate goes with
  no generalization at all.
- **Vocabulary and rules.** "flip rate was 0% at V =50, 5% at V =100, and
  close to 100% from V =500 upward"; "With V =100, flip rate was 5% with 2
  rules and 95% with 10 rules" (§3.2).
- **Role-token bias.** Every model generalized in distribution, yet "Flip
  rate nevertheless fell from 98% at 0% bias to near 0% at 100% bias"
  (§3.2, at V=100). Out of distribution, large-vocabulary models
  generalized at every bias level (§3.3).
- **Late emergence.** At V ≤ 100, "training models well past the point of
  convergence eventually led to a sharp increase in the flip rate" (§3.2),
  after a non-symbolic but generalizing phase. From V=500 up, flip rate
  and accuracy rise together, and a 2-layer model shows no first phase at
  all (App. D).
- **Architecture.** At V=10k the ablated transformers reach 100%, an MLP
  attention variant about 90%, and a pure MLP "reached a flip rate of 100%
  in all five runs" (§4.1). The transformer is about twice as fast to
  ceiling. The authors' reading: "greater data diversity promotes the
  efficient development of symbolic mechanisms".
- **Binding.** For entity–attribute binding IDs, bias lowers the flip rate
  from 100% to 44%; the IDs are defined by slot (first or second pair).
- **Admitted.** "how symbolic mechanisms are actually implemented in an
  MLP remains an open question" (§7).

## Assumptions

A high flip rate is the sign of an invariant, causally relevant symbolic
representation; for the MLP and for binding it is the only criterion. The
four diversity axes are treated as one construct. Small from-scratch
models stand in for LLMs. Three to five seeds.

## Concepts

Symbol abstraction heads; concept intervention and flip rate; role-token
bias; rule-dependent subspace rotation; binding IDs; a statistical phase
before a symbolic one.

## Bearing on the record

- **QUESTION-392** (creating a capability against making one reachable).
  A clean instance: every architecture can represent the symbolic
  solution; data diversity decides whether training reaches it and when,
  and at small vocabularies extra training reaches it late. Training is
  finite, so "never reached" is unshown.
- **CLAIM-567** (feasible, reachable, reliably reached). Corroborates: two
  task-solving solutions are feasible, and data and capacity decide which
  one training reaches first.
- **CLAIM-113** (transformations and invariants). The best fit: the role
  is what stays invariant when the vocabulary is relabelled, since tokens
  are drawn fresh for every prompt. Role-token bias breaks that invariance
  in the training distribution, and the invariant representation then
  fails to appear.
- **THEORY-1002** (frozen random networks reach above-chance interchange
  accuracy). No random-initialization control. The intervention is a
  fixed mean-difference vector, not an optimized rotation, and trained
  models that solve the task at a near-zero flip rate serve as internal
  negative controls. The concern is weakened, not removed.
- **QUESTION-234.** Not answered: no comparison of alignments, no
  uniqueness test.
- **THEORY-039**, **THEORY-782.** An instance and an analogy only.
- **QUESTION-tmpex36a** (the owner's hunch: role abstraction and fibration
  structure). The paper is silent at the level of units and partitions.
  A route through symmetry is open: at zero bias the data is invariant
  under relabelling; THEORY-981 holds that gradient descent then stays in
  the symmetric weight subspace; weight symmetry gives orbit synchrony
  (THEORY-276), which balanced partitions generalize (THEORY-1065). The
  test is in the question.
- Held neighbours the first search missed: THEORY-1009 (data statistics
  gate the emergence of induction circuits), THEORY-117 and THEORY-794
  (diversity and compositional generalization, LIT-667, which Li and Webb
  cite), THEORY-264 (function vectors). Not held: Yang, Campbell, Huang,
  Wang, Cohen and Webb 2025, "Emergent symbolic mechanisms support abstract
  reasoning in large language models", the paper this one extends.

## Limitations

Small synthetic models; part of the LLM circuit only; few seeds; the MLP
verdict rests on one criterion, and its intervention adds to the whole
flattened state at every block; no random baseline; architecture tested
only at high diversity; slot-defined binding IDs; no unit-level
mechanism.
