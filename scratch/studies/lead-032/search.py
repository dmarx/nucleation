"""LEAD-032 literature search: dismantling trials that remove safety behaviour
with exposure held fixed, and individual-level data showing hysteresis or
critical-transition signs in psychopathology.

Queries Europe PMC's REST search (resultType=core, abstracts included) with the
strings in QUERIES, each restricted to titles and abstracts (TITLE_ABS:).
A first run without the restriction matched full texts too (1,623 to 11,947
hits a query) and was discarded. No email address or other contact detail is sent
(ADR-008). On any HTTP error the query is recorded as failed and not retried.

Writes results/hits.jsonl (one deduplicated record per work, with the queries
that found it, abstracts removed), results/abstracts.jsonl (not committed) and
results/counts.tsv. Run from anywhere:

    python3 -I scratch/studies/lead-032/search.py
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")
UA = "nucleation-lit-search/1.0 (research record; no contact)"
SB = '("safety behavior" OR "safety behaviour" OR "safety behaviors" OR "safety behaviours" OR "safety-seeking")'

QUERIES = {
    # D1: exposure with the safety behaviour dropped vs the same exposure with it kept
    "D1_exposure_sb_trial": SB + ' AND (exposure) AND (randomized OR randomised OR "controlled" OR "dismantling" OR "component") AND (eliminat* OR drop* OR fading OR removal OR "without safety" OR abandon* OR "use of safety" OR judicious)',
    # D2: reviews and meta-analyses of safety behaviour within exposure
    "D2_sb_reviews": SB + ' AND (exposure) AND ("meta-analysis" OR "meta-analytic" OR "systematic review" OR review)',
    # D3: dismantling / component designs in exposure-based CBT for anxiety
    "D3_dismantling": '(dismantling OR "component analysis" OR "additive design" OR "component study") AND (exposure) AND (anxiety OR panic OR "social phobia" OR "social anxiety" OR "obsessive" OR phobia)',
    # H1: critical slowing down / early warning signals in individual patients
    "H1_csd_individual": '("critical slowing down" OR "early warning signals" OR "early warning signal" OR "critical transition" OR "critical transitions") AND (depression OR depressive OR anxiety OR psychopathology OR "mental disorder" OR psychiatric) AND (individual OR "single patient" OR "single-subject" OR "n-of-1" OR idiographic OR "within-person")',
    # H2: hysteresis in psychopathology
    "H2_hysteresis": '(hysteresis) AND (depression OR depressive OR anxiety OR psychopathology OR "mental disorder" OR psychiatric OR panic OR "symptom network")',
    # H3: alternative stable states or tipping points with intensive time series
    "H3_bistability_ts": '("alternative stable states" OR bistability OR bistable OR "tipping point" OR "tipping points" OR "sudden gains" OR "sudden transitions") AND (depression OR anxiety OR psychopathology) AND ("time series" OR "experience sampling" OR "ecological momentary" OR "daily diary")',
    # Added after the first pass, to catch what the six queries missed.
    # D4: safety-behaviour manipulations in the disorders of the classic trials, without requiring "exposure"
    "D4_sb_disorders": SB + ' AND (panic OR agoraphobia OR "social phobia" OR "social anxiety" OR claustrophobi* OR "spider" OR "contamination" OR "obsessive") AND (experiment* OR randomi* OR trial OR condition)',
    # H4: hysteresis tested in psychological time series
    "H4_hysteresis_psych": '(hysteresis OR hysteretic) AND (affect OR mood OR emotion OR psychological OR "experience sampling" OR "symptom" OR "network theory")',
    # H5: critical slowing down as a personalized signal (Wichers line), any wording
    "H5_csd_personalized": '("critical slowing down" OR "early warning") AND (depression OR depressive OR "mood") AND (personalized OR personalised OR "single" OR patient OR "n = 1" OR "n=1")',
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def europepmc(query, max_hits=400):
    hits, cursor, total = [], "*", 0
    while len(hits) < max_hits:
        params = {"query": query, "format": "json", "resultType": "core",
                  "pageSize": "100", "cursorMark": cursor}
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(params)
        d = get(url)
        total = d.get("hitCount", 0)
        res = d.get("resultList", {}).get("result", [])
        for r in res:
            hits.append({
                "id": r.get("doi") or (r.get("source", "") + ":" + str(r.get("id"))),
                "doi": r.get("doi"),
                "pmid": r.get("pmid"),
                "pmcid": r.get("pmcid"),
                "title": r.get("title"),
                "authors": r.get("authorString"),
                "year": r.get("pubYear"),
                "journal": (r.get("journalInfo") or {}).get("journal", {}).get("title"),
                "pubtype": (r.get("pubTypeList") or {}).get("pubType"),
                "oa": r.get("isOpenAccess"),
                "cited": r.get("citedByCount"),
                "abstract": r.get("abstractText"),
            })
        nxt = d.get("nextCursorMark")
        if not res or not nxt or nxt == cursor:
            break
        cursor = nxt
    return total, hits


def main(labels):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "hits.jsonl")
    merged = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                merged[rec["id"]] = rec
    counts = []
    for label in labels:
        q = "TITLE_ABS:(" + QUERIES[label] + ")"
        try:
            total, hits = europepmc(q)
        except urllib.error.HTTPError as e:
            counts.append((label, "HTTP %s" % e.code, 0))
            print(label, "HTTP", e.code, file=sys.stderr)
            continue
        counts.append((label, total, len(hits)))
        for h in hits:
            rec = merged.setdefault(h["id"], dict(h, queries=[]))
            if label not in rec["queries"]:
                rec["queries"].append(label)
        print(label, total, len(hits), file=sys.stderr)
    # Abstracts go to an uncommitted side file (see results/.gitignore), to
    # keep the committed hits file under 1 MB.
    apath = os.path.join(OUT, "abstracts.jsonl")
    abstracts = {}
    if os.path.exists(apath):
        with open(apath) as f:
            for line in f:
                a = json.loads(line)
                abstracts[a["id"]] = a["abstract"]
    for rec in merged.values():
        if rec.get("abstract"):
            abstracts[rec["id"]] = rec["abstract"]
        rec.pop("abstract", None)
    with open(path, "w") as f:
        for rec in merged.values():
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    with open(apath, "w") as f:
        for k, v in abstracts.items():
            f.write(json.dumps({"id": k, "abstract": v}, ensure_ascii=False) + "\n")
    with open(os.path.join(OUT, "counts.tsv"), "a") as f:
        for c in counts:
            f.write("%s\t%s\t%s\n" % c)


if __name__ == "__main__":
    main(sys.argv[1:] or list(QUERIES))
