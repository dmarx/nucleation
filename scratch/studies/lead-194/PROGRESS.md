# LEAD-194 progress

- Lead: LEAD-194 (resolve the tension between CLAIM-266 and CLAIM-517, named in the curation entry of 2026-11-11, 061331).
- Branch: `claude/lead-194-curation-admission-tension`, cut from origin/staging.
- Task as understood: state precisely the tension between CLAIM-266 (training probes cannot certify what is preserved) and CLAIM-517 (a distillation loss with boundary coverage certifies viability); file an objection CLAIM or a proposed revision (dated note with a Reframing), each valid resolution as an alternative with a lean; dated notes on LEAD-194, CLAIM-266 and CLAIM-517; changelog fragment. No status, stage or held text changed.

## Done

- Step 1: not already held. Searched record/changelog.d, the dated notes of LEAD-194, CLAIM-266 and CLAIM-517, and every claim's objects_to / superseded_by for CLAIM-266 or CLAIM-517: nothing objects to or revises either, no note names the tension, and the only mentions are the curation entry 061331 and the backlog audits (224759; 132527 lists LEAD-194 as not held).

- Filed CLAIM-tmpktdh5 (Proposed, thesis, demonstrated; objects_to CLAIM-266, rests_on CLAIM-517).
- Dated notes of 2026-11-22 on CLAIM-266 (tension, alternatives A and B, proposed Reframing of its title), CLAIM-517 (proposed clarification of its epsilon) and LEAD-194.
- Changelog fragment record/changelog.d/lead-194.md.

## Next

- Nothing; report. The pull request is the lead's to open.

## Choices

- The tension is real but narrow: the two agree where boundary contexts are uncovered (CLAIM-517's second half is CLAIM-266's limit), and disagree only under coverage, where a stated inequality (Lipschitz + Pinsker + coverage) bounds the preserved property by the training probe's value.
- Vehicle: an objection CLAIM (the condition has content of its own, ADR-072) plus a proposed Reframing of CLAIM-266's title in its dated note; neither applied.
- Role thesis with objects_to (an objection is an edge, not a role); warrant demonstrated (it follows from the bound and CLAIM-517's steps).
- Alternatives: A, CLAIM-266 narrows (lean: its clause "must be shown under probes not used to train it" is contradicted outright, CLAIM-517 shows preservation under the training family on fresh draws); B, neither narrows (read "certify" as the probe value alone; the objection would be answered).
- CLAIM-517 gets a proposed clarification under either: its epsilon is the population KL, estimated on draws not fitted to, holding with a stated confidence.
- No bears_on: QUESTION-258 (CLAIM-266's question) is about manuscript selection, not this point.
- The lead's title ("curation as revision and on admission") describes neither claim; reported, not changed.
