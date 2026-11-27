### Changed

- CI pins luria 1.12.0, up from 1.11.0, at the owner's go of 2026-11-27. The
  luria actions are pinned to the same release (`@1.12.0`, previously `@main`),
  so an action can no longer be newer than the luria it runs. With `@main`, a
  feature that landed in an action before it reached a release, such as the
  site build's `timings` switch, would have called code the pinned 1.11.0
  doesn't have.
- What 1.12.0 changes for this record: nothing it renders. A journal's books
  now come from a template luria ships, held byte-identical, and the generated
  pages built by 1.11.0 and 1.12.0 from this record differ in no file. The
  release's heading and page-title templates are opt-in, and this record
  configures neither.
