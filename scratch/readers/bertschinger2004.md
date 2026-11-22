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
