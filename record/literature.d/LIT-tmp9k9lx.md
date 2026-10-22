---
status: Active
status_note: >-
  read 2026-10-22 (NOTE-tmpyc06q), main text in full and appendices in
  part, from the arXiv v1 PDF; worth reading as the first interventional
  evidence that a language model has a functional analogue of conscious
  access in the access sense: a sparse set of verbalizable directions,
  found by a corpus-averaged Jacobian lens, carries report, held concepts,
  unspoken reasoning steps and reuse of one argument by many functions,
  while routine processing uses the same information without it; and
  ablating it flattens experiential language about the self and about
  others alike. Read it knowing its limits: one company's models studied
  by that company, unreplicated; a lens whose own statistics draw the
  layer band; an automatic/flexible split partly defined by the result;
  experiential language graded by another model; and an explicit refusal
  to say anything about phenomenal consciousness. Filed as
  THEORY-tmp111ci and THEORY-tmp9o12p.
title: 'Verbalizable Representations Form a Global Workspace in Language Models'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed, not read. Checked on 2026-10-21 against the article page at
    transformer-circuits.pub, which gives the authors and "Published July 6,
    2026", and against arXiv. `published:` is the page's date, 6 July 2026,
    earlier than the arXiv v1 date, 16 July 2026 (arXiv:2607.15495). No DOI.
- version: 2
  date: '2026-10-22'
  note: >-
    Read in NOTE-tmpyc06q from the arXiv v1 PDF (117 pages, footer
    "Archival Preprint"): the main text, pp. 1–60, in full; appendices
    A.1–A.4, A.12, A.15, A.16 and A.23 in full and A.8 in part; the other
    appendices skimmed by heading. The HTML page was fetched again and
    still gives "Published July 6, 2026"; the arXiv abstract page gives v1
    as Thu, 16 July 2026, so `published:` stands. Author list checked
    against the arXiv metadata: sixteen authors, Gurnee, Sofroniew and
    Lindsey core contributors, Lindsey corresponding; the HTML page gives
    Ben Thompson as "T. Ben Thompson". Status Deferred to Active. The
    summary is rewritten from the reading: the models are named, the
    J-space is defined, and the experiential-report ablation, the
    alignment audits and counterfactual reflection training are added. The
    "Not read" paragraph is replaced by Key takeaways. THEORY-tmp111ci and
    THEORY-tmp9o12p filed.
tags:
- consciousness
- representation-learning
- anthology-candidate
date: '2026-10-21'
published: '2026-07-06'
arxiv: '2607.15495'
url: 'https://transformer-circuits.pub/2026/workspace/index.html'
first_author: 'Gurnee'
keywords:
- 'global workspace'
- 'access consciousness'
- 'interpretability'
- 'Jacobian lens'
- 'J-space'
- 'language models'
- 'verbal report'
- 'experiential reports'
- 'counterfactual reflection training'
implementations: []
summary: >-
  Gurnee, Sofroniew et al. (2026), Anthropic, Transformer Circuits Thread;
  arXiv:2607.15495. A Jacobian lens, the Jacobian from a layer to the
  output averaged over a corpus, gives each vocabulary token a direction
  per layer; sparse combinations of them form the "J-space". In Claude
  Sonnet 4.5, Haiku 4.5, Opus 4.5 and Opus 4.6, swaps, injections and
  ablations show the J-space part of a representation, under a tenth of
  its variance, carrying verbal report, instructed concepts, two-hop
  intermediates and reuse of an argument by many functions, while
  continuation, anomaly detection and line wrapping use the same
  information without it. The J-space works in a middle band of layers,
  holds about 25 active directions, and is amplified and relayed by the
  weights. Ablating it flattens experiential language about the model and
  about others. Further sections apply it to alignment audits, show
  post-training installing the Assistant's point of view, and introduce
  counterfactual reflection training. The authors take no position on
  phenomenal consciousness.
---
<!-- inactive-ok-file: THEORY-tmp111ci THEORY-tmp9o12p — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-tmpdga80 CLAIM-tmp1lvwf TERM-tmpe36gg — Proposed; the batch's claims and term, cited as open -->

# LIT-tmp9k9lx: Verbalizable Representations Form a Global Workspace in Language Models

Gurnee, W., Sofroniew, N., Pearce, A., Piotrowski, M., Kauvar, I., Chen, R., Soligo, A., Bogdan, P., Ong, E., Wang, R., Thompson, T. B., Abrahams, D., Kantamneni, S., Ameisen, E., Batson, J. & Lindsey, J. (2026). Verbalizable Representations Form a Global Workspace in Language Models. *Transformer Circuits Thread* (Anthropic). <https://transformer-circuits.pub/2026/workspace/index.html>. arXiv:2607.15495.

## Key takeaways

*From the reading, NOTE-tmpyc06q. Pages are the arXiv PDF's.*

- **Access, not experience.** "Note that access consciousness is a purely
  functional notion"; on its relation to experience "we take no position
  on this issue" (p. 2).
- **Privileged for report and reasoning.** The J-space component of a
  concept, "a median of only 6–7% of the concept vector's variance"
  (p. 12), carries its report; the rest carries almost none once the
  J-space is clamped. The same holds for unspoken two-hop intermediates:
  "it is the J-space component that mediates the internal reasoning"
  (p. 19).
- **Selective.** The language of a passage is in the J-space in four tasks,
  but a swap there changes only naming it and facts that need it, not
  continuation or detecting a spliced sentence (pp. 22–24). The authors
  draw the blindsight parallel (p. 58).
- **Structure.** A band from about layer 38 to 92 of 100; about 25 active
  directions, under 10% of variance; amplified by MLPs and relayed by a
  distinct set of heads (§4). The late boundary is "somewhat post-hoc"
  (p. 55).
- **Experiential reports.** Ablating the J-space flattens the felt,
  first-person, sensory register of the models' stream-of-consciousness
  narrations, and equally of their descriptions of another person,
  beyond norm-matched controls (pp. 27–28). The score is graded by
  another model.
- **Workspace before self.** A base model already has the workspace;
  post-training installs the Assistant's point of view in it (§6, p. 57).
- **Uses.** Audits surface evaluation awareness, strategic deliberation
  and implanted misaligned dispositions not visible in output (§5).
  Training only counterfactual reflections improves honesty through
  implanted J-space content (§7).

## Why this is here

The owner's exchange of 2026-10-21, "Experience and interpretation", asked whether experience is constituted by interpretation or produced by it. The exchange cited this paper for a representation space in a language model whose contents are available for verbalization, deliberate manipulation and flexible reasoning, a functional analogue of the global workspace. It took the paper to make the overgeneration problem concrete: if interpretive organization of this kind sufficed for experience, the thesis would have to say whether this system has it. The reading confirms that description. It adds two things the exchange did not use: the experiential-report ablation, which bears on what report evidence can show in a machine (QUESTION-048), and the dissociation of the workspace from the Assistant's installed point of view, which separates TERM-tmpe36gg's organizational and represented senses of perspective. Bears on QUESTION-048, QUESTION-046 and QUESTION-tmpc4j7p, and on CLAIM-tmpdga80 and CLAIM-tmp1lvwf. The anthology may want it as interpretability work, and §7 carries an instruction for machine-learning practice, so the flag stands.
