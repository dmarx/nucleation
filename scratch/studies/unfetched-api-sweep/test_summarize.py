# scratch/studies/unfetched-api-sweep/test_summarize.py
from summarize import best, queue_class


def rec(*results_hosts):
    return {"probes": [{"result": r, "host": h} for r, h in results_hosts]}


def test_best_prefers_pdf_over_earlier_challenge():
    o, p = best(rec(("challenge", "a"), ("pdf", "b")))
    assert o == "pdf" and p["host"] == "b"


def test_best_no_candidate():
    assert best({"probes": []}) == ("no-candidate", None)


def test_queue_classes():
    assert queue_class("pdf", {"host": "x"}) == "read"
    assert queue_class("html", {"host": "pubmed.ncbi.nlm.nih.gov"}) == "none"
    assert queue_class("html", {"host": "research.rug.nl"}) == "check"
    assert queue_class("challenge", {"host": "x"}) == "none"
