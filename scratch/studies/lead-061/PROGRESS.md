# LEAD-061 progress

- Lead: LEAD-061 (advances QUESTION-184, narrower matter)
- Branch: claude/lead-061-golub-jackson
- Task: reread Golub & Jackson (2010; LIT-999, read in NOTE-840) Proposition 2
  and Theorem 3 with the definitions of influence and wisdom, and settle whether
  "largest influence weight -> 0 iff wise" holds for societies with several
  closed groups (the audit's sketch: n/k groups of size k = sqrt(log n)).
  Check numerically. File dated notes on NOTE-840, LIT-999, QUESTION-184,
  THEORY-321 and LEAD-061; a CLAIM if warranted.
- Step 1 check: not already held. THEORY-321 v2 and the audit decision leave
  the several-closed-groups case unchecked; no branch or entry answers it.

## Done

- Copy located: bengolub.net/wp-content/uploads/2020/05/naivelearning-1.pdf,
  HTTP 200, 38 pages, the AEJ:Micro published version (same copy as NOTE-840).
  Read 2026-11-22: Defs 1-3 (pp. 119-123), Lemma 1 + fn 14, Prop 2 (p. 124),
  closed groups, Def 7, Thms 2-3 (pp. 136-137), proofs of Thm 3, Lemma 1,
  Prop 2 (pp. 139-141).
- Finding (to be checked numerically): Theorem 3 normalizes s to sum to 1 on
  EACH minimal closed group; Definition 3 takes plim of the max over all agents
  ("jointly"). The proof of Prop 2's "if" shows plim p_{i_n} = mu along every
  deterministic sequence i_n, which does not give the max. The audit's
  counterexample stands: m = n/k groups of size k ~ sqrt(log n), equal weights,
  Bernoulli(1/2) signals: s_1 = 1/k -> 0, but P(some group all ones) =
  1 - (1 - 2^-k)^m -> 1, so not wise. "Only if" holds. "If" holds with a
  bounded number of closed groups (union bound), or under a Hoeffding-sum
  condition sum_B exp(-2 eps^2 / ||s_B||^2) -> 0.

## Next

- Script + pytest: exact probabilities for the counterexample; DeGroot
  iteration on a small several-group T to confirm Theorem 3's normalization;
  Monte Carlo of max deviation.
- File notes: NOTE-840, LIT-999, QUESTION-184, THEORY-321, LEAD-061; CLAIM.
