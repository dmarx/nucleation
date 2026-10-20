---
number: 987
status: Read
formerly:
- NOTE-tmpvy64o
paper: LIT-1244
title: 'Rosas, Mediano et al. — Reconciling emergences'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the publisher's open-access copy (PLOS Comput Biol
    16(12): e1008289, CC BY, 22 pp.) and its S1 Appendix (dated 19 November
    2020, 10 pp.), both fetched from journals.plos.org and extracted with
    pdftotext. The appendix was also compared with arXiv:2004.08220v1, whose
    Appendices A–F carry the same text (lemma numbering differs by one).
    Read: every section of the main text, the three toy examples, Lemma 1,
    Theorems 1–3, Corollary 1, Propositions 1–2, the discussion and
    limitations; in the appendix, Lemma 2 (Lemma 3 in the arXiv copy) with
    its proof, the five axioms, Corollary 2, the proofs of Lemma 1, Theorems
    1–3 and Propositions 1–2, the simulation details and the ECoG pipeline.
    Several displayed equations were garbled by extraction and were
    reconstructed from the arXiv copy, whose extraction kept the symbols
    (Ψ, Δ, Γ). Figures 4–6 and S1 Fig B were read from page renders; their
    values below are read off the plots and are approximate. Fig 3 (the ΦID
    lattice) was read from its caption only. The proof of the perfectly
    decoupled case ends mid-sentence in both copies. The code repository
    was not run. Small claims were re-checked with scripts in the session
    scratchpad, not in the repository.
date: '2026-10-20'
summary: >-
  The primary paper behind [LIT-025](../literature.d/LIT-025.md). A supervenient feature V is causally
  emergent of order k iff Un⁽ᵏ⁾(V_t; X_t′ | X_t) > 0; a system has one iff
  Syn⁽ᵏ⁾(X_t; X_t′) > 0, and the witness the proof gives is the microstate
  itself. Syn⁽ᵏ⁾ = D⁽ᵏ⁾ + G⁽ᵏ⁾ by definition of the ΦID atoms. The
  practical criteria Ψ, Δ, Γ are redundancy-free and sufficient only, and
  as proved they certify the system's capacity, not the candidate feature:
  under the minimum-MI decomposition the parity of two independent
  self-copying bits has Ψ = 1 bit and no emergence. Ψ is the whole-minus-sum
  information about V's next value minus V's one-step dynamical dependence,
  which ties it to Barnett–Seth dynamical independence ([THEORY-764](../theory.d/THEORY-764.md)).
---
<!-- inactive-ok-file: THEORY-497 THEORY-222 THEORY-257 — Proposed; the accounts this reading bears on, open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1137 — Deferred; registered unread, cited as open -->

# NOTE-987: Rosas, Mediano et al. — Reconciling emergences

## Contribution

It is the source the record has so far known only through the authors'
review ([LIT-025](../literature.d/LIT-025.md), [NOTE-010](NOTE-010.md)). It defines causal emergence of a
supervenient feature by partial information decomposition, proves that a
system hosts such a feature exactly when its parts carry synergy about their
own future, and splits that synergy, through ΦID atoms, into downward
causation and causal decoupling. It states the axioms a redundancy function
must meet for the theory to hold, which the review did not, and it gives
three redundancy-free practical criteria, Ψ, Δ and Γ. It applies Ψ (and
twice Γ) to the Game of Life, Reynolds boids and macaque ECoG.

## Key insight

Supervenience is a relation at one time and predictive power runs across
time, so a feature fully fixed by the present microstate can still carry
information about the future that no small group of parts carries
separately. "Emergence" here means that kind of irreducibility, relative to
a fixed partition into parts. It does not mean that a coarse description
predicts better than the fine one. By the data-processing inequality
I(V_t; V_t′) ≤ I(X_t; X_t′) it never can, which is the paper's own argument
against reading observational mutual information Hoel's way.

## Assumptions

- **A fixed partition** X_t = (X¹_t, …, Xⁿ_t), fully observed, with
  Markovian dynamics p(X_t′ | X_t) and two time points t < t′. "Emergence in
  the context of our theory always refers to 'emergence with respect to a
  given microscopic partition.'" The Markov and full-observation conditions
  are named as limitations in the discussion.
- **Supervenience (Definition 1).** V_t − X_t − X_t″ is a Markov chain for
  every t″ ≠ t. Deterministic V_t = F(X_t) and F(X_t) plus independent noise
  qualify; features computed over several time points generally do not.
- **Axioms on the PID (S1 Appendix §2).** The theory holds "for any PID"
  that meets them:
  - *deterministic equality* (if one source is a function of another, the
    decomposition reduces to that of the smaller set);
  - *non-negativity*, Syn⁽ᵏ⁾ ≥ 0 and min{I(Z;Y), I(Z;Y|X)} ≥ Un⁽ᵏ⁾(Z;Y|X) ≥
    0 (see Limitations: the second half is misstated);
  - *source data-processing* for Un⁽ᵏ⁾ along W − Z − (X, Y);
  - for D⁽ᵏ⁾, a ΦID bound Σ_{|α|=k} Syn⁽ᵏ⁾(X_t; X^α_t′) ≥ D⁽ᵏ⁾ ≥
    Syn⁽ᵏ⁾(X_t; X^β_t′) for every |β| = k, assumed, not derived;
  - for the practical criteria, *whole-minus-sum*, Syn⁽ᵏ⁾(X;Y) ≥ I(X;Y) −
    Σ_{|α|=k} I(X^α;Y), and *target data-processing*, Syn⁽ᵏ⁾(X;U) ≤
    Syn⁽ᵏ⁾(X;Y) along X − Y − U.
  - The appendix says the minimum-mutual-information (MMI) PID and its ΦID
    meet them all ("direct to check"; not shown).
- **For an interventional reading,** p(X_t, X_t′) must come from
  interventions; otherwise the quantities are Granger-type predictive ones.
  The paper takes no stand ("without taking a rigid stance on a theory of
  causality").

## Key results

- **k-th-order atoms (Lemma 2, S1 §1).** With S⁽ᵏ⁾ the antichains all of
  whose sets have more than k sources, U⁽ᵏ⁾(β) those containing β with every
  other set of size > k, and R⁽ᵏ⁾ those with two or more sets of size ≤ k,
  I(X;Y) = Red⁽ᵏ⁾ + Syn⁽ᵏ⁾ + Σ_{|β|≤k} Un⁽ᵏ⁾(X^β; Y | X^{−β}). The proof
  shows the three index sets partition the lattice, so it is exact for any
  PID. Checked.
- **Definition 2.** V_t is causally emergent of order k iff Un⁽ᵏ⁾(V_t; X_t′
  | X_t) > 0, the unique information computed in the PID with V_t added as an
  (n+1)-th source.
- **Lemma 1.** An order-1 emergent feature needs n ≥ 2 and is no
  deterministic function of a single part.
- **Theorem 1.** X_t has a causally emergent feature of order k iff
  Syn⁽ᵏ⁾(X_t; X_t′) > 0. **Corollary 1:** Un⁽ᵏ⁾(V_t; X_t′ | X_t) ≤
  Syn⁽ᵏ⁾(X_t; X_t′) for every supervenient V_t, the "emergence capacity".
  - The forward direction takes V_t = X_t: by Lemma 2 (the microstate as an
    extra source), Un⁽ᵏ⁾(X_t; X_t′ | X_t) = Syn⁽ᵏ⁾(X_t; X_t′). The authors
    say so: the system has emergent behaviour "if and only if the system as a
    whole seen as a feature (i.e. V_t = X_t) is causally emergent", and the
    microstate "in most cases also carries non-interesting information".
  - So the bound of Corollary 1 is attained by the microstate. Maximizing
    emergence over features selects no coarse-graining.
- **Taxonomy (Eqs. 4–7).** Each PID atom splits into ΦID atoms I∂^{α→β}.
  - D⁽ᵏ⁾ := Σ_{α∈S⁽ᵏ⁾, β∈A∖S⁽ᵏ⁾} I∂^{α→β}: synergistic sources to targets
    that some group of ≤ k future parts holds.
  - G⁽ᵏ⁾ := Σ_{α,β∈S⁽ᵏ⁾} I∂^{α→β}: synergistic sources to synergistic
    targets.
  - Syn⁽ᵏ⁾ = D⁽ᵏ⁾ + G⁽ᵏ⁾ (Eq. 7). This holds by the definitions, since every
    target node lies in S⁽ᵏ⁾ or outside it. The review's "exhaustive" is a
    tautology of the bookkeeping, not a finding.
- **Downward causation (Definition 3, Theorem 2).** V_t exerts it at order
  k iff Un⁽ᵏ⁾(V_t; X^α_t′ | X_t) > 0 for some |α| = k. A system admits such
  features iff D⁽ᵏ⁾ > 0. The proof rests on the assumed ΦID bound above.
- **Causal decoupling (Definition 4, Theorem 3).** V_t exhibits it at order
  k iff Un⁽ᵏ⁾(V_t; V_t′ | X_t, X_t′) > 0: information V_t and V_t′ share that
  no group of ≤ k parts at t or t′ has. *Pure* decoupling: emergent and
  Un⁽ᵏ⁾(V_t; X^α_t′ | X_t) = 0 for every |α| = k. A system admits decoupled
  features iff G⁽ᵏ⁾ > 0 (via Corollary 2, which needs "a natural
  multi-target extension" of deterministic equality), and is perfectly
  decoupled if G⁽ᵏ⁾ > 0 and D⁽ᵏ⁾ = 0.
- **Practical criteria (Eq. 10, S1 Eq. D1), k = 1:**
  - Ψ(V) := I(V_t; V_t′) − Σ_j I(X^j_t; V_t′);
  - Δ(V) := max_j [ I(V_t; X^j_t′) − Σ_i I(X^i_t; X^j_t′) ];
  - Γ(V) := max_j I(V_t; X^j_t′).
  - For general k, the sums and maxima run over groups of k parts.
- **Proposition 1** as stated: Ψ > 0 is sufficient for V_t to be causally
  emergent, Δ > 0 for V_t to exert downward causation, and Ψ > 0 with Γ = 0
  for causal decoupling.
  - What the proof shows is weaker (see Limitations). Ψ(V) ≤ I(X_t; V_t′) −
    Σ I(X^α_t; V_t′) ≤ Syn⁽ᵏ⁾(X_t; V_t′) ≤ Syn⁽ᵏ⁾(X_t; X_t′). So Ψ > 0 gives
    the *system* emergence capacity, and with Theorem 1 the existence of some
    emergent feature.
  - These are sufficient conditions only. Ψ ≤ 0 is "inconclusive", and
    redundancy among the parts is counted up to n times.
- **Synergistic channels (Eqs. 11–14).** Syn⁽ᵏ⁾_⋆ := sup I(V; X_t′) over
  channels p(V | X_t) whose output is independent of every k-group of parts.
  G⁽ᵏ⁾_⋆ uses such channels at both ends, and D⁽ᵏ⁾_⋆ := Syn⁽ᵏ⁾_⋆ − G⁽ᵏ⁾_⋆ ≥
  0. This is the one specific decomposition the paper names, from Rosas,
  Mediano, Rassouli and Barrett's synergistic-disclosure PID.
  **Proposition 2:** for stationary X_t, every autocorrelated k-synergistic
  observable is k-th-order emergent. Nothing in the case studies computes
  these quantities.
- **Case studies.** Only Ψ and Γ are computed, never an atom, so no
  redundancy function enters any reported number.
  - *Game of Life.* A 15 × 15 board (n = 225) set up as a "particle
    collider" with randomised particle types and positions. V_t is the
    indicator vector of particle types, and t′ − t = 1000 steps.
    5 × 10⁴ runs, Archer et al.'s quasi-Bayesian estimator.
    - Ψ = 0.58 ± 0.02, from I(V_t; V_t′) = 0.99 and Σ_i I(Xⁱ_t; V_t′) = 0.41
      (Fig 4).
    - Γ = 0.009 ± 0.0002, which the authors say "suggest[s]" decoupling.
  - *Boids.* N = 10 on a torus, a₁ = 0.15 and a₃ = 0.25 fixed, avoidance a₂
    swept from 0 to 0.2. V is the centre of mass. Trajectories were
    preprocessed as in Seth (2010) and the KSG estimator used.
    - Read off Fig 5a: Ψ ≈ −0.3 with a very wide error bar at a₂ = 0, ≈ 0.8
      at 0.05, falling to ≈ 0.1 at 0.2.
    - The low-a₂ failure is attributed to redundancy, not to a lack of
      synergy. Γ is not reported.
  - *Macaque ECoG.* 64 channels and wrist motion capture from Neurotycho.
    V_t = F(X_t) ∈ ℝ³ is a PLS (20 components) plus SVM decoder trained on 60%
    of the data. Ψ was computed on the rest with JIDT's Gaussian estimator.
    - At t′ − t = 8 ms, Ψ = 1.275 ± 0.002 and Γ = 0.049 ± 0.002. Ψ stays
      positive out to about 0.2 s.
    - A decoder trained on time-shuffled wrist positions gives a lower Ψ.
      Read off S1 Fig B, that surrogate is about 0.95 at 8 ms, against
      1.275.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | I(X;Y) splits exactly into Red⁽ᵏ⁾, Syn⁽ᵏ⁾ and the Un⁽ᵏ⁾ terms for any PID | strong | Lemma 2, a partition of the lattice; checked |
| C2 | A system has a k-th-order causally emergent feature iff Syn⁽ᵏ⁾(X_t;X_t′) > 0, and Syn⁽ᵏ⁾ bounds every feature's emergence | strong, given the axioms | Theorem 1 and Corollary 1, proved; the witness is V = X_t |
| C3 | Syn⁽ᵏ⁾ = D⁽ᵏ⁾ + G⁽ᵏ⁾, and D⁽ᵏ⁾ > 0 (G⁽ᵏ⁾ > 0) iff the system admits downward-causing (decoupled) features | strong for the identity (definitional); moderate for the iffs | Eq. 7; Theorems 2–3 rest on an assumed ΦID bound and an assumed multi-target deterministic equality |
| C4 | Ψ > 0 suffices for the candidate V to be causally emergent; Δ > 0 for V to exert downward causation; Ψ > 0 and Γ = 0 for V to be causally decoupled | weak as stated; strong for the system-level reading | Proposition 1's proof reaches Syn⁽ᵏ⁾(X_t;X_t′) > 0 only. Under MMI the claim about V fails (Limitations) |
| C5 | The practical criteria hold for every PID that meets the axioms | strong for the system-level reading | each step uses only whole-minus-sum and the two data-processing axioms |
| C6 | Particle collisions in the Game of Life, the boids' centre of mass and the decoded wrist position are causally emergent; GoL particles and the ECoG feature may be causally decoupled | weak to moderate | Ψ > 0 in simulation and data. That gives the systems capacity, not these features emergence; Γ is never 0; decoupling is hedged as "suggest" |
| C7 | Hoel's effective-information emergence cannot be read off observational mutual information, because I(V_t;V_t′) ≤ I(X_t;X_t′); its maximum-entropy interventions count transitions the system never makes | strong for the inequality; argued for the rest | data-processing inequality; §Relationship with other theories |
| C8 | Seth's G-emergence autonomy I(V_t;V_t′|X_t) > 0 conflates unique and synergistic information | weak as written | for a supervenient V_t in the paper's own sense, I(V_t;V_t′|X_t) = 0 always, so the example offered cannot arise (Limitations) |

## Concepts

- **Supervenient feature**: V_t with V_t − X_t − X_t″ Markov for all
  t″ ≠ t.
- **k-th-order synergy Syn⁽ᵏ⁾(X;Y)**: the information about Y that the whole
  provides and no group of ≤ k parts holds, considered separately from the
  rest.
- **Emergence capacity**: Syn⁽ᵏ⁾(X_t; X_t′).
- **Causal emergence of V (order k)**: Un⁽ᵏ⁾(V_t; X_t′ | X_t) > 0.
- **Downward causation**: Un⁽ᵏ⁾(V_t; X^α_t′ | X_t) > 0 for some group α of
  k future parts. System index D⁽ᵏ⁾: synergistic-source → non-synergistic
  target atoms.
- **Causal decoupling**: Un⁽ᵏ⁾(V_t; V_t′ | X_t, X_t′) > 0. System index
  G⁽ᵏ⁾: synergistic-source → synergistic-target atoms. *Pure* decoupling
  adds that V predicts no k-group of future parts uniquely, a "statistical
  ghost". The parity of Example 1 is the paper's case of it.
- **k-synergistic observable**: the output of a channel independent of
  every group of k parts.
- **Order k**: the size of the groups of parts excluded, the paper's
  "scale". It is not a coarse-graining.

## Connections

The paper places itself after Seth's G-emergence (2010), Hoel, Albantakis
and Tononi's effective information ([LIT-1038](../literature.d/LIT-1038.md), [THEORY-222](../theory.d/THEORY-222.md)) and Chang et
al.'s non-trivial informational closure. It builds on Williams and Beer's
PID and on Mediano et al.'s ΦID ("Beyond integrated information"), and it
names Rosas et al.'s synergistic-disclosure PID as one concrete
decomposition. The review that restates it is [LIT-025](../literature.d/LIT-025.md). Barnett and Seth's
dynamical independence ([LIT-979](../literature.d/LIT-979.md)), a paper with a shared author, came later
and is not cited here. The paper's closest relative to it is the NTIC
discussion: "NTIC requires features that are sufficient statistics for
their own dynamics, which is akin to our concept of causal decoupling."
That kinship is loose; see Bearing on the record.

## Bearing on the record

- **[THEORY-497](../theory.d/THEORY-497.md)** gets its first-hand source. What this reading
  establishes for it:
  - *The conditions of the iff theorem* are the axioms above. The
    witness is the microstate itself.
  - *Exhaustiveness.* The split into D and G is exhaustive by
    definition.
  - *The case studies use no redundancy function.* They use Ψ and Γ only.
    The review's silence on which function the applications used ([NOTE-010](NOTE-010.md))
    has that answer.
  - *What the axioms exclude.* Whole-minus-sum together with target
    data-processing forces Syn⁽¹⁾ ≥ 1 bit for two independent bits that
    each copy themselves. Take Y = X¹′ ⊕ X²′: then I(X;Y) = 1 and each
    I(Xʲ;Y) = 0. A measure with the identity property (Bertschinger et
    al., Harder et al.) gives 0 synergy for that copy system, and 1 bit
    for the XOR target. So it breaks target data-processing, and the
    paper's admissible class excludes it. MMI is in that class.
  - *[NOTE-010](NOTE-010.md)'s permutation example.* The same argument with Y = X¹′ =
    X¹⊕X² gives that example Syn⁽¹⁾ ≥ 1 bit under every admissible PID.
    So, inside the theory's own class, the disagreement with effective
    information that [NOTE-010](NOTE-010.md) found does not depend on the redundancy
    function. It vanishes only for measures the axioms rule out.
  - The coordinator may want [THEORY-497](../theory.d/THEORY-497.md)'s source, Connections and
    promote_when revised accordingly (see the report).
- **[THEORY-257](../theory.d/THEORY-257.md), [THEORY-733](../theory.d/THEORY-733.md): causal decoupling against dynamical
  independence.**
  - *They are different conditions.* Decoupling is about irreducibility:
    V's self-information is not held by any small group of parts. Barnett
    and Seth's independence is about sufficiency: the micro history adds
    nothing to V's self-prediction.
  - *The link the record can prove.* For any deterministic supervenient V
    and a Markov X,
    Ψ(V) = [I(X_t; V_t′) − Σ_j I(Xʲ_t; V_t′)] − I(V_t′; X_t | V_t).
    The last term is the one-step dynamical dependence, and its vanishing
    implies Barnett–Seth independence. Filed as [THEORY-764](../theory.d/THEORY-764.md), with
    examples both ways.
  - *Example 1's "statistical ghost".* The parity is exactly dynamically
    independent (one-step dependence 0, checked). There the two accounts
    agree.
  - *A parity that is not independent.* If its persistence probability
    depends on one bit, the parity passes the paper's decoupling test
    (Ψ = 0.231 bits, Γ = 0, n = 3). It is not dynamically independent: its
    one-step dependence is 0.141 bits.
  - *Independence without emergence.* A single part that copies itself is
    dynamically independent. By Lemma 1 it is not emergent.
- **[QUESTION-115](../questions.d/QUESTION-115.md)** (do retention, dynamical independence, effective
  information and an Occam price pick the same level?).
  - *ΦID emergence picks no level.* By Corollary 1 and the proof of Theorem 1,
    Un⁽ᵏ⁾(V; X_t′ | X_t) is maximized by V = X_t, the microstate. Only a price
    on description length would select a coarse feature. The authors gesture
    at one (H(V_t) < H(X_t)) and do not impose it. So this criterion needs
    the Occam price the question names as much as Krakauer et al.'s
    measures do ([LIT-1137](../literature.d/LIT-1137.md)).
  - *It answers a different question from effective information.* Effective
    information ([THEORY-222](../theory.d/THEORY-222.md)) ranks levels by how much they say. Ψ and Un⁽ᵏ⁾
    ask whether a feature's information is held by small groups of parts.
    The paper's own data-processing argument rules out a "macro beats
    micro" reading of observational information.
  - *Ψ and dynamical independence.* Ψ rewards dynamical independence and
    penalizes redundancy among the parts ([THEORY-764](../theory.d/THEORY-764.md)).
  - *A pair of predictions on which the criteria part.* A dynamically
    independent single part fails ΦID emergence. A non-independent parity
    passes the decoupling test.
  - *Where they agree, it need not be integration.* The sum of n ≥ 2
    independent, identical Gaussian AR(1) channels is exactly dynamically
    independent, and it passes Ψ > 0 for every coefficient 0 < |a| < 1
    (re-derived; for a = 0.9 and n = 2, Ψ = 0.449 bits, checked by
    simulation). Persistence of an aggregate of non-interacting parts is
    enough for both. That bears on A12's guard that "integration licenses
    a module": Ψ > 0 does not license one.
- **[QUESTION-218](../questions.d/QUESTION-218.md)** (what is the unit when there is closure without a
  block?). ΦID's emergent features are functions of the whole state. Lemma
  1 forbids a function of one part, and the theorem's witness is the whole
  microstate. Example 1's parity is a closed collective mode of the kind
  [CLAIM-388](../claims.d/CLAIM-388.md) names: it is dynamically independent, no part predicts the
  future of any part, and it is no block. It adds a fourth candidate
  unit beside those [NOTE-979](NOTE-979.md) lists: a feature whose self-prediction
  is synergistic across the parts.
- **[QUESTION-222](../questions.d/QUESTION-222.md)** (memory). The theory assumes a Markov, fully observed
  X. The ECoG case violates both, as the authors say, and their suggested
  remedy is delay embedding. Ψ's dependence term conditions on V_t alone,
  not on V's history. A non-Markov reduction would separate the two (see
  [THEORY-764](../theory.d/THEORY-764.md)).
- **No bearing** on [QUESTION-217](../questions.d/QUESTION-217.md), [QUESTION-220](../questions.d/QUESTION-220.md), [QUESTION-221](../questions.d/QUESTION-221.md) or
  [QUESTION-219](../questions.d/QUESTION-219.md) beyond the above. The paper has no coupling strength, no
  nesting of abstractions and no fluxes.
- No instruction for machine-learning practice. The ECoG decoder is a tool,
  not a recommendation. Nothing for the anthology.

## Limitations

- **Proposition 1 claims more than its proof shows.**
  - The chain (D2)–(D4) ends at Syn⁽ᵏ⁾(X_t; X_t′) > 0. Combined with Theorem
    1, that says *some* feature, possibly the microstate, is emergent. It
    does not say the candidate V is.
  - *Counterexample under MMI, which the appendix names as admissible.* Take
    two independent bits that each copy themselves, with V = X¹ ⊕ X². Then
    Ψ(V) = 1 bit. But in the three-source MMI PID of (X¹, X², V) about X_t′,
    all of V's information is redundant with X¹, so Un⁽¹⁾(V; X_t′ | X_t) = 0
    (computed).
  - The same gap affects Δ: its proof reaches D⁽ᵏ⁾(X_t; X_t′) > 0 and then
    cites "Theorem 1" where Theorem 2 is meant.
  - The same gap affects Γ. Its proof shows only that Γ = 0 rules out V's
    downward causation. It never shows Un⁽ᵏ⁾(V_t; V_t′ | X_t, X_t′) > 0,
    which Definition 4 requires.
  - So the conclusions that GoL particles, the flock's centre of mass and
    the decoded wrist position "are" emergent rest on an unproved step.
    What the data support is that each system has emergence capacity, under
    every admissible PID.
- **Γ = 0 is never met.** GoL gives Γ = 0.009 and ECoG 0.049. The criterion
  has no continuity bound, so a small Γ licenses nothing.
  - For ECoG, "orders of magnitude smaller" compares Γ with Ψ, and the ratio
    is about 26.
  - The authors' own hedges, "suggest" and "may", are the right strength.
- **The ECoG surrogate is itself strongly positive.** A decoder trained on
  shuffled wrist positions gives Ψ ≈ 0.95 at 8 ms, about three-quarters of
  the observed 1.275 (S1 Fig B, read off the plot).
  - The main text says only that the surrogate is "significantly lower".
    It does not say that the surrogate is itself well above zero.
  - That fits the AR(1) result above: a smooth projection of many
    autocorrelated channels passes Ψ > 0 without any motor content or
    interaction.
  - It is also unclear whether the sum over parts ran over the 64
    electrodes, as the main text says (X_t ∈ ℝ⁶⁴), or over the 20 PLS
    components the appendix projects onto. The partition matters by the
    paper's own account.
- **A misstated axiom.** Read literally, non-negativity's bound Un⁽ᵏ⁾(Z; Y |
  X) ≤ I(Z; Y | X) with X the whole system makes Definition 2 vacuous. Every
  supervenient V has I(V_t; X_t′ | X_t) = 0. It also contradicts Lemma 2,
  where Un⁽ᵏ⁾(X_t; X_t′ | X_t) = Syn⁽ᵏ⁾ > 0 while I(X_t; X_t′ | X_t) = 0.
  The intended bound is presumably by I(Z; Y | X^α) for each group α of ≤ k
  parts. Lemma 1's proof goes through under that reading. Both copies carry
  the literal form.
- **Theorems 2 and 3 rest on assumptions about ΦID,** not on its axioms:
  the D⁽ᵏ⁾ sandwich bound and a multi-target deterministic equality. The
  paper does not show that any ΦID other than MMI's satisfies them, and it
  shows MMI's only by assertion.
- **The axioms exclude identity-respecting redundancy measures,** as shown
  above. So the theory is not "agnostic" across PIDs. It is agnostic across
  a class that includes MMI and excludes Bertschinger et al.'s and Harder et
  al.'s measures. For three or more parts, [THEORY-713](../theory.d/THEORY-713.md) and [CLAIM-343](../claims.d/CLAIM-343.md)
  already show those cannot keep non-negativity anyway.
- **Emergence without interaction.** By those axioms, two non-interacting
  self-copying bits have emergence capacity, and their parity passes Ψ.
  This is the record's inference, not the paper's. Example 1's narrative
  ("no individual variable has any predictive power") makes emergence look
  like a property of coupled collectives. The axioms do not require that.
- **Seth's criterion misrendered.** For supervenient V_t, I(V_t; V_t′ | X_t)
  = 0 (by the chain rule, because V_t carries nothing beyond X_t). So the
  paper's example of Seth's autonomy "> 0 while I(V; V_t′) = 0" cannot occur
  for the features the theory admits. Seth's own measure conditions on
  histories.
- **Partition dependence,** which the authors state openly and leave open.
- **Equilibrium systems are out of scope:** a Gibbs distribution does not
  fix the dynamics (Glauber against Kawasaki).

## Open questions

- Is Proposition 1's claim about the candidate feature true under some
  admissible PID, and which? A proof that Ψ(V) > 0 implies Un⁽ᵏ⁾(V; X_t′ |
  X_t) > 0 under a named decomposition would settle it. The MMI
  counterexample shows it cannot hold for all of them.
- A continuity bound for Γ: how small must Γ be, relative to what, for
  decoupling to follow?
- With a description-length price on V, which feature maximizes
  Un⁽ᵏ⁾(V; X_t′ | X_t)? Does it coincide with a dynamically independent one?
  That is [QUESTION-115](../questions.d/QUESTION-115.md)'s comparison made concrete.
- Does the ECoG verdict survive a surrogate that keeps each channel's
  autocorrelation but destroys cross-channel structure? Per-channel
  phase randomization would test interaction rather than persistence.
- How do emergence verdicts move under an invertible remixing of parts,
  such as EEG source mixing? The authors pose this one themselves.
