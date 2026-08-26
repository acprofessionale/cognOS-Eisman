```markdown
# cognOS-Eisman Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill outlines the key development practices and workflows used in the `cognOS-Eisman` TypeScript codebase. It covers file organization, code style, commit conventions, and the process for managing Architecture Decision Records (ADRs). Use this guide to contribute code and documentation that aligns with project standards.

## Coding Conventions

### File Naming

- Use **kebab-case** for all file names.
  - Example: `user-profile.ts`, `data-fetcher.test.ts`

### Import Style

- Use **relative imports** for referencing modules.
  - Example:
    ```typescript
    import { fetchData } from './data-fetcher';
    ```

### Export Style

- Use **named exports** for all modules.
  - Example:
    ```typescript
    // In user-profile.ts
    export function getUserProfile(id: string) { ... }
    ```

### Commit Messages

- Follow **conventional commit** style.
  - Prefixes: `fix`, `docs`
  - Example:
    ```
    fix: correct user profile fetch logic
    docs: update ADR ratification process
    ```
- Keep commit messages concise (average ~46 characters).

## Workflows

### ADR Lifecycle Management

**Trigger:** When you need to update the status of an Architecture Decision Record (ADR), such as ratifying, reverting, or providing supporting evidence.

**Command:** `/adr-status-update`

#### Step-by-Step Instructions

1. **Edit the ADR Markdown File**
   - Navigate to `docs/adr/ADR-*.md`.
   - Update the status field or content as needed.
   - Example:
     ```markdown
     # ADR-001: Use TypeScript
     Status: Ratified
     ```

2. **Update or Create Supporting Files**
   - If ratifying, create or update the corresponding review file in `docs/reviews/ADR-*-RATIFICATION.md`.
   - For status changes or evidence, update or create a change request file in `docs/adr/CR-*-adr-*-change-request.md`.
   - Example review file:
     ```markdown
     # ADR-001-RATIFICATION
     Reviewer: Jane Doe
     Date: 2024-06-01
     Status: Approved
     ```

3. **Ensure Consistency**
   - Verify that all related documentation reflects the ADR's new status and supporting evidence.

4. **Commit Changes**
   - Use a conventional commit message, e.g.:
     ```
     docs: ratify ADR-001 and update supporting evidence
     ```

## Testing Patterns

- Test files use the `*.test.*` naming pattern.
  - Example: `data-fetcher.test.ts`
- The specific testing framework is not detected; follow existing patterns in the repository.
- Place test files alongside the modules they test or in a dedicated test directory as per project structure.

## Commands

| Command            | Purpose                                                      |
|--------------------|--------------------------------------------------------------|
| /adr-status-update | Initiate the ADR lifecycle management workflow               |
```
