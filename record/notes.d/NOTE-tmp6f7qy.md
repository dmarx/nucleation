---
status: Read
paper: LIT-tmpv6qcw
title: Labrinidis & Roussopoulos — WebView materialization
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' camera-ready copy posted on the
    University of Maryland Opsis project page (https://www.cs.umd.edu/projects/opsis/papers/2000/webviews.pdf;
    the project page links it as webviews.pdf.gz, which returns 404, and the uncompressed
    name serves the PDF). The copy is 12 pages numbered 1–12, made by dvips on 1
    March 2000, and carries the line "In the Proceedings of the ACM SIGMOD International
    Conference on Management of Data, Dallas, Texas, USA May 14 - 19, 2000"; the
    proceedings pages are 367–378 (OpenAlex), and the printed proceedings version
    was not seen (ACM Digital Library returned 403). Text extracted with pdftotext;
    the cost formulas (Eqs. 1–9) and the staleness formulas of Section 3.7 lose
    their layout in extraction, so they were read from a page image of page 7 and
    the extraction of pages 4–6. Read: abstract, Sections 1–5, Figures 1–9, Tables
    1–2 and the reference list. Nothing skipped. The figures' numbers were taken
    from the data tables printed under each chart. The 26-page technical report
    version (webviews-tr.pdf, same directory, created the same day) was fetched
    and searched for a selection algorithm and the Zipf results, which the conference
    paper defers to it; it was not otherwise read. Every quotation below was checked
    against the extracted text by script, with whitespace normalised.
date: '2026-10-15'
summary: >-
  For a page built from database queries, the paper compares three ways to serve
  it on a server with online updates: compute it on each request (virt), store the
  query result in the DBMS and refresh it on every update (matdb), or store the
  finished page as a file at the web server and rewrite it on every update (matweb).
  It gives a cost model summing access and update costs by their frequencies and
  states the selection problem (choose a policy per page to minimize mean response
  time, no space limit, no staleness allowed), but gives no algorithm for it. On
  one Apache/Informix testbed with cheap indexed queries, matweb answered 10 to
  230 times faster than the other two at all loads tried, and matdb was slower than
  virt whenever there were updates, because reading the stored result cost about
  as much as recomputing it. Staleness is defined as the delay from update to reply,
  sketched, and never measured; build cost and storage are outside the model.
---

# NOTE-tmp6f7qy: Labrinidis & Roussopoulos — WebView materialization

## Contribution

A WebView is "a web page automatically created from base data typically
stored in a DBMS." Earlier work by the same authors (WebDB 1999) compared
computing such pages on the fly with storing them at the web server. This
paper adds a third option, a materialized view inside the DBMS, and
compares the three "analytically, through a detailed cost model, and
quantitatively, through extensive experiments on an implemented system"
(WebMat: Apache 1.3.6 with mod_perl, Informix 9.14, and a Perl updater).
It argues that choosing a policy for each page differs from view selection
in a warehouse in four ways: where to store, online updates, many small
queries rather than few large ones, and no resource constraint.

## Key insight

Storing an answer does not save much unless the stored copy is cheaper to
reach than the recomputation, and unless keeping it current happens off the
path that serves requests. A query result stored as a table inside the
DBMS still costs a trip to the DBMS to read, about what an indexed
selection costs to recompute, and its refresh loads the same DBMS that
serves every request. A finished page stored as a file at the web server
is read without touching the DBMS, and its refresh runs in a separate
process. So the question "store it or not" is really "store it where",
and the answer turns on which resource is the bottleneck.

## Assumptions

- **No staleness.** "Since WebViews must be up to date, materialized
  WebViews are immediately refreshed with every update on the base data."
  The selection problem states it again: "In this paper, we also assume a
  no staleness requirement, i.e. the WebViews must always be up to date."
- **No storage limit.** "We assume that there is no storage constraint."
  Pages are small and live on disk; the paper takes 30KB per page and a
  50GB disk as holding about 1.5 million pages.
- **No build cost.** Nothing in the model charges for creating a stored
  view or page, or for switching a page between policies. All experiments
  fix one policy for a run.
- **Refresh by recomputation at the web server.** Under matweb every update
  to a source regenerates each affected page from scratch (Eq. 8). Under
  matdb, refresh may be incremental (Eq. 5) or by recomputation (Eq. 6).
- **Objective is mean response time measured at the server**, not total
  work. The aggregation is expected "to be more sensitive to the access
  costs than the update costs", since updates run in the background.
- **The DBMS is the bottleneck.** The cost aggregation keeps only the DBMS
  part of update costs (π_dbms) on the grounds that "the load on the DBMS
  is expected to dominate the average query response time."
- **Testbed workload.** 1000 WebViews over 10 source tables, each a
  selection on an indexed attribute returning 10 tuples, 3KB of HTML; one
  Sun UltraSparc-5 (320MB) as server, 22 Ultra-1 clients on one LAN, 10
  updater processes, runs of 10 minutes, access and updates uniform over
  pages unless stated, each update changing one attribute. Informix had no
  native materialized views, so matdb views were tables updated by SQL.

## Key results

Notation: A is the cost of one access, U of one update to a source, f_a and
f_u their frequencies.

- **Cost model (Eqs. 1–8).** A_virt = C_query(S_i) + C_format(v_i);
  U_virt = C_update(s_j). A_matdb = C_access(v_i) + C_format(v_i);
  U_matdb = C_update(s_j) + Σ over affected views of C_update(v_k), either
  C_refresh(v_k) or C_query(S_k) + C_store(v_k). A_matweb = C_read(w_i);
  U_matweb = C_update(s_j) + Σ over affected pages of C_query(S_k) +
  C_format(v_k) + C_write(w_k), the last two in the updater.
- **Total cost (Eq. 9).** TC = Σ_matweb f_a·A_matweb + Σ_matweb-sources
  b·f_u·π_dbms(U_matweb) + Σ_virt f_a·A_virt + Σ_virt-sources f_u·U_virt +
  Σ_matdb f_a·A_matdb + Σ_matdb-sources f_u·U_matdb, with b = 0 if every
  page is matweb and b = 1 otherwise: refreshing stored pages costs
  response time only when some requests still go to the DBMS.
- **Selection problem, stated and not solved.** "For every WebView at the
  server, select the materialization strategy (virtual, materialized
  inside the DBMS, materialized at the web server), which minimizes the
  average query response time on the clients." The paper gives no
  algorithm, no complexity result and no experiment with a mixed plan
  chosen by the model; the technical report has none either.
- **Minimum staleness (Section 3.7).** "We call minimum staleness, MS, the
  time it takes for an update to propagate to the user", measured to the
  reply. MS_matdb − MS_virt = T_refresh + T_access − T_query and
  MS_matweb − MS_virt = T_write + T_read, so under light load virt is
  freshest. The claim that under heavy load matweb has the least MS rests
  on Figure 3, a sketch; MS is never measured in Section 4.
- **Access rate (Figure 4).** With no updates, at 10/25/35/50/100
  requests per second, mean response time (s) was virt 0.039, 0.354,
  0.949, 1.488, 1.843; matdb 0.048, 0.323, 0.920, 1.498, 1.870; matweb
  0.0026, 0.0028, 0.0039, 0.0096, 0.189. With 5 updates per second, at
  10/25/35/50: virt 0.096, 0.518, 1.052, 1.595; matdb 0.339, 0.847, 1.315,
  1.831; matweb 0.0092, 0.0046, 0.0058, 0.054. matweb was "consistently at
  least an order of magnitude (10 - 230 times) less than those of the
  virt or matdb policies."
- **Reading a stored result cost about as much as recomputing it.** With
  no updates virt and matdb were close, because "the cost of accessing
  them is about the same as the cost of generating them from scratch".
  At 25 requests per second matdb was 9.69% faster with no updates and
  virt 63.53% faster with 5 updates per second.
- **Update rate (Figure 5).** At 25 requests per second and 0 to 25
  updates per second, virt rose from 0.354 to 0.877 s, matdb from 0.323 to
  1.37 s, matweb stayed between 0.003 and 0.006 s. The "virt policy gives
  56% - 93% faster query response times compared to the matdb policy in
  the presence of updates."
- **Number of pages (Figure 6),** with 10% of pages made joins. With no
  updates matdb beat virt at 100 pages (0.054 against 0.191 s, 3.5 times)
  and 1000 (0.295 against 0.346), and lost at 2000 (0.414 against 0.403),
  attributed to contention among the many view tables. With 5 updates per
  second virt won from 1000 pages on (0.400 against 0.525; 0.599 against
  0.857).
- **Size (Figures 7–8).** Doubling tuples per view raised virt by 50% and
  matdb by 15% and left matweb unchanged; HTML of 30KB instead of 3KB raised
  matweb from 0.0046 to 0.090 s.
- **Zipf access (θ = 0.7)** lowered response times 11–23% for all
  policies; the graphs are in the technical report.
- **Model check (Figure 9).** 500 virt and 500 matweb pages, 25 requests
  and 5 updates per second. virt pages' mean response time rose 27% when
  the updates fell on virt pages and 236% when they fell on matweb pages
  (0.092 to 0.309 s), because refreshing stored pages runs queries in the
  same DBMS. matweb pages stayed near 0.004 s. This matches the sign of
  Eq. 9's b term; the formula's values are never computed and compared.
- **Conclusion as stated:** "the matdb policy was better than the virt
  policy only for a very limited number of cases": 100 pages, or under 5
  updates per second.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): a frequency-weighted access-plus-upkeep cost, with a
new dimension (where to store), no staleness, no build cost, no algorithm.
It is not the joint model.**

- Its Eq. 9 has the shape Gupta 1997 ([LIT-1091](../literature.d/LIT-1091.md)) has: access frequency
  times access cost plus update frequency times upkeep, summed over stored
  items. It adds a third choice beside "store" and "recompute": where the
  stored copy lives, which sets both the cost of reading it and whose
  resources its upkeep consumes.
- Staleness is forbidden, as in Karlin et al. ([THEORY-348](../theory.d/THEORY-348.md)): every update
  refreshes at once. Minimum staleness is defined as propagation delay but
  is not priced, constrained or measured. Build cost and switching cost
  are absent; storage is assumed free. So of the question's four terms it
  has query savings and upkeep only.
- The selection problem is stated and left unsolved. The experiments fix
  one policy for every page in a run (except the 500/500 check), so the
  paper shows which uniform policy wins on its testbed, not how to choose
  per page. It is weaker than Gupta and Mumick ([THEORY-350](../theory.d/THEORY-350.md)) or Bruno and
  Chaudhuri ([THEORY-332](../theory.d/THEORY-332.md)), which at least give an algorithm.
- What it adds to the question is an observed fact: on this testbed,
  upkeep is not charged to the stored item alone. Refreshing stored pages
  raised the response time of unstored pages by 236%, because both used
  the DBMS. That is a resource-sharing form of the non-additivity Gupta and
  Mumick found in upkeep ([THEORY-350](../theory.d/THEORY-350.md)), seen in measurement.

**On [CLAIM-303](../claims.d/CLAIM-303.md): an instance where filing does not pay at any reuse count,
and where upkeep taxes what was not filed.**

- [CLAIM-303](../claims.d/CLAIM-303.md) requires c_r > c_a + u for filing to pay. matdb is the case
  c_a ≈ c_r: a stored result that costs as much to reach as to rebuild.
  Under updates it lost to recomputation at every load and size tried
  except 100 pages, whatever the reuse. So the claim's condition can fail
  through access cost alone, before reuse is counted. Where an argument is
  filed, and how cheaply it is found, matters as much as whether.
- The 236% result says the upkeep term u is not a per-item constant when
  upkeep and retrieval share a resource; the claim's arithmetic charges u
  to each filed item's own uses. If checking filed arguments competes with
  reconstructing unfiled ones for the same attention, filing raises the
  cost of everything else, not only of the filed item.
- It does nothing for the claim's staleness term. Stale reuse is ruled out
  by assumption here, so the paper is silent on A11's point that
  reusing an obsolete argument can cost more than recomputing it.
