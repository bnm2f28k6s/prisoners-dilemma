---
title: "Level 8: more than two players"
---

# Level 8: more than two players

[Previous](/levels/07-actions) | [Walkthrough](/) | [Next: who acts when](/levels/09-timing)

## Change one constraint

**Remove:** the game has exactly two players. Let the participant set have any specified size.

**Keep:** a fixed roster, simultaneous decisions, player-specific action sets, and a payoff for each player. There is still one common interaction, rather than a rematching process.

## Walk through the new possibility

Extend the contribution example to three players. Each contributes `x_i` from `{0, 1, 2}`. Every player receives `2 * (sum of contributions)` and pays `3 * x_i`.

At `(2, 1, 0)`, the benefit to each is 6, so the payoff vector is `(0, 3, 6)`. At `(2, 2, 2)`, each receives 6 after paying its cost. One player's decision can now affect more than one other person.

[![A slice of the three-player contribution game with the third contribution fixed at zero. Row and Column still vary down and across the matrix. Payoffs now list Row, Column, third player; x=2, y=1 gives (0, 3, 6).](/diagrams/matrix-three-player-slice.svg)](/diagrams/matrix-three-player-slice.svg)

To preserve the familiar axes, this picture fixes the third player's contribution at 0 and shows one **slice**, not the whole game. Row and Column keep their positions and colors; each tuple appends the third player's payoff. Different third-player contributions require other slices.

| Row contribution x | Column y = 0 | Column y = 1 | Column y = 2 |
| --- | --- | --- | --- |
| 0 | (0, 0, 0) | (2, -1, 2) | (4, -2, 4) |
| 1 | (-1, 2, 2) | (1, 1, 4) | (3, 0, 6) |
| 2 | (-2, 4, 4) | (0, 3, 6) | (2, 2, 8) |

```text
joint action = {player: that player's action for every participant}
payoffs = {player: that player's payoff for every participant}
```

A two-dimensional square is no longer the general representation. Do not replace a genuinely group-dependent payoff with a sum of pairwise prisoner's dilemmas unless that is an explicit modeling assumption. Threshold public goods, for example, can depend on the entire group reaching a target.

## Build this version

### Start from the previous version

Keep Level 7's player-specific legal actions, distributions, and supplied payoff function. Replace the two fixed player slots in the runner with a roster of stable identities. For this example, use Row, Column, and Third with contribution actions and identity execution.

### Make the change

1. Initialize views, memories, totals, and legal-action sets by identity for every roster member. Treat the roster's display order separately from the keys used for accounting.
2. Collect one intended action per participant from pre-event information. Check that the joint-action keys match the roster exactly. A missing Third action is not an implicit zero.
3. Replace the two-input payoff calculation with a group sum. Return a map with exactly the same player keys. Compute each cost from that player's own executed contribution.
4. Generalize delivery and accounting loops as well as choice collection. A player contributing zero still receives the public benefit. Render a tuple only at the presentation boundary, using the declared order Row, Column, Third.

```text
require keys(executed) == roster
benefit = 2 * sum(executed[player] for player in roster)
for player in roster:
    payoffs[player] = benefit - 3 * executed[player]
require keys(payoffs) == roster
for player in roster:
    totals[player] = totals[player] + payoffs[player]
deliver only each player's permitted information
```

The two-dimensional diagram fixes Third's contribution at zero for display. Your resolver must accept all three inputs, not restrict Third to the displayed slice. There are 27 legal joint actions in this finite example.

### Check your implementation

- Submit `{Row: 2, Column: 1, Third: 0}`. Expect `{Row: 0, Column: 3, Third: 6}`. Increase only Third to 1 and expect `(2, 5, 5)` in display order. At `(2, 2, 2)`, expect `(6, 6, 6)`.
- Supply the same keyed choices in a different iteration order. Each identity must receive the same payoff. Reversing roster order must not exchange balances.
- Reject a missing Third action, an extra unknown player, or duplicate roster identities. Do not partially pay the first two players before discovering an invalid third action.
- Select only Row and Column and the same group-sum formula. Every legal contribution pair must reproduce Level 7, including `(2, 1) -> (0, 3)`.

**Checkpoint:** If only the third player increases its contribution from 0 to 1 in the first example, what happens to all three payoffs?

**Concept added:** an indexed set of participants and a payoff vector of matching size. Select two players to recover the previous level. Entry and exit during play remain separate extensions.

Sources: [general strategic games](/sources#foundations).
