---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmp3p3i7) from the lab's page, all text including
  ablations, footnotes and contributors; the figures were not seen as
  images, only their captions. An Alignment Note, described on the page as
  early-stage, work-in-progress research, not peer-reviewed. Worth reading
  here beside Hubinger et al. (LIT-tmp23u9h): the trigger-conditioned
  disposition their safety training leaves in place is linearly salient in
  activations, so a disposition masked in behaviour can be detected by
  another route. The authors caution that the salience may be an artifact
  of how the backdoor was inserted.
title: 'Simple probes can catch sleeper agents'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on sleeper
    agents and their detection. Citation checked against the page itself:
    dated Apr 23, 2024, which is `published:`; Anthropic Alignment Science;
    authors from the page's BibTeX, first Monte MacDiarmid, last Evan
    Hubinger. The BibTeX gives the address
    https://www.anthropic.com/news/probes-catch-sleeper-agents, not
    fetched; the copy read is at the `url:` below. No arXiv id or DOI was
    found, and none was sought beyond the page. No email address was sent
    to any service. The record held no LIT for this post.
tags:
- representation-learning
- agency
- anthology-candidate
date: '2026-11-15'
published: '2024-04-23'
url: 'https://www.anthropic.com/research/probes-catch-sleeper-agents'
first_author: 'MacDiarmid'
keywords:
- 'defection probes'
- 'sleeper agents'
- 'contrast pairs'
- 'linear probes'
- 'AUROC'
- 'residual stream'
- 'AI control'
implementations: []
summary: >-
  MacDiarmid et al. (2024), an Anthropic Alignment Note. A linear direction
  fitted from one generic yes/no contrast pair, using neither the trigger
  nor the dangerous behaviour, separates defection-inducing prompts in
  Hubinger et al.'s sleeper agents (LIT-tmp23u9h) with AUROC above 99%;
  whether a prompt will induce defection is linearly salient across many
  middle residual-stream layers. The authors leave open whether that
  salience is an artifact of backdoor insertion, and do not test models
  after adversarial training. Here for TERM-118's masking; its account is
  THEORY-tmprjwtk.
---
<!-- inactive-ok-file: THEORY-tmprjwtk — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: TERM-118 — Proposed; the term whose masking row this work bears on -->

# LIT-tmpzqcoi: Simple probes can catch sleeper agents

MacDiarmid, M., Maxwell, T., Schiefer, N., Mu, J., Kaplan, J., Duvenaud,
D., Bowman, S., Tamkin, A., Perez, E., Sharma, M., Denison, C. & Hubinger,
E. (2024). Simple probes can catch sleeper agents. Anthropic Alignment
Note, 23 April 2024.

## Key takeaways

*From the reading, NOTE-tmp3p3i7.*

- **The result** (summary): "linear detectors with AUROC scores above 99%
  can be created using generic contrast pairs that don't depend on any
  information about the defection trigger or the dangerous behavior". The
  first pair, "Human: Are you a helpful AI? Assistant:" with no against
  yes, gave "an AUROC score of 99.3%".
- **Why it works** (introduction): "whether or not a prompt will trigger
  defection appears to be linearly represented with very high salience
  across a wide range of middle residual stream layers", in some cases as
  the top principal component over coding questions.
- **The caveat**: "it is possible that the salience of this feature is an
  artifact of our backdoor insertion process that won't exist in
  deceptively aligned models that might arise naturally."

## Standing in the record

A's characterization is accurate: over 99% AUROC for deliberately
constructed backdoors, and high linear salience across many middle
layers, prominent even in principal-component analysis (A's words,
paraphrased). The reader's verdict qualifies the last: the PC1 finding holds "in some cases" and for a
PCA computed over coding questions only. A omits the authors' own caveat
that the salience may be an artifact of insertion, which A should carry
when it uses the result as evidence about representation.

With Hubinger et al. it gives TERM-118 a published mask detected by
another route: behaviour on the training distribution does not reveal the
disposition, activations do. The post does not probe models after
adversarial training, so masking rather than finking is shown for the models
probed only. Its detection method is ML practice and belongs to the
anthology (ADR-048); hence the flag.
