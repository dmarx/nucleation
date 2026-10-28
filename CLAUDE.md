# CLAUDE.md

**Before anything else, read [the design principles](docs/design-principles.md)
in full, then [ADR-001](record/decisions.d/ADR-001.md) and
[ADR-048](record/decisions.d/ADR-048.md).** Together they say what this record
is for.

Nucleation is the catchall companion to the
[Anthology of the SOTA](https://github.com/dmarx/anthology-of-the-sota). It
holds whatever reading the owner files here. Its memory is a Luria record,
scaffolded, generated and linted by the `luria` CLI. This file is a
map, not a copy. When it disagrees with `luria --help` or with the record, this
file is wrong.

## Where things are

- `record/literature.d/`: one LIT note per work, and its standing here.
- `record/notes.d/`: one NOTE per work actually read, saying how deeply.
- `record/theory.d/`: THEORY documents, which are claims about what is true,
  each with its evidence.
- `record/questions.d/`, `record/claims.d/`, `record/cases.d/`,
  `record/terms.d/`, `record/arguments.d/` and `record/workbench.d/`: the
  record's OWN argument, as distinct from its readings of others'
  ([ADR-032](record/decisions.d/ADR-032.md)). A CLAIM has a credence (`status`), a voice (`role`) and a warrant
  (`warrant`: demonstrated, empirical or interpretive; [ADR-043](record/decisions.d/ADR-043.md));
  an objection is a claim; a thing gets a code the second time it turns up.
  `rests_on` is between claims and `grounds` points outside them, so the
  argument, its objection threads and its revisions render as chains.
- `record/decisions.d/`, `record/principles.d/`, `record/changelog.d/` and
  `record/curation.d/`: the record reasoning about itself.
- `docs/`: generated. Never edit an assembled page. See
  [docs/README.md](docs/README.md).

## The boundary

**Nucleation files any work the owner wants here, whether or not an anthology
topic could hold it** ([ADR-048](record/decisions.d/ADR-048.md)). Do not check
the anthology before filing: whether a work is also held there is the
anthology's question, not this record's. The one thing that still belongs to
the anthology is an instruction for machine-learning practice.

When you know the anthology's code for the same work, cite it (`ANTH-LIT-285`,
`ANTH-THEORY-106`). It is a nice-to-have, not a requirement. Codes are not
shared between the records. A work that the anthology may also want carries
the `anthology-candidate` flag last ([ADR-005](record/decisions.d/ADR-005.md)).

## Rules that are enforced

- **Every LIT names a source**: `arxiv:`, `doi:` or `url:`, in that order of
  preference.
- **Every THEORY names a `source:`**, and a Proposed one names a `promote_when:`.
- **Tags come from the closed `topics` vocabulary in `luria.yaml`, primary
  first.** A word the list lacks is added by decision, with a label and a
  blurb, never replaced by the nearest wrong one.
- **Never hand-write a link target.** Write the bare code; the pull
  request's CI repair spells the target.
- **Retire by status, never by deletion.**

## Working

    luria new lit --title "..."   # or: note, theory, question, claim, case,
                                  # term, arg, adr, dp, changelog, curation, workbench

`luria new` is the only command a contribution needs locally. Open the pull
request early and push each commit as you make it. The pull request's
`docs-check` job repairs the sources, pushes the repair onto the branch, and
lints the repaired tree. **Do not run `luria repair`, `link --fix`, `index` or
`lint` as a step before pushing** ([ADR-054](record/decisions.d/ADR-054.md)): it duplicates CI and, at
the record's size, takes minutes. If `docs-check` goes red, read its log, fix
what it names on the branch, and push again; a narrow local command is fine
for diagnosing. Pull before each push, since the bot's repair lands on the
branch as its own commit. Never commit generated views: they land on the
default branch through CI. Work goes to a branch and a pull request, and the
changelog fragment goes in the same contribution.
