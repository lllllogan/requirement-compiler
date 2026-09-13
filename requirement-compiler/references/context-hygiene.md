# Context Hygiene and Rollback

## Canonical-state rule

Execution uses the current Canonical Task Spec, not a naive accumulation of every prior message.

## Drift signals

Gate C should trigger when:

- two consecutive attempts fail for the same material reason;
- three corrections fail to converge;
- the same misunderstanding reappears after being corrected;
- the agent changes locked areas;
- the prompt/spec gets longer while results get worse;
- a previously settled decision becomes uncertain without new evidence.

## Recovery procedure

1. Stop execution.
2. Identify last known good state.
3. Reconstruct current valid requirements only.
4. Separate active / superseded / invalidated items.
5. Locate earliest broken layer: goal, path, spec, compilation, input, capability, or variance.
6. Preserve all stable upstream decisions.
7. Resume from the earliest broken layer.

## Context compression

For long projects, periodically compress history into:

- current goal;
- selected path;
- current Task Spec;
- major decisions and reasons;
- active critical unknowns;
- latest Attempt Ledger entry and diagnosis.

Do not preserve low-value wording history merely because it exists.
