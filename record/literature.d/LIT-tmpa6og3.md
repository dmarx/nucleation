---
status: Active
status_note: 'read in full 2026-10-17 (NOTE-tmpt2aw8); worth reading as the short, exact case that transfer entropy is not a measure of information flow: in two XOR processes it credits a bit to a source that holds none of it alone, and reports zero for sources that jointly fix the target. Read it knowing that "flow" is defined by the authors as information solely attributable to one source''s past, that the cure it points to (unique information) has no agreed measure, and that its conjecture that directed information and Ay and Polani''s interventional flow fail the same way is a conjecture. Filed as THEORY-tmpijy6i.'
title: 'Information Flows? A Critique of Transfer Entropies'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Filed at the owner's request as the critique the record lacked of
    reading transfer entropy as information flow. Citation checked against
    the arXiv API on 2026-10-16 (v1 21 December 2015; PRL 116, 238701,
    2016). Not held in the Anthology of the SOTA: a grep of its record/
    (clone of 2026-10-12, d1573d2) for the authors' names and the
    identifiers found nothing, and its topic vocabulary has no word for
    information measures. Read in full the same day from arXiv
    1512.06479v2 (17 June 2016, SFI Working Paper 16-01-001), 6 pp.; the
    PRL version was not compared. Declared `corrects: LIT-tmpz9o5z`
    because its target is the reading of transfer entropy as information
    transfer that Schreiber's title states.
tags:
- information-theory
- complex-systems
- causality
date: '2026-10-17'
published: '2015-12-21'
arxiv: '1512.06479'
doi: '10.1103/PhysRevLett.116.238701'
first_author: 'James'
keywords:
- 'stochastic process'
- 'transfer entropy'
- 'causation entropy'
- 'partial information decomposition'
- 'network science'
corrects:
- LIT-tmpz9o5z
implementations: []
summary: >-
  James, Barnett & Crutchfield (2016), *Physical Review Letters* 116, 238701, [ARXIV-1512.06479](https://arxiv.org/abs/1512.06479). Defines information flow from X to Y as information in Y attributable solely to X's past, and shows with two XOR processes that transfer entropy is not it. With Y_t = X_{t−1} ⊕ Y_{t−1}, T_{X→Y} = 1 bit, yet the bit is jointly carried by both pasts (co-information −1). With Z_t = X_{t−1} ⊕ Y_{t−1}, both transfer entropies are 0 and the causation entropies are 1 bit each. By PID, transfer entropy is unique plus synergistic information; only the unique part is a candidate for flow. Conditioning is not subtraction.
---

# LIT-tmpa6og3: Information Flows? A Critique of Transfer Entropies

Ryan G. James, Nix Barnett and James P. Crutchfield (2016), "Information Flows? A Critique of Transfer Entropies", *Physical Review Letters* 116: 238701 — [ARXIV-1512.06479](https://arxiv.org/abs/1512.06479)

## Key takeaways

*From the reading, [NOTE-tmpt2aw8](../notes.d/NOTE-tmpt2aw8.md).*

- **Flow, defined.** Information flow from X to Y is information
  currently in Y whose "cause" can be solely attributed to X's past:
  localized information (p. 1).
- **Overestimating flow.** X_t, Y_0 fair coins, Y_t = X_{t−1} ⊕ Y_{t−1}.
  T_{X→Y} = 1 bit, but I[Y_t : Y_{0:t}] = I[Y_t : X_{0:t}] = 0 and
  I[Y_t : Y_{0:t} | X_{0:t}] = 1 bit. The bit belongs to both pasts
  together; transfer entropy assigns it to X. Checked.
- **Underestimating influence.** X, Y fair coins, Z_t = X_{t−1} ⊕ Y_{t−1}.
  T_{X→Z} = T_{Y→Z} = 0, all pairwise informations vanish, and the
  causation entropy C_{X→Z|(Y,Z)} = 1 bit, which in turn localizes a
  joint bit. Checked.
- **Why.** I[X : Y | Z] is not "X and Y with Z removed"; it can exceed
  I[X : Y]. In Williams and Beer's PID, I[X₁ : Y | X₂] = U₁ + S, so
  transfer entropy is unique plus synergistic information.
- **Consequence for networks.** Graphs with transfer-entropy edges encode
  only dyadic relations. In the second example the three series are
  pairwise independent, so the graph is empty while Z is fixed by X and Y.

## Standing in the record

Filed on 2026-10-17 to fill the record's gap on whether transfer entropy
measures flow, and read the same day. Filed as [THEORY-tmpijy6i](../theory.d/THEORY-tmpijy6i.md). It is
the main source for [CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md). Its examples are the d = 1 corner of
Williams and Beer's coupled-process family ([LIT-tmpsbhb4](LIT-tmpsbhb4.md)), which those
authors call state-dependent transfer: the two papers agree on the
decomposition and disagree on the word. `causality` is for its question,
what kind of influence a transfer entropy reports. It carries no
instruction for machine-learning practice.
