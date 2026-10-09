---
status: Read
paper: 'LIT-tmpc5iin'
title: 'Discrete-event simulation of Lévi-Strauss''s myth analysis'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the publisher's version deposited in HAL
    (halshs-02970262; MDPI typesetting, pp. 1–23, CC BY 4.0): every
    section, both DEVS definitions, the figure captions and the reference
    list. The figures (DEVSimPy screenshots of the mytheme file, the
    transfolist editor and the generated graphs) are images and were not
    legible in the text layer, so the example operation lists and the
    M1-Bororo mytheme file were not seen. The replication materials could
    not be inspected: the DEVSimPy version-2.9 branch holds no myth
    library, and the core-cloud share was unreachable.
date: '2026-10-09'
summary: >-
  Specifies the DEVS models behind the authors' Lévi-Strauss simulation.
  A myth is a list of (term, function) mythemes; homology, inversion,
  opposition and symmetry are each the replacement of one term by a
  user-supplied other in every mytheme; mythemes can be added or
  removed; the canonical formula is described but not given a
  computation. Reproducing 70 Mythologiques myths and 28 Corsican tales
  by transformations chosen to produce them is offered as validation of
  Lévi-Strauss's method; it shows only that the encoding can express
  them.
---

<!-- inactive-ok-file: LIT-775 — Deferred; named as the source of the method modelled, not leaned on -->

# NOTE-tmplssm7: Discrete-event simulation of Lévi-Strauss's myth analysis

## Contribution

The paper specifies a library of DEVS models, in the authors' Python
environment DEVSimPy, that store a myth as a sequence of mythemes, apply
a list of transformation operations to it to produce a named variant,
chain such steps, and draw the variants as a directed graph. It is the
fullest statement of the engine that Doja, Capocchi and Santucci (2021)
summarise. Its new elements over the authors' earlier work (2009, 2010)
are, by its own account, the transformation models and the graph
visualisation. What is true after it: Lévi-Strauss's named operations can
be written as substitutions over (term, function) pairs and executed in a
simulator; and, on the authors' report, all 70 Mythologiques myths they
chose and 28 Corsican tales can be reached that way.

## Key insight

The paper's own: Lévi-Strauss wanted rules that would generate, from any
myth of reference, the whole set of real or possible myths, and that
generative engine can be simulated. What the specification shows is
narrower: every basic transformation is "replace term a by term t in
every mytheme", with t chosen by the analyst, so the engine is a
substitution grammar whose content lies in the analyst's table of which
terms are homologous, inverse, opposite or symmetric. The paper says so
in its Discussion.

## Assumptions

- Lévi-Strauss's analysis is generative and algorithmic, and its
  validity "is beyond discussion, as it is by now confirmed by
  mathematical validation" (citing Petitot, Maranda, Morava and others,
  refs 49–58). This is asserted, not argued.
- A myth decomposes into mythemes, each one term and one function, and
  "the basic mythical structures (armatures) remain unchanged" across
  variants while characters and roles change.
- The variants of a myth form a group of transformations, none
  privileged.
- The opposite, inverse or symmetric of a term (devil for ogre, ovenbird
  for nightjar, water for fire) is known beforehand from ethnography.

## Key results

- **Mytheme representation (§2.2, §4.1).** Example from a Corsican tale:
  (orcu, secret), (shepherd, jealous), (orcu, trapped), (shepherd,
  secret). Each mytheme is an atomic DEVS model; the myth is a coupled
  model; the data are a text file.
- **The seven operations (§2.2).** Homology a → b; inversion a → 1/a;
  opposition a → a⁻¹; symmetry a → −a; each "in each mytheme". Add a
  mytheme (a, x); remove a mytheme. And the canonical formula
  f_x(a) : f_y(b) :: f_x(b) : f_{a⁻¹}(y), read as two twists: a replaced
  by its opposite, and a term value exchanged with a function value. The
  worked examples of inversion and homology are the same operation (ogre
  → devil; ogre → "Sybille"); symmetry and opposition are distinguished
  only by example (a menstruating woman becomes "a non-woman (symmetry)
  but without being a man (opposition)").
- **Canonical formula example.** From The Jealous Potter:
  F_j(n) : F_p(w) :: F_j(w) : F_{n⁻¹}(p); since nightjar⁻¹ = ovenbird, the
  last term reads "the potter is good as an ovenbird for pottery", a
  mytheme Lévi-Strauss finds in other South American myths. This is
  quoted as an illustration; no procedure that would produce it from a
  mytheme file is stated, and the visible operation codes are "h for
  homology, d for deleting a mytheme etc."
- **Generation (§4.3).** TransformationADEVS holds `transfolist`: the new
  myth's name and a list of (operation code, parameters). M1-Bororo →
  M2 → M2-Bororo is the example; complex generations chain instances.
- **Graph (§4.4).** A Collector model gathers all events and draws, with
  NetworkX, a graph whose nodes are myths and whose arcs are generation
  steps.
- **Validation (§5–6).** 70 myths "issued from" the Mythologiques and 28
  Corsican folktales were generated, each by "selecting each time a set
  of transformations to be applied on a given myth"; the Mythologiques
  graph was "compared with the generation performed manually by Claude
  Lévi-Strauss", and the Corsican results "acknowledged by specialists"
  (the reference given is a 2010 book on Corsican popular religiosity).
  No myth list, operation list, comparison table or error is reported.
- **Programme (§7).** A "neo-structural model of canonical formalization"
  of identity politics in the US and EU, with Bayesian inference and
  DEVS; future work, as in the 2021 paper.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Lévi-Strauss's basic operations can be represented as term substitutions over mytheme lists and executed in DEVS | strong (as a specification) | §2.2, §4.3 |
| C2 | The canonical formula is implemented as an operation of the software | weak | listed as selectable (§2.3) and explained by example; no computation given, and the figures that might show it were not legible here |
| C3 | The software generated 70 Mythologiques myths and 28 Corsican tales matching the analysts' variants | moderate (reported, not shown) | §5–6; the transformations were chosen to produce those variants, and no data are given |
| C4 | This experimentally validates Lévi-Strauss's theory and method | not supported here | reproducing given analyses by operations selected to reproduce them cannot fail, so it tests nothing about myth |
| C5 | The variants form a group of transformations | not supported here | asserted from Lévi-Strauss; the implemented operations are not shown to compose to a group (see Bearing) |

## Method

DEVS (Zeigler): atomic models AM = ⟨X, Y, S, δ_int, δ_ext, λ, t_a⟩ and
coupled models CM = ⟨X, Y, COMP, {M_d}, EIC, EOC, IC⟩, run by an
abstract simulator (PythonDEVS, in DEVSimPy). Model classes: MythGen
(emits the reference myth's (term, function) list), TransformationADEVS
(applies its `transfolist`), MythemADEVS, Supervisor (for dynamic
structure), Collector (graph), Observor. The time base orders the chosen
operations; it is not historical time.

## Concepts

- **mytheme**: the basic element of a myth, a term with a function.
- **term / function**: a character or thing able to take a role / the
  role it takes.
- **homology, inversion, opposition, symmetry**: in this paper, each the
  replacement of a term by another term throughout a myth, labelled by
  the kind of relation the analyst holds between the two terms.
- **double twist**: the two exchanges in the canonical formula's fourth
  member, the term a inverted to a⁻¹ and moved into function position,
  and the function y moved into term position.
- **boundary condition**: a third, external condition of the canonical
  transformation: crossing a territorial, linguistic, social or other
  boundary, after which one people's myths are inverse transformations of
  another's.

## Connections

The paper continues Santucci and de Gentili (2009) and Santucci, de
Gentili and Thury-Bouvet (2010), which first proposed DEVS for
Lévi-Strauss, and is the source of the engine summarised in Doja,
Capocchi and Santucci 2021 ([LIT-tmp9axrl](../literature.d/LIT-tmp9axrl.md)); that paper's summary is
faithful to it. It reads Lévi-Strauss through "The Structural Study of
Myth" (1955), the Mythologiques, The Jealous Potter and The Story of
Lynx (the 1955 essay is collected in *Structural Anthropology*,
[LIT-775](../literature.d/LIT-775.md), unread here), and the canonical formula through Thom,
Petitot, Maranda, Mosko, Scubla, Côté, Désveaux, S. Marcus and Morava. It
cites Propp ([LIT-tmppp40q](../literature.d/LIT-tmppp40q.md)) and Greimas among earlier formalisations of
narrative, and Haskell and Badalamenti for an algebraic method, but does
not compare with any of them. Descola ([LIT-tmpmgblk](../literature.d/LIT-tmpmgblk.md)) is not cited.

## Bearing on the record

- **Lévi-Strauss computationally modelled, as prior art.** The 2021
  reader left open whether this paper held a fuller transformation model.
  It does not: the model is a substitution grammar over (term, function)
  pairs, with every substitution and its kind chosen by the analyst, and
  the canonical formula explained but not computed. Whoever cites this
  work as a computational model of Lévi-Strauss's analysis should say it
  encodes and executes an analyst's transformations; it does not find
  them, choose among them, or test them.
- **What is invariant.** The paper says the armatures stay unchanged
  while terms change, but represents no armature. As specified, the
  basic operations rewrite terms and leave each mytheme's function, and
  the order of mythemes, untouched; that sequence of functions is the
  only thing the implementation holds fixed. This is my reading of the
  specification, not a claim the paper makes.
- **Group or not.** "Replace a by b in every mytheme" is not invertible
  when b already occurs in the myth: the two terms merge, and no later
  substitution separates them. So the implemented operations generate a
  monoid of maps on myths, not a group, whatever Lévi-Strauss's variants
  form. Removal is undone only by an addition that remembers what was
  removed. This too is my observation, from §2.2.
- **Descola's point** ([LIT-tmpmgblk](../literature.d/LIT-tmpmgblk.md)) that in myth the analyst cuts the
  transformation continuum describes the software exactly, and the
  Discussion concedes it.
- No THEORY is filed: nothing here is a finding about myth. No
  instruction for machine-learning practice; nothing for the anthology.

## Limitations

- The canonical formula, the operation the title and the abstract lead
  with, has no stated computation.
- The validation reproduces given analyses with transformations chosen
  to reproduce them; no corpus is listed, no held-out myth, no measure,
  no comparison with another analysis or method.
- The "specialists" check of the Corsican tales is reported in one
  sentence with a book reference.
- The relation tables (which term inverts which) are external input and
  are not published in the paper.
- Much of §2.1 and all of §7 are a defence of Lévi-Strauss and a
  programme, not results.

## Open questions

- Given only the reference myth and a relation table, does the software
  produce exactly Lévi-Strauss's variants, or also many he does not
  record? That would show how much of the analysis the table carries.
- How is the double twist computed on a mytheme list, and does it
  reproduce the Jealous Potter step without the ovenbird being supplied?
- Can a system infer the relation table, the opposites and inverses,
  from a corpus of variants, rather than receive it?
