<!-- scratch/synthesis-review-2026-11-26/README.md: the synthesis review of 2026-11-26, stages 1 to 3, and stage 4's drafts -->
# Synthesis review of 2026-11-26: audits done, filing waits on #837

Requested by the owner on 2026-11-26 ("kick off a synthesis review"),
after the filing of the exchange "Alignment consequences brainstorm"
(dmarx/nucleation#837). Run under `.claude/skills/synthesis-review/SKILL.md`.

- **Stage 1:** `stage1.txt`, the output of
  `python3 -I scratch/formal/synthesis_candidates.py --top 12`, run on the
  tree of #837. That is staging plus the filing, so the exchange's
  temporary codes appear in it.
- **Stage 2:** the shortlist below. It adds by hand the two lines with no
  account (organization-of-perspective, self-correction) and what #837's
  curation entry left without an account.
- **Stage 3:** five auditors, briefed by `BRIEF.md`. Their drafts are in
  `drafts/w1` to `drafts/w5`, as files ready to drop into `record/`.
- **Stage 4:** waits until #837 merges into staging. The drafts cite its
  temporary codes and revise accounts that #837 also revises. When #837
  merges, this branch is brought up to date with staging. The drafts then
  go into `record/` with real codes in place of the placeholders
  (`SYNTHESIS-NEWOPT`, `SYNTHESIS-CODE-delegation`,
  `SYNTHESIS-CODE-capture`, `CLAIM-CODE`). After that come the
  cross-line audit (4b), the curation entry and the changelog fragment.

## Verdicts

| candidate | arm | verdict | draft |
|---|---|---|---|
| line organization-of-perspective | coverage | first account, 15 components, one argument | w1/NEW-SYNTHESIS-organization-of-perspective |
| CLAIM-545 | A | adds (separating case); stays | — |
| CLAIM-610 | A | fails either way the free parameter closes: false as worded, or nothing added | w1/CLAIM-610 (A: note to the owner), w1/CLAIM-610.ALT-B (B: Superseded by SYNTHESIS-048) |
| CLAIM-615 | A | adds; stays | — |
| line self-correction | coverage | SYNTHESIS-111 revised into its account (v4, 26 components); fidelity fix on CLAIM-1185; a split signal (two closed halves) recommended against | w2/SYNTHESIS-111 |
| CLAIM-620 | A | adds (separating case: the independent zeros); Admission extended | w2/CLAIM-620 |
| CLAIM-1228 | A | adds nothing (fixed order contradicts its premises; a runnable cycle is each premise's) | w2/CLAIM-1228 (Superseded by SYNTHESIS-118), w2/SYNTHESIS-118 |
| CLAIM-532, CLAIM-624 | A | add; stay | — |
| optimization jurisdiction and pathologies of success | coverage | new cross-line account, 32 components (the owner's U4 first); a bridge, not a line | w3/NEW-SYNTHESIS-optimization-jurisdiction |
| CLAIM-1331 | A | adds nothing (each premise states its own sign); reverses ADR-147's admission | w3/CLAIM-1331 (Superseded by the new account) |
| CLAIM-tmpygs06 | A | adds, but a realistic case partly defeats it as worded; narrower reading survives | w3/CLAIM-tmpygs06 (Admission) |
| QUESTION-481's bearings | B2 | LEAD-033's results, unintegrated; go in SYNTHESIS-102 | w3/SYNTHESIS-102 |
| CLAIM-754 and the learned-structure cluster | A, B1 | 754 adds (prediction), realistic separating case added; cluster's links already stated | w5/CLAIM-754, w5/SYNTHESIS-105 |
| QUESTION-380 | B2 | already stated (CLAIM-1090) | w5/SYNTHESIS-045 |
| CLAIM-tmpti7cf, CLAIM-tmpik3z0 | placement | SYNTHESIS-076, which holds all their premises | w5/SYNTHESIS-076 |
| CLAIM-611 | A | adds (separating case); its last clause false as worded unless CLAIM-983 or CLAIM-986 closes it | w4/CLAIM-611, w4/SYNTHESIS-046 |
| QUESTION-118 | B2 | two links tested, both fail | w4/SYNTHESIS-047 |
| A's purpose and composition claims | placement | SYNTHESIS-052 | w4/SYNTHESIS-052 |
| CLAIM-1147, CLAIM-1021 | B3 | belong in SYNTHESIS-050's conferral part; one Arm B link passes by derivation (capacity capture without a return channel; checked 395/395 at θ=0) | w4/NEW-CLAIM-capacity-capture-without-return, two new part accounts, w4/SYNTHESIS-050; check script `tools/check_capacity_return_cut.py` |

## For the owner

- Status changes the skill's stage 4 would make on held entries: CLAIM-1228 and
  CLAIM-1331 Superseded, and CLAIM-610 (alternative B). They wait for the
  owner, and until then are filed as proposals in dated notes.
- Narrowings, each the owner's call:
  - CLAIM-tmpygs06's statement;
  - CLAIM-754's `defeated_if`;
  - CLAIM-611's last clause, which ARG-216's open choice between CLAIM-983 and CLAIM-986 settles.
- The self-correction line's split signal: a decision about the `lines`
  vocabulary.
- Coverage gaps the audits found and left for a later pass:
  - QUESTION-493 and QUESTION-494's answers of 2026-11-23;
  - six formal-apparatus claims in no account;
  - about 40 in-force entries in SYNTHESIS-050's scope;
  - the perspectives-from-activity entries named in SYNTHESIS-047;
  - CLAIM-1155.
