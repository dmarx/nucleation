---
status: Read
paper: LIT-2968
title: 'Barabási, Network Science, Chapter 5, The Barabási-Albert Model, read for the model''s derivations, the regimes of nonlinear attachment and where linear attachment comes from'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from the author's own book
    site (https://networksciencebook.com/translations/en/partials/ch-5.html,
    an HTML fragment, 107,697 bytes), in full: Sections 5.1 to 5.12, Boxes
    5.1 to 5.3 and 5.5, the Advanced Topics (labelled 4.A to 4.C in this
    edition), the bibliography [1] to [36] and all 94 equations. Skipped:
    the 19 figures as images (captions read), including Image 5.2's
    history timeline, and Videos 5.1 and 5.2. The fetched pages carry no
    licence statement; the copy is the author's own site. The web edition
    is undated; the 2016 Cambridge print edition was not checked. Every
    quotation the filing leans on rechecked by the filer by script against
    the fetched text. No email address sent.
date: '2026-11-22'
summary: >-
  The textbook chapter on the Barabási–Albert model: degree dynamics
  k_i = m(t/t_i)^(1/2) ("first-mover advantage"), γ = 1/β + 1 = 3 by
  continuum theory and the exact p_k = 2m(m+1)/[k(k+1)(k+2)] by rate
  equation; Models A and B; measuring the attachment function, with α ≈ 1
  for the Internet and citations and 0.9 ± 0.1 for co-authorship and
  actors; the nonlinear-kernel regimes after Krapivsky, Redner and
  Leyvraz; and link selection, copying and optimisation read as routes
  that generate linear attachment, with the claim that "all known models
  and real systems that are scale-free" have preferential attachment.
---
<!-- inactive-ok-file: CLAIM-817 CLAIM-806 CLAIM-830 CLAIM-803 CLAIM-795 SYNTHESIS-119 THEORY-188 THEORY-tmpzmy66 THEORY-tmphcnj3 ARG-tmp3q9cy ARG-tmpmylwc — Proposed or new; the reading of this work, the arguments filed with it and the entries it bears on -->
<!-- inactive-ok-file: LIT-tmphxpqu — Deferred; Dorogovtsev, Mendes and Samukhin, registered and unread -->

# NOTE-tmpnpqc8: Barabási, Network Science, Chapter 5, The Barabási-Albert Model, read for the model's derivations, the regimes of nonlinear attachment and where linear attachment comes from

## Contribution

A textbook account that puts the Barabási–Albert model's derivations
(continuum and exact), its ablations, the measurement of the attachment
function, the nonlinear-kernel regimes and the mechanisms that generate
linear attachment in one place, and argues that preferential attachment is
necessary and sufficient for a scale-free network. The reading is
[THEORY-tmpzmy66](../theory.d/THEORY-tmpzmy66.md). The paper it builds on is read in [NOTE-tmpwgw8e](NOTE-tmpwgw8e.md).

## Key results

Section numbers are the web edition's.

- **Degree dynamics** (§5.4, Eqs. 5.3 to 5.8). dk_i/dt = k_i/(2t − 1) ≈
  k_i/2t, k_i(t) = m(t/t_i)^β with β = 1/2. "The earlier node i was added,
  the higher is its degree ki(t). Hence, hubs are large because they
  arrived earlier, a phenomenon called first-mover advantage."
- **Continuum theory** (§5.5, Box 5.3). Nodes added "at equal time step"
  give P(k) = 1 − (m/k)^(1/β) and γ = 1/β + 1 = 3; (5.10) "links the degree
  exponent" to "the dynamical exponent" β.
- **Exact law** (§5.5, Eq. 5.11; Advanced Topic). "While the continuum
  theory predicts the correct degree exponent, it fails to accurately
  predict the pre-factors"; p_k = 2m(m+1)/[k(k+1)(k+2)], from
  p_m = 2/(m+2) and p_k = p_{k−1}(k−1)/(k+2). Credited to Dorogovtsev,
  Mendes and Samukhin [12] ([LIT-tmphxpqu](../literature.d/LIT-tmphxpqu.md)), Krapivsky, Redner and Leyvraz
  [13] and Bollobás and others [10]. Checked with python3 -I, exactly in
  fractions for m = 1, 2, 3: the closed form satisfies the start and the
  recursion, and its partial sums are 1 − m(m+1)/[(K+1)(K+2)], which tend
  to 1.
- **Model A** (§5.6): p(k) = (e/m) exp(−k/m).
- **Model B** (§5.6, Eq. 5.19). "As Π(0)=0 nodes with k=0 are assumed to
  have k=1." "At early times, when there are only a few links in the
  network (i.e. L ≪ N), each new link connects previously unconnected
  nodes. In this stage the model's evolution is indistinguishable from the
  Barabási-Albert model with m=1", and "the model develops a degree
  distribution with a power-law tail". Later p_k is not stationary and
  "the network becomes a complete graph". §5.11: "if one of them is
  absent, either the scale-free property or stationarity is lost".
- **Measuring Π(k)** (§5.7). Δk_i/Δt from two snapshots, and the
  cumulative π(k). "For the Internet and citation networks we have
  α ≈ 1"; "For the co-authorship and the actor network the best fit
  provides α=0.9±0.1". Image 5.10's caption: "these measurements only
  consider links added through the arrival of new nodes".
- **Nonlinear kernel** (§5.8, Image 5.12; Advanced Topic, after Krapivsky,
  Redner and Leyvraz [13]). Sublinear: "The degree distribution follows the
  stretched exponential" (5.23), with k_max ∼ (ln t)^(1/(1−α)). For α > 2
  "a winner-takes-all phenomenon: almost all nodes connect to a few
  super-hubs"; 1 < α < 2 is less extreme. "Strictly speaking a stationary
  degree distribution only exists if" α ≤ 1. "Π(k) needs to depend strictly
  linearly on the degrees for the resulting network to have a pure power
  law", and sublinear attachment "is one reason the degree distribution of
  real networks deviates from a pure power-law", for which a stretched
  exponential "should offer a better fit".
- **Where linear Π(k) comes from** (§5.9). Link selection,
  q_k = kp_k/⟨k⟩; copying, Π(k) = p/N + (1 − p)k/2L; and optimisation,
  "such rational decisions can lead to preferential attachment [22, 23,
  24]", where [22] is Fabrikant, Koutsoupias and Papadimitriou and [24]
  Papadopoulos and others, "Popularity versus similarity in growing
  networks". "each of the mechanisms discussed above lead to linear
  preferential attachment"; "We are not aware of mechanisms capable of
  generating nonlinear preferential attachment".
- **Claimed sufficiency** (§5.11): "We offered a necessary and sufficient
  argument"; models without a built-in attachment function "do so by
  generating a linear Π(k)", and "To date all known models and real
  systems that are scale-free have been found to have preferential
  attachment."
- **Limits** (§5.11): "The model predicts γ=3 while the degree exponent of
  real networks varies between 2 and 5"; it is undirected, has no internal
  links or removal, and "does not allow us to distinguish between nodes
  based on some intrinsic characteristics".
- **Simon and Mandelbrot** (Image 5.17's caption, read as caption): their
  dispute framed as luck or reason, and "they were both right".

## Assumptions

- Event time (t = N), nodes arriving at equal steps.
- Undirected edges, constant m; only arriving nodes add links.
- A kernel exactly k or k^α, with no offset.
- Continuum dynamics, and p_k from rate equations in the stationary limit.
- In Model B, k = 0 counted as 1.

## Concepts

Growth; preferential attachment; the LCD model; the dynamical exponent β;
first-mover advantage; event time; continuum theory against rate
equations; stationarity; Models A and B; the cumulative attachment
function π(k); sublinear and superlinear kernels; the stretched
exponential; winner-takes-all and hub-and-spoke networks; link selection;
the copying model; optimisation; "luck or reason".

## Bearing on the record

- **[CLAIM-817](../claims.d/CLAIM-817.md)** (supports the whole title; a rival framing of one aside).
  §5.6 shows that both ingredients are needed, §5.8 gives the regimes and
  "Π(k) needs to depend strictly linearly". The chapter's regimes are
  Krapivsky, Redner and Leyvraz's, credited as such; it is a secondary
  source beside [NOTE-tmp2z733](NOTE-tmp2z733.md). For α > 1 it backs the claim's
  condensation (no stationary p_k, k_max ∼ t), though it is looser than
  the paper on how many hubs ("a few super-hubs"). The claim's aside that
  hyperbolic geometry ([THEORY-188](../theory.d/THEORY-188.md)) "needs no attachment at all" meets a
  rival framing: §§5.9 and 5.11 read optimisation and geometric models,
  Papadopoulos and others among them, as *generating* linear attachment,
  and say all known scale-free models have it. A contrast, not a
  refutation. [ARG-tmp3q9cy](../arguments.d/ARG-tmp3q9cy.md).
- **[CLAIM-806](../claims.d/CLAIM-806.md)** (supports; adds the empirical side). The regimes on both
  sides of α = 1; the measured α ≈ 1 for citations and the Internet and
  0.9 ± 0.1 for co-authorship and actors place real systems at or just
  below the boundary, by this measure. The chapter draws no analogy to
  criticality.
- **[CLAIM-830](../claims.d/CLAIM-830.md)** (supports the premise, the age reading and the caveat;
  qualifies the urn contrast). "hubs are large because they arrived
  earlier", and γ = 1/β + 1, so the survival exponent 1/β = 2 is the
  claim's λ/g. "fails to accurately predict the pre-factors" matches the
  claim's "accounts for the exponent ... not for any one node's degree".
  No log time and no comparison with Gibrat (Gibrat [4] appears only in
  the bibliography). Model B, as under [NOTE-tmpwgw8e](NOTE-tmpwgw8e.md). [ARG-tmpmylwc](../arguments.d/ARG-tmpmylwc.md).
- **[QUESTION-505](../questions.d/QUESTION-505.md)** (supports the partial pattern). (5.10) makes
  γ − 1 = 1/β; directed copying's γ = (2 − p)/(1 − p) is the formula
  already noted from Mitzenmacher; an attractiveness A shifts the
  exponent, as Newman's k + c does.
- **[NOTE-tmpleyjh](NOTE-tmpleyjh.md)**, **[THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md)** (a parallel and a contrast).
  Parallel: sublinear attachment as a reason real degree distributions
  deviate, with a stretched exponential "a better fit"; Broido and Clauset
  test a Weibull. The measured α fits their keeping attachment for
  citation networks. Contrast: "necessary and sufficient argument" and
  "all known ... scale-free" against their "relatively weak evidence"
  about mechanism; and the chapter's real exponents of 2 to 5 beside
  their median near 2.
- **[CLAIM-803](../claims.d/CLAIM-803.md)**, **[SYNTHESIS-119](../syntheses.d/SYNTHESIS-119.md)** (a parallel and a contrast). §5.7 is the
  "twice the degree, twice the links" test, conditioned only on degree, so
  the confound of fitness and age goes unaddressed; "necessary and
  sufficient" is the inference [CLAIM-803](../claims.d/CLAIM-803.md) rejects.
- **[THEORY-188](../theory.d/THEORY-188.md)**, **[NOTE-678](NOTE-678.md)**, **[LIT-865](../literature.d/LIT-865.md)** (a rival framing; see
  [CLAIM-817](../claims.d/CLAIM-817.md) above).
- **[LIT-2974](../literature.d/LIT-2974.md)** (restated). The chapter reproduces the α ≤ 1 derivation and
  states the α > 1 regimes without derivation.
- **[CLAIM-795](../claims.d/CLAIM-795.md)**, Pólya-urn entries (background). Image 5.17's "they were
  both right" on Simon and Mandelbrot; Eggenberger and Pólya (1923) in the
  bibliography.

## Limitations

- The figures were read only by caption, Image 5.2's history included.
- The web edition has slips, none affecting a quoted result: off
  cross-references, Advanced Topics labelled 4.A to 4.C, a dropped ln in
  (5.58), and "N = mt" for the number of links in Box 5.5. The reader
  reported two more equation slips the filer did not recheck.
- §5.7's measurement of Π(k) does not address the confound of fitness and
  age.
- Fitness is Chapter 6, outside this reading.
