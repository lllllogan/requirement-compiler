# AI Video Adapter

adapter_id: ai-video-general

Use for AI video generation/editing workflows.

## Determine task type before prompting

Possible routes include:

- text-to-video;
- image-to-video;
- reference-to-video;
- video editing;
- video extension;
- first/last-frame interpolation;
- camera/motion transfer;
- white-model/3D-guide generation;
- multi-shot narrative;
- hybrid 3D/compositing workflow.

Task type can be a Path decision, not merely a prompt detail.

## High-impact inputs

Inspect only what matters to the chosen route:

- what the shot must communicate;
- exact control role of each asset;
- character identity/wardrobe continuity;
- scene/layout continuity;
- subject blocking/trajectory;
- camera position/movement;
- temporal event order;
- locked vs transformable elements;
- duration vs requested complexity;
- whether one-pass generation is realistic;
- audio/dialogue when relevant.

## Asset-role rule

When several references exist, never accept “参考这些” as a sufficient role definition if roles can compete.

Example:

```yaml
assets:
  - id: character_image
    role: identity_and_wardrobe
    must_control: [face, hair, clothing]
    must_not_control: [camera_path]
  - id: street_image
    role: scene_appearance
    must_control: [architecture, road_layout, materials]
    must_not_control: [character_identity]
  - id: white_model_video
    role: spatial_and_motion_control
    must_control: [camera_path, blocking, subject_trajectory]
    must_not_control: [final_materials, final_character_appearance]
```

## Common failure signatures

Before adding prompt text, inspect:

- competing asset roles;
- too many simultaneous transformations;
- camera motion fighting subject motion;
- style leakage from a structural reference;
- event sequence too dense for duration;
- model asked to preserve too many things while transforming too many others;
- wrong task type (fresh generation vs edit/extension/reference workflow).
