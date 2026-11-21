---
name: read-and-file
description: How this record takes in reading. Use it to file an exchange, a pasted synthesis, an upload or a single work; to check whether something is "already on the record"; or to read registered works and file the readings. ADR-068 holds the invariants; this file holds the steps.
---
<!-- .claude/skills/read-and-file/SKILL.md -->

# Reading and filing

ADR-068 decides what must hold. This file says how it is done, and it is
meant to change. When a step here turns out wrong or missing, edit it in the
same pull request as the work that showed it, and say so in that change's
changelog fragment. Changing an invariant, the list in ADR-068, takes a
superseding ADR.

Before filling in a field, check `docs/record.md`: what each scheme must
carry, which relations point where, and which vocabularies are closed.

Bare codes only. Never write a link target, and do not run `luria repair`,
`link --fix`, `index` or `lint` before pushing (ADR-054).

## 1. Intake: what arrived, and in whose voice

- **Name the source.** It may be an exchange (a share link, with numbered
  turns U1… and A1…), a pasted text, an uploaded file, or a single work.
- **Separate the voices.** The owner's turns are the owner's. An
  assistant's turns, and anything pasted from another assistant, are that
  assistant's. The owner did not write them and has not endorsed them
  unless the owner says so. The filing assistant's own ideas are a third
  voice, kept apart from both (step 12).
- **Fetch a share link, then decode it.** The repository's settings allow
  `curl` to `https://chatgpt.com/share/*`. A plain request may be refused,
  so send browser headers:

      curl -sS -o share.html \
        -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36" \
        -H "Accept: text/html" https://chatgpt.com/share/<id>
      python3 -I scratch/tools/chatgpt_share.py share.html > exchange.txt

  The decoder imports `fire` and `loguru`; if the container lacks them,
  `pip install fire loguru` first.

  Save both files in their own new directory in the scratchpad. The
  decoder writes the shared branch only, as `===== U1 (user) <time> =====`
  and `===== A1 (assistant) … =====` blocks under a `TITLE:` line: the
  turns the share page shows. Under each assistant turn it adds what the
  page does not show, as `----- A1 · <kind> (not shown on the share
  page) -----` blocks: the assistant's reasoning summaries and recaps,
  code it ran and that code's output, tool calls with text, and hidden
  drafts with a line of their own. Duplicates, empty messages, tool calls
  without text and web results are counted in a closing `[omitted from
  this file, counted: …]` line, so every assistant message is either in
  the file or in that count. The reasoning blocks are the other
  assistant's working, not turns of the exchange: they are its voice, and
  ideas in them are filed, if at all, as that assistant's. Pass
  `--visible_only` for the visible turns alone. If the page has changed
  shape, the decoder stops with `ShareFormatError`: report that, and do
  not file from a partial transcript or reconstruct one by hand. Never
  put an email address in the request (ADR-008).
- **Keep the source whole.** Save it verbatim to the scratchpad, and point
  every reader and drafter at that file. A condensation written for a
  brief is the lead's own text. Label it so and keep it in a separate
  file. Never check a quotation against it: a phrase the lead wrote about
  the source is not a phrase the source used.

## 2. Check against the record before filing anything

- **For every work the source names**, search `record/literature.d` by DOI,
  arXiv id, exact title and first author. Note what is held, its status and
  its NOTE.
- **For every idea the source states**, search claims, theories, questions,
  cases and terms by its key words. Then read the nearest entries' titles,
  not just whether they matched.
- **List the source's own ideas, section by section.** A synthesis carries
  constructions, worked examples, distinctions, taxonomies, tables and
  proposed entries as well as references. Readers cover the references;
  nothing covers the rest unless the lead lists it. Write the list (an idea
  ledger) before briefing anyone. A drafter handed a short candidate list
  files that list and nothing else.
- **Give the ledger a gaps column** (ADR-137). For each item, note
  what the source's own argument needs and does not supply: an unstated
  premise or condition, a result asserted without its derivation, a
  number, formula or attribution that does not check, a test proposed
  without a design, a link asserted between ideas that no component
  states. Step 9a fills them.
- **Build the map**: each section or turn of the source, and each item of
  the ledger, against the codes that already hold it. Most of a synthesis is usually already held. The
  map is the main deliverable of an "is this on the record" request.
- **Check again after reading.** The first search can only use the
  source's own words. Reading surfaces more: the construction it rebuilds,
  the example it reinvents, a term it means in another sense, the entry an
  idea would contradict. Search the record a second time with those, and
  add what turns up to the map. An idea that looked new is often held
  under another name.

## 3. Verify identifiers

- **Use the services in order**: the arXiv API, Crossref, DataCite,
  doi.org, OpenAlex.
- **Never send an email address** (ADR-008). Leave out `mailto=` and
  `email=`, and don't put one in a header or user agent.
- **`published:`** is the earliest exact date the sources give (ADR-002).
  When an edition date is used instead, say why in the history.
- **Wrong attribution is common.** The source may name the wrong author,
  article type or year. Correct it from Crossref, and later from the text.

## 4. Register what is not held

`luria new lit --title "..."`, then fill in:

- **`status: Deferred`**, with a `status_note` saying where the work was
  registered from and whatever is known about a copy;
- **a history entry at version 1**: "Filed, not read", with the check made;
- **a summary** that says why the work is here and which entries it bears
  on. A claim the source makes about the work is "unverified until read";
- **tags** from the closed `topics` vocabulary, primary first, with
  `anthology-candidate` last when it applies (ADR-005).

## 5. Seek a lawful copy

- **Where to look**, roughly in this order: arXiv; PubMed Central and
  Europe PMC; the author's, lab's or institution's page; course and
  scholarly third-party pages (ADR-074); the locations OpenAlex lists.
- **Which copies count** (ADR-074). A copy of a published article, or of
  an author's manuscript, on a course or reading-list page, a faculty or
  research-group page, a scholarly third-party site (SciSpace or
  typeset.io, Semantic Scholar's PDF) or an author's own upload
  (academia.edu, ResearchGate) is lawful to read. Shadow libraries and
  ebook-piracy sites (Sci-Hub, LibGen, Anna's Archive, Z-Library,
  epdf.pub) and uploads of whole in-copyright books are not. Two more
  kinds count (ADR-102): a copy whose host states it is published
  with the rights holders' permission (the publisher, author or estate,
  named), with the statement quoted in the NOTE; and a reply posted by the
  scholar it answers, on that scholar's site beside their own paper. And
  anything a course hosts counts, on its page or its site, a whole
  in-copyright book included (ADR-113); a course's link to an excluded host does
  not. A brief may narrow this only with a reason stated in the curation
  entry.
- **Stop at any bot check**: captcha, Cloudflare or WAF challenge,
  "Access Denied", rate limit, paywall. Never try to get around one.
  Retrying the same host doesn't help either.
- **A repository's documented machine interface is a route in its own
  right** (ADR-101). Open-access full text served by the repository's
  own documented API may be read even when its website shows a challenge.
  If the interface itself shows a check, stop there. Known routes:
  - Europe PMC:
    `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`.

  Say in the NOTE's history that the interface was the route, and name the
  decision.
- **The outcome sets the status:**
  - read: the work goes on to step 6;
  - **Unfetched** (ADR-053): a lawful copy was located at an exact address
    and not read, whatever stopped it: a bot check, a TLS failure, a reset,
    or this session's own permission system or network policy (ADR-074).
    The status note gives the address, the obstacle and the date. Never
    work around a refusal; name a host the network policy blocks in the
    curation entry, so the owner can allow it;
  - **Unavailable** (ADR-041): no lawful copy was found, or only a
    paywalled one. The status note says where you looked. A located lawful
    copy never makes a work Unavailable.
- **A copy the owner supplies** returns any of these to reading.
- **When the work itself can't be read, read its neighbours.** Find
  accessible literature that carries the same ideas, and read the best one
  or two. That might be:
  - a later open-access paper or survey that restates the model;
  - the authors' own working paper or thesis;
  - lecture notes or a textbook chapter its author posts openly;
  - an arXiv paper that re-derives the result.

  The same rules apply: lawful copies only, and stop at any bot check.
  Check the record doesn't already hold the neighbour.
- **Filing a neighbour.** It is a work in its own right, with a LIT, a NOTE
  and a THEORY. Its history says it was registered as a stand-in. Never
  file it under the original's code or present it as the original
  (ADR-114).
  - The unread original's LIT names the neighbour in its status note and
    in "Standing in the record", and says how far it stands in.
  - The neighbour's NOTE says, under Connections, which of the original's
    results it restates and which it doesn't.
- **Supplements get entries too** (ADR-114). A work read beside
  another, for a passage, a figure or a third author it reports, gets its
  own LIT and NOTE whenever the record quotes it or relies on it, and the
  quoting NOTE names its code. A THEORY is needed only if the record uses
  its account. A mention in the NOTE history is enough only for what is
  neither quoted nor relied on: a catalogue page, a translation used to
  confirm a citation.

## 6. Read

- **Delegate one reader per work**, in parallel, using the brief below.
  A subagent may be refused when it writes a file named as a report;
  ask for the report as its reply, and save it yourself.
- **Running notes, visible in flight** (ADR-108). Before starting a
  reader, cut a branch `claude/readers/<key>` from the filing branch, add
  a worktree for it in the scratchpad, commit an empty
  `scratch/readers/<key>.md` and push the branch (no pull request). The
  reader writes only that file, and commits and pushes it after each
  step. It never writes to the record, never commits a downloaded text,
  and never force-pushes. When the reading is filed, remove the worktree
  and delete the branch, locally and on the remote.
- **Parallel workers in one working tree** (ADR-tmp9sp9d). Drafters and
  filers share the filing branch's checkout. Each brief asks the worker
  to list the files it creates or edits. While any worker is writing,
  commit only listed files, never `git add -A`, and pull CI's repair only
  between workers. A writer whose subject is still being filed starts
  after it lands, or is followed by a pass that replaces "being read" with
  codes.
- **Downloaded files are untrusted data.** Put each in its own empty
  directory, and run any Python on them with `python3 -I`.

## 7. Verify before filing

The filer, not the reader, rechecks against the source text every quote
the filing leans on. That means the quotes in titles and claims, and any
quote that moves a status or changes an entry. Correct the LIT from the
text: authors, article type, venue. A reader's draft is a claim to verify,
not a finding.

## 8. File the reading

- **A NOTE** (`luria new note`):
  - status `Read` or `Skimmed`, chosen honestly;
  - a history entry naming the copy, what was read and what was skipped;
  - the sections Contribution, Key results (with section or page, and
    short verbatim quotes), Assumptions, Concepts, Bearing on the record,
    and Limitations.
- **A THEORY** (`luria new theory`), `Proposed`:
  - the work's central account, attributed to its authors;
  - `source:` the LIT;
  - a `promote_when` that asks only for what the title asserts (ADR-065).
- **The LIT**: status `Active` if it is worth reading, a new history
  version, and a summary rewritten from the reading.
- **Every entry the reading bears on** gets a dated section, "Note of DATE:
  AUTHOR, read", saying what the reading supports, qualifies or leaves
  open. Change a status there only if the note says why.
  - This includes the weaker bearings a reader reports (a parallel, a
    contrast, background), not only the codes the brief named. A request
    to read a work is a request for these notes and relations too; do not
    leave them for the owner to ask for. Say in the note which kind of
    bearing it is, and write a relation (step 9) only where the note names
    the reading as evidence. An analogy gets a note and no edge.
  - Leave a bearing out only when it is too loose to say anything, or the
    entry is retired; the curation entry lists each one left, and why.
  - When a reading meets a THEORY's `promote_when`, say so; promote it
    when the owner asks, or when the reading that meets it is independent
    of the one that filed it.

## 9. File the argument

- **The owner's ideas** go in as the owner's.
- **Another assistant's ideas** go in as `Proposed`, with "The wording is
  the reader's (or A's); adopting it is the owner's call" in the summary.
- **An idea gets a code when it has content of its own** and the record
  doesn't already hold it, even if it turns up only once (ADR-072). A
  passing mention with no content of its own stays in the NOTE, and the
  curation entry says so. The second-time rule is for ADRs and DPs, which
  are written when their occasion recurs.
- **CLAIM fields**: `role`, `warrant` (ADR-043) and `defeated_if`.
  - `rests_on` and `complements` point to CLAIMs only.
  - `grounds` points outside the claims: THEORY, CASE, LIT.
  - `bears_on` points to QUESTIONs (ADR-060).
- **Support is an ARG** (ADR-061). When the filing says something about
  whether one entry supports another, file an ARG with a `form`,
  `grounds` and `concludes`, and answer the form's critical questions in
  its body. Saying something about support means arguing it, doubting it,
  or finding that a reading carries less than a claim cited it for. "X
  does not show Y" is the ARG from X to Y, Rejected. A claim's own
  `rests_on` needs no ARG.
- **An ARG's title names its route** (ADR-136): its grounds and the
  step, before the conclusion ("X, by analogy, shows that Y"), never the
  bare conclusion, since the title travels without its status. A Rejected
  ARG's summary says where its conclusion's own standing lives: the claim
  or question that holds it, or that no entry does, or the entry that
  tells against it. A conclusion the rejection leaves untouched, with
  content of its own, is held in an entry of its own, in the voice of
  whoever put it forward, and the ARG `concludes` it.
- **Independent evidence is `corroborates`** (ADR-058), on the THEORY,
  when a reading supports a claim that does not rest on it. A reading the
  claim needs is `grounds`. When a work cited before it was read turns
  out to carry less, move it from `grounds` to `corroborates` and file
  the ARG that says why.
- **A reading that marks a limit is `bounds`** (ADR-094), on the
  THEORY, when a claim's own text cites it as a limit of its scope. A
  rival account or an unanswered counterexample is an objection instead.
- **A case or term that uses a reading is `draws_on`** (ADR-095),
  on the case or term: a case's method, measure, design constraint, check
  or component, a term's sense. `reported_in` stays provenance.
- **A note that names a reading as evidence writes the relation.** When a
  dated note on a question or claim cites a reading as evidence for or on
  it, write `bears_on` or `corroborates` from the reading in the same
  change (ADR-093).
- **`rivals`** is only for accounts that cannot both be right. Accounts
  that differ on which mechanism mattered most get a dated note instead.
- **A QUESTION** needs a `line:`.
- **Titles and H1 headings** carry no codes, so they keep agreeing after
  CI's repair (dmarx/luria#393).

## 9a. Fill the gaps (ADR-137)

Every filing of an exchange, a pasted synthesis or an upload fills the gaps
the ledger found, not only when the owner asks.

- **Decide first whether each gap is real.** A step the source skips
  because it is textbook, or a condition it states elsewhere, is not one.
- **Fill a real gap in the assistant's voice**, as a Proposed entry or a
  dated note:
  - *the missing step*: a claim with its derivation, checked with
    `python3 -I` where it computes, the check stated in the entry;
  - *a correction*: in the entry that uses the mistaken step, quoting the
    source and giving the right value with the check;
  - *a question*: when the gap is open and the record should hold it so;
  - *a lead* (ADR-109): for a test or reading that would settle it.
- **Say which gap it fills** and which turn or passage it answers. The
  summary ends "The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call."
- **File without offering first**, in the filing's pull request. Proposed
  standing and the voice line keep adoption the owner's call. What only the
  whole filing shows, across sources, is step 12's and is still offered
  first.
- **Support judgements a fill makes** (a fill that narrows, qualifies or
  defeats another entry) need their ARG (step 9).
- **A drafter's brief carries this step**, with the ledger items whose gaps
  the drafter owns.
- **A filing of a single work** puts gaps in the work's own argument in
  its NOTE's Limitations, and fills one only when the record uses the step.

## 9b. Audit the syntheses (ADR-075)

A synthesis is any turn, section or pasted text that states an overall
account: an executive summary of the record, "the positive account I
would propose", a recap or "refreshed synthesis", "what is genuinely
new". The idea ledger maps its items to their source turns. That finds
new content but leaves the integration with no address, so audit the
synthesis as well.

- **Find and group.** List every synthesis by turn and section. A later
  synthesis that revises an earlier one is a new version of the same
  thesis. A thesis is distinct when it integrates a different set of
  components or makes a different integrating claim.
- **Classify** each distinct thesis:
  - *descriptive*: it says what the record holds. Audit it, and use it to
    file or revise the scope's account;
  - *supposed*: conditional on hypotheses holding. What it adds is a claim
    with role `supposed`;
  - *proposed*: it puts an account forward. What it adds is a claim with
    role `thesis`.
- **Decompose.** Map each component to a code, with its status and voice.
- **Audit each version** for:
  - **attribution**: an owner contribution told as joint, as A's, or as
    the argument's own logic, and A's sentence told as the owner's;
  - **coverage**: what the source contributed that the synthesis drops,
    the owner's contributions first;
  - **fidelity**: components misstated against their codes;
  - **standing**: Proposed or unverified components told as established;
  - **integration**: what it claims beyond its components. If that is
    only labels, it is a recap; say so.
- **File what it adds as a claim, and its map as an account** (ADR-084, ADR-131). A synthesis
  is two things: a map of its components, and whatever it adds to them.
  What it adds is filed as a CLAIM only if it passes one of three routes
  (ADR-075, step 5), and the claim's body says which, under "Admission":
  - *a separating case*: a coherent case, stipulated if need be, in which
    every premise holds (no premise's own `defeated_if` met) and the claim
    is false. A case that is not stipulated and could plainly occur is
    checked against the claim's own `defeated_if` first: it may show the
    claim false, not only separate;
  - *a derivation*: a valid, nontrivial inference from the components
    that no CLAIM already holds. Warrant `demonstrated`; give the
    derivation;
  - *a discriminating prediction*: a dependency, mechanism or outcome the
    components leave open, with the outcome that would go against it.

  If a narrower sentence passes where the stated one fails, file the
  narrower one. Watch for a free parameter ("a declared bearer"): it
  absorbs every case, and fixing it can contradict the synthesis's own
  premises. If nothing passes, file no claim. The test only routes: it
  decides whether a synthesis also yields a claim, never whether it is
  kept. The map still goes in its scope's account, with each link the test
  failed under "Not stated on the record" and the reason, and the audit
  goes in the curation entry. A recap, a synthesis that adds nothing but
  labels to components an account already maps together, stays in the
  curation entry alone.
- **The map goes in the scope's account.** A synthesis of a line, a part
  of one, or a theme that crosses lines revises that scope's account (a
  SYNTHESIS, ADR-083) as a new version, or files one where there is none:
  - every component in `integrates`, a claim filed from it among them;
  - each link attributed to the entry that states it;
  - nothing added;
  - `defeated_if` is fidelity: a component misstated, an in-force
    component left out, or a link no component states.

  The account is Proposed. The owner sets it Current once its mapping is
  reviewed.
- **Account for it.** The curation entry gets a section, "Syntheses
  audited": each synthesis, its classification, what was filed or why
  not, and the findings by check.

## 10. Account for everything

**Before writing it, reread the source end to end yourself**, from the
verbatim file, against the ledger and the codes filed. Agents' reports
say what they filed, not what they were never asked to file. Every item
must end up in one of three places: filed, mapped to a held code, or
listed as left with a reason.

**Then list the support judgements.** Go through the filed entries and
notes for every place that says one entry supports, qualifies or fails to
support another. A support relation needs an ARG (step 9) when it is
**load-bearing** or **contested**:
- *load-bearing*: a status, a `grounds` entry or a conclusion depends on
  it, for example a case grounding a claim, or a theory applied to one;
- *contested*: the filing doubts it, narrows it, or finds that a reading
  carries less than it was cited for.

A plain `illustrates` link, with nothing said about how much it supports,
needs none: an ARG there is recording overhead with no gain in
discrimination. File the ARGs before the curation entry. A brief for
filers carries step 9's rule; a brief that leaves it out gets entries
without their arguments.

Write a curation entry (`luria new curation`) with three parts:

- **where the record already held it**: the map from step 2;
- **what was filed**, with codes;
- **what was left, and why**: a citation that couldn't be identified,
  an idea already covered, a slogan;
- **gaps** (ADR-137): every gap the ledger found, filled (with
  codes) or left (with the reason).

Nothing in the source is dropped silently. Add a changelog fragment
(`record/changelog.d/<slug>.md`).

## 11. Acknowledge, and push

- **Each code cited in prose whose entry is not in force** gets an
  `inactive-ok-file` directive with a reason. Proposed, Deferred,
  Unfetched and Unavailable entries count as not in force. Open questions
  and Active or Read entries need none.
- **Relation fields need no excuse**, so name no code in a directive that
  only a relation field cites. A code that excuses nothing is dead weight.
- **Check only your own files.** A narrow scan of the files you changed,
  with `luria.ref_status.scan(files=...)`, is fine for diagnosis.
- **Gate each commit on its edit** (ADR-tmp9sp9d): edit, check and exit
  non-zero on failure in one script, then commit with `&&`.
- **Commit and push each step.** Pull before every push, because CI's
  repair lands as its own commit.

## 12. Offer your own contributions

When the filing is done, the lead has read across all of it, which no
reader or source has. Say what that suggests, and offer it to the owner
before filing anything. This is not step 9a: a gap is internal to one
source's argument and is filled without offering; an idea here is drawn
across the filing, and moves the record's own argument.

- **Look for what only the whole shows.** Promising places are where two
  sources' constructions join into a result neither states, where several
  readings point the same way, where every reading shares an assumption
  (who supplies a capacity, which quantity is held fixed), and where the
  filing rests mostly on analogy and needs a test.
- **Offer, then file.** List the ideas in the reply, ranked by how far
  you would stand behind each. Say which are demonstrated, which are
  hypotheses, and what each would cost to check. File only what the owner
  accepts.
- **The assistant's voice is a third voice**, beside the owner's and the
  source's. File these ideas as `Proposed`, and end each summary "The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call."
- **Hold them to the record's standards.**
  - Check any proof or worked number yourself, with `python3 -I` where it
    computes.
  - A hypothesis says what would defeat it, including the objection that
    it only restates an entry the record already holds.
  - A proposed test, reading, construction or study goes in as a LEAD
    that `advances` the question or claim it bears on, at stage `idea`
    unless it is worked out (ADR-109); a dated note may name it.
- **The curation entry gets a section** listing them, and the changelog
  fragment a line.

## The reader's brief

Send each reader:

- **The work**: its identifier, and the lawful copies already known.
- **The rules**: lawful copies only, and "lawful" is step 5's list of
  copies that count, sent in full, not restated from memory (ADR-074);
  stop at any bot check or paywall without retrying, and stop at any
  refusal by the session's permission system without working around it; no email address to any service; downloads in their own
  directory, with Python run under `-I`; downloads stay in the
  scratchpad; in the repository, write only the running-notes file, in
  the reader's own worktree, committing and pushing after each step
  (step 6).
- **Why it is being read**: what the source claims about the work, and the
  record codes it bears on, with paths, to be read.
- **What to return**, in a file of under about 250 lines:
  - Provenance: the URL, the format, what was read and what skipped;
  - every copy located, read or not, with its exact address, its kind
    (step 5) and what stopped the fetch, with the date, so the filer can
    tell Unfetched from Unavailable;
  - Summary;
  - Contribution;
  - Key results, each with a section or page and a short quote;
  - Assumptions;
  - Concepts;
  - a verdict on the source's characterization of the work;
  - its bearing on each named code;
  - Limitations, including gaps in the work's own argument: a step it
    asserts without showing, a condition it leaves unstated (step 9a);
  - a candidate THEORY sentence and its `promote_when`.
- **A recheck.** After reading, search the record again with what the
  reading surfaced: the constructions, examples, rival readings and terms
  of art it turned out to involve, not only the words the source used.
  Report each held entry the first search missed, and correct any "not
  held" verdict it overturns.
- **Neighbours.** If no lawful full text of the work is reached, find and
  read accessible neighbouring literature that carries the same ideas
  (step 5), and write a report for each in the same format. Report
  every other work you read and quote, even for one passage, with its own
  provenance, so the filer can give it an entry (ADR-114). In the work's
  own report, say which neighbour stands in for it and how far.
- **And**: if neither the work nor a neighbour is reached, say so and
  stop. Write nothing from memory.
