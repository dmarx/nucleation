### Changed

- CI pins luria 1.10.0, up from 1.9.0. 1.10.0 adds `luria unconcretize CODE...`, which gives a numbered document its number back as a temporary code, recording the old code under `formerly:` unless `--noformerly`. `concretize` now also rewrites `luria.yaml`. Nothing in CI calls the new command, so the record's checks are unchanged.
