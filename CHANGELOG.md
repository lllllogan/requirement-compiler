# Changelog

## 0.3.0

### Added
- Three hard gates: Path Gate, Critical Unknown Gate, Drift Gate.
- Mini vs Full Canonical Task Spec.
- Explicit mode/state transitions.
- Adapter Contract for domain/platform knowledge.
- Attempt Ledger for costly/stochastic/repeated execution.
- Spec versioning and execution-blocker validation.
- Copy-paste eval tasks covering non-video domains as well as AI video.

### Changed
- Narrowed trigger boundary: simple clear work should bypass the Skill.
- Clarification stops when remaining unknowns are safely defaultable.
- Context drift now triggers after two same-reason failures or three non-converging corrections.
- Seedance knowledge remains an adapter instead of defining the core workflow.

### Fixed
- Installable Skill directory is exactly `requirement-compiler`, matching frontmatter `name`.
- Human-facing docs are kept outside the installable Skill directory.

## 0.2.0
- Introduced Goal -> Path -> Spec -> Execute -> Diagnose.
- Added Canonical Task Spec, supersession, invalidation, last known good state, and context recovery.
