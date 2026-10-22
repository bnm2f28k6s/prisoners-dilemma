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

**Checkpoint:** If only the third player increases its contribution from 0 to 1 in the first example, what happens to all three payoffs?

**Concept added:** an indexed set of participants and a payoff vector of matching size. Select two players to recover the previous level. Entry and exit during play remain separate extensions.

Sources: [general strategic games](/sources#foundations).
