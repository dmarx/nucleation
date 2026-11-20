<!-- scratch/manuscripts/from-obstruction-to-reorganization/02-luria-mapped.md -->

## 3. Luria mapped onto the argument

### 3.1 Representational architecture

Luria is a command-line tool and a set of conventions for keeping a project's memory as plain files under version control [ref: luria repository]. Its configuration file, `luria.yaml`, declares:

- **Schemes:** typed document families with stable codes, such as `LIT-1631` or `CLAIM-532`. A code is never reused. Documents are retired by status and never deleted.
- **Fields,** required or optional per scheme, and **vocabularies,** some closed and some configured, from which certain fields must draw. Topic tags, for example, come from a closed list in which every value was chosen and described by someone.
- **Typed, directional relations** between documents, such as `rests_on`, `grounds`, `reviews` and `advances`. Each relation can declare a converse, which luria computes for every reader rather than storing.
- **Statuses** that encode standing, such as Proposed, Active, Superseded or Rejected, together with the history notes, version numbers and supersession links through which standing changes.
- **Generated views:** indexes by field value, line, topic and relation. These are built from the authored documents and never edited by hand.
- **Validation and repair:** a linter that enforces the configuration, and a repair step that writes link targets and normalises sources.

The distinction between authored documents and generated projections matters to the argument. A generated view makes a relationship visible without creating a second, independently maintained copy of it, so when the authored source changes, the view follows. This is the record's design principle DP-2: a hand-maintained projection of a source of truth will drift, so derive it.

### 3.2 Nucleation, and who did what

Nucleation began on 25 September 2026 as the catchall companion to a separate record, the Anthology of the SOTA. It was scaffolded with three schemes for reading: LIT (a work), NOTE (a reading of it, Read or Skimmed according to depth) and THEORY (a claim about what is true, with its evidence and the condition under which it would be promoted). It also carried decision records, design principles and a closed topic vocabulary (ADR-001). Its scope widened on 19 October to any work the owner wanted filed (ADR-048). On 7 October ADR-032 added five schemes for the record's *own* argument: QUESTION, CLAIM, CASE, TERM and ARG. A CLAIM carries a credence (status), a voice (role: thesis, counter, granted, disclaimed or supposed) and typed premises. Later schemes added SYNTHESIS, an account of what a scope of the argument holds; LEAD, a research opportunity with a stage and a status; and POSTMORTEM, a review of how a change has worked out. By 20 November the record held 2,935 LITs, 2,217 NOTEs, 2,129 THEORYs, 766 CLAIMs, 497 QUESTIONs, 298 CASEs, 131 TERMs, 123 ARGs, 108 SYNTHESISes, 198 LEADs, 114 ADRs and 3 POSTMORTEMs.

The account depends on keeping roles apart.

- **The owner,** a single human researcher, set the inquiry's direction, and initiated or ratified every architectural intervention examined here.
- **AI assistants** read sources, drafted entries, proposed decision records, carried out migrations, ran audits and wrote the postmortems. They were Claude Code sessions working on the repository, and ChatGPT in exchanges the owner later filed. Assistants often proposed the shape of a change and surfaced the evidence that one was needed. None changed the grammar without the owner's request or approval.
- **Executable mechanisms** enforced what had been decided: the linter, the repair step, and the CI job that runs both on every pull request.
- **Repository review** made each change inspectable. Every change is a pull request, and the owner merges decisions.

Assistant participation in implementation and review should not be mistaken for autonomous architectural judgment (§8.6).

### 3.3 The inquiry tuple, realised

TERM-095's tuple gives a component-by-component reading of what luria provides. The mapping is this paper's. The record holds the tuple, and it holds A16's remark that luria separates "working within an inquiry regime and investigating the regime itself" (CLAIM-470). It does not hold the table.

| Component of an inquiry (TERM-095) | What realises it in a luria record | In Nucleation |
|---|---|---|
| **Σ, language** | Schemes, fields, vocabularies and declared relation types: the record's relational vocabulary (TERM-091) | 12 local schemes, 18 vocabularies, 69 topics on 19 Nov; `rests_on`, `grounds`, `objects_to`, `refines` and others |
| **𝒜, answer space**: which differences would count as an answer | QUESTION entries and their "What would answer it?" sections; the statuses a CLAIM or QUESTION can take; classification fields that say what sort of answer is in hand | Answered, Open or Deferred questions; Proposed, Active, Rejected or Superseded claims; `warrant`; CASE `standing` and `kind` |
| **𝓘, interventions** | Reading a work; running an executed study; planned interventions; working sessions | LIT → NOTE; executed-study CASEs with scripts in `scratch/formal`; LEADs; workbench entries |
| **𝓞, observations** | What the interventions return, and what the record shows of itself | NOTEs, Read or Skimmed; generated indexes and views; lint reports; counts such as CASE-178's |
| **𝓚, criteria** | Conditions for changing standing; tests for admitting an entry; validation | THEORY `promote_when`; the test for a claim whose premises are claims (ADR-075, ADR-084); ARG judgements on support; the owner's review of each pull request; the linter |
| **𝓑, resources** | Rules that ration filing, review and computation | The second-occurrence rule (ADR-032, ADR-072); CI doing what local runs could not afford (ADR-054); postmortem triggers counted in use (ADR-110); the owner's reading time, to which `Unfetched` routes work (ADR-053) |
| **Reflexivity**: a component becomes the object | Amending `luria.yaml` by decision, with a migration and a first application; reviewing the amendment once used | ADRs, migrations, POSTMORTEMs |

Two features of the table matter for what follows. First, most of 𝒜 and 𝓚 is written in Σ: a status is a vocabulary value, and a criterion is a field or a relation. So an amendment to the grammar can change the answer space or the criteria as well as the language. Second, the last row is not a separate component but the operation that makes the inquiry reflexive. Luria offers it a place: the configuration is a versioned source file that only a decision changes, and every decision cites its first application (ADR-071).

### 3.4 The argument's concepts, realised

The concepts of §§2.1–2.4 also have luria counterparts. Here too the mapping is ours.

| Concept | Where it is argued | What realises it |
|---|---|---|
| **Anchor:** an addressable, persistent structure | CLAIM-182, CLAIM-185 | A code: stable, never reused, citable part by part |
| **Identity criteria, stipulated by decision** | CLAIM-195 | Versions, history notes, supersession, and the `formerly` field that carries a code's earlier temporary names; the decision that says when a change is a new entry rather than a revised one |
| **Recurrence trigger** | CLAIM-176, CLAIM-630 | The second-time rule, now confined to process (ADR-072) |
| **Traceability:** announced, located change | CLAIM-189 | Retire by status, never delete; history notes with dates; changelog fragments; version control |
| **Accountability structure** | CLAIM-250 | `rests_on`, `grounds`, `objects_to`, ARG entries on support, curation and workbench journals |
| **Support recorded, strength not** | CLAIM-293 | A known limit of `rests_on` and `grounds`, stated in the record |
| **Manuscript as a view** | CLAIM-178 | The `works` vocabulary: a claim's membership in a manuscript is a field, kept apart from its status, and the two can disagree |
| **Capture cost moved to the reader** | CLAIM-179 | Agent filing, with the owner's review of every pull request |
| **Question drift** | TERM-056 | QUESTION entries that `refine` one another, so a changed question is a new, related entry |
| **Inquiry frontier moved by stored specification** | TERM-092, CLAIM-475 | TERMs, CASE designs and LEADs that make later questions cheaper to pose |

### 3.5 Two loops

The mapping gives luria two loops. In the **inner loop**, the inquiry works within its regime: it files readings, states and revises claims, and runs studies, all in the grammar as it stands. In the **outer loop**, the inquiry takes the regime as its object. A difficulty in the inner loop is diagnosed as a defect of Σ, 𝒜, 𝓚 or 𝓑. A decision records the diagnosis and the alternatives. A migration carries the change through the existing entries, and validation makes it binding. Since November, a postmortem reviews it once used.

CASE-178 measured the outer loop's rate in the record's first 32 days (§5.5). It found that the outer loop is not a separate, slower process. Its events are rarer events of the same unit of work, arriving in the pull request whose documents needed them. In the terms of T2, reflexive inquiry happened inside ordinary inquiry, when ordinary inquiry ran into its regime.

### 3.6 What the argument predicts about the record's own development

If §2's account is right and the mapping holds, the record's history should show six things. Each is a prediction this paper tests, in part, against the record's own history.

- **P1. Misfits.** A grammar fixed early will meet moves it cannot hold (CLAIM-181). *Tested in §6:* each case starts from one.
- **P2. Revision of the regime.** A noticed misfit will be answered by revising a component of the tuple, not only by forcing the move into a category (CLAIM-470, CLAIM-419). *Tested in §6*, with each case annotated by the component it revised (Table 6.0).
- **P3. Traceable grammar change.** If the record secures traceability (CLAIM-189), changes to its grammar should be announced and located as changes to its claims are. Entries should keep their identity across reorganisation, and their reinterpretation should be recorded (T3). *Tested in §§6.9 and 7.1.*
- **P4. Costs and entrenchment.** Grammar change should carry construction, transition and maintenance costs, and a stabilised grammar may resist later change (T4, CLAIM-475, CLAIM-184). *Tested in part in §§5.5, 6.9 and 8.4; whether falling rates of grammar change mean settling or entrenchment is left open (§8.8).*
- **P5. Persistence without productivity.** A grammar element can be adopted and populated without improving the inquiry (CLAIM-595). *Not testable from the record alone (§10).*
- **P6. The limits of self-measurement.** Measures counted in the record's own grammar cannot by themselves certify that the inquiry improved. ARG-028 says so of the anchoring measures, and CLAIM-266 says it of any probe family that also supplies the training signal. *This bounds every tier-2 finding in this paper (§§5.3, 8.5).*

### 3.7 What the mapping does not claim

- That luria is the only, or the best, realisation of the tuple. QUESTION-458 asks what distinguishes it from ontology and metamodel evolution, and §4 places it.
- That the record constitutes its objects. CLAIM-476 is Proposed, and nothing here depends on it.
- That a self-modifying record is self-correcting (TERM-089). Whether the outer loop improves the inquiry is a tier-3 question this paper cannot answer (§9).
- That the theses T1–T4 are the record's. They are this paper's integrations of claims the record holds.
