# Attempt Ledger

Use for paid, stochastic, expensive, or repeated execution.

The ledger is experimental history. It does not define the current task.

## Minimal entry

```yaml
attempt_id: A-001
spec_version: 3
target: ""
inputs:
  - id: ""
    role: ""
changes_from_previous: []
expected_effect: ""
actual_result: ""
failure_layer: ""   # blank when successful
decision: ""
```

## Rules

1. Record deltas, not full duplicated prompts/history.
2. If an attempt fails, record the observed failure, not just “bad”.
3. Compare one meaningful change at a time when possible.
4. After two same-reason failures, Gate C triggers.
5. Successful/stable attempts may update `last_known_good_state` in the Full Spec.
