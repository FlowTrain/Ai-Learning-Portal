# LemonAid — First 4 Loops: Findings (2026-07-11)

Owner's local generator/critic experiment (the S73 "LemonAid local-AI experiment"), first real runs. Raw log: `research/lemonaid-first-4-loops.md`. This is the codegen-quality experiment's *local tier* producing its first data on owned hardware.

## Setup

- **Host:** AMD Ryzen 9 PRO 8945HS w/ Radeon 780M (the air-quotes "AI chip"); eGPU RX 9060 via dock; llama.cpp (external-GPU recognition cost ~a day).
- **Model:** DeepSeek 2 MoE, Q4 quant. **16K context window.** VRAM pinned ~15.5 GB every round. Token speed: acceptable.
- **Loop:** local model generates CCQG specs (10-section template) → TIMC Light scores (EARS / Sections / BDD) → regenerate with feedback.

## The result that matters

| Loop | Composite | Verdict |
|---|---|---|
| 1 | **100** (EARS 100 · Sections 100 · BDD 100) | PASS — clears the bar cold |
| 2 | 52 | NEEDS WORK |
| 3–4+ | 33, 33, 33 | NEEDS WORK — floor |

A 4-bit local MoE **can** produce a passing CCQG spec — once, with a clean window. Quality then collapses monotonically as feedback/history accumulates in a 16K window. This is context rot at rowboat scale, measured on an owned bench with an owned scorer.

**Owner's conclusion (design requirement, verbatim intent):** *the antagonist needs a rules engine so that what lands in the context window each turn is focused, minimizing token burn.* I.e., per-turn context is a **contract, not an accumulation**: a deterministic assembler that selects (spec section under revision + relevant findings only + template fragment), never appends. The same closed-schema instinct as the composition-JSON pipeline, applied to the loop's own memory.

## What this validates (library cross-refs)

- **context-engineering, boundary conditions:** "small local models have small effective contexts regardless of advertised window; Era 1 discipline (short, curated, explicit) is mandatory" — now with first-party data. The Select verb isn't optimization at 16K; it's survival.
- **agent-orchestration:** the critic loop degrades without coordination design — the reviewer's *output* becomes the generator's poison at accumulation. Rules-engine-as-context-assembler is the missing tool contract between generator and critic.
- **token-economics:** the constraint tax and context costs bite hardest exactly where inference looks free (local = $0/token, but the *quality* budget is the scarce window).
- **evaluation-practice:** the whole finding only exists because a deterministic scorer ran every loop. No TIMC Light, no curve — just vibes about "it got worse."

## Hardware ladder (owner's options, with honest notes)

1. **Now:** 8945HS + eGPU RX 9060 — proven, 16K ceiling, one-model-at-a-time. Fine for rules-engine development (the finding needs *software*, not more VRAM).
2. **Instinct MI-class 32GB on the DEG2 dock** — the nervousness is well-founded: ~300W sustained on a desk eGPU dock is a real power-delivery/thermal question; verify dock's continuous wattage rating before the water-cooled card ever meets it. Also verify software path: official ROCm support for that GPU generation has been dropped in recent releases — the community route is llama.cpp's Vulkan backend; confirm against current llama.cpp/ROCm state before buying anything (dated claim, re-verify).
3. **Ryzen 9 5000 + 4–8× Instinct 32GB backplane** / **Threadripper Zen3 32-core, 256GB, 8× Instinct open frame** — llama.cpp does multi-GPU layer/row splitting, but MoE across many PCIe cards is bandwidth-bound, and 8×300W ≈ 2.4kW before the loop pump. Verify the Vulkan multi-GPU path on that card generation *with one card first*.
4. **Zero-capital paths, 45 days out:** HF GPU grants; Quantic compute resources. **Sequence recommendation:** the rules engine is buildable on rig #1 today; the demo rig is justified by the demo, not the research.

**The demo-rig business case is real, though:** "a full spec runs to completion, flow to finish, with the ethernet cable visibly unplugged" is a regulated-industry workshop moment money can't easily buy — data never leaves the building, provably. That's a D5 one-pager (the workflow it changes: the *sales conversation*), not a toy. Write it as one before the eBay cart wins.

## Next experiment (smallest step)

Rules-engine v0 on current hardware: per-turn context = {system + template fragment for the section under revision + top-N findings for that section only}. Re-run the 4 loops. Hypothesis: the 100→33 collapse flattens materially. That result — either way — is a Part IV data point and the antagonist's first design validation.
