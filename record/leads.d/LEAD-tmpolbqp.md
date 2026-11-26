---
status: Open
title: "Pilot logical cooling with ghost retrieval on one research line: a retention field independent of standing, working views that stand in for tiers without moving files, a catalogue of cooled entries, and a log of every recovery"
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed from A34's fourth pilot, with A31 §§5, 9, 10 and 16, of the
    exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26).
    The checks against luria 1.11.0, the trial's arms and its criteria
    are the assistant's (Claude, in this session).
stage: costed
method:
- empirical
tags:
- information-retrieval
- design-rationale
- software-engineering
date: '2026-11-26'
line:
- record-as-apparatus
advances:
- CLAIM-tmpdid0k
- CLAIM-tmp6toz6
presupposes:
- LEAD-tmp79qro
blocked_on:
- the owner's choice of the line to trial
- the owner's ruling on declaring a retention vocabulary and field in luria.yaml, if the trial is to run on declared values rather than a scratch list
summary: >-
  A34, marked "Highest immediate practical value": "Introduce a retention
  vocabulary independently of standing, then classify a representative
  subset of the corpus." "Use generated working views to simulate these
  tiers without moving any files. Preserve a lightweight catalogue of
  cooled entries, inspired by ARC's ghost lists. Record whenever ordinary
  inquiry needs to recover cooled material." Evaluated by "retrieval
  precision, missed relevant material, tokens consumed, repeated
  derivations, and reactivation costs". A31 §16's "smallest coherent
  experiment" is the same trial in five steps. The tiers and ghost
  representations are those of A27 and A29 (TERM-tmp96b3g; LIT-tmpua7jt). The pilot is A's; the arms and criteria are
  the assistant's (Claude, in this session), and adopting them is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpdid0k CLAIM-tmp6toz6 CLAIM-1068 TERM-tmp96b3g LIT-tmpua7jt — Proposed, or cited for its design; the hypotheses this trial tests and the measures it borrows, cited on 2026-11-26 -->

# LEAD-tmpolbqp: Pilot logical cooling with ghost retrieval on one research line: a retention field independent of standing, working views that stand in for tiers without moving files, a catalogue of cooled entries, and a log of every recovery

## What A31 proposed, checked

Loaded into luria 1.11.0 with the record's `luria.yaml` as a stand-in, on
2026-11-26:

- A31 §5's `retention-tiers` vocabulary (unreviewed, hot, warm, cold) and a
  `retention` field on CLAIM with `default: unreviewed` load as written.
  A31's reason for the default, "to avoid treating the entire existing
  corpus as if its working-set membership had already been justified", is
  sound.
- **A view reads the default; a pattern does not.** `docs('CLAIM',
  retention='unreviewed')` returns all 1,346 claims, but the pattern
  `(c:CLAIM {retention: 'unreviewed'})` matches none: a pattern's property
  map reads the field as written. So A31 §6's `hot_on_cold` report and any
  pattern keyed on a tier see only the entries whose tier has been written,
  which is the right behaviour for this pilot (only reviewed entries are
  tiered) and worth knowing before relying on a default anywhere else.
- A31 §9's working-set template and §10's line-relative one are valid in
  form: `docs()` filters on any declared field, `line` included, and
  `vocabulary('lines')` gives each line's value and label.
- The record's present working account is large: `docs/current-account.md`
  was 619,499 bytes on 2026-11-26, which bears out A31 §9's "the page is
  itself becoming large".

## The trial

1. **Classify one line by hand** (A31 §16 steps 1 to 3). Take the
   worklists of LEAD-tmp79qro for the chosen line, and give each of its
   claims a tier: hot (in ordinary retrieval), warm (listed, not loaded),
   cold (in the ghost catalogue only). Until the owner rules on the field,
   the tiers live in a list under `scratch/`.
2. **Build the working view** (step 4): the line's hot claims in full, its
   warm claims as code and title, and a ghost catalogue of its cold ones,
   one line each (code, title, the codes it rests on), cheap to meet and
   enough to recover from.
3. **Run two arms** (step 5) on the same model and token budget:
   - *restricted*: the agent's search path is a worktree holding only the
     working view and the ghost catalogue, with an instruction to escalate
     to the full record when the view does not answer, and to log each
     escalation and each cold entry recovered;
   - *full*: the agent may search the whole repository, generated views
     included.

   The restriction is enforced by what the worktree holds, not only by
   instruction. A31 §9: "Otherwise, any storage-tier policy can be defeated
   by an indiscriminate `rg` over the entire repository."
4. **Tasks.** Twenty questions about the line whose answers the record
   holds, written from the line's SYNTHESIS and claims by someone who does
   not run the trial, each with its answer and the entries that hold it.
5. **Measures** (A34's): correctness against the held answer; tokens to
   answer; *repeated derivation*, an answer produced without citing the
   entry that holds it (CLAIM-1068's measure); recoveries of cold entries,
   and what each cost in tokens; missed relevant entries, from the key.

## What would count

- **For CLAIM-tmpdid0k on this line:** the restricted arm answers at least
  as correctly as the full arm (within 1 of 20), with at least 30 % fewer
  tokens, and the full arm re-derives more often.
- **Against:** the full arm is no costlier at equal correctness, or the
  restricted arm loses more than 2 of 20. Either is a result about the
  line's tiers as classified, so the classification is reread before it is
  read as a result about the claim.
- **About the tiers:** more than 2 of 20 tasks needing a cold entry says the
  classification cooled what is in use; none in 20, with savings, says the
  catalogue was enough.
- **About CLAIM-tmp6toz6:** whether the full arm's answers cite entries in
  proportion to how many generated pages repeat them, beyond their
  relevance by the key.

CASE-091's design, persistent memory varied with information and token
budget controlled separately, is the stricter version of the same
comparison, should this one be worth scaling.

## Cost

The classification of one line and the twenty-question key: a day. The two
arms: a few hours of agent runs.
