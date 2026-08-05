Experimental Framework for Evaluating LLM Code Convergence and Specification Adherence via Quality Guardian Orchestration
=========================================================================================================================

The Evolution of Agentic Engineering and Specification Paradigms
----------------------------------------------------------------

The landscape of software engineering is undergoing a foundational
transformation, transitioning from human-driven syntax generation
augmented by rudimentary autocomplete tools to fully autonomous,
multi-agent software factories. In this emerging paradigm, large
language models interact within complex orchestration frameworks to
design, implement, test, and deploy code with minimal human
intervention. The central challenge in this agentic era is no longer
evaluating whether a model can generate functionally correct syntax, but
rather determining its capacity to rigorously adhere to predefined
architectural rules, security protocols, and stylistic mandates over
extended conversational horizons. This adherence is universally governed
by a central specification file, commonly denoted as AGENT.md,
CLAUDE.md, or spec.md, which serves as the definitive constitutional
rulebook for the artificial intelligence agent\'s operational
parameters.^1^

The primary objective of advanced agentic experimentation is to
determine whether disparate language models---ranging from highly
optimized, locally hosted open-weights models to massive, cloud-based
frontier architectures---can produce comparable, uniform code when
subjected to an identical AGENT.md specification and evaluated by an
adversarial verification system. Historical empirical evidence
demonstrates that maintaining strict adherence to these specification
files across multi-turn interactions remains a persistent vulnerability
for both proprietary and open-weight models.^3.^ Models frequently
suffer from context degradation, semantic drift, and an inherent
structural bias toward functional expediency. They tend to prioritize
immediate execution over architectural constraints, often inventing
unauthorized abstractions or bypassing centralized state managers to
achieve a rapid solution.^4^

To counteract this degradation, modern AI-driven software architectures
have introduced the concept of the Quality Guardian. The Quality
Guardian is a specialized, read-only AI agent whose sole responsibility
is to audit the primary code generator against the central
specification.^7.^ By establishing a workflow in which the Quality
Guardian continuously checks the primary generative agent (the
Implementer), researchers can force convergence of outputs. The core
hypothesis of this experimental framework posits that by utilizing an
AI-agnostic orchestration platform, deploying an identical AGENT.md
file, and enforcing strict Quality Guardian oversight, the inherent
variations between models such as Gemini, OpenAI's Codex, Anthropic's
Claude, and locally hosted variants like Qwen 3.5 can be normalized,
resulting in highly comparable, specification-compliant codebase
implementations.

Hardware Architecture and the Economics of Local Deployment
-----------------------------------------------------------

Executing advanced large language models in localized environments
requires a deep understanding of hardware constraints, memory bandwidth
limitations, and the underlying software stack that accelerates
inference. The experimental infrastructure relies on a highly specific,
consumer-grade hybrid architecture: an AMD Ryzen 9 AI laptop processor
paired with an external or discrete AMD Radeon RX 9060 XT graphics
processing unit featuring 16GB of VRAM, supported by 32GB of unified
system RAM.^9^ Operating complex multi-agent workflows within these
specific parameters necessitates precise optimization techniques to
maximize computational throughput while maintaining the extensive
context windows required for autonomous coding loops.^9^

The 32GB system RAM constraint poses a significant logistical bottleneck
for deploying large-parameter reasoning models. In an ideal,
unconstrained environment, operating massive models requires
substantially higher memory capacities---such as dual 48GB memory
modules totaling 96GB of RAM---to accommodate the weights and the
expansive Key-Value (KV) cache without relying heavily on paging or
storage swapping. However, the economic realities of hardware
procurement often necessitate compromises. The 32GB configuration, while
limiting, provides an excellent testbed for evaluating the resilience of
memory-constrained inference engines and layer-splitting techniques.^11^

### The AMD ROCm Software Ecosystem

To effectively harness the computational capabilities of the AMD Radeon
RX 9060 XT, the experimental pipeline relies heavily on the ROCm (Radeon
Open Compute) software stack. The release of ROCm 7.2.1 marks a critical
milestone in democratizing local artificial intelligence development,
introducing robust, native PyTorch support for the Radeon 9000 Series
(based on the RDNA 4 architecture) on both Linux and Windows.^10^
Historically, developers utilizing AMD hardware faced severe
complexities regarding compatibility layers, customized kernel
compilations, and the necessity of dual-boot Linux configurations to
achieve reasonable inference speeds. However, the introduction of the
PyTorch Windows Preview Edition 25.20.01.14 driver enables seamless
execution of AI workloads directly on the host operating system,
eliminating the need for complex workarounds.^10^

For environments requiring maximum flexibility and memory optimization,
inference engines such as llama.cpp and vLLM have been extensively
optimized for ROCm architectures. The vLLM framework, recognized
industry-wide for its high-throughput inference capabilities and
efficient memory utilization via PagedAttention algorithms, provides an
ideal backend for serving models locally on the Radeon GPU.^14^ The
PagedAttention mechanism fundamentally alters how language models manage
memory; it mitigates the need to allocate large, contiguous memory
blocks for the attention KV cache. Instead, it partitions the cache into
smaller, dynamically managed pages, significantly reducing memory
fragmentation and allowing the hardware to support larger batch sizes or
extended context windows.^15^ This is a critical requirement when
feeding comprehensive AGENT.md files, extensive conversational
histories, and large codebase repositories into the model. Furthermore,
wrapper frameworks like ZLUDA offer experimental pathways to bypass
unsupported hardware blocks by executing natively compiled CUDA binaries
via ROCm translation layers, ensuring that AMD hardware remains broadly
compatible with the rapidly expanding ecosystem of AI agent
orchestration tooling.^16^

### Memory Architecture Constraints: VRAM and System RAM Dynamics

The primary constraint dictating model selection and performance in
local deployments is memory capacity, specifically the Video Random
Access Memory (VRAM). A graphics card with 16GB of VRAM sets a
definitive upper limit on the size of the model that can be fully
offloaded to the GPU to achieve uncompromised, maximum-speed
inference.^9^ Code generation models are uniquely sensitive to memory
constraints because agentic loops inherently rely on massive context
histories. Storing the system prompt, the intricate specification file,
the existing codebase files, and the iterative conversational history
requires a substantial and ever-growing KV cache footprint.

The 16GB VRAM limitation forces a strategic approach to model
quantization and hardware allocation:

Models operating in the 7-billion to 14-billion parameter range can
typically be fully offloaded to the 16GB VRAM buffer when quantized
using Q4\_K\_M or Q5 methods.^9^ Fully offloading the model ensures
maximum tokens-per-second throughput, preventing the severe latency
penalties inherent in transferring tensor data back and forth across the
PCIe bus between the GPU and the system RAM. Conversely, large-parameter
models, such as the Qwen 3.5 Coder 32B, pose a significant deployment
challenge. At a 4-bit quantization (e.g., Q4\_K\_M), the model weights
alone demand approximately 18GB to 20GB of memory, instantly exceeding
the total capacity of the RX 9060 XT.^11^ Consequently, the inference
engine must aggressively split the model layers, offloading the maximum
allowable number of layers to the GPU VRAM while allocating the
remainder to the 32GB of system RAM.^12^

Running models that exceed VRAM capacity requires relying on system RAM,
which operates at a significantly lower bandwidth than the GDDR6 video
memory on the discrete GPU. While the architecture of the AMD Ryzen 9 AI
processor facilitates highly efficient data management and memory
addressing, layer-splitting invariably results in a noticeable reduction
of inference speed. To mitigate this latency during prolonged agentic
coding loops, advanced prompt caching and speculative decoding
techniques must be implemented at the inference engine level.^9^ Prompt
caching allows the engine to retain the computed attention states of
static input segments---such as the invariant AGENT.md file and
foundational system prompts---across multiple generation turns. This
drastically reduces the time to first token (TTFT) while preserving
critical computational resources, making layer-split 32B models viable
on consumer hardware.^19^

Platform Agnosticism and Middleware API Standardization
-------------------------------------------------------

To ensure a scientifically valid comparison between locally hosted
models executing on AMD hardware and proprietary cloud-based models
running on hyperscale data centers, the integration layer must be
strictly standardized. The experiment requires a platform-agnostic
approach in which the orchestrating agent framework interacts with all
models via a uniform, interchangeable protocol.^8^ The orchestrating
software must not possess any awareness of whether the underlying
reasoning engine is a local Qwen 3.5 instance or a cloud-based Gemini
3.1 Pro API.

The Lemonade Server provides an optimal middleware solution for
achieving uniformity across AMD hardware environments. Designed as a
turnkey local LLM serving utility, Lemonade exposes standard,
OpenAI-compatible REST API endpoints (e.g., /v1/chat/completions) while
seamlessly abstracting the complex underlying hardware acceleration
paths.^20^ It natively supports hardware-specific ROCm builds of
llama.cpp and can dynamically route inference tasks between the Radeon
RX 9060 XT GPU and the Ryzen AI NPU using Vulkan or OnnxRuntime
APIs.^20^

By establishing this standardized OpenAI-compatible endpoint for the
local models, the experimental pipeline guarantees that the input
structure, the injection of the AGENT.md system prompts, the tool-call
parsers, and the formatting rules remain perfectly identical across all
tested models.^14^ When the orchestration agent submits a request to
generate a specific software feature based on the specification, the
same JSON payload is transmitted regardless of the model destination.
This absolute standardization isolates the variable of model capability,
allowing the experiment to measure how different architectures process
the identical ruleset accurately.

The Quality Guardian: Adversarial Orchestration and Pipeline Enforcement
------------------------------------------------------------------------

The core mechanism for testing and enforcing LLM adherence in this
experiment relies on a multi-agent orchestration architecture.
Traditional, single-agent code generation suffers from a critical,
documented flaw: LLMs are structurally biased toward autocomplete
behaviors and probability maximization, leading them to prioritize the
immediate production of functional syntax while gradually ignoring
systemic constraints outlined in peripheral context files.^22^ To
enforce rigorous specification adherence, modern software factories
deploy independent, adversarial agent roles operating in isolated
sequences.^7^

### Separation of Concerns in Agentic Workflows

The experimental design utilizes two distinct, specialized agent
profiles to evaluate the coding task: the Implementer and the Quality
Guardian.^23^

The Implementer is tasked with synthesizing code based on user requests,
interpreting the AGENT. and utilizing designated tools to write, modify,
and execute files within the workspace.^8^ The Implementer acts as the
primary creative engine of the pipeline, focusing on functionality,
algorithmic logic, and rapid task completion. However, its expansive
write permissions and generative focus make it highly susceptible to
architectural drift. In complex tasks, the Implementer may implement
\"quick fixes\" that violate overarching project patterns---such as
bypassing a centralized state management protocol in favor of a local
variable or ignoring error-handling requirements to pass a unit test
more quickly.^4^

The Quality Guardian, conversely, operates under strict, read-only
permissions.^24^ It possesses no capability to write or modify code
directly. Its singular mandate is to audit the artifacts produced by the
Implementer against the AGENT.md specification and universally accepted
security and structural paradigms.^25^ The Guardian analyzes uncommitted
changes in the repository, aggressively scanning for syntactic errors,
semantic drift, security vulnerabilities (such as hardcoded credentials
or injection vectors), complexity hotspots, and deviations from required
design patterns.^26^

This critical separation of concerns is enforced at the foundational
level of orchestration. In environments like Gitea Actions or localized
agent loops operating via tools such as Cline or Roo Code, identity
separation is strictly maintained.^8^ The Implementer and the Quality
Guardian operate within independent model lanes, maintaining separate
context windows and utilizing isolated API credentials (e.g.,
CLAUDE\_GITEA\_TOKEN versus QWEN\_GITEA\_TOKEN).^8^ This isolation
prevents the cognitive contamination that invariably occurs when a
single model instance attempts to generate code and objectively critique
its own output simultaneously.

### The Mechanics of the Quality Guardian Audit

The efficacy of the Quality Guardian relies entirely on its highly tuned
system prompt and its access to specialized read-only tools. The
Guardian\'s prompt explicitly instructs it to prioritize safety,
architectural consistency, and educational feedback over execution speed
or task completion.^26^

A standard operational cycle for the Quality Guardian involves multiple
analytical phases to ensure the Implementer\'s code converges with the
AGENT.MD specification:

The first phase involves Initial Triage and Heuristic Analysis. The
Guardian utilizes its tools to scan the generated code for immediate
critical failures. This includes running basic syntax validation
routines, checking for type safety violations in strictly typed
languages, and identifying severe security flaws.^26^ If the code fails
to compile or contains a catastrophic vulnerability, it is immediately
rejected without further semantic analysis.

The second phase involves Deep Semantic and Architectural Review.
Assuming the code passes the initial heuristic scan, the Guardian
cross-references the generated syntax with the AGENT. MD
specifications.md specifications. It evaluates whether the Implementer
strictly adhered to the required frameworks, maintained the prescribed
directory structures, utilized correct naming conventions, and followed
abstract design patterns such as the SOLID principles or avoided Don\'t
Repeat Yourself (DRY) violations.^28^ This phase is heavily reliant on
the Guardian model\'s reasoning capabilities, as it must compare
concrete code against abstract guidelines.

The third phase is Pedagogical Synthesis. The Guardian formulates a
structured response to the Implementer. Rather than merely stating that
an error occurred, the Guardian is instructed to explain precisely why
the implementation violates the specification. It details the negative
impact the violation would have on maintainability or security and
offers concrete remediation strategies or safer code examples without
directly applying the fix itself.^26^ This educational feedback is
crucial for guiding the Implementer toward a compliant solution in the
next iteration.

### Pipeline Integration and Blocking Mechanisms

The Quality Guardian is not merely an advisory component; it serves as a
hard gate in the automated pipeline. Suppose the Guardian detects
critical violations of the AGENT.md file, it issues a failure signal
that deterministically halts the entire workflow.^7^ Integrations with
tools such as hefesto-ai provide practical implementations of this
concept, returning standard UNIX exit codes (e.g., executing exit code 2
when issues are found) to block continuous integration pipelines or
iterative agent loops forcibly.^30^

When the Guardian rejects an implementation, the comprehensive feedback
artifact is captured and passed directly back into the Implementer\'s
context window as a new user message.^8^ The Implementer is then forced
to process this feedback, recognize its deviation from the AGENT.md
file, and revise its code to satisfy the Guardian\'s criteria. This
adversarial loop continues until the Guardian approves the
implementation or a predefined timeout limit (such as a maximum of five
iterative loops) is reached.^32^ By applying this intense, iterative
forcing function, the experiment aims to demonstrate that vastly
different models can be corralled into producing highly comparable,
specification-compliant code.

The Anatomy of AGENT.md and Strategies for Context Retention
------------------------------------------------------------

To objectively test adherence, the specification itself must be
engineered with absolute precision. The AGENT.md (or its functional
equivalent, CLAUDE.md) serves as the baseline ground truth against which
all model outputs are evaluated. If the specification is ambiguous,
contradictory, or poorly formatted, the resulting adherence evaluation
will inherently lack statistical validity.^33^

### The Function of AGENT.md in Coding Environments

In agentic coding environments, AGENT.md operates as a persistent,
injected system prompt. It is automatically parsed by the orchestrator
and appended to the context window at the initiation of every session,
functioning as the localized memory and constitutional rulebook for the
AI assistant.^1^ It dictates the technical stack, build commands, file
structures, and absolute boundaries, effectively creating a sandbox of
operational rules.^35^

Despite its ubiquity in modern development workflows, reliance on
passive markdown files presents significant challenges. Developers
frequently observe that while an LLM may perfectly comprehend a
specification in the first conversational turn, its adherence rapidly
degrades as the context window fills with subsequent conversational
data, deeply nested tool outputs, and large blocks of generated
code.^3.^ This phenomenon, often referred to as docstring drift or
semantic dilution, occurs because the attention mechanisms within the
Transformer architecture assign varying weights to different segments of
the context window. As the absolute distance between the injected
AGENT.md file (typically located at the very beginning of the context
sequence) and the current generation task increases, the model\'s
adherence probability exponentially decays.^5^

### Vulnerabilities in Context Adherence

The experiment must account for the primary failure modes associated
with system prompt adherence to ensure accurate evaluation:

Selective amnesia is a pervasive issue where models adhere to
high-level, easily recognizable instructions (such as \"Use the React
framework\") while completely ignoring nuanced, highly specific
directives (such as \"Always implement early-return error handling
before processing array iterations\").^3^ Format disobedience is another
common failure mode. Specifications often dictate strict output formats,
such as requiring the model to return pure JSON without markdown fences.
Models frequently violate these formatting rules, appending
conversational filler (e.g., \"Here is the code you requested:\") that
instantly breaks downstream parsing mechanisms.^36^ Finally,
over-defensive guardrails represent a failure of the KICE (Keep Inputs
Concise & Essential) principle. In attempting to follow rules strictly,
models may implement unnecessarily complex abstractions, leading to
bloated, over-engineered solutions that satisfy the letter of the
specification while destroying the maintainability of the code\'s
maintainability.^4^

### Advanced Prompt Structuring Techniques

To ensure the experiment strictly isolates the model\'s fundamental
capability to adhere, rather than penalizing it for poor prompt
engineering by the researcher, the AGENT.The md file must be optimized
using advanced, academically rigorous prompt-engineering frameworks.^37^

Structure-embedding wrappers represent the first line of defense against
context decay. Explicit delimiters must bound instructions. Utilizing
structured formats such as distinct XML tags (e.g., \<system-rules\>,
\<architectural-boundaries\>) or rigid YAML blocks within the markdown
file forces the model\'s attention mechanism to recognize the absolute
boundaries of the instruction set, significantly improving rule
retention compared to continuous plain prose.^39^

Hierarchical decomposition must be applied to the document. The
specification must be broken down into atomic, categorically distinct
sections. A well-engineered AGENT.md includes explicit sections for
Objective, Tech Stack, Commands, and absolute Boundaries.^35^

Furthermore, the experimental pipeline will implement the Self-Spec
methodology. Recent research indicates that LLMs perform significantly
better when they are forced to process and re-articulate the
specification before generating code. The Self-Spec workflow requires
the model to read the AGENT first.md, instantiate a compact
specification schema representing its internal understanding of the
rules, and only then proceed to implementation. This alignment of
internal representational bias reduces format mistakes and edge-case
failures, raising zero-shot pass rates on complex coding benchmarks by
measurable margins and ensuring the model truly \"understands\" the
document before attempting to write code.^5^

Model Landscape Analysis: Cloud Frontier vs. Local Constraints
--------------------------------------------------------------

The selection of models for this adherence experiment represents a
comprehensive cross-section of the 2026 artificial intelligence
ecosystem, encompassing both tightly optimized open-weights
architectures designed for local deployment and massive proprietary
models running on hyperscale cloud infrastructure. Based on current
benchmark trajectories, significant variations in baseline adherence and
generation speed are anticipated before the Quality Guardian\'s
intervention.

### Local Deployment Candidates

Operating within the stringent 16GB VRAM constraint of the AMD Radeon RX
9060 XT forces the selection of highly efficient parameter
configurations and advanced quantization techniques.

The DeepSeek Coder V2 Lite is a primary candidate for local execution.
This 16-billion-parameter Mixture-of-Experts (MoE) model represents the
frontier of hardware-efficient inference. Because of its MoE
architecture, it only activates approximately 2.4 billion parameters
during any single inference pass.^41^ This sparse activation means the
model comfortably resides entirely within the GPU VRAM, offering
exceptional token throughput without relying on slower system RAM.^41^
Early benchmarks indicate performance parity with much larger dense
models on code-specific tasks, making it a highly capable Implementer
model for rapid, iterative agent loops.^41^

Alibaba's Qwen 3.5 Coder (32B variant) represents a heavier, more
capable local alternative. The Qwen series remains a dominant force in
open-weights coding due to its extensive pre-training on code datasets.
However, the 32B variant requires aggressive quantization (e.g.,
Q4\_K\_M) and mandatory layer-splitting across the 32GB of system RAM to
function on the target AMD hardware.^18^ Despite the slight latency
penalty incurred by this memory offloading, its massive parameter count
provides superior reasoning capabilities, particularly in comprehending
and adhering to complex, multi-layered AGENT.md specifications when
compared to smaller models.^44^

The Llama 4 architecture (specifically the Maverick or Scout variants
tailored for local deployment) brings enhanced context tracking and
reasoning to the open-source ecosystem. While the larger variants are
strictly out of reach for consumer-grade local deployment, the highly
optimized, smaller variants demonstrate strong baseline performance on
SWE-bench metrics. However, they have historically exhibited slight
vulnerabilities in strictly adhering to output formatting constraints
compared to models fine-tuned exclusively for coding tasks.^46^

### Cloud-Based Frontier Models

The localized models serve as a baseline for measuring the delta between
consumer edge computing and virtually unlimited cloud resources accessed
via an API.

OpenAI's GPT-5.3 and GPT-5.4 Codex represent the bleeding edge of
proprietary logical reasoning. These models typically command the
highest scores on competitive programming benchmarks and software
engineering tests.^47^ Their massive context windows and highly advanced
attention mechanisms theoretically make them highly resistant to
docstring drift. However, their extensive safety alignment tuning can
sometimes result in overly defensive code generation that violates the
simplicity requested in a specification.^5^

Anthropic's Claude 4.6 (including the Sonnet and Opus tiers) has been
widely adopted for agentic workflows precisely due to its superior
handling of lengthy context files. Tools like Claude Code explicitly
rely on the model\'s ability to ingest and continuously follow
documents, such as CLAUDE.md.^1^ Anthropic models are expected to excel
in both the Implementer role and, crucially, as the ultimate,
unforgiving Quality Guardian, demonstrating the highest first-pass
architectural coherence.

Google's Gemini 3.1 Pro Preview boasts an architecture with a context
length of millions of tokens, theoretically rendering it immune to the
context degradation that plagues smaller models. It consistently ranks
at the top of LiveCodeBench metrics and is uniquely positioned to handle
massive codebase repositories seamlessly while strictly adhering to
complex specifications.^47^

Table 1 outlines the baseline benchmark expectations for the selected
models, based on aggregated current coding evaluations.

  ---------------------------- ------------------------- -------------------------- -------------------------------- -----------------------------------
  **Model Designation**        **Deployment Strategy**   **Architecture Profile**   **Anticipated SWE-bench Tier**   **Anticipated Context Stability**
  **DeepSeek Coder V2 Lite**   Local (Full VRAM)         16B MoE                    Moderate                         High
  **Qwen 3.5 Coder 32B**       Local (Split RAM)         32B Dense                  High                             Very High
  **Llama 4 Maverick**         Local (Split RAM)         Optimized Dense            Moderate                         Moderate
  **GPT-5.4 Codex**            Cloud API                 Proprietary                Frontier                         Exceptional
  **Claude 4.6 Sonnet**        Cloud API                 Proprietary                Frontier                         Exceptional
  **Gemini 3.1 Pro**           Cloud API                 Proprietary                Frontier                         Exceptional
  ---------------------------- ------------------------- -------------------------- -------------------------------- -----------------------------------

Hypothesizing Code Convergence Through Iterative Forcing
--------------------------------------------------------

The fundamental inquiry of this experimental design is to determine how
providing identical models with equal instructions and an identical
AGENT.md specification will ultimately create highly comparable code.
When models are allowed to operate in a zero-shot, single-pass
environment, their outputs diverge wildly based on their underlying
training distributions, parameter sizes, and inherent biases. A 16B
local model will invariably write code differently than a
trillion-parameter cloud model.

However, the introduction of the Quality Guardian fundamentally alters
this dynamic. By deploying a static, highly reliable frontier model
(e.g., Claude 4.6 or GPT-5.4) as the universal Quality Guardian across
all tests, the evaluation of the Implementer models becomes an exercise
in forced convergence.^8^

When the local Qwen 3.5 model generates its first draft, it may violate
several architectural constraints outlined in the AGENT.md. The Quality
Guardian detects these deviations, rejects the code, and provides highly
specific, educational feedback detailing exactly how the code must be
refactored to align with the specification. The Qwen model is then
forced to revise its output. Simultaneously, when the cloud-based Gemini
model generates its first draft, it may produce overly complex
abstractions that violate the KICE principles specified. The Guardian
also rejects this output, forcing Gemini to simplify its architecture.

Through this iterative forcing process, the Quality Guardian acts as a
funnel. Regardless of the Implementer model\'s initial generative
biases, it is relentlessly corralled toward a singular,
specification-compliant outcome. The experiment hypothesizes that while
the *number of iterations* required to reach compliance will vary
dramatically across models (e.g., a local model may require 4 loops,
while a frontier model may require only 1), the *final accepted
codebase* will exhibit remarkable uniformity across all models.^32^ This
convergence demonstrates the immense power of multi-agent orchestration:
by decoupling generation from verification, developers can achieve
enterprise-grade code quality even when utilizing heavily constrained
local hardware.

Quantitative and Qualitative Evaluation Metrics
-----------------------------------------------

Evaluating the outputs of large language models in coding tasks extends
far beyond merely verifying whether the resulting script compiles
without syntax errors. Meaningful evaluation requires a comprehensive,
multi-dimensional framework that captures adherence to stylistic
guidelines, structural constraints, and security protocols.^51^ The
experimental framework relies on a highly structured bifurcated
evaluation strategy: deterministic computational metrics for rigid
constraints, and model-based LLM-as-a-judge assessments for abstract
adherence.^53^

### Deterministic Evaluation Metrics

Deterministic metrics are rule-based, programmatic checks that offer
fast, objective, and perfectly reproducible evaluations of LLM
outputs.^53^ These metrics are exceptionally valuable for verifying
strict adherence to the non-negotiable, rigid constraints outlined in
the AGENT---md file.

Abstract Syntax Tree (AST) validation is a primary deterministic tool.
To detect structural deviations from the specification, the evaluation
framework parses the generated code into an AST. This enables the
programmatic, automated detection of architectural anti-patterns, such
as cyclical dependencies, improper use of global variables when
dependency injection is specified, or functions exceeding maximum
cyclomatic complexity thresholds.^31^

Format enforcement and semantic drift are measured using strict regular
expression (regex) matching and JSON schema validation. This ensures the
model has not violated formatting constraints.^54^ For example, if the
specification explicitly requires plain text output, returning code
wrapped in markdown fences constitutes an immediate, deterministic
failure.^36^ Static code analysis tools, such as specialized linters
integrated directly into the testing pipeline, automatically scan for
stylistic deviations, missing unit test assertions, and raw framework
violations without requiring LLM intervention.^7^

Furthermore, quantitative metrics are calculated to assess the maturity
of the generated code. The Defensive Ratio measures the frequency of
error-handling blocks relative to the total algorithmic logic, ensuring
the model isn\'t writing fragile code. Doc Density evaluates the
presence of required inline documentation against the strict parameters
set in the specification, proving the model read and adhered to
documentation standards.^55^

### Model-Based Assessment (LLM-as-a-Judge)

While deterministic checks are flawless for rigid, programmatic
constraints, they are entirely incapable of evaluating subjective
qualities such as conceptual coherence, the elegance of the system
architecture, or adherence to the abstract style defined in the system
prompt.^54^ To capture these nuanced dimensions, the framework utilizes
the LLM-as-a-judge methodology.

In this paradigm, a secondary, highly capable LLM evaluates the target
Implementer model\'s output against a detailed grading rubric.^57^ The
judge model receives the original user prompt, the AGENT.md
specifications, the expected theoretical outcome, and the generated
code.^58^ It is instructed to perform step-by-step reasoning, evaluating
Answer Relevancy (the degree to which the generated code directly
addresses the functional requirements without injecting unnecessary
scope) and Instruction Adherence (a strict qualitative assessment of how
well the model followed abstract directives, such as enforcing strict
Model-View-Controller separation).^57^ The judge also checks for
Hallucination and Tool Correctness, identifying instances where the
model utilized non-existent library functions or hallucinated API
parameters.^57^

### Statistical Tracking and Failure Attribution

The combination of deterministic and model-based metrics yields a deep,
multi-faceted dataset for every model interaction. The evaluation
framework records a granular set of comparative statistics to determine
which model performs best under Quality Guardian oversight.

The Task Success Rate (Pass\@1) measures the percentage of tasks in
which the Implementer model produces fully functional,
specification-compliant code on its first attempt, requiring no
intervention from the Quality Guardian.^50^ This is the ultimate metric
of a model\'s inherent capability to understand and follow instructions.

Stepwise Progress and Iteration Count track the number of feedback loops
required for the Implementer to satisfy the Quality Guardian. A model
that achieves compliance in two iterations is objectively superior to
one that requires five, demonstrating a greater capacity for failure
attribution and the ability to self-correct seamlessly based on
feedback.^32^ Finally, Kaplan-Meier Survival Analysis is utilized. By
plotting error resolution across iterative feedback loops, researchers
can mathematically model the learning curves of different LLMs and
visualize how quickly different architectures adapt to the strict
corrections provided by the Quality Guardian over time.^32^

Table 2 illustrates the structure for capturing the multi-dimensional
evaluation data across the tested models.

  ----------------------------- ----------------------------------------------------------------------------- -----------------------------------------------------
  **Evaluation Metric**         **Description of Measurement**                                                **Assessment Methodology**
  **Pass\@1 Success**           Strict specification compliance achieved on the first generation pass.        Automated unit tests + Deterministic format checks.
  **Iteration Efficiency**      Mean number of feedback loops required to satisfy the Quality Guardian.       Log analysis of the A2A orchestration pipeline.
  **Defensive Ratio**           Adherence to error-handling protocols specified in the AGENT.md.              AST static analysis.
  **Architectural Coherence**   Adherence to abstract design patterns (e.g., DRY/SOLID principles).           LLM-as-a-Judge grading rubric (Scale 1-5).
  **Semantic Drift Rate**       Frequency of deviations from the specified tone or formatting instructions.   Heuristic NLP analysis and Regex parsing.
  ----------------------------- ----------------------------------------------------------------------------- -----------------------------------------------------

Conclusion
----------

The transition toward autonomous, agentic software factories
necessitates a profound evolution in how machine learning systems are
evaluated and deployed. Generating syntactically correct code is no
longer the definitive metric of success; true utility in modern
engineering is defined by a language model\'s capacity to strictly
adhere to complex architectural constraints, security guidelines, and
stylistic mandates codified within comprehensive specification files
such as AGENT.md. By implementing a bifurcated orchestration
architecture---in which an uncompromising Quality Guardian relentlessly
audits generative output from an Implementer---researchers can
systematically quantify adherence and compel disparate models to
converge on standardized outputs.

The experimental design detailed herein provides a rigorous,
platform-agnostic blueprint for executing this complex evaluation. By
standardizing the API interface via Lemonade Server and meticulously
optimizing the AMD ROCm 7.2.1 stack to accommodate 16GB of VRAM and 32GB
of system RAM, the pipeline effectively isolates the reasoning
capabilities of localized models from proprietary cloud counterparts. By
applying deterministic syntax checks, dynamic LLM-as-a-judge rubrics,
and Kaplan-Meier survival analysis within iterative feedback loops, this
framework will yield unparalleled insights into specification retention
rates, semantic drift, and systemic reliability of the 2026 LLM
ecosystem. Ultimately, the resulting data will directly inform the
architectural strategies needed to deploy autonomous coding agents
safely and effectively, demonstrating that rigorous, AI-driven oversight
can deliver enterprise-grade reliability even in highly constrained
local deployments.

#### Works cited

1.  How to Create the Perfect CLAUDE.md (incl. Template) - Gradually AI,
    accessed April 7, 2026,
    [<https://www.gradually.ai/en/claude-md/>.]{.underline}

2.  How to Write a Good CLAUDE.md File - Builder.io, accessed April 7,
    2026,
    [[https://www.builder.io/blog/claude-md-guide]{.underline}](https://www.builder.io/blog/claude-md-guide)

3.  Evaluating AGENTS.md: Are they helpful for coding agents? - Hacker
    News, accessed April 7, 2026,
    [[https://news.ycombinator.com/item?id=47034087]{.underline}](https://news.ycombinator.com/item?id=47034087)

4.  AI Writing Code: Addressing Job Security Concerns for Junior and
    Mid-Level Engineers, accessed April 7, 2026,
    [[https://dev.to/svetlix/ai-writing-code-addressing-job-security-concerns-for-junior-and-mid-level-engineers-44l9]{.underline}](https://dev.to/svetlix/ai-writing-code-addressing-job-security-concerns-for-junior-and-mid-level-engineers-44l9)

5.  Self-Spec: Model-Authored Specifications for Reliable LLM Code
    Generation \| OpenReview, accessed April 7, 2026,
    [[https://openreview.net/forum?id=6pr7BUGkLp]{.underline}](https://openreview.net/forum?id=6pr7BUGkLp)

6.  My LLM coding workflow going into 2026 \| by Addy Osmani - Medium,
    accessed April 7, 2026,
    [[https://medium.com/\@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e]{.underline}](https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e)

7.  How AI Agents Automated Our QA: 700+ Test Coverage - OpenObserve,
    accessed April 7, 2026,
    [[https://openobserve.ai/blog/autonomous-qa-testing-ai-agents-claude-code/]{.underline}](https://openobserve.ai/blog/autonomous-qa-testing-ai-agents-claude-code/)

8.  The Agentic Software Factory: How AI Teams Debate, Code, and Can
    Secure Enterprise Infrastructure - DEV Community, accessed April 7,
    2026,
    [[https://dev.to/uenyioha/the-agentic-software-factory-how-ai-teams-debate-code-and-secure-enterprise-infrastructure-9eh]{.underline}](https://dev.to/uenyioha/the-agentic-software-factory-how-ai-teams-debate-code-and-secure-enterprise-infrastructure-9eh)

9.  For my setup with an AMD Radeon RX 9060 XT 16GB and 32GB DDR5 RAM,
    are there any better and faster local LLMs optimized for agent ? :
    r/LocalLLaMA - Reddit, accessed April 7, 2026,
    [[https://www.reddit.com/r/LocalLLaMA/comments/1rqkmop/for\_my\_setup\_with\_an\_amd\_radeon\_rx\_9060\_xt\_16gb/]{.underline}](https://www.reddit.com/r/LocalLLaMA/comments/1rqkmop/for_my_setup_with_an_amd_radeon_rx_9060_xt_16gb/)

10. A beginner\'s guide to deploying LLMs with AMD on Windows using
    PyTorch, accessed April 7, 2026,
    [[https://gpuopen.com/learn/pytorch-windows-amd-llm-guide/]{.underline}](https://gpuopen.com/learn/pytorch-windows-amd-llm-guide/)

11. AMD tested 20+ local models for coding & only 2 actually work
    (testing linked) - Reddit, accessed April 7, 2026,
    [[https://www.reddit.com/r/LocalLLaMA/comments/1nufu17/amd\_tested\_20\_local\_models\_for\_coding\_only\_2/]{.underline}](https://www.reddit.com/r/LocalLLaMA/comments/1nufu17/amd_tested_20_local_models_for_coding_only_2/)

12. DeepSeek-V2-Lite vs GPT-OSS-20B on my 2018 potato i3-8145U + UHD
    620, OpenVINO Comparison. : r/LocalLLaMA - Reddit, accessed April 7,
    2026,
    [[https://www.reddit.com/r/LocalLLaMA/comments/1qycn5s/deepseekv2lite\_vs\_gptoss20b\_on\_my\_2018\_potato/]{.underline}](https://www.reddit.com/r/LocalLLaMA/comments/1qycn5s/deepseekv2lite_vs_gptoss20b_on_my_2018_potato/)

13. Use ROCm on Radeon and Ryzen, accessed April 7, 2026,
    [[https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html]{.underline}](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html)

14. OpenClaw (Clawd Bot) with vLLM Running for Free on AMD Developer
    Cloud, accessed April 7, 2026,
    [[https://www.amd.com/en/developer/resources/technical-articles/2026/openclaw-with-vllm-running-for-free-on-amd-developer-cloud-.html]{.underline}](https://www.amd.com/en/developer/resources/technical-articles/2026/openclaw-with-vllm-running-for-free-on-amd-developer-cloud-.html)

15. Serving Large Language Models with vLLM on AMD ROCm GPUs \| by Trade
    Mamba, accessed April 7, 2026,
    [[https://medium.com/\@trademamba/serving-large-language-models-with-vllm-on-amd-rocm-gpus-a00ea352e2ac]{.underline}](https://medium.com/@trademamba/serving-large-language-models-with-vllm-on-amd-rocm-gpus-a00ea352e2ac)

16. Run any NVIDIA/CUDA only software on AMD CARDS (currently supported
    are iGPU and 5000-9000 series) : r/ROCm - Reddit, accessed April 7,
    2026,
    [[https://www.reddit.com/r/ROCm/comments/1sbp62q/run\_any\_nvidiacuda\_only\_software\_on\_amd\_cards/]{.underline}](https://www.reddit.com/r/ROCm/comments/1sbp62q/run_any_nvidiacuda_only_software_on_amd_cards/)

17. impressive performance of deepseek-coder-v2:16b on minipc with intel
    n100 and 32GB ram, accessed April 7, 2026,
    [[https://www.reddit.com/r/LocalLLaMA/comments/1dkmpja/impressive\_performance\_of\_deepseekcoderv216b\_on/]{.underline}](https://www.reddit.com/r/LocalLLaMA/comments/1dkmpja/impressive_performance_of_deepseekcoderv216b_on/)

18. Local AI Models for Coding: Is It Realistic in 2026? - Failing Fast,
    accessed April 7, 2026,
    [[https://failingfast.io/local-coding-ai-models/]{.underline}](https://failingfast.io/local-coding-ai-models/)

19. Compare DeepSeek Coder V2 Lite Instruct vs Mistral Small (Sep \'24)
    \| AI Model Comparison, accessed April 7, 2026,
    [[https://llmbase.ai/compare/deepseek-coder-v2-lite,mistral-small/]{.underline}](https://llmbase.ai/compare/deepseek-coder-v2-lite,mistral-small/)

20. Day 0 Support for Gemma 4 on AMD Processors and GPUs, accessed April
    7, 2026,
    [[https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-gemma-4-on-amd-processors-and-gpus.html]{.underline}](https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-gemma-4-on-amd-processors-and-gpus.html)

21. Lemonade by AMD: a fast and open source local LLM server using GPU
    and NPU \| Hacker News, accessed April 7, 2026,
    [[https://news.ycombinator.com/item?id=47612724]{.underline}](https://news.ycombinator.com/item?id=47612724)

22. Why Faster AI Code Isn\'t Faster Software (and How to Fix
    It)-(7)-Thriving in the New Normal of AI-Augmented Software
    Engineering \| by Jingwei Chen \| Medium, accessed April 7, 2026,
    [[https://medium.com/\@Voleco/why-faster-ai-code-isnt-faster-software-and-how-to-fix-it-7-thriving-in-the-new-normal-of-4cdf152bbefc]{.underline}](https://medium.com/@Voleco/why-faster-ai-code-isnt-faster-software-and-how-to-fix-it-7-thriving-in-the-new-normal-of-4cdf152bbefc)

23. claude-copilot/docs/10-architecture/01-agents.md at main - GitHub,
    accessed April 7, 2026,
    [[https://github.com/Everyone-Needs-A-Copilot/claude-copilot/blob/main/docs/10-architecture/01-agents.md]{.underline}](https://github.com/Everyone-Needs-A-Copilot/claude-copilot/blob/main/docs/10-architecture/01-agents.md)

24. MichelKerkmeester/opencode\--spec-kit-skilled-agent-orchestration: A
    practical AI-assisted coding setup: structured docs, semantic
    memory, and reusable skills so you spend less time re-explaining
    context and more time shipping. · GitHub, accessed April 7, 2026,
    [[https://github.com/MichelKerkmeester/opencode-spec-kit-framework]{.underline}](https://github.com/MichelKerkmeester/opencode-spec-kit-framework)

25. code-quality-guardian \| Skills Marke\... · LobeHub, accessed April
    7, 2026,
    [[https://lobehub.com/pl/skills/jiabinone-anyrouter-checkin-code-quality-guardian]{.underline}](https://lobehub.com/pl/skills/jiabinone-anyrouter-checkin-code-quality-guardian)

26. code-quality-guardian \| Skills Marke\... - LobeHub, accessed April
    7, 2026,
    [[https://lobehub.com/skills/neversight-skills\_feed-code-quality-guardian]{.underline}](https://lobehub.com/skills/neversight-skills_feed-code-quality-guardian)

27. agent-sh/agentsys: AI writes code. This automates everything else ·
    19 plugins, 47 agents, and 40 skills · for Claude Code, OpenCode,
    Codex, Cursor, Kiro. - GitHub, accessed April 7, 2026,
    [[https://github.com/agent-sh/agentsys]{.underline}](https://github.com/agent-sh/agentsys)

28. 程式碼品質守護者\| Skills Marketplace - LobeHub, accessed April 7,
    2026,
    [[https://lobehub.com/zh-TW/skills/neversight-skills\_feed-code-quality-guardian]{.underline}](https://lobehub.com/zh-TW/skills/neversight-skills_feed-code-quality-guardian)

29. How I Built an AI-Powered Code Quality Guardian for GitHub (And
    Blocked My Own PR), accessed April 7, 2026,
    [[https://medium.com/\@jtouley/building-a-github-code-quality-analyzer-with-openai-github-actions-9a457aea5a99]{.underline}](https://medium.com/@jtouley/building-a-github-code-quality-analyzer-with-openai-github-actions-9a457aea5a99)

30. artvepa80/Agents-Hefesto: AI-powered code quality agent with ML
    semantic analysis. Prevents technical debt before production. Free
    tier: static analysis. Pro tier: ML duplicate detection, real-time
    metrics, CI/CD automation. Built for AI coding era. Open core model:
    Phase 0 free, Phase 1 paid. - GitHub, accessed April 7, 2026,
    [[https://github.com/artvepa80/Agents-Hefesto]{.underline}](https://github.com/artvepa80/Agents-Hefesto)

31. Hefesto Code Guardian · Actions · GitHub Marketplace, accessed April
    7, 2026,
    [[https://github.com/marketplace/actions/hefesto-code-guardian]{.underline}](https://github.com/marketplace/actions/hefesto-code-guardian)

32. Benchmarking Large Language Models for ABAP Code Generation: An
    Empirical Study on Iterative Improvement by Compiler Feedback - x -
    arXiv, accessed April 7, 2026,
    [[https://arxiv.org/html/2601.15188v1]{.underline}](https://arxiv.org/html/2601.15188v1)

33. Validating Formal Specifications with LLM-generated Test Cases -
    arXiv, accessed April 7, 2026,
    [[https://arxiv.org/html/2510.23350v2]{.underline}](https://arxiv.org/html/2510.23350v2)

34. Difference between CLAUDE.md, Agents, Skills, Commands and Styles
    from api request, accessed April 7, 2026,
    [[https://www.reddit.com/r/ClaudeCode/comments/1o9qjn1/difference\_between\_claudemd\_agents\_skills/]{.underline}](https://www.reddit.com/r/ClaudeCode/comments/1o9qjn1/difference_between_claudemd_agents_skills/)

35. How to write a good spec for AI agents - Addy Osmani, accessed April
    7, 2026,
    [[https://addyosmani.com/blog/good-spec/]{.underline}](https://addyosmani.com/blog/good-spec/)

36. Implementing Automated Rules-Based Evaluations for LLM
    Applications - DEV Community, accessed April 7, 2026,
    [[https://dev.to/kalio/implementing-automated-rules-based-evaluations-for-llm-applications-468j]{.underline}](https://dev.to/kalio/implementing-automated-rules-based-evaluations-for-llm-applications-468j)

37. Reporting LLM Prompting in Automated Software Engineering: A
    Guideline Based on Current Practices and Expectations - arXiv,
    accessed April 7, 2026,
    [[https://arxiv.org/html/2601.01954v1]{.underline}](https://arxiv.org/html/2601.01954v1)

38. Prompt Engineering of LLM Prompt Engineering : r/PromptEngineering -
    Reddit, accessed April 7, 2026,
    [[https://www.reddit.com/r/PromptEngineering/comments/1hv1ni9/prompt\_engineering\_of\_llm\_prompt\_engineering/]{.underline}](https://www.reddit.com/r/PromptEngineering/comments/1hv1ni9/prompt_engineering_of_llm_prompt_engineering/)

39. What makes Claude Code so damn good (and how to recreate that magic
    in your agent)!?, accessed April 7, 2026,
    [[https://minusx.ai/blog/decoding-claude-code/]{.underline}](https://minusx.ai/blog/decoding-claude-code/)

40. Automated Framework to Evaluate and Harden LLM System Instructions
    against Encoding Attacks - arXiv, accessed April 7, 2026,
    [[https://arxiv.org/html/2604.01039v1]{.underline}](https://arxiv.org/html/2604.01039v1)

41. DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in
    Code Intelligence - GitHub, accessed April 7, 2026,
    [[https://github.com/deepseek-ai/DeepSeek-Coder-V2]{.underline}](https://github.com/deepseek-ai/DeepSeek-Coder-V2)

42. deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct - Hugging Face, accessed
    April 7, 2026,
    [[https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct]{.underline}](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct)

43. Which is better for coding in 16GB (V)RAM at q4: Qwen3.0-30B-A3B,
    Qwen3.0-14B, Qwen2.5-Coding-14B, Phi4-14B, Mistral Small 3.0/3.1
    24B? : r/LocalLLaMA - Reddit, accessed April 7, 2026,
    [[https://www.reddit.com/r/LocalLLaMA/comments/1kegoi2/which\_is\_better\_for\_coding\_in\_16gb\_vram\_at\_q4/]{.underline}](https://www.reddit.com/r/LocalLLaMA/comments/1kegoi2/which_is_better_for_coding_in_16gb_vram_at_q4/)

44. DeepSeek-V3 0324 vs Qwen2.5-Coder 32B Instruct - AnotherWrapper,
    accessed April 7, 2026,
    [[https://anotherwrapper.com/tools/llm-pricing/deepseek-v3-0324/qwen25-coder-32b-instruct]{.underline}](https://anotherwrapper.com/tools/llm-pricing/deepseek-v3-0324/qwen25-coder-32b-instruct)

45. Is qwen 2.5 coder still the best? : r/LocalLLaMA - Reddit, accessed
    April 7, 2026,
    [[https://www.reddit.com/r/LocalLLaMA/comments/1j2usb0/is\_qwen\_25\_coder\_still\_the\_best/]{.underline}](https://www.reddit.com/r/LocalLLaMA/comments/1j2usb0/is_qwen_25_coder_still_the_best/)

46. Comparison - Vals AI, accessed April 7, 2026,
    [[https://www.vals.ai/comparison?modelA=fireworks%2Fllama4-maverick-instruct-basic]{.underline}](https://www.vals.ai/comparison?modelA=fireworks/llama4-maverick-instruct-basic)

47. Best LLM for Coding 2026 \| AI Coding Model Rankings & Benchmarks -
    Onyx AI, accessed April 7, 2026,
    [[https://onyx.app/best-llm-for-coding]{.underline}](https://onyx.app/best-llm-for-coding)

48. Llama 4 underperforms: a benchmark against coding-centric models -
    Rootly, accessed April 7, 2026,
    [[https://rootly.com/blog/llama-4-underperforms-a-benchmark-against-coding-centric-models]{.underline}](https://rootly.com/blog/llama-4-underperforms-a-benchmark-against-coding-centric-models)

49. Best LLM for Coding (2026) --- AI Model Rankings \| Price Per Token,
    accessed April 7, 2026,
    [[https://pricepertoken.com/leaderboards/coding]{.underline}](https://pricepertoken.com/leaderboards/coding)

50. Evaluating LLM-based Agents: Metrics, Benchmarks, and Best
    Practices, accessed April 7, 2026,
    [[https://samiranama.com/posts/Evaluating-LLM-based-Agents-Metrics,-Benchmarks,-and-Best-Practices/]{.underline}](https://samiranama.com/posts/Evaluating-LLM-based-Agents-Metrics,-Benchmarks,-and-Best-Practices/)

51. Building an LLM evaluation framework: best practices - Datadog,
    accessed April 7, 2026,
    [[https://www.datadoghq.com/blog/llm-evaluation-framework-best-practices/]{.underline}](https://www.datadoghq.com/blog/llm-evaluation-framework-best-practices/)

52. A Practical Guide for Evaluating LLMs and LLM-Reliant Systems -
    arXiv, accessed April 7, 2026,
    [[https://arxiv.org/html/2506.13023v1]{.underline}](https://arxiv.org/html/2506.13023v1)

53. An evaluation framework for ambient digital scribing tools in
    clinical applications - PMC, accessed April 7, 2026,
    [[https://pmc.ncbi.nlm.nih.gov/articles/PMC12166074/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC12166074/)

54. The best approach to compare LLM outputs - Portkey, accessed April
    7, 2026,
    [[https://portkey.ai/blog/the-best-approach-to-compare-llm-outputs/]{.underline}](https://portkey.ai/blog/the-best-approach-to-compare-llm-outputs/)

55. Show and Tell: Prompt Strategies for Style Control in Multi-Turn LLM
    Code Generation, accessed April 7, 2026,
    [[https://arxiv.org/html/2511.13972v1]{.underline}](https://arxiv.org/html/2511.13972v1)

56. vibecoding/prompt-engineering-guide.md at main - GitHub, accessed
    April 7, 2026,
    [[https://github.com/cpjet64/vibecoding/blob/main/prompt-engineering-guide.md]{.underline}](https://github.com/cpjet64/vibecoding/blob/main/prompt-engineering-guide.md)

57. LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide -
    Confident AI, accessed April 7, 2026,
    [[https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation]{.underline}](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)

58. A list of metrics for evaluating LLM-generated content - Microsoft
    Learn, accessed April 7, 2026,
    [[https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/working-with-llms/evaluation/list-of-eval-metrics]{.underline}](https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/working-with-llms/evaluation/list-of-eval-metrics)
