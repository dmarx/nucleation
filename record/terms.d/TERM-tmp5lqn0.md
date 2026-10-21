---
status: Active
complements:
- TERM-055
- TERM-034
title: 'legibility, of a distinction to an observer for a task: whether the observer, with the rules, categories and resources it actually has, can recover the distinction from what it is given and bring it to bear on the task; a relation among a representation, an observer''s rule class, its resources and a task, bounded above by what the source makes possible for an ideal receiver, and directed, since what is legible to a governing institution and what of its governing is legible to others are different relations'
version: 3
history:
- version: 2
  date: '2026-10-21'
  note: >-
    The readings of 2026-10-21 added. The usable-information literature is
    now held (Xu et al., THEORY-tmpgz4cf, THEORY-tmp9m1g4); Scott is held
    and Unavailable; Hayek, Espeland and Sauder, Kleinberg and Raghavan,
    Perdomo et al., James et al., McCombs and Shaw, Barnehl and Schumacher
    and Hyzen et al. are cited where they bear on the regime, the
    direction, the stages, the cost to the observed and the line from
    salience. The definition is unchanged.
- version: 3
  date: '2026-10-21'
  note: >-
    The regime is no longer identified with Π_{o,B}: it also governs what
    is observed and recorded and the categories that organize it (owner's
    second review of 2026-10-21). Adopted: status Proposed → Active.
tags:
- epistemology
- information-theory
- society-and-governance
date: '2026-10-21'
line: distributed-agency
summary: >-
  The owner's, U22 of the exchange of 2026-10-20: "a theme we seem to be
  touching on that I'm not sure is laid out clearly in our current account
  is the role of legibility". A22 defined it and proposed three TERMs; one
  is filed, with the regime and the direction in its body. Its formal core
  is [CLAIM-199](../claims.d/CLAIM-199.md)'s usable information. [CLAIM-081](../claims.d/CLAIM-081.md) holds the record's earlier
  use. Adopted by the owner on 2026-10-21. It recurs through A23 to A27.
used_by:
- CLAIM-tmpjo2zr
- CLAIM-tmp4v4na
---
<!-- inactive-ok-file: THEORY-tmp9wdb3 THEORY-tmpr3dxe — Proposed; Hayek's argument and James et al.'s bidirectionality, cited as readings that bear on the term, nothing rests on them -->
<!-- inactive-ok-file: LIT-tmpb1r6m LIT-tmpmdlm4 — Unavailable; Scott and Lan, named as works the term's sources lean on that no lawful copy reached -->
<!-- inactive-ok-file: CLAIM-081 CLAIM-199 CLAIM-296 CLAIM-338 CLAIM-342 CLAIM-348 CLAIM-349 CLAIM-tmpjo2zr — Proposed; open claims that bear on or use the term, cited as open -->

# TERM-tmp5lqn0: legibility, of a distinction to an observer for a task: whether the observer, with the rules, categories and resources it actually has, can recover the distinction from what it is given and bring it to bear on the task; a relation among a representation, an observer's rule class, its resources and a task, bounded above by what the source makes possible for an ideal receiver, and directed, since what is legible to a governing institution and what of its governing is legible to others are different relations

## Definition

The owner, at U22, quoting A21 ("influencing not just which positions
citizens or officials adopt, but which questions are regarded as
important, which evidence is considered credible, which actors are
recognized as authoritative, and which alternatives appear politically
available"): "a theme we seem to be touching on that I'm not sure is laid
out clearly in our current account is the role of legibility". A22:
"**Legibility concerns which distinctions an observer or governing
organization can recognize, interpret, and bring to bear on its decisions
under the conditions in which it actually operates.**"

**The formal core is [CLAIM-199](../claims.d/CLAIM-199.md)'s.** "a given receiver's access is usable
information relative to the rules it can apply, which a garbling can raise
for that receiver but never above what the source makes possible." Its
example, which A22 §2 used: with X = (X₁, X₂) fair and independent and
Z = X₁ ⊕ X₂, a receiver that reads one coordinate gets Z with accuracy
1/2 from X and exactly from the rendering V = X₁ ⊕ X₂ (rechecked). A22:
"legibility need not be monotone in informational refinement for bounded
observers, although ideal information sufficiency remains monotone for a
fixed target." [CLAIM-199](../claims.d/CLAIM-199.md)'s ceiling is the bound in the title.

**One operationalization.** A22 §2 gave a task-relative score,

  L_{o,𝒬,B}(T) = −inf_{π∈Π_{o,B}} E[ℓ_𝒬(J, π(T(X)))],

for observer o, task family 𝒬, resources B and permitted procedures
Π_{o,B}. It is [CLAIM-199](../claims.d/CLAIM-199.md)'s "best risk over the rules in a class the
receiver can apply" with the sign turned, and A22 called it "one
**operationalization** of legibility, not an exhaustive philosophical
definition", with a caution that belongs to the term: "the loss function
and task family must be specified independently; otherwise whoever
controls the scoring criterion also controls what counts as legible."

**The usable-information literature,** read on 2026-10-21 (Xu et al.,
[LIT-tmp07k7g](../literature.d/LIT-tmp07k7g.md), [NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md)). Under log loss the score is their
V-information, with Π_{o,B} the predictive family V. That legibility is not
monotone in refinement is their failure of the data-processing inequality,
and the XOR example holds for their linear families as well as for the
one-coordinate receiver ([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)). The ceiling in the title holds
in risk as stated; written in V-information it needs the family's
input-free predictions to include the target's marginal, and without that
V-information can exceed Shannon information ([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)). For a
family of bounded complexity the score can be estimated from samples with
a stated error ([THEORY-tmp9m1g4](../theory.d/THEORY-tmp9m1g4.md)). Xu et al.'s §6.4 sharpens A22's caution:
what is not usable by one family can be usable by another, so the score is
relative to the family named ([NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md)).

**A cost stated in 1945.** Hayek ([LIT-tmpwcrya](../literature.d/LIT-tmpwcrya.md), [NOTE-tmp53juk](../notes.d/NOTE-tmp53juk.md)): statistics
are made "by lumping together, as resources of one kind, items which differ
as regards location, quality, and other particulars, in a way which may be
very significant for the specific decision", so a central planner reading
them cannot take those circumstances into account ([THEORY-tmp9wdb3](../theory.d/THEORY-tmp9wdb3.md), an
argument from examples, Proposed).

**The regime.** A22 §4's "legibility regime" ("Attention, categories,
representation, available evidence, interpretive resources") is the
maintained organization of observation channels, classifications,
attention and interpretive procedures through which distinctions become
accessible and usable to specified observers. It is wider than Π_{o,B}.
It governs what gets observed and recorded and which categories organize
it, which set the inputs T(X) an observer has, as well as which procedures
are available, which is Π_{o,B}, and which evidence reaches an evaluator.
[CASE-tmpc0mv0](../cases.d/CASE-tmpc0mv0.md) gives it a state of its own, with dynamics the two-variable
model lacks ([CLAIM-tmp4v4na](../claims.d/CLAIM-tmp4v4na.md)). It stays distinct from epistemic standing,
whether a recognized distinction receives credibility or authority. A22
proposed the regime as a TERM of its own; it is filed here, in the body.
(Wording of the owner's second review of 2026-10-21, which corrected an
earlier version that identified the regime with Π_{o,B}.)

Three readings of 2026-10-21 bear on it. Espeland and Sauder's
commensuration is such a regime, in their words "the relations of
relevancy and irrelevancy, visibility and invisibility, that are
conferred"; and "Because numbers decontextualize so thoroughly, they
invite recontextualization": law firms reuse a school's rank as an
interview threshold, legibility to an observer the measure was not built
for ([NOTE-tmpxq56d](../notes.d/NOTE-tmpxq56d.md)). Kleinberg and Raghavan give the formal case of A25's
worry that a shared regime costs organizational diversity: a more accurate
shared algorithm can be each firm's best choice and still lower welfare
([THEORY-tmp3qyox](../theory.d/THEORY-tmp3qyox.md)). Perdomo et al. treat a regime that reshapes what it
reads: its stable point is self-consistent for the world its own use
makes, not optimal ([THEORY-tmpwl9bj](../theory.d/THEORY-tmpwl9bj.md)).

**The direction.** A22 §3 and §7: "Society legible to an institution"
("Who can be classified, monitored, taxed, served, regulated, or
sanctioned?") against "Institution legible to society" ("Who made a
decision, on what evidence, through which authority, and how can it be
challenged?"). "The two can vary independently." A22's "governance
legibility" is the second direction. It is the same relation with observer
and observed exchanged, not a further concept.

James et al. ([NOTE-tmpgi1zu](../notes.d/NOTE-tmpgi1zu.md)) show the directions crossing: remedies
offered as legibility of the institution, access and transparency,
delivered as legibility of its subjects, "down" to the powerful and, under
Robo-debt's reverse onus, demanded of the governed ([THEORY-tmpr3dxe](../theory.d/THEORY-tmpr3dxe.md),
Proposed). Barnehl and Schumacher's measure is a method for the second
direction from output alone, an outlet placed between regime-owned and
opposition poles ([THEORY-tmp5rkez](../theory.d/THEORY-tmp5rkez.md)); whoever chooses the poles and the
topics controls what counts, A22's caution again.

**Stages.** A22 §1's five, existence, observability, legibility, standing
and practical efficacy, extend two the record holds: [CLAIM-296](../claims.d/CLAIM-296.md)'s has,
knows and can deploy, and [CLAIM-349](../claims.d/CLAIM-349.md)'s access, authority and action. This
term is the third of the five. Hyzen et al. ([NOTE-tmp4sv55](../notes.d/NOTE-tmp4sv55.md), skimmed) are
a third source with the shape, from the receiver's side: literacies "turn
availability into access", and critical skills "turn access into knowledge
acquisition". Their stages are an individual's, not an organization's.

**Where the record already used the word.** [CLAIM-081](../claims.d/CLAIM-081.md): "a message can
become more legible while becoming less informative about what originally
happened"; [CLAIM-270](../claims.d/CLAIM-270.md) is that claim's general content, filed after it.
[CLAIM-225](../claims.d/CLAIM-225.md): "[CLAIM-081](../claims.d/CLAIM-081.md)'s legibility is not a task in the manuscript's
family Q". [NOTE-649](../notes.d/NOTE-649.md) names Scott's legibility, by way of Farrell et al.
([LIT-848](../literature.d/LIT-848.md)), and finds "nothing new is added" to it there. Scott's *Seeing
Like a State*, which A22 and A25 lean on, is held as [LIT-tmpb1r6m](../literature.d/LIT-tmpb1r6m.md) and
Unavailable: no lawful copy was reached on 2026-10-21.

## What it is not

A22 §8's table:

| Not equivalent to | Reason |
|---|---|
| Truth | A false interpretation can be readily understood |
| Information preservation | A lossy representation may be easier for a bounded observer to use |
| Observability | A signal can be detected without its significance being understood |
| Salience | Something prominent may remain unintelligible (McCombs and Shaw measure salience in exactly this sense, [THEORY-tmpbonn4](../theory.d/THEORY-tmpbonn4.md)) |
| Credibility | An understandable assertion need not be believed |
| Practical authority | A recognized concern may still lack influence |
| Transparency | Disclosure does not guarantee understanding, usable access, or accountability |

Beside it:

- **Not operational availability** ([TERM-055](TERM-055.md)), which it complements.
  Availability is whether a resource is deployed for a task in time, given
  the cue. Legibility is whether a distinction can be recovered with the
  rules in hand. A situation can be legible and the resource it calls for
  unavailable, or the reverse.
- **Not fidelity** ([TERM-034](TERM-034.md)), which it complements. Fidelity is what a
  representation preserves for an interpreter. Legibility can rise as
  fidelity falls ([CLAIM-081](../claims.d/CLAIM-081.md)). A22: an account "can also become both more
  legible and more accurate. The two dimensions must be assessed
  separately."
- **Not free to the observed.** A25 §3: "**The party benefiting from
  increased legibility need not be the party paying to become legible.**"
  A score of the observer's performance does not show the cost to those
  who are made legible, and the description adequate for an institution
  can merge what its members need told apart ([CLAIM-348](../claims.d/CLAIM-348.md)). Espeland and
  Sauder's schools pay, in brochures and staff time, to be made legible to
  applicants and raters ([NOTE-tmpxq56d](../notes.d/NOTE-tmpxq56d.md)). Lan's version of the point, which
  A25 cited, stays unchecked ([LIT-tmpmdlm4](../literature.d/LIT-tmpmdlm4.md), Unavailable).
- **Not visibility to someone who can act.** A25 §5: "**An institution can
  make a contribution intelligible without making it visible to anyone in
  a position to respond.**" What is legible may still lack authority, which
  is [CLAIM-349](../claims.d/CLAIM-349.md)'s step.

## What it would add, and what would settle it

It names the step between preservation (what survives a representation)
and authority (what acquires influence), which the record has as separate
claims. A22 §4 put it inside the interpretation–authority loop: "Authority
can affect not merely how evidence is interpreted, but which facts become
legible enough to count as evidence at all." Whether that is a new arrow
of the loop or [CLAIM-340](../claims.d/CLAIM-340.md)'s κ′ is [QUESTION-tmp4147z](../questions.d/QUESTION-tmp4147z.md). [CLAIM-tmpjo2zr](../claims.d/CLAIM-tmpjo2zr.md) is
stated in this term.

Settled by the owner's adoption, and by a choice A22 left open: whether
the term takes the task-loss form above or stays qualitative.
