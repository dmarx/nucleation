<!-- scratch/manuscripts/from-obstruction-to-reorganization/analysis/census/CODEBOOK.md -->

# Codebook: census of the record's decisions

The coding scheme was fixed on 2026-11-20, before any decision was coded. The unit is one ADR file in `record/decisions.d/` (ADR-001 to ADR-114). Code from the ADR itself: its frontmatter, summary, body and history notes. You may also read entries the ADR names, when that is needed to settle a field. Never guess. Where the ADR does not say, code `unknown`.

Output one JSON object per ADR with exactly these keys:

| Key | Values | Rule |
|---|---|---|
| `adr` | `"ADR-042"` | |
| `date` | `"2026-10-14"` | Frontmatter `date` |
| `status` | Active, Proposed, Superseded, Rejected, Deferred | Frontmatter `status` |
| `grammar_change` | `true`, `false` | `true` if the decision changes `luria.yaml` or adds a lint or check: schemes, fields, relations, vocabularies, terms, statuses, lines, `fail_on` patterns, generated views. `false` for decisions about process, conventions or filing practice only. A Rejected or Deferred decision is `true` if it *proposed* such a change. |
| `level` | List from: term, vocabulary, field, relation, status, scheme, line, lint, view, process | Every level the decision touches |
| `operation` | List from: add, split, merge, widen, narrow, rename, remove, redefine, withdraw, decline, other | `widen` or `narrow`: a term's or relation's sense or scope changes under the same name. `redefine`: what an existing element means or does changes. `withdraw`: a type or abstraction is taken back. `decline`: the decision rejects or defers a proposed change. |
| `regime` | refine, revise, restraint, none | **refine**: adds a distinction or element, and what already counted as an answer, a criterion or a unit of inquiry still counts the same way. **revise**: changes what counts as an answer, a criterion or a unit of inquiry. It redraws a boundary between existing types, changes the meaning of an existing element, withdraws a type, or reassigns existing entries to a different kind of thing. **restraint**: a proposed change was declined or narrowed. **none**: not a grammar change. Code one value; if both refine and revise apply, code revise. |
| `component` | List from: language, answer_space, interventions, observations, criteria, resources | The TERM-095 inquiry tuple. language: types, fields, relations, vocabulary words. answer_space: what can be said of an entry (statuses, warrant, standing, stages). interventions: reading, studies, planned work. observations: views, indexes, reports. criteria: tests for standing, admission and validation. resources: rules rationing effort. |
| `trigger` | owner_request, assistant_in_session, filing_agent, external_assistant, review_or_audit, incident, other, unknown | What prompted the decision, as the ADR says. external_assistant: a ChatGPT exchange ("A", "A12" and so on) pasted by the owner. |
| `trigger_quote` | String, at most 25 words | Verbatim from the ADR, the words that show the trigger |
| `noticer` | owner, assistant, filing_agent, external_assistant, review_process, unknown | Who first noticed the need |
| `proposer` | Same values | Who proposed this decision's design |
| `decider` | owner, assistant, review_process, unknown | Who made the decision |
| `ratification` | explicit, standing_permission, merge_assent, none_recorded | **explicit**: the ADR records the owner's words or act approving *this* change. **standing_permission**: it cites an earlier blanket permission. **merge_assent**: approval only by merging, or by a review procedure the owner delegated to. **none_recorded**: no owner involvement stated. |
| `ratification_quote` | String, at most 25 words, or `""` | |
| `residue` | forced_category, prose_only, false_statement, prospective, unknown | The form the misfit took before the decision. **forced_category**: content was being filed under the nearest wrong value or type. **prose_only**: the distinction lived only in free text. **false_statement**: the grammar made the record assert something untrue. **prospective**: no misfit yet; the change anticipates a need. |
| `migration` | Integer or `null` | Number of existing entries changed, if the ADR states it |
| `outcome` | in_force, superseded, reversed, rejected, deferred, unknown | `reversed`: undone, or superseded within 7 days by a decision that takes it back |
| `later_harm` | String or `""` | A later version note or entry recording that the change caused an error, with its citation |
| `confidence` | high, medium, low | |
| `note` | String, at most 40 words | Anything a reader needs to interpret the codes |
