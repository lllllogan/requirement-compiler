# Seedance 2.5 Adapter

adapter_id: seedance-2.5
last_verified: 2026-09

This adapter is downstream of the Requirement Compiler. Verify current product behavior when UI, limits, pricing, or reference handling matters.

## Capability assumptions requiring freshness when material

Current public materials describe Seedance 2.5 as supporting long-form generation workflows, multimodal references, editing, and stronger control from references including white-model / clay-render style guidance for spatial structure, movement, blocking, and camera language.

Do not rely on this file for current input-count limits, UI placement, pricing, or exact C-end workflow. Verify those when they affect the path.

## High-impact questions/derivations

For reference-heavy work determine:

1. Which workflow/mode is actually being used in the current product UI?
2. What exact job does each image/video/audio/white-model input perform?
3. Which properties are locked and which may transfer?
4. Does white-model guidance need only trajectory/blocking, or also pacing/shot-size transitions?
5. Is the task fresh generation, edit, extension, or another reference workflow?
6. Is the shot too complex for one pass and better split into stages?

## White-model principle

Do not treat a white model as generic visual inspiration.

Prefer explicit control responsibility such as:

- camera movement;
- shot-size transition;
- subject trajectory;
- spatial blocking;
- action/pose structure;
- pacing when explicitly desired.

Assign final character appearance, scene appearance, materials, lighting, and art direction to appropriate assets/instructions.

## Compilation order

For reference-heavy generation prefer:

1. task/shot objective;
2. reference-role mapping;
3. temporal sequence;
4. camera + blocking;
5. appearance/style responsibilities;
6. locked invariants;
7. audio/dialogue if needed;
8. success condition.

## Diagnostic warning

If a result only partially follows the white model, do not immediately conclude the prompt needs more words.

Check:

- whether the C-end workflow actually accepts/uses the reference in the intended way;
- whether another reference competes with it;
- whether the white model was explicitly assigned to camera/blocking/trajectory;
- whether creative transformations overwhelm the structural constraint;
- whether an edit/staged workflow is better than fresh generation;
- whether this is simply a capability or variance limit.
