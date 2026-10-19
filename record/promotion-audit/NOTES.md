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
- CI's docs-check pushes a "docs: repair sources" commit onto a PR branch
  when sources need repair, for example unlinked codes in a changelog
  fragment written after `luria link --fix`. The run that bot commit
  triggers stops at action_required, and a maintainer has to approve it.
  Run `luria link --fix` last, after the changelog, and pull before pushing
  again.
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

## 2026-10-19 — batch 004 (wave 4)

**Patterns.**

- *Count the dependent's other Proposed premises.* Promoting a formal
  premise unlocked an entry only when nothing else under it was Proposed
  (CLAIM-322) or when the remaining premise could be swapped for an Active
  one (CLAIM-269, onto THEORY-004). Every dependent that also rests on an
  interpretive premise was retained.
- *Find dependents mechanically.* List the Proposed entries whose
  rests_on or grounds include a just-promoted code, with their other
  non-Active premises beside them. Twelve matched. The hand-off's guesses
  included two Active entries (CLAIM-310, ARG-006), which can be corrected
  but not promoted.
- *Pattern 1 again.* CLAIM-056, like CLAIM-193, is a "demonstrated"
  application whose formal core was split off under ADR-040, and its
  defeat condition is empirical. Every ADR-040 application claim with a
  demonstrated warrant should be suspected of this. CLAIM-081 is the next
  one.

**Open threads.**

- Batch 004's two promotion paths both wait on #165. Once it merges, one
  PR can split CLAIM-269 and promote CLAIM-322.
- Wave 2 seeding is still untried, and it is the better next batch.
  Wave 4 has little left with zero other Proposed premises.

## 2026-10-19 — batch 005 (wave 2 begins)

**Patterns.**

- *The promote_when says the proved half is done.* THEORY-174 ("already
  proved in refereed venues"), THEORY-168 ("already proved") and THEORY-017
  ("condition is met") each named a finished half and held the whole entry
  for the rest. Grep for those phrases first. Triage-002's keyword
  heuristic found them, and wave 2 went 5 of 5.
- *An elementary proof can be checked in the review itself.* THEORY-184's
  promote_when asked for "the proof checked independently of this reading".
  The proof is a triangle inequality on the pair (X, PX), so the review is
  that check. Write the computation in the decision's evidence, so the
  promotion PR can cite it.
- *The record's own derivation, found in a THEORY, goes to a CLAIM.*
  THEORY-165's Lipschitz bound is "the reader's derivation". It is
  correct, and its LP duality needs nothing from the paper once the primal
  is shown bounded. This is the same split as batch-000's THEORY-005.
- *Read the claims table in the source NOTE.* "asserted, no example" (C3)
  and "asserted, not computed" (C7) marked exactly what THEORY-168 must
  keep Proposed. "followed step by step" marked what could go Active.

**Traps.**

- In a worktree-isolated session, shell loops over `$n` and multi-command
  git pipelines are refused. Write `git show origin/main:<path> > file`
  one per call, then grep the files.
- The ledger branch's working tree lags main. Read entries with `git show
  origin/main:<path>`, not from disk.

**Open threads.**

- Batch 005's five follow-up PRs are not opened (batch-005.yaml).
- Wave 4 after them: CLAIM-237 could ground on THEORY-174's monotone half.
  CLAIM-105, -235, -319 and -320 may need only THEORY-165's Lipschitz
  claim. THEORY-018, THEORY-019 and CLAIM-148 may need only THEORY-017's
  core, which bears on CLAIM-269's THEORY-019 clause.

## 2026-10-19 — batch 006, in progress

- **Wave-4 re-grounding candidates after #176.** CLAIM-105, CLAIM-201,
  CLAIM-219, CLAIM-235, CLAIM-319, CLAIM-320 and CASE-037 cite THEORY-165
  for the continuity of the contextual fraction. That result is now held
  by CLAIM-tmp496tl, the Lipschitz bound split from THEORY-165 in #176.
  Once #176 merges, each one that needs only continuity can re-ground on
  the new claim.

## 2026-10-19 — batch 006 closed (wave 2 at 15 of 16)

**Is the wave-2 yield real, or is triage-002's heuristic picking easy
cases?** Mostly real, with a selection effect worth naming. Triage-002
scored promote_when texts for words like "met", "checked", "proved" and
"first half". Those words mark entries whose filer already found part of
the condition satisfied. So the heuristic does select for half-met
conditions, which is exactly the shape that splits. That is a selection
effect, but it is the intended one, because a split is a real promotion
of a real core. The evidence that the yield is not easy cases: in
batch 006, three of four promotion paths needed the record to supply a
missing step (a −δI shift, a contraction and occupancy-LP argument, a
column-space generalisation), not just to read a "Done". And the first
entry whose promote_when bundles nothing, THEORY-277, did not yield. Expect
the yield to fall as triage-002's keyword hits run out (THEORY-171 onward
mostly score on "checked" alone), and re-triage before treating 15 of 16
as the wave's rate.

**Patterns.**

- *A neutral example plus "persists with damping, not shown".* A uniform
  shift A − δI lowers every Lyapunov exponent by exactly δ, because
  Φ_δ(t) = e^(−δt)Φ(t). So any neutral-at-every-instant instability gives
  a stable-at-every-instant one. Worth remembering for other "stable at
  each instant" claims.
- *"Equal because both are the unique fixed point of one contraction."*
  Check that the two operators really are identical term by term, then
  the identification is immediate (THEORY-247).
- *A theorem stated at full rank often holds for a fixed column space.*
  THEORY-236's Theorem 1 is the case col = ℝⁿ of "a GL(p)-invariant index
  depends only on the column space". That generalisation is what a
  "write it for the centred case" request usually needs.
- *Re-derive the rank argument; don't trust the summary.* NOTE-693's
  sketch ("a dependence among rows of maximal |S|") does not close as
  stated. The working proof uses the zero lower-degree Taylor parts.
- *A promote_when that asks only for an independent proof does not
  split.* Register the independent source as a LIT, or put the THEORY-004
  standard (a step-by-step reading suffices) to the owner.

**Traps.**

- In a worktree-isolated fork, a long python heredoc that writes files,
  chained with git commands, is refused as "too complex to verify". Put
  the script in the scratchpad, run it alone, then run each git command
  separately.

## 2026-10-19 — batch 007: a control sample for triage-002

**What the control showed.** Five mathematics THEORYs whose promote_when
has none of triage-002's keywords, drawn by a fixed rule (sorted codes,
every 8th of 43). Four of five found a promotion path, against 15 of 16
for the keyword group. That is not a distinguishable difference at these
sizes, so triage-002's ranking is weakly informative at best. The class
predicts yield, not the keywords: a mathematical THEORY whose
promote_when asks for more than its title claims.

**What drives the control's yield.** Three of its four paths (THEORY-233,
THEORY-297 and THEORY-323's growth half) rest on short record-own proofs
standing in for a requested reading or second source. The keyword group's
paths more often rested on readings already done. So a high wave-2 rate
partly measures how often the record is willing to substitute its own
proof. That needs the owner's ruling (batch-007.yaml's owner_question,
and THEORY-277). Until then, every decision that substitutes says so in
its notes.

**Implications for triaging waves 3 and 5.**

- Don't rank by promote_when wording alone. Score instead (a) whether the
  promote_when names something the body's "What this does not say"
  disclaims, which is the bundling that splits, and (b) whether the title
  is mathematics with short textbook proofs. Both can be read off the
  entry in one pass.
- Wave 3 (source-backed, non-mathematical THEORYs) can't use the
  record-own-proof route. Its yield will depend on whether the NOTE says
  the source was "read in full" or "followed in outline". Score that from
  the NOTE's history line, and expect THEORY-106's shape (theorems read
  only in outline) to be common.
- Wave 5 (interpretive synthesis) should be sampled, not ranked, the way
  this batch did. No textual heuristic has yet been shown to predict
  yield, and a control is cheap.
- Always draw a small control alongside a ranked batch when a wave
  starts. Five entries was enough to show the ranking was not doing the
  work.

**Patterns.**

- *A title broader than its own body.* THEORY-009's title claims "spectral
  SSL" while its body lists three routes (symmetrized loss, kernel
  precondition, composition with an adjoint) that contradict it. Read the
  body's exceptions against the title.
- *A promote_when about something the THEORY disclaims.* THEORY-233
  (trained-network magnitude), THEORY-297 (truncation stability) and
  THEORY-009 (asymmetric objectives) each ask for evidence on a point the
  body says it does not claim. Move that clause to a QUESTION and judge the
  title on its own.
- *"Cited to" inside a THEORY's own list of results.* THEORY-323's
  white-noise inequality is cited in the source to an unread paper. Grep
  the body for "cited" before promoting a list of results whole.
