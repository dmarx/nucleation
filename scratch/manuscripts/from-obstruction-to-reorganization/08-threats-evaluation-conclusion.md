<!-- scratch/manuscripts/from-obstruction-to-reorganization/08-threats-evaluation-conclusion.md -->

## 10. Threats to validity, and limitations

**Construct validity.**

- **Self-measurement.** Every count is taken in the grammar it evaluates (E6, ARG-028, CLAIM-266). A populated field shows use, not correctness.
- **Policy confound.** Decision records accompany grammar changes partly because ADR-001 required them, so the coupling of decisions to grammar changes is in part compliance with that rule.
- **Definitions.** "Grammar", "misfit", "refinement" and "revision" were defined before coding (§5.2, `CODEBOOK.md`). The boundary cases the coders reported show these are not crisp: line rules (ADR-085, ADR-088), storage changes (ADR-079) and widened senses (ADR-036).
- **Touched is not re-read.** The term-change audit counts entries changed in the same unit of work as the change. That is a proxy for re-reading, not a measure of it.

**Internal validity.**

- **The framework was built from the case.** CLAIM-470 cites CASE-178. The inquiry tuple and the two-loop reading came from an assistant reading luria (§2). The expectations of §3.6 are postdictions.
- **No counterfactual.** Nothing shows what the record would have been with a fixed grammar, or with no decision records.
- **Selection.** The census removes the selection of *cases* but not the selection of *decisions*. Misfits never noticed, or noticed and left, are absent (§8.1).

**Reliability.**

- **Agreement.** Agreement between coders was high on the fields the argument uses (κ 0.81–1.00), moderate on the form of the misfit (0.65) and low on outcome (0.38), which is not used.
- **One model.** All five coders were instances of one model. Their agreement may partly reflect shared bias, so a human coder is needed.
- **Missing records.** Thirty-one decisions do not record who decided. The census codes these as unknown rather than guessing.

**External validity.**

- One owner, one record and eight weeks.
- The comparison records the record holds (luria's and strata-g's) have small grammars, and are not controls.

**Author independence.** The record, its studies of itself, its postmortems, the census, the scripts and this paper were produced largely by AI assistants working at the owner's direction, several of them instances of the model that drafted this text. The data and scripts are in the repository and can be re-run by others. The interpretations should be checked by someone outside the project.

**Unread sources.** Several related works are registered but unread (§4).

---

## 11. Future evaluation

### 11.1 Historical replay, with the census as ground truth

Reconstruct the record at the commit before each grammar change in the census. Give an assistant the grammar, the entries and the work then in progress, without the decision that followed, and ask it to report misfits. Score it against the census:

- Did it find the misfit the decision addressed?
- Did it propose a change at the right level, and distinguish refinement from revision?
- Did it recommend no change where the record showed restraint (ADR-036, ADR-050, ADR-056)?

The signatures of §9.4 give a scripted baseline to compare it with. Add commits at which no change followed, to count false alarms.

### 11.2 Counting the misfits nobody noticed

Sample the source exchanges and readings filed before each period. Have independent readers classify each contribution as held faithfully, forced into a category, kept only in prose, or lost, against the grammar of its day. This is the audit A25 proposed and CLAIM-419 records as unrun. It supplies the denominator for E1, and it shows whether unnoticed misfits became rarer as review procedures grew.

### 11.3 Governed and ungoverned schema change

CASE-253 (Proposed) crosses fixed against modifiable schemas with informal against explicit governance, for agents keeping a record. It tests CLAIM-667: governance raises the value of modifiability where inherited categories are inadequate. It also tests its secondary prediction, CLAIM-665: on routine tasks, governance adds cost and no benefit. The record has rejected one outside study as support for CLAIM-667 (ARG-098), so the hypothesis has no evidence behind it yet. Two further designs separate improving the record from improving the improver:

- CASE-254, which diagnoses before repairing;
- CASE-255, which compares improvers across generations.

### 11.4 Fixed, refinable and revisable regimes

CLAIM-470 names the study that would test its own distinctive clause. Investigators start with a schema that knows only kinds of equilibrium, studying a system that can be stationary or oscillatory. They work under one of three regimes:

- **fixed:** answers may be updated;
- **refinable:** distinctions may be added;
- **revisable:** questions, variables and evaluation may change.

All three are scored on the same external benchmarks. If the revisable regime finds the oscillation no sooner and no more reliably than the refinable one, revision has no point for practice. The census (§8.1) suggests the record does both, but cannot say which helped.

### 11.5 Delegation and the capacity it leaves

Measure the owner's own rate of noticing misfits over time, against the share noticed by procedures. CLAIM-675 says to judge support by the capabilities it leaves. CASE-262 (Proposed) is a design for this with learners: an assistant that does the hard step, against one that does only what the learner cannot yet do. Adapted, it would compare procedures that report candidate misfits with procedures that make the changes.

### 11.6 Knowledge and action

Following CASE-166, score a record of inquiry on two outcomes separately: what its keepers know about the state of their argument, and what they decide. LEAD-155 (Open) gives a design for the first: file one corpus under two grammars and test whether the grammar changes later inquiry. LEAD-079 (Open) asks for the identity-not-structure finding of §2.1 to be replicated with another owner or assistant family.

---

## 12. Conclusion

The predecessor manuscript held that an argument developed with memoryless collaborators drifts in identity, not structure, and that a project memory helps by making structure persist as addressable anchors. This paper took up the objection that manuscript left: anchors are written in a grammar that is fixed before the inquiry knows what it needs. Read through the record's account of inquiry as specification, the grammar is part of the inquiry. Changing it is the inquiry acting on its own regime, and a record that secures traceable change for its claims should secure it for its grammar.

The census of all 114 of the record's decisions shows what happened:

- **The grammar changed 88 times in eight weeks:** 62 refinements and 25 revisions, including a redefinition of what counts as an answer, boundaries redrawn between kinds of entry, a type withdrawn, and lines of inquiry split.
- **Misfits were forced or kept in prose before they were noticed,** in almost every case where there was a misfit at all.
- **Grammar changes were traced** by decision in every case examined, and carried through the entries when entries had to move. They were not carried through when only a meaning moved.
- **Changes had costs.** They migrated 2,664 entries, ten caused errors the record later found, and four were undone within days.

The work of noticing what the grammar needed was delegated, but not in the way first expected. It moved from filing agents who happened to meet a missing word to review procedures built to look. Permission for refinements was given by category. Judgment about revisions stayed mostly with the owner.

None of this shows that the inquiry is better for it. The record measures itself in its own grammar, its framework was built partly from its own history, and its expectations were written after the fact. What the case does show is a research record that made changing its own grammar an ordinary, traced and reviewable part of its work. The pattern of what was and was not delegated suggests where an assistant can help: in noticing. The record itself proposes how to test whether assistants could also judge.
