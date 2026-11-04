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

## Build this version

### Start from the previous version

Keep Level 2's duration options and the unchanged resolver. Change the output of a decision rule from one action to a distribution over legal actions. For testing this example, select a one-round fixed duration; random stopping remains available.

### Make the change

1. Represent a distribution as action/probability pairs. Validate that probabilities are finite, non-negative, sum to one within an explicitly chosen numerical tolerance, and refer only to legal actions. Reject an invalid distribution rather than guessing how to repair it.
2. Adapt each deterministic rule by assigning probability one to its chosen action. That preserves always defect and tit for tat without maintaining two choice pipelines.
3. Sample one intended action per player using that player's policy draw. Fix an action ordering for sampling, such as C then D. Use cumulative probability intervals and `u < cumulative_probability` for draws `u` in `[0, 1)`. If you accept a floating-point sum within tolerance, divide by that accepted sum before sampling and close the last positive-probability interval at 1. Never give rounding residue to a zero-probability action. Reject an invalid draw before selecting an action.
4. Commit all sampled actions before resolving. Independently drawn choices must not reuse one draw for both players. Keep policy sampling separate from the stopping draw.

```text
for player in acting group:
    distribution = policy(view[player], memory[player])
    validate distribution against that player's legal actions
    intended[player] = sample(distribution, policy_draw[player])
commit all intended actions
resolve intended actions using the unchanged table
```

Expected payoff calculations enumerate outcomes and weight their payoffs by probability. They do not replace the realized payoff returned by the resolver.

### Check your implementation

- With Row's distribution `{C: 0.75, D: 0.25}`, a draw of 0.20 selects C and a draw of 0.90 selects D. A draw of exactly 0.75 selects D under the stated boundary rule.
- With Column certainly C, those two Row draws produce payoffs `(3, 3)` and `(5, 0)` respectively. The weighted expected pair is `(3.5, 2.25)`, not a third possible cell.
- Reject negative probabilities, a total of 0.8, and a distribution containing X. Check that no invalid choice reaches the payoff resolver.
- Use point-mass distributions for Level 2's old decision rules. With the same duration inputs, expect the old traces and totals. Two independent half-C policies have four joint outcomes with probability 0.25 each, not only C/C and D/D.

**Checkpoint:** Which probability distribution expresses always defect?

**Concept added:** a decision rule can return an action distribution. Deterministic rules remain the special case with probability one on one action. Randomization does not mean the actuator made a mistake.

Sources: [utility and mixed strategies](/sources#foundations).
