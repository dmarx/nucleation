<!-- scratch/manuscripts/from-obstruction-to-reorganization/04-operationalization.md -->

# Part II. The theory inside its own investigative machinery

Part I's theory was not developed in the abstract and then applied. It was developed inside a research record, and that record is itself an apparatus of exactly the kind the theory describes. It draws distinctions among its entries, keeps them, enforces them, and revises them. Part II describes the record and its tool, then shows, principle by principle, how the theory is operationalized in the machinery the record uses to investigate.

The relation is reflexive in a specific sense. The record holds the theory as claims (CLAIM-470, CLAIM-532, CLAIM-535 and the rest), argued and graded like any other content. It also *runs* on mechanisms that embody those claims: decisions that weigh whether a distinction is needed, migrations that carry changes through, checks that enforce them, reviews that look for what the categories absorbed. Part III asks what happened when the record's inquiry met the limits of its own machinery.

## 8. Luria and Nucleation

### 8.1 Luria

Luria is a command-line tool, and a set of conventions, for keeping a project's memory as plain files under version control [ref: luria repository]. Its configuration file, `luria.yaml`, declares six kinds of thing:

- **Schemes.** Typed document families with stable codes, such as `CLAIM-532`. A code is never reused. Documents are retired by status, never deleted.
- **Fields.** Each is required or optional per scheme. Some draw on **vocabularies**, which may be closed: every value was chosen and described by someone.
- **Typed, directed relations** between documents, such as `rests_on`, `grounds`, `objects_to`, `refines` and `advances`. A directed relation declares its converse, which luria computes for every reader rather than storing (ADR-079, Proposed but applied). Symmetric relations such as `complements` stay stored on both sides.
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
| 21 Nov (ADR-115) | RETRO | A review of how a change or a stretch of work went, including what went right; POSTMORTEM narrowed to something that went wrong |

That gives twelve schemes on 19 November, thirteen on 20 November and fourteen on 21 November. On 20 November the record held 2,935 LITs, 2,217 NOTEs, 2,129 THEORYs, 766 CLAIMs, 497 QUESTIONs, 298 CASEs, 198 LEADs, 131 TERMs, 123 ARGs, 114 ADRs, 108 SYNTHESISes, 6 DPs and 3 POSTMORTEMs. On 21 November, after that night's promotion (`main` at `56479304e`), it held 2,956 LITs, 2,236 NOTEs, 2,147 THEORYs, 794 CLAIMs, 504 QUESTIONs, 300 CASEs, 206 LEADs, 134 TERMs, 124 ARGs, 135 ADRs, 118 SYNTHESISes, 7 RETROs, 6 DPs and 4 POSTMORTEMs (recomputed by the analytics pipeline, `analysis/analytics-2026-11-21.json`). The filing of the exchange "Rich Get Richer Power Laws", open on its branch that evening, adds 51 LITs and 92 entries more.

The record's work is done by four kinds of participant:

- **The owner,** a single human researcher.
- **Assistants in session:** Claude Code sessions on the repository, some coordinating **filing agents** that each read and file a batch of works.
- **External assistants:** ChatGPT, in exchanges the owner shares and the record files.
- **Mechanisms:** the linter, the repair step, generated worklists, and the CI job that runs on every pull request.

Every change is a pull request. Since 21 November work merges into a `staging` branch, and only a Promote workflow or the owner merges staging into `main` (ADR-116, Proposed but applied). While the dialectic regime is on, the assistant merges its own pull requests into staging (ADR-121, Active); the owner's review point is the promotion pull request from staging into main, which a workflow keeps open (ADR-125, Active). Who noticed, proposed, decided and ratified each change to the grammar is not assumed here; Part III codes it.

The record's argument is organized in **lines**, named inquiries that each entry carries one or more of. The theory of Part I comes mainly from these lines:

- `formal-apparatus` and `realizability` (§§2, 3.5–3.6, 4.3);
- `will-organization`, `readiness` and `transient-support` (§§3, 4.5);
- `distributed-agency` and `organizational-normativity` (§6);
- `pragmatic-transport` and `learned-structure` (§5.1);
- `nucleating-argument`, `records-of-inquiry` and `record-as-apparatus` (§§4–5).

The last three hold the predecessor manuscript's argument. Since 21 November Part I's own theme is a line as well, `learning-and-inquiry`: how a system that draws distinctions comes to learn and to inquire (ADR-130, Active). It was added at the owner's ruling, after the first audit of cross-line accounts (ADR-129, Active) found that the eight accounts of this paper's principles together answer a question no line held. The eight accounts take it first, CLAIM-535, CLAIM-402 and CLAIM-794 take it beside their lines, and "inquiry as specification" moved to it from `record-as-apparatus`. Its line account is SYNTHESIS-118 (Proposed).

## 9. How the record operationalizes the theory

### 9.1 The record as an apparatus

In TERM-089's sense, the record's grammar is an apparatus for the record's own objects. CLAIM-469 (Active, demonstrated) states this: luria "realizes a system of distinctions that fixes what counts as a referable and governable object within the record, so that a split scheme makes one object two and a promoted vocabulary makes a value an entity". Its four functions are each mechanized:

| Function (TERM-089) | Mechanism in a luria record |
|---|---|
| **Differentiate** | Schemes, fields, vocabularies and relation types: what can be said of an entry and how entries can relate |
| **Retain** | Codes never reused; retirement by status; version history; `formerly` for earlier temporary codes; git |
| **Enforce** | Required fields; closed vocabularies; the linter and its `fail_on` patterns; CI on every pull request; generated worklists |
| **Revise** | Amendments to `luria.yaml` by decision record, with a first application in the same pull request (ADR-071); migrations; retrospectives and postmortems (ADR-115) |

The record also holds its own limit as a claim. "A typed relation is more constrained than either of its relata", so its rigidity is "a fact about the grammar, not evidence that the dependency it records is sound" (CLAIM-479, Active, demonstrated). The grammar is "fixed at any moment but amendable by decision", and a move it could not hold has "repeatedly been treated as a defect of the grammar and answered by amending it". Whether every such move is caught "is not shown" (CLAIM-419, Active, empirical). The predecessor's objection, that the grammar "formalizes early" so that a move fitting no type "is forced into one or lost until the misfit is noticed" (CLAIM-181, Proposed), is the theory's stage 1 of §7.2, stated about this record.

### 9.2 The inquiry tuple, realized

| Component of an inquiry (TERM-095) | What realizes it in a luria record | In Nucleation |
|---|---|---|
| **Language** | Schemes, fields, vocabularies, relation types: the relational vocabulary (TERM-091) | 13 schemes, 20 vocabularies and 69 topic terms on 20 November, 14 schemes on 21 November (RETRO); `rests_on`, `grounds`, `objects_to`, `bears_on` and others |
| **Answer space** | What can be said of an entry's standing and kind | QUESTION statuses (Open, Answered, Deferred, Dissolved, Superseded) and the "What would answer it" sections of their bodies; CLAIM status, `role` and `warrant`; CASE `standing` and `kind`; LIT statuses such as Unavailable and Unfetched |
| **Interventions** | Ways of acting on the world or the record | Reading a work (LIT → NOTE); executed studies (CASEs with scripts in `scratch/formal`); LEADs, planned interventions with a stage and priority |
| **Observations** | What comes back, including what the record shows of itself | NOTEs (Read, Skimmed); generated views; lint reports; counts such as CASE-178's; devlog notes taken during the work for the next retrospective (ADR-115) |
| **Criteria** | Conditions for changing standing and for admission | THEORY `promote_when`; CLAIM `defeated_if`; the test for a claim whose premises are claims (ADR-084), which since 21 November decides whether a synthesis also yields a claim, not whether it is kept (ADR-131, Active); ARG judgments on support; the owner's review; `fail_on` patterns |
| **Resources** | Rules that ration effort | The second-occurrence rule (ADR-032, ADR-072); CI doing what local runs could not afford (ADR-054); review triggers counted in use, not by the calendar (ADR-110 as divided by ADR-115); `Unfetched` routing work to the owner's time (ADR-053); the dialectic regime, which spends the owner's turns on the argument rather than on permission (ADR-127, Active) |
| **Reflexivity** | The tuple becoming the object | Decision records that amend `luria.yaml`; migrations; retrospectives and postmortems that `review` decisions; skills that encode review procedures; an adoption review of the decisions' own statuses (ADR-124, Proposed) |

The answer space and the criteria are themselves written in the language. A status is a vocabulary value, and a criterion is a field, a relation or a lint pattern. A grammar change can therefore revise what counts as an answer, not only what can be said. Part III finds that it sometimes did.

### 9.3 The principles, mechanized

Each principle of §7.1 has one or more mechanisms that operationalize it in the record. Most were adopted for local reasons, not to implement a theory. The correspondence is this paper's observation.

| Principle | How the record operationalizes it |
|---|---|
| **P1:** a distinction is needed when actions differ | Grammar changes are argued in decision records, with alternatives considered and rejected. In the record's first month, nine changes in ten came with one (CASE-178). ADR-042 rejected adding values to `standing` because it "would answer two questions with one field". Decisions are judged by their first application (ADR-071), so a distinction must show what it does. Since 21 November the dialectic regime applies the same test to interpretation: when a turn admits several readings *that would be filed differently*, each is filed as an alternative, and the owner chooses (ADR-127); a reading that would be filed the same way is not a distinction worth drawing. |
| **P2:** split, merge, re-carve | The grammar can add, split, widen, narrow, rename, retire and withdraw. Retiring by status keeps both the old and the new partition and the map between them. On 21 November it did three of these in a day: POSTMORTEM was split into RETRO and a narrower POSTMORTEM, its three entries reassigned (ADR-115); a line was added and an existing line's blurb narrowed (ADR-130); a work was renamed and carried through 23 entries (ADR-135). |
| **P3:** no self-certification | Readings are filed by one session and reviewed by another. The owner reviews every pull request. Status reviews and synthesis reviews read the argument with procedures that do not depend on how it was filed. The linter checks consistency, which the record's own claims say is not correctness (CLAIM-293, CLAIM-479). In the filing of 21 November ("Rich Get Richer Power Laws") the coverage reread and the synthesis audit were each done by a reader other than the drafters, and the synthesis review of that day gave each audit to a separate reader briefed neutrally (curation entries of 2026-11-21, 18:01 and 14:58). Drafters checked every number they filed by script, and so corrected eight of the other assistant's figures and attributions. |
| **P4:** naming is its own decision | The second-occurrence rule for process (ADR-072). The rule that an idea gets a code "when it has content of its own and is not already held" (ADR-072). Piloting a field on a sample before requiring it (ADR-043, ADR-056). A theme that recurs across lines becomes a line only after three tests: it answers a question no line holds, it recurs, and it would be found more easily as a line (ADR-129); short of that it stays a bridge. A tag, not a field, marks an owner's earmark, a field being "the next rung" if tags prove not enough (ADR-126). |
| **P5:** discrepancy, then capacity | The one misfit recent filings reported was listed and then sent to a decision (CLAIM-419, note of 12 November). The curation journal records what each filing left and why. Decision records name the discrepancy that occasioned them. Since 21 November a discrepancy met during the work is noted as it is met, in the devlog, tagged for the next retrospective (ADR-115), and one the owner earmarks must be answered by name (ADR-126). A filing now records each gap its source leaves, and fills the real ones or says why not (ADR-tmpcb96w, Proposed). |
| **P6:** three ledgers | Construction: the decision and its first application. Transition: migrations, recorded with counts. Maintenance: required fields, lint, the reviews that exercise a distinction. |
| **P7:** maintenance by intervention; support can erode | CI runs the checks on every change. Skills write review procedures down so that a fresh session can carry them out (DP-5, "no private brains"). DP-4 ("fire before trusting") requires a guard to be run against a deliberate failure before it is relied on. Postmortems review a change once it has been used. The owner's review of every pull request keeps the owner exercising judgment that assistants could otherwise take over. Since 21 November that review sits at the promotion from staging to main (ADR-121, ADR-125), and the decisions' own statuses are reviewed for whether the rule is in force (ADR-124, Proposed). An analytics pipeline recomputes the record's derived figures and reports how far the hand-coded census lags (§12.1). |
| **P8:** reflexive inquiry | `luria.yaml` is a versioned file changed, as a rule, by decision. Decisions are themselves entries with status and history. POSTMORTEMs `review` decisions and name the decisions their recommendations `prompted` (ADR-112); RETROs do the same for how work went (ADR-115). The rule on the dialectic regime was itself revised three times in a day at the owner's rulings, once on whether a restart is a new session (ADR-127, version 3). |
| **P9:** anchors and traceability | Anchors of the second kind, tied to the inquiry's earlier states: stable codes as exact addresses, read by each session rather than passed along. `rests_on`, `grounds` and `objects_to` as accountability structure. Retirement by status, never deletion. History notes with dates. `formerly`. The `works` field, which keeps a claim's membership in a manuscript apart from its standing, so that a manuscript is "a view over the argument and not its only copy" (CLAIM-178). Channels of the first kind, tying the record to its targets: readings of sources, independent audits and fact-checks, status reviews. Generated views, regenerated from their sources, so that they follow a revision. Two of 21 November's changes extend the second kind: a shared pull-request description is written only if its text is unchanged since last read (ADR-128), and the decoder of shared exchanges now accounts for every assistant message, in the file or in a closing count (pull request 608). |
| **P10:** the ladder of uptake | Admission: a contribution is filed. Recognition: it gets a code in apt terms, with the right type and vocabulary. Credibility: its status and warrant. Uptake: a claim `rests_on` it, or a synthesis integrates it. Revision of the standards of uptake: a decision that changes the grammar or the criteria. ADR-131 separated two rungs that ADR-075 had joined: a synthesis that fails the test as a claim is still filed, as an account of its scope, so failing at credibility no longer costs admission. |

### 9.4 The predecessor's concepts, realized

| Concept | Where argued | What realizes it |
|---|---|---|
| Anchor | CLAIM-182, CLAIM-185 (Proposed) | A code: stable, never reused, citable part by part |
| Identity stipulated by decision | CLAIM-195 | Versions, history notes, supersession, `formerly` |
| Trigger for coding | CLAIM-176, CLAIM-630 (Proposed) | The second-occurrence rule, now confined to process |
| Accountability structure | CLAIM-250 (Proposed) | `rests_on`, `grounds`, `objects_to`, ARG; the curation and workbench journals |
| Support recorded, strength not | CLAIM-293 | A known limit of `rests_on` and `grounds` |
| No computed withdrawals | CLAIM-664 | Retiring an entry reports its dependants and leaves each to judgment |
| Faithful migration | CLAIM-666 (Proposed) | A decision stating what moved; entries re-read and given history notes |
| An anchor is not shared knowledge | CLAIM-668 (Proposed) | Access to the record does not show that each collaborator knows an entry's current standing |
| Capture cost moved to the reader | CLAIM-179 (Proposed) | Agent filing, with the owner reviewing each pull request |
| Question drift | TERM-056 | QUESTIONs that `refine` one another, so a changed question is a new, related entry |

### 9.5 Four loops

Read through the tuple, the record runs four nested loops:

1. **Within the regime.** Filing readings, stating and revising claims, running studies, all in the grammar as it stands.
2. **On the regime.** A difficulty in the inner loop is diagnosed as a defect of the grammar. A decision records the diagnosis and the alternatives, a migration carries the change through, and validation makes it binding.
3. **On the argument.** Status reviews, promotion audits, and synthesis and reading reviews re-examine standing, independently of how entries were filed.
4. **On the tool.** Problems found in the record change luria itself, and luria's changes come back as new grammar.

Part III shows each loop at work. The second is the flywheel of §7.2.

Several of the decisions that created these mechanisms were applied long before they were adopted. On 20 November they included, still Proposed, ADR-079 (computed converses), ADR-082 to ADR-084 (accounts and line splits), ADR-087, ADR-089 and ADR-100 (further splits), and ADR-109 and ADR-111 (LEAD). An adoption review on 21 November (ADR-124, itself still Proposed) moved them, and 24 other decisions, to Active. That review is a procedure for catching exactly this gap. ADR-110, ADR-112 and ADR-115, which govern review of the record's changes, are still Proposed (§14.4), as is ADR-116, which put staging under all of it.

The third loop gained a stage on 21 November: every account whose scope crosses lines is audited at the synthesis review as a possible sign of a missing line (ADR-129). Its first run produced a line (ADR-130). The loop on the argument had changed the grammar before, through the line splits that synthesis reviews found (ADR-087, ADR-100); this time it added a line where the argument had outgrown the existing ones, rather than splitting one.

## 10. What operationalization does and does not establish

Section 9 shows a correspondence between the theory's principles and the record's mechanisms. Five cautions limit what that correspondence establishes.

**Mechanisms were mostly adopted for local reasons.** A decision was required for every new word in the closed topic vocabulary from the first day (ADR-001), before the record held any of Part I's claims. The second-occurrence rule was a throttle on flooding. Retirement by status was a convention inherited from Luria. The correspondence in §9.3 is therefore partly convergence: practices adopted to keep a record usable turned out to embody claims the record later argued for. Convergence is weaker evidence than design would be. It is also more interesting, because it suggests the principles describe constraints any such record meets. Since 21 November there is one exception by design: the line `learning-and-inquiry` was added for this paper's theme (ADR-130), so from then on any correspondence the line shows is not convergence. The decisions of that day were also written by participants who had this draft's principles in view, and several cite its open items (§18).

**Holding a claim is not operating on it.** The record holds CLAIM-602, which says support that does the work erodes the capacity it supports. Holding it does not show that the record's own use of assistants respects it. Operationalization is a property of mechanisms, not of content, and §9.3 lists mechanisms. Where no mechanism exists, as for measuring whether the owner's capacity to judge revisions is maintained, the principle is held and not operationalized (§17.1).

**A mechanism can embody a principle and still fail at it.** The record keeps its accountability structure in typed relations. Its own claims say that structure records that support exists, not how much (CLAIM-293), and that it decides no withdrawals (CLAIM-664). A shared record shows who proposed a claim and what standing it has. It cannot show what any collaborator believes, or that each knows the current standing (CLAIM-668, Proposed). The mechanisms are partial realizations, and Part III finds where they fell short.

**The grammar is not the inquiry.** Luria fixes what can be said of an entry, not what an entry says. A claim's content is open prose (CLAIM-479). The theory's principles about distinctions apply to the grammar, and through it to how the record can hold the argument. They do not apply directly to whether the argument is right. CASE-084, the perfectly accountable false theory, is the standing reminder.

**Operationalizing in a record is one choice among several.** The same principles could be built into a lab's protocols, a model's training loop, or an institution's rules. The record is the case studied here because it keeps a complete, dated history of its own changes. That makes it unusually observable, not uniquely suited.
