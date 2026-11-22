# Reader notes: kesten1973 (LIT-3005)

Kesten, H. (1973), "Random difference equations and renewal theory for
products of random matrices", Acta Mathematica 131, 207-248,
doi:10.1007/BF02392040.

## Step 1: copies located (2026-11-22)

- OpenAlex (api.openalex.org/works/doi:10.1007/BF02392040, no email sent):
  bronze OA, oa_url the Project Euclid PDF below.
- https://projecteuclid.org/journals/acta-mathematica/volume-131/issue-none/Random-difference-equations-and-Renewal-theory-for-products-of-random/10.1007/BF02392040.pdf
  Kind: the open archive of Acta Mathematica on Project Euclid (bronze
  OA; also Semantic Scholar's openAccessPdf). Lawful. NOT READ: Imperva
  Incapsula WAF challenge ("Request unsuccessful. Incapsula incident ID
  ..."), 2026-11-22. Not retried.
- http://projecteuclid.org/euclid.acta/1485889791 (DOI landing): same
  Incapsula challenge, 2026-11-22.
- https://link.springer.com/content/pdf/10.1007/BF02392040.pdf: paywall
  ("Buy article PDF USD 39.95", hasAccess N), 2026-11-22.
- https://www.intlpress.com/site/pub/pages/journals/items/acta/content/vols/0131/index.php:
  HTTP 403, 2026-11-22 (tried once; not retried).

Outcome for the original: **Unfetched** (lawful copy located at Project
Euclid, stopped by a WAF challenge). Going to neighbours.

## Step 2: neighbours read (2026-11-22)

Checked first: record/ holds neither (no hit for 1512.07262, 1009.1728,
Kevei, Grincevičius, Alsmeyer or Mentemeier).

N1. Kevei, P. (2016), "A note on the Kesten–Grincevičius–Goldie theorem",
arXiv:1512.07262v2 (22 Jul 2016). https://arxiv.org/pdf/1512.07262v2,
PDF, 17 pp. Kind: arXiv author preprint. Read: §1 (pp. 1-6) in full, the
start of §2 (Theorem 5 and the smoothing step), the reference list.
Skipped: the remaining proofs and the appendix. Stands in for: the
statement and hypotheses of Kesten's theorem in one dimension, Goldie's
re-proof, and the reflecting (max) variant. It does NOT restate Kesten's
matrix theorem.

N2. Alsmeyer, G. and Mentemeier, S. (2011), "Tail behavior of stationary
solutions of random difference equations: the case of regular matrices",
arXiv:1009.1728v3. https://arxiv.org/pdf/1009.1728v3, PDF, 27 pp. Kind:
arXiv author preprint. Read: abstract, §1 with Theorem 1.1 and Remarks
1-4 (pp. 1-3). Skipped: §§2-8 (proofs). Stands in for: what Kesten's
article states in d dimensions, at second hand and for regular
(invertible) matrices.

## Summary (from the neighbours; the original is unread)

Kesten's article treats the random difference equation (perpetuity,
stochastic recurrence) X = AX + B, with (A, B) independent of X, and
proves that its stationary solution has a Pareto-like tail whose index κ
is the positive root of E A^κ = 1. Per Kevei he proved it "in d
dimension", for products of random matrices; Goldie (1991) re-proved the
one-dimensional case by implicit renewal theory, after Grincevičius. The
theorem is now called Kesten–Goldie, or Kesten–Grincevičius–Goldie.

## Contribution (as the neighbours attribute it)

The first existence-and-tail result for X = AX + B: "The first results on
existence and tail behavior of the solution are due to Kesten [25]"
(Kevei p. 1). A multidimensional tail result "originally stated by Kesten
at the end of his famous article [12]", proved in full later by Le Page
(Alsmeyer–Mentemeier, abstract and Remark 1, p. 3).

## Key results (quoted from the neighbours)

1. The scalar theorem (Kevei p. 1, eqs. (2)-(3)): Kesten "proved that if
   EAκ = 1, EAκ log+ A < ∞, log A conditioned on A ≠ 0 is nonarithmetic,
   and E|B|κ < ∞ for some κ > 0 ... then the solution of (1) has
   Pareto-like tail, i.e. P{X > x} ∼ c+ x−κ and P{X < −x} ∼ c− x−κ ...
   for some c+, c− ≥ 0, c+ + c− > 0." Standing assumptions (p. 1):
   P{Ax + B = x} < 1 for all x, A ≥ 0, A ≢ 1.
2. Dimension (Kevei p. 1): "Actually, Kesten proved a similar statement
   in d dimension. Later Goldie [18] simplified the proof of the same
   result in the one-dimensional case". Whether the 1973 paper states
   the scalar case separately is not settled by the neighbour.
3. Contraction is forced, not merely allowed (Kevei p. 6): "The
   assumption EAκ = 1 together with A ≢ 1 imply that E log A < 0, so the
   random walk tends to −∞". Growth is needed (p. 2): "if P{A > 1} > 0
   the tail decreases at least polynomially"; with A ≤ 1 a.s. "the
   solution has at least exponential tail" (Goldie and Grübel).
4. The other source of a power tail (Kevei p. 2): Grey "showed that if
   EAκ < 1, EAκ+ε < ∞, then the tail of X is regularly varying with
   parameter −κ if and only if the tail of B is ... the regular variation
   of the solution X of (1) is either caused by A alone, or by B alone".
5. The reflecting / max form (Kevei p. 4, eq. (12)): for X = AX ∨ B,
   "Theorem 5.2 in [18] [Goldie] states that if (2) holds, then there is
   a unique solution X to (12), and P{X > x} ∼ cx−κ with some c ≥ 0,
   and c > 0 if and only if P{B > 0} > 0." With B ≡ 1, "log X = M, where
   M = max{0, S1, S2, ...}": the maximum of a negative-drift random
   walk. This is Goldie's theorem, not Kesten's.
6. The method (Kevei p. 2): the tilted measure "Pκ{log A ∈ C} =
   E[I(log A ∈ C)Aκ]", under which the tail equation is a renewal
   equation; "If Eκ log A = EAκ log A ∈ (0, ∞), then a renewal theorem on
   the line implies the required tail asymptotics."
7. Without E A^κ log⁺A < ∞ the pure power law can fail (Kevei's own
   result, abstract): "P{X > x} ∼ cx−κ ℓ(x) holds, where ℓ is a
   nonconstant slowly varying function".
8. Matrix form (Alsmeyer–Mentemeier, Theorem 1.1, p. 2): for
   Rn = Mn Rn−1 + Qn with negative Lyapunov exponent β and (A1)-(A7),
   "there exists a unique κ ∈ (0, κ0] such that lim n−1 log E‖Πn‖κ = 0"
   and "lim tκ P(xR > t) = K(x) for all x ∈ S", K positive and
   continuous; R = Σ Πn−1 Qn (eq. (2)). Remark 1: "This result (with one
   extra condition) was stated by Kesten at the end of his famous
   article [12] and later proved by Le Page [15]".

## Assumptions

(A, B) i.i.d. pairs, A and B possibly dependent; X independent of (A, B);
non-degeneracy; nonarithmetic log A; a κ > 0 with E A^κ = 1;
E A^κ log⁺A < ∞; E|B|^κ < ∞. In d dimensions the Lyapunov exponent takes
the place of E log A and the growth rate of E‖Πn‖^κ that of E A^κ.

## Concepts

Random difference equation; perpetuity; stochastic fixed-point equation
X =d AX + B; Kesten–Goldie (Kesten–Grincevičius–Goldie) theorem;
Cramér-type condition E A^κ = 1 and the tilted measure; implicit renewal
theory; Grey's B-driven case; max recursion X = AX ∨ B and the maximum of
a random walk; Lyapunov exponent; Le Page's matrix theorem.
