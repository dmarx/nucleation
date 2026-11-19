---
status: Read
paper: LIT-tmprrdom
title: 'Lohmiller and Slotine 1998 — On Contraction Analysis for Non-linear Systems'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Located and read: https://web.mit.edu/nsl/www/preprints/contraction.pdf
    (HTTP 200, application/pdf, 251 KB, 27 pages), on the MIT Nonlinear
    Systems Laboratory (Slotine's research group) preprint page. The copy's
    own footer reads "NSL-961001, October, 1996. Revised, August, 1997.
    Final version, December 1997": the authors' final manuscript of the
    Automatica 34(6) paper (DOI 10.1016/S0005-1098(98)00019-3). Kind of
    copy: author's manuscript on a research-group page; lawful (step 5,
    ADR-074). It was not compared with the published Automatica text. Also
    seen, not used: a search result pointing to the same PDF through a
    library proxy (web-mit-edu.ezproxyberklee.flo.org/...), which is not a
    route to use; the publisher's page (ScienceDirect) was not tried, since
    a lawful copy was in hand. Date: 2026-11-19. Nothing stopped the fetch.
    Text: pdftotext -layout to dl/text.txt; equations survive partly
    (fraction bars and sub/superscripts are split across lines). Read:
    abstract, §1, §2 (Definition 1, Theorem 1, Examples 2.1-2.2), §3 entire
    (3.1-3.9: general metric, generalized eigenvalue analysis, metric
    analysis, Definition 2, Theorem 2, the converse theorem, the note on
    Krasovskii, the eight linear properties, parallel / feedback /
    hierarchical combinations with Examples 3.2-3.5, the additional
    remarks), §4.1 PD observers, §4.2 constrained systems, §5 discrete time
    (Definition 3, Theorem 3), §6 conclusions. Skimmed: §4.3 (LTV
    controllers, observers, separation principle, nonlinear controllers and
    observers): headings and conclusions only. Finding about the LIT's
    characterization: the paper does NOT contain "partial contraction toward
    invariant manifolds". Partial contraction is Wang and Slotine (2005),
    which NOTE-1020 cites separately and which the record does not hold.
    This paper's nearest statements are §3.9's remarks on positive semi-
    definite metrics (convergence of the components of δx on a subspace) and
    on lower-dimensional differential coordinates. RECHECK (record/ searched
    for: Lohmiller, contraction analysis, partial contraction, Krasovskii,
    Slotine, virtual displacement): - Not held as a work. Verdict stands.
    Krasovskii has no hit. - Held entries: LIT-1295 / NOTE-1020 / THEORY-773
    (Del Vecchio and Slotine 2013), whose Lemma 1 cites this paper's
    differential inequality; LIT-1292 / NOTE-1025 / THEORY-771 (Bousquet and
    Slotine 2015); QUESTION-287 (Answered by THEORY-773), QUESTION-221,
    QUESTION-222 and CLAIM-386 (Slotine hits). - Correction to the source's
    characterization: "partial contraction toward invariant manifolds" is
    Wang and Slotine (2005), cited in NOTE-1020 (Connections) and used there
    (NOTE-1020's Definition 1, partial contraction), but not held as a LIT.
    It is the work A29's selective contraction actually needs; registering
    it is the filer's call. arXiv nlin/0510025 and math-ph/0403027, which a
    web search returned, are Lohmiller and Slotine's later papers (higher-
    order contraction; distributed systems), checked on the arXiv API on
    2026-11-19, not Wang and Slotine.
date: '2026-11-19'
---
<!-- inactive-ok-file: QUESTION-287 — Answered; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-tmpw8xkt — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp2wkbb: Lohmiller and Slotine 1998 — On Contraction Analysis for Non-linear Systems

## Contribution

Lohmiller and Slotine found contraction analysis: stability judged differentially, by whether neighbouring trajectories converge to one another, instead of relative to a known nominal motion or through a Lyapunov function. If the symmetric part of the Jacobian, or of the generalized Jacobian F = (Θ̇ + Θ ∂f/∂x)Θ⁻¹ in a metric M = ΘᵀΘ, is uniformly negative definite on a region, virtual displacements decay exponentially and all trajectories in a ball there converge exponentially to one another; initial conditions are forgotten. They show the condition is also necessary for exponential convergence (a converse theorem), list properties contraction shares with linear systems, and prove closure under parallel, feedback and hierarchical combination, then apply it to observers, constrained systems, LTV systems and discrete time.

## Key results

- §1, the idea: "a system is stable in some region if initial con- ditions or temporary disturbances are somehow “forgotten,” i.e., if the final behavior of the system is independent of the initial conditions" (OCR hyphenation kept) and stability can be analysed differentially, "do nearby trajectories converge to one another?"
- §2, Definition 1 and Theorem 1: a contraction region is one where ∂f/∂x is uniformly negative definite; any trajectory starting in a ball about a given trajectory and staying in a contraction region "remains in that ball and converges exponentially to this trajectory"; globally if the whole space is a contraction region.
- §3.4, Definition 2 and Theorem 2: the same with respect to a uniformly positive definite metric M(x, t) = ΘᵀΘ, the condition being F uniformly negative definite or (∂f/∂x)ᵀM + M ∂f/∂x + Ṁ ≤ −β_M M.
- §3.5, converse: "any exponentially convergent system is contracting with respect to a suitable metric", so "Theorem 2 actually corresponds to a necessary and sufficient condi- tion for exponential convergence of a system".
- §3.7 (iv)-(v): "A convex contraction region contains at most one equilibrium point"; in a globally contracting autonomous system all trajectories converge to a unique equilibrium.
- §3.7 (vii), robustness: for a disturbed flow the distance R between trajectories satisfies Ṙ + |λmax|R ≤ ‖Θd‖ (eq. 15), so trajectories converge exponentially to a ball around the desired one.
- §3.8.2-3.8.3, combinations: a feedback combination with skew-symmetric coupling "is contracting if and only if the separated plants are contracting"; a hierarchical combination with contracting diagonal blocks and bounded off-diagonal block "globally exponentially converges to a single trajectory", which the authors offer as "a general common framework for sliding control concepts, singular perturbations, and triangular systems" (citing Simon 1981).
- §3.9, partial convergence: a uniformly negative trace of F (the divergence) means "any volume element δV shrinks exponentially to zero", "implying convergence to an (n − 1)- dimensional manifold rather than to a single trajectory"; and with a metric only positive semi-definite, F negative definite "implies exponential convergence to zero of the components of δx on the linear subspace spanned by the pi"; also "lower-dimensional coor- dinates can only lead to positive semi-definite metrics M".
- §6: "convergence analysis and limit behavior are in a sense treated separately".

## Assumptions

- Deterministic, smooth (continuously differentiable) dynamics ẋ = f(x, t).
- Uniform bounds: negative definiteness with a constant β > 0 for all x and t ≥ 0 in the region, and a uniformly positive definite metric (except in the §3.9 remarks).
- The ball of Theorems 1-2 must lie in the contraction region at all times; an arbitrary convex region will not do, since "tangential velocities could let trajectories" escape it (the sentence is split by Figure 2 in the copy).

## Concepts

- Virtual displacement δx and virtual dynamics δẋ = (∂f/∂x)δx.
- Contraction, semi-contraction and indifferent regions.
- Differential coordinate change δz = Θδx, metric M = ΘᵀΘ, generalized Jacobian F.
- Converse contraction theorem; Krasovskii's theorem as the constant-metric special case.
- Parallel, feedback and hierarchical combinations of contracting systems.

## Bearing on the record

- [THEORY-773](../theory.d/THEORY-773.md): supports an ingredient. [THEORY-773](../theory.d/THEORY-773.md)'s Lemma 1 for a constant metric, the disturbed-trajectory bound, rests on the differential inequality stated here as §3.7 (vii), eq. (15) ([NOTE-1020](NOTE-1020.md)'s C1 cites it to Lohmiller and Slotine), and §3.8.3's hierarchical combination is the structure of a singularly perturbed system with a contracting fast subsystem, which the authors themselves call a common framework for singular perturbations. The quantitative O(ε) bounds of [THEORY-773](../theory.d/THEORY-773.md) are not here.
- [CLAIM-481](../claims.d/CLAIM-481.md) (the note of 2026-11-19 and A29 on selective contraction): qualifies. The paper's main theorems contract everything: in a contraction region all trajectories converge to one, and a convex contraction region holds at most one equilibrium, so contraction in this sense erases every distinction, not some. Contraction that keeps some distinctions appears only in the §3.9 remarks (convergence of the components on a subspace for a semi-definite metric; volume contraction toward an (n − 1)-dimensional manifold). The LIT's summary credits this paper with partial contraction toward invariant manifolds; that is Wang and Slotine (2005), not held, which [NOTE-1020](NOTE-1020.md) cites separately.
- [CLAIM-tmpw8xkt](../claims.d/CLAIM-tmpw8xkt.md): leaves open; bears on the mechanism half. Full contraction is identification of all states by their limit behaviour, which yields one class, not several. The claim's completion by differentiation (A29 §5, [CLAIM-408](../claims.d/CLAIM-408.md)) is needed precisely because contraction as defined here cannot by itself leave several classes in a convex region.
- [LIT-1292](../literature.d/LIT-1292.md): consistent; Bousquet and Slotine's contracting fast modules and reduced slow system are instances of §3.8.3's hierarchy, with explicit rates.

## Limitations

- Deterministic and smooth only; no noise.
- The converse theorem's metric may become unbounded as t → ∞ (acknowledged in §3.5); the construction is not a practical way to find a metric.
- Partial (subspace or manifold) convergence is treated in bullet remarks, without theorems or examples beyond the statement.
- This reading used the authors' final manuscript (December 1997), not the Automatica text; §4.3 was skimmed.
