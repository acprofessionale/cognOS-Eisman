# PR #8 real-photo proposal gate

## Purpose

Close the remaining host-side gate for the capture proposal layer without
weakening the original requirement. CI proves deterministic mechanics; this
procedure proves the proposal writer against the previously validated real-photo
capture on the operator host.

The validation proposal is deliberately **ephemeral**: it is created through the
real proposal writer, read back and checked, hashed for the evidence result, then
removed. The raw capture and the normal review queue therefore remain unchanged
by the validation exercise.

## Existing source evidence

PR #7 recorded a successful real-device ingest on 2026-08-17 at exact candidate
head `1b6675db83ba05b4b5671bb23b1a404f9b332051`.

Durable evidence record: PR #7 issue comment `5321131590`.

Real photo recorded there:

- filename: `san-tommaso-photo.jpg`
- media type: `image/jpeg`
- size: `2106274` bytes
- SHA-256: `35cede6553363e1b9b95fdb471732a895c3c2b7a7b87181b6df542812ae5a49d`
- raw receipt state: `INBOX`
- publication class: `DENY`
- derived assertions: `[]`

That evidence proves capture ingest, not proposal creation. The following gate is
therefore still required.

## One-command gate

Run from a checkout of the reconciled proposal branch on the operator host:

```bash
python3 -m capture.real_photo_gate \
  --root ~/.cognos-eisman/capture \
  --sha256 35cede6553363e1b9b95fdb471732a895c3c2b7a7b87181b6df542812ae5a49d
```

Expected terminal verdict:

```text
REAL_PHOTO_PROPOSAL_GATE_PASS
```

The JSON result must also show:

- `raw_receipt_unchanged: true`
- `proposal_state: PROPOSED`
- `review_state: PENDING`
- `publication_class: DENY`
- `canonical_promotion: false`
- `semantic_image_assertion: false`
- `proposal_ephemeral: true`
- `proposal_cleanup: true`
- a 64-character `proposal_sha256` for the exact ephemeral proposal bytes that
  were exercised;
- the exact source SHA-256 above.

If the same image bytes were ingested more than once, the gate fails closed and
prints the matching capture IDs. Re-run with the intended ID:

```bash
python3 -m capture.real_photo_gate \
  --root ~/.cognos-eisman/capture \
  --sha256 35cede6553363e1b9b95fdb471732a895c3c2b7a7b87181b6df542812ae5a49d \
  --capture-id cap_<exact-id>
```

## What the gate verifies

1. the selected receipt is still raw-capture v1, `INBOX`, `DENY`, inference-free
   and in the expected vertical normative scope;
2. the receipt content-addressed `object_ref` is consistent with its SHA-256;
3. the referenced object exists inside the capture root;
4. the object SHA-256 still matches the receipt and the known real-photo digest;
5. proposal creation leaves the raw receipt byte-for-byte unchanged;
6. the proposal links to the exact capture ID and SHA-256;
7. the receipt reference persisted in the proposal is portable/relative, not an
   operator absolute path;
8. proposal state remains non-canonical and publication remains denied;
9. the validation proposal is removed after verification so the operator review
   queue is not polluted by test data.

## Non-goals

The gate does not infer what is in the photo, call an AI provider, create a
canonical entity, publish content, or grant any new authority. Its proposal
SHA-256 is an evidence checksum, not a digital signature or proof of authenticity.
