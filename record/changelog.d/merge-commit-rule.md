### Changed

- CLAUDE.md: a back-merge, or any pull request that brings main into staging,
  is merged with a merge commit, never a squash. A squash keeps the files but
  drops main as a parent, so the next promotion conflicts again. From
  RETRO-tmpd9oti's recommendation 2, at the owner's word.
