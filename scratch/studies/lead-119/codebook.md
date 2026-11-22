# LEAD-119 pilot: codebook and sampling rule

Fixed 2026-11-22 before any document was coded. Written and applied by one
coder: the assistant (Claude, Opus 5.5), the same model family that wrote
CLAIM-750, CASE-293 and this codebook. The pilot is therefore not
independent, and the coder knew the predicted result.

## Units

One document per item: one published postmortem (internal arm) or one final
investigation report (independent arm). Within a document the coder reads the
contributing causes (root cause, contributing factors, "what went wrong",
findings, causal analysis) and the action items (remediation, follow-ups,
"what we are doing", recommendations).

## Sampling rule

**Internal arm (target 30).** Source: Dan Luu's public list
`https://raw.githubusercontent.com/danluu/post-mortems/master/README.md`,
fetched 2026-11-22. Candidates: every link that heads an entry in the
sections "Config Errors" through "Uncategorized" (not "Other lists",
"Analysis"). Deduplicate by URL. Shuffle with Python
`random.Random(119).shuffle` on the list in file order. Walk the shuffled
list and include an item when all hold:

1. the URL (or, if the link is to web.archive.org, the archived copy) returns
   HTTP 200 to a plain `curl` GET with no bot check, captcha, Cloudflare or WAF
   challenge, login or paywall (any of these: exclude, record, never retry);
2. it is the organization's own account of its own incident (its blog, status
   page, official forum, mailing list or repository), not news, a third-party
   analysis or a regulator's report;
3. it yields at least 300 words of text after HTML stripping, and is in
   English.

Stop at 30 inclusions. Every exclusion is logged with its reason in
`sample_log.jsonl`. Commissioning body for this arm is coded "internal".

**Independent arm (target 10).** Source: the U.S. Chemical Safety Board's
"Completed Investigations" listing
(`https://www.csb.gov/investigations/completed-investigations/`, pages in
order), fetched 2026-11-22. Walk the listing in its order (most recent
first) and include each investigation whose page links a final investigation
report PDF that fetches under rule 1 above. Stop at 10. The CSB is chosen
for the pilot because its listing is plain HTML, its reports share one
format (executive summary, key findings, causal analysis, conclusions,
recommendations), and, like the NTSB, it sits outside the organizations it investigates and
its findings may not be used as evidence in suits for damages
(42 U.S.C. 7412(r)(6)(G); corrected before coding from "may not assign
fault", which the coder had misremembered). The NTSB arm is left to the full study.
For CSB reports the coder reads the executive summary, findings, conclusions,
cause statement and recommendations, not the technical body.

## Codes, per document

**H: highest organizational level whose decision or practice a contributing
cause names.** Ordinal:

- `0` unattributed only: every cause is "the system", "the process", "a bug",
  "a gap", a component failure, with no party's decision or practice named;
- `1` operator: an individual's action (an engineer ran a command, made a
  typo, an operator opened a valve);
- `2` team / engineering practice: a design, testing, tooling, deployment,
  monitoring or procedure decision or practice of the engineering group that
  owns the system ("we did not test X", "our deploy process lacked a
  canary", "the procedure did not require"). A company-voice "we" describing
  a technical or process decision is coded here;
- `3` management: a decision about priorities, schedules, deadlines,
  staffing, resourcing, or a cross-team policy, named as such or named as
  made above the working team (e.g. "we prioritised feature work over
  this migration", "the team was understaffed", "management approved
  deferring maintenance", a deferred project named as a resourcing choice);
- `4` organizational leadership: company-wide budget, strategy, safety
  culture, governance, corporate oversight of sites, or the safety management
  system as the organization's own choice ("corporate did not provide
  oversight", "the company's safety culture", "the organization lacked a
  management-of-change program");
- `5` outside authority: a regulator's, standard body's or oversight body's
  decision or gap (OSHA, EPA, a state, an industry code like API) named as a
  contributing cause.

A cause names a level only when the text says whose decision or practice it
was, or the decision is of a kind only that level makes (budget, staffing,
deadline, corporate policy). Vendor faults are flagged (`vendor`) and not
leveled.

**SYS: system language.** `1` if at least one cause is stated as "the
system", process, gap or component with no decision named; else `0`.

**A: highest level an action item targets.** Same scale, applied to who must
decide to carry it out: `1` individual (retraining one person); `2` team
technical or process change; `3` management change (re-prioritisation, a
freeze on feature work, hiring, staffing, reorganising ownership or on-call
across teams, a change of deadline policy); `4` organization-wide
governance, culture, budget or safety management system change, or a
recommendation addressed to the company's board or corporate leadership; `5`
a recommendation to a regulator, standard body or industry. `0` no action
items stated.

**ABOVE: any action item above the reviewing team.** `1` if A >= 3.

**COMM: commissioning body.** `internal` (the organization reviewing
itself) or `independent` (a body outside it; here the CSB). Also recorded
where stated: the author's role.

**Evidence.** For H and A, a verbatim quote of at most 30 words, or "none".

## Measures fixed in advance

- Rate of H >= 3 and of A >= 3 per arm; rate of H >= 4; rate of SYS = 1.
- Reading for CLAIM-750: its prediction holds in the pilot if internal
  H >= 3 is under 25% and A >= 3 under 25%, and the independent rates exceed
  the internal ones by at least 30 points. Its defeater's direction is met
  if the internal rates are within 15 points of the independent ones or
  above 50%. Anything else is "inconclusive". With n = 30 and 10 this is a
  pilot reading, not a test.
- Asymmetry noted in advance: the independent arm's recommendations to
  regulators score 5 by construction, and CSB reports are of serious
  physical accidents, the internal arm's of software outages. The pilot
  compares arms that differ in domain as well as commissioning body.
