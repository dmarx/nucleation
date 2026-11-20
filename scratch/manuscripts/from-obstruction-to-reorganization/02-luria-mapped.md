<!-- scratch/manuscripts/from-obstruction-to-reorganization/02-luria-mapped.md -->

## 3. Luria mapped onto the framework

### 3.1 Architecture

Luria is a command-line tool, and a set of conventions, for keeping a project's memory as plain files under version control [ref: luria repository]. Its configuration file, `luria.yaml`, declares six things:

- **Schemes.** Typed document families with stable codes, such as `CLAIM-532`. A code is never reused. Documents are retired by status and never deleted.
- **Fields.** Each is required or optional per scheme. Some draw on **vocabularies**, which may be closed: topic tags, for example, come from a list in which every value was chosen and described by someone.
- **Typed, directed relations** between documents, such as `rests_on`, `grounds`, `objects_to` and `refines`. A relation declares its converse, which luria computes for every reader rather than storing (ADR-079).
- **Statuses,** such as Proposed, Active, Superseded or Rejected, with the history notes, version numbers and supersession links through which standing changes.
- **Generated views:** indexes by field value, line, topic and relation, built from the documents and never edited by hand.
- **Validation and repair:** a linter, which includes `fail_on` patterns the project adds, and a repair step that writes link targets.

Generated views give the record DP-2's property: a projection derived from a source of truth cannot drift from it. They also propagate whatever the source says, errors included (§7.5).

### 3.2 Nucleation, and who does what

The repository was created empty on 7 September 2026, and the record was scaffolded on 25 September (commit `af387c07b`) as the catchall companion to a sibling record, the Anthology of the SOTA. It started with five schemes:

- LIT, a work;
- NOTE, a reading of it, marked Read or Skimmed;
- THEORY, a claim about what is true, with its evidence and a condition for promotion;
- ADR, a decision record;
- DP, a design principle.

It also had a closed topic vocabulary (ADR-001).

On 7 October, ADR-032 added five schemes for the record's *own* argument: QUESTION, CLAIM, CASE, TERM and ARG. A CLAIM carries a credence (its status), a voice (its role: thesis, counter, granted and so on) and typed premises. On 19 October, ADR-048 widened the record's scope to any work the owner wanted filed. November added three more schemes:

- SYNTHESIS, an account of what part of the argument holds;
- LEAD, a research opportunity;
- POSTMORTEM, a review of how a change has worked out.

That makes twelve schemes on 19 November and thirteen on 20 November.

On 20 November the record held:

| Scheme | Entries |
|---|---:|
| LIT | 2,935 |
| NOTE | 2,217 |
| THEORY | 2,129 |
| CLAIM | 766 |
| QUESTION | 497 |
| CASE | 298 |
| LEAD | 198 |
| TERM | 131 |
| ARG | 123 |
| ADR | 114 |
| SYNTHESIS | 108 |
| DP | 6 |
| POSTMORTEM | 3 |

Four kinds of participant take part:

- **The owner,** a single human researcher.
- **Assistants in session:** Claude Code sessions working on the repository. Some coordinate **filing agents,** subagents that each read and file a batch of works.
- **External assistants:** ChatGPT, in exchanges the owner pastes or shares and the record then files.
- **Mechanisms:** the linter, the repair step, generated worklists, and the CI job that runs on every pull request.

Every change is a pull request, and the owner merges.

Who noticed, proposed, decided and ratified each grammar change is not assumed here. It is coded in the census (§6.1). The answer changes over the eight weeks, and that change is one of the paper's main findings.

### 3.3 The inquiry tuple, realized

The record holds the tuple (TERM-095). It also holds A16's remark that luria separates "working within an inquiry regime and investigating the regime itself" (CLAIM-470). The following table is this paper's.

| Component | What realizes it in a luria record | In Nucleation |
|---|---|---|
| **Language** | Schemes, fields, vocabularies and declared relation types: the record's relational vocabulary (TERM-091) | 13 schemes, 18 vocabularies, 69 topics; `rests_on`, `grounds`, `objects_to`, `refines` |
| **Answer space**: which differences count as an answer | The statuses an entry can take; fields that say what sort of answer is in hand; QUESTION entries and their "What would answer it?" sections | Open, Answered and Deferred questions; Proposed, Active, Rejected and Superseded claims; `warrant`; CASE `standing` and `kind` |
| **Interventions** | Reading, executed studies, planned work, working sessions | LIT to NOTE; executed-study CASEs with scripts in `scratch/formal`; LEADs; workbench entries |
| **Observations** | What interventions return, and what the record shows of itself | NOTEs; generated views; lint reports; counts |
| **Criteria** | Conditions for changing standing, tests for admitting an entry, validation | THEORY `promote_when`; the test for a claim whose premises are claims (ADR-084); ARG judgments on support; the owner's review; `fail_on` patterns |
| **Resources** | Rules that ration filing, review and computation | The second-occurrence rule (ADR-032, ADR-072); CI doing what local runs could not afford (ADR-054); postmortem triggers counted in use (ADR-110); `Unfetched`, which routes work to the owner's time (ADR-053) |

Two features matter below:

- **Most of the answer space and the criteria are written in the language.** A status is a vocabulary value, and a criterion is a field, a relation or a lint pattern. A grammar change can therefore change the answer space or the criteria.
- **The table says where reflexive change happens, not whether it is refinement or revision.** That is coded case by case (§6.1).

### 3.4 The framework's concepts, realized

| Concept | Where argued | What realizes it |
|---|---|---|
| Anchor | CLAIM-182, CLAIM-185 | A code: stable, never reused, citable part by part |
| Identity stipulated by decision | CLAIM-195 | Versions, history notes, supersession, and `formerly`, which carries a code's earlier temporary names |
| Trigger for coding | CLAIM-176, CLAIM-630 | The second-occurrence rule, now confined to process (ADR-072) |
| Traceability | CLAIM-189 | Retirement by status, dated history notes, changelog fragments, version control |
| Accountability structure | CLAIM-250 | `rests_on`, `grounds`, `objects_to`, ARG entries; the curation and workbench journals |
| Support recorded, not its strength | CLAIM-293 | A known limit of `rests_on` and `grounds` |
| Faithful migration | CLAIM-666 | Decision records stating what moved; `formerly`; entries re-read and history-noted |
| No computed withdrawals | CLAIM-664 | Retiring reports dependants, and judgment does the rest |
| Manuscript as a view | CLAIM-178 | The `works` vocabulary: a claim's membership in a manuscript, kept apart from its status |
| Capture cost moved to the reader | CLAIM-179 | Agent filing, with the owner's review of each pull request |
| Question drift | TERM-056 | QUESTIONs that `refine` one another |

### 3.5 Two loops, and two more

Read through the tuple, luria gives an inquiry an **inner loop** and an **outer loop**:

- **Inner loop: working within the regime.** Filing readings, stating and revising claims, running studies.
- **Outer loop: taking the regime as the object.** A difficulty in the inner loop is diagnosed as a defect of the grammar. A decision records the diagnosis and the alternatives considered, a migration carries the change through existing entries, and validation makes it binding. Since November, a postmortem reviews the change once it has been used.

The record's history shows two further loops:

- **Reviewing the argument.** Status reviews, promotion audits, and synthesis and reading reviews re-examine the argument's standing, not its grammar (§7.2).
- **Changing the tool.** Problems found here change luria itself (§7.6).

### 3.6 What the framework leads one to expect, and what would count against it

The six expectations below were written after the history they are tested on. They are postdictions, not predictions, and the census (§6.1) is the main safeguard: it tests them against every decision the record made, not against chosen cases. Each states its falsifier.

| | Expectation | It fails if | Tested in |
|---|---|---|---|
| **E1** | Noticed misfits are answered by changing the grammar, not left in prose or forced | Most noticed misfits in the census end as prose-only or as a forced category without a decision | §§6.1, 8.1 |
| **E2** | Some grammar changes are revisions, not only refinements | Every grammar change in the census is a refinement or restraint | §§6.1, 8.1 |
| **E3** | Grammar changes are traceable: announced by decision, and carried through the entries that use what changed | Term rewordings or removals are made without a decision, or leave carrying entries with a changed meaning and no re-reading | §8.2 |
| **E4** | Grammar changes have costs, and some cause errors later | No migration is recorded, and no later error is traced to a grammar change | §§6.1, 8.3 |
| **E5** | The work of noticing and proposing grammar changes shifts from the owner toward assistants over time | The share of changes noticed or proposed by assistants does not rise, or ratification stays explicit throughout | §§6.1, 8.4 |
| **E6** | Measures taken in the record's own grammar cannot certify that the inquiry improved | Not a prediction: a bound on every finding (ARG-028, CLAIM-266) | §§8.5, 10 |

### 3.7 What the mapping does not claim

- **That luria is the only or the best realization of the tuple.** §4 compares it with the alternatives.
- **That the record constitutes its objects.** CLAIM-476 is Proposed.
- **That a self-modifying record is self-correcting** (TERM-089).
- **That F1–F4 are the record's.** They are this paper's.
