---
number: 91
status: Read
formerly:
- NOTE-tmp16i6y
paper: LIT-147
title: 'Pernu — Mental causation via neuroprosthetics?'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (Full text, Synthese 195(12):5159–5174 (16 pp., CC BY),
    read in full: abstract; §1–6; Figs 1–2 captions; footnote 1;
    acknowledgements; the reference list. Source: the Springer PDF
    (link.springer.com/content/pdf/10.1007/s11229-018-1713-z.pdf), fetched
    with a curl user agent into scratchpad/rawA/pernu.pdf and extracted with
    PyMuPDF into rawA/pernu.txt. The figures are diagrams; I read them from
    their captions and the §4–5 text, which describes them fully.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  The interventionist/difference-making case for nonreductive mental
  causation from BCIs (List & Menzies 2009; Menzies 2015; Woodward
  2008a,b, 2017) misplaces multiple realisation. What the ensemble
  recordings show is that one cortical-level variable N (the ensemble's
  average firing) is realised by many single-neuron patterns N1, N2. Each
  intention M corresponds to one value of N. So the counterfactual
  contrast "∼M □→ ∼B true, ∼N □→ ∼B false" fails, and neuroprosthetics
  supports mental causation only by identifying M with N, not nonreductive
  physicalism.
---
<!-- inactive-ok-file: LIT-164 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-144 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->

# NOTE-091: Pernu — Mental causation via neuroprosthetics?

## Contribution

The paper pins down where the BCI-based argument for autonomous mental causation goes wrong. The argument needs the mental property M to be realisation-insensitive with respect to its neural realisers: there must be nearby worlds with M, and with the behaviour B, but without the actual realiser. What neuroprosthetics exhibits is only the realisation-insensitivity of a coarse-grained *neural* variable N over single-neuron microstates. Every nearby world without M also lacks N. The work therefore gives no support to nonreductive physicalism, and it illustrates identity-style (reductive) mental causation.

## Key insight

Neuroprosthetics works because each intention has a well-defined physical correlate that a device can connect to. That same fact means the redundancy the interventionists point to is micro-over-macro *within* the physical, like microstates under a thermodynamic macrostate. It is not physical-under-mental. Showing that coarse-grained causes beat fine-grained ones is not the same as showing that mental causes beat physical ones, because "physicalism is not microphysicalism" (p. 5171).

## Assumptions

- **Difference-making causation with proportionality.** C causes E in w iff (a) C □→ E and (b) ∼C □→ ∼E hold in w (p. 5161). Pernu calls (a) sufficiency and (b) necessity (p. 5162).
- **Kim's exclusion setup.** Physicalism: every M is realised by some N, and N is causally sufficient for B. Distinct M then overdetermines, and systematic overdetermination is unacceptable (§2).
- **What the opponents assume.** Nonreductive physicalism needs M to be both distinct from N and multiply realised. If it is not, the difference-making argument yields only the "compatibility result" (p. 5170).
- **An empirical premise, asserted.** The intention variable decoded in BCI work (Musallam et al. 2004) corresponds one-to-one to a cortical-level value N, the ensemble's average firing rate (pp. 5167–5168).
- **Similarity ordering.** The closest ∼M worlds are ones where N is also absent. Worlds with M realised by some other cortical state Z are "quite far away" (p. 5171).

## Key results

The paper is an argument, not a theorem. Its structure:

- **The opponents' counterfactual pairs** (p. 5162). (1a) N □→ B, (1b) ∼N □→ ∼B; (2a) M □→ B, (2b) ∼M □→ ∼B. Under multiple realisation, (1b) fails and (2b) holds, so M, not N, is the difference-maker.
- **The reconstruction** (§4, pp. 5164–5165, quoting Woodward 2008a, p. 239). Intention I1 is realised by N11, N12, N13 on different occasions. Citing N11 is "overly specific".
- **Diagnosis** (§4–5). N11, N12… are single-neuron realisers of one cortical value N, not of I1 directly (Fig. 2a). The situation the argument needs is Fig. 2b: M realised by distinct cortical states N and Z. That situation is not what neuroprosthetics presents.
- **Consequence 1.** Relative to the actual evidence, (1b) with N read as the cortical variable holds whenever (2b) does, so the contrast collapses (pp. 5170–5171).
- **Consequence 2.** The mental is "not an epiphenomenon", but only "because the mental has now been identified with the physical" (p. 5168).
- **Conclusion** (§6). There are two difference-making defences: the *substantial* one (distinctness plus multiple realisability) and the *deflationary* one (mental causes are physical causes). BCI research supports only the deflationary one.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The BCI argument locates multiple realisation at the wrong level: what is multiply realised is the cortical variable N, not the intention M | moderate | informal argument §4–5, Fig. 2; relies on the premise in C3 |
| C2 | Without M-level multiple realisation, the (1b)/(2b) contrast the difference-making argument needs does not hold | moderate–strong | conceptual argument pp. 5170–5171, given the difference-making semantics |
| C3 | Each intention corresponds to a precise physical quantity, the average ensemble firing rate | weak | assertion from the BCI research agenda and a Musallam et al. (2004) quote; no analysis of the decoding methods |
| C4 | Neuroprosthetics illustrates mind–brain identity and cannot ground nonreductive physicalism | moderate (conditional on C3) | §4–6 |
| C5 | Monkey-to-human transfer tells against Putnam/Fodor cross-species multiple realisability | weak | one-sentence assertion, p. 5170 |
| C6 | The argument does not touch interventionist anti-exclusion arguments without proportionality | explicit scope statement | fn 1 |
| C7 | Coarse-grained over fine-grained causal preference is unsurprising and compatible with physicalism ("physicalism is not microphysicalism") | informal argument with citations | p. 5171 (Hüttemann; Papineau 2013) |

## Method

Conceptual analysis. The paper reconstructs the published arguments, applies the multiple-realisation dilemma (kind splitting vs realiser unification), draws an analogy with statistical mechanics, and reads the neuroprosthetics literature (Helmholtz; Fetz; Georgopoulos population vectors; Musallam et al. 2004; Aflalo et al. 2015) as a review.

## Concepts

- **Difference-making (with proportionality)**: C causes E iff C □→ E and ∼C □→ ∼E. Pernu distinguishes it from bare interventionism.
- **Sufficiency / necessity criterion**: conditions (a) and (b) respectively.
- **Realisation insensitivity** (List & Menzies): nearby worlds keep M and B but lack the actual realiser.
- **Kind splitting**: the purported multiply realised kind splits into kinds aligned with realisers (e.g. memory).
- **Realiser unification / merging**: the realisers share a feature with which the kind is identified. This is the BCI case.
- **Macroneural variable N**: an ensemble-average quantity, realised by many single-neuron distributions.
- **Substantial vs deflationary mental causation**: distinct plus multiply realised, vs identical to physical causation.

## Connections

Pernu's own earlier work on exclusion is held as [LIT-144](../literature.d/LIT-144.md) ("Causal Exclusion and Downward Counterfactuals", Erkenntnis 81, 2016, Deferred). This paper cites it on p. 5162 for the semantics of the difference-making counterfactuals, and the two should be read together. [LIT-164](../literature.d/LIT-164.md) (Poltorak on the scope of physical causal closure, Deferred) addresses the closure premise that §2's exclusion argument relies on. [LIT-138](../literature.d/LIT-138.md) (Register, *The Depth of the Body*, Read) is the other BCI-anchored philosophy paper held. It is about the moral body-part status of BCIs, not about mental causation, so the link is the shared case, not a shared thesis.

**Agency.** The work presupposes a causal theory of action: intentions are candidate causes of bodily or prosthetic movement, and the question is whether they cause *qua* mental. Its own position is reductive. The agent's intentions are efficacious because they are identical to cortical ensemble states. It says nothing about goals or autonomy beyond this. **The `agency` tag is justified** but secondary. The paper is about whether intentions do causal work in action control ("Action control" is a keyword), which is squarely the metaphysics of agency. `philosophy-of-science` correctly stays first.

## Bearing on the record

It supports any THEORY note on levels of causal description or mental causation. It would cut against a note that cites BCIs as evidence for nonreductive physicalism; I know of no such note in the record. For ML practice it carries no instruction. By analogy, it cautions against inferring that a model has a distinct higher-level "intention" from the fact that many activation patterns decode to the same coarse variable. That caution would need its own source in the Anthology, and it does not belong there from this paper.

## Limitations

- The argument is confined to difference-making with proportionality (fn 1).
- The central empirical premise, that one intention equals one ensemble-average value, is asserted, not shown. Real BCI decoders (Musallam et al. used ensemble decoding of goal signals) are not simple averages, and the paper does not examine whether one intention maps to one cortical value across sessions, electrodes or subjects. *My assessment; not discussed in the paper.*
- The closeness ordering of worlds (p. 5171) is asserted.
- The cross-species remark (C5) is a single sentence.
- No reply from Woodward, List or Menzies is engaged, since they preceded this paper.

## Open questions

- Is there any neuroscientific case of Fig. 2b: one intention realised by distinct coarse-grained cortical states, e.g. after plasticity or in decoder re-mapping? Such a case would restore the substantial difference-making argument.
- Does the diagnosis survive for interventionism without proportionality (Shapiro & Sober)? Pernu sets that aside.
- Have Woodward, List or Menzies replied? Unverified.

## Corrections to the seeded skim

- **Scope.** The dossier omits it: footnote 1 (p. 5162) confines the argument to the *difference-making* account, which builds in Yablo-style proportionality. Pernu says interventionist replies to exclusion that do not use proportionality (Shapiro 2010; Shapiro & Sober 2007) "are not affected by the argumentation presented in here". The paper therefore does not refute the interventionist response in general. Pernu notes that difference-making and interventionism are "conflated regrettably often".
- **The cortical variable is specified.** The dossier's "cortical, physical variable" leaves it vague. Pernu identifies N concretely as "the average neural activity that the given neural ensemble gives rise to", "the average firing rates of neurons in the relevant ensembles" (pp. 5167–5168). He calls it a "macroneural" variable and models it on a statistical-mechanics macrostate over microstates (Reif 1965; Pathria 1972), a kind of "multiple realisation" he says is "consistent with reductive physicalism".
- **Fig. 1 is missing from the dossier.** Fig. 1 (p. 5166) sets the diagnosis in the anti-multiple-realisation literature (Bechtel & Mundale; Bickle; Polger & Shapiro; Shapiro 2000). Purported multiple realisation dissolves either by **kind splitting** (the example is memory) or by **realiser unification/merging**. The BCI case is classed as merging.
- **Woodward 2017 is a target, not a reply.** The dossier asks whether Woodward (2017) replied. Woodward (2017), "Intervening in the exclusion argument", is one of the targets cited on p. 5160 and p. 5164; no reply to Pernu is cited or known to me (unverified).
- **An additional argument, missed by the dossier and only asserted:** the transfer of monkey BCI results to humans "could therefore be seen to speak against" even Putnam/Fodor-style cross-species multiple realisability (p. 5170).
- **The "charitable reading" argument is missing from the dossier.** §5 (p. 5170) argues that if M is simply identical to N, then identity's symmetry makes the case equally "a clear case of physical causation". That defeats the contrastive point of the difference-making argument and lands in what List & Menzies call the unsatisfying "compatibility result".
