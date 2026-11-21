<!-- scratch/manuscripts/from-obstruction-to-reorganization/09-flywheel.md -->

## 16. The flywheel, observed

Section 7.2 described the cycle the theory predicts for any inquiry held in a revisable apparatus. This section walks the record's history through that cycle, stage by stage, then shows something the theory did not predict but that its reflexivity makes possible. Some of the theory's own claims were revised by the very machinery the theory describes, and the instruments now used to state the theory are products of the cycle.

### 16.1 Stage by stage

**Stage 1: a misfit is absorbed.** In 63 of the 71 grammar changes that answered a misfit, the move had first been forced into the nearest category (43) or kept in prose (20) (§15.1). Concrete forms of this:

- 177 Deferred LITs carried a free-text note of a failed search, a distinction held only in prose (ADR-041);
- 42 claims were about whether one entry supports another, filed as substantive claims because ARG went unused (ADR-061);
- one topic word, `self-and-personhood`, held senses the owner asked to keep apart: agent, individual, self and person, and four kinds of unity (ADR-024).

**Stage 2: the misfit is noticed.** Who noticed changed over the period (§15.4).

- **Early:** filing agents, meeting a missing word in the course of reading.
- **Middle:** the owner, half of the time.
- **Late:** review procedures built to look: status reviews (31 sessions), synthesis and reading reviews, a line-splitting script (`scratch/formal/line_parts.py`, ADR-083) and postmortems.

Noticing moved from incidental to institutional. In P10's terms, the recognition link of the ladder was strengthened by building it into procedure.

**Stage 3: diagnosis against a target.** Grammar changes come with decision records that weigh alternatives. The diagnoses read as P1 in practice, though they do not cite it:

- ADR-042 refused to add values to `standing` because one field cannot answer two questions.
- ADR-036 widened `learning-theory` rather than split it, because the works sat on both sides and "two words would split one literature".
- ADR-056 piloted a TERM `kind` field and rejected it when five of sixteen terms forced an arbitrary choice. The test was P4's: would the name earn its keep?
- ADR-053 added `Unfetched` when the situations it separated called for different actions by different people (the owner could fetch them; no search could).

**Stage 4: the apparatus changes.** There were 88 grammar changes to 20 November: 62 refinements, 25 revisions and 1 restraint (§13.1). The 22 decisions of 21 November add three, two of them revisions (ADR-115, ADR-130), and 19 changes of process. The revisions show P2's full range:

- **re-carving** what counts as an answer (ADR-049);
- **redrawing boundaries** between kinds of entry (ADR-058, ADR-060, ADR-061);
- **withdrawing an abstraction** that had overreached: an admission route that let accounts assert (ADR-084);
- **splitting units of inquiry** (ADR-082, ADR-087, ADR-089, ADR-100).

**Stage 5: carry-through.** 2,664 existing entries were migrated by the 58 changes that state a count. Every removed vocabulary term in use was carried through every entry using it, and every split moved the entries it had to (§15.2). The failure the theory predicts at this stage, when only a meaning changes, is untested: the history holds no such change. An earlier version of this paper counted `anthology-candidate` as one; the owner ruled that the flag did not change meaning. The one carry-through failure found is of another kind, a correction that did not reach a derived summary (§14.5). Since 21 November there is a case to test: ADR-130 narrowed `record-as-apparatus` in place and touched 7 of its 80 carriers, leaving the rest to a later review (§15.2).

**Stage 6: maintenance.** Required fields, `fail_on` patterns, CI on every pull request, skills that write review procedures down, generated worklists (§14.3). The predicted failure also occurred. A correction to a postmortem's body did not reach its summary or the view generated from it (§14.5). In P7's terms, it was a correction recorded but not carried through everything that depends on it.

**Stage 7: the new capacity serves later cases.** Questions moved from expressible to askable:

- The question of which research opportunities are worked out enough to run became an index after LEAD and its revision (ADR-109, ADR-111).
- The question of what the owner could fetch by hand became a page after `Unfetched` (ADR-053).

New distinctions made new misfits visible. Once `warrant` existed, two readings of it were found in use (ADR-043, version 2). The predicted cost appeared too. Ten grammar changes caused errors that only later checks revealed (§13.9). As for entrenchment, additions to the grammar fell sharply within the first month (82 new terms, then 24), which fits settling and entrenchment equally (§15.3).

**Stage 8: the capacity to run the cycle forms.** The record built procedures for noticing, and then a procedure for reviewing its own changes:

- status reviews from 27 October;
- synthesis and reading reviews from 7 and 11 November;
- POSTMORTEM and its triggers on 20 November (ADR-110, ADR-112, both Proposed but applied), revised a day later into RETRO and a narrower POSTMORTEM (ADR-115, §14.4);
- one complete review-and-revision cycle within two days (§14.4);
- on 21 November, notes taken during the work for the next retrospective, earmarks the owner can set and a retrospective must answer, an adoption review of the decisions' own statuses, and an audit that treats a cross-line account as a sign of a missing line (ADR-115, ADR-124, ADR-126, ADR-129);
- an analytics pipeline that recomputes the record's derived figures and reports how far the hand-coded census lags (§12.1).

It also changed its tool. Mechanisms 3 to 5 of ADR-057 became features of luria 1.3.0 on 28 October (luria#382, §14.6). Whether the capacity to judge revisions was kept or eroded is the predicted risk, and it is not measured (§17.1).

### 16.2 The cycle acting on the theory itself

The record holds the theory of Part I as entries, and those entries pass through the same machinery as every other entry. CLAIM-532, the theory's account of learning, is the clearest case. Its history:

1. **6 November.** Promoted to Active at the twenty-sixth status review, at the status review's ruling: the owner had delegated such rulings to the procedure.
2. **10 November.** A lint sweep found it crossing lines as a `rests_on` step, and it was given the `distributed-agency` line under a rule proposed that day and applied at once (ADR-085, adopted on 21 November).
3. **11 November.** A synthesis review's reader found a separating case: a uniform change of priority among regimes. Read against the claim as it then stood, a definition, the case would meet its defeat condition if the record counted such a change as self-formation.
4. **18 November.** The next synthesis review wrote the case into the claim as an "Admission" section, and the record opened QUESTION-488 to hold it.
5. **18 November, later.** At the owner's direction, the claim was restated, on two observations of the owner's. First, it read as a definition where its body and CASE-191 support only a sufficient condition. That drove the restatement. As a sufficient condition, the claim "does not cover it either way". Second, the contrast between existing processes and a new ability was underspecified: if the components of a frozen random projection count as existing processes, "all feature learning is reweighting of them". That drove defining the claim's products by behaviour rather than mechanism.

Each step is a stage of the flywheel: a procedure promoting, a mechanism noticing, a review finding a case the claim could not hold, a revision. The claim it revised is the one behind P5, the principle that describes the flywheel's first and seventh stages.

Three of the instruments this paper uses to state the theory are products of the cycle:

- **Standings.** Every theory claim in Part I is labelled with a standing. That grading exists only because the record's grammar was revised to hold it. The `warrant` field (ADR-043) separates how a claim is supported from whether it is accepted, and it was itself a turn of the flywheel: a distinction an external assistant drew in conversation, which the owner noticed the record could not express.
- **The background digests.** They are built on SYNTHESIS accounts. The scheme for those accounts was created, overreached, and was withdrawn to its present form in two days (ADR-076, ADR-084).
- **The line this paper belongs to.** `record-as-apparatus`, the line whose argument this paper extends, exists because a line-splitting decision found it to be a separate inquiry (ADR-082).

The theory and the machinery that tests it were formed together, and each was revised by the other. That co-formation is what Part I means by reflexive inquiry (P8). It is also the paper's main threat to validity (§18): the theory cannot be wholly independent of the evidence it is shown against.

### 16.3 What echoes, and how strongly

| Principle | What in the record's history echoes it | Strength |
|---|---|---|
| P1: a distinction is needed when actions differ | ADR-042, ADR-053, ADR-036; every decision weighs alternatives | Observed in rationale (tier 1) |
| P2: split, merge, re-carve | 25 revisions, including a withdrawal and a redefinition of what counts as an answer | Observed (tier 2) |
| P3: no self-certification | Reviews by procedures independent of filing; separate readers for coverage, audits and checks of numbers (21 Nov); counter-example: a summary that propagated an error | Observed in design; one failure |
| P4: naming is its own decision | Pilots before required fields (ADR-043, ADR-056); the second-occurrence rule | Observed (tier 1) |
| P5: discrepancy then capacity; absorption first | 63 of 71 misfits absorbed first; new distinctions then served later cases | Observed (tier 2); transfer not formally tested |
| P6: three ledgers | 2,664 entries migrated; ten later errors; transition costs recorded | Observed (tier 2) |
| P7: maintenance; support erodes | Procedures built for maintenance; corrections that stopped short; erosion of the owner's capacity unmeasured | Partly observed; the key risk untested |
| P8: reflexive inquiry, owned criteria | Grammar revised by decision; criteria of revision stayed with the owner; the theory revised by the machinery | Observed (tier 1–2) |
| P9: anchors and traceable change | Codes, history, retirement by status; removals and splits fully carried through; one derived summary not | Observed (tier 2); one failure |
| P10: chain of uptake; correctability | Noticing moved into procedures; retrospectives and postmortems review decisions; failing the test as a claim no longer costs a synthesis its admission (ADR-131); correctability of the whole not measured | Partly observed |

Every entry in the table is tier 1 or tier 2 evidence: what the record says it did, and what its grammar now distinguishes. None is tier 3, evidence that the inquiry is better for it. Section 19 sets out how tier-3 evidence could be obtained.

### 16.4 A turn in one night (added 2026-11-21)

The night of 2026-11-21 ran the predicted cycle (§7.2) several times over, quickly enough to see each stage:

1. **Misfit.** Reframes of an entry had no place but history notes; an owner's earmark for the retrospective had no home; 48 decisions were Proposed though applied; a code in a title kept failing CI.
2. **Noticed.** By the owner in conversation, by CI, and by the assistant reading its own workflow: the noticing was mixed, part incidental and part procedural.
3. **Diagnosed against a target.** Each was put to the owner, often as alternative readings filed side by side, the owner choosing.
4. **Changed.** Decisions on reframings (ADR-120, Proposed), earmarks (ADR-126, Active), merging into staging (ADR-121, Active), the promotion pull request (ADR-125, Active) and an adoption review (ADR-124, Proposed); a guard upstream in luria, refusing a code in a title, taken into the record's pin later that day (pull request 601).
5. **Carried through.** The adoption review's first pass moved 34 decisions to Active; CI's repair then dropped the directives that had excused them, across about 400 files.
6. **Maintained.** Each change went into CLAUDE.md, a skill or a workflow.
7. **Serving later cases.** The adoption review is now a procedure for noticing (stage 2), as CLAIM-792 (Proposed) predicts.
8. **The capacity itself.** The night's retrospective (RETRO-005) records where the faster cycle let the assistant's own errors travel further before the owner caught them: the cost side of a flywheel that turns quickly.

The same night revised the review mechanism itself. One day after POSTMORTEM was created, it was split into RETRO, a review of how work went, and a narrower POSTMORTEM for what went wrong (ADR-115, Proposed; §14.4). That is stage 4 applied to stage 8: the criteria by which the cycle's own turns are judged were refined after one use, as P8 says reflexive inquiry may do.

This is one night, observed by a participant, and it is the cycle the theory predicts, so it is an illustration, not a test (§18).

### 16.5 A turn of the cycle the next day: lapses the owner caught, becoming rules (added 2026-11-21)

"A turn of the cycle" can be read two ways here, and the day of 21 November shows both. On the first reading, one obstruction runs through every stage, from a lapse to a maintained rule. On the second, the cycle acts on the procedures that run it, so that what changes is how the record files and reviews, not its grammar. The cases below are of the second kind, each followed from a lapse the owner caught to what it became. The stage labels are this draft's.

| Lapse or missing step, and who caught it | Stage 2: noticed | Stage 4: changed | Stage 6: maintained in |
|---|---|---|---|
| A filing mapped its source's gaps and did not fill them; the owner asked once for the gaps to be filled | The owner, in the request for the filing of "Rich Get Richer Power Laws" | ADR-tmpcb96w (Proposed): every filing of an exchange, synthesis or upload fills the gaps its source leaves, in the assistant's voice, without offering first | The `read-and-file` skill, step 9a, and the curation entry's "Gaps" section; first application the same filing, about forty fills and eight corrections of the other assistant's figures |
| The decoder had dropped code output and left reasoning and hidden drafts uncounted | The owner, from a turn count that fell from 96 to 43 | The decoder keeps all assistant content and counts what it leaves out (pull request 608); no decision was filed, since a tool's defect is fixed in the tool | Its tests (17), `--visible_only` for the old output, and the skill's step 1 |
| The assistant asked which of three senses of "separation" the owner meant, instead of filing all three | The owner: "when you encounter ambiguity … you file all of the available options (within reason)" | Nothing new: the rule existed (ADR-127). The two missing senses were filed as notes, and a devlog note recorded the lapse (2026-11-21, 18:29:55) | The rule as written; the note adds the sign to watch, a question ending "which did you mean?" while the regime is on |
| After a hold lifted, the assistant reported the state and did not act; the owner asked "you gonna open a new PR on staging or what?" | The owner, then RETRO-007 | ADR-132: when a hold lifts, name the held step and take it | CLAUDE.md's paragraph on the regime |
| A shared pull-request description was rebuilt by one writer, dropping the choices another had written | The assistant, re-reading before its own edit; then RETRO-007 | ADR-128: marked sections, and a write only if the text is unchanged | The promotion pull request's description |

Three things in the table are this draft's reading, not the record's.

- **The owner is still the main noticer of process lapses.** In four of the five rows the lapse or missing step was caught by the owner, by a count, a request or a question. Review procedures caught grammar misfits in the late period (§15.4); these lapses were in how the assistant worked, which no procedure yet reviews except the retrospective after the fact. That bears on §17.1: the owner's capacity to notice is being exercised, and it is also being relied on.
- **Not every turn ends in a decision.** The decoder's defect became a tool change, and the third lapse became a note, because the rule it broke already existed. In the cycle's terms, the third is a failure of stage 6, maintenance: a rule held in CLAUDE.md and in ADR-127 was not applied to a turn that was a question rather than a filing. Its own note says the fix is to recognize the sign, not to amend the rule.
- **The several-readings rule has itself come round the cycle.** ADR-127 gained it from the owner's words on 21 November, before the decision merged ("err on the side of filing all of the alternatives"). Within the day, it produced seven Rejected alternatives and an adopted reading for each of four requests (§13.8). It was applied in the filing of "Rich Get Richer Power Laws", where two of the owner's ideas each got two readings filed as alternatives (U5, U23). And it failed once, on a question, and was caught. That is stages 1 to 7 for one rule within a day, with its first maintenance failure recorded.
