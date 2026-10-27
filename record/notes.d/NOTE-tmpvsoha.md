---
status: Read
paper: LIT-tmpb4amz
title: 'Zurek — Quantum Darwinism'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the arXiv preprint 0903.5082v1 (29 March 2009, the
    only version), 10 pp., whose arXiv record gives the journal reference
    Nature Physics 5, 181–188 (2009). The text was extracted with
    `pdftotext`, both with and without `-layout`. I read the abstract,
    sections I–V, the captions of Figs. 1–4, the Box (p. 8), the
    acknowledgements and the forty references. Pages are the preprint's.
    The published Nature Physics text was not read, so differences between
    the two are unknown. The extraction garbles the figures' plotted
    content (Figs. 1 and 3 are images; only their captions survive), the
    ket notation (|u⟩ comes out as "|ui") and some fractions; where an
    expression below is reconstructed, it is said so.
date: '2026-10-27'
summary: >-
  A review. Decoherence singles out pointer states; quantum Darwinism adds
  that the environment is the channel observers read, and that decoherence
  leaves many copies of the pointer observable in it: the mutual
  information I(S : F_f) between the system and a fraction f of the
  environment rises steeply to a plateau at H_S, so R_δ = 1/f_δ fragments
  each hold nearly all of it, and redundancy is high only for the pointer
  observable. Zurek reads redundancy as objectivity. A clean unitarity
  argument (eq. 5) shows that only orthogonal states can be repeatably
  copied, without the Born rule, which he derives separately from
  envariance. The paper claims the measurement problem "largely settled";
  it does not state the later caveat that mutual information alone does
  not guarantee independently accessible records.
---
<!-- inactive-ok-file: QUESTION-tmpubsi9 CLAIM-tmpmx2ql CLAIM-342 CLAIM-tmpalzo4 THEORY-621 THEORY-017 TERM-tmpjdel0 THEORY-tmp0d0qe THEORY-tmp08c0w LIT-tmpqu50n — Open, Proposed, Deferred or new; the entries the reading bears on and the readings it files, cited as open -->

# NOTE-tmpvsoha: Zurek — Quantum Darwinism

## Contribution

A review of a programme, not a single new result. It joins three lines of
Zurek's earlier work into one account of "the classical": einselection
(decoherence selects pointer states), quantum Darwinism (the environment
holds redundant records of those states, and observers learn them from
fragments of it), and envariance (a derivation of the Born rule from
symmetries of entangled states). Its own summary: these "mark considerable
progress towards settling the quantum measurement problem" (abstract, p. 1),
and in the Discussion, "The essence of the measurement problem – accounting
for axioms (iv) and (v) – has been largely settled" (p. 9). The new
emphasis over decoherence theory is the change of question: not which
states survive information leaks to E, but "What information about the
system can be found out from fragments of E?" (p. 2).

## Key insight

"Tracing out" the environment is not what observers do: "Observers
eavesdrop on the environment. Vast majority of our data comes from
fragments of E. Environment is a witness to the state of the system" (p. 2).
What makes a state classical is then not only that it survives monitoring
but that it is copied many times into the environment: "Only states that
produce multiple informational offspring – multiple imprints on the
environment – can be found out from small fragments of E" (p. 2). When
many disjoint fragments each carry nearly all the information about the
same observable, many observers can learn it "independently, and without
perturbing it. This is how preferred states of S become objective.
Objective existence – hallmark of classicality – emerges from the quantum
substrate as a consequence of redundancy" (p. 2).

## Assumptions

- **A given split into system and environment, and a given subdivision of
  the environment.** "We recognize the subdivision of E into subsystems …
  The only requirement for a subsystem is that it should be individually
  accessible to measurements; observables of different subsystems commute"
  (Fig. 1 caption, p. 2). Fragments F are "non-overlapping collections of
  subsystems of E". Which subsystems are accessible is taken as given.
- **Postulates (i)–(iii) only, for sections III–IV**: states are vectors in
  Hilbert space, evolution is unitary, and "Immediate repetition of a
  measurement yields the same outcome" (p. 4). The collapse postulate (iv)
  and the Born rule (v) are what is to be derived. Tensor-product
  composition is used throughout ("often cited as additional 'axiom (0)'",
  p. 9).
- **Three "facts of life" for the Born-rule derivation (p. 8)**: "(1) When a
  system is not acted upon by a unitary transformation, its state remains
  unaffected"; "(2) Predictions regarding measurement outcomes on S
  (including their probabilities) can be inferred from the state of S";
  "(3) When S is entangled with other systems (e.g., the environment) the
  state of S alone is determined by the state of the whole SE." Also
  normalization (probabilities of an event and its complement sum to one),
  but not, it says, additivity in general (p. 8, Box).
- **The redundancy results of section II use the Born rule.** Mutual
  information is defined through von Neumann entropies of reduced density
  matrices (eqs. 1–3), and the paper says tracing out "relies on
  pk = |ψk|², Born's rule we want to derive. We have imposed that ban while
  deriving and analyzing Eq. (5), but relaxed it to plot Fig. 3" (p. 6). The
  ordering the Discussion proposes, deriving Born first and then using
  reduced density matrices "with every right" (p. 9), is how the paper
  answers the circularity.
- **Model-specific dynamics** for the quantitative results: a spin coupled
  to many spins by an Ising Hamiltonian (Fig. 3, N = 50, couplings drawn
  from (0, 1]) and quantum Brownian motion of an underdamped oscillator
  (p. 3). The results are cited from refs. [12]–[15]; none is derived in
  this text.

## Key results

### Decoherence and einselection (section I, pp. 1–2)

- **Pointer states.** "Interactions that depend on a certain observable
  correlate it with the environment, so its eigenstates are singled out,
  and phase relations between such pointer states are lost" (p. 1).
  "Negative selection due to decoherence is the essence of
  environment-induced superselection, or einselection" (p. 1).
- **ρ_S = Tr_E |Ψ_SE⟩⟨Ψ_SE|** (eq. 1, p. 1). The predictability sieve sorts
  pure states by the entropy their evolved ρ_S produces; pointer states
  produce least, superpositions produce it "rapidly, at decoherence rates,
  especially when S is macroscopic" (pp. 1–2). Position is preferred because
  interactions "tend to depend on distance"; for a weakly damped oscillator
  coherent states are einselected (p. 2).

### Environment as a witness (section II, pp. 2–4)

- **ρ_SF = Tr_{E/F} |Ψ_SE⟩⟨Ψ_SE|** (eq. 2) and
  **I(S : F) = H_S + H_F − H_{S,F}** (eq. 3), p. 2.
- **The plateau (Fig. 2 caption, p. 3).** For a global pure state of SE,
  I(S : F_f) for a typical fraction f is antisymmetric about f = ½. For
  Haar-random states, small fragments hold almost nothing and "once a
  threshold f = ½ is attained, nearly all information is in principle at
  hand", so "such random states … exhibit no redundancy". For states made
  by decoherence, I(S : F_f) "quickly rises to H_S (entropy of S due to
  decoherence) … More, up to 2H_S, can be obtained only through global
  measurements on S and nearly all E. H_S is therefore the classically
  accessible information." The plotted curves are schematic in the
  extraction; the text says model calculations "exhibit behavior
  illustrated by the red plot" (p. 3).
- **Redundancy, eq. (4), p. 3**: "Redundancy is the number of independent
  fragments of the environment that supply almost all classical
  information about S, i.e., (1 − δ)H_S": **R_δ = 1/f_δ**, with f_δ the
  fraction needed. "Rapid rise and gradual leveling of I(S : F_f), Fig. 2,
  implies redundancy" (p. 3). "The redundancy plateau is a classical
  plateau" (p. 3).
- **Objectivity by redundancy.** "Large redundancy implies objectivity: The
  state of the system can be found out indirectly and independently by
  many observers, who will agree about their conclusions" (Fig. 2 caption).
  "Observables of different F's commute – such measurements are
  independent. Yet, underlying correlations mean that their outcomes imply
  the same state of the system, as if S were classical" (p. 3). Records are
  damaged by reading them ("we destroy photons!"), so error correction by
  redundancy matters: "with many (R_δ) copies, state of S can be found out
  by ∼ R_δ observers … Consensus between copies suggests objective
  existence of the state of S" (p. 3).
- **Models (p. 3).** Spin environments [12–14]: "the same number of spins
  suffices to reach the plateau", so redundancy is "proportional to the
  number of the environment subsystems that interact with the system".
  Quantum Brownian motion [15, 16]: I(S : F) ≈ H_S + ½ ln(f/(1 − f))
  (reconstructed from the extraction) and R_δ ≈ s^{2δ} for an initially
  squeezed state with squeeze factor s; "Similar equation should hold for
  more general 'Schrödinger cat' states".
- **Branch structure (pp. 3, 5–6).** Decoherence states "are far from
  random. Roughly speaking, they have a branch structure" (p. 3). Eq. (6),
  p. 6: |Ψ_SE⟩ = Σ_k ψ_k |s_k⟩|e_k^(1)⟩…|e_k^(N)⟩ = Σ_k ψ_k |s_k⟩|ε_k⟩,
  "to a good approximation, a multi-system Schmidt decomposition", "a very
  atypical minimally entangled superposition" (p. 6).
- **Shannon versus von Neumann (p. 4).** With Shannon entropies of optimal
  local observables the I(S : F_f) graph "for small f would look very
  similar", but never exceeds H_S, "antisymmetry is lost, and the plateau
  continues until the end at f ∼ 1". The region above H_S needs global
  measurements, which is "why decoherence is so hard to undo".
- **Mixed environments (p. 4).** An environment with initial entropy h per
  bit is a noisy channel: a bit from E yields only 1 − h bits about S. "a
  completely mixed E (h = 1) is useless (even though it can still induce
  decoherence!)". A partly mixed one still "can still climb the same
  redundancy plateau at H_S [19]", needing a larger fragment. Ref. [19] is
  "in preparation".
- **Which environments carry records (p. 4).** Photons are ideal: they "do
  not interact with each other" and are far from equilibrium with our
  surroundings. "Air molecules scatter from one another, so that whatever
  record they may have gathered becomes effectively undecipherable." So
  decoherence and record-keeping can be done by different environments.

### From copying to quantum jumps (section III, pp. 4–6)

- **Eq. (5), p. 5.** If |u⟩ and |v⟩ each leave an imprint and stay
  unperturbed, |u⟩|e₀⟩ → |u⟩|e_u⟩, |v⟩|e₀⟩ → |v⟩|e_v⟩, unitarity preserves
  the scalar product: ⟨u|v⟩ = ⟨u|v⟩⟨e_u|e_v⟩. So "(a) either ⟨e_u|e_v⟩ = 1
  (which means that copying was completely unsuccessful), or; (b)
  ⟨u|v⟩ = 0". "As a consequence of unitarity, only sets of orthogonal
  states … can be so copied, explaining selection of a set of outcomes –
  terminal points of quantum jumps" (p. 5). It "relies on just two values
  of the scalar product – 0 and 1 – and, thus, does not appeal to Born's
  rule" (p. 5). No-cloning is evaded because "copying of observables" is
  not cloning of unknown states (p. 4).
- **Selectivity (Fig. 3, p. 5).** With Shannon-based quantities for
  σ(μ) = cos μ σ_z + sin μ σ_x, the whole environment "knows" many
  observables (Fig. 3a), but R_{δ=0.1}(σ) "is sharply peaked around the
  pointer observable: Redundancy is a very selective criterion" (Fig. 3b).
  Local random measurements on m environment spins reveal "pointer states –
  and only pointer states" (Fig. 3c). A theorem cited from [12, 24]: "only
  pointer states can be discovered from fractions of E. Other observables
  … can be deduced only to the extent they are correlated with the pointer
  observable" (p. 5).
- **Collapse as the rise of I (p. 6).** "This transition from uncertainty
  … to certainty (once a sufficiently long branch fragment becomes known)
  accounts for perception of 'collapse'. … Collapse is brief compared to
  the ensuing period of certainty about the outcome, as f_δ ≪ 1, but,
  nevertheless, not instantaneous."
- **Apparatus (p. 6).** It suffices that records "are 'repeatably
  accessible'. Transfer of responsibility for repeatability from a quantum
  S to a (still quantum) A allows one to model non-orthogonal measurement
  outcomes (POVM's)"; the apparatus pointer states are then the ones copied
  into E. "Indeed, we usually experience 'quantum jumps' via an apparatus
  pointer."
- **Stance (p. 6).** "our discussion is interpretation-free, and this is a
  virtue." "Quantum states acquire objective existence when reproduced in
  many copies. … And there is only one copy of the Universe. Treating its
  state as if it really existed [26, 27, 28] seems unwarranted and
  'classical'."

### Probabilities from entanglement (section IV and Box, pp. 6–8)

- **Envariance, eq. (7), p. 7**: u_S ⊗ 1_E |Ψ_SE⟩ = |Φ_SE⟩;
  1_S ⊗ u_E |Φ_SE⟩ = |Ψ_SE⟩. A phase change of Schmidt coefficients made on
  S can be undone on E, so by facts (1)–(3) phases cannot matter for S.
  "Such loss of phase significance for S entangled with E implies
  decoherence" (pp. 7–8).
- **Equiprobability (p. 8; Fig. 4).** For equal |ψ_k| a swap in S can be
  undone by a counterswap in E, so p(0) = p(1) = ½.
- **Born's rule by fine-graining (Box, p. 8).** For
  |ψ_SE⟩ ∝ √2 |0⟩|+⟩ + |2⟩|2⟩ (reconstructed), a controlled operation from E
  to an ancilla C gives three equal-amplitude Schmidt terms, so
  p₂ = ⅓ and, by normalization, p₀ = ⅔. The extension to commensurate
  probabilities "is conceptually straightforward but notationally
  cumbersome"; the noncommensurate case "is settled with an appeal to
  continuity" (p. 8).

### Discussion (section V, p. 9)

- The two contested postulates are claimed derived from the first three.
  "How Darwinian is Quantum Darwinism?": survival of the fittest, with
  fitness as the ability to procreate; no-cloning implies "competition for
  resources – space in E – so that only pointer states can multiply".
  The Universe's memory is finite, so "old events will be eventually
  'overwritten' by new ones … And if there is no record of an event, has
  it really happened?" Whether quantum Darwinism is "in some way behind
  the familiar natural selection" is raised and not answered.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Only sets of orthogonal states can be copied repeatably into an environment while left unperturbed; the argument uses unitarity and repeatability, not the Born rule | strong | eq. (5), p. 5: a two-line derivation from the preservation of scalar products |
| C2 | States of SE produced by decoherence put almost all of the system's information H_S into small fragments of E, so redundancy R_δ = 1/f_δ is large, unlike Haar-random states | moderate | cited model calculations (spin environments [12–14], quantum Brownian motion [15, 16]); schematic Fig. 2; not derived here |
| C3 | Redundancy is high only for the pointer observable; other observables are learnable from fragments only through their correlation with it | moderate | Fig. 3 for one spin model (N = 50); a theorem cited from [12, 24], not stated or proved here |
| C4 | Redundancy is what makes pointer states objective: many observers can learn them independently, indirectly and without perturbing S, and agree | weak | an interpretive identification (p. 2, Fig. 2 caption, p. 3); independence rests on fragments' observables commuting plus "underlying correlations" (p. 3); no result shows that each fragment's record determines the same outcome for every observer |
| C5 | The apparent collapse is the steep initial rise of I(S : F_f): brief but not instantaneous | weak | an interpretation of the plateau (p. 6) |
| C6 | Envariance gives the Born rule without assuming it or additivity of probabilities | moderate | Fig. 4, eq. (7), Box (pp. 7–8); rests on facts (1)–(3) and the equal probability of Schmidt partners; commensurate and continuity extensions are asserted; critiques [36, 37] are cited, not answered |
| C7 | A mixed environment still reaches the same plateau H_S, more slowly | weak | asserted with ref. [19] "in preparation" (p. 4) |
| C8 | The measurement problem has been "largely settled" | weak | the author's assessment (p. 9); the paper also says "Much work remains to be done" |

## Concepts

- **Einselection** — environment-induced superselection: "Under scrutiny
  of the environment, only pointer states remain unchanged. Other states
  decohere into mixtures of stable pointer states" (p. 1).
- **Pointer states** — the states singled out by the observable the
  system–environment interaction depends on; at the top of the
  predictability sieve (pp. 1–2).
- **Fragment F_f** — a non-overlapping collection of a fraction f of the
  environment's subsystems, each "individually accessible to
  measurements" (Fig. 1).
- **Redundancy R_δ** — the number of disjoint fragments each holding
  (1 − δ)H_S of the information about S; R_δ = 1/f_δ (eq. 4).
- **Redundancy (classical) plateau** — the level H_S at which I(S : F_f)
  levels off; "additional bits only confirm what is already known" (p. 3).
- **Branch** — a product term of eq. (6), labelled by a pointer state; its
  "bud" is the pointer state, its fragments imply it (pp. 3, 6).
- **Envariance** — entanglement-assisted invariance: a transformation of S
  that can be undone by acting on E alone (eq. 7).
- **Quantum Darwinism** — "the proliferation, in the environment, of
  multiple records of selected states of a quantum system" (abstract).

## Connections

- **Bohr** (ref. [1]): the classical apparatus the paper replaces with a
  quantum environment; outcome selection "parallels Bohr's insistence" but
  "follows from purely quantum Eq. (5)" (p. 6).
- **Everett, DeWitt** (refs. [26]–[28]): relative states "come to mind",
  but "We abstain" from the reality of other branches (p. 6). The
  "existential interpretation" of ref. [38] is named in the reference
  list only.
- **Zurek 1981, 1982** (refs. [6], [7]): pointer basis and einselection;
  [7] is the paper Rovelli credits with RQM's conclusion (NOTE-tmptc0hl).
  Not held.
- **Ollivier, Poulin and Zurek** (refs. [12], [24]), **Blume-Kohout and
  Zurek** (refs. [13]–[15]): the model results and the selectivity theorem
  this review relies on. Not held.
- **Wootters–Zurek, Dieks** (refs. [20], [21]): no-cloning, evaded by
  copying observables.
- **Gleason** (ref. [35]) and the critiques **Schlosshauer and Fine**,
  **Barnum** (refs. [36], [37]) for the Born-rule derivation.
- **Wheeler's "It from bit"** (ref. [39]), named as one way to think of the
  transition.
- Nothing in it on spectrum broadcast structures or strong quantum
  Darwinism, which postdate it; the paper's only refinement of mutual
  information is the switch to Shannon entropies of specific observables
  (Fig. 3; p. 5).

## Bearing on the record

- **QUESTION-tmpubsi9: the "redundant record" rung, as the paper has it,
  and what it adds to the "stable record" rung.** The exchange's
  description is right on the main points: pointer observables are copied
  into many fragments (eq. 4, Fig. 2, p. 3), and observers learn them
  "independently, and without perturbing it" (p. 2), "indirectly" (p. 3).
  Two things the question can use. First, the paper separates rungs the
  question keeps apart: decoherence (correlation with E) can happen without
  usable records, since a completely mixed environment "is useless (even
  though it can still induce decoherence!)" and air molecules decohere a
  system while their records become "effectively undecipherable" (p. 4).
  So correlation and accessible record come apart, with the medium's
  structure deciding which. Second, the paper ties the record rung to
  repeatability, its postulate (iii), and derives the outcome set from it
  (eq. 5): what can be recorded repeatedly without disturbance is exactly an
  orthogonal set. That is a physical criterion for "measurement" as
  separating alternatives into distinguishable outcomes, without an
  observer. Its p. 6 move, "Transfer of responsibility for repeatability
  from a quantum S to a (still quantum) A", is an apparatus in
  TERM-tmpjdel0's operational sense, with differentiation (copying) and
  retention (the pointer states) and nothing of use or revision. The
  Discussion touches the stable-record rung too: memory is finite, "old
  events will be eventually 'overwritten'", "if there is no record of an
  event, has it really happened?" (p. 9), a question about persistence the
  paper raises and does not pursue (Di Biagio and Rovelli, LIT-tmpqu50n,
  unread, is the record's other source for it).
- **The exchange's caveat is not in this paper.** "Mutual information alone
  does not guarantee independently accessible classical records" is not
  said here; the paper asserts the opposite inference: "Rapid rise and
  gradual leveling of I(S : F_f), Fig. 2, implies redundancy" (p. 3), and
  "Large redundancy implies objectivity" (Fig. 2). What it does have is a
  partial version of the worry: it notes that von Neumann mutual
  information can rise above H_S toward 2H_S through global, quantum
  correlations (Fig. 2, p. 4), calls H_S "the classically accessible
  information" on that ground, and switches to Shannon entropies of
  specific observables to ask "What observable is this information about?"
  (p. 5). Independence of observers is argued from the commuting of
  different fragments' observables plus "underlying correlations" (p. 3),
  not from any condition on the joint state of system and fragments. The
  A19 attribution of the caveat to later work is consistent with this
  reading; that work is not held and was not checked. THEORY-tmp0d0qe
  files the finding with this limit.
- **THEORY-621: a different route to inter-observer agreement, and a
  shared refusal.** THEORY-621's promote_when asks for a result that what
  one system records about another agrees across observers. Zurek gives a
  mechanism for agreement: observers who read disjoint fragments of a
  redundantly imprinted environment find "the same state of the system"
  (p. 3). But the setting is not RQM's: facts are not indexed to systems,
  probabilities come from the Born rule (derived by envariance, section
  IV), and agreement is shown only for pointer observables in models, and
  argued, not proved, for observers in general. So it does not meet the
  promote_when; it suggests what such a result might look like (consensus
  through a shared medium). The two agree that the universe has no
  quantum state to take as real: "there is only one copy of the Universe.
  Treating its state as if it really existed … seems unwarranted and
  'classical'" (p. 6), against THEORY-621's "no quantum state of the
  universe". Zurek's reason is different (objectivity needs copies), and
  he calls his account "interpretation-free" (p. 6). Rovelli's "stable
  facts" via decoherence (THEORY-621's p. 3) is the einselection half of
  this paper.
- **CLAIM-tmpmx2ql: weak, and only for the first half.** The paper's
  dynamics have a scale separation in kind: superpositions "produce entropy
  rapidly, at decoherence rates", while pointer states produce least
  (pp. 1–2), so after decoherence the pointer basis is what persists and
  fixes the set of possible outcomes for whatever reads the environment.
  That is the claim's "separation makes a constraint" in a quantum case.
  But the paper gives no time scales, and its "Collapse is brief compared
  to the ensuing period of certainty … as f_δ ≪ 1" (p. 6) is a ratio of
  fragment sizes standing in for times, not a derived separation. Support
  of the shape, no more.
- **THEORY-017: the paper takes its parts from outside.** Quantum Darwinism
  needs a system–environment split and a subdivision of E into
  "individually accessible" subsystems whose observables commute (Fig. 1).
  The paper supplies both by assumption. That is THEORY-017's point (a
  factorisation is extra data), here in a work whose objectivity claim
  depends on which factorisation is chosen.
- **NOTE-044 (Grangier and Auffèves)** names quantum Darwinism as the
  reductionist programme its postulate excludes, without engaging it. This
  reading is what that note's C6 would be checked against.
- **CLAIM-342.** Redundancy is a way evidence can reach many observers
  without passing through any one observer's reading of it (p. 3). That is
  a physical instance of evidence whose arrival does not pass through the
  interpretation it tests, at the level of records. It says nothing of
  judgement loops; noted only.
- **No instruction for machine-learning practice.**

## Limitations

- **A review.** The quantitative results (plateau shape, redundancy scaling,
  selectivity, mixed environments) are cited from refs. [12]–[19], two of
  them "in preparation". Fig. 2 is schematic. The theorem that only pointer
  states can be discovered from fragments is cited, not stated.
- **Objectivity is an identification, not a theorem.** "Large redundancy
  implies objectivity" (Fig. 2) and "Consensus between copies suggests
  objective existence" (p. 3) move from an information measure to a
  property of observers' access. The paper does not give conditions under
  which fragment records are each sufficient and mutually consistent for
  every observer.
- **The S/E split and the fragment structure are assumed.**
- **The Born-rule derivation** depends on facts (1)–(3) and on equal
  probabilities for Schmidt partners; its extension beyond the worked
  example is asserted; the cited critiques are not answered here.
- **"Largely settled"** is the author's verdict; single outcomes are
  addressed by "perception of 'collapse'" (p. 6) while the paper abstains
  on the reality of other branches.
- **Extraction.** Figure contents are lost; the QBM expression and the
  Box's state are reconstructed. The published journal text was not
  compared.

## Open questions

- Under what condition on the joint state of S and several fragments does
  a mutual-information plateau guarantee that distinct observers, each
  reading one fragment, obtain the same pointer outcome without
  disturbing S? This is the question the later strong-Darwinism and
  spectrum-broadcast work is standardly cited for (THEORY-tmp0d0qe).
- What fixes which environments preserve records (photons) and which
  scramble them (air), quantitatively, and over what times (p. 4)?
- The paper's last question: is quantum Darwinism "in some way behind the
  familiar natural selection" (p. 9)?
- Do the assumptions of the envariance argument hold up against refs. [36],
  [37]?
