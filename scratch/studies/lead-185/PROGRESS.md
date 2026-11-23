<!-- scratch/studies/lead-185/PROGRESS.md: the running state of LEAD-185's run -->
# LEAD-185: progress

- Lead: LEAD-185, "Study contested and accepted open-source successions, timing the community's verdicts against the move".
- Branch: `claude/lead-185-oss-successions`, cut from origin/staging on 2026-11-23.
- Task as understood: run CASE-223's design on public records. Code open-source forks and successions for the community's verdict on which successor continues the project and its timing against the move; rules first; each date with its source URL; CSV data, a timing script and pytest tests; file an executed-study CASE, empirical CLAIMs, dated notes, a changelog fragment.
- Step 1 (already held?): checked 2026-11-23. No changelog fragment, case or dated note reports the study run. Not held.

## Done

- Step 1 check.
- Scoping pass, then CODING.md (frame = CASE-223's list plus the brief's; GIMP/SourceForge and data.table excluded with reasons).
- cases.csv (11 cases), events.csv (51 events, all read 2026-11-23), timings.py, test_timings.py (14 passing), results.json, summary.md, README.md.
- Six LITs with NOTEs (the documents carrying the coded verdicts and reasons).
- CASE-tmpntt8e (executed study, Proposed, documented); CLAIM-tmpc47v8 and its alternative CLAIM-tmppui4z; CLAIM-tmpqpfvh; CLAIM-tmp79lxm.
- Dated notes on LEAD-185, ARG-067, CLAIM-617, CASE-223, CLAIM-329, CLAIM-328, QUESTION-118; changelog fragment.

## Choices made

- The sampling frame is the record's own list plus the brief's, not chosen by documentability.
- Verdicts are coded by the speaker's independence from the founders and by whether the statement is itself the speaker's move; reasons are the stated reasons.
- Six sources registered as LITs: those whose content (a verdict, a reason, a vote, a concession) the claims rely on. The other event sources are dates, kept with their addresses in events.csv.
- No THEORY filed from the LITs: they are primary documents coded as data, not accounts.
- Two readings of the main result filed as alternatives (CLAIM-tmpc47v8, leaned to; CLAIM-tmppui4z).

## Obstacles (not retried)

- Bot checks (Anubis): lists.fedoraproject.org pipermail (the MariaDB proposal thread), fedorapeople.org (F41 schedule).
- 403: www.jenkins.io/blog/2011/ (index), phys.org, eweek.com, en.opensuse.org, itsfoss.com.
- 404: documentfoundation.org's announcement copy (no Wayback capture), Oracle's 2010 press release, Eclipse forum Hudson 3.3.3 post, Gitea blog post on Gitea Ltd.

## Next (for the owner, or a later run)

- Rule ARG-067 (Rejected as far as the instances go, or kept Proposed for the survey arm).
- Choose between CLAIM-tmpc47v8 and CLAIM-tmppui4z.
- Survey arm; contributor counts; downstreams of Terraform, Gitea, Audacity.
