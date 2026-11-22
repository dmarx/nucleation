import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "epmc_lookup", Path(__file__).with_name("epmc_lookup.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_classify():
    assert m.classify(None, None, None) == "not-found"
    assert m.classify({"pmcid": "PMC1"}, 200, None) == "open-full-text"
    assert m.classify({"pmcid": "PMC1"}, 404, None) == "abstract-only"
    assert m.classify({"pmid": "1"}, None, None) == "abstract-only"
    assert m.classify({"pmcid": "PMC1"}, 500, "fullTextXML HTTP 500") == "obstacle"


def test_lead_codes_and_field():
    text = "x\n- [LIT-180](../a.md) (Unfetched)\n- [LIT-2](b) x\n  - [LIT-3](c)\n"
    assert m.lead_codes(text) == ["LIT-180", "LIT-2"]
    fm = "doi: '10.1/x'\ntitle: 'It''s a title'\n"
    assert m.frontmatter_field(fm, "doi") == "10.1/x"
    assert m.frontmatter_field(fm, "title") == "It's a title"
    assert m.frontmatter_field(fm, "url") is None


def test_pick():
    res = [{"doi": "10.1/A", "title": "Other"}, {"doi": "", "title": "The Title: here"}]
    assert m.pick(res, "10.1/a", None) is res[0]
    assert m.pick(res, None, "The title here") is res[1]
    assert m.pick(res, "10.9/z", None) is None
