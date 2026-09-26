---
number: 139
status: Read
formerly:
- NOTE-tmpjfcsj
paper: LIT-163
title: 'Wenmackers — Philosophy of probability (PhD thesis)'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the thesis PDF from the author's website (180
    PDF pp.; xii + 166 printed pp.). I read Chapters 1–6 in full, including
    both appendices to Ch. 5 (A, the derivation of eq. 5.1; B, the
    log-normal fits with Tables 5.4–5.5), the English Summary, and the List
    of Publications. The bibliography (pp. 139–154) was consulted only for
    specific entries. The Dutch Samenvatting, the acknowledgements, the
    conference list and the CV were not read. Figures were seen only through
    their captions (text extraction).). Upgraded from `Skimmed` to `Read`:
    the claims table, assumptions and results are new, and the skim is
    corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  A fair lottery on ℕ gets a uniform, regular probability on all of 𝒫(ℕ)
  by normalising Benci–Di Nasso numerosities, P_num(A) = num(A)/α. This is
  hyperrational-valued, determined only up to the choice of free
  ultrafilter, and "hypercountably" (really hyperfinitely) additive rather
  than countably additive, with st∘P_num = generalised asymptotic density
  (§2.5–2.6). The same "rounding-error" diagnosis gives Stratified Belief,
  a contextual Lockean thesis on which conjunction holds for a standard
  number of beliefs (Ch. 3). A separate agent-based model (Ch. 5) finds
  that one round of bounded-confidence averaging sends an agent to the
  inconsistent theory with probability at most 1.81 % in the cases
  computed (M = 2, 3 atomic sentences).
---

# NOTE-139: Wenmackers — Philosophy of probability (PhD thesis)

## Contribution

The thesis constructs an explicit probability function for a fair lottery on ℕ, P_num(A) = num(A)/α with num(A) = [⟨#(A∩{1..n})⟩]_U. The function is defined on all of 𝒫(ℕ), uniform, regular (each ticket gets 1/α > 0), and additive in a hypercountable sense. The thesis proves that its standard part equals Hahn–Banach asymptotic density. It then transfers the idea of an infinitesimal "rounding error" to rational belief. Relative (stratified) analysis turns the Lockean thesis into Stratified Belief, P(x) ≃_V 1, under which conjunction survives for "a few" beliefs. Separately, it gives the first exact count, with a sampling extension, of how often Hegselmann–Krause-style averaging over *theories* produces an inconsistent belief state. Finally, it sketches the Non-Archimedean Probability axioms (NAP0–4).

## Key insight

Both the failure of countable additivity for a fair infinite lottery and the failure of the conjunction principle in the Lottery Paradox are cast as an "adding problem". Each term carries a negligible rounding error, and "many × small" is not small (§4.2). Keeping the small quantities as (relative) infinitesimals instead of rounding them to 0 restores the adding rule within its proper scope. For the infinite lottery, the full rule holds over a hyperfinite index. For belief, conjunction holds over a standard ("few") number of conjuncts.

## Assumptions

- **Ch. 2**: the Axiom of Choice, since free ultrafilters exist only by Zorn's lemma (§2.6.1). ℕ = {1,2,3,…} carries its natural order: probabilities are *not* invariant under relabelling (LABEL is given up, §2.2.2). The intuitions FAIR, ALL and SUM are treated as desiderata, with FAIR "non-negotiable".
- **Ch. 3**: Hrbacek's relative analysis, with eight level axioms (§3.5.3.1) that include Stability, Closure, the Neighbor principle and density of levels. The Principal Principle holds, so subjective probability equals the objective lottery probability (p. 65). One context level per agent at a time (§3.6.4). Belief is binary: belief versus non-belief.
- **Ch. 5**: M atomic sentences; theories are subsets of the 2^M worlds (t_max = 2^(2^M)). Each of N agents independently draws a uniformly random consistent theory (an impartial culture). Updating is simultaneous, with homogeneous bound of confidence D (Hamming distance): each bit is averaged over neighbours and rounded, and a tie keeps the old bit. Only **one** update step is analysed. There is no truth-tracking, trust or network structure.
- **Ch. 6 (NAP)**: the range is an ordered field F chosen per problem, with a directed set of finite subsets Λ covering Ω.
- The author's standpoint is an "epistemic (intersubjective) approach to objective probability" (§1.3.2). The author declares she is not a Bayesian.

## Key results

- **Eq. 2.20–2.21**: P_num: 𝒫(ℕ) → *[0,1]_{*ℚ}, P_num(A) = num(A)/α = [⟨#(A∩{1..n})/n⟩]_U. A singleton gets 1/α; ℕ minus one ticket gets 1 − 1/α; each residue class mod m gets standard part 1/m (§2.6.4.2).
- **HCA theorem (eq. 2.27, §2.5.2.4)**: for disjoint {A_n}, num(⋃A_n) = Σ_{N∈*ℕ} (num⟨A_n⟩)_N, summing over the hyperextended family. For each family there is K ∈ *ℕ past which all terms vanish, so the additivity is effectively hyperfinite (HFA).
- **num is not CA (§2.5.2.2)**: no function into a non-standard set can be countably additive, because countable sums are undefined there.
- **Eq. 2.30**: st ∘ P_num = P_ad, the Hahn–Banach generalised asymptotic density, for every choice of ultrafilter. The real-valued solution's failure of SUM is quantified as accumulated rounding error: over all singletons, α·(1/α) = 1, "100% error".
- **Non-uniqueness (§2.6.2)**: one solution per free ultrafilter. For each m there are m scenarios, depending on which residue class is in U.
- **Hyperfinite lottery (§2.6.3)**: the internal measure *P_α on {1..α} is HFA by Transfer. The author argues it changes the problem, since ℕ is an external subset.
- **Stratified Belief, Def. 1 (eq. 3.4)**: B(x) ∈ R_{α,V} ⇔ P(x) ≃_V 1.
- **SCP, Def. 2 (eq. 3.5)**, with the generalisation in §3.6.3.2: if P(ψ(E1)) ≃_V 1 and P(ψ(E2)) ≃_V 1, then P(ψ(E1) ∧ ψ(E2)) ≃_V 1 (short proof). The rule fails for an ultralarge number of conjuncts (1 − N/N = 0).
- **SB_θ, Def. 3**: P(x) ≳_V θ. SCP then survives only for an arbitrary event plus a singleton. It is offered as a model of epistemicist vagueness.
- **Ch. 4 (§4.4)**: rational belief about a fair infinite lottery is obtained by two roundings: first the standard part, then relative-infinitesimal rounding.
- **Ch. 5**: exact analytical F_AG and F_OP (eq. 5.1). No zero-update occurs for M = 1, D = 1 or N = 2. The minimal case is M = 2, N = 3, D = 2, with F_OP = F_AG = 24/3375 = 0.711 %, checked by hand. Maxima are given in Table 5.3: F_AG ≤ 1.8112 % (M = 2), ≤ 0.3215 % (M = 3); F_OP up to 6.4298 % (M = 2), 16.867 % (M = 3, D = 6, N = 1780). Exact computation covered N ≤ 21 (M = 2) and N ≤ 4 (M = 3). Sampling used 10^6 profiles per point, up to N = 200 (M = 2) and N = 2500 (M = 3).
- **NAP0–4 (§6.2.3)**: domain 𝒫(Ω); P(A) = 0 ⇔ A = ∅; P(A) = 1 ⇔ A = Ω; finite additivity; a directed set of finite subsets implying a direct limit. Asserted consistent; the model is not given.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A uniform, regular, hyperrational-valued probability on all of 𝒫(ℕ) exists for a fair lottery | strong | explicit ultrafilter construction, §2.5.1 |
| C2 | It is hypercountably (hyperfinitely) additive | strong, but in a technical sense | proof of eq. 2.27, via Transfer over the hyperextended family |
| C3 | No non-standard-valued probability on 𝒫(ℕ) can be countably additive | moderate | short argument that ω-sums are undefined on *ℕ (§2.5.2.2) |
| C4 | Its standard part is the Hahn–Banach asymptotic density | strong | proof of eq. 2.30 |
| C5 | This gives "the SUM intuition its due" and is epistemologically preferable to de Finetti's FA solution | weak | informal argument; the two are empirically indistinguishable by the author's own admission (§2.6.4) |
| C6 | No choice of ultrafilter is privileged | weak | "as far as we can presently see" (§2.6.2, §2.7) |
| C7 | The threshold Lockean thesis violates CP even for two beliefs | strong | elementary derivation, eq. 3.3 |
| C8 | Stratified Belief satisfies conjunction for a standard number of beliefs but not for all | strong within relative analysis | proofs in §3.6.3 |
| C9 | The Lottery Paradox is fundamentally a symptom of vagueness that threshold models mishandle | weak | informal argument ("Observations 1–4", §3.4) |
| C10 | Stratified Belief is psychologically plausible | weak | analogy to Dehaene et al. on mental number lines (§3.6.4); the author calls the model "crude" |
| C11 | Stratified Belief models contextualist knowledge ascriptions (bank case) and the voting paradox | assertion | sketches in §3.7 |
| C12 | One-step averaging makes an agent inconsistent with probability < 2 % | moderate | exact enumeration plus sampling, for M = 2, 3 only |
| C13 | This probability "can be made arbitrarily small" by raising M or N | weak for M, moderate for N | M: two data points. N: sampled decreasing tails, with a law-of-large-numbers argument (§5.4.2). This is the abstract and Summary headline, and it claims more than the body shows |
| C14 | NAP0–4 are consistent and generalise the approach to any sample space | assertion | model and uncountable case deferred to future work |

## Method

- **Ch. 2**: characteristic bit string → partial sums S_n = #(A∩{1..n}) → ultrafilter class num(A) ∈ *ℕ → normalise by α.
- **Ch. 3**: formalise the Lockean thesis in Hrbacek's relative analysis, with levels as a context parameter and ≃_V as indistinguishability.
- **Ch. 5**: encode worlds and theories as bit strings. Update each bit by neighbourhood majority (Hamming distance ≤ D), with ties keeping the old bit. Count zero-updates over all anonymous profiles, weighted by multinomial coefficients (eq. 5.1); an Object Pascal program evaluated this. Sampling extends it (10^3 × 10^3 profiles per point), and log-normal curves are fitted in SigmaPlot (Appendix B).

## Concepts

- **FAIR, ALL, SUM, LABEL**: the four lottery intuitions (§2.2.1.2). Respectively: equiprobability; a probability for every set; supervenience of set probability on ticket probabilities; invariance under relabelling.
- **Numerosity**: the Benci–Di Nasso size of sets that respects the part–whole principle. num(ℕ) = α.
- **HCA/HFA**: hyper-countable/hyper-finite additivity, meaning summation over *ℕ or a hyperfinite initial segment.
- **Level; ultrasmall; ≃_V**: from relative analysis. A level is a predicate, not a set, and induction fails across it. Ultrasmall means a relative infinitesimal. ≃_V means ultraclose at level V.
- **Stratified Belief (SB), SB_θ, Stratified Conjunction Principle (SCP)**: Defs. 1–3, Ch. 3.
- **Zero-update**: updating to t = 0, the inconsistent theory. **F_AG / F_OP**: the agent-based and opinion-profile-based fractions of zero-updates.
- **Chance process**: a process where the available knowledge lets a rational agent specify at least two possible outcomes but not predict which (§1.3.3).
- **NAP**: Non-Archimedean Probability.

## Connections

The thesis builds on de Finetti's infinite lottery, Benci & Di Nasso's numerosities and alpha-theory, Robinson's NSA, Hrbacek's relative analysis, Kyburg's Lottery Paradox, Douven & Williamson (2006) on defeaters, and Hegselmann & Krause (2002) on opinion dynamics. It relates Ch. 5 to List (2005) on the discursive dilemma. Its programme continues in the later papers named in lit_status_note. It drew published critiques: Pruss, "Infinitesimals are too small for countably infinite fair lotteries" (Synthese, DOI 10.1007/s11229-013-0307-z); and "Indeterminacy of fair infinite lotteries" (Synthese, DOI 10.1007/s11229-013-0364-3; author unverified). None of these is held in the record. Within the record, the Ch. 5 agent model sits beside [LIT-070](../literature.d/LIT-070.md) (opinion dynamics with scrambled connectivity), which is a continuous-opinion, not a theory-valued, model. Pettigrew's [LIT-171](../literature.d/LIT-171.md) (accuracy-first credence) and [LIT-181](../literature.d/LIT-181.md) (value of knowledge) are neighbours on credence and belief, but they are not engaged; the thesis predates both.

**Epistemology tag.** The work is about rational credence and outright belief. It defends an epistemic (intersubjective) reading of probability and relies on the Principal Principle as a minimal rationality norm. Its position is that outright belief is "almost certainty" relative to a context level: a contextual, threshold-free Lockean thesis with a weakened conjunction principle. It extends this to social epistemology through averaging agents. Knowledge is explicitly set aside. The tag is justified, and it should be primary (see corrections).

## Bearing on the record

This is philosophy of probability and formal epistemology. It carries nothing for ML practice. A reader might hope infinitesimal probabilities bear on zero-probability events in continuous models, but the thesis gives no computational method, and its standard part is ordinary asymptotic density. So nothing goes to the Anthology of the SOTA. No THEORY document is affected. The seeded LIT's summary is accurate for Chs. 2–3 but should add the Ch. 5 finding with its limits (see corrections).

## Limitations

- The Ch. 2 solution is non-unique, one per free ultrafilter, and non-constructive (it needs AC). It gives up label invariance, and its "infinite additivity" is over *ℕ, not ℕ. The author concedes that her probability is empirically indistinguishable from the finitely additive real solution, so the case for preferring it is intuitive.
- The Ch. 3 Stratified Belief depends on relative analysis, whose levels have no explicit boundary by design. Any explicit threshold "collapses" it back to the standard threshold model (§3.5.5, §3.7.2.1). It is therefore not operational, and the author calls it "a crude model" (§3.6.4). Its handling of knowledge and of the bank case is a sketch.
- Ch. 5 has only one update step, uniform random initial theories, M ≤ 3, and no truth or evidence. The odd–even wobble is unexplained. The headline "arbitrarily small" generalisation over M outruns two data points. The Delphi-study recommendations are derived from this model without validation.
- NAP is a preview. Consistency, the uncountable case, and regularity for coin tosses are all deferred.

## Open questions

- Is there a principled constraint that selects an ultrafilter or narrows the family, for example requiring α to be divisible by every n? The author declines to endorse one (§2.6.2).
- Do infinitesimal probabilities survive the later arguments that they are "too small" for countable fair lotteries, and the indeterminacy objections?
- Does F_AG actually decrease for M ≥ 4, and what explains the odd–even oscillation? Exact or large-sample results at M = 4 would settle the first. The later journal version (EPJ B 2012) is where to check whether this was extended (unverified).
- Can Stratified Belief be extended to knowledge, and to more than one context level per agent?

## Corrections to the seeded skim

- Ch. 5: the skim says the probability of ending inconsistent "is under 2% and falls with more atomic sentences or a larger community". Three corrections:
  - The < 2 % bound holds for the agent-based fraction F_AG only. It is established numerically, not proved, and only for M = 2 (max 1.8112 % at D = 4, N = 5) and M = 3 (max 0.3215 %), after a single update, in an impartial culture (Table 5.3).
  - The population-level probability that at least one agent becomes inconsistent (F_OP) reaches 6.43 % at M = 2 and 16.867 % at M = 3 (D = 6, N = 1780). It therefore *rises* from M = 2 to M = 3.
  - "Arbitrarily small by increasing M" is extrapolated from two values of M. Appendix B says the data are "insufficient to predict the shape of D-curves for higher values of M".
- Ch. 5, recommendation (ii), "avoid even-numbered groups" (§5.5): this conflicts with the chapter's own finding that odd N gives the *higher* agent-based fraction (§5.4.1). The even-favouring wobble is in F_OP. The skim does not mention the recommendation. The wobble itself is left unexplained.
- Ultrafilter dependence (a skim open question): the thesis handles it directly in §2.6.2. The solution is "a whole family of solutions", one per free ultrafilter. For example, P_num(Odd) = ½ + 1/(2α) or exactly ½, depending on whether Odd is in the ultrafilter. The author sees "no convincing reasons" to impose further constraints. The non-uniqueness is acknowledged, not resolved.
- Additivity: the skim's "infinitely additive" needs a qualifier. The thesis proves additivity only as a hypercountable sum over *ℕ of the *star-extended* family ⟪*A_N⟫, including non-standard-indexed members (eq. 2.27). It then notes that this collapses to a hyperfinite sum ("HFA"). Countable additivity provably fails for any non-standard-valued function, because ω-sums are undefined on *ℕ (§2.5.2.2). The skim's "not a general endorsement of Regularity" is correct (§2.2.1.2, §2.7).
- The NAP axioms (§6.2.3) are stated, but their consistency proof ("giving a model") is "not presented here". The regularity result for infinite coin tosses, pace Williamson (2007), is promised for a paper in preparation, not shown.
- Ch. 3 treats rational belief only. The knowledge version of the Lottery Paradox is explicitly set aside (fn. 1, fn. 22), so Stratified Belief is not a theory of knowledge.
- Minor internal inconsistency: §1.4.1.3 calls the part–whole principle "Hume's principle" and one-to-one correspondence "Euclid's principle". Table 1.1 uses the standard, opposite labels. Table 5.4's F_OP-odd D = 4 row duplicates the F_AG-odd D = 4 row.
- primary topic: epistemology. Chs. 3–5 and the §1.3 interpretation of probability are about rational belief, credence and social epistemology. The foundations of probability part (Ch. 2, NAP) is philosophy of mathematics by the thesis's own description ("an interesting topic in the philosophy of mathematics", p. 13), and `philosophy-of-mathematics` should be added. `probabilistic-modeling` (blurbed as Bayesian inference and statistical models) fits poorly: the thesis builds no statistical model, and the author says she is "not convinced by the Bayesian discourse" (§1.3.2).
