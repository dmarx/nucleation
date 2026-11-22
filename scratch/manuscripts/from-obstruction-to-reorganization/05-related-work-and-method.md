<!-- scratch/manuscripts/from-obstruction-to-reorganization/05-related-work-and-method.md -->

## 11. Related work

*A work marked "unread" is registered on the record but has not been read first-hand. "Skimmed" means read in part. Claims about the content of unread works are the record's reports of them, and they must be checked before submission.*

**Formality and its costs.** The objection this paper answers is an old one. Shipman and Marshall's "Formality Considered Harmful" (LIT-756) found that users of interactive systems resist formal representation: formalizing early forces premature commitment, and the effort falls on those who gain least. CLAIM-181 adapts their finding to a record kept by agents. What is new here is not the objection but a history of meeting it.

**Ontology, schema and metamodel evolution.** The knowledge-engineering literature treats ontology change as a managed process:

- Flouris et al. (LIT-2499, skimmed) classify ontology-change operations, and list discovering "a design flaw in the original conceptualization" as a standard reason for change;
- Stojanovic et al. (LIT-2514, unread) describe a user-driven evolution process;
- COPE (LIT-2479) automates the *coupled* evolution of a metamodel and its models, which luria's migrations do by hand and by script.

Read against CLAIM-419, the record already holds several contrasts:

- WebProtégé records schema changes but not decisions about them (LIT-2508);
- Git4Voc amends a vocabulary by commit and discussion, not by decision record (LIT-2509);
- in OBO, principles and the checks for them are revised when found imprecise, but no decision record is described (LIT-2494, LIT-2313);
- Chong et al. patch an agent's schema when its trajectories reveal misfits, accepting a patch on measured gain with no record beyond a log (LIT-2311).

These place luria's distinctive feature, the one QUESTION-458 asks about, as the coupling of each schema change to a written decision, a migration of existing entries and an executable check.

[To add before submission: database schema evolution, e.g. PRISM.]

**Qualitative codebooks.** The closest methodological analogue may be codebook evolution in qualitative research. Analysts revise codes as data arrive, keep memos on why, and measure agreement between coders. The record's grammar is a codebook its own filers revise mid-study, and this paper borrows the discipline: a fixed codebook and a second coder (§12.3). [This literature is not yet on the record.]

**Classification and its consequences.** Bowker and Star (LIT-1631, unread) argue that classification systems foreground some situations and silence others, and that the work of fitting cases to categories goes unseen. Our cases are small, explicit instances of that thesis.

**Organizational learning and memory.**

- **Argyris** (LIT-745) distinguishes single-loop learning, which corrects action within fixed governing variables, from double-loop learning, which revises the variables. THEORY-145 records his warning that organizations espousing double-loop learning characteristically fail to practice it.
- **March** (LIT-729) models an organizational code that learns from its members and teaches them. In that model moderate turnover keeps an organization exploring (THEORY-142). Memoryless collaborators may play turnover's role (§17.5).
- **Hutchins**'s cockpit remembers speeds that neither pilot holds (THEORY-351, from LIT-1066). It is the classic case of memory held by an arrangement rather than a person.

**Postmortems.** Blameless postmortem practice treats an incident as evidence about a system rather than about a person (LIT-2784; Allspaw, LIT-2785, unread). Nucleation's POSTMORTEM applies the practice to a change to its grammar or process once that change has been used.

**Design rationale and decision records.**

- **IBIS** (LIT-758) represented design reasoning as issues, positions and arguments.
- **Grudin** (LIT-757) traced the failure of such capture to a disparity: the person who does the capture is not the one who benefits.
- **Argumentation-based rationale**: later work asked when it repays its cost (LIT-760, LIT-761, both unread).
- **Architectural decision records**: lightweight decision records are now common in software engineering [ref needed: Nygard 2011; Tyree and Akerman 2005].

The record files a decision for every grammar change. It also travels each decision with its first application (ADR-071), so that a reviewer judges the rule by what it does.

**Learning by reorganization.** The theory's nearest classical ancestor is Ashby's *Design for a Brain* (LIT-787):

- **Ultrastability.** A system that does not know how its environment affects its essential variables adapts by trial and error only if a second feedback, through those variables, changes the parameters of its primary feedback. If that second feedback acts "whenever, and for as long as, an essential variable is outside its limits", every equilibrium the whole can reach is an adapted one (THEORY-324, Active). This is the flywheel in its simplest form: an obstruction triggers reorganization of the parameters, not just a new response.
- **Retention.** Adaptation in a large system "finishes in a practicable time only if partial adaptations are retained". Retention requires that the parts be separated, at least temporarily, by constancies; where later learning shares parts with earlier learning, it destroys it (THEORY-307, Proposed). This anticipates both the record's line splits and the risk that a revision undoes what an earlier one secured.
- **Near-decomposability.** Simon's account of nearly decomposable systems (LIT-905; THEORY-661) separates fast dynamics within parts from slow, aggregate dynamics between them. CLAIM-388 shows that near-decomposability is not necessary for exact closure.
- **Commitment and anomaly.** Kuhn, as one reading has him, holds that firm commitment to a tradition is what lets research recognize where the tradition fails (THEORY-2096, Proposed, from LIT-2885). That is stage 7 of the flywheel: finer categories make misfits visible.

Where this paper's theory goes beyond these is in four places:

- separating the products of learning, distinction and channel (CLAIM-532);
- keeping formation, maintenance and transition costs apart (CLAIM-569);
- separating the observing budget from the acting budget (CLAIM-557);
- treating the apparatus of inquiry, not only the learner, as revisable (CLAIM-470).

[Not yet on the record, or unread: Bateson on deutero-learning (LIT-2323, Unfetched); Piaget on accommodation; Lakatos on research programmes; work on active inference, of which the record holds several readings (e.g. LIT-1363) that this draft does not use.]

**Theories of inquiry.** Dewey (LIT-1645, unread) and Collingwood (LIT-1651, unread) are the nearest predecessors of CLAIM-470. Rheinberger's epistemic things (LIT-1665, unread) are a third. The formal case the record has read is CEGAR (LIT-1652), with the disanalogies in §4.1.

[Not yet on the record: provenance models (PROV), nanopublications, argument mapping, boundary objects, and work on LLM agents with persistent memory.]

---

## 12. Method and materials

### 12.1 Evidence and observation points

The evidence is the version-controlled repository, read with its full history: 3,454 commits from the empty initial commit of 7 September 2026 to 20 November, as first counted (the pipeline counts 3,451 at `09950cdf`, and how the first count was made is not stated), and 3,739 reachable from `main` at `56479304e` on 21 November. The record's start is its scaffold on 25 September (`af387c07b`).

Figures come from four observation points:

| Observation point | Commit(s) | Used for |
|---|---|---|
| Historical snapshots: the last first-parent commit on `main` by 23:59 UTC on each date | 25 Sep `f5c040c6a`; 15 Oct `b84ad2e37`; 1 Nov `55cd0d814`; 19 Nov `eed84a74e` | Growth (§12.5) |
| Executed studies inside the record, both run on 27 Oct | CASE-178 (32 days from the scaffold); CASE-180 (50 days from 7 Sep, so 32 days of record) | Rates of grammar change and revision (§§12.6–12.7) |
| The current record | `main` at `09950cdf`, 20 Nov | Cross-tabulations (§13), census (§13.1), term-change analysis (§15.2), governance counts (§14) |
| The owner's measurements (U11 of the exchange that produced the first sketch) | Dated snapshots, no hashes | Cross-checked against the snapshots above; they agree to within 1.5% |
| The record after the promotion of 21 November, recomputed (added 2026-11-21) | `main` at `56479304e`, 18:20 UTC | The 21 November column of §12.5, the counts of §§8.2 and 14.1, the census's coverage and status drift, the term-change audit extended (`analysis/analytics-2026-11-21.json`, `analysis/analytics-terms-2026-11-21.json`) |

### 12.2 Units

- **Unit of analysis.** For the census, the unit is a **decision record** (ADR-001 to ADR-114; with the fifth batch, ADR-115 to ADR-135 and ADR-tmpcb96w). For the history of the grammar, it is a **unit of work**: the pull request a commit came in, or the commit itself where it cannot be tied to one.
- **Grammar.** The declarations in `luria.yaml` (schemes, fields, relations, vocabularies and their terms, statuses, lines, `fail_on` patterns and view definitions). Conventions held only in prose, such as CLAUDE.md or the skills, are *conventions*, not grammar.
- **Misfit.** A move the grammar of the day could not hold faithfully.
- **Obstruction.** A misfit someone noticed.

Unnoticed misfits are the denominator this method cannot see (§18).

### 12.3 The census, and agreement between coders

Every decision record was coded against a codebook fixed before any coding began (`analysis/census/CODEBOOK.md`). The codebook records:

- whether the decision changed the grammar;
- the level and operation;
- whether the change was a refinement, a revision or restraint;
- which component of the inquiry it touched;
- what triggered it;
- who noticed the need, who proposed the design, who decided and how the decision was ratified;
- what form the misfit took before the decision;
- the size of any migration, the outcome, and any later error.

Four coders (assistant subagents) coded the 114 decisions in four batches. A fifth coded a random sample of 30, seed 20261120, without seeing the first coding. Agreement is reported per field as raw agreement and Cohen's κ, and as mean Jaccard overlap for list-valued fields (§13.1). All five coders were instances of the same model, a limit discussed in §18.

**A fifth batch (added 2026-11-21).** The 22 decisions filed on 21 November, ADR-115 to ADR-135 and the still temporary ADR-tmpcb96w, were coded against the same codebook as `analysis/census/batch-5.json`. One coder coded them: the assistant revising this draft, which took part in the session that produced several of them. No second coder saw them, so the agreement figures of §13.1 do not cover them, and each row's note says so. Statuses are coded as they stood at coding; 34 of the first 114 have changed status since they were coded, which `census.py` now reports.

### 12.4 Evidential tiers

We separate three kinds of evidence:

1. **Recorded rationale:** what a decision says the difficulty was.
2. **Observed operation:** what the grammar now distinguishes, as shown by populated fields and cross-tabulations.
3. **Measured outcome:** whether the change improved later research.

The record is strong on the first, moderate on the second and silent on the third. Evidence of the second kind is also bounded by E7: it is counted in the grammar it evaluates.

### 12.5 Growth of the record and its grammar

| Measure | 25 Sep | 15 Oct | 1 Nov | 19 Nov | 21 Nov |
|---|---:|---:|---:|---:|---:|
| Repository files | 315 | 4,072 | 7,597 | 11,112 | 11,813 |
| Files under `record/` | 214 | 3,419 | 6,875 | 10,058 | 10,661 |
| Schemes | 5 | 10 | 10 | 12 | 14 |
| Vocabularies | 6 | 14 | 14 | 18 | 20 |
| Topic terms | 19 | 62 | 67 | 69 | 69 |
| `luria.yaml` lines | 481 | 1,468 | 1,736 | 2,379 | 2,601 |

The 21 November column was recomputed by the analytics pipeline at `main` `56479304e` (18:20 UTC, after that night's promotion), and the four earlier columns were reproduced exactly at the same run. To 19 November, record files grew 47-fold and configuration lines about 5-fold. Lines are a poor proxy for the grammar's content. The grammar grew in steps: five schemes added on 7 October, a plateau to the end of October, then SYNTHESIS and LEAD by 19 November, POSTMORTEM on 20 November and RETRO on 21 November.

### 12.6 Grammar change as part of ordinary work

CASE-178 read every change to `luria.yaml` in the 32 days after the scaffold.

| Kind of addition | Additions | Days with one | First half / second half |
|---|---:|---:|---:|
| Documents | 5,030 | 32 | 2,271 / 2,759 |
| Vocabulary terms | 106 | 18 | 82 / 24 |
| Fields and relations | 79 | 8 | 67 / 12 |
| Vocabularies | 8 | 3 | 6 / 2 |
| Schemes | 5 | 1 | 5 / 0 |

Grammar additions fell while filing rose. Beyond additions, fields and relations were redeclared 26 times on 9 days, terms were reworded 10 times, and 2 terms were removed. Ninety-four percent of new terms were used by a document changed in the same unit of work.

Decision records came with grammar changes far more often than with other work:

| Units that added | Share with a decision record |
|---|---:|
| Any pull request (296) | 16% |
| A term (35) | 91% |
| A field or relation (9) | 89% |
| A vocabulary (4) | 75% |
| A scheme (2) | 100% |

Two cautions apply:

- **Size.** The baseline is not matched for the size of a pull request.
- **Policy.** The coupling is partly a matter of rule: ADR-001 required that a missing word be "added by decision, not the nearest wrong one."

What the data show is that the rule was followed, and that grammar changes arrived inside the unit of work that needed them rather than in a separate redesign.

The same study also measured luria's own record and strata-g, the project luria was extracted from on 3 August. Their grammars are small: luria added two terms and four fields in the period, and strata-g added nothing. CASE-178 counts projects as the slowest level, with about five begun across the owner's records in four months. The extraction of luria from strata-g is the outermost loop: a project's practice became a tool.

### 12.7 Different rates of revision

CASE-180 measured 1,434 commits, 415 of them by the repository's bot. Once drafting was over, prose was revised about once in 21.8 days, status about once in 127.5 days, and an authored relation was gained or lost about once in 131.9 days. That is about a sixfold spread, not orders of magnitude. No relation type was redefined.

The ordering does not hold for every scheme. A CLAIM's relations changed far more often than its status (every 23 against every 654 days). These are inverse event frequencies over a short window, not time constants.
