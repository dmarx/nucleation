<!-- scratch/manuscripts/from-obstruction-to-reorganization/04-operationalization.md -->

# Part II. The theory inside its own investigative machinery

Part I's theory was not developed in the abstract and then applied. It was developed inside a research record, and that record is itself an apparatus of exactly the kind the theory describes. It draws distinctions among its entries, keeps them, enforces them, and revises them. Part II describes the record and its tool, then shows, principle by principle, how the theory is operationalized in the machinery the record uses to investigate.

The relation is reflexive in a specific sense. The record holds the theory as claims (CLAIM-470, CLAIM-532, CLAIM-535 and the rest), argued and graded like any other content. It also *runs* on mechanisms that embody those claims: decisions that weigh whether a distinction is needed, migrations that carry changes through, checks that enforce them, reviews that look for what the categories absorbed. Part III asks what happened when the record's inquiry met the limits of its own machinery.

## 8. Luria and Nucleation

### 8.1 Luria

Luria is a command-line tool, and a set of conventions, for keeping a project's memory as plain files under version control [ref: luria repository]. Its configuration file, `luria.yaml`, declares six kinds of thing:

- **Schemes.** Typed document families with stable codes, such as `CLAIM-532`. A code is never reused. Documents are retired by status, never deleted.
- **Fields.** Each is required or optional per scheme. Some draw on **vocabularies**, which may be closed: every value was chosen and described by someone.
- **Typed, directed relations** between documents, such as `rests_on`, `grounds`, `objects_to`, `refines` and `advances`. A relation declares its converse, which luria computes for every reader rather than storing (ADR-079).
- **Statuses.** These encode standing, such as Proposed, Active, Superseded and Rejected. History notes, version numbers and supersession links record how standing changes.
- **Generated views.** Indexes by field value, line, topic and relation, built from the documents and never edited by hand.
- **Validation and repair.** A linter, including `fail_on` patterns a project adds, and a repair step that writes link targets.

Generated views are derived, so they cannot drift from their sources (the record's design principle DP-2). They also propagate whatever their sources say, errors included.

### 8.2 Nucleation

The repository was created empty on 7 September 2026. The record was scaffolded on 25 September (commit `af387c07b`) as the catchall companion to a sibling record, the Anthology of the SOTA. Its growth in schemes:

| Date | Schemes added | Purpose |
|---|---|---|
| 25 Sep | LIT, NOTE, THEORY, ADR, DP | A work; a reading of it; a claim about what is true; a decision; a design principle |
| 7 Oct (ADR-032) | QUESTION, CLAIM, CASE, TERM, ARG | The record's *own* argument |
| November | SYNTHESIS, LEAD, POSTMORTEM | An account of what a part of the argument holds; a research opportunity; a review of how a change has worked out |

That gives twelve schemes on 19 November and thirteen on 20 November. On 20 November the record held 2,935 LITs, 2,217 NOTEs, 2,129 THEORYs, 766 CLAIMs, 497 QUESTIONs, 298 CASEs, 198 LEADs, 131 TERMs, 123 ARGs, 114 ADRs, 108 SYNTHESISes, 6 DPs and 3 POSTMORTEMs.

The record's work is done by four kinds of participant:

- **The owner,** a single human researcher.
- **Assistants in session:** Claude Code sessions on the repository, some coordinating **filing agents** that each read and file a batch of works.
- **External assistants:** ChatGPT, in exchanges the owner shares and the record files.
- **Mechanisms:** the linter, the repair step, generated worklists, and the CI job that runs on every pull request.

Every change is a pull request, and the owner merges. Who noticed, proposed, decided and ratified each change to the grammar is not assumed here; Part III codes it.

The record's argument is organized in **lines**, named inquiries that each entry carries one or more of. The theory of Part I comes mainly from these lines:

- `formal-apparatus` and `realizability` (§§2, 3.5–3.6, 4.3);
- `will-organization`, `readiness` and `transient-support` (§§3, 4.5);
- `distributed-agency` and `organizational-normativity` (§6);
- `pragmatic-transport` and `learned-structure` (§5.1);
- `nucleating-argument`, `records-of-inquiry` and `record-as-apparatus` (§§4–5).

The last three hold the predecessor manuscript's argument.

## 9. How the record operationalizes the theory

### 9.1 The record as an apparatus

In TERM-089's sense, the record's grammar is an apparatus for the record's own objects. CLAIM-469 (Active, demonstrated) states this: luria "realizes a system of distinctions that fixes what counts as a referable and governable object within the record, so that a split scheme makes one object two and a promoted vocabulary makes a value an entity". Its four functions are each mechanized:

| Function (TERM-089) | Mechanism in a luria record |
|---|---|
| **Differentiate** | Schemes, fields, vocabularies and relation types: what can be said of an entry and how entries can relate |
| **Retain** | Codes never reused; retirement by status; version history; `formerly` for earlier temporary codes; git |
| **Enforce** | Required fields; closed vocabularies; the linter and its `fail_on` patterns; CI on every pull request; generated worklists |
| **Revise** | Amendments to `luria.yaml` by decision record, with a first application in the same pull request (ADR-071); migrations; postmortems |

The record also holds its own limit as a claim. "A typed relation is more constrained than either of its relata", so its rigidity is "a fact about the grammar, not evidence that the dependency it records is sound" (CLAIM-479, Active, demonstrated). The grammar is "fixed at any moment but amendable by decision", and a move it could not hold has "repeatedly been treated as a defect of the grammar and answered by amending it". Whether every such move is caught "is not shown" (CLAIM-419, Active, empirical). The predecessor's objection, that the grammar "formalizes early" so that a move fitting no type "is forced into one or lost until the misfit is noticed" (CLAIM-181, Proposed), is the theory's stage 1 of §7.2, stated about this record.

### 9.2 The inquiry tuple, realized

| Component of an inquiry (TERM-095) | What realizes it in a luria record | In Nucleation |
|---|---|---|
| **Language** | Schemes, fields, vocabularies, relation types: the relational vocabulary (TERM-091) | 13 schemes, 18 vocabularies, 69 topic terms; `rests_on`, `grounds`, `objects_to`, `bears_on` and others |
| **Answer space** | What can be said of an entry's standing and kind | QUESTION statuses (Open, Answered, Deferred) and "What would answer it?"; CLAIM status, `role` and `warrant`; CASE `standing` and `kind`; LIT statuses such as Unavailable and Unfetched |
| **Interventions** | Ways of acting on the world or the record | Reading a work (LIT → NOTE); executed studies (CASEs with scripts in `scratch/formal`); LEADs, planned interventions with a stage and priority |
| **Observations** | What comes back, including what the record shows of itself | NOTEs (Read, Skimmed); generated views; lint reports; counts such as CASE-178's |
| **Criteria** | Conditions for changing standing and for admission | THEORY `promote_when`; CLAIM `defeated_if`; the test for a claim whose premises are claims (ADR-084); ARG judgments on support; the owner's review; `fail_on` patterns |
| **Resources** | Rules that ration effort | The second-occurrence rule (ADR-032, ADR-072); CI doing what local runs could not afford (ADR-054); postmortem triggers counted in use, not by the calendar (ADR-110); `Unfetched` routing work to the owner's time (ADR-053) |
| **Reflexivity** | The tuple becoming the object | Decision records that amend `luria.yaml`; migrations; postmortems; skills that encode review procedures |

The answer space and the criteria are themselves written in the language. A status is a vocabulary value, and a criterion is a field, a relation or a lint pattern. A grammar change can therefore revise what counts as an answer, not only what can be said. Part III finds that it sometimes did.

### 9.3 The principles, mechanized

Each principle of §7.1 has one or more mechanisms that operationalize it in the record. Most were adopted for local reasons, not to implement a theory. The correspondence is this paper's observation.

| Principle | How the record operationalizes it |
|---|---|
| **P1:** a distinction is needed when actions differ | Every grammar change is argued in a decision record, with alternatives considered and rejected. ADR-042 rejected adding values to `standing` because it "would answer two questions with one field". Decisions are judged by their first application (ADR-071), so a distinction must show what it does. |
| **P2:** split, merge, re-carve | The grammar can add, split, widen, narrow, rename, retire and withdraw. Retiring by status keeps both the old and the new partition and the map between them. |
| **P3:** no self-certification | Readings are filed by one session and reviewed by another. The owner reviews every pull request. Status reviews and synthesis reviews read the argument with procedures that do not depend on how it was filed. The linter checks consistency, which the record's own claims say is not correctness (CLAIM-293, CLAIM-479). |
| **P4:** naming is its own decision | The second-occurrence rule for process (ADR-072). The rule that an idea gets a code "when it has content of its own and is not already held" (ADR-072). Piloting a field on a sample before requiring it (ADR-043, ADR-056). |
| **P5:** discrepancy, then capacity | A misfit that a filing reports is "listed and then sent to a decision" (CLAIM-419). The curation journal records what each filing left and why. Decision records name the discrepancy that occasioned them. |
| **P6:** three ledgers | Construction: the decision and its first application. Transition: migrations, recorded with counts. Maintenance: required fields, lint, the reviews that exercise a distinction. |
| **P7:** maintenance by intervention; support can erode | CI runs the checks on every change. Skills write review procedures down so that a fresh session can carry them out (DP-5, "no private brains"). DP-4 ("fire before trusting") requires a guard to be run against a deliberate failure before it is relied on. Postmortems review a change once it has been used. The owner's review of every pull request keeps the owner exercising judgment that assistants could otherwise take over. |
| **P8:** reflexive inquiry | `luria.yaml` is a versioned file changed only by decision. Decisions are themselves entries with status and history. POSTMORTEMs `review` decisions and name the decisions their recommendations `prompted` (ADR-112). |
| **P9:** anchors and traceability | Stable codes as exact addresses. `rests_on`, `grounds` and `objects_to` as accountability structure. Retirement by status, never deletion. History notes with dates. `formerly`. The `works` field, which keeps a claim's membership in a manuscript apart from its standing, so that a manuscript is "a view over the argument and not its only copy" (CLAIM-178). |
| **P10:** the ladder of uptake | Admission: a contribution is filed. Recognition: it gets a code in apt terms, with the right type and vocabulary. Credibility: its status and warrant. Uptake: a claim `rests_on` it, or a synthesis integrates it. Revision of the standards of uptake: a decision that changes the grammar or the criteria. |

### 9.4 The predecessor's concepts, realized

| Concept | Where argued | What realizes it |
|---|---|---|
| Anchor | CLAIM-182, CLAIM-185 | A code: stable, never reused, citable part by part |
| Identity stipulated by decision | CLAIM-195 | Versions, history notes, supersession, `formerly` |
| Trigger for coding | CLAIM-176, CLAIM-630 | The second-occurrence rule, now confined to process |
| Accountability structure | CLAIM-250 | `rests_on`, `grounds`, `objects_to`, ARG; the curation and workbench journals |
| Support recorded, strength not | CLAIM-293 | A known limit of `rests_on` and `grounds` |
| No computed withdrawals | CLAIM-664 | Retiring an entry reports its dependants and leaves each to judgment |
| Faithful migration | CLAIM-666 (Proposed) | A decision stating what moved; entries re-read and given history notes |
| An anchor is not shared knowledge | CLAIM-668 (Proposed) | Access to the record does not show that each collaborator knows an entry's current standing |
| Capture cost moved to the reader | CLAIM-179 | Agent filing, with the owner reviewing each pull request |
| Question drift | TERM-056 | QUESTIONs that `refine` one another, so a changed question is a new, related entry |

### 9.5 Four loops

Read through the tuple, the record runs four nested loops:

1. **Within the regime.** Filing readings, stating and revising claims, running studies, all in the grammar as it stands.
2. **On the regime.** A difficulty in the inner loop is diagnosed as a defect of the grammar. A decision records the diagnosis and the alternatives, a migration carries the change through, and validation makes it binding.
3. **On the argument.** Status reviews, promotion audits, and synthesis and reading reviews re-examine standing, independently of how entries were filed.
4. **On the tool.** Problems found in the record change luria itself, and luria's changes come back as new grammar.

Part III shows each loop at work. The second is the flywheel of §7.2.

## 10. What operationalization does and does not establish

Section 9 shows a correspondence between the theory's principles and the record's mechanisms. Five cautions limit what that correspondence establishes.

**Mechanisms were mostly adopted for local reasons.** A decision record was required for every new vocabulary word from the first day (ADR-001), before the record held any of Part I's claims. The second-occurrence rule was a throttle on flooding. Retirement by status was a convention inherited from Luria. The correspondence in §9.3 is therefore partly convergence: practices adopted to keep a record usable turned out to embody claims the record later argued for. Convergence is weaker evidence than design would be. It is also more interesting, because it suggests the principles describe constraints any such record meets.

**Holding a claim is not operating on it.** The record holds CLAIM-602, which says support that does the work erodes the capacity it supports. Holding it does not show that the record's own use of assistants respects it. Operationalization is a property of mechanisms, not of content, and §9.3 lists mechanisms. Where no mechanism exists, as for measuring whether the owner's capacity to judge revisions is maintained, the principle is held and not operationalized (§17.1).

**A mechanism can embody a principle and still fail at it.** The record keeps its accountability structure in typed relations. Its own claims say that structure records that support exists, not how much (CLAIM-293), and that it decides no withdrawals (CLAIM-664). A shared record shows who proposed a claim and what standing it has. It cannot show what any collaborator believes, or that each knows the current standing (CLAIM-668, Proposed). The mechanisms are partial realizations, and Part III finds where they fell short.

**The grammar is not the inquiry.** Luria fixes what can be said of an entry, not what an entry says. A claim's content is open prose (CLAIM-479). The theory's principles about distinctions apply to the grammar, and through it to how the record can hold the argument. They do not apply directly to whether the argument is right. CASE-084, the perfectly accountable false theory, is the standing reminder.

**Operationalizing in a record is one choice among several.** The same principles could be built into a lab's protocols, a model's training loop, or an institution's rules. The record is the case studied here because it keeps a complete, dated history of its own changes. That makes it unusually observable, not uniquely suited.
