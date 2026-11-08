### Added

- ADR-tmp72iro (Proposed): a SYNTHESIS is an account of a scope of the record's argument and asserts nothing of its own. Whatever adds to its components is a CLAIM.
  - It supersedes ADR-076, ADR-077 and ADR-080.
  - It amends ADR-075, ADR-078 and ADR-tmpyihxy, which is now at version 3.
- Two lint rules, both failing the build: `current_account_on_superseded_claim` and `current_account_on_superseded_account`. An account in force must follow its components' revisions.
- New claims, filed from the syntheses that were never claims:
  - CLAIM-tmpt8x7l, the met-or-quiet complex (from SYNTHESIS-008);
  - CLAIM-tmpupm3q, the records' bounds on readiness (from SYNTHESIS-009);
  - CLAIM-tmp476gw, where the two justifications of the coding rule part. This was version 2 of the nucleating-argument line's synthesis.

### Changed

- **The SYNTHESIS scheme is accounts only.**
  - `role`, `warrant`, `admission`, `route`, `premises`, `grounds` and `uses` are removed, with their vocabularies.
  - Its statuses are Current, Proposed and Superseded, and mean whether the mapping is right.
  - `defeated_if` is fidelity.
  - A synthesis may be superseded by a claim, and a claim by an account.
- **Nine claims return under their own codes.** CLAIM-615, CLAIM-624, CLAIM-611, CLAIM-610, CLAIM-620, CLAIM-474, CLAIM-545, CLAIM-600 and CLAIM-336 take back the content of SYNTHESIS-001 to 007, 010 and 011, with their standing kept. Each of those syntheses is Superseded by its claim.
- **35 relations are repointed** from the syntheses to the claims: eight ARGs' `concludes`, two CASEs' `illustrates`, four claims' `rests_on` or `corroborates`, and 21 readings' `corroborates`.
- **A claim's `rests_on` and `corroborates`, and a reading's `corroborates`, name claims only again.**
  - The `argument` chain walks `rests_on` directly.
  - The `revisions` chain walks the new pattern `supersedes_claim`.
- **SYNTHESIS-tmpllsy7 is now the nucleating-argument line's account** (version 3), over its three part accounts and CLAIM-tmp476gw.
- **The five other accounts from the line-accounts work** drop their claim fields and their "unadmitted" wording.
- **The current-account view** sets out each line's accounts, and lists the lines with no account.
- **Skills and scripts:**
  - the `synthesis-review` skill and step 9b of `read-and-file` are rewritten for the new arms;
  - `scratch/formal/synthesis_fixture.py` tests the new rules, and passes;
  - `scratch/formal/synthesis_candidates.py` counts only accounts in force.

### Removed

- The pattern `rests_on_claim` and the six lint rules on admission, routes and premises.
