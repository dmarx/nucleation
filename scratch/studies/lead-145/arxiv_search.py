"""Query the arXiv API and print id | title | published. No email sent."""
import sys, urllib.request, urllib.parse
import xml.etree.ElementTree as ET

q = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
    {"search_query": q, "start": 0, "max_results": n, "sortBy": "relevance"}
)
data = urllib.request.urlopen(url, timeout=60).read()
ns = {"a": "http://www.w3.org/2005/Atom",
      "o": "http://a9.com/-/spec/opensearch/1.1/"}
t = ET.fromstring(data)
tot = t.find("o:totalResults", ns)
print("total:", tot.text if tot is not None else "?")
for e in t.findall("a:entry", ns):
    aid = e.find("a:id", ns).text.split("/abs/")[-1]
    title = e.find("a:title", ns).text.strip().replace("\n", " ")
    pub = e.find("a:published", ns).text[:10]
    print(aid, "|", title, "|", pub)
