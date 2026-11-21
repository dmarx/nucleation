### Changed

- [ADR-116](record/decisions.d/ADR-116.md), version 2: main is merged back into staging after every docs
  run on main, not only after a Promote run, by a script shared by Docs and
  Promote (`.github/scripts/back-merge.sh`). A promotion merged by hand, or a
  pull request into main, no longer leaves staging behind.
