# Contributing to CognOS-Eisman

*Version 1.0 — July 2026*

---

## Before You Contribute

Read these documents first. In this order.

1. [MANIFESTO.md](MANIFESTO.md) — Understand why this project exists and what it believes
2. [docs/design-tenets.md](docs/design-tenets.md) — Understand the immutable engineering principles
3. [docs/glossary.md](docs/glossary.md) — Learn the official vocabulary
4. [ROADMAP.md](ROADMAP.md) — Understand what phase the project is in

A contribution that contradicts the manifesto or violates a design tenet will not be accepted, regardless of its technical quality.

---

## The Fundamental Rule

**Knowledge Before Code.**

This is not a guideline. It is the governing principle of this repository.

No implementation is accepted without prior documentation of the design.
No design is accepted without a documented rationale.
No rationale is accepted without alignment with the architecture.

If you want to write code, first write the document that justifies the code.

---

## Types of Contribution

### 1. Documentation

Documentation is the highest-priority contribution type.

Accepted:
- New architectural documents
- Improvements to existing documents (clarity, accuracy, completeness)
- New ADRs for undocumented decisions
- Module contract improvements
- Glossary additions
- Prompt library additions

Requirements:
- Written in professional Markdown
- No marketing language
- No hype
- Consistent with the official vocabulary in docs/glossary.md
- Reviewed against docs/design-tenets.md for principle alignment

### 2. Architecture

Architecture contributions propose or modify system design.

Every significant architectural change requires an Architecture Decision Record (ADR) before any implementation.

An ADR must document:
- The decision being made
- The context that motivated it
- The alternatives considered
- The consequences accepted
- The rationale for the choice

See [docs/adr/](docs/adr/) for existing ADRs and format reference.

An architecture contribution without an ADR will not be merged.

### 3. Module Contracts

Module contract contributions define or refine the interface of a module.

A module contract (modules/[name]/README.md) must specify:
- Purpose (one paragraph)
- Responsibilities (what it does and does not do)
- Inputs (format, source, schema)
- Outputs (format, destination, schema)
- Dependencies (on other modules, external APIs, data sources)
- Future API (planned but not yet implemented)
- Roadmap (module-level milestones)

A module contract must be approved before any module implementation begins.

### 4. Implementation

Implementation contributions write code for a module or shared utility.

Requirements:
- The relevant module contract must already be approved
- An ADR must exist for any non-trivial technical decision in the implementation
- The implementation must not exceed the scope defined in the module contract
- Tests must accompany every implemented behavior
- The implementation must be observable (logs, traces, or audit records)

Implementation contributions that exceed their documented scope will be rejected and asked to split.

### 5. Review

Review contributions improve existing work through feedback.

Accepted:
- Consistency reviews across documents
- Terminology audits against the glossary
- Architectural gap identification
- ADR critique and improvement suggestions

---

## Contribution Process

### Step 1 — Check existing work

Before starting, check:
- Open issues and discussions
- Existing ADRs (does this decision already exist?)
- The module contract (does this behavior already have a home?)
- The roadmap (is this in scope for the current phase?)

### Step 2 — Document first

Write the document that justifies your contribution before writing any code.

For architecture changes: write the ADR.
For new modules: write the module contract.
For new features: update the relevant module contract.
For documentation improvements: the document is the contribution.

### Step 3 — Review your terminology

Check every term you use against [docs/glossary.md](docs/glossary.md).
Use official terms. Do not introduce synonyms.

### Step 4 — Submit

Submit a pull request with:
- A clear title describing what changes and why
- A description that links to the relevant ADR, module contract, or document
- Confirmation that you have read and aligned with the design tenets

---

## What Will Not Be Accepted

The following will be rejected without review:

- Code submitted without prior documentation
- Architecture changes without an ADR
- Terminology that contradicts the glossary
- Features outside the current roadmap phase scope
- AI-generated content submitted without human review and validation
- Any contribution that removes human accountability from a decision
- Monolithic patterns that couple modules together
- Vendor lock-in to a single AI provider

---

## Markdown Standards

All documentation must follow these rules:

- Use ATX-style headers (`#`, `##`, `###`)
- Use fenced code blocks with language identifiers
- Use tables for structured comparisons
- No trailing spaces
- One blank line between sections
- No inline HTML unless strictly necessary
- File names: lowercase, hyphen-separated (e.g., `system-overview.md`)

---

## ADR Format

Every ADR must use this structure:

```markdown
# ADR-NNNN: [Short Title]

*Status: [Proposed | Accepted | Deprecated | Superseded by ADR-XXXX]*
*Date: YYYY-MM-DD*
*Author: [name or handle]*

## Context
[What situation or problem motivated this decision?]

## Decision
[What was decided?]

## Alternatives Considered
[What other options were evaluated and why were they not chosen?]

## Consequences
[What are the implications — positive and negative — of this decision?]

## Rationale
[Why is this decision consistent with the design tenets?]
```

---

## Questions and Discussion

If you are unsure whether your contribution is appropriate, open a discussion before starting work.

It is better to ask and be redirected than to build something that cannot be accepted.

---

*CognOS-Eisman — Contributing Guidelines v1.0, July 2026*
