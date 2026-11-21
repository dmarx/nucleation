---
status: Read
paper: LIT-tmpl98s1
title: 'Bovier, Eckhoff, Gayrard and Klein — Metastability and low lying spectra'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv math/0007160v1 (26
    Jul 2000): §§1–3 and §5 in full; §§4 and 6 by their statements; the
    proofs of Lemmas 4.1–4.5, 5.5–5.6, Proposition 5.7 and Lemmas 6.3–6.5
    skipped. Running notes on the branch
    claude/readers/metastability-bovier (ADR-108). Quotations the filing
    leans on rechecked by the filer by script against the downloaded text.
date: '2026-11-21'
summary: >-
  For reversible chains with generically separated metastable points:
  minus log capacity is an ultrametric up to ln 3; mean exit times are
  valley mass over capacity; each metastable point owns one low-lying
  eigenvalue with an eigenvector near its valley's indicator. Large-N,
  generic, sharp to (1 + o(1)). A large-N limit with escape-probability
  definitions, not the record's small-noise ε^U form.
---
<!-- inactive-ok-file: ADR-108 THEORY-1366 THEORY-1370 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmp9lm3d CLAIM-tmpxi826 CLAIM-tmpy75jv — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmpjot4l: Bovier, Eckhoff, Gayrard and Klein — Metastability and low lying spectra

## Contribution

A potential-theoretic definition of metastability by escape probabilities, and sharp (1 + o(1)) results where Freidlin and Wentzell give logarithmic ones: exit times by capacities, the low-lying spectrum, exponential exit laws, and an almost-ultrametric on the metastable points.

## Key results

1. **Metastable points** (Definition 1.1): every state reaches the set with probability at least b_N before returning; between metastable points escape is at most a_N⁻¹, much smaller.
2. **Genericity** (Definition 1.2): relevant times differ by factors going to infinity.
3. **Exit times and spectrum** (Theorem 1.3): mean exit time is the valley's stationary mass over a capacity; each metastable point owns a simple eigenvalue λ = (1 + o(1))/E t; exit times are nearly exponential.
4. **The almost-ultrametric** (Corollary 2.6, (2.27)): e = −ln of capacity "furnishes an 'almost' ultra-metric", with slack ln 3, and "e(x,y) are essentially N times the heights of the essential saddles"; "The appearance of a natural ultra-metric structure on the set of metastable states under our minimal assumptions is interesting in itself." Lemma 2.5, behind it, holds for any points.
5. **Barriers relative to wells** (§5): ln T_{x,J} = e(x, J) − f(x), f = −ln Q_N(x).
6. **Degenerate cases** (remark after Theorem 1.3): where times "differ only by constant factors", the spectrum "will have to be computed specially through a finite dimensional, non-trivial diagonalisation problem".
7. **Electrical networks** (pp. 6–7): the escape probabilities satisfy a variational principle; "the same variational representation is at the basis of the 'electric network' method".

## Assumptions and concepts

Reversible, discrete-time, finite state space growing with N; metastability and genericity conditions; results asymptotic in N except Lemma 2.5, Corollary 2.6 and Theorem 3.1. Concepts: metastable set, valley, capacity, almost-ultrametric, effective depth, exclusion sets, Dirichlet operator.

## Bearing on the record

- **[CLAIM-tmpxi826](../claims.d/CLAIM-tmpxi826.md)** (supports and generalizes, and corrects one sentence). The paper's almost-ultrametric is the general reversible counterpart of the claim's bound, with a slack (ln 3) independent of N, n and E, and barriers measured from wells as the claim guessed. The claim's sentence that the record "holds neither" Freidlin–Wentzell nor metastability theory was wrong: [LIT-2035](../literature.d/LIT-2035.md) (Freidlin and Wentzell, [THEORY-1366](../theory.d/THEORY-1366.md)) and [LIT-2037](../literature.d/LIT-2037.md) (Berglund, [THEORY-1370](../theory.d/THEORY-1370.md)) are held. The reader also observed that the logarithm of any metric satisfies the ultrametric inequality up to ln 2 (d(x,z) ≤ 2·max(d(x,y), d(y,z))), so bounded hyperbolicity of a log commute-time geometry holds for every chain; what the rates add is which ultrametric and how far apart its levels are. The claim is restated (version 3).
- **[CLAIM-581](../claims.d/CLAIM-581.md)** (supports by analogy): the capacity ultrametric is the probabilistic counterpart of the peak-cost threshold.
- **[CLAIM-tmp9lm3d](../claims.d/CLAIM-tmp9lm3d.md)** (qualifies): genericity excludes near-crossings; the degenerate-case remark is the paper's form of levels blurring there.
- **[CLAIM-tmpy75jv](../claims.d/CLAIM-tmpy75jv.md)** (supports and qualifies): one eigenvalue per metastable point with eigenvector near the valley indicator is the spectral form of a closing aggregate; the ratio that matters combines rates, masses and the shape of the space.
- **[QUESTION-tmpv6fxp](../questions.d/QUESTION-tmpv6fxp.md)** (bears): separation here can come from geometry and entropy (the factor N^{−(d−2)/2}), not rates alone; the question is restated.
- **[QUESTION-tmp4ma9f](../questions.d/QUESTION-tmp4ma9f.md)** (bears): the ultrametric slack is ln 3 independent of n and E, supporting the suspicion that the proven factor's size dependence is an artefact.

## Limitations

Asymptotic and generic beyond §2, so it cannot ground claims about finite rate ratios; commute time not treated; degenerate cases excluded; no tree drawn; the proofs of §§4–6 not checked.
