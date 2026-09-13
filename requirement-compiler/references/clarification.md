# Clarification Strategy

## Value test

Ask only when the answer has meaningful expected value.

Prioritize by:

- consequence if guessed wrong;
- uncertainty;
- correction/rework cost;
- whether the answer can change the path;
- whether the user can reasonably know the answer.

## Question style

Prefer concrete contrasts:

“你说人物保持不变，是只锁脸和服装，还是连位置和动作节奏也要锁？这会决定我是否让模型自由表演。”

Avoid form-like jargon:

“请填写人物一致性需求。”

## If the user does not know

Do not ask the same thing again in different words.

Instead:
1. explain the tradeoff plainly;
2. recommend a default based on the outcome;
3. ask only for preference if preference still matters;
4. if the route itself is unclear, move to DISCOVER_PATH.

## One vs batch

Default: one decisive question at a time.

Batch only when:
- questions are independent;
- the user asked for a checklist/form;
- stopping after every answer would create more friction than value.

## Stop condition

Stop clarifying when all hard gates are open and remaining uncertainty is safely defaultable.
