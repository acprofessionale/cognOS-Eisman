# Mobile Capture MVP v0.1

Status: implementation candidate derived from accepted ADR-0002.

## Goal

Make field capture from the operator's phone as close as possible to: **share a photo / video / audio file, optionally add one short verbatim note, done**.

The MVP deliberately implements only the trustworthy first half of the flow:

`FILE → SHA-256 → immutable content-addressed object → inference-free inbox receipt`

It does **not** perform AI extraction, canonicalization, publication or external mutation.

## Local command

```bash
python3 capture/capture.py ingest /path/to/photo.jpg
```

Optional verbatim note:

```bash
python3 capture/capture.py ingest /path/to/photo.jpg --note "Knappenhof, appena fotografato"
```

Default local store:

```text
~/.cognos-eisman/capture/
├── inbox/
│   └── cap_<uuid>.json
└── objects/
    └── sha256/<prefix>/<digest>
```

## Safety / epistemic properties

- source bytes are hashed before acceptance;
- copied bytes are hashed again before atomic placement;
- object identity is content-addressed by SHA-256;
- the receipt is always `capture_state: INBOX`;
- the receipt is always `publication_class: DENY`;
- `derived_assertions` is empty at raw-capture time;
- a human note is stored verbatim as `raw_note`, not interpreted;
- repeated identical bytes reuse the immutable object but create distinct capture receipts.

## Phone integration boundary

Android/Termux share-target integration is intentionally the next tranche. It may invoke this ingest boundary, but must not weaken it. The phone UX target remains one gesture plus, optionally, a short note.

No cloud upload, AI call, location inference, person recognition or publication is authorized by this MVP.

## Validation

Standard-library tests:

```bash
python3 -m unittest tests/test_capture.py -v
```

The JSON Schema at `schemas/capture/raw-capture.v1.schema.json` documents the persisted raw-capture contract. Runtime schema validation is intentionally not added until the validator dependency and version policy are separately pinned.
