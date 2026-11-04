---
title: "Level 7: more than two actions"
---

# Level 7: more than two actions

[Previous](/levels/06-payoffs) | [Walkthrough](/) | [Next: more players](/levels/08-players)

## Change one constraint

**Remove:** each player has exactly two legal actions. Allow a player-specific set of choices, including numeric quantities.

**Keep:** two players, known payoff functions, and simultaneous decisions. A larger action set does not itself change timing or observations.

## Walk through the new possibility

Replace C/D with contributions `x` and `y`, each chosen from `{0, 1, 2}`. Define Row's payoff as `2(x + y) - 3x`, and Column's as `2(x + y) - 3y`.

For `(x, y) = (2, 1)`, the shared benefit is 6. Row pays 6 and receives payoff 0; Column pays 3 and receives payoff 3. For `(2, 2)`, each receives 2. Reducing your own contribution increases your payoff when the other's contribution is held fixed, yet both contributing fully beats both contributing nothing.

[![Three-by-three contribution matrix. Row chooses x down the left and Column chooses y across the top, each from 0, 1, 2. The outlined x=2, y=1 cell gives (0, 3).](/diagrams/matrix-contributions.svg)](/diagrams/matrix-contributions.svg)

Row stays on the left, Column stays across the top, and payoff order stays `(Row, Column)`. There are now three choices on each axis. The labels change because these choices are contribution quantities, not C/D under new names.

| Row contribution x | Column y = 0 | Column y = 1 | Column y = 2 |
| --- | --- | --- | --- |
| 0 | (0, 0) | (2, -1) | (4, -2) |
| 1 | (-1, 2) | (1, 1) | (3, 0) |
| 2 | (-2, 4) | (0, 3) | (2, 2) |

This is a new teaching game with the same incentive tension, not a claim that its numbers equal the old square. Level 6 already lets us supply the payoff functions; this step changes the domain on which they operate.

```text
actions for player i = its specified legal set
joint action = one legal choice for each acting player
payoff functions accept that joint action
```

The same formulas can use contributions anywhere in `[0, 2]`. That continuous variant needs suitable mathematical assumptions; a finite table no longer enumerates every possibility. Names such as "bid", "wait", or "send a message" can also label actions once their consequences are specified.

## Build this version

### Start from the previous version

Keep Level 6's supplied payoff rule and Level 5's separation of truth from reports. Remove assumptions that every legal action is C or D. The contribution example changes both the action domain and the supplied payoff function; it is not the original table with extra labels.

### Make the change

1. Store legal actions per player rather than in a shared C/D constant. For this finite example both sets are `{0, 1, 2}`. Validate a returned action against that player's set, including its expected kind of value.
2. Generalize distribution validation and sampling to iterate through the legal set. Use an explicit stable ordering instead of a two-way C/D branch.
3. Supply the contribution payoff function below. Enumerate all nine joint actions to check its domain before using it in a match.
4. Select identity execution for this example. Level 4's C/D flip has no meaning for three contribution quantities; reject it as incompatible rather than inventing a meaning for a flipped 2. Select controllers that return contributions too. Unmodified tit for tat returns C/D and is not a valid contribution controller.

```text
legal[Row] = {0, 1, 2}
legal[Column] = {0, 1, 2}
collect, validate, sample, and commit contributions x and y
executed = copy of intended contributions
benefit = 2 * (x + y)
payoffs = {Row: benefit - 3*x, Column: benefit - 3*y}
score and deliver under the existing information rules
```

Keep quantities as quantities throughout this path. Converting them back to C/D loses the distinction between contributions 1 and 2. A continuous action space would also need a different representation and validation strategy; this finite implementation does not already supply it.

### Check your implementation

- Submit `(2, 1)`. Expect shared benefit 6 and payoffs `(0, 3)`. Submit `(2, 2)` and expect `(2, 2)`; submit `(0, 0)` and expect `(0, 0)`. Enumerate all nine pairs and compare with the text table above.
- Hold y fixed and increase x by one within the legal set. Row's payoff falls by 1 and Column's rises by 2.
- Reject contribution 3, a C action, a distribution containing D, and a C/D-flip execution rule with this domain. Invalid inputs must not change totals or award payoffs.
- Restore `{C, D}`, compatible controllers and execution, and Level 6's chosen payoff function. The old two-action game should run without a separate match runner.

**Checkpoint:** What happens to Row's payoff if it increases x by one while y stays fixed?

**Concept added:** player-specific action spaces. Restoring `{C, D}` and the previous payoff functions recovers the previous level.

Sources: [general strategic-game definitions](/sources#foundations). Contribution formulas are our example.
