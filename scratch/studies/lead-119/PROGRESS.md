# LEAD-119 progress

- Lead: LEAD-119 (code public postmortems by organizational level; internal against independent reviews), operationalizing CASE-293, testing CLAIM-750.
- Branch: claude/lead-119-postmortem-coding (cut from origin/staging).
- Task as understood: fix a codebook and sampling rule in advance and commit them; code a pilot of about 30 public internal postmortems (company engineering blogs, public lists) and about 10 independent investigation reports (NTSB, CSB and the like) for (1) highest organizational level named among contributing causes, (2) action items above the reviewing team's authority, (3) commissioning body; write each coded item to an append-only JSONL; file a CASE (executed-study, pilot), a CLAIM if warranted, dated notes on the entries advanced and on LEAD-119, a changelog fragment. Single coder of the same model family as the claim's author: not independent.

## Done

- Codebook and sampling rule committed before coding (codebook.md; one gloss corrected before coding).
- Internal arm sampled from Dan Luu's list, seed 119 (sample_log.jsonl): 30 included; exclusions logged (web.archive.org unreachable, one 403, short pages, four failing rule 2 or 3).
- Independent arm: the 10 most recent CSB completed investigations with final reports.
- All 40 coded into coded.jsonl; results.md by summarize.py (tests pass).

## Results

Internal H>=3 2/30 (7%), A>=3 4/30 (13%); independent H>=3 7/10, A>=3 9/10. The rule fixed in advance reads "prediction holds in the pilot". Confounds: domain (software outages against fatal chemical accidents), one coder, keyword-located reading.

- Filed: CASE-tmp1ya4r (executed-study pilot), CLAIM-tmpst09o (finding, corroborates CLAIM-750); dated notes of 2026-11-22 on LEAD-119, CLAIM-750, CASE-293, QUESTION-476, CLAIM-751, CLAIM-719; changelog fragment record/changelog.d/lead-119.md. Frontmatter, title and H1 checks pass.

## Next

- Report to the lead. The pull request is opened by the lead, not this worker.

## Choices

- Independent arm is CSB only (plain listing, one report format); NTSB left to the full study.
- Internal postmortems coded from keyword-located passages, CSB from the summary sections: a time choice, stated in the CASE.
- A = 3 re-prioritisation rule sharpened after P10 (README).
- Commissioning body's authority not coded separately beyond the author's role, where seen.
