# CognOS Design Tenets

*Immutable engineering principles inherited by every CognOS repository.*
*Version 1.0 — July 2026*

---

## Purpose

Design tenets are not recommendations. They are engineering laws.

They represent the accumulated reasoning of the CognOS Ecosystem about how good systems are built and how they survive over time. They were not chosen arbitrarily — each one reflects a specific failure mode that the architecture is designed to prevent.

When a technical decision conflicts with a tenet, the tenet wins.
If you believe a tenet should be changed, open a discussion and propose an ADR.
Tenets are not changed through exceptions — they are changed through explicit, documented governance.

---

## The Tenets

---

### T-01 — Knowledge Before Code

> *Document it before you build it.*

Every module, feature, architectural decision, and interface must be documented before it is implemented. Documentation is not created to explain code that already exists — it is created to define what should exist and why.

**Rationale:** Code written without documented intent becomes opaque. Opaque code cannot be safely modified, extended, or replaced. Knowledge encoded only in code is knowledge that dies when the code is rewritten.

**Implications:**
- No pull request introducing new behavior is accepted without prior documentation
- Module contracts precede module implementations
- ADRs precede architectural changes

**Violation:** Writing code first and adding documentation as an afterthought.

---

### T-02 — Documentation is a First-Class Artifact

> *A document is not a comment. It is a deliverable.*

Documentation has the same status as code in this ecosystem. It is reviewed, versioned, maintained, and held to quality standards. A system with complete code and incomplete documentation is an incomplete system.

**Rationale:** Documentation degrades faster than code if it is not treated as a primary artifact. The moment documentation is treated as optional, it becomes untrustworthy.

**Implications:**
- Documentation has its own review process
- Outdated documentation is treated as a defect
- Documentation is listed as a deliverable in every phase of the roadmap

**Violation:** Treating documentation as a secondary artifact that can be deferred or skipped.

---

### T-03 — Architecture Before Implementation

> *Understand the structure before building the pieces.*

Architectural decisions are made and documented before implementation begins. Implementation that has not been preceded by explicit architectural thinking is speculation in code.

**Rationale:** Implementation decisions made without architectural context create local optimizations that are globally incoherent. Fixing architecture after the fact is exponentially more expensive than defining it upfront.

**Implications:**
- Phase 1 (Architecture) is complete before Phase 2 (Prototype) begins
- Every ADR is approved before implementation of the affected system begins
- No module is implemented without a completed module contract

**Violation:** Beginning implementation while architectural questions remain unresolved.

---

### T-04 — Human Accountability

> *AI amplifies. Humans decide.*

Every decision produced by a CognOS system is a recommendation to a human, not a command. The operator retains full authority and full responsibility for every operational decision. No CognOS system operates autonomously in a way that removes human accountability from the outcome.

**Rationale:** AI systems optimize for measurable proxies, not true goals. They lack context, values, and the ability to bear consequences. Human accountability is not a limitation — it is the correct boundary between tool and decision-maker.

**Implications:**
- Every output of the Opportunity Intelligence Engine must be a ranked recommendation with reasoning, not an instruction
- Every automated behavior must be auditable and reversible by the operator
- The voice interface always makes clear that the system is offering a recommendation, not a directive

**Violation:** Designing a system flow where the AI makes a decision without presenting it to the operator for confirmation.

---

### T-05 — Voice First

> *Design for the field, not the office.*

Every CognOS Vertical Module is designed to be fully operational through voice interaction. Screen-dependent interfaces are secondary. A mobile operator in motion, under pressure, without hands free, must be able to use the system effectively.

**Rationale:** The primary user of CognOS-Eisman is a mobile operator. Mobile operators cannot safely interact with dashboards while working. Voice is the only interface that does not compete with the physical demands of the job.

**Implications:**
- Every Decision output must be speakable — no tables, no complex formatting
- Every input pathway must have a voice-equivalent
- Voice interaction is tested before screen interaction is considered complete

**Violation:** Designing features that are only accessible through a visual interface.

---

### T-06 — Model Agnostic

> *Define what AI must do, not which AI must do it.*

No CognOS system may depend on a single AI provider, model, or API. AI capabilities are specified as interfaces. Specific models implement those interfaces. The system must function if any single model is replaced.

**Rationale:** The AI landscape changes rapidly. Models are deprecated, APIs change, providers raise prices or change terms. Lock-in to a single provider is a systemic fragility that compounds over time.

**Implications:**
- AI provider integrations are always wrapped in an abstraction layer
- Multiple providers are tested for each AI capability
- ADR required before using any provider-specific feature that has no equivalent elsewhere

**Violation:** Writing code that imports a specific AI provider's SDK directly into a module's business logic without an abstraction layer.

---

### T-07 — Modular by Default

> *Every capability belongs to a module.*

No shared behavior exists outside of a module. No functionality is implemented in a way that couples two modules together. Modules interact exclusively through defined interfaces, not through shared state or direct calls to each other's internals.

**Rationale:** Coupling is the primary source of long-term architectural fragility. A system where modules depend on each other's implementations cannot have any component safely replaced or upgraded in isolation.

**Implications:**
- Shared utilities live in `src/` with explicit interfaces
- No module imports another module's internal implementation
- Every module can be developed, tested, and deployed independently

**Violation:** A module directly reading the internal state of another module, or two modules sharing a database table without a defined interface.

---

### T-08 — Simplicity Over Complexity

> *If two approaches achieve the same result, the simpler one is correct.*

Complexity that does not serve a documented requirement is a defect. The temptation to over-engineer is treated as a design smell. Solutions are evaluated not only for what they enable, but for what burden they impose on future maintainers.

**Rationale:** Complexity accumulates. Every unnecessary abstraction, every premature optimization, every fashionable pattern that serves no current need adds cognitive overhead that compounds. Simplicity is the only gift you can give to future engineers.

**Implications:**
- New abstractions require a documented justification
- Performance optimizations require a measured problem before being introduced
- Dependency additions require an ADR or explicit documentation of necessity

**Violation:** Introducing a new framework or abstraction layer because it is technically interesting, without a documented requirement that it solves.

---

### T-09 — Everything Evolves

> *Design for change, not for permanence.*

No component of a CognOS system is expected to be permanent. Modules will be replaced. Models will change. Frameworks will expire. The architecture is designed to accommodate evolution without requiring reconstruction.

**Rationale:** Software that cannot evolve is software that decays. The modular architecture, the interface definitions, and the ADR process all exist to make evolution safe and traceable.

**Implications:**
- Interfaces are designed to be stable even when implementations change
- ADRs record the reasoning behind current decisions, making future supersession possible with context
- No module is "the only place" where a critical capability lives

**Violation:** Designing a system component that cannot be replaced without modifying other components.

---

### T-10 — Every Decision Must Be Explainable

> *If you cannot explain why, you should not have decided.*

Every significant decision — architectural, technical, operational — must be explainable to someone who was not present when it was made. This applies to code, configuration, module design, and every AI-generated recommendation.

**Rationale:** Unexplainable decisions cannot be reviewed, audited, challenged, or improved. A system full of decisions that "just work" becomes a system that nobody understands, and that eventually fails in ways nobody can diagnose.

**Implications:**
- ADRs document reasoning, not just conclusions
- AI recommendation outputs include a rationale field
- Code comments explain WHY, not WHAT

**Violation:** An ADR that says "we chose X" without explaining why X was chosen over its alternatives.

---

### T-11 — Every Module Must Be Replaceable

> *No module is irreplaceable. Design accordingly.*

Every module is designed and documented with the assumption that it will eventually be replaced — by a better implementation, a different provider, a changed requirement, or a superior approach. The module's interface, not its implementation, is the permanent artifact.

**Rationale:** Irreplaceable components become technical debt. They cannot be upgraded, cannot be improved without risk, and eventually hold the entire system hostage. Replaceability is a design requirement, not an aspiration.

**Implications:**
- Module contracts (interfaces) are versioned separately from module implementations
- Replacement is a documented scenario in every module's architecture plan
- No module implementation is allowed to become a de facto standard that other modules depend on

**Violation:** A module implementation that is referenced directly by three other modules, making it impossible to replace without a cascade of changes.

---

### T-12 — Knowledge is Permanent. Code is Temporary.

> *Invest in what lasts.*

Code written today will be refactored, replaced, or deleted. Documentation that clearly explains why a system was designed the way it was will remain useful for years — even after the code it documents no longer exists. Investment in knowledge yields compounding returns. Investment in code yields diminishing returns.

**Rationale:** This tenet synthesizes the foundational philosophy of CognOS. It is not a statement against code — it is a statement about relative priority. Every hour spent on knowledge that enables better code is a better investment than an hour spent on code that lacks knowledge.

**Implications:**
- Time spent on documentation, ADRs, module contracts, and the glossary is prioritized over time spent on implementation
- The Knowledge Foundation is a prerequisite, not an afterthought
- When resources are scarce, knowledge artifacts are preserved before code artifacts

**Violation:** Deleting or archiving a documentation artifact because the code it documented has been replaced.

---

## Using These Tenets

### In code review
Ask: does this change violate any tenet? If yes, reject with a reference to the specific tenet.

### In architectural decisions
Ask: which tenets are most relevant to this decision? Document your analysis in the ADR.

### In onboarding
New contributors must read these tenets before contributing. Alignment with these tenets is a prerequisite for participation.

### In design discussions
When two approaches are debated, resolve the debate by applying the relevant tenets. If the tenets do not resolve the debate, that is a signal that the tenets may need extension — open that discussion explicitly.

---

## Changing a Tenet

Tenets are not immutable in the absolute sense — they represent current best thinking, and thinking evolves.

To propose a change to a tenet:

1. Open a discussion explaining what problem the current tenet creates
2. Propose the revised tenet text
3. Explain how existing systems would be affected
4. Write an ADR if the proposed change is adopted

Tenets are changed through deliberation, not exception.

---

*CognOS Design Tenets v1.0 — July 2026*
*These tenets apply to every CognOS repository, every Vertical Module, and every contribution to the Ecosystem.*
