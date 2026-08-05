**1. Catchy Topic Title**

**Navigating the \"Black Box\": Human-in-the-Loop & Automated Testing
for AI Compliance in Finance**

**2. Topic Description**

The integration of Generative AI (GenAI) into the financial industry
presents unprecedented opportunities, but also a complex landscape of
regulatory compliance. FINRA and SEC guidance clearly state that
existing rules, from supervision and communication standards to
recordkeeping and ethical conduct, fully apply to AI-generated
activities. This session will delve into how software testing,
particularly through human-in-the-loop (HITL) and robust test automation
strategies, becomes indispensable for financial firms to meet these
stringent control requirements. We\'ll explore the critical aspects of
the AI lifecycle, from data preparation and model training to deployment
and ongoing monitoring and demonstrate how a disciplined approach to
quality assurance can ensure compliance.

We will cover the \"technology-neutral\" stance of regulators,
emphasizing that firms are fully responsible for AI outputs, regardless
of their origin. This necessitates rigorous validation processes, moving
beyond traditional software testing to address AI-specific risks like
data bias, model explainability, and the potential for unintended
outcomes. Attendees will learn how to implement effective HITL
strategies to review and approve AI-generated content, especially
customer communications, ensuring adherence to FINRA Rule 2210
(Communications with the Public) and preventing misleading claims.
Furthermore, we\'ll discuss how test automation can be leveraged to
continuously monitor AI model performance, detect drift, and verify
compliance with defined benchmarks and ethical guidelines. This includes
automating checks for data integrity, bias detection in training data,
and validating AI outputs for accuracy and fairness.

Drawing parallels from FDA\'s 21 CFR Part 11, we\'ll highlight the
importance of traceability and auditability in AI systems, showing how
robust testing practices contribute to maintaining detailed audit trails
of AI model lifecycles and linking AI outputs to human oversight and
approvals. We will also explore how Agile methodologies can be adapted
to bake compliance checkpoints into every stage of the AI development
lifecycle. By treating regulatory requirements as explicit \"user
stories\" and incorporating compliance-related non-functional
requirements and test cases into sprint planning, teams can proactively
build AI systems that are compliant by design. This session will provide
actionable insights for test automation engineers, QA professionals, and
developers on how to design and implement testing frameworks that not
only assure the quality and reliability of GenAI but also serve as
verifiable evidence of regulatory adherence, ultimately safeguarding
firms against potential enforcement actions and fostering trust in
AI-driven financial services.

**3. Topic Takeaways**

-   **Understanding Regulatory Expectations for AI:** Participants will
    gain a clear understanding of how existing FINRA and SEC rules, such
    as those related to supervision (FINRA Rule 3110), communications
    (FINRA Rule 2210), recordkeeping (FINRA Rule 4510 series, SEC Rule
    17a-4), and ethical conduct (FINRA Rule 2110/2010), apply directly
    to Generative AI use in finance.

-   **Implementing Human-in-the-Loop (HITL) Testing for AI Outputs:**
    Attendees will learn practical strategies for incorporating human
    review and approval into the AI output validation process,
    particularly for customer-facing communications. This includes
    understanding the need for human oversight to ensure AI-generated
    content is fair, balanced, and not misleading, and how to set up
    processes for reviewing and editing AI drafts before publication.

-   **Leveraging Test Automation for Continuous AI Compliance:** The
    session will provide insights into designing and implementing
    automated testing frameworks to monitor AI model performance, detect
    data drift, and ensure ongoing compliance. This includes using
    automation for validating training data for biases, verifying model
    outputs against performance benchmarks, and ensuring adherence to
    privacy and security protocols throughout the AI lifecycle.

-   **Establishing Traceability and Auditability in AI Systems:**
    Participants will discover how to build traceability from regulatory
    requirements to test cases and evidence, and how to maintain
    detailed audit trails of AI model lifecycles. This includes
    documenting model training, deployment approvals, and changes,
    drawing parallels to established frameworks like FDA\'s 21 CFR Part
    11 to ensure the integrity and reliability of AI-generated records.

-   **Integrating Compliance into Agile AI Development:** The
    presentation will demonstrate how to embed regulatory compliance as
    a core component of Agile development methodologies for AI. This
    involves treating compliance requirements as explicit \"user
    stories\" or Non-Functional Requirements (NFRs), creating specific
    test cases for these requirements, and integrating compliance
    sign-offs into release planning and sprint reviews.

-   **Addressing Data Privacy and Bias in AI Training:** Attendees will
    learn the critical importance of data governance in AI, including
    strategies for ensuring data quality, integrity, and appropriate
    use. This involves understanding how to review and curate training
    data to mitigate bias, protect personally identifiable information
    (PII) in accordance with SEC Regulation S-P and the Red Flags Rule,
    and implement cybersecurity policies for third-party AI solutions.

**4. Outline**

**I. Introduction: The Regulatory Imperative for AI in Finance (10
min)** A. Generative AI\'s transformative potential and associated risks
in financial services.

B. FINRA and SEC\'s \"technology-neutral\" approach: existing rules
apply to AI.

C. Core regulatory obligations in the AI context: supervision,
communications, recordkeeping, ethical conduct.

D. The heightened need for robust controls and why testing is paramount.

**II. Regulatory Landscape and Key Compliance Areas for AI (15 min)** A.
**Supervision, Governance, and Internal Policies (FINRA Rule 3110):** 1.
Governing AI models as rigorously as human employees or conventional
technology.

2\. Establishing enterprise-level AI governance programs (inventory,
risk classification, oversight).

3\. Defining \"AI\" internally and vendor management for third-party
solutions.

B. **Data Preparation and Privacy Controls (SEC Reg S-P, Reg S-ID):** 1.
Importance of data governance for AI applications.

2\. Addressing biased or unrepresentative training data and data
quality.

3\. Protecting customer PII: anonymization, encryption, consent.

4\. Preventing unauthorized access and data leakage; cybersecurity
policies.

C. **Model Training, Testing Rigor, and Explainability:**

1\. Comprehensive model risk management framework.

2\. Rigorous testing and validation processes for AI models.

3\. The \"black box\" problem and the demand for AI explainability.

4\. Techniques for explainability (documentation, sensitivity testing).

**III. Testing Strategies for AI Compliance: Human-in-the-Loop &
Automation (25 min)**

A. **AI Output Validation and Communication Compliance (FINRA Rule
2210):**

1\. Firms\' full responsibility for AI-generated communications.

2\. Application of content standards (no false/exaggerated claims,
material omissions).

3\. **Human-in-the-Loop (HITL) Testing:** a. Necessity of human review
and approval for AI-driven communications.

b\. Policies prohibiting fully automated customer messaging.

c\. Supervision of AI chatbot interactions and record retention (FINRA
Rule 4511, SEC Rule 17a-4).

d\. Classifying AI communications (correspondence vs. retail
communications).

B. **Ongoing Monitoring, Auditing, and Reporting Duties:**

1\. Continuous monitoring of AI model performance (drift, accuracy,
bias).

2\. Setting performance benchmarks and alert mechanisms.

3\. Human oversight and guardrails for autonomous AI (e.g., trading
algorithms).

4\. Reporting AI-related incidents (FINRA Rule 4530, Reg S-ID).

5\. Addressing AI-driven conflicts of interest (SEC proposal).

C. **Traceability and Auditability: Lessons from FDA 21 CFR Part 11:**
1. Concept of ensuring accuracy, traceability, reliability, and
integrity of electronic records.

2\. Maintaining detailed audit trails of AI model lifecycle (training
data, approvals, changes).

3\. Tracing AI outputs back to model versions and inputs.

4\. Accountability by identifiable individuals for AI processes.

5\. Lifecycle documentation, validation, and change control procedures
for AI systems.

6\. The intersection with SEC 17a-4/FINRA 4510 rules for recordkeeping.

**IV. QA Controls and Agile Practices for AI Compliance (15 min)** A.
**Baking Compliance into the SDLC:** 1. Treating regulatory requirements
as explicit \"user stories\" or Non-Functional Requirements (NFRs).

2\. Creating specific test cases for compliance requirements.

3\. Traceability from regulatory requirement → test case → evidence
(e.g., using test management tools).

B. **Agile Release Planning and Compliance Sign-offs:** 1. Integrating
compliance review into release cycles.

2\. Prioritizing model testing and documentation in sprint planning.

3\. \"Compliance Demos\" and integrating regulatory criteria into
\"definition of done.\"

C. **Work Policies and Continuous QA for AI:** 1. Establishing clear
internal policies for AI use (e.g., data restrictions, peer-review).

2\. Integrating model risk assessment checklists into workflows.

3\. Automated tests for ongoing monitoring of AI in production (drift
detection, output quality).

4\. Building a continuous compliance feedback loop.

**V. Conclusion: Building a Robust AI Lifecycle Management Program (5
min)** A. Recap of key themes: testing rigor, traceability, monitoring,
explainability, governance.

B. Achieving innovative AI solutions while meeting regulatory
expectations.

C. Future-proofing organizations for evolving AI regulations.
