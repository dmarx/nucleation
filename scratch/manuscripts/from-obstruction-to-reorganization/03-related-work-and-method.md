<!-- scratch/manuscripts/from-obstruction-to-reorganization/03-related-work-and-method.md -->

## 4. Related work

**Ontology and schema evolution.** The knowledge-engineering literature has long treated ontology change as a managed process. Stojanovic et al. (LIT-2514) set out a user-driven evolution process with change capture, representation, semantics of change, propagation, implementation and validation. Flouris et al. (LIT-2499) survey and classify ontology-change operations. In model-driven engineering, COPE (LIT-2479) automates the *coupled* evolution of a metamodel and the models that instantiate it. That is the same coupling Luria's migrations perform by hand and by script. Our case differs from these settings in three ways. The schema is changed in the course of the inquiry it serves, not by a separate maintenance team. The occasion for a change is an argumentative difficulty, not a requirements change. And each change is accompanied by a decision record and a first application. QUESTION-458 (Open) asks whether this coupling of schema change to recorded decision, migration and executable checks is what distinguishes Luria from ontology and metamodel evolution. This paper offers evidence on the descriptive half of that question.

**Classification and its consequences.** Bowker and Star (LIT-1631) showed that classification systems are never neutral. Each valorises some points of view and silences others, and the work of fitting cases to categories is mostly invisible. Our cases are small, explicit instances of their thesis. A category that conflates two situations makes one of them unrecordable, and recovering it costs a migration.

**Organisational learning.** Argyris's distinction between single-loop and double-loop learning (LIT-745) maps closely onto ours. Single-loop learning corrects an action within fixed governing variables. Double-loop learning revises the variables themselves. Re-filing a misfiled entry is single-loop. Changing the vocabulary that misfiled it is double-loop. The record's own CLAIM-422 adds a third distinction, between a corrective act, an executable procedure and a *maintained* corrective capacity, which we use in §8.3.

**Postmortems.** Blameless postmortem practice in site reliability engineering (LIT-2784, LIT-2785) treats an incident as evidence about a system rather than a person. Its products are recommendations with owners. Nucleation's POSTMORTEM adapts the practice to a different object: not an outage, but a change to the record's grammar or process once it has been used.

**Architectural decision records.** Lightweight decision records, each stating context, decision, alternatives and consequences, are an established software-engineering practice [ref needed: Nygard 2011, "Documenting Architecture Decisions"]. Nucleation uses them for every grammar change. It adds a rule that a decision travels in the same pull request as its first application (ADR-071), so that a reviewer judges the rule by what it does.

**Theories of inquiry.** The account in §2.5 has older relatives. The record's notes on CLAIM-470 name two of them. One is Dewey's logic of inquiry (LIT-1645), in which inquiry transforms an indeterminate situation into a determinate one. The other is Collingwood's logic of question and answer (LIT-1651), in which a proposition is intelligible only as the answer to a question. The record has not read either first-hand (both are Unavailable), and the comparison should be made before submission. Rheinberger's epistemic things (LIT-1665, Unavailable) are a third candidate: objects of research that are under-determined by design and are given shape by the experimental system. The nearest formal case the record holds is counterexample-guided abstraction refinement (LIT-1652), where an abstraction is refined exactly where a spurious counterexample shows it to be too coarse. Nucleation's grammar differs in having grown by addition and once by withdrawal, not only by splitting (§2.5).

**Design rationale.** Capturing the reasoning behind decisions has a long and largely discouraging history. IBIS represented design as issues, positions and arguments (LIT-758). Grudin traced the failure of groupware and capture systems to a disparity: the person who does the work of capture is not the one who benefits (LIT-757). Later work asked when argumentation-based rationale repays its cost (LIT-760, LIT-761, both Unavailable). CLAIM-179 places Nucleation against this history. When a memoryless agent does the filing, capture and benefit fall to the same party, and the disparity moves to the owner's review. The record's own question of when filing pays (CLAIM-303, CLAIM-308) is the design-rationale literature's question, put to a different division of labour.

[Owner: decide whether related work should also cover research-notebook and argument-mapping tools, and prior literature on LLM agents with persistent memory. Neither is on the record yet.]

---


---

## 5. Method and materials

### 5.1 Evidence and observation points

The study draws on the version-controlled record from its scaffold on 25 September 2026: dated repository snapshots, `luria.yaml` diffs, decision records, curation and workbench journals, changelog fragments, migration commits, generated indexes, CI workflows and postmortems. The quantitative evidence comes from three observation points, which we keep apart:

| Observation point | Source | Used for |
|---|---|---|
| **Historical snapshots** at the end of 25 Sep, 15 Oct, 1 Nov and 19 Nov (UTC) | Repository history at dated commits | Growth of the record and its configuration (§5.4) |
| **Executed studies inside the record** | CASE-178 (first 32 days after the scaffold) and CASE-180 (first 50 days, 1,434 commits, 5,034 documents), both run on 27 Oct | Rates of grammar change and of revision (§§5.5–5.6) |
| **Current generated indexes,** 20 Nov | Field values of every current entry | Classification cross-tabulations (§6) and governance census (§7) |

Two consequences follow. The cross-tabulations describe the record *after* every intervention discussed. They show that the distinctions are in use, not when each began to be used. And the LEAD comparison in §7.4 sets the 197 entries counted in POSTMORTEM-002 against the 198 in the later index. It is a change in distribution, not a fixed-cohort estimate of individual transitions.

### 5.2 Unit of analysis

The unit is a **representational intervention**, reconstructed where the record permits as a sequence:

> encountered difficulty → diagnosis → alternatives → decision → migration → operational consequence → later review.

Not every episode has every stage. Early episodes have no later review, because no review mechanism existed. Whether a stage is present is itself a datum about how governance developed.

### 5.3 Typology and evidential tiers

We classify interventions as: (a) refining a vocabulary; (b) adding an independent classification dimension; (c) revising the boundary between schemes; (d) withdrawing an abstraction; (e) decomposing a line of inquiry; (f) changing the mechanisms that govern future change; and (g) declining to add structure.

We separate three kinds of evidence:

1. **Recorded rationale:** what the decision record says the difficulty was and why the change answered it.
2. **Observed operation:** what the implemented representation now distinguishes, as shown by populated fields and cross-tabulations.
3. **Measured outcome:** whether the change improved later research, coordination or correction.

The record is strong on the first, moderate on the second and weak on the third. We say which tier each finding rests on. Tier-2 evidence has a further bound, prediction P6 of §3.6. It is counted in the record's own grammar, so it shows that a distinction is drawn and used. It cannot show that drawing it was right (ARG-028, CLAIM-266).

### 5.4 Growth of the record and its grammar

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

### 5.5 Grammar change as part of ordinary work

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

### 5.6 Different rates of persistence

CASE-180 measured how often each layer of the record changes, using 1,434 non-merge commits over the first 50 days. After drafting was over, an entry's prose was revised about once in 21.8 days, its status about once in 127.5 days, and an authored relation was gained or lost about once in 131.9 days. None of the 68 declared relation types was redefined, although new types continued to be added.

These are inverse event frequencies, not relaxation times. A 50-day window cannot estimate a 128-day process, and the study says so. What they support is narrower. The record's layers are revised at rates one to two orders of magnitude apart, and the grammar is slow to revise without being slow to grow. CASE-180 also found that on the first day of an entry's life all layers change together. The ordering appears only once drafting is over.

**Transition.** The machinery was stable under ordinary use and still amendable when the work exposed a need. The next section examines the amendments.

---
