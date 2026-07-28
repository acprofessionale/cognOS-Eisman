# ADR-0001 — Normative Authority and Governance Precedence
*Status: Proposed*
*Date: 2026-07-27*
*Decision Owners: CognOS Project Owner (human approval required before this ADR moves to Accepted)*


---

## Context

The CognOS Ecosystem currently operates with two normative governance sources that have not been given explicit, documented precedence over each other.

**Source 1 — CognOS-Core Architecture Manifesto**
- Document: `COGNOS_Architecture_Manifesto_v0.2` — authoritative version as of 2026-07-22 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md`). v0.1 retained as historical artefact per `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1127–1129`.
- Claimed authority: Constitutional baseline — highest normative authority in the Core document hierarchy (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:15–36`). Also normative: `CognOS-Core/GOVERNANCE.md` and `CognOS-Core/SECURITY.md` (level 2); Accepted ADRs (`CognOS-Core/docs/architecture/adr/`) (level 3).
- Contents verified:
  - Principles P1–P10: `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:141–231`
  - Constitutional invariants §5-bis (10 non-overridable release-validity conditions): `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:234–249`; normalised by `CognOS-Core/docs/architecture/adr/ADR-0004-constitutional-invariants-fail-closed-authority.md:27–30`
  - Decisions D-001–D-016 (v0.2 expanded from D-001–D-010 in v0.1): `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1006–1069`
  - Risk classification R0–R4: `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:174–191`; also `CognOS-Core/docs/GLOSSARY.md:71`; `CognOS-Core/GOVERNANCE.md:74`
  - Autonomy classification A0–A4: `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:778–785`; also `CognOS-Core/docs/GLOSSARY.md:73`; `CognOS-Core/GOVERNANCE.md:80–84`
- **Verification status: VERIFIED 2026-07-27. Full content of v0.2, GLOSSARY.md, GOVERNANCE.md, and ADR-0001/0002/0003/0004 read in their entirety. All `[TO BE VERIFIED]` markers replaced in this revision.**
- **Scope correction: v0.2 defines D-001–D-016, not D-001–D-010. D-011 (natural language non-authority), D-012 (untrusted outputs), D-013 (exact-argument authorization), D-014 (state as projection), D-015 (proprietary baseline), and D-016 (constitutional deny) were introduced in v0.2 and are normatively binding. All references below to "D-001–D-010" are corrected to "D-001–D-016" where applicable.**

**Source 2 — CognOS Ecosystem Design Tenets**
- Document: `docs/design-tenets.md` (CognOS-Eisman repository)
- Claimed authority: "Immutable engineering principles inherited by every CognOS repository" (`docs/design-tenets.md:3`)
- Contents: Engineering tenets T-01 through T-12 (`docs/design-tenets.md:24–225`)
- **Verification status: Fully accessible and read in its entirety.**

**Structural gap identified:**
The CognOS-Eisman repository README.md states: "The shared core — CognOS-Core — provides the common infrastructure, governance framework, and architectural conventions that all verticals inherit" (`README.md:131–132`). However, no document in CognOS-Eisman defines the boundary between what CognOS-Core governs and what the Ecosystem governs. The Design Tenets claim authority over "every CognOS repository" (`docs/design-tenets.md:260`) without specifying their relationship to CognOS-Core rules that may concern the same domains.

**Phase context:**
CognOS-Eisman is currently in Phase 0 (Bootstrap), as documented in `ROADMAP.md:26–61`. The `docs/adr/` directory is empty at time of authorship. This is the first ADR in the repository.

---

## Problem Statement

Two normative sources exist without an explicit precedence rule. In any domain where both sources could plausibly apply — particularly domains touching human accountability, automated behavior, and decision authority — authors, contributors, and reviewers cannot determine which source governs without subjective interpretation.

Specific failure modes without this ADR:

1. A Vertical Module design tenet could introduce a risk taxonomy that partially overlaps with R0–R4 (defined at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:174–191`; `CognOS-Core/docs/GLOSSARY.md:71`), creating two competing classification systems with no resolution rule.
2. A Vertical Module design tenet could define autonomy levels that differ from A0–A4 (defined at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:778–785`; `CognOS-Core/docs/GLOSSARY.md:73`), producing ambiguous operational constraints for agents built on CognOS-Core.
3. A CognOS-Core runtime rule could be applied to engineering governance decisions (documentation format, review process) in ways not appropriate to its authority domain.
4. Future ADRs in any vertical could unknowingly contradict a CognOS-Core principle because the cross-reference obligation was never documented.

T-04 (Human Accountability, `docs/design-tenets.md:75–88`) currently states: "Every automated behavior must be auditable and reversible by the operator." This statement touches execution safety — a domain governed by: P1 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:142–146`), P5 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:173–191`), P6 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:193–197`), D-003 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1015–1017`), D-008 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1035–1037`), D-009 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1039–1041`), Constitutional Invariant 1 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:238`), and Core ADR-0002 (`CognOS-Core/docs/architecture/adr/ADR-0002-human-in-the-loop-baseline.md`). Without this ADR, T-04 and the corresponding CognOS-Core execution rules operate in parallel without a defined relationship.

---

## Decision

### 1. Authority Domain Allocation

**CognOS Ecosystem Design Tenets** (`docs/design-tenets.md`) are the normative authority for:

- Software engineering principles (including all T-01–T-12 as currently written)
- Documentation standards and formats
- Repository governance (contribution process, review process, naming conventions)
- Modularity and interface design
- Interoperability between modules and verticals
- Architecture practices (ADR process, module contracts, design-before-build)
- Contribution practices
- Knowledge-management practices (glossary, prompt library, documentation as first-class artifact)
- Model-agnostic design requirements (T-06, `docs/design-tenets.md:109–123`)
- Explainability requirements for AI-generated outputs (T-10, `docs/design-tenets.md:178–191`)

These domains are governed at the Ecosystem layer. CognOS-Core does not override Ecosystem governance in these domains.

---

**CognOS-Core Architecture Manifesto** (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md` — ratified 2026-07-22) is the normative authority for:

- Runtime safety constraints — governed by P7 Safety by design (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:199–215`) and constitutional invariants §5-bis (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:234–249`)
- Execution control and operational permission levels — governed by D-001–D-016 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1006–1069`); key operational decisions are D-008 (auditabilità fail-closed), D-009 (autonomia progressiva governata), D-011 (natural language non-authority), D-013 (exact-argument authorization), D-016 (constitutional deny)
- Operational risk classification: **R0–R4 taxonomy is defined exclusively in CognOS-Core** (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:174–191`; `CognOS-Core/docs/GLOSSARY.md:71`; `CognOS-Core/GOVERNANCE.md:74`)
- Agent autonomy classification: **A0–A4 taxonomy is defined exclusively in CognOS-Core** (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:778–785`; `CognOS-Core/docs/GLOSSARY.md:73`; `CognOS-Core/GOVERNANCE.md:80–84`)
- Human approval requirements for agent actions at runtime — governed by P5 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:173–191`) and Core ADR-0002 (`CognOS-Core/docs/architecture/adr/ADR-0002-human-in-the-loop-baseline.md`)
- Irreversible action handling and approval gates — governed by P5 (R3/R4 require explicit human approval: `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:189–191`) and Constitutional Invariant 4 (fail closed: `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:241`)
- Security-sensitive operation constraints — governed by P7 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:199–215`) and Core ADR-0004 (`CognOS-Core/docs/architecture/adr/ADR-0004-constitutional-invariants-fail-closed-authority.md`)
- Production execution constraints — governed by D-008 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1035–1037`) and Constitutional Invariant 5 (constitutional deny non-overridable: `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:242`)

The taxonomies R0–R4 and A0–A4 must not be duplicated, extended, or redefined in any Ecosystem document, Vertical Module document, or repository-local rule. Reference is required; redefinition is forbidden.

---

### 2. Cross-Domain Obligation Rule

Any Design Tenet (T-01–T-12 or future tenets) whose subject matter intersects the following domains:

- Safety
- Risk
- Autonomy
- Approval requirements for agent or automated actions
- Execution permissions
- Irreversible operations

**must** include an explicit reference to the relevant CognOS-Core principle or classification. It must not create a parallel classification or define behavior that supersedes CognOS-Core execution rules.

**Current tenet requiring annotation:** T-04 (`docs/design-tenets.md:75–88`) states: "Every automated behavior must be auditable and reversible by the operator." This statement intersects execution safety. Upon acceptance of this ADR, T-04 must be annotated with the following verified Core references: P1 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:142–146`), P5 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:173–191`), P6 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:193–197`), D-003 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1015–1017`), D-008 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1035–1037`), D-009 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1039–1041`), Constitutional Invariant 1 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:238`), Core ADR-0002 (`CognOS-Core/docs/architecture/adr/ADR-0002-human-in-the-loop-baseline.md`). No substantive change to T-04 text is required — only the cross-reference annotation.

**Additional tenet requiring annotation:** T-05 (Voice First, `docs/design-tenets.md:92–105`) also intersects these domains. Its obligation, verified Core citations, and follow-up registration are stated in full in the applied instance below and are not restated here.

**CONSTRAINT:** This ADR does not authorize modification of T-04, T-05, or any other tenet. Those actions each require a separate ADR.

**Applied instance — T-05 (Voice First).** T-05 (`docs/design-tenets.md:92–105`) covers voice as an
input channel for CognOS interactions. Voice is a safety-adjacent domain and therefore falls
under this rule. `T-05` must carry an explicit reference to Core P4
(`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:159–171`) and to the voice constraints at
`:164–169`, which establish that voice is not identity, is not authentication, is not
authorisation, cannot alone approve `R2–R4` side effects, and must be marked with `channel_trust`
(`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:169`).
P4 states the marking obligation but not the value of that marking. The literal `untrusted_ambient`
classification is defined in the Core normative vocabulary at `CognOS-Core/docs/GLOSSARY.md:63`
("Channel trust — … la voce ambientale è `untrusted_ambient` e non autentica né autorizza"), is
applied to the voice flow at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:737` (§11
Interazione vocale — `channel_trust = untrusted_ambient`), and is carried as a binding
security-policy requirement at `CognOS-Core/SECURITY.md:56` ("voice/ambient input marcato
`untrusted_ambient`"). Constitutional Invariant 9
(`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:246`) states: "Voice is expressive, not
authoritative." T-05 and P4 are compatible and address complementary domains (T-05 governs
engineering design; P4 governs runtime channel-trust semantics), but T-05's subject matter
intersects the channel-trust and authorization boundary governed by Core. `T-05`'s engineering
intent does not contradict P4; the annotation records the runtime boundary that P4 and the
`untrusted_ambient` channel-trust classification impose on it.

Upon acceptance of this ADR, T-05 must be annotated with a reference to Core P4
(`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:159–171`), D-006
(`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1026–1028`), and Constitutional
Invariant 9 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:246`). No substantive change
to T-05 text is required — only the cross-reference annotation.

The annotation is required by CR-03 (safety-adjacent tenet cross-reference). Executing it modifies
`docs/design-tenets.md` and is therefore out of scope for this ADR; it is registered as **FU-02**.

---

### 3. Repository-Local Specialization Rule

Vertical Module repositories (such as CognOS-Eisman) may define repository-local implementation rules that:
- Specialize Ecosystem tenets for local context (example: specifying voice-first testing procedures specific to CognOS-Eisman's ice cream truck domain, consistent with T-05, `docs/design-tenets.md:92–105`)
- Add constraints more restrictive than the governing level

Repository-local rules may not:
- Contradict Ecosystem tenets
- Contradict CognOS-Core runtime safety or execution rules
- Substitute for or redefine any R0–R4 or A0–A4 classification

---

## Authority Matrix

| Domain | Normative Authority | Allowed Specialization | Forbidden Duplication | Conflict Resolution |
|---|---|---|---|---|
| Engineering principles | Ecosystem Design Tenets (`docs/design-tenets.md:1–260`) | Vertical Modules may add more specific engineering rules consistent with T-01–T-12 | No vertical may define an alternative principle set that contradicts T-01–T-12 | Ecosystem tenets prevail over vertical-local rules |
| Documentation standards | Ecosystem Design Tenets (T-01, T-02, T-12; `docs/design-tenets.md:24–54, 211–225`) | Verticals may define specific document formats consistent with Ecosystem standards | No vertical may exempt itself from documentation requirements | Ecosystem standards prevail; document format disputes escalate to ADR |
| Repository governance | Ecosystem (CONTRIBUTING.md, ADR process, glossary — `CONTRIBUTING.md:1–211`, `docs/glossary.md:1–159`) | Verticals may add contribution rules specific to their domain | No vertical may remove required governance steps (ADR-before-implementation, module contracts) | Ecosystem governance rules prevail |
| Runtime safety | CognOS-Core Manifesto v0.2 — P7 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:199–215`); constitutional invariants §5-bis (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:234–249`); ADR-0004 (`CognOS-Core/docs/architecture/adr/ADR-0004-constitutional-invariants-fail-closed-authority.md`) | Verticals may implement safety checks additional to Core requirements | No vertical may reduce or bypass Core safety constraints | CognOS-Core prevails unconditionally; law and security policy prevail over Core |
| Risk classification | CognOS-Core Manifesto v0.2 exclusively — R0–R4 defined at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:174–191`; `CognOS-Core/docs/GLOSSARY.md:71`; `CognOS-Core/GOVERNANCE.md:74` | None permitted — taxonomy must be used as defined | No document outside CognOS-Core may define R0–R4 or an alternative risk taxonomy | CognOS-Core prevails; any parallel taxonomy is a governance violation |
| Autonomy classification | CognOS-Core Manifesto v0.2 exclusively — A0–A4 defined at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:778–785`; `CognOS-Core/docs/GLOSSARY.md:73`; `CognOS-Core/GOVERNANCE.md:80–84` | None permitted — taxonomy must be used as defined | No document outside CognOS-Core may define A0–A4 or an alternative autonomy taxonomy | CognOS-Core prevails; any parallel taxonomy is a governance violation |
| Human approval requirements | CognOS-Core Manifesto v0.2 (runtime gate requirements) — P5 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:173–191`), D-003 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1015–1017`), D-009 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1039–1041`), Core ADR-0002 (`CognOS-Core/docs/architecture/adr/ADR-0002-human-in-the-loop-baseline.md`); Ecosystem T-04 (`docs/design-tenets.md:75–88`) for engineering design principle | T-04 governs design intent; CognOS-Core governs operational gate implementation | No vertical may remove human approval gates defined by CognOS-Core | CognOS-Core runtime requirement prevails over design intent in operational execution |
| AI-provider selection | Ecosystem Design Tenets (T-06, `docs/design-tenets.md:109–123`) | Verticals may document specific provider integrations consistent with T-06 | No vertical may mandate a single AI provider or skip the abstraction layer required by T-06 | T-06 prevails; provider-specific designs require an ADR per T-06:120–122 |
| Module-local implementation | Ecosystem tenets (T-07, T-11; `docs/design-tenets.md:127–139, 199–208`) + vertical module contract | Module contract governs implementation scope | No module may exceed its documented contract without an updated ADR | Module contract prevails; contract disputes escalate to ADR |
| Operational execution | CognOS-Core Manifesto v0.2 — D-001–D-016 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1006–1069`); R0–R4 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:174–191`); A0–A4 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:778–785`); constitutional invariants §5-bis (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:234–249`) | Verticals implement within Core-defined permission levels | No vertical may execute operations classified by Core as requiring approval without obtaining that approval | CognOS-Core prevails unconditionally in production execution contexts |
| Programme governance, security policy and policy-as-code (constitutional deny) | CognOS-Core — `GOVERNANCE.md` and `SECURITY.md` at Core hierarchy level 2 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:29`); policy-as-code / constitutional deny at level 4 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:31`). Verified line ranges for `SECURITY.md` (`CognOS-Core/SECURITY.md:1–179`, current main as of 2026-07-27): security posture `:3–7`; security invariants `:15–25`; identity, channel and approval `:52–60`; risk and execution control `:74–88`; deny semantics — constitutional and policy deny `:90–98`; fail-closed and degraded mode `:114–129`; security release gates `:152–164` | Ecosystem and repository-local processes may add **stricter** contribution gates, review requirements and CI checks | Restating or reinterpreting deny semantics (`CognOS-Core/GOVERNANCE.md:88–101`), gate blockers (`CognOS-Core/GOVERNANCE.md:128–140`) or AI/agent contributor constraints (`CognOS-Core/GOVERNANCE.md:22–30`) outside CognOS-Core | Core prevails. An Ecosystem or repository-local rule that weakens, narrows the applicability of, or reinterprets a deny rule or a gate blocker is void, not merely overridden |
| CognOS-Core internal governance hierarchy | CognOS-Core exclusively — governed by the Core Manifesto hierarchy: (1) `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md` (constitutional baseline); (2) `CognOS-Core/GOVERNANCE.md` and `CognOS-Core/SECURITY.md` (level 2: roles, deny semantics, gate blockers); (3) Accepted Core ADRs (`CognOS-Core/docs/architecture/adr/`); (4) policy-as-code and constitutional deny mechanisms (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:234–249`; `CognOS-Core/docs/architecture/adr/ADR-0004-constitutional-invariants-fail-closed-authority.md`); (5) runtime enforcement controls | The Ecosystem layer may reference and acknowledge these authorities; verticals may implement controls consistent with them | No Ecosystem document, Vertical Module, or Ecosystem ADR may redefine, reorder, override, or extend the Core internal hierarchy. Cross-referencing is required; substitution is forbidden | The Core internal hierarchy is self-governing. Conflicts inside the Core boundary are resolved by Core governance processes, not by this ADR |

---

## Precedence Rules

**Scope limitation.** The precedence order defined in this ADR governs the CognOS Ecosystem /
Vertical Module layer only. It does not restate, reorder, extend or amend the CognOS-Core
constitutional hierarchy (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:27–34`).
Where both hierarchies address the same subject, the Core hierarchy is authoritative for Core
runtime governance and this hierarchy is authoritative for Ecosystem engineering and repository
governance. This ADR claims no constitutional authority over CognOS-Core. Any change to the Core
hierarchy, or to the `R0–R4` / `A0–A4` taxonomies, requires a separate ADR accepted at
CognOS-Core level.

**Scope of this hierarchy:** The precedence order below governs the CognOS Ecosystem layer, Vertical Modules, repository engineering governance, and cross-repository architectural relationships. It does **not** replace, reorder, or supersede the internal constitutional hierarchy of CognOS-Core. The CognOS-Core internal hierarchy — Manifesto → GOVERNANCE.md/SECURITY.md → Accepted Core ADRs → policy-as-code/constitutional deny → schemas/protocols → registry → implementation (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:27–36`; `CognOS-Core/GOVERNANCE.md:35–42`) — remains authoritative inside the Core runtime and security boundary. This ADR is a governance instrument of the Ecosystem layer that acknowledges Core authority; it is not a constitutional instrument of the Core. Contributors must not apply this ADR's precedence order to resolve conflicts inside the Core boundary.

The following total order of precedence applies when any two governance sources conflict:

1. **Applicable law, contractual obligations, and security policy** — override all CognOS governance sources without exception.
2. **CognOS-Core runtime safety and execution rules** (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md` — P1–P10 at lines 141–231; constitutional invariants §5-bis at lines 234–249; D-001–D-016 at lines 1006–1069; `CognOS-Core/GOVERNANCE.md`; `CognOS-Core/docs/architecture/adr/ADR-0004-constitutional-invariants-fail-closed-authority.md`) — prevail over all CognOS governance sources in operational execution contexts. Constitutional invariants §5-bis are non-overridable release-validity conditions that take precedence even over Accepted ADRs within the Core hierarchy.
3. **CognOS Ecosystem Design Tenets** (`docs/design-tenets.md`, T-01–T-12) — prevail over repository-local rules in software engineering and repository governance domains.
4. **Repository-local rules** — may specialize higher-level rules in ways more restrictive than the parent rule; may never contradict a higher-level authority.
5. **ADRs** — may supersede previous ADRs only by explicit declaration (`Supersedes: ADR-XXXX`) and may not silently override any higher-level authority. An ADR that contradicts a Design Tenet or CognOS-Core rule is invalid until the parent document is explicitly amended.

**Conflict detection obligation:** Any contributor who identifies a conflict between two governance levels must open an issue or discussion immediately. Conflicts may not be resolved by private interpretation. They require an ADR.

---

## Consequences

### Positive Consequences

1. **Unambiguous authority assignment.** Every governance question can now be answered by determining which domain it falls in, rather than by subjective interpretation.
2. **Protection of the R0–R4 and A0–A4 taxonomies.** These classifications cannot be diluted by parallel definitions in Vertical Modules or Ecosystem documents. Their meaning is stable across the entire system.
3. **Defined cross-reference obligation.** Safety-adjacent Design Tenets (currently T-04) must reference CognOS-Core. This prevents silent divergence between engineering intent and runtime enforcement.
4. **Foundation for future ADRs.** All subsequent ADRs in CognOS-Eisman and future Vertical Modules inherit a clear authority hierarchy. Future governance conflicts have a documented resolution procedure.
5. **Alignment with T-01, T-03, T-10.** This ADR documents the authority structure before any implementation depends on it (`docs/design-tenets.md:28–37, 59–71, 178–191`). It is itself an example of governance-before-implementation.

### Negative Consequences

1. **Cross-reference maintenance burden.** Every safety-adjacent tenet addition or modification must now include a CognOS-Core reference. Contributors must know what CognOS-Core contains — which requires CognOS-Core to be accessible and well-documented.
2. **CognOS-Core access dependency.** ~~This ADR defines obligations toward CognOS-Core content that is currently inaccessible.~~ **RESOLVED 2026-07-27:** Full cross-repository validation completed. All formerly unresolved obligations are now documented with exact file-path and line-range citations. Residual dependency: CognOS-Core remains a separate repository; contributors must have access to both repositories to fulfill CR-03 and CR-04 independently.
3. **Increased ADR workload.** Decisions that previously could be made locally now require explicit authority-level attribution. The ADR process becomes the mandatory path for any cross-domain governance question.

---

## Risks

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| CognOS-Core Manifesto content contradicts Design Tenets upon inspection | High | Medium | Validation criteria below require cross-inspection before acceptance; conflicts escalate to human decision |
| CognOS-Core access — formerly unresolved items | High → **RESOLVED** | Medium → **CLOSED** | Cross-repository validation completed 2026-07-27; all citations verified. Residual: contributors need access to both repositories. |
| Contributors apply Precedence Rule 2 (Core prevails) to software engineering decisions inappropriately | Medium | Low | Authority Matrix explicitly scopes Core authority to operational execution; training and onboarding documentation must cite this ADR |
| Future Design Tenets (T-13+) unintentionally define safety behavior without Core reference | Medium | Medium | Compliance rule below requires every new tenet to be reviewed against this ADR before acceptance |
| This ADR is superseded implicitly by a future repository-local decision | Low | Low | Supersession Rules below require explicit declaration; implicit overrides are invalid |

---

## Compliance Rules

The following rules are active from the date this ADR is accepted:

**CR-01 — No parallel risk taxonomy.** No document in CognOS-Eisman or any CognOS Vertical Module may define a risk classification that overlaps with R0–R4 (defined at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:174–191`; `CognOS-Core/docs/GLOSSARY.md:71`). Risk levels in Vertical Modules must reference CognOS-Core R-classifications by identifier.

**CR-02 — No parallel autonomy taxonomy.** No document in CognOS-Eisman or any CognOS Vertical Module may define an autonomy level that overlaps with A0–A4 (defined at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:778–785`; `CognOS-Core/docs/GLOSSARY.md:73`). Autonomy levels must reference CognOS-Core A-classifications by identifier.

**CR-03 — Safety-adjacent tenet cross-reference.** Any Design Tenet whose rationale, implications, or violation description concerns safety, risk, approval requirements, irreversible operations, or execution permissions must include an explicit `Core Reference:` field citing the applicable CognOS-Core principle or classification by identifier.

**CR-04 — ADR cross-reference obligation.** Any ADR in CognOS-Eisman that makes a decision in a domain also governed by CognOS-Core must explicitly state which CognOS-Core principle or classification applies and confirm that the ADR decision is consistent with it.

**CR-05 — Supersession must be explicit.** Any future ADR that modifies the authority boundaries defined in this document must declare `Supersedes: ADR-0001` and must not reduce the authority of higher-level governance sources.

---

## Validation Criteria

This ADR may move from `Proposed` to `Accepted` only when ALL of the following conditions have been confirmed by the human project owner:

| # | Criterion | Verification Method | Status |
|---|---|---|---|
| V-01 | CognOS-Core Manifesto has been located and its full content confirmed | Human provides file path and access to CognOS-Core; reviewer confirms document existence | **MET — authoritative document is `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md` (v0.2, 2026-07-22, 1170 lines). Full content read 2026-07-27. Note: ADR-0001 was authored referencing v0.1; v0.2 is now the normative reference. All citations updated accordingly.** |
| V-02 | All P1–P10 have been read and confirmed consistent with this ADR's authority allocation | Human or designated reviewer reads P1–P10 against Section "Decision" and Authority Matrix | **MET — P1–P10 read at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:141–231`. All principles fall within the "runtime safety / execution / human accountability" domain assigned to Core in the Authority Matrix. No principle contradicts the Ecosystem tenet allocation.** |
| V-03 | All D-001–D-016 have been read and confirmed consistent with this ADR's authority allocation | Human or designated reviewer reads D-001–D-016 against Section "Decision" and Authority Matrix | **MET WITH SCOPE CORRECTION — v0.2 defines D-001–D-016 (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:1006–1069`), not D-001–D-010 as stated at authorship. D-011–D-016 (natural language non-authority, untrusted outputs, exact-argument authorization, state as projection, proprietary baseline, constitutional deny) are all normatively binding and consistent with this ADR's authority allocation. All references to "D-001–D-010" in this ADR have been corrected.** |
| V-04 | T-01–T-12 have been reviewed against P1–P10; no tenet redefines or contradicts any Core principle | Systematic comparison, documented as an appendix or separate review record | **MET — T-01–T-12 (`docs/design-tenets.md:24–225`) are engineering governance principles (documentation, modularity, architecture-before-implementation, model-agnostic design). None redefines, duplicates, or contradicts P1–P10. T-04/P1/P5 and T-06/P3 address complementary domains at different governance layers without conflict.** |
| V-05 | No Design Tenet (T-01–T-12) redefines R0–R4 | Confirmed: T-01–T-12 as read contain no risk taxonomy. Tenets are engineering principles, not operational classifiers. (`docs/design-tenets.md:24–225`) | **MET — T-01–T-12 contain no risk taxonomy. R0–R4 are defined exclusively in Core at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:174–191` and `CognOS-Core/docs/GLOSSARY.md:71`. No Eisman document (design-tenets.md, glossary.md, MANIFESTO.md) defines or references R0–R4.** |
| V-06 | No Design Tenet (T-01–T-12) redefines A0–A4 | Confirmed: T-01–T-12 as read contain no autonomy classification. (`docs/design-tenets.md:24–225`) | **MET — T-01–T-12 contain no autonomy classification. A0–A4 are defined exclusively in Core at `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:778–785` and `CognOS-Core/docs/GLOSSARY.md:73`. No Eisman document defines or references A0–A4.** |
| V-07 | T-04 annotated with its Core cross-references | The applicable Core references have been identified and are recorded in this ADR (Problem Statement; Cross-Domain Obligation Rule): P1 (`v0.2:142–146`), P5 (`v0.2:173–191`), P6 (`v0.2:193–197`), D-003 (`v0.2:1015–1017`), D-008 (`v0.2:1035–1037`), D-009 (`v0.2:1039–1041`), Constitutional Invariant 1 (`v0.2:238`), Core ADR-0002. Applying the annotation modifies `docs/design-tenets.md` and is tracked as **FU-01**. FU-01 is blocking for completion of the Foundation Review, **not** for acceptance of this ADR. No annotation is required before acceptance. | DEFERRED — non-blocking for acceptance of this ADR. The applicable CognOS-Core references have been identified and are recorded in this ADR (Problem Statement; Cross-Domain Obligation Rule). Applying the annotation to `docs/design-tenets.md` is tracked as FU-01, which is non-blocking for acceptance of this ADR and blocking for completion of the Foundation Review. |
| V-08 | Authority Matrix has no unresolved ownership overlaps | All 12 matrix data rows reviewed; overlaps documented and assigned | **MET — 12 data rows verified against Core v0.2. Eleven rows predate CR-01; CR-01 added exactly one row (Programme governance, security policy and policy-as-code), giving twelve data rows in total. That row closes the finding previously recorded here: Core v0.2 §0 places GOVERNANCE.md and SECURITY.md at level 2 of the Core hierarchy (`CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md:29`), and this authority is now represented in the Authority Matrix. All `[TO BE VERIFIED]` and `TO BE VERIFIED` markers are resolved against CognOS-Core current main. No unresolved ownership overlaps remain.** |
| V-09 | Human project owner explicitly approves this ADR in writing | Written approval recorded (GitHub PR approval, meeting minutes, or equivalent) | **OPEN — required** |

### Follow-up Actions

These items are tracked, non-blocking for the acceptance of this ADR, and must be resolved before
the Foundation Review concludes.

| ID | Action | Owner | Blocking for |
|---|---|---|---|
| FU-01 | Annotate `T-04` (`docs/design-tenets.md:75–88`) with its Core references: P1 (`v0.2:142–146`), P5 (`v0.2:173–191`), P6 (`v0.2:193–197`), D-003 (`v0.2:1015–1017`), D-008 (`v0.2:1035–1037`), D-009 (`v0.2:1039–1041`), Constitutional Invariant 1 (`v0.2:238`), Core ADR-0002. Requires a separate Eisman ADR — this ADR does not modify the Design Tenets. | Ecosystem Maintainer | Foundation Review |
| FU-02 | Annotate `T-05` (`docs/design-tenets.md:92–105`) with its Core references, as specified in section 2 (Cross-Domain Obligation Rule) of this ADR: P4 (`v0.2:159–171`), D-006 (`v0.2:1026–1028`), Constitutional Invariant 9 (`v0.2:246`), and the `untrusted_ambient` channel-trust classification (`CognOS-Core/docs/GLOSSARY.md:63`). Requires the same separate Eisman ADR — this ADR does not modify the Design Tenets. | Ecosystem Maintainer | Foundation Review |

---

## Supersession Rules

1. This ADR (ADR-0001) establishes the foundational authority hierarchy for CognOS-Eisman.
2. Any ADR that modifies the authority hierarchy defined here must explicitly declare `Supersedes: ADR-0001` in its header.
3. A superseding ADR may not reduce the precedence of law, security policy, or CognOS-Core runtime safety rules. It may only modify Ecosystem-level and repository-local authority assignments.
4. Partial supersession is permitted: an ADR may supersede specific sections of this document without replacing it entirely, provided the superseding sections and the unchanged sections do not create a contradiction.
5. Silent override — any implementation or document that contradicts this ADR without an explicit superseding ADR — is a governance violation.

---

## References

**CognOS-Eisman (verified — accessible at authorship):**
- `docs/design-tenets.md` — T-01–T-12, Design Tenets v1.0 July 2026 (lines 1–260)
- `docs/design-tenets.md:3` — claimed authority ("Immutable engineering principles inherited by every CognOS repository")
- `docs/design-tenets.md:24–38` — T-01 Knowledge Before Code
- `docs/design-tenets.md:42–54` — T-02 Documentation is a First-Class Artifact
- `docs/design-tenets.md:58–71` — T-03 Architecture Before Implementation
- `docs/design-tenets.md:75–88` — T-04 Human Accountability (safety-adjacent; cross-reference to Core required)
- `docs/design-tenets.md:92–105` — T-05 Voice First
- `docs/design-tenets.md:109–123` — T-06 Model Agnostic
- `docs/design-tenets.md:127–139` — T-07 Modular by Default
- `docs/design-tenets.md:143–157` — T-08 Simplicity Over Complexity
- `docs/design-tenets.md:161–173` — T-09 Everything Evolves
- `docs/design-tenets.md:177–191` — T-10 Every Decision Must Be Explainable
- `docs/design-tenets.md:195–208` — T-11 Every Module Must Be Replaceable
- `docs/design-tenets.md:211–225` — T-12 Knowledge is Permanent. Code is Temporary.
- `docs/design-tenets.md:248–255` — Tenet change process (ADR required)
- `MANIFESTO.md:1–148` — CognOS Ecosystem Manifesto v1.0 July 2026
- `MANIFESTO.md:36–44` — "Humans remain responsible" (philosophical basis for T-04)
- `README.md:131–132` — CognOS-Core described as providing "common infrastructure, governance framework, and architectural conventions"
- `ROADMAP.md:26–61` — Phase 0 Bootstrap, current phase
- `ROADMAP.md:144–153` — Phase 4 objective: formal CognOS-Core separation
- `docs/glossary.md:40–43` — CognOS-Core defined as "architectural contract" not a software library
- `docs/glossary.md:106–109` — ADR defined as "immutable once accepted, never deleted, only superseded"
- `CONTRIBUTING.md:59–68` — ADR requirement before architecture changes

**CognOS-Core (VERIFIED — full content read 2026-07-27):**
- `CognOS-Core/docs/COGNOS_Architecture_Manifesto_v0.2.md` — authoritative constitutional reference (v0.2, 2026-07-22, 1170 lines)
  - P1–P10 (foundational principles): lines 141–231
  - Constitutional invariants §5-bis (10 non-overridable conditions): lines 234–249
  - R0–R4 (risk classification): lines 174–191
  - A0–A4 (autonomy classification): lines 778–785
  - D-001–D-016 (foundational decisions): lines 1006–1069
  - Document hierarchy §0: lines 27–36
- `CognOS-Core/docs/GLOSSARY.md` — normative vocabulary; R0–R4 at line 71; A0–A4 at line 73
- `CognOS-Core/GOVERNANCE.md` — level 2 authority per v0.2 §0; roles and deny semantics; R0–R4 governance at line 74; A0–A4 levels at lines 80–84; gate blockers at lines 128–140
- `CognOS-Core/docs/architecture/adr/ADR-0001-capability-centric-cognitive-os.md` — Accepted; defines capability-centric architecture
- `CognOS-Core/docs/architecture/adr/ADR-0002-human-in-the-loop-baseline.md` — Accepted; defines A0–A1 baseline and R3/R4 deny-by-default
- `CognOS-Core/docs/architecture/adr/ADR-0003-regime-terminal-first-domain-pilot.md` — Accepted; defines read-only Regime Terminal constraints
- `CognOS-Core/docs/architecture/adr/ADR-0004-constitutional-invariants-fail-closed-authority.md` — Accepted on merge of PR #4; formalises fail-closed, exact-argument authorization, deny semantics, and self-modifying authority prohibition

**Location and scope (decided 2026-07-27).** This ADR resides in CognOS-Eisman at
`docs/adr/ADR-0001-normative-authority-and-precedence.md`. Its declared scope is
**Ecosystem / Vertical governance only**. It records and defers to CognOS-Core authority over
runtime safety, execution control, `R0–R4` and `A0–A4`; it does not exercise that authority.
No Core-side counterpart ADR is created at this time. A CognOS-Core ADR becomes necessary only if
the Core document hierarchy or the Core taxonomies are to be formally modified.

---

*ADR-0001 — Normative Authority and Governance Precedence*
*Authored: 2026-07-27*
*Author role: Independent Enterprise Architect and Governance Reviewer*
