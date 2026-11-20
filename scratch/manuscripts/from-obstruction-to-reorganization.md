<!-- scratch/manuscripts/from-obstruction-to-reorganization.md -->

# From Obstruction to Reorganization: The Co-Evolution of Representation and Governance in an AI-Assisted Research Record

*Working title. Alternative: "Nucleating an Inquiry: A Longitudinal Case Study of Reflexive Research Infrastructure."*

> **Status of this file.** A full working draft of the manuscript sketched in the ChatGPT exchange "Branch · Audit Luria Evolution" (2026-11-20). That exchange produced an abstract, an outline and the measurements in its U11 attachment. This draft writes them out as prose. It is kept under version control in `scratch/` as a working document, and it is **not part of the record**: luria does not read this directory, and codes cited here are cited in their bare form. Figures come from three observation points, which are kept apart in §4.1. Items that need the owner's decision before submission are collected in Appendix C. Wherever the draft depends on a decision that is still Proposed, it says so.

---

## Abstract

Persistent research records can give long-running AI-assisted inquiry its continuity. Their representational structures also limit which distinctions can be expressed, which contributions can bear on an argument, and which discrepancies can be recognised as problems at all. As an inquiry develops, those structures can become inadequate in their turn. A category may conflate circumstances that call for different responses. A relation may carry an inferential commitment its author did not intend. An entry type may turn out to be the wrong vehicle for the work it was meant to organise.

We present a longitudinal case study of Nucleation, an AI-assisted research project whose memory is a record kept with Luria, a configurable system of typed, versioned and interlinked documents. Between 25 September and 19 November 2026 the record grew from 214 to 10,070 files. Over the same period its local schemes grew from five to twelve, its configured vocabularies from six to eighteen, and its configuration from 482 to 2,380 lines. We reconstruct episodes in which a representational difficulty met in the course of inquiry was followed by a reorganisation. The episodes are vocabulary splits, an added orthogonal classification dimension, scheme boundaries redrawn and one abstraction withdrawn, and lines of inquiry decomposed. We also report the decisions not to add structure.

The added distinctions are in use. Fourteen of the eighteen possible combinations of CASE kind and standing are populated. Among 766 claims, 39 are Proposed with a demonstrated warrant and 185 are Active with an interpretive one, so the kind of support a claim has and the record's acceptance of it vary independently.

The reorganisation of representation was coupled to the development of governance. Architectural decision records stated why a change was made. Migrations applied it to existing entries, and executable checks made it consequential. In the record's first 32 days, 94% of newly added vocabulary values were used in the same unit of work that added them, and 91% of the units that added one also carried a decision record, against 16% of all pull requests. A later mechanism, the POSTMORTEM, made retrospective review of decisions a record type of its own. In one documented cycle, a review found that the research-backlog scheme's stage field failed to discriminate between entries. The revision that followed reduced the share of entries at the first stage from 96.4% to 69.2%.

We read these episodes through the record's own account of obstruction as an occasion for capability reorganisation. That account holds that an unresolved discrepancy can occasion a new distinction or a new channel of action, but does not guarantee one. On this reading, what changed was not just how information was stored but which distinctions, inferences and actions remained available to later inquiry.

The case documents a process that the owner directed and AI assistants carried out. It does not show that assistants can diagnose representational inadequacy on their own. We identify the observable signatures that preceded each reorganisation and propose evaluations of whether an assistant could detect them unprompted.

---

## 1. Introduction: inquiry can outgrow its representation

### 1.1 The continuity problem

A long-running inquiry conducted with AI assistants has a memory problem that is not solved by keeping transcripts. Each session starts without the last one's working context. What must survive is not only information but structure: what has been asserted, on what grounds, which objections bear on it, which questions it answers, what has been withdrawn and why. A summary keeps the gist and loses the identities. A transcript keeps everything and makes nothing addressable.

A structured record can supply both identity and relation. Each claim has a code, each objection names its target, and each change of mind is a change of status rather than an overwrite. But building such a record means deciding in advance what kinds of epistemic object exist and how they may relate. That decision is the subject of this paper.

### 1.2 The rigidity problem

The structure that makes a record dependable also makes it fallible in a particular way. No inquiry can anticipate every distinction it will need. A grammar designed around the first month's work can misfile the second month's contributions. It can collapse two independent dimensions into one field, or let a relation say more than its author meant. The record then preserves the mistake as faithfully as it preserves everything else.

So the problem is not only how to preserve an inquiry in a record. It is also how to preserve the inquiry's ability to challenge the record's organisation. A record that cannot be reorganised forces new contributions into old categories. A record that is reorganised without discipline loses the continuity it was built to provide.

### 1.3 Research question and contributions

**Research question.** How can an AI-assisted research project reorganise its representational and governance capabilities in response to difficulties met during inquiry, and what does that process require?

The paper contributes:

1. A longitudinal reconstruction of how one project's Luria configuration and governance mechanisms evolved over its first eight weeks (§§4–7).
2. A comparative analysis of eight representational interventions: vocabulary refinements, an orthogonal classification dimension, a scheme boundary redrawn, an abstraction withdrawn, inquiry decomposition, and deliberate restraint (§6).
3. Quantitative evidence on how fast the representation grew, whether new distinctions came into operational use, and what migration work conceptual reorganisation cost (§§4–6).
4. A worked account of the shift from recording architectural decisions to reviewing their consequences, through the POSTMORTEM mechanism and one complete review-and-revision cycle (§7).
5. An analysis of the observable *signatures* that preceded each reorganisation, offered as a starting point for delegating the diagnosis of representational inadequacy to AI assistants (§8.7), with evaluation designs to test whether that delegation works (§9).

### 1.4 The argument in brief

The record's representation was not simply extended to hold more material. It was repeatedly revised when its schemes, vocabularies and relations failed to keep apart what the inquiry needed to keep apart. Each revision changed what the record could distinguish, which inferences it could express, and how later work could be organised. The decision records kept the reasons for these changes. Migrations and executable checks made them binding. The POSTMORTEM made the consequences of past decisions evidence for revising them.

Nucleation thus shows an AI-assisted inquiry progressively institutionalising three activities: recognising the limits of its own representational apparatus, correcting them, and evaluating the corrections. It shows this as a process the owner directed. Whether an assistant can take over the recognition step is the next question, and the record makes it a testable one.

---

## 2. Background: Luria as an inquiry apparatus

### 2.1 Representational architecture

Luria is a command-line tool and a set of conventions for keeping a project's memory as plain files under version control [ref: luria repository]. Its configuration file, `luria.yaml`, declares:

- **Schemes:** typed document families with stable codes, such as `LIT-1631` or `CLAIM-532`. A document's code is never reused. Documents are retired by status and never deleted.
- **Fields,** required or optional per scheme, and **vocabularies,** some closed and some configured, from which certain fields must draw. Topic tags, for example, come from a closed list in which every value was chosen and described by someone.
- **Typed, directional relations** between documents, such as `rests_on`, `grounds`, `reviews` and `advances`. Each relation can declare a converse, which Luria computes for every reader rather than storing.
- **Statuses** that encode standing, such as Proposed, Active, Superseded or Rejected, and the history notes and supersession links through which standing changes.
- **Generated views:** indexes by field value, line, topic and relation. These are built from the authored documents and never edited by hand.
- **Validation and repair:** a linter that enforces the configuration, and a repair step that writes link targets and normalises sources.

The distinction between authored documents and generated projections matters to the argument. A generated view makes a relationship visible without creating a second, independently maintained copy of it. When the authored source changes, the view follows. This is the record's design principle DP-2, that a hand-maintained projection of a source of truth will drift and so should be derived.

### 2.2 Nucleation

Nucleation began on 25 September 2026 as the catchall companion to a separate record, the Anthology of the SOTA. It was scaffolded with three schemes for reading: LIT (a work), NOTE (a reading of it) and THEORY (a claim about what is true, with its evidence). It also carried decision records, design principles and a closed topic vocabulary seeded from the clusters of reading the anthology could not hold (ADR-001). Its scope widened on 19 October to any work the owner wanted filed (ADR-048).

The record soon came to hold more than readings of other people's work. On 7 October, ADR-032 added five schemes for the record's *own* argument: QUESTION, CLAIM, CASE, TERM and ARG. A CLAIM carries a credence (its status) and a voice (its role: thesis, counter, granted, and so on), with typed premises. Later schemes added SYNTHESIS, an account of what a scope of the argument holds; LEAD, a research opportunity with a stage and a status; and POSTMORTEM, a review of how a change has worked out. By 20 November the record held 2,935 LITs, 2,217 NOTEs, 2,129 THEORYs, 766 CLAIMs, 497 QUESTIONs, 298 CASEs, 131 TERMs, 123 ARGs, 108 SYNTHESISes, 198 LEADs, 114 ADRs and 3 POSTMORTEMs.

### 2.3 Who did what

The account depends on keeping roles apart, so we state them at the outset.

- **The owner,** a single human researcher, set the inquiry's direction. The owner initiated or ratified every architectural intervention examined here. In the record's own words, the changes to the grammar were "driven by" the owner.
- **AI assistants** (Claude Code sessions working on the repository, and ChatGPT in exchanges that the owner later filed) read sources, drafted entries, proposed decision records, carried out migrations, ran audits and wrote the postmortems. Assistants often *proposed* the shape of a change. They also often surfaced the evidence that a change was needed, for example by counting misfiled entries. None changed the grammar without the owner's request or approval.
- **Executable mechanisms** (the linter, the repair step, the CI job that runs both on every pull request) enforced what had been decided.
- **Repository review,** in which every change is a pull request and decisions are merged by the owner, made each change inspectable.

Assistant participation in implementation and review should not be mistaken for autonomous architectural judgment. The historical record cannot show the latter, and §9 proposes how it might be tested.

### 2.4 An operational account of the apparatus

The record holds its own account of what Luria is. TERM-089 defines an *apparatus*, in an operational sense that presupposes no observer: a realised organisation that selectively couples differences in one system to distinguishable outcomes in another. It names four functions that can come apart:

| Function | What it does in the record |
|---|---|
| Differentiation | Makes some distinctions expressible and actionable |
| Retention | Keeps identities and commitments across change |
| Enforcement | Makes constraints consequential for subsequent work |
| Revision | Changes the criteria of discrimination themselves |

CLAIM-469 (Active) holds that Luria is an apparatus in this sense for the record's objects. Splitting a scheme makes one object two, and promoting a vocabulary makes a value an entity. The grammar's distinctions are revised through the record's own use. A stronger thesis, that the record *constitutes* its objects in something like Barad's sense (LIT-1657), is held separately as CLAIM-476 and is still Proposed. This paper needs only the operational claim. Its subject is how the fourth function, revision, developed, and how it came to be governed.

---

## 3. Related work

**Ontology and schema evolution.** The knowledge-engineering literature has long treated ontology change as a managed process. Stojanovic et al. (LIT-2514) set out a user-driven evolution process with change capture, representation, semantics of change, propagation, implementation and validation. Flouris et al. (LIT-2499) survey and classify ontology-change operations. In model-driven engineering, COPE (LIT-2479) automates the *coupled* evolution of a metamodel and the models that instantiate it. That is the same coupling Luria's migrations perform by hand and by script. Our case differs from these settings in three ways. The schema is changed in the course of the inquiry it serves, not by a separate maintenance team. The occasion for a change is an argumentative difficulty, not a requirements change. And each change is accompanied by a decision record and a first application. QUESTION-458 (Open) asks whether this coupling of schema change to recorded decision, migration and executable checks is what distinguishes Luria from ontology and metamodel evolution. This paper offers evidence on the descriptive half of that question.

**Classification and its consequences.** Bowker and Star (LIT-1631) showed that classification systems are never neutral. Each valorises some points of view and silences others, and the work of fitting cases to categories is mostly invisible. Our cases are small, explicit instances of their thesis. A category that conflates two situations makes one of them unrecordable, and recovering it costs a migration.

**Organisational learning.** Argyris's distinction between single-loop and double-loop learning (LIT-745) maps closely onto ours. Single-loop learning corrects an action within fixed governing variables. Double-loop learning revises the variables themselves. Re-filing a misfiled entry is single-loop. Changing the vocabulary that misfiled it is double-loop. The record's own CLAIM-422 adds a third distinction, between a corrective act, an executable procedure and a *maintained* corrective capacity, which we use in §8.3.

**Postmortems.** Blameless postmortem practice in site reliability engineering (LIT-2784, LIT-2785) treats an incident as evidence about a system rather than a person. Its products are recommendations with owners. Nucleation's POSTMORTEM adapts the practice to a different object: not an outage, but a change to the record's grammar or process once it has been used.

**Architectural decision records.** Lightweight decision records, each stating context, decision, alternatives and consequences, are an established software-engineering practice [ref needed: Nygard 2011, "Documenting Architecture Decisions"]. Nucleation uses them for every grammar change. It adds a rule that a decision travels in the same pull request as its first application (ADR-071), so that a reviewer judges the rule by what it does.

[Owner: decide whether related work should also cover research-notebook and argument-mapping tools, and prior literature on LLM agents with persistent memory. Neither is on the record yet.]

---

## 4. Method and materials

### 4.1 Evidence and observation points

The study draws on the version-controlled record from its scaffold on 25 September 2026: dated repository snapshots, `luria.yaml` diffs, decision records, curation and workbench journals, changelog fragments, migration commits, generated indexes, CI workflows and postmortems. The quantitative evidence comes from three observation points, which we keep apart:

| Observation point | Source | Used for |
|---|---|---|
| **Historical snapshots** at the end of 25 Sep, 15 Oct, 1 Nov and 19 Nov (UTC) | Repository history at dated commits | Growth of the record and its configuration (§4.4) |
| **Executed studies inside the record** | CASE-178 (first 32 days after the scaffold) and CASE-180 (first 50 days, 1,434 commits, 5,034 documents), both run on 27 Oct | Rates of grammar change and of revision (§§4.5–4.6) |
| **Current generated indexes,** 20 Nov | Field values of every current entry | Classification cross-tabulations (§6) and governance census (§7) |

Two consequences follow. The cross-tabulations describe the record *after* every intervention discussed. They show that the distinctions are in use, not when each began to be used. And the LEAD comparison in §7.4 sets the 197 entries counted in POSTMORTEM-002 against the 198 in the later index. It is a change in distribution, not a fixed-cohort estimate of individual transitions.

### 4.2 Unit of analysis

The unit is a **representational intervention**, reconstructed where the record permits as a sequence:

> encountered difficulty → diagnosis → alternatives → decision → migration → operational consequence → later review.

Not every episode has every stage. Early episodes have no later review, because no review mechanism existed. Whether a stage is present is itself a datum about how governance developed.

### 4.3 Typology and evidential tiers

We classify interventions as: (a) refining a vocabulary; (b) adding an independent classification dimension; (c) revising the boundary between schemes; (d) withdrawing an abstraction; (e) decomposing a line of inquiry; (f) changing the mechanisms that govern future change; and (g) declining to add structure.

We separate three kinds of evidence:

1. **Recorded rationale:** what the decision record says the difficulty was and why the change answered it.
2. **Observed operation:** what the implemented representation now distinguishes, as shown by populated fields and cross-tabulations.
3. **Measured outcome:** whether the change improved later research, coordination or correction.

The record is strong on the first, moderate on the second and weak on the third. We say which tier each finding rests on.

### 4.4 Growth of the record and its grammar

| Measure | 25 Sep | 15 Oct | 1 Nov | 19 Nov |
|---|---:|---:|---:|---:|
| Repository files | 315 | 4,072 | 7,599 | 11,124 |
| Files under `record/` | 214 | 3,419 | 6,877 | 10,070 |
| Local record schemes | 5 | 10 | 10 | 12 |
| Configured vocabularies | 6 | 14 | 14 | 18 |
| Topic values | 19 | 62 | 67 | 69 |
| `luria.yaml` lines | 482 | 1,469 | 1,757 | 2,380 |

*Figure 1 (to draw): both series indexed to 25 Sep = 100. Record files rise to about 4,700, configuration lines to about 490.*

Record files grew about 47-fold and configuration lines about 4.9-fold. The two are different quantities, and line count is a poor proxy for semantic complexity. Still, the comparison shows that the grammar did not grow in proportion to the material it held. Most growth in the corpus was absorbed by existing structure. The grammar grew in steps: five new schemes by mid-October, a plateau through the end of the month, then SYNTHESIS, LEAD and POSTMORTEM in November.

### 4.5 Grammar change as part of ordinary work

CASE-178, an executed study the record ran on itself, read every change to `luria.yaml` in the first 32 days after the scaffold:

| Kind of addition | Additions | Days with one |
|---|---:|---:|
| Documents | 5,030 | 32 |
| Vocabulary values | 106 | 18 |
| Fields and relations | 79 | 8 |
| Whole vocabularies | 8 | 3 |
| Schemes | 5 | 1 |
| Remote projects | 1 | 1 |

The ordering by frequency matches the owner's prior guess: documents, then values, fields, vocabularies, schemes, projects. But the study's main finding is about *how* refinements arrived, not how often. **94% of the 106 new vocabulary values were used by a document changed in the same unit of work.** Decision records accompanied the units that changed the grammar far more often than other units:

| Work units | Included a decision record |
|---|---:|
| All 296 pull requests in the period | 16% |
| 35 units adding a vocabulary value | 91% |
| 9 units adding a field or relation | 89% |
| 4 units adding a vocabulary | 75% |
| 2 units adding a scheme | 100% |

CASE-178 concludes that the levels of the grammar are not slower processes of their own. They are rarer events within a single loop of work. The grammar was refined in the pull request that needed the refinement, and nine times in ten it was justified in writing. This is tier-2 evidence for the coupling QUESTION-458 asks about. The comparison with all pull requests is not controlled for the size of the unit, and the events are not independent. Nor does the study show that every misfit was noticed. It covers only the misfits that led to an amendment.

### 4.6 Different rates of persistence

CASE-180 measured how often each layer of the record changes, using 1,434 non-merge commits over the first 50 days. After drafting was over, an entry's prose was revised about once in 21.8 days, its status about once in 127.5 days, and an authored relation was gained or lost about once in 131.9 days. None of the 68 declared relation types was redefined, although new types continued to be added.

These are inverse event frequencies, not relaxation times. A 50-day window cannot estimate a 128-day process, and the study says so. What they support is narrower. The record's layers are revised at rates one to two orders of magnitude apart, and the grammar is slow to revise without being slow to grow. CASE-180 also found that on the first day of an entry's life all layers change together. The ordering appears only once drafting is over.

**Transition.** The machinery was stable under ordinary use and still amendable when the work exposed a need. The next section examines the amendments.

---

## 5. Encountering obstruction: what the cases have in common

Before the cases, a word on what counts as an *obstruction*. In each episode below, some piece of inquiry could not be recorded faithfully with the grammar as it stood. The contributor then had three options. They could force the contribution into the nearest category, losing a distinction. They could put the distinction into free prose, where no index, relation or check could reach it. Or they could stop and amend the grammar. CLAIM-419 (Active) records that the record has repeatedly treated "a move that fit no scheme or relation" as a defect of the grammar and answered it by amendment. It also records that whether every such move is caught is not shown.

The cases differ in which of the first two options the obstruction had already produced by the time it was noticed. That residue is what an assistant might learn to look for (§8.7).

---

## 6. Comparative cases of representational reorganisation

Each case gives the obstruction, the diagnosis and the alternatives weighed, the decision, the migration, and what the change now does. Figures for migrations are as reported by the decisions themselves. Figures for current use come from the indexes of 20 November.

### 6.1 Vocabulary refinement: agent, individual, self and person (ADR-015, ADR-024)

**Obstruction.** On 2 October ADR-015 added `self-and-personhood` to the topic vocabulary. At the same time it narrowed `identity` to `individuation`, the identity of things of any kind. Within two weeks the new word was carrying four senses that the readings needed to keep apart: what an agent is, what an individual is, what a self is, and what a person is. It was also carrying four different kinds of unity: behavioural integration, phenomenal unity, narrative unity and normative self-governance. Prose in several THEORY entries had begun to slide between senses.

**Diagnosis and alternatives.** The owner asked that agent, individual, self and person not be treated as synonyms, and that the four unities be represented separately. Two alternatives were rejected: subtopics under one word, and leaving the distinctions to prose.

**Decision.** ADR-024 retired `self-and-personhood` into `self` and `personhood`, alongside `agency` and `individuation`, and added four words for the unities: `behavioral-integration`, `phenomenal-unity`, `narrative-unity` and `self-governance`.

**Migration.** Forty-two documents were retagged and twenty-one more received a unity word. Several entries' prose was corrected where it had conflated senses of "self". The decision names four Proposed THEORYs among the documents it corrected.

**What it changed.** The refinement reached interpretation, not only retrieval. Once the predicates were separate tags, a reading could say that a system has behavioural integration without phenomenal unity, and the record could gather everything filed on one without the other. Tier 1 and tier 2: the rationale is recorded, and the tags are in use.

**Role in the paper.** This is the primary illustration of *conceptual differentiation*. A vocabulary change became a change in what the record's readings could say.

### 6.2 Action-guiding refinement: Deferred, Unavailable, Unfetched (ADR-041, ADR-053)

**Obstruction.** The status `Deferred` on a LIT held two situations: a work nobody had yet tried to read, and a work whose lawful full text had been sought and not found. These call for different next actions. The first should be read. The second needs a copy to be found, or the owner to supply one.

**Diagnosis.** When ADR-041 was written on 13 October, 177 of the 345 Deferred LITs carried a free-text status note recording a failed search. The distinction was already being made, but only in prose, where no index could find it.

**Decision 1.** ADR-041 added `Unavailable` ("no copy reached"), and `Deferred` kept "no attempt recorded". The 177 moved. ADR-041 considered a further split, between no lawful copy found and a copy found that this client could not fetch, and declined it: "eight entries do not justify a sixth status."

**Decision 2.** On 25 October the owner supplied two such works by hand. The owner asked for a status for "content that would be easy for me to access where you encountered obstacles". ADR-053 added `Unfetched`. A triage reclassified the relevant Unavailable entries. ADR-053 also made the owner's queue a generated page, the Unfetched status page, rather than a list kept by hand that would go stale.

**What it changed.** Today 2,935 LITs divide into 2,114 Active, 531 Unavailable, 179 Unfetched and 58 Deferred, with smaller counts at other statuses. Each status maps to a different worklist and a different actor. This is the clearest case in which a refined distinction supports *different operations*, not just a finer taxonomy.

**Role in the paper.** It also shows that a distinction declined once can become warranted later. In ADR-041's terms the second case was too rare to deserve a status. ADR-053 was prompted by a change in what the distinction was *for*: routing work to the one person who could act on it, not counting it.

### 6.3 An independent dimension: CASE kind against standing (ADR-042)

**Obstruction.** CASE entries carried a `standing` field (documented, stipulated or fictional) that said how much of a case is fact. Readers had been using it to say what *kind* of case it was. The owner asked whether the record could tell apart "proposed empirical experiments vs thought experiments vs steel-man vs etc." A survey of all 81 cases found `stipulated` alone holding proposed studies, thought experiments, formal constructions and real counterfactuals.

**Alternatives.** Four were weighed. Adding values to `standing` was rejected because it would "answer two questions with one field, which is the present problem". A separate STUDY scheme was rejected: a study is used by claims exactly as a case is, through the same relations, so a second scheme would split the index and the relations. Tags were rejected because topics say what something is about, not what it is. Finer kinds were rejected with the remark that "six is what the 81 cases need".

**Decision and migration.** ADR-042 added a required `kind` field drawing on six values: specimen, thought experiment, construction, reported study, proposed study and executed study. All 81 cases were classified in the same pull request.

**What it changed.** By 20 November the record held 298 CASEs:

| Kind | Documented | Stipulated | Fictional | Total |
|---|---:|---:|---:|---:|
| Specimen | 61 | 13 | 0 | 74 |
| Thought experiment | 1 | 24 | 29 | 54 |
| Construction | 2 | 38 | 51 | 91 |
| Reported study | 12 | 0 | 0 | 12 |
| Proposed study | 0 | 54 | 1 | 55 |
| Executed study | 3 | 7 | 2 | 12 |
| **Total** | **79** | **136** | **83** | **298** |

Fourteen of the eighteen combinations are populated. Constructions and thought experiments occur under all three standings. Executed studies, which include the record's studies of itself, occur under all three too. So kind does not determine standing, nor standing kind. The two fields are *conceptually* distinct. They are not *statistically* independent, and could not be: a reported study is documented by its nature. Tier 2.

*Figure 2 (to draw): a 6 × 3 heatmap of the table above.*

**Role in the paper.** This is the cleanest quantitative exhibit of a second dimension in use. It also contains a negative case in the rejected STUDY scheme, discussed in §6.8.

### 6.4 An independent dimension: CLAIM warrant against status (ADR-043)

**Obstruction.** During an exchange on 14 October, an assistant wrote of separating "what we've demonstrated by construction, what we've made plausible through examples, and what still requires empirical evidence". The owner asked whether anything in the record already segregated claims this way. Nothing did. `status` said whether the record accepted a claim, and `role` said in whose voice it was made. Neither said *how* the claim was supported.

**Decision and migration.** ADR-043 added a `warrant` field with three values: demonstrated, empirical and interpretive. It was piloted on the thirteen claims from that exchange before being made required. The pilot settled a hard case: an empirical hypothesis with no observation under it is interpretive. Once the field was required, eight readers classified the remaining 289 claims the same day, each reading every claim in their batch in full. That brought the total to 315: 87 demonstrated, 12 empirical, 216 interpretive. The owner described the lint failures this produced as "a forcing function to make you fill in the field. This is a feature, not a bug."

**What it changed.** Among 766 claims on 20 November:

| Warrant | Active | Proposed | Deferred, Rejected, Superseded | Total |
|---|---:|---:|---:|---:|
| Demonstrated | 198 | 39 | 6 | 243 |
| Empirical | 10 | 20 | 1 | 31 |
| Interpretive | 185 | 262 | 45 | 492 |
| **Total** | **393** | **321** | **52** | **766** |

Thirty-nine Proposed claims have a demonstrated warrant. These are typically constructions whose proof is done but whose role in the argument the owner has not yet accepted. One hundred and eighty-five Active claims rest on interpretation. The two fields therefore cannot stand in for each other. Every claim carries a warrant, which shows that the field was adopted. It does not show that every assignment is correct. Tier 2.

**Role in the paper.** Paired with §6.3, this provides the quantitative core. It also shows a distinction proposed by an assistant during substantive work, recognised by the owner as missing from the grammar, and piloted before being required.

### 6.5 Redrawing a scheme boundary: CLAIM and ARG (ADR-032, ADR-061)

**Obstruction.** ADR-032 created ARG for judgments about inferences, as distinct from substantive claims. It said an ARG should be filed only when something needed to point at an inference. After 10 October no ARG was filed for more than two weeks. Objections of exactly the kind ARG was built for kept coming, and they were filed as CLAIMs. A reading of all 453 claims found 42 whose subject was whether one entry supports another.

**Why it mattered.** An objection to an inference filed as a CLAIM looks like a rival substantive position. The record could not say "this conclusion may be right, but this argument for it fails" without seeming to dispute the conclusion.

**Decision.** ADR-061 redrew the boundary. An ARG is any claim about support, and a claim about what a source says is a THEORY.

**Migration.** Twenty-nine ARGs were filed (15 Rejected, 13 Proposed, 1 Active). Fourteen CLAIMs were superseded by them, and fifteen more were split along their subject matter. This was not relabelling. Each entry had to be read to decide whether it asserted something about the world or about an inference.

**What it changed.** The record now holds 123 ARGs. Thirty-five are Rejected, meaning the record judges those inferences to fail without thereby judging their conclusions. Disagreement about support and disagreement about truth have separate addresses.

**Role in the paper.** This illustrates *redistributed inferential responsibility*. The change altered which kinds of disagreement the record can express without misdirection.

### 6.6 Withdrawing an abstraction: SYNTHESIS and CLAIM (ADR-075, ADR-076, ADR-083, ADR-084)

**Obstruction.** Filed sources often contained syntheses: executive summaries, recaps, "refreshed" positive accounts. Filing mapped each item to its source turn and left the integration with no address of its own. As a result the record could not say what its current account was, and later syntheses could not be checked for drift (ADR-075).

**First design.** ADR-076 gave syntheses a scheme, SYNTHESIS, with an admission route. An integration that added something to its components could be admitted with statuses of its own. Some admitted syntheses were in fact *new propositions*. Keeping them in SYNTHESIS required accommodations so that they could carry a credence and a voice, and stand as premises.

**Diagnosis.** Asked what the admitted syntheses added, the record's answer was one proposition each, with a credence, a voice, a warrant and a defeater. Those are a CLAIM's fields. The owner observed that such an addition *is* a claim, and a claim is atomic however many premises it has.

**Decision.** ADR-084 (Proposed) refocused SYNTHESIS: it is an account of a scope of the argument and asserts nothing of its own. Anything that adds to its components is a CLAIM. ADR-076 was superseded, and ADR-083 gave each line or part of a line one account.

**Migration.** Eleven admitted syntheses returned to CLAIM, nine of them under the claim codes they had held before admission. SYNTHESIS now holds 108 entries: 97 Proposed accounts and 11 Superseded.

**What it changed.** The grammar *lost* an abstraction it had briefly held, a SYNTHESIS that asserts. The test for admitting a synthesis became the test for filing a claim whose premises are claims.

**Role in the paper.** This is the primary architectural example, because it shows that reorganisation is not monotone differentiation. An apparatus can make a distinction that does not earn its keep, and it can also unmake it. The episode has every stage: an attempted abstraction, mounting complications, a diagnosis, a reversal and a migration.

### 6.7 Decomposing an inquiry: splitting lines (ADR-082, ADR-087, ADR-100)

**Obstruction.** Each entry in the record's argument carries one or more `line` values, which name the inquiry it belongs to. When the record tried to write an account (a SYNTHESIS) of the `nucleating-argument` line, the account fell into five parts (ADR-083). Three of them, drift, anchors and the costs of anchoring, were densely linked to one another. The other two were not. "What a record of a developing argument keeps" had 25 relations inside it, 8 out and 3 in. "The record as its own apparatus" had 24 inside, 6 out and 1 in.

**Decision.** ADR-082 (Proposed) split the line in three: `nucleating-argument`, `records-of-inquiry` and `record-as-apparatus`. Forty-three entries were reassigned. ADR-083 made the test general: a line whose parts barely relate is a candidate to split.

**Replication.** The same test later split `readiness`, moving 30 entries to `transient-support` (ADR-087), and `organizational-normativity`, moving 29 entries to `dependence-and-domination` (ADR-100).

**What it changed.** A line is not just a topic label. It is the unit within which an argument is maintained, summarised and audited. Splitting one changes what counts as a single argument. This paper's own subject sits in the `record-as-apparatus` line that the first split created.

**Role in the paper.** This shows the *structure of inquiry itself* being revised. The diagnostic was quantitative (relation density inside and across parts) and was reapplied twice.

### 6.8 Negative cases: deciding not to differentiate

A record that only ever added distinctions would be evidence of accretion, not judgment. Four episodes show the contrary.

- **Widening instead of adding (ADR-036).** Readers of the 9 October batches on trained networks reported, independently and repeatedly, that the vocabulary had no word for training dynamics, and they used `learning-theory` loosely for it. The symptom was the same as in §6.1: one word covering several senses. The owner ruled that the word's description should be widened rather than a new word added.
- **A rejected scheme (ADR-042).** The separate STUDY scheme was rejected because studies are used by claims exactly as cases are. A second dimension inside CASE was preferred to a second scheme. (A later need for structured fields on proposed studies was met by LEAD, a different object: a plan, not a case.)
- **A distinction declined, then adopted (ADR-041 → ADR-053).** The sixth status was refused at eight entries and adopted when its purpose changed (§6.2).
- **A distinction falsified by its own pilot (ADR-056, Rejected).** The owner suggested that many TERMs might share a "kind" worth distinguishing. ADR-056 proposed four kinds of TERM: disambiguation, construct, criterion and position. It required a pilot before the field could be adopted. Of sixteen sampled TERMs, eleven sorted cleanly and five forced an arbitrary choice, especially between construct and criterion, which was exactly where the field was meant to decide something. The decision was rejected on its own evidence.

**Cross-case finding.** Representational development in Nucleation involved differentiation (§§6.1–6.4), redistribution (§6.5), withdrawal (§6.6), decomposition (§6.7) and deliberate restraint (§6.8). The common factor is not more structure. It is that each change answered a specific failure to keep apart, or to hold together, what the inquiry needed.

### 6.9 Migration as reinterpretation

| Intervention | Documented migration |
|---|---|
| Self and personhood split (ADR-024) | 42 documents retagged; 21 given a unity topic; prose corrected |
| Deferred → Unavailable (ADR-041) | 177 LITs moved |
| CASE `kind` (ADR-042) | 81 cases classified |
| CLAIM `warrant` (ADR-043) | 315 claims classified by nine readings (pilot + eight readers) |
| CLAIM / ARG boundary (ADR-061) | 29 ARGs filed; 14 claims superseded; 15 split |
| SYNTHESIS withdrawn (ADR-084) | 11 syntheses returned to CLAIM, 9 under original codes |
| `nucleating-argument` split (ADR-082) | 43 entries reassigned |
| `readiness` split (ADR-087) | 30 entries reassigned |
| `organizational-normativity` split (ADR-100) | 29 entries reassigned |
| LEAD stage revision (ADR-111) | 53 leads idea → specified; 1 → costed; priorities backfilled |

The point of the table is not the totals. It is that almost every migration required *reading*: deciding of each entry which side of a new line it fell on. Reorganising the grammar meant reinterpreting the record. That is why a grammar change costs more than editing a configuration file suggests, and it is the cost that §8.4 weighs.

---

## 7. From architectural decisions to reflexive governance

### 7.1 Decision records as accountable change

Every intervention in §6 has a decision record. The record holds 114 decision records: 70 Active, 37 Proposed, 5 Superseded, 1 Deferred and 1 Rejected. The format is context, decision, alternatives and consequences. It is supplemented by two rules the record gave itself. First, each logical unit of work gets its own branch and pull request, and a decision travels with its first application, which cites it by temporary code (ADR-071). A reviewer therefore approves a rule by what it does, and history leads from the rule to what it changed. Second, the "second-time rule" governs the record's *process*: a decision or principle is written when its occasion recurs. It does not govern the record's insights, which are filed when they have content of their own (ADR-072).

### 7.2 Making decisions operational

A decision recorded in prose is followed only when someone remembers it. The record's design principle DP-3, "culture must be compiled", names the ladder a norm climbs: prose, convention, mechanism, guarantee. Many interventions in §6 climbed it. `kind` and `warrant` were made required fields, so the linter refuses an entry without them. Converse relations are computed and never hand-written. Link targets are spelled by the repair step, never by the author. The CI job repairs and lints every pull request (ADR-054), which removed a costly manual step: at the record's size a local repair-and-lint pass had come to take more than ten minutes.

Compilation has a cost the record has documented itself. CASE-131 records "the graph that asserted an inference nobody made": filing one claim as supporting another made the link fixer write that the other *rested on* it. The tool consistently reproduced a commitment no author had made. CLAIM-479 (Active) generalises the point. A typed relation is more rigid than the prose at either end, so its rigidity is a fact about the grammar, not evidence that the dependency it records is sound. A formally valid record can reproduce a mistaken inference reliably.

### 7.3 POSTMORTEM: a second-order mechanism

Until 19 November the governance apparatus recorded *why* a change was made, not *how it had worked out*. Two decisions changed that. Both were still Proposed when the measurements were taken.

- **ADR-112** created POSTMORTEM, a review of how a change to the record has worked out once used. A POSTMORTEM `reviews` the decisions behind the change, with converse `reviewed_by` derived on the decision. It links the pull requests that carried the change and the discussions that asked for the review, and it names the decisions its recommendations `prompted`.
- **ADR-110** says when a postmortem is due. There are six triggers: a schema change that has been used (about 20 entries, or the end of the first session that used it); a batch of five or more pull requests in a session; a bulk filing of more than about 50 entries; a decision revised soon after landing; a process incident such as CI failing twice on the same cause or a revert; and an explicit request from the owner. The triggers count use and sessions, not calendar time, because the record moves at about ten pull requests, a few hundred entries and two decisions a day. The assistant checks the triggers when a batch closes. Leaving reviews to the owner's request alone was rejected because it "leaves the assistant, who sees the conflicts and repairs first, without a duty to say when a review is due".

With these two decisions, the consequences of a decision became a document type that cites the decision and can prompt its revision. In Argyris's terms, the governing variables of the record's *governance* became revisable through a recorded procedure.

### 7.4 A complete cycle: LEAD → POSTMORTEM-002 → ADR-111

**The scheme.** On 19 November the owner asked for a better way to keep the record's research opportunities. They were scattered across 54 proposed-study CASEs (28 of which bore on no question), "what would answer it?" prose on 264 of 451 open questions, and proposed tests in dated notes. ADR-109 (Proposed) created LEAD: a plan to advance a question or claim by any method. A LEAD has a status saying whether it is still worth following and a stage saying how far it is worked out (idea, specified, underway). A backlog audit filed 184 leads.

**The review.** The owner asked for a postmortem of the session's configuration changes. POSTMORTEM-002 found the LEAD scheme in use but failing in several ways:

- **The stage field did not discriminate.** 190 of 197 leads (96.4%) sat at `idea`, because `specified` required a cost estimate that no source supplied. The field conflated a design being specified with its cost being estimated.
- **There was no priority,** so the backlog could not be triaged.
- **There was no blocked state.** About 30 reading leads waited on copies the owner had to supply, and this could be said only in prose.
- Leads could not target a THEORY or a TERM. The question-dependency relation was unused.
- **The descriptions of the derived converse relations were misleading** (see §7.5).

**The revision.** ADR-111 (Proposed) carried out recommendations 1 to 5. `specified` no longer requires a cost. A new stage, `costed`, holds leads that have one. A `priority` field (high, medium, low) was added and backfilled from the audit's ratings, along with a `blocked_on` note. Leads may now advance a reading or a term. The converse descriptions were corrected.

**The outcome.**

| Stage | Before (POSTMORTEM-002, n = 197) | After (index, n = 198) |
|---|---:|---:|
| idea | 190 (96.4%) | 137 (69.2%) |
| specified | 4 | 57 |
| costed | — | 1 |
| underway | 3 | 3 |

*Figure 3 (to draw): paired bars of the table above.*

Fifty-nine leads are now high priority, 126 medium, and 13 have no priority. Views by priority and by blocker now exist where none could before.

**What this shows, and what it does not.** It shows that a review identified a field that failed to discriminate. It also shows that the revision redistributed entries into categories that support different decisions, and that the cycle from scheme (19 November) to review and revision (20 November) took two days. This is tier-2 evidence about the structure and adoption of a classification. It does not show that research was completed sooner, that priorities were better chosen, or that the inquiry gained. Those would need tier-3 evidence the record does not yet have.

### 7.5 A negative result inside the review apparatus

POSTMORTEM-002's first version called the absence of derived converse fields (`advanced_by`, `operationalizes`, and others) in the sources a defect. It counted a dry run's 161 pending back-references as theirs. On reading Luria's code, the filer found that for a directed pair Luria stores the primary side and computes the other for every reader by design. The 161 pending references were completions of undirected pairs elsewhere. The defect was in the relations' descriptions, not in the record. The body was corrected the same day. The frontmatter summary was not. It still says the derived converses "are declared but never written", and the generated postmortem index carries that sentence.

This is a small, clean instance of the problem the paper is about. A correction to the detailed account did not reach the compressed representation built from it. The generated views derive from the summary, so they faithfully propagate the uncorrected part. The review mechanism is itself an object that needs review.

### 7.6 The process postmortems

The other two postmortems review process rather than schema. POSTMORTEM-001 reviews a batch of six pull requests on 19 November, five of them stacked on a schema change and merged in sequence. It traces the costs to putting readings on the schema's pull request, codes broken at hyphens by line-wrapping, and a bot's repair commit colliding with an unpulled local commit. POSTMORTEM-003 reviews five pull requests on 19 and 20 November. Its main cost was conflicts on dated notes appended to the same entries by parallel pull requests. That is the contention DP-1 names ("a file every contribution must touch is a lock"), recurring at the scale of a single entry. It also records an inferred personal name that was nearly written into the record.

All three postmortems are Drafts. None has yet been accepted, so the mechanism is in use but its procedure has not been validated over time. We treat POSTMORTEM as an early mechanism with documented use, not as an established institution.

---

## 8. Discussion: obstruction, capability and the limits of self-correction

### 8.1 Obstruction as an occasion for reorganisation

The record's own account of how an agent develops new capacities gives the frame. CLAIM-532 (Active) holds that an unresolved discrepancy is an *occasion* for self-formation, not a guarantee of it. It suffices for self-formation that the agent's own activity on the discrepancy produce a maintained capacity that outlasts it and serves a class of later discrepancies. That capacity is either a new *distinction*, a feature of the situation the agent's policy comes to depend on, or a new *channel*, an outcome the agent can now reach. TERM-099 fixes the sense. The account was written about agents and organisations in general. Applied to the record:

- §6.2 is a new distinction that is also a new channel. `Unfetched` made a situation legible, and it opened a route, the owner's worklist, by which such situations get resolved.
- §§6.3–6.4 are new distinctions. Classifications came to depend on a feature, kind or warrant, that they had not depended on before.
- §§6.5–6.6 reorganised *inferential* capacity. The record can now direct an objection at an inference rather than a conclusion, and it no longer lets an account smuggle in a proposition.
- §7.4 is a distinction acquired by the governance apparatus itself.

The account's test for whether a capacity was *formed*, rather than merely exercised, is transfer: does it serve later discrepancies of the same class after the inducing conditions are gone? The line-splitting test of §6.7 passes it weakly. It was formulated once, for `nucleating-argument`, and reapplied twice to lines that were not its occasion. Most other cases have not yet had the chance.

### 8.2 What makes a distinction operationally significant?

Not every new field matters. CLAIM-535 (Active) states a criterion. An organisation that acts on what it observes has a policy acceptable in every circumstance exactly when, for each observation, the circumstances it cannot tell apart share an acceptable action. A distinction is *needed* when two circumstances the record treats alike require different legitimate responses. This sharpens §6. `Deferred` was inadequate because "not yet tried" and "tried and failed" share no acceptable next action. The CASE kinds matter where a thought experiment and a proposed study, both stipulated, call for different handling: one is argued from, the other is run. Where acceptable actions overlap, CLAIM-535 adds that several incomparable coarsest distinctions may suffice. Which one to make legible depends on which action the organisation commits to. That is consistent with the negative cases. ADR-036 and ADR-056 declined distinctions that no committed action required.

We should also distinguish a capability that was *unavailable* from one that was available through manual interpretation and became cheaper, more reliable or easier to maintain. Most of §6 is the second kind. A careful reader could always have found the failed searches among the Deferred LITs by reading their notes. Mechanisation turned that labour into a query.

### 8.3 Correction versus maintained corrective capacity

CLAIM-422 (Active) distinguishes three things: a successful corrective act, an executable procedure, and a maintained organisational capacity. An organisation can rewrite its rules without the corrected capacity being maintained. Nucleation's history contains many of the first kind and several of the second: the line-splitting test, the pilot-before-require pattern of ADR-043 and ADR-056, and the triggers of ADR-110. It contains early mechanisms aimed at the third. §7.5 is a reminder that the third is not yet secured. The procedure that should have carried a correction through to every derived view did not.

### 8.4 The costs of acquired distinctions

CLAIM-569 (Active) holds that a form has three resource requirements, to construct it, to maintain it, and to move into or out of it, and that none fixes another. Each intervention in §6 paid a construction cost (the decision, the migration of §6.9) and a transition cost (re-reading the affected entries). It also left a maintenance cost: every future filer must now choose a kind, a warrant, a status or a stage. CLAIM-310 (Active) adds a point about arrangement. Sorting schemes never conflict as descriptions, but they compete as arrangements, because one set of bins realises one partition. A split vocabulary is a new set of bins, and it is costly when what one searches for crosses them.

The withdrawal in §6.6 is the instructive case. Keeping SYNTHESIS as an asserting type would have required continuing accommodation. Every claim-like synthesis needed claim-like fields and relations. Reversing the abstraction cost one migration of eleven entries. Continuing to accommodate it would have cost something on every filing thereafter.

### 8.5 The epistemic risks of the apparatus

Three claims the record holds about organisations in general apply to the record as an organisation.

- **Admission is not uptake.** CLAIM-403 (Active) separates a contribution's admission, its recognition in apt terms, its credibility, its uptake, and its contributor's part in revising the standards of uptake. A record can file everything and still give some contributions no channel to change anything. The obstructions in §6 were cases of failed *recognition*: the inference objections of §6.5 were admitted, but under a category that misdescribed them.
- **Selection and scoring need different remedies.** CLAIM-466 (Active) shows, in a simulated population, that correcting for how evidence was selected does not correct how it is scored. A record that grades itself by its own lint, index coverage and schema completeness is scoring itself.
- **Tests are contested.** CLAIM-416 (Active) holds that success under an evaluative regime is evidence of competence relative to that regime, and that a perspective which gains influence over the test can change what later success shows.

Together these say that improvements in lint compliance, field coverage or index completeness are not substitutes for independent assessment of argument quality. The record's own metrics show adoption, and every figure in this paper's tier 2 is one of them. Whether the argument is better is a tier-3 question.

### 8.6 Self-formation and the provenance of improvement

Whose capacity was formed? Section 2.3 answers for the period studied. Every intervention was requested or approved by the owner. Assistants supplied evidence (the 177 failed searches, the 42 misfiled objections, the relation densities), proposed designs and carried out migrations. In one case an assistant's line during substantive work named the missing distinction before anyone asked for it (§6.4). In POSTMORTEM-002 an assistant, asked for a review, found the stage field's failure itself. But no assistant initiated a change to the grammar unprompted. CLAIM-522 (Active) shows, for a formal model, that recovery under perturbation cannot show where a maintaining capacity is realised; only interventions on the mechanisms that produce it can. By analogy, that the record now handles these cases well does not show where the capacity to handle them lives.

So the case documents an organisational capacity, the owner plus assistants plus mechanisms, that became better at reorganising its representation. It does not show that the assistants acquired that capacity. The open question is whether an assistant could recognise an inadequacy it has not seen before, propose a change of appropriate scope, and carry the lesson to later problems.

### 8.7 Toward delegation: the signatures of obstruction

The question that started this study was practical: which parts of the owner's role in this flywheel could an assistant take over? Re-reading the cases for what was observable *before* each reorganisation shows that most obstructions left a characteristic residue in the record:

| Signature | Observable as | Cases |
|---|---|---|
| **Prose carrying a structural distinction** | Free-text notes on many entries with one field value that sort them into recurring sub-situations | 177 of 345 Deferred LITs noting a failed search (§6.2) |
| **A scheme gone unused while its content goes elsewhere** | A scheme with no new entries over a period, and entries in a neighbouring scheme whose subject is that scheme's subject | No ARG after 10 Oct; 42 claims about support (§6.5) |
| **A type re-acquiring another type's fields** | Accommodations that give one scheme's entries the fields and relations of another | Admitted syntheses carrying credence, voice, warrant and defeater (§6.6) |
| **A degenerate distribution** | One value holding nearly all entries of a field meant to discriminate | 96.4% of LEADs at `idea` (§7.4) |
| **A field read as answering a second question** | Values of one field used, in prose or by readers, to answer a question the field was not defined for | `standing` read as kind (§6.3) |
| **Loose use of the nearest word** | Repeated reports of a missing word, or one tag carrying senses that readings keep apart | `self-and-personhood` (§6.1); `learning-theory` (§6.8) |
| **A partition with low internal coupling** | Relations dense within parts of a line and sparse across them | 25 in, 8 out, 3 in (§6.7) |
| **A summary diverging from its body** | Frontmatter that contradicts a later-corrected body | POSTMORTEM-002 (§7.5) |

Most of these can be computed: field distributions, scheme activity over time, relation density within candidate partitions, clustering of status-note text, field-set overlap across schemes. An assistant could run them at the moments ADR-110 already defines and report candidates, as the line-splitting test now does for lines.

What the table does not mechanise is the *response*. The same signature (one word, several senses) led to a split in §6.1 and a widening in §6.8. Three signatures in a row led to a rejected decision in ADR-056. Detection can plausibly be delegated. The choice of remedy depends on which actions the record commits to (§8.2) and what the distinction will cost to keep (§8.4), and in this history that choice was always the owner's. A conservative division of labour follows. The assistant detects and characterises; it proposes alternatives, including doing nothing; it pilots on a sample before anything becomes required, as ADR-043 and ADR-056 did; and the owner decides. Whether assistants can do the first two steps reliably is an empirical question. The next section proposes how to answer it.

---

## 9. Future evaluation: can the apparatus get better at improving itself?

### 9.1 Historical replay

Reconstruct the record as it stood immediately before each intervention in §6. Give an assistant that grammar, the entries, and the work then in progress, without the decision that followed. Ask it to identify representational obstructions. Score whether it finds the inadequacy the decision addressed. Score whether it proposes a change at the right level (value, field, scheme, line), offers credible alternatives, and recognises the negative cases of §6.8 as cases where no change, or a widening, is warranted. The table in §8.7 supplies features for a baseline detector against which an unaided assistant can be compared.

### 9.2 Measuring the misfits nobody noticed

Everything in §6 was noticed. To estimate the base rate, sample original exchanges and curation entries from before each intervention. Have independent readers classify each contribution as represented faithfully, forced into a misleading category, kept only in prose, or omitted. This supplies the denominator the record lacks (CLAIM-419's "whether every such move is caught is not shown"). It also allows a test of whether the rate of unnoticed misfits fell as governance matured.

### 9.3 Comparing governance regimes

The record already holds designs for this. CASE-253 (Proposed) gives agents a record whose grammar may or may not be adequate, and crosses fixed against modifiable schemas with informal against explicit change governance. It scores semantic correction without regressions. CASE-254 (Proposed) presents one surface failure generated by different hidden causes, for a team with a probe budget to diagnose before repairing. CASE-255 (Proposed) compares earlier and later "improvers" of a record-keeping collective from the same starting state, then damages the collective's diagnostic machinery. Together they would separate improvement in the *maintained record* from improvement in the *assistant's diagnostic procedure*, which §8.6 says the historical case cannot do. They would also address QUESTION-458 directly.

### 9.4 Value and cost

For a sample of interventions, measure: semantic correction (did conflated entries separate correctly?); coverage; actionability (did the new worklist or view get used?); migration burden; recurring filing effort; and downstream argument quality as judged blind by readers who do not know which grammar produced which record. Include the negative cases, and test directly whether more formalisation improved the work.

---

## 10. Limitations

- **One project, one owner.** Every intervention was shaped by one person's research interests and style of governance. Nothing here estimates how often such reorganisation succeeds elsewhere.
- **Participant authorship.** The record, its studies of itself (CASE-178, CASE-180), its postmortems and this draft were written by the project's own participants, largely AI assistants working at the owner's direction. The measurements were computed from the repository and can be reproduced. The interpretations cannot be separated from the people interpreting.
- **Selection of cases.** Cases were chosen because they are well documented and illustrate distinct intervention types. Interventions that were never written up are invisible to this method.
- **Proposed decisions.** Several mechanisms discussed are governed by decisions still Proposed when measured: ADR-082, ADR-083, ADR-084, ADR-109, ADR-110, ADR-111 and ADR-112. All three postmortems are Drafts. The record is in use under them, but they are not settled.
- **Short horizon.** Eight weeks is short for claims about maintained capacity (§8.3) or rates of slow processes (§4.6).
- **Tier-3 evidence is absent.** Nothing here shows that the reorganisations improved the inquiry's conclusions.
- **Counting definitions.** "Local schemes" and "configured vocabularies" depend on what is counted. The measurement note's prose once gave thirteen schemes on 19 November against twelve in its table. We use the tabulated value pending a recount (Appendix C).

---

## 11. Conclusion

Nucleation documents a research project whose inquiry and representational apparatus developed together. Its configuration was not merely extended to accommodate more material. It was repeatedly revised when schemes, vocabularies, relations and lines of inquiry failed to keep apart, or hold together, what the inquiry needed. The resulting changes altered what the record could distinguish, which inferences it could represent and contest, and how later work could be organised. Some changes added distinctions, one withdrew an abstraction, and several declined to add anything. Decision records made the reasons persistent. Migrations, required fields and continuous checks made them binding. The POSTMORTEM, still in draft, made the consequences of decisions evidence for revising them, and one complete cycle shows it working within two days.

The case illustrates a human-directed form of reflexive research infrastructure: a record that can make its own representational and governance arrangements objects of its inquiry. The obstructions that drove its reorganisations left observable signatures. Detecting them is a plausible first task to delegate to an assistant. Choosing a response has, so far, been a matter of judgment about which distinctions the inquiry commits to and what they cost. Whether this machinery improves research relative to simpler alternatives, and whether assistants can learn to recognise when it needs reorganising, are now questions the record can pose as studies of itself.

---

## Appendix A. Exhibits to produce

1. **Figure 1.** Record files and configuration lines, indexed to 25 Sep = 100 (§4.4).
2. **Figure 2.** CASE kind × standing heatmap, 6 × 3 (§6.3).
3. **Table.** CLAIM warrant × status (§6.4).
4. **Figure 3.** LEAD stage before and after ADR-111 (§7.4).
5. **Table.** Migration costs (§6.9).
6. **Table.** Signatures of obstruction (§8.7).
7. **Diagram (optional).** The intervention cycle, from difficulty to later review, annotated with which cases contain which stages. It would show the review stage appearing only in November.

## Appendix B. Source map

| Section | Record entries |
|---|---|
| 2.2 Scope | ADR-001, ADR-032, ADR-048 |
| 2.4 Apparatus | TERM-089, CLAIM-469, CLAIM-476 |
| 3 Related work | LIT-2514, LIT-2499, LIT-2479, LIT-1631, LIT-745, LIT-2784, LIT-2785, LIT-1657; QUESTION-458 |
| 4.5–4.6 Rates | CASE-178, CASE-180 |
| 5 Obstruction | CLAIM-419 |
| 6.1 | ADR-015, ADR-024 |
| 6.2 | ADR-041, ADR-053 |
| 6.3 | ADR-042 |
| 6.4 | ADR-043 |
| 6.5 | ADR-032, ADR-061 |
| 6.6 | ADR-075, ADR-076, ADR-083, ADR-084 |
| 6.7 | ADR-082, ADR-083, ADR-087, ADR-100 |
| 6.8 | ADR-036, ADR-042, ADR-041, ADR-053, ADR-056 |
| 7.1–7.2 | ADR-054, ADR-071, ADR-072, DP-1, DP-2, DP-3, CASE-131, CLAIM-479 |
| 7.3–7.6 | ADR-109, ADR-110, ADR-111, ADR-112, POSTMORTEM-001, POSTMORTEM-002, POSTMORTEM-003 |
| 8 | CLAIM-532, TERM-099, CLAIM-535, CLAIM-422, CLAIM-569, CLAIM-310, CLAIM-403, CLAIM-466, CLAIM-416, CLAIM-522 |
| 9 | CASE-253, CASE-254, CASE-255, QUESTION-458 |

## Appendix C. Open items for the owner

1. **Relation to the existing work `luria-nucleating-an-argument`.** The record already holds a manuscript, proposed on 11 October, with "luria is the tool and this record the case". Is this paper that manuscript's successor, a companion, or a replacement? The answer decides whether it gets a `works` term of its own and which claims join it.
2. **Scheme count on 19 November:** twelve in the measurement table, thirteen in its prose. Fix a definition of "local scheme" and recount.
3. **Decision-record count.** The U11 measurements gave 113 (36 Proposed). The index on 20 November gives 114 (37 Proposed). State a single observation date for the governance census.
4. **POSTMORTEM-002's summary** (§7.5). The draft uses the uncorrected summary as a finding. Correcting it in the record would remove the example, so decide whether to cite it as of a dated commit, or to correct it and describe the correction.
5. **Missing references:** the Luria repository and documentation, Nygard (2011) on decision records, and any literature on LLM agents with persistent memory. None of these is on the record.
6. **Venue and length.** The draft runs to roughly 10,000 words including tables. A workshop paper would keep §§1, 4.4–4.5, 6.3, 6.4, 6.6, 7.4 and 8.7.
7. **Authorship and disclosure** of AI assistance, given §10's second limitation.
