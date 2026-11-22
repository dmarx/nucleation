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

## Next

- Step 1 check.
