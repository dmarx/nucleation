---
status: Proposed
title: 'Hu, Lu and Clune (2024) report that a fixed foundation-model meta agent which writes new agents as code, scores each on validation data and conditions on an archive of earlier agents and their scores, finds agents that beat hand-designed agents on held-out test sets (for example +13.6 F1 on DROP and +14.4% on MGSM)'
version: 1
tags:
- agency
- anthology-candidate
date: '2026-11-12'
source:
- LIT-2298
promote_when: >-
  §4's tables confirm the DROP, MGSM and transfer gains on held-out test
  sets, and §3 and Appendix H show the meta agent and its prompt held fixed
  across iterations.
bears_on:
- QUESTION-tmp7a7l4
summary: >-
  The central account of [LIT-2298](../literature.d/LIT-2298.md), read in [NOTE-tmpzf0j8](../notes.d/NOTE-tmpzf0j8.md). Proposed until its
  promote_when is met.
---

# THEORY-tmpucrbf: Hu, Lu and Clune (2024) report that a fixed foundation-model meta agent which writes new agents as code, scores each on validation data and conditions on an archive of earlier agents and their scores, finds agents that beat hand-designed agents on held-out test sets (for example +13.6 F1 on DROP and +14.4% on MGSM)

## The account

Hu, Lu and Clune (2024) report that a fixed foundation-model meta agent which writes new agents as code, scores each on validation data and conditions on an archive of earlier agents and their scores, finds agents that beat hand-designed agents on held-out test sets (for example +13.6 F1 on DROP and +14.4% on MGSM). Agents found on math keep an advantage when moved to other domains and other models. The meta agent itself is not improved.
