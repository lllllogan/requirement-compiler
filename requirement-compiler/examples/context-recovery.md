# Example — Context recovery

Signals:

- several “不是这个” corrections;
- prompt keeps growing;
- character appearance that was previously correct starts changing;
- the same camera error remains.

Gate C triggers.

Recovery:

```yaml
last_known_good_state:
  preserved_items:
    - concept
    - character_identity
    - street_appearance
    - photoreal_style
locked:
  - concept
  - character_identity
  - street_appearance
invalidated:
  - "keep adding global prompt constraints"
critical_unknowns:
  - item: "correct control route for camera/blocking"
    impact: HIGH
    blocks_execution: true
next_action:
  mode: DISCOVER_PATH
  action: "verify the control workflow before another paid generation"
```
