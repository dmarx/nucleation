<!-- record/promotion-audit/NOTES.md -->
# Working notes

Append-only, newest last. Things a session learned that the queue and
decision files do not say.

## 2026-10-19 — opening the queue (batch-000, batch-001)

**Patterns that predicted the outcome.**

- *Demonstrated warrant, non-derivation defeater.* If a claim filed as
  demonstrated has a defeat condition about predictive power, modelling
  adequacy, a population's behaviour or an impossibility, the claim is
  compound or misclassified. Seen in CLAIM-077, CLAIM-098, CLAIM-285 and
  CLAIM-128. Read the `defeated_if` before the body: it is the quickest
  test.
- *A promote_when that bundles two jobs.* A proof plus "and it explains X",
  or a theorem plus "and humans behave so". These became splits or
  narrowings: THEORY-155, -008, -001, -156.
- *"The record's own" in a THEORY.* A result the record proves belongs in a
  CLAIM (ADR-032), as THEORY-005's became.
- *Check what the source actually proves.* THEORY-087's "regular half is
  derived in the sources" held only for linear-Gaussian models. Grep the
  NOTE's claims table for "cited" or "approximation" before trusting a
  promote_when's own summary.
- *Check the statement's quantifiers.* CLAIM-264 (strong generator vs
  density) and CLAIM-123 (sufficient stated as necessary) both had a
  correct theorem stated with the wrong scope. That is a correction, not a
  promotion blocker.

**Traps.**

- `luria lint` takes about eight minutes. The owner, 2026-10-19: open the PR
  and rely on CI to run luria, rather than waiting on it locally. `check.py`
  is the local check that matters for the ledger.
- `luria new adr` takes the next free number at once (the `filing` mode).
  Concurrent branches can collide on it.
- Codes in these YAML files are not linked or upgraded by `luria repair`.
  Use concretized codes. PR #165's tmp codes (CLAIM-tmpzk12h,
  CLAIM-tmpu2dsm, THEORY-tmpsuto2, THEORY-tmp2m4ke, THEORY-tmp60l2i,
  QUESTION-tmpxheie, QUESTION-tmp4uhs6) get numbers when it merges.
- Run the triage against a freshly fetched origin/main, never a local
  main. Queue version 1 was scored against a stale clone-time main
  (b84ad2e3), because `git checkout main || git fetch` never fetched once
  the checkout succeeded. Always `git fetch origin main` first, then cut
  the branch from origin/main. The triage script used for version 2 is
  `triage.py` here.

**Open threads.**

- Dependency unlocks (wave 4). CLAIM-056 rests on CLAIM-267 and CLAIM-081
  on CLAIM-270, but both also rest on Proposed claims (CLAIM-106 and
  CLAIM-056), so promoting 267 and 270 does not unlock them alone. CLAIM-189
  and CLAIM-191 apply CLAIM-270; check them once it is Active.
- The next triage should add a column for the warrant/defeater mismatch.
- Wave 2 has more seeds than the six already done. Grep THEORY for
  `promote_when` texts containing "Done", "met" or "confirmed", which mark a
  half-met condition.
