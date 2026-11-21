# Reader notes: ultrametric-ogielski (LIT-tmpslg57)

## Step 1, 2026-11-21: copies located
- OpenAlex: oa_status closed; locations = doi.org landing (APS), PubMed 10031875 (no abstract). No repository copy.
- Semantic Scholar: openAccessPdf CLOSED, abstract elided by publisher.
- journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.1634: HTTP 403 (stopped, not retried).
- Web search for a PDF: none found. Going to neighbours: cond-mat/0310079, SLAC-PUB-4077, cond-mat/0505585, arXiv 2404.18123.

## Step 2, 2026-11-21: neighbours read
- Bachas & Huberman, "Complexity and ultradiffusion", SLAC-PUB-4077 (Mar 1987; submitted J. Phys. A), slac.stanford.edu PDF, institutional (SLAC) host. Read sections 1-3 in full (exact solution, uniform trees). Credits Ogielski-Stein with some of sec. 3's results.
  Key: uniform b-ary tree, per-pair rate e^{-h}, height step Δh; silhouette s = ln b/Δh; autocorrelation ~ t^{-v}, v = s/(1-s), needs e^{Δh} > b; finite trees always decay exponentially at last.
  => with per-pair rate ratio g per level: v = ln b / (ln(1/g) - ln b), not ln b/ln(1/g). ln b/ln(1/g) holds when g is the ratio of TOTAL escape rates per level.
- Lukierska-Walasek & Topolski, cond-mat/0505585 (arXiv). Read in full. Describes the O-S model (regular Cayley tree, M levels, branching p, rates by ultrametric distance), says its eq. (32) "has the same form as corresponding equation (6) from [9]" (=O-S), and gets P_t ~ t^{-T ln2/Δ} with a_k = e^{-Δk/T} the total intensity to distance k.
- Nechaev & Vasilyev cond-mat/0310079: abstract + sec. II.D only; says O-S used a 3-branching Cayley tree.
- Bikulov & Zubarev arXiv 2404.18123: abstract + intro: power law modulated by log-periodic function.
## Own check (python3 -I, scratch scripts/um.py): b=2, depth 12, per-pair rate g^level, g=0.1: fitted slope 0.446 vs ln2/(ln10-ln2)=0.431 vs ln2/ln10=0.301.

## Step 3, 2026-11-21: recheck done (THEORY-1366/1309 Freidlin-Wentzell now held; THEORY-758; LIT-672). Report drafted.
