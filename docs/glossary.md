# CognOS Ecosystem — Official Glossary

*Authoritative vocabulary for the entire CognOS Ecosystem.*
*Version 1.0 — July 2026*

---

## Purpose

This glossary defines every important concept in the CognOS Ecosystem with one authoritative definition.

Terms defined here must be used consistently across all documents, ADRs, module contracts, prompts, and code.

When a term is not in this glossary, it should not be used in official documentation until it is added here.

Synonyms create ambiguity. Ambiguity creates misunderstanding. Misunderstanding creates defects.

---

## Conventions

Each entry follows this structure:

**Term** — *Category*
Definition. One or more sentences.
> *Use in a sentence: [example]*

---

## Core Concepts

---

**CognOS** — *Ecosystem*
A Cognitive Operating System. An ecosystem of autonomous, cooperative modules that together form an intelligent decision-support layer for real-world operations. CognOS is not a single application. It is an architectural philosophy instantiated through Vertical Modules built on CognOS-Core.
> *Use in a sentence: CognOS transforms fragmented operational signals into structured decisions.*

---

**CognOS-Core** — *Foundation*
The shared infrastructure, governance framework, architectural conventions, documentation standards, and design tenets that all CognOS Vertical Modules inherit. CognOS-Core is not a software library. It is an architectural contract. It lives in documentation, ADRs, the glossary, and the design tenets — not in a single codebase.
> *Use in a sentence: CognOS-Eisman and all future verticals inherit their governance rules from CognOS-Core.*

---

**CognOS-Eisman** — *Vertical Module*
The first operational Vertical Module of the CognOS Ecosystem. Its domain is mobile business operations, specifically an Ice Cream Truck. Its mission is to transform fragmented signals (weather, events, location, calendar) into ranked operational decisions. Named after the principle of turning information asymmetry into operational advantage.
> *Use in a sentence: CognOS-Eisman is the first validated instance of the CognOS architecture.*

---

**Ecosystem** — *System*
The totality of the CognOS project: its Vertical Modules, CognOS-Core, shared governance, documentation, prompt library, and architectural conventions. The Ecosystem is not a deployment — it is an evolving knowledge and software system.
> *Use in a sentence: The CognOS Ecosystem will include multiple Vertical Modules by 2028.*

---

**Vertical Module** — *Architecture*
A self-contained CognOS implementation targeting a specific operational domain. A Vertical Module uses CognOS-Core conventions but is independently developed, documented, and deployed. It is not a plugin of CognOS-Core — it is a complete system that inherits its architectural identity from CognOS-Core. Shorthand: "vertical" (acceptable after formal introduction).
> *Use in a sentence: CognOS-Eisman is a Vertical Module targeting mobile food operations.*

---

**Module** — *Architecture*
The fundamental unit of CognOS architecture. A module is an independent, composable, documented, testable, observable, and replaceable functional component within a Vertical Module. Modules communicate through defined interfaces. No module depends on another module's implementation — only on its interface.
> *Use in a sentence: The weather module provides meteorological context to the Opportunity Intelligence Engine.*

---

**Opportunity Intelligence Engine** — *System Component*
The strategic center of a CognOS Vertical Module. The Opportunity Intelligence Engine aggregates signals from all other modules (weather, events, maps, calendar, sales history) and produces ranked operational decisions with reasoning. It does not decide — it informs. The operator decides. Technical implementation lives in the `opportunity-engine` module directory.
> *Use in a sentence: The Opportunity Intelligence Engine ranked three locations based on today's event, weather, and historical performance data.*

---

**Knowledge** — *Principle*
Structured, documented understanding that survives technology change. In CognOS, knowledge is the primary artifact of development. Code is an implementation of knowledge. Documentation is knowledge made explicit. Knowledge is permanent; code is temporary. The CognOS principle "Knowledge Before Code" derives from this definition.
> *Use in a sentence: The module contract is a knowledge artifact that precedes and outlasts any specific implementation.*

---

**Governance** — *Process*
The set of rules, standards, processes, and decision records that regulate how the CognOS Ecosystem evolves. Governance includes: the ADR process, documentation standards, naming conventions, the glossary, contribution guidelines, and the design tenets. Good governance ensures that the ecosystem remains coherent as it grows.
> *Use in a sentence: The ADR process is the primary governance mechanism for architectural decisions.*

---

**Architecture** — *Discipline*
The set of structural decisions that define how CognOS systems are organized, how their components interact, and how they evolve over time. In CognOS, architecture is documented before implementation and governed through ADRs. Architecture decisions outlast any specific implementation.
> *Use in a sentence: The modular architecture ensures that replacing one module does not require rebuilding the system.*

---

**Documentation** — *Artifact*
In CognOS, documentation is not commentary on code. It is a first-class artifact that precedes, justifies, and governs implementation. The CognOS documentation system includes: module contracts, ADRs, architecture documents, the glossary, design tenets, the prompt library, and all root-level governance files. A system is not complete when the code is written — it is complete when the documentation is complete.
> *Use in a sentence: The module contract is a documentation artifact that defines the module's interface before any code is written.*

---

**Decision** — *Output*
The primary output of the CognOS system. A decision is a structured, ranked, reasoned recommendation for an operator action (where to go, when to go, what to prioritize). Decisions are produced by the Opportunity Intelligence Engine. Decisions are not commands — they are inputs to human judgment. Every decision must be traceable to its contributing signals.
> *Use in a sentence: The system produced a ranked decision recommending Piazza Navona at 15:00 based on the jazz festival event, 28°C forecast, and Friday historical performance.*

---

**ADR (Architecture Decision Record)** — *Governance*
A document that records a significant architectural decision: its context, the alternatives considered, the decision made, and its consequences. ADRs are immutable once accepted — they are never deleted, only superseded. ADRs are the institutional memory of architectural reasoning. Format: `ADR-NNNN-short-title.md` in `docs/adr/`.
> *Use in a sentence: ADR-0001 records the decision to establish Knowledge Before Code as the governing principle of the ecosystem.*

---

## Operational Concepts

---

**Signal** — *Data*
A structured input to the Opportunity Intelligence Engine from a module. A signal carries typed information (weather forecast, event classification, location score, calendar constraint) in a defined format. The Engine aggregates signals to produce a Decision.
> *Use in a sentence: The weather module emits a temperature signal; the event-intelligence module emits an event-presence signal.*

---

**Operator** — *Human*
The human who uses a CognOS Vertical Module to support real-world decisions. The operator is never replaced by the system — they are amplified by it. The operator provides context the system cannot infer, and bears responsibility for every decision made.
> *Use in a sentence: The operator heard the briefing, confirmed the recommendation, and drove to the suggested location.*

---

**Module Contract** — *Documentation*
The formal specification of a module's interface: its purpose, responsibilities, inputs, outputs, dependencies, and planned evolution. A module contract is written before any implementation. It is the authoritative definition of what a module does and does not do. Location: `modules/[name]/README.md`.
> *Use in a sentence: The voice module contract defines what audio input formats the module accepts and what text formats it emits.*

---

**Bootstrap Phase** — *Project State*
The initial phase of a CognOS Vertical Module development during which the knowledge foundation is established. No production code is written during the Bootstrap Phase. The Bootstrap Phase is complete when all documentation, ADRs, module contracts, and architectural blueprints are written, reviewed, and coherent.
> *Use in a sentence: CognOS-Eisman is currently in the Bootstrap Phase.*

---

**Knowledge Foundation** — *Artifact Set*
The complete set of documents produced during the Bootstrap Phase: manifesto, vision, roadmap, glossary, design tenets, project charter, ADRs, architecture documents, module contracts, and the prompt library. The Knowledge Foundation is the prerequisite for all implementation work.
> *Use in a sentence: The Knowledge Foundation must be complete before Phase 1 architecture work begins.*

---

**Prompt Library** — *Documentation*
A curated collection of reusable AI prompts that define roles, responsibilities, constraints, and expected outputs for AI-assisted work within the CognOS Ecosystem. The Prompt Library ensures that AI interactions are reproducible, auditable, and consistent with the design tenets. Location: `docs/prompts/`.
> *Use in a sentence: The architect.md prompt in the Prompt Library defines how to invoke AI assistance for architectural analysis.*

---

**Learning Loop** — *System Behavior*
The feedback cycle in which the outcome of a Decision (what actually happened when the operator followed a recommendation) is captured, processed by the `sales-learning` module, and used to improve future scoring by the Opportunity Intelligence Engine.
> *Use in a sentence: After 30 days, the Learning Loop had enough data to identify that Saturday afternoons near parks outperform Friday evenings in the city center.*

---

*CognOS Ecosystem Glossary v1.0 — July 2026*
*Maintained as an authoritative reference. Update through pull request with documented rationale.*
