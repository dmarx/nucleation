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
