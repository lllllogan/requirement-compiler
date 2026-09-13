# Example — Messy voice input

User:

“就是刚刚那个，不是，我的意思是人物还那样，然后右边那个楼往上，镜头别乱动，其他也别跟着变，反正还是那个真实一点的感觉。”

Normalize internally:

- keep previous character state;
- target: right-side building;
- requested change: “往上” is high-impact ambiguous;
- camera locked;
- other environment locked;
- appearance stays realistic.

Good response:

“我只确认一个会直接影响结果的点：你说右边的楼‘往上’，是整栋楼往上移动，还是建筑本身被拉高？人物、镜头和其他街景都沿用上一版不动。”
