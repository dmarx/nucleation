<!-- scratch/manuscripts/from-obstruction-to-reorganization/06-results.md -->

## 8. Results against the expectations

Each expectation of §3.6 is set against the census (§6.1), the term-change audit (`analysis/term_changes.py`) and the record's own counts. A verdict of *supported* means that the stated falsifier did not occur. It does not mean the framework is confirmed: the framework was built from this record (§2), and §10 lists what that costs.

### 8.1 E1 and E2: misfits answered by changing the grammar, and some of the changes revisions

**E1 cannot be tested by the census.** The census contains only decisions, which are misfits that were noticed and acted on. It cannot count misfits that were noticed and left. The record's one direct count is a floor. CLAIM-419's note of 12 November read every item that three recent filings reported leaving behind: of 22 items, one was left because the grammar could not hold it, and that one was sent to a decision. A misfit absorbed by choosing the nearest category leaves no such item. Known cases of noticed misfits that were left in place exist:

- the literature roles ADR-032 left in prose;
- ADR-050, deferred.

E1 is neither falsified nor tested.

**What the census does show is how misfits looked before they were noticed.** Among the 88 grammar changes:

| Form of the misfit before the decision | Changes |
|---|---:|
| Already forced into the nearest category | 43 |
| Held only in prose | 20 |
| No misfit yet: the change anticipated a need | 17 |
| The grammar had made the record assert something false | 4 |
| Unknown | 4 |

CLAIM-181 said a move the grammar cannot hold is first forced or lost. In 63 of the 71 changes made in answer to a misfit, the move had first been forced into a category or kept in prose. Noticing came after the grammar had already absorbed the move. That is CLAIM-181's mechanism, observed. It is also the reason the denominator matters: every one of these misfits sat in the record, forced or in prose, until someone noticed it.

**E2 is supported.** Twenty-five of the 88 grammar changes (28%) were revisions, with agreement κ = 0.84 on the distinction. They include five kinds:

- **What counts as an answer.** ADR-049 redefined `Answered` so that an Active THEORY, or several entries together, can answer a question as posed. ADR-059 redefined what a status means for an ARG.
- **Boundaries between kinds of entry.** ADR-058 (`grounds` and `corroborates`), ADR-060 (`answers` split from `bears_on`) and ADR-061 (CLAIM and ARG).
- **A type withdrawn.** ADR-084.
- **The unit of inquiry.** Entries were reassigned to new lines in ADR-073, ADR-082, ADR-087, ADR-089 and ADR-100.
- **A word's sense changed in place.** ADR-036 and ADR-048; and ADR-002 and ADR-046, which redefined a field and a status.

ADR-049 is the cleanest instance of CLAIM-470's distinctive clause: an inquiry revising what an answer could be.

### 8.2 E3: grammar changes made traceable

The term-change audit read every commit to `luria.yaml` across the whole history and found 34 events: 25 term declarations reworded and 9 terms removed.

- **Every event came with a decision record in the same unit of work** (34 of 34).
- **Removals were carried through.** In every removal whose term was in use, every carrying entry was changed in the same unit:

  | Term removed | Carrying entries changed |
  |---|---:|
  | `identity` | 41 of 41 |
  | `self-and-personhood` | 42 of 42 |
  | `admitted` (SYNTHESIS admission) | 12 of 12 |
  | `unadmitted` | 5 of 5 |
  | `hypothesis` (SYNTHESIS route) | 9 of 9 |
  | `derived` | 3 of 3 |

- **Splits moved the entries that moved.** `Deferred`: 177 of 345, exactly the entries reassigned. `ecology` lost `endosymbiosis`: 13 of 50. Each split line moved the entries its decision named.
- **Widening needed no re-reading, and got none.** `learning-theory` was widened by ADR-036, and 1 of its 92 carrying entries was touched. A widened word still holds every entry that held it before.
- **One redefinition in place was not carried through.** ADR-048 changed what `anthology-candidate` means, from "this work's filing here is in doubt" to "the anthology may want this work as well". None of the 237 entries carrying it was touched. The decision announced the change, but nothing located it in the entries. A reader of an old flag today reads it under a meaning it was not written with.

There is a second failure, of a different kind (§7.5). A correction to a postmortem's body did not reach its summary, and the generated view propagated the uncorrected summary.

**Verdict: supported for removals, splits and widenings. Falsified in one instance of in-place redefinition, and in one derived summary.** The record traced its grammar changes at the level of the grammar. It traced them at the level of entries when entries had to move. When only a meaning moved, the entries did not record it. By CLAIM-666's criterion, that a faithful migration preserves the accountability structure, ADR-048's migration was not faithful.

### 8.3 E4: costs, and errors caused by grammar changes

**Supported.**

- Fifty-eight grammar changes state a migration: 2,664 existing entries changed in all, median 6 per change.
- Ten grammar changes caused an error that was later recorded (§6.9). Two migrations went wrong in ways the census codes elsewhere (ADR-065, ADR-085).
- Four changes were undone within days.

Every error was found by the record itself, most within days.

**Settling or entrenchment is not settled.** Additions to the grammar fell sharply within the first month: new terms went from 82 in the first half of CASE-178's window to 24 in the second. Revisions peaked later, in the period 16 October to 5 November. Falling additions fit a grammar that is settling, but they fit one that is entrenching equally well. The record's own account of itself (SYNTHESIS-012) observes that the verdict depends on how cost is counted:

- in decisions per unit of work, revision stayed cheap;
- in entries carrying the revised type, it grew with the record.

`warrant` went to 315 claims in a day and would now go to 766. We repeat that observation rather than resolve it.

### 8.4 E5: the work of noticing and proposing, moving from the owner to assistants

**Falsified as stated.** The owner's share of noticing did not fall steadily:

| Period | Owner noticed |
|---|---:|
| 25 Sep–15 Oct | 9 of 43 (21%) |
| 16 Oct–5 Nov | 10 of 20 (50%) |
| 6–20 Nov | 7 of 25 (28%) |

Ratification did not become steadily less explicit either. No owner involvement is recorded for 17 of 43 changes, then 1 of 20, then 12 of 25.

**What did change was who, other than the owner, did the noticing.**

- **Early.** Most needs were noticed by *filing agents*, subagents reading a batch of works who found no word for what they read. These were refinements: 18 of the 20 changes filing agents noticed. Most were vocabulary terms, added under the owner's standing permission or with no recorded approval.
- **Late.** Most needs were noticed by *review procedures*: status reviews, synthesis reviews, reading reviews and postmortems. These are run by assistants, to procedures the owner asked for and set up. They noticed revisions as well as refinements: 8 of their 20.
- **Throughout.** Revisions were noticed by the owner (13) or by a procedure (8), almost never by an assistant working unprompted (1) or by a filing agent (2).

The census therefore shows delegation of a specific kind. It did not hand judgment to assistants acting on their own. It moved noticing:

- **from incidental to institutional:** from agents who happened to meet a missing word to procedures built to look;
- **by category:** standing permission for a class of refinements;
- **by procedure:** "merging it is the assent".

Judgment about revisions largely stayed with the owner. Where it was handed over, as in ADR-089, the hand-over was explicit and case by case.

### 8.5 E6: the bound on all of the above

Every figure in §§8.1–8.4 is a count taken in the record's own grammar and documents. It shows that distinctions are drawn, changes are traced and errors are found. It cannot show that the inquiry is better for any of it (ARG-028, CLAIM-266). Three entries sharpen the point against this paper's own evidence:

- **CLAIM-402 and CLAIM-342.** Categories that an institution acts on produce their own confirming regularities. A distribution over a vocabulary is shaped by the vocabulary.
- **CLAIM-448 and CASE-221.** What a legibility regime selects for recording can make a record look coherent. An intervention that improves self-governance can at first make disagreement more visible.
- **CASE-084.** A record can trace every commitment perfectly and still exclude the right explanation from its vocabulary.

None of these is answered here. Section 11 proposes the measurements that could.
