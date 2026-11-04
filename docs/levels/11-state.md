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

## Build this version

### Start from the previous version

Keep Level 10's schedule, optional message delivery, controller memory, and commit-before-resolution boundary. Replace only the material game for this worked branch: use withdrawals instead of C/D and initialize `world.stock = 4`. Messages remain optional and cannot replenish stock. Choose identity execution, public stock, and no replenishment for this example; these are overrides, not requirements to combine all earlier options.

### Make the change

1. Add authoritative stock to `world`, not to controller memory. Initialize it once per run, never once per decision or after forgetting.
2. Before each withdrawal event, derive each player's legal map from the same stock snapshot. Use `{0, 1}` at stock at least 2 and `{0}` at stock 0 or 1. Deliver that legal notice and the public stock before choices.
3. Commit the whole identity-keyed joint withdrawal. Reject a missing player, extra player, or illegal value before paying anyone. Do not let the first withdrawal reduce the second player's options.
4. Resolve withdrawals together, add each withdrawal to that player's `totals[player]`, then publish the successor stock. For this tutorial, run a configured finite number of events even at zero stock; zero stock alone does not terminate play. Reject negative or non-integer initial stock.

```text
input: world.stock, players, rules.eventLimit, totals
s = world.stock
legal = {p: ({0, 1} if s >= 2 else {0}) for p in players}
deliver public s and legal[p] into each view[p]
before = copy permitted views
joint = {p: choose(p, before[p], memory[p], legal[p]) for p in players}
require keys(joint) == players and joint[p] in legal[p] for every p
commit joint
world.stock = s - sum(joint[p] for p in players)
totals[p] += joint[p] for every p
record s, joint, world.stock for evaluator
deliver configured results; update memory only from deliveries
result: successor stock and earned totals
```

This resolver is deliberately for two players. Reject another group size until you define a feasible withdrawal rule for it.

### Check your implementation

- Given stock 4 and two successive joint withdrawals `{Row: 1, Column: 1}`, expect stocks 2 then 0 and cumulative totals `(2, 2)`.
- Given stock 1, expect only 0 legal for both; `(0, 0)` leaves stock 1. An attempted 1 must fail without deducting stock or adding payoff.
- Given cleared `memory[player]` after the first event, expect the next stock still to be 2, not 4.
- For backward compatibility, select a constant world and restore Level 10's original material resolver. Its messages and payoff fixtures must still work unchanged.

**Checkpoint:** If both players forget everything after the first event, does the stock return to 4?

**Concept added:** a world state and a transition rule. World state describes the situation; player memory describes retained information. A single unchanging environmental state recovers the repeated-stage model, even though the round count and history still exist.

Sources: [state, trajectories, and game descriptions](/sources#information-and-dynamics).
