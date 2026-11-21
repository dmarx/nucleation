<!-- scratch/manuscripts/from-obstruction-to-reorganization/08-results.md -->

## 15. Results against the expectations

Each expectation of §7.3 is set against the census (§13.1), the term-change audit (`analysis/term_changes.py`) and the record's own counts. A verdict of *supported* means that the stated falsifier did not occur. It does not mean the framework is confirmed: the framework was built from this record (§4), and §18 lists what that costs.

### 15.1 E1 and E2: misfits absorbed before they are noticed, and revision as well as refinement

**E1 is supported, within the census.** E1 expects misfits to be absorbed, forced into the nearest category or held in prose, before anyone notices them. That is stage 1 of the flywheel (§7.2), and it is CLAIM-181's prediction about this record. The census can test it only for misfits that were eventually noticed and acted on.

The census cannot count misfits that were noticed and left, or never noticed at all. The record's one direct count is a floor. CLAIM-419's note of 12 November read every item that three recent filings reported leaving behind: of 22 items, one was left because the grammar could not hold it, and that one was sent to a decision. A misfit absorbed by choosing the nearest category leaves no such item. Known cases of noticed misfits left in place exist:

- the literature roles ADR-032 left in prose;
- ADR-050, deferred.

**What the census does show is how misfits looked before they were noticed.** Among the 88 grammar changes:

| Form of the misfit before the decision | Changes |
|---|---:|
| Already forced into the nearest category | 43 |
| Held only in prose | 20 |
| No misfit yet: the change anticipated a need | 17 |
| The grammar had made the record assert something false | 4 |
| Unknown | 4 |

In 63 of the 71 changes made in answer to a misfit (89%), the move had first been forced into a category or kept in prose. Noticing came after the grammar had already absorbed the move. That is CLAIM-181's mechanism, observed, and P5's "borne, not learned from" until something made it an obstruction. It is also why the denominator matters: every one of these misfits sat in the record, forced or in prose, until someone noticed it.

**E2 is supported.** Twenty-five of the 88 grammar changes (28%) were revisions, with agreement κ = 0.84 on the distinction. They include five kinds:

- **What counts as an answer.** ADR-049 redefined `Answered` so that an Active THEORY, or several entries together, can answer a question as posed. ADR-059 redefined what a status means for an ARG.
- **Boundaries between kinds of entry.** ADR-058 (`grounds` and `corroborates`), ADR-060 (`answers` split from `bears_on`) and ADR-061 (CLAIM and ARG).
- **A type withdrawn.** ADR-084.
- **The unit of inquiry.** Entries were reassigned to new lines in ADR-073, ADR-082, ADR-087, ADR-089 and ADR-100.
- **A word's sense changed in place.** ADR-036 and ADR-048; and ADR-002 and ADR-046, which redefined a field and a status.

ADR-049 is the cleanest instance of CLAIM-470's distinctive clause: an inquiry revising what an answer could be.

### 15.2 E3: grammar changes made traceable

The term-change audit read every commit to `luria.yaml` across the whole history and found 34 events: 25 term declarations reworded and 9 terms removed.

- **Every event came with a decision record in the same unit of work** (34 of 34). One event's unit is a single commit, not a pull request.
- **Removals were carried through.** In every removal whose term was in use, every carrying entry was changed in the same unit:

  | Term removed | Carrying entries changed |
  |---|---:|
  | `identity` | 41 of 41 |
  | `self-and-personhood` | 42 of 42 |
  | `admitted` (SYNTHESIS admission) | 12 of 12 |
  | `unadmitted` | 5 of 5 |
  | `hypothesis` (SYNTHESIS route) | 9 of 9 |
  | `derived` | 3 of 3 |

- **Splits moved the entries that moved.** `Deferred`: 177 of 345, exactly the entries reassigned. `ecology` lost `endosymbiosis`: 13 of 50. Each line split moved at least the entries its decision named. The audit counts slightly more entries touched than each decision names, for example 44 against 43, because entries are touched for other reasons in the same unit.
- **Widening needed no re-reading, and got almost none.** `learning-theory` was widened by ADR-036, and 1 of its 92 carrying entries was touched. A widened word still holds every entry that held it before.
- **No redefinition in place.** An earlier version of this section read ADR-048's rewording of `anthology-candidate`, none of whose 237 entries was touched, as a redefinition left untraced. The owner ruled otherwise (2026-11-21): the flag did not change meaning. It records, as it always did, that someone judged the anthology may want the work; ADR-048 changed what that implies about filing here. Revisiting flags is the anthology's process. So nothing needed to be carried through, and the history holds no change of meaning alone (CLAIM-tmpj5aiv, version 2).

There is a second failure, of a different kind (§14.5). A correction to a postmortem's body did not reach its summary, and the generated view propagated the uncorrected summary.

**Verdict: supported for removals, splits and widenings, and falsified in one derived summary. The exception E3 predicts, where only a meaning changes, is untested.** The record traced its grammar changes at the level of the grammar, and at the level of entries whenever entries had to move. The history offers no case of a meaning changing alone, so E3's exception neither held nor failed. That is a gap in the test, not support for the theory.

### 15.3 E4: costs, and errors caused by grammar changes

**Supported.**

- Fifty-eight grammar changes state a migration: 2,664 existing entries changed in all, median 6 per change.
- Ten grammar changes caused an error that was later recorded (§13.9). Two migrations went wrong in ways the census codes elsewhere (ADR-065, ADR-085).
- Four changes were undone within days.

Every error was found by the record itself, most within days.

**Settling or entrenchment is not settled.** Additions to the grammar fell sharply within the first month: new terms went from 82 in the first half of CASE-178's window to 24 in the second. Revisions peaked later, in the period 16 October to 5 November. Falling additions fit a grammar that is settling, but they fit one that is entrenching equally well. The record's own account of itself (SYNTHESIS-012) observes that the verdict depends on how cost is counted:

- in decisions per unit of work, revision stayed cheap;
- in entries carrying the revised type, it grew with the record.

`warrant` went to 315 claims in a day and would now go to 766. We repeat that observation rather than resolve it.

The record has since filed a reason the question is hard, at the level of entries (CLAIM-768, Proposed). That an entry has stopped changing does not show what stopped it. Settling is the decay of its contracted features onto the record's convention, and retention is the start's value on what is copied exactly. The two are told apart only by retention against a reference fixed outside the record's later restatements, such as the owner's originating turn. The same holds of the grammar: a falling rate of change is what both settling and entrenchment predict. LEAD-201 (Open) proposes the measurement for entries. Its grammar-level analogue, retention of a change's original rationale against what later decisions say of it, is not yet proposed.

### 15.4 E5 and E6: who notices, and who judges

**History of these expectations.** An earlier draft of this paper expected the work of noticing and proposing grammar changes to move steadily from the owner to assistants. The census falsified that expectation. E5 and E6 as stated in §7.3 were written after the census, to say what it shows. They are reported here as findings, not as confirmed predictions.

**The earlier expectation fails.** The owner's share of noticing did not fall steadily:

| Period | Owner noticed |
|---|---:|
| 25 Sep–15 Oct | 9 of 43 (21%) |
| 16 Oct–5 Nov | 10 of 20 (50%) |
| 6–20 Nov | 7 of 25 (28%) |

Ratification did not become steadily less explicit either. No owner involvement is recorded for 17 of 43 changes, then 1 of 20, then 12 of 25.

**E5: noticing moved from incidental to institutional.** What changed was who, other than the owner, did the noticing.

- **Early.** Most needs were noticed by *filing agents*, subagents reading a batch of works who found no word for what they read. These were refinements: 18 of the 20 changes filing agents noticed. Most were vocabulary terms. Half were approved explicitly (10 of 20); the rest had no recorded approval (8) or came under a standing permission (2).
- **Late.** Most needs were noticed by *review procedures*: status reviews, synthesis reviews, reading reviews and postmortems. These are run by assistants, to procedures the owner asked for and set up. They noticed revisions as well as refinements: 8 of their 20.

In the flywheel's terms (§7.2, stage 2), noticing that depended on who happened to meet a misfit gave way to noticing by procedures built to look. That is P10's chain acquiring a stronger recognition link, and P7's stage 8: the capacity to run the cycle was itself formed.

**E6: revision stayed with whoever governs the criteria.** Revisions were noticed by the owner (13) or by a procedure (8), almost never by an assistant working unprompted (1) or by a filing agent (2). Delegation took three forms:

- **by category:** standing permission for a class of refinements, mostly vocabulary words;
- **by procedure:** "merging it is the assent";
- **case by case, and explicit:** ADR-089, where the owner "left the split to the assistant's judgement".

Judgment about revisions largely stayed with the owner. In QUESTION-388's terms, the criteria for revising the record's regime remained the owner's. On P8, that is why the record's reflexive inquiry is self-governing only at the level of the owner-and-procedures system, not at the level of its assistants.

### 15.5 E7: the bound on all of the above

Every figure in §§15.1–15.4 is a count taken in the record's own grammar and documents. It shows that distinctions are drawn, changes are traced and errors are found. It cannot show that the inquiry is better for any of it (ARG-028, CLAIM-266). Three entries sharpen the point against this paper's own evidence:

- **CLAIM-402 and CLAIM-342.** Categories that an institution acts on produce their own confirming regularities. A distribution over a vocabulary is shaped by the vocabulary.
- **CLAIM-448 and CASE-221.** What a legibility regime selects for recording can make a record look coherent. An intervention that improves self-governance can at first make disagreement more visible.
- **CASE-084.** A record can trace every commitment perfectly and still exclude the right explanation from its vocabulary.

None of these is answered here. Section 19 proposes the measurements that could.
