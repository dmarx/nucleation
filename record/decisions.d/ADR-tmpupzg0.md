---
status: Proposed
title: 'A RETRO scheme holds retrospectives, reviews of how a change or a stretch of work went, including what went right; POSTMORTEM is kept for something that went wrong; the devlog holds notes taken during the work for the next retrospective; and the existing postmortems become retrospectives'
version: 1
tags:
- record
- process
- taxonomy
date: '2026-11-21'
summary: >-
  The owner, 2026-11-21: "let's use it to document notes to revisit during
  the retrospective (we're currently calling this a POSTMORTEM, but that
  should be a rarer item and in response to something going wrong. we
  should probably keep the POSTMORTEM scheme, but add a RETROSPECTIVE
  scheme as well and convert our pre-existing postmortems to retros). A
  lot of stuff seems to be clicking right now, and we should document what
  seems to be going right." A new scheme RETRO; POSTMORTEM narrowed to
  incidents; [ADR-110](ADR-110.md)'s triggers divided between them; the devlog as the
  running notes; [POSTMORTEM-001](../postmortems.d/POSTMORTEM-001.md) to 003 converted. First application: the
  conversions, three devlog entries, a retrospective of the session of
  2026-11-20 and 21, and a postmortem of its docs-check failure.
---
<!-- inactive-ok-file: ADR-110 ADR-112 POSTMORTEM-001 RETRO-tmpb4hv3 RETRO-tmpcjeut RETRO-tmp89l09 RETRO-tmp50h9d POSTMORTEM-tmpynplw — Proposed, Draft or Superseded; the decisions this changes and the entries it converts or files -->

# ADR-tmpupzg0: A RETRO scheme holds retrospectives, reviews of how a change or a stretch of work went, including what went right; POSTMORTEM is kept for something that went wrong; the devlog holds notes taken during the work for the next retrospective; and the existing postmortems become retrospectives

## Context

[ADR-112](ADR-112.md) added POSTMORTEM as "a review of how a change to the record has worked
out once it has been used", and [ADR-110](ADR-110.md) set when one is due: a schema change
used, a batch closing, a bulk filing, a decision revised soon after landing, a
process incident, or the owner asking. All three postmortems filed so far
([POSTMORTEM-001](../postmortems.d/POSTMORTEM-001.md) to 003) review a change or a batch, not a failure.

The owner asked on 2026-11-21 to keep POSTMORTEM for something going wrong, to
add a scheme for the ordinary review of how work went, to convert the existing
postmortems, and to use the devlog for notes taken during the work to revisit at
that review, with emphasis on what is going right: "A lot of stuff seems to be
clicking right now, and we should document what seems to be going right."

The devlog has been configured since the record began and never used; it held
only its template.

## Decision

- **A new scheme, RETRO** (record/retrospectives.d): a review of how a change to
  the record, or a stretch of work, has gone: what it covered, what went well
  and why, so it can be kept on purpose, what did not, and what to change.
  Statuses as POSTMORTEM's (Draft, Accepted, Superseded; the vocabulary's blurb
  now names both). `reviews` (ADR) optional, since a stretch of work may follow
  no single decision; `prompted` (ADR) optional; `pull_requests` and
  `discussions` optional URL lists; tags from the open decision tags. Sections:
  what it covers, what went well and why, what did not, recommendations. The
  code is RETRO; the longer RETROSPECTIVE was considered and set aside for
  length in prose.
- **POSTMORTEM narrowed** to a review in response to something that went wrong:
  a check red and staying red, a revert, an entry retracted because it was filed
  wrong, a standing rule broken or nearly broken, a decision revised soon after
  landing. Its fields are unchanged. Its `superseded_by` may name a RETRO, so a
  postmortem that turns out to be a review of how things went can be converted.
- **[ADR-110](ADR-110.md)'s triggers are divided.** A schema change used, a batch closing, a
  bulk filing and the owner asking call for a RETRO. A decision revised soon
  after landing and a process incident call for a POSTMORTEM. The owner can ask
  for either. The assistant still checks the triggers when a batch closes, and
  says which are met.
- **The devlog holds notes for the next retrospective.** During the work, the
  assistant or the owner files a devlog entry (`luria new devlog`) when
  something seems to be going right or wrong and worth revisiting, tagged
  `retro`: what it is, why it seems to work or not, and the wrong theories and
  how they were found out. Going right is recorded as deliberately as going
  wrong, so that what works is kept on purpose. A RETRO reads the entries filed
  since the previous RETRO and cites them by date. A devlog entry goes in the
  pull request of the work it is about; it needs no asking.
- **ADR's derived converses** `reviewed_by` and `prompted_by` take both schemes.
- **Conversion.** [POSTMORTEM-001](../postmortems.d/POSTMORTEM-001.md), 002 and 003 are copied into new RETRO entries,
  their text unchanged apart from the heading, and retired by status
  (Superseded, `superseded_by` the RETRO), never deleted. The decisions that
  cite them keep their text; their history notes point here.

## Alternatives considered

- **Keep one scheme and add a kind field.** One scheme, two meanings, and the
  index would mix incidents with routine reviews. The owner asked for two
  schemes.
- **Rename POSTMORTEM to RETRO and make a new POSTMORTEM.** Renaming codes the
  record already cites breaks the citations; retiring by status keeps them.
- **Move the postmortems' files.** The same objection: a code is permanent.
- **Running notes in the workbench or the curation log.** The workbench holds
  the record's own argument as worked; curation holds why things entered. The
  devlog's own template already asks for "what was found along the way" and
  "the wrong theories and why they were wrong", which is what a retrospective
  needs.

## Consequences

- [ADR-110](ADR-110.md) and [ADR-112](ADR-112.md) take history notes pointing here; their bodies are
  unchanged.
- CLAUDE.md's map names retrospectives and the devlog's use.
- First application, in this pull request: [POSTMORTEM-001](../postmortems.d/POSTMORTEM-001.md) to 003 converted to
  [RETRO-tmpb4hv3](../retrospectives.d/RETRO-tmpb4hv3.md), [RETRO-tmpcjeut](../retrospectives.d/RETRO-tmpcjeut.md) and [RETRO-tmp89l09](../retrospectives.d/RETRO-tmp89l09.md); three devlog entries of
  2026-11-21; [RETRO-tmp50h9d](../retrospectives.d/RETRO-tmp50h9d.md), a retrospective of the session of 2026-11-20 and
  21, which reads them; and [POSTMORTEM-tmpynplw](../postmortems.d/POSTMORTEM-tmpynplw.md), on that session's docs-check
  failure, the first postmortem under the narrowed scheme.
