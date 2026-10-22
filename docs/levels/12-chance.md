---
title: "Level 12: environmental chance"
---

# Level 12: environmental chance

[Previous](/levels/11-state) | [Walkthrough](/) | [Next: hidden conditions](/levels/13-hidden-state)

## Change one constraint

**Remove:** a given state and executed joint action determine one environmental successor. Let the transition rule specify a distribution over successors.

**Keep:** the state is publicly known, and execution errors and signal errors remain separate mechanisms.

## Walk through the new possibility

After legal withdrawals in Level 11, let replenishment add 2 units with probability 0.5 and 0 units otherwise. Cap the stock at 4.

```text
replenishment = 2 or 0, each with probability 0.5
next stock = minimum(4, stock - total withdrawals + replenishment)
```

At stock 2, if both withdraw 1, the next stock is either 2 or 0, each with probability 0.5. The expected next stock is 1, although this particular transition never produces stock 1. Do not substitute an average state for the actual branches of the process.

Randomness can also affect outcomes or rewards directly. Specify a joint distribution when shocks are correlated; separate random draws would silently impose independence.

**Checkpoint:** Does a low stock prove that a player withdrew more than intended?

**Concept added:** an environmental transition law, often called a transition kernel. A point-mass distribution on the old successor recovers the deterministic rule. Strategic randomization, execution noise, observation noise, stopping uncertainty, and environmental chance are distinct places for uncertainty to enter.

Sources: [states and chance events](/sources#information-and-dynamics).
