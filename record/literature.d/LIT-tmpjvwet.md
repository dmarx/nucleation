---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmpl4x31](../notes.d/NOTE-tmpl4x31.md)) in full, from the Transformer Circuits
  page; worth reading for ten case studies that show, on single prompts
  and with interventions, a two-hop intermediate in Claude 3.5 Haiku
  ([THEORY-tmpgx2s5](../theory.d/THEORY-tmpgx2s5.md)), a rhyme planned on the newline before a line is
  written ([THEORY-tmpz8eh5](../theory.d/THEORY-tmpz8eh5.md)), a jailbreak whose target word is not
  represented before it is written ([THEORY-tmpzjxhi](../theory.d/THEORY-tmpzjxhi.md)), a trained-in goal
  represented in every Assistant context of a model organism
  ([THEORY-tmpaa9v2](../theory.d/THEORY-tmpaa9v2.md)), and a default "can't answer" circuit that known
  entities inhibit. Read it knowing that the authors find a satisfying
  graph for about a quarter of the prompts they try, that the graphs shown
  are curated and of a replacement model ([LIT-tmpsuo6l](LIT-tmpsuo6l.md)), that several
  cruxes run through attention the graphs cannot see, and that its general
  statements about the model ([THEORY-tmpfralg](../theory.d/THEORY-tmpfralg.md)) go beyond what the case
  studies show.
title: 'On the Biology of a Large Language Model'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 to register and
    read the core circuits literature the record lacked. Checked on
    2026-10-26 against the article's page: Jack Lindsey (lead), Wes
    Gurnee, Emmanuel Ameisen, Brian Chen, Adam Pearce, Nicholas L. Turner,
    Craig Citro and 20 further authors (Anthropic), Transformer Circuits
    Thread, "Published March 27, 2025", which is `published:` (ADR-002). No
    arXiv deposit was found in an arXiv title search, so the source is the
    article's URL. The summary follows the article's opening and
    introduction.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpl4x31) from the HTML of the article page, fetched
    2026-10-26 and reduced to text: every section and appendix except the
    Acknowledgments and Author Contributions. Interactive figures were not
    rendered and are taken from the text, captions and inline tables.
    Status Deferred → Active. Five accounts filed: THEORY-tmpgx2s5,
    THEORY-tmpz8eh5, THEORY-tmpzjxhi and THEORY-tmpaa9v2 (Active, each one
    case study read in full) and THEORY-tmpfralg (Proposed). The summary
    is checked against the reading and kept.
tags:
- representation-learning
- causality
- cognition
- anthology-candidate
date: '2026-10-26'
published: '2025-03-27'
url: 'https://transformer-circuits.pub/2025/attribution-graphs/biology.html'
first_author: 'Lindsey'
keywords:
- 'attribution graphs'
- 'circuit tracing'
- 'Claude 3.5 Haiku'
- 'multi-hop reasoning'
- 'planning'
- 'hallucination'
- 'chain-of-thought faithfulness'
- 'mechanistic interpretability'
implementations: []
summary: >-
  Lindsey et al. (2025), Transformer Circuits Thread. Ten case studies of
  Claude 3.5 Haiku with the attribution graphs of [LIT-tmpsuo6l](LIT-tmpsuo6l.md), each
  validated by perturbing features in the model: two-hop factual recall
  through an intermediate "Texas" representation, rhymes planned before a
  line is written, addition features reused across contexts, a default
  "can't answer" circuit inhibited by known entities whose misfire yields
  hallucination, unfaithful chains of thought, multilingual circuits,
  medical diagnosis, refusals, a jailbreak and a model with a hidden goal.
  The authors present each as an existence claim about specific prompts.
---
<!-- inactive-ok-file: THEORY-tmpfralg CLAIM-tmpwr001 — Proposed; the wider thesis filed from this reading and the record's own claim, cited as open -->

# LIT-tmpjvwet: On the Biology of a Large Language Model

Lindsey, J., Gurnee, W., Ameisen, E., Chen, B., Pearce, A., Turner, N. L.,
Citro, C., et al. (2025). On the biology of a large language model.
*Transformer Circuits Thread*, 27 March 2025.
<https://transformer-circuits.pub/2025/attribution-graphs/biology.html>

Read in full on 2026-10-26 ([NOTE-tmpl4x31](../notes.d/NOTE-tmpl4x31.md)). Five accounts were drawn from
it: [THEORY-tmpgx2s5](../theory.d/THEORY-tmpgx2s5.md), [THEORY-tmpz8eh5](../theory.d/THEORY-tmpz8eh5.md), [THEORY-tmpzjxhi](../theory.d/THEORY-tmpzjxhi.md), [THEORY-tmpaa9v2](../theory.d/THEORY-tmpaa9v2.md) and
[THEORY-tmpfralg](../theory.d/THEORY-tmpfralg.md).

## Why this is here

Registered and read at the owner's request of 2026-10-26, after "how's the
record on neural circuit theory?" found that the record held almost none
of the core circuits literature. It is the most cited set of circuit case
studies in a production-scale model, and the companion of [LIT-tmpsuo6l](LIT-tmpsuo6l.md),
whose method it applies. For the circuits line it adds the first entries
about intermediate steps and plans in a large model, as against small or
algorithmic ones ([LIT-345](LIT-345.md), [LIT-tmpe7b5o](LIT-tmpe7b5o.md)), and it bears on [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md)
(features read from activity, here validated by intervention) and on the
workspace reading of [LIT-1347](LIT-1347.md), by the same group.
