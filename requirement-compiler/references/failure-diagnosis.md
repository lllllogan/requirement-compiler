# Failure Diagnosis

Do not react to “不对” by automatically rewriting the prompt.

## Compare four things

1. Intended outcome/current Spec.
2. Actual result.
3. Last known good state or previous attempt.
4. What changed in this attempt.

## Failure layers

### GOAL_ERROR
The user's desired outcome was misunderstood.
Repair: reopen goal.

### PATH_ERROR
The workflow/technique is poorly suited to the outcome.
Repair: redesign the route or decompose the work.

### SPEC_ERROR
The path is viable but a critical requirement is missing, contradictory, or misprioritized.
Repair: clarify/update the Spec.

### COMPILATION_ERROR
The Spec is correct but translated badly for the target tool/model/person.
Repair: change target-specific wording/structure only.

### INPUT_ERROR
Assets/data/references are inadequate, conflicting, or assigned the wrong role.
Repair: replace or reassign inputs.

### CAPABILITY_LIMIT
The target system cannot reliably perform the requested combination.
Repair: change tool, reduce complexity, split stages, or use a hybrid route.

### EXECUTION_VARIANCE
The setup is sound but the stochastic/operational attempt failed.
Repair: rerun or change seed/settings before redesigning the task.

## Minimal-change rule

Preserve all stable layers above the diagnosed failure.

If concept, character, and environment are already correct, a motion-control failure must not trigger redesign of those layers.
