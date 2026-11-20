<!-- scratch/manuscripts/from-obstruction-to-reorganization/05-governance.md -->

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
