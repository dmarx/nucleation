# scratch/readers/sweep-pages.md

Which of the sweep's 17 landing pages hold a lawful copy (ADR-108 running notes).

Checked 2026-11-22. Outcomes: (a) full text reached, (b) metadata only or
restricted, (c) obstacle.

## LIT-1409 (Schulz-Hardt et al. 2006, hidden profiles)

- (c) http://mediatum.ub.tum.de/node?id=1156056 redirects to https and
  returns an Anubis "Making sure you're not a bot!" proof-of-work page
  (HTTP 200, /.within.website/). Stopped; not retried. 2026-11-22.

## LIT-1481 (Tilly 1985, War Making and State Making)

- (c) http://deepblue.lib.umich.edu/bitstream/2027.42/51028/1/256.pdf now
  serves the DSpace 7 Angular shell (HTML, not the PDF). Its documented
  REST API (https://deepblue.lib.umich.edu/server/api/pid/find?id=hdl:2027.42/51028)
  returned a Cloudflare "Just a moment..." challenge. Stopped. 2026-11-22.

## LIT-1567 (Karnkowska et al. 2016, Current Biology)

- (b) https://lup.lub.lu.se/search/publication/cfb80059-c720-48dd-9030-f0f47b3ba35b
  is a metadata record (authors Karnkowska ... Hampl, DOI matches); its
  only links are the Research Portal page, the DOI and Google Scholar. No
  file.

## LIT-1586 (Łukasik et al. 2018, PNAS)

- (b) https://ruj.uj.edu.pl/handle/item/54669: DSpace REST API
  (server/api/pid/find?id=item/54669, item ff8fb082-...) gives title,
  authors and DOI matching, dc.rights "Dodaję tylko opis bibliograficzny"
  (bibliographic description only), share type "otwarte czasopismo" (open
  journal, open 6 months after publication). The item has no bundles or
  bitstreams. Metadata only.

## LIT-1639 (Cervera, van der Schaft, Baños 2007, Automatica)

- (c), copy located: the RUG Pure record lists
  https://research.rug.nl/files/2818803/2007AutomaticaCervera.pdf,
  labelled "Final publisher's version, 366 KB" (title and authors on the
  record match the LIT). The file request returned HTTP 403 with a
  Cloudflare "Just a moment..." challenge. Stopped. 2026-11-22. Pure's web
  service needs an API key, so no documented open route was tried.

## LIT-1764 (Pembrey et al. 2006, EJHG)

- (b) Bristol Pure record: metadata only; "Access to Document" gives the
  DOI and a nature.com abstract link. No file.

## LIT-1862 (Contrast effects in stereotype formation, JESP 2002)

- (b) VU Pure record: metadata only; "Access to Document" gives the DOI
  and an old ScienceDirect link. No file.

## LIT-1947 (Metzinger 2021, Artificial Suffering)

- (a) https://zenodo.org/api/records/7034864/files/artificial-suffering-an-argument-for-a-global-moratorium-on-synthetic-phenomenology.pdf/content
  (Zenodo records API; record access "open", licence cc-zero). Published
  version: page 1 is the J. AI. Consci. 8(1) 43-66 typeset article,
  marked "OPEN ACCESS", "(c) The Author(s)". Title, author (Thomas
  Metzinger) and DOI checked. Downloaded to
  downloads/sweep-d/LIT-1947/metzinger-2021-artificial-suffering.pdf.

## LIT-1954 (Bartholomew, Ntoumanis, Ryan, Thogersen-Ntoumani 2011, JSEP)

- (c), copy located: the Birmingham Pure record (authors and title match)
  lists https://research.birmingham.ac.uk/files/2921594/Ntoumanis_2011_Journal_of_Sport_and_Exercise_Psychology.pdf
  (no version label shown). The file request returned HTTP 403 with a
  Cloudflare "Just a moment..." challenge. Stopped. 2026-11-22.

## LIT-1996 (Howard, Gagné, Bureau 2017, Psychological Bulletin)

- The given address redirects to https://curate.curtin.edu.au/ and
  answers HTTP 202 with x-amzn-waf-action: challenge (AWS WAF); stopped
  there. curate.curtin.edu.au is a Figshare repository, so its documented
  API was the route (ADR-101): api.figshare.com/v2/articles/31678804
  (handle 20.500.11937/69700, file 268067.pdf, "Is open access: Open
  access", not embargoed).
- (a) https://ndownloader.figshare.com/files/62711305. Author manuscript:
  the repository note says "This paper is not the copy of record"
  (c) APA 2017; page 1 is the authors' manuscript with running head.
  Title and authors (Joshua L. Howard, Marylène Gagné, Julien S. Bureau)
  checked. Downloaded to downloads/sweep-d/LIT-1996/268067.pdf.

## LIT-2065 (Fajstrup, Raussen, Goubault 2006, TCS)

- (b) https://vbn.aau.dk/da/publications/algebraic-topology-and-concurrency/
  (AAU Pure; title and authors match): metadata only. "Adgang til
  dokumentet" gives the DOI and an AUB catalogue link. No file.

## LIT-2175 (The 10 Principles of Burning Man)

- (a) The page is the work. https://burningman.org/about/10-principles/
  redirects to https://burningman.org/about-us/10-principles/ (HTTP 200,
  title "The 10 Principles - Burning Man Project", all ten principle
  headings present; the Cloudflare script on it is the passive beacon, not
  a challenge). Published version, by its publisher. Saved to
  downloads/sweep-d/LIT-2175/burningman-10-principles-2026-11-22.html.

## LIT-2403 (Dierickx, Gehrke, Lindén 2026, Journalism)

- (c), copy located: the RUG Pure record (title, authors and DOI match;
  CC BY) lists https://research.rug.nl/files/1574482845/dierickx-et-al-2026-from-normative-principles-to-epistemic-governance-a-workflow-based-analysis-of-european-journalism.pdf,
  labelled "Proof, 1.73 MB, Licence: CC BY" (the publisher's typeset
  open-access article). The file request returned HTTP 403 with a
  Cloudflare "Just a moment..." challenge. Stopped. 2026-11-22.

## LIT-2432 (Errando 2026, Journalism)

- (b) The given biblio.vub.ac.be address redirects to the VUB library
  catalogue's search start page (VUBIS/Iguana, JavaScript-only, no record
  shown). The same UUID on the VUB Pure portal,
  https://researchportal.vub.be/en/publications/7614c139-5645-411d-b810-b9b40f6bef1a,
  is the record (title matches; author Aina Errando): metadata only,
  "Access to Document" gives the DOI alone. No file.

## LIT-2452 (Pape, Helmers, Iaria, Wagner, Runge 2025, IJIO)

- (b) Bristol Pure record (title and authors match): metadata only.
  "Access to Document" gives the DOI, "Licence: CC BY". No file on the
  page; the CC BY publisher version is behind the DOI, not tried here.

## LIT-2625 (Hsu, Zhen, Stone, Joannopoulos, Soljačić 2016, Nat Rev Mater)

- (c), copy located: the OSTI record (and OSTI's documented API,
  https://www.osti.gov/api/v1/records/1557734) lists an "Accepted
  Manuscript (DOE)", fulltext https://www.osti.gov/servlets/purl/1557734.
  Title and authors match. That address redirects to
  https://dspace.mit.edu/bitstreams/2170bf2f-dea3-4b1d-8f6c-4f5243d84880/download,
  which answered HTTP 429 "Web Firewall ... protection has temporarily
  kicked in". Stopped; not retried. 2026-11-22.

## LIT-2787 (Topological defects propagate information in deep neural networks)

- (c) https://openreview.net/forum?id=fM5s2Tqe0t redirects to
  https://openreview.net/challenge?redirect=... ("Verifying your
  browser"). Its documented API, https://api2.openreview.net/notes?id=fM5s2Tqe0t,
  answered HTTP 403 ChallengeRequiredError. Stopped; the /pdf address on
  the same host was not tried. 2026-11-22.
