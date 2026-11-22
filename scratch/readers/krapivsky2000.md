# Reader notes: krapivsky2000 (LIT-2974)

Krapivsky, Redner and Leyvraz, "Connectivity of Growing Random Networks",
arXiv cond-mat/0005139 (v2, 18 Sep 2000; PRL 85, 4629, 2000).

## Step 1: copies located (2026-11-22)

- https://arxiv.org/pdf/cond-mat/0005139 : arXiv preprint (the authors'
  manuscript, v2, dated 18 Sep 2000), PDF, HTTP 200, 119,357 bytes,
  fetched 2026-11-22. Read in full. Lawful (arXiv). No other copy sought:
  the arXiv copy was complete. The published PRL version was not
  consulted, so page numbers below are the preprint's (pp. 1 to 4).

## Step 2: read

Provenance: the whole preprint (4 pages, Fig. 1, Fig. 2, Eqs. 1 to 17,
21 references) via pdftotext, no email sent anywhere. Nothing skipped.
Equations with products and cases were checked against the layout text,
which renders them poorly; the quotes below are from the running prose.

### Summary

A growing random network (GRN): at each step a new site joins and makes
one directed link to an earlier site with k links, chosen with
probability A_k/Σ A_j N_j. The graph is a directed tree; k counts k−1
incoming links plus the one outgoing link. The authors write rate
equations for N_k(t), the mean number of sites with k links (Eq. 1), and
solve them by kernel. For A_k = k^γ: γ = 0 gives n_k = 2^(−k); γ = 1
gives n_k = 4/[k(k+1)(k+2)] ∼ k^(−3) (Eq. 2); 0 < γ < 1 gives a
stretched exponential with leading term exp[−μ k^(1−γ)/(1−γ)] (Eq. 5),
μ(γ) rising smoothly from 1 to 2 (Fig. 2); γ > 1 gives gelation, one site
taking almost all links, with a cascade of transitions at γ = (m+1)/m.
Asymptotically linear kernels (A_k → a∞ k) give a power law whose
exponent ν = 1 + μ/a∞ can take any value above 2. They also give the most
popular site's degree (Eq. 13), test it on ISI citation data, and solve
the joint age and degree distribution (Eqs. 14 to 17).

### Contribution

An exact rate-equation solution for the whole family of degree-dependent
kernels, which shows that a power-law degree distribution is the
borderline case of linear attachment, flanked by stretched exponentials
and by condensation ("gel"), and that within the linear case the exponent
is not universal but is set by the kernel's details.

### Key results (preprint pages)

1. **Three regimes** (abstract, p. 1): "For γ < 1, the number of sites
   with k links, N_k, varies as stretched exponential. For γ > 1, a single
   site connects to nearly all other sites. In the borderline case
   A_k ∼ k, the power law N_k ∼ k^−ν is found, where the exponent ν can
   be tuned to any value in the range 2 < ν < ∞."
2. **Only γ = 1** (p. 1): "A power law distribution N_k ∼ k^−ν arises
   only for γ = 1. In this case, finer details of the dependence of the
   connection kernel on k affect the exponent ν."
3. **Linear kernel exactly** (p. 2, Eq. 2): n_k = 4/[k(k+1)(k+2)], i.e.
   k^(−3), from the recursion n_k = n_{k−1}(k−1)/(k+2).
4. **No preference** (p. 2): for γ = 0, μ = 1 and "the corresponding
   connectivity distributions are given by n_k = 2^−k". Exponential.
5. **Sublinear** (p. 2, Eq. 5): n_k ∼ k^(−γ) exp[−μ k^(1−γ)/(1−γ)] for
   1/2 < γ < 1, with more terms in the exponent "Whenever γ decreases
   below 1/m".
6. **Hard to tell apart** (p. 2): "for 0.8 ≲ γ ≲ 1, n_k depends weakly on
   γ for 1 ≤ k ≤ 1000. Thus, it is difficult to discriminate between
   different γ's and even to distinguish a power law from a stretched
   exponential in the GRN model."
7. **Tunable exponent** (p. 2, Eqs. 7 and 8): for A_k → a∞ k,
   "nk ∼ k^−ν with ν = 1 + µ/a∞"; for A_1 = 1, A_k = a∞ k (k ≥ 2),
   ν = (3 + √(1 + 8/a∞))/2, "tuned to any value larger than 2".
8. **Superlinear: gelation** (p. 1): "The case γ > 1 leads to phenomenon
   akin to gelation [19] in which a single 'gel' site connects to nearly
   every other site of the graph. For γ > 2, this phenomenon is so
   extreme that the number of connections between other sites is finite
   in an infinite graph." P = Π 1/(1 + N^(1−γ)) > 0 iff γ > 2 (Eq. 9):
   "for γ > 2 there is a non-zero probability that the initial site
   connects to all other sites" (p. 3).
9. **Transition cascade** (p. 3): M_γ ∝ t^γ; N_k = J_k t^(k−(k−1)γ) while
   k < γ/(γ−1); "the remaining t links must all connect to a single site
   which has t connections". "Generally for (m+1)/m < γ < m/(m−1), the
   number of sites with more than m links is finite".
10. **Largest degree** (p. 3, Eq. 13): k_max ∼ (ln t)^(1/(1−γ)) for
    sublinear, t^(1/(ν−1)) for asymptotically linear, t for superlinear.
    ISI data, 783,339 papers, most cited 8,904: "This accords with the
    first line of Eq. (13) for γ ≈ 0.86, and also with the second when
    ν ≈ 2.5."
11. **Age** (p. 4, Eqs. 16, 17): for A_k = k, c_k(t,a) is self-similar in
    a/t; "old sites are better connected". The model has no explicit
    aging of the kernel (p. 3).

### Assumptions

One link per new site (a tree); a kernel depending on degree only (no
fitness, no age); continual entry, one site per unit time (the δ_k1 term,
"the continuous introduction of new sites with no incoming links");
mean-field rate equations for averages N_k (fluctuations not treated,
except the γ > 2 probability P); k counts the outgoing link, so A_k = k
is BA-type attachment on total degree with m = 1; long-time limit.

### Concepts

Connection kernel A_k; homogeneous kernel k^γ; asymptotically linear
kernel; rate (master) equation for N_k; amplitude μ of M_γ = μt;
stretched exponential; gelation, the "gel" site; "winner take all";
connectivity transitions at γ = (m+1)/m; most popular site k_max;
age-and-connectivity distribution c_k(t, a).

### Verdict on how the exchange characterized the work

A1 §4's table (as filed in CLAIM-817): α = 0 "Exponential-type",
0 < α < 1 "Stretched-exponential tail", α = 1 "Power-law", α > 1 "Strong
concentration; potentially winner-take-all". **Accurate in the first
three rows, too weak in the last.** The paper calls γ > 1 "winner take
all" without hedging: a single gel site has ~t of the 2t link ends for
every γ > 1, and for γ > 2 all but finitely many sites link to it.
CLAIM-817's correction ("a condensation onto one node, not a heavy
tail") and its parenthesis "for α > 2 one node links to all but finitely
many" are both what the paper says (p. 3).

Two things the exchange and the filings leave out: (a) "α = 1 power law"
is k^(−3) only for A_k = k exactly; the paper's linear case is a family
with ν anywhere in (2, ∞); (b) the paper's own warning that for
0.8 ≲ γ ≲ 1 a stretched exponential and a power law cannot be told apart
up to k = 1000.

The LIT summary ("sublinear α gives a stretched-exponential degree
distribution, superlinear α a single hub taking almost all links; only
α = 1 gives a power law") is correct; it should add the tunable ν for
asymptotically linear kernels.

### Bearing on the named codes

- **CLAIM-817** (supports, the kernel half; leaves open the entry half).
  Results 1, 4, 5, 8, 9 are the claim's four regimes, derived exactly:
  "A power law distribution N_k ∼ k^−ν arises only for γ = 1" (p. 1).
  The `defeated_if` already exempts the shifted kernel, and result 7
  confirms that a non-pure linear kernel moves the exponent, which the
  claim allows. The paper always has entry (δ_k1 term); it never removes
  it, so "together with continual entry" is not tested here (it rests on
  CLAIM-830). Its simulations agree: at α = 1.5 one node holds 49.7% of
  edge ends, the paper's "the remaining t links must all connect to a
  single site" (t of 2t ends). Note γ = 3/2 is itself a transition point
  of the cascade (result 9), with "Logarithmic corrections". This is the
  `grounds` entry ARG-149 said the kernel regimes rest on; a THEORY from
  this reading can ground the claim directly.
- **CLAIM-806** (supports the marginality; qualifies the table and one
  aside). The paper names γ = 1 "the borderline case" (abstract) and
  calls γ > 1 "akin to gelation", which is the claim's "condensation"
  and its parallel to a giant cluster. Qualifications: (i) the table's
  "at it: k^(−3)" holds only for A_k = k; the paper's borderline is the
  class of asymptotically linear kernels, with ν from 2 to ∞ (p. 2).
  So the claim's "the boundary is a line in a larger space of kernels"
  is right, and the "standard result, not checked here" is now checked:
  ν = 1 + μ/a∞ (Eq. 7). (ii) The paper's indistinguishability remark
  (result 6) means the marginal point is sharp in the model and blurred
  in finite data, which agrees with the dated Clauset note already on the
  claim. (iii) The `defeated_if` (a power law over an open range of α
  around 1) is not met: the paper's γ ≠ 1 tails are never power laws.
  The upper side is a cascade of transitions at γ = (m+1)/m, not a single
  regime, which adds structure the claim's table lacks.
- **ARG-149** (supports its verdict). The argument says the kernel
  regimes rest on "Krapivsky, Redner and Leyvraz's (LIT-2974)"; read,
  they do. Nothing in the paper changes the argument's reading of
  Mitzenmacher.
- **NOTE-2237** (parallel). Mitzenmacher's mixing model gives
  c_j ∼ j^(−(2−α)/(1−α)), an exponent moved by mixing uniform with
  linear attachment; this paper's asymptotically linear kernel moves ν
  the same way (ν = 1 + μ/a∞). Two routes to the same fact, a
  non-universal exponent within linear attachment. NOTE-2237's line
  "The kernel regimes are Krapivsky, Redner and Leyvraz's" is borne out.

### Limitations

Mean-field rate equations for averages; trees only (one link per site);
degree-only kernels; the stretched-exponential asymptotics are given for
γ > 1/3 with a pattern stated beyond; the γ > 1 analysis is leading
order with logarithmic corrections at transition points not worked out;
the ISI test fits k_max with two different models (γ ≈ 0.86 or
ν ≈ 2.5), which by the authors' own account does not separate them; a
4-page letter, with the general-kernel age solution deferred to a
preprint [21].

### Candidate THEORY sentence

"In a growing tree where each new site links to an earlier site with
probability proportional to A_k, a homogeneous kernel A_k = k^γ gives a
stretched-exponential degree distribution for 0 < γ < 1 (exponential at
γ = 0), a single site holding nearly all links for γ > 1, and a power
law only at γ = 1, where an asymptotically linear kernel A_k → a∞ k
gives N_k ∼ k^(−ν) with ν = 1 + μ/a∞ anywhere in (2, ∞)."

promote_when: an independent derivation or simulation of the GRN model
reproduces the three regimes for k^γ kernels and the dependence of ν on
the asymptotically linear kernel (Oliveira and Spencer's rigorous
treatment of superlinear attachment, or Krapivsky and Redner's longer
PRE paper, would do).

## Step 3: recheck (grep of record/ after reading)

Searched for: gelation, superlinear/super-linear, stretched exponential,
rate equation, master equation, Redner, Dorogovtsev, Krapivsky,
winner-take-all, condensation, connection kernel, citation distribution,
tunable exponent. Held entries the first search missed:

- **QUESTION-505** (what fixes the exponent; bears on, supports the
  partial pattern). Its table gives linear attachment's survival exponent
  as "entry rate over growth rate". Result 7 gives ν − 1 = μ/a∞: the
  growth rate of the normalisation M_A = μt over the kernel's asymptotic
  slope, another ratio of rates, and one the kernel tunes. Also a
  counterweight: the exponent is set by the whole kernel through μ
  (Eq. 8), not only by two named rates.
- **CLAIM-830** (supports the entry term's role in the solution; leaves
  open removing entry). The rate equation's δ_k1 is the "continuous
  introduction of new sites", and the self-similar age solution (Eq. 16)
  and "old sites are better connected" fit the age mechanism. The paper
  never runs the no-entry case.
- **CLAIM-803** (supports, one clause). "a power law does not identify
  its mechanism": the paper's result 6 says a power law and a stretched
  exponential are hard to distinguish for 0.8 ≲ γ ≲ 1 up to k = 1000,
  and its ISI fit fits both. Also bears on the claim's attachment test
  (A3 §5): the paper's kernel A_k is the quantity that test measures.
- **CLAIM-796** (contrast). The claim CLAIM-806 objects to; the paper's
  "borderline case" wording is evidence for the objection.
- **SYNTHESIS-119** (background). Its "Cumulative advantage, in a
  particular form" line rests on CLAIM-817, which this reading grounds.
- **NOTE-678** (on LIT-867, Emergent Hyperbolic Network Geometry;
  background). Names "the standard master-equation treatment of growing
  networks (Dorogovtsev and Mendes; Krapivsky, Redner and Leyvraz)", the
  method of this paper. THEORY-188 (hyperbolic route to power-law degree)
  is CLAIM-817's cited contrast; no new bearing.
- Not held: Dorogovtsev, Mendes and Samukhin, cond-mat/0004434 (ref. 20,
  overlapping results, PRL 85, 4633), and Redner 1998 (ref. 16, the ISI
  citation data). Candidates for registration if the filer wants them.

No neighbour reading was needed: the work itself was read.

## Step 4: report

This file is the report; returned to the caller 2026-11-22.
