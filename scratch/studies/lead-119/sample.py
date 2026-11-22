"""LEAD-119 internal-arm sampler. Usage:
python3 -I sample.py <danluu README.md> <download dir> <sample_log.jsonl>
Applies the sampling rule of codebook.md: candidates from the sections
"Config Errors" through "Uncategorized", deduplicated, shuffled with
random.Random(119), fetched in order; appends one line per candidate tried to
the log, resuming past candidates already logged; stops at 30 inclusions.
Inclusion rule 2 (own account of own incident) is judged by the coder at
coding time; an item failing it is logged there as excluded and the next is
taken."""
import hashlib, html, json, os, random, re, subprocess, sys


def candidates(md: str) -> list[str]:
    lines = md.splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("## Config Errors"))
    end = next(i for i, l in enumerate(lines) if l.startswith("## Other lists"))
    out, seen = [], set()
    for l in lines[start:end]:
        m = re.match(r"\s*\[[^\]]+\]\((https?://[^)\s]+)\)", l)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            out.append(m.group(1))
    return out


def shuffled(urls: list[str]) -> list[str]:
    u = list(urls)
    random.Random(119).shuffle(u)
    return u


BOT = re.compile(r"captcha|cf-chl|challenge-platform|just a moment|attention required|access denied", re.I)


def strip(h: str) -> str:
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(h)).strip()


def main():
    md, ddir, log = sys.argv[1:4]
    done = {}
    if os.path.exists(log):
        for l in open(log):
            r = json.loads(l)
            done[r["url"]] = r
    included = sum(1 for r in done.values() if r["result"] == "fetched")
    for url in shuffled(candidates(open(md).read())):
        if included >= 30:
            break
        if url in done:
            continue
        fn = os.path.join(ddir, hashlib.sha1(url.encode()).hexdigest()[:12] + ".html")
        p = subprocess.run(["curl", "-sS", "-L", "--max-time", "30", "-o", fn, "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        code = p.stdout.strip()
        rec = {"url": url, "http": code, "file": os.path.basename(fn)}
        if code != "200":
            rec["result"] = "excluded: http " + code
        else:
            raw = open(fn, errors="replace").read()
            text = strip(raw)
            words = len(text.split())
            rec["words"] = words
            if BOT.search(raw[:20000]) and words < 600:
                rec["result"] = "excluded: bot check"
            elif words < 300:
                rec["result"] = "excluded: under 300 words"
            else:
                rec["result"] = "fetched"
                open(fn[:-5] + ".txt", "w").write(text)
                included += 1
        with open(log, "a") as f:
            f.write(json.dumps(rec) + "\n")
        print(rec["result"], url, flush=True)


if __name__ == "__main__":
    main()
