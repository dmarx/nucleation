# Design principles

Standing values this project keeps re-deriving in review, written down once so
they can be cited by number ("per [DP-1](design-principles.md#dp-1)") instead of re-argued.

These are **principles, not decisions.** A [decision](decisions/README.md)
records a choice among alternatives at a point in time; a principle is a value
that decisions *cite*.

**Principles are living documents.** Each carries a version, and a revised one
says so. A principle stated about one artifact is a principle nobody applies to
the next one, so when the same reasoning shows up somewhere the wording doesn't
cover, widen the wording and bump the version — don't write a second principle.

Add one on the *second* re-derivation of the same reasoning: one instance is a
decision, a pattern is a principle.

Each principle ends with an **origin note** naming the incident that earned it,
and the decisions whose experience produced it. This is not decoration. A rule
whose evidence is missing reads as taste, and taste gets re-litigated by the
next person with different taste.

<!-- GENERATED below this line by `luria index`, from the fragments in
     docs/principles/. Edit those, not this file. -->

---

<a id="dp-1"></a>

## 1. A file every contribution must touch is a lock — hand out fragments, generate the view

When contributing requires editing a file *everyone else* also edits, in the
same place, that file is a lock. Concurrent branches serialize on it, and the
conflicts carry no information — two changes that share nothing still collide
because both appended after the last thing. That is contention, not
carelessness, so "resolve them carefully" is not the fix.

Let each contribution own a file nobody else writes, and *generate* the shared
artifact from those. When the shared file's content is derivable, generate it
outright — then there is no collection step to forget.

*v1 · origin: Seeded from Luria. Replace this note with your own first instance*

<a id="dp-2"></a>

## 2. A hand-maintained projection of a source of truth will drift — derive it

No hand-maintained parallel copy of what an authoritative source already knows.
The copy is written carefully and drifts anyway; a missed entry ships silently.

Remedies, strongest first: **derive** the projection; or **guard the property,
not the list** (a test asserting "the list contains these names" is the drifting
list in a costume); or, if a hand list must remain, **choose its failure
polarity** and say so in a comment. Fail-stale — the miss ships as silently
wrong behavior — is never acceptable, and is the naive default.

*v1 · origin: Seeded from Luria. Replace this note with your own first instance*

<a id="dp-3"></a>

## 3. Culture must be compiled

A stateless collaborator can't be socialized, so a norm that exists only as
prose is followed probabilistically. Norms that matter get walked up the ladder
*prose → convention → mechanism → guarantee*. When you find yourself repeating a
correction, that is the signal to walk the norm up a rung.

*v1 · origin: Seeded from Luria. Replace this note with your own first instance*

<a id="dp-4"></a>

## 4. Fire before trusting

Every guard, alert and CI gate gets one deliberate sabotage run to prove it
catches, before anyone relies on it. **Provisioned is not working.** Even a
fail-safe guard needs firing once, or it silently never delivers the benefit it
exists for. Say so in the record when you fire one.

*v1 · origin: Seeded from Luria. Replace this note with your own first instance*

<a id="dp-5"></a>

## 5. No private brains

Knowledge is shared across collaborators regardless of species. Agent files are
legitimate as **bootloaders** — pointers to the shared record — never as
knowledge stores. The test: *would a new human hire need this?* Then it belongs
in the shared docs.

*v1 · origin: Seeded from Luria. Replace this note with your own first instance*

<a id="dp-6"></a>

## 6. It's not mine, but I'll pick it up anyway

When you encounter debt — a stale comment, a drifted convention, a dead test, a
number that collides, a guard nobody wired up — **fix it**, whether or not it
belongs to the thing you came here for. Leaving the shared space tidier than you
found it takes precedence over staying inside your task's boundary.

The principle exists because the *default* is the opposite, and the default is
expensive. Debt survives not because anyone decided to keep it but because every
individual encounter with it was, reasonably, someone else's problem — so the
cost is paid over and over in small amounts by people who each correctly
concluded it wasn't theirs to fix. *If not me, then who? If not now, then when?*
is the whole argument, and the answers are usually *nobody* and *never*.

This matters most in a **record**, because a record's debt is invisible while
the machinery still runs. An instruction that stopped being true, a citation to
a document that moved, a status nobody flipped — none of it fails a build, and
all of it costs the next reader.

Two rules keep it from becoming license to sprawl:

- **Repair, don't redesign.** Picking up litter is not remodelling the building.
  If the tidy-up turns out to be a decision rather than a repair — it needs a
  decision record, or it changes behaviour someone relies on — file it rather
  than smuggling it in.
- **Say what you picked up.** An unexplained unrelated change in a diff reads as
  noise, or worse as a mistake. One line in the commit message turns it into a
  gift.

*v1 · origin: Seeded from Luria. Replace this note with your own first instance*

<a id="dp-7"></a>

## 7. Pilot a change on a sample before sweeping

When a change of form will touch many entries — a new field, a retitling, a
relation retagged, a section restructured — **apply it first to a small
sample, have the owner review it, and only then sweep the rest.**

A rule can be read and agreed with and still come out wrong in its
application. Its wording describes what the author pictured, and the entries
it lands on vary more than that. The sample is where the gap shows, while
it costs a few edits to close. After a sweep the same gap is spread across
the whole scheme. It is reverted entry by entry, or, more often, it stays,
because nobody reads a thousand diffs.

What makes a sample useful:

- **It spans the variety, not the convenient cases.** Draw across the kinds,
  lengths and statuses the change will meet, including the awkward ones. A
  sample of the easiest entries tests nothing.
- **It is small enough to read in full.** Two or three entries for a new
  form; a few dozen when the variety is wide. The owner reads every one.
- **It goes out as a demonstration, not a description.** The reviewer sees
  the entries as they will be, in the pull request that will carry the
  sweep.
- **The sweep follows the reviewed form.** What the review changed applies
  to the rest. What the review did not see is not assumed approved.

The sweep waits for that review, even when the rule itself has already been
accepted. Accepting a rule approves what it says; the sample is how anyone
sees what it does.

*v1 · origin: Applied four times before it was stated: [ADR-043](../record/decisions.d/ADR-043.md)'s warrant field, [ADR-044](../record/decisions.d/ADR-044.md)'s corroborates relation, [ADR-056](../record/decisions.d/ADR-056.md)'s term kinds, and [ADR-148](../record/decisions.d/ADR-148.md)'s retitling. It was missed once, when a sweep of 115 syntheses nearly launched unpiloted ([RETRO-010](../record/retrospectives.d/RETRO-010.md), which recommends "pilot, then sweep"). The owner, on 2026-11-25: "this reflects a good generalizable policy"*
