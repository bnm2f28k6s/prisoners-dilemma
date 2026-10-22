---
title: "Level 4: intended and executed actions"
---

# Level 4: intended and executed actions

[Previous](/levels/03-randomization) | [Walkthrough](/) | [Next: imperfect reports](/levels/05-observations)

## Change one constraint

**Remove:** an intended action always executes correctly. For the example, an action independently flips C to D or D to C with probability epsilon.

**Keep:** payoffs depend on executed actions, and both players accurately see those completed actions. Choosing randomly and executing incorrectly remain separate processes.

## Walk through the new possibility

Both players use tit for tat and intend C initially. One execution error changes Row's first action to D. Assume no further errors in this particular trace.

[![Both intend C, but Row's action flips to D. The executed D/C outcome is the bottom-left cell and gives payoffs (5, 0). The matrix itself is unchanged.](/diagrams/matrix-execution.svg)](/diagrams/matrix-execution.svg)

| Round | Intended actions | Executed actions |
| --- | --- | --- |
| 1 | (C, C) | (D, C) |
| 2 | (C, D) | (C, D) |
| 3 | (D, C) | (D, C) |
| 4 | (C, D) | (C, D) |

One mistake can produce alternating retaliation. The table is a possible trace, not an average over noise. The rule also needs to say whether a player knows its own intended action, executed action, or both. Here it knows both; each opponent sees only the executed action.

```text
intended actions -> execution process -> executed actions
executed actions -> payoff table
```

**Checkpoint:** Did Row deliberately defect in round 1? Does Column's observation answer that question?

**Concept added:** an execution law separating choice from action. Probability zero of error recovers the previous model. Changing the policy's cooperation probability would not represent the same mechanism.

Sources: [noise and strategy experiments](/sources#experiments). The trace is our constructed example.
