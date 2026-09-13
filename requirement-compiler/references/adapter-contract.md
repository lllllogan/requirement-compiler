# Adapter Contract

Adapters add domain/platform expertise without replacing the general Requirement Compiler.

Each adapter should expose the following concepts, in prose or structured form.

## Identity

- `adapter_id`
- `applies_when`
- target domain/platform/model family
- `last_verified` when behavior can change over time

## Capability model

- what the target is good at;
- important limits;
- task types/modes that materially change the workflow.

## High-impact inputs

For each relevant input, define:

- what it can control;
- what it should not be asked to control;
- conflicts with other inputs.

## Clarification rules

- `ask_if_missing`: only high-impact unknowns;
- `safe_defaults`: things the adapter may choose without interrupting the user;
- `path_blockers`: unknowns that require DISCOVER_PATH rather than CLARIFY_SPEC.

## Compilation strategy

- preferred information order;
- target-specific language/structure;
- information to omit;
- decomposition rules.

## Diagnostics

- common failure signatures;
- likely failure layers;
- tests that distinguish prompt/input/path/capability problems.

## Freshness triggers

Require current verification when the answer depends on:

- platform UI/workflow;
- model version;
- input limits;
- pricing/credits;
- feature availability;
- task modes or reference behavior that may have changed.
