# Reader notes: LIT-tmpv9upr

Wei, Zhang, Cousseau, Ozeki & Amari (2008), "Dynamics of Learning Near
Singularities in Layered Networks", Neural Computation 20, 813–843,
DOI 10.1162/neco.2007.12-06-414. Read 2026-11-21.

## Provenance

- **Read:** https://typeset.io/pdf/dynamics-of-learning-near-singularities-in-layered-networks-1l6dod1kwo.pdf
  (redirects to scispace.com/pdf/...; SciSpace, a scholarly third-party
  site, ADR-074). PDF, 31 pages. It is the **published version**: the
  journal header "Neural Computation 20, 813–843 (2008) © 2008 Massachusetts
  Institute of Technology" and page numbers 814–843. Extracted with
  pdftotext. Read in full: abstract, §§1–5, appendix, references. Figures
  read only from captions and the surrounding text (the plotted curves
  do not survive extraction).
- **Other copies located:**
  - CiteSeerX, http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.523.4315
    (listed by OpenAlex as submittedVersion; a scholarly third-party
    index). Both the summary and
    https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=10.1.1.523.4315
    answered 301 to web.archive.org; the Wayback fetch reset
    ("curl: (35) Recv failure: Connection reset by peer"), 2026-11-21.
    Not retried. Not needed, since the published version was read.
  - Teikyo University repository, https://teikyo-u.repo.nii.ac.jp/records/2067543
    (OpenAlex: submittedVersion). Its own API record
    (/api/records/2067543) is metadata only, no file attached, 2026-11-21.
  - RIKEN BSI, https://bsi-ni.brain.riken.jp/database/file/274/280.pdf
    (a search hit; what it holds was not established): no response
    (curl returned no status), 2026-11-21. Not retried.
  - OpenAlex: oa_status closed; Semantic Scholar openAccessPdf CLOSED;
    PubMed 18045020 (abstract only). No arXiv copy (arXiv API title search
    empty). No email address sent anywhere.

## Summary

For a two-layer model f(x,θ) = Σ wᵢ φ(x, Jᵢ) (RBF networks, MLPs,
gaussian mixtures) trained by online gradient descent on squared loss, the
letter analyses the averaged gradient flow near the **overlap singularity**
R₁ (two hidden units with Jₐ = J_b) and the **elimination singularity** R₂
(wₐw_b = 0). In coordinates u = J_b − Jₐ, z = (wₐ − w_b)/(wₐ + w_b) (from
Fukumizu & Amari 2000), the critical line R₁* (u = 0, other parameters at
the best (k−1)-unit fit) has stability set by (1 − z²)H, H a matrix fixed
by the residual. To leading order the flow in (u, z) has a closed
first integral, so the orbits near R₁* are universal across these models.
Two plateau mechanisms follow: an **on-singularity plateau**, a
noise-driven random walk along the stable part of R₁* until it reaches
the unstable part and leaves (a "Milnor-like attractor"), and a
shorter **near-singularity plateau**, where an orbit passing close to R₁*
crosses the flat region at z = ±1 with Ė of order u⁴.

## Contribution

Universal trajectories near overlap singularities, for any teacher (not
only a teacher on the singularity, as in earlier Amari et al. 2006,
Cousseau et al., Wei & Amari 2006), in the original gradient rather than a
reparametrized one; and the separation of two kinds of plateau.

## Key results

1. **Two singular types** (§2.3, p. 819): "R(i) is called the elimination
   singularity"; "R(i, j) is called the overlap singularity". The two and
   their intersections are "the only singular regions in RBF networks and
   gaussian mixture systems where the Fisher information matrix
   degenerates" (citing Fukumizu 1996).
2. **Stability of the critical line** (Theorem 1, p. 825): "When the
   teacher is on the singularity R∗1, the whole critical line of R∗1 is
   stable. When H has both positive and negative eigenvalues, all points on
   the critical line R∗1 are saddles. Otherwise the line R∗1 is divided
   into stable and unstable parts."
3. **First integral** (Theorem 2, Eq. 3.10, p. 827): from u̇ = 2(1 − z²)Hu
   and Eq. 3.7, "h(u) = ½uᵀu = (2w∗²/3) log((z² + 3)²/|z|) + C … where C is
   a constant depending on the initial model parameter (u(0), z(0))". Near
   R₁* ∩ R₂*, Corollary 1: h = w∗²(log|z| + 1/|z|) + C.
4. **The constant decides the destination** (Eq. 3.15, pp. 830–831): "When
   C = C0 = −(8w∗²/3) log 2, the trajectory is tangential to R∗1. Otherwise,
   if C < C0, the trajectory has two intersection points with R∗1; if
   C > C0, the trajectory is totally above R∗1 and certainly passes the
   elimination singularity R∗2."
5. **Redundant case, generic destination** (§3.2, p. 829): "the basin of
   attraction of R∗1 is limited in the regions that |z| is small or |z| is
   large. So in most cases, the model parameter reaches R∗2." (One unit is
   eliminated rather than the two overlapping.)
6. **On-singularity plateau** (§4.1, p. 832): "the state is first
   attracted to the stable interval of R∗1; then it undergoes a long period
   of random walk on R∗1; finally it leaves R∗1"; "the singularity is
   completely different from the saddle point and is a Milnor-like
   attractor (Milnor, 1985)". Noise is essential: "the fluctuations due to
   the noise and the random sampling of input play an important role"
   (p. 835).
7. **Near-singularity plateau** (§4.2, p. 836): near z ≈ ±1 "Ė(ξ) is of
   order O(u⁴). This tells us that if u is small, E(ξ) remains almost
   unchanged when the model parameter crosses the lines z = ±1."
8. **The two differ** (p. 839): "In the case of the on-singularity
   plateau, Ė(ξ) = 0 on average … during the period of the near-singularity
   plateau, Ė(ξ) < 0 always holds, although its value is very small",
   which "explains why the time period of near-singularity plateau … is
   much shorter".
9. **Open** (§5, p. 840): "The dynamics of learning near the elimination
   singularities far away from the overlap singularities still remains
   unknown."

## Assumptions

Two-layer, one linear output; smooth φ (Taylor to O(u⁴)); squared loss,
additive zero-mean gaussian noise; online SGD replaced by its averaged
ODE (stochastic approximation); s, v, w held at the best (k−1)-unit fit
(the orbits are projections onto S*, Remark 1); small u; leading order in
u only. Experiments: two-unit RBF teacher and student, 2-d gaussian
inputs, widths fixed at 0.5, η = 0.05.

## Concepts

Overlap singularity; elimination singularity; critical line R₁*; Milnor-like
attractor; on-singularity plateau; near-singularity plateau;
quasi-plateau (Park et al. 2005); first integral of the averaged flow;
basin of positive measure; random walk on a line of equivalent models.

## Verdict on the exchange's characterization

The LIT's summary ("trajectories of gradient learning near the overlap and
elimination singularities … with the Milnor-attractor behaviour that
produces plateaus") is **accurate**. CLAIM-tmpcbfdj's remark that the
record "does not yet hold their distinction between the two kinds of
plateau" now has its answer: on- versus near-singularity. But the grounds
lists of CLAIM-tmpcbfdj and CLAIM-tmpv5asv should not read the paper as a
source of **algebraic relaxation**: it derives **orbits, not time
courses**. No t-scaling, power law or relaxation exponent appears
anywhere (grep for algebraic/power/exponent/slow: only "slow learning
speed around z = 1", p. 837, and titles in the references). Its
plateau mechanisms are (a) noise-driven diffusion along a flat line and
(b) a small gradient, O(u⁴), at the flat crossing; neither is a
derived algebraic decay. Its two "types" are overlap vs elimination
(where), and on vs near (how the orbit meets them), not "milder vs
stronger" orders of degeneracy.

## Bearing on the named codes

- **CLAIM-tmpcbfdj: parallel; leaves its exponent open; supports its
  caveat by analogy.** No result on t^(−1/(2k−2)) or any decay rate. But
  the caveat's structure recurs: in CLAIM-tmpcbfdj a conserved imbalance
  D = a² − b² decides whether the flow reaches the most degenerate point
  (D = 0) or a generic zero-set point (b = 0); here a first integral C
  (Eq. 3.10) decides whether the flow reaches the overlap line (C < C0) or
  only crosses the elimination singularity (C > C0), and "in most cases,
  the model parameter reaches R∗2" (p. 829). In both, reaching the more
  singular set needs a special start, and the generic one ends where one
  factor (output weight) is zero. Analogy only: different model, and the
  paper's flow is in a nonlinear two-unit network.
- **CLAIM-tmpv5asv: qualifies.** The paper offers plateaus without
  algebraic relaxation: the on-singularity plateau's length is set by a
  random walk on a line (noise-driven, p. 832), not by a degenerate
  direction's decay. So "slow learning near singularities" in this
  literature is not evidence for "algebraically relaxing singular modes";
  it is a third rival beside criticality and algebraic relaxation:
  noise-driven escape from a Milnor-like attractor. It says nothing about
  power laws or broad timescale distributions.
- **CLAIM-tmpp83vc: supports A37 §4's "dynamics are separate".** The same
  singular set is reached, crossed or left depending on H's signature
  and on C (Theorem 1, Eq. 3.15); existence of the singularity does not
  fix the dynamics. No account of transitions as resolutions; no learning
  coefficient. Background for reading (b) at most.
- **THEORY-082: background, consistent.** THEORY-082 derives from Amari
  (1998) that the MLP Fisher loses rank where an output weight is zero;
  this paper names that set the elimination singularity and adds the
  overlap singularity ("It is immediate to show that the Fisher
  information degenerates in this region", p. 819), and §5 cites natural
  gradient as one way to escape (p. 840).

## Limitations

Leading order in u, averaged dynamics, projection onto S* (s, v, w frozen
at their optimum; Remark 1). In the redundant case H = 0 (p. 825), so the
leading-order u̇ and ż of Eqs. 3.6–3.7 both vanish, yet Eq. 3.14 is given
with w₀; the reader did not find the higher-order justification in the
text. The plateau experiments are two-unit RBF networks in two
dimensions; the near-singularity experiment uses a stationary gaussian
process in place of the random walk (p. 834). Elimination singularities
away from overlaps are left open. No time-scaling of plateau length is
derived (only "it might take a long time", p. 832). Figures not read from
the image.

## Candidate THEORY

Wei, Zhang, Cousseau, Ozeki and Amari show that in two-layer networks
(RBF, MLP, gaussian mixture) trained by averaged online gradient descent,
the flow near an overlap singularity has, to leading order, the universal
first integral ½uᵀu = (2w∗²/3) log((z²+3)²/|z|) + C, whose constant decides
whether it reaches the overlap line or only crosses the elimination
singularity; that the line is partly stable by the signature of
(1 − z²)H, a Milnor-like attractor whose noise-driven random walk is the
on-singularity plateau; and that orbits passing near it give a shorter
near-singularity plateau, where the loss changes at order u⁴.

`promote_when`: the first integral (Eq. 3.10, Corollary 1) is checked by
numerically integrating Eqs. 3.6–3.7 for a definite H and confirming that
h − (2w∗²/3)log((z²+3)²/|z|) stays constant along orbits and that
C = −(8w∗²/3) log 2 separates orbits that meet u = 0 from those that do
not; and the stability claim of Theorem 1 is checked against Eq. 2.53.

## Recheck (grep of record/ with the reading's terms)

Searched: Milnor, overlap singularit, elimination singularit, Fukumizu,
Saad, Cousseau, on-singularity, quasi-plateau, plateau, permutation
symmetry, Inoue, neuromanifold, conserved quantity. Entries the first
search missed:
- **THEORY-2009** (Proposed): Chen, Kunin, Yamamura and Ganguli, the sets
  "where a hidden neuron vanishes or two neurons in a layer are
  identical are invariant under SGD" and attract under a curvature
  against noise condition. **Parallel and close**: the same two sets as
  this paper's elimination and overlap singularities, with noise again
  deciding attraction. The two should be cross-linked.
- **CLAIM-tmp9bp04**: a factored feature ŷ = abφ, pitchfork at s = λ,
  "relaxation there is algebraic". Contrast: an algebraic decay at a
  threshold, which this paper does not have.
- **THEORY-740, THEORY-186, THEORY-187, THEORY-792, QUESTION-166**: deep
  linear plateaus from small balanced starts. Contrast: their plateaus are
  the escape from a saddle at the origin, a time of order log(1/scale);
  this paper's on-singularity plateau is a noise-driven walk on a line of
  equivalent models.
- **LIT-tmp0z602** (Amari, Park & Ozeki 2006, Deferred): the paper this one
  generalizes ("first studied in the case of a gaussian mixture in Amari
  et al. (2006)", p. 815). Read it for the gaussian-mixture case.
- **NOTE-667** (on LIT-864, Saxe et al.): cites Fukumizu (1998) on
  plateaus; background.
- Not held: Fukumizu & Amari (2000), Cousseau, Ozeki & Amari (2008, IEEE
  TNN), Park, Inoue & Okada (2003, 2005), Saad & Solla (1995). Cousseau
  et al. is the MLP companion and the natural next read.

## Neighbours

None needed: the work itself was read.
