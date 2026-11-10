---
number: 235
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open
formerly:
- QUESTION-tmpsdkg1

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: 'When looking and holding are priced independently and timed per person, do people still prefer re-fetching information that stays in view where it costs more total time?'

version: 1
tags:
- embodied-cognition
- cognition
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: distributed-agency
summary: >-
  The promotion condition formerly on [THEORY-334](../theory.d/THEORY-334.md), moved unchanged when that
  account was narrowed to what Ballard et al. (1997) observed in block
  copying and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v3). Open: whether holding
  information carries a cost beyond time, as Ballard et al. infer, or
  people's choices follow total time, as Gray et al.'s model ([THEORY-346](../theory.d/THEORY-346.md))
  does.

refines:
- QUESTION-095
---

# QUESTION-235: When looking and holding are priced independently and timed per person, do people still prefer re-fetching information that stays in view where it costs more total time?

## Why it is a question

[THEORY-334](../theory.d/THEORY-334.md) holds what Ballard, Hayhoe, Pook and Rao ([LIT-1075](../literature.d/LIT-1075.md)) observed.
Seven subjects copying a pattern of coloured blocks looked back at the
model about 1.3 times per block. Their commonest cycle was the one that
holds least in memory, and it is the slowest in the authors' per-block
tallies. The authors infer that holding information costs more than
re-fetching it. That is inferred from choices, not measured, and with no
statistics. [THEORY-346](../theory.d/THEORY-346.md) (Gray et al.) sets against it a model that prices
memory and display access in time alone and fits a copying task. Bogacz's
commentary on the article reads the same timings as task unfamiliarity.
Until 2026-10-20 the test that would decide between these was
[THEORY-334](../theory.d/THEORY-334.md)'s promote_when.

## What would answer it

The condition as it stood, unchanged:

- A block-copying or similar study with enough participants for
  inferential statistics. The cost of looking and the cost of holding
  items are varied independently, and the time each strategy actually
  takes, encoding included, is measured per person.
- **For the carrying-cost reading.** People still prefer re-fetching where
  it costs more total time, so that memory carries a cost beyond time.
- **Against it.** Their choices follow total time, as [THEORY-346](../theory.d/THEORY-346.md)'s model
  does.

**What cannot settle it.** More fixation counts in the original design,
because its timings do not separate encoding spread over a trial from the
cost of each look.
