"""LEAD-054: search Europe PMC (and arXiv) for experience-sampling studies of
flow with affect reported during the episode.

Run:  python3 -I search.py OUTDIR
Writes OUTDIR/hits.json (deduplicated records with abstracts) and prints counts
per query. No email address is sent to any service (ADR-008).
"""
import json
import sys
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
ARXIV = "http://export.arxiv.org/api/query"
UA = {"User-Agent": "nucleation-lead-054-search/1.0"}

# Europe PMC query syntax: TITLE_ABS restricts to title and abstract.
EPMC_QUERIES = [
    'TITLE_ABS:"flow" AND (TITLE_ABS:"experience sampling" OR TITLE_ABS:"ecological momentary") AND (TITLE_ABS:"affect" OR TITLE_ABS:"happiness" OR TITLE_ABS:"emotion" OR TITLE_ABS:"enjoyment" OR TITLE_ABS:"mood")',
    '(TITLE_ABS:"flow experience" OR TITLE_ABS:"experience of flow" OR TITLE_ABS:"flow state") AND (TITLE_ABS:"experience sampling" OR TITLE_ABS:"ecological momentary" OR TITLE_ABS:"diary" OR TITLE_ABS:"ESM")',
    'TITLE_ABS:"flow" AND TITLE_ABS:"paradox of work"',
    'TITLE_ABS:"optimal experience" AND (TITLE_ABS:"experience sampling" OR TITLE_ABS:"ESM")',
    '(TITLE_ABS:"flow experience" OR TITLE_ABS:"flow state") AND (TITLE_ABS:"positive affect" OR TITLE_ABS:"valence" OR TITLE_ABS:"pleasantness") AND (TITLE_ABS:"during" OR TITLE_ABS:"momentary" OR TITLE_ABS:"real-time" OR TITLE_ABS:"in situ")',
]
# Second part of the lead: a measure separating intrinsic pleasantness from
# goal-conduciveness valence in flow.
MEASURE_QUERIES = [
    'TITLE_ABS:"flow" AND (TITLE_ABS:"intrinsic pleasantness" OR TITLE_ABS:"goal conduciveness" OR TITLE_ABS:"goal-conduciveness")',
    '(TITLE_ABS:"intrinsic pleasantness") AND (TITLE_ABS:"goal conduciveness" OR TITLE_ABS:"goal-conduciveness") AND (TITLE_ABS:"experience sampling" OR TITLE_ABS:"momentary" OR TITLE_ABS:"absorption" OR TITLE_ABS:"engagement")',
]
ARXIV_QUERIES = [
    'abs:"flow experience" AND abs:"experience sampling"',
    'abs:"flow state" AND (abs:"affect" OR abs:"emotion") AND (abs:"momentary" OR abs:"real-time" OR abs:"in-game")',
]


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def epmc(query):
    out, cursor = [], "*"
    while True:
        params = {"query": query, "format": "json", "pageSize": "1000",
                  "resultType": "core", "cursorMark": cursor}
        data = json.loads(get(EPMC + "?" + urllib.parse.urlencode(params)))
        res = data.get("resultList", {}).get("result", [])
        out += res
        nxt = data.get("nextCursorMark")
        if not res or nxt == cursor or len(out) >= data.get("hitCount", 0):
            return data.get("hitCount", 0), out
        cursor = nxt


def arxiv(query):
    import xml.etree.ElementTree as ET
    params = {"search_query": query, "max_results": "200"}
    root = ET.fromstring(get(ARXIV + "?" + urllib.parse.urlencode(params)))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    recs = []
    for e in root.findall("a:entry", ns):
        recs.append({
            "source": "arXiv",
            "id": e.findtext("a:id", "", ns).rsplit("/", 1)[-1],
            "title": " ".join(e.findtext("a:title", "", ns).split()),
            "abstractText": " ".join(e.findtext("a:summary", "", ns).split()),
            "pubYear": e.findtext("a:published", "", ns)[:4],
        })
    return len(recs), recs


def key(rec):
    return (rec.get("doi") or rec.get("id") or rec.get("title", "")).lower()


def main(outdir):
    seen = {}
    for q in EPMC_QUERIES:
        n, recs = epmc(q)
        print(f"EPMC\t{n}\t{q}")
        for r in recs:
            r.setdefault("queries", [])
            k = key(r)
            seen.setdefault(k, {**{f: r.get(f) for f in (
                "id", "source", "pmid", "pmcid", "doi", "title", "authorString",
                "journalTitle", "pubYear", "abstractText", "isOpenAccess",
                "pubType")}, "queries": []})["queries"].append(q[:40])
    for q in MEASURE_QUERIES:
        n, recs = epmc(q)
        print(f"EPMC-measure\t{n}\t{q}")
        for r in recs:
            print(f"  {r.get('pubYear')}\t{r.get('doi')}\t{r.get('title')}")
    for q in ARXIV_QUERIES:
        n, recs = arxiv(q)
        print(f"arXiv\t{n}\t{q}")
        for r in recs:
            seen.setdefault(key(r), {**r, "queries": []})["queries"].append(q[:40])
    print(f"unique records: {len(seen)}")
    with open(f"{outdir}/hits.json", "w") as f:
        json.dump(list(seen.values()), f, indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
