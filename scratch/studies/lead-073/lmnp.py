"""Pure-numpy forward passes of GPT-2 and GPT-NeoX (Pythia) checkpoints, CPU only.

No torch, no transformers: the weights are read from a .safetensors file with
a small parser, the byte-level BPE tokenizer is reimplemented from vocab and
merges. Only what LEAD-073's measurement needs: the final-layer-norm output
f(x) at each position (the representation that enters the logits), the
unembedding matrix g, and the next-token logits.
"""
from __future__ import annotations

import json
import struct
from dataclasses import dataclass

import numpy as np
import regex

_DT = {"F32": np.float32, "F16": np.float16, "BF16": None, "I64": np.int64,
       "U8": np.uint8, "BOOL": np.bool_}


def load_safetensors(path: str) -> dict[str, np.ndarray]:
    """Read every tensor of a .safetensors file as a float32 numpy array."""
    with open(path, "rb") as fh:
        n = struct.unpack("<Q", fh.read(8))[0]
        header = json.loads(fh.read(n))
        base = 8 + n
        out = {}
        for name, meta in header.items():
            if name == "__metadata__":
                continue
            b, e = meta["data_offsets"]
            fh.seek(base + b)
            buf = fh.read(e - b)
            dt = meta["dtype"]
            if dt == "BF16":
                u = np.frombuffer(buf, dtype=np.uint16).astype(np.uint32) << 16
                arr = u.view(np.float32)
            else:
                arr = np.frombuffer(buf, dtype=_DT[dt])
            arr = arr.reshape(meta["shape"]) if meta["shape"] else arr.reshape(())
            out[name] = arr.astype(np.float32) if arr.dtype.kind == "f" else arr
    return out


def save_safetensors(path: str, tensors: dict[str, np.ndarray]) -> None:
    """Write float32 tensors as .safetensors (used by the tests' tiny models)."""
    header, chunks, off = {}, [], 0
    for k, v in tensors.items():
        b = np.ascontiguousarray(v, dtype=np.float32).tobytes()
        header[k] = {"dtype": "F32", "shape": list(v.shape), "data_offsets": [off, off + len(b)]}
        chunks.append(b)
        off += len(b)
    h = json.dumps(header).encode()
    with open(path, "wb") as fh:
        fh.write(struct.pack("<Q", len(h)))
        fh.write(h)
        for c in chunks:
            fh.write(c)


# ---------------------------------------------------------------- tokenizer

_PAT = regex.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")


def _bytes_to_unicode() -> dict[int, str]:
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, map(chr, cs)))


class BPE:
    """Byte-level BPE as GPT-2 and Pythia use it (same pre-tokenizer pattern)."""

    def __init__(self, vocab: dict[str, int], merges: list[tuple[str, str]]):
        self.encoder = vocab
        self.decoder = {v: k for k, v in vocab.items()}
        self.ranks = {m: i for i, m in enumerate(merges)}
        self.b2u = _bytes_to_unicode()
        self.u2b = {v: k for k, v in self.b2u.items()}
        self.cache: dict[str, list[str]] = {}

    @classmethod
    def from_gpt2_files(cls, vocab_json: str, merges_txt: str) -> "BPE":
        vocab = json.load(open(vocab_json, encoding="utf-8"))
        lines = open(merges_txt, encoding="utf-8").read().split("\n")
        merges = [tuple(l.split()) for l in lines[1:] if l and not l.startswith("#version")]
        return cls(vocab, merges)

    @classmethod
    def from_tokenizer_json(cls, path: str) -> "BPE":
        tj = json.load(open(path, encoding="utf-8"))
        m = tj["model"]
        merges = [tuple(x.split(" ")) if isinstance(x, str) else tuple(x) for x in m["merges"]]
        vocab = dict(m["vocab"])
        for t in tj.get("added_tokens", []):
            vocab.setdefault(t["content"], t["id"])
        return cls(vocab, merges)

    def _bpe(self, token: str) -> list[str]:
        if token in self.cache:
            return self.cache[token]
        word = list(token)
        while len(word) > 1:
            pairs = [(self.ranks.get((a, b), 1 << 30), i) for i, (a, b) in enumerate(zip(word, word[1:]))]
            r, i = min(pairs)
            if r == 1 << 30:
                break
            a, b = word[i], word[i + 1]
            new, j = [], 0
            while j < len(word):
                if j < len(word) - 1 and word[j] == a and word[j + 1] == b:
                    new.append(a + b)
                    j += 2
                else:
                    new.append(word[j])
                    j += 1
            word = new
        self.cache[token] = word
        return word

    def encode(self, text: str) -> list[int]:
        ids = []
        for piece in _PAT.findall(text):
            u = "".join(self.b2u[b] for b in piece.encode("utf-8"))
            ids.extend(self.encoder[t] for t in self._bpe(u))
        return ids

    def decode(self, ids) -> str:
        s = "".join(self.decoder[int(i)] for i in ids)
        return bytearray(self.u2b[c] for c in s).decode("utf-8", errors="replace")


# ---------------------------------------------------------------- models

def _ln(x, w, b, eps):
    mu = x.mean(-1, keepdims=True)
    var = ((x - mu) ** 2).mean(-1, keepdims=True)
    return (x - mu) / np.sqrt(var + eps) * w + b


def _gelu_tanh(x):
    return 0.5 * x * (1.0 + np.tanh(0.7978845608028654 * (x + 0.044715 * x ** 3)))


def _gelu_erf(x):
    from scipy.special import erf
    return 0.5 * x * (1.0 + erf(x / np.sqrt(2.0)))


def _softmax(x, axis=-1):
    x = x - x.max(axis, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis, keepdims=True)


def _causal_attn(q, k, v):
    # q, k, v: (B, H, T, Dh)
    T = q.shape[2]
    s = q @ k.transpose(0, 1, 3, 2) / np.sqrt(q.shape[-1])
    mask = np.triu(np.ones((T, T), dtype=bool), 1)
    s = np.where(mask, -1e30, s)
    return _softmax(s) @ v


@dataclass
class LM:
    """f(x) = final layer-norm output; logits = f(x) @ g.T (+ no bias in either family)."""
    kind: str
    w: dict
    cfg: dict

    @property
    def g(self) -> np.ndarray:
        return self.w["wte.weight"] if self.kind == "gpt2" else self.w["embed_out.weight"]

    @property
    def d(self) -> int:
        return self.g.shape[1]

    def ln_f(self):
        if self.kind == "gpt2":
            return self.w["ln_f.weight"], self.w["ln_f.bias"]
        return self.w["gpt_neox.final_layer_norm.weight"], self.w["gpt_neox.final_layer_norm.bias"]

    def hidden(self, ids: np.ndarray) -> np.ndarray:
        """ids: (B, T) int. Returns f: (B, T, d) float32."""
        ids = np.asarray(ids)
        if ids.ndim == 1:
            ids = ids[None]
        return self._gpt2(ids) if self.kind == "gpt2" else self._neox(ids)

    def logits(self, f: np.ndarray) -> np.ndarray:
        return f @ self.g.T

    def _gpt2(self, ids):
        w, c = self.w, self.cfg
        B, T = ids.shape
        H = c["n_head"]
        d = w["wte.weight"].shape[1]
        eps = c.get("layer_norm_epsilon", 1e-5)
        x = w["wte.weight"][ids] + w["wpe.weight"][np.arange(T)][None]
        for i in range(c["n_layer"]):
            p = f"h.{i}."
            h = _ln(x, w[p + "ln_1.weight"], w[p + "ln_1.bias"], eps)
            qkv = h @ w[p + "attn.c_attn.weight"] + w[p + "attn.c_attn.bias"]
            q, k, v = np.split(qkv, 3, axis=-1)
            sh = lambda t: t.reshape(B, T, H, d // H).transpose(0, 2, 1, 3)
            a = _causal_attn(sh(q), sh(k), sh(v)).transpose(0, 2, 1, 3).reshape(B, T, d)
            x = x + a @ w[p + "attn.c_proj.weight"] + w[p + "attn.c_proj.bias"]
            h = _ln(x, w[p + "ln_2.weight"], w[p + "ln_2.bias"], eps)
            m = _gelu_tanh(h @ w[p + "mlp.c_fc.weight"] + w[p + "mlp.c_fc.bias"])
            x = x + m @ w[p + "mlp.c_proj.weight"] + w[p + "mlp.c_proj.bias"]
        return _ln(x, w["ln_f.weight"], w["ln_f.bias"], eps).astype(np.float32)

    def _neox(self, ids):
        w, c = self.w, self.cfg
        B, T = ids.shape
        H = c["num_attention_heads"]
        d = c["hidden_size"]
        dh = d // H
        rot = int(dh * c.get("rotary_pct", 1.0))
        eps = c.get("layer_norm_eps", 1e-5)
        inv = 1.0 / (c.get("rotary_emb_base", 10000) ** (np.arange(0, rot, 2) / rot))
        fr = np.outer(np.arange(T), inv)
        emb = np.concatenate([fr, fr], -1)
        cos, sin = np.cos(emb)[None, None], np.sin(emb)[None, None]

        def rope(t):
            tr, tp = t[..., :rot], t[..., rot:]
            x1, x2 = tr[..., : rot // 2], tr[..., rot // 2:]
            rh = np.concatenate([-x2, x1], -1)
            return np.concatenate([tr * cos + rh * sin, tp], -1)

        x = w["gpt_neox.embed_in.weight"][ids]
        for i in range(c["num_hidden_layers"]):
            p = f"gpt_neox.layers.{i}."
            h1 = _ln(x, w[p + "input_layernorm.weight"], w[p + "input_layernorm.bias"], eps)
            qkv = h1 @ w[p + "attention.query_key_value.weight"].T + w[p + "attention.query_key_value.bias"]
            qkv = qkv.reshape(B, T, H, 3 * dh).transpose(0, 2, 1, 3)
            q, k, v = qkv[..., :dh], qkv[..., dh:2 * dh], qkv[..., 2 * dh:]
            a = _causal_attn(rope(q), rope(k), v).transpose(0, 2, 1, 3).reshape(B, T, d)
            a = a @ w[p + "attention.dense.weight"].T + w[p + "attention.dense.bias"]
            h2 = _ln(x, w[p + "post_attention_layernorm.weight"], w[p + "post_attention_layernorm.bias"], eps)
            m = _gelu_erf(h2 @ w[p + "mlp.dense_h_to_4h.weight"].T + w[p + "mlp.dense_h_to_4h.bias"])
            m = m @ w[p + "mlp.dense_4h_to_h.weight"].T + w[p + "mlp.dense_4h_to_h.bias"]
            if c.get("use_parallel_residual", True):
                x = x + a + m
            else:  # pragma: no cover - Pythia uses the parallel residual
                raise NotImplementedError
        return _ln(x, w["gpt_neox.final_layer_norm.weight"], w["gpt_neox.final_layer_norm.bias"], eps).astype(np.float32)

    def sample(self, prompts: np.ndarray, steps: int, rng: np.random.Generator) -> np.ndarray:
        """Ancestral sampling at temperature 1, full recompute each step (short sequences only)."""
        ids = np.asarray(prompts)
        for _ in range(steps):
            f = self.hidden(ids)[:, -1]
            p = _softmax(self.logits(f).astype(np.float64))
            nxt = np.array([rng.choice(p.shape[1], p=row / row.sum()) for row in p])
            ids = np.concatenate([ids, nxt[:, None]], 1)
        return ids


def load_model(directory: str) -> tuple[LM, BPE]:
    cfg = json.load(open(f"{directory}/config.json"))
    w = load_safetensors(f"{directory}/model.safetensors")
    if cfg.get("model_type") == "gpt2":
        tok = BPE.from_gpt2_files(f"{directory}/vocab.json", f"{directory}/merges.txt")
        return LM("gpt2", w, cfg), tok
    tok = BPE.from_tokenizer_json(f"{directory}/tokenizer.json")
    return LM("neox", w, cfg), tok
