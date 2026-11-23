<!-- scratch/studies/lead-185/CODING.md: the coding rules of LEAD-185's study, written before the table was coded -->
# Coding rules

Written on 2026-11-23, after a scoping pass over the public sources (to
learn which kinds of dated document exist for these cases) and before any
row of `cases.csv` or `events.csv` was entered. Changes made after coding
began are listed at the end, with their reason.

## The sampling frame

The frame is fixed by the record and the brief, not by what was easy to
find: every case named in CASE-223 (A's arms, A55's additions and the
reader's suggestions) and every example the lead's brief names. That is:
Freenode/Libera Chat, Redis/Valkey, GIMP/SourceForge, OpenOffice.org/
LibreOffice, RethinkDB, `data.table`, Audacity/Muse Group, MySQL/MariaDB,
Hudson/Jenkins, `event-stream`, Node.js/io.js, Terraform/OpenTofu,
Gitea/Forgejo.

**Inclusion.** A case is coded when (1) a project's name, code, hosting or
governing terms passed to, or were changed by, a steward, or a party
claimed to continue the project apart from its steward; and (2) dated
public documents exist for the move and for at least one response.

**Exclusions, decided before coding.**

- GIMP/SourceForge: the account SourceForge took over was a distribution
  mirror, not the project, and no party claimed to continue GIMP apart
  from its developers (A's own caveat, kept in CASE-223). It is a case of
  hosting, not of succession.
- `data.table`: a governance reform with no change of steward and no rival
  claimant; A gave no author or title for the study it reported.

## Arms

- **contested**: after the move, two lines each publicly claim to be, or
  to continue, the project, and both issue a release within 12 months of
  the successor's announcement;
- **accepted**: one line only continues the project after the change of
  steward, with no rival line issuing a release within 12 months;
- **reunited** is an outcome, not an arm: a contested case whose lines
  later merged.

## Events (one row each in `events.csv`, each with its source URL)

Each event has a date (ISO, to the day where the source gives it,
`precision` = day or month), the URL it was read from, a short quote or
paraphrase, and whether the source was fetched and read on 2026-11-23
(`checked` = yes) or is known only from a search summary or an archive
path (`checked` = no, with the obstacle in the note).

- `move`: the act of the steward that the successor's founders name as
  their reason (an acquisition closing, a licence change, a takeover of
  control, a company's formation, a shutdown). Dated by its first public
  announcement.
- `announce`: the first public announcement of the successor under its own
  name, or of the succession (for an accepted case, the new steward's
  taking over).
- `first_release`: the successor's first release.
- `endorse_prearranged`: statements by organizations outside the founding
  group that appear in, or on the day of, the founders' own announcement.
  These are verdicts by non-founders, but arranged with the founders, so
  they are coded apart.
- `verdict_outside`: the first dated public statement, by an organization
  that is neither a founder nor a named backer of the successor, that
  treats the successor as the project's continuation or legitimate home,
  or the original as illegitimate. Its `act` field says whether the
  statement announces the speaker's own move to the successor in the same
  act (`statement+move`) or is a statement only (`statement`).
- `downstream_replace`: the first decision by a major downstream (a Linux
  distribution, a large host or service) that is independent of the
  founders, to ship or use the successor in place of the original. Dated
  by the decision; `independent` says whether the downstream is free of
  the founders (a downstream whose staff include founders is coded `no`).
  Its `reason` field codes the downstream's stated reason:
  `identity` (the successor is the project, or the original is
  illegitimate or no longer the project), `licence` (the original's terms
  bar it), `practical` (security, maintenance, compatibility, openness of
  process), or a combination.
- `reversal`: the original steward undoes or softens the move.
- `name_transfer`: the successor gains the original's name, or the lines
  reunite under it.
- `original_end`: the original line's last release before it was archived
  or declared unmaintained, or the original steward's own statement that
  it is replaced.

## Case-level codes (one row each in `cases.csv`)

- `maintainers_moved`: `yes` if the successor's founders include the
  original's creator or the body of its core maintainers or staff, and the
  original kept no active core team; `partial` if named core maintainers
  moved and the steward kept an employed team; `no` if none of the
  original's core maintainers is among the founders. From the founders'
  announcement or contemporary reporting; source URL given.
- `outcome_2026`: which line the community treats, by 2026-11-23, as the
  project's continuation: `successor` (the original ended, or its own
  later steward points to the successor, or the major downstreams
  replaced it and none returned); `original` (the original keeps its name
  and no major independent downstream replaced it); `split` (major
  independent downstreams divide); `reunited`; `undetermined` (not checked
  far enough to code).
- `name_followed`: whether the recognized continuation (outcome) carries
  the original's name.

## Measures computed by `timings.py`

- `lag_move_to_announce`: days from `move` to `announce`;
- `lag_announce_to_verdict`: days from `announce` to `verdict_outside`;
- `lag_announce_to_downstream`: days from `announce` to the first
  independent `downstream_replace`;
- `verdict_separate_from_move`: whether the first outside verdict was a
  statement only, not itself a move;
- `verdict_before_downstream`: whether the first outside verdict precedes
  the first independent downstream replacement;
- `legitimacy_to_capability_lag`: days from `announce` (the public loss of
  recognized legitimacy among the founders) to `original_end`; open
  (`None`) where the original still releases, with the days to the
  study date reported as a lower bound.

## What the coding does not do

- It does not count contributors. No contributor series was built; that
  would need repository histories mined at scale, which the brief's ban on
  the GitHub API for other repositories rules out. Contributor moves enter
  only as `maintainers_moved`, from announcements and reporting.
- It does not code private motives. A downstream's `reason` is its stated
  reason.

## Changes after coding began

- `precision` was added once the MariaDB proposal's archive page proved to
  sit behind a bot check, so that its date is known from the FESCo ticket
  that cites it.
- `outcome_2026` gained `undetermined` for cases whose downstreams were not
  checked, rather than defaulting them to `original`, and `revoked` for
  `event-stream`, whose accepted succession was undone.
- `arm` gained `unclassified` for Audacity, whose fork's first release was
  not dated, so the 12-month rule could not be applied.
- Event kinds added while coding, each because a source recorded an act the
  first list had no place for: `community_vote` (Jenkins's rename vote,
  io.js's vote to join the foundation), `host_accept` (a foundation or
  non-profit taking the successor in; never counted as independent, since
  the founders arrange it), `original_restewarded` (the original line
  passing to a new steward, as OpenOffice.org to Apache and Hudson to
  Eclipse), `steward_escalation` (freenode's channel takeovers),
  `downstream_proposal` and `downstream_effective` (a downstream's proposal
  and its release, beside its decision), `fork_call` and `revocation`.
- Reasons are written as `+`-joined sets in alphabetical order, so that
  "identity+practical" and "practical+identity" count as one.
- The lower bound on the legitimacy-to-capability lag is not computed for a
  reunited case, whose original line did not lose its producers but merged
  with them.
