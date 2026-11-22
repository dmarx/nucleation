---
name: run-lead
description: How a delegated worker carries out one LEAD of the record, from cutting its branch to its report, persisting its progress as it goes. Use it to brief a lead worker, or when carrying out a lead yourself. ADR-tmpvqx5l (or its alternative ADR-tmpyb409) holds the rule that work persists as it goes; this file holds the steps.
---
<!-- .claude/skills/run-lead/SKILL.md -->

# Running a lead

You carry out ONE lead (LEAD-NNN) of this record. The message that starts
you names the lead and your branch. You work in an isolated git worktree
of the repository.

This file was the lead-worker brief of 2026-11-22, which lived in the
session's scratchpad. It moved here under ADR-tmpvqx5l / ADR-tmpyb409,
with its persistence steps (4 and 5) added. When a step here turns out
wrong or missing, edit it in the same pull request as the work that showed
it.

## 1. Before anything

- Read CLAUDE.md, the opening of docs/design-principles.md, and the lead
  file in full. Then read every entry the lead's `advances` names, and the
  cases, claims and questions it cites. Read docs/record.md for the
  required fields of any kind you file.
- Before filing what the lead asks for, check that the record does not
  already hold it: grep the claims and questions the lead cites, and the
  entry that named it, for a later filing. A lead can outlive its target
  (LEAD-059's corollary was already CLAIM-629). If it is held, file no
  second code (ADR-072); add the dated note on the lead and report.
- First command: `git fetch origin staging && git checkout -b <your-branch> origin/staging`.

## 2. Push the branch at once

Before the first substantive step, create
`scratch/studies/<lead-code-lowercase>/PROGRESS.md` holding the lead's
code, your branch, the task as you understand it, and an empty "Done"
and "Next" list. Commit it and run `git push -u origin <your-branch>`.
From here on, a stop at any moment must lose at most the step in hand.

## 3. Doing the work

- Do what the lead asks, or the self-contained part your message names,
  and nothing beyond it.
  - Where the lead leaves a choice open, make it explicitly and say why.
  - Where a choice is genuinely the owner's (adoption, status, policy,
    choosing between readings the record leaves open), file the
    alternatives instead of choosing.
- **Computation.**
  - Use Python with `python3 -I`, numpy/scipy, CPU only. Keep runs to
    minutes, an hour at most.
  - Write a pytest test for any nontrivial function, and run it.
  - Commit scripts and small result files under
    `scratch/studies/<lead-code-lowercase>/`, with a README saying how to
    rerun.
  - Never commit downloaded texts, or data larger than about 1 MB.
- **Reading.**
  - Read lawful copies only: arXiv; the Europe PMC REST API; PMC; author,
    lab and course pages; and the copies ADR-074, ADR-101 and ADR-113
    admit.
  - Stop at any bot check, captcha, Cloudflare or WAF challenge, 403 or
    429, paywall or refusal. Do not retry it or work around it. Record
    the address, the obstacle and the date.
  - Put downloads in the session's scratchpad, never in the repository.
    Run Python on them with `python3 -I`, and keep scripts outside the
    download directory.
  - A reading follows the read-and-file skill, steps 5–9.
- **Never send an email address to any outside service** (ADR-008): not
  in a query parameter (Unpaywall's `email=`, Crossref's `mailto=`), a
  header or a body. Leave it out; where an address is required, use
  noreply@anthropic.com; otherwise do without the service.

## 4. Persist every step

- **Commit and push after every step:** each record file you create or
  edit, each computation that finishes, each copy located or section
  read. A step not yet complete gets a commit message beginning "work in
  progress:". A rejected push is followed by a pull and a second push,
  never a force-push.
- **Update PROGRESS.md in the same push.** It records what is done, what
  is next, and the choices made so far, so that a replacement could
  continue from your branch without your transcript.

## 5. Computations persist per item

- A computation that runs longer than a few minutes writes each item's
  result as it is produced, to an append-only file (for example JSON
  lines) inside the study directory. It resumes by skipping the items
  already written. Never hold results in memory to write at the end.
- While it runs, commit and push its results file at least every ten
  minutes. A small loop that copies, commits and pushes, then sleeps 600
  seconds until the process exits, does this from a second worktree.
- Several workers share one machine. Stop a process only by the PID you
  started (save it, for example `echo $! > run.pid`), never with `pkill` or
  `killall` by name or pattern, which kills other workers' runs. `$!` can
  name a wrapper (the shell or `timeout`) rather than the process itself:
  before relying on the saved PID, check it with `ps -o pid,ppid,cmd` and
  the process's working directory (`readlink /proc/PID/cwd`), and after a
  stop check that no child of it is still running. Keep your
  files in a subdirectory of the scratchpad named after your lead, not in
  its root.
- The machine is shared, so never delete or overwrite anything outside
  your own lead's scratchpad subdirectory and your worktree: no writing to
  shared device nodes (`mv`/`cp`/`>` to `/dev/null`, `/dev/zero` and the
  like, which replaces the node for every worker), and no deleting under
  `/tmp` or another worker's `scratch/studies/` directory. To discard
  output, redirect to `/dev/null`, do not move a file onto it.
- Estimate the run's time before starting. Give a background run a time
  limit above twice the estimate. If its measured pace says it will not
  finish in time, stop it and restructure it at once.
- Measure the pace under the real load: a shared machine can run several
  times slower than a smoke test, so set BLAS threads to 1 and cut seeds
  early rather than late.

## 6. Filing

- **Creating entries.** Use only `luria new <kind> --title "..."`, then
  replace the template entirely. Results go in as follows:
  - a study run: a CASE (kind executed-study, standing documented);
  - a finding or an argument: a CLAIM (Proposed, a role, a warrant of
    demonstrated, empirical or interpretive, and `defeated_if` for a
    thesis);
  - a distinction: a TERM;
  - a load-bearing support judgement: an ARG, whose title names the route
    first (ADR-136).
- **Your own wording** ends the summary with: "The wording is the
  assistant's (Claude, in this session); adopting it is the owner's
  call."
- **Held entries** (filed before the current batch) get only dated notes
  ("## Note of YYYY-MM-DD: ...") and relation fields.
  - Never change a status, a title or a held entry's text, with one
    exception: a LIT you have read moves as read-and-file step 8 says, to
    Active with a new history version, status note and summary, or stays
    Unfetched or Unavailable with the obstacle recorded. Filing the reading
    is that step, not a status change for the owner.
  - Add a dated note on the lead itself saying what was done and what
    remains.
  - Do NOT change the lead's status or stage; the owner marks it Done.
- **Titles.** No codes in titles. A single-quoted YAML title doubles
  every apostrophe (`''`). The H1 is `# <CODE>: <title>`, with the title
  exactly as written but with single apostrophes. Use bare codes in
  prose, and never hand-write link targets.
- **Vocabularies.** Tags and lines come only from luria.yaml's
  vocabularies.
- **Relations take the kinds docs/record.md names.** Check each field
  you write there. Most often missed: `bears_on` on a CLAIM or a CASE
  takes QUESTION codes only. A claim relates to other claims by
  `rests_on`, `complements`, `corroborates` or `objects_to`; a case
  relates to a claim by `illustrates` or `counterexample_to`. A
  relation to an entry your result only touches stays in the prose and
  in that entry's dated note.
- **Excuses for codes not in force.** For every code cited in prose whose
  entry is not in force (Proposed, Deferred, Unfetched, Unavailable,
  Rejected, or new), add `<!-- inactive-ok-file: CODES — reason -->`
  after the frontmatter.
  - Open questions and leads, and Active entries, need none.
  - A non-active entry that a claim depends on through `grounds`, and
    that is Unavailable or Unfetched, needs its own line:
    `<!-- inactive-ok-file: CODE until <date a few months on> — reason -->`.
  - An unused excuse fails lint.
- **Changelog.** Add a fragment
  `record/changelog.d/<lead-code-lowercase>.md` with "### Added" and
  "### Changed" bullets.
- **Checks before each commit.** With python3, check every changed record
  file:
  - its frontmatter parses with yaml.safe_load;
  - its title has no code;
  - its H1 matches its title.

  Do NOT run luria lint, repair, index or link.
- **Commits.** End each commit message with the attribution lines the
  session gives. Do not open a pull request; the lead opens it once you
  report.
- **Usage limits.** If you hit an API usage limit, everything up to the
  last step is already pushed. Stop and report.

## 7. Report (under about 80 lines)

- What was done.
- The result in plain words, and what it changes in the record's
  argument.
- Every file created or edited: code, kind, and a few words.
- Quotes or identifiers you could not verify.
- What remains of the lead, and what blocks it.
- Anything that is the owner's decision.
