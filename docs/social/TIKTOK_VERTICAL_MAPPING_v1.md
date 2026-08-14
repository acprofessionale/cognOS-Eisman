# CognOS-Eisman Social / TikTok Vertical Mapping v1

Status: PROPOSED FOUNDATION
Authority: Human Project Owner ratification required before merge

## Position

CognOS-Eisman Social is a CognOS vertical specialization. TikTok is an external provider/adapter target within that vertical. Neither CognOS-Eisman nor TikTok is permitted to redefine CognOS-Core risk, autonomy, policy, evidence or authority semantics.

## Core inheritance

This vertical inherits from CognOS-Core:

- capability contracts;
- provider abstraction;
- runtime risk derivation;
- policy decisions;
- human approval semantics;
- evidence/audit requirements;
- workspace isolation;
- secret handling principles;
- fail-closed behavior.

## Trust statements

- OAuth consent != CognOS authorization.
- TikTok API capability != policy permission.
- Policy permission != execution approval.
- Provider response != independent evidence by itself.
- Public content side effects require explicit governance.

## Initial TikTok mapping

| CognOS capability | TikTok role | Initial vertical state | Human gate | External side effect |
|---|---|---|---|---|
| `identity.connect` | OAuth account connection | DESIGNED | explicit user consent | account linkage |
| `identity.disconnect` | revoke/disconnect | DESIGNED | user/operator action | provider authority revoked |
| `profile.read` | authorized profile retrieval | DESIGNED | consent/policy | none beyond API read |
| `content.list` | authorized video/content listing | DESIGNED | consent/policy | none beyond API read |
| `content.draft` | local CognOS drafting/planning | DESIGNED | human review before escalation | local only |
| `content.upload` | provider upload capability | PROPOSED / NOT_VERIFIED | REQUIRED before execution according to runtime policy | provider-side stored asset/draft |
| `content.publish` | provider public publication | BLOCKED | EXPLICIT HUMAN GATE REQUIRED | public publication |
| `evidence.record` | CognOS-owned evidence | DESIGNED | n/a | local audit/evidence only |
| `policy.evaluate` | CognOS-owned policy | DESIGNED | n/a | none |
| `human.approve` | CognOS-owned authorization artifact | DESIGNED | Human Project Owner/operator per policy | authority decision only |

## Initial runtime profile

The initial pilot is intentionally staged:

1. verify account connection semantics;
2. exercise `profile.read`;
3. exercise `content.list`;
4. generate local `content.draft` artifacts;
5. verify evidence and audit coverage;
6. evaluate `content.upload` only in a separate tranche;
7. keep `content.publish` blocked until separately ratified.

No later step is authorized by the existence of an earlier successful step.

## OAuth boundary

The OAuth implementation must define and verify:

- redirect URI ownership;
- CSRF/state validation and PKCE where applicable;
- token exchange owner;
- secure token storage owner;
- refresh behavior;
- token expiry handling;
- provider revocation;
- local disconnect;
- consent withdrawal;
- audit events;
- deletion/retention semantics.

WordPress is not automatically the OAuth authority or token store. The callback owner must be selected by architecture, not convenience.

## Secrets

TikTok client secrets, access tokens and refresh tokens MUST NOT be stored in:

- public WordPress content;
- client-side JavaScript;
- Git history;
- analytics;
- public logs;
- page metadata.

Runtime secret ownership remains an explicit security-sensitive design decision.

## Evidence requirements

For each provider invocation capture at minimum:

- capability ID/version;
- vertical ID;
- principal/account binding;
- provider adapter/version;
- requested scope/permission set;
- concrete request fingerprint or exact-bound arguments where required;
- policy decision reference;
- human approval reference where required;
- timestamp/freshness;
- provider outcome metadata;
- error/failure classification;
- evidence status;
- redaction status.

Never record raw secrets as evidence.

## Public projection

The public portal may safely state facts such as:

- capability currently DESIGNED / VERIFIED / BLOCKED;
- provider is TikTok;
- human approval requirement;
- presence/absence of public side effect;
- latest verification timestamp;
- high-level purpose and limits.

It must not imply TikTok endorsement, expose credentials, disclose sensitive security implementation or claim a capability VERIFIED without evidence.

## Immediate acceptance criteria

- read capabilities remain separable from publish capabilities;
- Direct/public posting is not silently enabled;
- `content.publish` remains BLOCKED until a future explicit tranche;
- WordPress remains public presentation/trust surface, not authority source;
- provider-specific details do not contaminate canonical Core capability semantics;
- any undocumented current TikTok requirement is NOT_VERIFIED until checked against authoritative provider documentation.
