---
status: Active
status_note: >-
  read in full 2026-11-15 (NOTE-tmps6dyd) from arXiv v1 (30 pp.,
  NeurIPS 2026). Worth reading for its geometric account of why
  null-space-projected editing fails across domains (preservation
  constraints from different domains leave a small common null space),
  not for its recipe, which is machine-learning practice and belongs to
  the anthology (ADR-048).
title: 'MuEdit: An efficient multi-task editing method towards inter-domain knowledge conflicts'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 at the owner's request ("read and
    file" the arXiv URL). Checked against the record first: no LIT held
    the arXiv id or title; ROME (LIT-1536), MEMIT (LIT-1582) and Hase et
    al. (LIT-1578) are held, and AlphaEdit, the method this extends, is
    not. Citation from the arXiv API and the PDF: Songshi Liang, Ting-En
    Lin, Zixuan Huang, Yuchuan Wu, Yongbin Li, Zihe Wang and Rui Yan,
    "30 pages, accepted by NeurIPS 2026"; v1 submitted 2026-11-11, which
    is `published:`. The abstract in the arXiv listing ("distinct
    Jacobian geometries") differs from the PDF's ("domain-specific
    preservation representations"); the PDF's is used.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2026-11-11'
arxiv: '2611.14910'
first_author: 'Liang'
keywords:
- 'model editing'
- 'knowledge editing'
- 'multi-task editing'
- 'null-space projection'
- 'Conflict Index'
- 'low-rank approximation'
- 'large language models'
implementations: []
summary: >-
  Liang, Lin, Huang, Wu, Li, Wang & Yan (2026), NeurIPS. Null-space
  editing (AlphaEdit) protects preserved representations by confining an
  update's rows to the null space of their key matrix. Across several
  domains, the update must lie in the intersection of the domains' null
  spaces, which can be much smaller than any one; the authors call this
  "inter-domain null-space misalignment" and measure it by a Conflict
  Index, the share of the smaller null space lost in the intersection.
  MuEdit orders tasks to keep adjacent conflicts low and compresses a
  preservation matrix's rank when conflict is high. On Llama3-8B it beats
  AlphaEdit and other editors after sequential editing across five
  domains. In its seven-task test, though, greedy ordering scores within
  the 95% interval of the mean random order on every task.
---

<!-- inactive-ok-file: THEORY-1039 THEORY-1011 — Proposed and Rejected; named as the key–value reading the paper assumes, not relied on -->

# LIT-tmpy7s15: MuEdit: An efficient multi-task editing method towards inter-domain knowledge conflicts

Songshi Liang, Ting-En Lin, Zixuan Huang, Yuchuan Wu, Yongbin Li, Zihe Wang
and Rui Yan, "MuEdit: An efficient multi-task editing method towards
inter-domain knowledge conflicts", NeurIPS 2026; arXiv:2611.14910.

## Key takeaways

*From the reading, NOTE-tmps6dyd.*

- **The diagnosis.** An update that preserves several domains'
  representations must satisfy ΔKᵢ = 0 for each, so its rows lie in the
  intersection of their left null spaces. "Although each domain may
  individually admit many update directions, their intersection can be
  much smaller" (§1).
- **The measure.** The Conflict Index is 1 − dim(common null space) /
  min(individual null-space dimensions), averaged over edited layers. It
  is symmetric, lies in [0, 1], and is zero for a task against itself.
- **The method**, which is practice and not filed as such: conflict-aware
  task ordering, offline or greedy; rank reduction of the more
  conflicting preservation matrix when the index exceeds an adaptive
  threshold; and a projected closed-form update over a three-task window.
- **The results.** After five-domain sequential editing on Llama3-8B,
  ZsRE specificity is 0.8845 against AlphaEdit's 0.5506 under the same
  best order. General ability on SAMSum and Natural Questions declines
  little.

## Standing in the record

Filed on 2026-11-15 at the owner's request. Under ADR-048 nucleation
files what the owner wants, but an instruction for machine-learning
practice belongs to the anthology. This LIT therefore files the paper
for its account of why editing across domains fails, and carries the
`anthology-candidate` flag for the method.

It extends the record's editing line: ROME (LIT-1536), MEMIT
(LIT-1582, THEORY-1031) and Hase et al. on localization against editing
(LIT-1578, THEORY-1024). It assumes the key–value reading of MLP layers,
which the record holds only as a conjecture (THEORY-1039; THEORY-1011,
which also claimed localization, is Rejected). Its geometric argument
does not need that reading: it is linear algebra on the edited map. Its
problem of few admissible directions common to several constraints is a
cousin of CLAIM-366's shared
descent directions.
