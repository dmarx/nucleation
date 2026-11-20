<!-- scratch/manuscripts/from-obstruction-to-reorganization/10-discussion.md -->

## 17. Discussion

### 17.1 What was delegated, and what it risks

The question that began this study was practical: which parts of the owner's role in revising the grammar could an assistant take over? The census answers for the history (§15.4).

Noticing was delegated early and widely. Filing agents noticed missing words, and later review procedures noticed missing relations, unused fields and lines whose parts barely relate. Refinement was often delegated by category, under standing permission. Revision mostly was not. The owner noticed or decided most revisions, and the clearest hand-over (ADR-089) was explicit and limited to one case.

That division is close to the one a cautious design would choose. It also carries a risk the record has already described elsewhere. Where a capacity is learned by doing the work and decays with disuse, support that does the work first lowers the capacity kept (CLAIM-602, Active). Past a point, withdrawing the support no longer restores the capacity (CLAIM-605, Active). Support should therefore be judged by the capabilities it leaves later, not by present output (CLAIM-675, Active).

Agent filing, and procedures that notice on the owner's behalf, are such support. Whether the owner's own ability to notice what the grammar needs is being maintained or eroded is not measured anywhere in the record. QUESTION-471 (Open) states the related risk for the record as a whole, and names Nucleation as "a small-scale case of the tension": incorporation fast enough to outrun evaluation.

### 17.2 When a distinction is worth drawing

The formal results the record holds give a criterion and a stopping rule:

- **The criterion.** A coarse description preserves a judgment exactly when the judgment is constant on each class it merges (CLAIM-350, Active). An organization's policy is acceptable in every circumstance exactly when the circumstances it cannot tell apart share an acceptable action (CLAIM-535, Active). A distinction is *needed* when two situations the grammar treats alike call for different actions. `Deferred` failed this test, and ADR-041 and ADR-053 answered it.
- **The stopping rule.** Causes are found at the coarsest description whose interventions are unambiguous (CLAIM-497, Active), so a split that makes no action-relevant difference is over-splitting. ADR-056's pilot rejected a field on these grounds, and ADR-036 widened a word instead of splitting it.

Two results qualify the picture of revision as successive splitting:

- **Revision need not nest.** The best categories at a higher budget need not refine the best at a lower one (CLAIM-387, Active), so a better grammar may merge and re-split rather than add.
- **Copies change the trade-off.** One set of bins realizes one partition only when each item is stored once (CLAIM-313, Active). Multi-valued fields, such as several lines or several topics, can let overlapping classifications coexist. Some pressure to split can therefore be met by allowing more than one value. ADR-040, which made `line` many-valued, did exactly that.

### 17.3 Correction is not maintained capacity

CLAIM-422 (Active) separates three things: a successful corrective act, an executable procedure, and a maintained capacity. CASE-138 (Active) is the record's instance: Challenger to Columbia. NASA corrected its decisions and its safety organization after 1986, and the Columbia board found the same failure mechanisms recurring in 2003. The case puts it plainly: "A correction recorded is not a capacity maintained." Argyris's account (THEORY-145) adds that organizations which espouse revising their governing values characteristically fail to.

Nucleation has many corrective acts and several procedures: decisions, skills, worklists, triggers. It has early mechanisms meant to make the capacity last, chiefly postmortems and status reviews. Whether they will last is not something eight weeks can show. Section 14.5, a correction that stopped one level short, is a small reminder that they have not yet been shown to work.

A record may also improve what an organization knows more than what it does. In CASE-166 (Proposed), a simulation, keeping an incident team's records through a handoff cut the company's error in estimating its own state "about eightfold while barely changing what it does". Any evaluation of a record of inquiry that scores only decisions may find little. Any that scores only knowledge may overstate what the record does for the work.

### 17.4 Signatures of misfit, and their limits

Could an assistant detect when the grammar needs changing, without being asked? The census shows what each misfit looked like before it was noticed (§15.1). Each form suggests something a script could compute:

| Before it was noticed | A computable signature | Instance |
|---|---|---|
| Prose carrying a distinction | Free-text notes on entries that share one value, clustering into recurring kinds | 177 of 345 Deferred LITs noting a failed search (ADR-041) |
| A scheme unused while its content goes elsewhere | No new entries over a period, while a neighboring scheme's entries are about that scheme's subject | No ARG for two weeks; 42 claims about support (ADR-061) |
| A type re-acquiring another type's fields | Entries of one scheme gaining another scheme's fields and relations | Admitted syntheses with a CLAIM's fields (ADR-084) |
| A field that does not discriminate | One value holding nearly all entries | 96.4% of LEADs at `idea` (ADR-111) |
| One word, several senses | Repeated reports of a missing word; one tag carrying senses that readings keep apart | `self-and-personhood` (ADR-024), `learning-theory` (ADR-036) |
| A line made of separate inquiries | Relations dense within candidate parts and sparse across them | 25 within, 8 out, 3 in (ADR-082) |

One of these is already a tool: `scratch/formal/line_parts.py` (ADR-083) has driven four splits. The others are sketches.

Four limits apply to all of them:

- **They were found in hindsight.** They were identified by people who knew the outcome, with no count of false alarms and no misfits held back to test against.
- **They are measured in the grammar.** A distribution over a vocabulary is partly produced by the vocabulary (CLAIM-402), and what gets recorded is selected (CLAIM-448). A clean signature is weak evidence that nothing needs changing.
- **Some are not necessary.** A real unit need not be weakly coupled (CLAIM-388), so the absence of a coupling signature shows little.
- **They do not choose the response.** The same signature, one word with several senses, led to a split in ADR-024 and to a widening in ADR-036.

Detection is a plausible task to delegate. Choosing the remedy depends on which actions the inquiry commits to (§17.2) and what the change will cost to keep (§15.3). In this history, that choice stayed with the owner for revisions.

### 17.5 Memorylessness is not only a cost

The predecessor treated memoryless collaborators as the problem. March's model of organizational learning suggests a qualification (THEORY-142, Proposed). Slow socialization and moderate turnover raise what an organization knows, while an organization with no turnover in a changing environment degrades. Fresh collaborators who do not share the record's framings may play turnover's part: a source of exploration that a well-anchored record would otherwise lack. CLAIM-184's warning that anchors entrench is the other side of the same trade. The record has no measure of which effect dominates.

### 17.6 This paper's own drafts

The predecessor's CLAIM-178 holds that a manuscript drafted straight from an exchange drops commitments and changes its thesis silently, and that this shows only against a record. This paper's history is not that comparison:

- its first sketch was written by an external assistant from reading the repository;
- its drafts were written and checked by assistants of one family.

Checking against the record nonetheless corrected it repeatedly. A decision was misattributed. Dates and counts were wrong. A premise about who governed the grammar was false. And the first sketch omitted the account of inquiry the predecessor had built. The drafts are kept and could be compared blind by someone else.
