# RETRO documents

<!-- GENERATED below this line by `luria index` — edit README.stub instead. -->

**[The record](tags/record.md)** (4) — what the schemes hold, and the rules between them:
[001](../../record/retrospectives.d/RETRO-001.md) · [002](../../record/retrospectives.d/RETRO-002.md) · [003](../../record/retrospectives.d/RETRO-003.md) · [004](../../record/retrospectives.d/RETRO-004.md)

**[Taxonomy](tags/taxonomy.md)** (1) — the topic vocabulary and what enforces it:
[004](../../record/retrospectives.d/RETRO-004.md)

**[Mechanism](tags/mechanism.md)** (0) — identifiers, generation, the lint.

**[Migration](tags/migration.md)** (0) — what moves between this record and the Anthology of the SOTA, and why.

**[process](tags/process.md)** (3):
[001](../../record/retrospectives.d/RETRO-001.md) · [002](../../record/retrospectives.d/RETRO-002.md) · [003](../../record/retrospectives.d/RETRO-003.md)

**By status:** [Draft](status/Draft.md) (4) · [Accepted](status/Accepted.md) (0) · [Superseded](status/Superseded.md) (0)

What the status column means in this scheme — the words are luria's, the meanings are this project's.

| Status | | Means |
|---|---|---|
| `Draft` | Draft | Written and not yet accepted by the owner |
| `Accepted` | Accepted | The owner accepts its account of what happened and what it recommends |
| `Superseded` | Superseded | Replaced by a later review of the same change, named in `superseded_by` |

| # | Title | Summary | Status |
|---|---|---|---|
| [RETRO-001](../../record/retrospectives.d/RETRO-001.md) | The session of 2026-11-20 and 21: from an entry's life cycle to transformer depth in six stacked pull requests and a round of sixteen readings; what went right was the record as memory, the owner's challenges and reading after filing; what went wrong was claims stated before the record was searched, and a red check left unlooked-at | The first retrospective under the RETRO scheme, asked for by the owner on 2026-11-21 ("A lot of stuff seems to be clicking right now, and we should document what seems to be going right"). It reads the three devlog entries of 2026-11-21. Going right: the record held most formal pieces, the owner's challenges improved two claims, delegated readers corrected three and confirmed others. Going wrong: six results stated before the record or a triviality check would have caught them, a docs-check failure unseen across five stacked pull requests, reader branches the proxy would not delete. Five recommendations, none yet a decision. | Draft |
| [RETRO-002](../../record/retrospectives.d/RETRO-002.md) v2 | The batch of 2026-11-19 and 20: pull requests 541 to 545, parallel pull requests appending notes to the same entries | Trigger 2 of [ADR-110](../../record/decisions.d/ADR-110.md): five pull requests, one stacked on another and folded, merged on the owner's word. The costs were conflicts on dated notes appended to the same entries by parallel pull requests, twice on one of them; a branch that had to be remapped to concretized codes after main moved; a copy-lawfulness question the rule did not settle; and an inferred personal name nearly written into the record. What changes: a merge order for parallel pull requests, a question for the owner on how dated notes are filed, a wording question for [ADR-074](../../record/decisions.d/ADR-074.md), and a rule against inferring names. | Draft |
| [RETRO-003](../../record/retrospectives.d/RETRO-003.md) v2 | The batch of 2026-11-19: pull requests 535 to 540, a stacked series folded top-down | Trigger 2 of [ADR-110](../../record/decisions.d/ADR-110.md): six pull requests, five of them a stack built on a schema change and folded top-down into main. Everything landed green. The costs were a stack forced by putting readings on the schema pull request, codes split at hyphens by the filer's line-wrapping, a bot repair colliding with an unpulled second commit, an owner review that had to be merged up four branches, and reader branches the session could not delete. What changes: four small rules, and the reader-branch ending [ADR-108](../../record/decisions.d/ADR-108.md) left open. | Draft |
| [RETRO-004](../../record/retrospectives.d/RETRO-004.md) v2 | The session's changes to luria.yaml of 2026-11-19: a work for the owner's manuscript, the explication form, and the LEAD scheme | The owner asked on 2026-11-20 for a postmortem of the session's luria.yaml changes. The work vocabulary entry is used and fine. The explication form works but was filed before its source was read, and rewritten twice. The LEAD scheme holds 197 leads but its stage ladder does not discriminate (96 per cent at idea), it has no priority field for triage, question dependencies are unused, leads cannot target theories or terms, there is no blocked state, and its derived converses are declared but never written. Recommendations for one decision, and three process rules. | Draft |

