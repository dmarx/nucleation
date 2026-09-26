# Architecture decision records

A decision record is a **choice among alternatives at a point in time**. Write
one when you rejected an alternative, chose a constraint, or made something a
future edit could silently violate. Run `luria new adr`; it assigns the
identity and scaffolds from [`_template.md`](../../record/decisions.d/_template.md).

Values that decisions *cite* live in
[design-principles.md](../../docs/design-principles.md) instead — also generated, from
the fragments in `../principles/`. The split, and why these are separate files,
is [LU-ADR-001](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-001.md).

A decision whose **choice** changes is superseded by *adding* a decision and
flipping the old one's status — not by rewriting its body. A record you can
quietly rewrite can't be trusted about what you used to think.

That is a rule about silence, not about editing. A decision whose choice stands
but whose *reasoning* was wrong is corrected in place, with a `version` bump and
a `history:` entry saying what the previous version claimed. Nothing here is
frozen; it is only un-silently revisable. Luria's own record carries worked
examples of both: [LU-ADR-019](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-019.md).

<!-- GENERATED below this line by `luria index` — edit README.stub instead. -->

## By tag

**[The record](tags/record.md)** (5) — what the schemes hold, and the rules between them:
[001](../../record/decisions.d/ADR-001.md) · [002](../../record/decisions.d/ADR-002.md) · [003](../../record/decisions.d/ADR-003.md) · [004](../../record/decisions.d/ADR-004.md) · [005](../../record/decisions.d/ADR-005.md)

**[Taxonomy](tags/taxonomy.md)** (0) — the topic vocabulary and what enforces it.

**[Mechanism](tags/mechanism.md)** (0) — identifiers, generation, the lint.

**[Migration](tags/migration.md)** (0) — what moves between this record and the Anthology of the SOTA, and why.

**By status:** [Active](status/Active.md) (5) · [Proposed](status/Proposed.md) (0) · [Deferred](status/Deferred.md) (0) · [Superseded](status/Superseded.md) (0) · [Rejected](status/Rejected.md) (0)

## Chronological

What the status column means in this scheme — the words are luria's, the meanings are this project's.

| Status | | Means |
|---|---|---|
| `Active` | Active | In force — the current answer, and what a citation should normally point at |
| `Proposed` | Proposed | Not in force yet — an open question, so citing it as settled is the thing the report catches |
| `Deferred` | Deferred | Not in force and not being worked on; the question is real and the answer is waiting on something |
| `Superseded` | Superseded | No longer in force because something replaced it; the successor is named in the field, not the prose |
| `Rejected` | Rejected | No longer in force and nothing replaced it — kept because a rejection is worth being able to point at |

| # | Title | Summary | Status |
|---|---|---|---|
| [ADR-001](../../record/decisions.d/ADR-001.md) | Nucleation holds what the anthology's topics cannot: LIT, NOTE and THEORY, with a seeded closed vocabulary | The Anthology of the SOTA is scoped by its topic vocabulary, and its own rule is to add a topic rather than decline a document. But some reading is not about machine-learning practice at all: quantum foundations, network science, complex systems, mathematics, neuroscience, law. Nucleation is the catchall record for it. It ports the anthology's LIT, NOTE and THEORY schemes unchanged, so a work can move between the two without re-shaping. It leaves out the SOTA practice scheme, and starts with a closed topic vocabulary seeded from the out-of-scope clusters in the anthology's reading-time triage. | Active |
| [ADR-002](../../record/decisions.d/ADR-002.md) | published: is the exact date of first appearance where a source gives one | A LIT's `published:` records the day the work first appeared — an arXiv v1 submission date, a court filing date, a post's date — and falls back to the first of the month only when no source gives a day. The month-only convention inherited from the anthology threw away a fact every source already states. | Active |
| [ADR-003](../../record/decisions.d/ADR-003.md) | Ten more topics, seven of them grouped as philosophy | The topic vocabulary gains information-theory, social-science and linguistics, and seven philosophy words — metaphysics, mereology, agency, identity, ethics, consciousness, cognition — which a `philosophy` tag group labels as a set. The group is a label (`require: any`), not a rule: a work may carry any number of them, alongside any other topic. | Active |
| [ADR-004](../../record/decisions.d/ADR-004.md) | philosophy-of-science joins the philosophy group | An eighth philosophy word, `philosophy-of-science`, for what science is and what its theories say about the world: realism and structural realism, explanation, causation and evidence, the interpretation of physical theories. It joins the `philosophy` tag group [ADR-003](../../record/decisions.d/ADR-003.md) declared. | Active |
| [ADR-005](../../record/decisions.d/ADR-005.md) | anthology-candidate: a curation flag in the tag vocabulary | A work that may belong in the Anthology of the SOTA carries the tag `anthology-candidate`, after its topics and never first. The tag is a curation flag, not a subject, and a `flags` tag group labels it as one. Its generated tag page is the report of pending transfers. The work stays here until somebody decides to move it. | Active |

