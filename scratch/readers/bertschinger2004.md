# Reader notes: bertschinger2004 (LIT-2991)

Bertschinger & Natschläger (2004), "Real-Time Computation at the Edge of
Chaos in Recurrent Neural Networks", Neural Computation 16(7):1413-1436,
doi:10.1162/089976604323057443. Reader: Claude (subagent), 2026-11-22.

## Step 1: copies sought (2026-11-22)

- OpenAlex API, doi:10.1162/089976604323057443: `is_oa: false, oa_status: closed`;
  locations only https://doi.org/10.1162/089976604323057443 (publisher, paywalled)
  and https://pubmed.ncbi.nlm.nih.gov/15165396 (abstract only; no PMC copy).
- Semantic Scholar API: `openAccessPdf.status: CLOSED`. A second API call
  (for the NIPS paper) returned 429 rate limit; stopped there. The S2 web
  page https://www.semanticscholar.org/paper/04c6461e524107198eb98835cd6ba2f7733b3163
  (search snippet says "[PDF]") returned 403 to WebFetch; not retried.
- OpenAlex search API: second query refused, "Rate limit exceeded ...
  free daily budget ... used up"; stopped there.
- TU Graz IGI: https://www.igi.tugraz.at/tnatschl/ -> 404 (now
  https://www.tugraz.at/institute/igi/tnatschl/psfiles/ -> 404).
  igi-web.tugraz.at (the old IGI web host, e.g.
  https://igi-web.tugraz.at/people/maass/publications.html): TLS
  connection reset by peer (curl exit 35), no agent-proxy line. No exact
  address of a copy of this paper on that host was located.
- Wayback capture of the Natschläger page,
  http://web.archive.org/web/20160221061928/http://www.igi.tugraz.at:80/tnatschl/ :
  "Blocked by egress policy" (this session's network policy). Not worked around.
- TU Graz Pure, https://graz.elsevierpure.com/en/publications/?search=... and
  https://tugraz.elsevierpure.com/en/publications/real-time-computation-at-the-edge-of-chaos-in-recurrent-neural-ne/ :
  Cloudflare "Just a moment..." challenge (403). Stopped.
- Web searches found no author, course or repository copy of the Neural
  Computation article itself.

Outcome for the work: no lawful copy located at an exact address ->
**Unavailable** (ADR-041), with the caveat that igi-web.tugraz.at
(reset) and web.archive.org (egress policy) could not be searched; the
owner may allow them.

Neighbour located: the companion NIPS 2004 paper, Bertschinger,
Natschläger & Legenstein, "At the Edge of Chaos: Real-time Computations
and Self-Organized Criticality in Recurrent Neural Networks", NIPS 17,
pp. 145-152, on the proceedings site:
https://proceedings.nips.cc/paper_files/paper/2004/file/f8da71e562ff44a2bc7edf3578c593da-Paper.pdf
(publisher's open proceedings). Not held in record/literature.d (no hit
for the title or "Legenstein" as author).
