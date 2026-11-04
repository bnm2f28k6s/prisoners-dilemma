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

## Build this version

### Start from the previous version

Keep Level 11's persistent stock, conservative legal withdrawals, simultaneous commitments, and withdrawal payoffs. Replace the deterministic successor calculation with a sampled transition. For this example only, set capacity 4, replenishment probability 0.5, and replenishment amount 2; retain public stock and identity execution. Messages, execution noise, and stopping randomness remain independent options, not automatically enabled features.

### Make the change

1. Add the probability, amount, and capacity to `rules`. Validate a probability in `[0, 1]`, a nonnegative integer amount, and initial stock between zero and capacity.
2. Keep legal-action calculation based on pre-withdrawal stock. Commit and validate withdrawals before drawing replenishment. Replenishment cannot make an otherwise illegal withdrawal legal retroactively.
3. Draw one environmental value for the shared stock per event, not one per player. Our tutorial boundary convention uses a supplied uniform value `u` in `[0, 1)` and replenishes exactly when `u < probability`. This convention makes equality unambiguous.
4. Subtract withdrawals, add replenishment, then cap the result. Record the realized draw for evaluation, but deliver only the configured public successor and permitted outcome reports. Controller random draws must not substitute for this environmental draw.

```text
input: committed legal joint, old stock s, rules, environmental draw u
require 0 <= u < 1
withdrawn = sum(joint[p] for p in players)
replenishment = rules.amount if u < rules.probability else 0
next = minimum(rules.capacity, s - withdrawn + replenishment)
world.stock = next
totals[p] += joint[p] for each p
record s, joint, u, replenishment, next for evaluator
deliver public next and configured payoff reports
update memory from delivered information
result: one realized successor, not its expected value
```

Supply fixed draws in checks rather than waiting for a random run to happen to cover both branches. Reject malformed draws rather than silently clipping them.

### Check your implementation

- Given stock 2 and withdrawals `(1, 1)`, when `u = 0.25`, expect successor 2; when `u = 0.5`, expect successor 0. Both branches pay `(1, 1)`.
- Given stock 4, withdrawals `(0, 0)`, and `u = 0`, expect stock 4, not 6.
- Given stock 1, a requested withdrawal 1 remains illegal even with a replenishing draw. Given `u = 1`, reject the draw and leave the event unapplied.
- For backward compatibility, set replenishment probability to zero. Every legal event must reproduce Level 11's stock transition and totals for the same joint actions.

**Checkpoint:** Does a low stock prove that a player withdrew more than intended?

**Concept added:** an environmental transition law, often called a transition kernel. A point-mass distribution on the old successor recovers the deterministic rule. Strategic randomization, execution noise, observation noise, stopping uncertainty, and environmental chance are distinct places for uncertainty to enter.

Sources: [states and chance events](/sources#information-and-dynamics).
