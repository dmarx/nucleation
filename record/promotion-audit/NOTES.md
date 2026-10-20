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

## 2026-10-19 — the owner's rule on re-derivations (after batch 007)

Asked whether a record-own re-derivation meets a promote_when that asks
for a proof the record does not hold, the owner chose to promote the
THEORY (ADR-047 v2). The alternatives were filing the proof as a CLAIM
only, or holding the entry. In practice, write the derivation out step by
step in the decision file, as batches 006 and 007 did, and cite it in the
history note. THEORY-277 is requeued on this basis.

## 2026-10-19 — batch 008, the first batch under ADR-047 v2

- **Re-derivation works for short, self-contained proofs.** It closed
  THEORY-160's bracket equivalence, THEORY-158's finite-state cycle and
  Basu's theorem in a Markov category, each in a few lines. Write it in
  the decision file under `scope.accepted`, so the promotion PR can copy
  it into a dated note.
- **It stops at constructions.** THEORY-277's Lemma C.4 reduced cleanly,
  but the covering construction it rests on did not close in two rounds.
  The trap is an enumerable set chopped into blocks in enumeration order,
  whose last block never provably fills. When a proof uses "chop the
  enumerated objects into blocks", check how it handles the final block
  before trusting the bound. Record the blocked step exactly, so the next
  attempt needs only one retrieval round.
- **Lost diagrams are a reason to re-derive.** NOTE-588 could not check
  Fritz's string-diagram proofs, which did not survive text extraction.
  An algebraic re-derivation from the prose definitions recovers the
  check. State the definitions relied on, because they too were
  reconstructed from prose.
- **An existence title asked for a characterisation (THEORY-171).** One
  checked example settles an existence statement. When the promote_when
  says an example "does not count", it is asking about a stronger claim
  than the title makes. That calls for a narrowing.
- **Keep a superseded decision traceable.** When a candidate is re-reviewed,
  overwrite its decision file and record the earlier disposition in
  `supersedes_review`. check.py allows one file per code.

## 2026-10-19 — batch 009

- **A third scope error in a correct theorem.** THEORY-686's title says
  the observations with no generative effect are exactly the left
  adjoints. The absence of generative effects is about binary joins, while
  Thm 1.115 needs all joins. A constant map to ⊤ has no generative effect
  and is not a left adjoint. That makes three after CLAIM-264 and CLAIM-123.
  When re-deriving under ADR-047 v2, test the title's quantifiers against
  the smallest degenerate case: the empty join, a two-element order, a
  constant map.
- **Frames from Stonean spectra.** THEORY-037's Heyting structure follows
  in a few lines once each stage is extremally disconnected. Closures of
  open unions are then clopen, and S ∩ cl U = cl(S ∩ U) for clopen S. A
  promote_when that rules out "Sub(X) is Heyting in any topos" is met by an
  argument internal to the clopen sub-objects.
- **Full readings can already hold the core.** THEORY-002 needed no
  re-derivation. NOTE-738 read every proof in App. B, C and E. Its title
  simply bundled them with a reading of the Platonic hypothesis. Check a
  NOTE's version-1 history line, which says what was read, before
  re-deriving anything.
- **The Dietrich–List result is beyond a two-round pass.** Proposition 3
  for the court agenda needs path-connectedness and a decisive-coalition
  argument. It is requeued as a dedicated pass, not deferred.
- **Wave 2's triage-002 list is exhausted except for THEORY-565.** The yield
  stays high (27 of 30), so re-triage the remaining mathematics THEORYs by
  bundling (batch-009.yaml recommendation) before moving to wave 3.
- **A stale directive was left on purpose.** CLAIM-107 still has a THEORY-158
  `inactive-ok` directive. #183 left it in place because #173 rewrites that
  file. Trim it once both #173 and #183 have merged.

## 2026-10-19 — triage-003 and batch 010

- **Bundling scores saturate.** triage_bundling.py gives the full 3 to 27
  of 34 eligible mathematics THEORYs, so its ranking is mostly the
  tie-break. Batch 010 went 4 of 4 on its top four, which is no evidence the
  ranking helps: the keyword list went 15 of 16, and the keyword-free
  control 4 of 5. Within this class, review in code order and skip
  re-triaging.
- **A promote_when can be mis-targeted, not bundled.** THEORY-014's
  condition asks for a bridge between formalisms that its body explicitly
  disclaims. The title was fully supported by two Read sources. The remedy
  is promote, with the condition moved to a QUESTION. No split is needed,
  because nothing in the title is unsupported.
- **Recurring cores.** Four of five cores this batch were short
  linear-algebra or spectral facts that sources state and call standard:
  the diffusion-map isometry (needs the 1/π weighting), the Fisher–NTK
  spectral identity (needs the model Fisher, not the empirical one),
  weight decay as a nuclear norm (needs the rank bound from the inner
  dimension), and tight frames and POVMs (needs equal norms within each
  factor). Each holds only with the hypothesis in brackets, so the
  narrowed statement must carry it.
- **Worktree isolation.** A worktree-isolated fork can't run compound
  shell commands, such as git piped into tar or a heredoc after cd. Write
  helper scripts to a scratch directory inside the worktree (here
  .tmp-main/, not committed) and run them one at a time. `git archive -o
  file.tar origin/main record` followed by `tar -xf` gives a clean copy of
  main's record for triage.

## 2026-10-19 — merging the audit's PRs (#165–#188)

- **Merge one PR at a time.** The Docs workflow has no `concurrency:`
  group. Merges seconds apart start several `docs-generate` runs at once.
  Each concretizes the same tmp codes with different numbers, and the
  runs that lose the push race fail on rebase: the main runs for #182 and
  #184 did. Nothing broken landed, because a later run concretized
  everything. Still, if the last run to start is one that loses, its tmp
  codes stay on main until the next push. Wait for each merge's generate
  step (its "docs: regenerate views" commit) before merging the next. A
  concurrency group on the workflow would remove the race; that is the
  owner's decision.
- **GitHub's "has merge conflicts" can be stale.** After main's
  concretization commit, #181, #183 and #186 were refused as conflicted
  while `git merge-tree --write-tree` exited 0, and the refusal did not
  clear on retry. Merging origin/main into the branch (a plain merge
  commit, no conflicts) and pushing reset it. Check the merged tree for
  references to tmp codes that no longer exist before pushing.
- **Conflicts are almost all `inactive-ok` lines.** Several PRs trim the
  same directive. Resolve by position, and keep a code only if every side
  keeps it, so every trim survives. Where line counts differ, resolve
  by hand.
- **Bot repair commits on a branch** ("docs: repair sources") leave a run
  at action_required. CI on the commit beneath is what counts. Read the
  repair's diff before merging. So far every one has only added links.

## 2026-10-19 — batch 011 (wave 2)

- The tag misleads triage. triage-003 drew wave 2 from THEORYs tagged
  "mathematics", but THEORY-022, -191 and -192 are empirical.
  Interpretability and Betti-curve studies carry the tag for their tools.
  Classify by what the title asserts: a theorem, or a measurement.
- Bounded Gromov δ from a tree decomposition with clique bags. If a graph
  has a tree decomposition whose bags have diameter ≤ 1, its geodesic
  triangles are 2-thin. Take the node of the tripod spanned by the three
  corners' bags that is nearest a bag of p; its bag separates p from the
  two corners. This settles hyperbolicity for any complex grown by gluing
  on single faces (stacked polytopes, k-trees, Apollonian networks), and
  is worth reusing when a promote_when asks for "δ bounded independently
  of N".
- "A tree of X tiles H^d" fails for d ≥ 3. In a face-to-face tiling, tiles
  around a codimension-2 face form a finite cycle, and a tree of simplices
  has none. It holds in d = 2 only because the codimension-2 faces of
  ideal triangles are at infinity. Check any "tiling by a tree of cells"
  claim this way.
- "The dual is a tree" depends on the flavor. With preferential or uniform
  gluing (s = 0, 1), several simplices share a face, so the face-adjacency
  graph has cliques. The gluing or parent structure is always a tree; say
  which one is meant.

## 2026-10-19 — batch 015 (wave 4, dependency pass)

- Wave 4 counts: 5 reviewed, 1 promotion path (CLAIM-269 split).
- CLAIM-107 was decided in batch 003 (narrow-and-promote, carried out in
  #173); its decision file is overwritten with supersedes_review,
  disposition needs-correction. CLAIM-193 (batch 003, needs-correction,
  carried out) and CLAIM-269 (batch 004, split) likewise. The queue
  entries for these three need their batch and disposition updated.
- CLAIM-148 and CLAIM-164 are new to the queue: add them as wave-4
  candidates, decided.
- THEORY-127's dependents, for a later batch: CLAIM-192 (Proposed,
  interpretive) and CLAIM-271 (Proposed, interpretive) use only the court-
  agenda possibility, that premise-wise and conclusion-wise majority can
  disagree, so each can re-ground on THEORY-725. CLAIM-030 (Active,
  interpretive) cites 'a rational group cannot judge proposition by
  proposition from its members' judgments', which is the general
  impossibility (Propositions 2–3), still THEORY-127's; THEORY-725's
  Proposition 1 is one instance of it, enough as a formal anchor if the
  text says 'can fail to', not 'cannot'.
- Pattern: an Active claim with a Proposed ground and an inactive-ok
  directive is a cheap wave-4 find after a split. Grep for directives
  naming a split parent.

## 2026-10-19 — batch 017 (wave 3, control)

- Wave 3's control: 2 of 5, both formal. Non-formal entries 0 of 3.
  Triage-004's components did not discriminate.
- triage_wave3.py's depth takes the weakest source, which hides a full
  reading of the source that holds the core (THEORY-078: depth 0, though
  NOTE-479 read the derivations in full). Consider taking depth from the
  NOTE of the source that the accepted clause cites, or the maximum over
  sources.
- triage_wave3.py's firsthand misfires on entries whose 'What was actually
  shown' opens 'Nothing is measured' (THEORY-470). Add negative phrases
  such as 'nothing is measured' and 'no theorems'.
- The `mathematics` tag under-marks formal results. Triage-004's own
  report of untagged formal entries (THEORY-248, -369, -198, -315) and
  this batch's THEORY-078 and THEORY-309 point the same way.
- Annealed or mean-field derivations (THEORY-199) are a recurring non-
  yielder. The source proves the approximation exactly, not the title's
  claim about the exact model. Read the claims table for 'strong for the
  map' or 'numerical fidelity'.

## 2026-10-19 — batch 014

- *Check which direction of a Proposed ground is used.* Three claims
  listed THEORY-156 (general Blackwell converse) as a dependency. Two used
  only the definition of a garbling, and one used the converse only
  outside finite outcome spaces, where THEORY-717 (Active) covers the
  rest. Grep the body for the sentence that cites the ground before
  recording a dependency blocker.
- *A sign question in a THEORY is a cheap re-derivation.* THEORY-312's
  promote_when asked only to settle a remainder's sign. Lemma B.0.1 closes
  on three intervals using (1 + x/2)² ≤ e^x on [−2, 0], and Theorem B.1
  needs only log(1 + x) ≥ x/(1 + x) and E Var − HSIC(Z,Z) = Var μ₁.
- *Pattern 1 recurs in the fidelity line.* CLAIM-212 and CLAIM-228, both
  'the record's reply of 2026-10-10', are demonstrated over a reception-
  study defeater. Expect the other 2026-10-10 replies in pragmatic-
  transport to have the same misclassification, and check them in wave 5.

## 2026-10-19 — batch 012 (wave 2)

- Exact hyperbolic trigonometry beats small-angle substitutions. cosh d =
  cosh(r₁ + r₂) sin²(θ/2) + cosh(r₁ − r₂) cos²(θ/2) turns an angle-packing
  lower bound into two lines with constants (THEORY-196).
- Minimax uniqueness is fragile. A worst case is attained by one
  adversarial target, and any encoder that is perfect on that target's
  plane ties. Test 'the unique minimizer' with a small tilt and the
  S-lemma dual, min over λ of λ_max(R + λ(S − cI)), which is a few lines
  of numpy (THEORY-239).
- Counting arguments: the negative half (more independent equations than
  unknowns, so the solutions are null) becomes a proof via the incidence-
  bundle dimension. The positive half (balanced counts, so solutions exist
  generically) can fail over the reals on open sets. A 2 × 2 rotation is
  the standard witness (THEORY-257).
- A fourth and fifth scope error in correct theorems (THEORY-239's
  uniqueness, THEORY-234's 'only when'). Read 'unique', 'only', 'exactly'
  and 'generic' in a title against the body's disclaimers before re-
  deriving.
- Triage-003's eligibility admits empirical THEORYs about mathematical
  objects (THEORY-254, tangles). Screen the title's verb.
- Worktree isolation: python one-liners with file writes through the Write
  tool to a path outside the worktree are refused. Write scratch scripts
  with a heredoc into a scratch directory inside the worktree (here
  .tmp-b012/, not committed). scipy is not installed, so a grid over λ
  replaces minimize_scalar.

## 2026-10-19 — batch 013 (wave 2)

- Fixed-point subspaces settle symmetry-cluster claims. For an equivariant
  vector field, Fix(Σ) is invariant for every subgroup Σ. Isolated
  desynchronization is Fix(K), with K the product of the other factors,
  and it needs the moving factor's support to be the cluster (THEORY-276).
  Use this instead of equal-input computations.
- An empirical THEORY can hide a record-own invariance-in-law argument
  (THEORY-288). With equivariant initialisation and optimiser, the law of
  the learned representation inherits the architecture's symmetry group.
  The argument needs an orthogonally equivariant optimiser. Adam breaks
  it, leaving only signed-permutation invariance. Check the optimiser
  before filing any such claim.
- Numerical scaling THEORYs (THEORY-304) yield their lower bounds to a
  rescaling argument (lift-up at streamwise wavenumber 0). Their constants
  and sharpness need the computation. File the lower bounds as a CLAIM and
  keep the parent.
- A fourth correct-theorem, wrong-scope case (THEORY-299), after
  CLAIM-264, CLAIM-123 and THEORY-686. An identification exact for the
  source's normalised variant (squared norms) is read as covering the
  original models. Check which variant a source actually works with.
- Re-deriving a promote_when's lemma chain can remove a Proposed
  dependency. THEORY-301's Cor. 1 is one line, so its promotion does not
  rest on THEORY-008.

## 2026-10-19 — batch 016 (wave 3, ranked)

- Wave 3's yield comes from its formal members. Of five top-ranked
  entries, the two that yielded were formal results without a mathematics
  tag, promoted by re-derivation. The three empirical ones were held by
  measurements the record has not read. Expect that pattern to continue,
  and route untagged formal entries to wave 2.
- Look first at the step a NOTE took on trust. THEORY-481's NOTE-658 said
  the Wishart fourth-moment step was 'followed as statements, not re-
  derived'. Re-deriving it found the source commuting the rotated
  empirical covariance Ŝ, which is not diagonal at finite N. That makes
  its per-mode decoupling and s^∞ exact only as N → ∞, or for isotropic
  inputs. Grep NOTE history lines for 'followed as statements', 'not re-
  derived' and 'taken as stated' before trusting an 'exact' claim.
- A concentration argument settles high-dimensional nearest-neighbour
  bounds. For fixed N and uniform data, all squared distances are d/6 +
  o(d), and the midpoint of any two points is at d/8 from the query. So
  every convex cluster of at least two points meets the nearest-neighbour
  ball with probability tending to 1. The same trick may serve THEORY-366
  (Beyer et al.'s distance concentration).
- triage_wave3.py's firsthand markers miss 'stated by no source', 'the
  filer's synthesis' and 'nothing was tested'. Its depth score reads 'read
  in full' per NOTE, not per claim. Both fired falsely in this batch.
- A source-derivation error is a needs-correction even when the record
  read the source faithfully. Correct the THEORY with status unchanged,
  add a dated note to the NOTE, and requeue the THEORY for narrow-and-
  promote, so a status change never rides on a correction.

## 2026-10-19 — the parallel round (batches 011–017), summary

- **Yields.** Wave 2's last 16, in code order: 11 of 16 (011 at 2 of 5,
  012 at 4 of 5, 013 at 5 of 5, plus THEORY-312 in 014). Wave 4
  (015): 1 of 5, with three corrections to Active entries. Wave 3: the
  ranked top five (016) and the control five (017) each went 2 of 5. So
  triage-004's ranking did not predict yield. All four paths were formal
  results that carried no `mathematics` tag (THEORY-111's core,
  THEORY-369, THEORY-309, THEORY-078's algebra).
- **The tag is the wrong class boundary.** Batch 011 found wave-2 entries
  that are measurements (THEORY-022, -191, -192). Batches 016 and 017
  found wave-3 entries that are theorems. Classify by what the title
  asserts.
- **The owner's rule on single studies (ADR-047 v3).** One study read in
  full is enough for an empirical THEORY whose title claims no more than
  that study measured. The replication request moves to a QUESTION. This
  should raise wave 3's yield on the hedged empirical entries, and it
  leaves causal or generalising titles, such as THEORY-470, where they
  are.
- **Trap: history order.** A new `history:` entry goes last, not first.
  luria lint reads the last entry as the current version and fails with
  "`history:` ends at version N but the document says N+1". Four PRs from
  this round prepended entries (#190, #193, #201, and ADR-047 v3 on the
  ledger) and were fixed by reordering. Also, a CLAIM's `grounds` takes
  only THEORY, CASE or LIT codes; another claim used as a worked example
  is cited in the body, not listed (#196).

## 2026-10-19 — batch 022 (wave 5 opens, fixed-rule sample)

- Wave 5's population (sample_wave5.py): 219 codes, 179 Proposed
  interpretive CLAIMs and 40 multi-source non-mathematics THEORYs. The
  THEORY half of the definition (at least three distinct LIT sources) is a
  proxy for "synthesis" and was not validated; THEORY-058 fit it well.
- An interpretive warrant over an observational defeat condition is
  pattern 1's mirror (CLAIM-052). The fix is a warrant correction to
  empirical, not a split, when the claim is a single generalization that
  is simply untested. ADR-043's "empirical" covers untested hypotheses
  whose support would be observational.
- An existence title with a documented case is the cheapest promotion path
  in every wave so far (THEORY-171's in batch 008, CLAIM-328 here). For
  interpretive claims it still goes to the owner.
- Claims in one argument line should be decided root first. CLAIM-217
  cannot move before CLAIM-151, which cannot move before CLAIM-004 and
  CLAIM-061. Sampling such claims independently spends reviews on entries
  that are blocked by construction.

## 2026-10-19 — batch 021 (wave 4, THEORY-127 dependents)

- Wave 4 counts: 3 reviewed (CLAIM-192, -271, -030), 0 promotion paths.
  CLAIM-206 and CLAIM-126 are wave-1 candidates: 2 reviewed, 0 promotion
  paths.
- All five decisions are new; none supersedes an earlier review. Remove
  CLAIM-192, CLAIM-271 and CLAIM-030 from the requeue list.
- Pattern 1, a demonstrated warrant left over a split-off formal core, has
  now appeared in five ADR-040 parents: CLAIM-081, -193, -056, -269 and
  -126. Check every ADR-040 parent still marked demonstrated, in one
  sweep.
- Pattern: dependents of a split parent usually cite its general result
  only for an existence statement. 'Cannot always' or 'can fail to' is
  settled by one instance, so the split's core is enough.

## 2026-10-19 — batch 023 (THEORY-127, Proposition 3)

- The ultrafilter argument fits in a decision file. For a judgment
  aggregation impossibility, the work is finite. - List the agenda's
  minimally inconsistent sets. - Show conditional entailment connects all
  literals. - Find one minimally inconsistent triple that stays consistent
  with two of its members negated. The rest is the standard finite-
  ultrafilter lemma. Reusable for any "no independent, unanimous, non-
  dictatorial rule" claim in the record.
- A general title can be false although its worked case is a theorem.
  "Interconnected propositions" fails on affine agendas, for example {p,
  q, p↔q}, where issue-wise parity is a non-dictatorial, independent,
  unanimous, robustly rational rule. When a THEORY states a social-choice
  impossibility for a vaguely named class, test it on an affine agenda
  before promoting the general wording.
- The record holds no Dietrich–List paper, and a grep for "Dietrich" finds
  an unrelated LIT-912 (flow). Under ADR-047 v2 the re-derivation stands
  in for it.
- **Trap: codes inside written paths.** `luria repair` turns a code
  inside a path such as `record/promotion-audit/decisions/THEORY-127.yaml`
  into a link, which breaks the path. In record entries, cite a decision
  file as "the promotion audit's decision file for THEORY-127", not by
  path. QUESTION-140, -141, -147 and -148 on main already carry broken
  paths (found by batch 023, not yet fixed).

## 2026-10-19 — batch 020 (wave 3)

- Triage-004's top scores carry no information: five 7-of-7 entries gave
  one promotion. Sort wave 3 by what the title asserts (theorem, measured
  result, argument) instead.
- ADR-047 v3's first use. A model-run result, in hedged existence form and
  read in full, promotes once its scope is narrowed to the model actually
  run (THEORY-295: a memoryless single-test consensus). Expect more of
  these among the social-epistemology simulations.
- Exclusive "only" again (THEORY-546). Test a title's "only when" or
  "requires" against the dilemmas its own body reports. The body named
  multiple occupancy as the alternative to non-branching.

## 2026-10-19 — batch 018 (wave 3, ADR-047 v3)

- First use of ADR-047 v3. "Read in full" was taken to allow figures and
  supplements unseen, provided the title rests only on results the text
  reports. Both NOTEs (672, 668) qualify. A title resting on a
  supplementary table known only by summary would not.
- A promote_when that asks for a confirming instance of a logical
  consequence (THEORY-255: "a second model that also places the deviation
  outside the meet") is met by the proof of the consequence. What remains,
  which published models drop which assumption, is a QUESTION.
- Triage-004's maximum score (7) went 2 of 3 here and 2 of 5 in batch 016.
  The three 7s reviewed here split along formal content, which the rubric
  doesn't score. Batch 017's formal-content flag is the fix.
- THEORY-235 should move to wave 5 in the queue: a single-source
  philosophical argument with open objections.

## 2026-10-19 — batch 019 (wave 3, formal)

- ADR-047 v3 needs the measurements, not only the reading. NOTE-816
  (THEORY-292) and NOTE-758 (THEORY-256) both say "read in full" and
  "figures read through captions only". The difference was that LIT-986
  states its numbers in the text and LIT-937 does not. Grep the NOTE's
  history for "captions" and check that the title's numbers appear in the
  extracted text.
- A short derivation of a preparation-noncontextuality bound without
  outcome determinism. Put u = μ1 − μ3 and v = μ4 − μ2. The equivalence
  gives |u|, |v| ≤ ν pointwise, and |σa + τb| + |σa − τb| = 2max(|a|, |b|)
  ≤ 2. Together these give σ⟨X⟩ + τ⟨Z⟩ ≤ 1. Dropping the equivalence gives
  2, the gbit. The same template may serve other symmetric-orbit
  inequalities.
- Screening lemmas from full capture. If I(H:E) = I(V:E) with H drawn from
  V alone, then I(V:E|H) = 0, and any separation statement that holds
  given V passes to H. This is the core of THEORY-198, and it is a general
  tool for information-bottleneck claims in the record.
- "Stays finite" in a bound's title should name its finiteness condition.
  THEORY-248's Lipschitz bound is finite exactly when the output law's
  rate-distortion function is finite at ε/(2L).

## 2026-10-19 — round 018–023, summary

- **Yields.** Wave 3: 018 at 4 of 5, 019 at 4 of 5, 020 at 1 of 5.
  Wave 4: 021 at 0 of 5, with four corrections. Wave 5: 022 at 1 of 5,
  the owner's call. THEORY-127 (023): narrow-and-promote, after
  Proposition 3 was re-derived. Every wave-3 path was a formal result or
  a measurement read in full (ADR-047 v3). Arguments and conceptual
  analyses went 0 of 7.
- **Sort wave 3 by what the title asserts** (batch 020). A theorem goes
  to re-derivation, a measurement to v3, and an argument to wave 5.
  Triage-005's route flag does this. Its score does not.
- **v3 needs the numbers in the text.** "Read in full" excludes results
  that the NOTE saw only in figure captions (THEORY-292).
- **Warrant correction is the next cheap work.** Wave 5's first sample
  promoted almost nothing. It found misclassified warrants, and a
  mechanical count suggests 36 more. ADR-040 parents marked demonstrated
  are a second sweep (pattern 1, five cases now).

## 2026-10-19 — batch 028 (warrant-correction sweep)

- Two readings of ADR-043 are in use. The pilot's: an empirical claim with
  no observation under it is interpretive (CLAIM-117, CLAIM-063,
  CLAIM-056). Batch 022's: it is empirical (CLAIM-052, #204). Until the
  owner rules, don't correct warrants in either direction on that ground
  alone.
- Term-of-art false positives. "Empirical model" (contextuality) and
  "experiment" (Blackwell's statistical experiments) fire the cue list
  without naming anything observed. warrant_sweep.py excludes the first;
  the second needs a reading.
- Check the defeater's quantifier against the title's. An existence title
  ("can") with a frequency defeater ("at a rate no greater than") is a
  mismatch, but read the history first: CLAIM-238 (Active, granted) is why
  the 2026-10-10 restatements turned possibility defeaters into prevalence
  tests, so the fix may be the title, and that is a design choice.
- A title already corrected by its own body. CLAIM-074's body says the
  transient/persistent dichotomy in its title "does not hold"; the title
  is unchanged. Grep bodies for "does not hold" or "needs stating" in a
  later pass.
- Split parents and earlier corrections reappear in any mechanical sweep
  (CLAIM-056, CLAIM-063). Skip codes whose last decision was carried out
  unless their entry changed since.

## 2026-10-19 — batch 024 (wave 3, re-derivation route)

- The re-derivation route went 5 of 5. Every title asserted a theorem, and
  each disposition separated a proved core from an extension to trained
  models, random starts or real data.
- A dual certificate is a short route to max-margin geometry claims. For
  min ‖X‖_* under margin constraints, the polar factor of the candidate is
  a certificate whenever its columns are nonnegative combinations of the
  constraint normals, which reduces to a sign check on (ẐẐᵀ)^{+1/2}
  (THEORY-286). Reusable for other unconstrained-features results.
- "Linear attention" in a title should say whether it is normalized. Sun
  et al.'s identity holds for the unnormalized form only (THEORY-169).
- Logistic per-mode dynamics recur: THEORY-182 (tied symmetric
  factorization) and THEORY-186 (two-layer linear) reduce to u̇ = 2u(λ −
  u) once the start is aligned. A split core of this shape takes a few
  lines to re-derive.

## 2026-10-19 — batch 025 (wave 3, re-derivation route)

- A reconstruction can show that a toy is not recoverable from the record.
  For THEORY-320, rebuilding the toy graph from NOTE-833's description
  reproduced Theorem 5.2 exactly, but not Theorem 5.3's threshold or Lemma
  5.4's harm case. That shows the set-up is underdetermined, not that the
  paper is wrong. Record the reconstruction and its mismatches in the
  decision file, so the next reading of appendix B can settle it in one
  round.
- The Donsker–Varadhan approximation gap closes by two-sided truncation.
  The negative part of log dP/dQ is P-integrable whenever MI is finite: ∫
  p log(q/p) over {p < q} is at most 1, by log x ≤ x − 1. The estimation
  gap closes by weak convergence of the empirical measures, uniform over
  an equicontinuous family. Both are reusable for other variational-bound
  estimators (NWJ, InfoNCE) the record may hold.
- Representer theorems over the completed RKHS need only projection onto a
  finite span and strict monotonicity. Existence needs lower
  semicontinuity and coercivity, and a counterexample without lower
  semicontinuity takes one line. Use this template when other kernel
  results are stated over expansion classes rather than H_k.

## 2026-10-19 — batch 026 (wave 3)

- A conditional theorem should be promoted on the hypotheses its proof
  uses, not the ones its source names. THEORY-478's source assumed 'a tree
  heat kernel'. The proof needs only a Hölder bound and a separation bound
  on Hellinger distances, and the admissible range is α < θ/β. The
  source's range (θ = 1) and the reader's repaired range (θ = 1/2) are
  then two instances of one theorem, not a dispute.
- Multiscale sums of the form Σ_k 2^(−kα) h_k with a Hölder regime below a
  crossing scale and a separation regime above it are equivalent to d^(αβ)
  exactly when α < θ/β. The coarse-scale geometric sum is the only place
  the exponent condition enters. A reusable template for multiscale
  diffusion distances.
- 'No Bell-like no-go in a prepare-measure scenario' has a one-line proof:
  send λ = (x, a). Any distribution with Y independent of (X, A) is then
  realized. Worth reusing wherever a source states a realizability claim
  without derivation.
- Triage-005's formal flag, read against content: one of three doubted
  flags was right. The doubt followed the subject tags (philosophy,
  quantum foundations), not whether the title relates defined notions.
- THEORY-614 is the first re-derivation-route entry to stop at one unread
  appendix step. Record the step exactly (likelihood summed over delimiter
  states) so that a single retrieval can close it.

## 2026-10-19 — batch 027 (wave 3, missed formal)

- Triage-005's prose-title misses were real formal results (3 of 4). Its
  formal flag reads titles; these four have formal content in the summary
  and body ("exact", "conserved", an SDE equation, a composition
  identity). Score the summary too.
- An existence clause is proved by a constructed example, even inside a
  paper's own restricted protocol. THEORY-176's "can stitch differently"
  took a two-position, one-channel example in which a 1×1 stitcher cannot
  undo a position swap. When a promote_when asks for a measured instance
  of a "can", build the smallest case first.
- Narrowing to the derivation's hypothesis is the commonest fix for formal
  THEORYs read off a paper's theory section: THEORY-187 (decoupled,
  balanced start) and THEORY-211 (the SDE model, both groups noisy,
  product at stationarity). The title's law is kept and its scope is
  stated.
- Promoting THEORY-176 removes one Proposed premise from CLAIM-126,
  CLAIM-225 and CLAIM-199. A wave-4 recount should follow once the PR
  merges.
- ADR-047 v3 with captions-only figures: THEORY-195's results are stated
  in the paper's text, so batch 019's rule is met, but the curve collapses
  were not seen. Medium confidence is the honest record of that.

## 2026-10-19 — batch 029 (ADR-040 parent sweep)

- The ADR-040 parent population is closed: all eight parents are now
  interpretive once CLAIM-081's correction merges. Pattern 1 needs no
  further sweep over ADR-040 parents. Watch new splits instead: when a
  split leaves the parent only a reading of a domain, correct the warrant
  in the same PR.
- A regex for "empirical" defeat conditions misfires on terms of art
  ("empirical model" in contextuality). Read the defeat condition before
  counting it. Batch 022's count of 36 interpretive claims with empirical-
  sounding defeat conditions may hold similar false positives.
- When a decision defers a warrant review until a premise is decided, as
  batch 003 did for CLAIM-081, record the trigger in the requeue list.
  Otherwise it waits until a sweep finds it.

## 2026-10-19 — batch 030 (wave 5, roots)

- The roots option in sample_wave5.py (--roots_only) drops population
  members whose rests_on premises include a Proposed interpretive claim,
  queued or not. Of 212 in the population, 159 are roots.
- Batch 022's mechanical count of interpretive claims with empirical
  defeaters over-reports. An interpretive claim can rightly have an
  observational defeater when its support is argument (CLAIM-327). A
  warrant is misclassified only when the support, not the defeater, is
  observational (CLAIM-052). Before a correction sweep, read each one's
  support, not only its defeated_if.
- Decide argument clusters root first in one owner question. CLAIM-046
  sits under CLAIM-206 and CLAIM-217, and CLAIM-241 objects to CLAIM-217.
  Ruling on CLAIM-206 against CLAIM-217 without the other two would leave
  both of them stale.
- A theorem read in full can still hide inside a multi-LIT synthesis
  (THEORY-109's Theorem 1). Check every wave-5 THEORY's NOTE claims table
  for "strong (proof)".

## 2026-10-19 — round 024–030, summary

- **Yields.** Wave 3, re-derivation route: 024 at 5 of 5, 025 at 5 of 5,
  027 at 5 of 5 (the formal entries triage-005 missed), and 026 at 2 of 5.
  The three entries whose formal flag triage-005 doubted split one
  promotion, THEORY-231, and two retentions. So the route predicts yield
  well, and its errors run toward missing formal entries rather than
  over-flagging them.
- **Sweeps.** The warrant sweep (028) found no miswarranted claims in 10.
  The ADR-040 parent sweep (029) found one, CLAIM-081. Both are mostly
  done. Under ADR-043 v2, the 37 interpretive claims with empirical
  defeaters are correctly labelled.
- **The owner's warrant rule (ADR-043 v2, #221).** `warrant` records how
  a claim is supported now. An untested empirical claim is interpretive,
  and its defeat condition can still be an observation. CLAIM-052 is
  reverted. Do not relabel a warrant only because the defeater is
  empirical.
- **Wave 5 roots (030).** Drawing roots of argument lines worked:
  3 of 5 had a path. Two of them are interpretive promotions, so they go
  to the owner.

## 2026-10-19 — batch 031 (wave 3, source route)

- Sort class predicted all five outcomes in batch 031: two arguments
  retained, one single-study measurement promoted under v3 (THEORY-216),
  one cross-study generalisation retained (THEORY-115), one theorem-class
  entry retained (THEORY-116). Triage-005 scored all five at 6, which
  carried no information.
- A theorem-class title can state the direction its source does not prove
  (THEORY-116: the title is LIT-669's Conjecture 1; App. F.3 proves the
  converse). Check direction before re-deriving, and grep the Active
  THEORYs for the converse. Here THEORY-732 (iii) already holds it.
- When a narrowing excludes a universal clause, grep the dependents'
  bodies for that clause, not only their grounds. CLAIM-273 cites
  THEORY-216 for "the lasting artworks are the ones whose coalitions keep
  placing under overwriting", which the narrowing drops, so its bullet is
  restated in the same PR.
- Queue: THEORY-073 and THEORY-223 move to wave 5 (argument class).
  THEORY-115 and THEORY-116 stay retained in wave 3. THEORY-216 is
  decided, narrow-and-promote.

## 2026-10-19 — batch 032 (wave 3, source route)

- Wave 3's source route, first five: 1 of 5, and that one (THEORY-324,
  Ashby) was a theorem in prose. Triage-005's formal flag missed it. Flag
  prose deductions ("only if", "necessary and sufficient", "every
  equilibrium is") as formal.
- A trigger condition in a sufficiency theorem. "Changes the parameters
  when the variables leave their limits" is ambiguous between a jump on
  crossing and a change for as long as they stay outside. Only the second
  makes every equilibrium adapted. A jump on crossing can land in a field
  with an unadapted equilibrium and stay there. Check "when ... leaves"
  wording in any feedback or homeostasis title.
- The depth score reads a full reading of a secondary source as full depth
  (THEORY-560, a narrative review; THEORY-411, an encyclopedia entry).
  ADR-047 v3 needs the study itself. Treat results a review reports as
  cited, not read.
- Necessity relative to a rule. Ashby's "only if" holds for systems that
  follow the trial-and-error rule, and becomes nearly definitional once
  the rule is assumed. A fixed regulator stable across the whole
  environment class needs no channel. When a promote_when widens an "only
  if" to "any system that achieves X", look for a regulator that achieves
  X without searching.

## 2026-10-19 — batch 033 (wave 3, triage-005 control)

- Triage-005's control: the route flag predicted 2 of 4. It was right on
  both arguments (THEORY-071, -485) and wrong on both measurements
  (THEORY-178, -306), each routed to source and promoted under ADR-047 v3.
  Sort by what the title asserts (batch 020). The flag catches theorems
  only.
- empirical_hedged scored 0 on both yielders. THEORY-178's measured
  signature is a model ensemble that the title does not name, and
  THEORY-306's contrast (MAE and data2vec) sits in the title's last
  clause. Read 'What was actually shown' for a model run or a table, not
  the title.
- Thomas's rule is not enough for synchronous Boolean necessity claims. A
  free negative cycle (a' = ¬b, b' = a, period 4) can be phase-shifted by
  a transient clamp. Beside any other oscillation, that gives a new joint
  attractor with no positive circuit in reach. Check for it whenever a
  Boolean attractor claim says "only through a positive circuit".
  THEORY-178's condition holds in its network only because the network has
  no such oscillator outside the reach of positive circuits.
- An "explicit in X" clause in an empirical title can be a one-line
  identity (THEORY-306: −H(p̄) = D_KL(p̄ ‖ U) − log K). Check it before
  treating the title as measurement only.
- Move THEORY-593, THEORY-071 and THEORY-485 to wave 5: each is an
  argument or conceptual analysis read in full, with nothing to measure or
  re-derive.

## 2026-10-19 — batch 034 (possibility theses)

- Batch 028's CLAIM-033 and CLAIM-115 decision files were on its unmerged
  branch at this batch's revision. This batch's files replace them, with
  supersedes_review naming batch 028. When both branches are integrated,
  keep batch 034's files (check.py allows one file per code).
- A defeater restated in place leaves its title behind. Whenever a history
  note says a `defeated_if` was restated, check the title in the same
  review. All three of the 2026-10-10 in-place restatements CLAIM-238
  prompted left a possibility title over a prevalence test.
- A split parent can keep the split-off core's quantifier (CLAIM-105: its
  "can" is CLAIM-320's, since 2026-10-15). After an ADR-043 or ADR-040
  split, the parent's title should say only what the parent keeps.
- CLAIM-238's comparative half was answered with new entries (CLAIM-220,
  -202, -204), not by restating the old ones. So CLAIM-115 and CLAIM-139
  still carry marginless defeaters by design. Don't correct them; whether
  CLAIM-220 supersedes CLAIM-115 is the owner's open decision.
- CLAIM-139 and CLAIM-143, also named by CLAIM-238, are unreviewed for
  defeater fit. CLAIM-143's second disjunct is an impossibility, like
  CLAIM-077, and probably fits; CLAIM-139 is comparative, like CLAIM-115.

## 2026-10-19 — batch 035 (possibility theses, part 2)

- Read CLAIM-238's own lists before calling an objected-to claim a
  possibility thesis. It sorts its targets into three shapes: nulls with
  no margin, "can" theses, and impossibility conditions. The remedy
  differs by shape: a margin, a prevalence claim, or an argument.
  CLAIM-238's version-2 history names which targets have been restated; a
  target at version 1 is still bound in full.
- Exclusive "only" again, in a CLAIM (CLAIM-143). Test a singular "after X
  is fixed" against quantifying over a class of X. Here a disagreement can
  survive every admissible correspondence, so the claim holds only with "a
  class of correspondences" in place of "the correspondence".
- THEORY-628's outcome matches triage-005's route (source, retained). With
  it the control sample (THEORY-071, -178, -306, -485, -628) is fully
  reviewed; tally it against the route when integrating. The queue also
  marks THEORY-176 `control: true`, though triage-005's control list does
  not name it; reconcile. Arguments filed as THEORYs go to wave 5.
- A record-built toy model does not meet a promote_when that asks for a
  worked case of a conceptual distinction (THEORY-628). It builds the
  distinction in by construction. ADR-047 v2 covers proofs, not
  constructed cases.
- A coded-corpus result is a measurement under batch 020's rule, and
  ADR-047 v3 can apply (THEORY-167). Check that the coding data, not only
  its summary, is in the text read. Propp's per-tale schemes were garbled
  in the OCR and unread, and they carry the order claim.
- THEORY-167's Source line understates NOTE-615's reading (it names four
  chapters; the NOTE read all nine). Fix it when the entry is next edited.

## 2026-10-19 — round 031-035 tally and triage-006

- Round yield: 4 promotions (THEORY-216, -324, -178, -306), 3 title
  corrections (CLAIM-033, -087, -105, in #222), 16 retained. The source
  route went 1 of 5 in each of batches 031 and 032, and the one in 032
  (THEORY-324) was a prose deduction that the formal flag missed.
- Triage-005 control tally (THEORY-071, -178, -306, -485, -628): the route
  flag sent all five to source; two yielded (THEORY-178, -306, both
  measurements under ADR-047 v3). Batch 020's sort by what the title
  asserts got all ten of 031 and 033 right. Keep sorting by the title;
  use the flag only to order the queue.
- THEORY-176 has no `control` flag in the queue; batch 035's note about it
  was a misreading and needs no change.
- Triage-006 replaces the formal flag (signals: title, cites, relation,
  derived; minus a philosophical title; threshold 2). On the 30 labelled
  entries it gains recall (0.90 vs 0.76) at equal precision, but it was
  fitted to those 30. Every labelled false flag scores exactly 2, as do 53
  of 82 flagged; treat the score-2 band as noisy. THEORY-290 is wrongly
  penalised by the philosophical-title signal ("argument" there means
  debate content); review it as formal.
- Batch 034's decisions for CLAIM-033 and CLAIM-115 replace batch 028's;
  CLAIM-077's retain-proposed replaces batch 001's needs-correction.

## 2026-10-19 — owner ruling: prevalence over possibility

- The owner accepted #222's restatement of CLAIM-033, -087 and -105 as
  prevalence claims, as easier to corroborate and harder to reject. When a
  possibility thesis's defeater tests a rate, restate the title as a
  prevalence claim (CLAIM-238's remedy); do not weaken the defeater to
  "the cited instances fail on inspection".

## 2026-10-19 — batch 040 (wave 5, requeue)

- CLAIM-265's defeat condition was met by its own counterexample: a
  verdict reached over a whole class "without any correspondence being
  fixed". When a defeater names a condition, check whether a case the
  record already holds meets it.
- An argument whose title, cut down to what it establishes, becomes the
  premise or a conditional on it (THEORY-223, THEORY-593) is a conceptual
  proposal waiting on its experiment. Retain it. Do not keep narrowing.
- An argument THEORY can have a real narrow-and-promote path in wave 5
  (THEORY-073: restrict to the formulation and applications the critiques
  examined). ADR-047 has no route for arguments, so it goes to the owner
  like an interpretive CLAIM promotion.
- A correction that gives a CLAIM a proof (CLAIM-265) moves it to wave 1.
  Requeue it there as demonstrated once #227 merges.
- Requeue: CLAIM-265 to wave 1 after #227. CLAIM-143 after CLAIM-004 is
  decided and the owner rules on carrying the class wording into it.
  THEORY-223 and THEORY-593 wait on studies; no requeue.

## 2026-10-19 — batch 041 (wave 5, requeue)

- Judging an argument on its own terms in wave 5 did not change any of the
  three wave-3 verdicts. Each promote_when asks for something an argument
  cannot supply (a mechanical procedure for THEORY-071, a formally stated
  worked case for THEORY-628), or for readings the record lacks
  (THEORY-485). Requeuing an argument from wave 3 to wave 5 is only worth
  a review if its promote_when, its premises or its rival changed in
  between. Check git log on the entry, its NOTE and its rival before
  spending a review.
- The one route by which these arguments could move is a title that
  reports the argument ("X argue that ..."). That is batch 032's open
  owner question on THEORY-351. THEORY-071 and THEORY-628 both wait on it.
  Ask it once for the class.
- THEORY-485 is the cheapest of the three: its promote_when can be met by
  readings (Ney 2016 and 2021, Chalmers and McQueen 2022, Bikaraan-Behesht
  2022) plus an argument for P7. Queue a reading task.
- A numerical model result read in full counts as one study under v3
  (THEORY-178, now THEORY-290). Narrow to the model's sizes and strategy
  space, and keep the equilibrium-selection caveat in the body when a
  result depends on which equilibrium is chosen.
- Triage-006's philosophical-title penalty is a word match. THEORY-290's
  "argument" was debate content. Before applying the penalty, check
  whether the word is the entry's subject or its method.

## 2026-10-19 — batch 036 (wave 3, triage-006 formal 1-5)

- Triage-006's top five went 4 of 5 by re-derivation; the fifth
  (THEORY-080) derives too but is the record's own synthesis. Before re-
  deriving a formal_route entry, read its summary for "the filer's
  synthesis" or "stated by no source": those go to a CLAIM under ADR-032,
  not to promotion.
- A source theorem about a sequence of networks can hold as stated only
  under strong connectivity. When a title says "the consensus" or "the
  limit belief", check whether the source's statement allows several
  closed groups, and narrow to one if the derivation needs it
  (THEORY-321).
- "Learned not at all below X and in full above it" (THEORY-293) is a
  recurring overstatement of threshold theorems whose upper bound carries
  a margin. Check both ends of a threshold.
- For a "learns modes in order of eigenvalue" title, check that the order
  is stated for a common initial scale; the step time depends on the
  initial scale too (THEORY-229).
- The disintegrated change of measure plus the subgaussian square-moment
  bound reproduces Sefidgaran & Zaidi's Theorem 1 constants exactly; a
  reusable check for PAC-Bayes-shaped titles.

## 2026-10-19 — batch 037 (wave 3, triage-006 formal 6-10)

- Triage-006's formal route went 4 of 5 on its entries 6–10. The miss,
  THEORY-110, is a false flag of a nameable kind: an empirical conjecture
  whose body cites theorems proved for toy models. The "cites" signal
  fires on those. When the cited theorems are about a different model from
  the title's, the entry is not formal.
- Check every "only when A and B" in a title against the exact condition.
  THEORY-185's "weak and alike" turned out to be "alike relative to their
  size" (min s > s_(1) s_(2)). Equal strengths keep the analogies at any
  strength, so "weak" was a first-order assumption, not a necessity.
- A Kronecker or tensor-product eigenstructure gives clean attribute modes
  only when each factor's top eigenvector is constant (balanced
  attributes). Without that, even the top mode is a product. Check balance
  before reading "the eigenvectors are the attributes".
- A bound stated as "Bayes risk at most X above" can be X in expectation
  and 2X pointwise (THEORY-161's TV bound). The tower rule gives the
  expectation form. Check which one a title means.
- A conditional title ("When P, then Q") whose promote_when asks for P to
  be measured: under ADR-047 the measurement sits outside the title and
  moves to a QUESTION (THEORY-185). This is the same move as THEORY-324's
  wider form. It is flagged in the decision in case the owner reads such a
  promote_when as a hold.
- A reading claim about a field ("the frameworks of 2021–2025") can be
  held to the papers read in full, by analogy with ADR-047 v3. The field-
  wide form moves to a QUESTION (THEORY-161).
- THEORY-110 could be split in the manner of THEORY-109 once the record
  has checked Lin et al.'s Theorems 10, 11 and 18 (NOTE-535 read them for
  statement only).

## 2026-10-19 — batch 038 (wave 3, triage-006 formal 11-15)

- Triage-006's formal route went 4 of 5 on its entries 11–15, all at score
  3. The miss (THEORY-270) was a theorem whose long proofs the NOTE read
  only in outline. Read a NOTE's history line for "overviews" or "not
  checked line by line" before routing a theorem to a one-batch re-
  derivation.
- A flagged constant inconsistency can be a rescaling. THEORY-238's proof
  applies Lemma 3 at λ/2, so "λ/n < 1.36" in the proof and "λ/n < 0.68" in
  the lemma agree. Check the argument the lemma is applied at before
  calling the constants wrong.
- Check whether a promote_when was met by sources added later.
  THEORY-197's promote_when asked for a second derivation, and versions 2
  and 3 had already added two sources (LIT-887, LIT-891) that give it.
  Neither version note said the condition was met.
- THEORY-266's promotion rests on Theorem 4 of LIT-233, which is
  THEORY-263's framework and was reviewed elsewhere in this round. If that
  review finds a defect in Theorem 4's proof, revisit THEORY-266. #230
  also trims THEORY-266's and THEORY-238's names from THEORY-263's
  inactive-ok directives, so expect a directive-line conflict if a
  THEORY-263 PR touches the same lines.
- Numerical side conditions are worth one script. Lemma 3's second
  inequality is stated by the paper for x < 1.3, but the lemma needs it to
  1.36. It holds there, by 0.0025.
- THEORY-270 should be requeued for a dedicated re-derivation of LIT-941
  App. C, the common-nonsense upper and lower bounds. Once that is done,
  narrow the title to the stylised models and promote, moving the
  promote_when to a QUESTION.

## 2026-10-19 — lint trap: codes in titles

- Never put a bare code in a `title:`. `luria repair` links it in the body
  heading but not in the front matter, so `title:` and the heading
  disagree and lint fails (#230: THEORY-278, two new QUESTIONs). Name the
  source by its authors instead.

## 2026-10-19 — batch 039 (wave 3, triage-006 control)

- Triage-006 control: the formal flag went 1 of 5. Only the score-3 entry
  (THEORY-205) is formal. All four score-2 entries are measurements or
  arguments, and so were the four labelled false flags. The 'relation'
  signal fired on definitions and estimator formulas. Raise the threshold
  to 3, or require 'relation' together with 'derived' or 'cites'.
- Batch 020's title sort got 5 of 5 again. Measurements flagged formal
  still promote under v3 (THEORY-275, -365), so the score-2 band is worth
  reviewing as v3 work, not as re-derivation work.
- IB titles saying "first transition": the linear-stability point is β =
  1/ρ_m², the squared top singular value of the normalised channel. The
  point where the trivial encoder stops being optimal is 1/s*, the KL
  contraction coefficient, and s* ≥ ρ_m², so that point can come much
  earlier. They coincide in the symmetric Ising check (s*/ρ² = 0.999999)
  and differ 27-fold on a skewed 3-state chain. Name the bifurcation.
- The philosophical-title penalty's word list missed THEORY-162 ("is part
  of its meaning"). Thesis-shaped titles about what meaning, content or
  understanding "is" should count.
- Checking a NOTE's quotations against the source's extracted text
  (THEORY-365) is quick when the arXiv PDF is reachable, and it settles
  batch 018's 'title rests only on results the text reports' directly.

## 2026-10-19 — round 036-041 tally

- Triage-006's formal route went 12 of 15 on entries 1-15 (batches
  036-038), against 1 of 5 for its control (batch 039), where the one hit
  was the only score-3 entry. Two control misses still promoted as
  measurements under ADR-047 v3. Raise the formal threshold to 3, or
  require `relation` with `derived` or `cites`; send score-2 entries to a
  v3 review.
- Batch 020's sort by what the title asserts got all five control entries
  right again.
- Wave 5 (batches 040-041): the six requeued arguments moved none of their
  wave-3 verdicts except THEORY-073, which has a narrowing path that is
  the owner's call. Before requeuing an argument, check git log for a
  change to its promote_when, premises or rival.
- THEORY-080: the exact half is the record's own synthesis; file it as a
  demonstrated CLAIM (ADR-032) rather than promoting the THEORY.

## 2026-10-19 — batch 046 (follow-ups)

- A proof written the day before can contradict its own definition.
  CLAIM-265's steps 2 and 4 applied maps to both descriptions while the
  definition maps one onto the other. Recheck a fresh proof against its
  stated definitions, not only its conclusion.
- Stochastic maps are the class that makes "every pair is compatible" true
  on a single context (the constant kernel); deterministic maps do not.
  Use them for a vacuous-class example.
- A record-own result split from a THEORY can be filed Active at once when
  its proof is self-contained (CLAIM-370, CLAIM-384); its decision
  file is its review.
- THEORY-162 joins THEORY-485 and THEORY-167 as entries whose next step is
  a reading task, not a review. Track reading tasks separately from the
  requeue list.

## 2026-10-19 — batch 042 (wave 3, triage-006 formal 16-20)

- Triage-006's formal_route 16–20 went 3 of 5 to promotion, with every
  title in the band re-deriving; the two misses are a report title
  (THEORY-344, the owner's open question) and the record's own synthesis
  (THEORY-019, the THEORY-080 pattern). Entries 1–20 now stand at 15 of
  20.
- A title that reports "is stated" with the proof elsewhere (THEORY-387)
  is a theorem in waiting: if the record can re-derive the stated result,
  narrow the title to assert it for the case re-derived and move the rest
  to a QUESTION, rather than holding it as a report.
- NOTE-763 misreads the dual radii of Calo et al. as (1−γ)/6 and (1−γ)/2;
  they are 6/(1−γ) and 2/(1−γ). Fractions extracted by pdftotext -layout
  lose their bar; check a radius or step size against the lemma that uses
  it before transcribing it.
- THEORY-019 joins THEORY-080: two derived results filed as THEORYs that
  the record assembled itself. Both corrections can go in one PR filing
  two demonstrated CLAIMs.

## 2026-10-19 — batch 045 (wave 3, triage-006 score-2 band)

- The score-2 band went 5 of 5 under the batch 020 sort (8 of 10 with
  batch 039). Queue the remaining 44 score-2 entries for wave 3 in batches
  of five; do not re-derive by default, sort by title.
- "Least total X over models" versus "sum of least X per part": the two
  agree only when one model reaches every part's minimum at once. In
  Contextuality-by-Default that is noncontextuality (THEORY-177). Check
  any title that sums per-part minima.
- When a title says a quantity "equals" another over a protocol, check
  whether the source's identity is per step and the protocol result a
  bound (THEORY-026).
- When a kernel result holds because two kernels are proportional, the
  proportionality is the theorem; state its setting (THEORY-294: one-
  dimensional, zero bias, classes split by the origin).
- A cheap simulation can stand beside an ADR-047 v3 promotion:
  THEORY-253's two-task and rotated-quadratic results reproduced in
  seconds.

## 2026-10-19 — batch 044 (wave 3, score-3 and re-derivations)

- Triage-006's score-3 band went 2 of 3 (318, 585), and the miss (083) is
  the false-flag kind batch 037 named: end-state theorems quoted in the
  body of an empirical claim. Its formal route is now exhausted; the
  score-2 band should go to v3 review, as batch 039 advised.
- A re-derivation can find the title wrong as well as unproved. In
  THEORY-585 the source asserts the failure and the record had hedged it;
  proving it showed the failure set is decided by a context's projections
  (support on the first factor), not by whether the context factorises, so
  the "only on V₁⊗ℂ1" clause was false (Bell-basis contexts agree).
  Correct the title to what was proved, then promote.
- Source proofs carry small errors worth recording in the decision: Lin et
  al.'s Theorem 6 allows α ≠ 0 where its proof gives α > 0, and their
  Theorem 10's probability is not derived; Goldwasser et al.'s App. C.1
  computes τ(A_i) as if A_i ⊆ T. None changed a bound the record keeps,
  but each changes what may be quoted.
- The split pattern (ADR-040, THEORY-109) recurs for empirical conjectures
  that cite toy-model theorems: THEORY-110 now, and the false flags batch
  037 named. Check the cited theorems' proofs once, then split, rather
  than re-reviewing the conjecture.
- Queue: THEORY-083 requeued after a reading task (Figures 2–7 of
  arXiv:2008.08186 into NOTE-476). THEORY-270 and THEORY-110 leave the
  requeue list.

## 2026-10-19 — batch 043 (wave 3, triage-006 score-3)

- Triage-006's formal flag went 5 of 5 on the score-3 entries after the
  top 20. Together with batches 036–038 that is 17 of 20 at score 3 or
  more, against 1 of 5 for the score-2 control (batch 039).
- A source that asserts a sufficiency theorem "by a similar proof" can
  still be settled by re-derivation in one batch when the necessity proof
  already computes the boundary condition: at equality the condition
  becomes tangency (THEORY-189).
- "Tight only for X" titles: test the claim at p = q and at other trivial
  pairs; the intended reading is usually "for every pair" (THEORY-313).
- "Tight" applied to a bound family that includes InfoNCE: InfoNCE's
  supremum is at most log K and generally below I, so say "attains its
  supremum" and name the members that then equal I (THEORY-237).
- When a negative clause ("does not make the minimizer X") has a
  promote_when that accepts a finite counterexample, a numerical
  counterexample with many restarts settles it at medium confidence
  (THEORY-305). Record the generating recipe in the decision file, since
  scratch scripts do not survive the session.
- Check every constant a body quotes against the source text: THEORY-189's
  K ≤ 2ε/(1 − ε²) misread Eq. 25, which gives K ≤ ε/(1 − ε²).

## 2026-10-19 — round 042-046 tally

- Triage-006's formal route is exhausted: 17 of 20 at score 3 or more
  promoted (batches 036-038, 042-044), against 1 of 5 for the score-2
  control. But the score-2 band yields under ADR-047 v3 review: batch 045
  went 5 of 5, so 8 of 10 across both samples. Only 3 of the 9 checked
  score-2 entries were formal. Work through the remaining 44 by title.
- Misses on the formal route fall into four recognisable kinds: a report
  title (THEORY-344), the record's own synthesis (THEORY-019, -080, which
  go to a demonstrated CLAIM under ADR-032), a theorem read only in outline
  (THEORY-270, now re-derived), and an empirical conjecture citing toy-model
  theorems (THEORY-083, -110; split the theorems out once checked).
- A re-derivation can show a title false, not just unproved (THEORY-585,
  -313, -237). Correct the title to what was proved, then promote.
- Recheck a fresh proof against its own definitions: CLAIM-265's
  day-old proof contradicted its definition and was repaired in #237.
- Put the recipe for a numerical counterexample in the decision file;
  scratch scripts do not survive the session.

## 2026-10-19 — batch 051 (wave 3, score-2 band)

- The score-2 band went 4 of 5 here. With batches 039 and 045 that is 12
  of 15. Three of the five are formal in fact, so 6 of 14 checked score-2
  entries are formal. Sorting by title kept predicting every outcome.
- A possibility title ("an intervention can reproduce X without Y") is
  settled by an existence construction. The promote_when's request to show
  the measured cases are instances is wider than the title and moves to a
  QUESTION (THEORY-282).
- A promote_when asking for "a second reader's line-by-line check" is met
  by an ADR-047 v2 re-derivation in the decision file. When the re-
  derivation also shows the named counterexample cannot exist, no QUESTION
  is needed (THEORY-284, -281).
- For an "only when" over deterministic maps, check which hypotheses the
  necessity direction actually uses. THEORY-281's needs neither disjoint
  groups nor strict concavity; only sufficiency needs disjointness.
- In a single-study measurement, drop any clause the source states in
  words with no number (THEORY-272's "unless old ones are forgotten") and
  keep the measured one (no stored pattern stable at N = 100, n = 500).
- THEORY-302: requeue to wave 5.

## 2026-10-19 — batch 052 (follow-ups)

- A reading task can be done inside a batch when the source is on arXiv:
  render the figure pages (pdftoppm) and read the plots, not the extracted
  text, which scrambles multi-panel figures.
- Reading the plots changed the verdict's shape, not just its confidence:
  the captions said every measure "decreases" and the NOTE said "monotone
  across all 21 cells"; the plots show non-monotone cells and a partial
  collapse on ImageNet. A captions-only reading of a grid of curves tends
  to overstate both completeness and monotonicity.
- Check whether large drops in a training curve coincide with learning-
  rate cuts before crediting them to the phase the paper names.
- The THEORY-080 pattern applied cleanly a second time (THEORY-019): the
  split CLAIM carries the proof and the THEORY keeps the reading and its
  promote_when. Neither THEORY promotes on the split, since what remains
  asks for a held source.
- THEORY-019 supports CLAIM-193 and CLAIM-269. Whether they should rest on
  the new claim instead is for their next review.

## 2026-10-20 — tmp codes in the ledger

- A decision file for a CLAIM filed in a batch is named by its tmp code
  (CLAIM-tmprruzz). docs-generate concretizes the code in record/ but not
  in record/promotion-audit, so after the filing PR merges, rename the
  decision file and every ledger reference to the permanent code
  (CLAIM-tmprruzz became CLAIM-384).

## 2026-10-19 — batch 048 (wave 3, score-2 band)

- The score-2 band went 4 of 5 (12 of 15 with batches 039 and 045). Keep
  working through the remaining 34 by title.
- "Approximately closed" or "to first order" in a theorem title: bound the
  error, then check whether it vanishes uniformly or only in one regime,
  and narrow the title to the regime (THEORY-190).
- A promote_when that asks for a limit proof of a model's signatures,
  where the record's own derivation is the approximation being set aside,
  is a reading task, not a re-derivation (THEORY-188: the rigorous random-
  hyperbolic-graph literature).
- "Does not by itself favour X over Y" is settled by constructing a Y
  model that meets the regularity (THEORY-166's classical model with order
  events).
- A mechanism verb in a measurement title ("interpret by inverting")
  narrows to "matched" when the evidence is a fit of condition means with
  no rival fitted (THEORY-172).

## 2026-10-19 — batch 049 (wave 3, score-2 band)

- The score-2 band went 4 of 5 here, 12 of 15 across batches 039, 045 and
  049. Keep working through it by title.
- "A symmetry implies a mirror" depends on the group containing an
  involution with a nontrivial fixed subspace. Positive rescaling (ReLU's
  λ > 0) contains none, so check the sign before carrying a sparsity
  corollary (THEORY-213).
- A weight-decay threshold for "every minimum on the symmetric subspace"
  needs only a lower bound on the loss's Hessian, not smoothness: the even
  function's gradient vanishes at zero, so f(z) − f(0) ≥ −(c/2)‖z‖²
  (THEORY-213).
- A "can" thesis about an information measure promotes by construction
  once the title names the measure and the intervention distribution; its
  interpretive reading moves to a QUESTION (THEORY-222).
- Recomputing a quoted exponent from the paper's own equations is a cheap
  check that can close the theorem route (THEORY-203's ν ≈ 1.89 against a
  quoted 1.78).
- Requeue THEORY-203 if THEORY-199 is promoted and the ν gap is explained
  or a second parameter set is measured.

## 2026-10-19 — batch 047 (wave 3, score-2 band)

- Score-2 band: 4 of 5 here, 12 of 15 across batches 039, 045 and 047. Two
  of the four (THEORY-030, -133) were formal in fact and both titles were
  false as written; the other two were measurements narrowed under ADR-047
  v3. Keep sorting by title.
- Landauer-type titles: with reversible joint dynamics of memory and
  environment, the floor is on the logical entropy lost, H(X | f(X)), so
  many-to-one maps on known data have no floor either. "Learning has no
  minimum cost" is false in Goldt and Seifert's own framework; what has no
  floor is the heat (THEORY-030).
- Counterfactual "exactly when" titles: check that the precondition (the
  higher-level property is a difference-maker) is in the title, and
  whether the condition is "would" (all nearest worlds) or "might" (some)
  (THEORY-133).
- "Suitably arranged" in a determination result usually means a
  connectivity condition; state it (THEORY-117: the seen-pair graph must
  connect every value). A span condition needed for a classifier is not
  needed for determining the embeddings.
- THEORY-085's CFAC - KFAC identity is the record's own one-line algebra
  (class-weighted); file it as a demonstrated CLAIM with THEORY-019 in the
  next follow-up batch.

## 2026-10-19 — batch 050 (wave 3, score-2 band)

- The score-2 band went 5 of 5 (13 of 15 across batches 039, 045 and 050).
  Keep working through it by title.
- When a title says two quantities agree "only to within" some term, check
  whether the source shows the term is reached or only bounds the gap.
  THEORY-244's entropy gap is reached (a point mass); THEORY-259's alpha
  is only an upper bound, and the conditional form of domination replaces
  it by the likelihood family's complexity, constant over H.
- A promote_when that names a simulation as sufficient can often be met in
  the review itself (THEORY-261: Kanerva's basic SDM at up to 200,000
  locations, about 20 s per run). Record the design, seeds and results in
  the decision file; the scripts do not survive the session.
- For a theorem over "some labelling", look for a convexity argument that
  covers every labelling at once before following a case analysis
  (THEORY-271: a nonnegative affine function vanishing on half the cube
  vanishes on a facet).
- Jaeckel's SDM fidelity formula is slightly conservative at small p,
  because it treats the target's own activation count as additive noise,
  and slightly optimistic at large p, because Hamming-ball overlaps vary
  more than Poisson. Its optimum (2MT)^(-1/3) still sits between the
  measured and predicted optima.
