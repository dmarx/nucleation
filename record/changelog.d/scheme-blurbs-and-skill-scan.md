### Changed

- Each of the ten schemes in `luria.yaml` now has a `title` and a `blurb`, saying what the family is for. These are drafted from CLAUDE.md and the ADRs that set the schemes up, for the owner to edit. `docs/record.md` shows them under "What each family is" once it is next regenerated.
- `code.globs` now covers `.claude/skills/**/*.md`, so luria checks the codes the `read-and-file` skill cites (ADR-068 among them) and reports them if one is retired. The skill is scanned and not linked, so it stays plain text for the agent that loads it. Its citation of the Proposed ADR-068 is acknowledged.
