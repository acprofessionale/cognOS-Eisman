# CR-01 — Change Request for CognOS-Eisman ADR-0001

**Target file:** `docs/adr/ADR-0001-normative-authority-and-precedence.md` (CognOS-Eisman)
**Authorised by:** Ennio Princi (Human Project Owner), 2026-07-27
**Basis:** Cross-Repository Validation Report, findings F-04, F-05, F-06, F-08
**Resulting state:** `Proposed` — *Ready for Human Acceptance*

---

## Scope of this change request

Permitted operations, and nothing else:

1. Insert the scope-limitation clause (M-A).
2. Insert one new Authority Matrix row (M-B).
3. Reclassify V-07 and register two tracked follow-ups (M-C).
4. Record the T-05 annotation obligation (M-D).
5. Replace the location/placement recommendation (M-E).
6. Annotate the Status line (M-F).

**Forbidden in this change request:**

- Modifying `docs/design-tenets.md`, `MANIFESTO.md`, `docs/glossary.md` or any CognOS-Core file.
- Changing `Status` from `Proposed`.
- Adding governance taxonomies.
- Altering any existing citation.
- Editing sections not named above.

**Citation provenance.** They must be re-verified against the working tree at apply time.
Any reference that does not resolve must be flagged, not silently corrected.

---

## M-A — Scope limitation clause (F-04)

**Operation:** insert as the first paragraph of the **Precedence Rules** section, before rule 1.

```markdown
**Scope limitation.** The precedence order defined in this ADR governs the CognOS Ecosystem /
Vertical Module layer only. It does not restate, reorder, extend or amend the CognOS-Core
constitutional hierarchy (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:27–34`).
Where both hierarchies address the same subject, the Core hierarchy is authoritative for Core
runtime governance and this hierarchy is authoritative for Ecosystem engineering and repository
governance. This ADR claims no constitutional authority over CognOS-Core. Any change to the Core
hierarchy, or to the `R0–R4` / `A0–A4` taxonomies, requires a separate ADR accepted at
CognOS-Core level.
```

**Rationale:** F-04 identified that a 5-level Ecosystem hierarchy sitting beside a 7-level Core
hierarchy is readable as an attempted reordering of the Core. The clause removes the ambiguity
without changing either hierarchy.

---

## M-B — Authority Matrix row (F-05)

**Operation:** insert one row into the **Authority Matrix**, immediately after the
`Operational execution` row.

| Domain | Normative authority | Allowed specialization | Forbidden duplication | Conflict-resolution rule |
|---|---|---|---|---|
| Programme governance, security policy and policy-as-code (constitutional deny) | CognOS-Core — `GOVERNANCE.md` and `SECURITY.md` at Core hierarchy level 2 (`COGNOS_Architecture_Manifesto_v0.2.md:29`); policy-as-code / constitutional deny at level 4. Line ranges for `SECURITY.md`: `TO BE VERIFIED` | Ecosystem and repository-local processes may add **stricter** contribution gates, review requirements and CI checks | Restating or reinterpreting deny semantics (`CognOS-Core/GOVERNANCE.md:88–101`), gate blockers (`CognOS-Core/GOVERNANCE.md:128–140`) or AI/agent contributor constraints (`CognOS-Core/GOVERNANCE.md:22–30`) outside CognOS-Core | Core prevails. An Ecosystem or repository-local rule that weakens, narrows the applicability of, or reinterprets a deny rule or a gate blocker is void, not merely overridden |

**Rationale:** F-05 — Core level-2 authority had no representation in the matrix, leaving the
deny semantics and gate blockers without a declared owner in the Ecosystem view.

---

## M-C — Follow-up register (F-06)

**Operation A:** change the status of **V-07** from acceptance-blocking to deferred.

```markdown
| V-07 | T-04 annotated with its Core cross-references | DEFERRED — non-blocking for acceptance of this ADR. Core references already identified (see F-06). Tracked as FU-01. |
```

**Operation B:** append a `Follow-up Actions` sub-list at the end of the **Validation Criteria**
section (a sub-list, not a new top-level section — the ADR section structure is fixed).

```markdown
### Follow-up Actions

These items are tracked, non-blocking for the acceptance of this ADR, and must be resolved before
the Foundation Review concludes.

| ID | Action | Owner | Blocking for |
|---|---|---|---|
| FU-01 | Annotate `T-04` (`docs/design-tenets.md:75–88`) with its Core references: P1 (`v0.2:142–146`), P5 (`v0.2:173–191`), P6 (`v0.2:193–197`), D-003 (`v0.2:1015–1017`), D-008 (`v0.2:1035–1037`), D-009 (`v0.2:1039–1041`), Constitutional Invariant 1 (`v0.2:238`), Core ADR-0002. Requires a separate Eisman ADR — this ADR does not modify the Design Tenets. | Ecosystem Maintainer | Foundation Review |
| FU-02 | Annotate `T-05` (`docs/design-tenets.md:92–105`) per M-D below. Requires the same separate Eisman ADR. | Ecosystem Maintainer | Foundation Review |
```

---

## M-D — T-05 annotation obligation (F-08)

**Operation:** insert at the end of the **Cross-Domain Obligation Rule** (D4) subsection.

```markdown
**Applied instance — T-05 (Voice First).** Voice is a safety-adjacent domain and therefore falls
under this rule. `T-05` must carry an explicit reference to Core P4
(`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:159–171`) and to the trust constraints at
`:164–169`, which classify voice as `untrusted_ambient`: voice cannot authenticate, cannot
authorise, and cannot approve `R2–R4` side effects. `T-05`'s engineering intent does not
contradict P4; the annotation records the runtime boundary that P4 imposes on it.

The annotation is required by CR-03. Executing it modifies `docs/design-tenets.md` and is therefore
out of scope for this ADR; it is registered as **FU-02**.
```

**Note on asymmetry:** `T-04` and `T-05` are now handled identically — both obligations are
*recorded* here and *executed* under a separate ADR. This is deliberate: both require editing the
same protected document, so treating them differently would create an inconsistent precedent.

---

## M-E — Placement and scope declaration (Core split: NO)

**Operation:** replace the closing `Recommended location` paragraph in **References** with:

```markdown
**Location and scope (decided 2026-07-27).** This ADR resides in CognOS-Eisman at
`docs/adr/ADR-0001-normative-authority-and-precedence.md`. Its declared scope is
**Ecosystem / Vertical governance only**. It records and defers to CognOS-Core authority over
runtime safety, execution control, `R0–R4` and `A0–A4`; it does not exercise that authority.
No Core-side counterpart ADR is created at this time. A CognOS-Core ADR becomes necessary only if
the Core document hierarchy or the Core taxonomies are to be formally modified.
```

---

## M-F — Status annotation

**Operation:** in the **Status** section, keep `Proposed` and append:

```markdown
`Proposed` — **Ready for Human Acceptance**.

All evidence-based validation criteria are satisfied (see Validation Criteria). The only remaining
condition is explicit approval by the Human Project Owner. This ADR must not be marked `Accepted`
by any automated process.
```

---

## Post-apply verification

The change is correctly applied when all of the following hold:

- [ ] The scope-limitation clause appears once, at the head of Precedence Rules.
- [ ] The Authority Matrix has exactly one new row and eleven rows in total.
- [ ] `V-07` reads DEFERRED and references FU-01.
- [ ] `FU-01` and `FU-02` both appear in the Follow-up Actions table.
- [ ] `docs/design-tenets.md` is **unmodified** (`git diff --stat` shows only the ADR file).
- [ ] `Status` still reads `Proposed`.
- [ ] No CognOS-Core file appears in `git status`.
- [ ] Every `file:line` reference introduced by this CR resolves in the working tree, or is
      explicitly flagged as unresolved in the apply report.
