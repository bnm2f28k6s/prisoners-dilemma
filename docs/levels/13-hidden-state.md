---
title: "Level 13: hidden conditions"
---

# Level 13: hidden conditions

[Previous](/levels/12-chance) | [Walkthrough](/) | [Next: private types](/levels/14-private-types)

## Change one constraint

**Remove:** the environmental state is automatically public. Let the observation law reveal only selected information about it.

**Keep:** the world still has a definite state and evolves under the specified transition law. Hiding information does not change that law.

## Walk through the new possibility

Instead of displaying exact stock, a sensor reports "low" for stock 0, 1, or 2, and "high" for stock 3 or 4. Even an accurate "low" report leaves several possible states.

Legal-action notices can leak information too. With Level 11's withdrawal rule, seeing that withdrawal 1 is legal rules out stocks 0 and 1. A "low" signal plus that notice would identify stock 2 exactly. The model must include both channels, rather than pretending the sensor is the player's only clue.

```text
actual state -> transition and outcome rules
permitted signals and legal-action notices -> player's information
retained information -> optional belief about possible states
```

A **belief state** is a player's assessment of hidden possibilities, not the actual state. A Bayesian update needs an initial belief and a likelihood model; the conceptual framework need not require every player to update that way.

## Build this version

### Start from the previous version

Keep Level 12's actual stock transition, replenishment draw, legal withdrawals, and payoff accounting. Replace public stock delivery, not `world.stock` itself. For this example only, use the accurate low/high sensor with no additional report noise. Retain the earlier public-stock mode as an option. Do not enable beliefs, private types, or learning just because observations are now incomplete.

### Make the change

1. Add a stock-report rule that maps 0 through 2 to `low` and 3 through 4 to `high`. Validate its domain. Generate the initial report before the first decision and a new report after each resolved transition. A publicly announced initial stock of 4 is still known even without an exact-stock field. For the first-view checks below, instead announce one common uniform prior over stocks 0 through 4, select the actual stock privately, and keep that prior identical across cases.
2. Build each `view[player]` from an allowlist of delivered fields. Include the sensor report and that player's legal-action notice; exclude exact stock, replenishment draw, and evaluator `record`. Avoid passing a reference to `world` through a convenience context.
3. Preserve the conservative legal sets from Level 11. They intentionally convey information. In this fixture, deliver own withdrawal payoff but no extra numeric stock report. A controller can retain all these clues in `memory[player]`.
4. Freeze the permitted views, commit both actions, and run the unchanged true-state resolver. Only afterward deliver the successor reports. Belief updating, if added later, must consume deliveries rather than inspect truth.

```text
input: world.stock, rules, permitted deliveries, memory
legal = legal withdrawals from world.stock
for each p:
    report = low if world.stock <= 2 else high
    view[p] = allowed prior deliveries plus report and legal[p]
before = copy permitted views
joint = choose all players from before[p], memory[p], legal[p]
validate and commit joint
resolve Level 12 transition against world, updating totals
record actual stock, draw, joint, successor for evaluator
deliver sensor(successor), next legal notices, permitted own payoff
result: unchanged world dynamics, restricted controller information
```

Treat replacement as a delivery operation: do not leave yesterday's exact-stock field in the new view when switching modes.

### Check your implementation

- Given stock 0 or 1 before any history, expect the same `low` report and legal set `{0}`. Neither view may contain exact stock.
- Given stock 2, expect `low` with `{0, 1}`; this combination identifies 2. Do not claim it is indistinguishable from 0 or 1.
- Given stock 3 or 4, expect `high` with `{0, 1}`. Inject an evaluator-only replenishment value and check that it is absent from controller inputs.
- Given stock outside 0 through 4, reject initialization instead of inventing a sensor category. For backward compatibility, select full stock disclosure and recover Level 12's views and transition fixtures.

**Checkpoint:** Could two different stocks produce the same information before a decision? List every channel, not just the named sensor.

**Concept added:** partial observation of persistent state. This reuses Level 5's observation mechanism for the environmental state introduced later. Reveal that state fully to recover Level 12. A fixed latest observation need not contain everything useful in the player's previous signals.

Sources: [imperfect information and player information states](/sources#information-and-dynamics).
