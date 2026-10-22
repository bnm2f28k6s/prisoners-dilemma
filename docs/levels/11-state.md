---
title: "Level 11: a persistent environment"
---

# Level 11: a persistent environment

[Previous](/levels/10-messages) | [Walkthrough](/) | [Next: environmental chance](/levels/12-chance)

## Change one constraint

**Remove:** every round faces the same environmental conditions. Add a persistent, publicly known state that actions can change.

**Keep:** known rules, the selected schedule, and the existing action and signal mechanisms. For this new component, transitions are deterministic. Previous action or reporting noise can still be switched on separately.

## Walk through the new possibility

Let the environment be a shared stock `s`, initially 4. Two players each withdraw either 0 or 1 unit. In this illustrative variant, both withdrawals are legal only when at least two units remain; at stock 0 or 1, only withdrawal 0 is legal. There is no replenishment yet.

```text
next stock = current stock - total withdrawals
stage payoff for each player = that player's withdrawal
```

If both withdraw 1, the stock goes from 4 to 2, then from 2 to 0 on the next identical event. Future opportunities have changed even though neither player's memory need have changed.

A stage can now have state-dependent legal actions and payoffs. Define payoffs for every legal joint action, and define every possible transition. Arbitrary individual action sets do not automatically prevent incompatible simultaneous demands; this example avoids that conflict by restricting withdrawals conservatively.

**Checkpoint:** If both players forget everything after the first event, does the stock return to 4?

**Concept added:** a world state and a transition rule. World state describes the situation; player memory describes retained information. A single unchanging environmental state recovers the repeated-stage model, even though the round count and history still exist.

Sources: [state, trajectories, and game descriptions](/sources#information-and-dynamics).
