# record/status-review/README.md

How a status-review pass is run under ADR-057. The decision says what a pass
is for; this file is the working procedure the sixteen passes of 2026-10-27 to
2026-10-30 converged on. It replaces briefs that lived only in a session's
scratchpad. That is how one of them carried a wrong precedent, about a
narrowing's dropped clauses, for seven passes before a reviewer checked it
against ADR-047.

## 1. Build the worklist

On a freshly fetched `origin/main`, after the last pass's temporary codes are
concretized (main's latest commit is the docs bot's "regenerate views"):

    python -I record/status-review/worklist.py --top 30
    python -I record/status-review/worklist.py --show CLAIM-123

The first six sections must be empty: inversions, stale converses, sound
arguments whose conclusion is not held, unwritten concessions, retired
premises, and Open questions with an Active answer. Anything listed there is the pass's first
work. Then take work in this order:

1. **Ready for a ruling.** These claims have every premise held, no live
   objection and no standing blocker note. They are grouped by primary line,
   and a line's group is a natural cluster.
2. **Sole blockers.** These are the unheld premises that alone hold a claim
   back. Review the premise and the edge together: in passes 13 to 16 the
   blocker was more often a ground that is really corroboration (ADR-058)
   than a premise that could be promoted. A sole blocker is counted, not
   listed, while a recent blocker note holds the premise or every claim it
   holds back: that note already says what the wait is.
3. **Blocker notes something they name has moved since.** An entry the note
   names was revised, or a work it names got a reading, after the note was
   written. The wait may be over, so look before the timer runs out. When
   it is not, leave a new dated note that restates the wait and names the
   move that was checked, after the old one; replace the old note only
   where it is now wrong. The new note is the record that the look
   happened, and it takes the entry off this list.
4. **Proposed readings no source of which is read in full.** These need
   reading, not review. Leave them out of clusters.
5. **Live claims that need a work no NOTE reads.** An unread work takes no
   edge (ADR-058). Either the work is read, or the edge goes and the body
   keeps the citation; an Active claim on the list is checked first.

**The held timer is a floor, not the review.** An entry with a blocker note
under 14 days old is listed as held. The timer guarantees it is looked at
again at least once; it does not stop anyone looking sooner, and section 3
brings it back early when what it waits on moves (ADR-057 v7).

The load-bearing ranking by reach came last on 2026-10-30. By then the most
any Proposed entry was relied on was 1, and the ranking had stopped ordering
work.

## 2. Review, read-only

Size a pass at about five clusters, one reviewer each. A reviewer reads every
entry in full, with its premises, objections, dependents (grep the code) and
the NOTEs on its sources. It proposes exact text and edits nothing.

**Statuses.**

- **A CLAIM** goes Active when ADR-057's four criteria hold:
  - every premise is Active;
  - each live objection is answered or written in;
  - nothing in the record meets its `defeated_if`;
  - the ruling is made.
- **A THEORY** is a reading. It goes Active when it is read in full and its
  `promote_when` holds, or when its title claims no more than one study read
  in full measured (ADR-047's evidence rulings).
  - A `promote_when` asks only for what the title asserts (ADR-065). A title
    that reports what a source proposes, argues or finds, or what one study
    measured with its hedges kept, goes Active on its reading; a demand for
    replication or an independent test moves to a QUESTION, or, where the
    source asserts the wider thesis, to a Proposed THEORY that `extends` the
    entry and keeps the old condition. A demand for the version of record of
    a copy already read is dropped unless a discrepancy is named; the NOTE
    records which copy was read. A general title keeps its strict condition.
  - A checked, step-by-step re-derivation meets a request for a proof. Write
    it out, and put any computation in a script with controls that someone
    else re-runs before the ruling.
- **A TERM** is adopted when its definition is settled and every use says
  which sense it means.
- **An ARG** whose body names its own rejection condition goes Rejected
  when the condition is met.

**Narrowing.** Narrow a title only to make it promotable, and route every
clause the narrowing drops by ADR-047's "Where a narrowing's dropped claims
go":

1. A generalization the source asserts becomes a Proposed THEORY. It keeps
   the old wording, `extends` the narrowed entry, and inherits the old
   promote_when. Models: THEORY-164 and THEORY-174.
2. The record's own extrapolation becomes a Proposed CLAIM with
   `warrant: interpretive`, grounded in the narrowed entry.
3. A mis-statement, or a clause shown false, gets a dated note only.
4. Only open scope that nobody asserts becomes a QUESTION.

Passes 8 to 14 sent every dropped clause to a QUESTION, and the ADR-047
kind-1 sweep of 2026-10-30 repaired it.

**Narrow or split only when it frees something.** Narrow or split only when
doing so frees a dependent, or when the reading is promotable on its own
merits. A claim that needs only what an author proposes can stand on an
Active "X proposes that ..." THEORY split off on THEORY-1110's pattern; the
original reading stays Proposed.

**Relations (ADR-058, ADR-060, ADR-061).**

- **Corroboration, not grounds.** A Proposed reading the claim cites as an
  instance, a parallel, prior art or "weak support" is `corroborated_by`.
  This freed most of the claims promoted in passes 13 to 16.
- **No edge.** Each of these takes no edge, with the body citation as the
  link:
  - a rival account the claim's test must exclude;
  - an attribution;
  - an unread or Unavailable work.
- **Dropped.** A premise or ground the body never uses is dropped.
- **`answers` against `bears_on`.** `answers` is for an offered answer to
  the question as posed. A part-answer gets an ADR-049 split: an Answered
  child, and a narrowed parent that stays Open. Anything else is
  `bears_on`.
- **Field, not prose.** A body citation doing an objection's work goes in
  `objects_to`.

**Concessions (ADR-059).** A conceded objection is recorded by revising its
target. The target's history note must name the objection, or the target
carries a note headed `## Note of YYYY-MM-DD: filed with its concessions`
that names it. Promoting an objection makes its concession due: re-run the
worklist after each cluster lands.

**Kept Proposed.** An entry kept Proposed gets one to three sentences under
`## Note of YYYY-MM-DD: what holds it back`, stated as a missing result or an
unanswered objection. The heading is exact, because the worklist reads it.

**The traps.**

- **Inverted ground.** Promoting a claim that a Proposed THEORY or LIT still
  lists under `supports` fails the lint as inverted_ground. List every such
  reader in the report, and move or remove the edge.
- **Answered but open.** Promoting a claim that `answers` an Open QUESTION
  fails the lint unless the question changes status in the same change.

## 3. Rule, then apply

**Rulings.** The coordinator rules on each report. The owner delegated these
rulings to the status review on 2026-10-29, so the pull request lists the
interpretive ones for the owner to see, and merging it is the assent.

**Applying.** Each reviewer applies its own cluster. Clusters touch disjoint
files, and each reviewer is told the others' file lists. Reviewers do not run
git or any luria command except `luria new`. The conventions:

- **Codes.** Write codes bare. Never hand-write a link target.
- **Version and history.** Any content change bumps `version` and appends a
  `history` entry. The entry is dated the day of the change, says what
  changed and why, cites the decision, and quotes any old title or condition
  verbatim. A ruling is worded "at the status review's ruling (the owner
  delegated these rulings)".
  - A blocker note alone takes no bump.
  - Removing or changing a converse edge does take one.
- **Converse edges.** When an edge moves, remove its stale converse on the
  other entry by hand. The repair bot adds missing converses and never
  removes stale ones.
- **Promotion.** Promoting a THEORY deletes its `promote_when`.
- **Titles.** The `# CODE: title` heading matches the frontmatter title. A
  single-quoted YAML title doubles its apostrophes.
- **New entries.** New entries come from `luria new` under a temporary code.
  Overwrite the scaffold with clean frontmatter, using QUESTION-303 and
  THEORY-1117 as models.
- **Checks.** Check that every frontmatter parses.

## 4. Land it

**Commits.** Commit each cluster as its reviewer finishes, and push. Open the
pull request with the first cluster, and pull before each push: the
`docs-check` bot commits its repair onto the branch. Do not run `luria lint`,
`repair` or `index` locally (ADR-054).

**Before the last push.**

- Re-run the worklist on the branch. Its sections that must be empty include
  stale converses: an Active claim still listed under a Proposed reading's
  `supports`.
- File one workbench entry for the pass and one changelog fragment.

**The pull request** lists each cluster, the checks that were re-run, and
the calls the owner may want to see. It is ready when `docs-check` is green
on the last human commit; the bot's repair commit sits on top of it.

**After merging,** wait for main's docs-generate run to concretize the
temporary codes before cutting the next branch.
