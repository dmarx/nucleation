<!-- scratch/manuscripts/from-obstruction-to-reorganization/06-census-and-cases.md -->

## 13. The census, and eight cases drawn from it

### 13.1 The census

Of the 114 decisions, **88 changed the grammar** (§12.2 defines the term). The tables below are produced by `analysis/census.py` from the coded census and are reproduced in `analysis/census_report.md`.

**Agreement between coders.** These figures come from the 30 decisions coded twice.

| Field | Agreement | κ |
|---|---:|---:|
| Grammar change | 0.97 | 0.92 |
| Refinement, revision or restraint | 0.90 | 0.84 |
| Trigger | 0.87 | 0.81 |
| Who noticed | 0.87 | 0.82 |
| Who proposed | 0.90 | 0.85 |
| Who decided | 1.00 | 1.00 |
| Ratification | 1.00 | 1.00 |
| Form of the misfit | 0.73 | 0.65 |
| Outcome | 0.77 | 0.38 |

The low κ on outcome comes from a convention the codebook left open: coders split on whether a Proposed decision already applied is "in force" or "unknown". We therefore do not use the outcome field. Reversals are taken from the decisions themselves.

**Refinement and revision.** Of the 88 grammar changes, 62 were refinements, 25 revisions and 1 restraint.

| Period | Changes | Refine | Revise | Restraint |
|---|---:|---:|---:|---:|
| 25 Sep–15 Oct | 43 | 37 | 6 | 0 |
| 16 Oct–5 Nov | 20 | 8 | 11 | 1 |
| 6–20 Nov | 25 | 17 | 8 | 0 |

Revision is not rare: it makes up 28% of grammar changes. It is concentrated in the middle period. The level at which changes happened moved over the eight weeks:

- **Early:** vocabularies and their terms, in 35 of 43 decisions.
- **Middle:** vocabularies still (8 of 20), then lint patterns, relations and statuses.
- **Late:** relations (13 of 25), fields, views and lines.

**Who noticed.** The table shows who noticed the need for each grammar change.

| Period | Changes | Owner | Filing agents | Assistant in session | External assistant | Review procedure | Unknown |
|---|---:|---:|---:|---:|---:|---:|---:|
| 25 Sep–15 Oct | 43 | 9 | 16 | 1 | 0 | 4 | 13 |
| 16 Oct–5 Nov | 20 | 10 | 1 | 3 | 1 | 4 | 1 |
| 6–20 Nov | 25 | 7 | 3 | 2 | 0 | 12 | 1 |

Who noticed depends strongly on the kind of change:

| Noticed by | Refinements | Revisions |
|---|---:|---:|
| Filing agents | 18 | 2 |
| Owner | 12 | 13 |
| Review procedures | 12 | 8 |
| Assistant in session | 5 | 1 |

**Ratification.** Of the 88 changes:

- 48 record the owner's approval of that change;
- 6 cite a standing permission ("The owner authorised extending the vocabulary as the record sees fit", ADR-034);
- 4 were ratified only by merging, or by a review procedure the owner had delegated ("merging it is the assent");
- 30 record no owner involvement at all.

The owner is the decider in 49 changes, an assistant in 6 and a review procedure in 2. The decider is not stated in 31.

**Costs and errors.** Fifty-eight changes state how many existing entries they migrated: 2,664 in all, median 6. Ten grammar changes were followed by a recorded error that the change caused (§13.9). Four were undone within days (ADR-015 in part, ADR-076, ADR-077, ADR-080).

Section 15 reads these results against E1 to E7, and §16 against the flywheel of §7.2. The cases below are drawn from the census to illustrate each type it contains: refinement, revision and restraint, noticed by the owner, by an agent and by a procedure.

### 13.2 Refinement: CASE kind against standing (ADR-042)

*Refinement; noticed by the owner, proposed by an assistant.*

`standing` (documented, stipulated or fictional) says how much of a case is fact, and it was being read as what *kind* of case it is. The owner asked, "are we able to construct something like a typology of CASEs?" A survey of all 81 cases found that `stipulated` alone held proposed studies, thought experiments, formal constructions and counterfactuals.

ADR-042 added a required `kind` field with six values. It rejected four alternatives:

- **Adding values to `standing`:** this "would answer two questions with one field, which is the present problem".
- **A separate STUDY scheme:** this would split the indexes and the relations.
- **Tags:** these say what a case is about, not what it is.
- **Finer kinds:** "six is what the 81 cases need".

By 20 November the record held 298 CASEs:

| Kind | Documented | Stipulated | Fictional |
|---|---:|---:|---:|
| Specimen | 61 | 13 | 0 |
| Thought experiment | 1 | 24 | 29 |
| Construction | 2 | 38 | 51 |
| Reported study | 12 | 0 | 0 |
| Proposed study | 0 | 54 | 1 |
| Executed study | 3 | 7 | 2 |

Every case has a kind because the linter requires one, so coverage shows nothing. The distribution does show something. Fourteen of eighteen combinations are populated, and constructions, thought experiments and executed studies occur under all three standings, so the two fields answer different questions. They are not statistically independent, and could not be: a reported study is documented by its nature.

### 13.3 Refinement of criteria: CLAIM warrant against status (ADR-043)

*Refinement; noticed by the owner, proposed by an external assistant.*

In an exchange on 14 October, ChatGPT separated "what we've demonstrated by construction, what we've made plausible through examples, and what still requires empirical evidence". The owner asked whether anything in the record already did so. Nothing did: `status` says whether the record accepts a claim, and `role` says in whose voice it is made.

ADR-043 added a `warrant` field (demonstrated, empirical, interpretive). It was piloted on 28 claims before the owner made it required. Eight readers then classified the remaining 289 the same day. The decision reports 315 claims classified, two fewer than its parts sum to, and flags nineteen compound claims that were given a single warrant.

Among the 766 claims on 20 November:

| Warrant | Active | Proposed | Other | Total |
|---|---:|---:|---:|---:|
| Demonstrated | 198 | 39 | 6 | 243 |
| Empirical | 10 | 20 | 1 | 31 |
| Interpretive | 185 | 262 | 45 | 492 |

Thirty-nine Proposed claims are demonstrated, and 185 Active ones are interpretive, so how a claim is supported and whether it is accepted vary independently. This change also caused an error later. Two readings of `warrant` were in use, and one batch relabelled a claim on the reading the owner then rejected (version 2, 19 October).

### 13.4 Revision of an answer space, done twice: Deferred, Unavailable, Unfetched (ADR-041, ADR-053)

*Revision of a status vocabulary; noticed by the owner.*

`Deferred` on a LIT held two situations: not yet tried, and tried without reaching a lawful copy. On 13 October, 177 of the 345 Deferred LITs carried a free-text note of a failed search. The distinction existed only in prose, and ADR-041 moved those 177 to a new status, `Unavailable`. It declined a further split, between "no lawful copy found" and "found but not fetchable by this client", because "eight entries do not justify a sixth status".

On 25 October the owner supplied two such works by hand and asked for a status for "content that would be easy for me to access where you encountered obstacles". ADR-053 found **43** such entries, not eight. It also argued from an asymmetry of cost: clearing such an entry means only that the owner supplies a copy. So it added `Unfetched`, and made the owner's queue a generated page. Both a larger count and a change in what the distinction was for led to the reversal of ADR-041's restraint. Today 2,114 LITs are Active, 531 Unavailable, 179 Unfetched and 58 Deferred.

### 13.5 Revision of a boundary: CLAIM and ARG (ADR-032, ADR-061)

*Revision; who noticed is not recorded.*

ADR-032 created ARG for judgments about inferences, to be filed only when something had to point at an inference. After 10 October no ARG was filed for two weeks, while objections to inferences kept being filed as CLAIMs. A reading of all 453 claims found 42 whose subject was whether one entry supports another, and 17 that mixed the two. Filed as CLAIMs, such objections look like rival positions, so the record could not say "the conclusion may stand, but this argument for it fails".

ADR-061 redrew the boundary: an ARG is any claim about support. It filed 29 ARGs (15 Rejected, 13 Proposed, 1 Active), superseded 14 claims and split 15. Each entry had to be read to decide which kind of thing it was. This is a revision: existing entries were reassigned to a different kind of thing.

### 13.6 Revision by withdrawal: SYNTHESIS (ADR-075, ADR-076, ADR-084)

*Revision; noticed by the owner.*

ADR-075 first proposed filing integrations as thesis claims. ADR-076, the same day (7 November), instead gave them a scheme, SYNTHESIS, with an admission route. ChatGPT's reviews, pasted by the owner, added an `admission` field and removed a status. Admitted syntheses turned out to carry exactly a CLAIM's fields. Because `objects_to` accepted only CLAIMs, an objection to an admitted synthesis would have been stranded.

On 8 November the owner asked what the admitted syntheses added. ADR-084 withdrew the asserting role: a SYNTHESIS asserts nothing of its own, and whatever adds to its components is a CLAIM. Eleven admitted syntheses returned to CLAIM, nine under their original codes, and ADR-076, ADR-077 and ADR-080 were superseded. The asserting abstraction lived about a day. The episode is short, but it is the record's clearest case of the grammar *losing* a distinction it had briefly drawn.

### 13.7 Revision of the unit of inquiry: splitting lines (ADR-083 and its applications)

*Revision; noticed by the owner, then by a procedure.*

A *line* names the inquiry an entry belongs to. When the record tried to write an account of the `nucleating-argument` line, the account fell into five parts. Three were densely linked to one another, and two were not. "What a record of a developing argument keeps" had 25 relations inside it, 8 going out and 3 coming in.

ADR-083 turned the observation into a rule, and `scratch/formal/line_parts.py` into a tool: it counts stored relations within and across a line's candidate parts. Four lines have since been split:

- `nucleating-argument` in three (ADR-082, 43 entries);
- `readiness` (ADR-087, 30 entries; 69 of 79 relations within parts);
- `will-organization` (ADR-089);
- `organizational-normativity` (ADR-100, 29 entries; 93 of 102 within parts).

The tool does not decide. ADR-087 found that 24 of 28 cross-part pairs were mere mentions, so the type of relation matters, not only the count. ADR-089 split for a different reason: a root question refined the line's own. The owner "left the split to the assistant's judgement" in ADR-089, the clearest delegated decision in the census.

The tool also has a known blind spot. CLAIM-388 (Active) shows that a real unit need not be weakly coupled to its surroundings: a uniformly coupled system can have an exactly closed aggregate. So low coupling across a boundary suggests a split, but its absence does not show that no split is needed.

### 13.8 Restraint

*Rejected and deferred proposals, and refusals inside accepted decisions.*

- **ADR-056 (Rejected),** noticed by the owner and proposed by an external assistant. It proposed four kinds of TERM, to be piloted before becoming a field. Of sixteen sampled TERMs, eleven sorted cleanly and five forced an arbitrary choice, exactly where the field was meant to decide. The pilot rejected the field.
- **ADR-050 (Deferred).** A protocol for words such as "organized" and "effective" stopped at the convention rung, because a lint "would fire 395 times".
- **ADR-036.** Readers reported independently that the vocabulary had no word for training dynamics. The owner widened `learning-theory` rather than add a word. (The census codes this as a revision, because an existing word's meaning changed. §15.2 asks whether its 92 carrying entries were re-read.)
- **Refusals inside accepted decisions.** ADR-042 refused a STUDY scheme, and ADR-041 refused the sixth status until ADR-053.

### 13.9 When grammar changes went wrong

Ten grammar changes have a recorded later error that they caused:

| Change | What went wrong | How it was found |
|---|---|---|
| ADR-015 | One word for self and personhood forced a choice on a reading (LIT-142) | ADR-024, the next day |
| ADR-043 | Two readings of `warrant` were in use; a claim was relabelled on the rejected one | Its version 2 |
| ADR-047 | Narrowing claims to promote them lost the wider claims: 53 of 93 kept the wider form only in prose | Its version 4, then a sweep |
| ADR-057 | Revisions made for another purpose passed a check; an entry was listed as read when it was not | Its versions 5 and 8 |
| ADR-076, ADR-077 | Moved claims' objections would have been stranded | ADR-084 |
| ADR-090 | A view read converse fields that ADR-079 had stopped storing, and undercounted (277 for 406) | Its version 2 |
| ADR-104 | A claim was included in a work for a proviso only | Its version 2 |
| ADR-107 | A form was filed before its source was read, then rewritten twice within hours | POSTMORTEM-002 |
| ADR-109 | A stage field that did not discriminate; misleading converse descriptions | POSTMORTEM-002 |

The process search adds two errors in migrations that the census codes under other headings:

- **ADR-065's migration** wrote the question but not the tie on 95 of 129 questions.
- **ADR-085's sweep** added 94 lines to 87 entries before the owner narrowed the rule to 36 lines on 35 entries.

Every error was found by the record itself, through a later version note, a follow-up decision or a postmortem, and most were found within days.
