# scratch/studies/unfetched-api-sweep/test_sweep.py
from sweep import candidates, classify


def test_classify_pdf_and_html():
    assert classify(200, "application/pdf", b"%PDF-1.5") == "pdf"
    assert classify(200, "application/octet-stream", b"%PDF-1.4 x") == "pdf"
    assert classify(200, "text/html; charset=utf-8", b"<html>paper</html>") == "html"


def test_classify_challenges():
    assert classify(403, "text/html", b"") == "challenge"
    assert classify(200, "text/html", b"<title>Just a moment...</title>") == "challenge"
    assert classify(200, "text/html", b"<script src=/_Incapsula_Resource>") == "challenge"
    assert classify(429, "", b"") == "challenge"
    assert classify(401, "", b"") == "refused"


def test_classify_errors():
    assert classify(None, "", b"") == "error"
    assert classify(404, "", b"") == "not-found"
    assert classify(500, "", b"") == "error"


def test_candidates_order_dedupe_and_skip_resolvers():
    up = {"oa_locations": [
        {"url_for_pdf": "https://repo.example/a.pdf", "host_type": "repository",
         "version": "acceptedVersion", "url_for_landing_page": "https://repo.example/a"}]}
    oa = {"locations": [
        {"pdf_url": "https://repo.example/a.pdf", "landing_page_url": "https://doi.org/10.1/x",
         "version": "publishedVersion", "source": {"type": "journal"}},
        {"pdf_url": None, "landing_page_url": "https://citeseerx.example/v",
         "version": "submittedVersion", "source": None}]}
    c = candidates(oa, up)
    urls = [x["url"] for x in c]
    assert urls == ["https://repo.example/a.pdf", "https://repo.example/a", "https://citeseerx.example/v"]
    assert c[0]["via"] == "unpaywall"


def test_candidates_empty():
    assert candidates(None, None) == []
