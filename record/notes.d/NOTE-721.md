---
number: 721
status: Read
formerly:
- NOTE-tmpu3hq9
paper: LIT-1024
title: 'Smith & Varzi — Fiat and Bona Fide Boundaries'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the JSTOR PDF (20 pp., pp. 401–420, the published
    version) posted on Barry Smith's site at ontology.buffalo.edu
    (smith/articles/fiat.pdf, fetched over http; the https certificate does
    not match the host). OpenAlex also lists a green open-access copy in
    Columbia's Academic Commons (doi:10.7916/d8t43rtv), which was not
    fetched. Text extracted with pdftotext from the PDF's Paper Capture OCR
    layer. Read: the whole text, all 22 footnotes and the reference list.
    The OCR garbles the logical symbols throughout; the formulas below are
    restored by eye from the extracted text and the prose around them.
    Axioms A≤1–A≤3 and A≈2–A≈3 are missing from the extraction, and are
    given from the prose ("a partial ordering"; "an equivalence relation").
    Quotations of the paper were checked against the extracted text by script, with
    whitespace and line-end hyphenation normalised. The earlier versions
    (EJAP 1997; COSIT 1997, LNCS 1329, with more on geography) were not
    read.
date: '2026-10-13'
summary: >-
  Spatial boundaries are bona fide where there is a physical discontinuity
  or qualitative heterogeneity, and fiat where there is not and the boundary
  owes its existence to demarcation by cognition, language, law or
  mathematics. Bona fide boundaries get ordinary (Bolzanian) topology, in
  which a boundary belongs to one side only; fiat boundaries get a
  Brentanian theory, in which each side has its own and the two coincide.
  The distinction is about whether a discontinuity is there, not about who
  made it, so it does not map onto [CLAIM-194](../claims.d/CLAIM-194.md)'s produced/imposed.
---
<!-- inactive-ok-file: CLAIM-194 — Proposed; the counter this reading was filed to test -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-172 CLAIM-174 — Proposed; the candidate answers this reading bears on, open -->
<!-- inactive-ok-file: THEORY-071 THEORY-072 THEORY-073 — Proposed; the accounts CLAIM-194 grounds on, named as such -->

# NOTE-721: Smith & Varzi — Fiat and Bona Fide Boundaries

## Contribution

A short paper in formal ontology. It names a two-way typology of spatial
boundaries and argues that the classical puzzles of contact and division
(which half of a cut sphere owns the cut, which state owns the border) come
from treating every boundary as one kind. Bona fide boundaries get ordinary
closure topology, mereologised; fiat boundaries get a Brentanian theory of
coinciding boundaries. The formal part is a sketch: "Our aim will be
illustrative". Its one surprising formal result is that the bona fide theory
needs the fiat one, because self-connectedness has to be defined by fiat
connection.

## Key insight

A boundary is bona fide when there is something in the world for it to
follow: a gap, or a change of material. Otherwise it is fiat, and exists
because something demarcates it: an act of perception, a word, a treaty, a
definition. The test is whether the discontinuity is present. Who or what
made the discontinuity is not part of the test.

## Assumptions

- **Spatial, synchronic, macroscopic.** Variables range over "all spatial
  entities, both extended and nonextended", and the axioms are read
  synchronically (fn. 15). There is no time, no process and no dynamics in
  the formal theory. Non-spatial boundaries are not treated.
- **Common-sense level of description.** The authors grant that physics
  shows "macroscopic physical objects are not continuous and that they do
  not have boundaries of the sort countenanced by common sense at all". The
  theory is a theory of the common-sense world, defended as needed for
  "the fiat entities carved out by ordinary discourse".
- **No vague reality.** Vagueness "is a conceptual and semantic matter that
  pertains ontologically only to the fiat world"; every candidate
  aggregate of molecules is "precisely determinate".
- **Extensional mereology with unrestricted fusion** (A≤4, A≤5), chosen for
  simplicity, not argued for.
- **Material objects do not coincide**; fiat boundaries can, because they
  have no bulk.

## Key results

- **The typology (§1).**
  - Inner boundaries: "Inner boundaries involving spatial discontinuity
    (holes, fissures, slits) or qualitative heterogeneity (of material
    constitution, texture, electric charge) we shall call bona fide
    boundaries". The rest are fiat (the hemispheres of a homogeneous
    sphere).
  - Outer boundaries too: planet surfaces are bona fide, national borders
    fiat "at least in those cases where they lie skew to any qualitative
    differentiations or spatial discontinuities".
  - Kinds of fiat: social (generically dependent on beliefs and customs,
    "relatively isolated from causal change"), individual ("individually
    dependent (on these acts, taking place now)"), perceptual, linguistic
    (mass and count nouns: "cow" and "cows" differ in "the different sorts
    of boundary that are imposed upon this material"), and mathematical
    (the equator).
  - An object with any fiat portion of its boundary is a fiat object: the
    North Sea, and also "A mountain, a bay, the branches of a tree, or the
    stem of a champagne glass are all fiat objects in this sense."
  - Fiat objects are not arbitrary: "real properties of the underlying
    factual material ... both enable the drawing of fiat borders and
    constrain the types and location of fiat borders which can be drawn."
  - "while we can reasonably assume that all bona fide objects are
    connected, fiat objects may be scattered" (Polynesia, the constellation
    Orion).
- **Contact between bodies is impossible (§1.2, §2).** "As far as bona fide
  outer boundaries are concerned, however, no genuine contact or
  coincidence of boundaries between John and Mary is possible at all." A
  kiss is a real basis for a fiat demarcation, not contact.
- **Cutting (§2.1).** Cutting reveals no inner surface; the outer surface
  deforms until it splits, like an oil drop. A boundary made by cutting is
  new, not a fiat boundary turned bona fide. Likewise for fences built
  along a border: "this is not a process of transformation. The categorial
  distinction between fiat and bona fide boundaries is absolute."
- **Coincidence (§2.2).** A fiat border is owned by both sides: "each
  hemisphere has its own equator, and the two equators coincide".
  Asymmetric boundaries (only one of the pair present) are allowed: the old
  inner-German border.
- **Bona fide theory (§3.3).** Primitive B(x, y), "x is a bona fide
  boundary for y". Closure c(x) := x + b(x), with the Kuratowski axioms
  mereologised (AB1–AB3). Bona fide boundaries are transitive, dissective
  and symmetric: B(x, y) → B(x, −y) (TB3). Contact is external connection,
  and TB4: EC(x, y) → (Cl(x) → ¬Cl(y)). So John's head is not in bona fide
  contact with his body.
- **Fiat theory (§3.4).** Primitive B*(x, y). AB*1: B*(x, y) → x ≤ y. "the
  main distinguishing feature of fiat boundaries is that they are
  necessarily parts of the entities they bound". So there is no closure
  operator and no open/closed distinction; fiat boundaries are not
  symmetric ("oriented boundaries"). Connection by fiat boundary:
  C*(x, y) := O(x, y) ∨ ∃z∃w(B*(z, x) ∧ B*(w, y) ∧ z ≈ w), with ≈ spatial
  coincidence, an equivalence relation.
- **Dependence (§3.5).** All boundaries are dependent particulars, needing
  some host "of the appropriate kind" (generic, not specific, dependence).
  The naive thesis (AB4, AB*4) is trivially satisfied by a scattered host,
  so a self-connected host is required, and self-connection is defined by
  fiat connection: "A self-connected entity is one all of whose parts are
  separated at most by fiat", Cn*(x) := ∀y∀z(x = y + z → C*(y, z)). Hence
  "the theory of bona fide boundaries presupposes the theory of fiat
  boundaries".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Spatial boundaries divide into bona fide (discontinuity or heterogeneity present) and fiat (demarcated without one), and the division is absolute | moderate | examples and the cutting argument; a stipulated typology, not derived |
| C2 | Bona fide boundaries obey ordinary closure topology; fiat boundaries do not support the open/closed distinction | moderate as formal proposal | AB1–AB3, TB1–TB4; AB*1 and its consequences; no models or consistency proof given |
| C3 | The puzzles of contact and division dissolve once the two kinds are separated | moderate | §2, argued case by case (sphere, disk, equator, Mason–Dixon line) |
| C4 | Distinct bodies are never in genuine contact; apparent contact of bodies is a fiat matter | moderate | appeal to physics and to TB4; informal |
| C5 | Vagueness belongs only to fiat objects; bona fide reality is precise | weak | asserted, with Quine 1985; the supervaluation-style argument is a paragraph |
| C6 | The bona fide theory presupposes the fiat theory, through self-connectedness | moderate | AB5, AB*5, DB*5; "the formal implications of which have still to be examined" |

## Concepts

- **Bona fide boundary.** One that follows a spatial discontinuity or a
  qualitative heterogeneity in the world. The authors also gloss it as
  "physical".
- **Fiat boundary.** One that follows no such discontinuity and owes its
  existence to demarcation; it is part of what it bounds (AB*1).
- **Fiat object.** An object any part of whose outer boundary is fiat. It
  may be scattered.
- **Individual and social fiat.** Dependent on particular acts now, against
  generically dependent on a practice that can outlast any one act.
- **Coincidence (≈).** Sameness of spatial location, possible for
  boundaries, not for material bodies.
- **Generic dependence.** A boundary needs some host of the right kind,
  not any particular one; the host depends specifically on its boundary.

## Connections

- Builds on Brentano's theory of the continuum (through Chisholm and
  Smith 1997) for the fiat side, on Bolzano and Kuratowski for the bona
  fide side, and on Smith 1994 ("Fiat Objects"), where the terms were
  introduced.
- Varzi's SEP entry on mereology ([LIT-124](../literature.d/LIT-124.md)) is the neighbour already
  held; this paper is the mereotopological extension of that framework.
- Casati & Varzi on holes and location (cited in fn. 8, 19) supply the
  location/occupation distinction coincidence relies on.

## Bearing on the record

The LIT asked for four checks.

**1. Does fiat/bona fide map onto [CLAIM-194](../claims.d/CLAIM-194.md)'s produced/imposed?
No.** The two cut across each other. Bona fide is a test of whether a
discontinuity is there; produced is a test of who makes and keeps the
boundary. A cell membrane is bona fide and produced. The beam joining two
pendulums is bona fide and imposed: it is a body, and the paper counts
human-made things such as border fences as bona fide boundaries once they
exist, while denying that anything was transformed. The equator is fiat
and imposed. Nothing in the paper is fiat and produced, and the paper has
no place for a boundary the bounded thing draws for itself: fiat is drawn
by cognition or convention from outside, bona fide is found in the world.
So the distinction sorts the membrane and the beam *together*, exactly as
[CLAIM-194](../claims.d/CLAIM-194.md) says the gap criterion does. That is indirect support for
the counter's point that a criterion indifferent to who made a boundary
cannot separate the two cases. It is not a way of answering it.

A word to watch: the paper says boundaries are "imposed" on material by
cognition ("the systematic imposition of boundaries of many different
sorts"). That imposition is an observer's demarcation, the thing
[THEORY-071](../theory.d/THEORY-071.md)'s individuality condition rules out. [CLAIM-194](../claims.d/CLAIM-194.md)'s
"imposed on it" is something else: a physical constraint maintained by
something other than the system. The record should not read one as the
other.

**2. Is the beam pair's boundary fiat?** The LIT asked whether the boundary
around the coupled pair, drawn by the analyst's target, is fiat "only if a
target counts as demarcation". On the paper's own terms the answer is yes,
and for a stronger reason than the target. Distinct bodies are never in
genuine contact (C4): pendulums and beam are separate bodies, so the
assembly is not one bona fide object, and anything bounding it as one is at
least partly fiat. The same holds for every combined form of distinct
bodies the record has considered: the dancing couple ([CASE-046](../cases.d/CASE-046.md)) is
a scattered fiat object like Polynesia. A target-relative block
([CLAIM-157](../claims.d/CLAIM-157.md), relative as [CLAIM-152](../claims.d/CLAIM-152.md) requires) fits the paper's
individual fiat: dependent on a choice made now, enabled and constrained
by real properties of the material, which here are coupling strengths.
That last clause is the paper's nearest thing to the gap criterion.

**3. What this means for [QUESTION-035](../questions.d/QUESTION-035.md).** Since every combined form
of separate bodies comes out fiat, the distinction cannot discriminate
among the candidates the question cares about: the couple dancing and the
couple after the song are both fiat. It classifies the question's answers
rather than supplying one. It also fixes a vocabulary: whatever criterion
answers the question (gap, entrainment [CLAIM-172](../claims.d/CLAIM-172.md), compensation),
it draws a fiat boundary grounded in real differences, and the paper's
clause that real properties enable and constrain fiat borders is the right description of how such a boundary can
be non-arbitrary without being bona fide. The record may want that
sentence in [CLAIM-157](../claims.d/CLAIM-157.md)'s defence; the use is the record's, not the paper's.

**4. Where the resemblance fails.** The paper is spatial and synchronic.
Its heterogeneity is of "material constitution, texture, electric charge",
not of interaction strength, and it has no dynamics. Reading a
near-decomposability gap as a "qualitative heterogeneity" that makes a
block boundary bona fide would extend the paper, not apply it. Its
dependence relation is ontological (a boundary needs some host), not the
causal maintenance that [THEORY-072](../theory.d/THEORY-072.md)'s production and Weber & Varela's
self-production ([LIT-1018](../literature.d/LIT-1018.md)) are about. Nothing in it bears on
[CLAIM-174](../claims.d/CLAIM-174.md)'s agency conditions or on [THEORY-073](../theory.d/THEORY-073.md)'s Markov blankets
beyond the point in check 1.

No machine-learning instruction is carried; no anthology topic holds it.

## Limitations

- The formal theory is admittedly illustrative: no models, no consistency
  or completeness result, and the authors say the consequences of AB5 and
  AB*5 "have still to be examined".
- The typology is stipulated by examples. Borderline cases between the two
  kinds, such as a gradient of material with no sharp change, are handled
  only by the claim that vagueness is fiat.
- Time is absent. Boundaries that come and go, or are maintained by a
  process, are outside the theory; cutting and fencing are discussed only
  informally.
- The physics is gestured at, not used: the paper concedes that at the
  physical level bodies have no common-sense boundaries, which leaves the
  status of "bona fide" itself level-relative in a way the paper does not
  discuss.

## Open questions

- Is "bona fide" level-relative? If at the physical level there are no
  common-sense boundaries, then a membrane is bona fide only at a level of
  description, and the absoluteness of the distinction needs restating.
- Is there a third kind: a boundary neither found in the world nor drawn
  by an observer, but drawn and maintained by the bounded system? The
  autopoietic literature says yes. A formal theory of it would have to add
  time and a maintenance relation the paper does not have.
- Can a dynamical (non-spatial) gap be treated as heterogeneity, giving a
  bona fide boundary in a state space? A mereotopology of variables rather
  than regions would be needed to say.
