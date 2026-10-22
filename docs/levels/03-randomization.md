---
title: "Level 3: randomized choices"
---

# Level 3: randomized choices

[Previous](/levels/02-horizon) | [Walkthrough](/) | [Next: execution errors](/levels/04-execution)

## Change one constraint

**Remove:** a player's decision rule must select one action with certainty. Let it select a probability distribution over legal actions instead.

**Keep:** whichever stopping rule was selected, the C/D square, and accurate execution and observation. The next example has no shared random device; players draw independently.

## Walk through the new possibility

Row chooses C with probability 0.75. Column chooses C for certain. Row's expected stage payoff is `0.75 * 3 + 0.25 * 5 = 3.5`; Column's is `0.75 * 3 + 0.25 * 0 = 2.25`.

[![Only the unchanged left-column cells are possible: C/C with probability 75 percent and payoffs (3, 3), or D/C with probability 25 percent and payoffs (5, 0).](/diagrams/matrix-randomized.svg)](/diagrams/matrix-randomized.svg)

One realized round is still either `(C, C)` or `(D, C)`. Nobody actually receives the average merely because it was calculated. This is not an optimality claim: against certain C in the one-shot square, Row gets more by choosing D for certain.

```text
decision rule returns probabilities over legal actions
sample an intended action from those probabilities
```

Randomized forgiveness can now be expressed: after an observed D, cooperate with some specified probability. Whether that helps depends on the opponent and other settings.

Expected payoffs require utility numbers suitable for lottery comparisons. Merely preserving their ranking does not preserve all expected-payoff comparisons. Likewise, repeated-game sums use more structure than ordinal rankings alone.

**Checkpoint:** Which probability distribution expresses always defect?

**Concept added:** a decision rule can return an action distribution. Deterministic rules remain the special case with probability one on one action. Randomization does not mean the actuator made a mistake.

Sources: [utility and mixed strategies](/sources#foundations).
