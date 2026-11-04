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

## Build this version

### Start from the previous version

Keep Level 13's separation of world, permitted views, controller memory, and evaluator records. For this example, replace withdrawals with the two-player contribution game and contributions `{0, 1, 2}`. Use simultaneous choices and identity execution. Stock and sensor options remain available but inactive. Add private costs without handing the payoff-parameter map to controllers.

### Make the change

1. Put the announced type possibilities and prior in `rules`. At initialization, select Row's cost once: cost 1 when a supplied uniform draw is below 0.5, otherwise cost 3. Store the result in `world.types[Row]`; Column's cost is the known value 3.
2. Deliver Row's own cost to Row. Deliver only the prior to Column, together with its own known cost and the common contribution rules. Keep legal actions independent of type in this example, so notices do not reveal Row's cost.
3. Collect identity-keyed contributions from frozen pre-event views. Validate both contributions before resolving. The evaluator computes actual payoffs using the stored cost, not a controller's belief about it.
4. Our tutorial information choice is to deliver both completed contributions and each player's own payoff, never the opponent's payoff or hidden cost. This avoids a direct type leak through Row's numerical reward to Column. Behavior may still inform Column's beliefs. Types persist until a new run, not a new round.

```text
input: initialization draw u, rules, then permitted views and contributions
require 0 <= u < 1
world.types[Row] = 1 if u < 0.5 else 3
deliver own cost to Row; deliver prior to Column
legal = {p: {0, 1, 2} for p in players}
joint = choose all players from frozen view[p], memory[p], legal[p]
validate and commit joint
x = joint[Row]; y = joint[Column]
payoff[Row] = 2 * (x + y) - world.types[Row] * x
payoff[Column] = 2 * (x + y) - 3 * y
totals[p] += payoff[p] for each p
record types, joint, payoff for evaluator
deliver joint and own payoff only
result: type-dependent earnings without revealing hidden parameters
```

### Check your implementation

- Given contributions `(1, 0)`, expect payoffs `(1, 2)` for cost-1 Row and `(-1, 2)` for cost-3 Row. Column's initial view must be identical in both cases.
- Given initialization draw 0.5, expect cost 3; another round must not redraw it. Reject draw 1 or contribution 3 before applying the event.
- Given Column's delivered report, expect no Row payoff or stored type. A belief belongs in Column's memory, not in `world.types`.
- For backward compatibility, use one publicly known type and restore the preceding material game to recover Level 13. In the contribution branch, a known cost 3 recovers the earlier complete-information contribution payoffs.

**Checkpoint:** Is uncertainty about a player's cost the same as misreporting the action it actually took?

**Concept added:** private parameters and an information/prior structure. Degenerate known types recover the previous model. Unknown strategy, hidden environmental state, and private payoff type are related belief problems but different modeling choices.

Sources: [complete versus incomplete information](/sources#information-and-dynamics).
