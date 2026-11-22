# Reader notes: newman2005 (LIT-2976)

Newman, M. E. J., "Power laws, Pareto distributions and Zipf's law",
arXiv:cond-mat/0412004 (v3, 29 May 2006); Contemporary Physics 46, 323-351
(2005), doi:10.1080/00107510500052444 (journal ref and DOI from the arXiv API).

## Step 1: copies located (2026-11-22)

- https://arxiv.org/pdf/cond-mat/0412004 : arXiv preprint (author's
  manuscript, v3), PDF, HTTP 200, 1.52 MB, fetched 2026-11-22. Lawful
  (arXiv). Read.
- https://doi.org/10.1080/00107510500052444 : publisher's version (Taylor &
  Francis). Not sought; the arXiv copy suffices.

## Step 2: read (2026-11-22)

Provenance: https://arxiv.org/pdf/cond-mat/0412004 (resolves to v3, 29 May
2006), PDF, 28 pages, text extracted with pdftotext. Read in full: §I to §V
and Appendices A (rank/frequency plots) and B (maximum-likelihood
exponent). Skimmed: figure data, the reference list. Page numbers are the
PDF's. v3 postdates the journal version (Contemporary Physics 46, 323-351,
2005); differences from the published text were not checked.

### Summary

A tutorial review in three parts. §II, measuring: log-log histograms are
noisy in the tail; logarithmic binning helps; the cumulative distribution
P(x) is better, with exponent α − 1; least-squares slopes are biased, and
the maximum-likelihood estimator α = 1 + n[Σ ln(x_i/x_min)]^(−1) (Eq. 5,
error (α−1)/√n) should be used. Twelve data sets (Fig. 4, Table I) with
fitted exponents, and three broad distributions that are not power laws
(Fig. 5: lognormal bird abundances, stretched-exponential address books,
forest fires with a cutoff). §III, mathematics: normalization needs α > 1;
moments diverge for m ≥ α − 1; ⟨x_max⟩ ~ n^(1/(α−1)); Lorenz curves and
the 80/20 rule, W = P^((α−2)/(α−1)); the power law as the only scale-free
distribution, p(bx) = g(b)p(x); discrete forms (zeta, Yule). §IV,
mechanisms: combinations of exponentials (Miller's random typing, Shannon
information, Reed and Hughes); inverses of quantities; random-walk first
return times (gambler's ruin, taxon lifetimes); the Yule process and its
general form; critical phenomena via percolation and a coarse-graining
argument; self-organized criticality (Drossel-Schwabl forest fire); and
briefly highly optimized tolerance, coherent noise, lognormal
multiplicative processes (a true power law given a lower bound), record
dynamics. §V names the Yule process and criticality with SOC as "perhaps
the two most important".

### Contribution

A pedagogical synthesis, not new results, that (a) put the MLE exponent
estimator and the cumulative plot into common practice, superseded on the
fitting side by Clauset, Shalizi and Newman (LIT-2987, Deferred), and (b)
set out the standard catalogue of generating mechanisms, holding that
there are many and that different ones apply to different cases.

### Key results, with quotes

1. Many mechanisms, not one (§II.A, p. 5): "the conventional wisdom is
   that there are actually many different mechanisms for producing power
   laws and that different ones are applicable to different cases."
2. Log-log histograms are a poor test (§II, p. 3): "Just making a simple
   histogram, however, and plotting it on log scales to see if it looks
   straight is, in most cases, a poor way proceed" [sic]. Least squares "is
   known to introduce systematic biases into the value of the exponent"
   (p. 4): on synthetic α = 2.5 data it gives 2.26 ± 0.02, Eq. 5 gives
   2.500 ± 0.002.
3. Alternatives (§II.B, p. 8): "a power-law model is only one of several
   possibilities for fitting it." Some of Fig. 4's identifications (§II.A,
   p. 7) "should be considered unconfirmed".
4. Scale-free implies power law (§III.E, p. 11): "a power law is the only
   distribution that is the same whatever scale we look at it on", derived
   from p(bx) = g(b)p(x). Same page: "most experimentally observed power
   laws are probably not the result of phase transitions—a variety of
   other mechanisms produce power-law behaviour as well".
5. Combinations of exponentials (§IV.A, p. 13): y exponential with rate a
   and x ~ e^(by) give "a power law with exponent α = 1 − a/b". Miller's
   random typing gives α ≃ 2; Newman objects that real word lengths are not
   exponential (Fig. 7a), then partly rescues it with information content
   ("There may still be some merit in Miller's argument", p. 13). Reed and
   Hughes (p. 14): exponential growth with exponentially distributed death
   times gives a power law in sizes at death.
6. Inverses (§IV.B, p. 14): x = 1/y with p(y = 0) finite gives
   p(x) ~ x^(−2); x = y^(−γ) gives "α = 1+1/γ". Newman answers the
   objection that this "merely generates a power law by assuming another
   one": the input is a physical power-law relation, not a distribution.
   Ising magnetization fluctuations δ = Δm/m: simulated α = 1.98 ± 0.04.
7. Random walks (§IV.C, pp. 15-16): by generating functions, the first
   return time of a 1D walk has f_2n ~ n^(−3/2), "So the distribution of
   return times follows a power law with exponent α = 3/2", with a
   divergent mean. Fossil genus lifetimes α = 1.7 ± 0.3, which Newman calls
   "tenuous" (footnote 16).
8. Yule process (§IV.D, pp. 16-19): master equation (after Simon) gives
   p_k = (1 + 1/m)B(k, 2 + 1/m), α = 2 + 1/m; flowering plants m ≃ 2,
   α ≃ 2.5 against Willis and Yule's 2.5 ± 0.1, but "Most likely this
   agreement is fortuitous" (p. 18). General form with initial value k0
   and offset c: α = 2 + (k0 + c)/m; Barabási-Albert's c = m gives 3, and
   "there doesn't seem to be a good reason for this assumption" (p. 19).
   Names (p. 18): Simon "dubbed this type of “rich-get-richer” process the
   Gibrat principle", also Matthew effect, cumulative advantage,
   preferential attachment. "For several of the distributions shown in
   Fig. 4, especially citations, city populations and personal income, it
   is now the most widely accepted theory" (p. 19).
9. Criticality (§IV.E, pp. 19-21): tuning "makes the divergence of
   length-scales an unlikely explanation for generic power-law
   distributions" (p. 19). Percolation p_c = 0.5927462; a coarse-graining
   argument that at ⟨s⟩ → ∞ p(s) is scale-free and so a power law (tail
   only); finite-size cutoff. No value of τ is given.
10. SOC (§IV.F, pp. 21-22): forest-fire model α = 1.19 ± 0.01, cut off at
    the lattice size; "it is probably not the universal law that some have
    claimed it to be" (p. 22).
11. Other (§IV.G, pp. 23-24): HOT (Carlson and Doyle), coherent noise
    (Sneppen and Newman), the lognormal from products, which looks straight
    on log scales over orders of magnitude when σ is large;
    "random multiplication processes can also generate perfect power-law
    distributions with only a slight modification: if there is a lower
    bound on the value that the product of a set of numbers is allowed to
    take (for example if there is a “reflecting boundary” on the lower end
    of the range, or an additive noise term as well as a multiplicative
    one)" (p. 24); record dynamics (Sibani and Littlewood), waiting times
    with α = 1.

### Assumptions

A continuous power law above an x_min chosen by judgement (no method for
choosing it); MLE with a uniform prior on α and a pure power law above
x_min (Appendix B); a Yule process without extinction, in its stationary
limit; a heuristic coarse-graining ("I've had to fudge things around the
edges", p. 20); a symmetric ±1 walk.

### Concepts

power law, exponent, x_min, cumulative distribution / rank-frequency plot,
Zipf's law, Pareto distribution, logarithmic binning, maximum-likelihood
exponent, divergent moments, Lorenz curve, 80/20 rule, scale-free
distribution, Yule and zeta distributions, Yule process, Gibrat principle,
cumulative advantage, preferential attachment, gambler's ruin, first return
time, percolation, critical point, coarse-graining, finite-size effect,
self-organized criticality, forest-fire model, highly optimized tolerance,
coherent noise, lognormal, multiplicative process, reflecting boundary,
record dynamics.

### Verdict on how the exchange and the record characterized it

LIT-2976's summary (Yule process, critical phenomena, random walks,
combinations of exponentials) is accurate. Two corrections:
- "mixtures" in "(rich-get-richer, criticality, first passage, mixtures)"
  is wrong if it means a mixture of exponential rates (CLAIM-795 item 4).
  Newman's "combinations of exponentials" is an exponential of an
  exponentially distributed variable (x = e^(by)), which is item 6's age
  mechanism, not a gamma mixture. The review has no rate-mixture or
  superstatistics mechanism.
- "first passage": Newman treats the first return to the origin of a
  symmetric walk (gambler's ruin), by generating functions, not first
  passage to a boundary. Same 3/2.
CLAIM-795 calls the review "A's general reference": fair, but it covers
four of the seven items (2 percolation; 3 random walk; 6 Reed and Hughes;
7 inverses, without the d-ball geometry). Not in it: 1 critical branching,
4 rate mixtures, 5 sample-space reduction. It has no-feedback mechanisms
CLAIM-795 lacks: random typing (Miller), HOT, coherent noise, record
dynamics.

### Bearing on the named codes

- CLAIM-795: **supports** items 2, 3, 6 and 7 (in part) (results 5, 6, 7,
  9), with matching formulas: α = 1 − a/b with a = −λ, b = g is density
  exponent 1 + λ/g, i.e. Reed's survival exponent λ/g; x = 1/y gives
  x^(−2); p_c = 0.5927462. **Leaves open** items 1, 4, 5. Adds, without
  defeating, random typing (already noted from Mitzenmacher), HOT, coherent
  noise and record dynamics. A ground for items 2, 3, 6, 7 only.
- CLAIM-815: **leaves open; parallel.** Newman derives the walk's 3/2 by
  generating functions (Eqs. 51-58, pp. 15-16) and never mentions
  branching processes, the cycle lemma or Dwass. He gives the walk half of
  the coincidence, nothing on the identity. The claim's "Newman's review
  ... is unread" can become: read; it has the walk's 3/2 by another route
  and not the link.
- CLAIM-803: **supports** the first clause (result 1; result 4's "most ...
  probably not the result of phase transitions"; Miller, Yule and the
  lognormal all reaching similar slopes) and **supports in part** "fit
  first" (results 2 and 3, the MLE, and the lognormal mimicking a power law
  over four orders of magnitude, §IV.G, p. 24). **Leaves open** the
  comparison with alternatives (no likelihood-ratio test; that is
  LIT-2987) and the three dynamical tests. Newman is milder than the claim:
  §V ranks Yule and criticality "the two most important", and he calls
  Yule "the most widely accepted theory" for citations, cities and income,
  assigning mechanisms by plausibility rather than from dynamics.
- CLAIM-841: **supports** the distributional half: §III.E, p. 11, "most
  experimentally observed power laws are probably not the result of phase
  transitions", and §IV.E, p. 19, tuning makes criticality "an unlikely
  explanation for generic power-law distributions". **Leaves open** the
  routes the claim lists (symmetry, line of fixed points, KPZ, flux,
  coarsening): none is in the review, and footnote 1 (p. 2) puts
  non-statistical power laws out of scope. The routes it does give
  (Yule, combinations of exponentials, inverses, walks, HOT) bear only on
  the "cumulative advantage" and "broad relaxation" rows loosely.
  Background beyond that.

### Limitations

Pedagogical, with heuristic arguments the author flags. x_min by eye; no
goodness-of-fit or model comparison (LIT-2987 later supplied both).
Read as the 2006 v3, not the journal text. Table I's exponents were not
re-examined.

### Candidate THEORY sentence

Newman reviews power-law distributions, recommends cumulative plots and a
maximum-likelihood estimate of the exponent over least-squares fits to
log-log histograms, and holds that many different mechanisms produce power
laws (combinations of exponentials, inverses of quantities, random-walk
first return times, the Yule process, critical phenomena and self-organized
criticality, among others), that different ones apply to different cases,
and that most observed power laws are probably not the result of phase
transitions.

promote_when: an independent source gives the same catalogue with the same
exponents for these mechanisms (α = 1 − a/b, α = 1 + 1/γ, 3/2 for first
return, α = 2 + (k0 + c)/m for the general Yule process) and confirms that
least-squares slopes are biased where the maximum-likelihood estimate is
not.

## Step 3: recheck (2026-11-22)

Grepped record/ for Yule, Simon, Miller/random typing, Reed and Hughes,
highly optimized tolerance, coherent noise/Sneppen, record dynamics/Sibani,
Drossel/forest fire, 80/20/Lorenz, MLE exponent/x_min/Hill, gambler's ruin/
first return, percolation, Zipf, Pareto, reflecting boundary/Kesten,
lognormal, Gibrat, Matthew effect/cumulative advantage, scale-free,
Sornette. Only CLAIM-795, CLAIM-815 and LIT-2976 cite LIT-2976. Held
entries the first search missed, with bearing:

- CLAIM-817 (cumulative advantage gives a power law only with linear
  attachment plus continual entry): **supports** the linear-plus-entry
  half. Newman's Yule process founds one new genus per step (entry) and
  attaches in proportion to k (or k + c), giving α = 2 + (k0 + c)/m
  (§IV.D, pp. 17-19). Leaves open sublinear and superlinear kernels.
- CLAIM-830 (what separates linear attachment from Gibrat growth is entry):
  **supports** the entry point implicitly (entry is built into every Yule
  variant Newman gives) and gives a **terminological contrast** worth
  noting: Newman, after Simon, calls the rich-get-richer rule itself "the
  Gibrat principle" (p. 18), the very name CLAIM-830 reserves for
  lognormal proportional growth.
- CLAIM-824 (multiplicative growth gives a lognormal; with a floor, a power
  law): **supports** both halves qualitatively (§IV.G, p. 24, quote in
  result 11, citing refs 67-69). Gives no exponent condition (no
  E[A^κ] = 1).
- QUESTION-505 (what fixes the exponent): **supports** the "partial
  pattern" table. Newman's exponents are each a ratio: α = 1 − a/b
  (rates), α = 1 + 1/γ (a power), survival exponent (m + k0 + c)/m for
  Yule, the walk's 1/2 survival exponent, and for Miller
  α − 1 = ln m/(ln m − ln(1 − q_s)). Candidate rows for the table: inverse
  powers (1/γ) and random typing.
- LIT-3007 (Reed and Hughes, Deferred): Newman restates its mechanism
  (§IV.A, p. 14, his ref. 43) in two sentences; a neighbour description,
  not a stand-in for reading it.
- LIT-2987 (Clauset, Shalizi and Newman, Deferred): Newman 2005 is its
  predecessor; the MLE of Eq. 5 is the same estimator, without x_min
  selection or tests.
- LIT-3003 / THEORY-2150 (Mitzenmacher, read): Newman cites it as a
  companion review (ref. 19); both have Miller, Yule/Simon, lognormal
  versus power law. Newman adds percolation, SOC, HOT, coherent noise,
  inverses, record dynamics; Mitzenmacher adds Mandelbrot's optimization
  and the double Pareto. Parallel.
- LIT-2992 (Bak, Tang and Wiesenfeld, Deferred): cited by Newman for SOC
  (ref. 57); he illustrates SOC with the forest-fire model instead.
- LEAD-211 (track the cutoff): **background**. Newman notes finite-size
  cutoffs at criticality (footnote 6, p. 6; Fig. 14) and the forest-fire
  cutoff at the lattice size (p. 22), without using the cutoff as a test.
- CLAIM-769 / THEORY-2131 (mixtures of rates): **leaves open**; not in the
  review.
- THEORY-863 / NOTE-1052 (Arthur's adoption walk with absorbing barriers,
  gambler's ruin): parallel only; Newman's gambler's ruin is the lifetime,
  Arthur's the absorption probability.
- NOTE-1394 (Bak-Sneppen) and NOTE-124 (Drossel as a philosopher): name
  hits only, no bearing.

## Step 4: report

Read in full from arXiv. No obstacle met; no other copy needed; no
neighbour read (the work itself was reached). No outside service received
an email address (arXiv PDF and arXiv API, no contact parameters). Other
works quoted: none; the journal reference and DOI come from the arXiv API.

Filer's points:
1. LIT-2976 status: read (arXiv v3), so Deferred can move to Read with a
   NOTE and the THEORY above.
2. Correct LIT-2976's "mixtures" and "first passage" (see the verdict).
3. CLAIM-795: Newman grounds items 2, 3, 6, 7 only; consider naming that in
   the body. CLAIM-815's "is unread" line goes stale.
4. CLAIM-830 might note Newman/Simon's use of "Gibrat principle" for
   attachment.
