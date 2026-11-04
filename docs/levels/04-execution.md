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

## Build this version

### Start from the previous version

Keep Level 3's distributions and sampled intended actions. Insert an execution step between committing intentions and resolving payoffs. Do not implement mistakes by editing the policy's cooperation probability or the payoff table.

### Make the change

1. Add a validated error probability `epsilon` in `[0, 1]`. In this C/D example, independently flip each player's action when its execution draw is less than epsilon. The execution rule is specific to this action set; later action sets need their own rule.
2. Keep separate `intended` and `executed` maps. Copy intentions before applying errors so the original choice is not lost or mutated.
3. Feed only executed actions to the payoff lookup. Record both maps for evaluation. Deliver all completed executed actions, plus each player's own intention and payoff. Do not deliver the opponent's intention.
4. Update tit for tat from the opponent's executed action, not from the intention stored in the evaluator record. Draw independently of policy and continuation randomness for this example.

```text
intended = collect and commit policy samples
for player in players:
    if execution_draw[player] < epsilon:
        executed[player] = the other C/D action
    otherwise:
        executed[player] = intended[player]
payoffs = payoff_table applied to executed
record intended, executed, and payoffs for evaluation
deliver completed execution and permitted own information
```

### Check your implementation

- Set epsilon to 0.1, both intentions to C, and execution draws to Row 0.05 and Column 0.50. Expect intentions `(C, C)`, executions `(D, C)`, and payoffs `(5, 0)`. The intention record must still show C/C.
- For two tit-for-tat rules, inject only that first error and then draws above epsilon. Expect intended pairs `(C, C), (C, D), (D, C), (C, D)` and executed pairs `(D, C), (C, D), (D, C), (C, D)` over four rounds.
- At epsilon = 1, both C intentions become D and pay `(1, 1)`. Reject epsilon outside `[0, 1]`. A draw equal to epsilon does not flip.
- Set epsilon to zero. Expect exactly Level 3's outcomes for the same policy and duration inputs. Turning off errors must not shift those other random inputs.

**Checkpoint:** Did Row deliberately defect in round 1? Does Column's observation answer that question?

**Concept added:** an execution law separating choice from action. Probability zero of error recovers the previous model. Changing the policy's cooperation probability would not represent the same mechanism.

Sources: [noise and strategy experiments](/sources#experiments). The trace is our constructed example.
