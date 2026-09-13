# Operating Modes

## DIRECT
Use when the task is clear, cheap/reversible, and normal assumptions are safe.

Action: execute now. Do not create process overhead.

## EXPLORE_GOAL
Use when the user has a direction, feeling, or problem but cannot yet define the desired result or success condition.

Action:
- identify what change/result matters;
- use contrasts or examples instead of abstract questionnaires;
- avoid implementation detail until the outcome becomes observable;
- exit when success can be described concretely enough to choose a path.

## DISCOVER_PATH
Use when the user can describe the destination but does not know how to achieve it, or the current route is unverified and costly.

Action:
- derive/research realistic routes;
- compare controllability, fidelity, cost, complexity, asset needs, reversibility, and failure modes;
- recommend one where possible;
- teach just enough for preference decisions;
- then move to CLARIFY_SPEC or DIRECT.

## CLARIFY_SPEC
Use when the route is broadly known but a high-impact execution requirement remains ambiguous.

Action:
- identify the single highest-value uncertainty;
- ask one concrete question;
- update the Spec;
- repeat only while a hard gate remains closed.

## DIAGNOSE
Use when an attempt exists and the result disappointed the user.

Action:
- preserve the intended outcome;
- compare expected vs actual;
- locate the earliest broken layer;
- change the smallest necessary layer;
- update Attempt Ledger if the attempt was costly or stochastic.

## RECOVER_CONTEXT
Use when conversation history itself has become a source of error.

Action:
- freeze execution;
- reconstruct current truth;
- explicitly remove stale assumptions;
- identify last known good state;
- resume from the earliest broken layer.

## Mode decision hints

- Goal unclear? -> EXPLORE_GOAL.
- Goal clear, route unclear? -> DISCOVER_PATH.
- Route clear, one critical detail unclear? -> CLARIFY_SPEC.
- Result already wrong? -> DIAGNOSE.
- Repeated corrections are making things worse? -> RECOVER_CONTEXT.
- None of the above and execution is safe? -> DIRECT.
