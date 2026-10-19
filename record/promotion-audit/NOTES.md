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

## 2026-10-19 — batch-002

**Patterns.**

- *Counters are different.* Three of five were `role: counter`. They carry
  no `defeated_if`, so the warrant/defeater test does not apply; read the
  `objects_to` target instead. Promoting a counter means the record is
  persuaded, so pair it with a correction to the opposed entry (CLAIM-313 →
  CLAIM-310). A counter whose remedy is renaming (CLAIM-251) is the owner's
  call, not a proof.
- *Dropped qualifiers from an Active source.* Diff the claim's statement
  against the THEORY it grounds on. CLAIM-308 lost THEORY-348's
  "deterministic", and randomized rent-or-buy does better (e/(e−1) in
  expectation).
- *Exclusive "only" clauses.* Test them against the standard example of the
  field. CLAIM-251's "only the compatibility structure engages gluing" fails
  on CHSH, which carries both a PR box and product laws.
- *A demonstrated core no Active entry holds.* CLAIM-063's approximate
  identity: ARG-006 (Active) holds only the exact case. Check the ARG that
  concludes a claim before deciding a split is redundant.
- *A NOTE's "my inference".* NOTE-600's "consistently connected, by my
  inference" was a correct one-step derivation. Such remarks are cheap
  split cores.

**Traps.**

- Worktree-isolated sessions refuse compound shell commands with git. Run
  check, add, commit and push as separate calls, and do not commit after a
  failing check. It happened once here: queue version 4's wave counts were
  stale, and version 5 fixed them. Recompute the wave counts on every
  queue save.

**Open threads.**

- Wave 4 now has three concrete items: CLAIM-310 after CLAIM-313; ARG-006
  citing the CLAIM-063 split for the approximate case; CLAIM-081 and
  CLAIM-056 once CLAIM-270 and CLAIM-267 are Active.
- The next five pending in queue order: CLAIM-268, CLAIM-081, CLAIM-107,
  CLAIM-188, CLAIM-193. CLAIM-081 is better taken in the wave-4 pass after
  CLAIM-270.

## 2026-10-19 — batch-003

**Patterns.**

- *ADR-040 parents.* A claim whose note says "the general content is filed
  separately" (CLAIM-081 → CLAIM-270, CLAIM-193 → CLAIM-269) keeps only the
  carry-over to a domain. Its demonstrated warrant is then usually wrong.
  Review the general entry instead, and correct the parent's warrant.
- *An Active granted objection.* If an Active claim with `role: granted`
  objects to the candidate (CLAIM-094 → CLAIM-107), the granted point is
  the narrowing. Write it into the candidate's statement and promote the
  rest.
- *Empirical disjuncts that cannot defeat.* "Shown to agree on every pair
  tested" (CLAIM-268) does not refute a statement about what a method
  guarantees. Restate it as a derivation-type defeater rather than
  calling the claim compound.
- *Locate the singularity.* In model-reduction claims, check which model is
  singular at which parameter. For pruning, it is the model with the
  candidate, at the point where the candidate is switched off (THEORY-082),
  not the reduced model (CLAIM-188).
- *Look for an Active substitute ground.* CLAIM-269 grounds on THEORY-002
  (Proposed) for "kernels fix representations up to symmetry", but
  THEORY-004 (Active) proves the orthogonal-equivalence form. Before
  recording a dependency blocker, grep the Active THEORYs for the same
  statement.

**Traps.**

- Shell quoting: a note passed on the command line breaks on an
  apostrophe. Quote the whole note.

**Open threads.**

- Wave 1's yield fell from 3/5 to 2/5, and the remaining wave-1 candidates
  are mostly ones with Proposed premises. Run a wave-4 pass next: CLAIM-269
  (THEORY-004 and THEORY-008 re-grounding), CLAIM-310, ARG-006, and
  CLAIM-056 then CLAIM-081. Each is gated on an open PR merging (#165,
  #167, or batch 002's follow-ups).
- Wave 2 seeding (THEORY `promote_when` texts with "Done", "met" or
  "confirmed") is still untried.
