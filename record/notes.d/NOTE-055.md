---
number: 55
status: Read
formerly:
- NOTE-tmpgpet2
paper: LIT-046
title: 'Pilgrim et al. 2025, foundations of collective intelligence'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2509.07999v1, 20 pp. (title page dated
    11 Sep 2025; submitted 6 Sep 2025), extracted to rawC4/2509.07999.txt. I
    read all of it: abstract, significance statement, §1 Introduction, §2
    Collective Resources (2.1–2.4, Table 1), §3 Constraints (3.1
    Coordination, 3.2 Cooperation), §4 Collective Representations and
    Algorithms (4.1–4.5, Table 2), §5 Case Studies (5.1–5.3), §6 Discussion,
    and the 148-item reference list. Figs. 1–5 are known only from their
    captions and the text describing them; the images themselves were not
    viewed. There is no appendix or SI. v1 is the only version.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  A conceptual framework, with no model, data or derivation. It sets out
  individual and collective computational resources in four dimensions:
  sensing ΣI_i, states S_c × ∏S_i, processes F_c + ΣF_i, and actions ∏A_i
  (Table 1). It then maps the collective's surplus onto familiar
  mechanisms (aggregation with noise σ_i²/n, distributional beliefs P(H),
  memory persistence T_c, division of labour). Coordination and
  cooperation are given as the constraints that make the trade-off, and
  three animal case studies are retold in these terms.
---

<!-- inactive-ok-file: LIT-046 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-055: Pilgrim et al. 2025, foundations of collective intelligence

## Contribution

- A four-dimension resource inventory (sensory information, states, processes, actions) for individuals and collectives, written as set-level expressions (Table 1):
  - I_i vs ΣI_i
  - S_i vs S_c × ∏S_i
  - F_i vs F_c + ΣF_i
  - A_i vs ∏A_i
- A catalogue of constraints (§3). Coordination covers synchronisation, communication cost, individual–collective integration, and bandwidth. Cooperation covers diverging preferences, handled by compromise, leadership or fission; social dilemmas, handled by kin selection, reciprocity or interdependence; "participatory computation"; and incidental collective benefit from selfish behaviour.
- A mapping from surplus resources to algorithmic capacities (§4, Table 2, Fig. 4):
  - aggregation reduces noise from σ_i² to σ_i²/n under uncorrelated errors;
  - the combined states represent a distribution P(H) over beliefs;
  - collective memory persistence can be unbounded (T_c ≤ ∞) against T_i ≤ lifetime;
  - the joint action space supports utilities u(A_i, A_j).
- Three case studies, in golden shiners, ant nest choice and pigeon homing (§5), retold at Marr's computational, algorithmic and implementation levels.

## Key insight

Collective intelligence is resource rationality with a different budget and a different wiring diagram. A collective has more sensing, state, processing and action capacity. Because that capacity sits inside autonomous modules, it also faces coordination and cooperation costs. The same trade-off can therefore give quantitative gains (the same resource–quality curve, further along), qualitatively new algorithms (a different curve), or collective failure (Fig. 2).

## Assumptions

- Marr's three levels apply to collectives, and the analysis may run bottom-up (implementation → algorithm → computation). The authors note they still "very much support Marr's top-down approach" for specific behaviours (§6).
- Resources can be counted in the four dimensions. The collective totals are "not simple addition" (Table 1 caption), so no metric is specified.
- Environmental computation (for example pheromone trails) is set aside when resources are counted (§2).
- The σ²/n noise reduction assumes uncorrelated individual errors (Table 2 caption). Correlation is acknowledged in prose (§2.1, §4.1).

## Key results

This is not a results paper. The load-bearing statements are:

- **Table 1**: the state and action spaces of a collective grow exponentially with n, as Cartesian products (§2.2, §2.4).
- **Table 2**: with uncorrelated errors the aggregate's noise is σ_i²/n. A collective can represent P(H) where an individual holds one H_i. The collective's memory persistence T_c is unbounded while an individual's T_i is bounded by its lifetime.
- **§5.2 counterexample**: citing Sasaki et al. 2013, ant colonies beat individual ants on hard discriminations, but individuals beat colonies on easy ones, through early amplification of noisy assessments. The paper presents this as a coordination cost.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Wisdom of crowds, collective sensing, division of labour and cultural learning are "aspects of a single unifying principle" of resources and constraints | weak | informal argument (§1, §4, Fig. 4); a unifying vocabulary, not a derivation |
| C2 | Collective state and action spaces are the Cartesian products of the individual spaces, hence exponentially larger | moderate | definitional (Table 1, §2.2, §2.4); true as a count of configurations, silent on usable capacity |
| C3 | Aggregating opinions with uncorrelated errors reduces noise as σ²/n | strong (as a standard result) | central limit theorem, cited (Table 2) |
| C4 | Collectives can do disjunctive or counterfactual reasoning that no member can | weak | stated as speculation (§4.2), no example |
| C5 | Collectives switch between fast (Type 1) and deliberative (Type 2) modes depending on internal disagreement | weak | analogy plus citations (quorum responses, baboon movement; §4.3) |
| C6 | Golden shiner, ant nest-choice and pigeon cases are "qualitatively different" collective algorithms, not scaled-up individual ones | moderate | retellings of published empirical and model work (refs 13, 47–48, 104–105, 114, 116–117, 92, 100–101); no new analysis |
| C7 | The framework applies to human societies, neural circuits and AI integration | weak | assertion (§6) |

## Concepts

- **resources** — sensory information I, states S (memory and location), processes F, and actions A (§2).
- **S_c / F_c** — collective-level state (spatial or network structure) and inter-individual processes, beyond the members' own.
- **participatory computation** — a mechanism in which contributing and benefiting are the same act, so free-riding is impossible (for example flocking navigation; §3.2).
- **quantitative vs qualitative improvement** — the same resource–quality curve moved along, vs a different curve (Fig. 2).
- **individual–collective integration** — the coordination cost of decomposing a task and recombining the parts (§3.1).

## Connections

- The paper synthesizes:
  - resource rationality (Griffiths, Lieder & Goodman 2015);
  - Sumpter's interaction rules;
  - Galesic et al.'s "collective adaptation";
  - Couzin's collective cognition;
  - Steiner's (1972) group process losses;
  - the major-transitions literature (Szathmáry & Maynard Smith; West et al. 2015).
- In this record it sits alongside:
  - [LIT-075](../literature.d/LIT-075.md) (Dreyer et al.), a direct empirical instance of the "resources plus coordination cost" trade-off (ant groups gain, and human groups without speech lose), though [LIT-075](../literature.d/LIT-075.md) is not cited here;
  - the individuality and major-transitions cluster, which §4.5 and §6 touch.

## Bearing on the record

There is nothing for ML practice. The Discussion's line about designing systems "as we integrate artificial intelligence into society" is a remark, not an argument. The σ²/n aggregation result is standard ensembling and is not new here. For this record the paper is useful as vocabulary: a topic on collective intelligence could be organized along its resource/constraint axes. It does not support or contradict any THEORY document on its own evidence.

## Limitations

- There is no formal model, simulation or new data, and the unification is a mapping in prose.
- The resource dimensions are not given a metric. "Σ" and "×" are notational, so no quantitative comparison between collectives, or between an individual and its collective, can be computed from the framework.
- Constraints are listed, not modelled. The framework cannot say in advance when coordination costs outweigh resource gains, although Fig. 2's trade-off would require that.
- The case studies are retellings of the authors' and others' published work, chosen to fit.
- The "predictions" are research questions without stated observations that would refute them.

## Open questions

- Can the resource accounting be made quantitative, for example information-theoretic capacities for I, S and F, so that it predicts when a group beats its best member?
- Does any collective demonstrably perform disjunctive or counterfactual inference that its members cannot, and what experiment would show it?
- Is the "reverse Marr" conjecture (§6: perceived modularity of the world reflects the modularity of collectives) testable at all?

## Corrections to the seeded skim

- "Derived" and "predictions". The dossier's summary says the forms of collective intelligence "can all be derived from one principle", and the abstract says the framework "generates testable predictions". In the text:
  - The link from resources to mechanisms (§4) is argued in prose and via Table 2, with no formal derivation.
  - The one explicit prediction is flagged "Speculatively, we predict" (§4.2, disjunctive and counterfactual reasoning by distributed representations).
  - The Discussion's "concrete questions" (collective reasoning, biases, fast/slow switching, evolutionary pathways, reverse-Marr) are posed as questions, not predictions with a stated test.
  - The dossier's own question ("whether the predictions are sharp enough to be falsified") is therefore answered: they are not stated sharply enough to be.
- Formal or taxonomic? The dossier leaves this open. Tables 1–2 are the only notation, and Table 1's caption says its "+" and "Σ" "denote the total resources across the collective (not simple addition)". The operators are symbolic, so the framework is taxonomic.
- Connection to c31. The dossier says this paper cites ant cooperative transport "as a synchronisation example", linking it to c31 ([LIT-075](../literature.d/LIT-075.md)). The citation (§3.1, ref. 89) is McCreery et al. 2016, J. Exp. Biol., not Dreyer et al. The link to [LIT-075](../literature.d/LIT-075.md) is thematic only.
- Mechanisms list. The dossier lists "feedback and deliberation, collective memory, and division of labour". The paper's §4 has five subsections: 4.1 Information Aggregation (collective sensing, wisdom of crowds, spatial autocorrelation), 4.2 Distributions and Inference, 4.3 Feedback and Deliberation, 4.4 Collective Memory, and 4.5 Division of Labour and Specialisation. Cultural learning is folded into 4.4.
- Minor: references 22 and 23 are the same book (Bradbury & Vehrencamp). The title page is dated 11 Sep 2025, after the 6 Sep submission.
