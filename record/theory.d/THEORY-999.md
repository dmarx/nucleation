---
number: 999
status: Active
formerly:
- THEORY-tmppc921
title: 'In the finite beta–Bernoulli feature model with prevalences Beta(α/K, 1), the expected number of occupied features among N objects is K(1 − (α/K)B(α/K, N + 1)), strictly below the Indian buffet process''s αH_N for every finite K and tending to it as K grows, and each object holds Kα/(K + α) features on average rather than α'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1172. The finite model, its bound (11) and
    the limit αH_N are the paper's. The finite-K count of occupied
    features, the inequality and the numbers are the record's, re-derived
    below step by step and checked numerically, which meets the condition
    for Active under ADR-047 v2.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: the stick-breaking construction this account
    compares against was registered and read on 2026-10-27 (LIT-tmpfhqac);
    its 8.97 is confirmed exactly (THEORY-tmphvhg6) and the reason given for
    its closeness qualified. Title and status unchanged.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
source:
- LIT-1556
summary: >-
  Griffiths and Ghahramani (2011), [LIT-1556](../literature.d/LIT-1556.md), read in [NOTE-1172](../notes.d/NOTE-1172.md),
  derive the IBP as the K → ∞ limit of πk ~ Beta(α/K, 1), zik ~
  Bernoulli(πk), and give K+ ~ Poisson(αH_N) for the limit only. At finite
  K the count falls short, by 27% at N = 12, α = 3, K = 16. It says
  nothing about stick-breaking truncations, which approach the IBP much
  faster.
---

# THEORY-999: In the finite beta–Bernoulli feature model with prevalences Beta(α/K, 1), the expected number of occupied features among N objects is K(1 − (α/K)B(α/K, N + 1)), strictly below the Indian buffet process's αH_N for every finite K and tending to it as K grows, and each object holds Kα/(K + α) features on average rather than α

## Source

Griffiths and Ghahramani (2011), *JMLR* 12: 1185–1224, [LIT-1556](../literature.d/LIT-1556.md), read
in full in [NOTE-1172](../notes.d/NOTE-1172.md). The finite model is their (9), the per-feature
expectation their (11), and K+ ~ Poisson(αH_N) their §4.6, stated for the
limit. The finite-K count and the inequality below are the record's.

## What was actually shown

The model: for k = 1 … K, πk ~ Beta(α/K, 1) independently, and
zik | πk ~ Bernoulli(πk) for i = 1 … N.

**Per object.** E[zik] = E[πk] = (α/K)/(1 + α/K), so an object's expected
number of features is K(α/K)/(1 + α/K) = Kα/(K + α). The paper gives the
total, Nα/(1 + α/K), and its bound Nα (11).

**Occupied features.** Column k is occupied unless all N entries are 0:

P(mk > 0) = 1 − E[(1 − πk)^N]
= 1 − (α/K)∫₀¹ π^{α/K − 1}(1 − π)^N dπ = 1 − (α/K)B(α/K, N + 1).

The columns are identically distributed, so
E[K+] = K(1 − (α/K)B(α/K, N + 1)).

**Below αH_N.** Write ε = α/K. Then
εB(ε, N + 1) = Γ(1 + ε)Γ(N + 1)/Γ(N + 1 + ε) = ∏_{j=1}^{N} j/(j + ε)
= ∏_j (1 − xj), with xj = ε/(j + ε). By the Weierstrass product inequality
∏(1 − xj) ≥ 1 − Σ xj, so

E[K+] = K(1 − ∏(1 − xj)) ≤ K Σ_j ε/(j + ε) < K Σ_j ε/j = αH_N,

strictly for every finite K. As K → ∞, ∏ j/(j + ε) = 1 − εH_N + O(ε²), so
E[K+] → αH_N, the paper's limit.

**Numbers** (re-computed 2026-10-26, exact formula). N = 12, α = 3:
αH₁₂ = 9.310. E[K+] is 6.830 at K = 16, 8.381 at K = 50 and 9.259 at
K = 1000. Per object, Kα/(K + α) is 2.53 at K = 16 against α = 3. Under
the IBP itself P(K+ > 16) = 0.0149. For comparison, a stick-breaking
truncation at 16 (Teh et al. 2007, the construction [LIT-1548](../literature.d/LIT-1548.md) uses),
with vj ~ Beta(α, 1) and bk = ∏_{j≤k} vj, gives 8.97 occupied features
(Monte Carlo, 200,000 draws) and Σ_{k≤16}(α/(1 + α))^k = 2.97 features
per object.

## What this does not say

- That the finite model is a poor prior. It is a valid exchangeable prior
  in its own right; it is not the IBP with α at that K, and the IBP's
  quantities should not be quoted for it.
- That truncation must be large. A stick-breaking truncation at the same
  K is close to the IBP, because it keeps the largest prevalences and
  drops only the tail; the finite beta–Bernoulli model spreads α over K
  exchangeable columns instead.
- Anything about the posterior. The shortfall is in the prior; with data
  that need more features than the prior expects, the posterior can still
  occupy them, at a prior cost.

## Note of 2026-10-27: the stick-breaking comparison, at its source

The Numbers above compare the finite model with a stick-breaking
truncation at 16, cited as Teh et al. 2007 and computed by Monte Carlo.
That paper was registered and read on 2026-10-27, at the owner's request ("file the next readings"), as
[LIT-tmpfhqac](../literature.d/LIT-tmpfhqac.md) ([NOTE-tmptxvho](../notes.d/NOTE-tmptxvho.md)). From the construction the expected count
has a closed form, and at K = 16, N = 12 and α = 3 it is 8.974, with
2.97 features per object ([THEORY-tmphvhg6](THEORY-tmphvhg6.md)), which confirms both figures.

"What this does not say" explains the truncation's closeness by its
keeping "the largest prevalences and drop[ping] only the tail". The tail
is not empty: in 24% of draws at least one feature beyond the sixteenth
stick is occupied, and their expected number, 0.34, is the whole gap
9.31 − 8.97. The comparison stands. The IBP's original paper, [LIT-tmp3u0k8](../literature.d/LIT-tmp3u0k8.md),
read the same day, states αH_N for the limit only, as the review does
([THEORY-tmpo1cju](THEORY-tmpo1cju.md)). The title and status are unchanged.
