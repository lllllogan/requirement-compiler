# Evaluation Cases

Manual eval set for Requirement Compiler v0.3.

Score each case on:

- correct mode selection;
- gate behavior;
- number/value of clarification questions;
- preservation of locked state;
- route quality;
- whether execution starts too early;
- whether diagnosis changes the correct layer;
- user friction.

The copy-paste prompts and expected behaviors are in `../TEST_TASKS.zh-CN.md`.

Recommended 0–2 score per dimension:
- 0 = harmful/wrong
- 1 = usable but flawed
- 2 = strong

A release candidate should have no 0 on gate behavior for T3/T5/T6/T8 and no 0 on friction for T1/T7.
