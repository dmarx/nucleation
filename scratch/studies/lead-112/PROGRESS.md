# LEAD-112: progress

- Lead: LEAD-112
- Branch: claude/lead-112-dissociation-search
- Skill: .claude/skills/run-lead/SKILL.md (readings by read-and-file steps 5-9)

## Task as understood

Search the literature, for each kind of evidence the lead names (report,
no-report, deficit, architectural), for a case where access and experience
come apart, with QUESTION-048's three named targets in view (superblindsight,
inconspicuous rivalry recorded intracranially, a marker both sides accept in
advance) and QUESTION-061's (one content available to one consumer and
demonstrably absent from another at the same time). Register at most about 10
works (Deferred LITs), read at most 3 of the most decisive, and add dated notes
on QUESTION-048, QUESTION-061, CLAIM-039, CLAIM-003 and LEAD-112. Every query
is logged in search.md. Services: Europe PMC REST, arXiv, OpenAlex, no email.

## Done

- Read the lead, QUESTION-048, QUESTION-061, CLAIM-039, CLAIM-003, THEORY-091, THEORY-094.
- Searched Europe PMC (E1-E12) and arXiv (A1-A2); OpenAlex refused with 429 on the
  first call and was not used again. Log: search.md.
- Registered ten works as Deferred LITs (identifiers checked on Crossref, dates
  and copies on Europe PMC; summaries follow the abstracts):
  - LIT-tmpblnvk Pinto et al. 2017 (split brain) - deficit / architectural
  - LIT-tmpnsyqi Kapoor et al. 2022 (macaque PFC, no-report rivalry) - no-report, intracranial
  - LIT-tmp6iss9 Dwarakanath et al. 2023 (PFC bistability) - no-report, intracranial
  - LIT-tmp5rny4 Brascamp, Blake & Knapen 2015 (inconspicuous rivalry, fMRI) - no-report
  - LIT-tmpk79hb Canales-Johnson et al. 2023 (EEG, no-report bistable) - no-report
  - LIT-tmpz7h9h Phillips 2021 (blindsight is degraded conscious vision) - deficit
  - LIT-tmpp90k6 Persaud et al. 2011 (GY, matched performance) - deficit / report
  - LIT-tmp1goav Lau & Passingham 2006 (relative blindsight) - report
  - LIT-tmpw89hi Bayne et al. 2024 (tests for consciousness) - marker
  - LIT-tmpl6qwr Overgaard et al. 2008 (GR, degraded conscious vision) - deficit

- Read Brascamp 2015 (Europe PMC fullTextXML of PMC4603386, 2026-11-22):
  abstract, Introduction, Results, Discussion, Online Methods to Task;
  Supplementary not read. Same-colour rivalry switches detected at chance (d'),
  about 8 times fewer hits; fronto-parietal switch BOLD proportional to
  reportability; the measure is switch-related BOLD, not percept-specific
  content; n=6 in fMRI, two observers authors. NOTE/THEORY not yet written.
- Kapoor 2022: Europe PMC fullTextXML for PMC8940963 returned HTTP 500 twice
  (2026-11-22, server error, not a bot check). Read instead from the publisher's
  open-access article page https://www.nature.com/articles/s41467-022-28897-2
  (CC BY): abstract, Introduction, Results, Discussion; Methods headings only.
  Two macaques, 987 units, vlPFC Utah arrays, OKN-inferred BFS and BR; content
  decoded up to 95% and generalising PA<->BR. Switches were "unreported but
  clearly occurring": not inconspicuous. NOTE/THEORY not yet written.
- Filed Brascamp: NOTE-tmprcujk, THEORY-tmpvkp5f, LIT-tmp5rny4 -> Active.
- Filed Kapoor: NOTE-tmplluya, THEORY-tmpbu9we, LIT-tmpnsyqi -> Active.
- Pinto 2017: the OUP PDF https://academic.oup.com/brain/article-pdf/140/5/1231/18223376/aww358.pdf
  returned 403 with a Cloudflare "Just a moment..." challenge, 2026-11-22.
  Stopped; LIT-tmpblnvk to go Unfetched. Neighbour read instead: de Haan et al.
  2020, Neuropsychology Review 30: 224-233 (Pinto a co-author), PMC7305066 via
  Europe PMC fullTextXML, read in full. Registered as LIT-tmpsc6mi (stand-in,
  ADR-114). Scaffolded NOTE-tmpbwyy5, THEORY-tmpb3deq, ARG-tmpymket (to
  CLAIM-003).
- Checks: scratchpad check.py (YAML, title, H1, excuses) and quotes.py (every
  quotation against the downloaded text).
- Filed de Haan (stand-in): LIT-tmpsc6mi, NOTE-tmpbwyy5, THEORY-tmpb3deq
  (corroborates CLAIM-003), ARG-tmpymket; LIT-tmpblnvk -> Unfetched.
- Dated notes of 2026-11-22 on QUESTION-048, QUESTION-061, CLAIM-003,
  CLAIM-039, THEORY-091, THEORY-094, LEAD-112. Changelog fragment
  record/changelog.d/lead-112.md. Narrow luria.ref_status scan of the changed
  files: dangling 0, unused 0, lost 0.

## Choices made

- Read three: Brascamp 2015 (the inconspicuous design THEORY-094's promote_when
  asks to be read first-hand), Kapoor 2022 (the intracranial no-report recording,
  open in PMC), Pinto 2017 (the deficit case nearest QUESTION-061 and CLAIM-003;
  publisher's free PDF). Phillips 2021 left Deferred: it is an argument about
  blindsight, not a case, and the lead asks for cases first.
- Read myself (no subagent tool in this worker), so no reader branches.

## Next

- All steps in scope are done; the report goes to the lead.
- For a later worker: read Phillips 2021 (PsyArXiv gdk6m) first, then the other
  Deferred registrations; Pinto 2017 needs the owner's copy; Frässle 2014 unread;
  a wider search (OpenAlex, citation chasing from Brascamp 2015).
