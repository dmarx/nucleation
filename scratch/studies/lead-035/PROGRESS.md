# PROGRESS: LEAD-035

- Lead: LEAD-035 (check the SNR singular values against the predicted
  quarter-power law for neural collapse; advances QUESTION-051).
- Branch: claude/lead-035-snr-singular (cut from origin/staging).
- Skill: .claude/skills/run-lead/SKILL.md.

## Task as understood

1. Check the target is not already held (step 1 of the skill).
2. Train small networks in numpy under MSE, with no imposed
   re-whitening, track the singular values omega_j of
   Sigma_W^(-1/2) M~ (the SNR matrix of NOTE-783), and compare them with
   (4t/N)^(1/4) (Han, Papyan and Donoho, LIT-974, Corollary 1).
3. Register the work NOTE-772 names (lawful copies only).
4. File a CASE (executed-study), a CLAIM if warranted, dated notes on the
   entries advanced (QUESTION-051, QUESTION-181, THEORY-797) and on
   LEAD-035, and a changelog fragment.

## Done

- Step 1: not held. No CASE, CLAIM or LEAD measures the SNR singular
  values in trained networks; the target sits open in QUESTION-181 and
  THEORY-797's promote_when. The backlog audit (curation 2026-11-19) only
  lists the lead.
- snr.py (measures, Han et al.'s prediction, unconstrained-features flows,
  numpy MLP with optional full-batch BN), test_snr.py (10 pass). The
  projected step reproduces Lemma 5's rate, which fixes the time unit:
  t = learning rate x steps, gradients of the sample-averaged loss.
- Quick trial (seed 0, 1/10 length) done in scratchpad: renormalized flow
  matches (4t/N)^(1/4); every un-renormalized model grows omega far faster
  (log-log slopes 2-7), with NC1 stalling while omega diverges.
- Full runs launched 2026-11-22 in scratchpad/lead-035 (three processes,
  PIDs in *.pid): ufm (9 items), mlp2 (6), mlp3bn (6).

- All 21 planned items done 2026-11-22 (results-*.jsonl, summary.json):
  renorm control matches Proposition 2's exact solution to 4e-5 and the
  slope is 0.256; UFM plain and joint GD grow omega exponentially and
  spread it (max/min to 4-175), NC1 stalls 0.05-0.11; MLPs without weight
  decay grow omega with log-log slopes 2.4-3.9, max/min 2.4-15, NC1 stalls
  0.22-0.42; MLP2 with weight decay grows, stalls (t ~ 500-4000) while
  NC1 falls, then regrows (last-decade slopes 0.11-0.30, an average over
  stall and regrowth); MLP3-BN with weight decay rises to ~1e4 then
  collapses by 10x near t ~ 5000 (loss spike), slopes negative.
- mlp3bn weight-decay seeds s1, s2 run in parallel processes
  (results-mlp3bn-b/-c.jsonl); main mlp3bn process stopped by PID after s0.
- One long run (mlp2, wd 5e-4, seed 0, 1e6 steps) launched as item
  long-mlp2-wd0.0005, results-long.jsonl.
- Coordinator asked to resume after a usage limit: pulled, nothing lost,
  runs alive; continuing.

## Choices

- Models: three unconstrained-features dynamics (Han's renormalized flow
  as a control; plain gradient of L_LS without re-whitening, isolating
  A3; ordinary joint GD on W, b, H) and two small networks (ReLU MLP of
  two hidden layers; three hidden layers with full-batch BN), MSE,
  weight decay 0 and 5e-4, three seeds. Data: four-class Gaussian
  mixture in R^20, 50 per class. numpy only, full-batch GD.
- "The work NOTE-772 names": NOTE-772 names many works; the one that
  bears on whether gradient descent without renormalization follows the
  omega dynamics is Mixon, Parshall and Pi (2020, arXiv:2011.11619; authors checked on
  the arXiv API), squared loss, gradient
  flow on unconstrained features. Register that.

- Long run: settles, omega 198-386 from t ~ 1.3e4 to 5e4, max/min 1.6-1.9.
- Filed: CASE-tmpjn6f4, CLAIM-tmpcpr7t, LIT-tmpxyq0h; dated notes on
  LEAD-035, QUESTION-181, THEORY-797, QUESTION-051; changelog
  record/changelog.d/lead-035.md. Link targets in added text turned into
  bare codes (CLAUDE.md: never hand-write a link target).

## Next

- Nothing on the branch. The coordinator opens the pull request; CI
  repairs links and lints. Owner's calls: THEORY-797's status, adopting
  CLAIM-tmpcpr7t, LEAD-035's status.
