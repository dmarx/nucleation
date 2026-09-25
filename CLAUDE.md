# CLAUDE.md

**Before anything else, read [the design principles](docs/design-principles.md)
in full, then [ADR-001](record/decisions.d/ADR-001.md).** Together they say what
this record is for.

Nucleation is the catchall companion to the
[Anthology of the SOTA](https://github.com/dmarx/anthology-of-the-sota). It
holds reading whose subject no anthology topic can hold. Its memory is a Luria
record, scaffolded, generated and linted by the `luria` CLI. This file is a
map, not a copy. When it disagrees with `luria --help` or with the record, this
file is wrong.

## Where things are

- `record/literature.d/`: one LIT note per work, and its standing here.
- `record/notes.d/`: one NOTE per work actually read, saying how deeply.
- `record/theory.d/`: THEORY documents, which are claims about what is true,
  each with its evidence.
- `record/decisions.d/`, `record/principles.d/`, `record/changelog.d/` and
  `record/curation.d/`: the record reasoning about itself.
- `docs/`: generated. Never edit an assembled page. See
  [docs/README.md](docs/README.md).

## The boundary

**If an anthology topic can hold a work, it goes to the anthology, not here.**
If the work carries an instruction for machine-learning practice, the same
applies. Nothing is filed in both. To cite the anthology, write `ANTH-LIT-285`
or `ANTH-THEORY-106`. Codes are not shared between the records.

## Rules that are enforced

- **Every LIT names a source**: `arxiv:`, `doi:` or `url:`, in that order of
  preference.
- **Every THEORY names a `source:`**, and a Proposed one names a `promote_when:`.
- **Tags come from the closed `topics` vocabulary in `luria.yaml`, primary
  first.** A word the list lacks is added by decision, with a label and a
  blurb, never replaced by the nearest wrong one.
- **Never hand-write a link target.** Write the bare code and run `luria link
  --fix`.
- **Retire by status, never by deletion.**

## Working

    luria new lit --title "..."   # or: note, theory, adr, dp, changelog, curation
    luria repair
    luria link --fix
    luria index
    luria lint                    # the only command that can fail

Run all of them before pushing, then **do not commit what `luria index`
regenerated**. Views land on the default branch through CI. Work goes to a
branch and a pull request, and the changelog fragment goes in the same
contribution.
