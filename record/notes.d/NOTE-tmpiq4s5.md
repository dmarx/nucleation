---
status: Read
paper: LIT-tmpbmt5h
title: 'ZipNN'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (full text of arXiv v2 (4 Jun 2025, 13 pp.: §§I–VII and
    references; v2 has no appendix), plus a comparison read of arXiv v1 (7
    Nov 2024, 16 pp.), including v1's appendix listing the exact Hugging
    Face model identifiers behind Tables 1–3 and Figures 2, 4, 6, 7, 9 and
    10. Nothing skipped. Bibliography: Hershcovitch, Wood, Choshen,
    Girmonsky, Leibovitz, Ozeri, Ennmouri, Malka, Chin, Sundararaman, Harnik
    (IBM Research, IBM, Tel Aviv U., Boston U., MIT, Dartmouth). arXiv
    2411.05239, first appeared 2024-11-07 (v1). The v2 arXiv comment says
    "IEEE Cloud"; the year and proceedings details are unverified. Or Ozeri
    is an author in the v2 PDF but is missing from v1 and from arXiv's
    author metadata.). The first NOTE on this paper, which was seeded from
    its abstract alone.
date: '2026-09-27'
summary: >-
  Lossless compression of trained-model files works almost entirely
  through the float exponent. It is concentrated on about 40 of 256
  values, the top 12 hold ~99.9% of parameters, and it compresses to ~33%
  under order-0 Huffman coding, while sign and mantissa stay ≈100%. So
  "regular" BF16 models compress to ~66.4% and FP32 models to ~83%.
  Rounded "clean" models reach 33.7–48.1%, and ZipNN (exponent extraction
  plus Huffman only) beats vanilla Zstd by 17% in size and 62% in
  single-thread speed on Llama-3.1-8B BF16. The paper never computes an
  entropy and never compares its codes to one.
---

# NOTE-tmpiq4s5: ZipNN

## Contribution

The paper shows empirically that standard trained networks stored as BF16, FP32 or FP16 carry byte-level redundancy that lossless coders can remove. It locates that redundancy almost entirely in the exponent field. It builds ZipNN on this finding: separate the exponent (and, for rounded "clean" models, each fraction byte) into its own stream and code each stream with Huffman alone, dropping the LZ stage. The result is smaller and faster than Zstd. It also measures lossless compressibility of gradients, optimizer state and XOR checkpoint deltas.

## Key insight

The float encoding spends 8 exponent bits on a dynamic range trained weights never use. The weights sit in a narrow magnitude band, so the exponent symbol has a sharply peaked distribution that is nearly the same across models (Fig. 2). Mantissa and sign bits look random. Neighbouring parameters are unrelated, so the whole gain is order-0 (single-symbol) entropy coding of the exponent. Multi-byte repetition search (LZ) finds nothing real: a random shuffle of the parameters changes Zstd's exponent compression by at most 0.05% (§III-A b). The redundancy belongs to the number format, not to the learned function.

## Assumptions

- Models are "long arrays of numeric parameters". Code and metadata are negligible, and the first 10 MB (headers) are excluded in Table II (§II-B, Table II caption).
- Large models are measured on 1 GB taken "from the middle of the model", not the whole file (Fig. 2, Table II, Table III). Whole-model compressibility is extrapolated from this sample.
- The split into "regular" and "clean" models is empirical. Clean means rounded or type-converted after training, and it is detected at run time chunk by chunk (§III, §III-B b). No criterion beyond the measured compressibility is given.
- Compression ratio is reported as "compressed size in percent", lower is better (§II-C). The "17% better" and "34% improvement" figures are relative differences between two such percentages.
- Speed results come from a single thread on an Apple M1 Max. The multi-thread results come from 2× Intel Xeon Platinum 8480+ (224 cores, 2 TB DRAM) (§V-B, §V-C).

## Key results

- **Exponent distribution (Fig. 2; §III-A).** On Llama 3.1 BF16, Granite 7B BF16, Qwen BF16 and ResNet-50 FP32 (1 GB sample each), about 40 of the 256 exponent values occur (50 for ResNet). The top 12 values cover "almost 99.9%" of parameters (17 values for ResNet). The histograms are "strikingly similar" across models and dtypes, with support inside biased exponent ≈80–140.
- **Per-field compressibility (§III-A, Table II).** The exponent compresses to about 33% ("approximately a 3X factor"). Sign and fraction bytes compress to ≈100% on regular models. Hence BF16 ≈ ½·33.3 + ½·100 ≈ 66.6% and FP32 ≈ ¼·33.3 + ¾·100 ≈ 83.3%.
- **Table II (ZipNN with byte grouping; compressed size, then per byte group).**
  - Regular BF16:
    - Falcon-7B 66.4% (32.8, 100)
    - BLOOM 328.2 GB 67.4% (34.8, 100)
    - OpenLLaMA-3B 66.4% (32.7, 100)
    - Mistral 66.3% (32.5, 100)
    - Llama-3.1 (8B, 16 GB) 66.4% (32.8, 99.9)
  - Regular FP32:
    - wav2vec 83.3% (33.0, 100, 100, 100)
    - BERT 83.0% (32.6, 99.5, 100, 100)
    - OLMo 83.1% (32.5, 100, 100, 100)
  - FP16:
    - Stable-Video-Diffusion 84.8% (69.6, 100)
    - CapybaraHermes-Mistral 84.4% (68.8, 100)
  - Clean FP32:
    - xlm-RoBERTa 41.8% (33.9, 95.6, 37.5, 0.0)
    - CLIP 48.1% (33.1, 100, 45.9, 13.4)
    - T5-base 33.7% (34.6, 100, 0.0, 0.0)
  - Clean FP16, "likely" converted from BF16:
    - Llama2-13B 66.6% (64.2, 69.0)
    - Tulu-7B 66.6% (64.2, 68.9)
- **Ablation (Fig. 4).** Compressed size for Zstd vanilla / Huffman vanilla / Zstd with exponent extraction / Huffman with exponent extraction:
  - Llama 3.1 BF16: 77.6 / 77.7 / 68.8 / 66.4%
  - Granite BF16: 78.2 / 78.3 / 68.7 / 66.3%
  - OLMo FP32: 92.7 / 92.8 / 84.3 / 83.1%

  So Huffman beats Zstd on ratio only after the exponent is extracted. An FSE (tANS) entropy coder is "slightly better" (0–2%) and at times more than 2× slower (§III-A b).
- **Speed, single thread (Table III; 10 runs on 1 GB, max s.d. 2%).** Each row gives compressed size, compression speed, decompression speed.
  - Llama-3.1 BF16:
    - Zstd 77.7%, 0.71 GB/s, 1.02 GB/s
    - EE+Zstd 68.8%, 0.51, 1.21
    - ZipNN 66.4%, 1.15, 1.65
  - OLMo-1B FP32:
    - Zstd 92.3%, 0.97, 1.02
    - EE+Zstd 84.4%, 0.82, 1.97
    - ZipNN 83.2%, 1.64, 2.48
  - xlm-RoBERTa FP32 (clean):
    - Zstd 57.4%, 0.18, 0.77
    - EE+Zstd 46.7%, 0.42, 0.89
    - ZipNN 42.9%, 0.83, 1.41

  These give the headline figures: (77.7−66.4)/66.4 ≈ 17%, and speedups 1.15/0.71 ≈ 1.62 and 1.65/1.02 ≈ 1.62. On the clean model: ≈34% smaller, 4.6× faster compression, 83% faster decompression. LZ4 and Snappy achieve zero savings on these models.
- **Multi-threading (Fig. 10; §V-C).**
  - A single worker decompressing 10 GB exceeds 45 GB/s. Compression throughput peaks at around 16 threads.
  - With 16 workers × 7 threads on Llama 3.1 and blocks as small as 100 MB per worker: up to 80 GB/s decompression and up to 13 GB/s compression.
- **Training artifacts (§IV-A; Fig. 7).** RoBERTa BF16 under fine-tuning compresses to:
  - model 66.90%
  - gradients 47.43%
  - optimizer state 54.87%

  The gain sits in the token-embedding layer: gradient 0.36%, optimizer 29.56%, both coded with Zstd. The encoder layers compress to 68.84% (gradient) and 66.14% (optimizer).
- **Deltas (§IV-B; Figs. 8–9).**
  - ResNet-18 FP32 fine-tuning: all parameters change every epoch, but the fraction of unchanged bytes rises as training converges, stepping with the LR schedule. The exponent byte changes least.
  - Auto-selection rule: Zstd over Huffman if more than 90% of the chunk is zero bytes, or if any zero run exceeds 3% of the chunk.
  - Periodic bases every 5 or 10 checkpoints remain far better than standalone compression for ResNet, Amber (BF16) and OLMo (FP32).
  - Three RoBERTa-tweet fine-tunes: 83.7% standalone on average, 56% for pairwise deltas.
- **Hub and serving (Table I; §V-D).**
  - Table I, compressed size of top Hugging Face downloads, Oct 2024 ranks: Bge 42.1%, Mpnet 82.9%, Bert 83.9%, Qwen 66.9%, Whisper 42.7%, xlm-RoBERTa 42.3%, Clip 49.7%, Llama 3.1 (405B, 812 GB) 67.2%.
  - Serving test: vLLM 0.7.2 with 4 workers loading Granite-3.1-8b-instruct BF16 (16 GB, compressed to ⅔) took about 3 s, "on par" with the uncompressed model.
- **Quantized and other formats (§VI).** Some GPTQ and AWQ checkpoints compress to 85–91%. GGUF models "do not compress at all". ZFP 1.3.0 on FP32 is comparable to Zstd and worse than ZipNN.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In trained weights the exponent carries nearly all of the lossless-removable redundancy; sign and mantissa are near-incompressible (regular models) | strong (empirical) | Table II per-group breakdown over 15 models; Fig. 4 |
| C2 | The exponent distribution is highly skewed (~40 of 256 values; top 12 ≈ 99.9%) and similar across models and dtypes | moderate | Fig. 2, four models, 1 GB samples only |
| C3 | The exponent's compressibility is entirely order-0 (single-byte) skew; there is no inter-parameter structure for LZ to exploit | moderate | parameter-shuffle experiment, ≤0.05% change (§III-A b), one compressor; LZ4 and Snappy give 0% |
| C4 | The skew arises because weights start in [−1,1] and rarely leave it, and are floored by Adam's ε "noise" at ~2⁻²³ | weak (assertion) | §III-A prose only, with no measurement; see Limitations for the errors it contains |
| C5 | Exponent extraction with Huffman-only coding beats Zstd in both ratio and speed (17% smaller, 62% faster on Llama-3.1-8B BF16) | strong (empirical) | Table III, 10 runs, s.d. ≤ 2%, single machine |
| C6 | Decompression reaches up to 80 GB/s and compression up to 13 GB/s | moderate | Fig. 10(c), one cluster configuration, Llama only |
| C7 | Gradients and optimizer state compress better than weights, driven by the embedding layer | moderate | one BF16 RoBERTa fine-tuning run (Fig. 7) |
| C8 | Fewer bytes change per epoch as training converges, so delta compression improves | moderate | ResNet-18 run plus public Amber and OLMo checkpoints (Figs. 8–9) |
| C9 | The method could save "over an ExaByte per year" of Hugging Face traffic (abstract) | weak (assertion) | not derived anywhere in the body. The only input is Hugging Face's stated ~6 PB/day (§II-A1), about 2.2 EB/yr raw, so the claim needs average savings above ~45%, well above the ~33% BF16 figure. v1's abstract said "per month", which that same input rules out |
| C10 | The redundancy shows that "overparametrization is not fully used … and there is redundancy" (§VII) | weak (assertion) | not supported by what was measured. The measured redundancy is in the float format's exponent range, not in the parameters' functional content |

## Method

1. **Exponent extraction.** Regroup each parameter's bits so all exponents form one stream (Fig. 3, BF16).
2. **Byte grouping.** For FP32 (and FP16), split the remaining bytes into separate streams, one per byte position (Fig. 5).
3. **Coding.** Code each stream with Zstd's Huffman implementation alone, with no LZ stage. All-zero streams are truncated to a header.
4. **Skip incompressible data.** If a chunk is incompressible, skip the next few chunks before trying again (§III-B b).
5. **Chunking.** Chunks are 256 KB, so byte groups are 128 KB (BF16) or 64 KB (FP32). A metadata map records variable-size compressed chunks so they can be decompressed in parallel.
6. **Deltas.** XOR against a base, then auto-select Huffman or Zstd per byte group using the zero-fraction and zero-run rules above.

Implementation: about 2,000 lines of C and 4,000 of Python, on Zstd 1.5.6, with a Hugging Face Transformers integration (§V-A).

## Concepts

- **Regular model.** Trained and not modified afterwards. Only the exponent is compressible.
- **Clean model.** Rounded or type-converted after training, which leaves zero or low-entropy low-order fraction bytes. Clean models lose the extra compressibility once fine-tuned again (§III).
- **Exponent extraction (EE).** The bit rearrangement that isolates the exponent field into its own stream.
- **Byte grouping (BG).** One compression stream per byte position of the parameter.
- **Compressed size (%).** Output size over input size. Lower is better.

## Connections

- Its lineage is floating-point compression: exponent/mantissa separation in scientific-data coders (refs [58, 59]), dietgpu's exponent-only ANS variant (ref [60]), which the paper says matches ZipNN on regular models but not on clean models, deltas, gradients or optimizers, and ZFP.
- It positions itself against lossy model compression: pruning, distillation, and quantization such as [ANTH-LIT-081](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-081.md) (GPTQ) and [ANTH-LIT-585](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-585.md) (AWQ), whose checkpoints it finds still partly compressible at 85–91%. It cites [ANTH-LIT-378](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-378.md) (QLoRA) as quantization applied to deltas.
- It motivates the work with distributed and decentralized training, citing [ANTH-LIT-083](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-083.md) (FSDP), [ANTH-LIT-104](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-104.md) (ReLoRA) and [ANTH-LIT-316](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-316.md) (open collaborations).
- It uses models or formats from [ANTH-LIT-179](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-179.md) (Llama 3), [ANTH-LIT-671](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-671.md) (RoBERTa), [ANTH-LIT-189](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-189.md) (Switch Transformers, as the "terabytes" example) and [ANTH-LIT-022](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-022.md) (Megatron-LM).
- Its account of why the exponent is skewed invokes Adam's ε ([ANTH-LIT-001](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-001.md)) without measuring it.

**Information-theoretic connections, which the text supports only thinly.**

- **What the paper measures.** It uses "entropy" informally, as the order-0 byte entropy that Huffman exploits (§II-C, §III-A). It never computes the empirical entropy of the exponent, or of any stream, and never reports Huffman's gap to it. The closest it comes is the FSE comparison: FSE is 0–2% better, and FSE (tANS) approaches the order-0 entropy more closely than Huffman, whose redundancy is less than 1 bit per symbol.
- **What that implies, as this reader's inference and not the paper's.** ~33% of 8 bits is ≈2.6 bits per exponent, and Huffman satisfies H ≤ L < H+1. So the order-0 exponent entropy is roughly 1.6–2.6 bits, which is well below log₂40 ≈ 5.3. With the mantissa near-incompressible, a regular BF16 weight costs about 10.6 of 16 bits under order-0 per-field coding.
- **Grünwald & Vitányi ([LIT-224](../literature.d/LIT-224.md)).** They separate Shannon entropy, a property of a distribution, from Kolmogorov complexity, a property of an individual string. ZipNN's figures are empirical compression ratios for particular files under a particular order-0 coder. They are upper bounds on the files' description length, not estimates of a source entropy or of K(x). Nothing in the paper speaks to how close either is.
- **MDL works ([LIT-225](../literature.d/LIT-225.md), [LIT-238](../literature.d/LIT-238.md); also [LIT-229](../literature.d/LIT-229.md) and [LIT-239](../literature.d/LIT-239.md) on meaningful information and structure functions).** In these, the model's description length is the code length of the hypothesis at a precision chosen jointly with the data's code length. ZipNN compresses a fixed-precision serialization losslessly, down to every mantissa bit. It therefore measures the cost of the format at a precision nobody chose for statistical reasons, not the two-part code length of the learned hypothesis.
- **Compressibility-based generalization bounds by Sefidgaran et al. ([LIT-233](../literature.d/LIT-233.md), [LIT-236](../literature.d/LIT-236.md)).** Their compressibility is lossy or rate-distortion compressibility of the learning algorithm's output, relative to its effect on the loss. Lossless coding of the float representation does not bear on those quantities: it compresses the representation of the numbers, not the function. The mantissa, which carries the fine-grained values, is exactly the part that proved incompressible. The paper makes no such connection. Its §VII remark about "redundancy" from overparametrization (C10) runs this distinction together.
- **Contrast in the anthology.** [ANTH-LIT-440](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-440.md) ("How much do language models memorize?") measures information capacity in bits per parameter. That is the kind of functional information-content measure ZipNN's numbers are not. This reading does not assert a quantitative relation between the two.

## Bearing on the record

- **For nucleation.** A small, clean empirical datum for information-theory reading: the order-0 redundancy of the IEEE and bfloat16 encoding of trained weights sits in the exponent (roughly 1.6–2.6 bits of entropy in an 8-bit field, by this reader's inference). The explanation for why is not established. It does not support any claim about the Kolmogorov complexity, MDL code length or generalization-relevant compressibility of trained networks. Any record document that cited it for "trained weights have low information content" would be citing it for something it does not show.
- **For ML practice, the chief home.** It carries directly usable practice for the Anthology of the SOTA:
  - Serve and store BF16 checkpoints losslessly compressed, for a ~⅓ reduction.
  - Split fields and use entropy-only coding rather than general-purpose LZ+entropy compressors.
  - Delta-compress checkpoints against periodic bases.

  If filed there, it would sit near [ANTH-LIT-081](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-081.md), [ANTH-LIT-585](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-585.md), [ANTH-LIT-197](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-197.md) (microscaling formats) and [ANTH-LIT-186](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-186.md) (precision scaling laws). Hence `home: anthology`.

## Limitations

- **No entropy is ever measured.** The title question for an information-theoretic reader is how close the coding gets to the entropy. The paper answers it only indirectly, through the FSE-vs-Huffman comparison (0–2%).
- **The skew explanation is observation plus conjecture, and parts of it are wrong as stated** (§III-A).
  - Adam's ε sits in the update's denominator; it does not add noise to the weights.
  - 2⁻²³ corresponds to biased exponent 104, not "around 99". The usual ε = 1e-8 ≈ 2⁻²⁶·⁶ is ≈100.
  - |w| < 1 corresponds to biased exponent ≤ 126, not "do not tend to exceed 128".
  - That weights are "initially set in the space of [−1,+1]" is asserted, not measured.
  - The authors concede the point: "No matter the reason that the exponent is skewed…".
- **Sampling.** Large-model results come from a 1 GB middle slice. Fig. 2 uses four models. Speeds come from one machine per setting.
- **Figure and table disagree slightly.**
  - Llama Zstd: 77.6% (Fig. 4) vs 77.7% (Table III).
  - OLMo Zstd: 92.7% vs 92.3%.
  - OLMo EE+Zstd: 84.3% vs 84.4%.
  - OLMo Huffman+EE: 83.1% vs 83.2%.
- **The "clean" category is defined after the fact** by observed compressibility. The FP16 "clean" cases are explained only as "likely" BF16 conversions.
- **Training-artifact results each rest on one run:** a single RoBERTa fine-tune and a single ResNet-18 fine-tune. The embedding-layer effect is reported without a mechanism.
- **The ExaByte claim.** It is unargued (C9), and it changed from "per month" (v1) to "per year" (v2) without comment.
- **Overreach in the conclusion (C10).** It moves from format redundancy to the use of overparametrization.

## Open questions

- What are the order-0 and conditional (context-modelled) entropies of the exponent and mantissa streams? Does any context, for example per-tensor scale or neighbouring exponents, push below the Huffman figure? A measured entropy table per model would settle it.
- Is the exponent skew set by initialization scale, weight decay, normalization, or optimizer ε? A controlled training sweep with the exponent histogram tracked over training would test the §III-A conjecture.
- How does lossless float-level compressibility relate to lossy compressibility at fixed loss? The latter is the quantity in [LIT-233](../literature.d/LIT-233.md) and [LIT-236](../literature.d/LIT-236.md), and in functional capacity measures such as [ANTH-LIT-440](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-440.md). The paper gives no data on this.
