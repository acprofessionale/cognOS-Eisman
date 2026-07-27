# CognOS-Eisman — Roadmap

*Living document. Updated at the close of each phase.*
*Version 1.0 — July 2026*

---

## Roadmap Philosophy

This roadmap does not contain guaranteed delivery dates.
It contains phases, each with clear entry conditions, objectives, and exit criteria.

A phase is complete when its exit criteria are met — not when a calendar date arrives.

This distinction is intentional.

Knowledge work cannot be scheduled like manufacturing.
A phase that takes longer than expected because we are thinking carefully is better than a phase rushed to meet an arbitrary deadline.

---

## Phase Overview

| Phase | Name | Status | Focus |
|---|---|---|---|
| 0 | Bootstrap | **Active** | Knowledge foundation & governance |
| 1 | Architecture | Not started | System design & module contracts |
| 2 | Prototype | Not started | First working implementation |
| 3 | Learning Cycle | Not started | Operational data & model refinement |
| 4 | Vertical Template | Not started | Extraction & ecosystem expansion |

---

## Phase 0 — Bootstrap

**Status: Active**
**Objective:** Establish the knowledge foundation that will govern all future development.

Code written before this phase is complete is technical debt from day one.

### Entry Condition
Repository initialized with governance intent.

### Objectives

- [ ] Repository governance defined (CONTRIBUTING.md, naming conventions, versioning)
- [ ] Official vocabulary documented (docs/glossary.md)
- [ ] Immutable engineering principles documented (docs/design-tenets.md)
- [ ] Manifesto written and reviewed (MANIFESTO.md)
- [ ] Long-term vision documented (VISION2030.md)
- [ ] Project charter completed (docs/project-charter.md)
- [ ] All 5 foundational ADRs written and approved
- [ ] Prompt library established with all 9 role prompts (docs/prompts/)
- [ ] All 7 module contracts written (modules/*/README.md)
- [ ] Architecture documentation suite completed (docs/architecture/)
- [ ] Opportunity Intelligence Engine described in depth

### Exit Criteria
Every document listed above exists, is coherent, and has been reviewed.
No document has unresolved contradictions with another.
A new contributor can understand the system by reading docs/ alone.

---

## Phase 1 — Architecture

**Status: Not started**
**Objective:** Define the technical architecture with enough precision that implementation can begin without ambiguity.

### Entry Condition
Phase 0 exit criteria met.

### Objectives

- [ ] Technology stack finalized and documented (ADR required for each major choice)
- [ ] Module interface contracts defined (inputs, outputs, schemas)
- [ ] Inter-module communication protocol selected and documented
- [ ] Data persistence strategy defined
- [ ] Voice interface architecture designed
- [ ] Opportunity Intelligence Engine decision flow documented in detail
- [ ] Observability and audit logging strategy defined
- [ ] Development environment documented (setup, tooling, local run)
- [ ] CI/CD strategy outlined

### Exit Criteria
A developer can begin implementing any single module without asking any architectural questions.
Every interface between modules is defined in writing.
Every significant technology choice has an ADR.

---

## Phase 2 — Prototype

**Status: Not started**
**Objective:** Build the first working version of the system with real but minimal functionality.

### Entry Condition
Phase 1 exit criteria met.

### Objectives

- [ ] `weather` module — functional (fetches and formats weather data)
- [ ] `calendar` module — functional (reads schedule context)
- [ ] `maps` module — functional (resolves location intelligence)
- [ ] `event-intelligence` module — functional (detects and classifies relevant events)
- [ ] `voice` module — minimal (accepts spoken input, produces spoken output)
- [ ] Opportunity Intelligence Engine — functional (aggregates signals, produces ranked decisions)
- [ ] End-to-end flow: operator speaks a question → system produces a ranked decision
- [ ] All modules produce observable, auditable output
- [ ] Test coverage defined and initial tests passing

### Exit Criteria
A mobile operator can ask "where should I go today?" and receive a structured, reasoned answer.
The answer is traceable back to its contributing signals.

---

## Phase 3 — First Learning Cycle

**Status: Not started**
**Objective:** Introduce real operational data and activate the sales-learning module.

### Entry Condition
Phase 2 exit criteria met.
System has been operated for at least one real business day.

### Objectives

- [ ] `sales-learning` module — functional (records decisions and outcomes)
- [ ] Outcome feedback loop established (operator confirms or overrides decisions)
- [ ] Opportunity Intelligence Engine scoring model receives feedback
- [ ] First pattern report generated (which locations, events, weather correlate with performance)
- [ ] Voice interface covers the full daily briefing cycle
- [ ] System is demonstrably better after 30 days of data than on day 1

### Exit Criteria
The system makes measurably different (and better) recommendations than it did at the start of Phase 3, based on real operational data.
Learning loop is documented and auditable.

---

## Phase 4 — Vertical Template

**Status: Not started**
**Objective:** Extract the reusable patterns from CognOS-Eisman and formalize CognOS-Core.

### Entry Condition
Phase 3 exit criteria met.
CognOS-Eisman is operational.

### Objectives

- [ ] CognOS Vertical Template documented
- [ ] CognOS-Core concepts formally separated from CognOS-Eisman specifics
- [ ] Common governance artifacts identified and extracted
- [ ] Second Vertical Module domain identified
- [ ] Second vertical's bootstrap phase initiated using the template

### Exit Criteria
A new CognOS Vertical Module can be bootstrapped in less time than CognOS-Eisman required.
CognOS-Core exists as a defined, documented foundation — not just an implicit convention.

---

## Non-Goals (for this roadmap)

These are explicitly out of scope for the current roadmap period:

- Multi-user / SaaS infrastructure
- External API productization
- Mobile app (native iOS / Android)
- Predictive demand forecasting at scale (requires Phase 3 data first)
- Multi-city or multi-operator support

---

## Versioning of This Document

This roadmap is versioned alongside the repository.
When a phase is closed, it is marked **Completed** with a date.
Objectives are never deleted — they are either completed, deferred with reason, or cancelled with reason.

The history of this roadmap is itself a knowledge artifact.

---

*CognOS-Eisman Roadmap v1.0 — July 2026*
