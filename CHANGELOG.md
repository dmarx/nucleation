# Changelog

Assembled from `record/changelog.d/` fragments by `luria collect` on a weekly
cadence — never hand-edited.

### Added

- **The record exists.** It is a Luria record with LIT, NOTE and THEORY schemes
  ported from the Anthology of the SOTA, a closed topic vocabulary seeded
  from the anthology's out-of-scope clusters, and an `ANTH` remote for citing
  the anthology (`ADR-001`).

### Added

- **The first 29 works**, seeded from abstracts and skims: every out-of-scope
  work the anthology's reading-time triage set aside, bar the five that went
  to the anthology. Each LIT is `Deferred`; 26 carry a `Skimmed` NOTE.
- **A reading order** for the deeper readings still owed, in the curation
  entry of 2026-09-25.

### Changed

- **Five works read in full.** Spekkens's *Quasi-quantization*, Abramsky &
  Brandenburger, the *U.S. v. Google* remedies opinion, and Mediano et al.
  alongside Varley & Hoel. Each of their `Skimmed` NOTEs is now a `Read` one,
  and each LIT is now `Active`.

### Fixed

- **The "bridge" claim is withdrawn.** The reading order had called Abramsky &
  Brandenburger this record's bridge to the anthology's topos and sheaf
  work, and it is not.
- **A curation entry no longer asks the owner to mark NOTEs `Read`.** It had
  suggested this based on the owner's reading time. A `Read` NOTE is earned by
  reading the work.

### Changed

- **Nine more works read in full:**
  - Weber et al. on Forman–Ricci curvature (`LIT-020`), `Active`
  - the spectral-dimensions letter (`LIT-028`), `Active`
  - Lindgren & Liukkonen (`LIT-001`), **`Rejected`**
  - the two Spekkens-group papers (`LIT-019`, `LIT-003`), `Active`
  - Fuchs's thesis (`LIT-018`), `Active`
  - the nested HDP (`LIT-002`), `Active`
  - JP 3-12, Cyberspace Operations (`LIT-015`), `Active`
  - the Rhode Island Hospital subpoena order (`LIT-024`), `Active`

  Each `Skimmed` NOTE is now a `Read` one.
- **`published:` is now the exact date of first appearance** where a source
  gives one (`ADR-002`). All 29 LITs were backfilled; three keep month precision
  because no source gives a day.

### Changed

- **Nine more works read in full**, which completes the reading order. They
  are:
  - Artime & De Domenico (`LIT-021`)
  - Bourrat (`LIT-005`), `Proposed`
  - Ni et al. (`LIT-004`)
  - Lim et al. (`LIT-013`)
  - the Eulalia impact shower (`LIT-009`), `Proposed`
  - the waste-collection routing paper (`LIT-008`)
  - the quantum-thermodynamics review (`LIT-010`)
  - Spectral Sets (`LIT-011`)
  - Spectral Networks (`LIT-017`), `Proposed`
- **Four non-papers read in full:** the ISW report (`LIT-023`), the Segundo
  hearing transcript (`LIT-012`), Drezner (`LIT-022`) and Gelman (`LIT-014`).
- 27 of 29 works now have a `Read` NOTE. The two that remain are not open
  access and could not be obtained.

### Added

- **65 works seeded from the survey** of what the anthology had set aside as
  out of scope. Each is `Deferred`; 60 carry a `Skimmed` NOTE.
- **A reading order**, in the curation entry of 2026-09-25.

### Added

- **`philosophy-of-science`** joins the topics and the `philosophy` group
  ([ADR-004](record/decisions.d/ADR-004.md)). *Structural Realism* takes it as primary; three quantum-foundations
  works take it as secondary.

### Added

- **`philosophy-of-science`** joins the topics and the `philosophy` group
  ([ADR-004](record/decisions.d/ADR-004.md)).

### Changed

- **31 survey works read in full** (the first tier and all medium-priority
  works). Each `Skimmed` NOTE, or none, is now a `Read` one.
  - 24 are `Active`.
  - 6 are `Proposed`.
  - 1 is `Rejected`: *The Relativity of Causal Knowledge*.

### Fixed

- **The reading order no longer calls Bourrat's coarse-graining paper the
  successor to [LIT-005](record/literature.d/LIT-005.md).** It is the predecessor.

### Changed

- **30 low-priority survey works read in full.** Every reachable work in the
  record now has a `Read` NOTE. `LIT-068` (local separators) and `LIT-050`
  (Rosenblatt mean-field games) are `Rejected`.
- **`LIT-040`, the nLab two-level type theory page, is `Superseded`** by
  Annenkov, Capriotti, Kraus & Sattler, now filed.

### Fixed

- **The Broadview Six transcript's caption** is *United States v. Rabbitt
  et al.*

### Changed

- **`LIT-064`, *Talagrand Meets Talagrand*, is `Superseded` by `ANTH-LIT-726`.**
  The owner filed it in the anthology, and its reading moved with it.

### Added

- **Nagel, *What Is It Like to Be a Bat?*** (1974), `Active`, with a `Read`
  NOTE. It is the source of the "something it is like" criterion that `LIT-056`
  adopts, and of the argument that functional analysis cannot settle whether
  the criterion is met.

### Added

- **An `anthology-candidate` tag, and a `flags` tag group holding it**
  (`ADR-005`). A work that may belong in the Anthology of the SOTA carries it
  after its topics. Its generated tag page is the list of pending transfers.
  `LIT-056`, `LIT-058` and `LIT-085` carry it, because their readings already
  named the anthology as a possible home.

### Added

- **119 philosophy works from the papers-feed tracker**, all `Deferred`: 95
  with a `Skimmed` NOTE, and 24 seeded from the abstract. They cover
  philosophy of physics and structural realism, philosophy of biology, AI
  consciousness and philosophy of mind, epistemology and philosophy of
  science, and ethics. The curation entry of 2026-09-26 05:58 has the funnel
  and the reading order.
- **`epistemology` and `logic`** join the topics and the `philosophy` group
  (`ADR-006`).

### Changed

- **The four seeds on the `mereology` tag are read in full and now `Active`:**
  - the SEP *Mereology* (`LIT-124`)
  - Carroll (`LIT-123`)
  - Register (`LIT-138`)
  - Meincke (`LIT-142`)

  Each reading corrects its skim.
- **Eight held works whose subject is parts and wholes now carry the
  `mereology` tag,** after their existing topics.

### Changed

- **The six works newly tagged `mereology` are read in full.**
  - Five are `Active`: the SEP *Biological Individuals*, Bourrat's
    *Reproducees*, Baedke's *The Organism*, Schwitzgebel on the United States,
    and *The Extended Mind*.
  - *Scaffolding individuality* is `Proposed`.

### Fixed

- **Ten LIT summaries had lost their citation head (year and identifier).** A
  reading-application script had cut it at the first ". " inside "et al." or a
  DOI. All ten are restored from each document's own fields.

### Changed

- **Sixteen works on the `agency` tag are read in full.**
  - Twelve are `Active`.
  - The observer-theory paper (`LIT-133`) and Terziyan et al. (`LIT-182`) are
    `Rejected`.
  - Enoch (`LIT-117`) and Sharman (`LIT-197`) could not be obtained and stay
    `Deferred`, with the attempts recorded.
- **`LIT-182` loses `anthology-candidate`:** the reading found no ML practice in
  it.
- **`LIT-046` and `LIT-211` are tagged `agency`,** and `LIT-206` takes `agency`
  as its primary topic.

### Fixed

- **Reading notes no longer name local download paths.** 140 LITs, NOTEs and
  one curation entry had recorded where a reader saved a file (`raw4/…`,
  `rawM/…`, `scratchpad/…`), which means nothing outside the session that made
  it. The paths are removed. What was read, and how it was extracted, is kept.

### Added

- **`ADR-008`: no reader sends an email address to any service.** A reader
  sent the owner's address to a lookup service's API. Every agent reading,
  seeding or filing for this record now omits such fields, or uses
  `noreply@anthropic.com`. The rule is in the reading brief.

### Changed

- **Thirty works on the `metaphysics` tag are read in full.**
  - 27 are `Active`.
  - Allori is `Proposed`.
  - Karpenko and the pregeometry paper are `Rejected`.
  - Pernu 2015 and Carson could not be obtained and stay `Deferred`.
- **`philosophy-of-mathematics` and `religion` join the topics** (`ADR-007`).
  Six works are retagged.
- **Four works take `metaphysics` as their primary topic,** and four more are
  newly tagged `metaphysics`.

### Fixed

- **`LIT-110` no longer says Hazelwood argues against it.** His target is
  Laland and colleagues.

### Changed

- **Five works on the `identity` tag are read in full and `Active`.** *Philosophy
  of Fame and Celebrity* could not be obtained.
- **Five more works are tagged `identity`:** individuality, structural realism,
  and the three duality works.
- **Corfield takes `philosophy-of-mathematics` as primary.**
- **`LIT-116` carries its printed title.**

### Fixed

- **Five LIT summaries had kept their seed's opening in front of the reading's
  summary:** `LIT-045`, `047`, `059`, `066`, `075`. The leftover is removed.

### Added

- **Schwitzgebel's *The Weirdness of the World* (`LIT-216`)**, filed at the
  owner's request and read in full from the author's final manuscript.
  `LIT-159` now notes that it reappears, revised, as a chapter.

### Changed

- **Eleven works on the `consciousness` tag are read in full.**
  - 7 are `Active`.
  - Winkielman et al. and Terrill & Veit are `Proposed`.
  - Vieira and Šekrst are `Rejected`.
- **Birch's paper gains its PsyArXiv DOI.**
- **Five secondary tags** are added on the readings' recommendation.

### Added

- **Four sources for Ladyman and Ross's ontic structural realism and
  rainforest realism,** filed at the owner's request and read in full:
  - Ladyman 2001;
  - Ladyman, *Patterns All the Way Up*;
  - Ross 2008;
  - Dennett 1991, *Real Patterns*.

  *Every Thing Must Go* could not be obtained legitimately. The curation entry
  records the gaps and the sources that would close them.

### Added

- **An account of the Yoneda lemma, and the category-theory-and-OSR debate:**
  - the nLab page;
  - Bain 2013;
  - Lam & Wüthrich 2015, which `corrects` Bain.

  Each is read in full. No source in that literature names the lemma. The
  curation entry says what the lemma does and does not support.

### Added

- **Close readings of eleven works on the `epistemology` tag.** All eleven are
  `Active`: [LIT-118](record/literature.d/LIT-118.md), [LIT-131](record/literature.d/LIT-131.md), [LIT-139](record/literature.d/LIT-139.md), [LIT-158](record/literature.d/LIT-158.md), [LIT-161](record/literature.d/LIT-161.md), [LIT-162](record/literature.d/LIT-162.md), [LIT-163](record/literature.d/LIT-163.md),
  [LIT-165](record/literature.d/LIT-165.md), [LIT-175](record/literature.d/LIT-175.md), [LIT-189](record/literature.d/LIT-189.md) and [LIT-213](record/literature.d/LIT-213.md). Each has a `Read` NOTE, and the seeded
  summaries are corrected where the full text disagreed.

### Changed

- **`epistemology` added to five works** that are about knowledge, evidence or
  trust: [LIT-014](record/literature.d/LIT-014.md), [LIT-131](record/literature.d/LIT-131.md), [LIT-161](record/literature.d/LIT-161.md), [LIT-162](record/literature.d/LIT-162.md) and [LIT-213](record/literature.d/LIT-213.md).
- **Primary topic moved to `epistemology`** for [LIT-158](record/literature.d/LIT-158.md) and [LIT-163](record/literature.d/LIT-163.md).
  - [LIT-158](record/literature.d/LIT-158.md) also gains `social-science`.
  - [LIT-163](record/literature.d/LIT-163.md) also gains `philosophy-of-mathematics`.
- **`natural-sciences` added** to [LIT-175](record/literature.d/LIT-175.md).
- **Six unreachable works stay `Deferred`,** and each status note now says what
  was tried: [LIT-119](record/literature.d/LIT-119.md), [LIT-129](record/literature.d/LIT-129.md), [LIT-171](record/literature.d/LIT-171.md), [LIT-181](record/literature.d/LIT-181.md), [LIT-186](record/literature.d/LIT-186.md) and [LIT-203](record/literature.d/LIT-203.md).

### Added

- **Close readings of four works on the `ethics` tag:** [LIT-098](record/literature.d/LIT-098.md), [LIT-101](record/literature.d/LIT-101.md),
  [LIT-179](record/literature.d/LIT-179.md) and [LIT-198](record/literature.d/LIT-198.md). All four are `Active`, each with a `Read` NOTE.

### Changed

- **`ethics` added to [LIT-206](record/literature.d/LIT-206.md)**, whose §7 takes up welfare and moral
  consideration.
- **`ethics` removed from [LIT-101](record/literature.d/LIT-101.md)**, which is descriptive moral psychology and
  draws no normative conclusion. It now leads with `social-science`.
- **Four unreachable works stay `Deferred`,** and each status note now says
  what was tried: [LIT-128](record/literature.d/LIT-128.md), [LIT-174](record/literature.d/LIT-174.md), [LIT-183](record/literature.d/LIT-183.md) and [LIT-214](record/literature.d/LIT-214.md).

### Added

- **Close readings of six works on the `cognition` tag:** [LIT-099](record/literature.d/LIT-099.md), [LIT-140](record/literature.d/LIT-140.md),
  [LIT-149](record/literature.d/LIT-149.md), [LIT-153](record/literature.d/LIT-153.md), [LIT-155](record/literature.d/LIT-155.md) and [LIT-178](record/literature.d/LIT-178.md). All six are `Active`, each with a
  `Read` NOTE.

### Changed

- **`cognition` added** to [LIT-140](record/literature.d/LIT-140.md) and [LIT-147](record/literature.d/LIT-147.md).
- **Tags changed after the readings:**
  - [LIT-155](record/literature.d/LIT-155.md) leads with `social-science` and adds `epistemology`.
  - [LIT-178](record/literature.d/LIT-178.md) leads with `cognition`; it and [LIT-153](record/literature.d/LIT-153.md) drop `linguistics`.
  - [LIT-149](record/literature.d/LIT-149.md) and [LIT-153](record/literature.d/LIT-153.md) add `neuroscience`.
- **[LIT-134](record/literature.d/LIT-134.md) and [LIT-148](record/literature.d/LIT-148.md) stay `Deferred`,** and their status notes now say what
  was tried.

### Fixed

- **Two two-author citations no longer say "et al.":** Prinzing & Vazquez, and
  Bottou & Schölkopf.

### Added

- **`philosophy-of-language` topic** ([ADR-009](record/decisions.d/ADR-009.md)), in the `philosophy` group. It
  covers theories of meaning, meaning holism, assertion and whether machines
  assert, and conceptual change.
- **Close readings of six works on the `philosophy-of-science` tag:**
  - `Active`: [LIT-110](record/literature.d/LIT-110.md), [LIT-114](record/literature.d/LIT-114.md), [LIT-127](record/literature.d/LIT-127.md), [LIT-169](record/literature.d/LIT-169.md) and [LIT-205](record/literature.d/LIT-205.md);
  - `Proposed`: [LIT-208](record/literature.d/LIT-208.md).

### Changed

- **`philosophy-of-science` added** to [LIT-021](record/literature.d/LIT-021.md), [LIT-077](record/literature.d/LIT-077.md), [LIT-079](record/literature.d/LIT-079.md) and [LIT-086](record/literature.d/LIT-086.md).
- **`philosophy-of-language` applied** to five works:
  - [LIT-208](record/literature.d/LIT-208.md) now carries it alone, replacing two wrong tags;
  - [LIT-106](record/literature.d/LIT-106.md) and [LIT-214](record/literature.d/LIT-214.md) now lead with it;
  - [LIT-140](record/literature.d/LIT-140.md) and [LIT-178](record/literature.d/LIT-178.md) add it, and [LIT-140](record/literature.d/LIT-140.md) drops `linguistics`.
- **[LIT-127](record/literature.d/LIT-127.md)** now leads with `natural-sciences`.
- **[LIT-114](record/literature.d/LIT-114.md)** adds `information-theory` and `metaphysics`.
- **[LIT-108](record/literature.d/LIT-108.md), [LIT-180](record/literature.d/LIT-180.md) and [LIT-201](record/literature.d/LIT-201.md) stay `Deferred`,** with the access attempts
  recorded.

### Added

- **A close reading of [LIT-145](record/literature.d/LIT-145.md),** Turner's *Ultrafilters as Propositional
  Theories*. It is `Active`.

### Changed

- **`logic` added** to [LIT-032](record/literature.d/LIT-032.md), [LIT-054](record/literature.d/LIT-054.md) and [LIT-095](record/literature.d/LIT-095.md).
- **`philosophy-of-mathematics` added** to [LIT-151](record/literature.d/LIT-151.md).
- **`philosophy-of-language` added** to [LIT-207](record/literature.d/LIT-207.md).
- **[LIT-106](record/literature.d/LIT-106.md) stays `Deferred`.** Its status note now records why it could not
  be fetched.

### Changed

- **`information-theory` added to four works about information:** [LIT-005](record/literature.d/LIT-005.md),
  [LIT-010](record/literature.d/LIT-010.md), [LIT-025](record/literature.d/LIT-025.md) and [LIT-027](record/literature.d/LIT-027.md). Every work already on the tag had been read.

### Fixed

- **Thirty summaries no longer cite a two-author paper as "X et al."** They
  now name both authors (e.g. "Frigg & Werndl"). The seeded citation heads
  had used "et al." whatever the author count. The fix was checked against
  each work's own author line.

### Added

- **Twenty-two works from an owner-supplied reading list**, all `Deferred`:
  - knowledge sheaves;
  - Kolmogorov complexity, structure functions and MDL (Vitányi and
    collaborators; Grünwald & Roos);
  - compression and rate–distortion generalization bounds (Sefidgaran and
    collaborators);
  - the information and conditional-entropy bottlenecks;
  - the SEP entry *Natural Kinds*;
  - the Riesz representation theorem, bra–ket notation and the GNS
    construction;
  - six papers on self-supervised learning, five of them spectral accounts.

  Twenty-one have a `Skimmed` NOTE.
- **Topics `representation-learning` and `learning-theory`** ([ADR-010](record/decisions.d/ADR-010.md)).

### Changed

- **The seed filer no longer writes "et al." for a two-author work.** One
  author gives the surname, two give "X & Y", and three or more give
  "X et al."

### Added

- **Sixteen works found pursuing the owner's Riesz, Radon–Nikodym and GNS
  question,** all `Deferred` with `Skimmed` NOTEs. They cover:
  - the spectral and density-ratio accounts of contrastive learning;
  - kernel mean embeddings;
  - the representer theorem;
  - SSL-HSIC;
  - variational mutual-information bounds;
  - representational similarity and decodability;
  - identifiability;
  - GNS for kernels.
- **The record's first nine THEORY documents,** all `Proposed`. Six are proved
  in their sources and promote on a close reading. Three are inferences, each
  with a stated test. They are linked by `extends`.

### Added

- **van Rijsbergen, *The Geometry of Information Retrieval* (Cambridge,
  2004)**, filed `Deferred` at the owner's request. The book is closed access.
  Its seed rests on the publisher's contents and opening excerpts, the book's
  annotated bibliography, and Kantor's review.
- **Topic `information-retrieval`** ([ADR-011](record/decisions.d/ADR-011.md)). It is also added to Knowledge
  Sheaves.

### Added

- **Topic `contextuality`** ([ADR-012](record/decisions.d/ADR-012.md)). It leads on [LIT-016](record/literature.d/LIT-016.md) and [LIT-003](record/literature.d/LIT-003.md) and is
  added to [LIT-007](record/literature.d/LIT-007.md), [LIT-019](record/literature.d/LIT-019.md) and [LIT-077](record/literature.d/LIT-077.md).
- **Four bridging works on contextuality,** `Deferred` with `Skimmed` NOTEs:
  - Spekkens (2005);
  - the contextual fraction;
  - Budroni et al.'s review;
  - Contextuality-by-Default applied to behavioural data.
- **Seven THEORY documents bringing the record's contextuality threads
  together.** Two are `Active`, resting on read works. Five are `Proposed`.

### Changed

- **[LIT-262](record/literature.d/LIT-262.md) (van Rijsbergen, *The Geometry of Information Retrieval*) is read
  and `Active`,** from text the owner supplied (chapters 1–6 with front
  matter). It has a `Read` NOTE, and its seed is corrected on two points: the
  Riesz connection, and the book's treatment of non-commuting observables.

### Added

- **[ADR-013](record/decisions.d/ADR-013.md): a work may be held in both records** when each reads it for its
  own question. It narrows [ADR-001](record/decisions.d/ADR-001.md)'s "nothing is filed in both".
- **Xiong, *The Lattice Representation Hypothesis of Large Language Models*,**
  also held in the anthology as [ANTH-LIT-460](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-460.md). It is re-read here against van
  Rijsbergen's geometry of IR, and is `Proposed` with a `Read` NOTE.

### Added

- **Bricken & Pehlevan, *Attention Approximates Sparse Distributed Memory*,**
  also held in the anthology as [ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md) ([ADR-013](record/decisions.d/ADR-013.md)). It is read here as
  associative memory and a kernel read, `Active` with a `Read` NOTE.
- **ZipNN, *Lossless Compression for AI Models*,** read for the entropy
  structure of trained weights. It is `Active` with a `Read` NOTE and tagged
  `anthology-candidate`.

### Fixed

- **Acknowledgement directives are added** to [NOTE-239](record/notes.d/NOTE-239.md) and [NOTE-240](record/notes.d/NOTE-240.md) for
  their citations of `Proposed` documents.

### Added

- **Aerts et al., *Identifying Quantum Structure in AI Language*** (*Entropy*
  28(6):622), read and `Rejected`. Its CHSH values are computed over
  context-dependent marginals, the confound [THEORY-013](record/theory.d/THEORY-013.md) records for the same
  test design, and its Bose–Einstein fit is a relabelled Zipf curve.

### Added

- **Guo & Draper, *Neural Tangent Kernel of Matrix Product States*** (arXiv
  2111.14046), read and `Rejected`. Its sound core, that the infinite-bond
  MPS NTK is a constant multiple of its own GP product kernel, is covered
  rigorously by [ANTH-LIT-557](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-557.md). Its lazy-training lemma is circular, and its
  positive-definiteness claim is proved only as semi-definiteness.

### Added

- **DisCoCat.** Coecke, Sadrzadeh & Clark, *Mathematical Foundations for a
  Compositional Distributional Model of Meaning* (arXiv 1003.4394), and its
  Frobenius-algebra sequel by Kartsaklis, Sadrzadeh, Pulman & Coecke (arXiv
  1401.5980). Both are read and `Active`, as specifications rather than
  results: the first proves and tests nothing, and the second re-reports
  COLING 2012 numbers (best ρ = 0.172).

### Fixed

- [LIT-271](record/literature.d/LIT-271.md) carried a duplicate `number:` key.

### Added

- **[THEORY-017](record/theory.d/THEORY-017.md)** (`Proposed`): in a Hilbert-space model only unitarily
  invariant structure is intrinsic. A basis or factorisation is extra data,
  and Carroll, van Rijsbergen and the two DisCoCat papers differ in where
  they get it. It extends [THEORY-004](record/theory.d/THEORY-004.md).

### Changed

- **[NOTE-134](record/notes.d/NOTE-134.md)** (Carroll, *Reality as a Vector in Hilbert Space*) now connects
  to the Hilbert-space works filed after it was read.

### Added

- **Coecke, Pavlovic & Vicary, *A New Description of Orthogonal Bases***
  (arXiv 0810.0812), read and `Active`. Commutative †-Frobenius algebras on
  a finite-dimensional complex Hilbert space are its orthogonal bases, and
  the special ones are its orthonormal bases.

### Changed

- **[THEORY-017](record/theory.d/THEORY-017.md)** restates the basis–Frobenius correspondence as proved and
  adds that it fails over the reals. It stays `Proposed` on its remaining
  condition.
- **[NOTE-246](record/notes.d/NOTE-246.md)** corrects two statements attributed to that paper.

### Added

- **Abramsky & Heunen, *H\*-algebras and nonunital Frobenius algebras***
  (arXiv 1011.6123), read and `Active`. Without a unit, commutative special
  †-Frobenius algebras satisfying the H\*-axiom are orthonormal bases on a
  complex Hilbert space of any dimension.

### Changed

- **[THEORY-017](record/theory.d/THEORY-017.md)**'s finite-dimensional caveat is narrowed to continuous
  observables, and its real-scalar caveat extended to every dimension. It
  stays `Proposed`.

### Added

- **Ghose, *Measurement as Sheafification*** (arXiv 2512.12249 v2), read and
  `Rejected`. It restates Abramsky–Brandenburger by citation. Its
  "sheafification", Heyting algebra and σ–λ dynamics are never constructed,
  and v2's added Čech obstruction class is a coboundary's, so it is always
  zero.

### Added

- **Abramsky, Mansfield & Barbosa, *The Cohomology of Non-Locality and
  Contextuality*** (arXiv 1111.3620), read and `Active`. The Čech
  obstruction is a sufficient witness of contextuality that misses Hardy's
  model.

### Changed

- **[THEORY-012](record/theory.d/THEORY-012.md)** now says that the cohomological witness is sufficient, not
  necessary.

### Fixed

- **[NOTE-249](record/notes.d/NOTE-249.md)** (Ghose) described Abramsky, Mansfield & Barbosa's
  obstruction class wrongly; the description is corrected and the verdict
  is unchanged.

### Added

- **Abramsky, Barbosa, Kishida, Lal & Mansfield, *Contextuality, Cohomology
  and Paradox*** (arXiv 1502.03097), read and `Active`. All-vs-Nothing
  arguments over any ring imply strong contextuality, which the cohomology
  detects. The paradox connection is one exact case plus analogy.

### Changed

- **[THEORY-012](record/theory.d/THEORY-012.md)**'s cohomology line now says the witness is complete for
  All-vs-Nothing models.

### Added

- **Carù, *On the Cohomology of Contextuality*** (arXiv 1701.00656), read
  and `Active`. A strongly contextual model on a symmetric Bell cover has a
  vanishing cohomological obstruction on every section, refuting
  Conjecture 8.1 of [LIT-277](record/literature.d/LIT-277.md).

### Changed

- **[THEORY-012](record/theory.d/THEORY-012.md)**'s cohomology line records that refutation and the cases
  still open.

### Added

- **Carù, *Towards a complete cohomology invariant for non-locality and
  contextuality*** (arXiv 1807.04203), read and `Active`. The iterated
  joint-model cohomology is exact on cyclic scenarios (Thm 7.7), but its
  general conjecture fails on the §8 cover of [LIT-277](record/literature.d/LIT-277.md).

### Changed

- **[THEORY-012](record/theory.d/THEORY-012.md)**'s cohomology line records the cyclic repair and the
  refutation.

### Added

- **Carù, *Logical and Topological Contextuality in Quantum Mechanics and
  Beyond*** (DPhil thesis, Oxford 2019), read and `Active`. It republishes
  the 2017–2018 cohomology results without repairing the false extension
  or the refuted conjecture.

### Changed

- **[THEORY-012](record/theory.d/THEORY-012.md)**'s cohomology line cites the thesis.

### Added

- **Amartya Sen's capability approach, assembled from nine texts**, all
  read and `Active`:
  - Sen's own *Equality of What?* (1979), Nobel lecture (1998) and
    *Impossibility of a Paretian Liberal* (1970);
  - the SEP and IEP overviews;
  - Robeyns's *Wellbeing, Freedom and Social Justice* (2017);
  - critiques by Nussbaum (2003) and Valentini (2010);
  - Zwolinski's review of *The Idea of Justice*.

  A curation entry sets out the account piece by piece, marking what was
  read in Sen himself and what is second-hand, and lists the Sen texts that
  could not be obtained.

### Added

- **Harry Frankfurt's account of higher-order volitions, assembled from
  seven texts**, all read and `Active`:
  - Frankfurt's own Tanner Lectures (2004);
  - the SEP *Compatibilism*, SEP *Personal Autonomy*, IEP *Autonomy* and
    SEP *Alternative Possibilities* entries;
  - two Velleman critiques (1992, 2002).

  A curation entry sets out the 1971 hierarchy, wantons and persons, the
  mature view, Watson's objection and Frankfurt's replies. It marks what
  was read in Frankfurt himself, and records where the secondary sources
  disagree.

### Fixed

- `source-ok` acknowledgements for three older title mismatches ([LIT-009](record/literature.d/LIT-009.md),
  [LIT-032](record/literature.d/LIT-032.md), [LIT-256](record/literature.d/LIT-256.md)) that the lint's remote check now catches.

### Added

- **Every reference in the owner's prior-art novelty map is now
  registered.** Of 63 works, 6 were already held. The other 57 are new
  `Deferred` seeds with verified identifiers: quantum cognition and IR, topos
  and contextuality, representation theory, structural realism, conceptual
  spaces, the linear-representation and interpretability papers, and the
  thermodynamics of learning. A curation entry maps each reference to its
  code.

### Added

- **Close readings of the prior-art novelty map's references.** 36 of the 57
  seeds were read (34 in full, 2 books in part), each with a NOTE, and now
  carry a status from the reading: 35 `Active`, one `Proposed`. The other 21,
  mostly in-copyright books and paywalled papers, stay `Deferred` and record
  what was tried. A curation entry collects what the readings imply for the
  map.

### Fixed

- First-appearance `published:` dates for Aerts–Gabora I–II,
  Isham–Butterfield I, Döring–Isham I–IV and the information bottleneck
  paper.
- Stone 1936's printed title.
- Tags on three entries.
- Source URLs for Gelfand–Naimark 1943 and Toy Models of Superposition.

### Added

- **Supplemental readings for the prior-art novelty map.** Nine works
  are registered as the citations the map should use where the earlier
  readings found it wrong or unreachable:
  - Stone 1937 for Stone duality;
  - Husimi 1937 on orthomodularity;
  - Stanley's hyperplane-arrangement notes and Zaslavsky's 1975 announcement
    for topes;
  - Cohen & Welling 2014 and Lenc & Vedaldi 2015 as symmetry-detection prior
    art;
  - Russo & Zou for the information-usage bound;
  - Bennett on Landauer's principle;
  - Earman on superselection.

  Seven are read. Zaslavsky's announcement and Earman stay `Deferred`. A
  curation entry gives the verdict for each map row.

### Fixed

- Dated corrections in four earlier reading notes:
  - [NOTE-282](record/notes.d/NOTE-282.md): abelian groups do force degenerate pairs over ℝ;
  - [NOTE-288](record/notes.d/NOTE-288.md): the relay of Lenc & Vedaldi was overstated;
  - [NOTE-275](record/notes.d/NOTE-275.md): Husimi uses the orthomodular law but does not isolate it;
  - [NOTE-306](record/notes.d/NOTE-306.md): Russo & Zou's quantity was given in Xu & Raginsky's notation.
- Stone 1936 now points to Stone 1937.

### Added

- **Signal detection theory.** Five sources registered:
  - Neyman & Pearson 1933;
  - Peterson & Birdsall's 1953 report (the 1954 IRE paper's precursor);
  - Tanner & Swets 1954;
  - Green & Swets 1966;
  - Stanislaw & Todorov 1999.

  Three are read. Neyman & Pearson and Green & Swets stay `Deferred`. A
  curation entry records what the record now says about SDT, and that Peterson
  & Birdsall can stand in for the unreachable Van Trees on the detection half
  of the prior-art map's row 14.

### Changed

- [LIT-351](record/literature.d/LIT-351.md) (Van Trees) names the reachable stand-in.

### Added

- **Twenty-five THEORY documents** (9 Active, 14 Proposed, 2 Rejected),
  drawn from readings the record already held. They cover information and
  learning theory, the thermodynamics of computation, representation and
  symmetry, logic and quantum logic, signal detection, agency, ethics,
  consciousness, structural realism and real patterns. Before this, 21
  topics had no theory.
- **Four works on phases of training:** Saxe et al. 2018, Zucchet et al.
  2025, Prakash & Martin 2025 and Zhou et al. 2025, all read. Saxe and
  Zucchet are also held in the anthology. Together they back the rejection
  of the information-bottleneck compression account, and a new theory that
  the later phases of training differ in kind.

### Added

- **Chuai & Zhao 2020, *Anger makes fake news viral online*,** seeded as
  `Deferred` from the reading feed (the anthology's [issue 180](https://github.com/dmarx/anthology-of-the-sota/issues/180)), where it was read
  on three separate days. Its subject, how emotion drives the spread of false
  news, has no anthology topic, so it is filed here beside the record's other
  information-operations work. Read for triage only, so no NOTE yet.
- **Döring & Isham 2008, *'What is a Thing?': Topos Theory in the
  Foundations of Physics*,** filed `Active` and read in full, at the owner's
  direction after it had been set aside as out of scope. It is the one-volume
  statement of the topos programme whose four papers the record holds. Its
  new material is small, and it leaves [THEORY-037](record/theory.d/THEORY-037.md)'s open Heyting implication
  open.

### Added

- **Li 2026, "The two dragons of cognition: recursive condensation for
  predictive processing"** (Frontiers in Computational Neuroscience), read in
  full at the owner's request and filed `Rejected`. It is a hypothesis essay
  with no data or model, and it rests on two misstated results:
  - "memoized Savitch" inverts the theorem, which saves space by recomputing
    and still takes exponential time;
  - Urysohn's lemma is stated as an "if and only if", and is made to yield a
    linear readout it does not give.

  Its abstract's "demonstrate", "prove" and "derive" are not borne out in the
  text. Connections to [THEORY-030](record/theory.d/THEORY-030.md) and [THEORY-035](record/theory.d/THEORY-035.md) are recorded in the note.

### Fixed

- **Two title mismatches against arXiv, acknowledged with `source-ok`.**
  - [LIT-041](record/literature.d/LIT-041.md) was retitled in arXiv v2 (2026-09-30). The record keeps the v1
    title of first appearance.
  - [LIT-369](record/literature.d/LIT-369.md)'s title differs only by arXiv's TeX markup.

### Added

- **Li, "Structural Decoupling: A Scaffold-Flow Theory of Generalization and
  Alignment"** (arXiv 2506.20699 v2), read in full at the owner's request as
  possible follow-up to [LIT-373](record/literature.d/LIT-373.md), and filed `Rejected`.
  - What it proves is standard.
  - Its new results do not hold up:
    - the phase transition at width assumes its conclusion;
    - the width-versus-VC example contradicts itself;
    - the "fundamental theorem" is false as stated (it should use
      fat-shattering, not pseudo-dimension);
    - nothing shows the spectral estimator recovers width.
  - It repairs none of [LIT-373](record/literature.d/LIT-373.md)'s grounds for rejection, so [LIT-373](record/literature.d/LIT-373.md) stays
    `Rejected`.
  - `published:` is v2's date, because v1 under the same number is an
    unrelated paper.

### Fixed

- **[NOTE-321](record/notes.d/NOTE-321.md) said [LIT-373](record/literature.d/LIT-373.md)'s metabolic maintenance cost "runs against"
  [THEORY-030](record/theory.d/THEORY-030.md). It does not**, as the owner pointed out: a standing cost of
  holding structure means the structure is dissipative, which Landauer's
  principle allows. [THEORY-030](record/theory.d/THEORY-030.md) now says so under "What this does not say",
  noting that error correction against noise is itself an erasure it
  prices.

### Changed

- **Xin Li's structural-learning programme, re-read as one, charitably.** [LIT-374](record/literature.d/LIT-374.md) moves from `Rejected` to
  `Proposed`. [LIT-373](record/literature.d/LIT-373.md) stays `Rejected`, but on new grounds: after repair it is unoriginal, its predictions do not
  discriminate, and its Theorem 2 is unargued, rather than the repairable mathematical slips. [NOTE-321](record/notes.d/NOTE-321.md) and [NOTE-322](record/notes.d/NOTE-322.md)
  carry new summaries and superseding sections.

### Added

- **The programme's two companion papers**, both `Proposed`:
  - arXiv 2602.07974 v2, "Structural Learning Theory", its fullest formal statement;
  - arXiv 2603.15412 v1, "Local Urysohn Width". The identifier now serves an unrelated v2.

  A curation entry gives verdicts takeaway by takeaway.

### Added

- **Isham–Butterfield's "topos perspective on the Kochen–Specker theorem",
  parts II–IV**, read together as one series continuing part I ([LIT-325](record/literature.d/LIT-325.md)):
  - **II (Butterfield & Isham 1998), Active.** The sieve-valued semantics also
    arises classically, so it is generic, not a way around Kochen–Specker.
  - **III (Hamilton, Isham & Butterfield 1999), Superseded by IV.** It moves the
    base to commutative von Neumann algebras, with propositions as clopen
    regions of Gelfand spectra. It stays the citation for introducing that
    base.
  - **IV (Butterfield & Isham 2001), Active.** It proves the correspondence
    between coarse-graining and clopen regions, and shows that a state's
    valuation is fixed by its supports.

  The series' major takeaways are argued appropriately; the theorems are thin,
  and Döring–Isham is its mature form.

### Fixed

- [LIT-325](record/literature.d/LIT-325.md)'s note on the series gave Part II the wrong title and author order.
  [NOTE-292](record/notes.d/NOTE-292.md) had Part III's author order wrong.
- **arXiv identifiers that have served two different papers are now
  version-qualified.**
  - [LIT-374](record/literature.d/LIT-374.md) and [LIT-377](record/literature.d/LIT-377.md) both held `2506.20699`, so the identifier claimed two
    documents and `main`'s lint failed. They are now `2506.20699v2` and
    `2506.20699v1`, the paper each actually is.
  - [LIT-375](record/literature.d/LIT-375.md) is now `2602.07974v2`.
  - [LIT-376](record/literature.d/LIT-376.md) is now `2603.15412v1`. Its `source-ok` directive is gone, since
    the identifier now names the paper recorded.

### Added

- **Antonio Damasio, six works.** They run from the 1989 retroactivation
  proposal through the somatic marker hypothesis and Bechara et al.'s gambling
  task to feelings as the source of consciousness. Three were read in full,
  with NOTEs. Three are `Deferred` seeds because no full text was reachable.
- **`emotion-and-affect` joins the topics** ([ADR-014](record/decisions.d/ADR-014.md)), in the philosophy
  group. [LIT-379](record/literature.d/LIT-379.md) (anger and fake news) takes it.
- **The works held in both records now name their anthology entries**
  ([ADR-013](record/decisions.d/ADR-013.md)), now that the anthology has numbered them: ZipNN ([ANTH-LIT-750](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-750.md)),
  the context-content paper's v1 and v2 ([ANTH-LIT-769](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-769.md)), work capacity
  ([ANTH-LIT-756](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-756.md)), collective intelligence ([ANTH-LIT-742](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-742.md)) and Ricci-flow
  community detection ([ANTH-LIT-766](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-766.md)). ZipNN drops its `anthology-candidate`
  flag, since the transfer it awaited is decided.

### Fixed

- **`main` failed the unique-identifier check.** [LIT-377](record/literature.d/LIT-377.md) (context-content v1)
  and [LIT-374](record/literature.d/LIT-374.md) (the author's v2, filed in parallel) share arXiv 2506.20699.
  [LIT-377](record/literature.d/LIT-377.md) now names [LIT-374](record/literature.d/LIT-374.md) as its `superseded_by`, and each note names the
  other.

### Added

- **Marvin Minsky's Society of Mind programme, eight works.** They run from
  the 1974 frames memo through *The Society of Mind* (1986) to *The Emotion
  Machine* (2006, read from the author's posted draft). Six were read in
  full. The memos are linked by `extends:` as their own texts describe.
- **Douglas Hofstadter, eight works.** Four are papers on analogy and
  Copycat, including his lead essay in the world-models collection that
  [LIT-195](record/literature.d/LIT-195.md) introduces. Four are books. One was read in full; the rest are
  `Deferred` seeds because no lawful full text was reachable.
- **A bridge from Minsky's society of mind to Schwitzgebel's conscious
  United States: eleven works and a THEORY.** The works are Selfridge,
  Putnam, Block, Lycan, Brooks, List & Pettit, Huebner, IIT 3.0, Kammerer,
  List and Levin; seven were read in full. [THEORY-043](record/theory.d/THEORY-043.md) (Proposed) holds
  that the two are one functionalist move run in opposite directions. It
  finds that what separates them is an anti-nesting principle or an
  architectural criterion, and that the readings supply neither on
  principled grounds.

### Fixed

- **The source check on `main` failed when arXiv answered.** [LIT-376](record/literature.d/LIT-376.md) and
  [LIT-377](record/literature.d/LIT-377.md) carry version-qualified arXiv ids, which arXiv resolves to the
  latest version's title. Their `source-ok` acknowledgements now name the
  versioned ids.

### Added

- **Isham 1997, "Topos theory and consistent histories"** ([LIT-390](record/literature.d/LIT-390.md)),
  Active. This is the paper the Kochen–Specker topos series names as its
  motivation. It puts the consistent-histories formalism over the poset of
  Boolean subalgebras, and gives probability claims sieve-valued truth values
  in a Heyting logic. It is now a source for [THEORY-024](record/theory.d/THEORY-024.md)'s rejection, as the
  record's cleanest counterexample: global sections exist for every
  proposition, yet excluded middle fails.
- **Isham & Butterfield 1999, "Some possible roles for topos theory in
  quantum theory and quantum gravity"** ([LIT-389](record/literature.d/LIT-389.md)), Active, narrowly. It
  is the programme's manifesto, proves nothing new, and is mostly superseded
  by the series and the topos book.

### Fixed

- [NOTE-277](record/notes.d/NOTE-277.md) records that "neo-realism" appears in Isham 1997, eleven years
  before Döring–Isham's "we coin the term".

### Added

- **David Chalmers, thirteen works, eleven read in full.** These are the
  hard problem, fading qualia, the meta-problem, the combination problem,
  implementation and LLM consciousness, plus the extended-mind programme
  around [LIT-097](record/literature.d/LIT-097.md): Chalmers's foreword and 2019 chapter, Clark's reply, and
  the critics Adams & Aizawa and Rupert.
- **Daniel Dennett, twelve works, and *The Mind's I* with Turing and Searle
  filed from it.** Ten are read in full, across the intentional stance,
  "Quining Qualia", multiple drafts, "Facing Backwards", the narrative self
  and "Where Am I?".
- **[THEORY-043](record/theory.d/THEORY-043.md) gains a section from these readings.** Agency is cheap
  to agree on, discharge licenses only the downward move, invariance
  narrows the dispute to architecture, and there are two new candidate
  criteria.

### Fixed

- **Three older notes corrected from later readings.**
  - [NOTE-131](record/notes.d/NOTE-131.md) v3: Block's counterexample to Putnam, Putnam's paraphrased
    "quotation" and first printing, and which Brooks wrote "Brain City".
  - [NOTE-180](record/notes.d/NOTE-180.md) v3: the coupling–constitution objection is attributed to
    Adams & Aizawa 2001, now filed, with the name from their later work.
  - [NOTE-188](record/notes.d/NOTE-188.md) v2: Kammerer's principle is stated with both its conditions.

### Added

- **The personal-identity literature, eighteen works, twelve read in
  full.** Locke, Hume, Williams, Parfit and Lewis; Olson's SEP entry,
  Strawson's "Against Narrativity", Gallagher 2000 and Metzinger's "Self
  models"; and Shanahan's three papers on LLM selves. *Reasons and
  Persons*, *The Human Animal*, *The Constitution of Selves*, *Subjectivity
  and Selfhood*, *Being No One* and Chalmers's "What we talk to" are
  Deferred.
- **Six of the seven unidentified converted texts.** Frankish 2016, Taylor
  2024, Schwitzgebel's reply to Kammerer, Dennett's reply to Stich, Adams &
  Aizawa's "Defending the Bounds of Cognition" and Burns's review of
  *Fluid Concepts*, all read in full. The seventh is an excerpt of
  [LIT-439](record/literature.d/LIT-439.md).
- **Two topics.** `self-and-personhood` ([ADR-015](record/decisions.d/ADR-015.md)) and `phenomenology`
  ([ADR-016](record/decisions.d/ADR-016.md)).

### Changed

- **`identity` is renamed `individuation`** and narrowed to the
  individuation of things; the self and the person are now
  `self-and-personhood` ([ADR-015](record/decisions.d/ADR-015.md)).

### Fixed

- [NOTE-362](record/notes.d/NOTE-362.md) v2: Schwitzgebel's reply presses Kammerer's condition A, not B.
- [THEORY-043](record/theory.d/THEORY-043.md) v2: takes in the reply's condition-A gap, its simplicity
  dilemma and its Leo case.
- [NOTE-180](record/notes.d/NOTE-180.md) v4: the "coupling–constitution fallacy" name was in use by late
  2005.

### Added

- **Social ontology, twenty-four works, eight read in full.** Searle 2006,
  North 1991, Hindriks & Guala 2015, Epstein's SEP "Social Ontology",
  Durkheim's "Qu'est-ce qu'un fait social ?", Haslanger 2000 and both
  Ritchie papers are read. Searle 1990 and 1995, Gilbert 1989 and 1990,
  Bratman 1992 and 2014, Tuomela & Miller, Lewis's *Convention*,
  Bicchieri, Guala 2016, *The Ant Trap*, Berger & Luckmann, Hacking, Ásta,
  Thomasson and Tollefsen are Deferred.
- **`social-ontology` joins the topics** ([ADR-017](record/decisions.d/ADR-017.md)), and six existing works
  take it.

### Changed

- [THEORY-043](record/theory.d/THEORY-043.md) v3: a scoping note from Ritchie and Epstein on which group a
  criterion for group minds applies to; Tollefsen joins its unread works.

### Changed

- **CI pins luria 0.34.0**, up from 0.31.0, in the docs and pages
  workflows. The record needed no migration: `repair` and `link --fix` have
  nothing to do under it, and the lint gives the same findings as 0.31.0,
  now listing each retired or unresolved citation's sites inline.

### Added

- **Moral psychology, twenty-one works, seventeen read in full.**
  Morality-as-cooperation's own programme (Curry 2016, the MAC-Q, "Moral
  Molecules", the 256-society study, the Turkish validation); its rivals
  (Haidt 2001, Haidt & Joseph 2004, Graham et al. 2013, the MFQ-2, Rai &
  Fiske, Baumard, André & Sperber; Schein & Gray Deferred); and its
  evolutionary sources (Hamilton 1964 I and II, Trivers, Maynard Smith &
  Price, Axelrod & Hamilton, Nowak; Alexander, Boehm and Tomasello 2016
  Deferred).
- **Two topics.** `moral-psychology` ([ADR-018](record/decisions.d/ADR-018.md)) and `game-theory` ([ADR-019](record/decisions.d/ADR-019.md)).

### Fixed

- [NOTE-034](record/notes.d/NOTE-034.md) v3: the hawk–dove attribution to Maynard Smith & Price 1973 is
  corrected, C7's comparison with Moral Foundations Theory is qualified,
  and the replies to the purity objection are connected.

### Added

- **Dissipative structures, twenty-three works, fourteen read in full.**
  Prigogine's Nobel lecture, Turing 1952, the BZ reaction and Cross &
  Hohenberg (skimmed); the critics and fluctuation theorems (Dewar,
  Grinstein & Linsker, Kleidon, Jarzynski, Crooks, Seifert); and life as
  dissipation (Schneider & Kay, Morowitz & Smith, England 2013, Perunov,
  Marsland & England, Friston 2013). Glansdorff & Prigogine, Nicolis &
  Prigogine, *Order out of Chaos*, Landauer 1975, Martyushev & Seleznev,
  *What Is Life?*, *Incomplete Nature* and *Biological Autonomy* are
  Deferred.
- **`thermodynamics` joins the topics** ([ADR-020](record/decisions.d/ADR-020.md)); twenty-seven works and
  two THEORYs take it.

### Fixed

- [NOTE-094](record/notes.d/NOTE-094.md) v3: [LIT-211](record/literature.d/LIT-211.md) is read, not Deferred, and the demarcation question
  points to the new readings.

### Added

- **Psychopathology, emotion and psychotherapy: eighteen notes on fifteen
  requested works, ten of them read in full.**
  - Read in full: Borsboom's network theory, Hofmann & Hayes on
    process-based therapy, Salkovskis et al. on mechanisms of change,
    Gross on emotion regulation, Barrett's constructed emotion, the ACT
    model (Hayes et al. 2006) and Kashdan & Rottenberg on psychological
    flexibility.
  - Read in place of a work that could not be read: Kendler 2008 for
    Kendler 2005, Frijda et al. 2014 for *The Emotions*, and
    Barnes-Holmes et al. 2004 for *Relational Frame Theory*.
  - Deferred, with no lawful full text: Engel 1977, Kendler 2005,
    *Emotion and Adaptation*, *The Emotions*, the RFT book, Hayes et
    al. 1996, Macri & Rogge 2024 and Bandura 1977.
- **`psychopathology-and-treatment` joins the topics** ([ADR-021](record/decisions.d/ADR-021.md)). Fifteen
  of the eighteen notes take it.
- **`rivals` joins the LIT and THEORY relations** ([ADR-022](record/decisions.d/ADR-022.md)). It is symmetric:
  two accounts of the same phenomenon that cannot both be right, where
  neither yet corrects the other. Its first use is Barrett's constructed
  emotion against Lazarus's and Frijda's appraisal theories.

### Added

- **Fifteen theories** from the psychopathology, emotion and
  psychotherapy batch and from self-determination theory. One is Active,
  that a treatment's efficacy is not evidence for its theory of change.
  The other fourteen are Proposed. They cover:
  - felt affect as the body's regulatory state;
  - constructed emotion against appraisal theory, declared `rivals`;
  - regulation not separate from generation;
  - biology implementing psychology;
  - maintenance loops;
  - transdiagnostic inflexibility and need frustration;
  - ACT's account of the self, and self-as-context as a treatment
    process;
  - autonomy as graded integration, and acquisition history fixing it;
  - cognitive evaluation theory, and the reward undermining effect.
  Each is set against the record's philosophy-of-mind holdings. Those
  holdings now point back at the theories.
- **Self-determination theory**: five works read in full, plus the
  Cameron & Pierce side of the reward dispute as Deferred seeds.
- **`motivation` joins the topics** ([ADR-023](record/decisions.d/ADR-023.md)).

### Added

- **Agency, self, control and self-governance: 44 readings** (27 read, 17
  Deferred seeds), filed in five groups:
  - biological autonomy, enaction and the free-energy principle;
  - control and self-control;
  - evidence-accumulation models;
  - self, person and practical reason;
  - authenticity and self-governance.
- **Two Markov-blanket critiques now `correct` [LIT-526](record/literature.d/LIT-526.md).**
- **Nineteen theories from the batch**, two Active and seventeen Proposed:
  - **Behavioural integration (7):**
    - accumulator optimality: leak balanced by inhibition, Active;
    - the readiness potential;
    - goals as accumulation parameters;
    - Ainslie's bargaining;
    - model-based and model-free arbitration by reliability;
    - the expected value of control;
    - HKB coordination.
  - **Individuation and agency (4):**
    - a Markov blanket is relative to a chosen internal set, Active;
    - blankets do not individuate;
    - organisms against dissipative structures, the record's first answer
      to [NOTE-094](record/notes.d/NOTE-094.md);
    - minimal agency.
  - **Self-governance, narrative and the self (8):**
    - Bratman's diachronic self-governance, declared `rivals` with
      Ainslie's bargaining;
    - Korsgaard on the unity of agency, and on obligation;
    - narrative identity;
    - self-concordance;
    - authenticity constructs;
    - Metzinger's self-model;
    - phenomenal unity.
- **Six topics** ([ADR-025](record/decisions.d/ADR-025.md)): `well-being`, `learning-and-conditioning`,
  `psychometrics`, `philosophy-of-biology`, `embodied-cognition` and
  `free-will`. They are applied across 82 existing documents, and nine of
  those now take one first.

### Changed

- **Agent, individual, self and person are kept apart, and four unities
  are represented separately** ([ADR-024](record/decisions.d/ADR-024.md)).
  - `self-and-personhood` is retired into `self` and `personhood`.
  - New topics: `behavioral-integration`, `phenomenal-unity`,
    `narrative-unity` and `self-governance`.
  - Forty-two documents were retagged, twenty-one took a unity word, and
    prose that ran the terms together was corrected.
- [THEORY-029](record/theory.d/THEORY-029.md), [THEORY-040](record/theory.d/THEORY-040.md), [THEORY-044](record/theory.d/THEORY-044.md) and [THEORY-051](record/theory.d/THEORY-051.md) take the batch's
  readings: Frankfurt's 1987 essay, Bratman's and Korsgaard's stopping
  points, Korsgaard's structural account, and the Metzinger and IFS
  contrasts.

### Added

- **Model comparison and Fisher geometry: eighteen readings**, seventeen
  read in full, filed in three groups:
  - model comparison: Savage–Dickey, Bayesian model reduction, structure
    learning, MacKay, Watanabe's WBIC;
  - Fisher geometry and spectra: Amari, K-FAC, Shampoo, Papyan, neural
    collapse;
  - kernel spectra and SAEs: Bietti & Bach, Cao et al., Basri et al.,
    Gemma Scope.
- **`model-comparison` and `information-geometry` join the topics**
  ([ADR-026](record/decisions.d/ADR-026.md)).

### Changed

- **[LIT-354](record/literature.d/LIT-354.md).** Watanabe 2009 names WBIC as its read substitute.

### Documentation

- **CLAUDE.md.** The boundary section now states [ADR-013](record/decisions.d/ADR-013.md)'s dual-holding
  rule.

### Changed

- **Dickey (1971), [LIT-610](record/literature.d/LIT-610.md), is now read.** It was Deferred, then read in
  full from a copy the owner supplied (a JSTOR scan, OCR'd and checked
  against the page images), with a NOTE.
  - The Savage–Dickey ratio is its Eq. 3.9. It holds for any continuous
    likelihood.
  - Dickey credits the formula to Savage and the proof to Dickey & Lientz.
  - [THEORY-081](record/theory.d/THEORY-081.md) now takes it as a source for its point-mass clause.
  - [LIT-609](record/literature.d/LIT-609.md), [LIT-620](record/literature.d/LIT-620.md), [NOTE-484](record/notes.d/NOTE-484.md) and [NOTE-487](record/notes.d/NOTE-487.md) now cite it as read. [LIT-620](record/literature.d/LIT-620.md)'s
    description of Wagenmakers's continuity condition is corrected: Dickey's
    theorem needs both the continuity condition and the shared likelihood.

### Added

- **Neural dynamics and consciousness: eight readings**, six read in full,
  filed in two groups:
  - neural dynamics: co-ripple co-firing, interacting cortical spirals,
    sustained visual perception, and a traveling-waves review (Deferred);
  - consciousness and biophysics: tryptophan superradiance, conscious
    birds, ALARM theory, and spontaneous radiation versus Orch OR
    (Deferred).
- **Seven Proposed theories from the batch**, including a rival pair on
  what consciousness was first for: alarm, or a common currency for
  trade-offs.

### Changed

- **[NOTE-330](record/notes.d/NOTE-330.md).** Its unfiled subcortical-feeling candidate now points to the
  theory that carries it.

### Added

- **Ned Block on consciousness: seven papers**, all read in full from
  Block's own deposits: access vs phenomenal consciousness (1995), the
  harder problem (2002), two neural correlates (2005), overflow and the
  mesh argument (2007, 2011), comparing the major theories (2009), and the
  no-report paradigm (2019).
- **Four Proposed theories from them:** perceptual consciousness overflows
  access; its basis is recurrent sensory activity, not prefrontal access
  machinery; neither report nor no-report paradigms isolate that basis;
  and a deficit that removes consciousness and a capacity together does
  not show the capacity is a function of phenomenal consciousness.

### Changed

- **[THEORY-023](record/theory.d/THEORY-023.md)** (v2). Block 2002 (meta-inaccessibility) and Block 2009
  (the biological theory) join its sources.

### Added (continued)

- **Ned Block on functionalism, meaning, AI and perception: eight works
  read** from his own deposits:
  - Block & Fodor 1972, which corrects Putnam's machine-state theory;
  - "Psychologism and Behaviorism" (Blockhead), which corrects Turing's
    sufficient condition;
  - conceptual role semantics, in the "Advertisement" and in "Functional
    Role and Truth Conditions" (the record's "Block 1987");
  - "Inverted Earth";
  - "The Mind as the Software of the Brain";
  - "Mental Paint";
  - the précis of *The Border Between Seeing and Thinking*. The book is
    seeded Deferred.
- **Mashour, Roelfsema, Changeux & Dehaene 2020**, the record's first
  global-workspace source. It rivals Block's overflow and no-report papers
  and IIT.
- **Damasio & Damasio 2022**, "Homeostatic feelings and the biology of
  consciousness". It was skimmed through a summarising fetch tool, since
  the publisher's page is bot-challenged.

### Changed

- **Notes that cited Block by year now name the code:** [NOTE-093](record/notes.d/NOTE-093.md), [NOTE-104](record/notes.d/NOTE-104.md),
  [NOTE-117](record/notes.d/NOTE-117.md), [NOTE-143](record/notes.d/NOTE-143.md), [NOTE-342](record/notes.d/NOTE-342.md), [NOTE-354](record/notes.d/NOTE-354.md) and [LIT-404](record/literature.d/LIT-404.md).

### Added (theories)

- **Five more Proposed theories from the Block batch and its companions:**
  - psychologism: behavioural capacity does not fix intelligence;
  - long-arm accounts of phenomenal character fail;
  - two-factor content;
  - global availability by ignition, which rivals the two overflow
    theories;
  - consciousness supplied by homeostatic feeling, which extends
    [THEORY-045](record/theory.d/THEORY-045.md) and rivals global availability.

### Added

- **`loss-landscapes` joins the topics** ([ADR-027](record/decisions.d/ADR-027.md)).
- **Mode connectivity, loss landscapes and model merging: 33 readings**,
  all read, filed in four groups:
  - foundations (Garipov, Draxler, Frankle, Kuditipudi, Entezari, Git
    Re-Basin, Ferbach, Benton);
  - extensions (mechanistic, layerwise, geodesic and star-shaped
    connectivity, the symmetry account, transformers, mixtures of experts,
    adversarial robustness);
  - merging and other settings (TIES, ZipIt!, fine-tuning regions,
    continual and federated learning, GNNs, generative models, the ELBO);
  - landscape theory and generalization (Yang et al., Martin & Mahoney,
    two double-descent papers, and three on where generalization is
    carried).

  Entezari et al. and Git Re-Basin are [ADR-013](record/decisions.d/ADR-013.md) second readings of
  anthology holdings.

### Added (theories)

- **Fourteen Proposed theories from the batch:**
  - **Landscape structure:**
    - found solutions lie in one connected low-loss set;
    - linear connectivity emerges in training;
    - barriers vanish modulo the full symmetry group, with width lowering
      them and depth raising them;
    - star domains.
  - **Mechanisms and merging:**
    - a surviving barrier marks different mechanisms;
    - along a linear path, features interpolate;
    - shared-start connectivity needs shared structure;
    - fine-tuning regions;
    - ZipIt!'s unmatched deep features;
    - TIES's coordinate interference.
  - **Generalization:**
    - global structure over curvature;
    - the double-descent peak in random features;
    - the out-of-distribution-best readout lies below the top layer;
    - diversity, not volume, for compositional generalization.

### Changed

- **[LIT-669](record/literature.d/LIT-669.md) and [NOTE-538](record/notes.d/NOTE-538.md).** These were filed in this
  contribution as saying Lubana et al. prove their Conjecture 1 for one
  hidden layer. Appendix F.3 proves the converse, and both now say so.

### Added

- **Susan Wolf's Reason View, seeded:** "Asymmetrical Freedom",
  "Sanity and the Metaphysics of Responsibility", and *Freedom Within
  Reason*. All three are Deferred, because no lawful open copy exists. Each
  says what the secondary sources report and what a reader could supply.
- **Fischer & Ravizza's reasons-responsiveness:** the 1987 chapter and
  *Responsibility and Control*, both Deferred. Fischer's open-access
  "Stories and the Meaning of Life" and the SEP *Moral Responsibility*
  entry were both read.
- **Three Proposed theories:** Wolf's Reason View, her praise/blame
  asymmetry, and Fischer & Ravizza's guidance control. The asymmetry and
  guidance control are rivals on blame. Each says it rests on secondary
  reports.
- **Harry Frankfurt, first-hand:** the 1969 Frankfurt-cases paper and the
  1971 "Freedom of the Will and the Concept of a Person", both read. The
  1982 essay, "The Faintest Passion" and the 1988 collection are seeded
  Deferred.
- **Two Proposed theories from Frankfurt:** the hierarchical (endorsement)
  account, which rivals the regress, self-determination theory, Wolf and
  Fischer & Ravizza; and the falsity of the PAP, which Fischer & Ravizza
  now extend.

### Added

- **Posani et al. 2026**, "Rarely categorical, highly separable
  representations along the cortical hierarchy", read as an [ADR-013](record/decisions.d/ADR-013.md) second
  reading of [ANTH-LIT-696](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-696.md). It comes with one Proposed theory: within an
  area, no neuron types, but near-total separability.

### Fixed

- **Anthology note citations.** [LIT-652](record/literature.d/LIT-652.md), [LIT-661](record/literature.d/LIT-661.md), [NOTE-532](record/notes.d/NOTE-532.md) and [NOTE-537](record/notes.d/NOTE-537.md)
  cited the anthology's notes as bare NOTE codes, which resolved to this
  record's own notes. They now read [ANTH-NOTE-131](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-131.md) and [ANTH-NOTE-116](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-116.md).
- **The ANTH remote now knows the anthology's NOTE scheme**
  (`record/notes.d`). An ANTH-NOTE code used to link into
  `literature.d`, which has no notes.
- **Collective emotions and group agency: eleven readings.**
  - **Read:** Huebner, List & Pettit 2006, List 2014, von Scheve & Ismer,
    and Barsade's manuscript.
  - **Deferred:** Gilbert, Schmid, Wimsatt, Isaacs, Sanchez-Burks & Huy,
    Ashforth & Humphrey, and Frijda 1988.
  - **Four Proposed theories:** convergence, genuinely collective emotion,
    contagion, and judgment aggregation.
- **Stray tool-call markup removed** from the ends of nineteen
  literature and note files, ten of which were already on `main`.

### Added

- **`ecology` joins the topics** ([ADR-028](record/decisions.d/ADR-028.md)).
- **Corals as composite systems: four readings, all read.**
  - Goulet et al. 2020 on the holobiont paradigm;
  - Boilard et al. 2020 on bleaching as dysbiosis;
  - Kaniewska et al. 2015 on moonlight and mass spawning;
  - Hughes et al. 2007 on herbivory and reef resilience.
- **Three Proposed theories:** bleaching as breakdown of host–symbiont
  regulation, spawning timed by the night-light regime, and reef recovery
  depending on herbivory.

### Added

- **Sources cited by an essay on organizational will**, none of which the
  record held:
  - Aubin, *Viability Theory* (1991), registered; his 1999 mini-course
    notes, read;
  - Longino, *Science as Social Knowledge* (1990) and *The Fate of
    Knowledge* (2002), registered; her SEP entry on the social dimensions
    of scientific knowledge, read;
  - Ostrom, *Governing the Commons* (1990), registered; her Nobel lecture
    on polycentric governance, read;
  - Zollman 2007, 2010 and 2013 on epistemic networks, and Rosenstock,
    Bruner & O'Connor 2017 on their robustness, read.
- **Five theories:** viability relative to a constraint set (Active);
  Longino's community norms of objectivity (Proposed); Ostrom's design
  principles of durable self-governance (Active); the Zollman effect,
  confined to hard inquiry (Proposed); transient diversity (Proposed).

### Added

- **Supplements to the essay on organizational will**, chosen against the
  draft's gaps:
  - List & Menzies 2009 on realization-insensitive causation, read;
  - Pettit, *Responsibility Incorporated* (2007), registered; his 2017
    chapter "The Conversable, Responsible Corporation", read;
  - Holling 1973 on resilience and stability, read;
  - Scheffer et al. 2001, registered; Scheffer & Carpenter 2003 on
    evidence for alternative stable states, read;
  - Rasmussen 1997 on migration toward the boundary of acceptable
    performance, read;
  - Argyris 1977 on double-loop learning, registered; his 2002 article
    "Double-Loop Learning, Teaching, and Research", read.
- **Six theories:**
  - realization-insensitive higher-level causation (Proposed);
  - corporate fitness to be held responsible (Proposed, extending
    [THEORY-127](record/theory.d/THEORY-127.md));
  - stability versus resilience (Active);
  - the standard of evidence for alternative stable states (Active);
  - drift toward the boundary (Proposed);
  - defensive routines blocking double-loop learning (Proposed).

### Added

- **The remaining readings suggested for the essay on organizational
  will.**
  - Read: French 1979, March 1991, Aktipis et al. 2015, Holman & Bruner
    2017.
  - Read in place of a closed work:
    - Woodward's SEP entry, for *Making Things Happen*;
    - the Columbia Accident Investigation Board's "History As Cause", for
      Vaughan;
    - Hirschman's "Further Reflections";
    - Beer's 1984 paper on the Viable System Model;
    - Doctorow's "Tiktok's enshittification";
    - Okasha 2022;
    - Wolf's 2013 lecture;
    - List & Pettit's Episteme replies;
    - Tollefsen 2025.
  - Each closed work is registered, as is Holman & Bruner 2015.
- **Twelve theories**, one for each read work except the List & Pettit
  replies.

### Changed

- **Fischer read first-hand.** On the owner's authorisation of Andrew M.
  Bailey's collection, Fischer's 1987 "Responsiveness and Moral
  Responsibility" ([LIT-687](record/literature.d/LIT-687.md)) is read and Active, and the Fischer & Ravizza
  précis is filed and read. [THEORY-121](record/theory.d/THEORY-121.md) now takes both as sources and is
  Active, as its promotion condition set out.

- Unread entries for Wolf, Fischer & Ravizza, *Group Agency* and *Groups
  as Agents* now record the 2026-10-05 search and the substitutes read.

### Added

- **`presupposes` joins the THEORY relations** ([ADR-029](record/decisions.d/ADR-029.md)), with the converse
  `presupposed_by`. It means one account takes another's conclusion as a
  premise for a claim about something else. It joins no chain, so it needs
  no shared topic. First uses: [THEORY-136](record/theory.d/THEORY-136.md) presupposes [THEORY-132](record/theory.d/THEORY-132.md).

### Changed

- **[THEORY-139](record/theory.d/THEORY-139.md)'s `extends: THEORY-127` is re-filed as `presupposes`.**
  Pettit's responsibility claim rests on List and Pettit's aggregation
  result without refining it.

### Changed

- **Relation audit of the THEORY scheme under [ADR-029](record/decisions.d/ADR-029.md).** Every pair of
  theories where one names the other without a declared relation (250
  pairs by a count that turned out to include five false matches) was read against the relation definitions, and so was every
  declared relation (60).
- **Seven `extends` re-filed as `presupposes`**, each an account that takes
  the other's conclusion as a premise for a claim about something else:
  [THEORY-098](record/theory.d/THEORY-098.md) on [THEORY-103](record/theory.d/THEORY-103.md), [THEORY-126](record/theory.d/THEORY-126.md) on [THEORY-055](record/theory.d/THEORY-055.md), [THEORY-079](record/theory.d/THEORY-079.md) on
  [THEORY-087](record/theory.d/THEORY-087.md), [THEORY-084](record/theory.d/THEORY-084.md) on [THEORY-086](record/theory.d/THEORY-086.md), [THEORY-051](record/theory.d/THEORY-051.md) on [THEORY-050](record/theory.d/THEORY-050.md),
  [THEORY-002](record/theory.d/THEORY-002.md) on [THEORY-004](record/theory.d/THEORY-004.md), and [THEORY-019](record/theory.d/THEORY-019.md) on [THEORY-017](record/theory.d/THEORY-017.md). [THEORY-002](record/theory.d/THEORY-002.md) gains a
  Connections section saying what it takes.
- **Four relations the prose already stated are declared.** [THEORY-077](record/theory.d/THEORY-077.md)
  presupposes [THEORY-054](record/theory.d/THEORY-054.md), [THEORY-115](record/theory.d/THEORY-115.md) presupposes [THEORY-114](record/theory.d/THEORY-114.md) and [THEORY-098](record/theory.d/THEORY-098.md)
  presupposes [THEORY-094](record/theory.d/THEORY-094.md), each of which said so (or said the equivalent)
  before the relation existed; and [THEORY-080](record/theory.d/THEORY-080.md) extends [THEORY-087](record/theory.d/THEORY-087.md), which both
  documents' Connections already said and neither frontmatter carried.
- The remaining 241 pairs stay undeclared: contrasts, parallels in other
  domains, shared sources, and cross-references, which the relations are
  not for. Five more were false matches on anthology citations.

### Added

- **Cameron, Banko & Pierce (2001), [LIT-562](record/literature.d/LIT-562.md), read** ([NOTE-587](record/notes.d/NOTE-587.md)), on
  the owner's instruction. It moves from Deferred to Active.
- **[THEORY-154](record/theory.d/THEORY-154.md)**: whether an expected tangible reward lowers or raises
  later intrinsic motivation depends on how tightly its stated contingency
  ties it to performance and success. Proposed, and declared a rival of
  cognitive evaluation theory ([THEORY-049](record/theory.d/THEORY-049.md)).
- **Eisenberger, Pierce & Cameron (1999), [LIT-754](record/literature.d/LIT-754.md), registered
  Deferred.** It is the comment that compares rewards against controls given
  the same feedback, the comparison [THEORY-049](record/theory.d/THEORY-049.md)'s refutation clause needs.
  It is closed at APA, and the entry is written from [LIT-562](record/literature.d/LIT-562.md)'s account.

### Changed

- **[THEORY-046](record/theory.d/THEORY-046.md) is Active.** Its promotion condition was this reading. The
  reply finds the same undermining by rewards offered for doing an
  interesting task (K = 57, −0.35), so both sides of the dispute find the
  effect.
- **[THEORY-049](record/theory.d/THEORY-049.md) stays Proposed**, with the reading recorded. Rewards for
  exceeding others raise free choice in the reply. That would refute the
  account, but only against a control given the same feedback, and the
  reply pools both kinds of control.
- The documents that called [LIT-562](record/literature.d/LIT-562.md) unread are updated: [LIT-556](record/literature.d/LIT-556.md), [LIT-557](record/literature.d/LIT-557.md),
  [LIT-559](record/literature.d/LIT-559.md), [NOTE-438](record/notes.d/NOTE-438.md) and [NOTE-442](record/notes.d/NOTE-442.md).

### Added

- **The design-rationale literature**, filed as cautionary evidence for
  the argument-development schemes the owner is considering. Nine works,
  registered and unread, all Deferred:
  - Kunz & Rittel 1970 (IBIS), [LIT-758](record/literature.d/LIT-758.md);
  - Conklin & Begeman 1988 (gIBIS), [LIT-762](record/literature.d/LIT-762.md);
  - MacLean et al. 1991 (QOC), [LIT-763](record/literature.d/LIT-763.md);
  - Conklin & Burgess Yakemovic 1991 (the field trial), [LIT-755](record/literature.d/LIT-755.md);
  - Grudin 1988 and 1994 on why groupware fails, [LIT-759](record/literature.d/LIT-759.md) and
    [LIT-757](record/literature.d/LIT-757.md);
  - Buckingham Shum & Hammond 1994, [LIT-761](record/literature.d/LIT-761.md);
  - Lee 1997, [LIT-760](record/literature.d/LIT-760.md);
  - Shipman & Marshall 1999, [LIT-756](record/literature.d/LIT-756.md).
- **`design-rationale` joins the topics** ([ADR-030](record/decisions.d/ADR-030.md)).

### Added

- **Four works cited by the owner's essay "The Organization of Will",
  registered Deferred and unread**, so the essay's argument record has
  something to point at: Fraenkel, *The Dual State* ([LIT-805](record/literature.d/LIT-805.md)); Ashby,
  *Design for a Brain* ([LIT-787](record/literature.d/LIT-787.md)); Canguilhem, *On the Normal and the
  Pathological* ([LIT-817](record/literature.d/LIT-817.md)); Craver, *Explaining the Brain*
  ([LIT-832](record/literature.d/LIT-832.md)). Each is written from secondary description.

### Added

- Five schemes for developing the record's own arguments ([ADR-032](record/decisions.d/ADR-032.md)): QUESTION,
  CLAIM (with a voice — thesis, counter, granted, disclaimed, supposed —
  beside its credence), CASE, TERM and ARG. Also a workbench journal, and
  `lines` and `works` vocabularies. THEORY gains `answers` and `supports`;
  LIT gains `supports`.
- The owner's essay exchange of 2026-10-04 to 2026-10-06 filed as a
  demonstration: 5 questions, 7 terms, 14 cases, 29 claims, 5 arguments and 5
  workbench entries.
- Chains over the record's own argument: lines of argument (`rests_on`,
  reporting a step that crosses from one line of inquiry to another),
  objections and replies (`objects_to`), and how claims and terms were revised
  (`supersedes`). Claims and questions are indexed by line of inquiry.

### Changed

- CI runs luria 0.36.0, which lets a reference name several schemes.

### Changed

- `luria.yaml` declares the relations luria used to supply on its own. luria
  now takes relation semantics only from configuration (dmarx/luria#360), so
  `luria upgrade explicit-relations` wrote them down. That added a
  `superseded_by` reference, with the old required-when-retired and
  forbidden-when-active conditions, to LIT, NOTE, THEORY, ADR, DP, QUESTION,
  CASE and ARG. It also added `active`, `retires_on` and `successor` roles
  wherever they were missing. LIT's successor may name an anthology code,
  because one already does. CLAIM and TERM kept their own declarations. The
  upgrade only adds lines, and the record renders and lints as before.
- CI runs luria 1.0.0, the release that carries the change.

### Added

- **Twenty-two works from the owner's manuscript reference list.** The other
  two works on the list were already held ([LIT-016](record/literature.d/LIT-016.md), [LIT-338](record/literature.d/LIT-338.md)). Each work was
  read where a lawful full text could be reached, on its own merits and
  without the manuscript.
  - **Read, with a NOTE, now Active:** Shannon 1948 ([LIT-764](record/literature.d/LIT-764.md)), Blackwell
    1953 ([LIT-781](record/literature.d/LIT-781.md)), Fritz 2020 ([LIT-772](record/literature.d/LIT-772.md)), Baez & Fong 2013
    ([LIT-773](record/literature.d/LIT-773.md)), Dzhafarov & Kujala 2016 ([LIT-777](record/literature.d/LIT-777.md)), GenEval
    ([LIT-782](record/literature.d/LIT-782.md)), T2I-CompBench ([LIT-783](record/literature.d/LIT-783.md)), Composable Diffusion
    ([LIT-770](record/literature.d/LIT-770.md)), conditional diffusion Schrödinger bridges ([LIT-776](record/literature.d/LIT-776.md)),
    Griffiths & Kalish 2007 ([LIT-769](record/literature.d/LIT-769.md)), Saussure ([LIT-774](record/literature.d/LIT-774.md)), and
    Du Bois 2007 ([LIT-779](record/literature.d/LIT-779.md)).
  - **Skimmed, now Active:** Kirby, Cornish & Smith 2008 ([LIT-771](record/literature.d/LIT-771.md)).
  - **Filed, not read, Deferred until a copy is supplied:** Austin
    ([LIT-785](record/literature.d/LIT-785.md)), Goffman ([LIT-780](record/literature.d/LIT-780.md)), Gutt ([LIT-784](record/literature.d/LIT-784.md)), Hofstadter
    ([LIT-766](record/literature.d/LIT-766.md)), Lévi-Strauss ([LIT-775](record/literature.d/LIT-775.md)), Bartlett ([LIT-768](record/literature.d/LIT-768.md)),
    Cover & Thomas ([LIT-765](record/literature.d/LIT-765.md)), Torgersen ([LIT-778](record/literature.d/LIT-778.md)), and Wyner & Ziv
    ([LIT-767](record/literature.d/LIT-767.md)).
- **Five Proposed THEORY documents:** comparison of experiments
  ([THEORY-156](record/theory.d/THEORY-156.md)), sufficiency theorems in Markov categories
  ([THEORY-157](record/theory.d/THEORY-157.md)), a Noether theorem for Markov processes
  ([THEORY-158](record/theory.d/THEORY-158.md)), linguistic value ([THEORY-159](record/theory.d/THEORY-159.md)), and iterated
  learning converging to the prior ([THEORY-155](record/theory.d/THEORY-155.md)).
- **`compositionality` and `mathematical-statistics` join the topics**
  ([ADR-031](record/decisions.d/ADR-031.md)). [LIT-667](record/literature.d/LIT-667.md), [THEORY-117](record/theory.d/THEORY-117.md), [LIT-272](record/literature.d/LIT-272.md), [LIT-273](record/literature.d/LIT-273.md) and [LIT-349](record/literature.d/LIT-349.md) are retagged.

### Changed

- [THEORY-014](record/theory.d/THEORY-014.md) gains Contextuality-by-Default as a third instance, and its
  claim is unchanged.

### Added

- **What Survives Translation?**, the owner's working manuscript, filed as a
  work (`what-survives-translation`) on a new line, `pragmatic-transport`.
  It has a title question ([QUESTION-002](record/questions.d/QUESTION-002.md)), eight Proposed theses, and
  five granted claims where the readings filed from its references cut
  against how it uses them: Saussure ([CLAIM-072](record/claims.d/CLAIM-072.md)), Contextuality-by-Default
  ([CLAIM-069](record/claims.d/CLAIM-069.md)), Baez & Fong ([CLAIM-094](record/claims.d/CLAIM-094.md)), iterated learning
  ([CLAIM-066](record/claims.d/CLAIM-066.md)) and T2I-CompBench ([CLAIM-097](record/claims.d/CLAIM-097.md)). The workbench entry of
  2026-10-09 records the session.
- **The exchange that produced it, reconstructed** from the full transcript
  (39 owner turns, every outline and draft), in seven workbench entries for
  2026-10-08. The thesis is chained through its eleven versions, from the
  owner's frame thesis to the manuscript's. Redefined terms ("frame" six
  times, "fidelity" repeatedly) are TERM chains, and the relativity and
  quantum-measurement analogies are ARGs with their undercuts. The four
  experiments are cases with their results as stated, and none of those
  results reached a later draft. Claims and questions the drafts dropped are
  recovered as Proposed, outside the work, each saying where it was last
  present and why it fell out. C7's appendices were read: Proposition 1's
  proof holds, and Proposition 2 holds as stated, though its appendix proof
  is circular.

### Added

- **The bibliography of What Survives Translation? registered.** These are
  the 46 works the manuscript dropped, plus the prior art the exchange
  conceded: Krifka 2024, the semantic-communication survey, Chai et al. and
  Zhao et al. 2025.
  - 44 new LITs: 35 read and Active, 8 filed but not read (in copyright,
    with no lawful copy), and 1 Rejected (withdrawn by its authors).
  - The 7 works already held: [LIT-264](record/literature.d/LIT-264.md) and [LIT-265](record/literature.d/LIT-265.md) now read; [LIT-277](record/literature.d/LIT-277.md) was
    already read; the other four are still unreachable.
  - 12 Proposed THEORYs.
  - The readings are noted on the claims of the manuscript's argument they
    bear on. See the curation entry of 2026-10-09.
- **`translation`** ([ADR-033](record/decisions.d/ADR-033.md)), **`pragmatics`** and **`myth-and-folklore`**
  ([ADR-034](record/decisions.d/ADR-034.md)) join the topics, and **`causality`** ([ADR-035](record/decisions.d/ADR-035.md)), which is added
  beside existing tags on every work whose subject is causation.

### Fixed

- [LIT-316](record/literature.d/LIT-316.md)'s and [LIT-344](record/literature.d/LIT-344.md)'s history entries now run oldest first.
- The links in the U1–U13 workbench entry resolve from where it renders.

### Fixed

- Four documents' `history:` entries were written newest-first ([LIT-830](record/literature.d/LIT-830.md),
  [LIT-837](record/literature.d/LIT-837.md), [TERM-008](record/terms.d/TERM-008.md), [TERM-024](record/terms.d/TERM-024.md)). The lint failed on them after the manuscript
  stack merged, so the Docs workflow failed and the site was not redeployed.
  They now run oldest-first.

### Changed

- [ADR-032](record/decisions.d/ADR-032.md), the argument-development schemes, is accepted: Proposed → Active.

### Added

- Abramsky & Sadrzadeh 2014, "Semantic Unification: A sheaf theoretic
  approach to natural language" ([LIT-841](record/literature.d/LIT-841.md)), read in full and filed at
  the owner's request. It extends [LIT-016](record/literature.d/LIT-016.md). It is noted on three claims of
  the What Survives Translation? argument: ambiguity versus contextuality
  (sharpened), objects as local sections (prior art, with a different
  emphasis), and the narrowed novelty claim.

### Added

- Two works read and filed at the owner's request:
  - Wang, Sadrzadeh, Abramsky & Cervantes 2021, "On the Quantum-like
    Contextuality of Ambiguous Phrases" ([LIT-842](record/literature.d/LIT-842.md)). Its two contextual
    systems fail its own bootstrap, and every corpus model is signalling.
  - Abramsky, Barbosa & Searle 2024, "Combining contextuality and
    causality: a game semantics approach" ([LIT-843](record/literature.d/LIT-843.md)), which becomes a
    second source for [THEORY-171](record/theory.d/THEORY-171.md).
- Both are noted on the What Survives Translation? claims they bear on:
  [CLAIM-009](record/claims.d/CLAIM-009.md), [CLAIM-037](record/claims.d/CLAIM-037.md), [CLAIM-038](record/claims.d/CLAIM-038.md) and [CLAIM-044](record/claims.d/CLAIM-044.md).

### Added

- Six works read and filed at the owner's request.
  - **The BERT contextuality study:** Lo, Sadrzadeh & Mansfield 2025
    ([LIT-844](record/literature.d/LIT-844.md)).
  - **Simulations between empirical models:**
    - Karvonen 2018 ([LIT-846](record/literature.d/LIT-846.md));
    - Abramsky, Barbosa, Karvonen & Mansfield 2019 ([LIT-847](record/literature.d/LIT-847.md));
    - Barbosa, Karvonen & Mansfield, "Closing Bell" ([LIT-845](record/literature.d/LIT-845.md)).

    A Proposed THEORY comes with them ([THEORY-174](record/theory.d/THEORY-174.md)): classical
    simulations never create contextuality.
  - **Large AI models as cultural and social technologies:** Farrell,
    Gopnik, Shalizi & Evans 2025 ([LIT-848](record/literature.d/LIT-848.md)), with a Proposed THEORY
    ([THEORY-173](record/theory.d/THEORY-173.md)).
  - **Shanahan et al., role play ([LIT-460](record/literature.d/LIT-460.md)):** already held and read, so
    only a history line was added.
- What the readings change in the What Survives Translation? argument:
  - The open problem of transport between changing covers ([CLAIM-100](record/claims.d/CLAIM-100.md)) is
    answered in part.
  - The manuscript's Propositions 1 and 2 ([CLAIM-121](record/claims.d/CLAIM-121.md), [CLAIM-070](record/claims.d/CLAIM-070.md)) are special
    cases of Karvonen 2018.

<!-- inactive-ok-file: CLAIM-100 CLAIM-125 THEORY-174 — Superseded or Proposed; cited as what this contribution changed -->
### Changed

- The open problem of transport between changing covers is narrowed, at the
  owner's request. [CLAIM-100](record/claims.d/CLAIM-100.md) is Superseded by [CLAIM-125](record/claims.d/CLAIM-125.md), which holds
  open only what the simulations literature leaves: when a cover-changing
  transport preserves decision-relevant information, and how it extends to
  signalling data. Karvonen 2018 ([LIT-846](record/literature.d/LIT-846.md)), Abramsky, Barbosa, Karvonen &
  Mansfield 2019 ([LIT-847](record/literature.d/LIT-847.md)) and "Closing Bell" ([LIT-845](record/literature.d/LIT-845.md)) are its grounds and
  its first prior art.
- The manuscript's Propositions 1 and 2 ([CLAIM-121](record/claims.d/CLAIM-121.md), [CLAIM-070](record/claims.d/CLAIM-070.md)) now name
  Karvonen 2018 ([LIT-846](record/literature.d/LIT-846.md)) and [THEORY-174](record/theory.d/THEORY-174.md) in their grounds.

<!-- inactive-ok-file: CLAIM-126 CLAIM-125 THEORY-176 THEORY-175 — Proposed; cited as what this contribution filed or bears on -->
### Added

- Two works on comparing neural representations read and filed at the
  owner's request, as candidate prior art for the pragmatic-transport line:
  - Bansal, Nakkiran & Barak 2021, "Revisiting Model Stitching to Compare
    Neural Representations" ([LIT-850](record/literature.d/LIT-850.md)), with a Proposed THEORY
    ([THEORY-176](record/theory.d/THEORY-176.md)): a task-loss stitching penalty is not Blackwell's
    order.
  - Moschella et al. 2023, "Relative representations enable zero-shot
    latent space communication" ([LIT-849](record/literature.d/LIT-849.md)), with a Proposed THEORY
    ([THEORY-175](record/theory.d/THEORY-175.md)): cosines to matched anchors are invariant exactly to
    cosine-preserving maps, and independently trained encoders agree in
    them only approximately.
- A Proposed thesis on the pragmatic-transport line ([CLAIM-126](record/claims.d/CLAIM-126.md)):
  model stitching tests the decision-relevant half of [CLAIM-125](record/claims.d/CLAIM-125.md) only in its
  reconstruction form, in one direction, within its map class.

<!-- inactive-ok-file: CLAIM-082 THEORY-175 — Proposed; cited as what this contribution changed -->
### Changed

- The structuralist premise ([CLAIM-082](record/claims.d/CLAIM-082.md)) gains a qualification from machine
  representations: relative representations ([LIT-849](record/literature.d/LIT-849.md), [THEORY-175](record/theory.d/THEORY-175.md)) carry a
  decoder between systems by relations alone, but only once anchors are
  matched by an outside correspondence, and lossily. [THEORY-175](record/theory.d/THEORY-175.md) is added to
  its grounds.

<!-- inactive-ok-file: CLAIM-125 THEORY-177 — Proposed; cited as what this contribution filed or bears on -->
### Added

- Wang, Sadrzadeh, Abramsky & Cervantes 2021, "Analysing Ambiguous Nouns
  and Verbs with Quantum Contextuality Tools" ([LIT-851](record/literature.d/LIT-851.md)), the journal
  follow-up to [LIT-842](record/literature.d/LIT-842.md), read and filed at the owner's request. A Proposed
  THEORY comes with it ([THEORY-177](record/theory.d/THEORY-177.md)): in a binary cyclic system, the
  CbD signalling measure is twice the least direct influence any canonical
  causal model must contain. The reading finds that the paper's verb–noun
  headline does not hold over all systems, and that its homonymy result
  is significant only one-sided.

### Changed

- [CLAIM-125](record/claims.d/CLAIM-125.md) gains a section and a ground: language data are typically
  signalling, so the extension of transport to signalling data is needed,
  and the paper supplies a quantity a transport could be asked to bound.
- [LIT-842](record/literature.d/LIT-842.md) now points to the follow-up as filed.

<!-- inactive-ok-file: THEORY-179 THEORY-178 — Proposed; cited as what this contribution filed -->
### Added

- Three works on persistent states in bacteria, read and filed at the
  owner's request:
  - Bhattacharyya et al. 2023, "A heritable iron memory enables
    decision-making in Escherichia coli" ([LIT-853](record/literature.d/LIT-853.md)), with a Proposed
    THEORY ([THEORY-179](record/theory.d/THEORY-179.md)): swarming potential is a short-lived inherited
    state, shared for about four generations and lost by about seven,
    tracking iron status rather than a bistable switch.
  - Zhao, Wytock, Reynolds & Motter 2024, "Irreversibility in bacterial
    regulatory networks" ([LIT-854](record/literature.d/LIT-854.md)), with a Proposed THEORY
    ([THEORY-178](record/theory.d/THEORY-178.md)): in models, a transient change to one regulator can
    leave the network in a different self-maintaining state, only through a
    gene that reaches a positive circuit. No transient-perturbation
    experiment in cells was done.
  - Van Ngo et al. 2026, "A sensor of oxidative stress confers virulence
    via response memory in Acinetobacter baumannii" ([LIT-852](record/literature.d/LIT-852.md)), an
    unrefereed bioRxiv preprint (DOI prefix 10.64898, openRxiv's). No
    THEORY: its mechanism is assembled from reporters, correlative metal
    detection and simulation.

### Fixed

- [NOTE-645](record/notes.d/NOTE-645.md) no longer calls the journal follow-up's verb-share difference
  "significant at 95%": recomputed in [NOTE-654](record/notes.d/NOTE-654.md), it is significant one-sided
  only (Welch p ≈ 0.03; two-sided ≈ 0.06), and over all signalling systems
  verbs do not carry more of Δ than nouns.

<!-- inactive-ok-file: THEORY-180 THEORY-182 THEORY-181 — Proposed; cited as what this contribution filed -->
### Added

- Five papers on the theory of trained networks, read and filed at the
  owner's request: Boncoraglio et al. on single-head attention
  ([LIT-857](record/literature.d/LIT-857.md), [THEORY-180](record/theory.d/THEORY-180.md)), Karkada et al. on word2vec dynamics
  ([LIT-855](record/literature.d/LIT-855.md), [THEORY-182](record/theory.d/THEORY-182.md)), Mainali & Teixeira on in-context
  learning dynamics ([LIT-859](record/literature.d/LIT-859.md)), Liu et al. on grokking ([LIT-858](record/literature.d/LIT-858.md),
  [THEORY-181](record/theory.d/THEORY-181.md)), and Staats, Thamm & Rosenow on small singular values
  ([LIT-856](record/literature.d/LIT-856.md), also held in the anthology as [ANTH-LIT-517](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-517.md)).

### Changed

- [ADR-002](record/decisions.d/ADR-002.md), version 2: when sources disagree on a date, or the rules leave
  first appearance open, `published:` takes the earlier date (the owner's
  ruling of 2026-10-09).

<!-- inactive-ok-file: THEORY-022 THEORY-183 THEORY-169 THEORY-182 CLAIM-082 CLAIM-118 — Proposed; cited as what this contribution filed or changed -->
### Added

- Two papers read and filed at the owner's request:
  - Yang, Poggio, Chuang & Ziyin 2025, "Topological Invariance and
    Breakdown in Learning" ([LIT-861](record/literature.d/LIT-861.md)), with a Proposed THEORY
    ([THEORY-184](record/theory.d/THEORY-184.md)): below a step-size bound, distinct neurons cannot
    merge. Its experiments show fragmentation, not the merging it predicts.
  - Karkada, Korchinski, Nava, Wyart & Bahri 2026, "Symmetry in language
    statistics shapes the geometry of model representations"
    ([LIT-860](record/literature.d/LIT-860.md)), with a Proposed THEORY ([THEORY-183](record/theory.d/THEORY-183.md)): a
    translation-invariant co-occurrence kernel puts words on its Fourier
    modes.

### Changed

- [THEORY-022](record/theory.d/THEORY-022.md), version 2: Liu et al. 2022 ([LIT-858](record/literature.d/LIT-858.md)) and Karkada et al. 2026
  ([LIT-860](record/literature.d/LIT-860.md)) join its sources; the claim is unchanged.
- [CLAIM-118](record/claims.d/CLAIM-118.md) is grounded in [LIT-859](record/literature.d/LIT-859.md) and [THEORY-169](record/theory.d/THEORY-169.md), with a section on the
  exactly solved linear-attention case.
- [CLAIM-082](record/claims.d/CLAIM-082.md) gains [THEORY-182](record/theory.d/THEORY-182.md) as a ground and a section on word-embedding
  models whose meanings are purely relational.

<!-- inactive-ok-file: THEORY-185 THEORY-186 CLAIM-082 — Proposed; cited as what this contribution filed or changed -->
### Added

- Two works [LIT-860](record/literature.d/LIT-860.md) builds on, read and filed at the owner's request:
  - Korchinski, Karkada, Bahri & Wyart 2025, "On the Emergence of Linear
    Analogies in Word Embeddings" ([LIT-863](record/literature.d/LIT-863.md)), with a Proposed THEORY
    ([THEORY-185](record/theory.d/THEORY-185.md)): independent binary attributes make the PMI
    embedding realise analogy parallelograms exactly.
  - Saxe, McClelland & Ganguli 2019, "A mathematical theory of semantic
    development in deep neural networks" ([LIT-862](record/literature.d/LIT-862.md)), with a Proposed
    THEORY ([THEORY-186](record/theory.d/THEORY-186.md)): a deep linear network learns singular modes
    one at a time, in order of strength. The stepwise picture that [LIT-855](record/literature.d/LIT-855.md)
    and [LIT-859](record/literature.d/LIT-859.md) cite comes from Saxe et al. 2014, which neither record
    holds.

### Changed

- [LIT-860](record/literature.d/LIT-860.md) records that it extends both.
- [CLAIM-082](record/claims.d/CLAIM-082.md) gains [THEORY-185](record/theory.d/THEORY-185.md) as a ground and a paragraph on the
  binary-contrast model.

<!-- inactive-ok-file: THEORY-186 THEORY-187 — Proposed; cited as what this contribution filed or changed -->
### Added

- Saxe, McClelland & Ganguli 2014, "Exact solutions to the nonlinear
  dynamics of learning in deep linear neural networks" ([LIT-864](record/literature.d/LIT-864.md)), read
  and filed at the owner's request, with a Proposed THEORY
  ([THEORY-187](record/theory.d/THEORY-187.md)) on how depth sets the learning time through each
  mode's initial strength.
- [ADR-036](record/decisions.d/ADR-036.md): `learning-theory` widens to cover training dynamics, at the
  owner's ruling.

### Changed

- [THEORY-186](record/theory.d/THEORY-186.md), version 2: the 2014 paper joins its sources as the first
  appearance of the result; the claim is unchanged.

<!-- inactive-ok-file: THEORY-185 LIT-267 CLAIM-119 QUESTION-025 — Proposed or open; cited as what this contribution changed or opened -->
### Added

- [QUESTION-025](record/questions.d/QUESTION-025.md): do correlated or hierarchical attributes in
  co-occurrence still give linear attribute directions, and a concept
  lattice that is not Boolean?

### Changed

- [THEORY-185](record/theory.d/THEORY-185.md), version 2: a Connections section on the Lattice
  Representation Hypothesis. The result derives that hypothesis's premise
  and, by the same independence, makes its lattice Boolean.
- [LIT-267](record/literature.d/LIT-267.md), version 3, and [CLAIM-119](record/claims.d/CLAIM-119.md) note the same connection and the open
  question.

<!-- inactive-ok-file: QUESTION-025 — open; cited as what this contribution changed -->
### Added

- Thirteen works on hierarchy and hyperbolic geometry, read and filed at
  the owner's request, with nine Proposed THEORY and a curation entry:
  the random hierarchy model ([LIT-877](record/literature.d/LIT-877.md)), Krioukov et al. 2010
  ([LIT-865](record/literature.d/LIT-865.md)), Sala et al. 2018 ([LIT-874](record/literature.d/LIT-874.md)), Ganea et al. 2018
  ([LIT-866](record/literature.d/LIT-866.md)), Lin et al. 2023 ([LIT-870](record/literature.d/LIT-870.md)), Yang et al. 2023
  ([LIT-871](record/literature.d/LIT-871.md)), Zhang et al. 2022 ([LIT-876](record/literature.d/LIT-876.md)), Zhou, Smith &
  Sharpee 2018 ([LIT-872](record/literature.d/LIT-872.md)), Sharpee 2019 ([LIT-875](record/literature.d/LIT-875.md)), Bianconi &
  Rahmede 2017 ([LIT-867](record/literature.d/LIT-867.md)), García-Pérez et al. 2018 ([LIT-869](record/literature.d/LIT-869.md)),
  Koch-Janusz & Ringel 2018 ([LIT-873](record/literature.d/LIT-873.md)) and Larsson et al. 2022
  ([LIT-868](record/literature.d/LIT-868.md)).

### Changed

- [QUESTION-025](record/questions.d/QUESTION-025.md) gains a section on what the record holds toward an answer.

<!-- inactive-ok-file: THEORY-194 QUESTION-025 — Proposed or open; cited as what this contribution changed -->
### Added

- Seven works cited by the hierarchy and hyperbolic-geometry batch that
  neither record held, read and filed at the owner's request, with five
  Proposed THEORY: Sclocchi, Favero & Wyart ([LIT-884](record/literature.d/LIT-884.md)), Tomasini &
  Wyart ([LIT-880](record/literature.d/LIT-880.md)) and Cagnetta & Wyart ([LIT-883](record/literature.d/LIT-883.md)), follow-ups to
  the random hierarchy model; Lenggenhager et al. 2020 ([LIT-881](record/literature.d/LIT-881.md)) and
  Gökmen et al. 2021 ([LIT-878](record/literature.d/LIT-878.md)), sequels to Koch-Janusz & Ringel;
  Mehta & Schwab 2014 ([LIT-882](record/literature.d/LIT-882.md)), the position Koch-Janusz & Ringel
  dispute; and Ganea, Bécigneul & Hofmann's Hyperbolic Neural Networks
  ([LIT-879](record/literature.d/LIT-879.md)).

### Changed

- [THEORY-194](record/theory.d/THEORY-194.md), version 2: the two sequels join its sources; the claim is
  unchanged.
- [QUESTION-025](record/questions.d/QUESTION-025.md) gains two items on what the record holds toward an answer.

<!-- inactive-ok-file: THEORY-194 THEORY-197 — Proposed; cited as what this contribution changed -->
### Added

- Five more works, read and filed at the owner's request: Gordon,
  Banerjee, Koch-Janusz & Ringel 2021 ([LIT-885](record/literature.d/LIT-885.md)), Gökmen et al. 2021
  ([LIT-889](record/literature.d/LIT-889.md)), Lin, Tegmark & Rolnick ([LIT-887](record/literature.d/LIT-887.md)), Cagnetta,
  Raventós, Ganguli & Wyart 2026 on scaling laws ([LIT-888](record/literature.d/LIT-888.md)) and
  Sclocchi, Favero, Levi & Wyart 2025 ([LIT-886](record/literature.d/LIT-886.md)), with four Proposed
  THEORY.

### Fixed

- [THEORY-197](record/theory.d/THEORY-197.md) and [NOTE-683](record/notes.d/NOTE-683.md) no longer call the free-energy point the
  reader's alone: Lin, Tegmark & Rolnick's v2 appendix makes it in
  substance, and Mehta & Schwab conceded Eq. 8's "iff" as a typo.

### Changed

- [THEORY-194](record/theory.d/THEORY-194.md), version 3: Gordon et al. and Gökmen et al. 2021 join its
  sources; [THEORY-197](record/theory.d/THEORY-197.md), version 2, adds Lin, Tegmark & Rolnick.

### Added

- Rolnick & Tegmark, "The power of deeper networks for expressing natural
  functions" (ICLR 2018; [LIT-890](record/literature.d/LIT-890.md)), the sequel to [LIT-887](record/literature.d/LIT-887.md), read and
  filed at the owner's request, with a Proposed THEORY ([THEORY-206](record/theory.d/THEORY-206.md)):
  a single hidden layer's cost grows exponentially with a monomial's
  degree in distinct variables, not with the number of inputs. The
  reading finds the paper's uniform-approximation lower bounds rest on a
  false step; only the Taylor-sense versions are established.

<!-- inactive-ok-file: THEORY-197 — Proposed; cited as what this contribution changed -->
### Added

- Schwab & Mehta, "Comment on 'Why does deep and cheap learning work so
  well?'" (arXiv 1609.03541; [LIT-891](record/literature.d/LIT-891.md)), read and filed at the owner's
  request. It concedes Eq. 8's "iff" and shows Lin & Tegmark's v1
  counterexample violates the trace condition.

### Fixed

- [LIT-887](record/literature.d/LIT-887.md) no longer calls the comment "published"; [NOTE-688](record/notes.d/NOTE-688.md) no longer
  attributes the reader's trace formula to it.

### Changed

- [THEORY-197](record/theory.d/THEORY-197.md), version 3: the comment joins its sources.

### Added

- A claim that a framing intervention indexes the empirical model, e_C^do(a), and is not one more context in its cover ([CLAIM-127](record/claims.d/CLAIM-127.md)).
- A question asking whether DisCoCat's composition constrains transport between empirical models ([QUESTION-026](record/questions.d/QUESTION-026.md)).
- A workbench entry checking a review the owner relayed against the record: which of its points were already filed, what was filed from it, and what was left to the owner and why.

### Fixed

- `source-ok` acknowledgement for [LIT-891](record/literature.d/LIT-891.md), whose arXiv title appends the identifier of the paper it comments on. This mismatch was failing `luria lint` on main.

### Added

- **The exchange behind What Survives Translation?, reconstructed for owner
  turns U40–U60** (2026-10-09 07:23 to 2026-10-10 03:26), in four workbench
  entries for 2026-10-10. With the existing entry for U42 (2026-10-09,
  23:05:42) they cover 21 owner turns. The last entry closes the
  reconstruction: the thesis end to end, the owner's one-line moves, and the
  items most worth recovering.
- **The thesis after the manuscript, filed so that its changes are visible.**
  The v7 thesis, "relational continuity under admissible transformation"
  ([CLAIM-133](record/claims.d/CLAIM-133.md), A151 and A178), is Superseded by the October thesis
  ([CLAIM-139](record/claims.d/CLAIM-139.md), A203, A214 and A218). The October thesis answers a new
  top-level question ([QUESTION-029](record/questions.d/QUESTION-029.md)) that refines [QUESTION-002](record/questions.d/QUESTION-002.md) and
  [QUESTION-021](record/questions.d/QUESTION-021.md). A granted claim records that it replaces the receiver with
  the analyst's identifiability, unargued ([CLAIM-140](record/claims.d/CLAIM-140.md)). Both later
  theses complement [CLAIM-115](record/claims.d/CLAIM-115.md), which stays the manuscript's thesis because no
  draft carries either.
- **The observational object.** The communicative object as a
  context-indexed system of empirical constraints over a cover
  ([TERM-042](record/terms.d/TERM-042.md)); a compatible family of event-sheaf sections always glues, so
  the obstruction lies in supports or distributions ([CLAIM-131](record/claims.d/CLAIM-131.md)); and the
  weighted parity triangle ([CASE-037](record/cases.d/CASE-037.md)).
- **The causal layer.** Measurement context as the elicitation protocol
  ([TERM-039](record/terms.d/TERM-039.md)); telling an interpreter, do(I = a), is not changing the
  situation, do(S = s) ([CLAIM-130](record/claims.d/CLAIM-130.md)); descriptive, causal and constitutive
  relations ([TERM-038](record/terms.d/TERM-038.md)); and which interventions tell constitutive
  relations from diagnostic ones ([QUESTION-030](record/questions.d/QUESTION-030.md)).
- **Fidelity.** Fidelity as a profile of directed distortions
  ([TERM-043](record/terms.d/TERM-043.md)), and transports whose profiles trade off are incomparable
  until a task fixes weights ([CLAIM-128](record/claims.d/CLAIM-128.md)).
- **Correspondence and the relativity analogy.** Correspondence before
  comparison ([CLAIM-143](record/claims.d/CLAIM-143.md)); the meeting-point case ([CASE-039](record/cases.d/CASE-039.md)); frames
  differ in coordinates, not in gluing ([CLAIM-144](record/claims.d/CLAIM-144.md)); causal loops and
  contextuality respond oppositely to distributions ([CLAIM-141](record/claims.d/CLAIM-141.md)); and the
  owner's argument from causality paradoxes, Rejected and undercut by both
  ([ARG-010](record/arguments.d/ARG-010.md)).
- **Restricted probes.** Observational equivalence is relative to the probes
  ([CLAIM-142](record/claims.d/CLAIM-142.md)), and when a probe family separates what a task needs
  ([QUESTION-031](record/questions.d/QUESTION-031.md)).
- **Tropes.** TV Tropes as a case ([CASE-038](record/cases.d/CASE-038.md)), a trope as a family of
  profiles around a preserved core ([CLAIM-147](record/claims.d/CLAIM-147.md)), and the record's objection
  that trope analysis is Propp's and Lévi-Strauss's and its labels are fitted
  to their examples ([CLAIM-145](record/claims.d/CLAIM-145.md)). They are tagged `translation` and
  `pragmatics` until a word for narrative tropes is decided.
- **Probes in training.** FID and Projected GANs as a case, cited by
  anthology code ([CASE-041](record/cases.d/CASE-041.md)), and a probe family that trains a
  transformation cannot also certify it ([CLAIM-149](record/claims.d/CLAIM-149.md)).
- **The ontology of U52–U56.** Partial constitution of the act by its
  relations ([CLAIM-151](record/claims.d/CLAIM-151.md)); communicative kind ([TERM-040](record/terms.d/TERM-040.md)); the owner's
  U54 position in two parts, classificatory priority of a character-like
  invariant ([CLAIM-137](record/claims.d/CLAIM-137.md)) and relata without identity beyond their relations
  ([CLAIM-136](record/claims.d/CLAIM-136.md)); character-like structural signature ([TERM-041](record/terms.d/TERM-041.md)); the
  limits of characters ([CLAIM-132](record/claims.d/CLAIM-132.md)); two objections the exchange did not
  raise, Chakravartty's dilemma ([CLAIM-134](record/claims.d/CLAIM-134.md)) and Newman as the collapse
  objection in ontology ([CLAIM-138](record/claims.d/CLAIM-138.md)); identification is not constitution
  ([CLAIM-150](record/claims.d/CLAIM-150.md)); and when a category is a real effective kind
  ([QUESTION-028](record/questions.d/QUESTION-028.md)).
- **Matrix factorization (U57–U60).** Collaborative filtering and topic
  models as a case ([CASE-042](record/cases.d/CASE-042.md)); the topic × act factorial design
  ([CASE-040](record/cases.d/CASE-040.md)); factorization gauge is not a symmetry of the data
  ([CLAIM-148](record/claims.d/CLAIM-148.md)); the owner's prior-art objection, conceded
  ([CLAIM-146](record/claims.d/CLAIM-146.md)); reconstruction, identification and constitution are three
  achievements ([CLAIM-135](record/claims.d/CLAIM-135.md)); a topic can survive a change of act
  ([CLAIM-129](record/claims.d/CLAIM-129.md)); and the signature question ([QUESTION-027](record/questions.d/QUESTION-027.md)).
- **Four works registered unread, Deferred, to ground those claims:** Pearl's
  *Causality* ([LIT-894](record/literature.d/LIT-894.md)), Serre's *Linear Representations of Finite
  Groups* ([LIT-893](record/literature.d/LIT-893.md)), Deutsch on closed timelike lines ([LIT-892](record/literature.d/LIT-892.md)) and
  Esfeld & Lam on moderate structural realism ([LIT-895](record/literature.d/LIT-895.md)). None is held in
  the anthology. A curation entry states their depth and lists the works
  cited by anthology code and the anthology candidates left there.

### Fixed

- **[CLAIM-127](record/claims.d/CLAIM-127.md) → version 2.** Its provenance was wrong. The do() move is the
  owner's, at U41, and A129 §1 and §5 formalized it before the review that
  version 1 credited. Version 1 also counted observing and conditioning as
  two operations, which in Pearl's calculus are one. The three are now A129's: conditioning on the situation,
  intervening on it, and intervening on what the interpreter is told.
- **[TERM-002](record/terms.d/TERM-002.md) is Superseded** by [TERM-042](record/terms.d/TERM-042.md). "A compatible family of local
  sections" always glues in the event sheaf, so the definition presupposed
  nothing. The supersession is carried to [CLAIM-038](record/claims.d/CLAIM-038.md) (version 2, retitled),
  [CLAIM-044](record/claims.d/CLAIM-044.md), [CASE-035](record/cases.d/CASE-035.md) and [TERM-014](record/terms.d/TERM-014.md), and `inactive-ok` annotations are
  added where [TERM-002](record/terms.d/TERM-002.md) is still cited.
- **Workbench 2026/10/09/230542 gains a dated correction line.** The
  "Pearl-inspired refinement" it could not find is U41 and A129; the
  principle it called a first appearance was drafted at A129 §4; and [LIT-841](record/literature.d/LIT-841.md)
  and [LIT-843](record/literature.d/LIT-843.md) were recommended at A129 before [#99](https://github.com/dmarx/nucleation/issues/99) and [#100](https://github.com/dmarx/nucleation/issues/100) filed them.
- **[TERM-026](record/terms.d/TERM-026.md), [TERM-031](record/terms.d/TERM-031.md) and [TERM-033](record/terms.d/TERM-033.md) are Active with `superseded_by` set**,
  and nothing said why. Each now has a section saying which sense survives
  and where. Their statuses are unchanged. A relation for "split off, old
  sense still in force" would be a design change, and is left to the owner.

### Changed

- **[TERM-043](record/terms.d/TERM-043.md) supersedes [TERM-010](record/terms.d/TERM-010.md)** as the foundation of fidelity. The scalar
  survives as one weighting. [TERM-015](record/terms.d/TERM-015.md) and [TERM-021](record/terms.d/TERM-021.md) stay Active as
  components.
- **Notes on where existing entries went** in U40–U60: [CLAIM-115](record/claims.d/CLAIM-115.md) (restated
  twice, and the receiver dropped), [CLAIM-078](record/claims.d/CLAIM-078.md) (recognition of the same
  communicative kind), [CLAIM-125](record/claims.d/CLAIM-125.md) (displaced without argument), [CLAIM-011](record/claims.d/CLAIM-011.md)
  (four new uses), [CLAIM-004](record/claims.d/CLAIM-004.md) (re-derived four times without citation),
  [QUESTION-021](record/questions.d/QUESTION-021.md) (three further answers), [TERM-014](record/terms.d/TERM-014.md) (equivalence relative to the
  probes), [CASE-004](record/cases.d/CASE-004.md) and [CASE-018](record/cases.d/CASE-018.md) (formalized and varied).
- **Notes that qualify existing claims:** [CLAIM-105](record/claims.d/CLAIM-105.md) (classical transports
  preserve noncontextuality, and coarse-graining can lower it), [CLAIM-103](record/claims.d/CLAIM-103.md)
  (among Markov kernels on finite sets the invertible core is the
  relabellings), [CLAIM-107](record/claims.d/CLAIM-107.md) (on a finite irreducible chain every harmonic
  function is constant), [CLAIM-005](record/claims.d/CLAIM-005.md) (an unconditional distance cannot see a
  broken input–output pairing) and [THEORY-038](record/theory.d/THEORY-038.md) (Eva 2016 recommended again,
  still unread).
- **Left to the owner, not changed:** a tag for narrative tropes; whether
  "conceptual revision requires formal reconciliation" becomes a DP, now that
  this filing is its first practice; whether to join [CLAIM-011](record/claims.d/CLAIM-011.md) and
  [CLAIM-077](record/claims.d/CLAIM-077.md); whether the October thesis supersedes [CLAIM-115](record/claims.d/CLAIM-115.md); which of
  two individuation theses the owner holds; and whether the ontology is meant
  for objects in general, which would need a line of its own.

### Added

- **Floridi's line on artificial agency, at the owner's request: six works,
  all read.** Read, each with a NOTE: the target, Floridi
  2025 on AI as agency without intelligence and the Multiple Realisability
  of Agency thesis ([LIT-897](record/literature.d/LIT-897.md), [NOTE-702](record/notes.d/NOTE-702.md)), read in full from the
  published version the owner supplied after no open copy could be
  reached; Floridi 2023, "AI as Agency Without Intelligence" on ChatGPT and
  LLMs ([LIT-896](record/literature.d/LIT-896.md), [NOTE-697](record/notes.d/NOTE-697.md)); Floridi & Sanders 2004, "On the Morality
  of Artificial Agents" ([LIT-898](record/literature.d/LIT-898.md), [NOTE-701](record/notes.d/NOTE-701.md)); and Floridi 2008, "The
  Method of Levels of Abstraction" ([LIT-900](record/literature.d/LIT-900.md), [NOTE-700](record/notes.d/NOTE-700.md)). The target
  is a taxonomy of kinds of agency, not an argument for its thesis, and
  its account is filed Proposed as [THEORY-208](record/theory.d/THEORY-208.md), rival to the
  organisational account of minimal agency ([THEORY-071](record/theory.d/THEORY-071.md)) and to the
  account of large models as social technologies ([THEORY-173](record/theory.d/THEORY-173.md)).
  The other two were registered unread and then read in full from the
  published versions the owner supplied: Floridi 2013, "Distributed
  Morality in an Information Society" ([LIT-901](record/literature.d/LIT-901.md), [NOTE-698](record/notes.d/NOTE-698.md)), and
  Floridi 2016, "Faultless responsibility" ([LIT-899](record/literature.d/LIT-899.md), [NOTE-699](record/notes.d/NOTE-699.md)),
  whose account of allocating responsibility is filed Proposed as
  [THEORY-207](record/theory.d/THEORY-207.md). None of the six is held in the anthology. A curation
  entry states the depth of each, the relations between them, and where
  the line meets the record's distributed-agency claims and
  [QUESTION-009](record/questions.d/QUESTION-009.md).

<!-- inactive-ok-file: CLAIM-244 CLAIM-206 CLAIM-258 CLAIM-115 CLAIM-139 — Proposed; the counters this contribution filed and the theses they press, cited as open -->
<!-- inactive-ok-file: CLAIM-215 CLAIM-209 CLAIM-216 CLAIM-241 CLAIM-217 CLAIM-228 CLAIM-204 CLAIM-220 CLAIM-202 — Proposed; the theses and counters filed from U61–U62 and the claims they bear on, cited as open -->
### Added

- **Thirty-four objections to the pragmatic-transport line, filed as
  CLAIMs from the record's audit of the line on 2026-10-10** (structure,
  formal and empirical lenses), each a weakness no CLAIM or QUESTION had
  stated. By role: 15 granted (Active), which concede a point that is
  elementary or checkable from the texts, and 19 counters (Proposed),
  which are open and say what would answer them. By severity: 7
  load-bearing, 22 significant and 5 minor. They fall in three groups: the
  tests of the central theses, the premises (cases, readings,
  constitution and the October thesis), and the formal and measurement
  structure. The load-bearing ones:
  - [CLAIM-233](record/claims.d/CLAIM-233.md) (granted): the central defeat conditions pit the theses
    only against embedding, propositional or surface similarity, which no
    rival account holds.
  - [CLAIM-243](record/claims.d/CLAIM-243.md) (counter): read as description, [CLAIM-115](record/claims.d/CLAIM-115.md) is close to
    true by definition; read as a criterion, it is a schema until its
    decision family is fixed.
  - [CLAIM-244](record/claims.d/CLAIM-244.md) (counter): the defeat tests take one holistic,
    task-free judgement of fidelity as ground truth, though the line makes
    fidelity task- and interpreter-relative.
  - [CLAIM-206](record/claims.d/CLAIM-206.md) (counter): if a communicative kind can outrun every
    probe, human same-kind judgements can neither confirm nor defeat
    [CLAIM-139](record/claims.d/CLAIM-139.md).
  - [CLAIM-207](record/claims.d/CLAIM-207.md) (granted): the transports of Propositions 1–2 and of
    D_obs act on judgement outcomes, not texts, and for one source–target
    pair a constant kernel transports any overlap-consistent target.
  - [CLAIM-258](record/claims.d/CLAIM-258.md) (counter): Blackwell's order compares experiments about
    one parameter, and compensation and context-aware translation leave
    that case.
  - [CLAIM-225](record/claims.d/CLAIM-225.md) (counter): Blackwell's order describes an ideal
    decision-maker, and the line's claims that a rendering can improve
    access describe garblings that real receivers do better with.
- **And the record's replies to them** (workbench 2026-10-10/160148). Of the
  34: 2 refuted ([CLAIM-236](record/claims.d/CLAIM-236.md) and [CLAIM-246](record/claims.d/CLAIM-246.md), now Rejected), 7
  reconciled, 23 repaired and 2 conceded. Twelve counters that were right go
  Active as conceded; six stay Proposed with a "Where it stands" note. 22 new
  entries: 18 claims, the discriminating study [CASE-055](record/cases.d/CASE-055.md), and 3 questions.
  The revised theses [CLAIM-220](record/claims.d/CLAIM-220.md) (beside [CLAIM-115](record/claims.d/CLAIM-115.md)) and [CLAIM-204](record/claims.d/CLAIM-204.md)
  (beside [CLAIM-139](record/claims.d/CLAIM-139.md)) are proposals; adopting them is the owner's call. The
  line's distinctive contribution gets its own thesis, [CLAIM-202](record/claims.d/CLAIM-202.md).
  Thirteen existing entries are restated at version 2, with each replaced
  wording quoted in its history.
- **The interlocutor's reading of this PR (U61–U62, workbench
  2026-10-10/225718).** The owner shared a continuation in which the
  assistant read PR [#121](https://github.com/dmarx/nucleation/issues/121) and wrote a revised proposal (A232) and a
  hierarchy of six theses (A240). Nearly all of A232 was already held. New:
  the ontological thesis split out and narrowed ([CLAIM-215](record/claims.d/CLAIM-215.md)) and the
  restricted-recoverability thesis answering [QUESTION-027](record/questions.d/QUESTION-027.md)
  ([CLAIM-209](record/claims.d/CLAIM-209.md)), both Proposed; the objection that the October thesis
  makes its clauses rise or fall together ([CLAIM-216](record/claims.d/CLAIM-216.md), against
  [CLAIM-204](record/claims.d/CLAIM-204.md) and [CLAIM-139](record/claims.d/CLAIM-139.md)); competent uptake as a defeasible
  standard ([CLAIM-241](record/claims.d/CLAIM-241.md), against [CLAIM-217](record/claims.d/CLAIM-217.md), open); and a granted
  overreach in [CLAIM-228](record/claims.d/CLAIM-228.md)'s title ([CLAIM-200](record/claims.d/CLAIM-200.md)), repaired at
  version 2. Dated notes are added to [CASE-055](record/cases.d/CASE-055.md) (what A232 adds to the design)
  and [CLAIM-125](record/claims.d/CLAIM-125.md) (part 1 restored to the agenda). The assistant's
  recommendations, to supersede [CLAIM-115](record/claims.d/CLAIM-115.md) and [CLAIM-139](record/claims.d/CLAIM-139.md) and to make
  [CLAIM-202](record/claims.d/CLAIM-202.md) the principal empirical thesis, are recorded, not taken.
- **Twenty cases for the points in the argument that had none**, filed in
  the same PR at the owner's request and missing from this fragment until
  now ([DP-6](docs/design-principles.md#dp-6)). Seventeen are documented: the holy kiss ([CASE-056](record/cases.d/CASE-056.md)),
  Dolly's ты ([CASE-066](record/cases.d/CASE-066.md)), Hafez's "Shirazi Turk"
  ([CASE-072](record/cases.d/CASE-072.md)), Tatiana's letter ([CASE-059](record/cases.d/CASE-059.md)), contextuality
  tests on meaning data ([CASE-053](record/cases.d/CASE-053.md)), an order effect reversed across
  a rendering ([CASE-065](record/cases.d/CASE-065.md)), Labov's sounding sessions
  ([CASE-069](record/cases.d/CASE-069.md)), joking relationships ([CASE-054](record/cases.d/CASE-054.md)), Lindsey Stone's
  photograph ([CASE-064](record/cases.d/CASE-064.md)), "wonder-working power" ([CASE-061](record/cases.d/CASE-061.md)), the
  Kia Provo ([CASE-073](record/cases.d/CASE-073.md)), the Ace Attorney localization
  ([CASE-063](record/cases.d/CASE-063.md)), the reception of The Vegetarian ([CASE-067](record/cases.d/CASE-067.md)),
  BLEU-tied systems that differ on ты and вы ([CASE-070](record/cases.d/CASE-070.md)), metric bias
  in MBR decoding ([CASE-071](record/cases.d/CASE-071.md)), risk messages in diffusion chains
  ([CASE-068](record/cases.d/CASE-068.md)), and FactBank against stance-triangle annotation
  ([CASE-058](record/cases.d/CASE-058.md)). Three are stipulated, two on documented sources:
  simplified texts for two kinds of reader ([CASE-062](record/cases.d/CASE-062.md)), the T/V swap
  ([CASE-057](record/cases.d/CASE-057.md)), and two identical unnumbered ballots ([CASE-060](record/cases.d/CASE-060.md)).
  With the discriminating study, these are the PR's "17 documented and 4
  constructed".

### Added

- The self as a multi-agent system, connected to synchronization through
  temporal discounting, mindfulness and flow, in the will-organization
  line: [QUESTION-034](record/questions.d/QUESTION-034.md), [TERM-050](record/terms.d/TERM-050.md) (intrapersonal synchronization),
  claims [CLAIM-169](record/claims.d/CLAIM-169.md) (crossing curves make the population),
  [CLAIM-162](record/claims.d/CLAIM-162.md) (flow as synchronization), [CLAIM-156](record/claims.d/CLAIM-156.md) (mindfulness
  as suspension), the open objection [CLAIM-163](record/claims.d/CLAIM-163.md), and [CASE-051](record/cases.d/CASE-051.md)
  (the absorbed writer). All Proposed.
- Five works on flow and on mindfulness and discounting, registered unread:
  [LIT-914](record/literature.d/LIT-914.md), [LIT-912](record/literature.d/LIT-912.md), [LIT-910](record/literature.d/LIT-910.md), [LIT-906](record/literature.d/LIT-906.md), [LIT-916](record/literature.d/LIT-916.md).
- Extended self and entrainment (distributed-agency): [CLAIM-172](record/claims.d/CLAIM-172.md)
  (mutual entrainment bounds the coupled system) and its open objection
  [CLAIM-165](record/claims.d/CLAIM-165.md) (dancers: a system, not a self).
- Storage and meaning (pragmatic-transport): the owner's claim
  [CLAIM-160](record/claims.d/CLAIM-160.md) (intended meaning is fixed by the write), its open
  objection [CLAIM-171](record/claims.d/CLAIM-171.md), and three cases: the tree in the woods
  ([CASE-049](record/cases.d/CASE-049.md)), data written and never read ([CASE-043](record/cases.d/CASE-043.md)), and a
  film joke seen as a child and as an adult ([CASE-048](record/cases.d/CASE-048.md)).
- [CASE-050](record/cases.d/CASE-050.md): a corporate all-hands as a synchronization mechanism for the firm
  as a kind of self (distributed-agency).
- The owner's reply to the dancers objection, [CLAIM-175](record/claims.d/CLAIM-175.md): a dancing
  couple is one combined cognitive form on the extended-mind thesis's own
  terms. With it, [CASE-046](record/cases.d/CASE-046.md) (a partner-dancing couple), the objection
  [CLAIM-165](record/claims.d/CLAIM-165.md) narrowed to the subject sense of "self" (version 2), and
  [CLAIM-172](record/claims.d/CLAIM-172.md) restated with "combined form" for "extended self"
  (version 2).
- Readings behind the vocabulary discussion: Simon (1962), "The
  Architecture of Complexity", read ([LIT-905](record/literature.d/LIT-905.md), [NOTE-704](record/notes.d/NOTE-704.md)); and
  Kelso et al. (1984), Kugler, Kelso & Turvey (1980), Turvey (1977),
  Bernstein (1967) and Koestler (1967), registered unread ([LIT-902](record/literature.d/LIT-902.md),
  [LIT-913](record/literature.d/LIT-913.md), [LIT-904](record/literature.d/LIT-904.md), [LIT-907](record/literature.d/LIT-907.md), [LIT-908](record/literature.d/LIT-908.md)).
- Mathematics of Meaning registered as the remote MOM ([ADR-037](record/decisions.d/ADR-037.md), Proposed),
  and five of its entries dual-filed here for system boundaries:
  [CLAIM-154](record/claims.d/CLAIM-154.md) (the Occam-priced threshold, [MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md)), [CLAIM-164](record/claims.d/CLAIM-164.md)
  (the gap picks the object, [MOM-CLM-144](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-144.md)), [CLAIM-153](record/claims.d/CLAIM-153.md) (unity as a
  monodromy, [MOM-CLM-165](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-165.md)), [CLAIM-161](record/claims.d/CLAIM-161.md) (selfhood as conserved
  coherence, [MOM-CLM-153](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-153.md)) and [CLAIM-152](record/claims.d/CLAIM-152.md) (target-relativity,
  [MOM-POS-001](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/positions.d/POS-001.md)). [LIT-603](record/literature.d/LIT-603.md) and [LIT-905](record/literature.d/LIT-905.md) name their MOM twins.
- A threshold criterion for one system: [QUESTION-035](record/questions.d/QUESTION-035.md), the proposed
  answer [CLAIM-157](record/claims.d/CLAIM-157.md) (a nearly decomposable block whose gap beats its
  Occam factor, relative to a target), the open objection [CLAIM-173](record/claims.d/CLAIM-173.md)
  (strength is not direction; one-way drive passes) and a stipulated
  motion-capture study of the dancing couple, [CASE-045](record/cases.d/CASE-045.md).
- One-way drive passes: the owner's challenge, filed as [CLAIM-167](record/claims.d/CLAIM-167.md).
  [CLAIM-173](record/claims.d/CLAIM-173.md) is Rejected. [CLAIM-172](record/claims.d/CLAIM-172.md) goes to version 3: mutual
  entrainment marks a peer architecture and is not a condition of
  membership. The threshold question and claim, and the dancing-couple
  study, are revised to match.
- The agency question as drive profiles: [QUESTION-033](record/questions.d/QUESTION-033.md), [TERM-051](record/terms.d/TERM-051.md)
  (drive profile, provisional name), the owner's [CLAIM-158](record/claims.d/CLAIM-158.md) (a
  spectrum of cross-level kinds) and [CLAIM-166](record/claims.d/CLAIM-166.md) (drive is not
  constant, and can come from below: the microbiome), [CLAIM-159](record/claims.d/CLAIM-159.md) (the
  accounts of will sit in different cells), and [CASE-047](record/cases.d/CASE-047.md). Two reviews
  were read for the microbiome example ([LIT-903](record/literature.d/LIT-903.md), [LIT-915](record/literature.d/LIT-915.md)). The
  dancing-couple study adds a drive-profile measurement.
- Agents as the jurisdiction of a will-organization: [QUESTION-032](record/questions.d/QUESTION-032.md),
  [TERM-047](record/terms.d/TERM-047.md), the owner's thesis [CLAIM-170](record/claims.d/CLAIM-170.md), the admission test
  [CLAIM-174](record/claims.d/CLAIM-174.md) (system, description, adaptation), the open circularity
  counter [CLAIM-168](record/claims.d/CLAIM-168.md) and the thermostat case [CASE-044](record/cases.d/CASE-044.md). Orseau et
  al. (2018) and Kenton et al. (2022) were read ([LIT-911](record/literature.d/LIT-911.md),
  [LIT-909](record/literature.d/LIT-909.md)), both flagged anthology-candidate.
- Willed agents and a concept pass: [CLAIM-155](record/claims.d/CLAIM-155.md) (control system, then
  agent, then willed agent, then self, nested strictly). The owner's thesis
  [CLAIM-170](record/claims.d/CLAIM-170.md), the admission test [CLAIM-174](record/claims.d/CLAIM-174.md), [TERM-047](record/terms.d/TERM-047.md) and
  [QUESTION-032](record/questions.d/QUESTION-032.md) go to version 2. New TERMs for combined form, agent,
  willed agent, the senses of self, and notation ([TERM-049](record/terms.d/TERM-049.md),
  [TERM-044](record/terms.d/TERM-044.md), [TERM-048](record/terms.d/TERM-048.md), [TERM-045](record/terms.d/TERM-045.md), [TERM-046](record/terms.d/TERM-046.md)). `uses:`
  links were swept across the day's claims. The notation term records
  that δ/ε is used in two senses, which the threshold criterion joins by
  assumption.
- Concept sweep over all claims. [TERM-045](record/terms.d/TERM-045.md) version 2 adds the
  integrated sense of "self" ([ADR-024](record/decisions.d/ADR-024.md)'s behavioral integration).
  [CLAIM-169](record/claims.d/CLAIM-169.md) and [CLAIM-172](record/claims.d/CLAIM-172.md) state their sense of "self". `uses:`
  links were added where the vocabulary carries an argument, including to
  [CLAIM-021](record/claims.d/CLAIM-021.md) and [CLAIM-122](record/claims.d/CLAIM-122.md). [TERM-044](record/terms.d/TERM-044.md) version 2 records the will
  paper's sense of "agent".
- [ADR-038](record/decisions.d/ADR-038.md) (Proposed): a concept invoked as the record defines it is cited by
  its TERM code at its first use. A word used in another's sense is left
  unlinked. `uses:` lists only the terms a claim is stated in. Applied
  across the argument schemes: 25 inline citations, 13 `uses:` entries.
- CLAIM `uses` declares `explain: cited` in `luria.yaml`, so every TERM a
  claim lists must be cited in its body. Turning it on reported 70 rows;
  each is cleared by a `[[uses::TERM-…]]` citation at the point of use or
  by a `ref::uses-file:` statement with its reason. [ADR-038](record/decisions.d/ADR-038.md) goes to
  version 2 to adopt the mechanism, and the phrase check it cannot cover
  is filed upstream as dmarx/luria#370.
- [ADR-037](record/decisions.d/ADR-037.md) (Mathematics of Meaning as the remote MOM) and [ADR-038](record/decisions.d/ADR-038.md) (citing
  a TERM where its concept is invoked) are accepted by the owner and
  Active. [TERM-051](record/terms.d/TERM-051.md) goes to version 2: the name "drive profile" is settled,
  with the alternatives it was kept over.

### Added

- The owner's manuscript *luria: nucleating an argument* as a `works` term,
  with a new line of inquiry, `nucleating-argument`. A first reading of the
  argument is filed against it: two questions, nine Proposed theses, two
  counters and a term (the owner's "crystallized argument"), among them the owner's reframing of the nucleation threshold as
  whatever triggers persistence, and a workbench entry saying where each piece was already in the
  record.
- Eight works on nucleation, polymorphism, growth instability and
  self-organization, filed unread and Deferred for that line: Dunitz &
  Bernstein 1995, Ostwald 1897, De Yoreo & Vekilov 2003, Vekilov's two
  papers of 2010, Langer 1980, Witten & Sander 1981 and Haken 1977.
- Four works on memory for that line, filed unread: Hebb 1949, Kanerva's
  *Sparse Distributed Memory* (1988) and his 1992 review, both also held in
  the anthology ([ADR-013](record/decisions.d/ADR-013.md)), and Hopfield 1982, flagged `anthology-candidate`.
- Readings of Ostwald 1897 and Vekilov's 2010 perspective, both read in
  full from lawful open copies and now Active. The takeaways they had been
  filed with, from memory, are corrected; the other six works have no open
  copy and stay unread.

- A question on the translation manuscript's line, `pragmatic-transport`:
  whether a communicative kind's symmetries can be reconstructed from its
  realizations, the Tannaka-style question A198 posed and A203 left out.

### Fixed

- [LIT-899](record/literature.d/LIT-899.md) and [LIT-901](record/literature.d/LIT-901.md) list their `history:` oldest first, so `luria lint`
  reads their current version correctly.

### Added

- Four works on stability theory for the nucleating-argument line, filed
  unread: Farrell & Ioannou 1996, "Generalized Stability Theory" Parts I and
  II; Trefethen et al. 1993, "Hydrodynamic Stability Without Eigenvalues";
  and May 1972, "Will a Large Complex System be Stable?".
- Notes on [CLAIM-185](record/claims.d/CLAIM-185.md), [CLAIM-181](record/claims.d/CLAIM-181.md), [CLAIM-186](record/claims.d/CLAIM-186.md) and [CLAIM-179](record/claims.d/CLAIM-179.md) on what viability
  and generalized stability theory say about persistence, drift and
  capture, with [THEORY-134](record/theory.d/THEORY-134.md) and the new works as grounds.

### Added

- A synthesis round from a review of the record: a narrowing of [CLAIM-154](record/claims.d/CLAIM-154.md)
  for singular candidate structures; a claim that an argument's
  persistence constraint set is fixed by decision; the first bridge between
  the `pragmatic-transport` and `nucleating-argument` lines, as a thesis
  and its counter; typed partial answers on [QUESTION-025](record/questions.d/QUESTION-025.md); new grounds on
  [CLAIM-030](record/claims.d/CLAIM-030.md), [CLAIM-183](record/claims.d/CLAIM-183.md) and [CLAIM-184](record/claims.d/CLAIM-184.md); and notes on the 18 unanswered
  transport questions listing material that may bear on them.

### Added

- A second synthesis round: tests for the persistence claims on [CLAIM-184](record/claims.d/CLAIM-184.md)
  and [CLAIM-185](record/claims.d/CLAIM-185.md); [CLAIM-177](record/claims.d/CLAIM-177.md)'s unargued thesis changes read as a case of
  [CLAIM-030](record/claims.d/CLAIM-030.md); two templates for the transport line's invariant questions,
  one answering [QUESTION-031](record/questions.d/QUESTION-031.md); grounds for the deferred ownership claim
  [CLAIM-016](record/claims.d/CLAIM-016.md); a question whether an anchor needs endorsement; a counter that
  anchoring measures cannot certify reduced drift; and three questions
  making unmarked tensions between THEORY entries explicit.

### Added

- A third synthesis round over the 138 THEORY entries that had no edge to
  any claim or question: 39 typed edges (grounds on claims, partial answers
  on questions), each with a dated note giving its caveat; a counter,
  objecting to [CLAIM-157](record/claims.d/CLAIM-157.md) and [CLAIM-174](record/claims.d/CLAIM-174.md), that a gap or coupling criterion
  cannot tell a boundary a system produces from one imposed on it; and
  prose notes on [CLAIM-003](record/claims.d/CLAIM-003.md) and [CLAIM-039](record/claims.d/CLAIM-039.md) recording THEORYs that bear
  against them.

### Added

- [CLAIM-197](record/claims.d/CLAIM-197.md), dual-filed from [MOM-CLM-088](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-088.md) under [ADR-037](record/decisions.d/ADR-037.md) and Active
  after a re-check. Sections over contexts that do not overlap always
  glue, so a sense that differs between disjoint contexts, such as "tall"
  for people and for trees, is not a gluing failure. A failure needs an
  overlap, and the cover decides.
- [CLAIM-198](record/claims.d/CLAIM-198.md) (Proposed): preference reversal is not yet disunity.
  Interests that govern a choice at disjoint times glue, and a self is
  divided only on an overlap, which the agent's self-prediction creates.
  It answers [CLAIM-163](record/claims.d/CLAIM-163.md)'s missing coupling in part.
- [CLAIM-196](record/claims.d/CLAIM-196.md) (Proposed), ported from MoM's manuscript (v1 §11.5) in
  defensible form: a person's roles in contexts that do not meet cannot
  contradict, and role conflict needs an overlap, which segregating
  audiences prevents and collapsed contexts create. With [CASE-052](record/cases.d/CASE-052.md)
  (Carmichael's two speaking styles) and boyd (2008), *Taken Out of
  Context*, read in part ([LIT-1001](record/literature.d/LIT-1001.md), [NOTE-710](record/notes.d/NOTE-710.md)).

### Changed

- [CASE-048](record/cases.d/CASE-048.md) goes to version 2: the child's and the adult's readings of
  the joke glue until memory brings them together.
- [TERM-045](record/terms.d/TERM-045.md) goes to version 3 with a seventh sense of "self": presented,
  the self a person gives to audiences. [CLAIM-196](record/claims.d/CLAIM-196.md) is stated in it.

### Added

- Notes on four tensions between THEORY entries that no relation marked:
  the connectivity of SGD's solutions ([THEORY-108](record/theory.d/THEORY-108.md), [THEORY-109](record/theory.d/THEORY-109.md)), the
  workspace account's "sustains" ([THEORY-096](record/theory.d/THEORY-096.md), [THEORY-102](record/theory.d/THEORY-102.md)), the scope of
  global availability ([THEORY-090](record/theory.d/THEORY-090.md), [THEORY-096](record/theory.d/THEORY-096.md)), and Beer's metasystem
  against Ostrom's commons ([THEORY-153](record/theory.d/THEORY-153.md), [THEORY-149](record/theory.d/THEORY-149.md)). None is declared a
  rivalry.

### Added

- Two lines of inquiry, `evidence-for-experience` and `learned-structure`
  ([ADR-039](record/decisions.d/ADR-039.md)), and 27 questions placing the THEORY entries that no claim or
  question had asked for, with six partial answers on existing questions.
  Twelve readings are left unplaced, each with its reason.

### Added

- Four works filed unread: Fricker 2007, Bandura 2001, Haggard 2017 and
  Mackenzie & Stoljar 2000, on epistemic justice, personal agency, the sense
  of agency and relational autonomy; and a question on the
  `nucleating-argument` line, whether a project memory distributes
  credibility among an argument's contributors.
- Four works on manipulation, filed unread: Noggle's SEP entry, Susser,
  Roessler & Nissenbaum 2019, Coons & Weber 2014 and Pereboom 2001; and
  two questions, on whether a will-organization can be manipulated without
  its present structure showing it, and whether an organized whole can
  manipulate when no member intends to.
- "On Targeted Manipulation and Deception when Optimizing LLMs for User
  Feedback" (Williams et al. 2024),
  from the owner's papers-feed, filed unread as a second case for the
  question on manipulation by an organized whole.

### Added

- Sixty-eight works from the owner's papers-feed, matched to the record's
  questions by embedding similarity, judged against each question and filed
  unread, with their citations checked against arXiv and Crossref.

### Fixed

- `CHANGELOG.md` now exists, with the insertion marker `luria collect`
  needs. The weekly scheduled Docs run failed in its collect step because
  the file the `fragments:` setting names had never been created.

### Changed

- PR [#121](https://github.com/dmarx/nucleation/issues/121) reconciled with the record after [#122](https://github.com/dmarx/nucleation/issues/122)–[#129](https://github.com/dmarx/nucleation/issues/129): dated notes and typed
  relations where later entries had called unassessed what [#121](https://github.com/dmarx/nucleation/issues/121) assessed,
  or left [#121](https://github.com/dmarx/nucleation/issues/121)'s cases and assessments unlinked; neutral notes on four
  opposed positions now left to the owner.

### Added

- An interlocutor's reading of PR [#121](https://github.com/dmarx/nucleation/issues/121) and its reconciliation, filed as
  advice: two counters (a strong contextual baseline for the incremental
  thesis; three operations behind a "change of cover"), a question on
  predicting unobserved compositions, three Proposed theses (intention, act
  and recognition as distinct variables; kinds as invariance hypotheses;
  accountability structure as the fidelity object of a developing argument),
  and notes on the entries it addresses.

### Added

- An interlocutor's reading of [LIT-638](record/literature.d/LIT-638.md) against [CLAIM-163](record/claims.d/CLAIM-163.md), filed as advice: a
  note on [CLAIM-163](record/claims.d/CLAIM-163.md) and two will-line questions, on whether acting as one
  needs synchronized or only coordinated interests, and on whether
  coordination is discrete switching or continuous reorganization.
- The owner's answers to both questions, as Proposed theses:
  - synchronization of interests is desirable but not necessary, as
    internal conflict shows ([CLAIM-261](record/claims.d/CLAIM-261.md));
  - coordination is discrete or continuous depending on the agent's
    constitution ([CLAIM-262](record/claims.d/CLAIM-262.md)). Its example is a new case, Twitch
    Plays Pokémon's crowd-steered navigation ([CASE-075](record/cases.d/CASE-075.md)).
- A stipulated variant, Twitch Plays Pokémon in democracy mode with the
  tally visible as votes come in ([CASE-074](record/cases.d/CASE-074.md)). The owner judges it the
  better demonstration of drift-diffusion dynamics.
- What the democracy-mode case bears on:
  - illustrates-edges to [CLAIM-158](record/claims.d/CLAIM-158.md), [CLAIM-122](record/claims.d/CLAIM-122.md) and [CLAIM-261](record/claims.d/CLAIM-261.md), and
    from the anarchy-mode case to [CLAIM-025](record/claims.d/CLAIM-025.md);
  - notes on [CLAIM-163](record/claims.d/CLAIM-163.md) and [CLAIM-198](record/claims.d/CLAIM-198.md);
  - an Open question, [QUESTION-077](record/questions.d/QUESTION-077.md), on whether agreement by coupling
    is a distinct kind of integration.

### Added

- [ADR-040](record/decisions.d/ADR-040.md): a claim may hold more than one line, and a new
  `formal-apparatus` line is held as a second value by the general results
  other lines borrow. Setting pragmatic-transport aside no longer retires
  them. Approved by the owner.
- `formal-apparatus` added to the 24 group A claims. Twenty come from
  pragmatic-transport, including [CLAIM-197](record/claims.d/CLAIM-197.md), which [CLAIM-198](record/claims.d/CLAIM-198.md) and [CLAIM-196](record/claims.d/CLAIM-196.md)
  rest on. Four come from distributed-agency: [CLAIM-152](record/claims.d/CLAIM-152.md), 154, 164 and 188.
- The 7 group B claims split. Each general content is a new
  formal-apparatus claim resting on nothing: from 056, 081, 142, 143, 149,
  193 and 126. Each original now rests on its general form. [CLAIM-189](record/claims.d/CLAIM-189.md), 190
  and 191 (nucleating-argument) re-point to the general forms. Their only
  remaining premises in pragmatic-transport are [CLAIM-034](record/claims.d/CLAIM-034.md) and [CLAIM-002](record/claims.d/CLAIM-002.md).
- Group C, decided by the owner as recommended:
  - [CLAIM-011](record/claims.d/CLAIM-011.md), 079 and 123 tagged `formal-apparatus`;
  - [CLAIM-187](record/claims.d/CLAIM-187.md) split, with its protocol for trained networks filed as the
    first learned-structure claim ([CLAIM-263](record/claims.d/CLAIM-263.md));
  - [CLAIM-059](record/claims.d/CLAIM-059.md), 213 and 237 left as they are.

### Changed

- `luria.yaml`: CLAIM's `line` field is declared `many: true`, and the
  `lines` vocabulary gains `formal-apparatus`.

### Added

- Kunin et al. (2021), *The Limiting Dynamics of SGD*, read and filed:
  [LIT-1011](record/literature.d/LIT-1011.md), [NOTE-711](record/notes.d/NOTE-711.md) and [THEORY-209](record/theory.d/THEORY-209.md). Its account: a converged
  network is not at a point and does not sample its training loss. It
  samples a modified loss in broken detailed balance, at a speed and spread
  set by the optimizer. The THEORY answers [QUESTION-069](record/questions.d/QUESTION-069.md) in part, on the
  regime. Also held in the anthology ([ANTH-LIT-454](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-454.md)), under [ADR-013](record/decisions.d/ADR-013.md).

### Added

- [LIT-970](record/literature.d/LIT-970.md) (Zhao, Walters & Yu, *Symmetry in Neural Network Parameter
  Spaces*) read and promoted to Active. The new entries are
  [NOTE-712](record/notes.d/NOTE-712.md) and [THEORY-210](record/theory.d/THEORY-210.md). The account: continuous symmetries make
  connected flat minima, and give gradient flow conserved quantities that
  SGD breaks, so the position along an orbit is set by initialization and
  optimizer. It answers [QUESTION-069](record/questions.d/QUESTION-069.md) and [QUESTION-058](record/questions.d/QUESTION-058.md) in part, and covers
  the null space that [THEORY-209](record/theory.d/THEORY-209.md) leaves out.
- [QUESTION-080](record/questions.d/QUESTION-080.md) (learned-structure, refines [QUESTION-051](record/questions.d/QUESTION-051.md)): what stays
  fixed while a converged network's parameters keep moving, and whether
  neural collapse's geometry is among it.
- A note on [THEORY-209](record/theory.d/THEORY-209.md): [THEORY-085](record/theory.d/THEORY-085.md)'s bearing on its noise assumption and
  on the scope of its isotropy test, the null-space account, and the new
  question.

### Fixed

- The CLAIM template scaffolds `line:` as a list, matching the plural
  field [ADR-040](record/decisions.d/ADR-040.md) declared, so a claim copied from the form starts in the
  contract's shape.

### Added

- The `argument` chain walks the steps an argument draws, through a new
  path pattern `argued_from` (dmarx/luria#372). An ARG's premises are its
  `rests_on` and its conclusion is its `concludes`, so no single field
  related the two claims, and a chain over `rests_on` never showed them.
  Each such step now renders under its premise, "through" the argument
  that draws it: [ARG-006](record/arguments.d/ARG-006.md), [ARG-007](record/arguments.d/ARG-007.md) and [ARG-008](record/arguments.d/ARG-008.md). A Rejected argument draws
  no step, so [ARG-004](record/arguments.d/ARG-004.md) stays off the page.

### Changed

- CI runs luria 1.1.0, which adds path patterns. It also names a chain
  step's other parents by the relation that holds them (dmarx/luria#359),
  so the dialectic page reads "also objects to" where it wrongly read
  "also extends", which was dmarx/nucleation#92. The lineage page uses the
  relation's label: "also carries further".

### Added

- Neural Mechanics (Kunin et al. 2021) read: [LIT-1013](record/literature.d/LIT-1013.md), [NOTE-713](record/notes.d/NOTE-713.md).
  Symmetries give conservation laws under gradient flow, and weight decay
  and finite steps break them.
- Ziyin, Li & Ueda, Noise Balance and Stationary Distribution of SGD,
  read: [LIT-1012](record/literature.d/LIT-1012.md), [NOTE-714](record/notes.d/NOTE-714.md), and [THEORY-211](record/theory.d/THEORY-211.md), the law of
  balance. Along a rescaling symmetry, minibatch noise drives SGD to a
  noise-balanced point at a rate set by η/S.

### Changed

- [THEORY-210](record/theory.d/THEORY-210.md), version 2: the two new readings added as sources, and the
  survey's attribution "imbalance decays exponentially with large learning
  rates" corrected, since Neural Mechanics attributes the decay to weight
  decay.
- Notes on [NOTE-712](record/notes.d/NOTE-712.md) (the survey's two reports checked against their
  sources) and on [THEORY-209](record/theory.d/THEORY-209.md). Its constant-covariance assumption is what
  freezes the symmetry directions that the law of balance moves.

### Added

- Notes linking the law of balance ([THEORY-211](record/theory.d/THEORY-211.md)) to [CLAIM-093](record/claims.d/CLAIM-093.md) (now
  grounded by it), [CLAIM-094](record/claims.d/CLAIM-094.md), [THEORY-186](record/theory.d/THEORY-186.md) and [THEORY-187](record/theory.d/THEORY-187.md), and [THEORY-108](record/theory.d/THEORY-108.md).
  [THEORY-211](record/theory.d/THEORY-211.md) now answers [QUESTION-080](record/questions.d/QUESTION-080.md) in part.
- [LIT-943](record/literature.d/LIT-943.md) (Dominé et al., *From Lazy to Rich*) read and promoted to Active:
  [NOTE-715](record/notes.d/NOTE-715.md), and [THEORY-212](record/theory.d/THEORY-212.md) (answering [QUESTION-039](record/questions.d/QUESTION-039.md) in part). Under
  gradient flow, the conserved relative scale of the layers sets the rich
  or lazy regime.
- [QUESTION-081](record/questions.d/QUESTION-081.md) (learned-structure, refining [QUESTION-039](record/questions.d/QUESTION-039.md)): does that
  regime survive SGD, whose minibatch noise drives the relative scale
  toward balance?
- Ziyin (2024), *Symmetry Induces Structure and Constraint of Learning*,
  read: [LIT-1014](record/literature.d/LIT-1014.md), [NOTE-716](record/notes.d/NOTE-716.md), and [THEORY-213](record/theory.d/THEORY-213.md) (answering
  [QUESTION-058](record/questions.d/QUESTION-058.md) in part). Mirror symmetries make symmetric subspaces
  absorbing, and weight decay and noise make them favoured. Notes on
  [THEORY-184](record/theory.d/THEORY-184.md) (its asymptotic half) and [THEORY-083](record/theory.d/THEORY-083.md) (a symmetry account of
  collapse).

### Added

- Ten works the Mathematics of Meaning survey pointed to, each filed for a
  named question:
  - boundaries: Smith & Varzi ([LIT-1024](record/literature.d/LIT-1024.md)), Casati & Varzi ([LIT-1022](record/literature.d/LIT-1022.md)),
    Weber & Varela ([LIT-1018](record/literature.d/LIT-1018.md));
  - composition and the problem of the many: van Inwagen ([LIT-1016](record/literature.d/LIT-1016.md)),
    Unger ([LIT-1020](record/literature.d/LIT-1020.md)), Lewis ([LIT-1015](record/literature.d/LIT-1015.md));
  - viability and norms: Di Paolo ([LIT-1017](record/literature.d/LIT-1017.md));
  - transport between systems of distinctions: Barwise & Seligman
    ([LIT-1019](record/literature.d/LIT-1019.md));
  - composition as coarse-graining: Gallego & Orús ([LIT-1023](record/literature.d/LIT-1023.md)), held in
    both records with [ANTH-LIT-695](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-695.md);
  - influence without deception: Kamenica & Gentzkow ([LIT-1021](record/literature.d/LIT-1021.md)).
- Six of them read in full the same day:
  - Smith & Varzi ([NOTE-721](record/notes.d/NOTE-721.md))
  - Weber & Varela ([NOTE-720](record/notes.d/NOTE-720.md))
  - Di Paolo ([NOTE-719](record/notes.d/NOTE-719.md))
  - Lewis ([NOTE-722](record/notes.d/NOTE-722.md))
  - Kamenica & Gentzkow ([NOTE-717](record/notes.d/NOTE-717.md))
  - Gallego & Orús ([NOTE-718](record/notes.d/NOTE-718.md))

  The other four stay `Deferred`: no lawful full text was found, and each
  entry records where its reader looked.

  The curation entries of 2026-10-13 17:01 and 17:34 give the reasons, what
  the readings corrected in the filings, and the follow-ups left open.

### Added

- A LIT status, `Unavailable` ("No copy reached"), for a work whose lawful
  full text was looked for and not reached. The status note says where the
  reader looked ([ADR-041](record/decisions.d/ADR-041.md)). `Deferred` now means no search is recorded.

### Changed

- 177 LITs moved from `Deferred` to `Unavailable`, because their status
  notes record a failed search. 8 of them have a lawful copy this client
  could not fetch, which the owner could clear by hand:
  - [LIT-137](record/literature.d/LIT-137.md), [LIT-171](record/literature.d/LIT-171.md), [LIT-180](record/literature.d/LIT-180.md), [LIT-181](record/literature.d/LIT-181.md)
  - [LIT-186](record/literature.d/LIT-186.md), [LIT-387](record/literature.d/LIT-387.md), [LIT-536](record/literature.d/LIT-536.md), [LIT-636](record/literature.d/LIT-636.md)

  168 LITs stay `Deferred`.

### Added

- The intention-based line of illocution, which [CLAIM-221](record/claims.d/CLAIM-221.md) and
  [QUESTION-073](record/questions.d/QUESTION-073.md) named as held nowhere in the record:
  - Grice, "Meaning" (1957), read in full: [LIT-1042](record/literature.d/LIT-1042.md), [NOTE-735](record/notes.d/NOTE-735.md).
  - Strawson, "Intention and Convention in Speech Acts" (1964), read in
    full: [LIT-1043](record/literature.d/LIT-1043.md), [NOTE-736](record/notes.d/NOTE-736.md).
  - Grice, "Logic and Conversation" (1975), read only at pp. 45–47 (the
    Cooperative Principle and the maxims): [LIT-1041](record/literature.d/LIT-1041.md) (Unavailable: no full lawful copy reached),
    [NOTE-734](record/notes.d/NOTE-734.md) (Skimmed).
  - Bach and Harnish, *Linguistic Communication and Speech Acts* (1979),
    filed unread because no lawful copy was reachable: [LIT-1040](record/literature.d/LIT-1040.md)
    (Unavailable).
- Notes of 2026-10-13 on [CLAIM-221](record/claims.d/CLAIM-221.md) and [QUESTION-073](record/questions.d/QUESTION-073.md). Strawson confirms the
  objection in substance. But his account makes uptake a condition of the
  act and lets standing enter through the content of an order's
  intention, so [CLAIM-151](record/claims.d/CLAIM-151.md)'s defeat condition still does not fire.

### Added

- A question and a thesis on polling and collective reasons. The question
  ([QUESTION-082](record/questions.d/QUESTION-082.md)) asks whose reasons a polity's decisions carry when it
  is steered by polls. The claim ([CLAIM-271](record/claims.d/CLAIM-271.md)) rests on [CLAIM-030](record/claims.d/CLAIM-030.md) and is
  grounded in [THEORY-127](record/theory.d/THEORY-127.md), [THEORY-131](record/theory.d/THEORY-131.md) and [THEORY-139](record/theory.d/THEORY-139.md). It says a collective's
  reasons need not be any member's, so aggregating conclusions, as a poll
  does, can yield verdicts the collective's own reasons do not support.

### Added

- The 2026-10-13 exchange on meaning operators and selfhood
  (chatgpt.com/share/6ace9fd9-…), filed as a workbench reconstruction of
  U1–U11.
  - Seven claims:
    - endorsement without self-allocation of authority, [CLAIM-285](record/claims.d/CLAIM-285.md);
    - its algebraic limit, granted, [CLAIM-282](record/claims.d/CLAIM-282.md);
    - emergent trust and entrenchment, [CLAIM-277](record/claims.d/CLAIM-277.md);
    - roles as policy-relative regimes, [CLAIM-279](record/claims.d/CLAIM-279.md);
    - persistent product against persistent producer, [CLAIM-280](record/claims.d/CLAIM-280.md);
    - a self-governing self as an organization governing the conditions of
      its own persistence, [CLAIM-284](record/claims.d/CLAIM-284.md);
    - the record's counter on modeller-fixed objectives, [CLAIM-288](record/claims.d/CLAIM-288.md).
  - The owner's r/place case, [CASE-079](record/cases.d/CASE-079.md).
  - A question on telling self-maintenance from self-constitution,
    [QUESTION-086](record/questions.d/QUESTION-086.md).
  - A term for endorsement between processes, [TERM-053](record/terms.d/TERM-053.md).
- Eleven of the fifteen works registered below read the same day, each with
  a NOTE and a THEORY. Four had no lawful copy reachable and are
  Unavailable.
- Fifteen works registered, at first unread: the 2026 autonomy cluster,
  four r/place studies, three Hawkes-process sources, Hoel et al. 2013 and
  Bickhard 2000.

- The manuscript "The Self as a Recursive Ecology of Meaning and
  Influence" in the `works` vocabulary (`self-as-recursive-ecology`), with
  nineteen member claims.

### Documentation

- Dated notes on [CLAIM-086](record/claims.d/CLAIM-086.md), [CASE-013](record/cases.d/CASE-013.md), [QUESTION-054](record/questions.d/QUESTION-054.md) and [QUESTION-056](record/questions.d/QUESTION-056.md), which
  the exchange re-derived without citing.

### Added

- [ADR-042](record/decisions.d/ADR-042.md): a required `kind` field on CASE, from a closed vocabulary of
  six (specimen, thought-experiment, construction, reported-study,
  proposed-study, executed-study), orthogonal to `standing`. Approved by
  the owner and applied to all 81 cases. The `stipulated` blurb is widened
  for proposed studies, and the CASE template documents the field.

### Documentation

- A curation entry triages the 167 Deferred LITs. It ranks them by their
  priority lines, the questions and theories that cite them, and how much
  the record has worked on those questions. It checks each one's open copy
  through OpenAlex and one fetch. The result is a read-next queue, a queue
  for afterwards, a low-value list, and the valuable works that wait on the
  owner for a copy. No status changed.

### Changed

- 22 LITs between [LIT-301](record/literature.d/LIT-301.md) and [LIT-366](record/literature.d/LIT-366.md) move from `Deferred` to `Unavailable`.
  Their bodies record a failed search for a lawful copy, which [ADR-041](record/decisions.d/ADR-041.md)'s
  migration missed because it read only the status notes.

### Added

- Close readings of the 19 "read next" works from the 2026-10-14 triage of
  Deferred LITs. Each gets a NOTE (18 `Read`; [LIT-945](record/literature.d/LIT-945.md) `Skimmed`, its proofs
  unread), and its LIT moves from `Deferred` to `Active` with takeaways from
  the reading. Where a seeded skim NOTE existed, it is now `Superseded` by
  the reading. Mismatches between what the record's THEORY, QUESTION and
  CLAIM entries say a paper shows and what it shows are written in each
  NOTE's "Bearing on the record". The entries themselves are not edited
  here. Read: [LIT-1007](record/literature.d/LIT-1007.md), [LIT-1002](record/literature.d/LIT-1002.md), [LIT-246](record/literature.d/LIT-246.md), [LIT-247](record/literature.d/LIT-247.md), [LIT-997](record/literature.d/LIT-997.md), [LIT-990](record/literature.d/LIT-990.md),
  [LIT-242](record/literature.d/LIT-242.md), [LIT-228](record/literature.d/LIT-228.md), [LIT-950](record/literature.d/LIT-950.md), [LIT-936](record/literature.d/LIT-936.md), [LIT-249](record/literature.d/LIT-249.md), [LIT-258](record/literature.d/LIT-258.md), [LIT-253](record/literature.d/LIT-253.md), [LIT-250](record/literature.d/LIT-250.md),
  [LIT-226](record/literature.d/LIT-226.md), [LIT-245](record/literature.d/LIT-245.md), [LIT-254](record/literature.d/LIT-254.md), [LIT-266](record/literature.d/LIT-266.md), [LIT-945](record/literature.d/LIT-945.md).

### Fixed

- The 2026-10-14 triage entry overstated [LIT-950](record/literature.d/LIT-950.md) as the identifiability half
  of [QUESTION-027](record/questions.d/QUESTION-027.md). It bears on the unrestricted, in-probe form only.

### Changed

- THEORY and QUESTION entries corrected to say what the close readings
  found: [THEORY-001](record/theory.d/THEORY-001.md), 002, 004, 005, 006, 007, 008, 009, 011, 015, 016, 018
  and 035, and [QUESTION-009](record/questions.d/QUESTION-009.md), 027, 067, 070 and 071. [THEORY-006](record/theory.d/THEORY-006.md), 007, 011
  and 015 are promoted to Active, because the readings meet every clause
  of their `promote_when`. [LIT-245](record/literature.d/LIT-245.md) is now `compared_against` [LIT-240](record/literature.d/LIT-240.md), not
  `corrects`.

### Added

- Fourteen Proposed THEORYs filed from the close readings, each held to
  what its paper establishes: from [LIT-242](record/literature.d/LIT-242.md), [LIT-249](record/literature.d/LIT-249.md), [LIT-246](record/literature.d/LIT-246.md), [LIT-247](record/literature.d/LIT-247.md),
  [LIT-245](record/literature.d/LIT-245.md), [LIT-254](record/literature.d/LIT-254.md), [LIT-250](record/literature.d/LIT-250.md), [LIT-950](record/literature.d/LIT-950.md), [LIT-936](record/literature.d/LIT-936.md), [LIT-997](record/literature.d/LIT-997.md), [LIT-990](record/literature.d/LIT-990.md), [LIT-1002](record/literature.d/LIT-1002.md),
  [LIT-1007](record/literature.d/LIT-1007.md) and [LIT-945](record/literature.d/LIT-945.md). [LIT-228](record/literature.d/LIT-228.md), [LIT-258](record/literature.d/LIT-258.md), [LIT-226](record/literature.d/LIT-226.md), [LIT-253](record/literature.d/LIT-253.md) and [LIT-266](record/literature.d/LIT-266.md) earn
  none, because existing THEORYs already hold their claims.

### Documentation

- Existing THEORYs, QUESTIONs and the read LITs now point to the new
  THEORYs filed from them. Stale `inactive-ok` directives for codes that
  became Active in this contribution are removed.

### Added

- Close readings of the second queue from the 2026-10-14 triage of
  Deferred LITs, with the Proposed THEORYs each reading supports. Each read
  LIT moves from `Deferred` to `Active` with a NOTE. Wave 1 (29 works):
  [LIT-942](record/literature.d/LIT-942.md), [LIT-946](record/literature.d/LIT-946.md), [LIT-941](record/literature.d/LIT-941.md), [LIT-952](record/literature.d/LIT-952.md), [LIT-951](record/literature.d/LIT-951.md), [LIT-940](record/literature.d/LIT-940.md), [LIT-984](record/literature.d/LIT-984.md), [LIT-954](record/literature.d/LIT-954.md),
  [LIT-971](record/literature.d/LIT-971.md), [LIT-935](record/literature.d/LIT-935.md), [LIT-976](record/literature.d/LIT-976.md), [LIT-944](record/literature.d/LIT-944.md), [LIT-968](record/literature.d/LIT-968.md), [LIT-961](record/literature.d/LIT-961.md), [LIT-987](record/literature.d/LIT-987.md), [LIT-969](record/literature.d/LIT-969.md),
  [LIT-963](record/literature.d/LIT-963.md), [LIT-938](record/literature.d/LIT-938.md), [LIT-937](record/literature.d/LIT-937.md), [LIT-972](record/literature.d/LIT-972.md), [LIT-977](record/literature.d/LIT-977.md), [LIT-978](record/literature.d/LIT-978.md), [LIT-974](record/literature.d/LIT-974.md), [LIT-994](record/literature.d/LIT-994.md),
  [LIT-985](record/literature.d/LIT-985.md), [LIT-975](record/literature.d/LIT-975.md), [LIT-981](record/literature.d/LIT-981.md), [LIT-986](record/literature.d/LIT-986.md), [LIT-995](record/literature.d/LIT-995.md).

- Wave 2 (35 works): [LIT-953](record/literature.d/LIT-953.md), [LIT-955](record/literature.d/LIT-955.md), [LIT-989](record/literature.d/LIT-989.md), [LIT-939](record/literature.d/LIT-939.md), [LIT-958](record/literature.d/LIT-958.md),
  [LIT-966](record/literature.d/LIT-966.md), [LIT-988](record/literature.d/LIT-988.md), [LIT-933](record/literature.d/LIT-933.md), [LIT-960](record/literature.d/LIT-960.md), [LIT-947](record/literature.d/LIT-947.md), [LIT-979](record/literature.d/LIT-979.md), [LIT-998](record/literature.d/LIT-998.md), [LIT-983](record/literature.d/LIT-983.md),
  [LIT-973](record/literature.d/LIT-973.md), [LIT-965](record/literature.d/LIT-965.md), [LIT-934](record/literature.d/LIT-934.md), [LIT-956](record/literature.d/LIT-956.md), [LIT-1008](record/literature.d/LIT-1008.md), [LIT-918](record/literature.d/LIT-918.md), [LIT-921](record/literature.d/LIT-921.md), [LIT-758](record/literature.d/LIT-758.md),
  [LIT-244](record/literature.d/LIT-244.md), [LIT-239](record/literature.d/LIT-239.md), [LIT-238](record/literature.d/LIT-238.md), [LIT-224](record/literature.d/LIT-224.md), [LIT-225](record/literature.d/LIT-225.md), [LIT-229](record/literature.d/LIT-229.md), [LIT-233](record/literature.d/LIT-233.md), [LIT-236](record/literature.d/LIT-236.md),
  [LIT-948](record/literature.d/LIT-948.md), [LIT-962](record/literature.d/LIT-962.md), [LIT-949](record/literature.d/LIT-949.md), [LIT-1000](record/literature.d/LIT-1000.md), [LIT-957](record/literature.d/LIT-957.md), [LIT-996](record/literature.d/LIT-996.md). Their seeded
  skim NOTEs are Superseded.

### Changed

- Existing THEORY, QUESTION and CLAIM entries corrected or extended where
  the readings found them misstating or understating a paper, among them
  [THEORY-083](record/theory.d/THEORY-083.md) (NC2 limited to balanced classes), [THEORY-102](record/theory.d/THEORY-102.md) (narrowed to
  category and object identity), [THEORY-022](record/theory.d/THEORY-022.md), [THEORY-028](record/theory.d/THEORY-028.md), [THEORY-009](record/theory.d/THEORY-009.md),
  [CLAIM-157](record/claims.d/CLAIM-157.md), [CLAIM-172](record/claims.d/CLAIM-172.md), [CLAIM-180](record/claims.d/CLAIM-180.md), and [QUESTION-039](record/questions.d/QUESTION-039.md), -042, -053 and -063.
  No question is answered and no theory changes status.

### Fixed

- The triage entry said [LIT-942](record/literature.d/LIT-942.md) and [LIT-946](record/literature.d/LIT-946.md) point opposite ways for
  [QUESTION-024](record/questions.d/QUESTION-024.md). They point the same way.

### Added

- Kornblith et al. (2021), filed at the owner's request, read, and the
  source of a Proposed THEORY: losses that tighten last-layer class
  clusters buy trained-class accuracy and lower fixed-feature transfer to
  new classes. [LIT-233](record/literature.d/LIT-233.md) and [LIT-236](record/literature.d/LIT-236.md) carry `anthology-candidate`, and
  [CLAIM-172](record/claims.d/CLAIM-172.md)'s `defeated_if` is reworded so that a complete micro model no
  longer meets it, both at the owner's request.

### Added

- Close readings of the Deferred LITs left after the second queue: the
  open-access works the argument cites, with the Proposed THEORYs each
  supports, and lawful-copy searches for the closed ones. A work with no
  lawful copy is set `Unavailable` ([ADR-041](record/decisions.d/ADR-041.md)) with the places searched.

### Changed

- Existing THEORY, QUESTION, CLAIM, CASE and NOTE entries corrected where
  the third batch's readings found them misstating a paper, among them
  [THEORY-003](record/theory.d/THEORY-003.md) (the HSIC constant), [THEORY-001](record/theory.d/THEORY-001.md), 004, 005, 007, 008, 009,
  011, 012, 013 and 015, [CLAIM-179](record/claims.d/CLAIM-179.md) and [CLAIM-186](record/claims.d/CLAIM-186.md), [QUESTION-047](record/questions.d/QUESTION-047.md), 067, 071
  and 072, and [CASE-046](record/cases.d/CASE-046.md). Stale directives naming codes now in force are
  trimmed. No question is answered and no theory changes status.

### Fixed

- [QUESTION-047](record/questions.d/QUESTION-047.md)'s summary carried a temporary code split across a line
  break ([CLAIM-192](record/claims.d/CLAIM-192.md)); it now names [CLAIM-192](record/claims.d/CLAIM-192.md).

### Changed

- The last 14 Deferred LITs are resolved: each is read or, where no lawful
  copy was reached, set `Unavailable` with the places searched ([ADR-041](record/decisions.d/ADR-041.md)).
  The four in-copyright books under the owner's book rule ([LIT-746](record/literature.d/LIT-746.md),
  [LIT-753](record/literature.d/LIT-753.md), [LIT-715](record/literature.d/LIT-715.md), [LIT-546](record/literature.d/LIT-546.md)) were searched for the first time and are now
  `Unavailable`; each is still read through its named substitute. [ADR-041](record/decisions.d/ADR-041.md)
  kept [LIT-746](record/literature.d/LIT-746.md), [LIT-753](record/literature.d/LIT-753.md) and [LIT-715](record/literature.d/LIT-715.md) Deferred only because no search was
  recorded, which no longer holds.
- The ten low-value Deferred LITs: six read (the Riesz, bra-ket and GNS
  Wikipedia pages, Adler's REU paper, a 2017 concussion review, and Chuai
  & Zhao on anger and fake news, which yields one Proposed THEORY), four
  `Unavailable`. [THEORY-004](record/theory.d/THEORY-004.md) and [THEORY-009](record/theory.d/THEORY-009.md) now cite the Riesz and GNS
  articles only for what they say. No LIT remains `Deferred`.
- Promotions at the owner's direction, after an audit of every Proposed
  THEORY's `promote_when` against the readings now held: [THEORY-003](record/theory.d/THEORY-003.md),
  [THEORY-004](record/theory.d/THEORY-004.md) and [THEORY-260](record/theory.d/THEORY-260.md) are `Active`. No other THEORY met every
  clause.
- [LIT-074](record/literature.d/LIT-074.md) (a YouTube talk): a transcript was sought by every route a
  text-only client has, and each was bot-blocked. It stays `Unavailable`
  until a transcript is supplied.

### Added

- Lawful substitutes for two unread books. For Fricker's *Epistemic
  Injustice* ([LIT-1004](record/literature.d/LIT-1004.md)): her 2003, 2006 and 2017 papers, read in full,
  and two Proposed THEORYs. For Pereboom's four-case argument ([LIT-1006](record/literature.d/LIT-1006.md)):
  Caruso's SEP entry and De Marco & Cyr (2024), read in full, and one
  Proposed THEORY. [THEORY-317](record/theory.d/THEORY-317.md), filed from Fricker's précis, now
  names the 2006 paper's generic definition ([THEORY-326](record/theory.d/THEORY-326.md)) as its
  rival; the book would settle between them.
- [CLAIM-291](record/claims.d/CLAIM-291.md): the adjoint of a square-integrable integral operator
  is the integral operator with the conjugate-transposed kernel, proved
  by Cauchy–Schwarz and Fubini. It is the step [THEORY-009](record/theory.d/THEORY-009.md) marks as the
  record's own rather than the Riesz article's, and [THEORY-009](record/theory.d/THEORY-009.md) now cites it.
- [CLAIM-290](record/claims.d/CLAIM-290.md) and [CLAIM-289](record/claims.d/CLAIM-289.md): the other two steps this PR's
  promotions call the record's own, each with its proof. The first gives
  uniqueness of a kernel's minimal realizations up to a unitary, and the
  finite case with centring that [THEORY-004](record/theory.d/THEORY-004.md) uses, including rows that do
  not span. The second carries [LIT-239](record/literature.d/LIT-239.md)'s non-stochastic strings to total
  recursive models at O(log n), for [THEORY-260](record/theory.d/THEORY-260.md). It corrects [LIT-239](record/literature.d/LIT-239.md)'s
  §VI-D threshold to n − √n − O(log n), and [NOTE-787](record/notes.d/NOTE-787.md) is annotated to
  match.

### Added

- Random projections, which the record used in three places without holding
  the theory behind them. Seven anchor works are registered, and six are
  read the same day, each with a NOTE: Johnson & Lindenstrauss, Dasgupta &
  Gupta, Achlioptas, Larsen & Nelson, Baraniuk et al. on RIP, and Donoho &
  Tanner. Dasgupta et al. on the fly's hash is `Unavailable`: its bioRxiv
  preprint refused this client. [QUESTION-120](record/questions.d/QUESTION-120.md) asks whether random
  features, the superposition compressed-sensing bound and the
  expand-and-threshold codes of SDM and the mushroom body share one
  concentration fact. The readings answer it for distances and sparse
  recovery on the side of sufficiency only. The fly's matrix is not an
  Achlioptas ensemble, and the JL lower bound does not bound superposition
  capacity.
- After main moved: the question (now v3) and the fly LIT point to Indyk
  and Motwani ([LIT-1106](record/literature.d/LIT-1106.md)), its LSH account ([THEORY-388](record/theory.d/THEORY-388.md)) and the SDM recall
  account ([THEORY-261](record/theory.d/THEORY-261.md)), which reach the expand-and-threshold thread the
  readings did not. The fly LIT is tagged `databases` ([ADR-045](record/decisions.d/ADR-045.md)).
- Four THEORY documents from the readings: random projection keeps a fixed
  set's squared distances at k of order ε⁻² ln n ([THEORY-397](record/theory.d/THEORY-397.md)); that order
  is necessary for the worst set, up to a constant ([THEORY-395](record/theory.d/THEORY-395.md)); JL
  concentration gives the RIP at k log(N/k) measurements, as a sufficient
  condition only ([THEORY-390](record/theory.d/THEORY-390.md)); and the ℓ₁ recovery transition's observed
  universality across ensembles, Proposed ([THEORY-391](record/theory.d/THEORY-391.md)). All four answer
  [QUESTION-120](record/questions.d/QUESTION-120.md).
- Johnson and Lindenstrauss's extension theorems, filed for later use:
  [THEORY-392](record/theory.d/THEORY-392.md) (√(log n) for n-point sets, with a near-matching lower
  bound in L_p) and [THEORY-398](record/theory.d/THEORY-398.md) (6D/ε into Hilbert space, 4D/ε into any
  Banach space, for separated sets).
- Four later works on dimension reduction and Lipschitz extension. Three
  are read, each with a NOTE and THEORY documents: Linial, London and
  Rabinovich (Bourgain's O(log n) embedding and the expander lower bound,
  [THEORY-394](record/theory.d/THEORY-394.md)), Lee and Naor (extension by random partitions,
  [THEORY-396](record/theory.d/THEORY-396.md) and [THEORY-400](record/theory.d/THEORY-400.md)) and Alon and Klartag (the JL lower
  bound for every ε ≥ 2/√n, and a bipartite JL lemma, [THEORY-399](record/theory.d/THEORY-399.md) and
  [THEORY-393](record/theory.d/THEORY-393.md)). Bourgain (1985) is `Unavailable` and read through
  Linial, London and Rabinovich.

### Fixed

- [NOTE-679](record/notes.d/NOTE-679.md)'s citation of a Euclidean lower bound for trees to Linial,
  London and Rabinovich is annotated as wrong; that paper contains no such
  bound.

### Changed

- After the THEORY backfill, existing documents are brought into line with it: [THEORY-034](record/theory.d/THEORY-034.md)'s title and sources corrected, rivals and presupposes edges and grounds drawn to the new accounts ([THEORY-043](record/theory.d/THEORY-043.md), -060, -071, -138, -172, [CLAIM-029](record/claims.d/CLAIM-029.md), -287), wrong key takeaways in [LIT-124](record/literature.d/LIT-124.md), [LIT-165](record/literature.d/LIT-165.md), [LIT-175](record/literature.d/LIT-175.md) and [LIT-188](record/literature.d/LIT-188.md) corrected, skim-era text in 187 read LITs marked as preceding its reading, dated notes added to 82 NOTEs now cited by a THEORY, and stale directives fixed.
- Every `inactive-ok-file` directive now names the status its cited works hold: 877 corrected (most said "Deferred" of works now Unavailable), codes now Active dropped, and 40 obsolete directives removed.

### Added

- `warrant` on CLAIM ([ADR-043](record/decisions.d/ADR-043.md), now Active): demonstrated, empirical or
  interpretive, how a claim as stated is supported, apart from status and
  role. Required on every CLAIM; all 315 are classified (87 demonstrated,
  12 empirical, 216 interpretive). Nineteen compound claims are listed in
  [ADR-043](record/decisions.d/ADR-043.md) for splitting.

### Changed

- [CLAIM-298](record/claims.d/CLAIM-298.md)'s empirical half is split off as [CLAIM-315](record/claims.d/CLAIM-315.md), on which it now
  rests.

### Added

- Thirteen THEORYs from the first half of the cognition readings: the extended mind, Turing, Putnam, Dennett, Searle, Chalmers on implementation, Aerts and Gabora's concept model, the Iowa gambling task, and five recent papers on perception, representation, fictionalism and chatbots.

### Added

- Twelve THEORYs from the second half of the cognition readings: the extended-mind dispute as three rival accounts and the coupling point they share, belief ascription, machine-table functionalism, high-level perception, Minsky's emotions and frames, Block's border between seeing and thinking, word learning and human iterated learning. Pandemonium ([LIT-427](record/literature.d/LIT-427.md)) and Singh's exposition ([LIT-444](record/literature.d/LIT-444.md)) get none, and the curation entry says why.

### Added

- Thirteen THEORYs from the complex-systems readings: individuality measures, ΦID and synergy-bias emergence, variance pooling, non-reciprocal cycles, collective intelligence and the ants-and-humans puzzle, delayed Lotka–Volterra, the marks of emergence, dissipative structures, Turing's instability and near-decomposability.

### Added

- Thirteen THEORYs from the consciousness readings (the hard problem and its illusionist rival, organisational invariance, the combination and meta-problems, IIT's ill-definedness, and others); [LIT-459](record/literature.d/LIT-459.md) and [LIT-411](record/literature.d/LIT-411.md) join [THEORY-043](record/theory.d/THEORY-043.md) and [THEORY-023](record/theory.d/THEORY-023.md) as sources.

### Fixed

- [CLAIM-056](record/claims.d/CLAIM-056.md)'s warrant is now interpretive. Its derivation is [CLAIM-267](record/claims.d/CLAIM-267.md)'s,
  and its defeat condition is empirical with no observation under it. This
  carries out the promotion audit's batch-004 decision ([ADR-047](record/decisions.d/ADR-047.md)). The
  status is unchanged.

### Changed

- Three Active claims now cite the Active entries that recent splits made
  of their grounds (promotion audit, batch 015, [ADR-047](record/decisions.d/ADR-047.md)). [CLAIM-107](record/claims.d/CLAIM-107.md) no
  longer calls [THEORY-158](record/theory.d/THEORY-158.md) Proposed. [CLAIM-148](record/claims.d/CLAIM-148.md) grounds on [THEORY-726](record/theory.d/THEORY-726.md) and
  [THEORY-721](record/theory.d/THEORY-721.md) in place of [THEORY-180](record/theory.d/THEORY-180.md) and [THEORY-017](record/theory.d/THEORY-017.md), and adds the minimizer
  step as a note. [CLAIM-164](record/claims.d/CLAIM-164.md) notes that only [THEORY-084](record/theory.d/THEORY-084.md)'s spectral identity
  is established, as [CLAIM-377](record/claims.d/CLAIM-377.md). Statuses are unchanged.

### Fixed

- [CLAIM-188](record/claims.d/CLAIM-188.md) put the singularity in the model left after a candidate is
  removed. It is in the model with the candidate, where the candidate is
  switched off. The title is restated in that form, as the conditional the
  argument supports.
- [CLAIM-193](record/claims.d/CLAIM-193.md)'s demonstrated part is [CLAIM-269](record/claims.d/CLAIM-269.md)'s, so its warrant is now
  interpretive, and the defeat disjunct the two shared is dropped from it.
- Both carry out the promotion audit's batch-003 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
  Statuses are unchanged.

### Fixed

- [CLAIM-308](record/claims.d/CLAIM-308.md) dropped its source's "deterministic". No deterministic rule
  without foresight beats twice the hindsight cost, but a randomized rule
  can in expectation. The qualifier is restored.
- [CLAIM-251](record/claims.d/CLAIM-251.md) said only changing the compatibility structure engages
  gluing. On a fixed CHSH cover, changing the response distribution alone
  can make a model contextual. The title now separates changes of
  scenario from changes of empirical model.
- Both corrections carry out the promotion audit's batch-002 decisions
  ([ADR-047](record/decisions.d/ADR-047.md)). Statuses are unchanged.

### Changed

- [THEORY-481](record/theory.d/THEORY-481.md) corrected, still Proposed. Its per-mode logistic dynamics and
  finite-context fixed point are exact in the long-context limit, and at
  finite N only for isotropic inputs. In general the modes couple at order
  1/N, because the source commutes the non-diagonal empirical covariance at
  (A71) and (A73). [NOTE-658](record/notes.d/NOTE-658.md) records the error. This carries out the
  promotion audit's batch-016 decision ([ADR-047](record/decisions.d/ADR-047.md)).

### Fixed

- [CLAIM-077](record/claims.d/CLAIM-077.md) and [CLAIM-098](record/claims.d/CLAIM-098.md) were filed as demonstrated. Their defeat
  conditions are an impossibility argument and a comparison of predictive
  power, so both are interpretive ([ADR-043](record/decisions.d/ADR-043.md)). This carries out the
  promotion audit's batch-001 decisions ([ADR-047](record/decisions.d/ADR-047.md)). Statuses are unchanged.

### Added

- Twenty-three works at the intersection of database theory and semantic
  search, twenty-one read with NOTEs and THEORYs: staleness and refresh,
  answering queries using views, semantic caching, incremental view
  maintenance, provenance, and approximate nearest-neighbour search
  including HNSW. [QUESTION-114](record/questions.d/QUESTION-114.md) and [QUESTION-105](record/questions.d/QUESTION-105.md) record what they give.
- [CLAIM-314](record/claims.d/CLAIM-314.md) objects to [CLAIM-308](record/claims.d/CLAIM-308.md): recognizing that a filed argument
  answers a new question is a search whose cost grows with what is filed.
- [CLAIM-312](record/claims.d/CLAIM-312.md) supersedes [CLAIM-306](record/claims.d/CLAIM-306.md): the medic's rule asserts operational
  unavailability, and absence needs a certificate about the unsearched
  remainder, not exhaustion ([CLAIM-311](record/claims.d/CLAIM-311.md)).
- [CLAIM-313](record/claims.d/CLAIM-313.md) objects to [CLAIM-310](record/claims.d/CLAIM-310.md): with copies, partitions coexist.

### Added

- An ecological-coexistence and feature-learning bridge for the
  distributed-agency line, from a synthesis the owner relayed on
  2026-10-18 (workbench entry of that date):
  - In symmetric resource competition, Lotka–Volterra dynamics are
    multiplicative gradient flow on a feature-selection objective,
    invasion fitness is its negative partial derivative, and uninvadable
    equilibria are its KKT points. Demonstrated and Active,
    [CLAIM-369](record/claims.d/CLAIM-369.md).
  - Two constructions:
    - [CASE-118](record/cases.d/CASE-118.md): two components, where one Gram matrix supports
      coexistence or exclusion depending on the growth rates;
    - [CASE-119](record/cases.d/CASE-119.md): three demands, pairwise compatible but not jointly,
      relieved by enlarging the attainable set.
  - Four questions:
    - feature geometry against coexistence, [QUESTION-135](record/questions.d/QUESTION-135.md);
    - recovery when rare against imposed or entrenched roles,
      [QUESTION-132](record/questions.d/QUESTION-132.md);
    - relief of structural frustration by specialization,
      [QUESTION-133](record/questions.d/QUESTION-133.md);
    - competence lost through influence-dependent training,
      [QUESTION-134](record/questions.d/QUESTION-134.md).
  - A proposed population study, [CASE-117](record/cases.d/CASE-117.md).
- Eight works on coexistence theory, ecological optimization and
  mean-field feature learning registered unread. Chizat and Bach (2018),
  [LIT-1232](record/literature.d/LIT-1232.md), is held in both records under [ADR-013](record/decisions.d/ADR-013.md), beside
  [ANTH-LIT-298](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-298.md).

- Revised before merge at the owner's review: the bridge is stated for
  abundances, not normalized authority shares, with a sign condition for
  the competitive reading; recovery is tested from a small positive start,
  and internally maintained exploration is separated from external
  reintroduction; the study matches context-conditioned participation and
  separates fixed from revisable authority rules.

### Documentation

- Dated notes on [QUESTION-083](record/questions.d/QUESTION-083.md), [CLAIM-277](record/claims.d/CLAIM-277.md) and [CLAIM-185](record/claims.d/CLAIM-185.md).

### Added

- Seventeen THEORYs from the ethics and agency readings (moral status and precaution, Sen and Rawls, parasocial ethics, rule-consequentialism, intentional action, interpretationism, agent discovery, subsumption, distributed morality), with rivals and a presupposes edge.

### Added

- The owner's thesis that a lucid agent's model is kept in touch by a loop
  of judgement and observation, in which each judgement reshapes the
  observer, and not by action and perception, [CLAIM-341](record/claims.d/CLAIM-341.md). It rests on
  the operator model's circuit ([CLAIM-297](record/claims.d/CLAIM-297.md)) and on [CLAIM-275](record/claims.d/CLAIM-275.md), and sets the
  stronger synchronic form aside as open.
- Its counters: mental action, felt fluency and structure learning already
  run the loop inside active inference, [CLAIM-337](record/claims.d/CLAIM-337.md); cut off from action,
  the loop loses one source of evidence it did not select, [CLAIM-339](record/claims.d/CLAIM-339.md).
- The answer to the second, [CLAIM-342](record/claims.d/CLAIM-342.md): what anchors such a loop is
  evidence whose arrival or scoring does not pass through the
  interpretation it tests, after [CLAIM-330](record/claims.d/CLAIM-330.md) and [CLAIM-141](record/claims.d/CLAIM-141.md).
- Locked-in syndrome as a documented case, [CASE-107](record/cases.d/CASE-107.md), and eight works
  registered unread for it and for the claims.
- The owner's thesis that the pragmatic-transport and will-organization
  lines describe one model, with a mapping of both into the operator model
  that the owner has not yet endorsed, [CLAIM-336](record/claims.d/CLAIM-336.md).
- A question on what plays the part of independent scoring in a single
  mind, with five candidates, [QUESTION-121](record/questions.d/QUESTION-121.md).
- Nine more works registered unread, for covert awareness, measurement
  effects, Pattee's epistemic cut, QBism and perceptual control theory.
- A demonstrated answer to the formal part of that question: in the
  linearized operator model, scoring committed predictions gives a
  coupling with the sign of κ′ − κ̄, so commitment before evidence is not
  by itself independent scoring, [CLAIM-340](record/claims.d/CLAIM-340.md), with its construction,
  [CASE-106](record/cases.d/CASE-106.md).
- Readings of six of the registered works (Owen et al., Monti et al.,
  Feldman & Lynch, Slovic, QBism, Pattee, Powers 1973), two marked
  Unavailable, and Powers, Clark & McFarland (1960) registered.
- Four works the owner named, on attempted out-of-body perception, goal
  and uncertainty codes, emotion maps and auditory–prefrontal loops, read
  or found Unavailable. The eight works registered at the start and
  Powers et al. (1960, both parts) were read, and Laureys et al. and
  Bauby found Unavailable. The locked-in case, both counters and the
  thesis were corrected from the readings.
- The owner's thesis that active inference's selective sampling is the
  authority space of the coupled meaning–authority model, so that the
  free-energy agent is a coupled loop without independent scoring,
  [CLAIM-338](record/claims.d/CLAIM-338.md).

### Added

- [QUESTION-131](record/questions.d/QUESTION-131.md): how structural frustration among jointly
  incompatible demands relates to operative thwarting of a constituent's
  demand, and when one can occur without the other. A replacement term
  that would have superseded [TERM-060](record/terms.d/TERM-060.md) was withdrawn before merge; the
  question records its candidate definitions as relayed proposals,
  neither adopted.

### Changed

- [CLAIM-347](record/claims.d/CLAIM-347.md): structural frustration defined as joint infeasibility,
  S ∉ 𝒦(𝒪; D), on attainable outcomes within a horizon and budget;
  improvement, maintenance and threshold demands kept apart; relief as
  strict enlargement of 𝒦 under fixed reference demands.
- [CLAIM-357](record/claims.d/CLAIM-357.md): structural infeasibility, realized violation, minimax
  suboptimality and causal governance failure kept apart; positive regret
  can hold while every requirement is met.
- [CLAIM-368](record/claims.d/CLAIM-368.md): frustration is independent of strain; the structural
  definition is [CLAIM-347](record/claims.d/CLAIM-347.md)'s.

### Documentation

- A dated note on [TERM-060](record/terms.d/TERM-060.md) records an error in it, the refinements to
  keep, and that its structural sense is defined exactly in [CLAIM-347](record/claims.d/CLAIM-347.md).
  The review entry of 2026-10-18 records the later reviews and how relayed
  reviews are attributed.

### Added

- Granger causality, which nine documents named without the record
  holding it. Five works are registered. Three are read the same day,
  each with a NOTE and a THEORY: Barnett, Barrett and Seth on the Gaussian
  equivalence with transfer entropy ([THEORY-700](record/theory.d/THEORY-700.md)), Seth on
  G-autonomy and G-emergence ([THEORY-703](record/theory.d/THEORY-703.md), Proposed), and Eichler
  and Didelez on when Granger noncausality implies no intervention effect
  ([THEORY-704](record/theory.d/THEORY-704.md)). Granger (1969) and Geweke (1982) are `Unavailable`
  and read through them.
- The record's own terms for it: [TERM-058](record/terms.d/TERM-058.md) defines Granger
  causality, [CLAIM-333](record/claims.d/CLAIM-333.md) says when it bears on interventions, with a
  counterexample to complete measurement being enough, and
  [CLAIM-334](record/claims.d/CLAIM-334.md) disclaims reading macro-to-micro Granger causation as
  downward causation.

### Changed

- [LIT-048](record/literature.d/LIT-048.md) is tagged `causality` and extends Barnett, Barrett and Seth.
  [THEORY-641](record/theory.d/THEORY-641.md) extends [THEORY-700](record/theory.d/THEORY-700.md).

### Fixed

- [NOTE-010](record/notes.d/NOTE-010.md)'s C5, "if all relevant variables are measured, Granger- and
  Pearl-type analyses coincide", is annotated as false as stated.
  [NOTE-053](record/notes.d/NOTE-053.md)'s C7 is checked against its source.

### Added

- Ten THEORYs from the linguistics, pragmatics, philosophy-of-language and myth-and-folklore readings: wordhood, lexicalism, speaker meaning, illocution, stance, informative speakers, distributional holism, scorekeeping and Lévi-Straussian transformation.

### Added

- Twenty THEORYs from the representation-learning, learning-theory and loss-landscapes readings: concept lattices, the Platonic measurements, group equivariance, sparse-autoencoder fidelity, in-context demonstrations, order and test-time training, small singular values, hyperbolic hierarchy, structural width, phase transitions, attention dynamics and mode connectivity beyond classifiers.

### Added

- The LEGO material from Mathematics of Meaning, ported at the owner's
  request, with the whole monograph read (curation entry of 2026-10-15 03:31):
  - the owner's LEGO parable, a case, [CASE-094](record/cases.d/CASE-094.md);
  - retrieval and evidence as opposed criteria for a category, Active,
    [CLAIM-307](record/claims.d/CLAIM-307.md), from [MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md), re-checked;
  - sortings conflict as arrangements, not as descriptions, Active, [CLAIM-310](record/claims.d/CLAIM-310.md),
    with the construction [CASE-095](record/cases.d/CASE-095.md); the monograph's contextuality, rebuilt on
    [MOM-CLM-137](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-137.md);
  - blow-up adds no observation, Active, [CLAIM-305](record/claims.d/CLAIM-305.md), against the monograph's
    "resolution restores identifiability";
  - the castle topic persists as no eigenmode, a construction, [CASE-097](record/cases.d/CASE-097.md);
  - the owner's smoothie line, [CASE-096](record/cases.d/CASE-096.md), and goodness against discriminability,
    Active, [CLAIM-309](record/claims.d/CLAIM-309.md);
  - "If I can't find it, it isn't there" as a default stronger than
    negation as failure, Active, [CLAIM-306](record/claims.d/CLAIM-306.md);
  - two questions: sorting as amortized search, [QUESTION-114](record/questions.d/QUESTION-114.md), refining
    [QUESTION-095](record/questions.d/QUESTION-095.md), with a survey of database physical design; and three
    criteria for naming a category, [QUESTION-113](record/questions.d/QUESTION-113.md).
- Treisman and Gelade 1980, read ([LIT-1082](record/literature.d/LIT-1082.md)); Duncan and Humphreys 1989,
  Unavailable ([LIT-1081](record/literature.d/LIT-1081.md)); Reiter 1978 and Clark 1978, read ([LIT-1088](record/literature.d/LIT-1088.md),
  [LIT-1087](record/literature.d/LIT-1087.md)).
- Four works on database physical design and amortized organization,
  registered and read for [QUESTION-114](record/questions.d/QUESTION-114.md): Finkelstein et al. 1988
  ([LIT-1084](record/literature.d/LIT-1084.md)), Yao 1981 ([LIT-1097](record/literature.d/LIT-1097.md)), Idreos et al. 2007
  ([LIT-1090](record/literature.d/LIT-1090.md)), Sleator and Tarjan 1985 ([LIT-1093](record/literature.d/LIT-1093.md)).
- [ADR-044](record/decisions.d/ADR-044.md), accepted and applied: a `corroborates` relation between
  claims, for evidence that is not a dependency, with its converse
  `corroborated_by`; first applied to [CLAIM-310](record/claims.d/CLAIM-310.md) and [CLAIM-296](record/claims.d/CLAIM-296.md).
- Harinarayan, Rajaraman and Ullman 1996 ([LIT-1094](record/literature.d/LIT-1094.md)), registered and read
  for the same question: which answers to precompute.
- [ADR-045](record/decisions.d/ADR-045.md): `databases` (Databases and data structures) joins the topics,
  on the five works above.
- Three more for the sorting question, at the owner's request: Comer 1978,
  Unavailable ([LIT-1086](record/literature.d/LIT-1086.md)); Piatetsky-Shapiro 1983, read ([LIT-1089](record/literature.d/LIT-1089.md)),
  now cited for workload-based index selection being NP-hard; Karlin,
  Manasse, Rudolph and Sleator 1988, read ([LIT-1096](record/literature.d/LIT-1096.md)), rent-or-buy.
- Chaudhuri and Narasayya 1997, read ([LIT-1083](record/literature.d/LIT-1083.md)): workload-driven index
  selection in practice.
- Bruno and Chaudhuri 2007, read ([LIT-1095](record/literature.d/LIT-1095.md)): online index tuning, the
  nearest the record has to the joint cost model; Athanassoulis et al. 2016,
  read ([LIT-1085](record/literature.d/LIT-1085.md)): the RUM conjecture.
- Gupta 1997, read ([LIT-1091](record/literature.d/LIT-1091.md)): view selection with maintenance cost,
  the follow-up the owner asked for as Harinarayan's.
- Gupta and Mumick 1999, read ([LIT-1092](record/literature.d/LIT-1092.md)): view selection under a
  maintenance-time budget; upkeep is not additive, and staleness is not
  priced.
- Gupta and Mumick 2005, read ([LIT-1080](record/literature.d/LIT-1080.md)): the journal version of both
  ICDT papers; it adds proofs, not new results.
- Thirty-one THEORYs for the readings of this contribution and of PR [#148](https://github.com/dmarx/nucleation/issues/148),
  which filed none; claims that grounded read works as bare LITs now ground
  the accounts. Errors found while drafting are corrected.
- [CLAIM-308](record/claims.d/CLAIM-308.md) objects to [CLAIM-303](record/claims.d/CLAIM-303.md) from the rent-or-buy result: where
  reuse cannot be forecast, cost-weighted recurrence is the filing criterion.

### Added

- Eighteen THEORYs from the mathematics readings: fifteen proved results stated with their conditions, `Active`, and three accounts resting on an unrefereed preprint or a skim, `Proposed`.

### Added

- Thirteen THEORYs from the twelve read metaphysics and mereology works that no THEORY cited: one Active formal result on the axioms of classical mereology ([THEORY-493](record/theory.d/THEORY-493.md)) and twelve Proposed accounts.

### Added

- Twelve THEORYs for the moral-psychology readings, which had none: morality-as-cooperation and Moral Foundations Theory as rival accounts, the puritanical-morality, partner-choice, relationship-regulation, social-intuitionist and shared-obligation accounts, and the findings each rests on. Moral Molecules ([LIT-509](record/literature.d/LIT-509.md)) and the 256-society dictionary study ([LIT-512](record/literature.d/LIT-512.md)) get none, and the curation entry says why.

### Added

- The rest of the partial-information-decomposition literature the record
  leaned on. Four works read, each with a NOTE and a THEORY: Griffith and
  Koch's synergy ([THEORY-716](record/theory.d/THEORY-716.md)), Griffith et al.'s intersection information
  ([THEORY-715](record/theory.d/THEORY-715.md)), Rauh et al.'s three-source impossibility ([THEORY-713](record/theory.d/THEORY-713.md))
  and Ince's I_ccs ([THEORY-714](record/theory.d/THEORY-714.md), Proposed).
- [CLAIM-343](record/claims.d/CLAIM-343.md): for three or more parts no ΦID redundancy function can have
  both the identity property and nonnegative atoms, so such a verdict must
  name the axiom it drops.

### Changed

- [CLAIM-335](record/claims.d/CLAIM-335.md)'s examples hold under a fourth measure, I_ccs. [THEORY-497](record/theory.d/THEORY-497.md),
  [THEORY-705](record/theory.d/THEORY-705.md), [THEORY-708](record/theory.d/THEORY-708.md), [THEORY-712](record/theory.d/THEORY-712.md), [NOTE-010](record/notes.d/NOTE-010.md), [NOTE-020](record/notes.d/NOTE-020.md), [NOTE-944](record/notes.d/NOTE-944.md) and
  [LIT-1168](record/literature.d/LIT-1168.md) cross-reference the new readings.

### Added

- Ten THEORY documents backfilled from the natural-sciences topic group's readings (six Active, four Proposed): the morality-as-cooperation lineage (Hamilton I and II, Maynard Smith and Price, Trivers, Axelrod and Hamilton, Nowak), the Eulalia impact shower, the individualized niche, REST2 convergence diagnostics, and the Belousov-Zhabotinsky oscillation.

### Added

- Fourteen THEORYs from thirteen philosophy-of-science readings, part 1 of 2 (four Active, ten Proposed).

### Added

- Eleven THEORYs for the second half of the philosophy-of-science readings (explanatory power, niche concepts, structural realism, duality, randomisation and evidence, open science, individuality, the Price equation), two Active and nine Proposed.

### Added

- The foundations of partial information decomposition, which the record's
  transfer-entropy, ΦID and emergence readings used without holding. Three
  works read, each with a NOTE and a THEORY: Williams and Beer's I_min and
  redundancy lattice ([THEORY-706](record/theory.d/THEORY-706.md)), Harder, Salge and Polani's I_red
  ([THEORY-708](record/theory.d/THEORY-708.md)) and Bertschinger et al.'s unique information
  ([THEORY-705](record/theory.d/THEORY-705.md)).

### Changed

- [CLAIM-335](record/claims.d/CLAIM-335.md)'s worked examples are checked under all three measures, with
  the same values; it is grounded in [THEORY-705](record/theory.d/THEORY-705.md) as well.
  [THEORY-712](record/theory.d/THEORY-712.md), [LIT-1176](record/literature.d/LIT-1176.md) and [NOTE-942](record/notes.d/NOTE-942.md) name the held PID paper.
- [THEORY-581](record/theory.d/THEORY-581.md), [NOTE-020](record/notes.d/NOTE-020.md) and [NOTE-010](record/notes.d/NOTE-010.md) point to the critiques of I_min;
  [NOTE-010](record/notes.d/NOTE-010.md)'s permutation example is checked under I_red.
- [NOTE-828](record/notes.d/NOTE-828.md) names the held Kraskov et al.; [LIT-1169](record/literature.d/LIT-1169.md) relates Geweke's
  split to directed information.

### Fixed

- [NOTE-320](record/notes.d/NOTE-320.md)'s "Kraskov estimator" for H(T) is the Kozachenko–Leonenko entropy
  estimator, per Saxe et al.'s own appendix.

### Added

- Eighteen THEORYs from the probabilistic-modeling, information-theory and contextuality readings that had none, with a curation entry.

### Changed

- [CLAIM-267](record/claims.d/CLAIM-267.md) (per-step errors compound through later sensitivity) and
  [CLAIM-270](record/claims.d/CLAIM-270.md) (retention and drift are different properties) are promoted
  to Active, carrying out the promotion audit's batch-001 decisions
  ([ADR-047](record/decisions.d/ADR-047.md)). [CLAIM-267](record/claims.d/CLAIM-267.md)'s indices are pinned to one map, with exact
  witnesses for each regime. [CLAIM-270](record/claims.d/CLAIM-270.md) gains two-state constructions for
  all four combinations of retention and drift.

### Changed

- [CLAIM-313](record/claims.d/CLAIM-313.md) is promoted to Active: copies let several partitions coexist,
  so bins realize one partition only when each item is stored once.
  [CLAIM-310](record/claims.d/CLAIM-310.md), the thesis it countered, now states that one-copy condition.
  This carries out the promotion audit's batch-002 decision ([ADR-047](record/decisions.d/ADR-047.md)).

### Changed

- [CLAIM-268](record/claims.d/CLAIM-268.md) (model stitching certifies an order of information only in
  its reconstruction form) is promoted to Active. The composition argument,
  the difference-of-upper-bounds step and a 1×1-stitcher construction are
  now written out, and the empirical disjunct of its defeat condition is
  restated as a proof of monotonicity.
- [CLAIM-107](record/claims.d/CLAIM-107.md) is narrowed to what it shows and promoted to Active: a
  harmonic observable's mean is invariant under Markov kernels and drifts
  by at most Σ ε_i when nearly harmonic. "Conserved" and "Noether-type"
  leave the title, as [CLAIM-094](record/claims.d/CLAIM-094.md) (granted) said they should.
- Both carry out the promotion audit's batch-003 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [QUESTION-141](record/questions.d/QUESTION-141.md): what replaces eigenfunctions for asymmetric
  self-supervised objectives, formerly [THEORY-009](record/theory.d/THEORY-009.md)'s promotion condition.
- [QUESTION-140](record/questions.d/QUESTION-140.md): how far CKA and normalized Bures similarity disagree
  in trained networks, formerly a clause of [THEORY-233](record/theory.d/THEORY-233.md)'s promotion
  condition.

### Changed

- [THEORY-009](record/theory.d/THEORY-009.md) is narrowed to the positive-pair papers, where
  self-adjointness comes from the symmetry of the positive-pair
  distribution, and promoted to Active. The title now names the family's
  other routes to self-adjointness.
- [THEORY-233](record/theory.d/THEORY-233.md) (the rank envelope between CKA and normalized Bures
  similarity) is promoted to Active, with the envelope and eqs. 27–28
  derived directly.
- Both carry out the promotion audit's batch-007 decisions ([ADR-047](record/decisions.d/ADR-047.md)), under
  the owner's rule that a checked re-derivation meets a promotion condition
  that asks for a proof.

### Added

- [QUESTION-146](record/questions.d/QUESTION-146.md): whether a positivity-preserving map exists between
  sheaf signed global sections and GPT quasiprobability representations,
  the condition formerly on [THEORY-014](record/theory.d/THEORY-014.md).
- [QUESTION-145](record/questions.d/QUESTION-145.md): whether trained models reach the exact superposition
  configurations, the condition formerly on [THEORY-021](record/theory.d/THEORY-021.md). It refines
  [QUESTION-058](record/questions.d/QUESTION-058.md).

### Changed

- [THEORY-014](record/theory.d/THEORY-014.md) is promoted to Active. Each half is a theorem proved in a work
  the record has read, and its promotion condition, which asked for a map
  between the formalisms that the title does not claim, moves to a
  QUESTION.
- [THEORY-021](record/theory.d/THEORY-021.md) is narrowed to the exact configurations of uniform
  superposition and promoted to Active, with the frame-operator algebra
  re-derived. The square antiprism is excluded until checked.
- Both carry out the promotion audit's batch-010 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [QUESTION-143](record/questions.d/QUESTION-143.md), [QUESTION-142](record/questions.d/QUESTION-142.md) and [QUESTION-144](record/questions.d/QUESTION-144.md) hold the
  unchecked parts of [THEORY-171](record/theory.d/THEORY-171.md), [THEORY-160](record/theory.d/THEORY-160.md) and [THEORY-158](record/theory.d/THEORY-158.md): Theorem 2.34's
  characterisation of when causal functions form a sheaf, Alfsen and
  Shultz's JB-algebra theorem, and the general-space form of Baez and
  Fong's equivalence.

### Changed

- [THEORY-171](record/theory.d/THEORY-171.md), [THEORY-160](record/theory.d/THEORY-160.md) and [THEORY-158](record/theory.d/THEORY-158.md) are narrowed to what is checked
  and promoted to Active, carrying out the promotion audit's batch-008
  decisions ([ADR-047](record/decisions.d/ADR-047.md)). The narrowed claims are the non-gluing of causal
  functions, the symmetry–conservation equivalence for a bracket with
  unique flows, and the finite-state equivalence. Each cites its
  re-derivation, which by the owner's rule of 2026-10-19 meets the request
  for a proof the record lacked.

### Added

- [THEORY-730](record/theory.d/THEORY-730.md), Active: for an embedding with W Wᵀ = |M*| at full rank,
  words on a periodic lattice whose positive and negative co-occurrence
  parts are each translation invariant have Fourier modes as principal
  components, in degenerate cos/sin pairs ([LIT-860](record/literature.d/LIT-860.md) Propositions 1, 3 and
  4 and Corollary 2). Split from [THEORY-183](record/theory.d/THEORY-183.md), with Proposition 1 and
  Corollary 2 re-derived.

### Changed

- [THEORY-193](record/theory.d/THEORY-193.md), Active after correction: the grown complex's 1-skeleton has
  2-thin geodesic triangles at every size and for every flavor, so its
  graph metric is Gromov hyperbolic because of the growth. The
  equal-link ideal-simplex drawing tiles H² for d = 2 with s = −1, and is
  not a tiling of H^d for d ≥ 3. The dual-tree statement is corrected for
  s = 0, 1.
- [THEORY-183](record/theory.d/THEORY-183.md) stays Proposed for its empirical account and now extends
  the new entry. These changes carry out the promotion audit's batch-011
  decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [QUESTION-149](record/questions.d/QUESTION-149.md): whether the relational linear properties reported in
  released language models lie in the subspaces that enter the logits, so
  that they are properties of the distribution. This is the trained-model
  half of the condition formerly on [THEORY-234](record/theory.d/THEORY-234.md).

### Changed

- [THEORY-234](record/theory.d/THEORY-234.md) is narrowed and promoted to Active. Its title said a
  relational property is shared across equivalent models "only when" it
  lies in the logit subspaces. Theorem 14 gives a sufficient condition, so
  the title now says "when". Theorems 5 and 14 are re-derived in a dated
  note.
- [THEORY-239](record/theory.d/THEORY-239.md) is narrowed and promoted to Active. The top-d left singular
  span attains the minimum worst-case linear-probe error, but it is not the
  unique span that does, as its title and the thesis said. A dated note
  re-derives the bound, gives the counterexample, and works a non-reversible
  three-state case. [NOTE-770](record/notes.d/NOTE-770.md), [LIT-975](record/literature.d/LIT-975.md) and [QUESTION-052](record/questions.d/QUESTION-052.md) are corrected to
  match.
- Both carry out the promotion audit's batch-012 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [QUESTION-139](record/questions.d/QUESTION-139.md): whether the one-hidden-layer ∏(rᵢ+1) lower bound
  holds for uniform approximation, and what replaces it with biases. This
  is the open half of [THEORY-206](record/theory.d/THEORY-206.md)'s former promotion condition.

### Changed

- [THEORY-247](record/theory.d/THEORY-247.md) is narrowed to the fixed-point definition of the bisimulation
  metric and promoted to Active. The identification and the
  occupancy-coupling LP are re-derived in a note, and the logical
  characterisation is marked as cited.
- [THEORY-206](record/theory.d/THEORY-206.md) is narrowed to Taylor matching at the origin, keeping the
  uniform upper bounds, and promoted to Active. The lower bound is
  re-derived in a note.
- Both carry out the promotion audit's batch-006 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [QUESTION-147](record/questions.d/QUESTION-147.md): whether symmetry-cluster stability predictions hold
  in a second system of near-identical units, formerly [THEORY-276](record/theory.d/THEORY-276.md)'s
  promotion condition.
- [QUESTION-148](record/questions.d/QUESTION-148.md): whether bilinear knowledge-graph scores admit a
  sheaf-coboundary representation, formerly part of [THEORY-299](record/theory.d/THEORY-299.md)'s
  promotion condition.

### Changed

- [THEORY-276](record/theory.d/THEORY-276.md) (symmetry orbits as synchronization clusters, and isolated
  desynchronization) is promoted to Active. The invariance is derived
  through fixed-point subspaces, and the hypothesis that the cluster's
  factor moves nothing else is made explicit.
- [THEORY-299](record/theory.d/THEORY-299.md) (knowledge-graph embeddings as sheaf 0-cochains) is narrowed:
  each triple is scored by a norm of its coboundary, and the summed score
  is the Laplacian form only in the squared-Euclidean variant. It is
  promoted to Active.
- [THEORY-301](record/theory.d/THEORY-301.md) (Procrustes against decoding distance, through the
  participation ratio) is promoted to Active, with eqs. 25–26 derived
  directly for real matrices.
- Each carries out the promotion audit's batch-013 decisions ([ADR-047](record/decisions.d/ADR-047.md)),
  under the owner's rule that a checked re-derivation meets a promotion
  condition that asks for a proof.

### Added

- [THEORY-731](record/theory.d/THEORY-731.md), Active: for softmax cross-entropy with balanced classes,
  the Gauss–Newton matrix splits exactly into four positive semidefinite
  terms, and its k-th eigenvalue is never below that of the class-centre
  term, a rank-C matrix read from a C × C Gram matrix. Split from
  [THEORY-078](record/theory.d/THEORY-078.md), with the derivation.

### Changed

- [THEORY-309](record/theory.d/THEORY-309.md) is Active: if a context is any jointly measurable set, every
  nondisturbing behaviour is realized by effects proportional to the
  identity on a one-dimensional system. The general scenario is
  re-derived in the entry.
- [THEORY-078](record/theory.d/THEORY-078.md) stays Proposed for its measured attribution and extends the
  new entry. These changes carry out the promotion audit's batch-017
  decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Changed

- [THEORY-312](record/theory.d/THEORY-312.md) is promoted to Active. The large-batch InfoNCE loss is
  −HSIC(Z,Y) plus a nonnegative log-mean-exp, and Theorem B.1's remainder
  enters with a plus sign. Both are re-derived in a dated note, which
  settles the sign question its promotion condition asked about.
- [CLAIM-123](record/claims.d/CLAIM-123.md) is promoted to Active. It was reviewed again as demonstrated
  after its correction in [#165](https://github.com/dmarx/nucleation/issues/165): score addition composes conditions
  exactly when the conditional dependence ratio does not vary with x.
- Both carry out the promotion audit's batch-014 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
  Stale inactive-ok entries naming either code are trimmed.

### Added

- [ADR-047](record/decisions.d/ADR-047.md): the promotion audit runs in small, persisted batches, ranked
  by expected yield, with decisions recorded apart from status changes.
- `record/promotion-audit/`: the audit's versioned queue with a hand-off
  block, one decision file per reviewed candidate, batch files, working
  notes, and `check.py`, which fails when the queue and the decisions
  disagree. Batch 001 reviewed five demonstrated CLAIMs. [CLAIM-267](record/claims.d/CLAIM-267.md) and
  [CLAIM-270](record/claims.d/CLAIM-270.md) are to be promoted, [CLAIM-285](record/claims.d/CLAIM-285.md) split, and [CLAIM-077](record/claims.d/CLAIM-077.md) and
  [CLAIM-098](record/claims.d/CLAIM-098.md) have misclassified warrants. No status changes here.

### Added

- [CLAIM-371](record/claims.d/CLAIM-371.md), Active: under the componentwise order on distortion
  profiles, incomparability is exactly a trade-off, and positive weights
  can rank a trade-off either way but never reverse a dominance. Split
  from [CLAIM-128](record/claims.d/CLAIM-128.md).
- [QUESTION-137](record/questions.d/QUESTION-137.md): whether human transmission chains converge to an
  independently measured prior, the empirical test formerly in
  [THEORY-155](record/theory.d/THEORY-155.md)'s promotion condition.
- The proved parts of three Proposed THEORYs, filed apart and Active:
  [THEORY-719](record/theory.d/THEORY-719.md) (spectral and NT-Logistic minimizers, from [THEORY-001](record/theory.d/THEORY-001.md)),
  [THEORY-717](record/theory.d/THEORY-717.md) (Blackwell's theorem for finite outcome spaces, from
  [THEORY-156](record/theory.d/THEORY-156.md)), and [CLAIM-370](record/claims.d/CLAIM-370.md) (the conditional-expectation operator is
  Hilbert–Schmidt exactly when χ² is finite, the record's own derivation
  from [THEORY-005](record/theory.d/THEORY-005.md), now with a proof).
- [QUESTION-136](record/questions.d/QUESTION-136.md): the population form of the readout identities,
  formerly a clause of [THEORY-008](record/theory.d/THEORY-008.md)'s promotion condition.
- [THEORY-718](record/theory.d/THEORY-718.md), Active: in linear-Gaussian models the evidence is
  exactly best fit times an Occam factor costing (k/2) log n. Split from
  [THEORY-087](record/theory.d/THEORY-087.md).

### Fixed

- [CLAIM-123](record/claims.d/CLAIM-123.md) said adding conditional scores composes conditions only under
  conditional independence. That condition is sufficient, not necessary.
  The claim now gives the exact criterion and an example of dependent
  conditions that meet it.
- [CLAIM-264](record/claims.d/CLAIM-264.md) implied that a strong generator identifies objects. It makes
  the restricted Yoneda functor conservative, which is weaker: (ℤ/p)³ and
  the Heisenberg group mod p look the same through ℤ.

### Changed

- [CLAIM-264](record/claims.d/CLAIM-264.md) and [THEORY-155](record/theory.d/THEORY-155.md) are promoted to Active. [THEORY-155](record/theory.d/THEORY-155.md)'s title now
  states the ergodicity its convergence needs.
- [CLAIM-128](record/claims.d/CLAIM-128.md) keeps only its task-relativity thesis, and its warrant is now
  interpretive.
- [THEORY-008](record/theory.d/THEORY-008.md) is confined to a finite stimulus set, where its identities
  are proved, and promoted to Active.
- [THEORY-087](record/theory.d/THEORY-087.md)'s promotion condition no longer says its regular half is
  derived in the sources. Only the linear-Gaussian case is derived there,
  and the condition now asks for a proof of the general regular case as
  well.
- [CLAIM-323](record/claims.d/CLAIM-323.md) now rests on the finite-outcome Blackwell THEORY.
  [CLAIM-237](record/claims.d/CLAIM-237.md) and [CLAIM-326](record/claims.d/CLAIM-326.md) cite it alongside [THEORY-156](record/theory.d/THEORY-156.md).

### Added

- The 2026-10-14 exchange on prompting, epistemic memory and retrieval
  (chatgpt.com/share/6ad01c63-…), filed as a workbench reconstruction of
  U1–U23.
  - Thirteen claims:
    - current conclusions are not a sufficient state for revision, Active, [CLAIM-294](record/claims.d/CLAIM-294.md);
    - sufficiency is relative to model and decisions, Active, [CLAIM-300](record/claims.d/CLAIM-300.md);
    - support topology does not fix revision, granted, [CLAIM-293](record/claims.d/CLAIM-293.md);
    - what keeping justifications can buy, [CLAIM-295](record/claims.d/CLAIM-295.md);
    - sufficiency, accountability and correctness come apart, Active, [CLAIM-299](record/claims.d/CLAIM-299.md);
    - filing moves work across time, [CLAIM-303](record/claims.d/CLAIM-303.md);
    - feasible tests can be far coarser than statistical ones, Active and
      conditional, [CLAIM-302](record/claims.d/CLAIM-302.md), and a rendering can keep a distinction and make it
      infeasible to recover, [CLAIM-304](record/claims.d/CLAIM-304.md);
    - possession, knowledge and deployability differ, [CLAIM-296](record/claims.d/CLAIM-296.md);
    - a frame can act on what is reachable, [CLAIM-298](record/claims.d/CLAIM-298.md);
    - iterative retrieval can turn a guess into a premise, [CLAIM-301](record/claims.d/CLAIM-301.md), with the
      granted limit [CLAIM-292](record/claims.d/CLAIM-292.md);
    - coupled meaning and influence can capture an interpretation, [CLAIM-297](record/claims.d/CLAIM-297.md).
  - Sixteen questions, from [QUESTION-105](record/questions.d/QUESTION-105.md) to [QUESTION-100](record/questions.d/QUESTION-100.md).
  - Twelve cases, among them the owner's EMT case, [CASE-085](record/cases.d/CASE-085.md).
  - Two terms: operational availability, [TERM-055](record/terms.d/TERM-055.md); question drift, [TERM-056](record/terms.d/TERM-056.md).
- Eight works registered unread: selective accessibility (Strack and
  Mussweiler, two papers), Goldreich, Gibson, Hutchins, query drift (Mitra
  et al.), AGM and Hansson's survey of belief revision.
- [ADR-043](record/decisions.d/ADR-043.md), proposed: a `warrant` field on CLAIM, piloted before it is
  required.

### Documentation

- Dated notes on [CLAIM-029](record/claims.d/CLAIM-029.md), [CLAIM-199](record/claims.d/CLAIM-199.md), [CLAIM-250](record/claims.d/CLAIM-250.md) and [CLAIM-264](record/claims.d/CLAIM-264.md).
- Readings of the registered works: Strack & Mussweiler 1997, AGM 1985,
  Hansson's survey and Harris et al. 2019 read; Goldreich's 1995 draft
  skimmed (chapters 1–3); Mussweiler & Strack 1999, Gibson, Hutchins and
  Mitra et al. Unavailable. Harris et al. 2019 and Goldreich 1990
  registered.

### Changed

- From the readings: the feasible-test separation claim (unconditional;
  only samplability needs generators), the hidden-bit claim and the
  generator case, the anchoring claim (retrieval step inferred, not
  measured), and the question on retained state (narrowed).
- A question on amortized retrieval as amortized computation, from the
  cockpit reading, with eight works on offloading and amortization
  registered and read (Kirsh & Maglio, Kirsh, Ballard et al., Risko &
  Gilbert, Gray & Fu, Dasgupta et al., Lieder & Griffiths, Gershman &
  Goodman) and a citation search for prior joint treatments.
- A question on signal detection and computational indistinguishability,
  with Geisler 2011, Håstad et al. 1999, Dwork et al. 2021 and
  Hébert-Johnson et al. 2018 registered and read; and Kirsh 1996, Gray et
  al. 2006 and Dasgupta & Gershman 2021 read for the amortization question.
- Three scaling-law works on training against inference compute (Jones
  2021, Sardana et al. 2024, Snell et al. 2024) registered and read for
  the amortization question.
- Howes et al. 2016 registered and read; the description of it as a
  memorize-or-look-up trade, from Lieder & Griffiths, corrected.

### Added

- Twenty THEORYs for the quantum-foundations readings that no THEORY cited: ψ-ontology, wave-function readings, steering, quantum work, and the topos programme; [THEORY-037](record/theory.d/THEORY-037.md) now presupposes the clopen-region result.

### Added

- Fourteen THEORYs for the readings on the self, personhood and individuation, one Active and thirteen Proposed, drawn from fifteen of the sixteen readings that had none: Locke, Hume, Parfit, Lewis and Williams on persons over time; Dennett, Strawson, Gallagher and Shanahan on selves; Meincke and Wilson and Barker on biological individuals.

### Added

- Twenty THEORYs from sixteen readings in the small topics: status distrust, infinite fair lotteries, stratified belief, averaging over theories, network epistemology, somatic markers, emotion regulation, fluency, IFS, the gut–brain axis, causaltopes, do() as surgery, Łoś and compactness, waste-collection routing, duality, participatory sense-making, options in HRL and their neural mapping, structure learning by model reduction, and Shampoo.

### Added

- Twenty-two THEORYs from the social-science, network-science, compositionality, neuroscience and philosophy-of-biology readings that had none, with five claims' grounds pointed at them.

### Added

- Nine THEORYs from the social-ontology, game-theory, religion and design-rationale readings: Ritchie on groups (two), Haslanger, Searle against Hindriks & Guala, Durkheim, Epstein, List & Pettit on non-redundancy (Proposed), and Kamenica & Gentzkow's Bayesian persuasion (Active).

### Added

- Eleven THEORYs from twenty society-and-governance readings: the Google remedies opinion, Doctorow's four constraints on platform decay, competitive authoritarianism, Russian hybrid war and the information-war narrative, EEAS FIMI attribution, DISINFOX, algorithmic nudging, Gelman, Thompson and Moynihan.

### Changed

- Citations of content that [ADR-043](record/decisions.d/ADR-043.md)'s splits moved out of a claim now name
  the claim that holds it: twenty-four places in claims, questions, a case,
  a THEORY and reading notes. Quotations keep their original code with the
  new home added.

### Added

- [CLAIM-379](record/claims.d/CLAIM-379.md), Active: on a finite set of stimuli, regularized linear
  readouts with ridge b > 0 collapse exactly the orthogonal orbit of a
  centred representation, and the CCA member the invertible-linear orbit.
  Split from [CLAIM-269](record/claims.d/CLAIM-269.md) (promotion audit, batch 015, [ADR-047](record/decisions.d/ADR-047.md)), which rests
  on it and stays Proposed for its [THEORY-002](record/theory.d/THEORY-002.md) and [THEORY-019](record/theory.d/THEORY-019.md) clauses.

### Added

- [CLAIM-375](record/claims.d/CLAIM-375.md), Active: under one-hop allocation within an epoch, an
  operator's authority stays fixed while endorsing an ally nearer its own
  policy moves the collective decision toward it. A construction, split
  from [CLAIM-285](record/claims.d/CLAIM-285.md) under the promotion audit's batch-001 decision ([ADR-047](record/decisions.d/ADR-047.md)).

### Changed

- [CLAIM-285](record/claims.d/CLAIM-285.md) keeps the incentive thesis: that delegation does work in a
  population, and that the two conditions are not confined to one hop. It
  rests on the new claim and is now interpretive.

### Added

- [CLAIM-373](record/claims.d/CLAIM-373.md), Active: the commutator-distortion identity with its norm
  bound, Φ[A,B] − [A′,B′]Φ = A′E_B + E_A B − B′E_A − E_B A, split from
  [CLAIM-063](record/claims.d/CLAIM-063.md).
- [CLAIM-374](record/claims.d/CLAIM-374.md), Active: on consistently connected systems,
  Contextuality-by-Default and the sheaf criterion agree, split from
  [CLAIM-037](record/claims.d/CLAIM-037.md) and proved.

### Changed

- [CLAIM-063](record/claims.d/CLAIM-063.md) and [CLAIM-037](record/claims.d/CLAIM-037.md) keep their theses, rest on the new claims, and
  become interpretive. This carries out the promotion audit's batch-002
  decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [CLAIM-380](record/claims.d/CLAIM-380.md), Active, demonstrated. For finitely many states and
  outcomes, the directed Bayes-risk term D⁺ is zero from a garbling back to
  its source. It vanishes for every finite problem and prior exactly when
  the rendering is at least as informative ([THEORY-717](record/theory.d/THEORY-717.md)), and A86's D_Q is
  its symmetrization. Split from [CLAIM-326](record/claims.d/CLAIM-326.md).
- [CLAIM-381](record/claims.d/CLAIM-381.md), Active, demonstrated. Over finitely many items with
  finite judgement outcomes:
  - a constant kernel fits only item-independent target responses;
  - exact fit is a garbling;
  - Le Cam's deficiency is one linear programme.
  Split from [CLAIM-228](record/claims.d/CLAIM-228.md).

### Changed

- [CLAIM-326](record/claims.d/CLAIM-326.md) rests on the new claim and keeps the unrestricted case, which
  needs [THEORY-156](record/theory.d/THEORY-156.md). It stays Proposed.
- [CLAIM-228](record/claims.d/CLAIM-228.md) rests on the new claim and keeps the proposal that the
  restated measure is informative. Its warrant is corrected to empirical.
- [CLAIM-212](record/claims.d/CLAIM-212.md)'s warrant is corrected from demonstrated to interpretive,
  because it is a proposal whose defeat condition is a reception study.
- All carry out the promotion audit's batch-014 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [THEORY-723](record/theory.d/THEORY-723.md), Active: for a softmax model's final layer, the output
  distribution fixes the representation only up to an invertible linear
  map. Whether closeness in distribution bounds representational
  dissimilarity depends on the distance. Split from [THEORY-002](record/theory.d/THEORY-002.md).
- [THEORY-725](record/theory.d/THEORY-725.md), Active: on the court agenda, majority voting is not
  robustly rational and the premise-based procedure is, with set-wise
  supervenience and discontinuity. Split from [THEORY-127](record/theory.d/THEORY-127.md).
- [THEORY-729](record/theory.d/THEORY-729.md), Active: an adjunction into an opposite category
  restricts to a dual equivalence on its fixed points. Split from
  [THEORY-604](record/theory.d/THEORY-604.md), with the proof the source omits.

### Changed

- [THEORY-002](record/theory.d/THEORY-002.md), [THEORY-127](record/theory.d/THEORY-127.md) and [THEORY-604](record/theory.d/THEORY-604.md) extend the new entries and keep
  their unproved parts Proposed. This carries out the promotion audit's
  batch-009 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [THEORY-720](record/theory.d/THEORY-720.md), Active: classical simulations between no-signalling
  empirical models never create contextuality, and only non-contextual
  models can be cloned. This is the proved half of [THEORY-174](record/theory.d/THEORY-174.md).
- [THEORY-722](record/theory.d/THEORY-722.md), Active: in Contextuality-by-Default 2.0, coarse-graining
  can turn a noncontextual system into a contextual one, and CbD 1.0 and
  2.0 agree on two-variable connections. This is the proved part of
  [THEORY-168](record/theory.d/THEORY-168.md).
- Both carry out the promotion audit's batch-005 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
  [THEORY-174](record/theory.d/THEORY-174.md) and [THEORY-168](record/theory.d/THEORY-168.md) extend the new entries and stay Proposed.

### Added

- [THEORY-734](record/theory.d/THEORY-734.md) (Active): the planar lower bound on the precision of
  hyperbolic tree embeddings, split from [THEORY-196](record/theory.d/THEORY-196.md). A root with
  deg_max ≥ 15 chains needs Ω((ℓ/ε) log deg_max) bits per coordinate at
  distortion 1 + ε ≤ 2. It is proved by exact hyperbolic trigonometry,
  with explicit constants, where [LIT-874](record/literature.d/LIT-874.md) used a small-angle approximation
  as an equality.
- [THEORY-733](record/theory.d/THEORY-733.md) (Active): exact dynamical independence in linear VAR
  models, split from [THEORY-257](record/theory.d/THEORY-257.md). The VAR criterion is re-derived. For order
  above 1 the exceptional set is proved Lebesgue-null, where [LIT-979](record/literature.d/LIT-979.md)
  counted equations. For VAR(1), exact coarse-grainings exist on open sets
  but not at every scale generically.
- [QUESTION-150](record/questions.d/QUESTION-150.md): whether the code-based upper bound for tree
  embeddings in H^r, r > 2, is matched by a lower bound. This is the
  higher-dimensional half of the condition formerly on [THEORY-196](record/theory.d/THEORY-196.md).

### Changed

- [THEORY-196](record/theory.d/THEORY-196.md) extends [THEORY-734](record/theory.d/THEORY-734.md) and stays Proposed. Its promote_when
  narrows to Sarkar's distortion bound, the upper bound it still rests on.
- [THEORY-257](record/theory.d/THEORY-257.md) extends [THEORY-733](record/theory.d/THEORY-733.md) and stays Proposed. Its title now
  restricts "generically none is exact" to VAR order above 1, its VAR(1)
  bullet is corrected, and [NOTE-791](record/notes.d/NOTE-791.md)'s C4 is annotated.
- Both carry out the promotion audit's batch-012 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [CLAIM-382](record/claims.d/CLAIM-382.md) (demonstrated, Active): with i.i.d. Gaussian
  initialisation and SGD or momentum SGD, the law of an autoencoder's
  learned representation inherits the activation's orthogonal symmetry
  group, so radial activations privilege no basis in law. Split from
  [THEORY-288](record/theory.d/THEORY-288.md), with the optimiser condition the argument needs.
- [CLAIM-383](record/claims.d/CLAIM-383.md) (demonstrated, Active): the lift-up lower bounds for plane
  Couette and Poiseuille flow, with transient growth at least cR,
  resonance at least cR², and a destabilizing perturbation of norm at most
  CR⁻². Split from [THEORY-304](record/theory.d/THEORY-304.md).

### Changed

- [THEORY-288](record/theory.d/THEORY-288.md) and [THEORY-304](record/theory.d/THEORY-304.md) cite the new claims and keep their empirical
  or computed titles, Proposed, with their promote_whens unchanged. This
  carries out the promotion audit's batch-013 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [THEORY-724](record/theory.d/THEORY-724.md), Active: non-normality is necessary for time dependence
  to destabilize a uniformly stable operator, and a switched non-normal
  oscillator is unstable. Split from [THEORY-325](record/theory.d/THEORY-325.md).
- [CLAIM-376](record/claims.d/CLAIM-376.md), Active: shifting by −δI makes a system stable at every
  instant while keeping a positive exponent λ − δ. On the switched
  oscillator, λ = 0.0955 at δ = 0.1.
- [CLAIM-378](record/claims.d/CLAIM-378.md), Active: an index invariant to every invertible linear
  map depends only on the column space, which settles the column-centred
  case of [THEORY-236](record/theory.d/THEORY-236.md).

### Changed

- [THEORY-236](record/theory.d/THEORY-236.md) is promoted to Active.
- [THEORY-325](record/theory.d/THEORY-325.md) is narrowed to its stochastic half and stays Proposed.
- These carry out the promotion audit's batch-006 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [THEORY-728](record/theory.d/THEORY-728.md), Active: on a finite data set, the diffusion-map
  embedding turns the 1/π-weighted diffusion distance into Euclidean
  distance exactly. Split from [THEORY-565](record/theory.d/THEORY-565.md).
- [CLAIM-377](record/claims.d/CLAIM-377.md), Active: the Gauss–Newton Fisher βJᵀJ and the NTK Gram
  matrix JJᵀ share their non-zero spectrum, with the proof. Split from
  [THEORY-084](record/theory.d/THEORY-084.md).
- [THEORY-726](record/theory.d/THEORY-726.md), Active: weight decay on factors is a nuclear-norm
  penalty on their product. Split from [THEORY-180](record/theory.d/THEORY-180.md).

### Changed

- [THEORY-565](record/theory.d/THEORY-565.md), [THEORY-084](record/theory.d/THEORY-084.md) and [THEORY-180](record/theory.d/THEORY-180.md) stay Proposed for their
  remaining parts. Each now extends or cites the new entry. These
  changes carry out the promotion audit's batch-010 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [THEORY-721](record/theory.d/THEORY-721.md), Active: no basis or tensor factorisation of a
  finite-dimensional Hilbert space is distinguished by the space alone,
  and over ℂ, but not over ℝ, orthonormal bases are exactly the
  commutative special †-Frobenius algebras. Split from [THEORY-017](record/theory.d/THEORY-017.md) under
  the promotion audit's batch-005 decision ([ADR-047](record/decisions.d/ADR-047.md)).

### Changed

- [THEORY-017](record/theory.d/THEORY-017.md) keeps its cross-source synthesis and extends the new THEORY.
  Its promotion condition now names only the per-placement check.

### Added

- [THEORY-732](record/theory.d/THEORY-732.md), Active: for ReLU networks on a linear path, weak
  additivity and commutativity at every layer give exact layerwise
  linear feature connectivity, output linearity bounds the path's error
  by twice the endpoints', and one hidden layer with interpolating minima
  gives the exact case. Split from [THEORY-111](record/theory.d/THEORY-111.md).

### Changed

- [THEORY-369](record/theory.d/THEORY-369.md), Active, narrowed to a fixed number of points and clusters of
  at least two: as dimension grows, an optimal nearest-neighbour search
  must read every such cluster, with probability tending to 1. The record's
  concentration proof is written in.
- [THEORY-111](record/theory.d/THEORY-111.md) stays Proposed for its empirical regularity and the step to
  many-model averages, and now extends [THEORY-732](record/theory.d/THEORY-732.md). These changes carry
  out the promotion audit's batch-016 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- The 2026-10-16 exchange on what kind of thing a sports fandom is
  (chatgpt.com/share/6ad17889-…), filed as a workbench reconstruction of
  U1–U15.
  - Six claims:
    - persistence through total turnover is causal transmission of the
      producing organization, not resemblance, [CLAIM-329](record/claims.d/CLAIM-329.md);
    - the owner's timescale facet of a level of organization, [CLAIM-331](record/claims.d/CLAIM-331.md);
    - a slow collective variable is part of the dynamics when members use
      it and so regenerate it, [CLAIM-327](record/claims.d/CLAIM-327.md);
    - the dual canvases linearized: only the loop destabilizes symmetry,
      at βγ > (1 − α)(1 − δ), along a mixed direction, Active and
      demonstrated, [CLAIM-330](record/claims.d/CLAIM-330.md), a partial answer to [QUESTION-100](record/questions.d/QUESTION-100.md);
    - plural succession: separated continuities give several successors
      without identity branching, [CLAIM-328](record/claims.d/CLAIM-328.md);
    - distributed cultural uptake: a loose population can change an
      outside institution without a collective intention, [CLAIM-332](record/claims.d/CLAIM-332.md).
  - Five questions: what must be transmitted for a collective to persist
    ([QUESTION-118](record/questions.d/QUESTION-118.md)); a time-lagged block criterion ([QUESTION-116](record/questions.d/QUESTION-116.md));
    joint individuation by information, closure, effective information and
    an Occam price ([QUESTION-115](record/questions.d/QUESTION-115.md)); stance and effect without a
    procedure ([QUESTION-119](record/questions.d/QUESTION-119.md)); the dual canvases against reflected
    appraisal and adaptive networks ([QUESTION-117](record/questions.d/QUESTION-117.md)).
  - Eight cases: a rivalry, a reputation, a hated executive, the Washington
    Senators (documented), a college program through roster churn, the
    Juggernaut line (documented), three matched populations, and [CASE-092](record/cases.d/CASE-092.md)
    linearized.
- Twenty-five works registered unread (curation entry of 2026-10-16),
  among them Krakauer et al. on the information theory of individuality,
  Flack on multiple time-scales, Feldman and Pentland on routines, and
  Jia et al. on the DeGroot–Friedkin model; and five candidates for two
  works the exchange cited that could not be identified uniquely
  (curation entry of 2026-10-16, 01:54).

### Documentation

- Dated notes on [CASE-092](record/cases.d/CASE-092.md) (the linearization and the analyses proposed for
  it) and [QUESTION-093](record/questions.d/QUESTION-093.md) (Hoel et al. 2013 is read, not unread).

### Added

- The 2026-10-17 exchange "Synthesis opportunities analysis"
  (chatgpt.com/share/6ad41263-…), filed as a workbench reconstruction of
  U1–U47 in four entries of 2026-10-18.
  - Twenty-five claims. Six are demonstrated, all Active; one of these is
    granted. Eighteen are interpretive theses, all Proposed. One is a
    counter.
    - Graded freedom and autonomy (the owner's U9), compared by inclusion,
      [CLAIM-354](record/claims.d/CLAIM-354.md); control cost is not controllability rank,
      [CLAIM-345](record/claims.d/CLAIM-345.md); Sen's two aspects of freedom (the owner's U11),
      [CLAIM-352](record/claims.d/CLAIM-352.md).
    - Relationally indexed normative judgment (the owner's U17–U18),
      [CLAIM-363](record/claims.d/CLAIM-363.md); judgment-preserving coarse-graining, granted,
      [CLAIM-350](record/claims.d/CLAIM-350.md); no target-free normative adequacy, [CLAIM-348](record/claims.d/CLAIM-348.md).
    - The owner a self-model presents, with the binding real (the owner's
      U26–U27), [CLAIM-355](record/claims.d/CLAIM-355.md); training-time conditions belong to the
      unit whose jurisdiction governs the updates (U31), [CLAIM-367](record/claims.d/CLAIM-367.md).
    - Frustration, not distress (the owner's U33), [CLAIM-368](record/claims.d/CLAIM-368.md); a zero
      aggregate gradient conceals it, [CLAIM-351](record/claims.d/CLAIM-351.md); frustration is
      ordinal first (the owner's U37 correction), [CLAIM-347](record/claims.d/CLAIM-347.md); invariance
      of common descent, [CLAIM-366](record/claims.d/CLAIM-366.md); the residual and its dual,
      [CLAIM-365](record/claims.d/CLAIM-365.md); structural against governance-induced frustration,
      [CLAIM-357](record/claims.d/CLAIM-357.md); three independent obstructions (the owner's U36),
      [CLAIM-346](record/claims.d/CLAIM-346.md); jurisdiction, not information, [CLAIM-353](record/claims.d/CLAIM-353.md).
    - An external objective can become a goal of the training
      organization (the owner's U35), against [CLAIM-288](record/claims.d/CLAIM-288.md), [CLAIM-356](record/claims.d/CLAIM-356.md);
      relief judged against the original demands (U38), [CLAIM-361](record/claims.d/CLAIM-361.md);
      wide against deep (the owner's U38), [CLAIM-360](record/claims.d/CLAIM-360.md).
    - Robustness to compromised insiders (U41), [CLAIM-359](record/claims.d/CLAIM-359.md); access,
      authority and action, and overcontrol (the owner's U42),
      [CLAIM-349](record/claims.d/CLAIM-349.md); resolve (the owner's U37 frame), [CLAIM-344](record/claims.d/CLAIM-344.md).
    - Learned local accommodation can reduce the amortized cost of
      recurrent arbitration (the owner's U45),
      [CLAIM-358](record/claims.d/CLAIM-358.md); non-domination as a candidate constituent of
      authenticity (the owner's U45),
      [CLAIM-362](record/claims.d/CLAIM-362.md), with its counter, [CLAIM-364](record/claims.d/CLAIM-364.md).
  - Nine questions, among them normativity from first principles (the
    owner's U16), [QUESTION-128](record/questions.d/QUESTION-128.md), and a gauge account (the owner's U19),
    [QUESTION-130](record/questions.d/QUESTION-130.md).
  - Nine cases, among them the owner's two people with one commitment,
    [CASE-109](record/cases.d/CASE-109.md), five constructions and two proposed studies.
  - Three terms: relational normative realism, [TERM-059](record/terms.d/TERM-059.md); frustration,
    [TERM-060](record/terms.d/TERM-060.md); practical synchronization, [TERM-061](record/terms.d/TERM-061.md), a dimension
    independent of [TERM-050](record/terms.d/TERM-050.md)'s valuational concordance, which is unchanged.
- Twenty-five works registered unread (curation entry of 2026-10-18), among
  them Arrow 1950, Halpern and Moses on common knowledge, Désidéri's
  multiple-gradient descent, Edmondson on psychological safety, Guida et al.
  on organizational flexibility, DBT and RO-DBT sources, Chesson on
  coexistence and Kahneman 2011.

- The owner's review of the filing, before merge (workbench entry of
  2026-10-18): ordinal acceptance sets corrected so that the baseline does
  not satisfy every demand; practical synchronization set beside
  valuational concordance as an independent dimension, not its
  generalization; five claims and terms narrowed. A position note says how
  the entries fit into one account, with the recoverability of a rare
  specialist's influence made explicit.

### Documentation

- Dated notes on 55 existing entries that the exchange re-derived, extended
  or misread. Among them: [CLAIM-027](record/claims.d/CLAIM-027.md), whose essay the exchange's first
  manuscript rebuilds without citing; [QUESTION-086](record/questions.d/QUESTION-086.md), now with five
  second appearances; [THEORY-232](record/theory.d/THEORY-232.md), whose measure of frustration is an
  aggregate; [CLAIM-288](record/claims.d/CLAIM-288.md), to which the owner objected; [CLAIM-039](record/claims.d/CLAIM-039.md) and
  [TERM-006](record/terms.d/TERM-006.md), whose set-aside lines the exchange reopened. Whether those
  lines reopen is left to the owner.

### Changed

- A TERM may be Proposed: its status is the standing of its definition, not
  a credence ([ADR-046](record/decisions.d/ADR-046.md)). TERM gains `rivals`, `complements` and
  `refines`/`refined_by`, the relations THEORY, CLAIM and QUESTION already
  use, and `supersedes` is kept for an adoption that retires the earlier
  term. The TERM template lists the statuses and relations.
- [TERM-050](record/terms.d/TERM-050.md) and [TERM-061](record/terms.d/TERM-061.md) complement each other. [TERM-010](record/terms.d/TERM-010.md) now
  refines [TERM-043](record/terms.d/TERM-043.md) instead of being superseded by it, since it was never retired.

### Changed

- [THEORY-037](record/theory.d/THEORY-037.md) is promoted to Active. The record re-derives that the clopen
  sub-objects of the spectral presheaf form a complete Heyting algebra,
  that its negation is the source's pseudo-complement, and that excluded
  middle fails in the ℂ² case. This carries out the promotion audit's
  batch-009 decision under [ADR-047](record/decisions.d/ADR-047.md) v2.

### Fixed

- [THEORY-686](record/theory.d/THEORY-686.md) said the observations without generative effects are exactly
  the left adjoints. Having no generative effect is weaker than preserving
  all joins: the constant map to the top has none, and is not a left
  adjoint. The title now says "preserve all joins", with two
  counterexamples. With the record's re-derivations of Prop. 1.111 and
  Thm 1.115, the corrected account is promoted to Active (batch 009,
  [ADR-047](record/decisions.d/ADR-047.md) v2).

### Added

- [CLAIM-372](record/claims.d/CLAIM-372.md), Active: within a fixed scenario the contextual fraction
  is piecewise linear and Lipschitz in the empirical table, with a
  constant set by the scenario. This is the record's own derivation, split
  from [THEORY-165](record/theory.d/THEORY-165.md), with a proof.

### Changed

- [THEORY-184](record/theory.d/THEORY-184.md) (coincident neurons stay coincident, and distinct ones
  cannot merge in finitely many steps below 1/K) is promoted to Active.
  The independent check its promotion condition asked for is the audit's.
- [THEORY-165](record/theory.d/THEORY-165.md) is narrowed to what [LIT-265](record/literature.d/LIT-265.md) proves, the linear programme and
  convexity under mixing, and promoted to Active.
- Both carry out the promotion audit's batch-005 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [THEORY-727](record/theory.d/THEORY-727.md), Active: for a fixed linear operator, finite-time growth
  is the propagator's top singular value, which the eigenvalues bound only
  from below. Growth starts at the numerical abscissa, and the forced
  response is bounded by κ(E)/dist(iω, Λ(A)). Split from [THEORY-323](record/theory.d/THEORY-323.md).
- [QUESTION-138](record/questions.d/QUESTION-138.md): when the truncated functional-map matrix stays nearly
  orthogonal under a near-isometry, the clause formerly in [THEORY-297](record/theory.d/THEORY-297.md)'s
  promotion condition.

### Changed

- [THEORY-297](record/theory.d/THEORY-297.md) is promoted to Active, with "equivalent" qualified as "up to
  null sets" and its three statements re-derived in a dated note.
- [THEORY-323](record/theory.d/THEORY-323.md) is narrowed to the white-noise variance clause, which its
  source cites and does not prove, and stays Proposed.
- Both carry out the promotion audit's batch-007 decisions ([ADR-047](record/decisions.d/ADR-047.md)),
  under the owner's ruling of 2026-10-19 that a checked re-derivation
  meets a condition asking for a proof the record does not hold.

### Added

- Eight THEORYs (three Active, five Proposed) from the ten thermodynamics
  readings: the fluctuation theorems, England's macrostate bound,
  dissipative adaptation, gradient dissipation, life forced by
  geochemistry, maximum entropy production, the critique of its
  derivation, and life with planetary MEP.

### Added

- Transfer entropy, which the record used in a dozen documents while
  holding one source for it. Eight works are registered and seven read,
  each with a NOTE and a THEORY: Schreiber's definition ([THEORY-701](record/theory.d/THEORY-701.md)),
  Kraskov, Stögbauer and Grassberger's nearest-neighbour estimators
  ([THEORY-709](record/theory.d/THEORY-709.md)), Lizier, Prokopenko and Zomaya's local transfer entropy
  ([THEORY-702](record/theory.d/THEORY-702.md)), Williams and Beer's decomposition of it ([THEORY-712](record/theory.d/THEORY-712.md)),
  James, Barnett and Crutchfield's critique ([THEORY-707](record/theory.d/THEORY-707.md)), Massey's
  directed information ([THEORY-711](record/theory.d/THEORY-711.md)) and Ay and Polani's interventional
  information flow ([THEORY-710](record/theory.d/THEORY-710.md)). Kaiser and Schreiber (2002) is
  `Unavailable`.
- [TERM-057](record/terms.d/TERM-057.md) defines transfer entropy with its history lengths and
  conditioning set explicit. [CLAIM-335](record/claims.d/CLAIM-335.md) holds that it measures directed
  predictive improvement, unique plus synergistic information, and not
  information flow.

### Changed

- [CLAIM-333](record/claims.d/CLAIM-333.md), [TERM-058](record/terms.d/TERM-058.md) and [THEORY-704](record/theory.d/THEORY-704.md) name directed information
  and interventional flow. [NOTE-053](record/notes.d/NOTE-053.md) names its now-held sources.

### Fixed

- [NOTE-788](record/notes.d/NOTE-788.md)'s transfer entropy is Schreiber's only at lag 1; annotated, with
  "flow" there read as predictive direction, as in [THEORY-275](record/theory.d/THEORY-275.md).
  [NOTE-799](record/notes.d/NOTE-799.md)'s open question on a ΦID of transfer entropy is annotated.

### Changed

- Fourteen claims [ADR-043](record/decisions.d/ADR-043.md) found compound are split so that each claim
  carries one warrant: eleven new claims, three pointers to claims that
  already held the part. [CLAIM-240](record/claims.d/CLAIM-240.md) is kept whole.

### Added

- The rest of A39's examination of "I am whatever you say I am", from the exchange of 2026-10-22, filed at the owner's request around [CLAIM-415](record/claims.d/CLAIM-415.md):
  - a Proposed term for the attributed self in four senses, held, imagined, imagined audience and appropriated ([TERM-075](record/terms.d/TERM-075.md)), which gathers the exchange's "socially operative identity" and "recursive social self-modeling";
  - a Proposed claim that self-governance with respect to social judgement keeps access to others' judgements while making their authority depend on grounds, not visibility, repetition or attributed plurality ([CLAIM-425](record/claims.d/CLAIM-425.md));
  - an objection to that claim from hyperstition, raised by the owner on 2026-10-23: where a judgement's circulation helps bring about what it says, its visibility is evidence about what it will bring about, so the visibility rule holds for judgements of what already is ([CLAIM-426](record/claims.d/CLAIM-426.md)), with three works registered unread: Carstens and Land's interview defining hyperstition ([LIT-1396](record/literature.d/LIT-1396.md)), MacKenzie's *An Engine, Not a Camera* ([LIT-1395](record/literature.d/LIT-1395.md)) and Soros on reflexivity ([LIT-1397](record/literature.d/LIT-1397.md));
  - three stipulated cases: the label that confirms itself ([CASE-141](record/cases.d/CASE-141.md)), its variant confirmed by resistance ([CASE-142](record/cases.d/CASE-142.md)), and the attributed self as a test of the imagined audience ([CASE-140](record/cases.d/CASE-140.md));
  - a question on whether correcting the distribution of opinion dissolves an apparent consensus, refining [QUESTION-119](record/questions.d/QUESTION-119.md) ([QUESTION-261](record/questions.d/QUESTION-261.md));
  - two works registered: the song ([LIT-1394](record/literature.d/LIT-1394.md)) and Merton's "The Self-Fulfilling Prophecy" ([LIT-1398](record/literature.d/LIT-1398.md)).

### Changed

- [CLAIM-415](record/claims.d/CLAIM-415.md) revised: its sentence on Cooley no longer overstates him, step 2 cites Cooley's "remoter conformity" and the new resistance case, Cooley is added to its grounds, and the majority illusion is limited to the perceived-majority route.
- A dated note on [TERM-045](record/terms.d/TERM-045.md) points to the new term. The definition is unchanged.

### Added

- Berniūnas & Dranseika 2016, the reply to Nichols & Bruno 2010 on folk
  concepts of person and identity, filed Unavailable from its abstract.

### Changed

- [ADR-048](record/decisions.d/ADR-048.md): nucleation files any work the owner wants here, whether or not
  an anthology topic could hold it, and no anthology check comes before
  filing. Instructions for ML practice still belong to the anthology. An
  `ANTH-` code is cited when known and is no longer required. Whether a work
  is also held there is the anthology's question. The
  `anthology-candidate` flag is still applied. [ADR-001](record/decisions.d/ADR-001.md), [ADR-005](record/decisions.d/ADR-005.md) and
  [ADR-013](record/decisions.d/ADR-013.md) take history notes, and CLAUDE.md, the topics blurb and the
  README are rewritten to match.

[CLAIM-265](record/claims.d/CLAIM-265.md) is restated relative to a specified class of admissible correspondences, and its proviso is limited to a correspondence admitted only because it removes the disagreement (promotion audit, batch 040). The singular "only once the correspondence is fixed" was too strong: a disagreement can survive every member of a class with no one member fixed. A derivation in a dated note moves its warrant to demonstrated. Its status is unchanged.

### Added

- From the exchange of 2026-10-19 on coarse-to-fine processes and the physics of model reduction: [CLAIM-388](record/claims.d/CLAIM-388.md) (demonstrated, Active), that exact dynamical closure of a collective variable does not need a nearly decomposable block, with its construction [CASE-120](record/cases.d/CASE-120.md); six questions: three orders of coarse-to-fine ([QUESTION-217](record/questions.d/QUESTION-217.md)), nested optimal abstractions ([QUESTION-220](record/questions.d/QUESTION-220.md)), whether near-decomposability bounds dynamical dependence ([QUESTION-221](record/questions.d/QUESTION-221.md)), closure without a block ([QUESTION-218](record/questions.d/QUESTION-218.md)), memory and Markovian augmentation ([QUESTION-222](record/questions.d/QUESTION-222.md)) and flux-based organization ([QUESTION-219](record/questions.d/QUESTION-219.md)); nineteen works registered unread, among them the first Mori–Zwanzig and turbulence readings; dated notes on [CLAIM-157](record/claims.d/CLAIM-157.md) and [CLAIM-331](record/claims.d/CLAIM-331.md); a workbench entry and a curation entry.
- The first reading of the program: Shpak, Stadler, Wagner & Hermisson (2004), [LIT-1242](record/literature.d/LIT-1242.md), read in full in [NOTE-979](record/notes.d/NOTE-979.md), with [THEORY-755](record/theory.d/THEORY-755.md) (Active, re-derived): a linear system's block sums close for every state iff the partition is column-equitable, which is aggregation without decomposition. Its companion preprint on Simon–Ando decomposability, [LIT-1241](record/literature.d/LIT-1241.md), is registered unread.

- Further readings of 2026-10-20, each read in full with a NOTE: Shpak, Stadler, Wagner & Altenberg (2004), Eyink & Aluie (2009), Parish & Duraisamy (2017), and Chorin, Hald & Kupferman (2000, 2002); THEORYs [THEORY-754](record/theory.d/THEORY-754.md), [THEORY-760](record/theory.d/THEORY-760.md) and [THEORY-752](record/theory.d/THEORY-752.md) (Active) and [THEORY-747](record/theory.d/THEORY-747.md) (Proposed). Three demonstrated claims from them, re-checked: dependence of a block is second order in its incoming coupling ([CLAIM-390](record/claims.d/CLAIM-390.md)); the Simon–Ando aggregate's closure defect is exactly QA(I − VQ) ([CLAIM-386](record/claims.d/CLAIM-386.md)); in VAR(1) independence implies zero Mori–Zwanzig memory, not conversely ([CLAIM-389](record/claims.d/CLAIM-389.md)). Dated notes on [CLAIM-157](record/claims.d/CLAIM-157.md), [CLAIM-331](record/claims.d/CLAIM-331.md) and [THEORY-257](record/theory.d/THEORY-257.md); a curation entry for the batch.
- A second batch of readings of 2026-10-20: Equitz & Cover (1991), Raju, Machta & Sethna (2018), Shalizi & Crutchfield (2002), Crutchfield & Shalizi (1999), Rosas et al. (2020) and Coifman & Lafon (2006), each with a NOTE; THEORYs [THEORY-742](record/theory.d/THEORY-742.md), [THEORY-743](record/theory.d/THEORY-743.md), [THEORY-756](record/theory.d/THEORY-756.md), [THEORY-764](record/theory.d/THEORY-764.md), [THEORY-745](record/theory.d/THEORY-745.md) (Active) and [THEORY-751](record/theory.d/THEORY-751.md), [THEORY-744](record/theory.d/THEORY-744.md) (Proposed). [CLAIM-387](record/claims.d/CLAIM-387.md) (demonstrated): optimal deterministic information-bottleneck partitions need not nest. Notes on [CLAIM-152](record/claims.d/CLAIM-152.md) and [QUESTION-115](record/questions.d/QUESTION-115.md); connections on [THEORY-202](record/theory.d/THEORY-202.md), [THEORY-257](record/theory.d/THEORY-257.md) and [THEORY-497](record/theory.d/THEORY-497.md).
- A third batch of readings of 2026-10-20: Constantin, E & Titi (1994), Wiskott & Sejnowski (2002), Granero-Belinchón, Roux & Garnier (2016), Rahaman et al. (2019) and Coifman & Maggioni (2006), each with a NOTE; THEORYs [THEORY-749](record/theory.d/THEORY-749.md), [THEORY-746](record/theory.d/THEORY-746.md), [THEORY-750](record/theory.d/THEORY-750.md), [THEORY-748](record/theory.d/THEORY-748.md), [THEORY-761](record/theory.d/THEORY-761.md), [THEORY-758](record/theory.d/THEORY-758.md) (Active) and [THEORY-759](record/theory.d/THEORY-759.md) (Proposed). Connections on [THEORY-086](record/theory.d/THEORY-086.md) and [THEORY-754](record/theory.d/THEORY-754.md); [CLAIM-331](record/claims.d/CLAIM-331.md)'s note extended.
- Follow-ups registered and read on 2026-10-20: No, Ingber & Weissman (2016), Isett (2018, skimmed) and Nadler, Lafon, Coifman & Kevrekidis (2006); [THEORY-762](record/theory.d/THEORY-762.md) (Active: a reversible diffusion's eigenfunctions have no Mori–Zwanzig memory in mean, and are Markov in law only under a gradient condition) and [THEORY-763](record/theory.d/THEORY-763.md) (Proposed: Onsager's negative half, flux surviving in both directions). Notes on [CLAIM-164](record/claims.d/CLAIM-164.md) and [CLAIM-157](record/claims.d/CLAIM-157.md).
- Charvin, Catenacci Volpi & Polani (2023) registered and read: [THEORY-753](record/theory.d/THEORY-753.md) (refinability as garbling, and its hull test) and [THEORY-757](record/theory.d/THEORY-757.md) (refinable when Y = f(X) or both binary), Active; [CLAIM-392](record/claims.d/CLAIM-392.md) (demonstrated): stochastic information-bottleneck optima need not nest.
- Buckmaster, De Lellis, Székelyhidi & Vicol (2019) registered and read ([LIT-1300](record/literature.d/LIT-1300.md), [NOTE-1013](record/notes.d/NOTE-1013.md)): [THEORY-776](record/theory.d/THEORY-776.md) (Proposed), Hölder Euler solutions below 1/3 whose energy follows any strictly decreasing profile, so the flux into vanishing scales is one-way for the whole box. Ando & Fisher (1963), [LIT-1294](record/literature.d/LIT-1294.md), and Turner & Sahani (2007), [LIT-1287](record/literature.d/LIT-1287.md), are registered Unavailable.
- Machta, Chachra, Transtrum & Sethna (2013) and Bousquet & Slotine (2015) registered and read: [THEORY-774](record/theory.d/THEORY-774.md) (Active: a hopping model's Fisher eigenvalues scale as t^{3/2−k}), [THEORY-777](record/theory.d/THEORY-777.md) (Proposed: Ising decimation rates) and [THEORY-771](record/theory.d/THEORY-771.md) (Proposed: a first-order trajectory-error bound for near-decomposable contracting systems).
- Giri, Kwon & Novack (2023, skimmed) and Schüler & Wiskott (2025) registered and read: [THEORY-772](record/theory.d/THEORY-772.md) (Proposed: Onsager's negative half with a local energy inequality, in an L³-based class), [THEORY-775](record/theory.d/THEORY-775.md) (Active: the linear optimum of variational slow feature analysis) and [CLAIM-394](record/claims.d/CLAIM-394.md) (demonstrated: in a reversible linear Gaussian VAR(1), slow features are exactly dynamically independent).
- Del Vecchio & Slotine (2013) registered and read: [THEORY-773](record/theory.d/THEORY-773.md) (Active: contraction bounds make the memoryless quasi-steady-state reduction accurate to O(ε) for all time, provided the reduced system contracts, a hypothesis the paper's Theorem 3 omits).
- Isett (2017, skimmed) and Chorin & Lu (2015) registered and read: [THEORY-821](record/theory.d/THEORY-821.md) (Proposed: Hölder Euler flows below 1/15 with the local energy inequality, dissipating only during a final drain), [THEORY-818](record/theory.d/THEORY-818.md) (Proposed: a NARMAX closure of Lorenz 96) and [CLAIM-398](record/claims.d/CLAIM-398.md) (demonstrated: a scalar linear coarse variable of a Gaussian VAR(1) is exactly ARMA, so its memory has a finite augmentation in its own history).
- Rosas et al. (2024) registered and read: [THEORY-820](record/theory.d/THEORY-820.md) (Active: informational closure, causal closure and dynamical independence coincide) and [THEORY-822](record/theory.d/THEORY-822.md) (Active: closure of a Markov-chain partition is strong lumpability).
- Lin & Lu (2019) registered and read: [THEORY-819](record/theory.d/THEORY-819.md) (Active: the discrete Mori–Zwanzig identity and its Wiener-projection form) and [CLAIM-397](record/claims.d/CLAIM-397.md) (demonstrated: a scalar process's Mori memory is fixed by its autocovariance, with Hankel rank one less).

### Changed

- [THEORY-661](record/theory.d/THEORY-661.md) no longer says Simon–Ando gives its separation "to order ε": the open statement of the theorem gives no rate.
- Open copies recorded for six registered works; Germano (1992), Smith & Woodruff (1998) and Eyink (2005) are Unavailable. The ACHA papers' publication dates are corrected to the publisher's online dates.

- [LIT-1127](record/literature.d/LIT-1127.md) (Simon & Ando 1961) is Unavailable: no lawful full text was reached.
- [THEORY-749](record/theory.d/THEORY-749.md), [THEORY-763](record/theory.d/THEORY-763.md), [NOTE-974](record/notes.d/NOTE-974.md) and [QUESTION-219](record/questions.d/QUESTION-219.md) cite the admissible Onsager theorem in place of saying it is not held; [THEORY-749](record/theory.d/THEORY-749.md) no longer calls Isett's solutions dissipative.
- [THEORY-742](record/theory.d/THEORY-742.md) and [NOTE-972](record/notes.d/NOTE-972.md) credit the λ = d/2 dividing line to Machta et al.; [THEORY-661](record/theory.d/THEORY-661.md), [QUESTION-221](record/questions.d/QUESTION-221.md), [CLAIM-386](record/claims.d/CLAIM-386.md) and [QUESTION-217](record/questions.d/QUESTION-217.md) cite the new readings.
- [QUESTION-219](record/questions.d/QUESTION-219.md), [THEORY-776](record/theory.d/THEORY-776.md) and [NOTE-1013](record/notes.d/NOTE-1013.md) cite the local Onsager theorem; [QUESTION-217](record/questions.d/QUESTION-217.md), [CLAIM-331](record/claims.d/CLAIM-331.md) and [LIT-1287](record/literature.d/LIT-1287.md) cite the variational reading of slow feature analysis.
- [THEORY-661](record/theory.d/THEORY-661.md), [QUESTION-222](record/questions.d/QUESTION-222.md) and [THEORY-771](record/theory.d/THEORY-771.md) cite Del Vecchio & Slotine.
- [THEORY-771](record/theory.d/THEORY-771.md) (Bousquet & Slotine) is promoted to Active at the owner's direction, on re-derivations recorded in record/promotion-audit/decisions/[THEORY-771](record/theory.d/THEORY-771.md).yaml; the entries that cited it as Proposed are updated.
- [QUESTION-219](record/questions.d/QUESTION-219.md), [THEORY-776](record/theory.d/THEORY-776.md) and [THEORY-772](record/theory.d/THEORY-772.md) cite Isett's globally dissipative flows; [QUESTION-222](record/questions.d/QUESTION-222.md) cites Chorin & Lu and the ARMA claim.
- [QUESTION-218](record/questions.d/QUESTION-218.md), [QUESTION-221](record/questions.d/QUESTION-221.md), [CLAIM-388](record/claims.d/CLAIM-388.md), [THEORY-755](record/theory.d/THEORY-755.md), [CLAIM-394](record/claims.d/CLAIM-394.md) and [NOTE-124](record/notes.d/NOTE-124.md) cite the reading of Rosas et al.
- [QUESTION-222](record/questions.d/QUESTION-222.md), [CLAIM-389](record/claims.d/CLAIM-389.md), [CLAIM-398](record/claims.d/CLAIM-398.md) and [NOTE-1028](record/notes.d/NOTE-1028.md) cite the reading of Lin & Lu.

### Fixed

- [NOTE-988](record/notes.d/NOTE-988.md) credited the log-loss refinability result to No, Ingber & Weissman (2016); it is No & Weissman (2015), and it concerns direct log-loss, which does not bear on the information bottleneck.

- [THEORY-661](record/theory.d/THEORY-661.md) said the record does not hold Simon & Ando (1961); it is [LIT-1127](record/literature.d/LIT-1127.md).

### Added

- At the owner's request, the record's position on the corporation as a psychopathic entity:
  - a question: is "psychopathic" a category error for a corporation, or can the construct, its affective features included, be assigned to it functionally ([QUESTION-265](record/questions.d/QUESTION-265.md));
  - a claim: a corporation can be an agent fit to be held responsible and the bearer of functional affect, so psychopathy's affective features can be assigned to it; it lacks remorse, functionally, when harm to others reaches its decisions only as a threat from regulators or markets and never as its own concern ([CLAIM-432](record/claims.d/CLAIM-432.md));
  - its objection: a corporation's functional remorse cannot be told from prudence, since every concern it has was installed for its own ends ([CLAIM-431](record/claims.d/CLAIM-431.md));
  - Wells Fargo's sales practices, from the board's own investigation, as a documented case ([CASE-151](record/cases.d/CASE-151.md));
  - psychopathy as one dimensional construct with no essential component, from Hare and Neumann ([THEORY-892](record/theory.d/THEORY-892.md)).
- Eight works: two read in full (the Wells Fargo report; Hare and Neumann 2008), six Unavailable (Bakan, Velasquez 1983 and 2003, Hare 1996, Boddy, Collins). A curation entry.

### Changed

- At the owner's word, [CLAIM-039](record/claims.d/CLAIM-039.md) (affective states as properties of organized systems, after Frijda) is Proposed again, from Deferred, and is the corporate-psychopathy claim's premise.

### Changed

- [CLAIM-052](record/claims.d/CLAIM-052.md)'s warrant corrected from interpretive to empirical, still
  Proposed. That interpretive framing operations generally do not commute
  is a generalization only an observation could settle, and its defeat
  condition is one. This carries out the promotion audit's batch-022
  decision ([ADR-047](record/decisions.d/ADR-047.md)).

### Changed

- [CLAIM-081](record/claims.d/CLAIM-081.md)'s warrant corrected from demonstrated to interpretive, still
  Proposed. It is the last [ADR-040](record/decisions.d/ADR-040.md) parent that was still marked
  demonstrated. Its general content is [CLAIM-270](record/claims.d/CLAIM-270.md)'s, and what it keeps is a
  reading of serial reconstruction through [CLAIM-056](record/claims.d/CLAIM-056.md) ([ADR-043](record/decisions.d/ADR-043.md)). This
  carries out the promotion audit's batch-029 decision ([ADR-047](record/decisions.d/ADR-047.md)).

Corrections from the promotion audit's batch 021 ([ADR-047](record/decisions.d/ADR-047.md)), statuses unchanged. [CLAIM-192](record/claims.d/CLAIM-192.md) and [CLAIM-271](record/claims.d/CLAIM-271.md) re-ground from [THEORY-127](record/theory.d/THEORY-127.md) to [THEORY-725](record/theory.d/THEORY-725.md), which holds the court-agenda possibility each uses. [CLAIM-030](record/claims.d/CLAIM-030.md) adds [THEORY-725](record/theory.d/THEORY-725.md) as its formal anchor and says List and Pettit's aggregation can fail, not that it always does. [CLAIM-126](record/claims.d/CLAIM-126.md)'s warrant becomes interpretive: its formal content is [CLAIM-268](record/claims.d/CLAIM-268.md)'s.

### Added

- From the exchange of 2026-10-20/21 on effective description, governance and legibility (U1–U27): three demonstrated claims, Active: closure under ordinary dynamics does not give governance-response sufficiency ([CLAIM-407](record/claims.d/CLAIM-407.md)), with its construction, the hidden governance bit ([CASE-125](record/cases.d/CASE-125.md)); the deficiency Γ is refinement-monotone while informational closure is monotone in neither direction ([CLAIM-409](record/claims.d/CLAIM-409.md)); and an identity-neutral constraint can, by weakening, make an unequal allocation of authority stable without deciding which party gains ([CLAIM-408](record/claims.d/CLAIM-408.md)). Seven Proposed claims: the conditions on an effective description are not of one kind ([CLAIM-401](record/claims.d/CLAIM-401.md)), individuation relative to a fixed criterion and not arbitrary ([CLAIM-405](record/claims.d/CLAIM-405.md)), deregulation as a change of governance profile ([CLAIM-410](record/claims.d/CLAIM-410.md)), control through the conditions of decision ([CLAIM-404](record/claims.d/CLAIM-404.md)), structural testimonial injustice as the trust loop ([CLAIM-406](record/claims.d/CLAIM-406.md)), inclusion is not participation ([CLAIM-403](record/claims.d/CLAIM-403.md)) and self-confirming categories ([CLAIM-402](record/claims.d/CLAIM-402.md)); a stipulated case, the regulator and two accounts ([CASE-123](record/cases.d/CASE-123.md)); two questions, the owner's leave-one-out ([QUESTION-252](record/questions.d/QUESTION-252.md)) and legibility's place in the meaning–authority loop ([QUESTION-253](record/questions.d/QUESTION-253.md)); ten Proposed TERMs: closure and which sense ([TERM-068](record/terms.d/TERM-068.md)), organizational closure ([TERM-070](record/terms.d/TERM-070.md)), causal state ([TERM-062](record/terms.d/TERM-062.md)), observational equivalence under a probe family ([TERM-069](record/terms.d/TERM-069.md)), the effective-description regime ([TERM-065](record/terms.d/TERM-065.md)), persistence and which sense ([TERM-071](record/terms.d/TERM-071.md)), agent as regulating its own coupling ([TERM-063](record/terms.d/TERM-063.md)), the governance-response profile ([TERM-067](record/terms.d/TERM-067.md)), capture ([TERM-066](record/terms.d/TERM-066.md)) and legibility ([TERM-064](record/terms.d/TERM-064.md)); thirty-three works registered unread, with a curation entry; three workbench entries.
- The works read on 2026-10-21, at the owner's request ("get started reading the proposed works. also this one"): Xu et al.'s theory of usable information registered ([LIT-1309](record/literature.d/LIT-1309.md)), the thirty-fourth work; twenty-three read Active (one, Hyzen et al., skimmed; Arthur through its 1983 working paper; Collins in an authorized translation) and eleven Unavailable under [ADR-041](record/decisions.d/ADR-041.md); twenty-three NOTEs ([NOTE-1048](record/notes.d/NOTE-1048.md), [NOTE-1044](record/notes.d/NOTE-1044.md), [NOTE-1033](record/notes.d/NOTE-1033.md), [NOTE-1034](record/notes.d/NOTE-1034.md), [NOTE-1037](record/notes.d/NOTE-1037.md), [NOTE-1032](record/notes.d/NOTE-1032.md), [NOTE-1045](record/notes.d/NOTE-1045.md), [NOTE-1038](record/notes.d/NOTE-1038.md), [NOTE-1036](record/notes.d/NOTE-1036.md), [NOTE-1052](record/notes.d/NOTE-1052.md), [NOTE-1043](record/notes.d/NOTE-1043.md), [NOTE-1053](record/notes.d/NOTE-1053.md), [NOTE-1046](record/notes.d/NOTE-1046.md), [NOTE-1031](record/notes.d/NOTE-1031.md), [NOTE-1040](record/notes.d/NOTE-1040.md), [NOTE-1039](record/notes.d/NOTE-1039.md), [NOTE-1047](record/notes.d/NOTE-1047.md), [NOTE-1050](record/notes.d/NOTE-1050.md), [NOTE-1041](record/notes.d/NOTE-1041.md), [NOTE-1035](record/notes.d/NOTE-1035.md), [NOTE-1049](record/notes.d/NOTE-1049.md), [NOTE-1051](record/notes.d/NOTE-1051.md), [NOTE-1042](record/notes.d/NOTE-1042.md)); thirty-two THEORYs, twenty-two Active ([THEORY-846](record/theory.d/THEORY-846.md), [THEORY-840](record/theory.d/THEORY-840.md), [THEORY-861](record/theory.d/THEORY-861.md), [THEORY-839](record/theory.d/THEORY-839.md), [THEORY-835](record/theory.d/THEORY-835.md), [THEORY-844](record/theory.d/THEORY-844.md), [THEORY-847](record/theory.d/THEORY-847.md), [THEORY-848](record/theory.d/THEORY-848.md), [THEORY-849](record/theory.d/THEORY-849.md), [THEORY-843](record/theory.d/THEORY-843.md), [THEORY-855](record/theory.d/THEORY-855.md), [THEORY-845](record/theory.d/THEORY-845.md), [THEORY-863](record/theory.d/THEORY-863.md), [THEORY-856](record/theory.d/THEORY-856.md), [THEORY-842](record/theory.d/THEORY-842.md), [THEORY-837](record/theory.d/THEORY-837.md), [THEORY-851](record/theory.d/THEORY-851.md), [THEORY-850](record/theory.d/THEORY-850.md), [THEORY-860](record/theory.d/THEORY-860.md), [THEORY-836](record/theory.d/THEORY-836.md), [THEORY-862](record/theory.d/THEORY-862.md), [THEORY-833](record/theory.d/THEORY-833.md)) and ten Proposed ([THEORY-853](record/theory.d/THEORY-853.md), [THEORY-841](record/theory.d/THEORY-841.md), [THEORY-858](record/theory.d/THEORY-858.md), [THEORY-838](record/theory.d/THEORY-838.md), [THEORY-852](record/theory.d/THEORY-852.md), [THEORY-854](record/theory.d/THEORY-854.md), [THEORY-857](record/theory.d/THEORY-857.md), [THEORY-864](record/theory.d/THEORY-864.md), [THEORY-859](record/theory.d/THEORY-859.md), [THEORY-834](record/theory.d/THEORY-834.md)); and one demonstrated claim, Active, that causal abstraction as those papers define it does not secure governance-response sufficiency ([CLAIM-399](record/claims.d/CLAIM-399.md)). The curation entry records the outcomes and the corrections the readings made.

- From the owner's review of 2026-10-21: [CLAIM-400](record/claims.d/CLAIM-400.md) (demonstrated, Active), that a maintained legibility state in the linearized meaning–authority model destabilizes symmetry exactly when stronger two-variable couplings would, while adding a slow mode no two-variable model has, with its construction [CASE-124](record/cases.d/CASE-124.md); [QUESTION-253](record/questions.d/QUESTION-253.md) is Answered by it.

### Changed

- Dated notes of 2026-10-21, from the same exchange, on fifty-four entries it re-derived, misread or bore on, each claim, question, term, case or reading unchanged: [CLAIM-025](record/claims.d/CLAIM-025.md), [CLAIM-027](record/claims.d/CLAIM-027.md), [CLAIM-044](record/claims.d/CLAIM-044.md), [CLAIM-086](record/claims.d/CLAIM-086.md), [CLAIM-122](record/claims.d/CLAIM-122.md), [CLAIM-152](record/claims.d/CLAIM-152.md), [CLAIM-170](record/claims.d/CLAIM-170.md), [CLAIM-174](record/claims.d/CLAIM-174.md), [CLAIM-194](record/claims.d/CLAIM-194.md), [CLAIM-199](record/claims.d/CLAIM-199.md), [CLAIM-219](record/claims.d/CLAIM-219.md), [CLAIM-277](record/claims.d/CLAIM-277.md), [CLAIM-294](record/claims.d/CLAIM-294.md), [CLAIM-329](record/claims.d/CLAIM-329.md), [CLAIM-331](record/claims.d/CLAIM-331.md), [CLAIM-335](record/claims.d/CLAIM-335.md), [CLAIM-336](record/claims.d/CLAIM-336.md), [CLAIM-338](record/claims.d/CLAIM-338.md), [CLAIM-341](record/claims.d/CLAIM-341.md), [CLAIM-342](record/claims.d/CLAIM-342.md), [CLAIM-348](record/claims.d/CLAIM-348.md), [CLAIM-349](record/claims.d/CLAIM-349.md), [CLAIM-350](record/claims.d/CLAIM-350.md), [CLAIM-352](record/claims.d/CLAIM-352.md), [CLAIM-354](record/claims.d/CLAIM-354.md), [CLAIM-363](record/claims.d/CLAIM-363.md), [CLAIM-367](record/claims.d/CLAIM-367.md), [CLAIM-389](record/claims.d/CLAIM-389.md), [CLAIM-392](record/claims.d/CLAIM-392.md) and [CLAIM-397](record/claims.d/CLAIM-397.md); [QUESTION-007](record/questions.d/QUESTION-007.md), [QUESTION-011](record/questions.d/QUESTION-011.md), [QUESTION-028](record/questions.d/QUESTION-028.md), [QUESTION-029](record/questions.d/QUESTION-029.md), [QUESTION-041](record/questions.d/QUESTION-041.md), [QUESTION-071](record/questions.d/QUESTION-071.md), [QUESTION-072](record/questions.d/QUESTION-072.md), [QUESTION-086](record/questions.d/QUESTION-086.md), [QUESTION-093](record/questions.d/QUESTION-093.md), [QUESTION-115](record/questions.d/QUESTION-115.md), [QUESTION-117](record/questions.d/QUESTION-117.md), [QUESTION-132](record/questions.d/QUESTION-132.md), [QUESTION-217](record/questions.d/QUESTION-217.md), [QUESTION-218](record/questions.d/QUESTION-218.md) and [QUESTION-221](record/questions.d/QUESTION-221.md); [TERM-009](record/terms.d/TERM-009.md), [TERM-044](record/terms.d/TERM-044.md) and [TERM-060](record/terms.d/TERM-060.md); [CASE-112](record/cases.d/CASE-112.md) (its hysteresis placed in the tilt, not the constraint); [THEORY-424](record/theory.d/THEORY-424.md), [THEORY-470](record/theory.d/THEORY-470.md) and [THEORY-820](record/theory.d/THEORY-820.md); [LIT-751](record/literature.d/LIT-751.md) and [LIT-1021](record/literature.d/LIT-1021.md).
- From the readings of 2026-10-21: this PR's entries cite the works now read and drop their "not held" and "unread" statements ([TERM-064](record/terms.d/TERM-064.md), [TERM-066](record/terms.d/TERM-066.md), [TERM-065](record/terms.d/TERM-065.md), [CLAIM-407](record/claims.d/CLAIM-407.md), [CLAIM-409](record/claims.d/CLAIM-409.md), [CLAIM-404](record/claims.d/CLAIM-404.md), [CLAIM-406](record/claims.d/CLAIM-406.md), [CLAIM-403](record/claims.d/CLAIM-403.md), [CLAIM-402](record/claims.d/CLAIM-402.md), [CLAIM-408](record/claims.d/CLAIM-408.md), [CLAIM-410](record/claims.d/CLAIM-410.md), [CASE-125](record/cases.d/CASE-125.md), [CASE-123](record/cases.d/CASE-123.md), [QUESTION-253](record/questions.d/QUESTION-253.md)), with new THEORYs in `grounds` where they bear; new dated notes on [CLAIM-225](record/claims.d/CLAIM-225.md), [QUESTION-110](record/questions.d/QUESTION-110.md), [TERM-043](record/terms.d/TERM-043.md), [THEORY-143](record/theory.d/THEORY-143.md), [THEORY-404](record/theory.d/THEORY-404.md) and [THEORY-755](record/theory.d/THEORY-755.md); and the notes of the same day on [CLAIM-025](record/claims.d/CLAIM-025.md), [CLAIM-199](record/claims.d/CLAIM-199.md) (which gains [THEORY-846](record/theory.d/THEORY-846.md) in `grounds`), [CLAIM-342](record/claims.d/CLAIM-342.md), [CLAIM-348](record/claims.d/CLAIM-348.md), [CLAIM-350](record/claims.d/CLAIM-350.md), [QUESTION-028](record/questions.d/QUESTION-028.md), [QUESTION-072](record/questions.d/QUESTION-072.md), [QUESTION-117](record/questions.d/QUESTION-117.md), [CASE-112](record/cases.d/CASE-112.md), [LIT-751](record/literature.d/LIT-751.md) and [LIT-1021](record/literature.d/LIT-1021.md) extended. Each claim, question, term, case or reading is unchanged.

- From the same review: [CLAIM-408](record/claims.d/CLAIM-408.md)'s title says an unequal allocation, not domination, since the stable asymmetry is arbitrarily small near the threshold; [TERM-066](record/terms.d/TERM-066.md) is renamed "interpretive capture", leaving "capture" an umbrella word.

- From the owner's second review of 2026-10-21: [ADR-046](record/decisions.d/ADR-046.md) is accepted, and eight TERMs are adopted (Active): legibility ([TERM-064](record/terms.d/TERM-064.md)), the governance-response profile ([TERM-067](record/terms.d/TERM-067.md)), closure and which sense ([TERM-068](record/terms.d/TERM-068.md)), organizational closure ([TERM-070](record/terms.d/TERM-070.md)), observational equivalence under a probe family ([TERM-069](record/terms.d/TERM-069.md)), persistence and which sense ([TERM-071](record/terms.d/TERM-071.md)), the effective-description regime, revised to keep the description out of the regime ([TERM-065](record/terms.d/TERM-065.md)), and causal state, revised to separate the states from the machine ([TERM-062](record/terms.d/TERM-062.md)). Interpretive capture ([TERM-066](record/terms.d/TERM-066.md)) and the rival agent ([TERM-063](record/terms.d/TERM-063.md)) stay Proposed; the capture term now calls the instability a possible mechanism, not the definition.

### Fixed

- The μ arrow of [CASE-124](record/cases.d/CASE-124.md) and [CLAIM-400](record/claims.d/CLAIM-400.md) was described as the question's κ′ reading; it is a direct effect of the regime on scoring, and a regime that only varies κ′ enters at second order.

- [QUESTION-222](record/questions.d/QUESTION-222.md)'s inactive-ok annotation listed [LIT-1245](record/literature.d/LIT-1245.md), [LIT-1253](record/literature.d/LIT-1253.md) and [LIT-1259](record/literature.d/LIT-1259.md) as Deferred; all three are Active, and it now names only [LIT-1251](record/literature.d/LIT-1251.md), Unavailable.
- [TERM-067](record/terms.d/TERM-067.md) said the governance-response profile narrows [TERM-043](record/terms.d/TERM-043.md)'s causal component, as that component with the identity correspondence. The readings showed that component is zero for the hidden governance bit, where sufficiency fails; the `refines` link, and its converse on [TERM-043](record/terms.d/TERM-043.md), are removed, and the relation is [CLAIM-399](record/claims.d/CLAIM-399.md).
- Inactive-ok annotations written earlier in this PR named works as Deferred that the readings made Active or Unavailable ([CLAIM-025](record/claims.d/CLAIM-025.md), [CLAIM-342](record/claims.d/CLAIM-342.md), [CLAIM-348](record/claims.d/CLAIM-348.md), [QUESTION-117](record/questions.d/QUESTION-117.md), [LIT-751](record/literature.d/LIT-751.md), [LIT-1021](record/literature.d/LIT-1021.md)); they now give the current status, or are removed where the work is Active.

### Added

- From the exchange of 2026-10-21 on experience and interpretation: the owner's thesis that experience is constituted by interpretive organization, not produced by it ([CLAIM-412](record/claims.d/CLAIM-412.md), Proposed), with its objection that, under the broad nonphenomenal definition, much processing not shown to be experiential counts as interpretation, so the thesis lacks a sufficiency condition ([CLAIM-411](record/claims.d/CLAIM-411.md), counter); the owner's grounding premise restated as a relation that comes apart from whether an experience occurs ([CLAIM-413](record/claims.d/CLAIM-413.md), resting on [CLAIM-342](record/claims.d/CLAIM-342.md)); two questions: what makes an interpretive organization an experiential perspective ([QUESTION-254](record/questions.d/QUESTION-254.md), narrowing [QUESTION-046](record/questions.d/QUESTION-046.md)) and whether a model that genuinely fails to glue can take part in one unified experience ([QUESTION-255](record/questions.d/QUESTION-255.md), set against [CLAIM-153](record/claims.d/CLAIM-153.md)); twenty-two works registered unread; a note on [CASE-114](record/cases.d/CASE-114.md); a workbench entry and a curation entry.
- From U8–U11 of the same exchange (2026-10-22): two Proposed terms, interpretation ([TERM-073](record/terms.d/TERM-073.md)) and perspective in three senses, organizational, represented and phenomenal ([TERM-072](record/terms.d/TERM-072.md)); a demonstrated claim that matched ordinary trajectories can conceal differences in an interpretation's efficacy, its endogenous allocation and the maintenance of its constraints, which a specified intervention exposes ([CLAIM-414](record/claims.d/CLAIM-414.md), Active), with its construction [CASE-126](record/cases.d/CASE-126.md); dated notes on [QUESTION-254](record/questions.d/QUESTION-254.md), [QUESTION-255](record/questions.d/QUESTION-255.md), [CLAIM-411](record/claims.d/CLAIM-411.md) and [CLAIM-412](record/claims.d/CLAIM-412.md); a second workbench entry.
- The twenty-two registered works sought on 2026-10-22: eighteen read in full from lawful copies, each with a NOTE, and nineteen Proposed THEORYs filed from them; He et al., Isaac, Villalobos & Cea and Putnam are Unavailable. Dated notes on the exchange's claims, questions and terms, and on [CLAIM-355](record/claims.d/CLAIM-355.md), record how the readings bear; a curation entry lists the corrections they made to the exchange.

### Changed

- After a review the owner relayed on 2026-10-22: the counter-claim no longer says "any definition" or "most interpretation"; the unity question separates conflicts that glue from genuine non-gluing; the perspective question's grounding condition is narrowed to current veridical grounding and it gains the perspectival-target problem; the perspective term keeps a represented perspective apart from a represented owner; the demonstrated claim is narrowed to its two constructions; and the constitutive thesis no longer lists rival or confounded readings as its grounds.

### Added

- [LIT-1298](record/literature.d/LIT-1298.md) and [NOTE-1023](record/notes.d/NOTE-1023.md): Lessig's *Remix: Making Art and Commerce
  Thrive in the Hybrid Economy* (2008), read in full from the CC BY-NC
  Bloomsbury Academic edition. It is the record's first work on remix
  culture.

### Changed

- [LIT-1121](record/literature.d/LIT-1121.md) (*Convergence Culture*) and [LIT-1143](record/literature.d/LIT-1143.md) (*Spreadable Media*):
  Deferred → Unavailable under [ADR-041](record/decisions.d/ADR-041.md), after a search for a lawful full
  text reached none.

### Added

- Seven works in conversation with Lessig's *Remix* on property and
  expression, each read in full with a NOTE:
  - *Andy Warhol Foundation v. Goldsmith* (2023), [LIT-1302](record/literature.d/LIT-1302.md);
  - the Copyright Office's *Generative AI Training* report (2025),
    [LIT-1293](record/literature.d/LIT-1293.md), flagged `anthology-candidate`;
  - Boyle's *The Public Domain* (2008), [LIT-1301](record/literature.d/LIT-1301.md);
  - Boyle's *The Line* (2024), [LIT-1288](record/literature.d/LIT-1288.md);
  - Perzanowski & Schultz's *The End of Ownership* (2016), [LIT-1297](record/literature.d/LIT-1297.md);
  - Tushnet's "Worth a Thousand Words" (2012), [LIT-1303](record/literature.d/LIT-1303.md);
  - Balganesh's review of Drassinower (2017), [LIT-1291](record/literature.d/LIT-1291.md).
- Three more registered as Unavailable after a search reached no lawful
  copy: Drassinower ([LIT-1285](record/literature.d/LIT-1285.md)), Netanel ([LIT-1286](record/literature.d/LIT-1286.md)), McLeod &
  DiCola ([LIT-1290](record/literature.d/LIT-1290.md)).

### Added

- [CASE-121](record/cases.d/CASE-121.md): one melody from a 1951 gospel record to a 2005 Katrina
  protest song, each link a different relation (illustrates [CLAIM-002](record/claims.d/CLAIM-002.md)
  and [CLAIM-210](record/claims.d/CLAIM-210.md)).
- [CASE-122](record/cases.d/CASE-122.md): *Warhol v. Goldsmith*, one rendering judged by purpose
  and by meaning (illustrates [CLAIM-034](record/claims.d/CLAIM-034.md) and [CLAIM-210](record/claims.d/CLAIM-210.md)).
- [CLAIM-393](record/claims.d/CLAIM-393.md): a counter to [CLAIM-174](record/claims.d/CLAIM-174.md). Attributions of agency to
  artifacts track whether the mechanism is understood, so they cannot
  defeat its test.

### Added

- From the exchange of 2026-10-22, "Ben Franklin Effect Explained":
  - the favour as a perspectival invitation, an interaction that makes available a way of relating its participants' perspectives did not hold ([CLAIM-430](record/claims.d/CLAIM-430.md));
  - an intervention on a coupled interpretation–cooperation loop changes its state or its coupling, and only the second changes how later evidence is taken ([CLAIM-429](record/claims.d/CLAIM-429.md));
  - material interdependence does not fix the perspective that organizes it ([CLAIM-428](record/claims.d/CLAIM-428.md));
  - cases: Franklin's borrowed book ([CASE-143](record/cases.d/CASE-143.md)), two friendships across a group line ([CASE-146](record/cases.d/CASE-146.md)), Kalla and Broockman's conversations against arguments ([CASE-147](record/cases.d/CASE-147.md)), Kleinman, Liu and Redding's economic and political alignment ([CASE-150](record/cases.d/CASE-150.md));
  - a question refining [QUESTION-259](record/questions.d/QUESTION-259.md), on state against coupling and taking part against being told ([QUESTION-262](record/questions.d/QUESTION-262.md)).
- From the exchange of 2026-10-23, "Framework Overview Request":
  - three grades of evidence for the organizational-perspective framework, of which only out-predicting the strongest alternatives under intervention bears on its defeater ([CLAIM-427](record/claims.d/CLAIM-427.md));
  - when the organizations of significance, authority and reproduction coincide or diverge, proposed as the manuscript's research problem ([QUESTION-264](record/questions.d/QUESTION-264.md));
  - three proposed studies: the evaluator that stops tracking ([CASE-144](record/cases.d/CASE-144.md)), perspective transplantation ([CASE-148](record/cases.d/CASE-148.md)), perspective without collective agency ([CASE-145](record/cases.d/CASE-145.md));
  - Bigand et al.'s dance synchrony, read, as [CASE-149](record/cases.d/CASE-149.md) and a Proposed THEORY answering [QUESTION-063](record/questions.d/QUESTION-063.md) in part ([THEORY-891](record/theory.d/THEORY-891.md));
  - [QUESTION-063](record/questions.d/QUESTION-063.md) split under [ADR-049](record/decisions.d/ADR-049.md): its negative part, answered by [THEORY-275](record/theory.d/THEORY-275.md), is the Answered child [QUESTION-263](record/questions.d/QUESTION-263.md).
- Twenty-six works registered: one read, three Unavailable, twenty-two unread. Two workbench entries and a curation entry.

### Changed

- Dated notes on the proposed studies [CASE-045](record/cases.d/CASE-045.md), [CASE-078](record/cases.d/CASE-078.md), [CASE-092](record/cases.d/CASE-092.md), [CASE-101](record/cases.d/CASE-101.md), [CASE-108](record/cases.d/CASE-108.md), [CASE-114](record/cases.d/CASE-114.md) and [CASE-117](record/cases.d/CASE-117.md), and on [QUESTION-063](record/questions.d/QUESTION-063.md), [QUESTION-089](record/questions.d/QUESTION-089.md) and [QUESTION-118](record/questions.d/QUESTION-118.md), saying what published results already settle and what is left.
- [QUESTION-063](record/questions.d/QUESTION-063.md) reworded to its open remainder, and [THEORY-275](record/theory.d/THEORY-275.md)'s `answers` moved to the child.
- At the owner's direction, a CASE can name where the record got it: `reported_in` links it to LITs, NOTEs and THEORYs, with the converse `reports` ([ADR-051](record/decisions.d/ADR-051.md)). Used on the four documented cases this filing adds; existing cases are not backfilled.
- Two claims' references to other claims moved from `uses`, which names TERMs only, to `rests_on` and `complements`.

### Added

- From the exchange of 2026-10-23/24: the owner's reading of wanting as prediction under do(), with model-based and cue-triggered levels kept apart and wanting kept apart from will ([CLAIM-447](record/claims.d/CLAIM-447.md)); a learned prior over which processes govern, as a mechanism for durable authority and for amortization, where persistence alone is not amortization ([CLAIM-443](record/claims.d/CLAIM-443.md)); cycles in an organization's wins read as nonintegrability, separated from tension and from cognitive dissonance ([CLAIM-451](record/claims.d/CLAIM-451.md)); governance-maintained anxiety as a candidate answer to [QUESTION-045](record/questions.d/QUESTION-045.md) ([CLAIM-446](record/claims.d/CLAIM-446.md)), and its form across institutions and states ([CLAIM-445](record/claims.d/CLAIM-445.md)); two objections to [CLAIM-440](record/claims.d/CLAIM-440.md), on contested rankings against frustrated demands ([CLAIM-449](record/claims.d/CLAIM-449.md)) and on coherence produced by selective contestation ([CLAIM-448](record/claims.d/CLAIM-448.md)); three standards for a communicative distinction, connecting Amari and Watanabe to the pragmatic-transport line ([CLAIM-450](record/claims.d/CLAIM-450.md)). Four cases: a proposed sentry study ([CASE-153](record/cases.d/CASE-153.md)), a legibility filter giving [CASE-124](record/cases.d/CASE-124.md)'s ν ([CASE-156](record/cases.d/CASE-156.md)), a bounded-observer trade-off between tasks ([CASE-154](record/cases.d/CASE-154.md)), and a singular response model ([CASE-152](record/cases.d/CASE-152.md)). Also a question on accurate evaluations denied authority ([QUESTION-270](record/questions.d/QUESTION-270.md)), a Proposed term for belief ([TERM-079](record/terms.d/TERM-079.md)), works registered unread, and dated notes on fourteen entries. A workbench entry and a curation entry.

- At the owner's request, Soma et al., "The hive mind is a single reinforcement learning agent" (arXiv:2410.17517), filed and read in full ([LIT-1484](record/literature.d/LIT-1484.md), [NOTE-1132](record/notes.d/NOTE-1132.md)), with two Proposed THEORYs: the proved equivalence of imitation with bandit learning in expectation ([THEORY-899](record/theory.d/THEORY-899.md)) and its finite-population limits ([THEORY-905](record/theory.d/THEORY-905.md)).

- At the owner's direction, the replicator tools applied to the record's governance dynamics: a construction reading authority as a replicator population, with evidence-tracking authority as Bayes' rule and lock-in under authority-dependent scoring at an explicit threshold ([CASE-155](record/cases.d/CASE-155.md)), and the claim that the replicator model is the special case of the meaning–authority–legibility model in which interpretation is the authority-weighted mixture and legibility keeps no memory ([CLAIM-444](record/claims.d/CLAIM-444.md)).

### Changed

- The third review of PR [#327](https://github.com/dmarx/nucleation/issues/327), left unapplied at merge: [TERM-078](record/terms.d/TERM-078.md) no longer derives resumption from a Lyapunov function, and [TERM-077](record/terms.d/TERM-077.md)'s four senses of currency are stated as an evidential pair and a representational pair, not a chain of implications.

### Added

- At the owner's request, the record's first multi-agent learning and learning-in-games literature: twenty-one works registered and sought, eighteen read and three Unavailable, with twenty-three Proposed THEORYs (curation entry of 2026-10-24); a question on capture-resistant evaluation of an organization's processes ([QUESTION-271](record/questions.d/QUESTION-271.md)); and dated notes on the replicator construction and claim, the cycles claim, the anxiety claim and the correlated-equilibrium reading of institutions.
- At the owner's direction, the owner's 2014 BoostTheVote model filed as an executed study, re-run through a Python port in scratch/formal/: full-information multiplicative weights as the counterpart of the replicator construction, with the capture its author predicted and a proposed three-axis extension ([CASE-157](record/cases.d/CASE-157.md)).
- At the owner's direction, the BoostTheVote extension run (scratch/formal/boost_the_vote_extension.py): an endogenous metric and outcome-conditional observation each suffice for lock-in, bandit feedback over voters changes little, and age-targeted renewal rescues all but full endogeneity; recorded in [CASE-157](record/cases.d/CASE-157.md), with a note on [CLAIM-446](record/claims.d/CLAIM-446.md).

The narrowing-loss sweep ([ADR-047](record/decisions.d/ADR-047.md) v4, batch 068) files the wider claims five narrowed THEORYs had dropped as new Proposed THEORYs: E. coli regulatory memory, the data-limited horizon mechanism, optimizer-driven skill order, grokking's critical fraction for addition, and SGD noise toward mirror subspaces.

### Added

- From the exchange of 2026-10-22, "Graph Learning Applications": the owner's thesis that the record's selves are better described as organizational perspectives, narrowed to [TERM-045](record/terms.d/TERM-045.md)'s senses 2, 3, 5 and 6 with the subject sense left apart ([CLAIM-417](record/claims.d/CLAIM-417.md)); reflexive governance of a perspective, re-scoping [CLAIM-284](record/claims.d/CLAIM-284.md) ([CLAIM-424](record/claims.d/CLAIM-424.md)); competition over the tests that measure competitors ([CLAIM-416](record/claims.d/CLAIM-416.md)); story, perspective and descent as separate legacies ([CLAIM-420](record/claims.d/CLAIM-420.md)); the owner's thesis that timescales help decide authority in political collectives ([CLAIM-423](record/claims.d/CLAIM-423.md)); act, procedure and maintained capacity ([CLAIM-422](record/claims.d/CLAIM-422.md)); the imagined audience as a false unity ([CLAIM-415](record/claims.d/CLAIM-415.md)); and the owner's observation that the record amends its grammar when a move does not fit, the first reply to [CLAIM-181](record/claims.d/CLAIM-181.md) ([CLAIM-419](record/claims.d/CLAIM-419.md)). All Proposed.
- Three questions: what continuity self-governance needs and what can be supplied from outside ([QUESTION-256](record/questions.d/QUESTION-256.md)); how perspectives are generated and when one governs itself, refining [QUESTION-090](record/questions.d/QUESTION-090.md) ([QUESTION-259](record/questions.d/QUESTION-259.md)); and how a manuscript should be chosen from the record ([QUESTION-258](record/questions.d/QUESTION-258.md)).
- Eleven cases, six documented: Clive Wearing ([CASE-137](record/cases.d/CASE-137.md)), the Brookhollow fire ([CASE-135](record/cases.d/CASE-135.md)), Challenger to Columbia ([CASE-138](record/cases.d/CASE-138.md)), United 173 and Crew Resource Management ([CASE-127](record/cases.d/CASE-127.md)), party realignment ([CASE-133](record/cases.d/CASE-133.md)), Gracie jiu-jitsu against luta livre ([CASE-130](record/cases.d/CASE-130.md)); and the record's own [ADR-044](record/decisions.d/ADR-044.md) as a specimen ([CASE-131](record/cases.d/CASE-131.md)); with four stipulated: Northstar's commander handoff ([CASE-134](record/cases.d/CASE-134.md)), the alarm that learned and the alarm that was disabled ([CASE-129](record/cases.d/CASE-129.md)), the voluntary delegation ([CASE-128](record/cases.d/CASE-128.md)), and one complaint under two taxonomies ([CASE-132](record/cases.d/CASE-132.md)).
- Twenty-three works registered unread, two workbench entries and a curation entry.
- From the branch of the same exchange (B37–B39): kinds of interruption of a perspective, of activation, enactment and reproduction ([CLAIM-421](record/claims.d/CLAIM-421.md)); a perspective is not thereby an agent, and perspectival, agential and institutional boundaries need not coincide ([CLAIM-418](record/claims.d/CLAIM-418.md)); two questions, on interruption and reconstruction ([QUESTION-257](record/questions.d/QUESTION-257.md)) and on when a perspective is an agent's own ([QUESTION-260](record/questions.d/QUESTION-260.md), refining [QUESTION-093](record/questions.d/QUESTION-093.md)); two documented cases, the doorway effect ([CASE-136](record/cases.d/CASE-136.md)) and Chinese martial traditions through the Cultural Revolution ([CASE-139](record/cases.d/CASE-139.md)); six works registered unread, a workbench entry and a curation entry.
- From a proposal the owner relayed on 2026-10-22, "Toward a controlled vocabulary for Nucleation": a Proposed term for organization in four senses, relational arrangement (the default), organizational maintenance, collective institution and organizational closure ([TERM-074](record/terms.d/TERM-074.md)); and a Proposed usage protocol, under which a claim that calls something organized, a perspective, an agent, effective, exhausted, constituted or grounded says which sense, target or criterion it means ([ADR-050](record/decisions.d/ADR-050.md)).
- A works term for the owner's manuscript from the exchange, "The Organization of Perspective: Character, Practical Authority, and Historical Persistence Across Minds and Institutions" (`organization-of-perspective`), with [CLAIM-417](record/claims.d/CLAIM-417.md), [CLAIM-424](record/claims.d/CLAIM-424.md), [CLAIM-420](record/claims.d/CLAIM-420.md), [CLAIM-423](record/claims.d/CLAIM-423.md), [CLAIM-422](record/claims.d/CLAIM-422.md) and [CLAIM-418](record/claims.d/CLAIM-418.md) marked as in it; and four works terms for the 6,000-word essays it was assembled from, "The Self Without a Sovereign" (`self-without-a-sovereign`), "Who Gets to Say Stop?" (`who-gets-to-say-stop`), "The Character That Changed Parties" (`character-that-changed-parties`) and "Who Makes the Promise When Governments Change?" (`who-makes-the-promise`), each with the claims it argues. [CLAIM-355](record/claims.d/CLAIM-355.md) joins the first essay and the synthesis, and [CLAIM-329](record/claims.d/CLAIM-329.md) the third and the synthesis. Membership is not endorsement: every claim marked stays Proposed.

### Changed

- Dated notes on [TERM-072](record/terms.d/TERM-072.md) (the owner's U31, and a perspective with many carriers, for the owner's adoption decision), [TERM-045](record/terms.d/TERM-045.md), [CLAIM-355](record/claims.d/CLAIM-355.md), [CLAIM-284](record/claims.d/CLAIM-284.md), [CLAIM-329](record/claims.d/CLAIM-329.md), [CLAIM-364](record/claims.d/CLAIM-364.md), [CASE-014](record/cases.d/CASE-014.md) and [CASE-036](record/cases.d/CASE-036.md). None changes what the entry holds.
- After a review relayed by the owner from the branch: [TERM-045](record/terms.d/TERM-045.md)'s note no longer has Clive Wearing failing persistence; the organizational-perspectives claim and [TERM-072](record/terms.d/TERM-072.md)'s note allow a perspective realized across several carriers, and no longer reduce narrative, presented and modeled selves to representations of a perspective; reflexive governance is attributed to a perspective-bearing organization; the party-realignment case and the note on [CLAIM-329](record/claims.d/CLAIM-329.md) no longer say the parties' perspective did not persist; the Challenger case no longer implies one unchanged cause; the timescales and competition claims gain qualifications; two documented cases say their standing is the event's, not the reading's.
- A note on [TERM-072](record/terms.d/TERM-072.md) lists what "the same perspective" can mean (realization, kind, lineage, distributed realization, representation) and keeps the relayed restatement of sense 1 as a candidate. The definition is unchanged.
- After the owner's final review of 2026-10-22: the agency claim no longer asserts that agency is exercised through perspectives in general, only where a perspective contributes; the interruption claim is about the dispositions, capacities and reproductive relationships that outlast a perspective's enactment, and its defeat condition no longer turns on the doorway effect; the organization term no longer calls closure its strongest sense; [ADR-050](record/decisions.d/ADR-050.md) exempts unambiguous ordinary uses.

### Added

- Readings of the 29 works registered unread from the exchange of 2026-10-22, "Graph Learning Applications" ([LIT-1365](record/literature.d/LIT-1365.md) to [LIT-1393](record/literature.d/LIT-1393.md)): 17 read and 4 skimmed, each with a NOTE; 8 Unavailable under [ADR-041](record/decisions.d/ADR-041.md). Seven Proposed THEORYs: event segmentation, the doorway effect as interference between event models, the majority illusion, Swidler's two models of culture, path dependence in politics, the county legacy of slavery, and the Ledger of Will's revision closure. A curation entry lists the outcomes.

### Changed

- Dated notes on 18 entries the readings bear on, among them the exchange's claims and cases, [THEORY-242](record/theory.d/THEORY-242.md) and [QUESTION-112](record/questions.d/QUESTION-112.md). Three case titles are corrected against their sources: the doorway effect ([CASE-136](record/cases.d/CASE-136.md)), United 173 ([CASE-127](record/cases.d/CASE-127.md)) and the Brookhollow mayday ([CASE-135](record/cases.d/CASE-135.md)).
- Several LIT summaries corrected by their readings: [LIT-1374](record/literature.d/LIT-1374.md), [LIT-1386](record/literature.d/LIT-1386.md), [LIT-1388](record/literature.d/LIT-1388.md), [LIT-1392](record/literature.d/LIT-1392.md) and [LIT-1379](record/literature.d/LIT-1379.md). Each version note gives the reason.

### Changed

- From the owner's v2.7–v2.9 proposals, checked against the stored results of the Perspective Population Lab's v2.7 to v2.9 (dmarx/PerspectiveLab@c54617e: trained affect, the perspective engine and endogenous frames): new dated notes of 2026-10-26 on six entries. [CLAIM-427](record/claims.d/CLAIM-427.md) (v2.7 matches the information given to fitted predictors but not their complexity, its uptake predictor loses in the world built for it, and v2.9's ridge rival is weaker, not stronger), [CLAIM-278](record/claims.d/CLAIM-278.md) (no added constraint, and a hand-written frame that helps or harms as its reading fits the world), [CLAIM-336](record/claims.d/CLAIM-336.md) (frames enter the lab, and in v2.9 the engine reduces to a one-feature selector), [QUESTION-088](record/questions.d/QUESTION-088.md) (habit fitted within one phenomenon, and reframing built), [QUESTION-270](record/questions.d/QUESTION-270.md) (predictors fitted to the same experiences, with registration and authority set by the experimenter rather than measured) and [QUESTION-273](record/questions.d/QUESTION-273.md) (one mechanism built, with grant and exclusion effect measured). Each is titled "(later)" where the entry already had a note of that date. The proposed notes on [CLAIM-437](record/claims.d/CLAIM-437.md), [CLAIM-286](record/claims.d/CLAIM-286.md), [CLAIM-453](record/claims.d/CLAIM-453.md), [CASE-160](record/cases.d/CASE-160.md) and [QUESTION-031](record/questions.d/QUESTION-031.md) were not applied. No title, status or warrant changed. A workbench entry records what was kept, corrected and declined.

The titles of [CLAIM-033](record/claims.d/CLAIM-033.md), [CLAIM-087](record/claims.d/CLAIM-087.md) and [CLAIM-105](record/claims.d/CLAIM-105.md) are restated as claims of prevalence, to match the defeat conditions they were given on 2026-10-10 after [CLAIM-238](record/claims.d/CLAIM-238.md) (promotion audit, batch 034). Each title still said "can", which one instance settles and no rate defeats. Defeat conditions, statuses and warrants are unchanged.

### Added

- From an owner-supplied package of proposed updates ("Priority A"), checked against the stored results of the Perspective Population Lab, now held as dmarx/PerspectiveLab (v1.0 at @41e56df, v1.1–v1.8 at @7e2edc2, v1.9–v2.2 at @9f82bfd): four Proposed cases. Capture and selectively admitted evidence in a four-variable model and a 32-member population, with the router still ahead in [CASE-158](record/cases.d/CASE-158.md)'s design run with equal audit delay and cost ([CASE-162](record/cases.d/CASE-162.md)); a 192-state organization on which informational closure, strong lumpability and intervention deficiency give different verdicts on one kernel, with Γ = 0.55·H₂(1/3) ≈ 0.5051 bits and finite-sample estimates that misread it ([CASE-164](record/cases.d/CASE-164.md)); reciprocally produced, externally reset and feedback-only governing rules separated by loss, repair and producer interventions with ordinary trajectories identical ([CASE-161](record/cases.d/CASE-161.md)); and identification of the maintaining mechanism and its parameters from diagnostic probes within a known catalog ([CASE-163](record/cases.d/CASE-163.md)). A workbench entry records what was kept, corrected and declined.

### Changed

- Dated notes of 2026-10-26 from the same package on fifteen entries: [CLAIM-278](record/claims.d/CLAIM-278.md) (the router result reproduced, and run on equal terms), [CLAIM-297](record/claims.d/CLAIM-297.md) (two running realizations, without retrieval), [CLAIM-336](record/claims.d/CLAIM-336.md) (the lab held, and its later versions), [CLAIM-401](record/claims.d/CLAIM-401.md) (one kernel, several verdicts), [CLAIM-407](record/claims.d/CLAIM-407.md) (a second exact witness), [CLAIM-414](record/claims.d/CLAIM-414.md) (the maintenance separation in a population), [CLAIM-427](record/claims.d/CLAIM-427.md) (where the lab stands on the grades), [QUESTION-031](record/questions.d/QUESTION-031.md) (a nonlinear case, with a known catalog), [QUESTION-086](record/questions.d/QUESTION-086.md) (interventions named, for arrangements the modeller assigns), [QUESTION-088](record/questions.d/QUESTION-088.md) (the lab is not yet the comparison), [QUESTION-100](record/questions.d/QUESTION-100.md) (a nonlinear fold, and capture in a population), [QUESTION-117](record/questions.d/QUESTION-117.md) (phenomena shown, no comparison made), [QUESTION-222](record/questions.d/QUESTION-222.md) (history against state, in finite chains), [QUESTION-252](record/questions.d/QUESTION-252.md) (pairwise separations on one kernel) and [QUESTION-271](record/questions.d/QUESTION-271.md) (two failures run, in weakened form). The package's note on [CLAIM-443](record/claims.d/CLAIM-443.md) was not applied. No title, status or warrant changed.

### Fixed

- [QUESTION-031](record/questions.d/QUESTION-031.md)'s history item for its split was dated 2026-10-21; the split was made on 2026-10-25, as its note says.
- From the owner's v2.3 amendment, the same day: the notes on [CLAIM-427](record/claims.d/CLAIM-427.md), [CLAIM-278](record/claims.d/CLAIM-278.md) and [QUESTION-117](record/questions.d/QUESTION-117.md) extended with the lab's v2.3 matched comparator (dmarx/PerspectiveLab@e9efcf4). With equal source data and fitted-parameter counts, a same-basis state-space model ties the structural model exactly, and a generic 20-coefficient polynomial transports better on most withheld production laws. The structural basis is still unpriced, and no status changes.
- From the owner's v2.5 amendment, the same day: the notes on [CLAIM-427](record/claims.d/CLAIM-427.md), [QUESTION-031](record/questions.d/QUESTION-031.md) and [QUESTION-086](record/questions.d/QUESTION-086.md) extended with the lab's v2.4 and v2.5 (dmarx/PerspectiveLab@f392084). Adaptive probes change the organization they diagnose; an adequacy alarm catches one out-of-catalog law and its fallback hurts under another; and a same-kernel conventional controller takes every action the guard takes. No status changes.
- From the owner's v2.6 amendment, the same day: dated notes on [QUESTION-270](record/questions.d/QUESTION-270.md) and [CLAIM-437](record/claims.d/CLAIM-437.md), and the notes on [CLAIM-427](record/claims.d/CLAIM-427.md) and [QUESTION-088](record/questions.d/QUESTION-088.md) extended, with the lab's v2.6 affective dissociation (dmarx/PerspectiveLab@74621fb). Five stipulated causes of pursuit after devaluation share one pursuit probability and are separated by interventions; a registered evaluation denied authority is told apart from one never registered by intervention, not by passive history; a same-kernel conventional predictor ties; and an unmodelled hybrid is assigned to a catalog class in every test world. No status changes.

[THEORY-026](record/theory.d/THEORY-026.md), [THEORY-177](record/theory.d/THEORY-177.md) and [THEORY-294](record/theory.d/THEORY-294.md) are narrowed and promoted under [ADR-047](record/decisions.d/ADR-047.md) v2 on derivations written out in their dated notes: [THEORY-026](record/theory.d/THEORY-026.md)'s nostalgia bound under its two conditions, with the rest moved to [QUESTION-191](record/questions.d/QUESTION-191.md); [THEORY-177](record/theory.d/THEORY-177.md)'s correspondence between canonical models and couplings, held to the sum of per-content minima; and [THEORY-294](record/theory.d/THEORY-294.md)'s proportional kernels, held to one-dimensional zero-bias data, with the wider case moved to [QUESTION-192](record/questions.d/QUESTION-192.md) (promotion audit, batch 045).

[THEORY-166](record/theory.d/THEORY-166.md), [THEORY-172](record/theory.d/THEORY-172.md) and [THEORY-175](record/theory.d/THEORY-175.md) are narrowed and promoted under [ADR-047](record/decisions.d/ADR-047.md) (promotion audit, batch 048): [THEORY-166](record/theory.d/THEORY-166.md) to the 66 Pew surveys, with the QQ equality and a classical model that meets it worked in a dated note and a preregistered test moved to [QUESTION-210](record/questions.d/QUESTION-210.md); [THEORY-172](record/theory.d/THEORY-172.md) to what Frank and Goodman's and Bergen, Goodman and Levy's games measured, with a test against named rivals moved to [QUESTION-209](record/questions.d/QUESTION-209.md); [THEORY-175](record/theory.d/THEORY-175.md) to its anchor-cosine invariance, re-derived, and Moschella et al.'s experiments, with a direct measurement of the maps between trained spaces moved to [QUESTION-211](record/questions.d/QUESTION-211.md).

### Added

- [QUESTION-159](record/questions.d/QUESTION-159.md): whether an exact train-then-predict identity holds
  for further sequence-layer classes, or is bounded by some standard
  attention layer. It holds [THEORY-169](record/theory.d/THEORY-169.md)'s former scope test, unchanged.
- [QUESTION-158](record/questions.d/QUESTION-158.md): whether gradient descent, without a spectral
  initialization, reaches the hierarchical multi-index thresholds, and
  whether they survive a second input law. It holds [THEORY-283](record/theory.d/THEORY-283.md)'s former
  promote_when, unchanged, and refines [QUESTION-039](record/questions.d/QUESTION-039.md).

### Changed

- [THEORY-169](record/theory.d/THEORY-169.md), Active after narrowing: for unnormalized causal linear
  attention and for softmax attention, conditioning on a context is a
  learner's train-then-predict step. The three identities are re-derived.
- [THEORY-283](record/theory.d/THEORY-283.md), Active after narrowing: the sample-size thresholds and rates
  are stated for the Bayes-optimal and spectral estimators and for a
  network with a spectral first layer, not for gradient descent. These
  changes carry out the promotion audit's batch-024 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [QUESTION-162](record/questions.d/QUESTION-162.md): whether hyperbolic networks' advantage on tree-like
  data goes with the Möbius bias translations and the distance-based output
  layer. It holds [THEORY-566](record/theory.d/THEORY-566.md)'s former promote_when, unchanged, and refines
  [QUESTION-025](record/questions.d/QUESTION-025.md).
- [QUESTION-163](record/questions.d/QUESTION-163.md): whether Blackwell-equivalent representations of
  trained networks stitch differently by a measurable margin under the
  paper's protocol. It holds [THEORY-176](record/theory.d/THEORY-176.md)'s former promote_when, unchanged.

### Changed

- [THEORY-566](record/theory.d/THEORY-566.md), Active: in Ganea et al.'s hyperbolic networks, curvature acts
  only through the bias translations and the distance-based output layer.
  The composition argument is written out, with the sense of "conjugated".
- [THEORY-176](record/theory.d/THEORY-176.md), Active: the stitching penalty is not Blackwell's order. A
  constructed example now shows that Blackwell-equivalent representations
  can stitch differently, inside the paper's own map class. These changes
  carry out the promotion audit's batch-027 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

[THEORY-178](record/theory.d/THEORY-178.md) is narrowed to the Boolean model ensemble on the E. coli regulatory core and promoted under [ADR-047](record/decisions.d/ADR-047.md) v3, with its positive-circuit condition stated for that network and its cell experiment moved to [QUESTION-172](record/questions.d/QUESTION-172.md). [THEORY-306](record/theory.d/THEORY-306.md) is narrowed to MSN's and SwAV's explicit cluster-size prior and one study's imbalanced-batch measurement and promoted under [ADR-047](record/decisions.d/ADR-047.md) v3, with its derivation and long-tail conditions moved to [QUESTION-171](record/questions.d/QUESTION-171.md) (promotion audit, batch 033).

[THEORY-181](record/theory.d/THEORY-181.md) is narrowed to the zero-loss model with an injective decoder, whose theorem is re-derived, and to the one size Liu et al. measured, non-modular addition with p = 10, and promoted under [ADR-047](record/decisions.d/ADR-047.md) v2 and v3, with the test across sizes moved to [QUESTION-199](record/questions.d/QUESTION-199.md). [THEORY-237](record/theory.d/THEORY-237.md) is promoted with every member's optimum derived, InfoNCE's included, and its title now says each bound attains its supremum, rather than is tight, at the log density ratio up to its free term (promotion audit, batch 043).

Promotion audit, batch 037 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-185](record/theory.d/THEORY-185.md) is narrowed and promoted: Korchinski et al.'s conditional theorem on independent multiplicative attributes is re-derived, its PMI clauses stand, and its raw-ratio clause is held to the full, balanced hypercube with the exact condition on the strengths. [THEORY-161](record/theory.d/THEORY-161.md) is narrowed and promoted: its two identities are re-derived, and its reading of the field is held to the two frameworks read in full. The premise measurement and the field-wide reading move to [QUESTION-178](record/questions.d/QUESTION-178.md) and [QUESTION-177](record/questions.d/QUESTION-177.md).

### Added

- [QUESTION-166](record/questions.d/QUESTION-166.md): whether the depth law of deep linear networks holds
  from starts off the decoupled set, such as random orthogonal weights. It
  holds [THEORY-187](record/theory.d/THEORY-187.md)'s former promote_when, unchanged, and refines
  [QUESTION-039](record/questions.d/QUESTION-039.md).
- [QUESTION-165](record/questions.d/QUESTION-165.md): whether the number of examples a deep network needs on
  the Random Hierarchy Model is set by the detectability of patch–label
  correlations or by the grammar's size. It holds [THEORY-195](record/theory.d/THEORY-195.md)'s former
  promote_when, unchanged.
- [QUESTION-164](record/questions.d/QUESTION-164.md): whether the law of balance holds in a deep network
  trained on real data. It holds [THEORY-211](record/theory.d/THEORY-211.md)'s former promote_when,
  unchanged, and refines [QUESTION-069](record/questions.d/QUESTION-069.md).

### Changed

- [THEORY-187](record/theory.d/THEORY-187.md), Active after narrowing: the depth law of deep linear networks
  is stated for whitened inputs and decoupled, balanced starts, with
  iterations counted at the stable step size. The finite-depth plateau
  exponent and the iteration count are re-derived.
- [THEORY-195](record/theory.d/THEORY-195.md), Active after narrowing under [ADR-047](record/decisions.d/ADR-047.md) v3: what the Random
  Hierarchy Model experiments measured, in the range they cover. The
  attribution of the sample size to correlation detection moves to a
  QUESTION.
- [THEORY-211](record/theory.d/THEORY-211.md), Active after narrowing: the law of balance in the SDE model
  of SGD, whenever both groups carry noise, re-derived by Itô's lemma.
  These changes carry out the promotion audit's batch-027 decisions
  ([ADR-047](record/decisions.d/ADR-047.md)).

[THEORY-189](record/theory.d/THEORY-189.md) is promoted under [ADR-047](record/decisions.d/ADR-047.md) v2 with a proof of the source's unproved Theorem 4, that the closed-form hyperbolic entailment cones are transitive in every dimension, and its bound on K is corrected to ε/(1 − ε²). [THEORY-305](record/theory.d/THEORY-305.md) is promoted with Tan et al.'s identity re-derived and a finite-graph counterexample showing InfoNCE's minimizer outside every bottom-eigenvector span. [THEORY-313](record/theory.d/THEORY-313.md) is narrowed to say the kernel bound is tight for every pair only for an orthonormal embedding, and to the kernel family its O(σ²) gap is proved for, and promoted, with the wider rate moved to [QUESTION-198](record/questions.d/QUESTION-198.md) (promotion audit, batch 043).

### Added

- [QUESTION-153](record/questions.d/QUESTION-153.md), Open: whether the hyperbolic Betti-curve matches in
  odour space and in CA1 separate a hyperbolic metric from a flat sphere
  or a flat multiscale code, and whether they replicate. It holds
  [THEORY-191](record/theory.d/THEORY-191.md)'s and [THEORY-192](record/theory.d/THEORY-192.md)'s former promote_when clauses, unchanged.

### Changed

- [THEORY-191](record/theory.d/THEORY-191.md), Active: in four natural odour sources, concentration
  correlations have the Betti-curve signature of a 3D hyperbolic shell and
  not of any uniform Euclidean cube tried, and 127 odorants' descriptor
  profiles that of a full 3D hyperbolic ball ([LIT-872](record/literature.d/LIT-872.md)). The title is
  narrowed to the data measured.
- [THEORY-192](record/theory.d/THEORY-192.md), Active: in twelve rat CA1 sessions from three data sets,
  correlations have the Betti-curve signature of a uniform 3D hyperbolic
  ball, and the fitted radius rose with log exploration time ([LIT-876](record/literature.d/LIT-876.md)).
  The title is narrowed to the data measured.
- Both carry out the promotion audit's batch-018 decisions under the
  owner's single-study rule ([ADR-047](record/decisions.d/ADR-047.md) v3).

### Added

- [QUESTION-154](record/questions.d/QUESTION-154.md): whether a coarse-graining short of full capture keeps
  longer-range couplings bounded by the information lost, in two or more
  dimensions. It holds [THEORY-198](record/theory.d/THEORY-198.md)'s former promote_when, unchanged, and
  refines [QUESTION-065](record/questions.d/QUESTION-065.md).
- [QUESTION-155](record/questions.d/QUESTION-155.md): whether a lossy-compression generalisation bound
  gives a non-trivial value for an algorithm with infinite I(S;W). It holds
  [THEORY-248](record/theory.d/THEORY-248.md)'s former promote_when, unchanged.

### Changed

- [THEORY-315](record/theory.d/THEORY-315.md), Active: for a state whose four-state reflection orbit is
  realizable, preparation noncontextuality bounds |⟨X⟩| + |⟨Z⟩| ≤ 1. An
  independent derivation, which needs no outcome determinism, meets its
  promote_when.
- [THEORY-198](record/theory.d/THEORY-198.md), Active after narrowing: full capture makes the coarse measure
  factorize across the block in 1D, and in D dimensions under the per-block
  capture hypothesis, now stated in the title with the no-cancellation
  exclusion. The Lemma is re-derived.
- [THEORY-248](record/theory.d/THEORY-248.md), Active after narrowing: the Lipschitz rate-distortion bound
  is finite wherever the output law's rate-distortion function is finite at
  distortion ε/(2L). Theorem 4 and Corollary 6 are re-derived. These
  changes carry out the promotion audit's batch-019 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

[THEORY-204](record/theory.d/THEORY-204.md) (the data-limited scaling exponent γ/(2β)) and [THEORY-243](record/theory.d/THEORY-243.md) (basis-related alignments tying under interchange interventions) are narrowed and promoted. [THEORY-204](record/theory.d/THEORY-204.md) now states the measured match on two corpora and the re-derived conditional exponent min(δ, γ/(2β)); [THEORY-243](record/theory.d/THEORY-243.md) states what the constructed three-unit network proves. Each one's wider test moves to a new QUESTION.

[THEORY-205](record/theory.d/THEORY-205.md) is re-derived exactly and promoted under [ADR-047](record/decisions.d/ADR-047.md) v2, narrowed to the point where the uninformative information-bottleneck encoder first loses stability, since on a skewed 3-state chain the uninformative encoder stops being optimal earlier; when the two coincide is [QUESTION-185](record/questions.d/QUESTION-185.md). [THEORY-275](record/theory.d/THEORY-275.md) is narrowed to the one hydrodynamically coupled bead system it was measured in, and [THEORY-365](record/theory.d/THEORY-365.md) to what the HNSW paper's text reports, and both are promoted under [ADR-047](record/decisions.d/ADR-047.md) v3, with their promote_when conditions moved to [QUESTION-186](record/questions.d/QUESTION-186.md) and [QUESTION-187](record/questions.d/QUESTION-187.md) (promotion audit, batch 039).

Promotion audit, batch 037 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-228](record/theory.d/THEORY-228.md) is narrowed and promoted: HaoChen et al.'s guarantee for the spectral contrastive loss is re-derived step by step on a finite augmentation space, and the title says so and states the bound up to constant and logarithmic factors. [THEORY-319](record/theory.d/THEORY-319.md) is narrowed and promoted: Tosh et al.'s redundancy lemma and landmark bound are re-derived for a general joint law of two views, and the title states mean squared error and the exact, square-integrable ratio. Their promote_whens' wider clauses move to [QUESTION-183](record/questions.d/QUESTION-183.md) and [QUESTION-182](record/questions.d/QUESTION-182.md).

Promotion audit, batch 038 ([ADR-047](record/decisions.d/ADR-047.md) v2 and v3). Three learning-theory accounts are narrowed and promoted. [THEORY-238](record/theory.d/THEORY-238.md): the constant in Theorem 4 of [LIT-245](record/literature.d/LIT-245.md) is re-derived and stands, because the proof applies Lemma 3 at λ/2; the lossy-finiteness clause now says "can stay finite". [THEORY-266](record/theory.d/THEORY-266.md): Theorem 7 of [LIT-233](record/literature.d/LIT-233.md) is re-checked, and its title now names the theorem's hypotheses and its 4Lε term. [THEORY-278](record/theory.d/THEORY-278.md): the measured half is narrowed to [LIT-974](record/literature.d/LIT-974.md)'s fifteen cells, and the renormalized dynamics are re-derived. Their promote_when requests, which ask whether the bounds or the dynamics account for trained networks, move to [QUESTION-179](record/questions.d/QUESTION-179.md), [QUESTION-180](record/questions.d/QUESTION-180.md) and [QUESTION-181](record/questions.d/QUESTION-181.md).

[THEORY-244](record/theory.d/THEORY-244.md), [THEORY-259](record/theory.d/THEORY-259.md) and [THEORY-271](record/theory.d/THEORY-271.md) are promoted under [ADR-047](record/decisions.d/ADR-047.md) v2 on derivations the record wrote out (promotion audit, batch 050). [THEORY-244](record/theory.d/THEORY-244.md) is narrowed to the entropy and mutual-information bridges, re-derived from domination and the coding theorem; its distortion-rate bridge, which rests on an asserted step, moves to [QUESTION-208](record/questions.d/QUESTION-208.md). [THEORY-259](record/theory.d/THEORY-259.md) is restated as an identity: under the universal prior, the Bayesian and ideal-MDL two-part lengths differ by the data's randomness deficiency for the hypothesis, up to a constant fixed by the likelihood family, so the paper's slack is an upper bound and not the gap. [THEORY-271](record/theory.d/THEORY-271.md)'s toy-corpus theorem is proved for every labelling and for any number of aspects.

Promotion audit, batch 063 ([ADR-047](record/decisions.d/ADR-047.md) v2 and v3). [THEORY-246](record/theory.d/THEORY-246.md) is narrowed to what Kornblith et al. measured among ImageNet-trained ResNet-50s and promoted; its general claim that tighter class clusters buy training accuracy at the cost of new tasks leaves the title. [THEORY-334](record/theory.d/THEORY-334.md) is narrowed to what Ballard et al. observed in block copying and promoted; the inference that holding information costs more than re-fetching it, which [THEORY-346](record/theory.d/THEORY-346.md) contests, stays in the body. The Random Hierarchy Model's derived statistics are split from [THEORY-201](record/theory.d/THEORY-201.md) as [THEORY-778](record/theory.d/THEORY-778.md), re-derived to leading order and checked by exact computation; [THEORY-201](record/theory.d/THEORY-201.md) keeps the learning curves and the argued link and stays Proposed. The generality, mechanism and powered-replication requests move to [QUESTION-236](record/questions.d/QUESTION-236.md) and [QUESTION-235](record/questions.d/QUESTION-235.md).

[THEORY-253](record/theory.d/THEORY-253.md) and [THEORY-382](record/theory.d/THEORY-382.md) are promoted under [ADR-047](record/decisions.d/ADR-047.md) v3 on single studies read in full: [THEORY-253](record/theory.d/THEORY-253.md) narrowed to the Geometry model's measured split between gradient and sign descent, which the record reproduced, with a derivation and a trained-network test moved to [QUESTION-193](record/questions.d/QUESTION-193.md); [THEORY-382](record/theory.d/THEORY-382.md) with its freshness-tracking clause held to the authors' reading of their curves, and its distance from the best plan moved to [QUESTION-194](record/questions.d/QUESTION-194.md) (promotion audit, batch 045).

Promotion audit, batch 036 ([ADR-047](record/decisions.d/ADR-047.md) v2 and v3). [THEORY-263](record/theory.d/THEORY-263.md) is promoted: its PAC-Bayes clause is re-derived in any measurable space by the disintegrated change of measure, and the request for a covering-argument source moves to [QUESTION-174](record/questions.d/QUESTION-174.md). [THEORY-293](record/theory.d/THEORY-293.md) is narrowed and promoted: Theorem 4.3 is re-derived by exchange, the facts are learned in full only once capacity exceeds the threshold by their total entropy, the Pythia runs are said to show a threshold, not the same one, and the link test moves to [QUESTION-176](record/questions.d/QUESTION-176.md). [THEORY-229](record/theory.d/THEORY-229.md) is narrowed and promoted to small aligned initialization of common scale, with Propositions 4.1, 4.3 and 5.1 re-derived; generic initialization moves to [QUESTION-175](record/questions.d/QUESTION-175.md).

[THEORY-267](record/theory.d/THEORY-267.md) and [THEORY-261](record/theory.d/THEORY-261.md) are promoted (promotion audit, batch 050). [THEORY-267](record/theory.d/THEORY-267.md) is narrowed under [ADR-047](record/decisions.d/ADR-047.md) v3 to what Rasooly and Rozzi's randomised experiment on Manifold measured, about 59% of a random price shock still present after 60 days, with their model's mechanism reported as theirs; replication elsewhere and whether traders came to believe the shocked price move to [QUESTION-212](record/questions.d/QUESTION-212.md). [THEORY-261](record/theory.d/THEORY-261.md)'s sparse-distributed-memory capacity analysis is confirmed by the record's own simulation of the basic design at up to 200,000 hard locations, which the former promote_when named as sufficient; the title now says exact cues and capacity rising toward a tenth of the locations.

Promotion audit, batch 042 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-280](record/theory.d/THEORY-280.md) is narrowed and promoted: Theorem 1 of Calo et al. was re-checked against the arXiv text, the rate holds with constant-level slips, the title now names the occupancy-sampling model, observed finite states, the known bounded cost and the probability 1 − δ, and the ε⁻² lower-bound request moves to [QUESTION-190](record/questions.d/QUESTION-190.md); [NOTE-763](record/notes.d/NOTE-763.md)'s dual radii are corrected. [THEORY-289](record/theory.d/THEORY-289.md) is narrowed and promoted to least squares on reused isotropic Gaussian covariates, with Theorems 1 and 2 re-derived; the extension request moves to [QUESTION-189](record/questions.d/QUESTION-189.md). [THEORY-387](record/theory.d/THEORY-387.md) is narrowed and promoted to positive recursive Datalog under set semantics, with Theorem 7.1 re-derived for that case; stratified negation, aggregation and the overestimate's size move to [QUESTION-188](record/questions.d/QUESTION-188.md).

Promotion audit, batch 051 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-281](record/theory.d/THEORY-281.md) is narrowed to X of finite support and promoted: the erasure cap, the necessity of the permutation condition for deterministic maps, its sufficiency under disjoint groups and the stochastic attainment condition are re-derived. [THEORY-284](record/theory.d/THEORY-284.md) is promoted with its title unchanged: Theorem 1 is re-derived in both directions, with the shortest-path step for the intrinsic length metric. [THEORY-282](record/theory.d/THEORY-282.md) is promoted with its title unchanged: the construction behind its possibility claim is re-derived, and its promote_when about the measured GPT-2 cases moves to [QUESTION-200](record/questions.d/QUESTION-200.md).

Promotion audit, batch 025 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-308](record/theory.d/THEORY-308.md) is narrowed and promoted: its approximation lemma is closed by a two-sided truncation, its estimation lemma restated as almost-sure convergence, and its sample-complexity clause re-derived with its assumptions named. [THEORY-314](record/theory.d/THEORY-314.md) is promoted over the completed RKHS, with sufficient conditions for a minimizer to exist. [THEORY-320](record/theory.d/THEORY-320.md) is split: the exact residual identity is a new Active [THEORY-737](record/theory.d/THEORY-737.md), and [THEORY-320](record/theory.d/THEORY-320.md) keeps its toy clauses, Proposed, with a note recording a reconstruction that reproduces Theorem 5.2 but not Theorem 5.3 or Lemma 5.4.

Promotion audit, batch 053 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-332](record/theory.d/THEORY-332.md) is promoted with a corrected title: Bruno and Chaudhuri's single-index tuner is not three-competitive for any bound on step size, since a constructed workload with steps at most fB approaches 3 + 2f times the optimum; the upper-bound question moves to [QUESTION-224](record/questions.d/QUESTION-224.md). [THEORY-362](record/theory.d/THEORY-362.md) is promoted: counting-based maintenance of nonrecursive views with stratified negation and aggregation is re-derived from the delta rules' telescoping identity and checked against full recomputation. [THEORY-367](record/theory.d/THEORY-367.md) is narrowed to SPJU queries and promoted: minimal witnesses are proved invariant across equivalent queries, and where-provenance is shown not to be; the rewrite-system clauses move to [QUESTION-225](record/questions.d/QUESTION-225.md).

Promotion audit, batch 054. [THEORY-377](record/theory.d/THEORY-377.md) is narrowed to Olston, Loo and Widom's simulations and promoted ([ADR-047](record/decisions.d/ADR-047.md) v3); its convergence and other-data request moves to [QUESTION-227](record/questions.d/QUESTION-227.md). [THEORY-380](record/theory.d/THEORY-380.md) is promoted with Theorems 5.6, 6.4 and 6.5 of Green, Karvounarakis and Tannen proved ([ADR-047](record/decisions.d/ADR-047.md) v2); its infinite-coefficient clause, false as the paper states it, is corrected to a unit-rule cycle on any tuple in a derivation tree. [THEORY-419](record/theory.d/THEORY-419.md) is narrowed to the do-operator as Pearl defines it in the pages read and promoted with its two consequences derived; the book-wide reading moves to [QUESTION-226](record/questions.d/QUESTION-226.md).

Promotion audit, batch 025 ([ADR-047](record/decisions.d/ADR-047.md) v3). [THEORY-391](record/theory.d/THEORY-391.md) is narrowed and promoted to what Donoho and Tanner measured, with the Gaussian transition attributed to the authors' earlier face-counting theorems and the N^(−1/2) exponent marked as fitted on the same data; its promote_when moves to [QUESTION-168](record/questions.d/QUESTION-168.md), refining [QUESTION-120](record/questions.d/QUESTION-120.md). [THEORY-472](record/theory.d/THEORY-472.md) is narrowed and promoted: the size principle derived from an informative speaker under a point-mass intent and uniform literal meanings, and the two studies' results as measured; its promote_when, a discriminating experiment, moves to [QUESTION-167](record/questions.d/QUESTION-167.md).

Promotion audit, batch 026 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-478](record/theory.d/THEORY-478.md) is narrowed to the equivalence its proof gives under two Hellinger bounds, with the admissible range α < θ/β, and promoted, re-derived in a dated note; its condition on tree heat kernels and sampled data moves to [QUESTION-160](record/questions.d/QUESTION-160.md). [THEORY-231](record/theory.d/THEORY-231.md) is promoted, with the Leibnizianity-to-noncontextuality chain and the prepare-measure realizability claim re-derived. [THEORY-614](record/theory.d/THEORY-614.md) stays Proposed: its promote_when, which asked about trained networks the title disclaims, moves to [QUESTION-161](record/questions.d/QUESTION-161.md), and it now asks for the one unchecked step of Theorem 1.

Promotion audit, batch 055 ([ADR-047](record/decisions.d/ADR-047.md) v2 and v3). [THEORY-580](record/theory.d/THEORY-580.md) is promoted with its title unchanged, after the proofs of Theorem 2.25 and Proposition 2.29 were read and checked against the definitions they take from "The Topology of Causality"; [NOTE-624](record/notes.d/NOTE-624.md) records the check. [THEORY-548](record/theory.d/THEORY-548.md) is narrowed and promoted: the critical-delay formula and transversal crossing are re-derived, and a re-run at the paper's setting shows community variability falling with diversity exactly as an averaging null does. [THEORY-527](record/theory.d/THEORY-527.md) is narrowed to Kenton et al.'s recovery theorem on their definition of agents, re-derived; the verdicts argued from the definition leave the title. Their wider requests move to [QUESTION-229](record/questions.d/QUESTION-229.md) and [QUESTION-228](record/questions.d/QUESTION-228.md).

Promotion audit, batch 060 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-751](record/theory.d/THEORY-751.md) is promoted with its title unchanged. The two steps it lacked are now re-derived: achievability by superposition coding, and a closed-form degrading channel between the Hamming rate–distortion optima of every finite source. [THEORY-744](record/theory.d/THEORY-744.md) is narrowed and promoted. The source's kernel expansion is re-derived for a compact manifold without boundary, and the title now says "without boundary" and that the limit is minus the diffusion's generator. The boundary rate and the semigroup limit move to [QUESTION-231](record/questions.d/QUESTION-231.md).

Narrowed and promoted [THEORY-127](record/theory.d/THEORY-127.md) (batch 023 of the promotion audit, [ADR-047](record/decisions.d/ADR-047.md) v2): the record re-derives List and Pettit's Proposition 3 for the court agenda by the decisive-coalition argument, with Proposition 2 as a corollary; the title now names the court agenda and the two connectedness conditions the proof uses, since issue-wise parity on affine agendas refutes the unconditioned form. The extension to corporate attitudes moves to [QUESTION-152](record/questions.d/QUESTION-152.md).

[THEORY-190](record/theory.d/THEORY-190.md) is narrowed and promoted under [ADR-047](record/decisions.d/ADR-047.md) v2 (promotion audit, batch 048): the S¹ model's closure under geometric coarse-graining is proved at large separation with its error bounded, and shown in a worked example to fail between nearby supernodes, and the source's degree flow, which rests on closure at every separation, moves to [QUESTION-203](record/questions.d/QUESTION-203.md).

Promotion audit, batch 038 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-197](record/theory.d/THEORY-197.md) is promoted. Its promote_when asked for a second derivation stating Mehta and Schwab's correspondence with the same scope, and [LIT-887](record/literature.d/LIT-887.md) and [LIT-891](record/literature.d/LIT-891.md), which the record already held, state it. The identity, the exactness condition and the free-energy point are re-derived, with one refinement: a perfect fit gives an exact step only up to a constant shift of the RBM energy.

[THEORY-216](record/theory.d/THEORY-216.md) is narrowed to what Wu and Silva measured on the 2017 r/place log (low early predictability from four coalition-state features, recovered coalitions growing larger, and persistence under attack in existence form) and promoted under [ADR-047](record/decisions.d/ADR-047.md) v3, with its population and interaction-feature condition moved to [QUESTION-169](record/questions.d/QUESTION-169.md). [CLAIM-273](record/claims.d/CLAIM-273.md)'s citation of the dropped universal clause is restated (promotion audit, batch 031).

### Added

- [THEORY-735](record/theory.d/THEORY-735.md), Active: under a local quadratic model with the greedy
  optimal step, per-step progress is ΔL_max/(1 + B_noise/B), and the
  steps–examples hyperbola (S/S_min − 1)(E/E_min − 1) = 1 holds exactly
  ([LIT-348](record/literature.d/LIT-348.md), re-derived). Split from [THEORY-033](record/theory.d/THEORY-033.md).
- [QUESTION-156](record/questions.d/QUESTION-156.md), Open: which published concept-combination models
  reproduce overextension by dropping conjunction-as-meet, and which by
  dropping a monotone membership weight.

### Changed

- [THEORY-255](record/theory.d/THEORY-255.md), Active: in any lattice with an order-preserving membership
  weight, whatever its negation, conjunction as meet cannot overextend.
  So a model of the guppy-type deviations must drop the meet or
  monotonicity. The generalisation of Aerts's Theorem 9 is checked in a
  dated note, and the title no longer says an emergent concept is needed.
- [THEORY-033](record/theory.d/THEORY-033.md) stays Proposed, extends the new entry, and is corrected. The
  noise scale tracks the critical batch within about 10× on six of eight
  tasks and about 20× on two, not "within an order of magnitude".
- These changes carry out the promotion audit's batch-018 decisions
  ([ADR-047](record/decisions.d/ADR-047.md)).

### Added

- [QUESTION-157](record/questions.d/QUESTION-157.md): whether factored-process results replicate on other
  generator families or objectives, and what loss gap the factored
  representation pays when noise makes it lossy. It holds [THEORY-256](record/theory.d/THEORY-256.md)'s
  former promote_when, unchanged, and refines [QUESTION-060](record/questions.d/QUESTION-060.md).

### Changed

- [THEORY-256](record/theory.d/THEORY-256.md), Active after narrowing: the lossless per-factor embedding of
  a tensor-product generator's predictive state, re-derived, together with
  what [LIT-986](record/literature.d/LIT-986.md) measured. That is 4-layer GPT-2-style transformers on five
  Mess3 and Bloch Walk factors, settling near the factored dimension in
  linearly independent subspaces that are approximately orthogonal in their
  leading components, and reaching it first under the token noise tested.
  It is promoted on one study read in full under [ADR-047](record/decisions.d/ADR-047.md) v3, carrying out
  the promotion audit's batch-019 decision.

Promotion audit, batch 051 ([ADR-047](record/decisions.d/ADR-047.md) v3). [THEORY-272](record/theory.d/THEORY-272.md) is narrowed to Hopfield's 1982 simulations at N = 30 and 100 and promoted. The energy argument and the crosstalk estimate are checked, the fusion and overload clauses are held to the measured cases, and the forgetting clause, reported only in words, is dropped. The large-N request moves to [QUESTION-201](record/questions.d/QUESTION-201.md).

[THEORY-290](record/theory.d/THEORY-290.md) is narrowed to the two-debater, three-proposition model of deductive debate it was computed in and promoted under [ADR-047](record/decisions.d/ADR-047.md) v3, with its group and richer-strategy conditions moved to [QUESTION-173](record/questions.d/QUESTION-173.md) (promotion audit, batch 041).

[THEORY-295](record/theory.d/THEORY-295.md) is narrowed to a consensus that a single test can replace and promoted under [ADR-047](record/decisions.d/ADR-047.md) v3, with its replication-and-memory condition moved to [QUESTION-151](record/questions.d/QUESTION-151.md). [THEORY-546](record/theory.d/THEORY-546.md)'s title is corrected: fission needs a non-branching clause or multiple occupancy, and quasi-memory answers circularity; it stays Proposed (promotion audit, batch 020).

Promotion audit, batch 036 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-321](record/theory.d/THEORY-321.md) is narrowed and promoted: Golub and Jackson's characterization of wisdom under DeGroot averaging is re-derived for a strongly connected society, the title now says so, and the former promote_when, a case outside the model, moves to [QUESTION-184](record/questions.d/QUESTION-184.md) together with a check of the case with several closed groups.

Promotion audit, batch 032 ([ADR-047](record/decisions.d/ADR-047.md) v2). [THEORY-324](record/theory.d/THEORY-324.md) is narrowed and promoted: Ashby's necessity and sufficiency deductions for ultrastability are re-derived step by step, the second feedback must change the parameters whenever, and for as long as, an essential variable is outside its limits, and the unknown environment is stated as one whose effect on the essential variables the system does not know. Its promote_when's wider form, any system that comes to keep its essential variables within limits, moves to [QUESTION-170](record/questions.d/QUESTION-170.md).

Promotion audit, batch 053 ([ADR-047](record/decisions.d/ADR-047.md) v3). [THEORY-368](record/theory.d/THEORY-368.md) is narrowed and promoted on Indyk and Xu's single study, rechecked against the arXiv text: the "until about 10% of the points" clause is held to fast-preprocessing DiskANN, HNSW and NSG, and the ten-index comparison to Table 1's recall@5 at queue length 0.1n. The replication request moves to [QUESTION-230](record/questions.d/QUESTION-230.md).

Promotion audit, batch 063 ([ADR-047](record/decisions.d/ADR-047.md) v3). [THEORY-385](record/theory.d/THEORY-385.md) is narrowed to HNSW and promoted after an independent re-run of Malkov and Yashunin's clustered test: on 30,000 points in 100 isolated clusters, linking each item to its nearest neighbours left part of the bottom layer unreachable and capped recall@10 at 0.72–0.83, at matched build cost and at lower and higher degree, while the pruning rule reached 0.999 with half the links; on uniform data the two rules were within about 0.02. Candidate extension, which the paper recommends for clustered data, did not help in the re-run and leaves the title.

### Added

- [ADR-049](record/decisions.d/ADR-049.md): a QUESTION is Answered when Active CLAIMs or THEORYs answer it
  as posed and in full scope. An Active THEORY counts, so a CLAIM is not
  filed only to restate a reading. A partly answered question is split:
  the answered part becomes a child QUESTION that refines the parent and
  is marked Answered, and the parent is reworded to what is left and stays
  Open.

### Changed

- The Answered status blurb in `luria.yaml` now says "an Active CLAIM or
  THEORY" and cites [ADR-049](record/decisions.d/ADR-049.md).

### Fixed

- Stale `answers` links found by the question audit of 2026-10-21 are
  dropped:
  - [CLAIM-047](record/claims.d/CLAIM-047.md) and [CLAIM-080](record/claims.d/CLAIM-080.md) on [QUESTION-015](record/questions.d/QUESTION-015.md) (a premise and a
    supposition);
  - [THEORY-195](record/theory.d/THEORY-195.md) on [QUESTION-025](record/questions.d/QUESTION-025.md) (its own text says it leaves the question
    as it was);
  - [THEORY-527](record/theory.d/THEORY-527.md) on [QUESTION-032](record/questions.d/QUESTION-032.md) (narrowed to the recovery theorem;
    [THEORY-801](record/theory.d/THEORY-801.md) carries the answer);
  - [CLAIM-304](record/claims.d/CLAIM-304.md) on [QUESTION-111](record/questions.d/QUESTION-111.md) (a precondition, not an answer).
- [CLAIM-366](record/claims.d/CLAIM-366.md) now `answers` [QUESTION-127](record/questions.d/QUESTION-127.md). It proves the first three rows of
  that question's table, and its body says so.
- [QUESTION-186](record/questions.d/QUESTION-186.md) now `refines` [QUESTION-063](record/questions.d/QUESTION-063.md). It was filed from [THEORY-275](record/theory.d/THEORY-275.md)'s
  promotion condition, and [THEORY-275](record/theory.d/THEORY-275.md) answers [QUESTION-063](record/questions.d/QUESTION-063.md).

Chalmers and McQueen's consciousness-collapse paper is filed and read in part, to check how [LIT-164](record/literature.d/LIT-164.md) represents it for [THEORY-485](record/theory.d/THEORY-485.md) (promotion audit, batch 059); [NOTE-112](record/notes.d/NOTE-112.md) and [NOTE-615](record/notes.d/NOTE-615.md) get dated notes, the latter recording what Propp's appendices show about the sample behind [THEORY-167](record/theory.d/THEORY-167.md)'s order claim.

### Changed

- At the owner's direction, `reported_in` backfilled on existing CASEs under [ADR-051](record/decisions.d/ADR-051.md). Of the 146 cases reviewed, 18 gained the field, naming the LITs, NOTEs and THEORYs they were taken from; with the four filed under [ADR-051](record/decisions.d/ADR-051.md) itself, 22 cases now carry it. The converse `reports` was written on 50 LITs, NOTEs and THEORYs. About 26 documented cases stay without it, because the work they were taken from is not registered here, and a work named only in passing, or supplying no fact the case states, is not counted as its report.

### Added

- From the continuation of the exchange of 2026-10-23/24 (U28–U47, 2026-10-24/25): the owner's hypothesis that a population of perspectives advocating one of two interpretations decides by drift diffusion, stated with its conditions and demonstrated in two constructions, corroborating [CLAIM-262](record/claims.d/CLAIM-262.md) ([CLAIM-453](record/claims.d/CLAIM-453.md)); the reduction behind it, in which the influence-weighted support of interacting accumulators on a row-stochastic network is exactly an Ornstein–Uhlenbeck process and a drift-diffusion process when coupling balances leak, with the nonlinear transition corrected to κ_c = λ/E[sech² ε] ([CASE-160](record/cases.d/CASE-160.md)); the Fisher metric of an organization's responses as the pullback of the metric on authority shares, never larger and zero between processes that respond alike ([CASE-159](record/cases.d/CASE-159.md)); a proposed study of audited governance against a contextual router after a reversal of expertise, with the exchange's results recorded as reported and not reproduced ([CASE-158](record/cases.d/CASE-158.md)); and a question on the owner's three mechanisms of influence and how far nominal influence predicts counterfactual influence ([QUESTION-273](record/questions.d/QUESTION-273.md)). Seven works registered unread: Bartók et al. on partial monitoring ([LIT-1528](record/literature.d/LIT-1528.md)), Chaloner and Verdinelli on Bayesian experimental design ([LIT-1525](record/literature.d/LIT-1525.md)), Kwon and Perchet on approachability under partial monitoring ([LIT-1526](record/literature.d/LIT-1526.md)), Wald's sequential tests ([LIT-1523](record/literature.d/LIT-1523.md)), DeGroot's consensus ([LIT-1527](record/literature.d/LIT-1527.md)), MultiDiffusion ([LIT-1522](record/literature.d/LIT-1522.md)) and Multi-LoRA Composition ([LIT-1529](record/literature.d/LIT-1529.md)). A workbench entry and a curation entry.
- The same day, five of the seven works read and made Active, each with a NOTE and two THEORYs: Bartók et al. ([NOTE-1164](record/notes.d/NOTE-1164.md); the observability lemma, [THEORY-962](record/theory.d/THEORY-962.md), and the four-class classification, [THEORY-964](record/theory.d/THEORY-964.md)), Kwon and Perchet ([NOTE-1159](record/notes.d/NOTE-1159.md); the rates, [THEORY-947](record/theory.d/THEORY-947.md), and the exploration floor that decision-dependent signals need, [THEORY-957](record/theory.d/THEORY-957.md)), Chaloner and Verdinelli ([NOTE-1161](record/notes.d/NOTE-1161.md); linear Bayesian design, [THEORY-956](record/theory.d/THEORY-956.md), and nonlinear design as prior-averaged local design, [THEORY-954](record/theory.d/THEORY-954.md)), MultiDiffusion ([NOTE-1158](record/notes.d/NOTE-1158.md); the fusion step as a per-pixel weighted mean, [THEORY-958](record/theory.d/THEORY-958.md), and its reported results, [THEORY-948](record/theory.d/THEORY-948.md)) and Multi-LoRA Composition ([NOTE-1160](record/notes.d/NOTE-1160.md); its reported results, [THEORY-955](record/theory.d/THEORY-955.md), and the switching ablation, [THEORY-949](record/theory.d/THEORY-949.md)). The readings corrected MultiDiffusion's Eq. 4 (as printed it weights by W², and Eq. 5 is exact only for 0/1 weights), Multi-LoRA Composition's §5.1.1 (it gives LoRA Switch's 6.56 and 5.08 to LoRA Composite) and named a confound in its comparison (the merge baseline is not rescaled, so its scale grows with the number of LoRAs). Wald and DeGroot were sought and found Unavailable, and were then read from copies the owner supplied (below). Left for the owner: Lattimore and Szepesvári 2019 (arXiv:1805.09247), the corrected adversarial classification, is not registered; a child QUESTION of [QUESTION-031](record/questions.d/QUESTION-031.md) and a CLAIM on identifying mixture shares, both proposed by the readings, were not filed.

- At the owner's direction, 2026-10-25: [CLAIM-452](record/claims.d/CLAIM-452.md) (demonstrated, Active), that the authority shares of a mixture of known response profiles are identifiable from a set of probe contexts exactly when the profiles over them are affinely independent; and [QUESTION-272](record/questions.d/QUESTION-272.md), split from [QUESTION-031](record/questions.d/QUESTION-031.md) under [ADR-049](record/decisions.d/ADR-049.md) and Answered by it and by [THEORY-962](record/theory.d/THEORY-962.md). [QUESTION-031](record/questions.d/QUESTION-031.md) is reworded to the nonlinear remainder and stays Open.
- Drafted at the owner's request of 2026-10-25, and accepted the same day (below): [ADR-053](record/decisions.d/ADR-053.md), a LIT status `Unfetched` ("Copy found, not fetched") for works whose lawful free copy was located and this client could not fetch, with the copy's address required in the note, so that the generated status page is the owner's queue. A triage of the 140 `Unavailable` notes that record an access obstacle found 43 such works; 37 would move on acceptance.
- At the owner's request, 2026-10-25: Lattimore and Szepesvári 2019, the corrected classification of adversarial partial monitoring, registered and read ([LIT-1524](record/literature.d/LIT-1524.md), [NOTE-1162](record/notes.d/NOTE-1162.md)): the four classes for every finite game, with the trivial class as no pair of neighbouring actions ([THEORY-963](record/theory.d/THEORY-963.md), Active); how degenerate and duplicate actions enter, with the corrected kernel step of the T^2/3 lower bound ([THEORY-961](record/theory.d/THEORY-961.md), Active); and RelExp3's bound for point-locally observable games ([THEORY-950](record/theory.d/THEORY-950.md), Proposed). [THEORY-964](record/theory.d/THEORY-964.md)'s promote_when is met, but two of its clauses are mis-stated, so the reading proposes it be Superseded by [THEORY-963](record/theory.d/THEORY-963.md); that is left for the owner.
- The owner supplied Wald (1945) and DeGroot (1974), which had been sought and not reached. Both were read in full from the copies ([NOTE-1165](record/notes.d/NOTE-1165.md), [NOTE-1157](record/notes.d/NOTE-1157.md)) and are Active ([LIT-1523](record/literature.d/LIT-1523.md), [LIT-1527](record/literature.d/LIT-1527.md)), with three THEORYs filed Active: Wald's boundaries and error inequalities ([THEORY-952](record/theory.d/THEORY-952.md)), the SPRT's OC, ASN and optimality up to the overshoot, with its overshoot-free formulas exactly those of Brownian motion ([THEORY-951](record/theory.d/THEORY-951.md)), and DeGroot's consensus conditions and weights ([THEORY-960](record/theory.d/THEORY-960.md)).
- Accepted by the owner, 2026-10-25: [ADR-053](record/decisions.d/ADR-053.md), and with it the LIT status `Unfetched` ("Copy found, not fetched") in `luria.yaml`, with `Unavailable` narrowed to works with no lawful copy found or only a paywalled one. 34 of the 37 LITs it names moved, each with a history item and the copy's address in its note; three stay `Unavailable` on its own lines (an unconfirmed uploader, no exact address, a host down for a second fetcher too). [ADR-041](record/decisions.d/ADR-041.md) gets a dated note, and the LIT template names the new status.
- At the owner's decision, 2026-10-25: [THEORY-964](record/theory.d/THEORY-964.md) (Bartók et al.'s classification) Superseded by [THEORY-963](record/theory.d/THEORY-963.md) rather than promoted, under [ADR-047](record/decisions.d/ADR-047.md).
- At the owner's request, 2026-10-25: Isaac (2025), "Phenomenal structure: What is it and what is it for?" ([LIT-1361](record/literature.d/LIT-1361.md)), which had stayed Unavailable under [ADR-053](record/decisions.d/ADR-053.md), read in full from the publisher's open-access copy and made Active, with [NOTE-1163](record/notes.d/NOTE-1163.md) and two THEORYs filed Proposed: constancies as invariants of transformations within experience, and after Cassirer as what separates subject from object ([THEORY-959](record/theory.d/THEORY-959.md)), and convergence of quality-space models from different behavioural procedures as the evidence that they target experience ([THEORY-953](record/theory.d/THEORY-953.md)). The finding: a programmatic structuralism that, unlike Lyre's, says geometry is not enough and adds constancy and valence/affordance layers, but the author calls those layers "mere suggestive sketches", and its subject–object claim has no criterion that would separate it from mere invariant extraction.

### Changed

- Dated notes of 2026-10-25 from the same turns on twenty-five entries: [CLAIM-357](record/claims.d/CLAIM-357.md) (approachability and what averaging costs), [CLAIM-400](record/claims.d/CLAIM-400.md) (when the slow regime can be reduced), [CLAIM-444](record/claims.d/CLAIM-444.md) (the geometry in which evidence arrives), [QUESTION-031](record/questions.d/QUESTION-031.md) (choosing probes), [CLAIM-450](record/claims.d/CLAIM-450.md) (information design is not efficacy), [CASE-153](record/cases.d/CASE-153.md) (proposed again, and partly run), [QUESTION-270](record/questions.d/QUESTION-270.md) (four rivals for failed uptake), [CLAIM-446](record/claims.d/CLAIM-446.md) (the approach–avoid game as partial monitoring), [CASE-156](record/cases.d/CASE-156.md) (the reported run, checked: the app's carried rule reproduces A22's numbers), [CASE-155](record/cases.d/CASE-155.md) (two processes as a drift-diffusion decider, and the conformity arm), [CASE-074](record/cases.d/CASE-074.md) (the crowd as a network of accumulators), [CLAIM-262](record/claims.d/CLAIM-262.md) (the owner's hypothesis, restated for a simulation), [THEORY-321](record/theory.d/THEORY-321.md) (influence concentration in diffusion form), [QUESTION-117](record/questions.d/QUESTION-117.md) (endogenous influence and repeated messages), [QUESTION-252](record/questions.d/QUESTION-252.md) (predictive closure proposed for a population), [TERM-067](record/terms.d/TERM-067.md) (the matched-populations test), [CLAIM-279](record/claims.d/CLAIM-279.md) (learned operators), [QUESTION-271](record/questions.d/QUESTION-271.md) (asked again, and an arm per failure), [TERM-066](record/terms.d/TERM-066.md) (built in by design), [CLAIM-336](record/claims.d/CLAIM-336.md) (a running instance, and a typed workspace), [CLAIM-277](record/claims.d/CLAIM-277.md) (the entrenchment loop, named and not run), [CLAIM-123](record/claims.d/CLAIM-123.md) (masked composition of perspectives' predictions), [CASE-144](record/cases.d/CASE-144.md) (run without citation, with a router added), [CLAIM-278](record/claims.d/CLAIM-278.md) (evidence reported for the objection) and [CASE-157](record/cases.d/CASE-157.md) (an independent convergence).
- After the readings of 2026-10-25: the notes of the same day on [CLAIM-446](record/claims.d/CLAIM-446.md) (the avoid-only phrase made exact, two variants with suppressed feedback and a dominated check, the floor sufficient but not required; [THEORY-962](record/theory.d/THEORY-962.md) added to grounds), [CLAIM-357](record/claims.d/CLAIM-357.md) (the target and distance Kwon and Perchet use), [QUESTION-031](record/questions.d/QUESTION-031.md) (the criteria named, and one decision family answered), [CLAIM-123](record/claims.d/CLAIM-123.md) (A45's step as MultiDiffusion's, and an average is not a sum) and [CLAIM-336](record/claims.d/CLAIM-336.md) (A45's distinction mapped onto the two papers) extended; dated notes on [THEORY-405](record/theory.d/THEORY-405.md) (compositions that average) and [THEORY-611](record/theory.d/THEORY-611.md) (guided fields combined convexly); [CASE-159](record/cases.d/CASE-159.md) (a worked D-optimal probe design), [CASE-158](record/cases.d/CASE-158.md) (prior art for the fixed arm), [QUESTION-273](record/questions.d/QUESTION-273.md) (the third mechanism's published forms) and [CASE-160](record/cases.d/CASE-160.md) (aperiodicity in discrete time) amended.
- After the reading of Lattimore and Szepesvári: [LIT-1528](record/literature.d/LIT-1528.md), [NOTE-1164](record/notes.d/NOTE-1164.md), [THEORY-962](record/theory.d/THEORY-962.md), [THEORY-964](record/theory.d/THEORY-964.md), [QUESTION-272](record/questions.d/QUESTION-272.md) and [CLAIM-446](record/claims.d/CLAIM-446.md) (the easy case is k ≤ Hc/(H + c), and the construction is the paper's spam game) updated.
- After the readings of Wald and DeGroot from the owner's copies: [CLAIM-453](record/claims.d/CLAIM-453.md) (the SPRT link read in the primary source, the connectivity condition made DeGroot's single closed class, and the three new THEORYs added to grounds) and [CASE-160](record/cases.d/CASE-160.md) (ℓ as DeGroot's Theorem 3, aperiodicity as his own statement, and a W with one closed class and transient members covered) amended; [CASE-155](record/cases.d/CASE-155.md)'s note of the same day sharpened (the walk is Wald's Z_m, and the limit is not his statement); dated notes on [THEORY-068](record/theory.d/THEORY-068.md) (optimality up to the overshoot, and the limit as the case where Wald's formulas are exact) and [THEORY-321](record/theory.d/THEORY-321.md) (DeGroot's original conditions); the curation entry and the workbench entry of the session updated to say both works were read and are Active; and [ADR-053](record/decisions.d/ADR-053.md)'s Wald bullet updated.
- After the reading of Isaac ([LIT-1361](record/literature.d/LIT-1361.md)): [NOTE-1060](record/notes.d/NOTE-1060.md) and [NOTE-1054](record/notes.d/NOTE-1054.md) (stale text and inactive-ok comments calling it Unavailable or unreached updated), [QUESTION-255](record/questions.d/QUESTION-255.md) (the same fix, and a dated note: its dynamical structure is material for kind (1), not kind (2)) and [QUESTION-254](record/questions.d/QUESTION-254.md) (a dated note: a structural mark of a perspective, with no criterion against a perspective-free invariant extractor); dated notes on [CLAIM-412](record/claims.d/CLAIM-412.md) (Isaac addresses character only, and his layers are a structural analogue of interpretive organization; no grounds added), [THEORY-880](record/theory.d/THEORY-880.md) (a structuralist who cites Lyre and denies that geometry suffices), [THEORY-867](record/theory.d/THEORY-867.md) (not a similarity structuralist; his DKL case bears on the test, not the premise), [THEORY-868](record/theory.d/THEORY-868.md) (the methodological structuralism Negro allows), [CLAIM-138](record/claims.d/CLAIM-138.md) (Newman set aside, relations fixed by named behavioural procedures: a further instance of the remedy) and [CLAIM-368](record/claims.d/CLAIM-368.md) (the tea towel, an analogy for managing a frustrated demand by altering the field).

### Added

- Five works on the rubber hand illusion and bodily self-consciousness, each
  with a LIT and a full-reading NOTE: Botvinick & Cohen 1998, Lenggenhager
  et al. 2007, Blanke & Metzinger 2009, Apps & Tsakiris 2014 and Seth 2013.
  They supply the evidence behind claim C6 of [NOTE-372](record/notes.d/NOTE-372.md), and link the
  record's interoception holdings to body ownership.
- Four Proposed THEORYs from that batch: the rubber hand synchrony effect;
  ownership as a graded belief about the common cause of multisensory
  input; interoceptive signals in body ownership; and minimal selfhood as
  identification with the whole body, with agency only enabling it.
- Nine experimental works building on the rubber hand illusion, each read
  in full: the suggestion debate (Lush 2020; Lush et al. 2020; Ehrsson et
  al. 2022; Lush & Seth 2022; Roseboom & Lush 2022), two studies separating
  proprioceptive drift from ownership (Rohde et al. 2011; Abdulkarim &
  Ehrsson 2016), Longo et al. 2008 and Kalckert & Ehrsson 2012.
- Six more: Hohwy & Paton 2010 and Alsmith & Longo 2014, experiments by
  philosophers on the rubber hand and on self-location; and folk-concept
  experimental philosophy on where the self is (Starmans & Bloom 2012),
  personal identity (Nichols & Bruno 2010) and whether pain is in the body
  (Reuter, Sienhold & Sytsma 2019; Borg et al. 2020).

### Changed

- The rubber hand synchrony THEORY is Rejected by its own refutation
  condition and corrected by a narrower one about reports. The other three
  rubber-hand THEORYs take tighter promotion tests that control for
  expectation.
- The rubber hand THEORY on ownership as a graded belief notes that the
  cooling evidence its source cites is thinner than cited.
- [THEORY-458](record/theory.d/THEORY-458.md) takes Kalckert & Ehrsson 2012 as a source and records one
  refutation route as closed, subject to an expectation control. [THEORY-531](record/theory.d/THEORY-531.md)
  notes that ordinary verdicts on Williams's two tellings do not follow
  the person of the telling (Nichols & Bruno 2010).

### Added

- [QUESTION-251](record/questions.d/QUESTION-251.md), Answered, split off [QUESTION-120](record/questions.d/QUESTION-120.md) under [ADR-049](record/decisions.d/ADR-049.md). The
  distance and sparse-recovery thresholds share one sufficiency proof, a
  per-vector tail and a union bound, and not a necessity proof
  ([THEORY-397](record/theory.d/THEORY-397.md), [THEORY-390](record/theory.d/THEORY-390.md), [THEORY-395](record/theory.d/THEORY-395.md), [THEORY-399](record/theory.d/THEORY-399.md), [THEORY-391](record/theory.d/THEORY-391.md)).

### Changed

- [QUESTION-120](record/questions.d/QUESTION-120.md) is reworded to what its child leaves open. The five
  THEORYs' `answers` links move to the child.

### Fixed

- [QUESTION-217](record/questions.d/QUESTION-217.md) loses a stale comment that listed [CLAIM-394](record/claims.d/CLAIM-394.md) and [THEORY-775](record/theory.d/THEORY-775.md)
  as inactive; both are Active.

### Added

- Three more QUESTIONs marked Answered, the first answered by Active
  THEORYs, each split off a partly answered parent under [ADR-049](record/decisions.d/ADR-049.md):
  - [QUESTION-249](record/questions.d/QUESTION-249.md), from [QUESTION-010](record/questions.d/QUESTION-010.md): a map that keeps nothing about
    a categorical concept A keeps at most H(X|A) about X, and when it
    keeps that much ([THEORY-281](record/theory.d/THEORY-281.md)).
  - [QUESTION-247](record/questions.d/QUESTION-247.md), from [QUESTION-055](record/questions.d/QUESTION-055.md): over a presheaf of contexts,
    negation is the Heyting pseudo-complement the base category fixes,
    not an orthocomplement ([THEORY-516](record/theory.d/THEORY-516.md), [THEORY-037](record/theory.d/THEORY-037.md)).
  - [QUESTION-246](record/questions.d/QUESTION-246.md), from [QUESTION-067](record/questions.d/QUESTION-067.md): what a Kochen–Specker failure
    refutes, as against a generalized-noncontextuality failure, and that
    the generalized notion is strictly broader ([THEORY-011](record/theory.d/THEORY-011.md), [THEORY-015](record/theory.d/THEORY-015.md),
    [THEORY-016](record/theory.d/THEORY-016.md), [THEORY-231](record/theory.d/THEORY-231.md), [THEORY-559](record/theory.d/THEORY-559.md)).

### Changed

- [QUESTION-055](record/questions.d/QUESTION-055.md) and [QUESTION-067](record/questions.d/QUESTION-067.md) are reworded to what their children leave
  open. [QUESTION-010](record/questions.d/QUESTION-010.md)'s title is unchanged. The eight THEORYs' `answers`
  links move to the children. [QUESTION-055](record/questions.d/QUESTION-055.md) no longer calls [THEORY-037](record/theory.d/THEORY-037.md)'s
  Heyting laws unchecked, and [QUESTION-067](record/questions.d/QUESTION-067.md)'s "What the record holds" now
  lists [THEORY-231](record/theory.d/THEORY-231.md), [THEORY-315](record/theory.d/THEORY-315.md) and [THEORY-559](record/theory.d/THEORY-559.md).

### Added

- The first QUESTIONs marked Answered, each split off a partly answered
  parent under [ADR-049](record/decisions.d/ADR-049.md):
  - [QUESTION-240](record/questions.d/QUESTION-240.md), from [QUESTION-022](record/questions.d/QUESTION-022.md): restriction-compatible kernels
    preserve overlap consistency, and kernels from one global kernel
    preserve global extendability ([CLAIM-121](record/claims.d/CLAIM-121.md), [CLAIM-070](record/claims.d/CLAIM-070.md)).
  - [QUESTION-241](record/questions.d/QUESTION-241.md), from [QUESTION-100](record/questions.d/QUESTION-100.md): when the linearized symmetric
    state is unstable, and that independent scoring removes it
    ([CLAIM-330](record/claims.d/CLAIM-330.md)).
  - [QUESTION-239](record/questions.d/QUESTION-239.md), from [QUESTION-121](record/questions.d/QUESTION-121.md): commitment before evidence is
    not Regime B ([CLAIM-340](record/claims.d/CLAIM-340.md)).

### Changed

- [QUESTION-022](record/questions.d/QUESTION-022.md) and [QUESTION-100](record/questions.d/QUESTION-100.md) are reworded to what their children leave
  open. [QUESTION-121](record/questions.d/QUESTION-121.md)'s title is unchanged. The four CLAIMs' `answers`
  links move to the children.

### Added

- Three Answered QUESTIONs, each split off a partly answered parent under
  [ADR-049](record/decisions.d/ADR-049.md), on Active THEORYs:
  - [QUESTION-245](record/questions.d/QUESTION-245.md), from [QUESTION-052](record/questions.d/QUESTION-052.md): for linear decisions at the
    population level, the top eigenspace is a stable, minimax-optimal
    span for symmetric pairs, and the top left singular span takes that
    role for directed ones ([THEORY-007](record/theory.d/THEORY-007.md), [THEORY-228](record/theory.d/THEORY-228.md), [THEORY-239](record/theory.d/THEORY-239.md),
    [THEORY-319](record/theory.d/THEORY-319.md)).
  - [QUESTION-250](record/questions.d/QUESTION-250.md), from [QUESTION-093](record/questions.d/QUESTION-093.md): a macro description can have an
    effective-information advantage without organizational closure or
    self-individuation ([THEORY-222](record/theory.d/THEORY-222.md)).
  - [QUESTION-243](record/questions.d/QUESTION-243.md), from [QUESTION-115](record/questions.d/QUESTION-115.md): retention tracks association,
    not propagation, and Ψ and dynamical independence diverge, detect no
    interaction and price no size ([THEORY-424](record/theory.d/THEORY-424.md), [THEORY-764](record/theory.d/THEORY-764.md)).

### Changed

- [QUESTION-052](record/questions.d/QUESTION-052.md), [QUESTION-093](record/questions.d/QUESTION-093.md) and [QUESTION-115](record/questions.d/QUESTION-115.md) are reworded to what their
  children leave open. The seven THEORYs' `answers` links move to the
  children.
- [THEORY-239](record/theory.d/THEORY-239.md) no longer says the directed case on one space is unworked.
  Its note of 2026-10-19 works it.

### Added

- Three QUESTIONs marked Answered, split off partly answered parents
  under [ADR-049](record/decisions.d/ADR-049.md):
  - [QUESTION-244](record/questions.d/QUESTION-244.md), from [QUESTION-220](record/questions.d/QUESTION-220.md): information-bottleneck optima at
    two budgets need not nest ([CLAIM-387](record/claims.d/CLAIM-387.md), [CLAIM-392](record/claims.d/CLAIM-392.md)).
  - [QUESTION-242](record/questions.d/QUESTION-242.md), from [QUESTION-221](record/questions.d/QUESTION-221.md): exact closure of an aggregate
    does not require a nearly decomposable block ([CLAIM-388](record/claims.d/CLAIM-388.md)).
  - [QUESTION-248](record/questions.d/QUESTION-248.md), from [QUESTION-222](record/questions.d/QUESTION-222.md): a scalar linear coarse variable
    of a linear Gaussian VAR(1) has an exact finite Markovian
    augmentation ([CLAIM-398](record/claims.d/CLAIM-398.md)).

### Changed

- [QUESTION-220](record/questions.d/QUESTION-220.md), 221 and 222 are reworded to what their children leave
  open. The four CLAIMs' `answers` links move to the children.

### Added

- [THEORY-739](record/theory.d/THEORY-739.md), Active: for word2vec's quartic proxy with tied weights
  and symmetric reweighting, the rank-d minimisers are the top eigenvectors
  of M*, and from an aligned start each is acquired in a logistic rise, in
  order of eigenvalue. Split from [THEORY-182](record/theory.d/THEORY-182.md), re-derived.
- [THEORY-740](record/theory.d/THEORY-740.md), Active: a two-layer linear network from a decoupled,
  balanced start learns its correlation's singular modes one at a time in
  order of strength, while one layer learns them all on one timescale.
  Split from [THEORY-186](record/theory.d/THEORY-186.md), re-derived.
- [THEORY-738](record/theory.d/THEORY-738.md), Active: the unconstrained-features max-margin geometry
  under step imbalance is simplex-encoded-label interpolation, and the
  simplex ETF only for balanced or binary data. Split from [THEORY-286](record/theory.d/THEORY-286.md),
  re-derived by a dual certificate.

### Changed

- [THEORY-182](record/theory.d/THEORY-182.md), [THEORY-186](record/theory.d/THEORY-186.md) and [THEORY-286](record/theory.d/THEORY-286.md) extend the new entries and keep
  their unproved parts, Proposed, with their promote_whens unchanged. These
  changes carry out the promotion audit's batch-024 decisions ([ADR-047](record/decisions.d/ADR-047.md)).

[THEORY-109](record/theory.d/THEORY-109.md)'s formal core, Kuditipudi et al.'s Theorem 1 that ε-dropout-stable ReLU solutions are ε-connected, with Draxler et al.'s concatenation bound, is split into [THEORY-736](record/theory.d/THEORY-736.md) and filed Active (promotion audit, batch 030). [THEORY-109](record/theory.d/THEORY-109.md) extends it and stays Proposed for the claim that training's solutions form one connected set.

[THEORY-209](record/theory.d/THEORY-209.md)'s exact result, Kunin et al.'s stationary state of SGD with momentum on linear regression with Hessian-proportional noise, is split off as a new Active THEORY after the promotion audit re-derived it. [THEORY-209](record/theory.d/THEORY-209.md) keeps the claim that converged deep networks are in that state and stays Proposed. A dated note corrects "broken detailed balance": in the model the current is reversible.

### Added

- At the owner's direction, valence as ordering-potential:
  - a term: goal-conduciveness valence as a regime in which an ordering of a system's own states by their bearing on its maintenance prevails in the negotiation among its perspectives ([TERM-076](record/terms.d/TERM-076.md));
  - the owner's thesis: appraisal is that negotiation, a common currency is its admitting an ordering, valence presupposes frustration, sign is progress against a reference course, intensity is the potential's strength, and ambivalence differs from neutrality ([CLAIM-440](record/claims.d/CLAIM-440.md));
  - a demonstrated claim: on finite options an ordering is a currency; the lexicographic order of the square has none; a continuous ordering has a continuous one (Eilenberg; Debreu); a threshold override has a discontinuous one ([CLAIM-436](record/claims.d/CLAIM-436.md));
  - Veit's currency and ALARM's override recast as continuous and overriding potential, with a trade-off test ([CLAIM-435](record/claims.d/CLAIM-435.md));
  - two questions: how potential is measured ([QUESTION-268](record/questions.d/QUESTION-268.md)), and whether potential of a proxy for maintenance is valence ([QUESTION-267](record/questions.d/QUESTION-267.md)).
  - a question on operationalizing felt valence in three independently measured layers ([QUESTION-266](record/questions.d/QUESTION-266.md)), and a candidate claim: valence is felt when the system models its own potential ([CLAIM-439](record/claims.d/CLAIM-439.md));
  - Berridge's liking–wanting dissociation ([THEORY-893](record/theory.d/THEORY-893.md)), and from it an objection that potential tracks wanting, not liking ([CLAIM-438](record/claims.d/CLAIM-438.md)).
  - a reply conceding that objection in a principled form, on the component process model's levels of valence: the account is of goal-conduciveness valence ([CLAIM-433](record/claims.d/CLAIM-433.md)).
  - incentive sensitization ([THEORY-895](record/theory.d/THEORY-895.md)), and notes on [CLAIM-433](record/claims.d/CLAIM-433.md) and [QUESTION-267](record/questions.d/QUESTION-267.md) relating it and a taxonomy of addictive design features to the account.
  - the owner's claim that 'wanting' and 'liking' are saliences relative to different processes, with valence relative to a perspective ([CLAIM-437](record/claims.d/CLAIM-437.md));
  - a demonstrated claim: a potential exists exactly when winning moves never cycle; a transitive binary record's cyclic share is (n − 2)/3n in a complete tournament but not on a sparse graph; the Hodge gradient can reverse a comparison the wins settle; netting erases alternation; a record fixes a class of potentials; coherence is not alignment ([CLAIM-434](record/claims.d/CLAIM-434.md));
  - two terms carrying the hierarchy a review proposed: ordinal potential ([TERM-077](record/terms.d/TERM-077.md)) and persistent potential ([TERM-078](record/terms.d/TERM-078.md)), under goal-conduciveness valence and the felt candidate;
  - synthetic cases for each measure, in scratch/formal/valence.py.
- Forty new works in six batches, and a note on [NOTE-1063](record/notes.d/NOTE-1063.md) relating the beautiful-loop reading to the felt candidate. A curation entry.

### Changed

- After a review of the pull request, before merge: a common currency means only the weakest ordinal sense, as against scalar currency and cardinal trade-off structure; existence, coherence and intensity are ordinal, and the Hodge decomposition measures only cardinal inconsistency; valence is undefined without contested pairs; ambivalence is read in windows, not in a netted record, against a graph-preserving null model; the potential is reported as a class and identified by intervention; and the predicted coincidence of pleasantness and goal conduciveness is made conditional ([TERM-076](record/terms.d/TERM-076.md), [CLAIM-440](record/claims.d/CLAIM-440.md), [QUESTION-268](record/questions.d/QUESTION-268.md), [QUESTION-266](record/questions.d/QUESTION-266.md)).
- After a second review, before merge: the first level renamed ordinal extendibility, since acyclic wins show only that some complete ordering fits them ([TERM-077](record/terms.d/TERM-077.md)); an approximate persistent potential separated from an exact one, which alone is a Lyapunov function ([TERM-078](record/terms.d/TERM-078.md)); sign and intensity set-valued across the class of potentials, and a selected ordering scored on held-out contests ([TERM-076](record/terms.d/TERM-076.md)); three more parts of [CLAIM-434](record/claims.d/CLAIM-434.md) and four more cases in scratch/formal/valence.py.
- At the owner's direction, the thesis and its term revised before merge from "hedonic" to "goal-conduciveness" valence, and the wanting–liking objection conceded.
- "Dominance" renamed "potential" throughout the line, to avoid the pleasure–arousal–dominance and decision-theoretic senses.
- [CLAIM-432](record/claims.d/CLAIM-432.md)'s defeater corrected: [THEORY-101](record/theory.d/THEORY-101.md) threatens it only joined to a denial that a corporation is conscious. A dated note relates it to valence as ordering-potential.
- Dated notes on [THEORY-101](record/theory.d/THEORY-101.md) and [THEORY-090](record/theory.d/THEORY-090.md) recasting their rivalry.

### Changed

- [ADR-043](record/decisions.d/ADR-043.md) v2: `warrant` records how a claim is supported now, not how it
  would have to be settled. That is the owner's decision on the promotion
  audit's batch 028 question. An untested empirical generalization stays
  interpretive until the record holds the observations.
- [CLAIM-052](record/claims.d/CLAIM-052.md)'s warrant is restored to interpretive, reversing [#204](https://github.com/dmarx/nucleation/issues/204). The
  record holds no observation of the framing-order effect it predicts.
  It is still Proposed.

### Added

- At the owner's direction, from a comparison of the will-organization and affect lines:
  - a claim: emotion is on the claim side of the gap between claimed precedence and granted authority, a perspective's valence on its claims, the system's valence on grants, so suspension changes the system's valence and not the perspectives' ([CLAIM-442](record/claims.d/CLAIM-442.md));
  - an objection: flow, with nothing contested, has undefined valence on the potential account yet is reported as positive, with four exits ([CLAIM-441](record/claims.d/CLAIM-441.md));
  - a question: does the potential account need accessibility, jurisdiction, suspension and transformation beside who wins ([QUESTION-269](record/questions.d/QUESTION-269.md));
  - a decision: the record's own argument is stated ordinally first, with a measure's cardinality stated and partial identification reported as a result ([ADR-052](record/decisions.d/ADR-052.md)).
- A dated note on [QUESTION-267](record/questions.d/QUESTION-267.md) reading a proxy-keyed potential as a protective lock-in.

<!-- luria-insert-here -->
