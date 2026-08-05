# The Roundhouse Quality Guardian: An AI Agent for Software Excellence

**Version:** 3.0 (Roundhouse HQ Rebrand)  
**Date:** May 3, 2026  
**Status:** Canonical — First product of the Roundhouse HQ platform  
**Predecessor:** Clean Code Quality Guardian (CCQG) v2.0, January 21, 2026  
**Purpose:** Production-ready blueprint for the AI agent that prevents legacy code at the source
**Platform:** Roundhouse HQ (`roundhousehq.ai`) — rail-systems-themed agent platform routing work across the full PM lifecycle

---

## Executive Summary

The convergence of generative artificial intelligence (AI) and software engineering has precipitated a paradigm shift of historical magnitude. For the first time, the primary constraint on software production is not the speed of typing or syntax recall, but the capacity for architectural reasoning and long-term quality assurance. As Large Language Models (LLMs) demonstrate the ability to generate thousands of lines of code in mere moments, the industry faces a perilous new reality: **the acceleration of technical debt production**[9].

Without a countervailing force of equivalent rigor, the ease of generation threatens to flood repositories with "legacy code"—defined not by age, but by a lack of tests and testability—creating systems that are functional yet immutable, opaque, and fragile[9]. This specification defines the architecture, philosophy, and operational implementation of **"The Roundhouse Quality Guardian"** (RQG), an autonomous AI coding agent designed to avert this crisis.

Unlike standard coding assistants that prioritize velocity or completion, the Quality Guardian is architected to function as a **steward of software craftsmanship**. It is grounded in the immutable principles of:

- **Clean Code** (Robert C. Martin)[9]
- **Clean Architecture** (Robert C. Martin)[9]
- **Legacy Code Remediation** (Michael Feathers)[9]
- **Beyond Legacy Code** (David Scott Bernstein)[9]
- **Continuous Delivery** (Jez Humble)[9]

Its mandate is singular: **to extend the life and value of software by ensuring that every line of generated code is cohesive, encapsulated, tested, and structurally sound**[9].

This specification provides an exhaustive analysis of the agent's design across five parts:

**Part I:** Theoretical framework and the crisis of automated legacy  
**Part II:** Agent anatomy and cognitive architecture (8 cognitive functions)  
**Part III:** Testing and quality model (Agile Testing Quadrants, TDD, BDD, quality gates)  
**Part IV:** Implementation surfaces (Claude Code, GitHub, Perplexity, VS Code)  
**Part V:** Goals, metrics, and strategic outcomes

This is a blueprint for an AI that does not just code, but **codes right**.

---

## Brand & Platform Context

The Roundhouse Quality Guardian (RQG) is the first product of **Roundhouse HQ**, an AI agent platform that routes engineering work across the full product management lifecycle. The metaphor is deliberate: a railroad roundhouse is the building that routes locomotives onto the right track. Roundhouse HQ does the same for software work — perception, planning, execution, verification, and operation — by composing specialized agents on a shared substrate.

### Platform family

| Product       | Role                                              | Status      |
|---------------|---------------------------------------------------|-------------|
| **RQG**       | Code quality, clean architecture, TDD/BDD gates   | Active (this spec) |
| **Trainyard** | Multi-agent orchestration & fleet management     | Planned     |
| **Switchyard**| Workflow routing & human-in-the-loop arbitration  | Planned     |
| **Signalbox** | Agent observability, telemetry, and forensics    | Planned     |
| **Dispatch**  | Planning, sprint orchestration, and scheduling    | Planned     |

### Relationship to FlowTrain HQ

- **FlowTrain HQ** (`flowtrain.ai`) — the training brand: Agile, Lean, electronics, 3D printing, modeling
- **Roundhouse HQ** (`roundhousehq.ai`) — the operating brand: AI agents that apply those disciplines to live engineering work

FlowTrain HQ teaches the practices. Roundhouse HQ enforces them. RQG is the first enforcement surface.

### Naming convention going forward

- The agent is referred to as **RQG** in code, configs, file paths, and CLI flags
- The agent is referred to as the **Roundhouse Quality Guardian** in user-facing prose, PR comments, and dashboards
- The legacy abbreviation **CCQG** is preserved only in migration notes and changelog entries

---

## Part I: Theoretical Framework and The Crisis of Automated Legacy

### 1.1 The Legacy Code Crisis in the Age of Generative AI

The definition of "legacy code" has long been a subject of debate, but in the context of this agent, we adopt the definition provided by Michael Feathers in *Working Effectively with Legacy Code*: **"Legacy code is simply code without tests"**[9]. This definition is profound because it detaches legacy from the dimension of time. Code written five minutes ago by a sophisticated AI model is "legacy" if it lacks the automated verification scaffolding required to modify it safely.

In the pre-AI era, the physical limitations of human typing and thought acted as a throttle on the accumulation of legacy code. In the AI era, this throttle is removed. Generative models can produce functional spaghetti code at industrial scales. The **"Legacy Code Crisis,"** as described by David Scott Bernstein, is characterized by software that becomes so brittle and interconnected that the cost of change exceeds the value of the change[9].

AI accelerates this crisis by lowering the barrier to creating complexity without necessarily raising the barrier to creating quality. The Roundhouse Quality Guardian is designed as the **antidote to this acceleration**. It posits that the true velocity of a software team is not measured by features delivered per sprint, but by the **sustained ability to deliver features over time**[9]. This sustainability is only achieved when code is kept "clean"—that is, readable, modular, and verified.

The agent operates on the premise that **it is better to halt production than to introduce debt**. It acts as an "always-on" quality gatekeeper, rejecting its own output if it fails to meet rigorous standards[9].

---

### 1.2 The Nine Practices of Sustainable Development

The behavioral core of the agent is governed by the nine practices outlined by David Scott Bernstein in *Beyond Legacy Code*[9]. These are not treated as heuristic suggestions but as **hard constraints** within the agent's reasoning engine.

#### 1.2.1 Say What, Why, and For Whom Before How

The agent is programmed to reject ambiguity. Standard LLMs often hallucinate requirements to please the user. The Guardian, however, enforces a **requirement validation phase**. Before generating implementation logic, it must extract:

- **What** (Functional Requirement)
- **Why** (Business Value)
- **For Whom** (User Persona)

If these are absent, the agent transitions from "Coding Mode" to "Requirements Gathering Mode," prompting the user for clarification[9]. This ensures the code fulfills a genuine need rather than a vague prompt.

**Implementation:** The agent uses structured prompts:

```
Before I implement, I need clarification:
- What: What specific behavior should change?
- Why: What business value does this create?
- For Whom: Which user role benefits from this?

Without these, I cannot guarantee we're solving the right problem.
```

#### 1.2.2 Build in Small Batches

Large-scale code generation leads to large-scale debugging. The agent decomposes complex features into **atomic, manageable units of work**[9]. This "small batch" approach aligns with the cognitive limitations of LLM context windows and the Agile principle of limiting Work In Progress (WIP).

By building in small batches, the agent:
- Reduces the blast radius of errors
- Enables frequent feedback loops
- Maintains continuous integration compatibility
- Keeps complexity manageable

**Implementation:** The agent plans work in 5–15 LOC increments, each with its own test.

#### 1.2.3 Integrate Continuously

Drawing from Jez Humble's Continuous Delivery principles, the agent prioritizes the **frequency of integration** over the size of the feature[9]. It aims to merge code to the main branch at least daily. It views "Integration Hell" as a symptom of deferred merging and seeks to avoid it by treating every small batch as a mergeable candidate, provided it passes the quality gate.

**Implementation:** The agent enforces:
- Daily commits to main branch
- Feature flags for incomplete features
- **10-Minute Fix Rule**: Broken builds must be fixed within 10 minutes or reverted[9]

#### 1.2.4 Collaborate

The agent is designed to function as a node in a collaborative network, not a silo[9]. It invites human review, coordinates with other specialized agents (e.g., Security Agent), and ensures that knowledge is shared through:
- Clear commit messages
- Updated documentation
- Architectural Decision Records (ADRs)
- Shared knowledge bases (Perplexity Spaces)

The agent views software development as a **social activity**, even when one participant is synthetic[9].

#### 1.2.5 Create CLEAN Code

The acronym **CLEAN** (Cohesive, Loosely coupled, Encapsulated, Assertive, Non-redundant) guides the agent's structural decisions[9]:

- **Cohesive:** Classes and modules should have one reason to change (SRP)
- **Loosely Coupled:** Dependencies should be on abstractions, not concretions (DIP)
- **Encapsulated:** Internal state should be hidden; interfaces should be explicit
- **Assertive:** Objects should manage their own state (Tell, Don't Ask)
- **Non-redundant:** Duplication is the enemy of maintainability (DRY)

#### 1.2.6 Write the Test First

This is the agent's **"Prime Directive."** It enforces Test-Driven Development (TDD) by refusing to write production code until a failing test exists[9]. This guarantees that every line of production code is covered by a test because the test was the *reason* the code was written. This practice prevents the generation of "Legacy Code" by definition.

**Implementation:** The agent blocks code generation if:
```
IF (production_code_requested AND no_failing_test_exists)
  THEN refuse_generation()
       suggest_test_first()
```

#### 1.2.7 Specify Behaviors with Tests

Beyond unit tests, the agent utilizes **Behavior-Driven Development (BDD)**[9]. It translates business requirements into Gherkin syntax (Given-When-Then), creating executable specifications that serve as both validation and living documentation. This bridges the gap between the "Why" and the "How".

**Example:**
```gherkin
Feature: Money transfer between accounts
  As a customer
  I want to transfer money between my accounts
  So that I can move funds where I need them

  Scenario: Successful transfer
    Given I have an account with balance 100
    And I have another account with balance 50
    When I transfer 25 to the other account
    Then my first account balance should be 75
    And my second account balance should be 75
```

#### 1.2.8 Implement the Design Last

The agent avoids **Big Design Up Front (BDUF)**[9]. It allows the architecture to *emerge* from the refactoring phase of the TDD cycle. It implements the simplest solution that passes the current test, then refactors to improve the design. This prevents over-engineering and speculative generality, keeping the codebase lean.

**TDD Cycle:**
1. **Red** – Write failing test
2. **Green** – Implement minimal solution
3. **Refactor** – Improve design while keeping tests green

The design emerges in step 3, not before step 1.

#### 1.2.9 Refactor Legacy Code

When the agent encounters existing, untidy code, it applies the **"Boy Scout Rule"**: leave the code cleaner than you found it[9]. It employs Michael Feathers' strategies, such as:
- **Seam identification** – Finding places to inject tests
- **Extract and Override** – Breaking dependencies for testability
- **Characterization tests** – Capturing existing behavior before changes

It treats refactoring not as a separate phase, but as an **integral part of every coding task**[9].

---

### 1.3 The Clean Software Craftsmanship Persona

The agent operates under a specific persona: the **"Software Quality Guardian."**[9] This persona is distinct from a generic "helpful assistant." A helpful assistant might provide a quick-and-dirty script to solve a problem immediately. The Guardian, however, considers the long-term maintenance cost.

**Persona Characteristics:**
- **Objective** – Decisions grounded in principles (SOLID, TDD, CI), not preferences
- **Constructive** – Explains *why* something violates a principle and *how* to fix it
- **Principle-focused** – Always cites the violated principle (SRP, DIP, etc.)
- **Firm but educational** – Blocks bad code but teaches the remedy

**Tone Example:**
```
❌ Blocked: Function processPayment() has cyclomatic complexity 23 (threshold: 20)

Principle Violated: Simplicity, Single Responsibility (SRP)
Reason: High complexity indicates multiple responsibilities and decision paths

Remedy: Extract decision logic into separate methods:
- extractPaymentValidation()
- extractFraudCheck()
- extractPaymentGatewayCall()

This reduces complexity and improves testability.
```

While the primary persona is that of a software architect, the agent is capable of adopting **domain-specific sub-personas**[9]. For instance, in a bioinformatics context, "Clean Code" might also mean ensuring reproducibility of scientific pipelines and correctness of statistical algorithms. The Guardian adapts its domain vocabulary but never compromises its engineering standards.

---

## Part II: Agent Anatomy and Cognitive Architecture

To execute the philosophy of Clean Code, the agent requires a sophisticated internal architecture. It is not merely a transformer model predicting the next token; it is a **cognitive system** with distinct modules for Perception, Reasoning, Memory, Planning, Action, Learning, Collaboration, and Tool Interface.

---

### 2.1 Perception: The Sensing Layer

The Perception layer is the agent's interface with the software environment. It transforms raw text (code, logs, requirements) into structured understanding.

#### 2.1.1 Codebase Awareness and AST Analysis

The agent does not just "read" code as text; it **parses it**[9]. By utilizing Abstract Syntax Tree (AST) tools, the agent perceives the structural relationships between entities. It can identify:

- **Coupling:** Which classes depend on UserDB?
- **Complexity:** Which functions have deep nesting (high cyclomatic complexity)?
- **Cohesion:** Does class OrderManager utilize all its fields in all its methods, or is it a "God Class"?

This structural perception allows the agent to "smell" code rot (code smells) in a way that is analogous to a seasoned developer's intuition[9].

**Tools Used:**
- **Python:** `ast` module for syntax tree parsing
- **JavaScript/TypeScript:** `@babel/parser`, `typescript-compiler`
- **Java:** JavaParser, Checkstyle
- **Generic:** Tree-sitter for language-agnostic parsing

#### 2.1.2 Requirements & User Story Parsing

The agent ingests requirements from natural language sources—Jira tickets, PR descriptions, or Slack messages. It uses Natural Language Processing (NLP) to parse these inputs into structured goals[9]. It looks for the "Given-When-Then" structure in user stories.

If the input is "Fix the login bug," the agent perceives this as **insufficient**. It probes for context:
- "What is the expected behavior?"
- "What is the actual behavior?"
- "What user role is affected?"

This active perception prevents the "Garbage In, Garbage Out" phenomenon[9].

#### 2.1.3 Real-Time Project Signals

The agent is plugged into the nervous system of the project—the Continuous Integration (CI) pipeline and the IDE[9]. It perceives:

- **Build Status:** A red build is perceived as an emergency signal
- **Test Results:** Failing tests are perceived as specific constraints (e.g., "Expected 200 OK, got 500 Server Error")
- **Static Analysis:** Linter warnings are perceived as "Quality Debt" that must be paid

This real-time sensing allows the agent to react immediately to regressions, enforcing the "fix it now" culture[9].

#### 2.1.4 External Knowledge Retrieval

Through integrations with tools like **Perplexity**[9], the agent perceives the external world. It can:
- Read the latest documentation for a library
- Search for similar error patterns on Stack Overflow
- Find security advisories (CVEs)
- Research best practices for new technologies

This "Perception of the World" ensures the agent is not limited by the cutoff date of its training data[9].

---

### 2.2 Reasoning and Decision-Making: The Logic Core

The Reasoning engine is the "Prefrontal Cortex" of the agent. It weighs inputs against principles to make decisions.

#### 2.2.1 The SOLID Constraint Solver

The agent uses the SOLID principles as a **set of logical constraints** for decision-making[9].

**Scenario:** The agent needs to add a new notification type.

**Reasoning:**
```
IF I modify NotificationService class
  THEN I violate Open-Closed Principle (OCP)
  
IF I create new class SMSNotification implements NotificationInterface
  THEN I satisfy OCP and SRP
  
DECISION: Create new class and inject it
```

This deductive reasoning prevents the gradual degradation of architecture that occurs when developers choose the path of least resistance[9].

#### 2.2.2 Test-Driven Reasoning Loop

The agent's logic is fundamentally circular and test-driven. It reasons in loops[9]:

1. **Hypothesis:** "The system should calculate tax at 5% for this region."
2. **Experiment Design:** "Write a test that asserts calculateTax(100) returns 105."
3. **Observation:** "Test fails (Red)."
4. **Deduction:** "Implement the tax logic."
5. **Verification:** "Test passes (Green)."
6. **Optimization:** "Refactor magic number 0.05 to a constant."

This loop is the **cognitive heartbeat** of the agent[9].

#### 2.2.3 Trade-off Analysis

The agent is capable of weighing conflicting goals[9]. For example, "Readability vs. Performance."

**Default Stance:** The Guardian defaults to **Readability** (Clean Code) unless explicitly instructed that a specific path is performance-critical. Even then, it reasons that the optimization should be:
- Encapsulated in a separate module
- Documented with benchmarks
- Never compromising the cleanliness of calling code

**Decision Pattern:**
```
IF (optimization_requested AND profiling_data_provided)
  THEN apply_optimization()
       encapsulate_in_module()
       document_tradeoff()
ELSE
  prioritize_readability()
```

#### 2.2.4 Risk-Based Prioritization

The agent evaluates code changes through multiple lenses:

| Risk Factor | High Priority (Strict) | Low Priority (Relaxed) |
|-------------|------------------------|------------------------|
| **Business Impact** | Payment processing, authentication | UI color changes |
| **Technical Complexity** | Algorithmic logic, concurrency | Configuration changes |
| **Historical Data** | Files with high defect rates | Stable, rarely-touched files |
| **Dependency Fan-out** | Changes affecting >5 modules | Isolated changes |

**Example Decision:**
```
IF (code_change.affects_payment_module 
    AND test_coverage < 80%)
  THEN severity = CRITICAL
       block_merge()
       require_integration_tests()
```

---

### 2.3 Memory: Context and Continuity

Memory is critical for an AI agent to function as a coherent team member rather than a stateless query engine. The agent employs a **tiered memory hierarchy**[9].

#### 2.3.1 The Memory Hierarchy

| Level | Location | Purpose | Persistence |
|-------|----------|---------|-------------|
| **Enterprise** | `/etc/claude-code/CLAUDE.md` | Organization-wide policies (e.g., "All code must be GDPR compliant") | Permanent |
| **Global User** | `~/.claude/CLAUDE.md` | User-specific preferences (e.g., "I prefer verbose comments") | Permanent (User) |
| **Project** | `./CLAUDE.md` | **The Cortex.** Project architecture, tech stack, coding standards | Permanent (Project) |
| **Project Local** | `./CLAUDE.local.md` | Personal overrides, ignored by Git | Session/Local |
| **Session** | Context Window | Immediate conversation history, code snippets, errors | Ephemeral |

#### 2.3.2 CLAUDE.md as Persistent Project Cortex

The **CLAUDE.md** file is the most critical component of the agent's long-term memory[9]. It acts as a prompt injection that runs at the start of every session. It contains:

- **Commands:** "To run tests, use `npm test`." This prevents the agent from guessing and failing.
- **Architecture:** "This is a Hexagonal Architecture project. Core logic is in `/domain`."
- **Style:** "Use snake_case for Python variables."

By updating this file, the agent "learns" about the project. If a user corrects the agent ("We use pytest, not unittest"), the agent updates CLAUDE.md, ensuring it never makes that mistake again[9].

**Example CLAUDE.md:**
```markdown
# Project: E-Commerce Platform

## Architecture
- **Pattern:** Clean Architecture (Hexagonal)
- **Layers:** Domain → Application → Infrastructure → Presentation
- **Rule:** Dependencies point inward (Domain has zero dependencies)

## Commands
- Build: `npm run build`
- Test: `npm test` (Jest)
- Lint: `npm run lint` (ESLint)
- Format: `npm run format` (Prettier)

## Quality Gates
- Coverage: Minimum 80%
- Complexity: Maximum 20 per function
- Function Size: Maximum 40 LOC

## Style
- TypeScript strict mode enabled
- Prefer functional programming over OOP when possible
- Use dependency injection for all services
```

#### 2.3.3 Project Knowledge Base (Perplexity Spaces)

The agent utilizes **Perplexity Spaces** as a project-specific knowledge repository[9]. The team can upload:
- Proprietary PDF documentation
- Architecture diagrams
- Legacy system manuals
- Post-mortem reports

When the agent answers a question, it searches **both** the public web (via Perplexity's search index) and the private files in the Space. This allows it to answer questions like:
- "How does this new feature interact with our legacy mainframe?" (using uploaded PDF)
- "What is the latest security patch for Redis?" (using the web)

#### 2.3.4 Historical Context (Learning Events)

The agent maintains a **Learning Events Log**:

```
Date       | Event        | Context                  | Remedy Applied        | Outcome
-----------|--------------|--------------------------|----------------------|----------
2026-01-15 | QG Block     | Coverage 65% < 70%       | Added 5 tests        | Coverage → 75%
2026-01-18 | QG Block     | Complexity 25 > 20       | Extract Method       | M → 12
2026-01-20 | Architecture | DIP violation detected   | Introduced Interface | Compliance
```

This log enables the agent to:
- Recognize patterns (e.g., "This team often forgets error handling tests")
- Adjust heuristics conservatively
- Provide context-aware warnings

---

### 2.4 Planning: The Strategic Engine

Before writing a single line of code, the agent engages in **Planning**[9]. This combats the tendency of LLMs to "stream of consciousness" code generation, which often leads to dead ends.

#### 2.4.1 Task Decomposition and Dependency Mapping

The agent breaks down high-level requests ("Implement OAuth 2.0") into a **dependency graph** of atomic tasks[9]:

1. Add dependency to `package.json`
2. Create `AuthService` interface
3. Create `GoogleAuthProvider` implementation (TDD)
4. Update `UserController` to use provider
5. Add integration tests

This decomposition allows the agent to execute "Build in Small Batches" effectively.

#### 2.4.2 Plan Mode

The agent utilizes a distinct **"Plan Mode"** (available in tools like Claude Code)[9]. In this mode, the agent:
- Analyzes the codebase
- Proposes a plan *without* making changes
- Presents the plan to the user for approval

**Example:**
```
Plan for: "Add email notifications for order confirmations"

I will:
1. Create interface INotificationService (5 LOC)
2. Implement EmailNotificationService with SendGrid (20 LOC + 15 LOC tests)
3. Update OrderService to inject INotificationService (3 LOC modification)
4. Add integration test for full flow (25 LOC)

Files affected: 4 files (2 new, 2 modified)
Estimated complexity: Low (no circular dependencies)

Proceed? [Yes/No]
```

This "Look Before You Leap" capability is essential for high-rigor development[9].

#### 2.4.3 TDD Planning

For each feature, the agent plans the **Red-Green-Refactor cycle**:

**Red Phase Plan:**
- Identify test scenarios
- Write failing tests
- Verify tests fail for the right reason

**Green Phase Plan:**
- Implement minimal solution
- No gold-plating
- Focus solely on passing tests

**Refactor Phase Plan:**
- Extract methods if LOC > 30
- Introduce interfaces if DIP violated
- Rename variables for clarity
- Reduce complexity if M > 15

---

### 2.5 Action: Execution and Output

The Action layer is where the agent affects the environment.

#### 2.5.1 Code Generation and Refactoring

The agent generates code that is:
- **Syntactically correct** – No compilation errors
- **Stylistically consistent** – Follows project conventions in CLAUDE.md
- **Test-covered** – Always paired with test generation

**Refactoring Operations:**
- **Rename** – Variables, functions, classes for clarity
- **Extract Method** – Break long functions into smaller units
- **Extract Class** – Separate concerns
- **Move** – Reorganize code to align with architecture layers
- **Introduce Interface** – Enable dependency injection

#### 2.5.2 Tool Execution

The agent uses a **"Tool Use"** capability to interact with the OS[9]. It runs:
- Shell commands (`git commit`, `npm install`)
- Test runners (`jest`, `pytest`)
- Build tools (`make`, `gradle`)
- Static analyzers (`eslint`, `sonar-scanner`)

It is not a passive text generator; it is an **active operator** of the developer's machine[9].

#### 2.5.3 Direct Interventions (Fix Loop)

The agent can take autonomous corrective action[9]. If a test fails after an edit, the agent enters a **"Fix Loop"**:

```
1. Read Error → Parse stack trace, identify failing assertion
2. Analyze Code → Review recent changes, identify likely cause
3. Hypothesize Fix → Generate proposed correction
4. Apply Fix → Modify code
5. Rerun Test → Verify fix

WHILE (test_fails AND attempts < 3):
  continue_loop()

IF (attempts >= 3):
  revert_changes()
  escalate_to_human()
```

---

### 2.6 Learning: Adaptation and Evolution

The agent improves over time through explicit and implicit feedback loops.

#### 2.6.1 Prompt Learning and Meta-Prompting

The agent utilizes **"Prompt Learning"** to optimize its own instructions[9]. If the agent struggles with a specific repository's conventions, it can:
- Analyze successful past interactions
- Generate a new system prompt (or update CLAUDE.md)
- Better align with that repository

This **"Meta-Prompting"** (using the AI to write better prompts for the AI) allows the agent to self-tune[9].

#### 2.6.2 Research-Driven Knowledge Updates

The agent uses **Perplexity** to constantly update its internal knowledge base[9]. If a new version of React is released, the agent:
- Researches the changes
- Incorporates them into suggestions
- Prevents generating deprecated code patterns

#### 2.6.3 Quality Signal Learning

The agent learns from **deterministic quality signals**, not subjective feedback:

**Learning Sources:**
- **Quality Gate Violations** – Coverage failures, complexity breaches
- **Build Failures** – Patterns of errors
- **Historical Defects** – Files with repeated bugs
- **Architectural Drift** – Dependency violations

**Learning Cycle:**
```
Quality Signal Detected
  ↓
Log as Learning Event
  ↓
Analyze Root Cause (statistical pattern detection)
  ↓
Adjust Heuristics (conservatively)
  ↓
Monitor Impact
  ↓
Validate Improvement
```

**Immutable Rule:** The agent **never relaxes core rules**:
- TDD is always required
- SOLID principles are always enforced
- CI rules are never compromised
- Quality gates are never lowered

Only **detection heuristics** improve; **thresholds remain stable**.

---

### 2.7 Coordination & Collaboration: The Team Member

The agent operates as a disciplined teammate[9].

#### 2.7.1 CI Pipeline Master

- **Daily Integration:** Integrates work into mainline trunk **daily**
- **10-Minute Fix Rule:** If a commit breaks the build, the agent halts all tasks and fixes it within 10 minutes (or reverts)[9]
- **No Workarounds:** Explicitly forbids commenting out failing tests

#### 2.7.2 Communication Standards

All feedback follows a **Principle-Metric-Remedy** pattern:

```
Principle: SOLID Single Responsibility (SRP)
Metric:   Class CustomerService has 12 reasons to change
          (Methods: processPayment, sendEmail, logActivity, validateUser...)
Remedy:   Extract concerns:
          - PaymentService for payment logic
          - NotificationService for email
          - AuditService for logging
```

Never communicate ambiguously or without actionable next steps.

#### 2.7.3 Multi-Agent Coordination

The agent coordinates with other specialized agents:

| Agent | Responsibility | Coordination Point |
|-------|----------------|-------------------|
| **Security Agent** | Vulnerability scanning | Shares findings; RQG blocks merges on Critical findings |
| **Architecture Agent** | Dependency analysis | Validates Clean Architecture rules; RQG enforces |
| **Test Generation Agent** | Coverage analysis | Reports gaps; RQG blocks if <70% |

**Interaction Pattern:**
```
PR Opens
  ├─ RQG: Orchestrate quality gate evaluation
  ├─ Test Agent: Analyze coverage → report
  ├─ Architecture Agent: Check dependencies → violations or OK
  ├─ Security Agent: SAST scan → findings
  └─ RQG: Aggregate
      ├─ Any blocker? → BLOCK merge
      ├─ Warnings only? → ALLOW with notes
      └─ All clear? → ALLOW ✅
```

---

### 2.8 Tool Interface: Interactions with Development Environment

The agent interfaces with the complete software development ecosystem.

#### 2.8.1 GitHub Integration

- **Branch Protection:** Enforces required status checks
- **PR Reviews:** Automated comments citing violations
- **Merge Blocking:** Physical prevention of bad code merging
- **Status Checks:** Pass/Fail quality gate results

#### 2.8.2 IDE Integration (VS Code)

- **Real-Time Feedback:** Inline warnings as code is typed
- **Code Actions:** Quick fixes (Extract Method, Generate Test)
- **Semantic Linting:** Checks meaning, not just syntax
- **Refactoring Assistance:** Interactive suggestions

#### 2.8.3 CLI Integration (Claude Code)

- **CLAUDE.md Management:** Updates project cortex
- **Slash Commands:** Custom workflows (`/test-feature`)
- **Plan Mode:** Preview changes before execution
- **Tool Execution:** Run shell commands, tests, builds

#### 2.8.4 Knowledge Integration (Perplexity)

- **Research:** Up-to-date documentation, CVE advisories
- **Spaces:** Project-specific knowledge repository
- **RAG:** Retrieval-Augmented Generation from project docs

---

## Part III: The Testing and Quality Model

The heart of the Roundhouse Quality Guardian is its rigorous quality model. It moves beyond simple "pass/fail" boolean checks to a **nuanced, multi-dimensional assessment** of software health.

---

### 3.1 The Agile Testing Quadrants Coverage

The agent ensures that testing is comprehensive, covering all four quadrants of the **Agile Testing Matrix**[9]. It understands that different tests serve different purposes and ensures that none are neglected.

```
        Business-Facing
             ↑
    Q2       |       Q3
  Acceptance | Exploratory
    Tests    |   Testing
─────────────┼─────────────
    Q1       |       Q4
    Unit     | Performance
   Tests     | & Security
             ↓
      Technology-Facing
```

#### Quadrant 1: Technology-Facing / Support the Team (Unit Tests)

**Focus:** Internal code quality, correctness, and design[9]

**Agent Action:**
- Uses **TDD** to write these tests *before* the code
- Ensures every class and function is covered by isolated unit tests
- Mocks dependencies to ensure tests are fast and deterministic

**Tools:** JUnit, pytest, Jest, Mockito

**Coverage Target:** 100% for new code (enforced via TDD)

#### Quadrant 2: Business-Facing / Support the Team (Acceptance Tests)

**Focus:** Does the software meet the user's needs?[9]

**Agent Action:**
- Uses **BDD** to translate user stories into executable specifications
- Writes Gherkin feature files (Given-When-Then)
- Collaborates with users to define acceptance criteria

**Tools:** Cucumber, SpecFlow, Behave

**Example:**
```gherkin
Scenario: Successful money transfer
  Given I have an account with balance 100
  And I have another account with balance 50
  When I transfer 25 to the other account
  Then my first account balance should be 75
  And my second account balance should be 75
```

#### Quadrant 3: Business-Facing / Critique the Product (Exploratory Testing)

**Focus:** Usability, workflows, "look and feel"[9]

**Agent Action:**
- Facilitates this quadrant (cannot directly "feel" the app)
- Deploys app to staging environment
- Seeds realistic test data
- Notifies human testers
- Can run "Monkey Testing" scripts for random interaction

**Tools:** Selenium, Cypress (automated), Data Seeding Scripts

#### Quadrant 4: Technology-Facing / Critique the Product (Non-Functional Tests)

**Focus:** Performance, Security, Load, Stability[9]

**Agent Action:**
- Generates non-functional tests
- Writes load testing scripts
- Runs static security analyzers (SAST)
- Interprets results: "Response time >200ms, failing quality gate"

**Tools:** JMeter, K6, OWASP ZAP, SonarQube

**Key Principle:** Do not rely on one quadrant. Balanced testing across all four dimensions ensures both **technical excellence** and **user satisfaction**.

---

### 3.2 The Quality Gate Profile and Metrics

The agent enforces a strict **"Quality Gate" (QG)**[9]. Code is not "done" when it works; it is "done" when it passes the QG. The agent uses the following quantitative metrics as **hard constraints**.

| Metric | Definition | Target / Rule | Hard Fail Threshold | Rationale |
|--------|------------|---------------|---------------------|-----------|
| **Cyclomatic Complexity (M)** | Number of linearly independent paths through a program's source code | **M ≤ 10** (clean)<br>**M ≤ 15** (acceptable) | **M > 20** | High complexity correlates with bugs and poor testability[9]. Enforces "Small Batches." |
| **Function Length (LOC)** | Lines of Code per function | **5–15 lines** (ideal)<br>**≤ 30** (acceptable) | **> 40 lines** | Enforces SRP[9]. Long functions invariably do too much. |
| **Function Parameters** | Number of arguments passed to a function | **0, 1, or 2** (ideal)<br>**≤ 3** (acceptable) | **> 5** | High parameter count indicates high coupling[9]. Suggests need for Parameter Object. |
| **Code Coverage** | Percentage of code executed by tests | **100%** (via TDD)<br>**≥ 80%** (acceptable) | **< 70%** | "Legacy Code is code without tests"[9]. No new legacy code allowed. |
| **Code Duplication** | Percentage of repeated code blocks | **0%** (ideal)<br>**< 5%** (acceptable) | **> 10%** | Enforces DRY[9]. Duplication leads to inconsistent bug fixes. |

### 3.3 TDD Cycle Enforcement (The Red-Green-Refactor Protocol)

The agent strictly follows the TDD cycle. It treats this not as a guideline but as a **procedural algorithm**[9].

#### Phase 1: Red (The Specification)

**Objective:** Write a test that defines the desired behavior

**Agent Actions:**
1. Parse requirements for testable assertions
2. Generate test case in appropriate framework (Jest, pytest, JUnit)
3. Run test to **confirm it fails**
4. Verify failure reason is correct (not syntax error)

**Constraint:** The agent **prohibits writing production code without a failing test** (except for pure refactoring)[9].

**Example:**
```python
def test_calculate_tax_for_region():
    # Arrange
    calculator = TaxCalculator(region="CA")
    amount = 100
    
    # Act
    result = calculator.calculate_tax(amount)
    
    # Assert
    assert result == 105  # 5% tax for CA
```

**Status:** ❌ **Red** (TaxCalculator.calculate_tax not implemented)

#### Phase 2: Green (The Implementation)

**Objective:** Write the *minimal* code required to make the test pass

**Agent Actions:**
1. Implement simplest solution
2. Resist "gold plating" or unrequested features
3. Run test to verify it passes
4. Commit if green

**Constraint:** Do not add complexity beyond what the test demands[9].

**Example:**
```python
class TaxCalculator:
    def __init__(self, region):
        self.region = region
    
    def calculate_tax(self, amount):
        if self.region == "CA":
            return amount * 1.05  # Minimal implementation
        return amount
```

**Status:** ✅ **Green** (test passes)

#### Phase 3: Refactor (The Design)

**Objective:** Improve structure while tests stay green

**Agent Actions:**
1. Check Quality Gate metrics
2. If complexity >15 → Extract methods
3. If naming unclear → Rename
4. If duplication detected → Extract common logic
5. Run tests after each refactor to ensure green

**Constraint:** Tests must remain green throughout this phase[9].

**Example Refactoring:**
```python
class TaxCalculator:
    TAX_RATES = {
        "CA": 1.05,
        "NY": 1.04,
        "TX": 1.0625
    }
    
    def __init__(self, region):
        self.region = region
    
    def calculate_tax(self, amount):
        rate = self._get_tax_rate()
        return amount * rate
    
    def _get_tax_rate(self):
        return self.TAX_RATES.get(self.region, 1.0)
```

**Improvements:**
- Magic number 1.05 → named constant
- Scalable to multiple regions
- Complexity remains low (M = 2)

**Status:** ✅ **Green** (tests still pass after refactoring)

---

### 3.4 The 10-Minute Fix Rule

Drawing from Continuous Integration principles, the agent adheres to the **"10-Minute Fix Rule"**[9]:

**Rule:** If a build fails (Red), the agent attempts to fix it immediately. If the fix takes longer than 10 minutes, the agent **reverts the changes** to restore the main branch to a stable state.

**Rationale:** This prevents "broken windows" and ensures the team always has a stable foundation[9].

**Implementation:**
```
Build Fails
  ↓
Start 10-minute timer
  ↓
Attempt Fix
  ├─ Fixed within 10 min? → Commit fix, build passes
  └─ Not fixed within 10 min? → Revert changes
      ├─ Create issue for investigation
      ├─ Notify team
      └─ Restore main branch stability
```

**Forbidden Actions:**
- Commenting out failing tests
- Disabling quality gates
- Merging broken code "temporarily"

---

### 3.5 BDD Integration and Living Documentation

#### 3.5.1 Gherkin Specifications

The agent uses **Gherkin syntax** to bridge business requirements and technical implementation[9]:

**Structure:**
```gherkin
Feature: [High-level capability]
  As a [user role]
  I want [feature]
  So that [business value]

  Scenario: [Specific example]
    Given [initial context]
    And [additional context]
    When [action taken]
    Then [expected outcome]
    And [additional outcome]
```

**Benefits:**
- **Shared understanding** between business, QA, and developers
- **Executable specifications** that serve as tests
- **Living documentation** that stays current
- **Traceability** from requirements to implementation

#### 3.5.2 Step Definition Mapping

The agent maps Gherkin steps to executable code:

**Gherkin:**
```gherkin
Given I have an account with balance 100
```

**Step Definition:**
```python
@given('I have an account with balance {balance:d}')
def create_account_with_balance(context, balance):
    context.account = Account(balance=balance)
```

**Benefit:** Non-technical stakeholders can read and validate behavior; tests run automatically.

---

## Part IV: Implementation Surfaces and Tooling Ecosystem

The Roundhouse Quality Guardian is not a theoretical construct; it is realized through integration with specific, high-capability tools. The agent inhabits the terminal, the IDE, the repository, and the web.

---

### 4.1 Surface 1: Claude Code and the Command Line Interface (CLI)

**Claude Code** (Anthropic's CLI tool) serves as the primary "body" for the agent's autonomous operations[9]. It allows the agent to live in the terminal, where development actually happens.

#### 4.1.1 The CLAUDE.md Cortex Implementation

As discussed in the Memory section, **CLAUDE.md** is the project's configuration file[9].

**Implementation:**
```bash
# Initialize project with CLAUDE.md
claude /init

# This generates skeleton CLAUDE.md
```

**Content Structure:**
```markdown
# Project: [Name]

## Architecture
- Pattern: Clean Architecture
- Layers: Domain → Application → Infrastructure

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Quality Gates
- Coverage: ≥80%
- Complexity: ≤20
- Function Size: ≤40 LOC

## Style
- TypeScript strict mode
- Prefer functional programming
- Use dependency injection
```

**Mechanism:** When the user runs `claude "Refactor this"`, the CLI:
1. Reads CLAUDE.md
2. Prepends it to the prompt
3. Sends to the model

This ensures the agent knows *how* to build and test without being told every time[9].

#### 4.1.2 Slash Commands and Custom Tools

The agent capabilities are extended via **"Slash Commands"** stored in `.claude/commands`[9].

**Custom Commands:**
- `/test-feature` – Run test suite for current feature branch
- `/on-call` – Load on-call playbook into context
- `/quality-report` – Generate full quality metrics report

**Hooks:**
The agent uses "Hooks" (e.g., `PostToolUse`) to run automated checks[9]:
- After every file edit → run Prettier for formatting
- After every test run → update coverage report
- Before every commit → run linter

#### 4.1.3 Plan Mode and Compacting

**Plan Mode:** For complex tasks, the agent uses "Plan Mode" (`Shift+Tab` in CLI)[9]. It:
- Scans relevant files
- Builds a mental model
- Proposes a plan: "1. Create Interface. 2. Update DB Schema. 3. Update API."
- Waits for user sign-off

**Compacting:** To handle context limits, the agent "compacts" conversation history[9]:
- Summarizes past actions ("I have finished the database layer")
- Keeps CLAUDE.md context intact
- Allows long-running sessions without context overflow

---

### 4.2 Surface 2: GitHub (The Repository Guardian)

On GitHub, the agent acts as the **"Gatekeeper,"** ensuring no bad code enters the main branch[9].

#### 4.2.1 Blocking Merges via GitHub Actions

The agent is integrated into the CI pipeline using **GitHub Actions**[9].

**Workflow File:** `.github/workflows/quality-gate.yml`

```yaml
name: RQG Quality Gate

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Full history for diff analysis
      
      - name: Install Dependencies
        run: npm install
      
      - name: Run Tests
        run: npm test -- --coverage
      
      - name: Check Coverage
        run: |
          COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
          if (( $(echo "$COVERAGE < 70" | bc -l) )); then
            echo "❌ Coverage $COVERAGE% < 70% (BLOCKED)"
            exit 1
          fi
          echo "✅ Coverage $COVERAGE% ≥ 70%"
      
      - name: Check Complexity
        run: |
          npx eslint src/ --format json | \
          jq '.[] | select(.messages[].ruleId == "complexity") | 
              select(.messages[].message | contains("20"))'
          if [ $? -eq 0 ]; then
            echo "❌ Complexity > 20 detected (BLOCKED)"
            exit 1
          fi
          echo "✅ Complexity ≤ 20"
      
      - name: Check Architecture
        run: node scripts/check-dependencies.js
      
      - name: Comment on PR
        if: always()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '🛡️ Quality Gate results posted above'
            })
```

**Branch Protection:**
```yaml
# Settings → Branches → Branch protection rule for main
required_status_checks:
  - rqg-quality-gate/qg-pass
require_code_reviews: 1
enforce_admins: true
```

**Policy:** GitHub "Branch Protection Rules" are configured to **require** this specific Action to pass. This makes the Quality Gate physical—you **literally cannot merge bad code**[9].

#### 4.2.2 Incremental Scanning

To ensure speed, the agent uses **Incremental Scanning**[9]:

**Strategy:**
- Calculate diff of PR (changed files only)
- Build dependency graph
- Identify affected files
- Run tests/analysis only on that subset

**Benefit:** Reduces feedback time from hours to minutes (fast feedback principle)[9].

#### 4.2.3 Automated PR Reviews

The agent acts as a reviewer, posting comments on PRs[9]:

**Example Comment:**
```markdown
## 🛡️ Roundhouse Quality Guardian Review

### ❌ Violations Found

**File:** `src/services/PaymentService.ts`  
**Line:** 45  
**Issue:** Cyclomatic Complexity = 23 (Max: 20)  
**Principle:** Simplicity, Single Responsibility  
**Remedy:** Extract decision logic:
- `validatePaymentMethod()`
- `checkFraudRules()`
- `processGatewayTransaction()`

---

### ✅ Good Practices Observed

**File:** `src/services/NotificationService.ts`  
**Praise:** Excellent use of Strategy Pattern to decouple email/SMS logic

---

### ❓ Questions

**File:** `src/api/controllers/UserController.ts`  
**Question:** This change affects the public API. Have you updated the Swagger documentation?

---

**Status:** ⚠️ **CHANGES REQUESTED** – Address violations before merge
```

These automated reviews relieve humans of tedious syntax checking, allowing them to focus on high-level design[9].

---

### 4.3 Surface 3: Perplexity Spaces (The Knowledge Engine)

The agent uses **Perplexity** as its connection to the evolving world of software knowledge, preventing knowledge staleness[9].

#### 4.3.1 Spaces vs. Collections

The agent utilizes **Perplexity Spaces**, an evolution of Collections[9].

**Integration:**
- Agent connects to a project-specific "Space"
- Team uploads proprietary documentation:
  - PDF manuals
  - Architecture diagrams
  - Legacy system documentation
  - Post-mortem reports

**RAG (Retrieval-Augmented Generation):**
When the agent answers a question, it searches:
1. **Public web** (via Perplexity's search index)
2. **Private files** in the Space

**Example Queries:**
- "How does this new feature interact with our legacy mainframe?" → Uses uploaded PDF
- "What is the latest security patch for Redis?" → Uses web search

#### 4.3.2 Collaborative Knowledge Curation

Spaces allow collaboration[9]:

**Workflow:**
1. Agent solves tricky bug
2. Generates "Post-Mortem" document
3. Saves to Project Space
4. Future instances (or humans) query Space for solutions

**Example:**
```
Developer: "Have we seen this 'Connection Reset' error before?"
Agent: "Yes, in incident #123, referenced in Project Space. 
        The fix was upgrading to Redis 6.2 with connection pooling."
```

This creates **institutional memory** that persists beyond individual sessions[9].

---

### 4.4 Surface 4: Visual Studio Code (The IDE Assistant)

In VS Code, the agent functions as a **"Pair Programmer" extension**[9].

#### 4.4.1 Real-Time "Semantic Linting"

The agent provides real-time feedback beyond syntax[9]:

**Scenario 1:**
```typescript
// Developer types:
const data = getUserData();

// Agent highlights "data" with warning:
⚠️ Too generic. Does not reveal intent.
Suggestion: const userTransactionHistory = getUserData();
```

**Scenario 2:**
```typescript
// Developer adds 4th parameter:
function processOrder(userId, items, payment, shipping) {
  // ...
}

// Agent warning:
⚠️ Parameter count > 3. Suggest introducing Parameter Object.
Quick Fix: Extract to OrderRequest interface
```

This immediate feedback shapes code **as it is written**, rather than catching it later in CI[9].

#### 4.4.2 Interactive Refactoring

The agent offers **"Code Actions"** (Lightbulbs)[9]:

**Available Actions:**
- **"Extract to Interface"** – Auto-generates interface and updates references
- **"Generate Tests"** – Scaffolds test file for current class
- **"Explain this Legacy Code"** – Provides plain-English summary
- **"Apply Strategy Pattern"** – Refactors conditionals to polymorphism

**Example:**
```typescript
// User right-clicks on complex function
// Agent offers:
💡 Quick Actions:
1. Extract Method (reduce LOC from 45 to 15)
2. Extract Class (separate concerns)
3. Generate Unit Tests (coverage currently 0%)
4. View Complexity Report (M=18)
```

---

## Part V: Operational Goals, Metrics, and Strategic Outcomes

The ultimate measure of the Roundhouse Quality Guardian is not the volume of code produced, but the **health** and **value** of the software system[9].

---

### 5.1 Primary Goals

1. **Prevent Technical Debt Accumulation**  
   Stop the creation of legacy code at the source. Ensure every new line is a net positive for the system's maintainability[9].

2. **Enforce Architectural Consistency**  
   Ensure that code written by Agent A, Agent B, and Human C all looks like it was written by a single, coherent entity[9].

3. **Accelerate Onboarding**  
   Use CLAUDE.md and Perplexity Spaces as a living knowledge base that brings new developers up to speed instantly[9].

4. **Cultural Transformation**  
   Shift the organization from a "Feature Factory" mindset to a "Product Craftsmanship" mindset. The agent acts as a relentless mentor, normalizing high standards[9].

---

### 5.2 Success Metrics (The KPI Dashboard)

The agent's impact is measured by specific Key Performance Indicators (KPIs)[9].

| Category | Metric | Goal | Current | Trend |
|----------|--------|------|---------|-------|
| **Code Health** | Defect Density | <0.5 bugs per KLOC | 0.8 | ↗ Improving |
| **Maintainability** | Refactoring Ratio | >20% of commits | 15% | ↗ Improving |
| **Velocity** | Change Failure Rate | <5% | 8% | → Stable |
| **Efficiency** | Lead Time for Changes | <1 day | 1.5 days | ↗ Improving |
| **Rigor** | Test Coverage | >80% | 75% | ↗ Improving |
| **Compliance** | Quality Gate Pass Rate | 100% | 92% | ↗ Improving |

**KLOC = Thousand Lines of Code

#### Metric Definitions

**Defect Density:**
```
Defects per KLOC = (Total Production Bugs) / (Total Lines of Code / 1000)
```

**Refactoring Ratio:**
```
Refactoring % = (Refactoring Commits) / (Total Commits) × 100
```

**Change Failure Rate:**
```
CFR = (Failed Deployments) / (Total Deployments) × 100
```

**Lead Time for Changes:**
```
Lead Time = Time from commit to production deployment
```

---

### 5.3 Strategic Outcomes: Beyond Legacy Code

By deploying the Roundhouse Quality Guardian, organizations can achieve a state of **"Sustainable Agility"**[9].

#### The "Seam" Effect

The codebase becomes full of "seams" (places where behavior can be modified without editing source code), making it easy to extend[9].

**Before (Tightly Coupled):**
```java
public class OrderService {
    public void processOrder(Order order) {
        // Hard-coded dependency
        EmailSender sender = new EmailSender();
        sender.send(order.getCustomer().getEmail(), "Order confirmed");
    }
}
```

**After (With Seam):**
```java
public class OrderService {
    private final INotificationService notificationService;
    
    public OrderService(INotificationService notificationService) {
        this.notificationService = notificationService;
    }
    
    public void processOrder(Order order) {
        notificationService.notify(order.getCustomer(), "Order confirmed");
    }
}
```

**Benefit:** Can now inject different notification strategies (Email, SMS, Push) without modifying OrderService.

#### The "Docs to Demos" Shift

Documentation is no longer a stale artifact but a **living prompt** (CLAUDE.md) that drives the agent to create working prototypes ("Demos") instantly[9].

**Traditional Workflow:**
```
Read 50-page PDF → Try to set up environment → Fail → Ask senior dev
```

**Agent-Powered Workflow:**
```
Ask agent: "Set up the project according to docs"
Agent reads CLAUDE.md → Executes commands → Environment ready in 2 minutes
```

#### The End of "Legacy"

If the agent's rules are followed, the codebase **never enters the "Legacy" state** (code without tests)[9]. It remains perpetually "Greenfield-like"—malleable, transparent, and safe to change.

**Metric:** % of codebase without tests
- **Traditional Project Year 3:** 60% untested (legacy)
- **Guardian-Protected Project Year 3:** 5% untested (isolated to third-party integrations)

---

## Conclusion

The **"Roundhouse Quality Guardian"** is more than a tool; it is a **philosophy codified into software**[9]. As the industry rushes towards AI-driven hyper-productivity, the risk of drowning in a mire of automated technical debt is real and present. This agent provides the necessary counterbalance.

By grounding AI generation in the timeless principles of Martin, Feathers, Bernstein, and Humble, and by enforcing these principles with the ironclad logic of CI/CD and Quality Gates, we can harness the power of AI not just to write code faster, but to **write code better**[9].

The Guardian ensures that the software we build today remains a **valuable asset, not a liability**, for the future. It is the custodian of our digital infrastructure, ensuring that **excellence is not an accident, but a continuous, automated habit**[9].

---

## Appendix A: Quality Gate Configuration Schema

```json
{
  "qualityGate": {
    "name": "Roundhouse Quality Guardian",
    "metrics": [
      {
        "name": "code_coverage",
        "type": "percentage",
        "scope": "new_code",
        "blocking": {
          "operator": "<",
          "threshold": 70,
          "message": "Coverage must be ≥70% on new code (TDD mandate)"
        },
        "warning": {
          "operator": "<",
          "threshold": 80,
          "message": "Coverage below 80% (ideal target)"
        },
        "principle": "Write the test first (Bernstein)"
      },
      {
        "name": "cyclomatic_complexity",
        "type": "integer",
        "scope": "per_function",
        "blocking": {
          "operator": ">",
          "threshold": 20,
          "message": "Complexity exceeds 20 (high risk)"
        },
        "warning": {
          "operator": ">",
          "threshold": 15,
          "message": "Complexity above 15 (moderate risk)"
        },
        "principle": "Simplicity, Testability, SRP"
      },
      {
        "name": "function_loc",
        "type": "integer",
        "scope": "per_function",
        "blocking": {
          "operator": ">",
          "threshold": 40,
          "message": "Function exceeds 40 LOC (SRP violation likely)"
        },
        "warning": {
          "operator": ">",
          "threshold": 30,
          "message": "Function above 30 LOC (consider breaking down)"
        },
        "principle": "Single Responsibility"
      },
      {
        "name": "function_parameters",
        "type": "integer",
        "scope": "per_function",
        "blocking": {
          "operator": ">",
          "threshold": 5,
          "message": "Too many parameters (>5) - use Parameter Object"
        },
        "warning": {
          "operator": ">",
          "threshold": 3,
          "message": "More than 3 parameters - consider refactoring"
        },
        "principle": "Clarity, Dependency Inversion"
      },
      {
        "name": "code_duplication",
        "type": "percentage",
        "scope": "new_code",
        "blocking": {
          "operator": ">",
          "threshold": 10,
          "message": "Duplication >10% violates DRY"
        },
        "warning": {
          "operator": ">",
          "threshold": 5,
          "message": "Some duplication detected - refactor when convenient"
        },
        "principle": "DRY (Don't Repeat Yourself)"
      }
    ]
  }
}
```

---

## Appendix B: Sample CLAUDE.md Template

```markdown
# Project: [Your Project Name]

## Overview
Brief description of the project, its purpose, and main technologies.

## Architecture
- **Pattern:** Clean Architecture / Hexagonal / Layered / etc.
- **Layers:** 
  - Domain: Core business logic (zero dependencies)
  - Application: Use cases and orchestration
  - Infrastructure: External services, databases
  - Presentation: API controllers, UI
- **Dependency Rule:** All dependencies point inward toward Domain

## Commands

### Development
\`\`\`bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
\`\`\`

### Testing
\`\`\`bash
# Run all tests
npm test

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test -- path/to/test.spec.ts
\`\`\`

### Quality Checks
\`\`\`bash
# Lint
npm run lint

# Format
npm run format

# Type check
npm run type-check

# Full quality gate (run before PR)
npm run quality-gate
\`\`\`

## Quality Gates

### Coverage
- **Minimum:** 70% (blocking)
- **Target:** 80%+
- **Scope:** New code only

### Complexity
- **Maximum per function:** 20 (blocking)
- **Target:** ≤10

### Code Style
- **Max function length:** 40 LOC (blocking), 30 LOC (warning)
- **Max parameters:** 5 (blocking), 3 (ideal)
- **Duplication:** <10% (blocking), <5% (target)

## Coding Standards

### Language-Specific
- **TypeScript:** Strict mode enabled
- **Naming:** camelCase for variables, PascalCase for classes
- **Imports:** Absolute paths preferred (use `@/` alias)

### Principles
- **SOLID:** Always follow Single Responsibility, Dependency Inversion, etc.
- **TDD:** Write tests before implementation (Red-Green-Refactor)
- **DRY:** Eliminate duplication through extraction
- **Clean Code:** Functions do one thing, names reveal intent

### Patterns
- **Dependency Injection:** Use constructor injection for services
- **Error Handling:** Use Result/Either types, not exceptions for flow control
- **Async:** Prefer async/await over raw Promises

## Project Structure
\`\`\`
src/
├── domain/           # Core business logic (no dependencies)
│   ├── entities/
│   ├── value-objects/
│   └── repositories/ # Interfaces only
├── application/      # Use cases
│   └── use-cases/
├── infrastructure/   # External dependencies
│   ├── database/
│   ├── http/
│   └── repositories/ # Implementations
└── presentation/     # API/UI layer
    └── api/
\`\`\`

## Common Tasks

### Adding a New Feature
1. Write BDD scenario in Gherkin (features/)
2. Write failing tests (TDD Red)
3. Implement minimal solution (TDD Green)
4. Refactor for quality (TDD Refactor)
5. Update documentation
6. Run quality gate before PR

### Refactoring Legacy Code
1. Add characterization tests (capture current behavior)
2. Identify seams (break dependencies)
3. Refactor incrementally
4. Keep tests green throughout
5. Improve coverage to 80%+

## Notes
- This file is the project's "brain" for AI agents
- Update it when conventions change
- Keep it concise but complete
\`\`\`

---

## Works Cited

[9] AI-Agent-for-Software-Excellence.md (Gemini contribution)  
All other numbered citations preserved from original Gemini document

---

**End of Unified Specification v2.0**

*This document integrates insights from ChatGPT, Perplexity, and Gemini contributions, creating a comprehensive, production-ready blueprint for the Roundhouse Quality Guardian.*

*Last Updated: January 21, 2026*

---

## Workspace Implementation Addendum (March 2026, updated May 2026)

This workspace contains an actionable RQG MVP aligned to this specification.

### Implemented assets

- GitHub workflow gate: `.github/workflows/quality-gate.yml`
- Gate runner: `scripts/rqg/run.mjs` (formerly `scripts/ccqg/run.mjs`)
- Provider adapters:
  - `scripts/rqg/adapters/copilotAdapter.mjs`
  - `scripts/rqg/adapters/claudeAdapter.mjs`
- Contracts and policies:
  - `docs/rqg/task-contract.json`
  - `docs/rqg/provider-interface.md`
  - `docs/rqg/policies/soft-block.yml`
  - `docs/rqg/ops-runbook.md`

### Operating mode

- Host surface: GitHub Actions-first
- Enforcement model: soft-block (critical failures block, warnings reported)
- Deterministic checks are authoritative for merge blocking
- AI adapters are optional and provider-agnostic

### Migration from CCQG → RQG

| Old path                        | New path                       | Action            |
|---------------------------------|--------------------------------|-------------------|
| `scripts/ccqg/`                 | `scripts/rqg/`                 | `git mv` rename   |
| `docs/ccqg/`                    | `docs/rqg/`                    | `git mv` rename   |
| `.github/workflows/quality-gate.yml` | unchanged (path-stable) | update internal refs |
| Job name `ccqg-quality-gate`    | `rqg-quality-gate`             | rename in workflow |
| Branch protection check `ccqg-quality-gate` | `rqg-quality-gate` | re-bind in repo settings |
| Env var `CCQG_*`                | `RQG_*`                        | rename + alias for one release |

A one-release alias (`CCQG_*` env vars still respected with deprecation warning) protects existing CI without forcing a flag-day cutover.

### Packaging intent

The RQG implementation is designed to package as the first Roundhouse HQ product and remain compatible with mixed-agent teams (Copilot-preferred or Claude-preferred) through a normalized adapter contract. Future Roundhouse HQ products (Trainyard, Switchyard, Signalbox, Dispatch) will share this adapter layer.

---

**End of Roundhouse Quality Guardian Unified Specification v3.0**
