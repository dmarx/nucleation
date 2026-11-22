"""Fetch arXiv abstracts by id_list. No email sent."""
import sys, urllib.request, urllib.parse
import xml.etree.ElementTree as ET

ids = sys.argv[1]
url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
    {"id_list": ids, "max_results": 30}
)
data = urllib.request.urlopen(url, timeout=60).read()
ns = {"a": "http://www.w3.org/2005/Atom"}
t = ET.fromstring(data)
for e in t.findall("a:entry", ns):
    print("ID:", e.find("a:id", ns).text.split("/abs/")[-1])
    print("TITLE:", e.find("a:title", ns).text.strip().replace("\n", " "))
    authors = [a.find("a:name", ns).text for a in e.findall("a:author", ns)]
    print("AUTHORS:", ", ".join(authors))
    cat = e.find("{http://arxiv.org/schemas/atom}primary_category")
    print("CAT:", cat.get("term") if cat is not None else "?")
    print("PUB:", e.find("a:published", ns).text[:10])
    print("ABSTRACT:", e.find("a:summary", ns).text.strip().replace("\n", " "))
    print("-" * 80)
