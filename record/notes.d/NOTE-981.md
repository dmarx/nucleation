---
number: 981
status: Read
formerly:
- NOTE-tmpnodc1
paper: 'LIT-1258'
title: 'Charvin, Catenacci Volpi and Polani — Exact and soft successive refinement of the IB'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the published PDF (51 pages, CC BY) in the University of Hertfordshire Research Archive, eprint 10690, text extracted with pdftotext. The MDPI and PMC PDFs were refused to this client. Read: the abstract, §1 (conceptualisation, related work, preliminaries with Definitions 1–4), §2 (Definition 5, Propositions 1–5, the numerical results of §2.3), §3 (Definitions 7–9, Propositions 6–7, the numerical results of §3.2 with the σ ratios), §4 (decision problems, Definitions 10–11, Proposition 8; deep learning, Remark 4), §5–§6, and Appendices A (Propositions A1–A2), B.1–B.8 (all proofs, the operational interpretation, the Gaussian semigroup argument, the linear programme and its complexity, the binary proof with Lemmas A2–A4), C.1 and D (Conjectures 1–2). Equations were partly garbled by extraction and were reconstructed from the text. Figures 1–12 and A1–A4 (simplex trajectories, SR patterns, UI landscapes) were read from their captions and the text describing them; their plotted values were not read, and the example distributions on the authors' GitLab were not fetched. Not read: the cited results two proofs rest on (Witsenhausen and Wyner for Lemma A3; Kline and Palmer's semigroup for Proposition 2), and Banerjee, Rauh and Montúfar's unique-information algorithm. The paper's linear-programming test was run on CLAIM-387's source with scripts in /tmp/claude-0/-home-user-nucleation/409f735e-c44b-5ba1-82f0-18d34af58efc/scratchpad/charvin-scripts/ (ib_sr_lp.py, ui_check.py, sr_pattern.py); that computation is the record's.
date: '2026-10-20'
summary: >-
  Defines successive refinement for the information bottleneck as extending a coarse optimum T₁ to a fine optimum (T₁, S), and shows it equivalent to some pair of optima forming X → T₂ → T₁. With an injective fine decoder, it is also equivalent to the coarse decoder points lying in the convex hull of the fine ones, which a linear programme checks. Refinability is proved for binary X and Y, for Y a function of X, and for jointly Gaussian variables. Numerically the hull test on computed optima often fails, and the loss, measured by unique information, stays under a few percent. Those failures are uncertified. Run here with certified optima, the test shows that the four-state source of [CLAIM-387](../claims.d/CLAIM-387.md) is not refinable between β = 8 and β = 12: its stochastic optima do not nest either.
---
<!-- inactive-ok-file: THEORY-751 THEORY-163 CLAIM-157 — Proposed; the rate–distortion analogue, the annealed colour-naming hierarchy and a dynamical entry named for contrast, cited as open, nothing here rests on them -->
# NOTE-981: Charvin, Catenacci Volpi and Polani — Exact and soft successive refinement of the IB

## Contribution

It gives the information bottleneck a single-letter notion of successive
refinement and three equivalent forms of it: a Markov chain between optimal
encoders, a Blackwell garbling, and a convex-hull inclusion of decoder
points. The last makes refinability checkable by a linear programme. It
collects and proves the cases where refinability always holds (binary X and
Y; Y a function of X; jointly Gaussian), and shows numerically that it often
fails beyond them. It then proposes a graded measure, the unique information
UI(X : T₁ \ T₂), of how much a two-stage learner must discard.

## Key insight

What a bottleneck knows about X is the convex hull of its decoder points
q(X|t) on the source simplex. A finer optimum refines a coarser one exactly
when its hull contains the coarser hull. So the question of nesting becomes
one about how the decoder points move as the budget grows. When they move
along a curve, as on the two-symbol branch between the first two
bifurcations, the hulls of different budgets are different chords of that
curve, and refinement fails. Refinement returns once a bifurcation opens the
fine hull into a new dimension wide enough to swallow the curvature.

## Assumptions

- **Discrete X and Y** for the hull characterization, the linear programme,
  the binary result and all numerics. Proposition 2 (Gaussian) and
  Proposition 3 (Y = f(X)) also cover continuous variables.
- **Single-letter definitions.** A bottleneck at λ maximizes I(Y; T) over
  q(T|X) with T → X → Y and I(X; T) ≤ λ. The operational, block-coding
  meaning is imported (Appendix B.2, from Tian and Chen, Tuncel, and
  Mahvari, Kobayashi and Zaidi), not proved.
- **Two stages** for the hull characterization, the binary result and the
  numerics. Definition 5 and Proposition 1 allow n stages.
- **An injective (affinely independent) fine decoder q(X|T₂)** for the
  converse of the hull characterization (Proposition 4). It always held in
  the numerics after merging equal symbols.
- **The Lagrangian problem** for the numerics and for the Gaussian result.
  The authors observed strictly concave information curves in every example,
  so the Lagrangian reached every primal budget there.
- **Optima from Blahut–Arimoto with reverse deterministic annealing**,
  started from T = X at large β. Global optimality and uniqueness are not
  checked (Appendix D).

## Key results

- **Definition 5.** (λ₁, …, λₙ)-refinable if there are a bottleneck T₁ at λ₁
  and S₂, …, Sₙ with Tᵢ = (Tᵢ₋₁, Sᵢ) a bottleneck at λᵢ.
- **Proposition 1.** Refinable iff some bottlenecks T₁, …, Tₙ have an
  extension with X → Tₙ → ⋯ → T₁, equivalently with
  Y → X → Tₙ → ⋯ → T₁. The quantifier is existential, over optima.
- **Proposition 2.** Jointly Gaussian (X, Y): the Lagrangian problem is
  refinable for all β₁ < ⋯ < βₙ. This follows from Kline and Palmer's
  semigroup: compressing a Gaussian bottleneck T₂ at β′₁ gives a bottleneck
  of the original problem at β₁ = β′₁β₂/(β′₁ + β₂ − 1) (A18), and every
  β₁ ∈ [β_IB, β₂) is reached (Proposition A6).
- **Proposition 3.** Y a deterministic function of X: refinable at all
  budgets, by nested erasures of Y (Kolchinsky, Tracey and van Kuyk's
  solution). The paper notes the solution "is nothing more than an
  increasingly noisy version of Y".
- **Proposition 4 (convex-hull characterization).** If refinable at
  (λ₁, λ₂), some bottlenecks satisfy
  Hull{q(X|t₁)} ⊆ Hull{q(X|t₂)} (7). Conversely, if bottlenecks satisfy (7)
  and q(X|T₂) is injective, the problem is refinable, and the extension with
  X → T₂ → T₁ is unique. Checking (7) is one linear programme per t₁, the
  first phase of the simplex method (Appendix B.6), with complexity
  Õ(|X|^{ω+1} log(|X|/δ)).
- **Proposition 5.** |X| = |Y| = 2: refinable at every λ₁ < λ₂ (two stages).
  The proof uses the convexity approach: optima reach the lower convex
  envelope of F_β(p) = H(κp) − H(p)/β. The set P(β) where F_β exceeds its
  envelope is an open interval whose ends are the decoder points (Lemma A3,
  cited from Witsenhausen and Wyner), and it grows with β (Lemma A2).
- **Proposition 6.** UI(X : T₁ \ T₂) = min over extensions of I(X; T₁ | T₂)
  = D_KL(Δ_{q₁,q₂} ‖ Δ_SR,2). This is the KL distance from the set of
  extensions to the set of laws with the chain.
- **Proposition 7** (cited). UI is continuous in q₁(X, T₁) and q₂(X, T₂).
- **Proposition 8.** Refinable iff some optimal encoders satisfy
  q(T₂|X) ⊒ q(T₁|X) in the decision order, iff q(T₁|X) is a garbling of
  q(T₂|X) (Blackwell–Sherman–Stein, via Bertschinger and Rauh).
- **Numerics, exact (§2.3).**
  - |X| = |Y| = 2: the hull condition always held on random p(X, Y), as
    Proposition 5 says.
  - |X| = |Y| = 3: "in these examples as in most non-reported examples, the
    convex hull condition … breaks as long as λ₂ < λ_c(2)", the second
    bifurcation. Above it the pattern varies, but it seems "typically
    necessary, for SR to hold, that the larger parameter λ₂ has crossed the
    bifurcation value".
  - No count or fraction of sampled distributions is reported.
- **Numerics, soft (§3.2).** UI landscapes over (λ₁, λ₂) for three 3×3
  examples, one 5×3 example and one 7×5 example. UI drops sharply when λ₂
  crosses a bifurcation from below. The ratio σ = UI / I_q(X; T₁, T₂) had
  maxima of 1.89%, 0.39%, 1.82%, 2.03%, 1.34% and 0.31% for Figures 7–12,
  never above 5.4% in any example, up to |X| = 20, |Y| = 10. The number of
  examples is not reported.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | IB refinability is equivalent to a Markov chain between some optimal encoders, and to a Blackwell garbling | strong | Propositions 1 and 8; proofs in B.1 checked, and re-derived in [THEORY-753](../theory.d/THEORY-753.md) |
| C2 | With an injective fine decoder, refinability for a given pair is equivalent to the convex-hull inclusion (7), decidable by a linear programme | strong | Proposition 4, proof in B.5 checked; re-derived in [THEORY-753](../theory.d/THEORY-753.md) |
| C3 | Binary X and Y are always refinable (two stages) | strong, resting on a cited lemma | Proposition 5; the cited Lemma A3 is replaced by a direct argument in [THEORY-757](../theory.d/THEORY-757.md) |
| C4 | Y = f(X) is always refinable | strong | Proposition 3, re-derived in [THEORY-757](../theory.d/THEORY-757.md) |
| C5 | Jointly Gaussian variables are always refinable (Lagrangian) | strong as a consequence of the cited semigroup result | Proposition 2, B.3; Kline and Palmer not read here |
| C6 | Successive refinement "does not always hold" for the IB | weak as shown in the paper; established here for one source | §2.3 numerics on uncertified optima; the paper calls its patterns "mere numerical proxies" (Appendix D). Certified below for [CLAIM-387](../claims.d/CLAIM-387.md)'s source |
| C7 | Refinement patterns are shaped by bifurcations; refinement typically needs λ₂ past the second bifurcation | moderate, phenomenological | Figures 4–6, 10–12, A3; consistent with the record's run below |
| C8 | The loss of optimality from two-stage processing is typically small, σ ≲ 1–2%, never above 5.4% | moderate as an observation, with sample size unstated; σ is an upper bound for the given optima | §3.2 |
| C9 | Trained deep networks should, or might, sit near IB bifurcations | weak | interpretation in §4.2, conditional on the contested IB theory of deep learning |

## Method

- **Optima.** Blahut–Arimoto with reverse deterministic annealing, from
  T = X at large β downward, because forward annealing followed suboptimal
  branches at bifurcations.
- **Canonical form.** Symbols with equal decoder points are merged.
  Bifurcations are located where the number of distinct points changes.
- **Hull test.** For each t₁, a phase-one linear programme decides whether
  q(X|t₁) is a convex combination of the q(X|t₂), with threshold 10⁻⁶.
- **Unique information.** Computed with Banerjee, Rauh and Montúfar's
  provably convergent algorithm (the computeUI code).

## Concepts

- **Bottleneck (primal / Lagrangian).** A maximizer of I(Y; T) at
  I(X; T) ≤ λ, or a minimizer of I(X; T) − β I(Y; T).
- **Effective cardinality k(T).** The number of distinct decoder points
  q(X|t). For Lagrangian optima it equals the number of distinct q(Y|t)
  (Proposition A1).
- **Canonical bottleneck.** One whose decoder points are all distinct.
- **Exact successive refinement.** Definition 5, as above.
- **Soft successive refinement.** The unique information
  UI(X : T₁ \ T₂) = min over couplings of I_q(X; T₁ | T₂), with the
  (X, T₁) and (X, T₂) laws fixed. For n stages:
  D_KL(Δ_{q₁…qₙ} ‖ Δ_SR,n).
- **Bottleneck trajectory.** The path of the decoder points on Δ_X as λ
  grows: piecewise continuous, jumping at each symbol split.
- **SR pattern.** The set of (λ₁, λ₂) at which the hull test passes.

## Connections

It builds on Equitz and Cover's characterization of successive refinement
([THEORY-751](../theory.d/THEORY-751.md)) and carries it to the bottleneck, where the reproduction
alphabet is a simplex. The operational form comes from Tian and Chen (2008),
the record's other unread lead, and from Mahvari, Kobayashi and Zaidi's
scalable bottleneck. It generalizes Yang, Piantanida and Gündüz's
multi-layer bottleneck lemmas (the binary symmetric and scalar Gaussian
cases), and No (2019), refinability for Y = X. The convexity machinery is
Witsenhausen and Wyner's, via Asoodeh and Calmon. The bifurcation reading
follows Zaslavsky and Tishby's account of deterministic annealing.

## Bearing on the record

**[QUESTION-220](../questions.d/QUESTION-220.md), the stochastic half: answered in the negative for the
record's own example.** The paper gives the test. The record ran it on
[CLAIM-387](../claims.d/CLAIM-387.md)'s source, X uniform on four states with
P(Y = 1 | x) = (0, 0, 1/8, 3/8), with optima certified rather than merely
found. This is the record's computation, not the paper's (scripts named in
the history note).

1. *Reduction.* States 0 and 1 share p(Y|x), so every optimum is constant on
   them ([THEORY-743](../theory.d/THEORY-743.md), step 1). The problem is effectively three states,
   a = {0, 1} with mass ½, b = {2} and c = {3}, and binary Y.
2. *Optima.* Blahut–Arimoto from 400 random starts, |T| = 5, gave
   (I(X; T), I(T; Y)) = (0.5457, 0.0972) bits at β = 8, with two decoder
   points, and (0.9522, 0.1386) bits at β = 12, with three. These match
   [NOTE-980](NOTE-980.md)'s values.
   - At β = 8, in (a, b, c) coordinates, the decoder points are
     (0.751, 0.244, 0.004) and (0.067, 0.260, 0.674).
   - At β = 12 they are (1, 0, 0), (0.314, 0.661, 0.025) and
     (0.010, 0.207, 0.784).
   These are soft versions of the deterministic optima {0,1,2 | 3} and
   {0,1 | 2 | 3}. The β = 12 optimum keeps a pure {0, 1} symbol.
3. *Certificate.* By [THEORY-753](../theory.d/THEORY-753.md) step 5, take the affine function ℓ
   through the decoder points' values of F_β, tangent to F_β at them. At
   β = 8 there are only two points, and ℓ was fitted by least squares to
   the values and gradients. Then check F_β − ℓ ≥ 0 over the simplex.
   - On a grid of spacing 1/1200, its minimum was ≈ 10⁻⁷ at β = 8 and 0 at
     β = 10 and 12, attained at the decoder points.
   - Away from the decoder points the minimum was +1.5 × 10⁻⁵, +1.1 × 10⁻⁵
     and +1.9 × 10⁻⁵.
   - 300 local minimizations started from the lowest grid points all
     converged to the decoder points.
   - Near the vertex a, F_β − ℓ grows like (1/8 − 1/β)·ε log(1/ε) toward b
     and like (3/8 − 1/β)·ε log(1/ε) toward c, both positive for β > 8. So
     the grid cannot miss a dip there.
   So the optima are globally optimal, and the touching sets are exactly the
   two or three decoder points, which are affinely independent. The
   canonical optimum at each β is therefore unique.
4. *Test.* The β = 8 point (0.751, 0.244, 0.004) is outside the hull of the
   β = 12 points. The phase-one programme's optimum was 0.26, not 0, and the
   Euclidean distance to the hull was 5.6 × 10⁻³, far above the solver's
   error of about 10⁻⁷. The hull's edge from (1, 0, 0) to
   (0.314, 0.661, 0.025) has c ≈ 0.009 at b = 0.244, more than the point's
   0.004. The same holds for β = 8 against 10 (distance 2.5 × 10⁻³) and for
   10 against 12 (8.7 × 10⁻³), with all three optima certified.
5. *Conclusion.* By [THEORY-753](../theory.d/THEORY-753.md), no pair of IB optima at
   λ₁ = 0.5457 and λ₂ = 0.9522 bits forms X → T₂ → T₁. **The stochastic
   optima do not nest either: raising the budget from β = 8 to β = 12
   reorganizes the optimum.** The certificate is numerical, a fine grid with
   local refinement and an asymptotic argument at the vertex, not interval
   arithmetic, so it is a demonstration short of a proof.
6. *How much is lost.* The unique information
   UI(X : T_{β=8} \ T_{β=12}) is 4.7 × 10⁻³ bits, with σ = 0.49% by the
   paper's ratio. For 8 against 10 it is 2.7 × 10⁻³ bits (0.34%), and for
   10 against 12 it is 3.5 × 10⁻³ bits (0.37%). These were computed by SLSQP
   from 20 starts, all agreeing, on a convex problem. They are within the
   paper's range.
7. *The pattern.* Over a grid of 16 values of β from 5 to 60, with optima
   from 60 restarts each (uncertified except at 8, 10 and 12):
   - The hull test failed between any two β in the two-symbol branch
     (β ≤ 8.5).
   - It failed for most pairs with β₁ ≥ 7.5 and β₂ ≤ 16.
   - It passed for β₁ ≤ 6 against β₂ ≥ 9.5, for β₁ ≤ 8 against β₂ ≥ 20, and
     for β₁ ≤ 14 against β₂ ≥ 30.
   So nested pairs exist, but a moderate step in budget generally does not
   nest. The pattern is not monotone: β₁ = 8.5 and 9 fail against β₂ = 20,
   while 8 and 9.5 pass. That may reflect uncertified optima near the
   bifurcation at β ≈ 9, where only 27% of restarts reached the best value.
   - The pure {0, 1} symbol appears between β = 8.5 and 9. It cannot appear
     for β < 8. Moving a decoder point a distance ε from the vertex toward b
     changes F_β by (1/8 − 1/β)·ε log(1/ε) to leading order, which is
     negative there, so the vertex cannot be a touching point.

This answers what [CLAIM-387](../claims.d/CLAIM-387.md) left open: "Whether stochastic optima nest
stays open". For this source, they do not, at the budgets of [CLAIM-387](../claims.d/CLAIM-387.md)'s
two incomparable partitions. With Proposition 5 it also fixes the smallest
case where refinability can fail. It holds for |X| = |Y| = 2, and fails here
with three effective source states and binary Y.

**What stays open on [QUESTION-220](../questions.d/QUESTION-220.md).**
- A structural condition beyond the three special cases.
- A proof without numerics. An exact argument for this source would show
  that the β = 8 envelope touches the edge region below the β = 12 hull's
  edge, which looks tractable since Y is binary.
- Whether the loss is always small. The paper's σ ≤ 5.4% is an observation,
  and the σ here is 0.5%.
- The operational, rate-loss meaning of UI, which the paper also leaves open.
- Whether annealing paths in [THEORY-163](../theory.d/THEORY-163.md)'s colour-naming hierarchy pass the
  test. They now can be tested. [THEORY-163](../theory.d/THEORY-163.md) is not contradicted, since a
  failed test there would show non-nesting only with certified optima.

**Recommended to the coordinator.**
- File the four-state result as a CLAIM answering [QUESTION-220](../questions.d/QUESTION-220.md), warrant
  `demonstrated` (or `empirical`, if a numerical certificate is not taken as
  a demonstration). Possible title: "Stochastic information-bottleneck optima
  at two budgets need not be nested: for [CLAIM-387](../claims.d/CLAIM-387.md)'s source the unique
  optima at β = 8 and β = 12 admit no Markov chain X → T₂ → T₁". Ground it in
  [LIT-1258](../literature.d/LIT-1258.md) and rest it on [THEORY-753](../theory.d/THEORY-753.md).
- Amend [CLAIM-387](../claims.d/CLAIM-387.md)'s "What it does not say" first bullet, which says the
  stochastic case stays open, to point to it.
- Update [QUESTION-220](../questions.d/QUESTION-220.md)'s last bullet, which says the Charvin et al. test
  is "not yet registered", and its closing paragraph.

**Two THEORY entries are filed.** [THEORY-753](../theory.d/THEORY-753.md) (Active) holds the
characterization and when a failed test proves non-refinability.
[THEORY-757](../theory.d/THEORY-757.md) (Active) holds the two finite sufficient conditions. The
Gaussian case is not filed, since it rests on an unread semigroup result. No
THEORY is filed for the soft measure or the bifurcation phenomenology, which
are observations on uncertified optima.

**Other entries.** [NOTE-980](NOTE-980.md)'s direct-versus-remote log-loss argument is
consistent with this paper. The paper's Proposition 3 is the direct case
(Y = f(X)), and it cites No (2019) for Y = X. The paper does not bear on the
dynamical entries named for this batch ([THEORY-733](../theory.d/THEORY-733.md), [THEORY-661](../theory.d/THEORY-661.md), [CLAIM-157](../claims.d/CLAIM-157.md)).

**Anthology.** No instruction for machine-learning practice. §4.2 reads
refinability as a condition for the layers of a deep network to be IB-optimal
together, which is why the LIT carries `anthology-candidate`.

## Limitations

- **The failures in the paper are uncertified.** The test is run on solver
  outputs. Global optimality is not checked, and uniqueness is conjectured
  (Conjecture 1). The authors say so in Appendix D, but the abstract and §6
  state the finding ("successive refinement does not always hold") without
  the hedge.
- **No denominators.** Neither how many distributions were sampled nor how
  often the test failed is given. "Most non-reported examples" is the only
  frequency.
- **σ is an upper bound for the given optima,** as Appendix D notes. Its
  denominator, I(X; T₁, T₂) = λ₂ + UI, is the larger budget, which makes the
  ratio look small. Against λ₁, the loss in the record's example is 0.9%.
- **The commentary on Proposition 8 swaps (ii) and (iii).** The text says
  "Point (ii) means that … T₁ can be retrieved by post-processing" T₂, and
  that point (iii) "relies on the mathematically deep part" of Blackwell's
  theorem. But (ii) is the decision order (Definition 10) and (iii) the
  garbling order (Definition 11). §4.2's "Proposition 8-(ii)" inherits the
  swap.
- **Proposition A1's proof has a wrong intermediate step.** From
  q(Y|t₁) = q(Y|t₂), the self-consistent equation gives q(t₁|x) ∝ q(t₂|x),
  with ratio q(t₁)/q(t₂), not equality. The conclusion, q(X|t₁) = q(X|t₂),
  still follows.
- **"A bottleneck must saturate the information constraint" (§1.3.2) is
  false on the flat part of the information curve.** Above
  λ = H(ε(X)), the entropy of the causal partition, I(Y; T) is already
  maximal ([THEORY-743](../theory.d/THEORY-743.md)). For Y = f(X) this is any λ > H(Y). The paper's
  Proposition 3 proof avoids the issue by restricting to λ ≤ I(X; Y).
- **Cross-reference slips.**
  - "Theorem 4" is cited for Proposition 4 in seven places.
  - "Proposition 4-(iii)" in B.2 should be Proposition 1-(iii).
  - Proposition A2 refers to "(A38)" for problem (1)/(A5).
  - "Theorem A3" should be Proposition A3.
  - The gloss of (2) writes Iλ(X; T) twice.
  - The PDF's citation box drops "Exact and Soft" from the title.
  None affects a result.
- **The Gaussian result is for the Lagrangian problem** and rests on a cited
  semigroup property, so it was not checked here.
- **The deep-learning section is conditional** on the contested IB theory of
  deep learning, and its recommendation, that layers should sit near
  bifurcations, is a conjecture from 3×3 examples.

## Open questions

- **Conjecture 1.** With a strictly concave information curve, the canonical
  optimum is unique and its decoder injective. A proof would turn every
  failed test in the paper into a theorem. The envelope certificate used
  here settles it case by case.
- **A characterization of the refinable (λ₁, λ₂) pairs** from the
  bifurcation structure. The paper and the record's run agree that the
  two-symbol branch never refines within itself once it is curved.
- **An operational meaning for UI**, as a rate or relevance penalty in a
  two-stage code.
- **More than two stages for soft refinement.** No algorithm with a
  convergence guarantee is known for D_KL(Δ_{q₁…qₙ} ‖ Δ_SR,n), n > 2.
- **An exact proof of the four-state failure.** The certificate here is
  numerical.
