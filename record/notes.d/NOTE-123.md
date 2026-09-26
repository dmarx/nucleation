---
number: 123
status: Read
formerly:
- NOTE-tmpf3r2h
paper: LIT-131
title: 'Freeborn — A Model of Understanding in Deep Learning'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv 2604.04171v1 (5 Apr 2026, cs.AI), 60
    pp.: abstract, §§1–8 (pp. 1–49), all 55 footnotes, figure captions for
    Figs 1–6, and a scan of the reference list (pp. 49–60) to check
    citations. There are no appendices. Figures were read through their
    captions and the surrounding prose; the plots in Figs 4–5 were not
    inspected as images. The companion Jupyter notebooks (GitHub) were not
    run or read. The PhilSci-Archive 28921 copy was not compared.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  Freeborn defines "systematic understanding" as four conditions: an
  internal model, non-memorizing tracking of a property, bridge principles
  fixed in the deployed pipeline, and derivation by the agent itself. Four
  small demonstrations (the genus of a torus, Mars's eccentricity e≈0.096
  with Kepler's form built in, grokked modular addition mod 113, and
  Othello-GPT from Li et al.) show it can be met. The Fractured
  Understanding Hypothesis (§7.5), which the paper argues for but does not
  test, says the understanding deep networks reach is characteristically
  symbolically misaligned, non-reductive, locally fractured,
  proxy-dependent and representationally fragmented.
---

# NOTE-123: Freeborn — A Model of Understanding in Deep Learning

## Contribution

The paper offers a regimented, deliberately non-anthropocentric explication of one kind of understanding ("systematic understanding"), meant to apply to humans, collectives and machine-learning pipelines alike (§4.2). It then argues, through four small worked examples with released code (§6), that deep networks can meet it. Finally it proposes the Fractured Understanding Hypothesis (§7.5) to explain the "jagged frontier": the understanding such systems reach is real but characteristically falls short of the "Ideal of Scientific Understanding" (symbolic, reductive, unifying; §4.7). It recasts the memorization/generalization and interpolation/extrapolation debates as "proxy battles" over understanding (§3).

## Key insight

Understanding is a relation between an agent pipeline and a property of a target. It needs a compressive internal model that stays predictive under perturbations that should not matter, coupled to the target by interfaces that are part of the deployed system rather than supplied by an observer. Under that criterion "curve fitter" and "understander" are not exclusive. A ReLU spline can understand a property, but it tends to do so in a patchwork: many locally reliable pieces, in coordinates that are not the target's natural variables, with little pressure from the loss to unify them.

## Assumptions

- **Explication, not analysis** (p. 3 fn 2; p. 12 fn 10). The account does not claim to capture the ordinary concept or a natural kind, and does not claim sufficiency for causal-mechanistic scientific understanding.
- **Real patterns via compression** (Dennett 1991; §4.1). A pattern is real iff a finite algorithmic description compresses the data better than enumeration and predicts materially above chance. MDL: a hypothesis H compresses iff L(H)+L(D|H) < L(D) (Eq. 6). Compression is necessary but not sufficient (p. 14).
- **Modest naturalism about aboutness** (pp. 17–18). Intentionality can be realized physically; informational, teleofunctional or real-patterns accounts all suffice. No linguistic meaning or consciousness is required.
- **Structuralist modelling choice** (p. 15). Agents and targets are treated as structured systems ⟨X,R⟩. This is explicitly not an ontological commitment.
- **Bridge principles belong to the agent** only if fixed at deployment, executed automatically, part of closed-loop competence, and functionally integrated (p. 19).
- **Setting of the formal treatment**: feed-forward ReLU networks as continuous piecewise-affine maps (Eqs. 2–4), with structural understanding as the operative species (§5). The general claims are said to "apply more broadly" (fn 3), but that is asserted, not shown. LLMs are explicitly deferred (pp. 3–4, §8).

## Key results

- **Definition (§4.2, p. 15).** S systematically understands property p of target T "insofar as": (1) S contains a subsystem M that is an adequate model of some aspect of T; (2) M tracks p without memorizing it; (3) bridge principles connect M's terms to T's; (4) S can use M to (approximately) derive properties of p.
- **Non-memorization operationalized (p. 19, Eq. 7).** A necessary condition is stability p̂(S,ω) ≈ p̂(S,π(ω)) for all ω in the intended domain and all π in a family Π of structure-preserving perturbations. This is supplemented by a compression proxy: effective description length does not scale linearly with the number of training examples (p. 20). Degree of understanding grows with both compression and the breadth of Π.
- **Species.** Structural understanding (§4.3: a structure-preserving map, typically a homomorphism; worked example of Ba-137m decay, Eqs. 8–11). Reductive understanding (§4.4: Nagel–Schaffner derivability, with the order relative to structural understanding left open). Causal understanding (§4.5: P(p|do(X=x)), not developed). Tacit vs symbolic (§4.6).
- **Pipeline schema (Eqs. 13, 15).** Ω_T →ι→ X →r_θ→ Z →g_θ→ Y →δ→ Ŷ. The model M is ⟨X_M,R_M⟩ on the occupied latent set, a polytope partition (Eq. 16). The universal approximation theorem (Cybenko 1989) is invoked to show that spline form does not preclude understanding (p. 27).
- **Torus (§6.1).** A 3→64→64→1 ReLU MLP (4,481 parameters) was trained with MSE on 262,144 grid samples of F=(R−√(x²+y²))²+z²−r², R=2.0, r=0.7, using Adam at 1e-3 for 5,000 epochs. The extracted zero-isosurface is a single closed surface with χ=0, hence genus 1 (fn 36). The claim is structural understanding of a global property from local supervision.
- **Mars (§6.2).** Data: 12 of Brahe's oppositions plus 10 triangulation constraints (fn 38). A "Baseline" net regressing angles on time captures synodic periodicity and retrograde loops but gives no orbital elements. A "Keplerian" variant, with conic sections, heliocentrism and the area law built in, fits e_M≈0.096 and P_M≈687.05 d (modern ≈0.093, ≈687 d). The author concedes the credit may belong to the hand-built scaffold (pp. 33–34).
- **Modular addition (§6.3).** m=113, trained on 60% of pairs, with a 2-layer, 4-head transformer (d=128) and weight decay. It shows grokking, including "slingshot" spikes near steps 22k and 42k (Fig. 4). After grokking, the 2D DFT of the logits concentrates on few frequencies (Fig. 5). This is called "an especially clear-cut case" of structural understanding.
- **Othello (§6.4).** This example reports Li et al. 2023's own results rather than new ones: nonlinear probes reach ≈2% per-square error at mid layers, probes on a random network fail, and interventions shift legal-move predictions even for unreachable boards. Nanda (2023) is cited for mine/theirs linear probes. The conclusion is that the system has systematic understanding of the board state (p. 41).
- **FUH (§7.5, pp. 45–46).** Five features: symbolic misalignment, non-reducibility, local fracturing, proxy-dependent fragmentation, and representational fragmentation. Each is traced to a cause: loss-driven coordinates, patchwork as a stable resting point, piecewise structure, rewards for any predictive dependence, and no pressure to factorize. §7.4 explains prevalence: patchwork solutions are available, discoverable by local gradient descent, and stable once the loss is low.
- **Lessons (§8).** Bridge principles and interfaces "are not neutral conveniences", so work on measurement, featurization, tokenization and decoding matters, "not merely … scaling parameters" (p. 48). The paper recommends neuro-symbolic hybrids, symbolic regression, causal representation learning, equivariant or Hamiltonian architectures, and mechanistic interpretability as "an epistemic tool" (p. 49).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Systematic understanding = adequate internal model + non-memorizing tracking + agent-internal bridge principles + agent-internal derivation | n/a (definition) | stipulative explication, §4.2, motivated by the Kepler→Newton→Gauss case (§4) and the ability-based literature |
| C2 | Memorization is the zero-compression limit, and non-memorization requires stability under a perturbation family Π | moderate | MDL formalism (Eqs. 5–6) and Eq. 7; the choice of Π is left interest-relative (fn 19) |
| C3 | Piecewise-affine (spline) form does not preclude understanding | moderate | informal argument plus universal approximation (p. 27) and the change-of-variables point (p. 28) |
| C4 | A small ReLU MLP trained on local scalar values structurally understands the torus's genus | weak–moderate | single run, χ=0 check (fn 36); the derivation step (marching cubes) is placed both inside and outside the agent (fn 32 vs fn 33) |
| C5 | With Kepler's hypothesis space built in, the learned model tracks Mars's eccentricity (e≈0.096) | weak as evidence about deep learning | one experiment; the author concedes the credit may go to the scaffold and that it is "debatable" whether this is deep learning at all (p. 34) |
| C6 | Grokked modular addition is a clear-cut case of structural understanding | moderate | own replication (Fig. 4) plus Fourier concentration (Fig. 5), leaning on Nanda et al. 2023 |
| C7 | Othello-GPT systematically understands the board state | moderate as a report of Li et al.; weak as an application of the criteria | secondary evidence; the p. 41 argument uses probe mappings as bridge principles, which fn 50 and p. 19 exclude |
| C8 | Without weight decay the modular-addition model "remains in the memorization regime indefinitely" (fn 47) | weak (assertion with citation) | attributed to Power et al. 2022; [ANTH-LIT-538](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-538.md)'s reading reports weight decay as the strongest intervention, "more than halving" the data needed, which is a matter of degree, not "indefinitely" |
| C9 | Deep-learning understanding is characteristically fractured in five named ways (FUH) | weak (hypothesis) | informal argument from the structural causes of §7.4 and cited literature (Geirhos et al. 2020; Nikankin et al. 2025; Kumar et al. 2025); no test of prevalence is offered |
| C10 | Fractured understanding may be one cause of the "jagged frontier" | weak | assertion (p. 46) |
| C11 | Much human understanding is itself tacit, non-reductive and piecemeal, so fractured understanding is still understanding | weak | informal argument by analogy (ball-catching, bees, chess; §§4.6–4.7, 7.5) |

## Method

This is conceptual explication followed by case studies. A definition is stated (§4.2), two species are specified formally (structural, reductive), and the definition is applied to four toy or near-toy systems, three of them trained by the author with released notebooks (§6.1–6.3) and one reported from Li et al. 2023b (§6.4). The FUH is then abduced from the examples and the ML literature (§7).

## Concepts

- **systematic understanding**: the four-criterion relation of §4.2. It is graded by the degree of compression and the breadth of Π.
- **bridge principles**: "any stable mappings, conventions, or interface relations that connect elements of the model M to elements of the target system T" (p. 18). In ML this means preprocessing/encoding ι and decoding δ. They count as part of the agent only under conditions (i)–(iii) and functional integration (p. 19).
- **derivation**: a fixed, agent-available procedure mapping target situations to claims about p. Investigator-only analyses do not count (p. 19).
- **memorization**: the limiting case of zero genuine compression, where model complexity scales with the data, not with the regularities (p. 14).
- **real pattern**: Dennett's notion: compressible and predictive above chance (pp. 3, 13).
- **structural / reductive / causal understanding**: tracking by homomorphism, by Nagel–Schaffner reduction, or by interventional dependence, respectively (§§4.3–4.5).
- **Ideal of Scientific Understanding**: understanding that is symbolic, reductive and unifying at once (§4.7).
- **monstrous theory**: Votsis 2015: a conjunction whose parts are not confirmationally connected. Used here to characterize patchwork networks (§7.3).
- **Fractured Understanding Hypothesis (FUH)**: §7.5, as above.

## Connections

- The paper builds on ability-based and interventionist accounts of understanding (de Regt 2017; Grimm; Strevens; Woodward), on Pritchard's (2010) anti-luck requirement, on Kitcher-style unification and Votsis's confirmational unification, on Dennett's real patterns and on MDL. It positions itself against "stochastic parrot" skepticism (Bender et al.) and alongside Beckmann & Queloz (2025), Sullivan (2022) and Tamir & Shech (2023) on machine understanding (p. 44). It adjudicates Prasetya (2022) vs Erasmus & Brunet (2022) on unificationist explanation of networks (§7.3).
- **Epistemology.** The epistemic notion is *understanding*, treated as distinct from and graded beyond mere reliable prediction. Its position is externalist and ability-based: understanding needs no reflective access, linguistic articulation or psychological states. It excludes luck and rote memorization, and it can be tacit (Polanyi; Ryle's knowing-how, fn 24). It is explicitly anti-anthropocentric and it declines to engage testimonial accounts (fn 11, Hills 2016). The tag is justified: understanding and its relation to knowledge, luck and prediction is a core question in contemporary epistemology, and the paper takes a definite position on it. The paper's framing and sources are chiefly philosophy of science, though, so epistemology is secondary.
- Held works: [LIT-195](../literature.d/LIT-195.md) (world models and life–mind continuity) and [LIT-148](../literature.d/LIT-148.md) (computational functionalism for deep learning) are natural neighbours. Freeborn's two-step programme for LLMs (does the model understand language, and does linguistic understanding yield a world model? p. 48) offers a criterion either could be checked against. [LIT-207](../literature.d/LIT-207.md) (Talkative AI and the fiction of artificial minds) takes the opposing fictionalist line.

## Bearing on the record

- **Nucleation.** This is a usable, citable middle position between "parrot" and "understander" for any note on machine understanding or world models. Its most useful export is the pair of conditions p. 19 bridge principles and Eq. 7 stability, not the FUH.
- **ML practice (Anthology).** The paper touches practice at two points, neither of them a tested instruction. (a) Its grokking case replicates Power et al. and Nanda et al. and adds nothing new. Its fn 47 claim ("without [weight decay] the system remains in the memorization regime indefinitely") is stronger than what [ANTH-THEORY-069](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-069.md) and [ANTH-LIT-538](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-538.md) record: weight decay is one of several knobs and changes how much data grokking needs, not whether it can happen at all. (b) §8's "work on interfaces, not merely scaling" and "interpretability as an epistemic tool" are recommendations argued by analogy (the Keplerian example), not by experiment. Nothing here should source an ANTH-SOTA practice. Its FUH could at most be cited alongside [ANTH-THEORY-064](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-064.md) or shortcut-learning theories as a philosophical gloss.

## Limitations

- **The paper's own criteria are applied inconsistently.** For Othello, the bridge principles invoked (activation → decoded board) are post hoc probes, which fn 50 and p. 19 exclude from the agent. By the paper's own conditions, the case supports only that information about the board is present and causally used; whether the deployed system "understands the board state" would need the board variable to be connected to T by an agent-internal bridge. The paper does not address this. For the torus, marching cubes is placed both outside (fn 32) and inside (fn 33) the agent.
- The Keplerian result owes its eccentricity largely to a hand-built hypothesis space, a point the author concedes (pp. 33–34). As evidence about *deep learning* it is weak.
- The examples are toys, each a single run, with no ablations, seeds or error bars. Only modular addition shows a transition from memorization to generalization.
- The abstract's claim that DL systems "often can and do achieve such understanding" rests on these four examples plus cited literature. "Often" is not measured anywhere.
- The FUH is a hypothesis with a causal story (§7.4) but no test. Its five features are not operationalized beyond Eq. 7 and the compression proxy. The abstract's three-feature statement and the §7.5 five-feature list do not match.
- The perturbation family Π is interest-relative (fn 19), so degree-of-understanding verdicts inherit whatever choice of Π an evaluator makes.
- The paper excludes LLMs by design and leaves causal understanding undeveloped (§4.5).
- Scholarship slips: the Carlini et al. 2023 citation points to a diffusion-model paper for an LLM claim (p. 8). Dennett 1991 is duplicated as 1991a and 1991b. "Li et al. 2023a, Do large language models have a world model?" is cited without venue (unverified).

## Open questions

- Can the Othello verdict be restated without probe-based bridges? For example: is legality tracked by the deployed next-move distribution under Π-perturbations of transcripts that preserve the board? That test would settle whether C7 meets the paper's own criteria.
- How should Π be chosen non-arbitrarily? The author's answer ("specified by the bridge principles") risks letting the designer set the bar.
- Does the FUH predict anything measurable, such as the rate of local fracturing across ReLU region boundaries, or does it redescribe known distribution-shift failures? A result linking region-boundary crossings to competence changes on structure-preserving perturbations would test "local fracturing".
- Is reductive understanding strictly stronger than structural understanding? The paper leaves this open (p. 22).
- Can the two-step LLM programme (§8) be carried out: does language understanding yield extra-linguistic world understanding?

## Corrections to the seeded skim

- The skim's open question, whether bridge principles are "specified independently of the interpreter", is answered in the text (pp. 18–19). A pipeline component counts as a bridge principle only if it is (i) fixed at deployment, (ii) executed automatically and (iii) part of the system's closed-loop competence, plus "functional integration". Post hoc interpretability probes are explicitly excluded (p. 19; fn 50). What stays observer-relative is the perturbation family Π: what counts as "structure-preserving" is "necessarily interest-relative" (fn 19).
- New finding: the paper does not keep to its own exclusion. For Othello (p. 41) the "third" criterion cites bridge principles that "connect internal activations to decoded board variables". Those are the post hoc probes that fn 50 says are "not part of the agent system". For the torus, fn 32 calls marching cubes "a tool used by the human investigator, rather than as part of the agent system", while fn 33 and p. 29 put the same marching-cubes-plus-Euler-characteristic step inside S as its derivation procedure.
- The skim puts the Kuhn/Lakatos analogy for grokking and double descent in §8. It is in footnote 55, attached to the last paragraph of §7.5 (p. 47). §8 only restates the FUH and draws engineering lessons.
- The skim says the FUH lists five features. It does, but the abstract and the §7 opening name only three: symbolic misalignment, non-reductive, weakly unifying. The five-item list in §7.5 swaps "weakly unifying" for local fracturing, proxy-dependent fragmentation and representational fragmentation. "Weak unification" is the §7.3 heading and survives only through Votsis's "monstrous" theories.
- The skim does not mention §4.5 (causal understanding, set aside) or the claim that the Keplerian model is not clearly a deep-learning system. The author concedes this is "debatable" (p. 34): the curve form, heliocentrism and the area law are all built in.
- Citation mismatch (p. 8): the text cites Carlini et al. (2023) for "attacks that extract verbatim training snippets from LLMs", but the reference list gives Carlini et al. 2023 as "Extracting training data from diffusion models". Dennett 1991a and 1991b are the same entry, duplicated.
- primary topic: philosophy-of-science is right and should stay first. epistemology is justified as a secondary tag (see Bearing).
