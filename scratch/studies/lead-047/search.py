"""LEAD-047 literature search: a manipulation of a defensive process's authority
(or of its evidence access) with the represented threat held fixed.

Queries Europe PMC's REST search (abstracts included, resultType=core) and
Semantic Scholar's Graph API paper search, with the strings in QUERIES. No
email address or other contact detail is sent to either service (ADR-008).
Stops on any HTTP error (403/429 etc.) for that service without retrying.

Writes results/hits.jsonl (one deduplicated record per work, with the queries
that found it) and results/counts.tsv. Run:

    python3 -I scratch/studies/lead-047/search.py

The abstract-level pre-screen is in screen.py; the final screening table is
screening.tsv, coded by hand from the pre-screen.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")
UA = "nucleation-lit-search/1.0 (research record; no contact)"

# Each query targets one family of nearest design. The labels are used in
# the screening table.
QUERIES = {
    # Q1: belief corrected by instruction, avoidance measured afterwards
    "Q1_instructed": '(avoidance) AND ("instructed extinction" OR "verbal instructions" OR "instructed safety" OR "instructed removal") AND (expectancy OR "threat belief")',
    # Q2: explicit (instructed) threat probability, intervention on the arbitration
    "Q2_aac_intervention": '("approach-avoidance conflict" OR "approach avoidance conflict") AND ("threat probability" OR "explicit probability" OR "loss probability") AND (lorazepam OR benzodiazepine OR lesion OR TMS OR tDCS OR stimulation OR pharmacological OR anxiolytic)',
    # Q3: cost of avoidance manipulated, threat expectancy measured
    "Q3_costly": '("costly avoidance" OR "cost of avoidance" OR "avoidance costs") AND (expectancy OR "threat belief" OR "US expectancy")',
    # Q4: evidence access forced (response prevention), threat expectancy measured
    "Q4_response_prevention": '(avoidance) AND ("response prevention" OR "blocked avoidance" OR "avoidance prevention") AND ("US expectancy" OR "threat expectancy" OR "shock expectancy")',
    # Q5: dissociation of avoidance from threat belief
    "Q5_dissociation": '(avoidance) AND (dissociation OR "despite" OR "persistent avoidance" OR "irrational avoidance") AND ("threat expectancy" OR "US expectancy" OR "threat belief") AND (extinction OR safety)',
    # Q6: safety behaviour manipulated, threat belief measured
    "Q6_safety_behaviour": '("safety behavior" OR "safety behaviour" OR "safety behaviors" OR "safety behaviours") AND (fading OR elimination OR "experimental manipulation" OR "randomized") AND ("threat belief" OR "threat expectancy" OR "harm expectancy" OR "belief rating")',
    # Q7: defusion / acceptance manipulations of the link from fear to action
    # Q8: drug or lesion in an approach-avoidance conflict task with explicit threat level
    "Q8_aac_drug_lesion": '("approach-avoidance conflict" OR "approach avoidance conflict" OR "passive avoidance") AND (human OR humans OR participants) AND (lorazepam OR diazepam OR benzodiazepine OR ketamine OR "amygdala lesion" OR "amygdala lesions" OR "hippocampal lesion" OR "Urbach-Wiethe")',
    # Q9: instruction or cognitive strategy changes avoidance while expectancy is unchanged
    "Q9_instruction_dissociation": '(avoidance) AND (instruction OR instructions OR "cognitive strategy" OR "cognitive-behavioural" OR "cognitive-behavioral") AND ("threat expectancy" OR "US expectancy" OR "US-expectancy") AND ("without" OR "did not alter" OR "unchanged" OR "dissociat")',
    "Q7_defusion": '(defusion OR acceptance) AND (avoidance OR "approach behavior" OR "behavioral approach") AND ("threat expectancy" OR "US expectancy" OR "fear expectancy" OR "harm expectancy") AND (experiment OR experimental OR randomized)',
}

S2_QUERIES = {
    "S1": "avoidance persists after instructed extinction threat expectancy",
    "S2": "approach-avoidance conflict explicit threat probability anxiolytic",
    "S3": "costly avoidance threat expectancy dissociation",
    "S4": "avoidance behavior dissociated from threat belief manipulation",
    "S5": "manipulating avoidance cost holding threat constant",
}


SKIP_S2 = True


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def europepmc(query, max_hits=300):
    hits, cursor = [], "*"
    while len(hits) < max_hits:
        params = {"query": query, "format": "json", "resultType": "core",
                  "pageSize": "100", "cursorMark": cursor}
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(params)
        d = get(url)
        total = d.get("hitCount", 0)
        res = d.get("resultList", {}).get("result", [])
        for r in res:
            hits.append({
                "source": "europepmc",
                "id": r.get("id"),
                "pmid": r.get("pmid"),
                "pmcid": r.get("pmcid"),
                "doi": r.get("doi"),
                "title": r.get("title"),
                "authors": r.get("authorString"),
                "year": r.get("pubYear"),
                "journal": (r.get("journalInfo") or {}).get("journal", {}).get("title"),
                "abstract": r.get("abstractText") or "",
                "open_access": r.get("isOpenAccess"),
            })
        nxt = d.get("nextCursorMark")
        if not res or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.5)
    return total, hits


def s2(query, limit=100):
    params = {"query": query, "limit": str(limit),
              "fields": "title,abstract,year,externalIds,authors,venue,openAccessPdf"}
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    d = get(url)
    out = []
    for p in d.get("data", []):
        ext = p.get("externalIds") or {}
        out.append({
            "source": "s2",
            "id": p.get("paperId"),
            "pmid": ext.get("PubMed"),
            "pmcid": ("PMC" + ext["PubMedCentral"]) if ext.get("PubMedCentral") else None,
            "doi": ext.get("DOI"),
            "title": p.get("title"),
            "authors": ", ".join(a.get("name", "") for a in (p.get("authors") or [])),
            "year": p.get("year"),
            "journal": p.get("venue"),
            "abstract": p.get("abstract") or "",
            "open_access": bool(p.get("openAccessPdf")),
        })
    return d.get("total", len(out)), out


def key(h):
    if h.get("doi"):
        return "doi:" + h["doi"].lower()
    return "t:" + "".join(c for c in (h.get("title") or "").lower() if c.isalnum())[:80]


def main():
    """With labels as arguments, run only those Europe PMC queries and merge
    their hits into the existing results (used to fill in queries that
    failed with a server error on an earlier run)."""
    os.makedirs(OUT, exist_ok=True)
    only = sys.argv[1:]
    merged, counts = {}, []
    if only:
        with open(os.path.join(OUT, "hits.jsonl")) as f:
            for line in f:
                h = json.loads(line)
                merged[key(h)] = h
        with open(os.path.join(OUT, "counts.tsv")) as f:
            next(f)
            counts = [tuple(l.rstrip("\n").split("\t")) for l in f if l.split("\t")[0] not in only]
    for label, q in QUERIES.items():
        if only and label not in only:
            continue
        try:
            total, hits = europepmc(q)
        except urllib.error.HTTPError as e:
            # Recorded, not retried; a 403 or 429 stops the service, a
            # server error (5xx) skips only this query.
            print(f"Europe PMC failed at {label}: HTTP {e.code}; not retried", file=sys.stderr)
            counts.append((label, "europepmc", q, f"HTTP {e.code}", 0))
            if e.code in (403, 429):
                break
            continue
        counts.append((label, "europepmc", q, total, len(hits)))
        for h in hits:
            m = merged.setdefault(key(h), dict(h, queries=[]))
            m["queries"].append(label)
            if not m.get("abstract") and h.get("abstract"):
                m["abstract"] = h["abstract"]
    # Semantic Scholar answered the first query with HTTP 429 on 2026-11-22;
    # per the brief it is not retried, so later runs skip it.
    for label, q in ({} if (SKIP_S2 or only) else S2_QUERIES).items():
        try:
            total, hits = s2(q)
        except urllib.error.HTTPError as e:
            print(f"Semantic Scholar stopped at {label}: HTTP {e.code}; not retried", file=sys.stderr)
            counts.append((label, "s2", q, f"HTTP {e.code}", 0))
            break
        counts.append((label, "s2", q, total, len(hits)))
        for h in hits:
            m = merged.setdefault(key(h), dict(h, queries=[]))
            m["queries"].append(label)
            if not m.get("abstract") and h.get("abstract"):
                m["abstract"] = h["abstract"]
        time.sleep(3)
    with open(os.path.join(OUT, "hits.jsonl"), "w") as f:
        for h in merged.values():
            f.write(json.dumps(h) + "\n")
    with open(os.path.join(OUT, "counts.tsv"), "w") as f:
        f.write("label\tservice\tquery\thit_count\tretrieved\n")
        for row in counts:
            f.write("\t".join(str(x) for x in row) + "\n")
    print(f"{len(merged)} unique works")
    for row in counts:
        print(row[0], row[1], row[3], row[4])


if __name__ == "__main__":
    main()
