# Canonical Task Spec

The Task Spec is a mutable representation of the **current** task truth. It is not a transcript and not a dump of every idea mentioned.

## Mini Spec

Use by default for one-off but non-trivial work.

```yaml
spec_level: mini
spec_version: 1
outcome: ""
confirmed: []
critical_unknowns:
  - item: ""
    impact: HIGH|MEDIUM|LOW
    blocks_execution: true|false
locked: []
success_checks: []
next_action:
  mode: DIRECT|EXPLORE_GOAL|DISCOVER_PATH|CLARIFY_SPEC|DIAGNOSE|RECOVER_CONTEXT
  action: ""
```

## Full Spec

Use when the work is long-running, multi-stage, multi-asset, costly, or has started drifting.

```yaml
spec_level: full
spec_version: 1
outcome:
  statement: ""
  deliverable: ""
  why_it_matters: ""
current_stage: ""
selected_path:
  summary: ""
  rationale: ""
confirmed: []
derived:
  - claim: ""
    basis: ""
critical_unknowns:
  - item: ""
    impact: HIGH|MEDIUM|LOW
    why_it_matters: ""
    blocks_execution: true|false
assumptions:
  - assumption: ""
    risk_if_wrong: ""
locked: []
flexible: []
assets:
  - id: ""
    type: ""
    role: ""
    must_control: []
    must_not_control: []
success_checks: []
superseded:
  - old_item: ""
    replaced_by: ""
invalidated:
  - item: ""
    reason: ""
last_known_good_state:
  description: ""
  preserved_items: []
next_action:
  mode: DIRECT|EXPLORE_GOAL|DISCOVER_PATH|CLARIFY_SPEC|DIAGNOSE|RECOVER_CONTEXT
  action: ""
```

## Upgrade rule

Upgrade Mini -> Full when any of these appears:

- more than one execution stage;
- multiple assets with different control roles;
- paid/expensive attempts;
- repeated revisions;
- several decisions must be preserved across turns;
- RECOVER_CONTEXT or serious DIAGNOSE work begins.

Do not downgrade Full during an active unstable phase. After completion, archive a compact summary.

## Update rules

1. Store only information that can affect future execution.
2. Separate user-confirmed facts from agent-derived conclusions.
3. Every `HIGH` unknown must say whether it blocks execution.
4. `locked` cannot be changed by downstream iteration without explicit evidence or user intent.
5. When new information conflicts with old information, mark the old item superseded or invalidated.
6. Never preserve stale wording just because it exists in chat history.
7. Increment `spec_version` when a decision materially changes the executable task.
