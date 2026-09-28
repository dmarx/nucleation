---
status: Read
paper: LIT-tmp93aoy
title: 'The Impossibility of a Paretian Liberal'
version: 1
history:
- version: 1
  date: '2026-09-28'
  note: >-
    Read in full (Full text of the version of record, from Harvard's DASH
    repository (hdl 1/3612779, "Other Posted Material (LAA)"): a DASH cover
    sheet plus six scanned pages, JPE pp. 152–157, with no text layer. I
    rendered the pages to images (PyMuPDF) and read them visually: §I
    Introduction, §II The Theorem (Definitions 1–3, Conditions U, P, L, L*,
    Theorems I and II, and the proof), §III An Example, §IV Relevance, all
    six footnotes and the three references. Nothing was skipped. I checked
    the proof and the example by hand, and also the unproved strengthening
    in fn. 3. Crossref (queried without any contact address) confirms doi
    10.1086/259614: J. Political Economy 78(1), 152–157, issue dated January
    1970. The day is not known, so `published:` is the first of the month.).
    The first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-28'
summary: >-
  Sen proves that no social decision function can satisfy three conditions
  at once: unrestricted domain (U), the weak Pareto principle (P), and
  "minimal liberalism" (L*). A social decision function only has to yield
  a best element in every subset, and need not be transitive or satisfy
  independence. L* says at least two individuals are each decisive, both
  ways, over at least one pair of alternatives. I checked the two-case
  proof and it is correct: it builds a strict social cycle over 3 or 4
  alternatives. The Lady Chatterley's Lover example is a correct
  3-alternative instance. Sen's moral is that "in a very basic sense
  liberal values conflict with the Pareto principle" (p. 157).
---

# NOTE-tmp009zd: The Impossibility of a Paretian Liberal

## Contribution

Before this paper, the standard escape routes from Arrow's theorem were to drop transitivity (keeping only a choice function) or to drop the independence of irrelevant alternatives. Sen shows a new impossibility that survives both relaxations. A very weak form of individual liberty cannot coexist with the weak Pareto principle over an unrestricted domain. So respecting even minimal personal liberty can require overriding unanimous preference, and the Pareto principle, which economists treat as uncontroversial, can have "deeply illiberal" consequences (p. 157).

## Key insight

Pareto and liberty both look innocuous because each is stated one pair at a time. But decisiveness assigned to different people over different pairs, combined with unanimity over a third pair, can close a strict cycle. When people have preferences about each other's private matters ("nosey" preferences, p. 152), unanimity is a unanimity of meddling. Respecting it undoes the liberty assignments.

## Assumptions

- **Setting (p. 152).** X is the set of all social states; each state is "a complete description of society including every individual's position in it". There are n individuals with orderings R_i on X. R is the social preference relation.
- **Definition 1.** A *collective choice rule* is a functional relationship that gives exactly one social preference relation R for each n-tuple of individual orderings.
- **Definition 2.** A *social welfare function* (Arrow) is a collective choice rule whose range is restricted to orderings.
- **Definition 3.** A *social decision function* is a collective choice rule whose range is restricted to relations that generate a choice function. That is, in every subset of alternatives there must be at least one alternative "at least as good as all the other alternatives in that subset" (pp. 152–153). No transitivity of strict preference or of indifference is required (p. 156). Sen notes that Sen (1969) had shown Arrow's conditions to be "perfectly consistent" for social decision functions (p. 153).
- **Condition U (Unrestricted Domain).** Every logically possible set of individual orderings is in the domain (p. 153).
- **Condition P (weak Pareto).** If every individual prefers x to y, then society must prefer x to y (p. 153).
- **Condition L (Liberalism).** For each individual i there is at least one pair (x, y) such that i's strict preference between them, in either direction, determines society's strict preference (p. 153).
- **Condition L\* (Minimal Liberalism).** There are at least two individuals, each decisive in this two-way sense over at least one pair (p. 154).
- **Not assumed.** Transitivity (only a best element is required), independence of irrelevant alternatives, nondictatorship (L* rules out a single dictator implicitly), and any restriction of the decisive pairs to a "personal" sphere.

## Key results

- **Theorem I (p. 153).** No social decision function satisfies U, P and L. This tacitly needs n ≥ 2; see corrections.
- **Theorem II (p. 154).** No social decision function satisfies U, P and L\*. It "is stronger than Theorem I and subsumes it".
- **Proof of Theorem II (p. 154), which I checked.** Let individuals 1 and 2 be decisive over (x, y) and (z, w) respectively.
  - *Same pair.* If the pairs are the same, take 1 preferring x to y and 2 preferring y to x. U admits this profile, and L\* then demands both xPy and yPx, which is a contradiction.
  - *One shared alternative, say x = z.* Take 1: x ≻ y ≻ w; 2: y ≻ w ≻ x; everyone else with y ≻ w. U admits this profile. L\* gives xPy (from 1) and wPx (from 2, over the pair (x, w)). Pareto gives yPw. So xPyPwPx, a strict 3-cycle on {x, y, w}. Every element is strictly beaten, so no best element exists. The other ways of sharing an alternative (x = w, y = z, y = w) follow by relabelling, because decisiveness in L\* is two-way.
  - *All four distinct.* Take 1: w ≻ x ≻ y; 2: y ≻ z ≻ w; everyone with w ≻ x and y ≻ z. These are consistent orderings. L\* gives xPy and zPw. Pareto gives wPx and yPz. So xPyPzPwPx, a strict 4-cycle, and the subset {x, y, z, w} has no best element.
  - The proof is correct and complete. It uses only a handful of profiles, so it needs far less than full U. It uses only pairwise conditions on R, which is why independence is never needed.
- **Footnote 3 strengthening (p. 154), unproved in the paper.** L\* can be weakened to *one-way* decisiveness: 1 decisive for x against y only, 2 for z against w only, with x ≠ z and y ≠ w. Sen says the impossibility still holds. I checked the cases.
  - *All four distinct:* the 4-cycle above uses exactly these directions.
  - *y = z:* 1: w ≻ x ≻ y; 2: y ≻ w ≻ x; all w ≻ x. This gives xPy, yPw and wPx, a cycle.
  - *x = w:* 1: x ≻ y ≻ z; 2: y ≻ z ≻ x; all y ≻ z. This gives xPy, zPx and yPz, a cycle.
  - *y = z and x = w together:* the rights are x over y and y over x, which contradict on a single profile.
  - The claim holds.
- **Lady Chatterley example (§III, p. 155).** There is one copy of the book and three alternatives: x = 1 reads it, y = 2 reads it, z = no one reads it.
  - *Preferences.* Person 1, "a prude", ranks z ≻ x ≻ y. Person 2 ranks x ≻ y ≻ z, delighting in the thought that the prude may have to read Lawrence.
  - *Liberal values.* They give 1 the say over (x, z), so zPx, and 2 the say over (y, z), so yPz.
  - *Pareto.* Both prefer x to y, so xPy.
  - *Result.* The cycle is x ≻ y ≻ z ≻ x, and every option is "bettered by some other solution". I checked this, and it is correct. This is the shared-alternative case, with z shared.
- **§IV Relevance (pp. 155–157).**
  - *When the conflict arises.* It arises only for some preference configurations. "The ultimate guarantee for individual liberty may rest not on rules for social choice but on developing individual values that respect each other's personal choices" (pp. 155–156).
  - *Transitivity is not the escape.* The theorem does not need transitivity. Fn. 4: dropping binariness (a choice function without an underlying relation) does not escape either, if P and L are suitably redefined. The choice set can then be empty "even without bringing in acyclicity". Details are deferred to Sen's forthcoming book, ch. 6.
  - *IIA is not the escape.* The theorem does not use IIA, so relaxing it, "an appealing way of escaping the Arrow dilemma", "is not open here".
  - *Pareto is used weakly.* P is used in its weak, strict-unanimity form.
  - *Moral.* "If someone takes the Pareto principle seriously, as economists seem to do, then he has to face problems of consistency in cherishing liberal values, even very mild ones" (p. 157). Fn. 6: the issue is the *acceptability* of Pareto optimality given certain externalities, not the difficulty of *achieving* it.
- **Fn. 5, a report of other work.** Gibbard's then-unpublished oligarchy theorem: a quasi-transitive social decision function satisfying U, P, non-dictatorship and IIA must be an oligarchy. Sen notes his own theorem does not impose IIA.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | No social decision function satisfies U, P and L\* (Theorem II) | strong | Complete proof, p. 154; checked in this reading |
| C2 | No social decision function satisfies U, P and L (Theorem I) | strong for n ≥ 2 | Follows from C1 when n ≥ 2; false for n = 1, a case the statement does not exclude |
| C3 | The impossibility persists with one-way decisiveness (x ≠ z, y ≠ w) | strong (my check); asserted in the paper | fn. 3 says "can be shown" without proof; the case check is above |
| C4 | Neither dropping transitivity nor dropping IIA escapes the result | strong | The proof uses neither: only best-element existence and pairwise conditions |
| C5 | Dropping binariness (choice functions not based on a relation) does not escape it either | informal argument | fn. 4 sketches redefinitions and defers to the forthcoming book (ch. 6) |
| C6 | Condition L captures a value "involving individual liberty that many people would subscribe to" | informal argument | Motivated by the pink walls and sleeping-position examples, pp. 152–153, fns. 1–2. The formal condition does not restrict decisive pairs to personal matters |
| C7 | Liberal values conflict with the Pareto principle "in a very basic sense"; Pareto can be "deeply illiberal" | informal argument, resting on C1 | p. 157 |
| C8 | The ultimate guarantee of liberty may lie in mutually respectful individual values, not in choice rules | assertion | pp. 155–156 |

## Method

A direct constructive proof. For any assignment of two individuals' decisive pairs, it exhibits a preference profile, admissible by U, on which the liberty conditions and Pareto together produce a strict cycle. No best element then exists in the cycled subset, contradicting the choice-function requirement. There are two cases: one shared alternative gives a 3-cycle, and four distinct alternatives give a 4-cycle.

## Concepts

- **Collective choice rule / social welfare function / social decision function.** Definitions 1–3. The last requires only a best element in every subset.
- **Decisive (over a pair).** An individual whose strict preference over that pair, either way, fixes society's strict preference.
- **Liberalism (Condition L) / Minimal Liberalism (L\*).** Every individual, or at least two individuals, decisive over at least one pair. Sen flags that "liberalism" is "elusive" and says he does not argue about the word (fn. 1).
- **Paretian liberal.** A social decision rule meeting both P and L. The theorem shows it cannot exist on an unrestricted domain.
- **Nosey preferences.** Preferences over others' personal choices (p. 152). This term is the paper's wording in the introduction, not a defined condition.

## Connections

- **Within this batch.**
  - *"Equality of What?" (1979)* cites this result (as Sen 1970, ch. 6) for the claim that libertarian non-utility information "may require even the rejection of the so-called Pareto principle based on utility dominance" (p. 212). That is the bridge from this theorem to Sen's anti-welfarism.
  - *The Nobel lecture (1998, §XI)* restates the result and adds three later judgements. The 1970 formulation concerned the "opportunity aspect" of liberty. Recasting liberty as process does not by itself dissolve the conflict (fn. 46). The lecture credits Sugden and Gaertner et al. with rejecting the opportunity-only formulation. Calling their proposals "game-form" rights is my gloss, not the lecture's. And unlike Arrow's theorem, this one is not resolved by interpersonal comparisons, only by information about people's own priorities between liberty and desire-fulfilment.
- **Sen 1969 on quasi-transitivity.** This paper relies on it for the consistency of Arrow's conditions under social decision functions (p. 153). Morganti's "From OSR to metaphysical coherentism" ([LIT-173](../literature.d/LIT-173.md); [NOTE-095](NOTE-095.md)) uses the same Sen 1969 quasi-transitivity notion in a quite different setting, keeping irreflexivity of symmetric dependence. That is a shared formal tool, not a substantive link.
- **General equilibrium ([LIT-067](../literature.d/LIT-067.md)).** Debreu's 1952 existence theorem is the record's only other formal-economics result. It is unrelated in content.
- **Anthology of the SOTA.** Nothing bears on it.

## Bearing on the record

- **No THEORY in the record bears on this.** The theorem is a clean, fully proved formal result. It could support a THEORY that "welfarist unanimity principles conflict with rights assignments", but the record has none on social choice.
- **No ML-practice content.** There is a structural echo in preference aggregation for alignment, where unanimity plus individual vetoes can cycle, but the paper does not discuss it and it should not be carried to the Anthology.
- **For filing.** File under `society-and-governance` first (liberty, collective decision). `mathematics` is justified, because the paper is a theorem with a proof and a reader browsing formal results should find it. `ethics` fits because of the liberty-versus-Pareto conflict. `logic` is not proposed: the result is combinatorial, not about logic.

## Limitations

- **Pairwise decisiveness may not model liberty.** The model of liberty is decisiveness over pairs of complete social states. Whether that captures rights is the main point the later literature (Nozick 1974, Gärdenfors 1981, Sugden 1985, Gaertner et al. 1992, all cited in the 1998 lecture) disputes. The paper argues for its formalisation only by examples.
- **n ≥ 2 is unstated.** Theorem I omits the condition that there be at least two individuals.
- **The binariness extension is only sketched.** The extension to choice functions without an underlying relation (fn. 4) is deferred to another work.
- **U is much stronger than needed.** The proof needs only a few profiles, and the paper does not ask which domain restrictions would escape the result. It only says the conflict arises "with only particular configurations" (p. 155).
- **The positive suggestion is not developed.** The idea that liberty rests on individuals' mutually respectful values (pp. 155–156) is stated and left there.

## Open questions

- **Rights or Pareto?** Which should give way, and on what grounds? The paper states the dilemma. Sen's later answer (1998) is informational: use people's own priorities between liberty and desire-fulfilment. That answer is programmatic.
- **Is there a better model of rights?** Does a game-form or process model of rights avoid the paradox, or just relocate it? The 1998 lecture says a process-only approach does not resolve it, but gives no formal result there.
- **Which domain restrictions are enough?** What is the weakest domain restriction, for example requiring that individuals not have nosey preferences, under which U, P and L\* become consistent?

## Corrections to the seeded skim

- none (there was no seed or dossier)
- **Theorem I tacitly needs n ≥ 2.** As stated ("for each individual i"), Theorem I is false for a one-person society. There, making the single individual decisive over every pair satisfies U, P and L together. Theorem II builds the requirement in, since L* names two individuals, and Sen says Theorem II subsumes Theorem I. That holds only for n ≥ 2.
- The scoping report calls the DASH file "7 pp.: DASH cover plus 6 scanned pages". That is correct. The example's title is printed "Lady Chatterly's Lover" (p. 155), not "Chatterley's".
- **Condition L's formal content is wider than its motivation.** The introduction and fn. 2 motivate L by personal choices ("his own walls pink rather than white, other things remaining the same"). But Condition L and L* as defined put no such restriction on the decisive pair. In the example, person 1 is made decisive over "1 reads it" versus "no one reads it", and person 2 over "2 reads it" versus "no one reads it". The theorem is therefore about pairwise decisiveness, and whether that models liberty is a separate question. Sen's own Nobel lecture (1998, §XI) later says the 1970 formulation captured only the "opportunity aspect" of liberty.
