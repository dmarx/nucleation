# Reader notes: LIT-tmpwdtfj (Mitzenmacher 2004)

## Provenance
- Copy read: https://www.eecs.harvard.edu/~michaelm/postscripts/im2004a.pdf
  Kind: the author's faculty page (Harvard EECS), lawful under ADR-074. It is the
  published version: header "Internet Mathematics Vol. 1, No. 2: 226-251", "© A K Peters, Ltd."
  Fetched 2026-11-21: HTTP 200, application/pdf, no bot check. Converted with pdftotext.
- What was read: all of the text, pp. 226-245 (§§1-8, footnotes, Figure 1 caption).
  What was skipped: the reference list (pp. 245-251), consulted only to identify [Kesten 73],
  [Gabaix 99], [Reed 00], [Champernowne 53], [Simon 55], [Yule 25].
- Bibliographic: Vol. 1, No. 2, pp. 226-251. The LIT has no volume, issue or pages; the filer may add them.
- No other copy was sought because this one was read. No other work was read or quoted.

## Summary
A survey for computer scientists, prompted by Downey's argument that file sizes are lognormal and
not power-law. It covers the definitions and the log-log closeness of the two laws (§2); preferential
attachment from Yule (1925) and Simon (1955) to the Web-graph models (§3); Mandelbrot's
optimization derivation of Zipf's law and the Simon-Mandelbrot dispute (§4); Gibrat's multiplicative
process and the lognormal, and Champernowne's model, where a minimum income turns the same process
into a power law (§5, §5.1); Miller's monkeys typing at random and the Perline lognormal confusion
(§6); and random observation time, which gives Reed's double Pareto (§7). It concludes that the two
are so closely connected that a definitive answer may not be possible, and that power laws may be
"more robust" models (§8).

## Contribution
A historical and expository map, not new theorems. Its own contributions are the Fibonacci monkey
example (§6), the observation that the monkey power law is a geometric mixture of lognormals (end of
§7), and its recursive-tree file-size model (cited from Mitzenmacher 02). Its thesis: "Very similar
basic generative models can lead to either power law or lognormal distributions, depending on
seemingly trivial variations" (§1, p. 227).

## Key results (with verbatim quotes)
1. Lognormal looks like a power law (§2, p. 229): "if the variance of the corresponding normal
   distribution is large, the distribution may appear linear on a log-log plot for several orders
   of magnitude." This is shown via the quadratic term of ln f(x), eq. (2.2).
2. Preferential attachment (§3, pp. 230-231). A new page links uniformly with probability α, else in
   proportion to indegree; the mean-field recurrence gives c_j ~ c j^(-(2-α)/(1-α)). "the first
   similar argument dates back to at least 1925. It was introduced by Yule" (p. 232). Simon's argument
   "is painfully similar to the outline above" (p. 232). The recursive tree (attachment ∝ 1 + children)
   is "essentially equivalent ... with the probability α ... equal to 1/2" (p. 233).
3. Optimization (§4, pp. 233-235). In Mandelbrot's argument, minimizing cost per unit entropy with
   C_j ~ log_d j gives p_j as a power law. On the "heated exchange" with Simon: "economists appear to
   have given the nod to Simon and the preferential attachment model" (p. 235).
4. Multiplicative to lognormal (§5, p. 236): "if the ln F_k are independent and identically
   distributed variables with finite mean and variance, then asymptotically X_j will approach a
   lognormal distribution."
5. A floor turns it into a power law (§5.1, pp. 237-238). Champernowne's chain: F = 1/2 with
   probability 2/3 and 2 with probability 1/3, with a lowest class. This gives Pr[X ≥ x] = m/x.
   "In the multiplicative model, income can become arbitrarily close to zero through successive
   decreases; in the Champernowne model, there is a minimum income ... This small change allows one
   model to produce a power law distribution while the other produces a lognormal. As long as there
   is a bounded minimum that acts as a lower reflective barrier to the multiplicative model, it will
   yield a power law instead of a lognormal distribution. The theory of this phenomenon is more fully
   developed in [Gabaix 99, Kesten 73]."
6. Another simpler mechanism may exist (§6, p. 238): "Just because one finds a compelling mechanism
   to explain a power law does not mean that there are not other, perhaps simpler, explanations."
   With equal letter probabilities, monkeys give q_j = q · r_j^(log_n(1-q) - 1) for rank r_j = n^j (p. 239). The paper
   rebuts Perline's claim that unequal letters give a lognormal: "for each value of m we obtain a
   slightly different lognormal distribution", so the limit "need not be lognormal" (p. 240).
7. Random stopping time (§7, pp. 241-242): "instead of examining X_t for a specific value of t, we
   examine the random variable X_T where T itself is a random variable." The case of lognormal with
   mean 0 and variance t, stopped at Exp(λ), gives f(x) ∝ x^(-1-√(2λ)) for x ≥ 1 and x^(-1+√(2λ))
   for x ≤ 1, which is the double Pareto (Reed 00). It credits Montroll and Schlesinger (geometric
   mixture: "essentially a lognormal body but a power law distribution in the tail") and Huberman
   and Adamic (exponential site ages on an exponentially growing Web).
8. Its own model (§7, p. 243): new roots arrive with probability γ, otherwise a uniformly chosen node
   has a child whose size is the parent's times a D2 factor. Depths are geometric, so the size is "a
   geometric mixture of lognormally distributed random variables ... In fact, the tail behaviors are
   the same." The monkeys case is "a geometric mixture of approximately lognormal random variables
   ... hence, the resulting power law is unsurprising" (pp. 243-244).
9. Conclusions (§8, p. 244): "Given the close relationship between the two models, it is not clear
   that a definitive answer is possible"; "The fact that power law distributions arise for
   multiplicative models once the observation time is random or a lower boundary is put into effect,
   however, may suggest that power laws are more robust models." It recommends the double Pareto.
   An open question: when the small differences "manifest themselves in vastly different qualitative
   behavior" (pp. 244-245).

## Assumptions
- The derivations are "intuitive ... rather than rigorous" (§1). §3 uses a mean-field
  steady-state ansatz X_j = c_j t, which the paper justifies by pointing to Kurtz and Wormald.
- §5 assumes i.i.d. log-multipliers with finite mean and variance. §5.1 uses one worked example and
  states the general floor result without conditions, deferring to Kesten and Gabaix.
- §7 assumes zero-drift lognormal growth with variance t, a continuous number of steps, and
  exponential T.

## Concepts
Power law and Pareto; lognormal; law of proportionate effect (Gibrat); multiplicative process;
preferential attachment (Yule, Simon); recursive trees; Mandelbrot's optimization (cost per unit
entropy); Champernowne's model; lower reflecting barrier; monkeys typing (Miller); Anscombe's CLT;
random observation or stopping time; double Pareto and double Pareto-lognormal (Reed); geometric
mixture of lognormals.

## Verdict on the exchange's characterization
The exchange's reasons for citing the work are accurate: the history of preferential attachment
(Yule, Simon) and of multiplicative models (Gibrat, Kapteyn, McAlister); the closeness of the two laws;
and the floor and the random stopping time each turning a lognormal into a power law (§5.1, §7, §8).
Three cautions:
- The paper's floor is a lower reflecting barrier, a minimum income. It is not Kesten's additive B.
  The paper does not give E[A^κ] = 1, and it states no conditions; it defers to Kesten 73 and Gabaix 99.
- It never treats attachment kernels k^α with α ≠ 1. Its α is the probability of a uniform choice.
  CLAIM-tmpepx9m cites it beside A3's "preferential attachment alone does not guarantee this result";
  the paper does not say that. The kernel regimes are Krapivsky, Redner and Leyvraz, not Mitzenmacher.
- It does not identify preferential attachment with the age mechanism. It keeps §3 and §7 separate,
  joined only by its recursive-tree model.

## Bearing on the named codes
- **CLAIM-tmpiervv: supports, and qualifies.** For the lognormal half, see result 4. For the floor
  half, see result 5. The Champernowne example instantiates the claim's formula, though the paper
  does not say so. With E[F^κ] = (2/3)2^(-κ) + (1/3)2^κ = 1, κ = 1, which is the paper's m/x
  (checked by hand). E[ln F] = -(1/3)ln 2 < 0 while E[F] = 1, so it "contracts on average" in log
  terms with a constant mean. The qualification is that the paper's floor is reflecting, not additive.
  The claim's "additive floor" is one form; "a bounded minimum that acts as a lower reflective barrier"
  is the other. Neither the conditions nor the κ formula are in this paper. The claim's three-way
  account (entry, floor, both) matches §8's two routes, "observation time is random or a lower
  boundary is put into effect".
- **CLAIM-tmply70l: background; supports the age half and leaves the identification open.** §7 shows
  multiplicative growth with exponentially distributed ages giving a power law (Huberman and Adamic,
  Reed), and that Web growth makes ages exponential. That is the "entry makes the Pareto" ingredient,
  for Gibrat growth. The paper's §3 attachment model always has entry (a new page each step), and it
  never considers attachment without entry or casts §3 in log-time. It also gives the exponent of the
  mixture with uniform choice, (2-α)/(1-α) in density, which at α = 1/2 is 3, the BA k^(-3).
- **CLAIM-tmp8h6nt: supports.** Result 6 says almost the claim's first clause. Result 1 says a lognormal
  can look straight on log-log for orders of magnitude, and result 9 says it is "not clear that a
  definitive answer is possible". The monkeys show one law with three mechanisms: preferential
  attachment, optimization and random typing. There is a qualification: §2 calls the log-log straight
  line "a simple empirical test", and the paper gives no fitting method and none of the claim's
  dynamical tests.
- **CLAIM-tmpepx9m: background, with one point of support and one mismatch.** It supports the history
  and the identity of the feedback (Yule, Simon, Web models). Its α-mixture, uniform plus
  proportional, is a shifted linear kernel that moves the exponent, which agrees with the claim's
  `defeated_if` carve-out. The mismatch is that the paper has nothing on sublinear or superlinear
  kernels, or on "both ingredients are needed". The grounds should not lean on it for those.
- **THEORY-2131 (held): parallel.** §7 has the same structure as Sozou's: average a time-indexed family
  over an exponential distribution of the time and a power law appears (∫λe^(-λt)·lognormal_t dt
  → x^(-1-√(2λ))). Sozou averages exponentials over an exponential spread of hazards and gets a
  hyperbola.
- **CLAIM-769 (held): parallel, adding a case.** It is a further instance of "averaging over a spread
  gives a power law". Here the spread is of observation times, not of rates. The paper does not make
  this connection.

## Recheck (grep of record/ after reading)
I searched for Champernowne, Kesten, Gibrat, Yule, Simon, Zipf, double Pareto, Reed, monkey, Mandelbrot,
Gabaix, lognormal, Huberman, Pólya urn, reflecting barrier and Lotka. The search turned up these,
beyond the named codes:
- **CLAIM-tmp1dlyp** (Proposed, "Power laws arise from many mechanisms with no positive feedback").
  Its list lacks two routes this paper gives: random typing (Miller's monkeys, §6), and optimization
  (Mandelbrot, with Carlson-Doyle HOT, §4). Both need no positive feedback, and the random-typing route
  at least plainly belongs on the list. Its item 6 (growth with a spread of ages) is supported by §7,
  and the paper adds the zero-drift exponent 1+√(2λ). The bearing is that it supports item 6 and
  points to an omission.
- **SYNTHESIS-tmp69tyj** (Proposed, "a power law does not identify its mechanism"): supports, by the
  same passages as for CLAIM-tmp8h6nt.
- **QUESTION-tmp21jtb** (Open, "What fixes the exponent"): the paper gives three exponent formulas.
  For attachment it is the mixing probability, (2-α)/(1-α). For a stopping time it is the balance of
  stopping rate and variance, √(2λ). For the Champernowne floor it is the up and down probabilities
  (κ = 1 here). That is evidence for the "balance of growth against loss" option.
- **CLAIM-tmp9a83b** (Proposed): no direct bearing; the paper does not discuss criticality.
- Already registered and Deferred, so not missed: LIT-tmpx9axf (Kesten), LIT-tmpyexjc (Reed),
  LIT-tmpchmeb (Newman 2005).
- **LIT-1127** (Simon, "Aggregation of Variables", Unavailable) is a different Simon work.
- The Kesten hits in THEORY-456 and THEORY-407, the Huberman hits in THEORY-1117 (Bachas and Huberman),
  and the Gabaix hit in NOTE-873 are unrelated.
- No held entry covers Champernowne, Miller's monkeys, Mandelbrot's 1953 optimization or the double
  Pareto.

## Limitations
- The paper is expository and non-rigorous. It gives the floor result by one example and the double
  Pareto for the zero-drift case only.
- It is from 2004. It predates Clauset, Shalizi and Newman (2009), so it has no statistical method for
  telling the two laws apart. Its empirical test is the log-log line.
- It does not cover kernels other than linear, aging or fitness, or criticality.

## Candidate THEORY
Sentence: "Mitzenmacher's survey traces preferential attachment from Yule (1925) and Simon (1955) to
the Web-graph models, and Gibrat's multiplicative process to the lognormal, and shows that the
lognormal can look straight on a log-log plot for orders of magnitude and that small changes to the
multiplicative process turn its lognormal into a power law: a lower reflecting barrier
(Champernowne's minimum income gives Pr[X ≥ x] = m/x) or an exponentially distributed observation
time (Reed's double Pareto, with tails x^(-1∓√(2λ)))."
- source: LIT-tmpwdtfj. The work was read in full, so this could be Active.
- If filed Proposed, promote_when: "§5.1 and §7 of the published version confirmed, by a second
  reading or by the owner, to state that a lower reflecting barrier turns the multiplicative model's
  lognormal into a power law and that an exponential observation time gives the double Pareto with
  exponents -1∓√(2λ)."
