# Reader notes: barabasi (LIT-3004, LIT-2968)

## Step 1: copies located (2026-11-22)

- LIT-3004: arXiv preprint https://arxiv.org/abs/cond-mat/9910332 (v1, submitted
  21 Oct 1999; journal ref "Science 286, 509 (1999)"); PDF
  https://arxiv.org/pdf/cond-mat/9910332 fetched, HTTP 200. Kind: arXiv
  (author's manuscript).
- LIT-2968: https://networksciencebook.com/translations/en/partials/ch-5.html,
  HTTP 200, text/html, 107,697 bytes. Kind: the author's own book site.

## Step 2: read (2026-11-22)

- LIT-3004: arXiv v1 PDF read in full (11 pp.: text, references and notes,
  figure captions; figures seen only as extracted axis text). OpenAlex
  (no email sent) lists arXiv as the only OA location (green), plus
  CiteSeerX summaries of the submitted version. The Science page
  https://www.science.org/doi/10.1126/science.286.5439.509 returned 403
  with a Cloudflare "Just a moment..." challenge on 2026-11-22; stopped,
  not retried. So the published version is not read.
- LIT-2968: the chapter partial read in full, prose and its 94 MathJax
  (math/tex) equations, Sections 5.1 to 5.16 incl. Advanced Topics and
  bibliography; the 19 figures read only by caption.

## Step 3: recheck (2026-11-22)

Grepped record/ for Krapivsky, Jeong, copying model, link selection,
Linearized Chord / Bollobás, first-mover, Bianconi / fitness, stretched
exponential, Mandelbrot, dynamical exponent, Dorogovtsev, Fabrikant,
Papadopoulos / popularity versus similarity, Price, Pólya urn,
Watts–Strogatz and scale-free. The held entries the first search missed
are under "Recheck" below, each with its bearing. None of these had a
hit: the copying model, link selection, the LCD or Bollobás, Fabrikant's
optimisation model, "dynamical exponent".

---

# Report

## (1) LIT-3004: Barabási and Albert (1999), "Emergence of Scaling in Random Networks"

### Provenance
- **Read**: arXiv preprint cond-mat/9910332v1,
  https://arxiv.org/pdf/cond-mat/9910332. PDF, 11 pp., submitted 21 Oct
  1999; arXiv gives the journal ref "Science 286, 509 (1999)". Kind:
  arXiv, the authors' submitted version (OpenAlex: `submittedVersion`).
  Read in full: the text, references and notes 1–20, and the captions of
  Figs. 1–2. The figures were seen only as axis text.
- **Not read**: the published Science version.
  https://www.science.org/doi/10.1126/science.286.5439.509 returned 403
  with a Cloudflare "Just a moment..." challenge on 2026-11-22. I stopped
  there and did not retry. The print text may differ from the preprint,
  so every quote below is from the preprint.
- **Other locations**, from the OpenAlex API by DOI (no email sent):
  - PubMed 10521342, an abstract record, not fetched;
  - six CiteSeerX summary pages of the submitted version
    (10.1.1.226.2025, .305.7919, .401.2501, .408.9676, .411.6891,
    .719.7426), not fetched because the arXiv copy was read.

  OpenAlex gives oa_status green, with the arXiv PDF as oa_url.

### Summary
The paper reports power-law degree tails in four networks: actors
(γ = 2.3 ± 0.1), WWW in-links (2.1 ± 0.1), the western-US power grid
(about 4) and citations (3, after Redner). It argues that the Erdős–Rényi
and Watts–Strogatz models miss these tails because they fix N and link
uniformly. It proposes a model with two ingredients:
- growth: one new vertex with m edges each step;
- linear preferential attachment: Π(k_i) = k_i/Σ_j k_j.

Simulation gives a stationary γ = 2.9 ± 0.1 and a mean-field argument
gives γ = 3. Two variant models show that both ingredients are needed.

### Contribution
Three things:
- growth plus preferential attachment, named as the generic mechanism for
  scale-free degree distributions;
- the mean-field derivation of γ = 3 from the arrival-time argument;
- the argument from removing one ingredient at a time (Models A and B).

It also claims that the result generalises across networks.

### Key results (preprint page numbers)
- **The model** (p. 5): "starting with a small number (m0) of vertices, at every timestep we add a new vertex with m(≤ m0) edges … Π(ki) = ki/Σj kj". Simulation: "an exponent γmodel = 2.9±0.1 (Fig. 2A)"; "P(k) is independent of time … the system organizes itself into a scale-free stationary state."
- **Model A**, growth without preference (p. 6): "Such a model (Fig. 2B) leads to P(k) ∼ exp(−βk)."
- **Model B**, preference without growth (p. 6): "In model B we start with N vertices and no edges … While at early times the model exhibits power-law scaling, P(k) is not stationary … after T ≃ N² timesteps the system reaches a state in which all vertices are connected." Conclusion: "both ingredients, namely growth and preferential attachment, are needed for the development of the stationary power-law distribution."
- **Mean field** (pp. 6–7): "∂ki/∂t = ki/2t, which gives ki(t) = m(t/ti)^0.5 … older (smaller ti) vertices increase their connectivity at the expense of the younger … a ”rich-gets-richer” phenomenon". Then "Assuming that we add the vertices at equal time intervals … 1 − m²t/k²(t + m0)", which at long times gives "P(k) = 2m²/k³, giving γ = 3, independent of m."
- **Nonlinear kernel** (p. 7): "while in general Π(k) could have an arbitrary nonlinear form Π(k) ∼ k^α, simulations indicate that scaling is present only for α = 1."
- **Other exponents** (p. 7): "if we assume that a fraction p of the links is directed, we obtain γ(p) = 3 − p, which is supported by numerical simulations". No derivation is given. Note 16: "choosing m randomly will not change the exponent γ".
- **Generality** (pp. 7–8): "we expect that the scale-invariant state … is a generic property of many complex networks". On inequality: "the scale-free inhomogeneities are the inevitable consequence of self-organization due to the local decisions made by the individual vertices, based on information that is biased towards the more visible (richer) vertices, irrespective of the nature and the origin of this visibility."

### Assumptions
- Edges are undirected and m is constant.
- Vertices arrive at equal time intervals.
- The kernel is exactly linear, with no offset.
- There is no rewiring, no edge added between existing vertices, and no
  deletion.
- k_i is treated as a deterministic continuum (mean field).
- The empirical exponents are dashed lines drawn on log–log plots ("The
  dashed lines have slopes"). No fit or test is given.

### Concepts
Growth; preferential attachment; the scale-free stationary state;
rich-gets-richer; the mean-field continuum rate equation; the
arrival-time (age) argument; Models A and B as tests that remove one
ingredient; the nonlinear kernel k^α.

### Verdict on how the exchange characterised it
**Accurate.** LIT-3004's summary and CLAIM-817's "base case" match
pp. 6–7: dk_i/dt = k_i/2t, k_i ≈ (t/t_i)^(1/2), uniform births,
P(K ≥ k) ∝ k^(−2), P(K = k) ∝ k^(−3). The record drops the factor m,
which is harmless at m = 1. Two refinements:
- 3 is the mean-field exponent; the simulated one is 2.9 ± 0.1.
- A3 said that attachment alone does not guarantee the result, and that
  growth and the form of attachment matter. CLAIM-817 could not ground
  this in Mitzenmacher, but **this paper says it**: Models A and B,
  "both ingredients … are needed", and "scaling is present only for
  α = 1". The paper is a lawful ground for that clause.

### Bearing on the named codes
- **CLAIM-817: supports** both halves at the base case.
  - Growth is necessary (Model B, p. 6).
  - Preference is necessary (Model A).
  - Only a linear kernel gives a power law (p. 7). The regimes for α ≠ 1
    come from KRL (LIT-2974) and the chapter below, not from this paper.
  - The closing "irrespective of the nature and the origin of this
    visibility" supports "unequal outcomes need no unequal ability".
- **CLAIM-830: supports the premise and qualifies one contrast.**
  - The premise is the arrival-time derivation at equal intervals. The
    paper does not cast it in log time and does not mention Gibrat.
  - The claim says that without entry, linear attachment among fixed
    nodes "is a Pólya urn with a near-exponential spread". Model B
    qualifies this. It is a fixed-N model with preferential attachment,
    and "at early times … exhibits power-law scaling" before it ends as a
    complete graph.
  - This does not defeat the claim under its `defeated_if`, since the
    tail is transient and not stationary.
  - Model B also differs from the urn: it starts with no edges, so
    unconnected vertices are drawn in as the first links arrive. On my
    reading (not the paper's), those vertices act as entrants. The claim
    could note this case.
- **QUESTION-505: bears on it, and leaves it open.** γ = 3 is
  "independent of m". γ(p) = 3 − p is stated without derivation and is
  not obviously a ratio of rates, so it is a candidate row that the
  "partial pattern" must fit or set aside.
- **NOTE-tmpleyjh / THEORY-tmphcnj3: contrast.**
  - The paper's generality claim rests on four networks with slopes
    drawn by eye: "independent of the system and the identity of its
    constituents … decays as a power-law" (p. 2) and "a generic property
    of many complex networks" (p. 7).
  - This is the premise Broido and Clauset test, and most networks fail
    their test. THEORY-tmphcnj3 qualifies the work, as LIT-3004's note of
    2026-11-22 already says.
  - The power grid (γ ≃ 4 on 4941 vertices, with "less prominent"
    scaling) is the kind of infrastructure network that BC class Not
    Scale Free. They name roads and airports; I did not check the power
    grid in BC.

### Limitations
- This is the preprint, not the print version.
- The empirical claims carry no statistics.
- The nonlinear-kernel result is one sentence ("simulations indicate").
- γ(p) = 3 − p has no derivation.

### Candidate THEORY
"Barabási and Albert grow a network by one vertex with m edges per step,
attached with probability proportional to degree. They find:
- by simulation, a stationary degree distribution P(k) ∼ k^(−γ) with
  γ = 2.9 ± 0.1;
- by a mean-field argument, k_i(t) = m(t/t_i)^(1/2) and P(k) = 2m²/k³;
- an exponential distribution without preferential attachment;
- a non-stationary distribution tending to a complete graph without
  growth;
- scaling only for a linear kernel.

They propose growth and preferential attachment as the generic origin of
the power-law degree tails they report for actor, Web, power-grid and
citation networks."

`promote_when`: the published Science text is confirmed to carry these
results as the preprint states them (a lawful copy of the print version,
or a later author statement), and the filer rechecks the mean-field
steps, which I checked by hand.

---

## (2) LIT-2968: Barabási, *Network Science*, Chapter 5, "The Barabási-Albert Model"

### Provenance
- **Read**: https://networksciencebook.com/translations/en/partials/ch-5.html,
  an HTML fragment (HTTP 200, 107,697 bytes), fetched 2026-11-22. Kind:
  the author's own book site.
  - The fetched pages carry no licence or permission statement: neither
    the partial nor https://networksciencebook.com/, which is a
    JavaScript shell. I did not look further.
  - Read in full: §§5.1–5.12, Boxes 5.1–5.3 and 5.5, the Advanced Topics
    (§§5.13–5.15, labelled "4.A–4.C" in this edition), the bibliography
    [1]–[36], and all 94 equations (math/tex scripts, extracted).
  - Skipped: the 19 figures as images (captions read), including Image
    5.2's history timeline; Videos 5.1 and 5.2.
- The web edition is undated. LIT-2968 takes 2016 from the Cambridge
  print edition, which I did not check.

### Summary
The chapter motivates growth and preferential attachment, then defines
the BA model and its exactly solvable version, the LCD (Bollobás et al.).
It derives:
- the degree dynamics k_i = m(t/t_i)^β, with β = 1/2;
- the degree distribution by continuum theory, γ = 1/β + 1 = 3;
- the exact distribution by rate equation,
  p_k = 2m(m+1)/[k(k+1)(k+2)].

It goes on to:
- Models A and B (each without one ingredient);
- measuring Π(k) in data;
- the regimes of a nonlinear kernel, after KRL;
- where linear attachment comes from: local rules (link selection,
  copying) and optimisation (Fabrikant et al.);
- diameter and clustering;
- the model's limits.

### Key results
- **Degree dynamics** (§5.4, eqs. 5.3–5.8): dk_i/dt = k_i/(2t − 1) ≈ k_i/2t, "k_i(t) = m(t/t_i)^β", "β = 1/2". "The earlier node i was added, the higher is its degree ki(t). Hence, hubs are large because they arrived earlier, a phenomenon called first-mover advantage."
- **Continuum theory** (§5.5, Box 5.3, eqs. 5.9–5.15): "p(k) ≈ 2m^{1/β}k^{−γ}" with "γ = 1/β + 1 = 3", and "(5.10) links the degree exponent, γ … to the dynamical exponent β". It assumes "In the model we add a node at equal time step" and gives "P(k) = 1 − (m/k)^{1/β}".
- **Exact law** (§5.5 eq. 5.11; Advanced Topic, eqs. 5.31–5.41): "While the continuum theory predicts the correct degree exponent, it fails to accurately predict the pre-factors"; "p_k = 2m(m+1)/(k(k+1)(k+2))". It follows from p_m = 2/(m+2) and p_k = (k−1)/(k+2)·p_{k−1}. I checked by hand that it satisfies both and sums to 1. The chapter attributes it to Dorogovtsev–Mendes–Samukhin [12], KRL [13] and Bollobás et al. [10].
- **Model A** (§5.6, eqs. 5.16–5.18): k_i(t) = m ln(e(m0+t−1)/(m0+t_i−1)), and "p(k) = (e/m) exp(−k/m)".
- **Model B** (§5.6, eq. 5.19): "As Π(0)=0 nodes with k=0 are assumed to have k=1". "At early times, when there are only a few links in the network (i.e. L ≪ N), each new link connects previously unconnected nodes. In this stage the model's evolution is indistinguishable from the Barabási-Albert model with m=1 … the model develops a degree distribution with a power-law tail". "Yet, pk is not stationary … the degree develops a peak … the network becomes a complete graph." §5.11: "if one of them is absent, either the scale-free property or stationarity is lost".
- **Measuring Π(k)** (§5.7, eqs. 5.20–5.22): Δk_i/Δt ∼ Π(k_i) from two snapshots, and the cumulative π(k), which goes as k with no preference and as k² if attachment is linear. "For the Internet and citation networks we have α ≈ 1 … For the co-authorship and the actor network the best fit provides α=0.9±0.1". Image 5.10's caption: "these measurements only consider links added through the arrival of new nodes".
- **Nonlinear kernel** (§5.8, eqs. 5.23–5.25, Image 5.12; Advanced Topic 5.14, after KRL [13]):
  - 0 < α < 1: "the degrees follow the stretched exponential", p_k ∼ k^{−α} exp(−2μ(α)k^{1−α}/(⟨k⟩(1−α))), with k_max ∼ (ln t)^{1/(1−α)}.
  - α > 2: "a winner-takes-all phenomenon: almost all nodes connect to a few super-hubs".
  - 1 < α < 2: "less extreme, but similar".
  - α > 1: k_max ∼ t, and "Strictly speaking a stationary degree distribution only exists if α ≤ 1".
  - Conclusion: "Π(k) needs to depend strictly linearly on the degrees for the resulting network to have a pure power law pk … This nonlinear Π(k) is one reason the degree distribution of real networks deviates from a pure power-law … for systems with sublinear Π(k) the stretched exponential (5.23) should offer a better fit".
- **Where linear Π(k) comes from** (§5.9):
  - link selection: q_k = kp_k/⟨k⟩;
  - copying: Π(k) = p/N + (1−p)k/2L;
  - the optimisation model C_i = min_j[δd_ij + h_j], scale-free for 4 ≤ δ ≤ N^{1/2}; Papadopoulos et al. [24] are cited among the optimisation routes.
  - "each of the mechanisms discussed above lead to linear preferential attachment … We are not aware of mechanisms capable of generating nonlinear preferential attachment".
- **Claimed sufficiency** (§5.11): "We offered a necessary and sufficient argument … To date all known models and real systems that are scale-free have been found to have preferential attachment."
- **Limits** (§5.11): "The model predicts γ=3 while the degree exponent of real networks varies between 2 and 5". It is undirected, has no internal links and no removal, and "does not allow us to distinguish between nodes based on some intrinsic characteristics".
- **Other exponents** (Homework):
  - a directed BA model with attractiveness A, Π ∝ k_in + A: "For A = 0 the scaling exponent … is different from γ = 3";
  - directed copying: "γ_i = (2 − p)/(1 − p)".

### Assumptions
- Time is event time (t = N, Box 5.2), and nodes arrive at equal steps.
- Edges are undirected and m is constant.
- The kernel is exactly k or k^α, with no offset.
- Only arriving nodes add links.
- The dynamics are treated as a continuum; p_k comes from rate equations
  in the stationary limit.
- In Model B, k = 0 is counted as 1.

### Concepts
Growth; preferential attachment; the LCD; the dynamical exponent β;
first-mover advantage; event time; continuum theory against rate (master)
equations; stationarity; Models A and B; the cumulative preferential
attachment function π(k); sublinear and superlinear kernels; the
stretched exponential; winner-takes-all and hub-and-spoke networks; link
selection; the copying model; optimisation (Fabrikant, Koutsoupias and
Papadimitriou); "luck or reason" (Simon against Mandelbrot);
⟨d⟩ ∼ ln N/ln ln N; ⟨C⟩ ∼ (ln N)²/N.

### Verdict on how the exchange characterised it
**Accurate, and the chapter carries more than A used.**
- LIT-2968's summary holds: "growth plus preferential attachment, the
  degree exponent, and the model's limits".
- CLAIM-817's kernel table is in §5.8 and Image 5.12: α = 0 exponential,
  0 < α < 1 stretched exponential, α = 1 power law, α > 1
  winner-take-all. The chapter credits it to KRL [13], so it can ground
  the table as a secondary source, and the table need not rest on the
  unread LIT-2974 alone.
- For α > 1 the chapter backs CLAIM-817's sharper word: there is no
  stationary p_k and k_max ∼ t. That is condensation, not a heavy tail.
  The chapter is looser than KRL on how many hubs ("a few super-hubs").

### Bearing on the named codes
- **CLAIM-817: supports** the whole title. §5.6 shows that both
  ingredients are needed. §5.8 gives the regimes and "Π(k) needs to
  depend strictly linearly".
  - It **qualifies one aside**: "hyperbolic geometry (THEORY-188) needs
    no attachment at all". §§5.9 and 5.11 read geometric and
    optimisation models as *generating* linear attachment, citing
    Papadopoulos et al. [24], and say "all known models … that are
    scale-free … have preferential attachment".
  - This is a rival framing, and the chapter does not refute the aside.
- **CLAIM-830: supports the premise, the age reading and the caveat, and
  leaves the identification open.**
  - The age mechanism: "hubs are large because they arrived earlier",
    and γ = 1/β + 1 (5.10). The survival exponent 1/β = 2 is the claim's
    λ/g.
  - The caveat: "fails to accurately predict the pre-factors" matches the
    claim's "accounts for the exponent … not for any one node's degree".
  - Not in the chapter: log time, or any comparison with Gibrat. Gibrat
    [4] appears only in the bibliography.
  - Model B qualifies the Pólya-urn contrast, as under LIT-3004. But the
    chapter says the early phase "connects previously unconnected nodes"
    and "is indistinguishable from the Barabási-Albert model with m=1".
    That is entry in effect, so on this reading Model B is evidence *for*
    the claim's thesis (the reading is the filer's, not the chapter's).
- **QUESTION-505: supports the partial pattern.**
  - (5.10) makes γ − 1 = 1/β, the entry rate over the growth rate.
  - Directed copying's γ = (2 − p)/(1 − p) is the formula already noted
    from Mitzenmacher.
  - The attractiveness A shifts the exponent, as Newman's k + c does.
  - No counterexample.
- **NOTE-tmpleyjh / THEORY-tmphcnj3: a parallel and a contrast.**
  - Parallel: §5.8 says sublinear Π(k) "is one reason the degree
    distribution of real networks deviates from a pure power-law", and
    that a stretched exponential "should offer a better fit". BC test a
    Weibull, which is a stretched exponential.
  - Parallel: §5.7's α ≈ 1 for citations and 0.9 for co-authorship and
    actors fits BC's keeping attachment for citation networks, and their
    finding that social networks are at best weakly scale free.
  - Contrast: §5.11's "necessary and sufficient argument" and "all known
    … scale-free … have preferential attachment" run against BC's
    "relatively weak evidence" about mechanism and their 4% Strongest.
  - Contrast: the chapter's range of 2 to 5 for real exponents sits
    beside BC's median near 2.

### Limitations
- The figures were not read, including Image 5.2's history.
- The web edition has slips. None affects a result quoted above:
  - cross-references are off: §5.8 points to "SECTION 5.7" for the kernel
    and to "SECTION 5.4" for Model A, and Model B's inset is cited as
    "Image 5.7b";
  - the Advanced Topics are labelled 4.A–4.C;
  - (5.52) has a sign error (p_m = −…);
  - (5.58) drops the ln;
  - the α = 1/2 line of (5.65) has k^{−2} in the exponent;
  - Box 5.5 has "Number of Links N = mt".
- Fitness is Chapter 6, outside this chapter.
- §5.7's measurement of Π(k) does not address the confound of fitness
  and age.

### Candidate THEORY
"Barabási's *Network Science* chapter on the Barabási–Albert model
derives k_i = m(t/t_i)^(1/2). From arrival at equal steps, continuum
theory gives γ = 1/β + 1 = 3, and the rate equation gives the exact
p_k = 2m(m+1)/[k(k+1)(k+2)]. It shows that growth without preferential
attachment gives an exponential distribution, and that preferential
attachment without growth gives a non-stationary one tending to a
complete graph. After Krapivsky, Redner and Leyvraz, it states that
Π(k) ∼ k^α gives:
- a stretched exponential for 0 < α < 1;
- winner-take-all hubs with k_max ∼ t for α > 1;

so a pure power law needs linear attachment. It reports measured α ≈ 1
for the Internet and citations and α ≈ 0.9 for co-authorship and actor
networks."

`promote_when`: all three of these hold.
- The filer confirms the rate-equation recursion and its solution
  (checked by hand here).
- The regimes are confirmed against KRL (LIT-2974) or another
  independent derivation.
- The measured α are confirmed as the chapter's report of Jeong, Néda and
  Barabási (2003). The sentence asserts them only as reported.

---

## Recheck: held entries the first search missed

- **CLAIM-806** (linear attachment as a marginal point between a
  stretched exponential and condensation): **supports**. Chapter §5.8,
  Image 5.12 and "Π(k) needs to depend strictly linearly" give the
  regimes on both sides; BA p. 7 gives "scaling … only for α = 1". The
  chapter does not draw the analogy to criticality.
- **CLAIM-803** (a power law does not identify its mechanism; the
  attachment test is confounded by fitness and age): **a parallel and a
  contrast**.
  - §5.7 *is* the "twice the degree, twice the links" test, in the Δk/Δt
    and π(k) form of Jeong, Néda and Barabási (2003).
  - It conditions only on degree at time t, so the confound CLAIM-803
    names goes unaddressed.
  - §5.11's "necessary and sufficient argument" is the inference
    CLAIM-803 rejects.
- **SYNTHESIS-119** (the same thesis as CLAIM-803): the same contrast
  with §5.11. Its bullet on CLAIM-817 and CLAIM-830 is supported, as
  above.
- **THEORY-188 / NOTE-678 / LIT-865** (hyperbolic geometry; popularity
  versus similarity): **a rival framing**. The chapter cites Papadopoulos
  et al. (2012) [24] as optimisation that *generates* preferential
  attachment, where CLAIM-817's aside says geometry needs none. NOTE-678
  already names the rate equations of KRL and of Dorogovtsev–Mendes,
  which the chapter's Advanced Topics use.
- **LIT-2974** (KRL, Deferred): the chapter restates its regimes. It
  stands in only partly: it reproduces the α ≤ 1 derivation (adapted to
  m > 1) and states the α > 1 regimes without derivation.
- **Pólya urn entries** (CLAIM-277, CLAIM-536, THEORY-1927, NOTE-1076,
  NOTE-2025): **background**. The chapter's bibliography lists
  Eggenberger and Pólya (1923) [2] in preferential attachment's history
  (Image 5.2, not read).
- **Mandelbrot–Simon** (LIT-270, CLAIM-795, NOTE-243): **background**.
  Image 5.17's caption frames their dispute as "luck or reason" and says
  "they were both right".
- **Not held**: the copying model, link selection, the LCD, Fabrikant's
  optimisation model and the dynamical exponent β. They are candidates
  for terms, or for claims on where linear attachment comes from, if
  wanted.

## Neighbours and other works read
None was needed: both works were read. OpenAlex's API record served only
as a catalogue lookup, and the Science page was refused (above). No other
work was read or quoted. No email address was sent to any service.
