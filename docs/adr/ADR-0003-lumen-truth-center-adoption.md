# ADR-0003 — LUMEN Truth Center Adoption for Eisman

**Status:** Accepted  
**Date:** 2026-08-26  
**Decision owner:** Ennio Princi, Human Project Owner  
**Ratification:** Explicitly approved on 2026-08-26  
**Normative scope:** `VERTICAL_EISMAN_PROVISIONAL`  
**Upstream profile:** CognOS Constitutional Engineering Framework merge `1f9fb782c70bae421fdce843b090d58bc8dfb1c7`

## Context

ADR-0002 separates immutable capture, proposed interpretation, canonical knowledge, and publication. The proposal-envelope work requires an evidence-ready validation against the previously validated real-photo receipt on the operator host. Eisman needs a durable receipt proving that the proposal evaluated and the action authorized are the same bounded operation.

## Decision

Eisman adopts the following upstream constitutional principles:

- `TRUTH-CENTER-001`
- `ENTROPIC-IMPRINT-002`
- `SINCERITY-003`
- LUMEN Decision Passport v0.1

The adoption is an evidence profile. It does not expand runtime authority, change the CognOS-Core taxonomy, or permit autonomous canonicalization.

## Required mapping

| Eisman artifact | LUMEN field |
|---|---|
| immutable receipt/photo digest | `evidence[].sha256` |
| source reference and capture time | `evidence[].uri`, `observed_at`, `provenance` |
| proposal-envelope intent | `intent.statement`, `contract_sha256` |
| proposed interpretation | `truth_claim` |
| runtime risk inputs | `imprint` |
| policy result | `governance.decision` |
| operator `CONFIRM` | scoped `governance.approval` |
| writer arguments | `execution.arguments_sha256` |
| persisted result | `execution.result_sha256` |

`CORRECT` creates a new proposal and digest. `LATER` leaves execution as `not_started` and approval as `pending`. Neither state may be represented as `verified`.

## Real-photo validation gate

The proposal-envelope candidate may leave draft only when the operator-host run produces a sanitized evidence package containing:

1. the exact tested commit SHA;
2. SHA-256 of the already validated real-photo receipt, without committing the raw image;
3. SHA-256 of the proposal contract and exact writer arguments;
4. the generated LUMEN Decision Passport;
5. verifier output showing `PASS`;
6. negative evidence showing that a mutated proposal or mismatched approval fails;
7. an explicit operator decision: `CONFIRM`, `CORRECT`, or `LATER`;
8. no secret, personal raw media, credential, or private reasoning trace.

## Fail-closed invariants

- A raw capture is never a truth claim.
- `ask` plus anything other than a matching, unexpired `approved` scope cannot complete execution.
- A digest mismatch blocks promotion.
- A higher policy tier may strengthen, but never weaken, the entropic-imprint tier.
- A crystallized receipt is append-only; corrections use `supersedes`.
- No `constitutional_deny` can be overridden by this vertical.

## Consequences

Positive:

- receipt validation becomes portable and independently checkable;
- human confirmation is cryptographically bound to the reviewed proposal;
- field evidence remains local while its integrity is attestable;
- later observability systems can correlate on `decision_id`.

Costs:

- every consequential proposal requires digest materialization;
- operator-host validation remains necessary for real media;
- v0.1 digest integrity is not identity non-repudiation; a later signature profile is required for that property.

## Promotion rule

Operational evidence from Eisman may motivate a CognOS-Core ADR. It does not automatically become Core authority. Promotion requires independent Core review, threat analysis, schema compatibility review, and explicit ratification.

