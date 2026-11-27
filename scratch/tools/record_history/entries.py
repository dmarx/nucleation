# scratch/tools/record_history/entries.py
"""Parse a record entry and normalize it so that mechanical edits vanish."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

import yaml

try:  # libyaml is ~10x faster, and the history holds ~100k blobs
    _Loader = yaml.CSafeLoader
except AttributeError:  # pragma: no cover
    _Loader = yaml.SafeLoader

CODE = r"[A-Z]+-(?:tmp[a-z0-9]+|\d+)"
CODE_RE = re.compile(rf"\b({CODE})\b")
_PATH_RE = re.compile(rf"(?:^|/)({CODE})\.md$")
_LINK_RE = re.compile(rf"\[({CODE})\]\([^)]*\)")
_DIRECTIVE_RE = re.compile(r"<!--\s*inactive-ok[^>]*-->", re.S)
_WS_RE = re.compile(r"\s+")


def parse_entry(text: str) -> tuple[dict, str]:
    """Split an entry into its front matter and body; never raise."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    try:
        fields = yaml.load(text[4:end], Loader=_Loader) or {}
    except yaml.YAMLError:
        return {}, text[end + 5:]
    if not isinstance(fields, dict):
        fields = {}
    return fields, text[end + 5:]


def code_of_path(path: str) -> str | None:
    """The entry code a scheme file is named for, or None for other files."""
    m = _PATH_RE.search(path)
    return m.group(1) if m else None


def canonical(code: str, alias: dict[str, str]) -> str:
    """Follow alias chains (temporary code to concrete code) to the end."""
    seen = {code}
    while code in alias and alias[code] not in seen:
        code = alias[code]
        seen.add(code)
    return code


def normalize_text(text: str, alias: dict[str, str]) -> str:
    """Bare codes, canonical codes, single spaces."""
    text = _LINK_RE.sub(r"\1", text)
    text = CODE_RE.sub(lambda m: canonical(m.group(1), alias), text)
    return _WS_RE.sub(" ", text).strip()


def normalize_body(body: str, alias: dict[str, str]) -> list[str]:
    """Body lines with link targets, directives and whitespace normalized."""
    body = _DIRECTIVE_RE.sub("", body)
    lines = (normalize_text(line, alias) for line in body.splitlines())
    return [line for line in lines if line]


def as_codes(value, alias: dict[str, str]) -> set[str]:
    """The canonical codes a relation field names, whatever its shape."""
    if value is None:
        return set()
    if isinstance(value, str):
        value = [value]
    out: set[str] = set()
    for item in value if isinstance(value, list) else []:
        if isinstance(item, dict):  # e.g. {code: ..., note: ...}
            item = item.get("code") or next(iter(item.values()), "")
        for m in CODE_RE.finditer(str(item)):
            out.add(canonical(m.group(1), alias))
    return out


@dataclass
class Schema:
    """What luria.yaml says about each scheme's relation fields."""
    forward: dict[str, set[str]] = field(default_factory=dict)
    derived: dict[str, set[str]] = field(default_factory=dict)
    active: dict[str, set[str]] = field(default_factory=dict)

    @classmethod
    def from_config(cls, config: dict) -> "Schema":
        s = cls()
        for name, scheme in (config.get("schemes") or {}).items():
            refs = scheme.get("references") or {}
            s.forward[name] = {k for k, v in refs.items() if not (v or {}).get("derived")}
            s.derived[name] = {k for k, v in refs.items() if (v or {}).get("derived")}
            act = scheme.get("active") or []
            s.active[name] = set(act if isinstance(act, list) else [act])
        return s

    def scheme_of(self, code: str) -> str | None:
        prefix = code.split("-", 1)[0]
        return prefix if prefix in self.forward else None

    def forward_fields(self, scheme: str) -> set[str]:
        return self.forward.get(scheme, set())

    def derived_fields(self, scheme: str) -> set[str]:
        return self.derived.get(scheme, set())
