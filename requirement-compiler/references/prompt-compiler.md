# Prompt Compiler

A prompt is a compiled artifact, not the source of truth.

## Inputs

Compile from:
- outcome;
- selected path;
- locked/flexible constraints;
- asset roles;
- temporal/causal order;
- success criteria;
- relevant platform/model strategy.

## Compilation rules

1. Select only information relevant to the target system.
2. Convert vague human language into observable instructions where necessary.
3. Preserve priority: must / should / may.
4. Make time/order explicit when sequence matters.
5. Assign each reference asset a single clear job when multiple references exist.
6. Avoid duplicate or competing control instructions.
7. Keep target-specific structure separate from the Canonical Task Spec.
8. If the target performs better with simpler prompts, keep it simple.
9. Do not use adjective density as a substitute for unresolved requirements.

## Final check

- Main subject/action clear?
- Locked elements preserved?
- Asset responsibilities non-competing?
- Ambiguous adjectives translated where needed?
- Sequence/timing explicit if important?
- Task likely within capability?
- Would staged execution outperform one giant prompt?
