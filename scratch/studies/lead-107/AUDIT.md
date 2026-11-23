# LEAD-107 rule audit (one coder checking its own rules; not a second coder)

The lead worker read random samples of the mechanically coded events
(`events_v2.jsonl`, rules v2) and judged each by reading the sentence in its
reconstruction. This measures how well the rules do what the codebook says,
as judged by the same coder who wrote them. It is not inter-rater agreement.

## Sample of 30 events coded `new` (seed 2026)

- Clearly a report that an item was restated in the exchange as though new
  or without its code: 23.
- Borderline, 2: the filing itself restated a claim without citing it (not
  the exchange; sentence 256 of 2026/11/07/015132), and "The exchange cited
  none of this" (held work not cited where it bore, no restatement stated).
- Wrong, 5: "as new evidence" inside a quotation (2026/10/25/043048, 107);
  "not to rediscover" inside a quotation (2026/10/21/025604, 130); entries
  not cited because they were not yet on the branch the replies read
  (2026/10/27/171939, 22); the replies *found* the held literature
  (2026/10/27/091400, 6); a manuscript's references left uncited
  (2026/10/09/023739, 26).
- Precision: 23/30 strict (0.77), 25/30 counting the borderline (0.83).

## Sample of 30 events coded `neutral` (seed 2027)

- A held or coded item restated, missed or proposed again without citation,
  which a reader would code `new`: about 9 (for example "Missed: CLAIM-278
  and TERM-067, again"; "Already held: CLAIM-444 ... and CLAIM-451";
  "the matched test proposed a fourth and fifth time").
- A restatement retrieved by citation or back-reference: 0.
- The rest: recurrences inside an exchange with no outcome stated, the
  filer's own restatements, or no restatement at all ("U1–U7 ... are not
  repeated here").

## Every event coded `retrieved` or `conflict` (rules v2)

- retrieved, 1: "Branching succession is already held, though A cites
  CLAIM-287 where QUESTION-290 and CLAIM-328 hold it" (2026/11/07/015132):
  a code cited, but the wrong one.
- conflict, 2: "CLAIM-122 (re-derived again, this time cited)"
  (2026/10/21/025602), the one clean report of a coded item restated *with*
  its code; and "its proposed question is QUESTION-257's first half,
  uncited; ... CLAIM-328 with CLAIM-002, of which it cited only the second"
  (2026/10/27/010126).
- Under rules v1, four more sentences were `retrieved`; all four were false
  positives ("of the 133 codes cited"; "no work was cited"; two
  "recurring strength" sentences about the replies' quality). Rules v2 were
  written to remove them (CODEBOOK.md, "Deviation").

## What the audit changes

The misclassifications go both ways between `new` and `neutral`, but none
of the 60 sampled events, and none of the events coded `retrieved` or
`conflict`, is a restatement successfully retrieved by its code, apart from
CLAIM-122's. The asymmetry the study reports (restatements recorded almost
only when they fail) does not depend on the rule errors found here.
