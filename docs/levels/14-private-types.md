---
title: "Level 14: private types"
---

# Level 14: private types

[Previous](/levels/13-hidden-state) | [Walkthrough](/) | [Next: changing partners](/levels/15-matching)

## Change one constraint

**Remove:** everybody knows the exact parameters governing everyone else's incentives or capabilities. Give a player a possibly private **type**.

**Keep:** an announced family of possible payoff and action rules. For this example, types are fixed during the interaction. This differs from a resource stock that changes after withdrawals.

## Walk through the new possibility

Return to the contribution game. Row's cost per contributed unit is either 1 or 3. Row knows which; Column initially assigns probability 0.5 to each, and that information arrangement is common knowledge. Keep the shared benefit coefficient at 2.

```text
Row's payoff = 2(x + y) - Row's private cost * x
Column's payoff = 2(x + y) - 3y
```

A cost-1 Row gains 1 by increasing x by one, holding y fixed. A cost-3 Row loses 1. Column may use observed behavior to revise a belief about Row's type. But a single observed action need not identify a type when strategies can randomize or execution can fail.

The model specifies the actual type, how it is selected, and who learns it. Players do not get hidden parameters just because an evaluator needs them to compute outcomes. Correlated types need a joint prior, not independent guesses by default.

**Checkpoint:** Is uncertainty about a player's cost the same as misreporting the action it actually took?

**Concept added:** private parameters and an information/prior structure. Degenerate known types recover the previous model. Unknown strategy, hidden environmental state, and private payoff type are related belief problems but different modeling choices.

Sources: [complete versus incomplete information](/sources#information-and-dynamics).
