# Requirement Compiler

Requirement Compiler is a portable Agent Skill for turning casual, incomplete, voice-transcribed, path-uncertain, or drifting requests into reliable execution.

The central model is:

**Goal -> Path -> Spec -> Execute -> Diagnose**

The repository separates the actual installable Skill (`requirement-compiler/`) from human documentation and eval cases.

## v0.3 focus

- three hard execution gates;
- Mini vs Full Canonical Task Spec;
- explicit state transitions;
- common Adapter Contract;
- Attempt Ledger for expensive/stochastic work;
- context rollback after non-converging attempts;
- narrower trigger boundary so simple tasks stay fast.

See `README.zh-CN.md` for the Chinese guide and `TEST_TASKS.zh-CN.md` for copy-paste evaluation tasks.
