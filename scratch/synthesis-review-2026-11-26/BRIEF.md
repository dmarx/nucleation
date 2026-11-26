# Brief: synthesis review of 2026-11-26, stage 3 (audit) and stage 4 drafts

You are one of five auditors in a synthesis review of the Nucleation record
(checkout: /home/user/nucleation, currently on branch
claude/trusting-albattani-hoxegv, which is staging plus a just-filed
exchange whose entries carry temporary codes like CLAIM-tmpe432a; read them
as ordinary entries).

## Read first, in full

1. /home/user/nucleation/CLAUDE.md
2. /home/user/nucleation/.claude/skills/synthesis-review/SKILL.md — you do
   stage 3 for your candidates, and DRAFT stage 4. The lead does stage 1
   and 2 (done), 4b, 5 and all filing.
3. record/decisions.d/ADR-075.md (step 5: the three routes), ADR-084,
   ADR-151, ADR-083; docs/record.md (SYNTHESIS and CLAIM fields).
4. Two held accounts for form: record/syntheses.d/SYNTHESIS-012.md and
   SYNTHESIS-017.md.

## The tests (state them as they are; no target outcome)

For each candidate: read it and every component in full. Run ADR-075's
checks (attribution, coverage, fidelity, standing, integration). State in
one sentence what the candidate adds to its components, or say that no such
sentence can be written. Test that sentence by the three routes (separating
case, derivation, discriminating prediction); check a realistic separating
case against the claim's own `defeated_if`; close any free parameter before
testing. For a scope with no account, or an account to revise, the account
comes first (stage 4's first bullet).

## Rules

- Do NOT write in /home/user/nucleation at all, and run no git command
  that changes anything. Read-only. Put every draft in your own directory
  /tmp/claude-0/-home-user-nucleation/db27049e-0300-5c62-8c3b-bd1ccdca0d74/scratchpad/sr/<your-id>/
  as complete files ready to drop into the record: a new SYNTHESIS or CLAIM
  as `NEW-SYNTHESIS-<slug>.md` / `NEW-CLAIM-<slug>.md` (front matter and
  body; leave `number`/code out, write `CODE` in the H1 as `# CODE: title`),
  a revision of a held entry as the whole revised file under its own name
  (e.g. `SYNTHESIS-052.md`) with version bump and a 2026-11-26 history
  note. Bare codes only, never link targets. Titles carry no codes.
- Accounts are Proposed; never Current. Statuses of held entries do not
  change, except an Arm A claim that adds nothing, which stage 4 sets
  Superseded by its account: draft that, and list each claim whose
  `rests_on` names it, with the repointing it needs.
- New claims (Arm B passes) end their summary with "The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call."
- Never send an email address to any outside service (you need none).

## Report (final reply, under ~150 lines)

One row per candidate: arm, the sentence it adds (or "none"), pass/fail and
route, and what you drafted (file names). Then: each scope's account drafted
or revised, with its components; every Arm A claim proposed Superseded and
the repointing; links put under "Not stated on the record"; for each
cross-line account you drafted, the lines its components come from (by
script: read each component's `line:`); anything you could not decide.
