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

## Next

- Registered Mixon, Parshall and Pi as LIT-tmpxyq0h (Deferred).
- Copy results in, analyze, write README.
- File CASE, CLAIM, dated notes, changelog.
