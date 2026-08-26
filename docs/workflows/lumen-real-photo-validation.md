# LUMEN Real-Photo Receipt Validation

Use this runbook on the trusted operator host. Do not commit the raw receipt image.

## Inputs

- exact candidate commit SHA;
- local path to the previously validated receipt photo;
- proposal-envelope command or writer entry point;
- operator identity reference;
- applicable policy references.

## Procedure

1. Record the candidate SHA and confirm the working tree is clean.
2. Compute the photo SHA-256 locally.
3. Run the proposal writer against the photo using the production-equivalent path.
4. Materialize the exact proposal contract and arguments digests.
5. Calculate `Wg = S × I × R × H(Δ)` and record every factor.
6. Evaluate policy as `DENY`, `ASK`, or `ALLOW`.
7. If `ASK`, present the exact scope to the operator and record `CONFIRM`, `CORRECT`, or `LATER`.
8. Produce the LUMEN Decision Passport and calculate its canonical digest.
9. Run the reference verifier.
10. Mutate one proposal field in a copy and prove that verification fails.
11. Store only sanitized receipts, hashes, command versions, timestamps, and verifier output.

## Evidence receipt template

```text
candidate_sha:
receipt_sha256:
proposal_contract_sha256:
arguments_sha256:
decision_id:
imprint: {scope:, impact:, irreversibility:, entropy:, weight:, tier:}
policy_decision:
operator_decision: CONFIRM | CORRECT | LATER
passport_sha256:
positive_verifier_result:
negative_mutation_result:
raw_media_committed: false
secrets_detected: false
recorded_at:
recorded_by:
```

## Exit decision

- `READY`: positive verification passes, negative mutation fails, operator confirms, and the evidence package is complete.
- `REWORK`: schema, digest, mapping, or proposal behavior is incorrect.
- `BLOCKED`: operator approval, trusted host, real-photo fixture, or required provenance is unavailable.

Only `READY` justifies taking the proposal-envelope PR out of draft. Merge remains a separate decision governed by the repository's normal controls.

