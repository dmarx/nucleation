# scratch/tools/chatgpt_share.py: decode a saved ChatGPT share page into numbered turns
"""Turn a public ChatGPT share page into the verbatim text the record files
from (the read-and-file skill, step 1; ADR-068).

Fetch the page with curl first; the repository's settings allow it:

    curl -sS -o share.html \\
      -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36" \\
      -H "Accept: text/html" https://chatgpt.com/share/<id>

then decode it:

    python3 -I scratch/tools/chatgpt_share.py share.html > exchange.txt

The page carries the conversation as a turbo-stream payload split across
`streamController.enqueue("...")` script calls: one flat table of values, in
which a dict's keys are `_<i>` pointers to string entries and its values are
indices into the table. The decoder rebuilds the conversation, walks from
`current_node` back to the root, so that only the branch that was shared
comes out, and numbers the turns U1… for the user and A1… for the assistant.
It drops system and tool messages, assistant messages addressed to a tool,
hidden context and redacted plugin output.

The format is not a published interface. When the page changes shape the
decoder raises ShareFormatError rather than writing a partial transcript;
it never guesses.
"""
import datetime
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ENQUEUE = re.compile(r'streamController\.enqueue\((".*?")\);?\s*</script>', re.S)
REDACTED = "The output of this plugin was redacted."


class ShareFormatError(ValueError):
    """The page is not a share page in the format this decoder knows."""


@dataclass
class Turn:
    label: str
    role: str
    time: str
    text: str


@dataclass
class Exchange:
    title: str
    turns: list[Turn] = field(default_factory=list)


def _table(html: str) -> list:
    chunks = ENQUEUE.findall(html)
    if not chunks:
        raise ShareFormatError("no streamController.enqueue payload on the page: "
                               "a challenge page, a login wall, or a changed format")
    data = "".join(json.loads(c) for c in chunks)
    first = next((line for line in data.split("\n") if line.strip()), "")
    try:
        table = json.loads(first)
    except json.JSONDecodeError as e:
        raise ShareFormatError(f"the payload's first line is not JSON: {e}") from e
    if not isinstance(table, list):
        raise ShareFormatError("the payload's first line is not a value table")
    return table


def _resolve(table: list):
    cache: dict[int, object] = {}

    def res(i):
        if not isinstance(i, int):
            return i
        if i < 0:
            return None
        if i in cache:
            return cache[i]
        v = table[i]
        if isinstance(v, dict):
            out: dict = {}
            cache[i] = out
            for k, val in v.items():
                key = table[int(k[1:])] if k.startswith("_") else k
                out[key] = res(val)
            return out
        if isinstance(v, list):
            out_l: list = []
            cache[i] = out_l
            out_l.extend(res(x) for x in v)
            return out_l
        return v

    return res


def _conversation(table: list) -> dict:
    res = _resolve(table)
    for i, v in enumerate(table):
        if isinstance(v, dict) and any(
                k.startswith("_") and table[int(k[1:])] == "mapping" for k in v):
            conv = res(i)
            if isinstance(conv.get("mapping"), dict):
                return conv
    raise ShareFormatError("no conversation `mapping` in the payload")


def _text(content: dict) -> str:
    parts = content.get("parts") or []
    return "\n".join(p if isinstance(p, str) else (p.get("text", "") if isinstance(p, dict) else "")
                     for p in parts if p).strip("\n")


def decode(html: str) -> Exchange:
    """Decode a share page's HTML into the shared branch's numbered turns."""
    conv = _conversation(_table(html))
    mapping, cur = conv["mapping"], conv.get("current_node")
    if cur not in mapping:
        raise ShareFormatError("the conversation's `current_node` is missing from its mapping")
    chain = []
    while cur:
        node = mapping[cur]
        chain.append(node)
        cur = node.get("parent")
    exchange = Exchange(title=conv.get("title") or "")
    counts = {"user": 0, "assistant": 0}
    for node in reversed(chain):
        m = node.get("message")
        if not m:
            continue
        role = (m.get("author") or {}).get("role")
        content = m.get("content") or {}
        text = _text(content)
        if role not in counts or not text.strip():
            continue
        if content.get("content_type") not in ("text", "multimodal_text"):
            continue
        if (m.get("metadata") or {}).get("is_visually_hidden_from_conversation"):
            continue
        if role == "assistant" and (m.get("recipient") not in (None, "all") or text.strip() == REDACTED):
            continue
        counts[role] += 1
        ts = m.get("create_time")
        when = (datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
                if ts else "")
        label = ("U" if role == "user" else "A") + str(counts[role])
        exchange.turns.append(Turn(label, role, when, text))
    if not exchange.turns:
        raise ShareFormatError("the shared branch has no user or assistant turns")
    return exchange


def render(exchange: Exchange) -> str:
    """The verbatim text: a TITLE line, then one headed block per turn."""
    blocks = [f"===== {t.label} ({t.role}) {t.time} =====\n{t.text}\n" for t in exchange.turns]
    return f"TITLE: {exchange.title}\n\n" + "\n".join(blocks)


def main(page: str) -> None:
    """Print the decoded exchange from a saved share page."""
    print(render(decode(Path(page).read_text(encoding="utf-8"))), end="")


if __name__ == "__main__":
    import fire

    fire.Fire(main)
