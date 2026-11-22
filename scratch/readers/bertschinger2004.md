# Reader notes: bertschinger2004 (LIT-2991)

Bertschinger & Natschläger (2004), "Real-Time Computation at the Edge of
Chaos in Recurrent Neural Networks", Neural Computation 16(7):1413-1436,
doi:10.1162/089976604323057443. Reader: Claude (subagent), 2026-11-22.

## Step 1: copies sought (2026-11-22)

- OpenAlex API, doi:10.1162/089976604323057443: `is_oa: false, oa_status: closed`;
  locations only https://doi.org/10.1162/089976604323057443 (publisher, paywalled)
  and https://pubmed.ncbi.nlm.nih.gov/15165396 (abstract only; no PMC copy).
- Semantic Scholar API: `openAccessPdf.status: CLOSED`. A second API call
  (for the NIPS paper) returned 429 rate limit; stopped there. The S2 web
  page https://www.semanticscholar.org/paper/04c6461e524107198eb98835cd6ba2f7733b3163
  (search snippet says "[PDF]") returned 403 to WebFetch; not retried.
- OpenAlex search API: second query refused, "Rate limit exceeded ...
  free daily budget ... used up"; stopped there.
- TU Graz IGI: https://www.igi.tugraz.at/tnatschl/ -> 404 (now
  https://www.tugraz.at/institute/igi/tnatschl/psfiles/ -> 404).
  igi-web.tugraz.at (the old IGI web host, e.g.
  https://igi-web.tugraz.at/people/maass/publications.html): TLS
  connection reset by peer (curl exit 35), no agent-proxy line. No exact
  address of a copy of this paper on that host was located.
- Wayback capture of the Natschläger page,
  http://web.archive.org/web/20160221061928/http://www.igi.tugraz.at:80/tnatschl/ :
  "Blocked by egress policy" (this session's network policy). Not worked around.
- TU Graz Pure, https://graz.elsevierpure.com/en/publications/?search=... and
  https://tugraz.elsevierpure.com/en/publications/real-time-computation-at-the-edge-of-chaos-in-recurrent-neural-ne/ :
  Cloudflare "Just a moment..." challenge (403). Stopped.
- Web searches found no author, course or repository copy of the Neural
  Computation article itself.

Outcome for the work: no lawful copy located at an exact address ->
**Unavailable** (ADR-041), with the caveat that igi-web.tugraz.at
(reset) and web.archive.org (egress policy) could not be searched; the
owner may allow them.

Neighbour located: the companion NIPS 2004 paper, Bertschinger,
Natschläger & Legenstein, "At the Edge of Chaos: Real-time Computations
and Self-Organized Criticality in Recurrent Neural Networks", NIPS 17,
pp. 145-152, on the proceedings site:
https://proceedings.nips.cc/paper_files/paper/2004/file/f8da71e562ff44a2bc7edf3578c593da-Paper.pdf
(publisher's open proceedings). Not held in record/literature.d (no hit
for the title or "Legenstein" as author).

## Step 2: read (2026-11-22)

What was read:

- **The work's abstract only**, from PubMed via NCBI E-utilities efetch
  (https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15165396&rettype=abstract&retmode=text),
  plain text, no email sent. Body not read.
- **Neighbour N1, read in full** (8 pp., text via pdftotext; figures read
  from their captions and axis labels): Natschläger, Bertschinger &
  Legenstein, "At the Edge of Chaos: Real-time Computations and
  Self-Organized Criticality in Recurrent Neural Networks", Advances in
  NIPS 17 (2004/2005), pp. 145-152. PDF at
  https://proceedings.nips.cc/paper_files/paper/2004/file/f8da71e562ff44a2bc7edf3578c593da-Paper.pdf
  (author order on the PDF: Natschläger, Bertschinger, Legenstein;
  NeurIPS and S2 listings give Bertschinger, Natschläger, Legenstein).
  Kind: the publisher's own open proceedings. Not held in the record.
- **Neighbour N2, one passage**: Calvet, Reulet & Rouat, "The connectivity
  degree controls the difficulty of RBN reservoir design", arXiv:2312.08522v1
  (13 Dec 2023), https://arxiv.org/pdf/2312.08522 . Read: introduction's
  citations of B&N 2004 and the Discussion (pp. 25-26). Not held.
- Mean-field supplement cited by N1 as
  http://www.igi.tugraz.at/tnatschl/edge-of-chaos/mean-field-supplement.pdf :
  redirects to https://www.tugraz.at/institute/iml/tnatschl/edge-of-chaos/mean-field-supplement
  -> 404; igi-web.tugraz.at/people/tnatschl/edge-of-chaos/mean-field-supplement.pdf
  -> TLS reset (curl 35). Not read. 2026-11-22.

How far N1 stands in. N1 says of the work: "A similar analysis for a
restricted case (zero mean of synaptic weights) of the network model
considered in this paper can be found in [4]" ([4] = the work), and that
N1's model "differs in two important aspects: a) By using states xi ∈
{0, 1} ... b) ... the Gaussian distribution from which the non-zero
weights are drawn is allowed to have an arbitrary mean µ". So N1 is a
generalization by the same authors: it restates the work's programme
(mean-field critical line for input-driven threshold networks; computation
on time series peaking at the critical line; the LSM readout test) and
cites the work for the experimental details ("for details see [4]", §5).
It does not restate the work's own model (zero-mean weights, its state
coding), its exact figures, or anything in the work N1 does not repeat.
N1 adds NM-separation as a predictor and the SOC synaptic-scaling rule
(the work, per its abstract, has neither; that NM-separation is new in
N1 is stated: "we propose a novel complexity measure (Sec. 4)").

### Summary (from the abstract and N1)

Randomly connected networks of N binary threshold gates, each with K
inputs whose weights are Gaussian (mean µ, variance σ²), driven by a
random binary input injected into every node. A Derrida-style annealed
mean-field theory of the Hamming distance between two state trajectories
under the same input gives a critical line in (µ, σ²) separating order
(perturbations die, fading memory) from chaos (perturbations persist).
Networks with a trained linear threshold readout are tested on delayed
3-bit parity and random 5-bit Boolean functions; performance is highest
near the critical line.

### Contribution

The order-chaos transition for *input-driven* networks computed
analytically, and an empirical link from it to real-time (online)
computation with a trained readout, as opposed to Langton's and
Derrida's autonomous ("off-line") setting.

### Key results

1. Critical boundary computed (abstract): "we calculate the critical
   boundary in parameter space where the transition from ordered to
   chaotic dynamics takes place." N1 §3, eq. (1): the critical line is
   where P_bf = 1/K, "the probability ... that a node will change its
   output if a single out of its K input bits is flipped"; "ordered,
   critical or chaotic regime if α* < 1, α* = 1 or α* > 1".
2. Computation only near it (abstract): "we show that only near the
   critical boundary can such networks perform complex computations on
   time series." N1 §5: "The highest performance is clearly achieved for
   parameter values close to the critical line" (Fig. 3, MC = Σ_τ MI).
3. Order = fading memory (N1 §3): fading memory "is equivalent to the
   requirement that all state differences vanish, i.e. being in the
   ordered phase"; in chaos the state "contains 'spurious' information
   about the initial conditions".
4. NM-separation (N1 §4, eq. 2): NM_sep = s* − f* − i*, separation from
   input differences minus that from initial conditions (f*) and from
   immediate input drive (i*); it "peaks very close to the critical line"
   (Fig. 2). N1 footnote 4: values are "numerical estimates" of the map,
   "Hopefully ... replaced by analytic results in the future."
5. Generality of tasks (N1 §5): networks "are not optimized for any
   specific task but their computational capabilities are assessed by
   evaluating them for many different tasks. Therefore a network that is
   specifically designed for a single task will not show a good
   performance in this setup."
6. SOC (N1 §6, Figs 4-5; not in the work): a local synaptic-scaling rule
   driving each node's estimated P_bf to 1/K moves networks from either
   side to the critical line, and MC rises to the level of networks set
   critical a priori.
7. Conclusion as worded (abstract): "this result strongly supports
   conjectures that dynamical systems that are capable of doing complex
   computational tasks should operate near the edge of chaos". N1 §7:
   "support the hypothesis that dynamics near the critical line are
   expected to be a general property of input driven dynamical systems
   which support complex real-time computations."

### Assumptions

Annealed (mean-field) approximation, fixed in-degree K, i.i.d. Gaussian
weights, i.i.d. binary input (rate r, offset ū) injected identically into
all nodes, synchronous update, large N (N = 500 in N1's figures), a
linear threshold readout trained per task, tasks on the last few input
bits (memory of a few steps). "Edge of chaos" here is the
damage-spreading transition of a deterministic driven map, not a
critical point of activity.

### Concepts

Edge of chaos; Derrida-Pomeau annealed approximation; damage spreading
(Hamming distance); fading memory; separation property; liquid state
machine / reservoir readout; NM-separation; bit-flip probability P_bf and
the sensitivity condition K·P_bf = 1; synaptic scaling for SOC.

### N2 (Calvet et al. 2023), the passage relied on

Discussion, p. 25: "the edge of chaos, or the critical region, does not
consistently align with the peak performance region ... this alignment
is contingent upon the sign of excitatory-inhibitory balance b"; pp.
25-26: "Refining initial literature (Bertschinger und Natschläger, 2004;
...), the highest-performing region is characterized by a preponderance
of irregular attractors within the disordered region." Random Boolean
network reservoirs, N up to 10000, varying K and balance b. A later
qualification of the work's result, not a restatement of it.

## Step 3: verdict, bearings, recheck (2026-11-22)

### Verdict on the exchange's characterization

- LIT-2991's summary ("Randomly connected threshold networks compute best
  on time series near the transition between ordered and chaotic
  dynamics") matches the abstract. Fair.
- Authorship. A's "Bertschinger, Natschläger, and Legenstein" is not a
  bare error: those three wrote the 2004 NIPS companion (N1). A conflated
  the two 2004 papers. CLAIM-809's "Misattribution" bullet ("Legenstein is
  an author of a separate paper with Maass (2007)") should instead, or
  also, name N1. LIT-2991's status note "he is not one" stays right for
  the NC paper.
- CLAIM-809 strand 1 (ordered forgets; chaotic "separates but cannot be
  read reliably"; near the transition both hold): supported in substance
  by N1 §3-§4 (fading memory = order; chaos carries "spurious"
  information about initial conditions; NM-separation subtracts f*, the
  chaos-driven separation). Note the mechanism: chaos fails because
  separation is polluted by initial conditions, not because of readout
  noise.

### Bearing on each named code

- **QUESTION-507: supports one side, leaves the dilemma open.** The
  abstract's claim ("only near the critical boundary can such networks
  perform complex computations") is the "distinctive capacity" side, for
  one class (driven random threshold networks) and one task family
  (short-memory nonlinear Boolean filters). It does not test the
  "redistribute a bounded capacity" side: no capacity total, no bound.
  On **point 1 (which transition)** it adds something the record lacks:
  the order-chaos line in these networks is defined by K·P_bf = 1 (N1
  eq. 1), the expected number of nodes a single flipped bit flips in the
  next step, i.e. a *branching ratio of perturbations (damage)* equal to
  one. That is a formal bridge between the edge of chaos and branching
  criticality, but of damage, not of activity: N1 Fig. 1 shows the mean
  activity a* varying widely along the critical line (0.4 to 0.8). So the
  two transitions are related by analogy of their order parameter, not
  identified. (This reading of eq. 1 is the reader's, Claude's; the paper
  does not draw it.) **Point 2 (measure)**: the measure is memory capacity
  as summed MI on Boolean tasks, and NM-separation as predictor; one
  measure family, both peaking at the line. **Point 3 (environment)**:
  silent; input i.i.d. binary.
- **CLAIM-809: qualifies (in tension with the headline, consistent with
  the conditions).** The abstract's "only near the critical boundary"
  and N1 §7's "general property of input driven dynamical systems" are
  the universal reading the thesis rejects. But the design is what makes
  the optimum land at the line: N1 §5 averages over "many different
  tasks", and says a network "designed for a single task will not show a
  good performance in this setup". That is a task-averaged optimum, which
  the thesis allows ("A single task whose optimum sits at the transition
  does not defeat it"); the paper does not report per-task optima or
  allocation, so it neither defeats nor supports the redistribution
  clause. The defeater asks for "every component ... maximized at the
  transition for every task"; this work does not show per-task or
  per-component maxima, so it does not meet it. Strand 1 is supported
  (above). N2 (Calvet et al.) adds that in RBN reservoirs the peak
  "does not consistently align" with the edge and lies "within the
  disordered region" for some balances, which supports the thesis's
  "best distance depends" clause against the work's "only near".
- **CLAIM-814: parallel/contrast.** Different system (nonlinear,
  high-dimensional, binary) and a different edge (damage spreading vs a
  scalar's marginal linear stability). In CLAIM-814 the chaotic side does
  not exist; in this work the failure past the edge is loss of fading
  memory, a cost CLAIM-814's linear model cannot show. Nothing in it
  bears on the scalar derivation.
- **ARG-148: background/contrast.** ARG-148 notes its case leaves "the
  trade of linear memory for nonlinear transformation" untouched; this
  work is the classic case where nonlinear tasks (parity) are the test,
  so it marks the territory ARG-148 says it does not reach. It does not
  supply an existence case of redistribution.
- **THEORY-tmpye6xs (Azizpour et al.): contrast.** Opposite transition
  type and opposite direction: Azizpour's branching network has its
  finite-window optimum subcritical; here the optimum sits on the
  order-chaos line (N1's Fig. 3 shows performance near, and on parts of
  the line on the chaotic side; read from the figure, not stated). Azizpour
  itself says the side "will ... depend on both the task and the type of
  phase transition", citing Toyoizumi & Abbott (LIT-tmpfn6b8) for the
  chaotic side; this work is a further example on the order-chaos side,
  with no finite-window analysis.

### Limitations

Body of the NC paper unread: its zero-mean model, its exact tasks,
figures, network sizes and any caveats it states are not known here;
everything beyond the abstract is through N1, a generalization by the
same authors. N1's NM-separation is numerical, not analytic (fn. 4).
Mean-field (annealed) theory; finite N = 500; tasks need memory of only a
few steps; one input statistic; "performance near the line" is read from
interpolated gray-scale images (Fig. 3 caption: "an interpolation between
the data points").

### Candidate THEORY sentence (for the neighbour N1, which was read)

"Natschläger, Bertschinger and Legenstein show, by an annealed mean-field
theory and simulation, that randomly connected networks of binary
threshold gates driven by random binary input have an order-to-chaos line
where a single input-bit flip propagates to on average one node
(K·P_bf = 1), that a trained linear readout performs best on delayed
parity and random Boolean functions of recent inputs, averaged over
tasks, near that line, and that a separation measure corrected for
initial-condition and immediate-input separation peaks there; a local
synaptic-scaling rule drives networks to the line."
promote_when: "An independent study or replication in driven random
threshold or Boolean networks finds task-averaged readout performance on
nonlinear functions of recent inputs maximal near the damage-spreading
critical line K·P_bf = 1, and the corrected separation measure peaking
there."

For the unread work, a THEORY should wait for the text; at most its
abstract's claim, marked unread.

### Recheck (grep after reading)

Terms searched: fading memory, separation property, Derrida, annealed
approximation, Hamming distance, damage spreading, synaptic scaling,
self-organized criticality, Bornholdt, Langton, liquid state, echo state,
Jaeger, parity, random Boolean, Kauffman, order-to-chaos, onset of chaos.
Held entries the first search missed, with bearing:

- **CLAIM-850** (Proposed; chaos, criticality and cascades are distinct):
  qualifies. The damage-branching condition K·P_bf = 1 is a case where an
  order-chaos edge *is* a branching-ratio-one condition, of perturbations;
  CLAIM-850 should note it as a "particular mechanism" by which chaos
  onset and a critical branching meet, without activity being critical.
- **QUESTION-508** (Open; why some systems reach scale invariance
  untuned): bears via N1 §6, a local synaptic-scaling rule that
  self-tunes to the edge of chaos, an SOC mechanism by adaptation of a
  parameter, citing Bornholdt & Röhl (2003).
- **LIT-1139** (Active; Gross & Blasius, adaptive coevolutionary networks
  review): its note says "Bornholdt and Rohlf reverses one sentence";
  same family of self-organization to the edge in threshold networks as
  N1 §6 (N1 cites Bornholdt & Röhl 2003, PRE 67:066118, not held).
- **ARG-128** (Proposed): records that Dambre's edge "takes the edge's
  value as an assumption, citing Langton"; this work (via N1) is the
  empirical support for that assumption in driven networks, and Langton
  1990 is its ref. [1] too. Background.
- **THEORY-2041** (Schoenholz et al.): parallel. Same Derrida-style
  mean-field of two-trajectory correlation, for deep feedforward nets,
  depth scale diverging at the order-chaos line; this is its recurrent,
  input-driven, binary counterpart.
- **THEORY-2158** (Dambre et al.): contrast. Dambre's bound would say a
  driven threshold network's total capacity is ≤ N for any (µ, σ²); this
  work reports a task-family performance, not a total, so the two do not
  conflict, and the work cannot show that nearness raises the total.
- **CLAIM-841** (a power law does not indicate criticality): no bearing
  found beyond the topic.

Not held, cited by N1, possibly worth registering: Langton 1990 (Physica D
42); Derrida & Pomeau 1986 (Europhys. Lett. 1:45); Derrida 1987 (J. Phys.
A 20:721); Maass, Natschläger & Markram 2002 (Neural Comput. 14(11));
Jaeger & Haas 2004 (Science 304:78); Bornholdt & Röhl 2003 (PRE 67:066118);
the mean-field supplement (unreachable, above).

### Status recommendation for LIT-2991

**Unavailable** (ADR-041): no lawful copy located; paywalled at the
publisher; OpenAlex and S2 report closed. Caveat for the curation entry:
igi-web.tugraz.at (TLS reset, 2026-11-22) and web.archive.org ("Blocked
by egress policy", 2026-11-22) could not be searched, and the TU Graz
Pure pages showed a Cloudflare challenge; any of them might hold an
author copy. N1 to be filed as a neighbour (stand-in) with its own LIT,
NOTE and THEORY (ADR-114); N2 as a supplement if its passage is quoted.
