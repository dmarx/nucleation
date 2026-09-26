---
number: 100
status: Read
formerly:
- NOTE-tmp4hykx
paper: LIT-157
title: 'Bourrat — Reproducees, reproducers, Darwinian individuals'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the typeset article, Synthese (2025) 205:62,
    26 pp. (pp. 1–22 body, pp. 22–25 references, p. 26 publisher's note).
    Downloaded 2026-09-26 from pierrickbourrat.com/publication/a-60/a-60.pdf
    to rawM/a60.pdf. I extracted it with PyMuPDF to rawM/a60.txt, because
    pdftotext is not installed. I checked Figs. 2 and 3 against rendered
    images of pp. 8 and 22 (rawM/a60_p8.png, a60_p22.png). Fig. 1, the
    decision tree on p. 4, I read from its caption and the text of pp. 4–7
    only. I read every section: the abstract, §§1–7, footnotes 1–11, the
    acknowledgements and the reference list. Nothing was skipped. The header
    gives received 25 Feb 2024 and accepted 13 Dec 2024. The online date (3
    Feb 2025) comes from the dossier's Crossref lookup and was not
    re-checked.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  Bourrat builds a nested vocabulary. A reproducee is a B that comes after
  A, is caused by A, and is of A's relevant class. A reproducer is a
  reproducee with reproductive autonomy, meaning it can reproduce across a
  range of backgrounds. A Darwinian individual is a reproducer with high
  reproductive causal control, meaning heredity survives as the parent's
  description is made finer. On that vocabulary, genes of multicellular
  organisms are, like hearts, mere reproducees, but with high control.
  Material overlap is necessary for reproducers, which are whole life
  cycles, and unnecessary for reproducees, so Griesemer and Godfrey-Smith
  partly talk past each other. Both quantities get an
  information-theoretic recipe (conditional MI after Bertschinger et al.
  2008 for autonomy; interventional MI across grains, Griffiths et al.'s
  INF, for control), and neither is computed.
---
<!-- inactive-ok-file: LIT-160 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-188 — Proposed: read in full and unproven; cited by a close reading as a related account, not as an established result -->
<!-- inactive-ok-file: LIT-049 — Proposed: read in full and unproven; cited by a close reading as a related account, not as an established result -->
<!-- inactive-ok-file: LIT-005 — Proposed: read in full and unproven; cited by a close reading as a related account, not as an established result -->

# NOTE-100: Bourrat — Reproducees, reproducers, Darwinian individuals

## Contribution

The paper sorts reproduction talk into three nested statuses, shown in Fig. 2 (p. 8): Darwinian individual ⊂ reproducer ⊂ reproducee. Two graded properties separate them: reproductive autonomy and reproductive causal control. The three statuses are then placed on a two-axis map (Fig. 3, p. 22), adapted from Godfrey-Smith's Darwinian space.

What is new:
- An explicit, minimal set of conditions for *being reproduced*, kept apart from *reproducing* (§2).
- A definition of *reproductive causal control* that is distinct from fidelity of transmission (§5).
- A case that genes of multicellular organisms are reproducees, not reproducers (§6).
- A scoping of the Griesemer/Godfrey-Smith material-overlap dispute that lets each be right about a different kind of object (§4).
- A recasting of ecological-scaffolding ETIs as reproducees acquiring autonomy (§6).

## Key insight

"X is reproduced" does not entail "X reproduces" (p. 3). The replicator concept is the standing example: a gene "is replicated but does not replicate" (p. 3). Once reproducing is made a graded capacity relative to a background (autonomy), the parts of a reproducer are all reproducees that serve it. Genes, hearts and life-cycle stages are all examples. What makes genes special is not that they reproduce. It is that their fine-grained variation is transmitted, which is high causal control.

The mereological upshot is that material overlap is a property of the wholes, not of their parts. A mother overlaps her daughter across a life cycle through hybrid objects, but her heart does not overlap her daughter's heart, and a parent virion does not overlap its offspring virion. That is why overlap can be necessary for reproducers and unnecessary for reproducees (pp. 11–13, 22).

## Assumptions

- **Objects are distinguishable from their environment** and extend in time as well as space (p. 4). How the object/environment boundary is drawn is itself a choice (pp. 10, 21).
- **"Minimal" conditions** are the most abstract, meaning any further loss of detail would make reproduction unassessable, and the most general, meaning they cover the largest number of cases. These senses follow Godfrey-Smith (2009) and Levy (2021) (p. 4).
- **Relevant class is chosen pragmatically.** A class is "a collection of entities that share a common property" (p. 6). The paper concedes there is "no mind-independent way" to fix it (p. 6). The partial fix is to use properties whose variation features in the biological explanation (pp. 6–7).
- **Autonomy is relative.** It only makes sense for comparisons under "similar" environmental backgrounds, and otherwise the autonomies are "incommensurable" (p. 8).
- **§5's population assumptions.** The objects are assumed to satisfy the reproducer conditions, to vary, to differ in reproductive output, and to transmit variation "more or less faithfully" (p. 14). The Lewontin-condition subtleties are set aside (pp. 13–14).
- **The human material-overlap example sets aside two things:** microchimerism (fn. 3, p. 11) and cell turnover (p. 11).
- **The CaCO₃ running example idealises** the three crystal forms as equally stable (p. 6), and treats secondary nucleation by breaking off as illustrative, not typical (fn. 1, p. 5).
- **Information-theoretic measurement assumes more than the text states.** It needs a fixed grain of description (p. 10) and the possibility of ideal interventions on parental phenotype at chosen grains (pp. 15–16). Neither the intervention distribution nor the environmental distribution is specified.

## Key results

The paper has no theorems, models or data. Its formal content is definitional.

- **Reproducee (§2, pp. 4–7; Fig. 1).** B is a reproducee of A iff:
  1. "B should come into existence after A." This rules out co-occurrence.
  2. "A should be a cause of the existence of B." This rules out mere recurrence and puts Veigl et al.'s causally unconnected reconstitution outside reproduction (p. 5).
  3. "A and B should be of the same (relevant) class of objects set by the description of A." This rules out mere production: life-cycle stages, secretions, a moult (p. 7).

  The conditions build on Sterelny et al. (1996) conditions (i)–(ii) and Godfrey-Smith (2009, p. 69).
- **Reproducer (§3, pp. 8–10).** A reproducee that can "paradigmatically *autonomously* produce a new object with the same capacity". Reproductive autonomy is "the capacity to reproduce within a range of (relevant) background conditions. The larger the range (both in terms of features and values for each feature), the more reproductively autonomous" (p. 8). All reproducers are reproducees, except perhaps the first (p. 8). "The existence of a reproducee necessarily implies the existence of a reproducer" (p. 9).
  - **Autonomy recipe 1 (p. 8).** Treat parent and offspring as sender and receiver, and ask "the extent to which conditioning on the environment decreases the mutual information between parent and offspring. The larger the decrease, the less reproductively autonomous." The source is Bertschinger et al. (2008). The paper links it to Woodward's causal stability (p. 9).
  - **Autonomy recipe 2 (p. 10).** Over candidate object/environment boundaries at a fixed grain, choose the boundary with maximal "mutual information between the parental and offspring object conditioned on the state of the environment at the parental generation". The prediction is that "the smallest objects for which there is maximal mutual information" are whole life cycles.
  - **Life cycles (p. 10).** With non-null development (Griesemer's term), every stage is "at best a mere reproducee", so whole life cycles are the reproducers.
  - **Ordering (p. 9).** DNA in a multicellular cell is highly non-autonomous. Viruses are "bona fide reproducers" because they "get into a cell in the first place". Bacteria are highly autonomous.
- **Material overlap (§4, pp. 10–13).**
  - *Formal appearance from partial description.* Take the human case: 30 trillion cells (Sender et al. 2016) and 3 billion base pairs. That gives "a single base that belongs to the mother in one of 10,000 cells of the daughter on average", so on this description reproduction looks formal (p. 11). The paper's answer is that the description is incomplete, and one "must track the flow of matter throughout the entire process" (p. 11).
  - *Hybrid objects.* Any continuous tracking of matter meets objects that hold both future-parental and future-offspring parts. These are Griesemer's (2014) "hybrid individuals", which the paper calls "hybrid objects" (p. 11). The inference is "If there always exist some objects during the life cycle of a reproducer that contain both (future) parental and offspring parts, by contraposition, formal reproduction never exists" (p. 12).
  - *Relabelling parts* ("half a parental cell and half an offspring cell") is rejected as against biological practice, ad hoc, regressive, and implying that all reproduction is formal (p. 12).
  - *Verdict.* Overlap is necessary for reproducers and not for reproducees. The virion→virion stage is the example: A causes B without overlap (pp. 12–13, 22).
- **Reproductive causal control and the Darwinian individual (§5, pp. 13–17).**
  - Godfrey-Smith's (2009) Darwinian individual is a member of a Darwinian population. The paper adds an individual-level feature, reproductive causal control. It has three formulations, which are not shown to be equivalent:
    - (a) "the extent to which small changes in the nature of an object lead to correspondingly small changes in their offspring" (p. 3);
    - (b) "the capacity to retain their property of being reproducers as we consider increasingly finer classes" (p. 15);
    - (c) "the extent to which fidelity of transmission is retained while the grain at which the parent is described becomes finer or the class to which the parent belongs becomes narrower because the number of properties considered for the object is greater" (p. 16).
  - Control combined with autonomy is what the paper "associate[s] with Darwinian individuality" (p. 15).
  - *Distinct from fidelity* (p. 16). The red reproducer has 100% colour fidelity and none for shade. The "azure" reproducer has 50% colour fidelity, but its blue offspring are always azure. So "the blue reproducer scores higher on Darwinian individuality … despite having a lower fidelity".
  - *Measurement* (pp. 16–17). Use causal MI under increasingly fine ideal interventions, which is Griffiths et al.'s (2015) INF. "The finer the grain at which causal mutual information is the highest between parent and offspring, the higher the degree of reproductive causal control."
  - CaCO₃ crystals have low control, with few features transmitted at coarse grain. This fits Maynard Smith and Szathmáry's "limited" vs "unlimited heredity" (pp. 15–16).
- **Genes (§6, pp. 17–20).**
  - Genes and hearts are both mere reproducees on autonomy. They differ in control: an A→C switch in a gene is transmitted, and heart changes are not (p. 19).
  - "Scaffolded reproducer" is an "antinomy" (p. 17).
  - Autonomy over timescales shorter than cell division, in a cellular background, is ranked: autonomous retrotransposon > non-autonomous retrotransposon > regular gene. So the autonomous retrotransposon is a reproducer and the gene a reproducee (p. 18). The paper assumes the two have "roughly the same" control.
  - There should be selection for separating the mechanisms of transmission from the phenotype, a "primordial form of modularity" (p. 19).
  - "Historical reproducers" is offered as a way to salvage genes' status (p. 20).
- **ETIs (§6, pp. 20–21).** Take Black et al.'s (2020) scaffolded patches. Collectives have "no (or very little) reproductive autonomy" but fine-grained control inherited from the cells. Endogenisation is gaining autonomy. Moving the scaffold (the patches) inside the object boundary does not help, because the patches "are not reproducees; they are recurring structures". Endogenisation needs either patch properties to become reproducees coupled to the cells, or the collective to reproduce independently of the patch (p. 21).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Being reproduced does not entail reproducing; the gene-as-replicator is the standing example of the non sequitur | informal argument | §2, p. 3; developed in §6 |
| C2 | B is a reproducee of A iff B is later than A, caused by A, and of A's relevant class | definition, with examples (CaCO₃ secondary nucleation, moult, secretion) | §2, pp. 4–7, Fig. 1 |
| C3 | Choosing the relevant class is pragmatic; ITSNTS's extension of units of selection to holobionts and biogeochemical cycles depends on a very abstract class choice | informal argument | pp. 6–7 |
| C4 | Reproductive autonomy is the range of relevant backgrounds (features × values) over which an object reproduces; it is graded and comparable only across similar backgrounds | definition | §3, p. 8 |
| C5 | Autonomy can be measured by conditional MI between parent and offspring given environment | **proposal; two recipes that differ, neither computed** | p. 8 ("decrease" on conditioning) vs p. 10 (maximal conditional MI). The first is I(P;O) − I(P;O\|E). The second is I(P;O\|E). They are different quantities, and the first can be negative: with O = P ⊕ E, P and E independent and uniform, I(P;O) = 0 and I(P;O\|E) = 1 bit (my example). Both measure parent–offspring *resemblance* given environment, not the *range of backgrounds* over which reproduction occurs, which is C4's definition. |
| C6 | Whole life cycles, not stages, are reproducers; the smallest boundary maximising conditional parent–offspring MI will pick out the life cycle | informal argument + untested prediction | p. 10 |
| C7 | Viruses are reproducers (though less than bacteria); genes in multicellular organisms are not (or only marginally) | informal argument | p. 9 |
| C8 | Material overlap is necessary for reproduction by reproducers | **informal argument resting on an asserted premise** | pp. 11–12. The premise that "any explanation that tracks continuously the flow of matter … will involve some hybrid objects" is asserted for reproduction in general. It is shown only for retroviruses, by citing Griesemer 2014. The Conclusion's "necessarily" (p. 22) is stronger than this support. |
| C9 | Reproducees can be reproduced without material overlap, so Godfrey-Smith is right about them; the dispute is partly the two talking past each other | informal argument + example (virion → virion) | pp. 12–13 |
| C10 | In humans, on average one maternal base per 10,000 daughter cells | back-of-envelope arithmetic; the ratio is correct (3×10¹³ / 3×10⁹ = 10⁴), but the spatial reading is not | p. 11. The ratio is right. "One base … in one of 10,000 cells" assumes uniform spreading. Under semi-conservative replication, parental strands persist largely intact in a few cell lineages (my observation, not checked against the paper's sources). The count also ignores egg cytoplasm and mitochondria. The qualitative point, that almost none of the daughter is maternal matter, survives. |
| C11 | Reproductive causal control is distinct from fidelity of transmission, and can rank a lower-fidelity reproducer above a higher-fidelity one | toy example (red vs azure) | §5, p. 16 |
| C12 | Higher reproductive causal control means more cumulative evolution, hence more Darwinian individuality | informal argument (thought experiment on colour/shade and number of features) | §5, pp. 14–15; no model |
| C13 | Control can be measured as the finest grain at which interventional parent–offspring MI is highest (Griffiths et al.'s INF) | **proposal; not computed; no normalisation** | pp. 16–17. Raw MI is bounded by the entropy at each grain, which grows as the grain is refined. Without normalisation, "finest grain at which MI is highest" is biased toward fine grains. |
| C14 | "Scaffolded reproducer" is an antinomy: a scaffolded object is by definition non-autonomous relative to the background | argument from definition | p. 17 |
| C15 | Genes and hearts are both mere reproducees; they differ in control, not in reproducer status | informal argument + example (A→C switch vs heart change) | pp. 17–19 |
| C16 | Autonomous retrotransposons are reproducers and regular genes reproducees, relative to a cellular background on sub-cell-division timescales | informal argument; the boundary depends on the chosen background and timescale | p. 18. A degree property becomes a binary verdict ("some" vs none). |
| C17 | Selection should favour separating mechanisms of transmission from phenotype (primordial modularity); modern genes are evolved modules of reproducers | informal argument, speculative | p. 19, citing Wagner & Altenberg 1996 |
| C18 | Ecologically scaffolded collectives are reproducees with high control "for free"; endogenisation = evolving reproductive autonomy | recasting of Black et al. 2020 | pp. 20–21 |
| C19 | Folding the scaffold (patches) into the object does not yield a reproducer, because the patches are recurring, not reproduced | informal argument | p. 21 |
| C20 | Abstract: the framework "provides some fuel" for Griesemer's material-overlap view | matches the body | Abstract; §4. The abstract is modest. The Conclusion's "necessarily" (p. 22) is where the claim outruns the support (C8). |

## Concepts

- **Reproducee.** B is a reproducee of A if it satisfies the three conditions of C2. A *mere reproducee* also has little or no reproductive autonomy. Mere reproducees are "either part of a reproducer or composed of them" (p. 3).
- **Reproducer** (a term from Griesemer, used here "not necessarily … in the exact same sense"). A reproducee with reproductive autonomy. Paradigmatically it is a whole life cycle (p. 10).
- **Reproductive autonomy.** The capacity to reproduce within a range of relevant background conditions (features and their values). It is graded and relative (p. 8). Having internal reproductive machinery is one route to it. Another is being able to "find itself in an environment that contains this machinery", as viruses do (p. 9).
- **Reproductive causal control.** How well fidelity of transmission is retained as the parent's description becomes finer or its class narrower (more properties) (pp. 15–16). An early statement is "small changes … lead to correspondingly small changes in their offspring" (p. 3). The word "control" is non-agential (fn. 5). The definition is written for reproducers ("retain their property of being reproducers", p. 15), but §6 applies it to reproducees too.
- **Darwinian individual.** Godfrey-Smith's (2009) "member of a Darwinian population". The paper adds that paradigmatic Darwinian individuals are reproducers with a high degree of reproductive causal control, which is autonomy plus control (pp. 13, 15; Fig. 3 top right).
- **Fidelity of transmission.** How reliably a trait is passed on, relative to one grain (p. 16).
- **Material overlap.** The paper never defines it. It is used in Griesemer's sense. From the hybrid-object argument it can be reconstructed (my reconstruction) as: some material part of the parent becomes a material part of the offspring through the process. This is a *diachronic* overlap, carried by persisting matter, not the synchronic O of classical mereology.
- **Hybrid object** (Griesemer's "hybrid individual"). An object during reproduction that contains parts that will end up in the parent and parts that will end up in the offspring (p. 11).
- **Formal reproduction.** Reproduction with no material overlap between parent and offspring. Godfrey-Smith's example is retroviruses (p. 10).
- **Null / non-null development** (Griesemer). A reproducer is "ready made" at birth, or must be transformed before it can reproduce (p. 10).
- **Scaffolded reproducer** (Godfrey-Smith 2009). Rejected here as an antinomy (p. 17).
- **Historical reproducer.** A reproducee descended from former reproducers, such as genes if the RNA world is right. It is offered tentatively (p. 20).
- **Simple reproducer.** A reproducer that can transmit only a single property at one grain, by analogy with Maynard Smith and Szathmáry's "simple replicators" (fn. 4).
- **Production / recurrence / co-occurrence.** Three non-reproduction outcomes, ruled out by conditions 3, 2 and 1 respectively (Fig. 1).

## Connections

**Against Bourrat's other two held papers, [LIT-005](../literature.d/LIT-005.md) ([NOTE-027](NOTE-027.md)) and [LIT-049](../literature.d/LIT-049.md) ([NOTE-064](NOTE-064.md)).** This paper is the latest of the three. [LIT-049](../literature.d/LIT-049.md) was published in 2023. [LIT-005](../literature.d/LIT-005.md) was published in Feb 2024 and is cited here as "Bourrat 2024" (p. 21, among ecological-scaffolding works). [LIT-049](../literature.d/LIT-049.md) (Biol. Philos. 2023) is **not** in this paper's reference list, even though "grain of description" does much of the work in both. For each weakness the two NOTEs recorded:

- **Nothing computed (both NOTEs): inherited.** Autonomy (conditional MI) and control (interventional MI across grains) are both "could be" recipes (pp. 8, 10, 16–17). The p. 10 life-cycle prediction is untested. The cost is lower here than in [LIT-005](../literature.d/LIT-005.md) or [LIT-049](../literature.d/LIT-049.md), because this paper's main work is taxonomic and the recipes are secondary. The abstract claims no implementation, so the headline/body gap that [NOTE-027](NOTE-027.md) and [NOTE-064](NOTE-064.md) flagged is largely absent. The exception is the Conclusion's "necessarily" (C8, C20).
- **Observational vs interventional quantities ([LIT-005](../literature.d/LIT-005.md) C5): partly fixed, partly repeated.**
  - *Fixed:* the paper now keeps the two apart. Autonomy is explicitly an associational conditional MI ("a measure of association", p. 8). Control is explicitly interventional ("ideal interventions", pp. 15–16). So the two are no longer equated.
  - *Repeated:* it gives two different autonomy quantities as if they were one (C5). The difference form breaks on the same S′ = S ⊕ E example that [NOTE-027](NOTE-027.md) used against [LIT-005](../literature.d/LIT-005.md). More seriously, conditional MI measures resemblance given environment, which is heredity. The verbal definition of autonomy is about whether reproduction happens across backgrounds, which is closer to robustness of fitness. The proxy measures the wrong thing for the concept it is attached to.
- **Scale selection and degeneracy ([LIT-049](../literature.d/LIT-049.md) C4; [LIT-005](../literature.d/LIT-005.md) §7): acknowledged, handled by a tie-break, not solved.**
  - [LIT-049](../literature.d/LIT-049.md)'s δC criterion is minimised by the finest partition. [LIT-005](../literature.d/LIT-005.md) proposed "the coarsest grain of description in which Â is maximal".
  - Here the grain is fixed and the object/environment *boundary* varies (p. 10). The opposite degeneracy looms: an object that absorbs its whole environment has nothing left to condition on. The paper's rule is to take "the smallest objects" at maximal MI. That is an explicit selection rule, which [LIT-049](../literature.d/LIT-049.md) lacked, and so a partial repair.
  - It runs in the opposite direction from [LIT-005](../literature.d/LIT-005.md)'s "coarsest" wording. The two vary different things, so this is a tension rather than a contradiction, but it is not reconciled.
  - For control, "the finer the grain at which causal MI is highest" (p. 17) inherits the normalisation problem [LIT-005](../literature.d/LIT-005.md) raised for its C1 (Â/H(Ŝ)). Raw MI favours finer grains, and nothing here corrects for that.
- **Environmental confounding ([LIT-049](../literature.d/LIT-049.md) δC|E; [LIT-005](../literature.d/LIT-005.md) Â): unchanged.** Autonomy is again handled by conditioning on the environment at the parental generation (p. 10). That is the stratify-on-E move which [NOTE-064](NOTE-064.md) traced to [LIT-049](../literature.d/LIT-049.md) and which [LIT-005](../literature.d/LIT-005.md) tried to replace with intervention. No intervention distribution is specified for either measure, the same gap as [LIT-005](../literature.d/LIT-005.md)'s fn. 4.
- **Continuities that improve.**
  - §6's endogenisation, "to become less sensitive to environmental variations" (p. 21), is the verbal form of [LIT-005](../literature.d/LIT-005.md)'s criterion C2: low variance of Â under interventions on E. The present paper puts the ETI story in a clearer two-axis form: control arrives free from the cells, and autonomy must be gained.
  - [LIT-049](../literature.d/LIT-049.md) held that levels are levels of *description*. This paper keeps that stance: class choice is pragmatic with "no mind-independent way" to fix it (p. 6), and autonomy is background-relative (p. 8). It does not overclaim ontology, which fixes [LIT-049](../literature.d/LIT-049.md)'s abstract-vs-body tension ([NOTE-064](NOTE-064.md) C12).
- **My observation (not in the paper).** Formulation (c) of causal control, heredity that survives refinement of the parent's description, is [LIT-049](../literature.d/LIT-049.md)'s truthful/projected commuting condition read in the refining direction. Control is high when the parent→offspring map commutes with coarse-graining at many grains. Neither paper makes the link.

**Other held works.**
- **[LIT-168](../literature.d/LIT-168.md)** (SEP, Biological Individuals). As seeded, it summarises the field as treating "genes [as] Darwinian individuals without being agents". This paper denies that genes of multicellular organisms are reproducers, "let alone Darwinian individuals" (p. 21). The disagreement is direct. [LIT-168](../literature.d/LIT-168.md) is Deferred, so whether the SEP entry itself says this or only reports it is unverified.
- **[LIT-188](../literature.d/LIT-188.md)** (Griesemer & Shavit 2023). Cited here only in a list of ecological-scaffolding work (p. 21). The reproducer concept, hybrid objects and non-null development all come from Griesemer. [LIT-188](../literature.d/LIT-188.md)'s seeded summary says reproducing systems "hybridize with environmental components through eco-devo scaffolding". That is the route this paper's p. 21 allows for endogenisation: patch properties becoming reproducees coupled with the cells.
- **[LIT-124](../literature.d/LIT-124.md)** (SEP, Mereology). The paper uses mereological notions without any formal apparatus:
  - reproducees as parts of reproducers or composed of them (p. 3);
  - genes as modules/parts (pp. 19, 22);
  - life-cycle stages as parts of the life-cycle reproducer (p. 10);
  - hybrid objects (pp. 11–12).

  Its "material overlap" is not the entry's synchronic overlap (sharing a part at a time). It is diachronic, carried by persisting matter, so it presupposes cross-time identity of material parts. The entry's apparatus does not supply that, and the paper does not address it (my reading). The relabelling move the paper rejects (p. 12) is a choice between counting one hybrid whole and two proper parts, which is where [LIT-124](../literature.d/LIT-124.md)'s questions about sums and composition would come in. The paper does not take them up.
- **[LIT-160](../literature.d/LIT-160.md)** (SEP, Units and Levels of Selection; Lloyd). It separates the replicator/reproducer question from others. This paper's C1 dissolves the gene-as-replicator by making "is replicated" and "replicates" distinct statuses. It is not cited.
- **[LIT-142](../literature.d/LIT-142.md)** (Meincke, pregnancy as process). The paper's mother/daughter overlap example, and its bracketed microchimerism (fn. 3), concern the same part–whole question about the pregnant organism. This link is mine and is not cited.
- **Named lineage:**
  - Griesemer 2000a–c, 2005, 2014, 2016, 2018 (reproducer, hybrids, development);
  - Godfrey-Smith 2009, 2015 (Darwinian populations, scaffolded reproducers, hearts);
  - Sterelny et al. 1996;
  - Maynard Smith & Szathmáry 1995 (unlimited heredity);
  - Bertschinger et al. 2008 (autonomy);
  - Griffiths et al. 2015 and Pocheville et al. 2017 (causal specificity);
  - Black et al. 2020 (ecological scaffolding);
  - Veigl et al. 2022 (reconstitutor);
  - Doolittle & Booth 2017 and Doolittle & Inkpen 2018 (ITSNTS).

## Bearing on the record

- **[LIT-157](../literature.d/LIT-157.md)'s seeded summary is accurate on the taxonomy and on material overlap.** It should add two things. First, genes differ from hearts by reproductive causal control. Second, the ETI result is that control comes free and autonomy must evolve (see corrections). The `mereology` tag is justified. The paper's central sorting is parts (reproducees) versus the wholes they belong to (reproducers). Its material-overlap verdict is a claim that overlap holds between wholes, not between their parts.
- **[LIT-168](../literature.d/LIT-168.md) and this paper disagree** on whether genes are Darwinian individuals. When [LIT-168](../literature.d/LIT-168.md) is read, the disagreement should be recorded in both places.
- **Across Bourrat's held papers,** the two formal weaknesses carry through all three: no computed measure, and conditioning on E in place of intervention with no stated distribution. This is the one of the three whose main contribution does not depend on its measures.
- **No bearing on the Anthology of the SOTA.** The paper carries no instruction for ML practice and supports or contradicts no THEORY document. There are loose analogies, but they are the reader's own: heritable variation at fine grain as a condition for cumulative search (evolutionary algorithms, representation granularity), and the reproducer/reproducee split applied to self-replicating code. The paper makes no ML connection. Nothing here warrants an ANTH- document.

## Limitations

- **No worked model or data.** Both measures are recipes (pp. 8, 10, 16–17), and the life-cycle prediction (p. 10) is untested.
- **The autonomy proxy does not match the autonomy definition (C5).** The definition is a range of backgrounds; the proxy is conditional MI of parent–offspring states. The two recipes also disagree with each other.
- **Causal control has three unreconciled formulations** (p. 3 smoothness; p. 15 retention of reproducer status; p. 16 retention of fidelity). It is defined for reproducers but applied to reproducees (genes, scaffolded collectives), and Fig. 2's nesting shows it only inside reproducers while Fig. 3 treats it as an independent axis.
- **The material-overlap argument rests on an unproven general premise** (C8). Every continuous tracking of reproduction is said to meet hybrid objects, but this is shown only for retroviruses via Griesemer. "Material overlap" is never defined. Nor does the paper derive the overlap requirement from reproductive autonomy. The link is only that reproducers are whole life cycles, at which scale hybrids appear.
- **Relativity does the deciding.** Whether something is a reproducer depends on the chosen background and timescale. The gene/retrotransposon verdict (C16) holds for a cellular background on sub-cell-division timescales. The paper admits the relativity (p. 18) but still states categorical conclusions (p. 21).
- **The relevant-class problem is acknowledged, not solved** (pp. 6–7).
- **The human-DNA arithmetic** gives a correct ratio but a physically wrong spatial picture (C10). This does not affect the point.
- **Slips:**
  - "valerite" for vaterite (p. 15);
  - "CaCo3" (p. 19);
  - "retotransposons" and "endonucleanase" (p. 18);
  - "Maynard-Smith" (fn. 7);
  - in-text citations "Bourrat 2019a, b, 2021a, b, 2021c" have no letter suffixes in the reference list;
  - p. 5 "Griesemer (2000b)" and similar are unresolvable because the three Griesemer 2000 entries carry no letters.

## Open questions

- Can the two measures be computed on one explicit model, for example Black et al.'s scaffolding simulation? Would they place scaffolded collectives top-left and endogenised ones top-right, as §6 says?
- What quantity measures autonomy as *range of backgrounds*? For example, the measure of the set of E-values in which expected offspring number is ≥ 1, as against conditional MI. Does it rank retrotransposons, genes and viruses as p. 18 does?
- Which normalisation, and which intervention distribution, makes "the finest grain at which causal MI is highest" non-trivial? Does the red/azure ranking survive it?
- Is the hybrid-object premise true generally? Is there a clear case of a reproducer, a whole life cycle, whose continuous material tracking finds no hybrid stage? Candidates would be cultural or artificial reproducers.
- How does diachronic material overlap relate to the synchronic overlap of classical mereology ([LIT-124](../literature.d/LIT-124.md))? Does the overlap requirement need a theory of persisting matter, or of temporal parts?

## Corrections to the seeded skim

- **The dossier has the ETI result backwards.** It says "control can evolve through ecological scaffolding in transitions in individuality". The paper says the reverse. Scaffolded collectives already have high reproductive causal control "'for free' … as a byproduct of properties of lower-level Darwinian individuals (the cells)" (p. 21). What has to evolve, in the endogenisation step, is reproductive *autonomy*: "Endogenization involves the capacity to gain some reproductive autonomy: that is, to become less sensitive to environmental variations" (p. 21). Recast in the framework, scaffolded collectives are "reproducees with a high degree of reproductive causal control without being reproducers" (p. 21).
- **Material overlap: the Griesemer verdict is only half the conclusion.** The dossier says §4 "sides with Griesemer for reproducers". That is right but incomplete. The paper also grants Godfrey-Smith that the three reproducee conditions "can be satisfied without any material overlap", so his claim is "true" for reproducees (p. 12). If only Griesemer is talking about reproducers, the two are "talking past each other" (p. 12).
- **Genes are not simply "like hearts".** The skim summary puts genes and hearts in one class. The paper puts both there only on the autonomy axis. What separates them is reproductive causal control: a nucleotide switch in a gene reappears in offspring genes, but changes to a heart do not (p. 19). The paper also floats "historical reproducers" as a way to keep genes' past status (p. 20), and it recasts modern genes as "evolved modules of a reproducer with the function to transmit information" (p. 19).
- **The dossier omits §3's two main moves.** First, whole life cycles, not stages, are the reproducers. With non-null development, any single stage is "at best a mere reproducee" because the other stages would have to count as environment (p. 10). Second, §3 gives a measurement procedure: choose the object/environment boundary that maximises parent–offspring MI conditioned on the parental environment, and predict that the *smallest* such object is the whole life cycle (p. 10).
- **The dossier's open question (how is control measured?) has a textual answer.** The paper proposes Griffiths et al.'s (2015) INF, a fine-grained causal specificity. It is mutual information between parent and offspring phenotype under ideal interventions at successively finer grains, with control higher "the finer the grain at which causal mutual information is the highest" (pp. 16–17). It is never computed, and the paper gives no normalisation across grains.
- **Page ranges.** §2 runs pp. 3–7, not pp. 3–8; §3 starts on p. 8. §5 is pp. 13–17 and §6 is pp. 17–21. §7 is pp. 21–22, and Fig. 3 is on p. 22.
- **Fig. 3's axes and placements.** The x-axis is reproductive autonomy and the y-axis reproductive causal control. The figure places:
  - genes top left;
  - non-autonomous retrotransposons and then autonomous retrotransposons with retroviruses along the top, moving right;
  - bacteria and multicellular organisms top right, as "paradigmatic Darwinian individuals";
  - CaCO₃ crystals lower right;
  - "early replicative/reproductive structures" in the middle;
  - hearts, enzymes and other somatic structures bottom left.
- **The source of "reproducee" is more tangled than the dossier says.** The dossier notes the term comes from Godfrey-Smith (2009, p. 88). The paper also says there that it is "a near synonym of 'scaffolded reproducer'" (p. 2). It later rejects "scaffolded reproducer" as an "antinomy" (p. 17), so the borrowed term is kept while its synonym is thrown out.
