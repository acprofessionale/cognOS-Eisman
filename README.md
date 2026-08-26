# CognOS-Eisman

> First operational vertical of the CognOS Ecosystem.
> Mission: transform information into operational decisions for a mobile business.

---

## What is CognOS?

CognOS is a Cognitive Operating System.

It is not a single application. It is an ecosystem of autonomous, cooperative modules that together form an intelligent decision-support layer for real-world operations.

CognOS does not replace human judgment. It amplifies it.

---

## What is CognOS-Eisman?

Eisman is the first operational vertical of the CognOS Ecosystem.

Its domain is the management of a mobile business — specifically, an Ice Cream Truck operation.

Its mission is to take raw, fragmented information (weather, events, location, calendar, market signals) and produce structured, actionable operational decisions: where to go, when to go, what to sell, and why.

The name references the discipline of turning information asymmetry into operational advantage — understanding what others overlook, and acting on it before it becomes obvious.

---

## Architecture

CognOS-Eisman is built on seven cooperative modules. Each module is:

- **Independent** — it can be developed, tested, and replaced in isolation
- **Composable** — it communicates through defined interfaces
- **Documented** — knowledge precedes implementation
- **Observable** — its behavior is traceable and auditable

### Module Map

| Module | Responsibility |
|---|---|
| `event-intelligence` | Detects and classifies local events that affect demand |
| `opportunity-engine` | Aggregates signals and produces ranked operational decisions (Opportunity Intelligence Engine) |
| `weather` | Provides weather context for demand forecasting |
| `maps` | Provides geographic and location intelligence |
| `calendar` | Manages temporal context and scheduling |
| `voice` | Natural-language interface for input and output |
| `sales-learning` | Learns from historical performance to improve future decisions |

The `opportunity-engine` implements the **Opportunity Intelligence Engine** — the strategic center of the system. It receives signals from all other modules and produces the final decision output.

---

## Repository Structure

```
CognOS-Eisman/
├── docs/
│   ├── architecture/       System blueprints and design documents
│   ├── adr/                Architecture Decision Records
│   ├── prompts/            Reusable AI prompt library
│   ├── principles/         Foundational principles documentation
│   ├── reference/          Reference materials and external standards
│   └── workflows/          Business process and operational workflows
├── modules/
│   ├── calendar/
│   ├── event-intelligence/
│   ├── maps/
│   ├── opportunity-engine/
│   ├── sales-learning/
│   ├── voice/
│   └── weather/
├── src/                    Shared source code and utilities
├── tests/                  Test suites
└── scripts/                Automation and tooling scripts
```

---

## Guiding Principles

**Knowledge Before Code.** Documentation is written before code. Architecture is defined before implementation. Knowledge survives technology.

**Human First.** AI amplifies human judgment. Humans remain responsible for every decision. AI does not replace vision.

**Voice First.** Voice is the natural interface for a mobile operator. Every interaction is designed to work without a screen when possible.

**Modular Architecture.** No module depends on another module's implementation. Dependencies are expressed through interfaces, not code coupling.

**Model Agnostic.** The system never depends on a single AI provider. Orchestration across multiple models is by design.

**Long-Term Thinking.** Every architectural decision is evaluated for durability. Fashionable solutions are avoided. Simplicity is preferred.

---

## Current Status

This repository is in the **Bootstrap Phase**.

The architecture is being defined. The knowledge foundation is being built. No production code exists yet.

This is intentional.

See [ROADMAP.md](ROADMAP.md) for the development timeline.
See [docs/project-charter.md](docs/project-charter.md) for objectives and scope.
See [docs/architecture/](docs/architecture/) for system blueprints.

---

## Documentation Index

| Document | Purpose |
|---|---|
| [MANIFESTO.md](MANIFESTO.md) | Philosophical foundation of CognOS |
| [VISION2030.md](VISION2030.md) | Long-term ecosystem vision |
| [ROADMAP.md](ROADMAP.md) | Development timeline and milestones |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines and standards |
| [docs/project-charter.md](docs/project-charter.md) | Project charter, scope, and objectives |
| [docs/architecture/system-overview.md](docs/architecture/system-overview.md) | Full system architecture |
| [docs/adr/](docs/adr/) | Architecture Decision Records (ADR) |
| [docs/prompts/](docs/prompts/) | AI prompt library |
| [docs/glossary.md](docs/glossary.md) | Official vocabulary and term definitions |
| [docs/design-tenets.md](docs/design-tenets.md) | Immutable engineering principles |

---

## Part of the CognOS Ecosystem

CognOS-Eisman is the first Vertical Module. The architecture, governance standards, and documentation conventions established here will serve as the foundation template for all future CognOS Vertical Modules.

The shared core — **CognOS-Core** — provides the common infrastructure, governance framework, and architectural conventions that all verticals inherit.

---

*CognOS Ecosystem — Knowledge before code. Architecture before implementation. Vision before execution.*

## LUMEN Truth Center pilot

CognOS-Eisman is the first operational vertical adopting the ratified Truth Center profile and LUMEN Decision Passport v0.1.

- [ADR-0003 — LUMEN Truth Center Adoption](docs/adr/ADR-0003-lumen-truth-center-adoption.md)
- [Real-Photo Receipt Validation Runbook](docs/workflows/lumen-real-photo-validation.md)

The pilot binds field evidence, proposal intent, proportional governance, operator approval, execution, and verification to one portable `decision_id`. It does not expand Eisman's runtime authority.

