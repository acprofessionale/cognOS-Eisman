# ADR-0002 — Mobile Capture and Controlled Projection

**Status:** Proposed  
**Date:** 2026-08-17  
**Decision owner:** Human Project Owner  
**Normative scope:** `VERTICAL_EISMAN_PROVISIONAL`  
**Core authority:** CognOS-Core v0.2 remains authoritative for runtime safety, execution authority, R0–R4/A0–A4 and constitutional deny semantics.  
**Promotion rule:** No vertical decision becomes Core authority by inheritance. Any promotion requires a fresh CognOS-Core ADR, complete re-derivation, review and explicit ratification.

## Context

CognOS-Eisman is used in a field environment where the operator is moving, working from the Eiswagen, meeting people, photographing places/products/documents, recording voice and video, and collecting real-world evidence. The system must reduce operator friction rather than turn field activity into metadata administration.

The primary interaction device is the phone. The desired operator experience is deliberately minimal: capture reality now, structure it later, preserve provenance throughout, and require human confirmation before semantic assertions become canonical knowledge or publication.

This ADR is vertical-local and provisional. It does not amend CognOS-Core and does not authorize a new Core taxonomy.

## Decision

### 1. Separate raw capture, canonical knowledge and publication

The following invariant is mandatory:

`RAW_CAPTURE != CANONICAL_KNOWLEDGE != PUBLICATION`

A raw capture is evidence material. It is not automatically a claim, a fact, canonical knowledge or public content.

### 2. Raw capture is immutable and inference-free

A raw capture may contain source-native data and mechanically observed metadata such as timestamp, device-origin identifiers and the original media payload.

Inferences must not be written back into the raw record. Inferred place, person, object, wine, event, meaning or relationship belongs to a derived proposal/observation layer with its own provenance and confidence.

### 3. AI may propose; AI may not create authority

AI may:
- transcribe;
- extract text;
- classify candidate entities;
- propose observations, claims and relations;
- suggest links to existing people, places, projects or evidence;
- propose narrative or aesthetic projections.

AI may not:
- fabricate provenance;
- silently promote an inference to fact;
- silently mutate raw evidence;
- self-ratify a canonical assertion;
- self-publish epistemic content.

### 4. Human review is intentionally low-friction

The target review interaction is:

`CONFIRM | CORRECT | LATER`

The operator is not required to edit YAML/JSON/Markdown on the phone. `LATER` is a valid fail-closed state: the item remains in the inbox and is not promoted.

### 5. Entity model and state model are distinct

Canonical entities are expected to include, at minimum:
- Capture
- Observation
- Claim
- Evidence
- Attestation

Evidence is not a later state of a Claim; it is a distinct entity with potentially many-to-many support/refutation relationships.

Claim status must use orthogonal dimensions rather than one overloaded enum:

- verification: `UNVERIFIED | PARTIALLY_VERIFIED | VERIFIED`
- contested: independent boolean or dispute relation
- lifecycle: `ACTIVE | SUPERSEDED`

### 6. Provenance semantics are split

The term `authority` is not reused for epistemic source provenance because CognOS-Core already uses authority with execution/governance meaning.

Required conceptual dimensions:

`source_class`
- `HUMAN_REPORTED`
- `DIRECT_OBSERVATION`
- `DOCUMENTARY_SOURCE`
- `EXTERNAL_AUTHORITY`

`assertion_mode`
- `HUMAN_ASSERTED`
- `AI_PROPOSED`
- `AI_EXTRACTED`

These dimensions answer different questions and must not be collapsed.

### 7. Publication is controlled projection

Canonical knowledge must never be exposed directly as the public site/content surface.

Future structured epistemic artifacts require a publication control that is materially DENY by default. Any default that affects epistemic or publication meaning must be materialized into the persisted artifact at write time; validator-injected semantic defaults are forbidden.

The projection layer must evaluate publication eligibility, provenance integrity and required digests before creating public output.

### 8. Canonical inputs must be anchored and verifiable

For the epistemic path, content is admissible to assured projection only when its identity and provenance are reproducible.

Remote/live sources are not canonical merely because they are fetched at build time. Canonical inputs must be repo-anchored or explicitly digest-pinned with verifiable provenance.

Live/request-time collections are prohibited for Observation, Claim, Evidence and Attestation canonical publication paths.

### 9. Media masters may live outside Git only with content identity

Large image/video/audio masters may be stored outside Git to prevent repository bloat, but references must carry at least:
- stable URI/reference;
- cryptographic content digest (target: SHA-256);
- retention class/policy.

Missing or mismatched digest must fail closed for assured projection.

### 10. Static-site technology is downstream

A website is a projection, not the system of record.

Astro or any later framework decision is implementation-level and must be pinned at implementation time, including runtime and validator semantics. Features that introduce runtime or cache paths capable of bypassing the projection assurance gate must be disabled or proven safe before use.

No framework choice is ratified by this ADR.

## Mobile MVP flow

`PHOTO / VOICE / VIDEO`
→ immutable raw capture
→ digest + source timestamp
→ extraction/proposals
→ human `CONFIRM | CORRECT | LATER`
→ canonical entities/relations
→ optional curation
→ controlled projection

The operator's field workload must remain dominated by living/working/capturing, not metadata entry.

## Non-goals

This ADR does not authorize:
- RAG;
- vector databases;
- a CMS;
- live publishing;
- autonomous canonicalization;
- OAuth/token acquisition;
- social publication;
- runtime actions against external services;
- any modification of CognOS-Core;
- any new Core authority taxonomy.

## Governance

This ADR is governed locally by the Human Project Owner under CognOS-Eisman ADR-0001.

It is explicitly provisional and non-normative for Core. If experience from this vertical later motivates a Core-level model, Core must re-derive the proposal from current Core authority and evidence. This ADR supplies evidence and experience only; it does not carry ratification upward.

## Acceptance criteria before implementation

- review against current CognOS-Eisman ADR-0001;
- review against current ratified CognOS-Core v0.2 authority;
- no reverse dependency from Core to Eisman;
- no runtime or publication authority introduced;
- exact candidate SHA identified;
- explicit Human Project Owner ratification after review.

Until then, status remains **Proposed**.