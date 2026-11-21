<!-- scratch/manuscripts/from-obstruction-to-reorganization/11-threats-evaluation-conclusion.md -->

## 18. Threats to validity, and limitations

**Construct validity.**

- **Self-measurement.** Every count is taken in the grammar it evaluates (E7, ARG-028, CLAIM-266). A populated field shows use, not correctness.
- **Policy confound.** Decision records accompany grammar changes partly because ADR-001 required them, so the coupling of decisions to grammar changes is in part compliance with that rule.
- **Definitions.** "Grammar", "misfit", "refinement" and "revision" were defined before coding (§12.2, `CODEBOOK.md`). The boundary cases the coders reported show these are not crisp: line rules (ADR-085, ADR-088), storage changes (ADR-079) and widened senses (ADR-036).
- **Touched is not re-read.** The term-change audit counts entries changed in the same unit of work as the change. That is a proxy for re-reading, not a measure of it.
- **The unit of work changed under staging.** Since 21 November a change reaches `main` inside a promotion of a whole batch, so the audit's unit, the pull request that reached main, is wider than the decision's own pull request (§15.2). Its counts for later events are more lenient than for earlier ones.
- **Recording, not involvement.** The fifth batch records the owner's words for every decision (§13.1). Part of that is how rulings are now written down (inline on the promotion pull request, or by choosing a filed alternative), so a rise in explicit ratification need not mean more owner involvement.

**Internal validity.**

- **The framework was built from the case.** CLAIM-470 cites CASE-178. The inquiry tuple and the two-loop reading came from an assistant reading luria (§4). The expectations of §7.3 are postdictions.
- **The case now carries the framework.** Since 21 November the record has a line, `learning-and-inquiry`, added for this paper's theme (ADR-130), and its work is renamed after this draft (ADR-135). Several of that day's decisions answer this draft's open items. Evidence drawn from the record after that day is not independent of the draft in the way earlier history is.
- **No counterfactual.** Nothing shows what the record would have been with a fixed grammar, or with no decision records.
- **Selection.** The census removes the selection of *cases* but not the selection of *decisions*. Misfits never noticed, or noticed and left, are absent (§15.1).

**Reliability.**

- **Agreement.** Agreement between coders was high on the fields the argument uses (κ 0.81–1.00), moderate on the form of the misfit (0.65) and low on outcome (0.38), which is not used.
- **One model.** All five coders were instances of one model. Their agreement may partly reflect shared bias, so a human coder is needed. The owner's ruling filed this as a lead (LEAD-206, Open).
- **One coder, a participant, for the fifth batch.** The 22 decisions of 21 November were coded by one coder, the assistant revising this draft, which took part in the session that filed many of them and drafted several. No second coder has seen them (§12.3).
- **Coded status goes stale.** The census codes each decision's status as it stood when coded. Thirty-four of the first 114 have since moved from Proposed to Active. The argument uses outcome from the decisions themselves, not the status field (§13.1).
- **Missing records.** Thirty-one of the 88 grammar changes, and 42 of all 114 decisions, do not record who decided. The census codes these as unknown rather than guessing. Every decision of the fifth batch records one.

**External validity.**

- One owner, one record and eight weeks.
- The comparison records the record holds (luria's and strata-g's) have small grammars, and are not controls.

**Author independence.** The record, its studies of itself, its postmortems, the census, the scripts and this paper were produced largely by AI assistants working at the owner's direction, several of them instances of the model that drafted this text. The data and scripts are in the repository and can be re-run by others. The interpretations should be checked by someone outside the project.

**Unread sources.** Several related works are registered but unread (§11).

---

## 19. Future evaluation

### 19.1 Historical replay, with the census as ground truth

Reconstruct the record at the commit before each grammar change in the census. Give an assistant the grammar, the entries and the work then in progress, without the decision that followed, and ask it to report misfits. Score it against the census:

- Did it find the misfit the decision addressed?
- Did it propose a change at the right level, and distinguish refinement from revision?
- Did it recommend no change where the record showed restraint (ADR-036, ADR-050, ADR-056)?

The signatures of §17.4 give a scripted baseline to compare it with. Add commits at which no change followed, to count false alarms.

### 19.2 Counting the misfits nobody noticed

Sample the source exchanges and readings filed before each period. Have independent readers classify each contribution as held faithfully, forced into a category, kept only in prose, or lost, against the grammar of its day. This is the audit A25 proposed and CLAIM-419 records as unrun. It supplies the denominator for E1, and it shows whether unnoticed misfits became rarer as review procedures grew.

### 19.3 Governed and ungoverned schema change

CASE-253 (Proposed) crosses fixed against modifiable schemas with informal against explicit governance, for agents keeping a record. It tests CLAIM-667: governance raises the value of modifiability where inherited categories are inadequate. It also tests its secondary prediction, CLAIM-665: on routine tasks, governance adds cost and no benefit. The record has rejected one outside study as support for CLAIM-667 (ARG-098), so the hypothesis has no evidence behind it yet. Two further designs separate improving the record from improving the improver:

- CASE-254, which diagnoses before repairing;
- CASE-255, which compares improvers across generations.

### 19.4 Fixed, refinable and revisable regimes

CLAIM-470 names the study that would test its own distinctive clause. Investigators start with a schema that knows only kinds of equilibrium, studying a system that can be stationary or oscillatory. They work under one of three regimes:

- **fixed:** answers may be updated;
- **refinable:** distinctions may be added;
- **revisable:** questions, variables and evaluation may change.

All three are scored on the same external benchmarks. If the revisable regime finds the oscillation no sooner and no more reliably than the refinable one, revision has no point for practice. The census (§15.1) suggests the record does both, but cannot say which helped.

### 19.5 Delegation and the capacity it leaves

Measure the owner's own rate of noticing misfits over time, against the share noticed by procedures. CLAIM-675 says to judge support by the capabilities it leaves. CASE-262 (Proposed) is a design for this with learners: an assistant that does the hard step, against one that does only what the learner cannot yet do. Adapted, it would compare procedures that report candidate misfits with procedures that make the changes.

### 19.6 Drift, measured on the record's own history

The formal account of drift filed on 2026-11-21 names three measurements the record's history allows, and the account of anchoring filed after it two more:

- **Ideas restated before they were coded (LEAD-204).** Trace them through the exchange history, to tell whether their drift saturates at the collaborators' framings, grows linearly, or has no direction. Also test whether the ideas furthest from those framings were lost first, as CLAIM-776 predicts.
- **Revision against citation (LEAD-199).** Count how often each claim is substantively revised before and after it is first relied on.
- **Retention of the originating turn (LEAD-201).** Measure, judged blind against a metric fixed in advance, how much of the owner's originating turn each settled claim retains. This separates exact copying from contraction onto convention (CLAIM-768).

- **The reader's offset (CLAIM-793).** Have one coded entry read and restated by several sessions briefed alike and by several briefed differently, and compare each restatement with the entry. If the account is right, the first group's restatements agree with each other more than the second group's, and differ from the entry by more. Agreement among readers who share a framing is then no evidence of fidelity.
- **Stale copies (CLAIM-789).** List every hand-copied or carried-over text (summaries, titles quoted in other entries, fields carried to a successor) and check it against the current version of its source. Compare the rate of staleness with that of generated views.

Together they would test the anchoring account of §5 on the record that motivated it, with one reference, the originating turns, fixed outside the record's later restatements.

### 19.8 Checks the record can run now (added 2026-11-21)

Three checks need no new design:

- **E3's exception, on ADR-130.** Read the 73 carriers of `record-as-apparatus` the narrowing did not touch, and classify each as the record's own case or inquiry in general (§15.2). If entries of the second kind stayed under the narrowed line with no note, carry-through failed where only a meaning moved, as E3 predicts. If ADR-130's deferral to the synthesis review was kept, the exception held.
- **The fifth batch, recoded.** Give the 22 decisions of 21 November to a coder who did not take part in them, ideally the human coder of LEAD-206, and report agreement as in §13.1.
- **The census in the pipeline.** The analytics pipeline already reports the census's coverage and status drift. Its census copy (`scratch/formal/decision-census`) and this draft's (`analysis/`) have diverged: only this draft's holds the fifth batch and the fourth period. Pointing the pipeline at one copy would let every figure in §§13–16 be regenerated and dated by one command.

### 19.7 Knowledge and action

Following CASE-166, score a record of inquiry on two outcomes separately: what its keepers know about the state of their argument, and what they decide. LEAD-155 (Open) gives a design for the first: file one corpus under two grammars and test whether the grammar changes later inquiry. LEAD-079 (Open) asks for the identity-not-structure finding of §5.2 to be replicated with another owner or assistant family.

---

## 20. Conclusion

Part I set out a theory of how systems learn and inquire.

- **Distinctions.** A distinction is relative to a target and a regime. Whether to draw a new one depends on whether situations treated alike call for different actions. As resources grow, categories may need to split, merge or be re-carved.
- **Learning** is the formation of a maintained capacity, a new distinction or a new channel. It is occasioned by a discrepancy the system cannot resolve, it is not guaranteed by it, and it is costed in three separate ledgers. A capacity's maintenance is known only by intervention, and help that does the work erodes it.
- **Inquiry** is a form of specification that can revise what counts as an answer. It is self-governing only where the criteria of revision are the system's own.
- **Transmission.** Without anchors, transmission drifts toward the transmitters. An anchor secures what it is tied to: tied to the target, content and a discrepancy that registers; tied to the inquiry's own past, continuity; tied to nothing, bias. What a record can secure is traceable change, not fidelity.
- **Collectives** learn through a chain of separable achievements, any of which can fail while the others hold, and they confirm themselves without independent evidence.

From these principles the theory predicts a cycle for any inquiry held in a revisable apparatus. Misfits are absorbed before they are noticed. Noticing is the scarce step. Diagnosis weighs actions, not just data. Revision includes merging and withdrawal as well as splitting. Carry-through is predicted to fail where only a meaning moves. Maintenance fails where a correction stops short. Each turn stores work that later turns use, and that also entrenches.

Part II showed that the record in which the theory was developed is an apparatus of exactly this kind, and that each principle has a mechanism in its machinery. Many of those mechanisms were adopted for local reasons before the claims they embody were argued.

Part III traced what the machinery did over eight weeks:

- **The grammar changed 88 times to 20 November:** 62 refinements and 25 revisions, including a redefinition of what counts as an answer and the withdrawal of an abstraction that had overreached. The 22 decisions of 21 November add three grammar changes, two of them revisions, and many more changes to how the record files and reviews, decided by the owner among alternatives filed side by side.
- **Absorption came first.** In almost nine cases in ten, the misfit had first been absorbed, forced or held in prose.
- **Carry-through was traced where entries had to move.** Removals reached every entry that used the removed term, and splits moved the entries they had to. A correction failed to reach one derived summary. No change of meaning alone is in the history, so that predicted failure is untested.
- **The costs were real.** 2,664 entries were migrated, and ten changes caused errors that later checks found.
- **Noticing became institutional.** It moved from whoever happened to meet a misfit to procedures built to look.
- **Judgment about revision stayed with the owner,** who governs the criteria. On 21 November the initiative to file, and to merge into staging, moved to the assistant with a report and a revert, while statuses and decisions stayed the owner's.
- **The cycle turned on its own procedures.** Lapses the owner caught became rules within a day: filing fills the gaps a source leaves, the decoder counts what it drops, a lifted hold is acted on. One rule failed once in a new context and was caught again.
- **The theory was itself revised.** The theory's own account of learning went through the cycle it describes, and the standings used to state the theory are products of that cycle.

What the case cannot show is that any of this made the inquiry better. The theory and its demonstration share a source. The record measures itself in its own grammar. The expectations were written after the history. These are the limits of a reflexive case, and they are why §19's designs matter. Replaying the record's history to an assistant that has not seen the decisions would test whether noticing can be delegated. Counting the misfits nobody noticed would supply the denominator the census lacks. Comparing fixed, refinable and revisable regimes on common benchmarks would test whether revision does work that refinement cannot. Measuring the owner's own noticing over time would test whether the help that makes the cycle run is eroding the capacity to govern it.

If the theory is right, a system that inquires for long enough will meet the limits of its own apparatus. What then distinguishes inquiry from mere accumulation is whether it can notice those limits, decide what they call for, change the apparatus, carry the change through what it already holds, and keep the capacity to do so again. The record studied here did each of these some of the time. It failed at each in ways the theory names, and it kept a history detailed enough to tell which was which.
