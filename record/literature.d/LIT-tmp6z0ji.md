---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpyiwng](../notes.d/NOTE-tmpyiwng.md)); worth reading as the formal statement of how reciprocity can start, spread and hold: tit-for-tat is robust in Axelrod''s tournaments, cannot be bettered by any mutant when the continuation probability w is high enough, and can enter an all-defect population through kinship or clustering. "Evolutionarily stable" is stronger than what is proved: the proof shows no strategy does better than TIT FOR TAT, and always-cooperate does as well, which Boyd & Lorberbaum (1987) later turned into a proof that no pure strategy is evolutionarily stable in the repeated game. It grounds the exchange domain of morality-as-cooperation; it is not about morality.'
title: 'The Evolution of Cooperation'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the JSTOR printout of Science 211(4489): 1390–1396
    posted on Robert Axelrod's University of Michigan page,
    www-personal.umich.edu/~axe/research/Axelrod%20and%20Hamilton%20EC%201981.pdf,
    11 pp. including the preceding article's endnotes and JSTOR's linked
    references; text extracted with PyMuPDF). I read the summary, every
    section (Strategies in the Prisoner's Dilemma, Robustness, Stability,
    Initial Viability, Applications, Conclusion) and notes 1–42. Two
    displayed inequalities lost their right-hand sides in extraction and
    are reconstructed from the stated payoff sums, which the note says.
    Citation checked against Crossref (27 March 1981). Not held in the
    Anthology of the SOTA (grep of its literature.d for the DOI, the title
    and "Axelrod": nothing), nor already in this record. Filed for the
    lineage of morality-as-cooperation (ADR-018).
tags:
- natural-sciences
- game-theory
- mathematics
- complex-systems
date: '2026-10-02'
published: '1981-03-27'
doi: '10.1126/science.7466396'
first_author: 'Axelrod'
keywords:
- 'cooperation'
- "Prisoner's Dilemma"
- 'tit for tat'
- 'evolutionarily stable strategy'
- 'reciprocity'
- 'kin selection'
- 'clustering'
implementations: []
summary: >-
  Axelrod & Hamilton (1981), DOI-10.1126/science.7466396. In an iterated
  Prisoner's Dilemma with probability w of meeting again, TIT FOR TAT won
  two computer tournaments (14 and 62 entries) and an ecological
  simulation, and no strategy can do better against it when
  w ≥ max((T−R)/(T−P), (T−R)/(R−S)). ALL D is always stable; reciprocity
  can still enter through kinship or a cluster, after which a nice stable
  strategy resists clusters. Applications range from cleaner fish to
  disease and nondisjunction.
---

<!-- inactive-ok-file: LIT-tmpcsgn6 — Proposed: Curry 2016, the statement of morality-as-cooperation filed in the same batch; cited for which sources it credits for each domain -->

# LIT-tmp6z0ji: The Evolution of Cooperation

Robert Axelrod and William D. Hamilton (1981), *Science 211(4489): 1390–1396, 27 March 1981* — DOI-10.1126/science.7466396

## Key takeaways

- With a probability w that two individuals meet again, cooperation based on reciprocity can be robust (TIT FOR TAT won both of Axelrod's tournaments and took over an ecological simulation), stable (no mutant does better against an established TIT FOR TAT if w is large enough) and initially viable (via kinship or clustering), although always-defect is stable for every w.
- "The gear wheels of social evolution have a ratchet": a nice strategy that is stable cannot be invaded even by a cluster, whereas a cluster of TIT FOR TAT can invade always-defect.
- Effective retaliation needs individual recognition, or a substitute (permanent pairing, a fixed meeting place, territoriality), and a high enough w; falling w (illness, ageing) should make partners defect.

## Standing in the record

Filed on 2026-10-02 at the owner's request, as one of the evolutionary
sources of morality-as-cooperation. [NOTE-034](../notes.d/NOTE-034.md)'s lineage paragraph does not
name it: it names Trivers for reciprocity, and Curry 2016 ([LIT-tmpcsgn6](LIT-tmpcsgn6.md))
cites Axelrod's 1984 book, not this paper, beside Trivers. It is filed
because it is the formal core of both.

[NOTE-tmpyiwng](../notes.d/NOTE-tmpyiwng.md) is the close reading of 2026-10-02, and it placed the work:
**Active**. It turns Trivers's verbal model ([LIT-tmppstp9](LIT-tmppstp9.md)) into an ESS
analysis and adds the question of how reciprocity gets started, answering
it with Hamilton's kinship ([LIT-tmp17vtr](LIT-tmp17vtr.md)) and with clustering. For
morality-as-cooperation it grounds the exchange domain, and it shows why
that domain needs retaliation as well as giving. TIT FOR TAT's three
properties (never first to defect, provocable, forgiving after one
retaliation) are behaviours, not moral judgements; the paper does not
discuss morality.

Two cautions for anyone citing it for stability. The proof shows that no
strategy does *better* than TIT FOR TAT against TIT FOR TAT; always
cooperate does exactly as well, so TIT FOR TAT is not an ESS in Maynard
Smith and Price's strict sense ([LIT-tmpex4cg](LIT-tmpex4cg.md), p. 17). Boyd & Lorberbaum,
Nature 327:58–59 (1987), DOI-10.1038/327058a0, showed that no pure
strategy is evolutionarily stable in the repeated Prisoner's Dilemma;
not read here. And Nowak ([LIT-tmpbmh7b](LIT-tmpbmh7b.md)) reports that with errors TIT FOR
TAT's performance declines and generous variants and win-stay, lose-shift
replace it.

The applications include speculative ones the authors label as such:
chronic and acute phases of infection, cancer onset, and Down's syndrome
as defection between homologous chromosomes in oogenesis ("pure
speculation").

Its continuation probability w is the "shadow of the future" that
Fitouchi, André & Baumard's moral disciplining ([LIT-101](LIT-101.md)) needs: their
reading ([NOTE-132](../notes.d/NOTE-132.md), assumption A1) cites Axelrod for the claim that
reciprocal cooperation requires delayed gratification.

**Topic.** `natural-sciences` first: it is evolutionary biology, applied
from bacteria to primates. `mathematics` for the game theory.
`complex-systems` for its account of how cooperation arises in a
population of strategies (the tournament's ecology, clustering, the
ratchet). Not `probabilistic-modeling` (its blurb is Bayesian and
statistical models) and not `moral-psychology`.

**Anthology.** No instruction for machine-learning practice. Iterated
Prisoner's Dilemma tournaments are used in multi-agent learning research,
but the anthology's literature.d holds no such link (grepped for
"Prisoner's Dilemma" and "tit for tat"), so it is not flagged.
