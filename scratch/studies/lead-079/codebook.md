<!-- scratch/studies/lead-079/codebook.md: the study materials of CASE-tmpzi1u3, copied from the delegated coder's working directory on 2026-11-22 -->
# LEAD-079 codebook: identity failures against structure failures, move by move

Written 2026-11-22T07:16Z, before any coding of the exchange "Rich Get Richer
Power Laws" (ChatGPT, 2026-11-20 to 21). The coder had read only the turn
index and the owner's turns (to size the task) when this was written.
Single coder: Claude (Opus 5.5), an AI coding another AI's exchange.

## 1. What the record fixes (recovered)

Source: ADR-032 Context (the will exchange, chatgpt.com/share/6ac5887a...,
2026-10-04 to 06, 95 owner turns, ~300 replies, "read in full by seven
parallel readers, which coded every argumentative move"); CLAIM-177;
CLAIM-483 defeated_if; workbench entries of 2026-10-07 (011440-011446).

- Unit of coding: the argumentative move. No segmentation rule survives.
- Identity failures named (with the will exchange's counts):
  - concept redefined silently: "will" five or more times; "concordance" five
    times; the perspective and level schemes swapped turn to turn;
  - a worked case changed identity: one case six times (Northstar: one name
    for six scenarios); the reef's job changed four times;
  - an objection re-derived as though new: permissiveness six or more times
    (and returning after its withdrawal, A118, A147, "unlinked to its
    withdrawal"); ordinary-control three times with different criteria;
  - readings the record already held recommended: three times;
  - commitments dropped and never retired (CASE-014 at A205; the first
    draft's concession and falsifier dropped in the rewrite);
  - (CLAIM-177, from the translation exchange) thesis changed without a turn
    arguing the change.
- Structure failures named (CLAIM-483 defeated_if): no premises stated,
  inferences never laid out, objections never answered.
- The structure count reported: "7 of about 30 claims in the final
  manuscript had more than one independent line of support". This is a
  thinness measure on a final manuscript, not a count of structure defects
  during development. Also reported: half to two-thirds of objections were
  inference attacks, mostly on analogies; 40+ "X does not establish Y"
  sentences in the audit stretch, read as disclaimers, not attacks.

## 2. What the record does not fix

- No codebook text, no segmentation of moves, no counting rule (per
  occurrence or per item), no totals per category, no denominator (moves or
  turns), no inter-rater agreement. So no numeric identity:structure ratio
  exists for the will exchange; "the same ratio" (LEAD-079) can only be
  compared qualitatively: identity failures predominant, structure thin but
  not the named defect.
- The will exchange was a joint argument-building exchange (an essay with a
  thesis); whether the new exchange is "comparable" (CLAIM-483) is itself a
  judgement, recorded in the report.

## 3. Choices fixed in advance

C1. Code only visible turns. Reasoning summaries (`----- A<n> · reasoning`)
    and code blocks are not coded. Preamble stubs (A2, A4, A9 ...; <600
    chars) are not counted as replies.
C2. Denominators: owner turns (27), substantive assistant replies (count
    reported), and kilochars of visible assistant text.
C3. Unit: a move is a claim, definition, distinction, mechanism, case,
    objection/caveat, proposal or recommendation the turn puts forward.
    Background exposition stated as textbook fact is a move only if a later
    turn's argument uses it. Failures are coded per occurrence (each turn in
    which it happens) with an item id, so recurrences group into items; both
    occurrence counts and item counts are reported.
C4. Identity codes (within the exchange; the earlier occurrence must be in
    an earlier turn of this exchange):
  - ID-REDEF: a term the exchange has already defined or used in a fixed
    sense is used in a materially different sense, or given a new definition,
    with no notice of the change.
  - ID-REDERIV: a point, mechanism, distinction, objection or caveat already
    made is presented again as though new (framed as a new point, "another",
    a fresh heading or numbered item, no back-reference). A restatement that
    points back ("as above", "earlier", "recall") is not a failure. A
    recapitulation explicitly labelled as a summary is not a failure.
  - ID-CASE: a named case, model or example changes what it stands for or
    what it is used to show, unannounced.
  - ID-THESIS: the governing thesis or organizing frame changes without a
    turn arguing the change.
  - ID-DROP: a commitment the exchange made (a claim, a criterion, a
    caveat) is later contradicted or silently abandoned without retraction.
  - ID-HELD (record-relative): a reading or idea the record already holds
    is recommended or introduced as new. Coded only after the blind pass,
    from the prior filing ledgers of this exchange, and reported separately
    as non-blind.
C5. Structure codes (applied only to moves the turn marks as its own
    substantive conclusions: headline/bolded theses, "the key point",
    proposals, conjectures it endorses; not textbook background):
  - ST-PREM: a conclusion asserted with a premise it needs left unstated,
    where a competent reader would contest the conclusion without it.
  - ST-INF: premises and conclusion stated but the step not laid out: an
    analogy or shared form taken as shared mechanism, or "so/therefore/this
    suggests" across a non-obvious gap.
  - ST-OBJ: an objection, caveat or challenge raised (by either party) and
    never answered in the exchange; or an owner's question/challenge that the
    reply does not address.
  - Not defects: "X does not establish Y" disclaimers (per ADR-032);
    hedged conjectures explicitly flagged as speculative AND given a stated
    test (they lay out their status).
C6. Ambiguity: a failure that fits both an identity and a structure code is
    coded under the one that names what went wrong first (as the defeater
    contrasts them), and flagged "dual".
C7. Defeater test (CLAIM-483) applied as: met for this exchange if
    structure occurrences > identity occurrences AND ID-REDEF + ID-REDERIV
    are "rare" (fixed in advance: fewer than 1 per 5 substantive replies).
    CLAIM-177 recurrence: whether ID-REDEF, ID-REDERIV (objection or reading
    returning as new) and ID-THESIS each occur at least once.
C8. Verbatim quotes are short (<= 25 words) and copied exactly.
